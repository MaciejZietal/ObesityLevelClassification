import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
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
X_train, X_test, y_train_res, y_test = train_test_split(x, y, train_size=0.7, random_state=42)

#data scaling
X_train_cat = X_train.iloc[:,:-6]
X_train_cat.reset_index(drop=True, inplace=True)
X_train_con = X_train.iloc[:,-6:]
X_test_cat = X_test.iloc[:,:-6]
X_test_cat.reset_index(drop=True, inplace=True)
X_test_con = X_test.iloc[:,-6:]

scaler = MinMaxScaler()
X_train_con = pd.DataFrame(scaler.fit_transform(X_train_con))
X_test_con = pd.DataFrame(scaler.transform(X_test_con))

X_train_res = pd.concat([X_train_con, X_train_cat],axis=1, ignore_index=True)
X_test = pd.concat([X_test_con, X_test_cat],axis=1, ignore_index=True)

#Model evaluation
samplers = ["", RandomOverSampler, SMOTE,
                ADASYN, BorderlineSMOTE, RandomUnderSampler, NearMiss,
                TomekLinks, SMOTETomek]

#FB_score
fb_score = make_scorer(fbeta_score, beta=1/2, pos_label=1)

#Params grid
param_grid = {'C': [0.1, 1, 10, 100, 1000],
              'gamma': [1, 0.1, 0.01, 0.001, 0.0001]}

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
    svc = SVC()
    grid_cv = GridSearchCV(svc, param_grid, scoring=fb_score, 
                           n_jobs=-1, cv=5).fit(X_train_res, y_train_res)
    
    #Creating model
    svc = SVC(**grid_cv.best_params_)
    svc.fit(X_train_res, y_train_res)
    
    #Prediction
    y_pred = svc.predict(X_test)
    #Confusion matrix
    cf_matrix = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cf_matrix.ravel()
    
    result = svc.score(X_test, y_test)
    
    s = f"Acc = {result}\ntp: {tp}   fp: {fp}\nfn: {fn}   tn: {tn}"
    if sampler == "":
        results["None"] = s
    else:
        results[sampler.__name__] = s
    

for n, r in zip(results.keys(), results.values()):
    print(f"{n}\n{r}\n")