import re

def reg_deal(pattern_list, text, func_dict=None):
    if func_dict is None:
        func_dict = {}
    for pattern in pattern_list:
        match_obj = re.match(pattern, text)
        if match_obj:
            #动态替换取出来的key值，get函数获取字典对应的键值，没有就返回默认设置的lambda x: x，此处不能为默认v,需要写匿名函数，可调用
            return {k: func_dict.get(k, lambda x: x)(v) for k, v in match_obj.groupdict().items()}
            # return {k: v for k, v in match_obj.groupdict().items()}

def test_reg():
    #匹配含有email的日志行
    # email_pattern = "(?P<Time>\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})\s*\[(?P<LogLevel>INFO)\]\s*.*:(?P<IP>(\d{1," \
    #                 r"3}\.){3}\d{1,3}).*:(?P<Email>\w+@\w+\.\w+)\D*(?P<status>\d+)\D*(?P<data_size>\d+)KB"
    email_pattern = r"(?P<Time>\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})\s*\[(?P<LogLevel>INFO)\]\s*.*:(?P<IP>(\d{1," \
                    r"3}\.){3}\d{1,3}).*:(?P<Email>\w+@\w+.\w+)\D*(?P<status>\d+)\D*(?P<data_size>\d+)KB"
    #匹配含有phone的日志行
    phone_pattern = "(?P<Time>\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})\s*\[(?P<LogLevel>INFO)\]\s*.*:(?P<IP>(\d{1," \
                    r"3}\.){3}\d{1,3}).*:(?P<Phonenum>((\+|00)86)?1[3-9]\d{9})\D*(?P<status>\d+)\D*(?P<data_size>\d+)KB"
    #匹配含有警告信息的日志行
    warn_pattern = "(?P<Time>\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})\s*\[(?P<LogLevel>WARN)\]\s*.*:(?P<IP>(\d{1," \
                   r"3}\.){3}\d{1,3}).*"
    #匹配还有错误信息的日志行
    error_pattern = "(?P<Time>\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}:\d{2})\s*\[(?P<LogLevel>ERROR)\]\s*(?P<ERROR_Message>.*)"
    pattern_list = [email_pattern, phone_pattern, warn_pattern, error_pattern]
    status_dict = {
        '1': 'Sucess',
        '2': 'Fail'
    }
    func_dict = {
        'status': lambda x: status_dict[x],
        'data_size': lambda x: int(x) / 1024
    }
    result_list = []
    with open(r'../logs/logcontent.log', 'r', encoding='utf-8') as f:
        for data in f:
            result_dict = reg_deal(pattern_list, data, func_dict)
            print("=========:",result_dict)
            result_list.append(result_dict)
    print(result_list)

if __name__ == '__main__':
    pass