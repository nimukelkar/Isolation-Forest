![isolation_forest](https://user-images.githubusercontent.com/60577980/140609005-b9220624-183e-43a5-b4a7-da37da361fed.png)
# Isolation-Forest
Anomaly Detection Machine Learning Algorithm

What is an anomaly?
In layman language an anomaly is anything that doesn't follow a particular trend and can be considered as an outlier to a given dataset.This is useful in credit card fraud detection, social media outlier event detection and so on.
![fish](https://user-images.githubusercontent.com/60577980/141651606-dcacd6c5-7ad2-4cb7-a9dd-196561105acd.png)
      
Why isolation forest?
       Most anomaly detection algorithms start from the cluster and then see which data point does not fit the trend and is labelled as the outlier.Isolation Forest directly starts from the outlier and does not go to the intermediate clusters.This is explained with the below example.
       ![Jeff_Bezoz](https://user-images.githubusercontent.com/60577980/141651838-93017d21-dc9a-4d5b-9146-14619751f185.png)

    The first deciding factor is the annual income of those people greater than 1 billion dollars.
    So Jeff Bezoz automatically becomes our outlier in the first comparison itself!!!
    
   ![Isolation_Forest (2)](https://user-images.githubusercontent.com/60577980/141651775-57a24791-8ef0-41c2-811e-5a7fe0b34658.png)
    
    The data structure used here is an Isolation Forest.We can say that in our isolation Forest Algorithm,
    the minimum depth can be associated with the outlier!.
This is the main concept behind  the Isolation Forest Algorithm.!
All outliers as seen above, have minimum depth.
           Same data point example (1,2) is applied to all the isolation trees.The average depth is calculated for all, and the minimum average depth of the isolation forest are associated with the outliers.This was performed on the iris dataset using the skicit library.The contamination factor decides the number of outliers.More the contamination factor, more the number of outliers.
           


