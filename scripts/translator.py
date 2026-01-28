#!/usr/bin/env python3
"""
Script para traduzir paginas HTML do site de teoria musical
"""

import os
import re
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
from music_terms import MUSIC_TERMS

INPUT_DIR = Path(__file__).parent.parent / "original"
OUTPUT_DIR = Path(__file__).parent.parent / "pt-br"

# Lista de elementos que contem texto para traduzir
TEXT_ELEMENTS = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'td', 'th', 'span', 'a', 'div', 'figcaption', 'label', 'button']

# Classes/IDs que nao devem ser traduzidos (codigo, formulas matematicas, etc.)
SKIP_CLASSES = ['process-math', 'MathJax', 'code', 'codenumber', 'ptx-navbar', 'searchbox']
SKIP_IDS = ['latex-macros', 'ptx-navbar']


def should_translate_element(element):
    """Verifica se o elemento deve ser traduzido"""
    # Nao traduzir se for script, style, code, etc.
    if element.name in ['script', 'style', 'code', 'pre', 'math', 'svg']:
        return False

    # Verificar classes que devem ser puladas
    classes = element.get('class', [])
    if any(skip in classes for skip in SKIP_CLASSES):
        return False

    # Verificar IDs que devem ser pulados
    elem_id = element.get('id', '')
    if elem_id in SKIP_IDS:
        return False

    return True


def translate_text(text):
    """Traduz um texto usando o dicionario de termos"""
    if not text or not text.strip():
        return text

    result = text

    # Ordenar termos por tamanho (maior primeiro) para evitar substituicoes parciais
    sorted_terms = sorted(MUSIC_TERMS.items(), key=lambda x: len(x[0]), reverse=True)

    for eng, pt in sorted_terms:
        # Usar regex para substituir apenas palavras completas
        pattern = r'\b' + re.escape(eng) + r'\b'
        result = re.sub(pattern, pt, result)

    return result


def translate_html_file(input_path, output_path):
    """Traduz um arquivo HTML"""
    with open(input_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Atualizar atributo lang
    html_tag = soup.find('html')
    if html_tag:
        html_tag['lang'] = 'pt-BR'

    # Traduzir titulo da pagina
    title_tag = soup.find('title')
    if title_tag and title_tag.string:
        title_tag.string = translate_text(title_tag.string)

    # Traduzir meta tags
    for meta in soup.find_all('meta', {'property': True}):
        if meta.get('content'):
            meta['content'] = translate_text(meta['content'])

    # Traduzir conteudo de texto
    for element in soup.find_all(TEXT_ELEMENTS):
        if not should_translate_element(element):
            continue

        for child in element.children:
            if isinstance(child, NavigableString) and not isinstance(child, (type(soup.new_string('')).__class__.__bases__[0] if hasattr(type(soup.new_string('')), '__bases__') else type(None))):
                if child.string and child.string.strip():
                    translated = translate_text(str(child))
                    child.replace_with(translated)

    # Salvar arquivo traduzido
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    return True


def translate_all():
    """Traduz todos os arquivos HTML"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    html_files = list(INPUT_DIR.glob('*.html'))
    total = len(html_files)

    print(f"Traduzindo {total} arquivos...")

    for i, input_path in enumerate(html_files, 1):
        output_path = OUTPUT_DIR / input_path.name
        print(f"[{i}/{total}] {input_path.name}")

        try:
            translate_html_file(input_path, output_path)
        except Exception as e:
            print(f"  ERRO: {e}")

    print(f"\nTraducao concluida! Arquivos salvos em {OUTPUT_DIR}")


if __name__ == "__main__":
    translate_all()
