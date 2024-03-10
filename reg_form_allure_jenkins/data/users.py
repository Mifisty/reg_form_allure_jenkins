import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number: int
    birth_month: str
    birth_year: int
    birth_day: int
    subjects: str
    subjects2: str
    hobbies: str
    address: str
    state: str
    city: str


student = User(
    first_name='Evgenii',
    last_name='Mif',
    email='email@mail.ru',
    gender='Male',
    number=9123456789,
    birth_month='August',
    birth_year=1985,
    birth_day=22,
    subjects='Maths',
    subjects2='English',
    hobbies='Sports',
    address='Earth',
    state='Haryana',
    city='Panipat'
)
