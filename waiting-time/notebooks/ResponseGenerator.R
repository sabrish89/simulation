install.packages("xlsx")
library(xlsx)

y = rbinom(1000,5,0.7)
mean(y)

write.xlsx(y, file = "CSS3.xlsx")



   
