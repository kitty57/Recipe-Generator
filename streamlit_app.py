import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY")
model = genai.GenerativeModel(model_name="gemini-pro")
def generate_recipe(preference, ingredients,allergies):
    prompt = f'"As an experienced culinarian and as a person who not only knows a variety of dishes but can also cook them, Given the following list of ingredients, suggest a suitable recipe to cook. The ingredients: {", ".join(ingredients)}. The user has a preference for {preference} dishes, and he user is alergic to these ingredients:{allergies}."'
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("Recipe Generator")
    preference = st.selectbox("Select your preference:", ["vegetarian", "non-vegetarian","vegan"])
    ingredients_input = st.text_input("Enter ingredients separated by comma (e.g., onion, tomato, potato):")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    allergies=st.text_input("Do you have any allergies?(If None enter None):")
    
    if st.button("Generate Recipe"):
        recipe = generate_recipe(preference, ingredients,allergies)
        st.subheader("Generated Recipe")
        st.info(recipe)
        st.session_state.ingredients_input = ""
        st.session_state.preference = ""
        st.session_state.allergies=""

if __name__ == "__main__":
    if "ingredients_input" not in st.session_state:
        st.session_state.ingredients_input = ""
    if "preference" not in st.session_state:
        st.session_state.preference = ""
    if "allergies" not in st.session_state:
        st.session_state.allergies=""

    main()
