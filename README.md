# Mock Assignment ChatBot

The files my_assistant.py, my_tool.py, and my_main.py all build a mock chatbot assistant that helps you keep track of your assignment's deadlines. It is a mock chatbot because it provides pre-defined responses based on a select few queries rather than giving a unique response for every query passed through (it doesn't use generative AI). The requests which go through include 'major', 'schedule', 'registration', 'deadline', and 'due'. Major, schedule and registration all pass off the student to their advisor since those queries require consultation with an educational advisor. Deadline and due checks the message for an assignment ID and returns that assignment's deadline, if the assignment exists and if it has a deadline. If this tool used real student data, it would likely crash due to multiple courses having multiple similarly named/ID-ed assignments. In that case, the tool would also need to account for courses alongside deadlines.



## AI Attribution Statement
AI was not used at any point throughout this project.