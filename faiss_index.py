import faiss
import numpy as np

class FAISSIndex:
    def __init__(self, dimension):
        """
        初始化FAISS索引
        :param dimension: 嵌入向量维度
        """
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []
    
    def add(self, embeddings, documents):
        """
        添加嵌入向量和对应文档
        :param embeddings: 嵌入向量列表
        :param documents: 文档列表
        """
        self.index.add(np.array(embeddings))
        self.documents.extend(documents)
    
    def search(self, query_embedding, k=3):
        """
        搜索相似文档
        :param query_embedding: 查询嵌入向量
        :param k: 返回结果数量
        :return: 相似文档列表
        """
        distances, indices = self.index.search(np.array([query_embedding]), k)
        results = []
        for i in indices[0]:
            if i < len(self.documents):
                results.append(self.documents[i])
        return results
