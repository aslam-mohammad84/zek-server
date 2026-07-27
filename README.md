# ZEK Server OS

> Personal AI Home Server built by **Mohammad Aslam**

ZEK is a self-hosted AI assistant and home server designed to run completely offline on a Samsung Galaxy M12 using Ubuntu (Proot) inside Termux.

The goal is to build an intelligent personal assistant that can monitor the server, manage files, answer questions, automate tasks, and eventually interact through Telegram and voice—all while keeping user data private.

---

# Vision

Create a portable, low-power AI server that provides:

- Personal AI Assistant
- Home Cloud
- Server Monitoring
- File Management
- AI Chat
- Automation
- Voice Assistant
- Telegram Integration

Everything runs on your own hardware.

---

# Hardware

Device:
Samsung Galaxy M12

Specifications

- Exynos 850
- ARM64
- 6 GB RAM
- 128 GB Storage
- Android
- Ubuntu running inside Proot (Termux)

---

# Current Technology Stack

## Backend

- FastAPI
- Python
- SQLite
- Uvicorn

## AI

- llama.cpp
- Qwen2.5
- Offline Inference
- Local Context Builder
- Conversation History

## Frontend

- React
- Vite
- CSS

## Remote Access

- Cloudflare Tunnel

## Version Control

- Git
- GitHub

---

# Current Project Structure

```
aslam-ai-server/

│
├── app/
│   │
│   ├── ai/
│   │   ├── config.py
│   │   ├── context_builder.py
│   │   ├── history.py
│   │   ├── llm.py
│   │   ├── prompts.py
│   │   └── tools.py
│   │
│   ├── api/
│   │   ├── ai.py
│   │   ├── auth.py
│   │   ├── cloud.py
│   │   └── dashboard.py
│   │
│   ├── services/
│   │   ├── system_monitor.py
│   │   └── file_stats.py
│   │
│   ├── database/
│   │
│   └── main.py
│
├── dashboard/
│   │
│   ├── src/
│   │   ├── App.jsx
│   │   ├── Chat.jsx
│   │   ├── Cloud.jsx
│   │   └── ...
│   │
│   └── vite.config.js
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

# Current Features

## Dashboard

- Server Status
- Cloud Section
- AI Chat Interface
- Responsive UI

---

## AI

Current AI can

- Hold conversations
- Remember recent messages
- Use server context
- Answer programming questions
- Answer server questions
- Run completely offline

Current Model

Qwen2.5 running with llama.cpp

---

## Server Monitoring

Current metrics

- CPU Usage
- RAM Usage
- Storage
- Internet Status
- Battery Status
- Uptime

---

## Cloud

Current

- File Browser
- File Metadata
- Download Support

Future

- Upload Files
- Delete Files
- Folder Management
- Search
- Image Preview

---

## Authentication

Current

- Login
- Protected API

Future

- JWT Refresh
- Multi-user
- Role Permissions

---

## Remote Access

Implemented

Cloudflare Quick Tunnel

Planned

Cloudflare Named Tunnel

Benefits

- Permanent URL
- HTTPS
- Secure Remote Access
- No Port Forwarding

---

# AI Architecture

```
User

↓

React Dashboard

↓

FastAPI

↓

Context Builder

↓

Conversation History

↓

System Prompt

↓

Qwen2.5

↓

Response

↓

Dashboard
```

---

# Current AI Capabilities

General Conversation

Programming Help

Server Monitoring

Context Awareness

Offline AI

Natural Responses

Recent Conversation Memory

---

# Development Roadmap

## Phase 1 — Core Server

Status:
Nearly Complete

Completed

- FastAPI
- React Dashboard
- SQLite
- Authentication
- AI Chat
- Context Builder
- Conversation History
- GitHub
- Cloudflare Quick Tunnel

Remaining

- Permanent Cloudflare Tunnel
- Production Deployment
- Backend Cleanup
- .gitignore Improvements

---

## Phase 2 — Server Health Dashboard

Planned

- Live CPU Graph
- Live RAM Graph
- Storage Graph
- Battery Graph
- Internet Monitor
- Running Services
- Live Logs

---

## Phase 3 — Telegram Assistant

Planned

Features

- Telegram Bot
- Remote Commands
- Notifications
- Server Status
- File Download
- AI Chat

---

## Phase 4 — Intelligent AI Assistant

Goals

- Better reasoning
- Automatic Tool Selection
- Better Memory
- Long-Term Memory
- Task Planning
- Code Generation
- Local Knowledge Base

---

## Phase 5 — Voice Assistant

Features

- Speech Recognition
- Text to Speech
- Wake Word
- Voice Commands
- Voice Chat

---

## Phase 6 — Reminder System

Features

- Daily Reminders
- Tasks
- Calendar
- Notes
- Notifications

---

## Phase 7 — Personal Cloud

Features

- File Upload
- File Download
- Folder Management
- Image Gallery
- Video Streaming
- Document Viewer

---

## Phase 8 — Automation

Features

- Scheduled Tasks
- Smart Workflows
- Auto Backup
- Server Actions
- AI Automation

---

## Phase 9 — Security

Features

- Permanent Cloudflare Tunnel
- HTTPS
- API Security
- JWT Refresh
- Audit Logs
- Encryption

---

# Future AI Goals

ZEK should eventually become capable of

- Managing the server
- Understanding natural language
- Running local AI models
- Managing reminders
- Answering technical questions
- Monitoring hardware
- Managing cloud files
- Performing automation
- Talking through voice
- Integrating with Telegram
- Acting as a personal digital assistant

---

# Current Repository Status

Backend
✓

Frontend
✓

AI
✓

Dashboard
✓

Cloud
✓

GitHub
✓

Cloudflare
✓

Offline AI
✓

---

# Author

Mohammad Aslam

Computer Science Engineer

Personal AI Home Server Project

2026

---

# License

This project is intended for personal learning, experimentation, and self-hosting.
