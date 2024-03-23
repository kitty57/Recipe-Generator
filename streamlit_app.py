import streamlit as st
import google.generativeai as genai

# Configure GenerativeAI
genai.configure(api_key="AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY")

# Initialize GenerativeModel
model = genai.GenerativeModel(model_name="gemini-pro")

# Define function to generate recipe
def generate_recipe(preference, ingredients):
    prompt = f'"As an experienced culinarian and as a person who not only knows a variety of dishes but can also cook them, Given the following list of ingredients, suggest a suitable recipe to cook. The ingredients: {", ".join(ingredients)}. The user has a preference for {preference} dishes."'
    response = model.generate_content(prompt)
    return response.text

# Streamlit app
def main():
    st.title("Recipe Generator")
    
    # User input
    preference = st.selectbox("Select your preference:", ["vegetarian", "non-vegetarian"])
    ingredients_input = st.text_input("Enter ingredients separated by comma (e.g., onion, tomato, potato):")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    
    # Generate recipe
    if st.button("Generate Recipe"):
        recipe = generate_recipe(preference, ingredients)
        st.subheader("Generated Recipe")
        st.markdown(recipe)

if __name__ == "__main__":
    main()
