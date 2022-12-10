
# Please use gensim==3.8.3

# This is the python code using node2vec to select most distince subgraphs from different graphs.
# Example to use it:
# subgraph_size = 20 # Select 20 nodes from the original graph
# result = get_embedding()
# get_subgraph(20, result["node_embeddings"], result["node_ids"])

import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from node2vec import Node2Vec as n2v

def get_embedding(dimension=20, walk_length=16, num_walks=100, window=10, min_count=1, batch_words=4):
  function_words = open("dataset/functionwords_list.txt", "r")
  words = function_words.read()
  words = words.replace("\n", "")
  words2list = words.split(" ")
  cols = len(words2list)
  function_words.close()
  word_dict = dict(list(enumerate(words2list)))
  book_list = ["austen_2", "austen_4", "dickens_1", "dickens_4", "shakespeare_1", "shakespeare_5", "twain_1", "twain_4"]
  adj = {}
  G = {}
  for book in book_list:
    adj[book] = np.loadtxt('dataset/'+book+'.txt', usecols = range(cols))
    G[book] = nx.from_numpy_matrix(adj[book], create_using=nx.DiGraph)
    G[book] = nx.relabel_nodes(G[book], word_dict)

  # Remove all isolated nodes
  isolate_words = set()
  for book in book_list:
    isolate_words = isolate_words.union(set(nx.isolates(G[book])))
  for book in book_list:
    G[book].remove_nodes_from(list(isolate_words))

  node_embeddings = {}
  node_embeddings_2d = {}
  #data_tsne = {}

  # Fit node2vec models 
  for book in book_list:
    g_emb = n2v(
      G[book],
      dimensions=dimension,
      walk_length=walk_length, 
      num_walks=num_walks
    )

    model = g_emb.fit(
      window=window,
      min_count=min_count,
      batch_words=batch_words
    )

      
    node_embeddings[book] = (model.wv.vectors) 

    # If you want to visualize the node embedding, you can use the following code to get a 2d dimension reduction
    """
    trans = TSNE(n_components = 2, early_exaggeration = 10,
                    perplexity = 35, n_iter = 1000, n_iter_without_progress = 500,
                    learning_rate = 600.0, random_state = 42)
    node_embeddings_2d[book] = trans.fit_transform(node_embeddings[book])
    data_tsne[book] = pd.DataFrame(zip(node_ids[book], list(node_embeddings_2d[book][:,0]),list(node_embeddings_2d[book][:,1])),
                          columns = ['node_ids','x','y'])
    """
  
  node_ids = model.wv.index2word # list of node IDs
  result = {"node_ids":node_ids, "node_embeddings":node_embeddings}
  return result

def get_subgraph(subgraph_size, node_embeddings, node_ids, dimension=20, walk_length=16, num_walks=100, window=10, min_count=1, batch_words=4,):

  book_list = ["austen_2", "austen_4", "dickens_1", "dickens_4", "shakespeare_1", "shakespeare_5", "twain_1", "twain_4"]

  # Find the center for each node
  node_avg = np.mean(list(node_embeddings.values()), axis=0)

  # Compute the distance to the center for each book
  node_emb_distance = np.zeros(node_avg.shape[0])

  #Aggregate the distance for each node
  for book in book_list:
    node_emb_distance += np.sum(np.abs(node_embeddings[book] - node_avg)**2,axis=-1)**(1./2)

  node_dist_df = pd.DataFrame(zip(node_ids, list(node_emb_distance)), columns = ["words", "variation"])
  node_dist_df = node_dist_df.sort_values(by=['variation'], ascending=False)
  return list(node_dist_df['words'][:subgraph_size])