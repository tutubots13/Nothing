{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPlWk4/tS6oOClLEEPuKBZi",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/tutubots13/Nothing/blob/main/dictionary%2Band%2Bfor_loop%2Bwith%2Binput.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kU-i4lrA6P-N",
        "outputId": "e30b49fb-150d-4ca9-a8f9-a325cc7f0e11"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ticket ID: 324124\n",
            "Issue Type: agent offline\n",
            "=== Ticket Details ===\n",
            "Ticket ID: 324124 (Type: str)\n",
            "Issue Type: agent offline (Type: str)\n",
            "Priority Level: 1 (Type: str)\n",
            "Estimated Resolution Time (minutes): 270.0 (Type: float)\n",
            "Customer Feedback Score: 4.8 (Type: float)\n",
            "\n",
            "Average Score: 2.9\n"
          ]
        }
      ],
      "source": [
        "\n",
        "# original\n",
        "'''\n",
        "ticket_ID = int(\"12345\")\n",
        "issue_Type = str(\"Network Down\")\n",
        "priority_Level = str(\"1\")\n",
        "estinated_Resolution_Time = float(\"4.5\") * 60\n",
        "customer_Feedback_SCore = float(\"4.8\")\n",
        "devidents = 2\n",
        "\n",
        "print(f\"Ticket ID: {ticket_ID}, Type: {type(ticket_ID).__name__}\")\n",
        "print(f\"Issue Type: {issue_Type}, Type: {type(issue_Type).__name__}\")\n",
        "print(f\"Priority Level: {priority_Level}, Type: {type(priority_Level).__name__}\")\n",
        "print(f\"Estimated Resolution Time: {estinated_Resolution_Time} minutes, Type: {type(estinated_Resolution_Time).__name__}\")\n",
        "print(f\"Customer Feedback Score: {customer_Feedback_SCore}, Type: {type(customer_Feedback_SCore).__name__}\")\n",
        "\n",
        "average_Score = (float(priority_Level) + float(customer_Feedback_SCore)) / devidents\n",
        "\n",
        "# another way to output variable in strings is \"print(\"Average Score:\"+str(average_Score))\"\n",
        "print(f\"Average Score: {average_Score}\")\n",
        "\n",
        "\n",
        "'''\n",
        "\n",
        "\n",
        "# Data initialization\n",
        "ticket_data = {\n",
        "    \"Ticket ID\": input(\"Ticket ID: \"),\n",
        "    \"Issue Type\": input(\"Issue Type: \"),\n",
        "    \"Priority Level\": str(\"1\"),\n",
        "    \"Estimated Resolution Time (minutes)\": float(\"4.5\") * 60,\n",
        "    \"Customer Feedback Score\": float(\"4.8\")\n",
        "}\n",
        "\n",
        "# Print ticket details with types\n",
        "print(\"=== Ticket Details ===\")\n",
        "for key, value in ticket_data.items():\n",
        "    print(f\"{key}: {value} (Type: {type(value).__name__})\")\n",
        "\n",
        "# Calculate average score\n",
        "average_score = (float(ticket_data[\"Priority Level\"]) + ticket_data[\"Customer Feedback Score\"]) / 2\n",
        "print(f\"\\nAverage Score: {average_score}\")"
      ]
    }
  ]
}