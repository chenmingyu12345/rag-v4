def chunk_text(text, chunk_size=500, overlap=100):
    """
    将文本分块
    :param text: 输入文本
    :param chunk_size: 块大小
    :param overlap: 重叠大小
    :return: 分块后的文本列表
    """
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    
    return chunks

def load_and_chunk(file_path):
    """
    加载文件并分块
    :param file_path: 文件路径
    :return: 分块后的文本列表
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    return chunk_text(text)
