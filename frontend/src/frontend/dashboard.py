import streamlit as st 
import httpx
import os 

# try to get environment variable BACKEND_URL, if not exist default to 2nd argument
BASE_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


def main():
    st.markdown("# PokeDash")

    stats = httpx.get(f"{BASE_URL}/pokemons/stats", timeout=30).json()
    st.dataframe(stats)

if __name__ == "__main__":
    main()