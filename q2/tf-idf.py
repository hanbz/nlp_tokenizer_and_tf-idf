import jieba.analyse

f_token = open('../q1/output.txt', 'r')
f_output = open('output.txt', 'w')

for line in f_token.readlines():
    keywords = jieba.analyse.extract_tags(line, topK=0, withWeight=True)
    f_output.write(line)
    for item in keywords:
        f_output.write(item[0] + " : [" + str(item[1]) + "]\n")
    f_output.write("\n")
