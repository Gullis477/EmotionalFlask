# Load libraries
from pandas import read_csv

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

import pickle

def emotion_to_number(x):
    if x == 'negative':
        x = 0
    else:
        x = 1
    return x


names = ['id','alpha_bin','beta_bin','gamma_bin','delta_bin','theta_bin','alpha_beta','alpha_gamma','alpha_delta','alpha_theta','beta_alpha','beta_gamma','beta_delta','beta_theta','gamma_alpha','gamma_beta','gamma_delta','gamma_theta','delta_alpha','delta_beta','delta_gamma','delta_theta','theta_alpha','theta_beta','theta_gamma','theta_delta','min_att,max_att','mean_att_difference','sd_att_difference','min_med','max_med','mean_med_difference','sd_med_difference','mean_SCL','AUC_Phasic','min_peak_amplitude','max_peak_amplitude','mean_phasic_peak','sum_phasic_peak_amplitude','mean_temp','mean_temp_difference,max_temp','max_temp_difference,min_temp','min_temp_difference','difference_BVPpeaks_ampl','mean_BVPpeaks_ampl','min_BVPpeaks_ampl','max_BVPpeaks_ampl','sum_peak_ampl','HR_mean_difference','HR_variance_difference','valence']
dataset = read_csv("csvfiles\SAM_valence.csv")
dataset['valence'] = dataset['valence'].apply(emotion_to_number)
print(dataset.shape)
# Split-out validation dataset
array = dataset.values

X = array[:,1:53]
y = array[:,53]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)
name = 'KNN'
model = KNeighborsClassifier()
kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Make predictions on validation dataset
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print("Accuracy: ",accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

#saving model
filename = "test_valence_algoritm.sav"
pickle.dump(model, open(filename,'wb'))
