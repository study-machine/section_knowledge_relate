# coding=utf8
import pymysql
from base_field import *
from base_model import *


class Assist(BaseModel):
    def __init__(self, **kwargs):
        TeachingAssistID = IntegerField()
        Name = StringField()
        Summary = StringField()
        AddTime = StringField()
        HasSection = IntegerField()
        JiaocaiID = IntegerField()
        IsPublic = IntegerField()
        QuestionType = IntegerField()
        IsDelete = IntegerField()
        OrderNum = IntegerField()
        Grade = IntegerField()
        Subject = IntegerField()
        super(Assist, self).__init__(**kwargs)

    def __repr__(self):
        return '<教辅 id:{},name:{}>'.format(self.TeachingAssistID, self.Name)

    @classmethod
    def get_assists_by_type(cls, q_type):
        sql = """
        SELECT * FROM wx_edu_teachingassist
        WHERE QuestionType={} AND IsDelete=0;
        """.format(q_type)
        res = cls.select(sql)
        return [
            cls(
                TeachingAssistID=d['TeachingAssistID'],
                Name=d['Name'],
                Summary=d['Summary'],
                AddTime=d['AddTime'],
                HasSection=d['HasSection'],
                JiaocaiID=d['JiaocaiID'],
                IsPublic=d['IsPublic'],
                QuestionType=d['QuestionType'],
                IsDelete=d['IsDelete'],
                OrderNum=d['OrderNum'],
                Grade=d['Grade'],
                Subject=d['Subject']
            ) for d in res
        ]


class Section(BaseModel):
    def __init__(self, **kwargs):
        CourseSectionID = IntegerField()
        SectionName = StringField()
        Summary = StringField()
        sLevel = IntegerField()
        ParentID = IntegerField()
        OrderNum = IntegerField()
        JiaoCaiID = IntegerField()
        SectionOrder = IntegerField()
        TeachingAssistID = IntegerField()
        Grade = IntegerField()
        Subject = IntegerField()
        IsDelete = IntegerField()
        Last = IntegerField()
        AddTime = IntegerField()
        QuestionType = IntegerField()
        super(Section, self).__init__(**kwargs)

    def __repr__(self):
        return '<章节 id:{},name:{}>'.format(self.CourseSectionID, self.SectionName)

    @classmethod
    def get_sections_by_aid_level(cls, a_id, level):
        sql = """
            SELECT CourseSectionID,SectionName,Summary,sLevel,ParentID,OrderNum,JiaoCaiID,
            SectionOrder,TeachingAssistID,Grade,Subject,IsDelete,Last,AddTime,QuestionType
            FROM wx_edu_coursesection WHERE TeachingAssistID={a_id} AND sLevel={level} and IsDelete=0;
                """.format(a_id=a_id, level=level)
        res = cls.select(sql)
        return [
            cls(
                CourseSectionID=d['CourseSectionID'],
                SectionName=d['SectionName'],
                Summary=d['Summary'],
                sLevel=d['sLevel'],
                ParentID=d['ParentID'],
                OrderNum=d['OrderNum'],
                JiaoCaiID=d['JiaoCaiID'],
                SectionOrder=d['SectionOrder'],
                TeachingAssistID=d['TeachingAssistID'],
                Grade=d['Grade'],
                Subject=d['Subject'],
                IsDelete=d['IsDelete'],
                Last=d['Last'],
                AddTime=d['AddTime'],
                QuestionType=d['QuestionType']
            ) for d in res
        ]

    def write_relate_section_knowledge(self, k_id):
        assert self.CourseSectionID
        sql = """
        INSERT INTO edu_relate_coursesection_knowledge (CourseSectionID,KnowID) 
        VALUES ({CourseSectionID},{KnowID});
        """.format(CourseSectionID=self.CourseSectionID, KnowID=k_id)
        self.insert(sql)


class QuestionNew(BaseModel):
    def __init__(self, **kwargs):
        QuestionID = IntegerField(),
        Question = StringField(),
        QuestionType = IntegerField(),
        AddTime = IntegerField(),
        RightAnswer = StringField(),
        AnswerExplain = StringField(),
        Options = StringField(),
        Level = IntegerField(),
        IsPublic = IntegerField(),
        Status = IntegerField(),
        QuestionAnalyze = StringField(),
        Grade = IntegerField(),
        Subject = IntegerField(),
        ShortQuestion = StringField()
        super(QuestionNew, self).__init__(**kwargs)

    def __repr__(self):
        return '<题目 id:{},name:{}>'.format(self.QuestionID, self.Question)

    @classmethod
    def get_questions_by_section(cls, s_id):
        sql = """
        select q.QuestionID,q.Question,q.QuestionType,q.AddTime,q.RightAnswer,q.AnswerExplain,
        q.Options,q.Level,q.IsPublic,q.Status,q.QuestionAnalyze,q.Grade,q.Subject,q.ShortQuestion
        from wx_edu_questions_new as q 
        inner join edu_relate_courseassistquestion as r
        on q.QuestionID=r.QuestionID
        where r.CourseSectionID={};
        """.format(s_id)
        res = cls.select(sql)
        return [
            cls(
                QuestionID=d['QuestionID'],
                Question=d['Question'],
                QuestionType=d['QuestionType'],
                AddTime=d['AddTime'],
                RightAnswer=d['RightAnswer'],
                AnswerExplain=d['AnswerExplain'],
                Options=d['Options'],
                Level=d['Level'],
                IsPublic=d['IsPublic'],
                Status=d['Status'],
                QuestionAnalyze=d['QuestionAnalyze'],
                Grade=d['Grade'],
                Subject=d['Subject'],
                ShortQuestion=d['ShortQuestion']
            ) for d in res
        ]


class Knowledge(BaseModel):
    def __init__(self, **kwargs):
        KnowID = IntegerField()
        KnowName = StringField()
        Summary = StringField()
        Level = IntegerField()
        ParentID = IntegerField()
        OrderNum = IntegerField()
        Subject = IntegerField()
        KnowOrder = IntegerField()
        QuestionCount = IntegerField()
        IsDelete = IntegerField()
        Last = IntegerField()
        QuestionType = IntegerField()
        super(Knowledge, self).__init__(**kwargs)

    def __repr__(self):
        return '<知识点 id:{},name:{}>'.format(self.KnowID, self.KnowName)

    @classmethod
    def get_knowledge_by_q_id(cls, q_id):
        sql = """
        select  k.KnowID, k.KnowName, k.Summary, k.Level, k.ParentID, k.OrderNum, k.Subject,
        k.KnowOrder, k.QuestionCount, k.IsDelete, k.Last, k.QuestionType 
        from wx_edu_knowledge as k 
        inner join edu_relate_knowledgequestion as r on k.KnowID=r.KnowID 
        where QuestionID={} and IsDelete=0;
        """.format(q_id)
        res = cls.select(sql)
        return [
            cls(
                KnowID=d['KnowID'],
                KnowName=d['KnowName'],
                Summary=d['Summary'],
                Level=d['Level'],
                ParentID=d['ParentID'],
                OrderNum=d['OrderNum'],
                Subject=d['Subject'],
                KnowOrder=d['KnowOrder'],
                QuestionCount=d['QuestionCount'],
                IsDelete=d['IsDelete'],
                Last=d['Last'],
                QuestionType=d['QuestionType']
            ) for d in res
        ]
