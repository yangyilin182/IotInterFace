
class Configini:
    def __init__(self, file_path):
        self.file_path = file_path
        # 文件内容列表，每个元素为一个字典，格式为{"type":TYPE_XX, "section":"XX", "option":"XXX", "value":"XXX"}
        self.file_data = []

    '''
        读取配置文件，直接读取ini文件内容
    '''
    def read(self):
        self.file_data.clear()
        dataList = []
        try:
            f = open(self.file_path, 'r')
            dataList = f.readlines()
        finally:
            f.close()

        # 解析成列表
        section_temp = ""
        for dataline in dataList:
            dataline = dataline.strip()
            data = {"section": "", "option": "", "value": ""}
            if dataline[0:1] == "#" or dataline[0:1] == ";":
                data["value"] = dataline
            elif dataline[0:1] == "[":
                data["section"] = dataline[1:-1].strip()
                section_temp = data["section"]
            elif dataline.find("=") != -1:
                data["section"] = section_temp
                data["option"] = dataline[:dataline.find("=")].strip()
                data["value"] = dataline[dataline.find("=") + 1:].strip()
            else:
                data["value"] = dataline
            self.file_data.append(data)
        return

    '''
        获取ini文件内所有的section，以列表形式返回['logging', 'mysql']
    '''
    def sections(self):
        section_list = []
        for data_dic in self.file_data:
            section = data_dic["section"]
            if section != "" and section not in section_list:
                section_list.append(data_dic["section"])
        return section_list

    '''
        获取指定sections下所有options ，以列表形式返回['host', 'port', 'user', 'password']
    '''
    def options(self, sections):
        option_list = []
        for data_dic in self.file_data:
            if data_dic["section"] == sections and data_dic["option"] != "" and data_dic["value"] != "":
                option_list.append(data_dic["option"])
        return option_list

    '''
        获取指定section下所有的键值对，[('host', '127.0.0.1'), ('port', '3306'), ('user', 'root'), ('password', '123456')]
    '''
    def items(self, section):
        value_list = []
        for data_dic in self.file_data:
            if data_dic["section"] == section and data_dic["option"] != "" and data_dic["value"] != "":
                value_list.append((data_dic["option"], data_dic["value"]))
        return value_list

    '''
        获取section中option的值，返回为string类型
    '''
    def get(self, section, option):
        # 先读取一下
        self.read()

        for data_dic in self.file_data:
            if data_dic["section"] == section and data_dic["option"] == option:
                return data_dic["value"]
        return ""

    '''
        设置section中option的值
    '''
    def set(self, section, option, value):
        # 先读取一下
        self.read()

        for data_dic in self.file_data:
            if data_dic["section"] == section and data_dic["option"] == option:
                data_dic["value"] = value
                break

        # 保存文件
        with open(self.file_path, "w") as f:
            for data_dic in self.file_data:
                section = data_dic["section"]
                option = data_dic["option"]
                value = data_dic["value"]
                if section == "" and value != "":   # 这种情况为注释，直接写文件即可
                    f.write(value)
                elif section != "" and option == "":    # 这种情况为section的定义，写文件需要添加括号
                    f.write("[" + section + "]")
                elif section != "" and option != "":    # 这种情况为option的键值对
                    f.write(option + " = " + value)
                else:
                    f.write("\n")
                    continue
                f.write("\n")
        f.close()
        return
