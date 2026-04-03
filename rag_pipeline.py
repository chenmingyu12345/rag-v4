from chunk import load_and_chunk
from embedding import EmbeddingModel
from faiss_index import FAISSIndex
from rerank import Reranker

class RAGPipeline:
    def __init__(self):
        """
        初始化RAG pipeline
        """
        self.embedder = EmbeddingModel()
        self.reranker = Reranker()
        self.index = None
    
    def build_index(self, file_path):
        """
        构建索引
        :param file_path: 文档文件路径
        """
        # 加载并分块
        chunks = load_and_chunk(file_path)
        
        # 生成嵌入
        embeddings = self.embedder.embed(chunks)
        
        # 构建FAISS索引
        dimension = len(embeddings[0])
        self.index = FAISSIndex(dimension)
        self.index.add(embeddings, chunks)
    
    def retrieve(self, query, k=3):
        """
        检索相关文档
        :param query: 查询文本
        :param k: 返回结果数量
        :return: 检索到的文档列表
        """
        if not self.index:
            raise ValueError("Index not built. Call build_index first.")
        
        # 生成查询嵌入
        query_embedding = self.embedder.embed_query(query)
        
        # FAISS检索
        results = self.index.search(query_embedding, k)
        
        # 重排序
        reranked_results = self.reranker.rerank(query, results)
        
        return reranked_results
