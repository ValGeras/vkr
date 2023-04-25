from flask import Flask, request, render_template
import tensorflow as tf

app = Flask(__name__)

@app.route('/')
def choose_prediction_method():
    return render_template('index.html')


def nn_prediction(params): 
    model = tf.keras.models.load_model('my_models/tf_models')
    pred = model.predict([params])
    return pred


@app.route('/', methods=['POST', 'GET']) 
def nn_predict():
    message = ''
    if request.method == 'POST':
        param_list = ('par1', 'par2', 'par3', 'par4', 'par5', 'par6',  
                      'par7', 'par8', 'par9', 'par10', 'par11', 'par12')
        params = []
        for i in param_list:
            param = request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        message = f'Соотношение матрица-наполнитель для введенных параметров: {nn_prediction(params)}'
    return render_template('index.html', message=message) 

if __name__ == '__main__': 
    app.run() 