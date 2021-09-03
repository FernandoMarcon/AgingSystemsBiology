import pdftotext
import re

# PIPELINE
# read pdf
# extract text
# full text
# find topics
# split full text by topics
# for each topic:
#     write a markdown file, named by topic title

#--- Read PDF
file = open('Dissertation/FernandoMarconPassosDefesaMestrado.pdf','rb')
pdf = pdftotext.PDF(file)
pdf = list(pdf)[:80:]

#--- Extract text
def get_page(page):
    return page.replace('\u200b','').strip()

full_text = '\n\n'.join([get_page(page) for page in pdf])

#--- Find Topics
topics_idx = {'cover':0,'cover2':1,'acknowledgements':2,'abstract':[3,4],'abstract2':[5,6],'summary':7}
topics_idx

pdf[topics_idx['summary']].encode('utf-8')
summary = get_page(pdf[topics_idx['summary']]).split('\n')
