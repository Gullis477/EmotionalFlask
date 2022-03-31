# Load libraries
import pickle
import random
import matplotlib.pyplot as plt
import time
import handleCSV

# ------------------------------------------------------------------------------


def fake_data():
    '''
    Creates 4 random floats between 0 and 1 in a list
    '''
    data = [random.random() for _ in range(4)]
    return data


def classify(data, model):
    '''Classify the the input data with the input model and returns a string with the classification'''
    predicted_class = model.predict([data])
    return predicted_class[0]


def bar_chart_arousal(data, names, classification):
    '''Creates a barchart with the input data and the names as column names, the input classification will go in the title '''
    
    plt.clf()
    plt.bar(names, data)
    plt.title('Your Arousal is: '+classification)
    plt.xlabel('Brainwave')
    plt.ylabel('BrainDamage')
    plt.savefig('static/eyy.png')


# ------------------------------------------------------------------------------
# load the model from disk


loaded_model = pickle.load(open('test_algoritm.sav', 'rb'))
names = ['alpha_bin','beta_bin','gamma_bin','delta_bin']
def run(names=names):
    for _ in range(10):
        dataset = fake_data()
        result = classify(dataset,loaded_model)
        bar_chart_arousal(dataset,names,result)
        time.sleep(3)




