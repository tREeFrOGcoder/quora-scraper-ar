from datasketch import MinHash, MinHashLSH
import re

def preprocess(text):
    text = text
    return text.split()

def create_minhash(shingles, num_perm=128):
    m = MinHash(num_perm=num_perm)
    for s in shingles:
        m.update(s.encode('utf8'))
    return m

def remove_duplicates_with_lsh(questions, threshold, num_perm):
    num_perm = num_perm
    threshold = threshold
    
    lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)
    
    unique_questions = {}
    duplicates = {}
    
    for i, question in enumerate(questions):
        shingles = preprocess(question)
        minhash = create_minhash(shingles, num_perm)
        
        # 查询相似的问题
        result = lsh.query(minhash)
        
        if len(result) == 0:
            # 如果没有找到相似项，添加到 LSH 和唯一问题列表中
            lsh.insert(i, minhash)
            unique_questions[i] = question
        else:
            # 如果找到了相似项，标记为重复
            duplicates[i] = result
            
    return unique_questions, duplicates




def main(file, threshold, perm):
    with open(file, "r") as infile:
        arabic_questions = infile.read().split("\n")

    # 执行去重，并设置精度控制参数为 0.8
    unique_questions, duplicates = remove_duplicates_with_lsh(arabic_questions, threshold, perm)

    with open(f"cleaned_{file}", "w") as outfile:
        for key, value in unique_questions.items():
            outfile.write(f"{value}\n")

    # print("Unique Questions:", list(unique_questions.values()))
    # print("Duplicates:", duplicates)
    # print("Unique Questions:")
    # for key, value in unique_questions.items():
    #     print(key, value)




main("combined_ar_questions.txt", 0.8, 128)



