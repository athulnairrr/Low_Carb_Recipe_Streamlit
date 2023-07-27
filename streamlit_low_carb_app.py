import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()
def get_api_key():
    return os.getenv("API_KEY")


def get_random_low_carb_recipe():
    url = "https://low-carb-recipes.p.rapidapi.com/random"
    headers = {
        "X-RapidAPI-Key": get_api_key(),
        "X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
    }
    tags = [
        "15-minute-meals", "beef-free", "breakfast", "chicken-free",
        "dairy-free", "desserts", "eggs", "fish-free", "gluten-free", "keto"
    ]
    params = {"tags": ",".join(tags)}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def get_low_carb_recipe_by_id():
    url = "https://low-carb-recipes.p.rapidapi.com/recipes/2807982c-986a-4def-9e3a-153a3066af7a"
    headers = {
        "X-RapidAPI-Key": "d55227a8f6mshcc8497c44392a08p15d4f6jsn6467ef680ddc",
        "X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
    }
    tags = [
        "15-minute-meals", "beef-free", "breakfast", "chicken-free",
        "dairy-free", "desserts", "eggs", "fish-free", "gluten-free", "keto"
    ]
    params = {"tags": ",".join(tags)}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    
    st.sidebar.title('Low Carb Recipe')

    # Add widgets in the sidebar
    option = st.sidebar.selectbox('Select Option', ['Random', 'Recommended'])
    

    st.title("Low Carb Recipe Randomizer")

    
    if option == 'Random':
        recipe_data = get_random_low_carb_recipe()
        if recipe_data:
            st.subheader("Recipe Name:")
            st.write(recipe_data["name"])

            st.subheader("Ingredients:")
            for ingredient in recipe_data["ingredients"]:
                name = ingredient.get("name", "")
                serving_size = ingredient["servingSize"].get("desc", "") if "servingSize" in ingredient else ""
                st.write(f"- {name} ({serving_size})")
            
            st.subheader("Recipe Step:")
            i = 1
            for recipesteps in recipe_data["steps"]:
                st.write(f'Step{i} : {recipesteps}')
                i += 1 
                
    elif option == 'Recommended':
        recipe_data = get_low_carb_recipe_by_id()
        if recipe_data and option[1] :
            st.subheader("Recipe Name:")
            st.write(recipe_data["name"])

            st.subheader("Ingredients:")
            for ingredient in recipe_data["ingredients"]:
                st.write(f"- {ingredient['name']} ({ingredient['servingSize']['desc']})")
            
            st.subheader("Recipe Step:")
            i = 1
            for recipesteps in recipe_data["steps"]:
                st.write(f'Step{i} : {recipesteps}')
                i += 1 
    else:
        st.error("Failed to retrieve a random low-carb recipe. Please try again later.")
    

if __name__ == "__main__":
    main()
