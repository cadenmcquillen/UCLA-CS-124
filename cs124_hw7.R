library(dplyr)
setwd("/Users/Caden/Downloads")

#######Question 3 part A###################
methylation_data = read.delim("mlgenetics_hw7_TRAIN.txt",header = FALSE)
res.pca <- prcomp(methylation_data, scale = TRUE)
summ <- summary(res.pca)
variance = summ$importance[2,]
variance_ten = variance[1:10]
q1 = sum(variance_ten)


#######Question 3 part B###################
res.ind <- get_pca_ind(res.pca)
scores = res.ind$contrib
scores_ten = scores[,1:10]

batch_vec = read.delim("mlgenetics_hw7_TRAIN_batch.txt", header = FALSE)
highest_score = 0
highest_corr = 0
counter = 0
for (i in 1:10){
  temp = scores_ten[,i]

  corr = cor(temp,batch_vec$V1)
  corr2 = corr^2
  print(corr2)
  counter = counter + 1
  if (counter == 1){
    highest_score = counter
    highest_corr = corr2
  }
  else if(corr2 > highest_corr){
    highest_score = counter
    highest_corr = corr2
  }


}


#######Question 3 part C###################
loadings = data.table::as.data.table(res.pca$rotation)
PC4_loadings = loadings[,4]
PC4_loadings = abs(PC4_loadings)

library(tibble)
PC4_loadings <- tibble::rownames_to_column(PC4_loadings, "Position")
top1000 <- PC4_loadings  %>% top_n(1000)

subset_pos = as.vector(as.numeric(top1000$Position))

subset_methylation = methylation_data[,subset_pos]
subset_PCA = prcomp(subset_methylation, scale = TRUE)

subset_PCA.ind <- get_pca_ind(subset_PCA)
subset_scores = subset_PCA.ind$contrib
subset_scores_ten = subset_scores[,1:10]
#

sub_highest_score = 0
sub_highest_corr = 0
sub_counter = 0
for (i in 1:10){
  temp = subset_scores_ten[,i]

  sub_corr = cor(temp,batch_vec$V1)
  sub_corr2 = sub_corr^2
  print(sub_corr2)
  sub_counter = sub_counter + 1
  if (sub_counter == 1){
    sub_highest_score = sub_counter
    sub_highest_corr = sub_corr2
  }
  else if(sub_corr2 > sub_highest_corr){
    sub_highest_score = sub_counter
    sub_highest_corr = sub_corr2
  }


}

#########Question 3 part D##################

for_regression1 = cbind(batch_vec,scores_ten)
names(for_regression1)[1] <- 'Batch'
pc1_model = glm(Batch~Dim.1,data = for_regression1)
pc2_model = glm(Batch~Dim.2,data = for_regression1)
pc3_model = glm(Batch~Dim.3,data = for_regression1)
pc4_model = glm(Batch~Dim.4,data = for_regression1)
pc5_model = glm(Batch~Dim.5,data = for_regression1)


                               