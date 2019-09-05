import sys

############################ Madelon Dataset Generation #############################
num_class = 2
num_sample_per_cluster = 100
num_cluster_per_class = 4

num_useful_feat = 5
num_redundant_feat = 5
num_useless_feat = 30

random_seed = 79

num_F = num_useful_feat + num_redundant_feat + num_useless_feat

# random_seed = np.random.randint(1, 100)

sys.path.append('/Users/shenzixiao/Dropbox/Python/Madelon-Dataset-Generation')
from Madelon_Generator import hypercube_data

[X, Y] = hypercube_data(num_class, num_useful_feat,
                        num_redundant_feat, num_useless_feat,
                        num_cluster_per_class, num_sample_per_cluster,
                        random_seed)
