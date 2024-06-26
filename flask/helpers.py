import whisper
import pytube as pt
from transformers import pipeline
import nltk
from newspaper import Article
import openai
import nltk
from youtube_transcript_api import YouTubeTranscriptApi
import re
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# nltk.download('punkt')


def get_summary(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    article_summary = article.summary
    return article_summary


def gpt3(text):
    # Get the API key from the environment variable
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text,
        temperature=0.7,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )
    content = response.choices[0].text
    print(content)
    return response.choices[0].text


def fact_check(text_peice):
    topic = text_peice
    query1 = f"check if this is fake news {topic} and cite if sources with links if it is and if it is not fake"
    query2 = "fact check this statement with statistics and official goverment sources {topic} and also provide other sources with links"
    response1 = gpt3(query1)
    response2 = gpt3(query2)
    print(response1)
    print(response2)
    return response1, response2


def one_word(text_piece):
    query = f"Check and respond with a boolean value whether or not the given news piece is fake or real. Answer in one word. {text_piece}"
    response = gpt3(query)
    print(response)
    return response


# **********************************************************************************
# **********************************************************************************
# **********************************************************************************
# **********************************************************************************

extract_imp_words = pipeline(
    "token-classification", model="ml6team/keyphrase-extraction-kbir-inspec")
zero_shot_classfier = pipeline("zero-shot-classification", model = 'facebook/bart-large-mnli')


def get_text(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    article_text = article.text
    return article_text


def category_identifier(text):
    final_classification = zero_shot_classfier(text, candidate_labels=[
                                               "sports", "politics", "education", "business", "entertainment", "healthcare and medicine", "science and technology", "religion", "product reviews", "projects and tutorials"])
    return final_classification['labels'][0]


def l_by_r(text):
    final_classification = zero_shot_classfier(
        text, candidate_labels=["left_views", "right_views"], return_all_scores=True)
    return (0.01*(final_classification['scores'][0]/final_classification['scores'][1]))


def type_of_views(text):
    final_classification = zero_shot_classfier(text, candidate_labels=["progessive left", "established liberal", "democractic mainstays",
                                               "outsider left", "ambivalent right", "populist right", "commited conservatives", "faith and flag conservatives"])
    return final_classification['labels'][0]


def news_type(text):
    final_classification = zero_shot_classfier(
        text, candidate_labels=["misinformation or fake news", "factual news"])
    return final_classification['labels'][0]


def type_of_propaganda(text):
    final_classification = zero_shot_classfier(text, candidate_labels=["Presenting Irrelevant Data", "Stereotyping", "Misrepresentation of Someone's Position,", "Whataboutism", "Causal Oversimplification", "Obfuscation, Intentional vagueness, Confusion", "Appeal to authority",
                                               "Black-and-white Fallacy", "Dictatorship", "Name calling or labeling", "Loaded Language", "Exaggeration or Minimisation", " Flag-waving", "Doubt", "Appeal to fear/prejudice", "Thought-terminating cliché", "Bandwagon", "Reductio ad hitlerum"])
    return final_classification['labels'][0:2]


def hatespeech(text):
    final_calssification = zero_shot_classfier(
        text, candidate_labels=['normal', 'offensive', 'hate speech'])
    return final_calssification['labels'][0]


def clickbait(text):
    final_calssification = zero_shot_classfier(
        text, candidate_labels=['not clickbait', 'clickbait'], return_all_scores=True)
    return final_calssification['scores'][1]


def sentiment_analysis(text):
    classifier = pipeline("text-classification", model = 'distilbert/distilbert-base-uncased-finetuned-sst-2-english')
    prediction = classifier(text)
    return prediction


def extract_keywords(text):
    data = extract_imp_words(text)
    keywords = [entry['word'] for entry in data]
    return keywords

# *****************************************************************************
# *****************************************************************************
# *****************************************************************************


def create_yt_transscript(url):
    yt = pt.YouTube(url)
    stream = yt.streams.filter(only_audio=True)[0]
    stream.download(filename="audio_english.mp3")
    model = whisper.load_model("medium")
    result = model.transcribe(
        "audio_english.mp3", ffmpeg_path="C:/Program Files/ffmpeg-2023-08-07-git-d295b6b693-full_build")
    return result


def transcript_generation(video_id):
    # YouTubeTranscriptApi.get_transcript(video_id)
    # transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    # for transcript in transcript_list:
    #     print("this is fetching data :", transcript.fetch())
    # return transcript_list
    data = YouTubeTranscriptApi.get_transcript(video_id)
    transscript = [entry['text'] for entry in data]
    transscript = ' '.join(transscript)
    print(transscript)
    return transscript
