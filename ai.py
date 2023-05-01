from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from flask import Flask, render_template, request
import csv
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(_name_)

codes = []  # Load the CSV file containing the codes
with open('test_codechef_distinctcol.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        codes.append(row[0])

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()


def preprocess(code):

    code = code.translate(str.maketrans('', '', string.punctuation))

    tokens = word_tokenize(code.lower())     # Tokenize the code

    filtered_tokens = [token for token in tokens if token not in stop_words]

    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    preprocessed_code = ' '.join(stemmed_tokens)
    return preprocessed_code


preprocessed_codes = [preprocess(code) for code in codes]

# Calculate the TF-IDF vectors for the preprocessed codes
vectorizer = TfidfVectorizer()
tfidf_vectors = vectorizer.fit_transform(preprocessed_codes)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    user_code = request.form['user_code']

    # Preprocess the user code and calculate its TF-IDF vector
    preprocessed_user_code = preprocess(user_code)
    user_tfidf_vector = vectorizer.transform([preprocessed_user_code])

    # Calculate the cosine similarity between the user code and each of the 50 codes
    similarities = cosine_similarity(user_tfidf_vector, tfidf_vectors)

    for i, similarity in enumerate(similarities[0]):
        if similarity > 0.8:
            plagiarism_percentage = similarity*100
            break
    else:
        plagiarism_percentage = None

    return render_template('index.html', plagiarism_percentage=plagiarism_percentage)


if _name_ == '_main_':
    app.run(debug=True)
