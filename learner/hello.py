from sqlalchemy import create_engine, Column, INT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建基类，返回一个定制的metaclass 类
Base = declarative_base()


# 自定义类
class Student(Base):
    # 表名
    __tablename__ = 'student'
    # 字段映射
    id = Column('id', INT, primary_key=True)
    name = Column('name', VARCHAR)
    code = Column('code', VARCHAR)
    sex = Column('sex', VARCHAR)

    def to_dict(self):
        """
        将查询的结果转化为字典类型
        Student 对象的内容如下 {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x10174c898>, 'sex': 'nan', 'name': 'ygh', 'code': 'AU', 'school': 'hua'}
        获取其值剔除 "_sa_instance_state 即可。但不能在self.__dict__上直接删除”_sa_instance_state” 这个值是公用的。
        :return:
        """
        return {k: v for k, v in self.__dict__.items() if k != "info"}


# 创建引擎 , echo=True ,表示需要开启 sql 打印，调试的以后特别好用
engine = create_engine("mysql://root:123456@127.0.0.1:3306/test", pool_size=2, max_overflow=0,
                       echo=True)  # 创建会话对象，用于操作数据库
Session = sessionmaker(bind=engine)
session = Session()

# 案例二： 全部查询
result = session.query(Student).all()
for i in result:
    # i是一个Student对象，所以可以使用其 to_dict() 去格式化其对象的值
    if isinstance(i, Student):
        print(i.to_dict())

# 案例三： 部分字段查询
result = session.query(Student.id, Student.name).all()
for i in result:
    # 此时返回的是一个tuple ,而不是一个Student对象
    print(i)

# 案例四：多条件查询, or_ , and_
result = session.query(Student).filter(or_(Student.name == "Bob", Student.sex != "aa")).first()
print(result.to_dict())

result = session.query(Student).filter(and_(Student.name == "Bob", Student.sex != "aa")).first()
print(result.to_dict())
