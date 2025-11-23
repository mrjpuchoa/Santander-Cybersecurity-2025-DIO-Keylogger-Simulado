# Santander-Cybersecurity-2025-DIO-Keylogger-Simulado
Este repositório tem o objetivo de apresentar o desafio final proposto pelo bootcamp Santander Cibersegurança 2025 (DIO), referente ao Lab Project do módulo "Simulando um Malware de Captura de Dados Simples em Python e Aprendendo a se Proteger".

# Keylogger Educacional - Bootcamp Cibersegurança Santander/DIO

## AVISO IMPORTANTE

Este keylogger foi desenvolvido **EXCLUSIVAMENTE** para fins educacionais e de aprendizado em ambiente controlado. 

**USE APENAS:**
- Em seu próprio computador
- Em máquinas virtuais sob seu controle
- Para fins educacionais e de pesquisa em segurança

**NUNCA USE:**
- Em computadores de terceiros sem autorização
- Para atividades ilegais
- Para espionagem ou coleta não autorizada de dados

O uso não autorizado de keyloggers é **ILEGAL** em muitos países e pode resultar em consequências legais graves.

## Requisitos

- Python 3.6 ou superior
- Biblioteca `pynput`

## Instalação

1. Instale as dependências:
```bash
pip3 install pynput
```

**Nota:** Em sistemas Linux com ambiente gerenciado (como Kali), você pode precisar criar um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
pip install pynput
```

2. No Linux, pode ser necessário instalar dependências do sistema:
```bash
sudo apt-get install python3-tk python3-dev
```

## Como Usar

### Execução Normal:
```bash
python3 keylogger.pyw
```

### Parar o Keylogger:
Pressione `ESC` para parar, ou use:
```bash
pkill -f keylogger.pyw
```

## Configuração de Email

O keylogger está configurado para usar **Mailtrap** para captura de emails de teste.

**Configuração Atual:**
- **Servidor SMTP:** `sandbox.smtp.mailtrap.io`
- **Porta:** `2525`
- **Email Destinatário:** `usuario1@test.com` (não importa o email, vai cair no mailtrap, o que importa são as credenciais de autenticação do mailtrap)
- **Threshold:** Envia email a cada 20 caracteres capturados

**Sobre o Mailtrap:**
- O Mailtrap é um serviço de teste que **não envia emails reais**
- Os emails são capturados e podem ser visualizados na inbox do Mailtrap
- Acesse https://mailtrap.io para ver os emails capturados

**Para usar outro serviço de email:**

## Arquivos Gerados

- `log.txt`: Arquivo contendo todas as teclas capturadas (formato linear, sem timestamps)
- `log_backup.txt`: Backup dos logs quando o envio de email falhar

## Funcionalidades

- Captura de teclas em tempo real
- Logging linear (sem quebras de linha ou timestamps)
- Execução furtiva (background)
- Envio automático de logs por email a cada 20 caracteres
- Suporte a autenticação SMTP
- Sistema de backup automático em caso de falha no envio
- Tratamento de erros silencioso para manter furtividade
- Ignora teclas modificadoras (Shift, Ctrl, Alt)
- Converte Enter e Tab em espaços para manter formato linear

## Personalização

Você pode ajustar as seguintes variáveis no código:

- `CHAR_THRESHOLD`: Número de caracteres antes de enviar email (padrão: 20)
- `EMAIL_TO`: Email destinatário
- `EMAIL_FROM`: Email remetente
- `SMTP_SERVER`: Servidor SMTP
- `SMTP_PORT`: Porta SMTP (2525 para Mailtrap)
- `SMTP_USER` e `SMTP_PASS`: Credenciais de autenticação
- `USE_AUTH`: Habilitar/desabilitar autenticação SMTP

## Notas Técnicas

- O keylogger captura apenas caracteres visíveis e espaços
- Os logs são salvos de forma linear, sem timestamps ou quebras de linha
- O sistema de threading garante que o envio de email não bloqueie a captura
- O arquivo de log é limpo após cada envio de email bem-sucedido
- Em caso de falha no envio, os logs são salvos em `log_backup.txt`
- Teclas especiais (Backspace, Delete, ESC) são ignoradas
- Enter e Tab são convertidos em espaços para manter o formato linear

## Segurança

- As credenciais SMTP estão hardcoded no código (apenas para fins educacionais)
- Em produção, use variáveis de ambiente ou arquivos de configuração seguros
- Não compartilhe credenciais de email em código público

## Considerações Legais e Éticas

Este código é fornecido apenas para fins educacionais. O desenvolvedor não se responsabiliza pelo uso indevido deste software. Sempre obtenha autorização explícita antes de usar qualquer ferramenta de monitoramento.

## Estrutura do Código

- `format_key()`: Formata teclas pressionadas para string legível
- `write_to_log()`: Escreve dados no arquivo de log e verifica threshold
- `send_email_log()`: Envia logs por email via SMTP
- `on_press()`: Callback quando uma tecla é pressionada
- `on_release()`: Callback quando uma tecla é solta
- `main()`: Função principal que inicia o keylogger
