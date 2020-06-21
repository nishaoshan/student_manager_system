"""
业务逻辑层
"""

from model import StudentModel
from typing import List


class StudentController:
    """
        学生逻辑控制:负责处理核心业务逻辑
    """

    def __init__(self):
        self.__list_students = []  # type:List[StudentModel]
        self.__start_id = 1001

    @property
    def list_students(self):
        return self.__list_students

    def add_student(self, stu):
        """

        :param stu:
        :return:
        """
        stu.sid = self.__start_id
        self.__start_id += 1  # 学生编号自增长
        self.__list_students.append(stu)

    def remove_student(self, sid) -> bool:
        """

        :param sid:
        :return:
        """
        for i in range(len(self.list_students)):
            if self.list_students[i].sid == sid:
                del self.list_students[i]
                return True  # 删除成功
        return False  # 删除失败
