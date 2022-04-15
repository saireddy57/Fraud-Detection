from sklearn.svm import SVC
from app_log import logger
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV


class model_creation:
    def __init__(self):
        self.fie_obj = open('Model Creation.txt','w')
        self.logger = logger.app_log()
        # self.svc=SVC()
        # self.xgb = XGBClassifier()


    def best_params_xgb(self,x_train,y_train,x_test,test_y):
        try:
            param_dict = {
                'max_depth':[1,2,3,4,5,6,7,8,9,10],
                'min_child_weight':[1,2,3,7,8,9,10,4,5,6],
                'n_estimators':[100,130],
                'criterion':['gini','entropy']
            }

            self.xgb_grid=GridSearchCV(estimator = XGBClassifier( learning_rate=0.1, n_estimators=540, max_depth=5,
                                         min_child_weight=2, gamma=0, subsample=0.8, colsample_bytree=0.8,
                                         objective= 'binary:logistic', nthread=4, scale_pos_weight=1,seed=27),
                                         param_grid = param_dict, scoring='roc_auc',n_jobs=4, cv=10)
            self.xgb_grid.fit(x_train,y_train)

            self.best_crit=self.xgb_grid.best_params_['criterion']
            self.max_depth = self.xgb_grid.best_params_['max_depth']
            self.n_estimator = self.xgb_grid.best_params_['n_estimators']

            self.xgb_tuned = XGBClassifier(criterion=self.best_crit,n_estimators=self.n_estimator,max_depth=self.max_depth,n_jobs=-1)

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
            pass

            # self.xgboost_model =

        except Exception as e:
            print(e)



