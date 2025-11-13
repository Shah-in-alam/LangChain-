from pydantic import BaseModel, EmailStr,Field
from typing import Optional


class Student(BaseModel):
    name: str ='Shahin'
    age: Optional[int] = None
    email: EmailStr
    cgpa:float=Field(default=3.5,ge=0.0,le=4.0)



new_student ={"age": 32,'cpga':3.8,'email':'abc@gmail.com'}

student=Student(**new_student)
student_dict=dict(student)
student_json=student.model_dump_json()
print(type(student))

print(student_dict['age'])
print(student_json)