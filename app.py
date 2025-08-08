import os
import streamlit as st

# --- Apply tech green theme with custom CSS ---
st.markdown(
    """
    <style>
    /* Background */
    .main {
        background-color: #0f3d0f;  /* dark tech green */
        color: #b6f0b6;  /* light green text */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Headings */
    h1, h2, h3, .stButton>button {
        color: #7fff7f;  /* bright tech green */
    }
    /* Buttons */
    div.stButton > button {
        background-color: #228b22; /* forest green */
        color: white;
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: bold;
        border: none;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #32cd32; /* lime green */
        color: #004d00;
    }
    /* Radio buttons */
    .stRadio > div {
        color: #b6f0b6;
    }
    /* Progress bar */
    .stProgress > div > div > div > div {
        background-color: #32cd32 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.set_page_config(page_title="CodeFromScratch.AI", page_icon="💻")

# Show logo if present
if os.path.exists("logo.png"):
    st.image("logo.png", width=120)

st.title("💻 CodeFromScratch.AI")
st.write("Learn coding from scratch — bite-sized lessons like Duolingo for code!")

question_bank = {
    "Python": [
        {
            "q": "What does `print('Hello')` do in Python?",
            "options": [
                "Prints Hello to the screen",
                "Saves Hello to a file",
                "Creates a variable",
                "Starts a loop"
            ],
            "answer": "Prints Hello to the screen",
            "explain": "print(...) outputs text to the console."
        },
        {
            "q": "Which symbol starts a comment in Python?",
            "options": ["//", "#", "/* */", "<!-- -->"],
            "answer": "#",
            "explain": "Python comments start with #."
        },
        {
            "q": "How do you create a list with 1, 2, 3 in Python?",
            "options": ["(1,2,3)", "{1,2,3}", "[1,2,3]", "<1,2,3>"],
            "answer": "[1,2,3]",
            "explain": "Lists use square brackets."
        }
    ],
    "JavaScript": [
        {
            "q": "Which keyword declares a variable in JavaScript?",
            "options": ["var", "let", "const", "All of the above"],
            "answer": "All of the above",
            "explain": "JavaScript supports var, let, and const for variable declaration."
        },
        {
            "q": "What does `console.log('Hello')` do?",
            "options": ["Logs text to console", "Saves text to file", "Opens a dialog", "Starts a loop"],
            "answer": "Logs text to console",
            "explain": "console.log(...) prints messages to the browser console."
        },
        {
            "q": "Which symbol starts a comment in JavaScript?",
            "options": ["//", "#", "<!-- -->", "--"],
            "answer": "//",
            "explain": "Single-line comments in JavaScript use //."
        }
    ],
    "Java": [
        {
            "q": "Which method prints text to console in Java?",
            "options": ["print()", "System.out.println()", "echo()", "console.log()"],
            "answer": "System.out.println()",
            "explain": "System.out.println(...) prints to console in Java."
        },
        {
            "q": "Which symbol starts a single-line comment in Java?",
            "options": ["//", "#", "/* */", "--"],
            "answer": "//",
            "explain": "Java single-line comments start with //."
        },
        {
            "q": "Which keyword is used to define a class in Java?",
            "options": ["class", "Class", "define", "object"],
            "answer": "class",
            "explain": "Java classes are defined using the 'class' keyword."
        }
    ],
    "C++": [
        {
            "q": "Which header is needed for output in C++?",
            "options": ["<iostream>", "<stdio.h>", "<output.h>", "<string>"],
            "answer": "<iostream>",
            "explain": "#include <iostream> allows use of cout for output."
        },
        {
            "q": "Which operator is used for output in C++?",
            "options": ["<<", ">>", "::", "->"],
            "answer": "<<",
            "explain": "cout << outputs text to the console."
        },
        {
            "q": "Which symbol starts a comment in C++?",
            "options": ["//", "#", "/* */", "--"],
            "answer": "//",
            "explain": "C++ single-line comments start with //."
        }
    ]
}

if "language" not in st.session_state:
    st.session_state.language = None
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "completed" not in st.session_state:
    st.session_state.completed = False

if st.session_state.language is None:
    st.subheader("Choose your language to start:")
    lang_choice = st.selectbox("Pick a coding language:", list(question_bank.keys()))
    if st.button("Start Lesson"):
        st.session_state.language = lang_choice
else:
    questions = question_bank[st.session_state.language]
    total = len(questions)

    if st.session_state.completed:
        st.success(f"Lesson finished in {st.session_state.language} — score {st.session_state.score}/{total}")
        st.write("Imagine future levels, streaks, AI-generated lessons!")
        if st.button("Play again"):
            st.session_state.q_index = 0
            st.session_state.score = 0
            st.session_state.completed = False
            st.session_state.language = None
    else:
        q = questions[st.session_state.q_index]
        st.subheader(f"Question {st.session_state.q_index + 1} of {total} — {st.session_state.language}")
        st.write(q["q"])
        choice = st.radio("Pick an answer", q["options"], key=f"choice_{st.session_state.q_index}")

        if st.button("Submit", key=f"submit_{st.session_state.q_index}"):
            if choice == q["answer"]:
                st.success("✅ Correct")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect. Correct answer: {q['answer']}")
            st.write(q.get("explain", ""))

            if st.session_state.q_index + 1 >= total:
                st.balloons()
                st.session_state.completed = True
            else:
                st.session_state.q_index += 1

        st.write(f"**Score:** {st.session_state.score} / {total}")
        streamlit run app.py
        
