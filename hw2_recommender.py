from lightfm import LightFM
import numpy as np
from lightfm.datasets import fetch_movielens
import matplotlib
import matplotlib.pyplot as plt
from lightfm.evaluation import auc_score

movielens = fetch_movielens(min_rating=5.0)
print(repr(movielens['train']))
print(repr(movielens['test']))


train, test = movielens['train'], movielens['test']

alpha = 1e-3
epochs = 70

model = LightFM(no_components=30,
                loss='logistic',
                learning_schedule='adadelta',
                user_alpha=alpha,
                item_alpha=alpha)

auc = []

for epoch in range(epochs):
    model.fit_partial(train, epochs=1)
    auc.append(auc_score(model, test).mean())


def sample_recommendation(model, data, user_ids):

    n_users, n_items = data['train'].shape

    for user_id in user_ids:
        known_positives = data['item_labels'][data['train'].tocsr()[
            user_id].indices]

        scores = model.predict(user_id, np.arange(n_items))
        top_items = data['item_labels'][np.argsort(-scores)]

        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)


sample_recommendation(model, movielens, [11, 33, 555, 777])
