DevOps Final Project

Учебный DevOps-проект: Python Backend + Nginx + Docker + Docker Compose.

1. Описание проекта

Проект демонстрирует развёртывание небольшого Backend-приложения в Docker с использованием Nginx в качестве Reverse Proxy.

Nginx принимает HTTP-запросы на порту 8089 и перенаправляет их Backend-приложению, работающему внутри отдельного контейнера на порту 8000.

2. Архитектура

Пользователь
     |
     | HTTP :8089
     v
  Nginx
  :80
     |
     | Docker Network
     v
  Backend
  :8000
     |
     v
  Python Application

3. Используемые технологии

Linux (Debian)

Docker

Docker Compose

Dockerfile

Python 3

Nginx

HTTP

YAML

Linux permissions

Environment Variables

4. Структура проекта

devops-final/
├── backend/
│   ├── app.py
│   └── Dockerfile
├── nginx/
│   ├── nginx.conf
│   └── Dockerfile
├── compose.yaml
├── .env
├── .gitignore
└── README.md

5. Реализованные DevOps-практики

Контейнеризация Backend-приложения.

Использование Nginx как Reverse Proxy.

Управление несколькими сервисами через Docker Compose.

Передача настроек через Environment Variables.

Использование .env для хранения локальных конфигурационных значений.

Запуск Backend от непривилегированного пользователя appuser.

Настройка Docker Healthcheck.

Ограничение оперативной памяти Backend до 128 MiB.

Настройка политики автоматического перезапуска unless-stopped.

Просмотр логов и диагностика состояния контейнеров.

Проверка доступности приложения через curl.

6. Запуск проекта

Перейти в каталог проекта:

cd /opt/devops-final

Запустить сборку и контейнеры:

sudo docker compose up -d --build

Проверить состояние:

sudo docker compose ps

7. Проверка приложения

Главная страница:

curl http://127.0.0.1:8089/

Проверка другого URL:

curl http://127.0.0.1:8089/test

8. Полезные команды

Посмотреть логи:

sudo docker compose logs -f

Посмотреть состояние контейнеров:

sudo docker compose ps -a

Посмотреть потребление ресурсов:

sudo docker stats

Перезапустить сервисы:

sudo docker compose restart

Остановить и удалить контейнеры и сеть проекта:

sudo docker compose down

9. Безопасность

Backend работает от пользователя appuser, а не от root.

Файл .env исключён из Git через .gitignore.

Для .env установлены права доступа 600.

Для Backend установлен лимит памяти 128 MiB.

Важно: .env используется для локальной конфигурации и не является полноценным хранилищем секретов. Для production-среды следует использовать специализированное управление секретами.

10. Результат

Развёрнутое приложение доступно через Nginx по адресу:

http://127.0.0.1:8089/

Проект демонстрирует базовые навыки контейнеризации, настройки Reverse Proxy, управления инфраструктурой через Docker Compose, мониторинга состояния контейнеров и применения базовых практик безопасности.
