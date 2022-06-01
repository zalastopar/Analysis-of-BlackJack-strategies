setwd("~/AMAT/Analysis-of-BlackJack-strategies")
library(readr)
library("ggplot2")
library(dplyr)


#############################################################################################################################
# Import 
#############################################################################################################################

na_to_0 <- function(tab) {
 tab[is.na(tab)] <- 0
 return(tab)
}

for (el in c('paroli', '1326', 'increase', 'counting', 'martingale', 'oscar'))  {
 assign(paste(el, '_bet', sep = ''), na_to_0(data.frame(read_csv(paste("data/", el, "-bet.csv", sep = ''))[,-1])))
 assign(paste(el, '_balance', sep = ''), na_to_0(data.frame(read_csv(paste("data/", el, "-balance.csv", sep = ''))[,-1])))
 assign(el, na_to_0(data.frame(read.csv(paste("data/", el, ".csv", sep = ''))[,-1])))
}

#############################################################################################################################
# Osnovni grafi
#############################################################################################################################
for (el in c('paroli', '1326', 'increase', 'counting', 'martingale', 'oscar'))
 {
# isto se za balance
tab <- get(paste(el, '_balance', sep = ''))
avg_balance <- c()
for (i in 1:100){
  avg_balance <- c(avg_balance, mean(as.numeric(tab[i,])))
}
png(paste("reports/analysis/", el, '-balance.png', sep = ''), height =600 , width = 700)
plot(tab[,1], type = 'l', col=rgb(red=1, green=0.6, blue=0.5, alpha=0.4), xlab = 'Dealing', ylab = 'Balance', main = paste('Balance after each dealing \n', el, sep = ''),
     ylim = c(0, 1800))
for (i in 1:500){
  lines(tab[,i], type = 'l', col=rgb(red=1, green=0.6, blue=0.5, alpha=0.4))
}
lines(avg_balance, type = 'l', col = 'hotpink', lwd = 3)
dev.off()

tab2 <- get(el)

 # data 0x, 3x, 5x, 10x - brez 0 ##########################################################################################
 avg_data_0 <- data.frame(colSums(tab2)/colSums(!!tab2), c('0x', '3x', '5x', '10x'))
 colnames(avg_data_0) <- c('a', 'b')
 plot_avg_data_0 <- ggplot(avg_data_0, aes(x=b, y = a)) + geom_col(fill = 'deeppink3') +
  scale_x_discrete(limits=avg_data_0$b) + theme_classic() +
  labs(x = 'Balance value', y = 'Average number of dealings', title = 'Average number of dealings to get to the multiple of balance',
       subtitle = el)
 
 png(paste("reports/analysis/", el, '-hist.png', sep = ''), height =600 , width = 700)
 print(plot_avg_data_0)
 dev.off()
 
 # data 0x ###############################################################################################################
 avg_data_0 <- data.frame(colSums(tab2)/colSums(!!tab2), c('0x', '3x', '5x', '10x'))
 plot_data_0 <- ggplot(tab2, aes(x=c(1:500), y = data_0x)) + geom_col(fill = 'palevioletred2') + theme_classic() +
  labs(x = 'Game', y = 'Number of dealings', title = 'Number of dealings in each game to get to 0 balance',
       subtitle = el) +
  geom_hline(yintercept=avg_data_0[1,1], color = 'deeppink', size = 1, linetype="dashed")
 png(paste("reports/analysis/", el, '-data_0.png', sep = ''), height =600 , width = 700)
 print(plot_data_0)
 dev.off()
 # data 3x #############################################################################################################
 plot_data_3 <- ggplot(tab2, aes(x=c(1:500), y = data_3x)) + geom_col(fill = 'plum3') + theme_classic() +
  labs(x = 'Game', y = 'Number of dealings', title = 'Number of dealings in each game to get to 3x balance',
       subtitle = el) +
  geom_hline(yintercept=avg_data_0[2,1], color = 'mediumorchid4', size = 1, linetype="dashed")
 png(paste("reports/analysis/", el, '-data_3.png', sep = ''), height =600 , width = 700)
 print(plot_data_3)
 dev.off()
 # data 5x ##############################################################################################################
 plot_data_5 <- ggplot(tab2, aes(x=c(1:500), y = data_5x)) + geom_col(fill = 'rosybrown3') + theme_classic() +
  labs(x = 'Game', y = 'Number of dealings', title = 'Number of dealings in each game to get to 5x balance',
       subtitle = el) +
  geom_hline(yintercept=avg_data_0[3,1], color = 'wheat4', size = 1, linetype="dashed")
 png(paste("reports/analysis/", el, '-data_5.png', sep = ''), height =600 , width = 700)
 print(plot_data_5)
 dev.off()
 # data 10x ###############################################################################################################
 plot_data_10 <- ggplot(tab2, aes(x=c(1:500), y = data_10x)) + geom_col(fill = 'khaki2') + theme_classic() +
  labs(x = 'Game', y = 'Number of dealings', title = 'Number of dealings in each game to get to 10x balance',
       subtitle = el) + ylim(0, 1) +
  geom_hline(yintercept=avg_data_0[4,1], color = 'tan2', size = 1, linetype="dashed")
 png(paste("reports/analysis/", el, '-data_10.png', sep = ''), height =600 , width = 700)
 print(plot_data_10)
 dev.off()
}

#############################################################################################################################
# average bet -combine strategies
#############################################################################################################################

avg_bet <- c()
for (i in 1:100){
avg_bet <- c(avg_bet, mean(as.numeric(paroli_bet[i,])))
}

png('reports/analysis/average-bet.png', height =600 , width = 700)
plot(avg_bet, type = 'l', col = 'hotpink', ylim = c(0,25), lwd =2, ylab = 'Average bet', xlab = 'Dealing',
   main = 'Average bet per dealing')
colors <- c('deepskyblue', 'firebrick1', 'mediumorchid1', 'springgreen', 'gold')
legend(75, 25, legend = c('paroli','1326', 'counting', 'increase', 'martingale', 'oscar'),
     col = c('hotpink', colors), lty = 1, lwd = 2)
for (el in c('1326', 'counting', 'increase', 'martingale', 'oscar')){
avg_bet <- c()
tab <- get(paste(el, '_bet', sep = ''))
for (i in 1:100){
  avg_bet <- c(avg_bet, mean(as.numeric(tab[i,])))
}
lines(avg_bet, type = 'l', col = colors[1], lwd = 2)
colors <- colors[-1]
}
dev.off()



 #############################################################################################################################
 # average balance - combine strategies
 ##############################################################################################################################

 avg_balance <- c()
 for (i in 1:100){
   avg_balance <- c(avg_balance, mean(as.numeric(paroli_balance[i,])))
 }
 png('reports/analysis/average-balance.png', height =600 , width = 700)

 plot(avg_balance, type = 'l', col = 'hotpink', lwd =2, ylab = 'Average balance', xlab = 'Dealing',
      main = 'Average balance per dealing', ylim = c(70, 110))
 colors <- c('deepskyblue', 'firebrick1', 'mediumorchid1', 'springgreen', 'gold')
 legend(0, 85, legend = c('paroli','1326', 'counting', 'increase', 'martingale', 'oscar'),
        col = c('hotpink', colors), lty = 1, lwd = 2)
 for (el in c('1326', 'counting', 'increase', 'martingale', 'oscar')){
   avg_balance <- c()
   tab <- get(paste(el, '_balance', sep = ''))
   for (i in 1:100){
     avg_balance <- c(avg_balance, mean(as.numeric(tab[i,])))
   }
   lines(avg_balance, type = 'l', col = colors[1], lwd = 2)
   colors <- colors[-1]
 }
 dev.off()


#############################################################################################################################
# Average balance at the end
#############################################################################################################################

 avg_balance <- c()
 for (el in c('paroli', '1326', 'counting', 'increase', 'martingale', 'oscar')){
   
  tab <- get(paste(el, '_balance', sep = ''))
  avg_balance <- c(avg_balance, mean(as.numeric(tab[100,])))
 }

 p <- ggplot(data.frame(avg_balance), aes(x=c('paroli', '1326', 'counting', 'increase', 'martingale', 'oscar'), y = avg_balance)) + 
   geom_col(fill = 'violetred1') + theme_classic() +
  labs(x = 'Strategy', y = 'Balance', title = 'Average balance after 100 dealings')
 
 png('reports/analysis/avg_balance-end.png', height =600 , width = 700)
 print(p)
 dev.off()





#############################################################################################################################
 PROBABILITY # stolpci so player
#############################################################################################################################
calculate_prob <- function(el) {
     if (is.na(el)){
       el <- 0
     } else if (nchar(el) == 1 | nchar(el) == 2){
       el <- el
     } else {      
       b <- list(strsplit(substring(el, 2, nchar(el)-1), ','))
       prva <- as.numeric(b[[1]][[1]][1])
       druga <- as.numeric(b[[1]][[1]][2])
       prob <- round(prva/druga, 2)
       el <- prob
     }
 return(el)
   }

heat_table <- function(tab){
 value <- c()
 row_n <- c()
 col_n <- c()
 move <- c()
 for (i in 1:nrow(tab)){
     for (j in 1:ncol(tab)){
       c <- as.numeric(substring(colnames(tab)[j],2))
       r <- as.numeric(rownames(tab)[i])
       prob <- calculate_prob(tab[i,j])
       
       value <- c(value, prob)
       row_n <- c(row_n, r)
       col_n <- c(col_n, c)
   }
 }

 tabela <- data.frame(row_n, col_n, value)
 return(tabela)
}


#############################################################################################################################
# HEATMAPS
#############################################################################################################################
# SOFT DATA #################################################################################################################

soft_data <- data.frame(read_csv("data/soft_data.csv"))
rownames(soft_data) <- soft_data[,1]
soft_data <- soft_data[,2:10]
# moves
soft_data_moves <- data.frame(read_csv("data/soft_data_moves.csv"))
rownames(soft_data_moves) <- soft_data_moves[,1]
soft_data_moves <- soft_data_moves[,-1]

m <- merge(heat_table(soft_data_moves), heat_table(soft_data), by =c('row_n', 'col_n'))
p <- ggplot(m, aes(x = col_n, y = row_n, fill = value.y)) + geom_tile(color = "white", lwd = 1.5, linetype = 1) + coord_fixed() + 
 labs(x = 'Players second card', y = 'Dealers card', title = 'Simulated probability of winning by playing by \n strategy with soft hand', fill = 'Probability') +
 scale_fill_gradient2(low = "#075AFF", mid = "#FFFFCC", high = "deeppink") + geom_text(aes(label = value.x), color = "gray33", size = 5, lwd = 10) +
 scale_x_discrete(limits = m$col_n) + scale_y_discrete(limits = m$row_n)

png('reports/analysis/soft_data.png', height =600 , width = 700)
print(p)
dev.off()

# SPLIT DATA ################################################################################################################

split_data <- data.frame(read_csv("data/split_data.csv"))
rownames(split_data) <- split_data[,1]
split_data <- split_data[,-1]
# moves
split_data_moves <- data.frame(read_csv("data/split_data_moves.csv"))
rownames(split_data_moves) <- split_data_moves[,1]
split_data_moves <- split_data_moves[,-1]

m <- merge(heat_table(split_data_moves), heat_table(split_data), by =c('row_n', 'col_n'))
p <- ggplot(m, aes(x = col_n, y = row_n, fill = value.y)) + geom_tile(color = "white", lwd = 1.5, linetype = 1) + coord_fixed() + 
 labs(x = 'Players cards (both are the same', y = 'Dealers card', title = 'Simulated probability of winning by playing by \n strategy with split hand', fill = 'Probability') +
 scale_fill_gradient2(low = "#075AFF", mid = "#FFFFCC", high = "deeppink") + geom_text(aes(label = value.x), color = "gray33", size = 5) +
 scale_x_discrete(limits = m$col_n) + scale_y_discrete(limits = m$row_n)

png('reports/analysis/split_data.png', height =600 , width = 700)
print(p)
dev.off()

# PROB DATA ###################################################################################################################


prob_data <- data.frame(read_csv("data/prob_data.csv"))
rownames(prob_data) <- prob_data[,1]
prob_data <- prob_data[-1]

prob_data_moves <- data.frame(read_csv("data/prob_data_moves.csv"))
rownames(prob_data_moves) <- prob_data_moves[,1]
prob_data_moves <- prob_data_moves[,-1]

# add columns prob data
row_n <- c()
col_n <- c()
value <- c()
for (i in (2:11)){
 for (j in (2:8)){
   row_n <- c(row_n, i)
   col_n <- c(col_n, j)
   value <- c(value, 'H')
 }
}
col_n
row_n
for (i in (2:11)){
 for (j in (18:21)){
   row_n <- c(row_n, i)
   col_n <- c(col_n, j)
   value <- c(value, 'S')
 }
}

moves1 <- data.frame(row_n, col_n, value)
moves2 <- rbind(moves1, heat_table(prob_data_moves))
m <- merge(moves2, heat_table(prob_data), by =c('row_n', 'col_n'))
p <- ggplot(m, aes(x = col_n, y = row_n, fill = value.y)) + geom_tile(color = "white", lwd = 1.5, linetype = 1) + coord_fixed() + 
 labs(x = 'Players hand value', y = 'Dealers card', title = 'Simulated probability of winning by playing by \n strategy with normal hand', fill = 'Probability') +
 scale_fill_gradient2(low = "#075AFF", mid = "#FFFFCC", high = "deeppink") + geom_text(aes(label = value.x), color = "gray33", size = 5) +
 scale_x_discrete(limits = m$col_n) + scale_y_discrete(limits = m$row_n)

png('reports/analysis/prob_data.png', height =600 , width = 700)
print(p)
dev.off()
