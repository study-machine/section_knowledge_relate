from tiku_orm.tiku_model import *


class FlushSectionKnowledge(object):
    def __init__(self):
        self.assist_list = Assist.get_assists_by_type(118)
        self.section_list = self.get_section_list()

    def get_section_list(self):
        s_list = []
        for assist in self.assist_list:
            s_list += Section.get_sections_by_aid_level(assist.TeachingAssistID, 3)
        return s_list


if __name__ == '__main__':
    f = FlushSectionKnowledge()
    print f.section_list