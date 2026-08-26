import streamlit as st 
import httpx


def main():
    st.markdown("# PokeDash")

    stats = httpx.get("http://127.0.0.1:8000/pokemons/stats", timeout=30)
    st.write(stats)

if __name__ == "__main__":
    main()