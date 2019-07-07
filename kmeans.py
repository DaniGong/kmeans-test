import random,math
import numpy as np
import time
import copy
from matplotlib import pyplot as plt

class RandomDS(object):
    def __init__(self,count):
        self.min = 0
        self.max = 10
        self.file = "data_%d.txt" %int(time.time())
        self.count = count
        self.rand_data = list(self.data_iter())

    def output(self):
        with open(self.file,'a') as f:
            for x,y in self.rand_data:
                f.writelines("%f%s%f%s" %(x," ",y,"\n"))

    def data_iter(self):
        for i in range(self.count):
            yield (random.uniform(self.min,self.max),random.uniform(self.min,self.max))

    @property
    def data(self):
        return self.rand_data

    def __call__(self, new_min, new_max):
        self.min = new_min
        self.max = new_max

# def dist(a,b):
#     return math.sqrt(pow(a-b,2))
#

# for p in rds.data:
#     print(dist(p[0],p[1]))
class Cluster(object):
    def __init__(self,centroid):
        self.centroid = centroid
        self.points = []

    def add_point(self,point):
        self.points.append(point)

    def clear_points(self):
        self.points = []

class KMDataSet(object):
    def __init__(self,points,k):
        self.points = points
        self.clusters = []
        self.k = k
        self.cents = self.rand_cents()
        for cent in zip(self.cents[0],self.cents[1]):
            self.clusters.append(Cluster(cent))
        self.allocate()
        self.colors = ["orange","green","yellow","grey","black","blue"]

    def rand_cents(self):
        centlist_x,centlist_y = [],[]
        for i in range(self.k):
            centvalue = self.points.data[random.randint(0,len(self.points.data)-1)]
            if not centvalue[0] in centlist_x:
                centlist_x.append(centvalue[0])
                centlist_y.append(centvalue[1])
        return [centlist_x,centlist_y]

    def points_to_xy(self,points):
        x_list,y_list = [],[]
        for x,y in points:
            x_list.append(x)
            y_list.append(y)
        return [x_list,y_list]

    def update_cents(self):
        cent_x,cent_y = [],[]
        for cl in self.clusters:
            cl.centroid = (np.mean(self.points_to_xy(cl.points)[0]),np.mean(self.points_to_xy(cl.points)[1]))
            cent_x.append(cl.centroid[0])
            cent_y.append(cl.centroid[1])
        self.cents[0] = cent_x
        self.cents[1] = cent_y
        print(self.cents)

    def dist(self,point,centroid):
        return math.sqrt(pow(point[0]-centroid[0],2)+pow(point[1]-centroid[1],2))

    def allocate(self):
        for clust_to_be_cleared in self.clusters:
            clust_to_be_cleared.clear_points()
        for point in self.points.data:
            dists = []
            for clust in self.clusters:
                dists.append(self.dist(point,clust.centroid))
            self.clusters[dists.index(min(dists))].add_point(point)
        # for c in self.clusters:
        #     print(c.points)

    def is_eq(self,old_clusters,new_clusters):
        is_equal = True
        for old_c,new_c in zip(old_clusters,new_clusters):
            if set(old_c.points) != set(new_c.points):
                is_equal = False
        return is_equal

    def draw_points(self,figure_indx):
        plt.ion()
        plt.figure(num=figure_indx,figsize=(12, 8))
        plt.title("K-Means demo")
        color_indx = 0
        for cluster in self.clusters:
            xlist, ylist = ds.points_to_xy(cluster.points)
            plt.plot(xlist, ylist, "ob", color=self.colors[color_indx])
            color_indx += 1
        plt.plot(self.cents[0], self.cents[1], "+", color='tab:red')
        # plt.imshow(im_data)
        plt.pause(10)
        # plt.close()

    def clustering(self):
        clusterChanged = True
        figure_num = 1
        while clusterChanged:
            self.draw_points(figure_num)
            figure_num += 1
            old_clusters = copy.deepcopy(self.clusters)
            clusterChanged = False
            self.update_cents()
            self.allocate()
            if not self.is_eq(old_clusters,self.clusters):
                clusterChanged = True


rds = RandomDS(50)
# print(rds.data)
ds = KMDataSet(rds,5)

ds.clustering()
# while True:
# colors = ["orange","green","yellow","grey","black","blue"]
# plt.title("K-Means demo")
# color_indx = 0
# for cluster in ds.clusters:
#     xlist,ylist = ds.points_to_xy(cluster.points)
#     plt.plot(xlist, ylist, "ob",color=colors[color_indx])
#     color_indx += 1
# plt.plot(ds.cents[0],ds.cents[1],"+",color='tab:red')
# # plt.draw()
# plt.show()



# print(ds.rand_cents)

#






