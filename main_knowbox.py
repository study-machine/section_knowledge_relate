# coding=utf8
from datetime import datetime

from tiku_orm.knowbox_model import *
import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(levelname)s %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    filename='relate_sect-know-{}.log'.format(datetime.now().strftime('%y-%m-%dT%H:%M:%S')),
    filemode='w')


class FlushSectionKnowledge(object):
    def __init__(self):
        self.count = 0
        self.assist_list = Assist.get_assists_by_type(118)
        self.section_list = self.get_section_list()

    def get_section_list(self):
        s_list = []
        for assist in self.assist_list:
            s_list += Section.get_sections_by_aid_level(assist.assist_id, 3)
        return s_list

    def run(self):
        for section in self.section_list:
            log.debug('找到章节{}'.format(section))
            section_knowledge_id_list = []
            self.get_section_knowledge_id_list(section.section_id, section_knowledge_id_list)
            section_knowledge_id_set = set(section_knowledge_id_list)
            self.write_relate_section_knowledge(section, section_knowledge_id_set)

    def get_section_knowledge_id_list(self, section_id, section_knowledge_id_list):
        questions = QuestionNew.get_questions_by_section(section_id)
        for question in questions:
            log.debug('找到题目{}'.format(question))
            knowledges = Knowledge.get_knowledge_by_q_id(question.question_id)
            question_knowledge_id_list = [k.know_id for k in knowledges]
            log.debug('找到题目对应的KnowIDs{}'.format(question_knowledge_id_list))
            section_knowledge_id_list.extend(question_knowledge_id_list)

    def write_relate_section_knowledge(self, section, k_id_set):
        k_id_list = list(k_id_set)
        for k_id in k_id_list:
            section.write_relate_section_knowledge(k_id)
            log_text = 'Insert into relate section_id:{} and know_id:{}'.format(section.section_id, k_id)
            log.info(log_text)
            print log_text
            self.count += 1


if __name__ == '__main__':
    start = datetime.now()
    f = FlushSectionKnowledge()
    f.run()
    end = datetime.now()
    td = end - start
    log_text = 'finish spend: {} s,insert: {}'.format(td.total_seconds(), f.count)
    print log_text
    log.info(log_text)
