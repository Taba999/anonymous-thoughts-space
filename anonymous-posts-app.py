import streamlit as st
import random
from gsheets import add_post, get_posts

st.set_page_config(layout="wide")

# -----------------------
# STYLE (CARDS)
# -----------------------
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
# SESSION STATE (ONLY WHAT WE NEED)
# -----------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "universe" not in st.session_state:
    st.session_state.universe = None

if "character" not in st.session_state:
    st.session_state.character = None

if "username" not in st.session_state:
    st.session_state.username = "Anonymous"

# -----------------------
# CHARACTER LISTS
# -----------------------
dcu = ["Batman","Superman","Wonder Woman","Flash","Aquaman",
"Green Lantern","Nightwing","Robin","Red Hood","Batgirl",
"Cyborg","Martian Manhunter","Green Arrow","Black Canary",
"Shazam","Supergirl","Zatanna","Constantine","Harley Quinn",
"Joker","Lex Luthor","Deathstroke","Bane","Riddler"]

mcu = ["Iron Man","Spider-Man","Thor","Hulk","Black Widow",
"Captain America","Doctor Strange","Scarlet Witch","Vision",
"Loki","Hawkeye","Ant-Man","Wasp","Black Panther",
"Winter Soldier","Falcon","War Machine","Star-Lord",
"Gamora","Rocket","Groot","Nebula","Mantis"]

star_wars = ["Luke Skywalker","Leia Organa","Han Solo","Chewbacca",
"Darth Vader","Yoda","Obi-Wan Kenobi","Anakin Skywalker",
"Rey","Kylo Ren","Ahsoka Tano","Mace Windu",
"Boba Fett","Din Djarin","Grogu","Palpatine",
"Count Dooku","General Grievous","Thrawn",
"Ezra Bridger","Sabine Wren","R2-D2","C-3PO"]

lotr = ["Frodo Baggins","Samwise Gamgee","Merry Brandybuck",
"Pippin Took","Aragorn","Legolas","Gimli","Gandalf",
"Boromir","Faramir","Arwen","Elrond","Galadriel",
"Eowyn","Theoden","Saruman","Sauron","Gollum",
"Bilbo Baggins","Thorin Oakenshield"]

harry_potter = ["Harry Potter","Hermione Granger","Ron Weasley",
"Dumbledore","Snape","Hagrid","Draco Malfoy",
"Luna Lovegood","Neville Longbottom","McGonagall",
"Sirius Black","Remus Lupin","Bellatrix Lestrange",
"Voldemort","Fred Weasley","George Weasley",
"Dobby","Lucius Malfoy","Moody","Umbridge"]

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

# -----------------------
# HOME PAGE
# -----------------------
if st.session_state.page == "Home":

    st.title("🏠 Home")
    st.write("Welcome to Anonymous Thoughts Space 💬")
    st.write("Share your thoughts anonymously with a random universe identity.")

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
        st.success(f"You are posting as: {st.session_state.character}")

    post = st.text_area("What's on your mind?", height=150)

    if st.button("Post"):
        if post:
            add_post(
                st.session_state.username,
                st.session_state.character,
                post
            )
            st.success("Posted 🌐")
            st.rerun()

# -----------------------
# ALL POSTS PAGE
# -----------------------
if st.session_state.page == "All":

    st.title("📖 All Posts")

    st.write("Newest posts first 🔥")

    posts = get_posts()

    if not posts:
        st.info("No posts yet. Be the first to post ✍️")

    for post in reversed(posts):
        st.markdown(
            f"""
            <div class="post-card">
                <div class="post-name">
                    🎭 {post['character']}
                </div>
                <div class="post-text">
                    {post['text']}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
