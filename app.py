import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="My Mentor Hub", page_icon="🧭", layout="centered")

# --- API SETUP (Placeholder for now) ---
# Once you generate a Gemini API key, you will store it in Streamlit Secrets
# genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- SYSTEM PROMPTS ---
SAKSHI_PROMPT = """You are Sakshi, an empathetic wellness guide. 
Focus on mental clarity, values, and life balance. Keep your responses short, 
conversational, and always end by asking a thoughtful, supportive question."""

ANVESH_PROMPT = """You are Anvesh, a logical, strict, and highly motivated project mentor. 
Focus on hard goals, technical tasks, exam prep, and accountability. 
Keep responses direct, short, and action-oriented. Do not let the user make excuses."""

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Mentor Hub")
st.sidebar.write("Select your mentor below:")
mentor = st.sidebar.radio("Active Persona:", ["🌿 Sakshi (Wellness)", "⚡ Anvesh (Strategy)"])

# Clear chat history when switching mentors
if "current_mentor" not in st.session_state:
    st.session_state.current_mentor = mentor
if st.session_state.current_mentor != mentor:
    st.session_state.messages = []
    st.session_state.current_mentor = mentor

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- MAIN DASHBOARD UI ---
if mentor == "🌿 Sakshi (Wellness)":
    st.title("🌿 Sakshi")
    st.subheader("Your space for clarity and balance.")
    if not st.session_state.messages:
        st.info("Sakshi: Take a deep breath. How are you feeling today, and what can we do to make sure you are finding a good balance?")
        
elif mentor == "⚡ Anvesh (Strategy)":
    st.title("⚡ Anvesh")
    st.subheader("Your engine for strategy and execution.")
    if not st.session_state.messages:
        st.info("Anvesh: Let's get to work. What are your top 3 targets for today, and what is our strategy to hit them?")

st.divider()

# --- CHAT DISPLAY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- CHAT INPUT & LOGIC ---
if prompt := st.chat_input("Type your message here..."):
    # 1. Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 2. Save User Message to Memory
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 3. Generate AI Response (Simulated for now until API is connected)
    with st.chat_message("assistant"):
        # FUTURE: This is where we will pass the System Prompt and User Prompt to the Gemini API
        placeholder_response = f"*(This is where the API will generate the response based on the {mentor.split()[1]} persona.)*"
        st.markdown(placeholder_response)
        
    # 4. Save AI Message to Memory
    st.session_state.messages.append({"role": "assistant", "content": placeholder_response})
