import os
import streamlit as st
import requests

class LowCarbRecipeConnection:
    def __init__(self, api_key):
        self.url = "https://low-carb-recipes.p.rapidapi.com"
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "low-carb-recipes.p.rapidapi.com"
        }

    def get_random_recipe(self):
        endpoint = "/random"
        response = requests.get(self.url + endpoint, headers=self.headers)
        return response.json() if response.status_code == 200 else None

    def get_recipe_by_id(self, recipe_id):
        endpoint = f"/recipes/{recipe_id}"
        response = requests.get(self.url + endpoint, headers=self.headers)
        return response.json() if response.status_code == 200 else None

def main():
    st.sidebar.title('Low Carb Recipe')

    # Add widgets in the sidebar
    option = st.sidebar.selectbox('Select Option', ['Random', 'Recommended'])

    st.title("Low Carb Recipe Randomizer")

    # Create the connection object and get the API key from GitHub Secrets
    api_key = os.getenv("API_KEY")
    connection = LowCarbRecipeConnection(api_key)

    if option == 'Random':
        # Get a random recipe
        recipe_data = connection.get_random_recipe()
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
            for recipestep in recipe_data["steps"]:
                st.write(f'Step{i}: {recipestep}')
                i += 1

    elif option == 'Recommended':
        # Get the ID of the previously fetched random recipe
        recommended_recipe_id = "2807982c-986a-4def-9e3a-153a3066af7a"

        if recommended_recipe_id:
            # Fetch the recommended recipe by ID
            recipe_data = connection.get_recipe_by_id(recommended_recipe_id)
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
                for recipestep in recipe_data["steps"]:
                    st.write(f'Step{i}: {recipestep}')
                    i += 1
        else:
            st.error("No recommended recipe found. Please try the 'Random' option first.")

    else:
        st.error("Invalid option selected. Please choose 'Random' or 'Recommended'.")

if __name__ == "__main__":
    main()
