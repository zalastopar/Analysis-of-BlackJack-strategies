library(readr)
library("ggplot2")

paroli_bet <- data.frame(read_csv("data/paroli-bet.csv")[,-1])
paroli_balance <- data.frame(read_csv("data/paroli-balance.csv")[,-1])
paroli <- data.frame(read_csv("data/paroli.csv")[,-1])
paroli[is.na(paroli)] <-0
paroli_balance[is.na(paroli_balance)] <-0
paroli_bet[is.na(paroli_bet)] <-0
#X1326_balance <- read_csv("data/1326-balance.csv")


plot(paroli_bet[,1], type = 'l')
for (i in 2:50){
  lines(paroli_bet[,i], type = 'l')
}

# data 0x, 3x, 5x, 10x
avg_data <- data.frame(colMeans(paroli[sapply(paroli, is.numeric)]), c('0x', '3x', '5x', '10x'))
colnames(avg_data) <- c('a', 'b')
plot_avg_data <- ggplot(avg_data, aes(x=b, y = a)) + geom_histogram(stat = "identity", fill = 'deeppink3') + 
  scale_x_discrete(limits=avg_data$b) + theme_classic() + 
  labs(x = 'Balance value', y = 'Average number of dealings', title = 'Average number of dealings to get to the multiple of balance', 
       subtitle = 'Paroli system')
plot_avg_data

# data 0x
plot_data_0 <- ggplot(paroli, aes(x=c(1:500), y = data_0x)) + geom_histogram(stat = "identity", fill = 'palevioletred2') + theme_classic() + 
  labs(x = 'Game', y = 'Number of dealings', title = 'Number of dealings in each game to get to 0 balance', 
       subtitle = 'Paroli system') + 
  geom_hline(yintercept=avg_data[1,1], color = 'deeppink', size = 1, linetype="dashed")
plot_data_0

# data 3x
plot_data_3 <- ggplot(paroli, aes(x=c(1:500), y = data_3x)) + geom_histogram(stat = "identity", fill = 'plum3') + theme_classic() + 
  labs(x = 'Game', y = 'Number of dealings', title = 'Number of dealings in each game to get to 3x balance', 
       subtitle = 'Paroli system') + 
  geom_hline(yintercept=avg_data[2,1], color = 'mediumorchid4', size = 1, linetype="dashed")
plot_data_3

# data 5x
plot_data_5 <- ggplot(paroli, aes(x=c(1:500), y = data_5x)) + geom_histogram(stat = "identity", fill = 'rosybrown3') + theme_classic() + 
  labs(x = 'Game', y = 'Number of dealings', title = 'Number of dealings in each game to get to 5x balance', 
       subtitle = 'Paroli system') + 
  geom_hline(yintercept=avg_data[3,1], color = 'wheat4', size = 1, linetype="dashed")
plot_data_5

# data 10x
plot_data_10 <- ggplot(paroli, aes(x=c(1:500), y = data_10x)) + geom_histogram(stat = "identity", fill = 'khaki2') + theme_classic() + 
  labs(x = 'Game', y = 'Number of dealings', title = 'Number of dealings in each game to get to 10x balance', 
       subtitle = 'Paroli system') + 
  geom_hline(yintercept=avg_data[4,1], color = 'tan2', size = 1, linetype="dashed")
plot_data_10






# average bet # mogoce damo na en graf za use strategije
avg_bet <- c()
for (i in 1:100){
  avg_bet <- c(avg_bet, mean(as.numeric(paroli_bet[i,])))
}
plot(avg_bet, type = 'l')


# isto se za balance
avg_balance <- c()
for (i in 1:100){
  avg_balance <- c(avg_balance, mean(as.numeric(paroli_balance[i,])))
}
plot(avg_balance, type = 'l')




