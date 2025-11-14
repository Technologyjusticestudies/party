# --- 1. IMPORT YOUR TOOLS ---
# We're importing the 'streamlit' library, which is a set of tools for building web apps.
# We give it a nickname 'st' so it's faster to type (e.g., st.title instead of streamlit.title).
import streamlit as st

# --- 2. SET UP THE APP'S TITLE ---
# This command draws the main title on our web page.
st.title("My Emoji Translator 💬➡️😎")

# --- NEW: Instructions Section ---
with st.expander("👉 How to use this app"):
    st.write("""
        1.  Type a sentence in the **"Enter your text"** box.
        2.  If your sentence includes any of the "Magic Words" listed below, they will be translated into emojis!
        3.  Try it! Type: `I love coding with python and my cat`
    """)
# --- End of new section ---


# --- 3. CREATE THE "DICTIONARY" ---
# This is a Python Dictionary. It stores data as "key: value" pairs.
# It's our 'brain' for translating. The 'key' is the word to find,
# and the 'value' is the emoji to replace it with.
#
# --- CHALLENGE 1: Add your words! ---
# Add at least 5 of your own key:value pairs to this dictionary.
# Don't forget the comma after each line!
#
EMOJI_DICT = {
    "love": "❤️",
    "happy": "😊",
    "sad": "😢",
    "cat": "🐱",
    "dog": "🐶",
    "sun": "☀️",
    "coding": "💻",
    "win": "🏆",
    "python": "🐍",
    "fire": "🔥"
    # Students can add more!
}

# ------------------------------------

# --- 4. (Helper) SHOW THE "MAGIC WORDS" ---
# This isn't part of the challenge. This code just
# joins all the 'keys' (words) from our dictionary and
# displays them on the screen so the user knows what to type.
st.subheader("Magic Words We Know:")
# We'll join all the keys (the words) into a single string
st.write(", ".join(EMOJI_DICT.keys()))
st.markdown("---")  # Adds a horizontal line
# --- End of new section ---


# --- 5. GET INPUT FROM THE USER ---
# We need to ask the user to type something.
#
# --- CHALLENGE 2: Get user input ---
# Use the correct `st` command to draw a text box on the screen.
# The text inside the parentheses is the 'prompt' the user will see.
# We store whatever the user types in a variable called `user_input`.
#
user_input = st.text_input("Enter your text to translate:")

# --- 6. "TRANSLATE" THE TEXT ---
# This is where the main logic happens!

# First, we make all words lowercase (so 'Cat' becomes 'cat')
# Second, we 'split' the sentence into a list of individual words.
# e.g., "My Cat is cool" -> ["my", "cat", "is", "cool"]
words = user_input.lower().split()

# We create a new, empty list to store our translated words.
translated_words = []

# --- 7. LOOP THROUGH ALL THE WORDS ---
# This 'for' loop looks at each 'word' in our 'words' list, one by one.
for word in words:
    # Use .get() to find the word in our dictionary.
    # If it's not found, it just returns the original word.
    translated_word = EMOJI_DICT.get(word, word)
    translated_words.append(translated_word)

# --- 8. JOIN THE WORDS BACK TOGETHER ---
# We're doing the opposite of .split(). We're 'joining' the
# list of translated words back into a single string,
# separated by a space (" ").
output_sentence = " ".join(translated_words)

# --- 9. DISPLAY THE RESULT ---
# If the user typed something, show the result.
if output_sentence:
    st.header("Your Emoji Sentence:")
    st.write(output_sentence)
