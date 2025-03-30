import streamlit as st

from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Corsant", page_icon="📦", layout="wide")
    st.image("./images/wmremove-transformed.png", use_container_width=False)
    st.title("Welcome to Corsant!")
    st.write("Discover our amazing products.")


    #TEST
    
    # Sidebar Navigation with Styling
    with st.sidebar:
        page = option_menu(
            menu_title="Menu",
            options = ["Home", "Products"],
            default_index=0
        )
    
    if page == "Home":
        st.header("About Corsant")
        st.write("Corsant is a health technology startup dedicated to design solutions for the future of medicine")
    
    elif page == "Products":
        show_products()

def show_products():
    st.header("Our Products")
    products = {
        "Corsant colposcopy software": {
            "description": "Visualization of colposcopy studies and report pdf generation",
            "download": "https://drive.google.com/uc?export=download&id=1AEG4gVJm3A701bKEFZ-sfVNoBVZEVBE1"
        },
    }
    
    for product, details in products.items():
        with st.expander(product):
            st.write(details["description"])
            st.image("./images/Entrada_video.png", use_container_width=True)
            st.write("After aquiring the images, the software will generate a pdf report like the one below.")
            st.image("./images/pdf1.png", use_container_width=True)
            st.write("You can also configure user information and preferences, as shown below.")
            st.image("./images/Usuario.png", use_container_width=True)
            st.image("./images/Preferencias.png", use_container_width=True)
            st.write("To download the software, click the link below.")
            st.markdown(f"[Download Here]({details['download']})")

if __name__ == "__main__":
    main()
