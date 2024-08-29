import streamlit as st

def calculate_pearsons_square(feed1_protein, feed2_protein, feed3_protein, desired_protein, final_weight):
    """
    Calculates the proportions of feeds needed to achieve a desired protein content
    using Pearson's Square method, considering the final weight.

    Args:
        feed1_protein: Protein content of feed 1 (as a percentage).
        feed2_protein: Protein content of feed 2 (as a percentage).
        feed3_protein: Protein content of feed 3 (as a percentage), optional.
        desired_protein: Target protein content of the final feed (as a percentage).
        final_weight: Desired weight of the final feed (in kg or any consistent unit).

    Returns:
        A dictionary containing the weights of each feed needed to sum up to final_weight.
    """
    explanations = []
    
    if feed3_protein is None:
        diff1 = abs(desired_protein - feed1_protein)
        diff2 = abs(desired_protein - feed2_protein)
        explanations.append(f"Difference for Feed 1: |{desired_protein} - {feed1_protein}| = {diff1}")
        explanations.append(f"Difference for Feed 2: |{desired_protein} - {feed2_protein}| = {diff2}")

        total_parts = diff1 + diff2
        explanations.append(f"Total parts (sum of differences): {diff1} + {diff2} = {total_parts}")

        part1 = diff2 / total_parts
        part2 = diff1 / total_parts
        explanations.append(f"Proportion of Feed 1: {diff2} / {total_parts} = {part1:.2f}")
        explanations.append(f"Proportion of Feed 2: {diff1} / {total_parts} = {part2:.2f}")

        weight1 = part1 * final_weight
        weight2 = part2 * final_weight
        explanations.append(f"Weight of Feed 1: {part1:.2f} * {final_weight} kg = {weight1:.2f} kg")
        explanations.append(f"Weight of Feed 2: {part2:.2f} * {final_weight} kg = {weight2:.2f} kg")

        total_weight = weight1 + weight2
        weight1 = (weight1 / total_weight) * final_weight
        weight2 = (weight2 / total_weight) * final_weight
        explanations.append(f"Adjusted weight of Feed 1: {weight1:.2f} kg")
        explanations.append(f"Adjusted weight of Feed 2: {weight2:.2f} kg")

        return {
            "Feed 1": weight1,
            "Feed 2": weight2,
            "explanations": explanations
        }
    else:
        diff1 = abs(desired_protein - feed1_protein)
        diff2 = abs(desired_protein - feed2_protein)
        diff3 = abs(desired_protein - feed3_protein)
        explanations.append(f"Difference for Feed 1: |{desired_protein} - {feed1_protein}| = {diff1}")
        explanations.append(f"Difference for Feed 2: |{desired_protein} - {feed2_protein}| = {diff2}")
        explanations.append(f"Difference for Feed 3: |{desired_protein} - {feed3_protein}| = {diff3}")

        total_parts = diff1 + diff2 + diff3
        explanations.append(f"Total parts (sum of differences): {diff1} + {diff2} + {diff3} = {total_parts}")

        part1 = (diff2 + diff3) / total_parts
        part2 = (diff1 + diff3) / total_parts
        part3 = (diff1 + diff2) / total_parts
        explanations.append(f"Proportion of Feed 1: ({diff2} + {diff3}) / {total_parts} = {part1:.2f}")
        explanations.append(f"Proportion of Feed 2: ({diff1} + {diff3}) / {total_parts} = {part2:.2f}")
        explanations.append(f"Proportion of Feed 3: ({diff1} + {diff2}) / {total_parts} = {part3:.2f}")

        weight1 = part1 * final_weight
        weight2 = part2 * final_weight
        weight3 = part3 * final_weight
        explanations.append(f"Weight of Feed 1: {part1:.2f} * {final_weight} kg = {weight1:.2f} kg")
        explanations.append(f"Weight of Feed 2: {part2:.2f} * {final_weight} kg = {weight2:.2f} kg")
        explanations.append(f"Weight of Feed 3: {part3:.2f} * {final_weight} kg = {weight3:.2f} kg")

        total_weight = weight1 + weight2 + weight3
        weight1 = (weight1 / total_weight) * final_weight
        weight2 = (weight2 / total_weight) * final_weight
        weight3 = (weight3 / total_weight) * final_weight
        explanations.append(f"Adjusted weight of Feed 1: {weight1:.2f} kg")
        explanations.append(f"Adjusted weight of Feed 2: {weight2:.2f} kg")
        explanations.append(f"Adjusted weight of Feed 3: {weight3:.2f} kg")

        return {
            "Feed 1": weight1,
            "Feed 2": weight2,
            "Feed 3": weight3,
            "explanations": explanations
        }

# Streamlit app
st.title("Fish Feeding Ratio Calculator")

# Feed options (common elements used in fish feeds)
feed_options = ["Fish Meal", "Soybean Meal", "Corn Gluten Meal", "Wheat Bran", "Rice Bran", "Cottonseed Meal", "Sunflower Meal"]

# Step 1: Select Feed 1
feed1 = st.selectbox("Select Feed 1", feed_options)

# Step 2: Update options for Feed 2 to exclude the selected Feed 1
feed_options_for_2 = [feed for feed in feed_options if feed != feed1]
feed2 = st.selectbox("Select Feed 2", feed_options_for_2)

# Step 3: Optionally include a third feed, updating options to exclude selected Feeds 1 and 2
feed3_option = st.checkbox("Include a third feed?")
if feed3_option:
    feed_options_for_3 = [feed for feed in feed_options if feed != feed1 and feed != feed2]
    feed3 = st.selectbox("Select Feed 3", feed_options_for_3)
else:
    feed3 = None

# Protein content input
feed1_protein = st.number_input(f"Protein content of {feed1} (%)", min_value=0.0, max_value=100.0, value=30.0)
feed2_protein = st.number_input(f"Protein content of {feed2} (%)", min_value=0.0, max_value=100.0, value=40.0)
if feed3_option:
    feed3_protein = st.number_input(f"Protein content of {feed3} (%)", min_value=0.0, max_value=100.0, value=50.0)
else:
    feed3_protein = None

# Desired protein content
desired_protein = st.number_input("Desired protein content (%)", min_value=0.0, max_value=100.0, value=35.0)

# Final weight
final_weight = st.number_input("Final weight of feed (kg)", min_value=0.0, value=100.0)

# Error handling for invalid input
if feed1_protein > desired_protein and feed2_protein > desired_protein and (feed3_protein is None or feed3_protein > desired_protein):
    st.error("All selected feeds have higher protein content than the desired value. Please choose different feeds or adjust the desired protein content.")
elif feed1_protein < desired_protein and feed2_protein < desired_protein and (feed3_protein is None or feed3_protein < desired_protein):
    st.error("All selected feeds have lower protein content than the desired value. Please choose different feeds or adjust the desired protein content.")
else:
    # Calculate and display results
    if st.button("Calculate"):
        result = calculate_pearsons_square(feed1_protein, feed2_protein, feed3_protein, desired_protein, final_weight)
        st.write("**Feeding Ratios:**")
        for feed, weight in result.items():
            if feed != "explanations":
                st.write(f"{feed}: {weight:.2f} kg")
        st.write("**Calculation Steps:**")
        for explanation in result["explanations"]:
            st.write(f"- {explanation}")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)