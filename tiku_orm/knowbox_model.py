# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 下午8:46
# @Author  : wxy
# @File    : knowbox_model.py

from base_field import *
from base_model import *


class Assist(BaseModel):
    def __init__(self, **kwargs):
        assist_id = IntegerField()
        name = StringField()
        type = IntegerField()
        summary = StringField()
        book_id = IntegerField()
        super(Assist, self).__init__(**kwargs)

    def __repr__(self):
        return '<教辅 id:{},name:{}>'.format(self.assist_id, self.name)

    @classmethod
    def get_assists_by_type(cls, q_type):
        sql = """
        select * from base_assist 
        where status=0 and online_status=2
        and type={};
        """.format(q_type)
        res = cls.select(sql)
        return [
            cls(
                assist_id=d['assist_id'],
                name=d['name'],
                type=d['type'],
                summary=d['summary'],
                book_id=d['book_id']
            ) for d in res
        ]


class Section(BaseModel):
    def __init__(self, **kwargs):
        section_id = IntegerField()
        name = IntegerField()
        summary = IntegerField()
        level = IntegerField()
        parent_id = IntegerField()
        order_num = IntegerField()
        section_order = IntegerField()
        assist_id = IntegerField()
        last = IntegerField()
        super(Section, self).__init__(**kwargs)

    def __repr__(self):
        return '<章节 id:{},name:{}>'.format(self.section_id, self.name)

    @classmethod
    def get_sections_by_aid_level(cls, a_id, level):
        sql = """
            SELECT * FROM base_course_section 
            WHERE status=0 and online_status=2 
            and assist_id={a_id} AND level={level};
            """.format(a_id=a_id, level=level)
        res = cls.select(sql)
        return [
            cls(
                section_id=d['section_id'],
                name=d['name'],
                summary=d['summary'],
                level=d['level'],
                parent_id=d['parent_id'],
                order_num=d['order_num'],
                section_order=d['section_order'],
                assist_id=d['assist_id'],
                last=d['last']
            ) for d in res
        ]

    def write_relate_section_knowledge(self, k_id):
        assert self.section_id
        sql = """
        INSERT INTO relate_section_knowledge (section_id,know_id) 
        VALUES ({section_id},{know_id});
        """.format(section_id=self.section_id, know_id=k_id)
        self.insert(sql)


class QuestionNew(BaseModel):
    def __init__(self, **kwargs):
        question_id = IntegerField()
        question = StringField()
        super(QuestionNew, self).__init__(**kwargs)

    def __repr__(self):
        return '<题目 id:{},name:{}>'.format(self.question_id, self.question)

    @classmethod
    def get_questions_by_section(cls, s_id):
        sql = """
        select q.question_id,q.question from base_question as q 
        inner join relate_section_question as r on q.question_id=r.question_id
        where r.status=0 and r.online_status=2
        and q.status=0 and q.online_status=2
        and r.section_id={};
        """.format(s_id)
        res = cls.select(sql)
        return [
            cls(
                question_id=d['question_id'],
                question=d['question']
            ) for d in res
        ]


class Knowledge(BaseModel):
    def __init__(self, **kwargs):
        know_id = IntegerField()
        name = StringField()

        super(Knowledge, self).__init__(**kwargs)

    def __repr__(self):
        return '<知识点 id:{},name:{}>'.format(self.know_id, self.name)

    @classmethod
    def get_knowledge_by_q_id(cls, q_id):
        sql = """
        select k.know_id, k.name from base_knowledge_node as k 
        inner join relate_knowledge_question as r on k.know_id=r.know_id 
        where r.status=0 and r.online_status=2
        and k.status=0 and k.online_status=2
        and r.question_id={};
        """.format(q_id)
        res = cls.select(sql)
        return [
            cls(
                know_id=d['know_id'],
                name=d['name']
            ) for d in res
        ]
