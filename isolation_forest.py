import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import genfromtxt
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
sns.set_style("darkgrid")

X = genfromtxt('Iris.csv',delimiter=',',skip_header=1,usecols=(1,2,3,4))


# n_estimators is number of trees in the forest
# max_samples is number of samples to be drawn to train each base estimator  (si)
# contamination - estimated number of outliers in the data
# max_features - Number of features drawn from total number of features to train


iforest = IsolationForest(n_estimators=100, max_samples='auto',
                          contamination=0.01, max_features=1.0,
                          bootstrap=False, n_jobs=-1, random_state=1)

# WE have average depth of each data point. This converted to anomaly score [0,1]
# Returns 1 of inliers, -1 for outliers
pred = iforest.fit_predict(X)

print(type(pred))
print(pred)

# outlier_index is a 1D array that gives the index value(0-150) of the outlier record(full row).
outlier_index = np.where(pred==-1)
print(outlier_index)
outlier_values = X[outlier_index]
print(outlier_values)

# Feature scaling
sc=StandardScaler()
X_scaled = sc.fit_transform(X)
outlier_values_scaled = sc.transform(outlier_values)

# Apply PCA to reduce the dimensionality
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
outlier_values_pca = pca.transform(outlier_values_scaled)

# Plot the data
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1])
plt.title("Isolation Forest - All data",
           fontsize=15, pad=15)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.savefig("Isolation Forest Detection.png", dpi=80)
plt.show()


sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1])
sns.scatterplot(x=outlier_values_pca[:,0],
                y=outlier_values_pca[:,1], color='r' )
plt.title("Isolation Forest - anomalies in red",
           fontsize=15, pad=15)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.savefig("Isolation Forest Detection.png", dpi=80)
plt.show()