# Data initialization
ticket_data = {
    "Ticket ID": int("12345"),
    "Issue Type": str("Network Down"),
    "Priority Level": str("1"),
    "Estimated Resolution Time (minutes)": float("4.5") * 60,
    "Customer Feedback Score": float("4.8")
}

# Print ticket details with types
print("=== Ticket Details ===")
for key, value in ticket_data.items():
    print(f"{key}: {value} (Type: {type(value).__name__})")

# Calculate average score
average_score = (float(ticket_data["Priority Level"]) + ticket_data["Customer Feedback Score"]) / 2
print(f"\nAverage Score: {average_score}")
