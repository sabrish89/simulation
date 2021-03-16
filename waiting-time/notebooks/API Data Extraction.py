import requests
import zipfile

url = "https://ltafarecard.s3.amazonaws.com/201808/transport_node_bus_201808.zip?x-amz-security-token=FQoGZXIvYXdzEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDODUUEVnEPaOB27jPiKmA4mHPaCaf08cv79Gy7swCeBvuc%2FkIpjiyTtwyq1thuhJTx%2Bx4dj4LDZombPNBHt%2F4nLz4SVt55JoG9pxNmExoU9zptzSS%2BzX830mgEBpP7DeA1CdkMMTpydAEmsOMzo7oR5IwKpYrkgsAdZsgUGKdAekty%2FNvYRKb0y%2FUJg5TZu2Ehew6T8glOZyfo8vCQDFiGlxiVMTgz18LzvUyixEjIDI4i3Eiy0kTW3Y4beLzS27G58X7HBbTHSRCi%2FdhhfHLyk52YduRx%2FkFTepaS1rjUJnrJHMnFb0sP7CfJDXz5aZ6rvCRs7664T68S11yt5gvbE3UizSZD5GVA1%2FgAix5442YgBUSnytym9LTPtlKdIX0dd5yYmpXn5sdzz6PmRikpjQ0cpmsM1Pi%2Bosm0pQdJAk3Er77JngP9PHdwX9wwasUNi5Cx0MtNRpeUxSqxT8ziAo%2BaU8BJTzKBTBGd%2BkOA9catz9yDiExEwLoTVmxshNcyLMlFdo4rAydU3shCpGEqTSfEM0I7dVyV8OY4hZ2AsDgB90s39vVDacc6uM8ZToh%2BbGtPpsKLqNmN0F&AWSAccessKeyId=ASIAU6UAMAS4JMDPRGWG&Expires=1537609454&Signature=l6uUjUznJCplR53PCOLuKL%2FqKlk%3D"

target_path = 'H:\Service Analytics\API\lta.zip'

response = requests.get(url, stream=True)
handle = open(target_path, "wb")
for chunk in response.iter_content(chunk_size=512):
    if chunk:  # filter out keep-alive new chunks
        handle.write(chunk)
handle.close()