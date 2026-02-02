#!/bin/bash
# Script para preparar arquivos para a Wiki do GitHub

echo "Preparando arquivos para a Wiki do GitHub..."

# Criar diretório wiki se não existir
mkdir -p wiki

# Copiar arquivos traduzidos
echo "Copiando arquivos traduzidos do pt-br/ para wiki/..."
cp -v pt-br/*.md wiki/

# Copiar arquivos de configuração da wiki
echo "Arquivos wiki criados!"

echo ""
echo "✓ Wiki preparada!"
echo ""
echo "Próximos passos:"
echo "1. Clone o repositório wiki:"
echo "   git clone https://github.com/pedrospdc/teoria-musical.wiki.git"
echo ""
echo "2. Copie os arquivos:"
echo "   cp wiki/* teoria-musical.wiki/"
echo ""
echo "3. Commit e push:"
echo "   cd teoria-musical.wiki"
echo "   git add -A"
echo "   git commit -m 'Adiciona conteúdo traduzido'"
echo "   git push"
