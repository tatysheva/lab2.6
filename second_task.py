if __name__ == '__main__':
    student = {
        1: 'anton',
        2: 'varvara',
        3: 'pavel',
        4: 'anna',
        5: 'igor',
        6: 'liza',
        7: 'dasha'
    }
    print(student)
    dict_items = student.items()
    new_student = dict(zip(student.values(), student.keys()))
    print(new_student)