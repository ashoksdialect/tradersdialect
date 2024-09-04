import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Ashok's Portfolio", layout="wide")

# Load images for icons
def load_icon(image_name):
    return Image.open(f"icons/{image_name}.png")

# Social media links
social_links = {
    "LinkedIn": "https://www.linkedin.com/in/ashoksdialect/",
    "Facebook": "https://www.facebook.com/ashoksdialect/",
    "Instagram": "https://www.instagram.com/ashoksdialect/",
    "Snapchat": "https://www.snapchat.com/add/ashoksdialect",
    "X Platform": "https://twitter.com/ashoksdialect",
    "Threads": "https://www.threads.net/ashoksdialect",
    "Pinterest": "https://www.pinterest.com/ashoksdialect/",
    "Telegram": "https://t.me/ashoksdialect",
    "GitHub": "https://github.com/ashoksdialect",
}

# Title and description
st.title("Welcome to My Portfolio")
st.write("Connect with me on social media or explore my work.")

# Layout for icons
cols = st.columns(len(social_links))

for col, (platform, link) in zip(cols, social_links.items()):
    with col:
        icon = load_icon(platform.lower().replace(" ", "_"))
        st.image(icon, use_column_width=True)
        st.markdown(f"[{platform}]({link})")

# Add a section for personal projects
st.header("Personal Projects")
st.write("Check out some of the projects I've been working on:")

# Example project links
project_links = {
    "Project 1": "https://github.com/ashoksdialect/ashoksdialect",
    "Project 2": "https://github.com/ashoksdialect/tradersdialect",
}

for project, link in project_links.items():
    st.markdown(f"[{project}]({link})")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Created with ❤️ by Ashok</p>
    </div>
    """,
    unsafe_allow_html=True,
)
