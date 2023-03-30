import numpy as np

# np.random.seed(42)

# x1 = [x1,y1] | x2 = [x2,y2]
def euclidean_distance(x1,x2):
	x1 = np.array(x1)
	x2 = np.array(x2)
	return np.sqrt(np.sum((x1-x2)**2))

class KMeans:

	def __init__(self, K=2, max_iters=100, plot_steps=False):
		self.K = K
		self.max_iters = max_iters
		self.plot_steps = plot_steps
		self.clusters = [[] for _ in range(0,self.K)]
		self.centroids = []

	def predict(self,X):
		self.X = np.array(X)
		self.n_samples, self.n_features = X.shape

		# initialization of centroids
		random_samples = np.random.choice(self.n_samples, self.K, replace = False)
		self.centroids = [self.X[_] for _ in random_samples]

		# optimization
		for _ in range(self.max_iters):
			# update clusters
			self.clusters = self.create_clusters(self.centroids)

			# update centroids
			old_centroids = self.centroids
			self.centroids = self.get_centroids(self.clusters)

			# check if converged
			if self.is_converged(old_centroids, self.centroids):
				break
		# return clusters
		return [self.X[i] for i in self.clusters]

	def create_clusters(self, centroids):
		# initialize clusters
		clusters = [[] for _ in range(self.K)]

		# group points into clusters
		for idx, sample in enumerate(self.X):
			centroid_idx = self.nearest_index(sample, self.centroids)
			print(f"{idx}->{centroid_idx}")
			clusters[centroid_idx].append(idx)
		return clusters

	def nearest_index(self, point, centroids):
		distances = [euclidean_distance(point, x) for x in (centroids)]
		# getting the closest index
		return np.argmin(distances)

	def get_centroids(self, clusters):
		centroids = np.zeros((self.K, self.n_features))
		for cluster_idx, cluster in enumerate(clusters):
			centroids[cluster_idx] = np.mean(self.X[cluster], axis=0)

		return centroids

	def is_converged(self, centroids_old, centroids_new):
		distances = [euclidean_distance(centroids_old[i], centroids_new[i]) for i in range(self.K)]
		return sum(distances) == 0


b = [[1,2],[1,4],[3,2],[5,2],[8,9],[10,10]]
print(f"Data is: {b}")
k = KMeans(K=3, max_iters=100)
pred = k.predict(np.array(b))
print(f"Clusters are:\n{pred}")