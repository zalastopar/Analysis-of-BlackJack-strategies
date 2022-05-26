library(readr)
library("ggplot2")

paroli_bet <- read_csv("data/paroli-bet.csv")[,-1]
paroli_balance <- read_csv("data/paroli-balance.csv")[,-1]
paroli <- read_csv("data/paroli.csv")
#X1326_balance <- read_csv("data/1326-balance.csv")

ggp <- ggplot(paroli_balance, aes(x, y, col = group)) +             # Create ggplot2 plot
  geom_line()