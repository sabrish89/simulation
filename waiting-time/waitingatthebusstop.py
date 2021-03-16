import simpy
import random

RANDOM_SEED = 42
NEW_CUSTOMERS = 9999999
INTERVAL_CUSTOMERS = 2.0
MIN_PATIENCE = 5
MAX_PATIENCE = 15


def source_on_demand(env, number, interval, counter):
    """Source generates commuters randomly"""
    for i in range(number):
        bus_arrival = random.uniform(5, 15)
        c = customer(env, 'Customer_%02d' % (i + 1), counter, time_in_stop=bus_arrival)
        env.process(c)
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)


def customer(env, name, counter, time_in_stop):
    """Commuter arrives at stop, waits for bus and is served or leaves."""
    arrive = env.now
    print('%7.4f %s: Arrives at Bus Stop' % (arrive, name))

    with counter.request() as req:
        patience = random.uniform(MIN_PATIENCE, MAX_PATIENCE)
        # Wait for the bus or abort at the end of our tether
        results = yield req | env.timeout(patience)

        wait = env.now - arrive

        if req in results:
            if time_in_stop == 12.0:
                tib = random.expovariate(1.0 / time_in_stop)
            else:
                tib = service_bound_exponential(1.0 / time_in_stop)
            yield env.timeout(tib)
            print('%7.4f %s: Boards Bus after waiting for %6.3f' % (env.now, name, tib))
        else:
            print('%7.4f %s: RENEGED(I am taking a Grab!!!)/Lost after %6.3f' % (env.now, name, wait))


def source_deterministic(env, number, interval, counter):
    """Source generates commuters randomly"""
    for i in range(number):
        bus_arrival = 12.0  # deterministic - fixed frequency
        c = customer(env, 'Customer_%02d' % (i + 1), counter, time_in_stop=bus_arrival)
        env.process(c)
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)


def service_bound_exponential(alpha):
    gen = random.expovariate(alpha)
    while gen > 15:
        gen = random.expovariate(alpha)
    return gen

if __name__ == '__main__':
    # Setup and start the simulation
    print('Bus Stop Simulation - On Demand')
    # random.seed(RANDOM_SEED)
    env = simpy.Environment()

    # Start processes and run
    counter = simpy.Resource(env, capacity=3)
    env.process(source_on_demand(env, NEW_CUSTOMERS, INTERVAL_CUSTOMERS, counter))
    env.run(until=30)