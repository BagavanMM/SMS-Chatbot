import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

# Need to change tehse logs depending on what kind of tone/stuff you want to give
start_chat_log = '''Human: What is maternal health?
AI: Maternal health refers to the health of women during pregnancy, childbirth and the postpartum period.
Human: What is maternal health?
AI: A maternal death is defined as “the death of a woman while pregnant or within 42 days of termination of pregnancy, irrespective of the duration and the site of the pregnancy, from any cause related to or aggravated by the pregnancy or its management, but not from accidental or incidental causes.”
Human: How is maternal health measure?
AI: There are numerous indicators used to measure and track maternal health across the globe. One of the most commonly used indicators is the maternal mortality ratio (MMR).
Human: What is the current maternal mortality ratio (MMR)?
AI: In Bolivia, the maternal mortality ratio is 155 per 100000 live births
Human: Are maternal deaths decreasing over time?
AI: In Bolivia, the it is! from 2003 the rate was 297 deaths per 100,000 live briths. In 2017 it decreased to 155 deaths 
Human: What are the casues of maternal deaths?
AI: The majority of maternal deaths occur from severe bleeding (after child birth), infections, high blood pressure during pregnancy, complications from deliver or unsafe abortion.

'''


# create the ask function to make the GPT-3 queries
def ask(question, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = completion.create(
        prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
        top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
        max_tokens=150)
    answer = response.choices[0].text.strip()
    return answer

# creating a function to append the questions and reponses into the chat log --> i..e, giving the chatbot "memory" of some sort
def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat_log
    return f'{chat_log}Human: {question}\nAI: {answer}\n'

try:
    while True:
        question = input(str("Human: "))
        answer = ask(question)
        print("AI: " +  answer)
except KeyboardInterrupt:
    pass