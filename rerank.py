from sentence_transformers import CrossEncoder

class Reranker:
    def __init__(self, model_name='cross-encoder/ms-marco-MiniLM-L-6-v2'):
        """
        初始化重排序模型
        :param model_name: 模型名称
        """
        self.model = CrossEncoder(model_name)
    
    def rerank(self, query, documents):
        """
        对文档进行重排序
        :param query: 查询文本
        :param documents: 文档列表
        :return: 重排序后的文档列表
        """
        if not documents:
            return []
        
        # 创建查询-文档对
        pairs = [[query, doc] for doc in documents]
        
        # 计算相关性得分
        scores = self.model.predict(pairs)
        
        # 根据得分排序
        sorted_docs = [doc for _, doc in sorted(zip(scores, documents), key=lambda x: x[0], reverse=True)]
        
        return sorted_docs
