library(readr)
library("ggplot2")
for (el in c('paroli', '1326', 'counting', 'increase', 'martingale', 'oscar')) {
  assign(paste(el, '_bet', sep = ''), data.frame(read_csv(paste("data/", el, "-bet.csv", sep = ''))[,-1]))
  assign(paste(el, '_balance', sep = ''), data.frame(read_csv(paste("data/", el, "-balance.csv", sep = ''))[,-1]))
  assign(el, data.frame(read_csv(paste("data/", el, ".csv", sep = ''))[,-1]))
  
  eval(parse(text = el))[is.na(eval(parse(text = el)))] <-0
  eval(parse(text = paste(el, '_balance', sep = '')))[is.na(eval(parse(text = paste(el, '_balance', sep = ''))))] <-0
  eval(parse(text = paste(el, '_bet', sep = '')))[is.na(eval(parse(text = paste(el, '_bet', sep = ''))))] <-0
}


# isto se za balance
avg_balance <- c()
for (i in 1:100){
  avg_balance <- c(avg_balance, mean(as.numeric(paroli_balance[i,])))
}

plot(paroli_balance[,1], type = 'l', col='#ffc0cb80')
for (i in 1:500){
  lines(paroli_balance[,i], type = 'l', col='#ffc0cb80')
}
lines(avg_balance, type = 'l', col = 'deeppink3')



# data 0x, 3x, 5x, 10x - brez 0
avg_data_0_paroli <- data.frame(colSums(paroli)/colSums(!!paroli), c('0x', '3x', '5x', '10x'))
avg_data_0_paroli[is.na(avg_data_0_paroli)] = 0
colnames(avg_data_0_paroli) <- c('a', 'b')
plot_avg_data_0_paroli <- ggplot(avg_data_0_paroli, aes(x=b, y = a)) + geom_histogram(stat = "identity", fill = 'deeppink3') + 
  scale_x_discrete(limits=avg_data_0_paroli$b) + theme_classic() + 
  labs(x = 'Balance value', y = 'Average number of dealings', title = 'Average number of dealings to get to the multiple of balance', 
       subtitle = 'Paroli system')
plot_avg_data_0_paroli



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
       subtitle = 'Paroli system') + ylim(0, 1) + 
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



## lab

