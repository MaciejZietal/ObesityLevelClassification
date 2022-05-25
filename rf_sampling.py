import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, fbeta_score
from imblearn.over_sampling import BorderlineSMOTE
from imblearn.over_sampling import ADASYN
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import NearMiss
from imblearn.under_sampling import TomekLinks
from imblearn.combine import SMOTETomek
import random

random.seed(10)

data = pd.read_csv('data/preparedData.csv')

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

#Data type to category
colnames = list(x.columns)[:-6]
for col in colnames:
    x[col] = x[col].astype('category')

#train and test split
X_train_res, X_test, y_train_res, y_test = train_test_split(x, y, train_size=0.7, random_state=42)

#Model evaluation
samplers = ["", RandomOverSampler, SMOTE,
                ADASYN, BorderlineSMOTE, RandomUnderSampler, NearMiss,
                TomekLinks, SMOTETomek]

#FB_score
fb_score = make_scorer(fbeta_score, beta=1/2, pos_label=1)

#Params grid
param_grid = {
    "max_depth": [3,4,5,7,10,15,20,None],
    "min_samples_split": [2,5,7,10],
    "min_samples_leaf": [1,2,3,4,5]
}

results = {}

for sampler in samplers:
    #Oversampling
    if sampler != "":
        if sampler == NearMiss:
            os = sampler(version=3)
        elif sampler == TomekLinks:
            os = sampler()
        else:
            os = sampler(random_state=12)
        X_train_res, y_train_res = os.fit_resample(X_train_res, y_train_res)
        X_train_res.fillna(0, inplace=True)
    
    #Searching models params
    rf = RandomForestClassifier()
    grid_cv = GridSearchCV(rf, param_grid, scoring=fb_score, 
                           n_jobs=-1, cv=5).fit(X_train_res, y_train_res)
    
    #Creating model
    rf = RandomForestClassifier(**grid_cv.best_params_)
    rf.fit(X_train_res, y_train_res)
    
    #Prediction
    y_pred = rf.predict(X_test)
    #Confusion matrix
    cf_matrix = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cf_matrix.ravel()
    
    result = rf.score(X_test, y_test)
    
    s = f"Acc = {result}\ntp: {tp}   fp: {fp}\nfn: {fn}   tn: {tn}"
    if sampler == "":
        results["None"] = s
    else:
        results[sampler.__name__] = s
    

for n, r in zip(results.keys(), results.values()):
    print(f"{n}\n{r}\n")