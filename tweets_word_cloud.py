from wordcloud import WordCloud, get_single_color_func
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt
import re
import io 
import os

pt_stopwords = nltk.corpus.stopwords.words('portuguese')

my_path = os.path.abspath("./img")
generated_png_file = 'tweets_venezuelanos_word_cloud.png'

with open('C:/Users/wei/Projects/Artigo_Revista_Ideias_Analise_Tweets/input/to_3_Third_treatment/tweets_text_out_txt_from_second_treatment.txt', 'r') as f:
    corpus = f.read()

    
corpus_filtered = re.sub("[^a-zA-Z\u00C0-\u017F]"," ",str([w for w in word_tokenize(corpus) if w not in pt_stopwords and len(w) > 6 and w not in ['https', 'httpswww']]))

cloud = WordCloud(width=1600, height=800, collocations=False).generate(corpus_filtered)
plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig(os.path.join(my_path, generated_png_file))
plt.show()



