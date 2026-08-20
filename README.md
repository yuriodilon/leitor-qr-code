# 📷 Leitor de QR Code

Aplicativo desktop para ler QR Codes diretamente da tela, sem necessidade de abrir um botão manual de captura. Basta abrir o programa, selecionar a área desejada e o app identifica o QR automaticamente.

## ✅ Funcionalidades

- Seleção direta da tela com arraste do mouse
- Leitura automática de QR Code
- Abertura automática de links
- Copiar conteúdo para a área de transferência
- Interface leve e focada em uso rápido
- Executável gerado sem console para uso final

## 📋 Requisitos

- Windows 10/11
- Python 3.13+ para rodar a versão em código
- Biblioteca do projeto já listada em [requirements.txt](requirements.txt)

## 🚀 Como rodar em Python

1. Abra o terminal no diretório do projeto
2. Crie/ative o ambiente virtual
3. Instale as dependências:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

### Teste rápido sem gerar executável

Para validar a lógica do app sem rebuild do `.exe`:

```powershell
.\venv\Scripts\python.exe main.py
```

Se quiser abrir sem janela de terminal:

```powershell
.\venv\Scripts\pythonw.exe main.py
```

## 🧩 Como usar

1. Execute o programa
2. A aplicação entra imediatamente no modo de seleção
3. Arraste o mouse para marcar a área com o QR Code
4. Solte o mouse
5. O app identifica o QR e exibe o conteúdo
6. Se for um link, ele abre automaticamente
7. Você pode copiar o texto com um botão

## 📦 Estrutura do projeto

```text
leitor-qr-code/
├── main.py
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── qr_scanner.py
│   └── utils.py
├── dist/
│   └── QRCodeReader.exe
└── .gitignore
```

## 🏗️ Gerar executável

O app já foi configurado para gerar um executável sem janela de terminal. Para gerar novamente:

```powershell
.\venv\Scripts\python.exe -m PyInstaller --onefile --windowed --name "QRCodeReader" --hidden-import=cv2 --hidden-import=pyzbar --hidden-import=PIL --hidden-import=numpy --hidden-import=pygetwindow --collect-all=cv2 --collect-all=pyzbar --collect-all=PIL --collect-all=numpy --add-data "src;src" main.py
```

## 🐛 Problemas comuns

- `Erro ao Capturar área: unknown option "-pad"`  
  Isso foi corrigido. O problema era uso incorreto do parâmetro `pad` no widget `Tkinter.Text`. O correto é `padx` e `pady`.

- O programa não reconhece o QR  
  Verifique se a área selecionada está bem centralizada no QR e se a imagem está nítida.

- O link não abre  
  O programa tenta abrir automaticamente quando o conteúdo começa com `http://` ou `https://`.

## 📝 Licença

MIT

## 🤝 Autor

[@yuriodilon](https://github.com/yuriodilon)
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Jupyter Notebooks
.ipynb_checkpoints

# pyenv
.python-version

# celery beat schedule
celerybeat-schedule

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/

# Temporary files
*.tmp
*.temp

# Database
*.db
*.sqlite
*.sqlite3

# Secrets
*.key
*.pem
*.crt
*.csr
secrets.py
config.local.py

# Project specific
captured_qrcodes/
temp_images/
```

### LICENSE

```markdown
MIT License

Copyright (c) 2024 [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### run.bat (Windows)

```batch
@echo off
title Leitor de QR Code

echo ========================================
echo   📷 Leitor de QR Code - Captura de Tela
echo ========================================
echo.

REM Verificar se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo Por favor, instale o Python 3.7 ou superior.
    echo.
    pause
    exit /b 1
)

REM Verificar se o ambiente virtual existe
if not exist "venv\" (
    echo [INFO] Criando ambiente virtual...
    python -m venv venv
    if errorlevel 1 (
        echo [ERRO] Falha ao criar ambiente virtual!
        pause
        exit /b 1
    )
)

REM Ativar ambiente virtual
echo [INFO] Ativando ambiente virtual...
call venv\Scripts\activate

REM Verificar dependências
echo [INFO] Verificando dependencias...
python -c "import cv2, pyzbar, PIL" >nul 2>&1
if errorlevel 1 (
    echo [INFO] Instalando dependencias...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependencias!
        pause
        exit /b 1
    )
)

REM Executar programa
echo.
echo [INFO] Iniciando programa...
python main.py

REM Desativar ambiente virtual
deactivate

pause
```

### run.sh (Linux/macOS)

```bash
#!/bin/bash

echo "========================================"
echo "  📷 Leitor de QR Code - Captura de Tela"
echo "========================================"
echo ""

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python 3 não encontrado!"
    echo "Por favor, instale o Python 3.7 ou superior."
    exit 1
fi

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "[INFO] Criando ambiente virtual..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERRO] Falha ao criar ambiente virtual!"
        exit 1
    fi
fi

# Ativar ambiente virtual
echo "[INFO] Ativando ambiente virtual..."
source venv/bin/activate

# Verificar dependências
echo "[INFO] Verificando dependencias..."
python3 -c "import cv2, pyzbar, PIL" &> /dev/null
if [ $? -ne 0 ]; then
    echo "[INFO] Instalando dependencias..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "[ERRO] Falha ao instalar dependencias!"
        exit 1
    fi
fi

# Executar programa
echo ""
echo "[INFO] Iniciando programa..."
python3 main.py

# Desativar ambiente virtual
deactivate
```

### requirements-dev.txt (opcional)

```txt
# Dependências de desenvolvimento
pytest==7.4.2
pytest-cov==4.1.0
flake8==6.1.0
black==23.9.1
mypy==1.5.1
pyinstaller==5.13.0
sphinx==7.2.6
```

### CHANGELOG.md

```markdown
# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2024-01-XX

### Adicionado
- Funcionalidade de captura de tela
- Leitura de QR Codes usando pyzbar
- Interface gráfica com Tkinter
- Botão para copiar resultados
- Suporte a múltiplos QR Codes
- Atalho ESC para cancelar seleção
- Documentação completa

### Corrigido
- Tratamento de erros na captura de tela
- Compatibilidade com diferentes sistemas operacionais

### Melhorado
- Performance na detecção de QR Codes
- Interface mais intuitiva
- Código organizado em módulos
```

### CONTRIBUTING.md

```markdown
# Guia de Contribuição

Obrigado por considerar contribuir com o projeto! 🎉

## Como contribuir

### Reportar bugs

1. Verifique se o bug não foi reportado na [issue tracker](https://github.com/seu-usuario/leitor-qr-code/issues)
2. Use o template de issue para bugs
3. Inclua passos para reproduzir o bug
4. Adicione screenshots se possível

### Sugerir melhorias

1. Abra uma issue com a tag `enhancement`
2. Descreva a melhoria em detalhes
3. Explique por que seria útil

### Pull Requests

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Padrões de código

- Siga PEP 8 para Python
- Use type hints
- Documente funções com docstrings
- Mantenha testes cobrindo novas funcionalidades

## Testes

```bash
# Executar todos os testes
pytest

# Executar com cobertura
pytest --cov=src/

# Executar testes específicos
pytest tests/test_qr_scanner.py
```

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a licença MIT.
```