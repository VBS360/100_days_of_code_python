class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

new_question = Question("ABCD","Self")
print(new_question.text, new_question.answer)