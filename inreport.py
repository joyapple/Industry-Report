# Developer Information:
# Name: [Joyapple]
# GitHub: [https://github.com/joyapple]

# Open Source Information:
# This code is open source and free to use, modify and distribute under the MIT License.

import openai
import json

# Input OpenAI API Key
openai.api_key = "You_OpenAI_API_Key"

# Define query function and add a parameter for length
def generate_report(keyword, report_type, length):
    # Validate input parameters
    if not keyword:
        raise ValueError("Please enter a keyword")
    if report_type not in ["Analysis", "Market Share", "Sales"]:
        raise ValueError("Please enter a valid report type (Analysis/Market Share/Sales)")
    if length <= 0:
        raise ValueError("Please enter a character limit greater than 0")

    # Choose OpenAI query model based on report type
    if report_type == "Market Share":
        model_name = "text-davinci-003"
        chapter = "##"
    elif report_type == "Analysis":
        model_name = "text-davinci-003"
        chapter = "##"
    elif report_type == "Sales":
        model_name = "text-davinci-003"
        chapter = "##"

    # Define input format and add character limit
    prompt = f"{chapter} Please write a '{keyword}' {report_type} report for me, with a character limit of {length}, and include professional and authoritative media reports."

    # Use OpenAI query model
    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        max_tokens=length,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Process OpenAI response
    report = response.choices[0].text.strip()

    # Return report data
    return report

# Input keyword, report type and character limit
keyword = input("Please enter a keyword: ")
report_type = input("Please enter a report type (Analysis/Market Share/Sales): ")
length = int(input("Please enter a character limit: "))

try:
    # Generate report
    report = generate_report(keyword, report_type, length)

    # Print report
    print(report)

    # Save report as md file
    with open(f"{keyword}_{report_type}.md", "w", encoding="utf-8") as f:
        # Add title and chapter
        if report_type == "Analysis":
            f.write(f"# {keyword} {report_type} Report\n")
        else:
            f.write(f"# {keyword} {report_type} Report\n\n")
        f.write(report.replace("##", "###"))
        print("Report saved as md file")
except ValueError as e:
    print(f"Parameter error: {e}")
