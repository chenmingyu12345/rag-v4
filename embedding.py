from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """
        初始化嵌入模型
        :param model_name: 模型名称
        """
        self.model = SentenceTransformer(model_name)
    
    def embed(self, texts):
        """
        生成文本嵌入
        :param texts: 文本列表
        :return: 嵌入向量列表
        """
        return self.model.encode(texts)
    
    def embed_query(self, query):
        """
        生成查询嵌入
        :param query: 查询文本
        :return: 嵌入向量
        """
        return self.model.encode([query])[0]
