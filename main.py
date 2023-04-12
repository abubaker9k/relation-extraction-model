import spacy
import nltk
from moviepy.editor import *
import os

os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'


# Load the pre-trained English language model from spaCy
nlp = spacy.load('en_core_web_sm')

# Load the text file
with open('my_text_file.txt', 'r') as f:
    text = f.read()
   # C:\users\administrator\appdata\local\packages\pythonsoftwarefoundation.python.3.11_qbz5n2kfra8p0\localcache\local-packages\python311\site-packages\en_core_web_sm

# Preprocess the text using spaCy to extract relevant information
doc = nlp(text)

# Extract all the named entities in the text
entities = [ent for ent in doc.ents]

# Extract all the sentences in the text
sentences = [sent for sent in doc.sents]

# Create a list of tuples, where each tuple contains the sentence text and the named entities in that sentence
sentences_and_entities = []
for sent in sentences:
    entities_in_sent = [ent for ent in entities if ent.sent == sent]
    sentences_and_entities.append((sent.text, entities_in_sent))

# Use moviepy to create an edited video based on the extracted information
clips = []
for sent, entities in sentences_and_entities:
    # Create a text clip for the sentence
    text_clip = TextClip(sent, fontsize=50, color='white', bg_color='black').set_duration(5)

    # Create a video clip for each named entity
    entity_clips = []
    for ent in entities:
        entity_clip = ImageClip(f'{ent.label_}.jpg').set_duration(5)
        entity_clips.append(entity_clip)

    # Combine the text clip and the entity clips into a single video clip
    final_clip = CompositeVideoClip([text_clip] + entity_clips)

    # Add the final clip to the list of clips
    clips.append(final_clip)

# Concatenate all the clips together into a single video
final_video = concatenate_videoclips(clips)

# Save the edited video
final_video.write_videofile('my_edited_video.mp4', fps=24)
