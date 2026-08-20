Aqui está um README.md completo e profissional para o seu projeto:

```markdown
# 📷 Leitor de QR Code - Captura de Tela

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)]()

Uma ferramenta desktop intuitiva para capturar e ler QR Codes diretamente da tela. Com uma interface simples e amigável, você pode selecionar qualquer área da tela e obter instantaneamente o conteúdo do QR Code.

## ✨ Funcionalidades

- 🖱️ **Seleção intuitiva**: Arraste o mouse para selecionar qualquer área da tela
- 📱 **Leitura automática**: Detecta e decodifica QR Codes automaticamente
- 📋 **Cópia rápida**: Copie o conteúdo do QR Code com um clique
- 🎯 **Múltiplos QR Codes**: Suporta múltiplos QR Codes na mesma captura
- 🖥️ **Multi-plataforma**: Funciona no Windows, Linux e macOS
- 🎨 **Interface moderna**: Design limpo e intuitivo

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

## 🚀 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/leitor-qr-code.git
cd leitor-qr-code
```

### 2. Criar e ativar ambiente virtual (recomendado)

#### Windows (CMD/PowerShell)
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📦 Dependências

| Pacote | Versão | Descrição |
|--------|--------|-----------|
| opencv-python | 4.8.1.78 | Processamento de imagens |
| pyzbar | 0.1.9 | Leitura de QR Codes |
| pillow | 10.1.0 | Manipulação de imagens |
| pygetwindow | 0.0.9 | Controle de janelas |
| numpy | 1.24.3 | Operações matemáticas |

## 🎯 Como usar

1. **Inicie o programa**
   ```bash
   python main.py
   ```

2. **Capture o QR Code**
   - Clique no botão "🔍 Capturar QR Code"
   - A tela ficará semi-transparente
   - Arraste o mouse para selecionar a área do QR Code
   - Solte o mouse para capturar

3. **Visualize o resultado**
   - O conteúdo do QR Code será exibido automaticamente
   - Clique em "📋 Copiar" para copiar o texto
   - Múltiplos QR Codes serão listados separadamente

### 🎮 Atalhos do teclado

- `ESC`: Cancela a seleção atual
- `Ctrl+C`: Copia o conteúdo (quando disponível)

## 📁 Estrutura do projeto

```
leitor-qr-code/
│
├── src/
│   ├── __init__.py         # Pacote Python
│   ├── main.py             # Ponto de entrada
│   ├── qr_scanner.py       # Classe principal do scanner
│   └── utils.py            # Funções utilitárias
│
├── requirements.txt        # Dependências do projeto
├── run.bat                 # Script de execução (Windows)
├── run.sh                  # Script de execução (Linux/Mac)
├── .gitignore             # Arquivos ignorados pelo Git
├── LICENSE                # Licença MIT
└── README.md              # Documentação
```

## 🔧 Configuração

### Ambiente de desenvolvimento

```bash
# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt  # Se existir

# Executar testes
python -m pytest tests/

# Verificar estilo de código
flake8 src/
```

### Criar executável (opcional)

```bash
# Instalar PyInstaller
pip install pyinstaller

# Gerar executável
pyinstaller --onefile --windowed --icon=icon.ico --name "QRCodeReader" main.py
```

## 🐛 Solução de problemas

### Problemas comuns e soluções

| Problema | Solução |
|----------|---------|
| **Erro: `ModuleNotFoundError`** | Execute `pip install -r requirements.txt` |
| **QR Code não detectado** | Certifique-se de que o QR Code está nítido e bem iluminado |
| **Erro de permissão** | Execute como administrador (Windows) ou com `sudo` (Linux/Mac) |
| **Interface não abre** | Verifique se o Python 3.7+ está instalado |

### Logs de erro

Os erros são exibidos diretamente no console. Para debug:

```bash
python main.py --debug  # Modo debug
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Guidelines

- Mantenha o código limpo e documentado
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário
- Siga o PEP 8 para estilo de código

## 📝 Licença MIT

Copyright (c) 2024 [Seu Nome]

A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e arquivos de documentação associados (o "Software"), para lidar
no Software sem restrição, incluindo sem limitação os direitos
de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender
cópias do Software, e permitir que pessoas a quem o Software seja
fornecido o façam, sujeito às seguintes condições:

O aviso de copyright acima e este aviso de permissão devem ser incluídos em todas
as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
IMPLÍCITA, INCLUINDO MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO,
ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM NENHUM CASO OS AUTORES OU
TITULARES DE DIREITOS DE AUTOR SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS
OU OUTRA RESPONSABILIDADE, SEJA EM AÇÃO DE CONTRATO, TORT OU OUTRA FORMA, DECORRENTE
DE, OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTRAS NEGOCIAÇÕES NO SOFTWARE.

## 📊 Roadmap

- [ ] Suporte a diferentes tipos de código de barras (EAN, UPC, etc.)
- [ ] Histórico de QR Codes lidos
- [ ] Exportar resultados para arquivo
- [ ] Reconhecimento de QR Codes em imagens salvas
- [ ] Tema escuro/claro
- [ ] Notificações do sistema

## 📞 Suporte

- 📧 Email: seu-email@exemplo.com
- 💬 Issues: [GitHub Issues](https://github.com/seu-usuario/leitor-qr-code/issues)
- 📖 Documentação: [Wiki do projeto](https://github.com/seu-usuario/leitor-qr-code/wiki)

## 🙏 Agradecimentos

- [OpenCV](https://opencv.org/) - Processamento de imagens
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) - Leitura de QR Codes
- [Pillow](https://python-pillow.org/) - Manipulação de imagens
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Interface gráfica

## 📈 Estatísticas

![GitHub stars](https://img.shields.io/github/stars/seu-usuario/leitor-qr-code)
![GitHub forks](https://img.shields.io/github/forks/seu-usuario/leitor-qr-code)
![GitHub issues](https://img.shields.io/github/issues/seu-usuario/leitor-qr-code)

---

⭐ **Se este projeto ajudou você, considere dar uma estrela no GitHub!**

Feito com ❤️ por [Seu Nome](https://github.com/seu-usuario)

```

## 📁 Criar arquivos adicionais

### .gitignore completo

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual Environment
venv/
env/
ENV/
env.bak/
venv.bak/

# PyCharm
.idea/
*.iml

# VSCode
.vscode/
*.code-workspace

# Sublime Text
*.sublime-project
*.sublime-workspace

# Spyder
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
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

Agora você tem um projeto completo, profissional e bem documentado! 🚀