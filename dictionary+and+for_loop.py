
# original
'''
ticket_ID = int("12345")
issue_Type = str("Network Down")
priority_Level = str("1")
estinated_Resolution_Time = float("4.5") * 60
customer_Feedback_SCore = float("4.8")
devidents = 2

print(f"Ticket ID: {ticket_ID}, Type: {type(ticket_ID).__name__}")
print(f"Issue Type: {issue_Type}, Type: {type(issue_Type).__name__}")
print(f"Priority Level: {priority_Level}, Type: {type(priority_Level).__name__}")
print(f"Estimated Resolution Time: {estinated_Resolution_Time} minutes, Type: {type(estinated_Resolution_Time).__name__}")
print(f"Customer Feedback Score: {customer_Feedback_SCore}, Type: {type(customer_Feedback_SCore).__name__}")

average_Score = (float(priority_Level) + float(customer_Feedback_SCore)) / devidents

# another way to output variable in strings is "print("Average Score:"+str(average_Score))"
print(f"Average Score: {average_Score}")


'''


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
