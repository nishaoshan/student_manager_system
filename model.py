"""
模型层
"""
class StudentModel:
    """
        学生模型:封装数据
    """

    def __init__(self, name="", sex="", age=0, score=0, sid=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
        self.sid = sid  # 对信息的唯一标识