from DataProcessing import load_data
from DataProcessing import split_data
from DataProcessing import encode_class_labels_train
from DataProcessing import encode_class_labels_test
from DataProcessing import report_results
from DataProcessing import extract_feats_from_text_test
from DataProcessing import extract_feats_from_text_train
from DataProcessing import extract_feats_from_text_and_desc_test
from DataProcessing import extract_feats_from_text_and_desc_train

from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import MultinomialNB

JOBS = 4
PARAMS = [{'alpha': [8, 4, 2, 1, 0.5, 0.25, 0.1, 0.07, 0.05, 0.03, 0.01, 0.001]}]

df = load_data()
x_train, x_test = split_data()

y_test, class_names = encode_class_labels_test(x_test)

y_train, class_names1 = encode_class_labels_train(x_train)

print("Features only from Text")

X_test = extract_feats_from_text_test(x_test)
X_train = extract_feats_from_text_train(x_train)

grid_search = GridSearchCV(MultinomialNB(), PARAMS, n_jobs=JOBS, verbose=5, cv=4,
                           scoring="f1")

grid_search.fit(X_train, y_train)
report_results(grid_search, y_train, X_train, y_test, X_test, class_names)

print("Features from tweet text and description")

X_test = extract_feats_from_text_and_desc_test(x_test)
X_train = extract_feats_from_text_and_desc_train(x_train)

grid_search = GridSearchCV(MultinomialNB(), PARAMS, n_jobs=JOBS, verbose=5, cv=4,
                           scoring="f1")

grid_search.fit(X_train, y_train)
report_results(grid_search, y_train, X_train, y_test, X_test, class_names)