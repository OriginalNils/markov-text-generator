
# Markov Chain Text Generator 📖✍️

This Python project uses a Markov chain model to learn the statistical patterns from one or more texts and generate new, stylistically similar text.





## ✨ Key Features

- **Trains on Multiple Sources:** The model can be trained on a single `.txt file or an entire directory of `.txt` files to build a richer statistical base.

- **Efficient Model:** Uses Python's `collections.Counter` for a memory-efficient and fast way to store word transition probabilities.

- **Debug Mode:** An optional mode to print the probabilities for the possible next words at each step of the generation process, providing insight into the model's "decisions."


## 🧠 How It Works

The generator is based on a Markov chain, a statistical model with a "short-term memory." It analyzes a given text to build a probability map of which word is most likely to follow any other given word. When generating new text, it starts with a random word and then makes a series of weighted random choices to select the next word, creating a new text that statistically resembles the original author's style.
## 📚 Data Source: Project Gutenberg

The best source for training data for this project is **Project Gutenberg**, a digital library of over 70,000 free, public domain eBooks.

- **Website**: gutenberg.org

You can download classic literature as clean **Plain Text UTF-8** (`.txt`) files, which are perfect for training the model. For best results, use multiple books from the same author to give the model a large, stylistically consistent dataset to learn from.
## 🚀 Installation & Usage

To run this application locally, please follow these steps.

#### 1. Clone the repository:

```bash
git clone https://github.com/OriginalNils/markov-text-generator.git
cd markov-text-generator
```

#### 2. Get training data:
If you want to use your own training data, just download them from **Project Gutenberg** and paste the cleaned `.txt`file into the `text_corpus`folder.

#### 3. Run the script:
Execute the main script from your terminal. It will automatically read all the files in the text_corpus folder, train the model, and print a newly generated text.

```bash
python main.py
```

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

