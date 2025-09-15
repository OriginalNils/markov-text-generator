import random, os, re
from collections import Counter

def load_and_clean_text_from_directory(directory_path: str) -> list:
    all_words = []
    
    print(f"Reading files from directory: {directory_path}")
    
    try:
        # Loop through all files in the given directory
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory_path, filename)
                print(f"  - Processing file: {filename}")
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                
                # Cleaning steps (same as before)
                text = text.lower()
                text = text.replace('"', '')
                text = text.replace('“', '')
                text = text.replace('”', '')
                text = re.sub(r'[^a-zßäöü .,!?]', ' ', text)
                text = text.replace('.', '. ').replace(',', ', ').replace('!', '! ').replace('?', '? ')
                
                # Add the words from this file to our main list
                all_words.extend(text.split())

        if not all_words:
            print("Warning: No .txt files found or files were empty.")
        else:
            print(f"\nSuccessfully loaded and cleaned all files. Found {len(all_words)} total words.")
        
        return all_words

    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' was not found.")
        return []

def train_model(words: list) -> dict:
    model = {}
    for i in range(len(words) - 1):
        current_word = words[i]
        next_word = words[i+1]
        
        if current_word not in model:
            model[current_word] = Counter()
            
        model[current_word][next_word] += 1
        
    return model

def generate_text(model: dict, num_words: int = 100, show_odds: bool = True) -> str:
    if not model:
        return "The model is not trained. Please provide text files."

    current_word = random.choice(list(model.keys()))
    generated_words = [current_word]
    
    print("--- Starting Text Generation ---")
    if show_odds:
        print(f"Start word: '{current_word}'\n" + "="*30)

    for i in range(num_words - 1):
        next_word_counts = model.get(current_word)
        if not next_word_counts:
            break
        
        # --- NEU: Wahrscheinlichkeiten berechnen und ausgeben ---
        if show_odds:
            total_occurrences = sum(next_word_counts.values())
            
            # Berechne die Wahrscheinlichkeit für jedes mögliche Folgewort
            odds = []
            for word, count in next_word_counts.items():
                probability = count / total_occurrences
                odds.append((word, probability))
            
            # Sortiere die Liste nach Wahrscheinlichkeit (absteigend)
            odds.sort(key=lambda item: item[1], reverse=True)
            
            print(f"Current word: '{current_word}'")
            print("Possible next words (Top 5):")
            for word, prob in odds[:5]: # Zeige nur die Top 5 an
                print(f"  - '{word}': {prob:.2%}")
        
        # --- Die gewichtete Zufallsauswahl bleibt gleich ---
        possible_next_words = list(next_word_counts.keys())
        weights = list(next_word_counts.values())
        
        chosen_word = random.choices(possible_next_words, weights=weights, k=1)[0]
        generated_words.append(chosen_word)
        current_word = chosen_word
        
        if show_odds:
            print(f"--> Chosen word: '{chosen_word}'\n" + "="*30)
            
    return ' '.join(generated_words)

if __name__ == "__main__":
    corpus_directory = 'text_corpus' # The name of your folder

    word_list = load_and_clean_text_from_directory(corpus_directory)
    
    if word_list:
        markov_model = train_model(word_list)

        print("\n--- GENERATED TEXT ---")
        new_text = generate_text(markov_model, num_words=150)
        print(new_text)