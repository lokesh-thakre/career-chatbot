# CareerChatBot – AI FAQ Chatbot for Career Guidance

## 1. Project Description  
**CareerChatBot** is an AI-powered FAQ chatbot designed especially for early-career professionals and job-seekers. It recognises common career-related questions (resume writing, skill development, interview preparation, remote work tips, LinkedIn profile optimisation, etc.) and provides concise, useful responses — helping users get immediate guidance 24/7.

## 2. Motivation  
Many early-career individuals repeatedly ask similar questions like:  
> “How do I write a resume?”  
> “What skills do I need to become a data analyst?”  
> “How do I prepare for a remote job interview?”  
Rather than navigating through dozens of articles, CareerChatBot provides a quicker, conversational experience. It aims to lower the barrier to career advice by making it accessible, automated and interactive.

## 3. Features  
- Recognises ~25+ intents of career-query types (e.g., resume tips, job search strategy, LinkedIn profile suggestions)  
- Pre-processes user input (tokenisation, lemmatisation), converts into vector form and classifies into an intent  
- Randomly selects a curated response for the detected intent, making the conversation feel more natural  
- Fallback logic: if the bot doesn’t understand a query, it apologises and asks the user to rephrase  
- Lightweight architecture: easy to extend and deploy  

## 4. Tech Stack  
- **Python 3.x** – core implementation  
- **NLTK / spaCy** – for text preprocessing (tokenisation, lemmatisation)  
- **scikit-learn** – for building the intent classifier (e.g., LogisticRegression)  
- **TF-IDF Vectorizer** (or optional sentence embeddings) – for converting text into numeric form  
- **Streamlit** (or Flask) – for a simple user interface/demo  
- **JSON** – for storing intents (patterns + responses)  

## 5. Architecture  
See `architecture_diagram.png` for an overview.  
**Flow**:  
1. User enters question → 2. Preprocessing (cleaning, lemmatisation) → 3. Vectorisation → 4. Classifier predicts intent tag → 5. Response selector picks a response from `intents.json` → 6. UI shows answer (or fallback if tag is unknown).  
This lightweight pipeline keeps the bot fast and simple to maintain.
