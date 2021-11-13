![isolation_forest](https://user-images.githubusercontent.com/60577980/140609005-b9220624-183e-43a5-b4a7-da37da361fed.png)
# Isolation-Forest
Anomaly Detection Machine Learning Algorithm

What is an anomaly?
In layman language an anomaly is anything that doesn't follow a particular trend and can be considered as an outlier to a given dataset.This is useful in credit card fraud detection, social media outlier event detection and so on.
![fish](https://user-images.githubusercontent.com/60577980/141651606-dcacd6c5-7ad2-4cb7-a9dd-196561105acd.png)

        
Why isolation forest?
       Most anomaly dteection algorithms start from the cluster and then see which data point does not fit the trend and is labelled as the outlier.Isolation Forest directly starts from the outlier and does not go to the intermediate clusters.This is explained with the below example.
       
       

    The first deciding factor is the annual income of those people greater than 1 billion dollars.So Jeff Bezoz automatically becomes our outlier in the first comparison itself!!!.
    The data structure used here is an Isolation Forest.We can say that in our isolation Forest Algorithm, the minimum depth can be associated with the outlier!.
This is the main concept behind  the Isolation Forest Algorithm.!

All outliers as seen above, have minimum depth.


