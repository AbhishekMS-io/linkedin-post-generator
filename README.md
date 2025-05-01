# LinkedIn Post Generator using Generative AI

🚀 **LinkedIn Post Generator** is a powerful tool that leverages generative AI to help you craft high-quality LinkedIn posts in seconds. This tool will analyze posts of a LinkedIn influencer and help them create the new posts based on the writing style in their old posts. Whether you want to create short, medium, or long posts tailored to specific topics, this project makes content creation effortless and efficient.

---

## Features

- Generate LinkedIn posts based on selected topics (tags), length, and language.
- Supports English language with potential for Hinglish (Hindi + English) mix.
- Uses few-shot learning with curated example posts to guide the AI's writing style.
- Preprocesses raw LinkedIn posts to extract metadata such as language, line count, and tags.
- Unifies tags to maintain consistency across post topics.
- Interactive web interface built with Streamlit for easy customization and post generation.

---

## How It Works

1. **Data Preprocessing**  
   The `preprocess.py` script cleans raw LinkedIn posts, extracts metadata (line count, language, tags), and unifies tags for consistency.

2. **Few-Shot Learning**  
   The `few_shot.py` module loads processed posts and categorizes them by length and language, providing example posts to guide the AI generation.

3. **Post Generation**  
   The `post_generator.py` module constructs prompts based on user-selected parameters and invokes the generative language model to create posts.

4. **Language Model Integration**  
   The `llm_helper.py` module connects to the Groq LLM API (using the `ChatGroq` model) to generate content.

5. **User Interface**  
   The `main.py` script runs a Streamlit app where users can select a topic, post length, and language, then generate a LinkedIn post instantly.

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd linkedin-post-generator
   ```

2. Install dependencies (assuming Python environment):

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the root directory and add your Groq API key:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Prepare data:

   Place your raw LinkedIn posts JSON file at `data/raw_posts.json` and run preprocessing:

   ```bash
   python preprocess.py
   ```

---

## Usage

Start the Streamlit app:

```bash
streamlit run main.py
```

Use the web interface to:

- Select a post topic (tag)
- Choose the desired post length (Short, Medium, Long)
- Pick the language (English)
- Click "Generate Post" to create your LinkedIn post instantly

---

## Project Structure

- `preprocess.py` - Cleans and enriches raw post data with metadata and unified tags.
- `few_shot.py` - Loads processed posts and provides example posts for few-shot prompting.
- `post_generator.py` - Builds prompts and generates posts using the language model.
- `llm_helper.py` - Handles connection to the Groq LLM API.
- `main.py` - Streamlit app for user interaction and post generation.
- `data/` - Contains raw and processed post data files.

---

## Technologies Used

- Python 3
- Streamlit for the web interface
- LangChain for prompt templates and output parsing
- Groq LLM API for generative AI
- Pandas for data handling

---

## About

This project demonstrates how generative AI can be harnessed to automate content creation for professional networking platforms like LinkedIn. It combines data preprocessing, few-shot learning, and prompt engineering to produce relevant and engaging posts tailored to user preferences.

---

## License

This project is licensed under the MIT License.

---

Feel free to connect with me on LinkedIn and share your feedback or contributions!
