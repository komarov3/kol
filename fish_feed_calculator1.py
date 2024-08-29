import streamlit as st

def calculate_pearsons_square(feed1_protein, feed2_protein, feed3_protein, desired_protein, final_weight):
  """
  Calculates the proportions of three feeds needed to achieve a desired protein content
  using Pearson's Square method, considering the final weight.

  Args:
    feed1_protein: Protein content of feed 1 (as a percentage).
    feed2_protein: Protein content of feed 2 (as a percentage).
    feed3_protein: Protein content of feed 3 (as a percentage).
    desired_protein: Target protein content of the final feed (as a percentage).
    final_weight: Desired weight of the final feed (in kg or any consistent unit).

  Returns:
    A dictionary containing the proportions of each feed needed (in the same unit as final_weight).
  """

  # Calculate differences for Pearson's Square
  diff1 = abs(desired_protein - feed1_protein)
  diff2 = abs(desired_protein - feed2_protein)
  diff3 = abs(desired_protein - feed3_protein)

  # Calculate proportions (parts)
  total_parts = diff1 + diff2 + diff3
  part1 = (diff2 + diff3) / total_parts
  part2 = (diff1 + diff3) / total_parts
  part3 = (diff1 + diff2) / total_parts

  # Calculate weights based on final weight
  weight1 = part1 * final_weight
  weight2 = part2 * final_weight
  weight3 = part3 * final_weight

  return {
      "Feed 1": weight1,
      "Feed 2": weight2,
      "Feed 3": weight3
  }

# Streamlit app
st.title("Fish Feed Ratio Calculator (Pearson's Square)")

# Input fields
feed1_protein = st.number_input("Protein content of Feed 1 (%)", min_value=0.0, max_value=100.0, value=30.0)
feed2_protein = st.number_input("Protein content of Feed 2 (%)", min_value=0.0, max_value=100.0, value=40.0)
feed3_protein = st.number_input("Protein content of Feed 3 (%)", min_value=0.0, max_value=100.0, value=50.0)
desired_protein = st.number_input("Desired protein content (%)", min_value=0.0, max_value=100.0, value=35.0)
final_weight = st.number_input("Desired final weight (kg)", min_value=0.0, value=100.0)

# Calculate button
if st.button("Calculate"):
  result = calculate_pearsons_square(feed1_protein, feed2_protein, feed3_protein, desired_protein, final_weight)

  # Display results
  st.write("**Calculated Feed Ratios:**")
  for feed, weight in result.items():
    st.write(f"{feed}: {weight:.2f} kg")

