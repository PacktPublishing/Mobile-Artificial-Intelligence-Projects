
# coding: utf-8

# In[3]:


from flask import Flask, request
from keras import backend as K
from keras.models import load_model
import numpy
app = Flask(__name__)


# In[2]:


@app.route('/')
def hello_world():
    return 'Index page'


# In[4]:


@app.route('/predict', methods=['POST'])
def add():
    req_data = request.get_json()

    bizprop = req_data['bizprop']
    rooms = req_data['rooms']
    age = req_data['age']
    highways = req_data['highways']
    tax = req_data['tax']
    ptratio = req_data['ptratio']
    lstat = req_data['lstat']
    
    # This is where you load the actual saved model into new variable.
    deep_and_wide_net = load_model('deep_and_wide_net.h5')
    
    # Now you can use this to predict on new data (without fitting model2, because it uses the older saved model)
    value = deep_and_wide_net.predict_on_batch(numpy.array([[bizprop, rooms, age  ,  highways   , tax   ,  ptratio  ,   lstat]], dtype=float))
    K.clear_session()
    return str(value)

