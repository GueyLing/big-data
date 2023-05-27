import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import joblib
from tensorflow.keras.preprocessing.sequence import pad_sequences
tokenizer = joblib.load('tokenizer.pkl')
model = joblib.load('sentiment_analysis_model.pkl')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    dcc.Input(id='input-field', type='text', placeholder='Enter input'),
    html.Button('Process', id='process-button', n_clicks=0),
    html.Div(id='output')
])

# Tokenize the text
def tokenization(inputs):  
    return word_tokenize(inputs)

# Remove stop words
stop_words = set(stopwords.words('english'))
stop_words.remove('not')

def stopwords_remove(inputs): 
    return [k for k in inputs if k not in stop_words]

# Perform lemmatization
lemmatizer = WordNetLemmatizer()

def lemmatization(inputs):  
    return [lemmatizer.lemmatize(word=kk, pos='v') for kk in inputs]

def predict_recommendation(user_text): 
    user_text = user_text.lower()
    user_text = re.sub(r'[^a-z]', ' ', user_text)
    user_text = tokenization(user_text)
    user_text = stopwords_remove(user_text)
    user_text = lemmatization(user_text)
    user_text = ' '.join(user_text)
    user_text = tokenizer.texts_to_sequences([user_text])
    user_text = pad_sequences(user_text, maxlen=50, padding='pre')
    return user_text

# Define the callback function
@app.callback(Output('output', 'children'),
              [Input('process-button', 'n_clicks')],
              [Input('input-field', 'value')])
def process_button_click(n_clicks, input_value):
    if n_clicks > 0:
        # Call the function and get the processed output
        processed_output = predict_recommendation(input_value)
        result = model.predict(processed_output)
        if result >= 0.5:
            # Return the processed output
            return 'Recommended'
        else:
            # Return the processed output
            return 'Not recommended'
    else:
        return ''

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)