# Day 2 Assignment: Personal Expense Tracker
# In this assignment you’ll be building your own Personal Expense Tracker based on what we covered in the Day 2 
# session of the Python Bootcamp. This command-line app will help you track daily expenses with the following features:
# Requirements:

# 1. Add Expenses with categories.
# 2. View All Expenses and calculate your total spending.
# 3. Save Expenses to a text file for record-keeping.

# Submission Instructions:

# 1. Ensure that your code is clean and well-commented.
# 2. Upload your project to a public GitHub repository.
# 3. Submit your GitHub repository link in the assignment submission section on CipherSchools.

# Happy coding! 😎


import google.generativeai as genai
from datetime import datetime



def expenseTracker(lines): #function is for writing the data into a new file Expensetxt
    date = datetime.now().strftime("%Y-%m-%d")
    with open("Expenses.txt", 'a') as f:
       
        f.write(f"today's Date: {date}\nExpenses: \n") #not necessary but yeah it shows on which date you have purchase what
        for i, line in enumerate(lines, start=1):
            f.write(f"{i}: Rs.{line}\n")
            
    readExpense()
    
def readExpense(): #function to read the data from the Expense file
    with open("Expenses.txt", 'r') as f:
        s = ""
        lines = f.readlines()
        for line in lines:
            s+=line
    print("your data")
    print(s)
    userInput = int(input("Do you want to get advise for you total spend if yes then 1 otherwise 0:  "))
    if(userInput):
        AdviseForExpensesByGemini(s)
    else:
        print("thankyou for your time have a nice day boi boi!")
        
    
#this is a gemini model i have used it to make it interesting and as we know the world is dependent on AI and its a crucial technology to learn so why not yeah you can use your
#api key which is free interesting right!
#search GEMINI API KEY and generate your key and place it where i have written API_KEY  
#also if you dont want to try it you can just go with the read function it alsso works 
#Ai is just for fun 

#also i have not attached by API due to privacy reasons 

def AdviseForExpensesByGemini(prompt):
    try:
        
        """
        Install the Google AI Python SDK

        $ pip install google-generativeai
        """

        

        genai.configure(api_key="API_KEY") #api will be in some this for AJHdjsdkjasnd-AJSnjsdjka23132njd-ouashdjq2 you can find yours from gemini api key

        # Create the model
        generation_config = {
          "temperature": 1,
          "top_p": 0.95,
          "top_k": 64,
          "max_output_tokens": 8192,
          "response_mime_type": "text/plain",
        }

        model = genai.GenerativeModel(
          model_name="gemini-1.5-flash",
          generation_config=generation_config,
          # safety_settings = Adjust safety settings
          # See https://ai.google.dev/gemini-api/docs/safety-settings
        )

        chat_session = model.start_chat(
          history=[
          ]
        )

        response = model.generate_content([prompt+'''you have given a data for the exppense tracking now first is date then mobile data then electricity bill and other 
                                           charges and money saved advice the user how they should spend their beloved money and how to save it tell them in points well mannered soo they can learn '''])

        print(response.text)
    except Exception as e:
        return {"status":500, "message": "Something went wrong", "error": {e}}
    


#it should look like this 500,400,1200

UserInput = input("Please enter your expenses as Mobile expense, Electricty Bill, other expense, Money saved: ").split(",")

expenseTracker(UserInput)



    
            
        


