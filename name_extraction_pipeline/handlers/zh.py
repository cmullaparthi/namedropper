import logging
import jieba

jieba.setLogLevel(logging.ERROR)

COMMON_CHINESE_SURNAMES = {
    "王", "李", "张", "刘", "陈", "杨", "赵", "吴", "周", "徐", "孙"
}

def get_first_name(name: str):
    name = name.strip()
    if not name:
        return {"first_name": "", "from_model": False, "confidence": 0.0}

    # Tokenize using jieba
    tokens = list(jieba.cut(name, HMM=True))
    
    if len(tokens) == 1 and len(tokens[0]) == 2:
        surname, given = tokens[0][0], tokens[0][1]
        confidence = 0.8 if surname in COMMON_CHINESE_SURNAMES else 0.6
        return {"first_name": given, "from_model": False, "confidence": confidence}

    if len(tokens) >= 2:
        surname = tokens[0]
        given = ''.join(tokens[1:])
        confidence = 0.8 if surname in COMMON_CHINESE_SURNAMES else 0.6
        return {"first_name": given, "from_model": False, "confidence": confidence}

    return {"first_name": name, "from_model": False, "confidence": 0.4}
