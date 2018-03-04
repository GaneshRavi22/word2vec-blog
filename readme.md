# Word2vec Example on Brown corpus

This project contains code supporting the blog at url => https://humansandai.wordpress.com/2018/03/04/nlp-models-bow-word2vec-paragraph2vec/

## Source files
* word2vec_brown.py => This stand-alone python file contains the code to building a word2vec model
using gensim library. The brown corpus was used to build the model. Simple pre-processing like stop-word
removal and lowercasing text was employed. Also showcases simple operations on the final word vectors built.


## Running the example
### Running from PyCharm
* Import the cloned project into PyCharm. PyCharm will automatically install the required dependencies
from the _requirements.txt_ file
* Right and click on 'Run' option on the _word2vec_brown.py_ file from the project window.

### Running from the Terminal
* Python 2.x and pip should already be installed on the machine.
* Install the requirements from the _requirements.txt_ file, using the command
```
pip install -r requirements.txt
```
You might have to use sudo, if the user does not have enough permissions to install packages.
* Execute the python file using the command
```
python word2vec_brown.py
```