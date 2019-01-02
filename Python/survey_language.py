from survey import AnonymousSurvey

# Define a question, and made a survey
question = "What is your favorite video game?"
my_survey = AnonymousSurvey(question)

# Show the quesiton, and store the response to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit. ")

while True:
	response = input("\nGame: ")
	if response == 'q':
		break
	my_survey.store_response(response)
	
# Show the survey 
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

