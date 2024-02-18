from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]                            #
    question_answer = question["answer"]                        #define vaiables which will be used for object attributes later
    new_question = Question(question_text, question_answer)     #create new object
    question_bank.append(new_question)                          #add the created object to the list

#print(question_data[0]["text"])
print(question_bank[0].text)                                    # don't forget to use the methods from the objects!
