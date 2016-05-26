A naive Bayes classifier to identify hotel reviews as either truthful or deceptive, and either positive or negative. Word tokens are used as features for classification.

DATA:
A set of training data is made available in a directory. 
-A top-level directory with two sub-directories, one for positive reviews and another for negative reviews.
-Each of the subdirectories contains two sub-directories, one with truthful reviews and one with deceptive reviews.
-Each of these subdirectories contains four subdirectories, called “folds”.
-Each of the folds contains 80 text files with English text (one review per file).

PROGRAMS:
-nblearn.py - will learn a naive Bayes model from the training data.
-nbclassify.py - will use the model to classify new data.

The learning program will be invoked in the following way:

> python nblearn.py /path/to/input

The argument is the directory of the training data; the program will learn a naive Bayes model, and write the model parameters to a file called nbmodel.txt.

The classification program will be invoked in the following way:

> python nbclassify.py /path/to/input

The argument is the directory of the test data; the program will read the parameters of a naive Bayes model from the file nbmodel.txt, classify each file in the test data, and write the results to a text file called nboutput.txt in the following format:

label_a label_b path1
label_a label_b path2 
⋮

In the above format, label_a is either “truthful” or “deceptive”, label_b is either “positive” or “negative”, and pathn is the path of the text file being classified.


NOTES:
-Development data - While developing the programs, you should reserve some of the data as development data in order to test the performance of your programs. folds 2, 3, and 4 as training data, and fold 1 as development data: that is, it will run nblearn.py on a directory containing only folds 2, 3, and 4, and it will run nbclassify.py on a directory containing only fold 1.
-Problem formulation - You may treat the problem as two binary classification problems (truthful/deceptive and positive/negative), or as a 4-class single classification problem. (I have used 4-class single classification)
-Smoothing and unknown tokens - You should implement some method of smoothing for the training data and a way to handle unknown vocabulary in the test data, otherwise your programs won’t work. My solution will use add-one smoothing on the training data, and will simply ignore unknown tokens in the test data. You may use more sophisticated methods which you implement yourselves.
-Tokenization - You’d need to develop some reasonable method of identifying tokens in the text (since these are the features for the naive Bayes classifier). Some common options are removing certain punctuation, or lowercasing all the letters. You may also find it useful to ignore certain high-frequency or low-frequency tokens. You may use any tokenization method which you implement yourselves
