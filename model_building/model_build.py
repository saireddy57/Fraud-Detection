from sklearn.svm import SVC
from app_log import logger
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,roc_auc_score


class model_creation:
    def __init__(self):
        self.fie_obj = open('Model Creation.txt','w')
        self.logger = logger.app_log()
        # self.svc=SVC()
        # self.xgb = XGBClassifier()


    def best_params_xgb(self,x_train,y_train):
        try:
            param_dict = {
                'max_depth':[1,2,3,4,5,6,7,8,9,10],
                'min_child_weight':[1,2,3,7,8,9,10,4,5,6],
                'n_estimators':[100,130],
            }

            self.xgb_grid=GridSearchCV(estimator = XGBClassifier(use_label_encoder=False, learning_rate=0.1, n_estimators=540, max_depth=5,
                                         min_child_weight=2, gamma=0, subsample=0.8, colsample_bytree=0.8,
                                         eval_metric='mlogloss', nthread=4, scale_pos_weight=1,seed=27),
                                         param_grid = param_dict, scoring='roc_auc',n_jobs=4, cv=10)
            self.xgb_grid.fit(x_train,y_train)

            self.max_depth = self.xgb_grid.best_params_['max_depth']
            self.n_estimator = self.xgb_grid.best_params_['n_estimators']

            self.xgb_tuned = XGBClassifier(n_estimators=self.n_estimator,max_depth=self.max_depth,n_jobs=-1)

            self.xgb_tuned.fit(x_train,y_train)

            return self.xgb_tuned
        except Exception as e:
            print(e)


    def best_params_svc(self,x_train,y_train):

        try:
            self.svc = SVC()
            param_dict = {"kernel": ['rbf', 'sigmoid', 'poly'],
                          "C": [0.1, 0.5, 1.0],
                          "random_state": [0, 100, 200, 300]}
            self.svm_grid = GridSearchCV(self.svc, param_grid=param_dict, verbose=3)

            self.svm_grid.fit(x_train,y_train)

            self.svc_kernel = self.svm_grid.best_params_['kernel']
            self.svc_c = self.svm_grid.best_params_['C']
            self.svc_rand = self.svm_grid.best_params_['random_state']

            self.svc_tuned = SVC(kernel=self.svc_kernel,C=self.svc_c,random_state=self.svc_rand)

            self.svc_tuned.fit(x_train,y_train)

            return self.svc_tuned
        except Exception as e:
            print(e)

    def find_best_params(self,train_x,train_y,test_x,test_y):

        try:

            self.xgboost_model = self.best_params_xgb(train_x,train_y)
            self.xgb_pred = self.xgboost_model.predict(test_x)

            if len(test_y.unique()) == 1:
                self.score = accuracy_score(test_y,self.xgb_pred,normalize=False)
                print("accuracy----------------------------------score",self.score)
            else:
                self.score = roc_auc_score(test_y,self.xgb_pred)
                print("roc---------------auc------------------score",self.score)

            self.svc_model = self.best_params_svc(train_x,train_y)
            self.svc_pred = self.svc_model.predict(test_x)

            if len(test_y.unique()) == 1:
                self.svc_score = accuracy_score(test_y,self.svc_pred,normalize=False)
            else:
                self.svc_score = roc_auc_score(test_y,self.svc_pred)


            if self.svc_score > self.score :

                return self.svc_model,"SVC Model"
            else:
                return self.xgboost_model,"XGBoost Model"


        except Exception as e:
            print(e)



