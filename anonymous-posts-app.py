import streamlit as st
import random

st.set_page_config(layout="wide")

st.markdown("""
<style>
.post-card {
    background-color: #1e1e1e;
    padding: 18px;
    border-radius: 15px;
    margin-bottom: 15px;
    border-left: 6px solid #7f5af0;
}

.post-name {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 8px;
}

.post-text {
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# SESSION STATE
# -----------------------
if "posts" not in st.session_state:
    st.session_state.posts = []

if "names" not in st.session_state:
    st.session_state.names = []

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "universe" not in st.session_state:
    st.session_state.universe = None

if "character" not in st.session_state:
    st.session_state.character = None


# -----------------------
# CHARACTER LISTS
# -----------------------
dcu = [
"Batman","Superman","Wonder Woman","Flash","Aquaman",
"Green Lantern","Nightwing","Robin","Red Hood","Batgirl",
"Cyborg","Martian Manhunter","Green Arrow","Black Canary",
"Shazam","Supergirl","Zatanna","Constantine","Harley Quinn",
"Joker","Lex Luthor","Deathstroke","Bane","Riddler"
]

mcu = [
"Iron Man","Spider-Man","Thor","Hulk","Black Widow",
"Captain America","Doctor Strange","Scarlet Witch","Vision",
"Loki","Hawkeye","Ant-Man","Wasp","Black Panther",
"Winter Soldier","Falcon","War Machine","Star-Lord",
"Gamora","Rocket","Groot","Nebula","Mantis",
"Shang-Chi","Moon Knight","She-Hulk","Ms Marvel",
"Nick Fury","Yelena Belova","Wong","Okoye"
]

star_wars = [
"Luke Skywalker","Leia Organa","Han Solo","Chewbacca",
"Darth Vader","Yoda","Obi-Wan Kenobi","Anakin Skywalker",
"Rey","Kylo Ren","Ahsoka Tano","Mace Windu",
"Boba Fett","Din Djarin","Grogu","Palpatine",
"Count Dooku","General Grievous","Thrawn",
"Ezra Bridger","Sabine Wren","R2-D2","C-3PO"
]

lotr = [
"Frodo Baggins","Samwise Gamgee","Merry Brandybuck",
"Pippin Took","Aragorn","Legolas","Gimli","Gandalf",
"Boromir","Faramir","Arwen","Elrond","Galadriel",
"Eowyn","Theoden","Saruman","Sauron","Gollum",
"Bilbo Baggins","Thorin Oakenshield"
]

harry_potter = [
"Harry Potter","Hermione Granger","Ron Weasley",
"Dumbledore","Snape","Hagrid","Draco Malfoy",
"Luna Lovegood","Neville Longbottom","McGonagall",
"Sirius Black","Remus Lupin","Bellatrix Lestrange",
"Voldemort","Fred Weasley","George Weasley",
"Dobby","Lucius Malfoy","Moody","Umbridge"
]


# -----------------------
# SIDEBAR NAVIGATION
# -----------------------
st.sidebar.title("📍 Navigation")

if st.sidebar.button("🏠 Home"):
    st.session_state.page = "Home"

if st.sidebar.button("✍️ Create Post"):
    st.session_state.page = "Create"

if st.sidebar.button("📖 All Posts"):
    st.session_state.page = "All"

if st.sidebar.button("👤 My Posts"):
    st.session_state.page = "Mine"


# -----------------------
# HOME PAGE
# -----------------------
if st.session_state.page == "Home":

    st.title("🏠 Home")

    st.write("Welcome to Anonymous Thoughts Space 💬")
    st.write("Share your thoughts, feelings, or rants anonymously.")

    st.write("Choose your universe:")

    if st.button("🦇 DC"):
        st.session_state.universe = "DC"
        st.session_state.character = random.choice(dcu)
        st.session_state.page = "Create"

    if st.button("🛡️ Marvel"):
        st.session_state.universe = "Marvel"
        st.session_state.character = random.choice(mcu)
        st.session_state.page = "Create"

    if st.button("🌌 Star Wars"):
        st.session_state.universe = "Star Wars"
        st.session_state.character = random.choice(star_wars)
        st.session_state.page = "Create"

    if st.button("💍 LOTR"):
        st.session_state.universe = "LOTR"
        st.session_state.character = random.choice(lotr)
        st.session_state.page = "Create"

    if st.button("⚡ Harry Potter"):
        st.session_state.universe = "Harry Potter"
        st.session_state.character = random.choice(harry_potter)
        st.session_state.page = "Create"


# -----------------------
# CREATE POST PAGE
# -----------------------
if st.session_state.page == "Create":

    st.title("✍️ Create Post")

    if st.session_state.character:
        st.write(f"You are posting as: **{st.session_state.character}**")

    post = st.text_input("What's on your mind?")

    if st.button("Post"):
        if post:
            st.session_state.posts.append(post)
            st.session_state.names.append(st.session_state.character)
            st.success("Posted 💬")


# -----------------------
# ALL POSTS PAGE
# -----------------------
if st.session_state.page == "All":

    st.title("📖 All Posts")

    st.write("Newest posts first 🔥")

    for i in reversed(range(len(st.session_state.posts))):
        st.markdown(
    f"""
    <div class="post-card">
        <div class="post-name">
            🎭 {st.session_state.names[i]}
        </div>

        <div class="post-text">
            {st.session_state.posts[i]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------
# MY POSTS PAGE
# -----------------------
if st.session_state.page == "Mine":

    st.title("👤 My Posts")

    for i in reversed(range(len(st.session_state.posts))):

        if st.session_state.names[i] == st.session_state.character:

            st.markdown(
    f"""
    <div class="post-card">
        <div class="post-name">
            🎭 {st.session_state.names[i]}
        </div>

        <div class="post-text">
            {st.session_state.posts[i]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

            if st.button("🗑 Delete", key=f"del_{i}"):
                st.session_state.posts.pop(i)
                st.session_state.names.pop(i)
                st.rerun()