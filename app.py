import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Mandala Generator",
    page_icon="🎨",
    layout="centered"
)

# App title and description
st.title("🎨 Mandala Generator")
st.write("Generate beautiful black and white mandala art inspired by a single word!")

# Instructions
with st.expander("📖 How to use this app"):
    st.write("""
    1. Enter your OpenAI API key in the sidebar
    2. Type a single word that inspires you (e.g., peace, love, nature, harmony)
    3. Click 'Generate Mandala' to create your artwork
    4. Download your mandala as a JPEG file for printing
    
    **Note:** Keep your API key safe and don't share it with others!
    """)

# Sidebar for API key
st.sidebar.header("🔑 API Configuration")
api_key = st.sidebar.text_input(
    "Enter your OpenAI API Key:",
    type="password",
    help="Your API key will not be stored and is only used for this session"
)

# Main interface
st.header("Create Your Mandala")

# Input for inspiration word
inspiration_word = st.text_input(
    "Enter one word for inspiration:",
    placeholder="e.g., peace, love, nature...",
    max_chars=50
)

# Generate button
if st.button("🎨 Generate Mandala", type="primary"):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar first!")
    elif not inspiration_word.strip():
        st.error("Please enter an inspiration word!")
    else:
        try:
            # Clean the inspiration word - simple cleaning
            cleaned_word = inspiration_word.strip()
            
            # Set up OpenAI client
            client = openai.OpenAI(api_key=api_key)
            
            # Create the prompt
            prompt = f"A black and white mandala inspired by {cleaned_word}"
            
            # Show loading message
            with st.spinner("Creating your mandala... This may take a few seconds ✨"):
                # Generate image using DALL-E
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                
                # Get the image URL
                image_url = response.data[0].url
                
                # Download the image
                image_response = requests.get(image_url)
                image = Image.open(BytesIO(image_response.content))
                
                # Display the generated mandala
                st.success("Your mandala has been generated! 🎉")
                st.image(image, caption=f"Mandala inspired by: {cleaned_word}")
                
                # Convert to JPEG for download
                img_buffer = BytesIO()
                if image.mode == 'RGBA':
                    # Convert RGBA to RGB for JPEG
                    rgb_image = Image.new('RGB', image.size, (255, 255, 255))
                    rgb_image.paste(image, mask=image.split()[-1] if len(image.split()) == 4 else None)
                    rgb_image.save(img_buffer, format='JPEG', quality=95)
                else:
                    image.save(img_buffer, format='JPEG', quality=95)
                
                img_buffer.seek(0)
                
                # Create a safe filename
                safe_filename = cleaned_word.lower().replace(' ', '_')
                
                # Download button
                st.download_button(
                    label="📥 Download Mandala (JPEG)",
                    data=img_buffer.getvalue(),
                    file_name=f"mandala_{safe_filename}.jpg",
                    mime="image/jpeg"
                )
                
        except openai.AuthenticationError:
            st.error("Invalid API key. Please check your OpenAI API key and try again.")
        except openai.RateLimitError:
            st.error("Rate limit exceeded. Please wait a moment and try again.")
        except openai.BadRequestError as e:
            st.error(f"Request error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    "Made with ❤️ using Streamlit and OpenAI DALL-E | "
    "Remember to keep your API key secure!"
)