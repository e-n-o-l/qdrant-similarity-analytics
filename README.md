# Qdrant Vector Similarity & Latent Space Analytics

An analytical toolkit and diagnostic module designed to evaluate vector space distribution, measure cluster variance, and compute retrieval performance metrics for Qdrant vector embeddings.

### Key Features & Technical Highlights
* **Dimensionality Reduction & Latent Space Visualization:** Uses **UMAP** (Uniform Manifold Approximation and Projection) to project high-dimensional multi-image embeddings into 2D visual map.
* **Intra-Listing Cluster Diagnostics:** Identifies key vector spatial properties, proving that multi-image embeddings derived from a single listing span broad, distinct clusters (e.g., close-up wheel shots vs. cabin interior vs. full body exteriors) rather than collapsing into single point clusters.
* **Retrieval Metric Suite:** Calculates standard retrieval metrics over Qdrant collections using `torchmetrics.retrieval`, including **Recall@K**, **Precision@K**, **MRR (Mean Reciprocal Rank)**, **MAP**, and **nDCG**.
