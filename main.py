import re
import random
from collections import Counter

def load_and_clean_text(filepath: str) -> list:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # convert to lowercase
        text = text.lower()
        
        # remove unwanted characters using regular expressions
        text = re.sub(r'[^a-zßäöü .,!?]', ' ', text)
        
        # add spaces around punctuation so they become separate "words"
        text = text.replace('.', '. ').replace(',', ', ').replace('!', '! ').replace('?', '? ')
        
        # 4. Split the text into a list of words
        words = text.split()
        
        print(f"Successfully loaded and cleaned the text. Found {len(words)} words.")
        return words

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []

def train_model(words: list) -> dict:
    model = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        
        # Wenn wir das Wort zum ersten Mal sehen, erstellen wir einen neuen Counter
        if current_word not in model:
            model[current_word] = Counter()
            
        # Zähle das Vorkommen des nächsten Wortes hoch
        model[current_word][next_word] += 1
        
    return model

def generate_text(model: dict, num_words: int = 100) -> str:
    # Wähle einen zufälligen Startpunkt
    current_word = random.choice(list(model.keys()))
    generated_words = [current_word]

    for _ in range(num_words - 1):
        # Hole den Counter für das aktuelle Wort
        next_word_counts = model.get(current_word)
        
        # Wenn es keine bekannten Folgewörter gibt (z.B. das letzte Wort im Text), stoppen
        if not next_word_counts:
            break
            
        # Trenne die möglichen nächsten Wörter und ihre Häufigkeiten
        possible_next_words = list(next_word_counts.keys())
        weights = list(next_word_counts.values())
        
        # Treffe eine gewichtete Zufallsauswahl
        chosen_word = random.choices(possible_next_words, weights=weights, k=1)[0]
        
        generated_words.append(chosen_word)
        current_word = chosen_word
        
    return ' '.join(generated_words)

if __name__ == "__main__":
    text_file = 'matamorphism_kafka.txt' 
    
    word_list = load_and_clean_text(text_file)
    
    if word_list:
        print("\nHere are the first 20 words from the cleaned list:")
        print(word_list[:20])
        markov_model = train_model(word_list)
        new_text = generate_text(markov_model)
        print(new_text)