# Plagiarism Checker
This program is designed to recommend similar codes based on user input. The program uses Natural Language Processing techniques to preprocess and vectorize the codes, and then calculates the cosine similarity between the user input and each of the codes. The program outputs the codes that have the highest similarity to the user input.

![image](https://user-images.githubusercontent.com/77913618/235352040-84d3e798-85fa-47fe-9e6e-8114f96291bd.png)


YouTube : https://youtu.be/Ynv6IpoZgsA

This code loads a CSV file containing a list of code snippets and prompts the user to enter a code. It then preprocesses the codes by removing punctuation, tokenizing the code, removing stop words, and stemming the tokens. After preprocessing, it calculates the TF-IDF vectors for each code snippet. 

The user's entered code is also preprocessed and its TF-IDF vector is calculated. Cosine similarity is then calculated between the user's code and each of the 50 code snippets using the TF-IDF vectors. Codes with a similarity score greater than 0.8 are printed to the console along with their similarity percentage.

This code could be used for various applications such as code plagiarism detection or finding similar code snippets in a repository. However, it is worth noting that cosine similarity is just one approach to code similarity and there may be other techniques that could be used depending on the specific requirements of the use case.
