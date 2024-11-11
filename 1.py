import gensim.downloader as api
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np

# Load the model
model = api.load("glove-wiki-gigaword-50")

# Select a subset of words for visualization
words = ['tower', 'building', 'height', 'city', 'architecture', 'skyline', 'structure', 'urban', 'office', 'apartment']
vectors = np.array([model[word] for word in words])

# Reduce dimensionality with t-SNE
tsne = TSNE(n_components=2, random_state=0, perplexity=5)
vectors_2d = tsne.fit_transform(vectors)

# Plotting
plt.figure(figsize=(12, 8))
plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], s=100, color='blue')

# Annotate points
for i, word in enumerate(words):
    plt.annotate(word, xy=(vectors_2d[i, 0], vectors_2d[i, 1]), fontsize=12)

plt.title("t-SNE visualization of GloVe embeddings")
plt.show()
