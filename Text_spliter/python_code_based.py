from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

from langchain_community.document_loaders import PyPDFLoader

text= """
class Student:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old."

    def study(self):
        return f"I am studying {self.subject}."


def create_students():
    students = []
    students.append(Student("Shahin", 23, "Data Science"))
    students.append(Student("Ayaan", 21, "Cyber Security"))
    students.append(Student("Sara", 22, "Artificial Intelligence"))
    return students


def print_student_info(students):
    for student in students:
        print(student.introduce())
        print(student.study())
        print("-" * 30)


def main():
    students = create_students()
    print_student_info(students)


if __name__ == "__main__":
    main()

"""
# Initialize the loader and load the document
spliter =RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)
# perform the splitting
result=spliter.split_text(text)
print(len(result))
print(result[2])