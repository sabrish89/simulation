library(pacman)
p_load(readxl)

data_demand<-read_xlsx("~/Bus_255_Weekday.xlsx")

data_demand$DAY_TYPE<-as.factor(data_demand$DAY_TYPE)
data_demand$TIME_PER_HOUR<-as.factor(data_demand$TIME_PER_HOUR)
data_demand$PT_TYPE<-as.factor(data_demand$PT_TYPE)
data_demand$PT_CODE<-as.factor(data_demand$PT_CODE)

p_load(MASS)

neg_bin_reg<-glm.nb(TOTAL_TAP_IN_VOLUME~.,data = data_demand[,c(2,3,5,6,7)])

summary(neg_bin_reg)

predictions<-round(neg_bin_reg$fitted.values)

View(predictions)

write.csv(predictions,"~/Predictions.csv")
