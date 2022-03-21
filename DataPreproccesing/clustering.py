import matplotlib.pyplot

from app_log.logger import app_log
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from kneed import KneeLocator
from file_methods.file_method import file_operations
from pylab import *


class Cluster:

    # def __init__(self):
    #     pass

    def elbow_plot(self,x,y):
        wcss = []
        try:
            for cluster in range(1,30):
                kmean = KMeans(n_clusters=cluster,init='k-means++',random_state=30)
                kmean.fit(x,y)
                wcss.append(kmean.inertia_)
            plt.plot(range(1,30),wcss)
            plt.show()
            knee = KneeLocator(x = range(1,30),y = wcss,curve='convex',direction="decreasing")
            print("KNe-------------------------------------eeeeeeeeeeeeeeeeeeeeee",knee,knee.knee)
            return knee.knee

        except Exception as e:
            print(e)

    def create_clusters(self,knee,x,y):
        try:
            kmean = KMeans(n_clusters=knee,init = 'k-means++',random_state=42)
            kmean.fit(x)
            # file_class = file_operations(self.model_path)
            file_operations.save_model(self,kmean,'KMean')

            x['Cluster'] = kmean.predict(x)
            # figure(10,10)
            # plot()
            # plot(kmean.predict(x),'b+')
            # matplotlib.pyplot.show()
            print("Clu---------------------------------ster",x.columns,x['Cluster'],x['Cluster'].value_counts())
        except Exception as e:
            print(e)

