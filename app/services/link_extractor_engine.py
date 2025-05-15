from newspaper import Article

def extract_content_from_url(url: str) -> dict:
    """
    Recebe uma URL e retorna um dicionário com título e texto principal da página.
    """
    try:
        article = Article(url, language='pt')
        article.download()
        article.parse()
        

        # Texto com quebra de parágrafos
        raw_text = article.text

        # Limpa múltiplas quebras de linha e espaços extras
        clean_text = ' '.join(raw_text.split())

        return {
            "title": article.title,
            "text": clean_text
        }

    except Exception as e:
        raise RuntimeError(f"Erro ao extrair conteúdo da URL: {str(e)}")
