from eval_dataset import dataset

def hit_at_k(results, target):
    for r in results:
        if target in r:
            return 1
    return 0

def recall_at_k(results, target):
    if target in results:
        return 1
    return 0

def retrieve(query):
    # 模拟检索过程，返回top-3结果
    mock_results = {
        "What is artificial intelligence?": [
            "Artificial Intelligence simulates human intelligence.",
            "AI is a branch of computer science.",
            "Machine learning is a subset of AI."
        ],
        "What is machine learning?": [
            "Machine learning is a subset of AI.",
            "ML algorithms learn from data.",
            "Deep learning is a subset of machine learning."
        ],
        "What is deep learning?": [
            "Deep learning uses neural networks.",
            "DL is a subset of machine learning.",
            "Neural networks have multiple layers."
        ],
        "What is natural language processing?": [
            "NLP deals with human language.",
            "Natural language processing is a field of AI.",
            "NLP enables computers to understand text."
        ],
        "What is computer vision?": [
            "Computer vision enables machines to see.",
            "CV is a field of AI.",
            "Computer vision processes images."
        ]
    }
    return mock_results.get(query, [])

def evaluate(dataset):
    hits = 0
    recalls = 0
    
    for item in dataset:
        query = item["query"]
        target = item["relevant_doc"]
        results = retrieve(query)
        
        # 可视化输出
        print("Query:", query)
        print("Retrieved:", results)
        print("Target:", target)
        print()
        
        hits += hit_at_k(results, target)
        recalls += recall_at_k(results, target)
    
    hit_score = hits / len(dataset)
    recall_score = recalls / len(dataset)
    
    return hit_score, recall_score

if __name__ == "__main__":
    hit_score, recall_score = evaluate(dataset)
    print("Hit@3:", round(hit_score, 2))
    print("Recall@3:", round(recall_score, 2))
