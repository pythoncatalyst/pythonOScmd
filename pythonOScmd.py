#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pythonOScmd - Unified Terminal Operating System."""

################################################################################
# PYTHONOS COMMAND - UNIFIED TERMINAL OPERATING SYSTEM
################################################################################
# Author: Ahmed Dragonclaw Suche Orangatang DiluteChimp Washington Sayyed
# Version: pythonOScmd65 (Base: pythonOS70, Version 21.1)
# Description: Terminal OS with monitoring, security tools, media capabilities
#
# TABLE OF CONTENTS:
# ------------------
# SECTION 1:  Imports & Core Dependencies
# SECTION 2:  Configuration & Constants
# SECTION 3:  Core System Utilities (Boot Loader, Audio Init)
# SECTION 4:  Database & Logging System (Complete Suite)
# SECTION 5:  UI & Display System (Colors, Visual FX, Headers)
# SECTION 6:  Weather & Environmental Monitoring
# SECTION 7:  Satellite & Orbital Tracking
# SECTION 8:  Network & Connectivity (WiFi, Bluetooth, Network Tools)
# SECTION 9:  Security & Penetration Testing
# SECTION 10: Defence & Protection Systems
# SECTION 11: Media & Entertainment (ASCII Player, Media Scanner)
# SECTION 12: Hardware Monitoring & Diagnostics
# SECTION 13: AI & Analytics (Deep Probe, Autonomous Optimizer)
# SECTION 14: System Management Tools
# SECTION 15: Web & Remote Dashboard
# SECTION 16: Plugin System & Extensibility
# SECTION 17: Download Center & Package Management
# SECTION 18: Developer Tools (PWN Tools, Python Power)
# SECTION 19: Integration & Bridge Functions
# SECTION 20: Main Application Logic
# SECTION 21: Startup & Initialization
#
# IMPORTANT NOTES:
# - Indentation is just as important as your Incantation
# - Runs video in terminal with full color ASCII support
# - Option 3 and 13 are most like a T.V.
# - Fix needed: Command Center Option 9, selection 2 (Ctrl+C handling)
################################################################################
# ================================================================================
# SECTION 1: IMPORTS & CORE DEPENDENCIES
# ================================================================================

# Standard Library Imports
import sys
import subprocess
import os
import time
import ctypes # Added for Admin/Root probing
import calendar # Added for AI/Calendar expansion
import csv
import textwrap
import tempfile
import importlib

# ================================================================================
# SECTION 3: CORE SYSTEM UTILITIES
# ================================================================================

def boot_loader():
    # Fix for UnicodeEncodeError: Force UTF-8 encoding for stdout if possible
    if sys.stdout.encoding != 'utf-8':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 1. Define required libraries
    required = {'psutil', 'requests', 'beautifulsoup4', 'Pillow', 'gputil', 'numpy'}
    missing = set()

    # 2. Check what is actually installed without using pkg_resources1

    for lib in required:
        try:
            # Map pip package names to actual python import names
            import_name = {
                'beautifulsoup4': 'bs4',
                'Pillow': 'PIL',
                'gputil': 'GPUtil'
            }.get(lib, lib)
            __import__(import_name)
        except ImportError:
            missing.add(lib)

    # 3. If anything is missing, ask the user
    if missing:
        print(f"\033[93m[!] 📦 Missing Libraries detected: {', '.join(missing)}\033[0m")
        choice = input("📥 Do you want to install them now? (y/n): ").strip().lower()

        if choice == 'y':
            print(f"🚀 Installing: {missing}...")
            try:
                # Uses global 'sys' which is now safely imported at the top
                subprocess.check_call([sys.executable, "-m", "pip", "install", *missing],
                                      stdout=subprocess.DEVNULL)
                print("✅ Setup complete. Launching Monitor...\n")
                time.sleep(1)
            except Exception as e:
                print(f"❌ Auto-install failed. Try running: pip install {' '.join(missing)}")
                sys.exit(1)
        else:
            # 4. User said NO - Enable Safe Mode (Mocking)
            print("\n\033[91m[!] ⚠️ WARNING: You chose not to install dependencies.\033[0m")

            # Specific warning for Pillow
            if 'Pillow' in missing:
                print("\033[91m[!] 🖼️ NOTE: Pillow is missing. Web Image/ASCII functionality will be REDUCED.\033[0m")

            print("🛡️ Loading in Safe Mode (Some features may display 'N/A')...\n")
            time.sleep(2)

            # Define a Mock Class to prevent 'ImportError' crashes
            class MockModule:
                def __init__(self, *args, **kwargs): pass
                def __getattr__(self, name): return self
                def __call__(self, *args, **kwargs): return self
                def __iter__(self): return iter([]) # Return empty list for loops
                def __bool__(self): return False    # Treat as False in boolean checks

            # Inject fake modules into system memory
            for lib in missing:
                if lib == 'Pillow':
                    sys.modules['PIL'] = MockModule()
                    sys.modules['PIL.Image'] = MockModule()
                elif lib == 'beautifulsoup4':
                    sys.modules['bs4'] = MockModule()
                elif lib == 'gputil':
                    sys.modules['GPUtil'] = MockModule()
                elif lib == 'numpy':
                    sys.modules['numpy'] = MockModule()
                else:
                    sys.modules[lib] = MockModule()

# Run the bootloader before importing the main libraries
boot_loader()

# Third-Party Library Imports (after boot_loader ensures they exist)
import platform
import psutil
import socket
import getpass
import uuid
import datetime
import threading
import random
import math
import cmath
import statistics
import curses
import numpy as np
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import GPUtil
from collections import deque
from pathlib import Path
import re # Added for Visual FX Regex

import shutil # Added for check_pentest_tool
import sqlite3 # Added for Database/Log system
import json # Added for JSON logging
from urllib.parse import urlparse, parse_qs, urlencode
from http.server import BaseHTTPRequestHandler, HTTPServer
import traceback

# Textual imports are loaded lazily to keep classic mode fast and avoid hard dependency at startup.
App = ComposeResult = Container = Horizontal = Vertical = Grid = None
reactive = None
Header = Footer = Static = ListView = ListItem = Label = Tabs = Tab = Digits = Markdown = None
_TEXTUAL_IMPORTED = False
_TEXTUAL_IMPORT_ERROR = None


def _ensure_textual_imports():
    """Lazy-load Textual widgets the first time enhanced mode is launched."""
    global App, ComposeResult, Container, Horizontal, Vertical, Grid, reactive
    global Header, Footer, Static, ListView, ListItem, Label, Tabs, Tab, Digits, Markdown
    global _TEXTUAL_IMPORTED, _TEXTUAL_IMPORT_ERROR
    if _TEXTUAL_IMPORTED:
        return True
    try:
        from textual.app import App, ComposeResult
        from textual.containers import Container, Horizontal, Vertical, Grid
        from textual.reactive import reactive
        from textual.widgets import Header, Footer, Static, ListView, ListItem, Label, Tabs, Tab
        try:
            from textual.widgets import Digits, Markdown
        except Exception:
            # Fallbacks if specific widgets are missing in older/newer releases
            Digits = Static
            Markdown = Static
        _TEXTUAL_IMPORTED = True
        _TEXTUAL_IMPORT_ERROR = None
        return True
    except Exception as exc:
        _TEXTUAL_IMPORTED = False
        _TEXTUAL_IMPORT_ERROR = exc
        App = ComposeResult = Container = Horizontal = Vertical = Grid = None
        reactive = None
        Header = Footer = Static = ListView = ListItem = Label = Tabs = Tab = Digits = Markdown = None
        return False

def init_audio_device():
    """Detect default audio output (PulseAudio/PipeWire) and set env override."""
    if os.name != 'posix':

        return None
    try:
        res = subprocess.run(
            ["pactl", "info"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
    except FileNotFoundError:
        return None
    if res.returncode != 0:
        return None
    for line in res.stdout.splitlines():
        if line.lower().startswith("default sink:"):
            sink = line.split(":", 1)[1].strip()
            if sink:
                os.environ.setdefault("PULSE_SINK", sink)
                return sink
    return None

DEFAULT_AUDIO_SINK = init_audio_device()

# ================================================================================
# SECTION 2: CONFIGURATION & CONSTANTS
# ================================================================================

# Database and Log Directory Setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(SCRIPT_DIR, "pythonOS_data")
LOG_DIR = os.path.join(DB_DIR, "logs")
DB_FILE = os.path.join(DB_DIR, "pythonOS.db")

SWAP_CACHE_DIR = os.path.join(DB_DIR, "swap_cache")
CONFIG_FILE = os.path.join(DB_DIR, "config.json")
DOC_LIBRARY_DIR = os.path.join(DB_DIR, "documents")

# Log Categories
LOG_CATEGORIES = {
    "system": "System Information",
    "network": "Network Operations",

    "security": "Security & Audit",
    "hardware": "Hardware Probing",
    "media": "Media Operations",
    "weather": "Weather Data",
    "process": "Process Management",
    "ai": "AI & Analytics",
    "pentest": "Penetration Testing",
    "defense": "Defense Operations",
    "general": "General Logs",
    "aggressive_scan": "Aggressive Intelligence Scan"
}

DB_API_PORT = 8092
_db_api_server = None
_db_scheduler_running = False
_db_scheduled_tasks = []

# ================================================================================
# SECTION 4: DATABASE & LOGGING SYSTEM (Version 21.2)
# ================================================================================

# Complete database and logging infrastructure including:
# - SQLite connection management
# - Log file categorization and storage
# - Swap cache system for performance
# - File tracking and metadata
# - Database export/import

# - Advanced query tools
# ================================================================================

def _db_connect():
    conn = sqlite3.connect(DB_FILE, timeout=10)
    try:
        conn.execute("PRAGMA busy_timeout = 5000")
    except Exception:

        pass
    return conn

def safe_run(category, operation, func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:

        tb = traceback.format_exc()
        print(f"{COLORS['1'][0]}❌ Error in {operation}: {e}{RESET}")
        try:
            file_path = save_log_file(category, f"{operation}_Error", tb, prompt_user=False)
            log_to_database(category, operation, tb, file_path=file_path, status="error")
        except Exception:
            pass
        return None

def _load_user_config():
    os.makedirs(DB_DIR, exist_ok=True)
    if not os.path.exists(CONFIG_FILE):
        return {}
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def _save_user_config(config, allow_create=False):
    # Avoid creating a fresh config file unless explicitly allowed
    if not allow_create and not os.path.exists(CONFIG_FILE):
        return

    os.makedirs(DB_DIR, exist_ok=True)
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)

    except Exception:
        pass

def init_database_system():
    """Initialize the database and directory structure."""
    try:
        # Create directories if they don't exist
        os.makedirs(DB_DIR, exist_ok=True)

        os.makedirs(LOG_DIR, exist_ok=True)
        os.makedirs(SWAP_CACHE_DIR, exist_ok=True)

        # Create category subdirectories
        for category in LOG_CATEGORIES.keys():
            os.makedirs(os.path.join(LOG_DIR, category), exist_ok=True)

        # Initialize SQLite database
        with _db_connect() as conn:
            cursor = conn.cursor()

        # Create tables

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS log_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    category TEXT NOT NULL,
                    operation TEXT NOT NULL,
                    data TEXT,
                    file_path TEXT,
                    status TEXT DEFAULT 'success'
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS file_tracking (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_path TEXT UNIQUE NOT NULL,
                    file_type TEXT,
                    file_size INTEGER,
                    created_date TEXT,
                    last_accessed TEXT,
                    access_count INTEGER DEFAULT 0,
                    metadata TEXT

                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS swap_cache (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cache_key TEXT UNIQUE NOT NULL,
                    cache_data TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    expires_at TEXT,
                    access_count INTEGER DEFAULT 0,
                    last_accessed TEXT
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS session_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_start TEXT NOT NULL,

                    session_end TEXT,
                    operations_count INTEGER DEFAULT 0,
                    features_used TEXT
                )
            ''')

            conn.commit()
        return True
    except Exception as e:
        print(f"⚠️ Database initialization error: {e}")
        return False

def log_to_database(category, operation, data=None, file_path=None, status="success"):
    """Log an entry to the SQLite database."""
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cursor.execute('''
                INSERT INTO log_entries (timestamp, category, operation, data, file_path, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (timestamp, category, operation, str(data) if data else None, file_path, status))

            conn.commit()

        return True
    except Exception as e:
        print(f"⚠️ Database logging error: {e}")
        return False

def save_log_file(category, operation, content, prompt_user=True):
    """Save a log file to categorized folder and optionally log to database."""
    if prompt_user:
        response = input(f"\n{BOLD}💾 Save this data to log file? (y/n): {RESET}").strip().lower()
        if response != 'y':
            return None

    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        category_dir = os.path.join(LOG_DIR, category)
        filename = f"{operation.replace(' ', '_')}_{timestamp}.log"
        file_path = os.path.join(category_dir, filename)


        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"=== {operation} ===\n")
            f.write(f"Timestamp: {timestamp}\n")
            f.write(f"Category: {category}\n")
            f.write("=" * 50 + "\n\n")
            f.write(content)

        # Log to database
        log_to_database(category, operation, content[:500], file_path, "saved")

        print(f"{COLORS['2'][0]}✅ Log saved: {file_path}{RESET}")
        return file_path
    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Error saving log: {e}{RESET}")
        return None

def track_file(file_path, file_type=None, metadata=None):
    """Track a file in the database for future reference."""
    try:
        if not os.path.exists(file_path):
            return False

        file_size = os.path.getsize(file_path)
        created_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
        last_accessed = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO file_tracking
                (file_path, file_type, file_size, created_date, last_accessed, access_count, metadata)
                VALUES (?, ?, ?, ?, ?,
                    COALESCE((SELECT access_count + 1 FROM file_tracking WHERE file_path = ?), 1),
                    ?)
            ''', (file_path, file_type, file_size, created_date, last_accessed, file_path, json.dumps(metadata) if metadata else None))

            conn.commit()
        return True
    except Exception as e:

        print(f"⚠️ File tracking error: {e}")
        return False

def cache_data(key, data, expire_minutes=30):
    """Cache data in SQLite swap system for performance boost."""
    try:
        created_at = datetime.datetime.now()
        expires_at = created_at + datetime.timedelta(minutes=expire_minutes)

        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO swap_cache (cache_key, cache_data, created_at, expires_at, access_count, last_accessed)
                VALUES (?, ?, ?, ?,
                    COALESCE((SELECT access_count + 1 FROM swap_cache WHERE cache_key = ?), 1),
                    ?)
            ''', (key, json.dumps(data), created_at.strftime("%Y-%m-%d %H:%M:%S"),
                  expires_at.strftime("%Y-%m-%d %H:%M:%S"), key, created_at.strftime("%Y-%m-%d %H:%M:%S")))

            conn.commit()
        return True
    except Exception as e:
        return False

def get_cached_data(key):
    """Retrieve cached data from swap system."""
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT cache_data, expires_at FROM swap_cache

                WHERE cache_key = ? AND datetime(expires_at) > datetime('now')
            ''', (key,))

            result = cursor.fetchone()

        if result:
            return json.loads(result[0])
        return None
    except Exception as e:
        return None

def clean_expired_cache():
    """Clean up expired cache entries."""
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM swap_cache WHERE datetime(expires_at) <= datetime('now')")
            deleted = cursor.rowcount

            conn.commit()
        return deleted
    except Exception as e:
        return 0

def clear_cached_data(key):
    """Remove a cached entry by key."""
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM swap_cache WHERE cache_key = ?", (key,))
            deleted = cursor.rowcount
            conn.commit()
        return deleted
    except Exception:
        return 0

def feature_database_log_center():
    """Database & Log Files Management Center."""
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("💾 Database & Log Files Center")

        # Quick stats
        try:
            with _db_connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM log_entries")
                log_count = cursor.fetchone()[0]

                cursor.execute("SELECT COUNT(*) FROM file_tracking")
                tracked_files = cursor.fetchone()[0]

                cursor.execute("SELECT COUNT(*) FROM swap_cache WHERE datetime(expires_at) > datetime('now')")
                cache_count = cursor.fetchone()[0]

            print(f"{BOLD}📊 System Status:{RESET}")
            print(f"  📝 Total Log Entries: {log_count}")
            print(f"  📂 Tracked Files: {tracked_files}")
            print(f"  🚀 Active Cache Entries: {cache_count}")
            print(f"  📁 Database Location: {DB_FILE}")
        except:
            print(f"{COLORS['1'][0]}⚠️ Database not accessible{RESET}")


        print(f"\n{BOLD}Main Menu:{RESET}")
        print(f" {BOLD}[1]{RESET} 📋 View Log Files (by Category)")
        print(f" {BOLD}[2]{RESET} 🔍 Search Logs")
        print(f" {BOLD}[3]{RESET} 📊 Database Statistics")
        print(f" {BOLD}[4]{RESET} 📂 File Tracking Browser")
        print(f" {BOLD}[5]{RESET} 🚀 Swap Cache Management")
        print(f" {BOLD}[6]{RESET} 💾 Export Database (SQL/JSON)")
        print(f" {BOLD}[7]{RESET} 📥 Import Data")
        print(f" {BOLD}[8]{RESET} 🧹 Clean & Optimize")
        print(f" {BOLD}[9]{RESET} ⚙️ Database Settings")
        print(f" {BOLD}[10]{RESET} 🔍 Lite Scan (Quick System Snapshot)")

        print(f" {BOLD}[11]{RESET} 🚨 Aggressive Scan (Deep Intelligence)")
        print(f" {BOLD}[12]{RESET} 🧭 Advanced Database Suite")
        print(f" {BOLD}[13]{RESET} 📡 Start DB API Server")
        print(f" {BOLD}[14]{RESET} 🌐 Open DB API Stats Endpoint")
        print(f" {BOLD}[0]{RESET} ↩️  Return to Command Center")

        choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

        if choice == '0':
            break
        elif choice == '1':
            safe_run("general", "View_Log_Files", _view_log_files)
        elif choice == '2':
            safe_run("general", "Search_Logs", _search_logs)
        elif choice == '3':
            safe_run("general", "Database_Statistics", _database_statistics)
        elif choice == '4':
            safe_run("general", "File_Tracking_Browser", _file_tracking_browser)
        elif choice == '5':
            safe_run("general", "Swap_Cache_Management", _swap_cache_management)
        elif choice == '6':
            safe_run("general", "Export_Database", _export_database)
        elif choice == '7':
            safe_run("general", "Import_Data", _import_data)
        elif choice == '8':
            safe_run("general", "Clean_Optimize", _clean_optimize)
        elif choice == '9':
            safe_run("general", "Database_Settings", _database_settings)
        elif choice == '10':
            safe_run("system", "Lite_Scan", _lite_scan)
            _enhanced_satellite_view(stdscr, state)
            safe_run("aggressive_scan", "Aggressive_Scan", _aggressive_scan)
        elif choice == '12':
            safe_run("general", "Advanced_Database_Suite", _advanced_database_suite)
        elif choice == '13':
            _db_api_server_start()
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '14':
            _db_api_server_start()
            _open_url(f"http://localhost:{DB_API_PORT}/stats")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _view_log_files():
    """View log files by category."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📋 Log Files by Category")

    print(f"\n{BOLD}Select Category:{RESET}")
    categories = list(LOG_CATEGORIES.keys())
    for i, (cat_key, cat_name) in enumerate(LOG_CATEGORIES.items(), 1):
        # Count files in category
        cat_dir = os.path.join(LOG_DIR, cat_key)
        file_count = len([f for f in os.listdir(cat_dir) if f.endswith('.log')]) if os.path.exists(cat_dir) else 0
        print(f" {BOLD}[{i}]{RESET} {cat_name} ({file_count} files)")

    choice = input(f"\n{BOLD}Select category (1-{len(categories)}): {RESET}").strip()

    try:
        idx = int(choice) - 1
        if 0 <= idx < len(categories):
            category = categories[idx]
            cat_dir = os.path.join(LOG_DIR, category)

            if os.path.exists(cat_dir):
                log_files = sorted([f for f in os.listdir(cat_dir) if f.endswith('.log')], reverse=True)

                if not log_files:
                    print(f"\n{COLORS['4'][0]}📭 No log files in this category{RESET}")
                else:
                    page_size = 10
                    page = 0
                    while True:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_header(f"📋 Logs: {LOG_CATEGORIES[category]}")
                        start = page * page_size
                        end = start + page_size
                        page_items = log_files[start:end]
                        print(f"\n{BOLD}Page {page + 1}/{(len(log_files) - 1) // page_size + 1}:{RESET}")
                        for i, log_file in enumerate(page_items, 1):
                            file_path = os.path.join(cat_dir, log_file)
                            file_size = os.path.getsize(file_path)
                            print(f" {i}. {log_file} ({file_size} bytes)")

                        print("\n[N]ext  [P]rev  [V]iew <num>  [B]ack")
                        cmd = input("Select: ").strip().lower()
                        if cmd == 'b':
                            break
                        if cmd == 'n' and end < len(log_files):
                            page += 1
                            continue
                        if cmd == 'p' and page > 0:
                            page -= 1
                            continue
                        if cmd.startswith('v'):
                            num = cmd[1:].strip()
                            if not num.isdigit():
                                num = input("Enter number to view: ").strip()
                            if num.isdigit():
                                file_idx = int(num) - 1
                                if 0 <= file_idx < len(page_items):
                                    file_path = os.path.join(cat_dir, page_items[file_idx])
                                    with open(file_path, 'r', encoding='utf-8') as f:
                                        content = f.read()
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print_header(f"📄 {page_items[file_idx]}")
                                    print(content[:2000])
                                    if len(content) > 2000:
                                        print(f"\n... (truncated, total {len(content)} characters)")
                                    input("\nPress Enter to return...")
    except Exception:
        print(f"{COLORS['1'][0]}❌ Invalid selection{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _search_logs():
    """Search logs in database."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🔍 Search Logs")

    search_term = input(f"\n{BOLD}Enter search term: {RESET}").strip()

    if not search_term:
        return

    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT timestamp, category, operation, data, status
                FROM log_entries
                WHERE operation LIKE ? OR data LIKE ? OR category LIKE ?
                ORDER BY timestamp DESC LIMIT 50
            ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            results = cursor.fetchall()

        if results:
            print(f"\n{BOLD}Found {len(results)} matching entries:{RESET}\n")
            for timestamp, category, operation, data, status in results:
                print(f"{COLORS['2'][0]}[{timestamp}]{RESET} {category.upper()}: {operation}")
                if data:
                    print(f"  {data[:100]}..." if len(data) > 100 else f"  {data}")
                print()
        else:
            print(f"\n{COLORS['4'][0]}No matching entries found{RESET}")
    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Search error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _database_statistics():
    """Show detailed database statistics."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📊 Database Statistics")

    try:
        with _db_connect() as conn:
            cursor = conn.cursor()

            # Log statistics by category
            print(f"\n{BOLD}Log Entries by Category:{RESET}")
            cursor.execute('''
                SELECT category, COUNT(*) as count
                FROM log_entries
                GROUP BY category
                ORDER BY count DESC
            ''')
            for category, count in cursor.fetchall():
                print(f"  {category.capitalize()}: {count}")

            # Recent operations
            print(f"\n{BOLD}Recent Operations (Last 10):{RESET}")
            cursor.execute('''
                SELECT timestamp, category, operation
                FROM log_entries
                ORDER BY timestamp DESC LIMIT 10
            ''')
            for timestamp, category, operation in cursor.fetchall():
                print(f"  [{timestamp}] {category}: {operation}")

            # Cache statistics
            print(f"\n{BOLD}Cache Performance:{RESET}")
            cursor.execute("SELECT COUNT(*), SUM(access_count) FROM swap_cache WHERE datetime(expires_at) > datetime('now')")
            cache_count, total_hits = cursor.fetchone()
            print(f"  Active Entries: {cache_count}")
            print(f"  Total Cache Hits: {total_hits or 0}")

            # File tracking
            print(f"\n{BOLD}File Tracking:{RESET}")
            cursor.execute("SELECT file_type, COUNT(*) FROM file_tracking GROUP BY file_type")
            for file_type, count in cursor.fetchall():
                print(f"  {file_type or 'Unknown'}: {count}")

            # Database size
            db_size = os.path.getsize(DB_FILE) / 1024  # KB
            print(f"\n{BOLD}Database Size:{RESET} {db_size:.2f} KB")

    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _file_tracking_browser():
    """Browse tracked files."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📂 File Tracking Browser")

    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT file_path, file_type, file_size, last_accessed, access_count
                FROM file_tracking
                ORDER BY last_accessed DESC
            ''')
            results = cursor.fetchall()

        if results:
            page_size = 8
            page = 0
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print_header("📂 File Tracking Browser")
                start = page * page_size
                end = start + page_size
                page_items = results[start:end]
                print(f"\n{BOLD}Page {page + 1}/{(len(results) - 1) // page_size + 1}:{RESET}\n")
                for file_path, file_type, file_size, last_accessed, access_count in page_items:
                    size_mb = file_size / (1024 * 1024) if file_size else 0
                    print(f"{COLORS['6'][0]}{os.path.basename(file_path)}{RESET}")
                    print(f"  Path: {file_path}")
                    print(f"  Type: {file_type or 'Unknown'} | Size: {size_mb:.2f} MB")
                    print(f"  Last Accessed: {last_accessed} | Access Count: {access_count}")
                    print()

                print("[N]ext  [P]rev  [B]ack")
                cmd = input("Select: ").strip().lower()
                if cmd == 'b':
                    break
                if cmd == 'n' and end < len(results):
                    page += 1
                elif cmd == 'p' and page > 0:
                    page -= 1
        else:
            print(f"\n{COLORS['4'][0]}No tracked files yet{RESET}")
    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _swap_cache_management():
    """Manage swap cache system."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🚀 Swap Cache Management")

    try:
        with _db_connect() as conn:
            cursor = conn.cursor()

            # Active cache entries
            cursor.execute('''
                SELECT cache_key, created_at, expires_at, access_count
                FROM swap_cache
                WHERE datetime(expires_at) > datetime('now')
                ORDER BY access_count DESC
            ''')

            results = cursor.fetchall()

        print(f"\n{BOLD}Active Cache Entries:{RESET}\n")
        if results:
            for cache_key, created_at, expires_at, access_count in results:
                print(f"{COLORS['2'][0]}{cache_key}{RESET}")
                print(f"  Created: {created_at} | Expires: {expires_at}")
                print(f"  Access Count: {access_count}")
                print()
        else:
            print(f"{COLORS['4'][0]}No active cache entries{RESET}")

            # Expired entries count
            cursor.execute("SELECT COUNT(*) FROM swap_cache WHERE datetime(expires_at) <= datetime('now')")
            expired_count = cursor.fetchone()[0]

        if expired_count > 0:
            print(f"\n{COLORS['4'][0]}⚠️ {expired_count} expired cache entries found{RESET}")
            clean = input(f"{BOLD}Clean expired entries? (y/n): {RESET}").strip().lower()
            if clean == 'y':
                deleted = clean_expired_cache()
                print(f"{COLORS['2'][0]}✅ Cleaned {deleted} expired entries{RESET}")
    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _export_database():
    """Export database to SQL or JSON."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("💾 Export Database")

    print(f"\n{BOLD}Export Format:{RESET}")
    print(f" {BOLD}[1]{RESET} SQL Dump")
    print(f" {BOLD}[2]{RESET} JSON Export (All Tables)")
    print(f" {BOLD}[3]{RESET} CSV Export (Logs Only)")

    choice = input(f"\n{BOLD}Select format: {RESET}").strip()

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        if choice == '1':
            # SQL Dump
            export_file = os.path.join(DB_DIR, f"pythonOS_export_{timestamp}.sql")
            with _db_connect() as conn:
                with open(export_file, 'w') as f:
                    for line in conn.iterdump():
                        f.write(f"{line}\n")
            print(f"\n{COLORS['2'][0]}✅ Exported to: {export_file}{RESET}")

        elif choice == '2':
            # JSON Export
            export_file = os.path.join(DB_DIR, f"pythonOS_export_{timestamp}.json")
            with _db_connect() as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()

            export_data = {}
            for table in ['log_entries', 'file_tracking', 'swap_cache', 'session_history']:
                cursor.execute(f"SELECT * FROM {table}")
                export_data[table] = [dict(row) for row in cursor.fetchall()]

            with open(export_file, 'w') as f:
                json.dump(export_data, f, indent=2)
            print(f"\n{COLORS['2'][0]}✅ Exported to: {export_file}{RESET}")

        elif choice == '3':
            # CSV Export (Logs)
            export_file = os.path.join(DB_DIR, f"pythonOS_logs_{timestamp}.csv")
            with _db_connect() as conn:
                cursor = conn.cursor()

            cursor.execute("SELECT * FROM log_entries")
            rows = cursor.fetchall()

            with open(export_file, 'w') as f:
                f.write("ID,Timestamp,Category,Operation,Data,FilePath,Status\n")
                for row in rows:
                    # Escape commas and quotes in data
                    escaped_row = [str(field).replace('"', '""') if field else '' for field in row]
                    f.write(','.join(f'"{field}"' for field in escaped_row) + '\n')

            print(f"\n{COLORS['2'][0]}✅ Exported to: {export_file}{RESET}")
    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Export error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _import_data():
    """Import data from JSON."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📥 Import Data")

    import_file = input(f"\n{BOLD}Enter JSON file path: {RESET}").strip()

    if not os.path.exists(import_file):
        print(f"{COLORS['1'][0]}❌ File not found{RESET}")
        input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")
        return

    try:
        with open(import_file, 'r') as f:
            import_data = json.load(f)

        with _db_connect() as conn:
            cursor = conn.cursor()

        imported_count = 0
        for table, records in import_data.items():
            if table in ['log_entries', 'file_tracking', 'swap_cache', 'session_history']:
                for record in records:
                    try:
                        columns = ', '.join(record.keys())
                        placeholders = ', '.join(['?' for _ in record])
                        values = tuple(record.values())

                        cursor.execute(f"INSERT OR IGNORE INTO {table} ({columns}) VALUES ({placeholders})", values)
                        imported_count += 1
                    except:
                        pass

            conn.commit()

        print(f"\n{COLORS['2'][0]}✅ Imported {imported_count} records{RESET}")
    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Import error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _clean_optimize():
    """Clean and optimize database."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🧹 Clean & Optimize")

    print(f"\n{BOLD}Optimization Options:{RESET}")
    print(f" {BOLD}[1]{RESET} Clean expired cache entries")
    print(f" {BOLD}[2]{RESET} Delete old logs (>30 days)")
    print(f" {BOLD}[3]{RESET} Vacuum database (reclaim space)")
    print(f" {BOLD}[4]{RESET} Full cleanup (all above)")

    choice = input(f"\n{BOLD}Select option: {RESET}").strip()

    try:
        with _db_connect() as conn:
            cursor = conn.cursor()

        if choice in ['1', '4']:
            cursor.execute("DELETE FROM swap_cache WHERE datetime(expires_at) <= datetime('now')")
            deleted_cache = cursor.rowcount
            print(f"{COLORS['2'][0]}✅ Deleted {deleted_cache} expired cache entries{RESET}")

        if choice in ['2', '4']:
            cursor.execute("DELETE FROM log_entries WHERE datetime(timestamp) <= datetime('now', '-30 days')")
            deleted_logs = cursor.rowcount
            print(f"{COLORS['2'][0]}✅ Deleted {deleted_logs} old log entries{RESET}")

        if choice in ['3', '4']:
            cursor.execute("VACUUM")
            print(f"{COLORS['2'][0]}✅ Database vacuumed and optimized{RESET}")

            conn.commit()
    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Optimization error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _database_settings():
    """Database settings and configuration."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("⚙️ Database Settings")

    print(f"\n{BOLD}Database Information:{RESET}")
    print(f"  Location: {DB_FILE}")
    print(f"  Log Directory: {LOG_DIR}")
    print(f"  Swap Cache: {SWAP_CACHE_DIR}")

    if os.path.exists(DB_FILE):
        db_size = os.path.getsize(DB_FILE) / 1024
        print(f"  Size: {db_size:.2f} KB")

    print(f"\n{BOLD}Actions:{RESET}")
    print(f" {BOLD}[1]{RESET} Reset Database (⚠️ Deletes all data)")
    print(f" {BOLD}[2]{RESET} Backup Database")
    print(f" {BOLD}[3]{RESET} Open Database Directory")

    choice = input(f"\n{BOLD}Select action: {RESET}").strip()

    if choice == '1':
        confirm = input(f"{COLORS['1'][0]}⚠️ This will delete ALL data! Confirm (yes/no): {RESET}").strip().lower()
        if confirm == 'yes':
            try:
                if os.path.exists(DB_FILE):
                    os.remove(DB_FILE)
                init_database_system()
                print(f"{COLORS['2'][0]}✅ Database reset successfully{RESET}")
            except Exception as e:
                print(f"{COLORS['1'][0]}❌ Reset error: {e}{RESET}")

    elif choice == '2':
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = os.path.join(DB_DIR, f"pythonOS_backup_{timestamp}.db")
            shutil.copy2(DB_FILE, backup_file)
            print(f"{COLORS['2'][0]}✅ Backup created: {backup_file}{RESET}")
        except Exception as e:
            print(f"{COLORS['1'][0]}❌ Backup error: {e}{RESET}")

    elif choice == '3':
        print(f"\n{COLORS['6'][0]}Opening: {DB_DIR}{RESET}")
        if os.name == 'posix':
            os.system(f"xdg-open '{DB_DIR}' 2>/dev/null || nautilus '{DB_DIR}' 2>/dev/null || echo 'Please open manually'")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _db_execute_sql(cursor, sql):
    cmd = sql.strip().rstrip(';')
    if not cmd:
        return None, None
    lower = cmd.lower()
    if lower.startswith("select") or lower.startswith("pragma"):
        cursor.execute(cmd)
        rows = cursor.fetchall()
        cols = [d[0] for d in cursor.description] if cursor.description else []
        return cols, rows
    cursor.execute(cmd)
    return None, cursor.rowcount

def _db_interactive_sql_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🧠 SQL Console")
    print("Enter SQL statements. Type 'run' on a blank line to execute.")
    print("Type 'exit' to return.")

    buffer = []
    with _db_connect() as conn:
        cursor = conn.cursor()
        while True:
            line = input("SQL> ").strip()
            if line.lower() == 'exit':
                break
            if line.lower() == 'run':
                sql = "\n".join(buffer)
                buffer = []
                try:
                    cols, result = _db_execute_sql(cursor, sql)
                    if cols is not None:
                        print(" | ".join(cols))
                        print("-" * max(20, len(" | ".join(cols))))
                        for row in result[:50]:
                            print(" | ".join(str(x) for x in row))
                        if len(result) > 50:
                            print(f"... ({len(result)} rows total)")
                    else:
                        conn.commit()
                        print(f"✅ Rows affected: {result}")
                except Exception as e:
                    print(f"❌ SQL error: {e}")
                continue
            buffer.append(line)

def _db_table_manager():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🧱 Table Manager")
        print(" [1] Create Table")
        print(" [2] Alter Table (Add Column)")
        print(" [3] Drop Table")
        print(" [4] List Tables")
        print(" [0] Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            break
        try:
            with _db_connect() as conn:
                cursor = conn.cursor()
                if choice == '1':
                    name = input("Table name: ").strip()
                    cols = input("Columns (e.g., id INTEGER PRIMARY KEY, name TEXT): ").strip()
                    if name and cols:
                        cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({cols})")
                        conn.commit()
                        print("✅ Table created/verified.")
                elif choice == '2':
                    name = input("Table name: ").strip()
                    col = input("New column (e.g., status TEXT): ").strip()
                    if name and col:
                        cursor.execute(f"ALTER TABLE {name} ADD COLUMN {col}")
                        conn.commit()
                        print("✅ Column added.")
                elif choice == '3':
                    name = input("Table name to drop: ").strip()
                    confirm = input("Type DELETE to confirm: ").strip()
                    if confirm == "DELETE" and name:
                        cursor.execute(f"DROP TABLE IF EXISTS {name}")
                        conn.commit()
                        print("✅ Table dropped.")
                elif choice == '4':
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
                    tables = [r[0] for r in cursor.fetchall()]
                    print("\nTables:")
                    for t in tables:
                        print(f" - {t}")
                else:
                    print("Invalid option")
        except Exception as e:
            print(f"❌ Error: {e}")
        input("\nPress Enter to continue...")

def _db_transaction_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🔐 Transaction Console")
    print("Enter SQL statements. Type 'commit' or 'rollback' to finish.")
    print("Type 'exit' to return without changes.")

    with _db_connect() as conn:
        cursor = conn.cursor()
        conn.execute("BEGIN")
        while True:
            line = input("TX> ").strip()
            if line.lower() == 'exit':
                conn.rollback()
                break
            if line.lower() == 'commit':
                conn.commit()
                print("✅ Transaction committed.")
                break
            if line.lower() == 'rollback':
                conn.rollback()
                print("✅ Transaction rolled back.")
                break
            try:
                cols, result = _db_execute_sql(cursor, line)
                if cols is not None:
                    print(" | ".join(cols))
                    for row in result[:20]:
                        print(" | ".join(str(x) for x in row))
                else:
                    print(f"✅ Rows affected: {result}")
            except Exception as e:
                print(f"❌ SQL error: {e}")

def _db_quick_crud():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🧩 Quick CRUD")
    print(" [1] INSERT")
    print(" [2] UPDATE")
    print(" [3] DELETE")
    print(" [0] Return")
    choice = input("\nSelect option: ").strip()
    if choice == '0':
        return

    table = input("Table: ").strip()
    if not table:
        return
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            if choice == '1':
                cols = input("Columns (comma separated): ").strip()
                vals = input("Values (comma separated, use quotes for text): ").strip()
                if cols and vals:
                    cursor.execute(f"INSERT INTO {table} ({cols}) VALUES ({vals})")
                    conn.commit()
                    print("✅ Inserted.")
            elif choice == '2':
                set_clause = input("SET clause (e.g., name='x'): ").strip()
                where = input("WHERE clause (optional): ").strip()
                sql = f"UPDATE {table} SET {set_clause}"
                if where:
                    sql += f" WHERE {where}"
                cursor.execute(sql)
                conn.commit()
                print(f"✅ Updated {cursor.rowcount} rows.")
            elif choice == '3':
                where = input("WHERE clause (optional): ").strip()
                sql = f"DELETE FROM {table}"
                if where:
                    sql += f" WHERE {where}"
                cursor.execute(sql)
                conn.commit()
                print(f"✅ Deleted {cursor.rowcount} rows.")
    except Exception as e:
        print(f"❌ CRUD error: {e}")
    input("\nPress Enter to continue...")

def _db_export_table_csv():
    table = input("Table to export: ").strip()
    if not table:
        return
    export_file = os.path.join(DB_DIR, f"{table}_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            cols = [d[0] for d in cursor.description]
        with open(export_file, 'w') as f:
            f.write(','.join(cols) + '\n')
            for row in rows:
                escaped = [str(x).replace('"', '""') if x is not None else '' for x in row]
                f.write(','.join(f'"{x}"' for x in escaped) + '\n')
        print(f"✅ Exported: {export_file}")
    except Exception as e:
        print(f"❌ Export error: {e}")

def _db_import_csv():
    csv_path = input("CSV file path: ").strip()
    table = input("Target table name: ").strip()
    if not csv_path or not table:
        return
    if not os.path.exists(csv_path):
        print("❌ File not found")
        return
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            with open(csv_path, 'r') as f:
                header = f.readline().strip().split(',')
                header = [h.strip().strip('"') for h in header]
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({', '.join(h + ' TEXT' for h in header)})")
                for line in f:
                    parts = [p.strip().strip('"') for p in line.split(',')]
                    placeholders = ','.join(['?' for _ in parts])
                    cursor.execute(f"INSERT INTO {table} ({', '.join(header)}) VALUES ({placeholders})", parts)
            conn.commit()
            print("✅ CSV imported.")
    except Exception as e:
        print(f"❌ Import error: {e}")

def _db_generate_report():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📊 Report Generator")
    print(" [1] CSV report (log_entries)")
    print(" [2] JSON report (log_entries)")
    print(" [3] PDF report (if reportlab installed)")
    print(" [0] Return")
    choice = input("\nSelect option: ").strip()
    if choice == '0':
        return

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT timestamp, category, operation, data, status FROM log_entries ORDER BY timestamp DESC")
            rows = cursor.fetchall()
        if choice == '1':
            out = os.path.join(DB_DIR, f"ai_report_{timestamp}.csv")
            with open(out, 'w') as f:
                f.write("timestamp,category,operation,data,status\n")
                for r in rows:
                    esc = [str(x).replace('"', '""') if x is not None else '' for x in r]
                    f.write(','.join(f'"{x}"' for x in esc) + '\n')
            print(f"✅ CSV report: {out}")
        elif choice == '2':
            out = os.path.join(DB_DIR, f"ai_report_{timestamp}.json")
            data = [
                {
                    "timestamp": r[0],
                    "category": r[1],
                    "operation": r[2],
                    "data": r[3],
                    "status": r[4]
                }
                for r in rows
            ]
            with open(out, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"✅ JSON report: {out}")
        elif choice == '3':
            try:
                from reportlab.lib.pagesizes import letter
                from reportlab.pdfgen import canvas
                out = os.path.join(DB_DIR, f"ai_report_{timestamp}.pdf")
                c = canvas.Canvas(out, pagesize=letter)
                width, height = letter
                y = height - 40
                c.setFont("Helvetica", 10)
                c.drawString(40, y, "pythonOS AI Report")
                y -= 20
                for r in rows[:200]:
                    line = f"{r[0]} | {r[1]} | {r[2]}"
                    c.drawString(40, y, line[:120])
                    y -= 12
                    if y < 40:
                        c.showPage()
                        c.setFont("Helvetica", 10)
                        y = height - 40
                c.save()
                print(f"✅ PDF report: {out}")
            except Exception:
                print("❌ reportlab not installed. Use CSV/JSON instead.")
        else:
            print("Invalid option")
    except Exception as e:
        print(f"❌ Report error: {e}")
    input("\nPress Enter to continue...")

def _db_clean_transform():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🧽 Data Cleaning & Transformation")
    print(" [1] Trim whitespace in log_entries.data")
    print(" [2] Normalize category to lowercase")
    print(" [3] Remove empty log entries (no data)")
    print(" [0] Return")
    choice = input("\nSelect option: ").strip()
    if choice == '0':
        return
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            if choice == '1':
                cursor.execute("UPDATE log_entries SET data = TRIM(data) WHERE data IS NOT NULL")
            elif choice == '2':
                cursor.execute("UPDATE log_entries SET category = LOWER(category) WHERE category IS NOT NULL")
            elif choice == '3':
                cursor.execute("DELETE FROM log_entries WHERE data IS NULL OR TRIM(data) = ''")
            else:
                print("Invalid option")
                return
            conn.commit()
            print(f"✅ Rows affected: {cursor.rowcount}")
    except Exception as e:
        print(f"❌ Cleaning error: {e}")
    input("\nPress Enter to continue...")

def _db_run_scheduled_tasks():
    global _db_scheduler_running
    while _db_scheduler_running:
        now = time.time()
        for task in _db_scheduled_tasks:
            if now >= task["next_run"]:
                try:
                    task["action"]()
                except Exception:
                    pass
                task["next_run"] = now + task["interval"]
        time.sleep(1)

def _db_schedule_tasks_menu():
    global _db_scheduler_running
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("⏱️ Task Scheduler")
    print(" [1] Schedule backup (every 30 min)")
    print(" [2] Schedule clean expired cache (every 15 min)")
    print(" [3] Schedule vacuum (every 6 hrs)")
    print(" [4] Stop scheduler")
    print(" [0] Return")
    choice = input("\nSelect option: ").strip()

    def _backup_action():
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(DB_DIR, f"pythonOS_backup_{timestamp}.db")
        try:
            shutil.copy2(DB_FILE, backup_file)
        except Exception:
            pass

    def _clean_cache_action():
        try:
            clean_expired_cache()
        except Exception:
            pass

    def _vacuum_action():
        try:
            with _db_connect() as conn:
                cursor = conn.cursor()
                cursor.execute("VACUUM")
                conn.commit()
        except Exception:
            pass

    if choice == '1':
        _db_scheduled_tasks.append({"interval": 1800, "next_run": time.time() + 5, "action": _backup_action})
        print("✅ Backup scheduled.")
    elif choice == '2':
        _db_scheduled_tasks.append({"interval": 900, "next_run": time.time() + 5, "action": _clean_cache_action})
        print("✅ Cache cleanup scheduled.")
    elif choice == '3':
        _db_scheduled_tasks.append({"interval": 21600, "next_run": time.time() + 5, "action": _vacuum_action})
        print("✅ Vacuum scheduled.")
    elif choice == '4':
        _db_scheduler_running = False
        print("✅ Scheduler stopped.")
    if not _db_scheduler_running and _db_scheduled_tasks:
        _db_scheduler_running = True
        threading.Thread(target=_db_run_scheduled_tasks, daemon=True).start()
    input("\nPress Enter to continue...")

def _db_analysis_dashboard():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📈 Analysis & Visualization")
    with _db_connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT category, COUNT(*) FROM log_entries GROUP BY category ORDER BY COUNT(*) DESC")
        rows = cursor.fetchall()
    if not rows:
        print("No log data to analyze.")
        input("\nPress Enter to continue...")
        return
    print("\nLog Entries by Category:")
    max_count = max(r[1] for r in rows)
    for cat, count in rows:
        bar = "#" * int((count / max_count) * 40)
        print(f" {cat:<16} {count:>6} | {bar}")
    input("\nPress Enter to continue...")

def _db_ml_probe():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🧪 ML Integration")
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.cluster import KMeans
    except Exception:
        print("scikit-learn not installed. Install via Download Center > Data Science.")
        input("\nPress Enter to continue...")
        return

    with _db_connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT operation, data FROM log_entries WHERE data IS NOT NULL ORDER BY timestamp DESC LIMIT 200")
        rows = cursor.fetchall()
    texts = [f"{r[0]} {r[1]}" for r in rows if r[1]]
    if len(texts) < 10:
        print("Not enough data for ML clustering.")
        input("\nPress Enter to continue...")
        return
    vectorizer = TfidfVectorizer(max_features=200)
    X = vectorizer.fit_transform(texts)
    k = 3
    model = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = model.fit_predict(X)
    counts = {i: 0 for i in range(k)}
    for label in labels:
        counts[label] += 1
    print("Cluster Distribution:")
    for i in range(k):
        print(f" Cluster {i}: {counts[i]} entries")
    input("\nPress Enter to continue...")

class _DBApiHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_GET(self):
        try:
            if self.path.startswith("/stats"):
                with _db_connect() as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT COUNT(*) FROM log_entries")
                    log_count = cursor.fetchone()[0]
                    cursor.execute("SELECT COUNT(*) FROM file_tracking")
                    file_count = cursor.fetchone()[0]
                payload = {
                    "log_entries": log_count,
                    "file_tracking": file_count,
                    "timestamp": datetime.datetime.now().isoformat()
                }
                data = json.dumps(payload).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
                return
        except Exception:
            pass
        self.send_response(404)
        self.end_headers()

def _db_api_server_start():
    global _db_api_server
    if _db_api_server is not None:
        print("API server already running.")
        return
    def run_server():
        global _db_api_server
        _db_api_server = HTTPServer(("0.0.0.0", DB_API_PORT), _DBApiHandler)
        _db_api_server.serve_forever()
    threading.Thread(target=run_server, daemon=True).start()
    print(f"✅ DB API running on port {DB_API_PORT} (path: /stats)")

def _db_orm_view():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🧬 ORM View (Lightweight)")
    with _db_connect() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM log_entries ORDER BY timestamp DESC LIMIT 5")
        rows = cursor.fetchall()
    for row in rows:
        print(dict(row))
    input("\nPress Enter to continue...")

def _advanced_database_suite():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🧭 Advanced Database Suite")
        print(" [1] Core DB Operations (CRUD + SQL + Tables + Transactions)")
        print(" [2] Data Management & Automation")
        print(" [3] Advanced Analysis & App Dev")
        print(" [0] Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print_header("⚙️ Core DB Operations")
                print(" [1] SQL Console")
                print(" [2] Table Manager")
                print(" [3] Quick CRUD")
                print(" [4] Transaction Console")
                print(" [0] Return")
                sub = input("\nSelect option: ").strip()
                if sub == '0':
                    break
                if sub == '1':
                    _db_interactive_sql_console()
                elif sub == '2':
                    _db_table_manager()
                elif sub == '3':
                    _db_quick_crud()
                elif sub == '4':
                    _db_transaction_console()
        elif choice == '2':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print_header("🧰 Data Management & Automation")
                print(" [1] Backup Database")
                print(" [2] Restore Database")
                print(" [3] Export Table to CSV")
                print(" [4] Import CSV to Table")
                print(" [5] Data Cleaning & Transformation")
                print(" [6] Report Generation")
                print(" [7] Task Scheduler")
                print(" [0] Return")
                sub = input("\nSelect option: ").strip()
                if sub == '0':
                    break
                if sub == '1':
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_file = os.path.join(DB_DIR, f"pythonOS_backup_{timestamp}.db")
                    try:
                        shutil.copy2(DB_FILE, backup_file)
                        print(f"✅ Backup created: {backup_file}")
                    except Exception as e:
                        print(f"❌ Backup error: {e}")
                    input("\nPress Enter to continue...")
                elif sub == '2':
                    path = input("Backup file path: ").strip()
                    if os.path.exists(path):
                        confirm = input("Type RESTORE to confirm: ").strip()
                        if confirm == "RESTORE":
                            try:
                                shutil.copy2(path, DB_FILE)
                                print("✅ Database restored.")
                            except Exception as e:
                                print(f"❌ Restore error: {e}")
                    else:
                        print("❌ File not found")
                    input("\nPress Enter to continue...")
                elif sub == '3':
                    _db_export_table_csv()
                    input("\nPress Enter to continue...")
                elif sub == '4':
                    _db_import_csv()
                    input("\nPress Enter to continue...")
                elif sub == '5':
                    _db_clean_transform()
                elif sub == '6':
                    _db_generate_report()
                elif sub == '7':
                    _db_schedule_tasks_menu()
        elif choice == '3':
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print_header("🔬 Advanced Analysis & App Dev")
                print(" [1] ORM View (lightweight)")
                print(" [2] Data Analysis & Visualization")
                print(" [3] ML Integration")
                print(" [4] Start DB API Server")
                print(" [0] Return")
                sub = input("\nSelect option: ").strip()
                if sub == '0':
                    break
                if sub == '1':
                    _db_orm_view()
                elif sub == '2':
                    _db_analysis_dashboard()
                elif sub == '3':
                    _db_ml_probe()
                elif sub == '4':
                    _db_api_server_start()
                    input("\nPress Enter to continue...")

def _lite_scan():
    """Quick system snapshot - essential data capture."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🔍 Lite Scan - Quick System Snapshot")

    print(f"{COLORS['6'][0]}Starting Lite Scan...{RESET}\n")

    scan_data = []
    scan_data.append("=" * 60)
    scan_data.append("LITE SYSTEM SCAN REPORT")
    scan_data.append("=" * 60)
    scan_data.append(f"Scan Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    scan_data.append("\n" + "=" * 60)

    # 1. Basic System Info
    print(f"{COLORS['2'][0]}[1/5] Collecting System Information...{RESET}")
    scan_data.append("\n[SYSTEM INFORMATION]")
    scan_data.append(f"OS: {platform.system()} {platform.release()}")
    scan_data.append(f"Architecture: {platform.machine()}")
    scan_data.append(f"Processor: {platform.processor()}")
    scan_data.append(f"Node: {platform.node()}")
    scan_data.append(f"Python Version: {platform.python_version()}")

    # 2. CPU & Memory
    print(f"{COLORS['2'][0]}[2/5] Scanning CPU & Memory...{RESET}")
    scan_data.append("\n[CPU & MEMORY]")
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    scan_data.append(f"CPU Usage: {cpu_percent}%")
    scan_data.append(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    scan_data.append(f"Total Threads: {psutil.cpu_count(logical=True)}")
    scan_data.append(f"Total RAM: {mem.total / (1024**3):.2f} GB")
    scan_data.append(f"Available RAM: {mem.available / (1024**3):.2f} GB")
    scan_data.append(f"RAM Usage: {mem.percent}%")

    # 3. Disk Info
    print(f"{COLORS['2'][0]}[3/5] Checking Disk Storage...{RESET}")
    scan_data.append("\n[DISK STORAGE]")
    disk = psutil.disk_usage('/')
    scan_data.append(f"Total Space: {disk.total / (1024**3):.2f} GB")
    scan_data.append(f"Used Space: {disk.used / (1024**3):.2f} GB ({disk.percent}%)")
    scan_data.append(f"Free Space: {disk.free / (1024**3):.2f} GB")

    # 4. Network Info
    print(f"{COLORS['2'][0]}[4/5] Collecting Network Data...{RESET}")
    scan_data.append("\n[NETWORK INFORMATION]")
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        scan_data.append(f"Hostname: {hostname}")
        scan_data.append(f"Local IP: {local_ip}")
    except:
        scan_data.append("Network info unavailable")

    net_io = psutil.net_io_counters()
    scan_data.append(f"Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
    scan_data.append(f"Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")

    # 5. Top Processes
    print(f"{COLORS['2'][0]}[5/5] Scanning Top Processes...{RESET}")
    scan_data.append("\n[TOP 10 PROCESSES BY MEMORY]")
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            procs.append(p.info)
        except:
            continue
    procs.sort(key=lambda x: x['memory_percent'] or 0, reverse=True)
    for p in procs[:10]:
        scan_data.append(f"  {p['name'][:30]:30} - PID: {p['pid']} - MEM: {p['memory_percent']:.2f}%")

    scan_data.append("\n" + "=" * 60)
    scan_data.append("END OF LITE SCAN")
    scan_data.append("=" * 60)

    # Save to database and file
    full_content = "\n".join(scan_data)
    print(f"\n{COLORS['2'][0]}✅ Lite Scan Complete!{RESET}")
    print(f"\nCollected {len(scan_data)} data points.")

    # Save to system category
    file_path = save_log_file("system", "Lite_Scan", full_content, prompt_user=False)

    if file_path:
        print(f"{COLORS['6'][0]}📁 Report saved to: {file_path}{RESET}")
        log_to_database("system", "Lite_Scan_Complete", f"Collected {len(scan_data)} data points", file_path)

    # Show preview
    preview = input(f"\n{BOLD}View scan summary? (y/n): {RESET}").strip().lower()
    if preview == 'y':
        print(f"\n{COLORS['6'][0]}" + "\n".join(scan_data[:50]) + f"{RESET}")
        if len(scan_data) > 50:
            print(f"\n... (showing first 50 lines, full report saved to file)")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _aggressive_scan():
    """Deep intelligence gathering - comprehensive system scan."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🚨 Aggressive Scan - Deep Intelligence Gathering")

    print(f"{COLORS['1'][0]}⚠️  WARNING: This scan will collect extensive system data{RESET}")
    print(f"{COLORS['4'][0]}This may take several minutes...{RESET}\n")

    confirm = input(f"{BOLD}Proceed with aggressive scan? (yes/no): {RESET}").strip().lower()
    if confirm != 'yes':
        print(f"{COLORS['4'][0]}Scan cancelled.{RESET}")
        input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")
        return

    print(f"\n{COLORS['6'][0]}🚀 Initiating Deep Scan Protocol...{RESET}\n")

    scan_data = []
    scan_data.append("=" * 80)
    scan_data.append("AGGRESSIVE INTELLIGENCE SCAN - COMPREHENSIVE SYSTEM ANALYSIS")
    scan_data.append("=" * 80)
    scan_data.append(f"Scan Initiated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    scan_data.append(f"Scan Profile: AGGRESSIVE (Maximum Data Collection)")
    scan_data.append("=" * 80)

    # 1. System Intelligence
    print(f"{COLORS['2'][0]}[1/12] 🖥️  Deep System Analysis...{RESET}")
    scan_data.append("\n" + "="*80)
    scan_data.append("[SECTION 1: SYSTEM INTELLIGENCE]")
    scan_data.append("="*80)
    scan_data.append(f"Operating System: {platform.system()} {platform.release()} {platform.version()}")
    scan_data.append(f"Architecture: {platform.machine()} ({platform.architecture()[0]})")
    scan_data.append(f"Processor: {platform.processor()}")
    scan_data.append(f"Node Name: {platform.node()}")
    scan_data.append(f"Python Implementation: {platform.python_implementation()}")
    scan_data.append(f"Python Version: {platform.python_version()}")
    scan_data.append(f"Python Compiler: {platform.python_compiler()}")

    try:
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.datetime.now() - boot_time
        scan_data.append(f"System Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
        scan_data.append(f"Uptime: {str(uptime).split('.')[0]}")
    except:
        pass

    # 2. CPU Deep Dive
    print(f"{COLORS['2'][0]}[2/12] 🧠 CPU Deep Analysis...{RESET}")
    scan_data.append("\n[SECTION 2: CPU ANALYSIS]")
    scan_data.append(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    scan_data.append(f"Total Threads: {psutil.cpu_count(logical=True)}")
    try:
        freq = psutil.cpu_freq()
        if freq:
            scan_data.append(f"Current Frequency: {freq.current:.2f} MHz")
            scan_data.append(f"Min Frequency: {freq.min:.2f} MHz")
            scan_data.append(f"Max Frequency: {freq.max:.2f} MHz")
    except:
        pass

    cpu_percent = psutil.cpu_percent(interval=2, percpu=True)
    scan_data.append(f"CPU Usage (Overall): {sum(cpu_percent)/len(cpu_percent):.2f}%")
    for i, pct in enumerate(cpu_percent):
        scan_data.append(f"  Core {i}: {pct}%")

    # 3. Memory Deep Dive
    print(f"{COLORS['2'][0]}[3/12] 💾 Memory Deep Analysis...{RESET}")
    scan_data.append("\n[SECTION 3: MEMORY ANALYSIS]")
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    scan_data.append(f"Total RAM: {mem.total / (1024**3):.2f} GB")
    scan_data.append(f"Available RAM: {mem.available / (1024**3):.2f} GB")
    scan_data.append(f"Used RAM: {mem.used / (1024**3):.2f} GB ({mem.percent}%)")
    scan_data.append(f"Free RAM: {mem.free / (1024**3):.2f} GB")
    scan_data.append(f"Buffers: {mem.buffers / (1024**2):.2f} MB" if hasattr(mem, 'buffers') else "Buffers: N/A")
    scan_data.append(f"Cached: {mem.cached / (1024**2):.2f} MB" if hasattr(mem, 'cached') else "Cached: N/A")
    scan_data.append(f"\nSwap Total: {swap.total / (1024**3):.2f} GB")
    scan_data.append(f"Swap Used: {swap.used / (1024**3):.2f} GB ({swap.percent}%)")
    scan_data.append(f"Swap Free: {swap.free / (1024**3):.2f} GB")

    # 4. Disk Intelligence
    print(f"{COLORS['2'][0]}[4/12] 💽 Disk Deep Analysis...{RESET}")
    scan_data.append("\n[SECTION 4: DISK INTELLIGENCE]")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        scan_data.append(f"\nPartition: {partition.device}")
        scan_data.append(f"  Mountpoint: {partition.mountpoint}")
        scan_data.append(f"  File System: {partition.fstype}")
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            scan_data.append(f"  Total: {usage.total / (1024**3):.2f} GB")
            scan_data.append(f"  Used: {usage.used / (1024**3):.2f} GB ({usage.percent}%)")
            scan_data.append(f"  Free: {usage.free / (1024**3):.2f} GB")
        except:
            scan_data.append("  Access denied or unavailable")

    disk_io = psutil.disk_io_counters()
    if disk_io:
        scan_data.append(f"\nDisk I/O Statistics:")
        scan_data.append(f"  Read: {disk_io.read_bytes / (1024**3):.2f} GB")
        scan_data.append(f"  Written: {disk_io.write_bytes / (1024**3):.2f} GB")
        scan_data.append(f"  Read Count: {disk_io.read_count}")
        scan_data.append(f"  Write Count: {disk_io.write_count}")

    # 5. Network Deep Intelligence
    print(f"{COLORS['2'][0]}[5/12] 🌐 Network Deep Analysis...{RESET}")
    scan_data.append("\n[SECTION 5: NETWORK INTELLIGENCE]")
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        scan_data.append(f"Hostname: {hostname}")
        scan_data.append(f"Local IP: {local_ip}")
    except:
        scan_data.append("Basic network info unavailable")

    # MAC Address
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    scan_data.append(f"MAC Address: {mac}")

    # Network Interfaces
    net_if_addrs = psutil.net_if_addrs()
    scan_data.append("\nNetwork Interfaces:")
    for interface, addrs in net_if_addrs.items():
        scan_data.append(f"  Interface: {interface}")
        for addr in addrs:
            scan_data.append(f"    Family: {addr.family}, Address: {addr.address}")

    # Network I/O
    net_io = psutil.net_io_counters()
    scan_data.append(f"\nNetwork I/O:")
    scan_data.append(f"  Bytes Sent: {net_io.bytes_sent / (1024**2):.2f} MB")
    scan_data.append(f"  Bytes Received: {net_io.bytes_recv / (1024**2):.2f} MB")
    scan_data.append(f"  Packets Sent: {net_io.packets_sent}")
    scan_data.append(f"  Packets Received: {net_io.packets_recv}")
    scan_data.append(f"  Errors In: {net_io.errin}")
    scan_data.append(f"  Errors Out: {net_io.errout}")

    # 6. Process Intelligence
    print(f"{COLORS['2'][0]}[6/12] 📋 Process Deep Analysis...{RESET}")
    scan_data.append("\n[SECTION 6: PROCESS INTELLIGENCE]")
    all_procs = []
    for p in psutil.process_iter(['pid', 'name', 'username', 'memory_percent', 'cpu_percent', 'status', 'create_time']):
        try:
            all_procs.append(p.info)
        except:
            continue

    scan_data.append(f"Total Running Processes: {len(all_procs)}")
    scan_data.append(f"\nTop 20 Processes by Memory:")
    all_procs.sort(key=lambda x: x['memory_percent'] or 0, reverse=True)
    for i, p in enumerate(all_procs[:20], 1):
        try:
            created = datetime.datetime.fromtimestamp(p['create_time']).strftime('%Y-%m-%d %H:%M')
        except:
            created = 'Unknown'
        scan_data.append(f"  {i}. {p['name'][:30]:30} | PID: {p['pid']:6} | MEM: {p['memory_percent']:.2f}% | USER: {p['username']} | Created: {created}")

    # 7. Weather & Geolocation
    print(f"{COLORS['2'][0]}[7/12] 🌍 Geolocation & Weather...{RESET}")
    scan_data.append("\n[SECTION 7: GEOLOCATION & WEATHER INTELLIGENCE]")
    try:
        geo_data = requests.get("http://ip-api.com/json/", timeout=5).json()
        scan_data.append(f"Public IP: {geo_data.get('query', 'N/A')}")
        scan_data.append(f"Country: {geo_data.get('country', 'N/A')}")
        scan_data.append(f"Region: {geo_data.get('regionName', 'N/A')}")
        scan_data.append(f"City: {geo_data.get('city', 'N/A')}")
        scan_data.append(f"Postal Code: {geo_data.get('zip', 'N/A')}")
        scan_data.append(f"Latitude: {geo_data.get('lat', 'N/A')}")
        scan_data.append(f"Longitude: {geo_data.get('lon', 'N/A')}")
        scan_data.append(f"ISP: {geo_data.get('isp', 'N/A')}")
        scan_data.append(f"Organization: {geo_data.get('org', 'N/A')}")
        scan_data.append(f"AS: {geo_data.get('as', 'N/A')}")
        scan_data.append(f"Timezone: {geo_data.get('timezone', 'N/A')}")
    except:
        scan_data.append("Geolocation data unavailable")

    weather_data = get_weather_data()
    if weather_data:
        scan_data.append(f"\nWeather Data:")
        scan_data.append(f"  Temperature: {weather_data.get('temp', 'N/A')}")
        scan_data.append(f"  Feels Like: {weather_data.get('feels', 'N/A')}")
        scan_data.append(f"  Humidity: {weather_data.get('humidity', 'N/A')}")
        scan_data.append(f"  Wind: {weather_data.get('wind', 'N/A')}")
        scan_data.append(f"  Conditions: {weather_data.get('icon', 'N/A')}")

    # 8. Hardware Sensors
    print(f"{COLORS['2'][0]}[8/12] 🌡️  Hardware Sensors...{RESET}")
    scan_data.append("\n[SECTION 8: HARDWARE SENSORS]")
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            scan_data.append("Temperature Sensors:")
            for name, entries in temps.items():
                for entry in entries:
                    label = entry.label or name
                    scan_data.append(f"  {label}: {entry.current}°C (High: {entry.high}°C, Critical: {entry.critical}°C)")
        else:
            scan_data.append("No temperature sensors detected")
    except:
        scan_data.append("Temperature sensors not available")

    try:
        fans = psutil.sensors_fans()
        if fans:
            scan_data.append("\nFan Sensors:")
            for name, entries in fans.items():
                for entry in entries:
                    label = entry.label or name
                    scan_data.append(f"  {label}: {entry.current} RPM")
        else:
            scan_data.append("No fan sensors detected")
    except:
        scan_data.append("Fan sensors not available")

    try:
        battery = psutil.sensors_battery()
        if battery:
            scan_data.append(f"\nBattery:")
            scan_data.append(f"  Percent: {battery.percent}%")
            scan_data.append(f"  Power Plugged: {battery.power_plugged}")
            scan_data.append(f"  Time Left: {battery.secsleft // 60} minutes" if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "  Time Left: Unlimited")
    except:
        scan_data.append("\nBattery info not available")

    # 9. GPU Information
    print(f"{COLORS['2'][0]}[9/12] 🎮 GPU Analysis...{RESET}")
    scan_data.append("\n[SECTION 9: GPU INTELLIGENCE]")
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            for i, gpu in enumerate(gpus):
                scan_data.append(f"\nGPU {i}: {gpu.name}")
                scan_data.append(f"  Load: {gpu.load*100:.1f}%")
                scan_data.append(f"  Temperature: {gpu.temperature}°C")
                scan_data.append(f"  Memory Total: {gpu.memoryTotal} MB")
                scan_data.append(f"  Memory Used: {gpu.memoryUsed} MB ({gpu.memoryUsed/gpu.memoryTotal*100:.1f}%)")
                scan_data.append(f"  Memory Free: {gpu.memoryFree} MB")
                scan_data.append(f"  Driver: {gpu.driver}")
        else:
            scan_data.append("No discrete GPU detected")
    except:
        scan_data.append("GPU information unavailable")

    # 10. Security Audit
    print(f"{COLORS['2'][0]}[10/12] 🔒 Security Status...{RESET}")
    scan_data.append("\n[SECTION 10: SECURITY AUDIT]")
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389, 5432, 8080, 8443]
    open_ports = []
    for port in common_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            if s.connect_ex(('127.0.0.1', port)) == 0:
                open_ports.append(port)

    scan_data.append(f"Scanned {len(common_ports)} common ports")
    if open_ports:
        scan_data.append(f"Open Ports: {', '.join(map(str, open_ports))}")
    else:
        scan_data.append("No high-risk ports open")

    try:
        is_admin = os.getuid() == 0
    except:
        try:
            import ctypes
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            is_admin = False
    scan_data.append(f"Running as Admin/Root: {is_admin}")

    # 11. Database Statistics
    print(f"{COLORS['2'][0]}[11/12] 📊 Database Intelligence...{RESET}")
    scan_data.append("\n[SECTION 11: DATABASE STATISTICS]")
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM log_entries")
            log_count = cursor.fetchone()[0]
            scan_data.append(f"Total Log Entries: {log_count}")

            cursor.execute("SELECT COUNT(*) FROM file_tracking")
            file_count = cursor.fetchone()[0]
            scan_data.append(f"Tracked Files: {file_count}")

            cursor.execute("SELECT COUNT(*) FROM swap_cache WHERE datetime(expires_at) > datetime('now')")
            cache_count = cursor.fetchone()[0]
            scan_data.append(f"Active Cache Entries: {cache_count}")

            cursor.execute("SELECT category, COUNT(*) FROM log_entries GROUP BY category")
            scan_data.append("\nLog Entries by Category:")
            for cat, count in cursor.fetchall():
                scan_data.append(f"  {cat}: {count}")
    except:
        scan_data.append("Database statistics unavailable")

    # 12. System Metadata
    print(f"{COLORS['2'][0]}[12/12] 📝 System Metadata Collection...{RESET}")
    scan_data.append("\n[SECTION 12: SYSTEM METADATA]")
    scan_data.append(f"User Environment Variables:")
    for key, value in list(os.environ.items())[:20]:  # Limit to first 20
        if 'PASSWORD' not in key.upper() and 'SECRET' not in key.upper() and 'KEY' not in key.upper():
            scan_data.append(f"  {key}: {value[:100]}" if len(value) < 100 else f"  {key}: {value[:100]}...")

    scan_data.append(f"\nWorking Directory: {os.getcwd()}")
    scan_data.append(f"Script Directory: {SCRIPT_DIR}")
    scan_data.append(f"Database Directory: {DB_DIR}")
    scan_data.append(f"Database Size: {os.path.getsize(DB_FILE) / 1024:.2f} KB" if os.path.exists(DB_FILE) else "Database not found")

    # Completion
    scan_data.append("\n" + "="*80)
    scan_data.append(f"AGGRESSIVE SCAN COMPLETED: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    scan_data.append(f"Total Data Points Collected: {len(scan_data)}")
    scan_data.append("="*80)

    # Save to aggressive_scan category
    full_content = "\n".join(scan_data)
    print(f"\n{COLORS['2'][0]}✅ Aggressive Scan Complete!{RESET}")
    print(f"Collected {len(scan_data)} comprehensive data points.\n")

    file_path = save_log_file("aggressive_scan", "Aggressive_Intelligence_Scan", full_content, prompt_user=False)

    if file_path:
        print(f"{COLORS['6'][0]}📁 Comprehensive report saved to: {file_path}{RESET}")
        log_to_database("aggressive_scan", "Aggressive_Scan_Complete", f"Collected {len(scan_data)} data points", file_path)

    # Statistics
    print(f"\n{BOLD}Scan Statistics:{RESET}")
    print(f"  Total Sections: 12")
    print(f"  Data Points: {len(scan_data)}")
    print(f"  File Size: {len(full_content) / 1024:.2f} KB")

    view = input(f"\n{BOLD}View scan summary? (y/n): {RESET}").strip().lower()
    if view == 'y':
        print(f"\n{COLORS['6'][0]}" + "\n".join(scan_data[:80]) + f"{RESET}")
        if len(scan_data) > 80:
            print(f"\n... (showing first 80 lines, full report saved to file)")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

# Initialize database on script start
try:
    init_database_system()
except:
    pass  # Silent fail, will try again later

# --- END DATABASE & LOGGING SYSTEM ---

# --- DETECT SYSTEM CAPABILITY FOR BOX DRAWING ---
try:
    "╔═╗".encode(sys.stdout.encoding)
    BOX_CHARS = {"TL": "╔", "TR": "╗", "BL": "╚", "BR": "╝", "H": "═", "V": "║", "BAR": "█"}
except (UnicodeEncodeError, TypeError):
    BOX_CHARS = {"TL": "+", "TR": "+", "BL": "+", "BR": "+", "H": "-", "V": "|", "BAR": "#"}

# --- COLOR & EFFECTS TOOLKIT ---
COLORS = {
    "1": ("\033[91m", "\033[5;91m", "Red"),
    "2": ("\033[92m", "\033[5;92m", "Green"),
    "3": ("\033[94m", "\033[5;94m", "Blue"),
    "4": ("\033[93m", "\033[5;93m", "Yellow"),
    "5": ("\033[95m", "\033[5;95m", "Magenta"),
    "6": ("\033[96m", "\033[5;96m", "Cyan"),
    "7": ("\033[97m", "\033[5;97m", "White"),
    "8": ("\033[38;5;208m", "\033[5;38;5;208m", "Orange"),
    "9": ("\033[38;5;13m", "\033[5;38;5;13m", "Pink"),
    "10": ("\033[38;5;46m", "\033[5;38;5;46m", "Neon Green")
}

active_color_key = "6"
user_has_chosen = False
BOLD = "\033[1m"
RESET = "\033[0m"
is_blinking = True
stop_clock = False
temp_unit = "C"
truncated_thermal = False
mini_view = False
doc_word_render_mode = "pandoc"
display_mode = "classic"
textual_style_mode = "inline"
textual_layout_mode = "two_pane"
TEXTUAL_CSS_PATH = os.path.join(SCRIPT_DIR, "textual_enhanced.css")

_user_config = _load_user_config()
if isinstance(_user_config, dict):
    active_color_key = _user_config.get("active_color_key", active_color_key)
    user_has_chosen = _user_config.get("user_has_chosen", user_has_chosen)
    is_blinking = _user_config.get("is_blinking", is_blinking)
    temp_unit = _user_config.get("temp_unit", temp_unit)
    truncated_thermal = _user_config.get("truncated_thermal", truncated_thermal)
    mini_view = _user_config.get("mini_view", mini_view)
    doc_word_render_mode = _user_config.get("doc_word_render_mode", doc_word_render_mode)
    display_mode = _user_config.get("display_mode", display_mode)
    textual_style_mode = _user_config.get("textual_style_mode", textual_style_mode)
    textual_layout_mode = _user_config.get("textual_layout_mode", textual_layout_mode)

def _update_user_config(create_if_missing=False, **updates):
    if not isinstance(_user_config, dict):
        return
    _user_config.update(updates)
    _save_user_config(_user_config, allow_create=create_if_missing)

def _set_display_mode(mode):
    global display_mode
    display_mode = mode
    _update_user_config(display_mode=display_mode)

# --- NEW: VISUAL FX STREAM FILTER ---
class VisualFXFilter:
    def __init__(self, original_stdout):
        self.stdout = original_stdout
        self.mode = 0 # 0=Normal, 1=Same-Letter(Wide), 2=Density, 3=Dot
        # Emoji animation support
        self.start_time = time.time()
        self.fps = 2  # frames per second for emoji animations
        # Groups of similar emoji to animate (cycle through variants)
        self.emoji_groups = {
            'earth': ['🌍', '🌎', '🌏', '🎮'],
            'moon': ['🌑', '🌘', '🌗', '🌖', '🌕'],
            'clouds': ['☁️', '⛅', '🌤️'],
            'sun': ['☀️', '🌞'],
            'stars': ['✨', '💫', '⭐'],
        }
        # reverse lookup for quick mapping emoji -> group list
        self.emoji_to_group = {}
        for grp in self.emoji_groups.values():
            for e in grp:
                self.emoji_to_group[e] = grp
        # record seen emoji across writes
        global emoji_seen
        if 'emoji_seen' not in globals():
            emoji_seen = set()
        # ANSI color frames to animate arbitrary emoji
        self._anim_colors = [
            "\x1b[38;5;196m", # red
            "\x1b[38;5;202m", # orange
            "\x1b[38;5;226m", # yellow
            "\x1b[38;5;46m",  # green
            "\x1b[38;5;51m",  # cyan
            "\x1b[38;5;21m",  # blue
            "\x1b[38;5;201m", # magenta
        ]
        # regex to match common emoji sequences (covers many ranges)
        self._emoji_pattern = re.compile(
            r"([\U0001F1E6-\U0001F1FF]{1,2}|[\U0001F300-\U0001F5FF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U00002600-\U000026FF\U00002700-\U000027BF\U00002B00-\U00002BFF\U00002300-\U000023FF]+)",
            flags=re.UNICODE
        )

    def write(self, message):
        # Always process emoji (we "take note" of them and animate grouped variants).
        process_only_emojis = (self.mode == 0)

        # Split ANSI codes so we don't break colors
        parts = re.split(r'(\x1b\[[0-9;]*m)', message)
        transformed = []

        for part in parts:
            if part.startswith('\x1b'):
                transformed.append(part)
                continue

            # First, build a string with any mode-specific transforms (unless we only animate emoji)
            new_str = ""
            if not process_only_emojis:
                for char in part:
                    # Preserve structure
                    if char in ('\n', '\r', '\t'):
                        new_str += char
                        continue

                    if self.mode == 1: # Same-Letter / Banner (Simulated via Fullwidth)
                        if '!' <= char <= '~':
                            new_str += chr(ord(char) + 0xFEE0)
                        else:
                            new_str += char
                    elif self.mode == 2: # AI Algorithm (Density Mapping)
                        if char == ' ': new_str += ' '
                        elif char in ".,-`": new_str += "░"
                        elif char in ":;|+=": new_str += "▒"
                        elif char.isupper() or char in "@#$%&": new_str += "█"
                        else: new_str += "▓"
                    elif self.mode == 3: # Dot Version (Pointillism)
                        if char == ' ': new_str += ' '
                        else: new_str += random.choice(["●", "•", "·"])
                    else:
                        new_str += char
            else:
                # keep original content for emoji-only processing
                new_str = part

            # Emoji animation and weather sync
            global is_blinking, weather_cache

            # Weather-related emoji set (these should reflect forecast)
            weather_set = set(['🌍', '🌎', '🌏', '☁️', '⛅', '🌤️', '☀️', '🌞', '🌧️', '⛈️', '❄️', '🌫️', '🌑', '🌘', '🌗', '🌕'])

            # Always record any seen emoji and map weather emoji to current forecast icon
            def _record_and_weather(m):
                ch = m.group(0)
                try:
                    emoji_seen.add(ch)
                except Exception:
                    pass
                if ch in weather_set:
                    return weather_cache.get('icon', ch)
                return ch

            # If blinking is disabled, do not animate — just replace weather emoji and record
            if not is_blinking:
                # record weather and other emoji without animation
                new_str = self._emoji_pattern.sub(_record_and_weather, new_str)
            else:
                # blinking enabled: animate known groups and color-cycle other emoji
                frame_idx = int((time.time() - self.start_time) * self.fps)

                def _replace_known(m):
                    ch = m.group(0)
                    try:
                        emoji_seen.add(ch)
                    except Exception:
                        pass
                    if ch in weather_set:
                        return weather_cache.get('icon', ch)
                    grp = self.emoji_to_group.get(ch)
                    if grp and len(grp) > 1:
                        return grp[frame_idx % len(grp)]
                    return ch

                known_pattern = re.compile('(' + '|'.join(re.escape(e) for e in self.emoji_to_group.keys()) + ')')
                new_str = known_pattern.sub(_replace_known, new_str)

                def _color_wrap(m):
                    ch = m.group(0)
                    try:
                        emoji_seen.add(ch)
                    except Exception:
                        pass
                    if ch in weather_set:
                        return weather_cache.get('icon', ch)
                    color = self._anim_colors[frame_idx % len(self._anim_colors)]
                    return f"{color}{ch}{RESET}"

                new_str = self._emoji_pattern.sub(_color_wrap, new_str)

            transformed.append(new_str)

        self.stdout.write("".join(transformed))

    def flush(self):
        self.stdout.flush()

# Activate the filter hook
if not isinstance(sys.stdout, VisualFXFilter):
    sys.stdout = VisualFXFilter(sys.stdout)

def _ensure_cursor_visible():
    try:
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
    except Exception:
        pass

try:
    import builtins as _builtins
    _orig_input = _builtins.input
    def input(prompt=""):
        _ensure_cursor_visible()
        return _orig_input(prompt)
    _builtins.input = input
except Exception:
    pass

# ================================================================================
# SECTION 6: WEATHER & ENVIRONMENTAL MONITORING
# ================================================================================
# Weather data fetching, display, and live ticker integration
# ================================================================================

# Global weather cache for live ticker
weather_cache = {"temp": "N/A", "icon": "☁️", "humidity": "N/A", "wind": "N/A"}

def get_current_color():
    standard, blink, name = COLORS[active_color_key]
    return blink if is_blinking else standard

def draw_bar(pct):
    width = 15
    try:
        pct_value = float(pct)
    except (TypeError, ValueError):
        return "N/A"
    filled = int(width * pct_value / 100)
    filled = max(0, min(width, filled))
    bar = BOX_CHARS["BAR"] * filled + "░" * (width - filled)
    return f"{bar} {pct_value}%"

def _format_gb(value):
    try:
        return f"{float(value) / (1024**3):.2f} GB"
    except (TypeError, ValueError):
        return "N/A"

def _format_mb(value):
    try:
        return f"{float(value) / (1024**2):.2f} MB"
    except (TypeError, ValueError):
        return "N/A"

def _format_boot_info(timestamp):
    try:
        boot_time = datetime.datetime.fromtimestamp(float(timestamp))
        uptime = datetime.datetime.now() - boot_time
        return boot_time.strftime('%Y-%m-%d %H:%M:%S'), str(uptime).split('.')[0]
    except (TypeError, ValueError, OSError):
        return "N/A", "N/A"

def _safe_float(value, default=None):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

def print_header(title, extra_info=""):
    dash = BOX_CHARS["H"] * 20
    if user_has_chosen:
        current_color = get_current_color()
    else:
        random_key = random.choice(list(COLORS.keys()))
        standard, blink, name = COLORS[random_key]
        current_color = blink if is_blinking else standard
    print(f"\n{current_color}{BOX_CHARS['TL']}{dash} {title.upper()} {extra_info} {dash}{BOX_CHARS['TR']}{RESET}")

# --- ENHANCED: WEATHER SYSTEM WITH OPEN-METEO & NWS INTEGRATION ---

def get_weather_data():
    global weather_cache

    # Try to get cached data first (5 minute cache)
    cached = get_cached_data("weather_data")
    if cached:
        weather_cache = cached
        return weather_cache

    try:
        # 1. Get location via IP
        geo = requests.get("http://ip-api.com/json/", timeout=3).json()
        lat, lon = geo.get('lat'), geo.get('lon')
        city = geo.get('city', 'Unknown')

        # 2. Get Advanced Data from Open-Meteo (No API Key Required)
        om_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m&wind_speed_unit=mph"
        om_res = requests.get(om_url, timeout=5).json()
        current = om_res['current']

        temp_raw = current['temperature_2m']
        if temp_unit == "F":
            temp_raw = (temp_raw * 9/5) + 32

        # 3. Simple Map for Weather Codes to Icons
        code = current['weather_code']
        icon = "☀️"
        if code in [1, 2, 3]: icon = "⛅"
        elif code in [45, 48]: icon = "🌫️"
        elif code in [51, 53, 55, 61, 63, 65]: icon = "🌧️"
        elif code in [71, 73, 75]: icon = "❄️"
        elif code in [95, 96, 99]: icon = "⛈️"

        weather_cache = {
            "temp": f"{temp_raw:.1f}°{temp_unit}",
            "icon": icon,
            "city": city,
            "humidity": f"{current['relative_humidity_2m']}%",
            "wind": f"{current['wind_speed_10m']} mph",
            "feels": f"{current['apparent_temperature']:.1f}°{temp_unit}"
        }

        # Cache the weather data for 5 minutes
        cache_data("weather_data", weather_cache, expire_minutes=5)

        return weather_cache
    except:
        # Fallback to wttr.in if Open-Meteo fails
        try:
            res = requests.get("https://wttr.in/?format=%C+%t", timeout=5).text.strip()
            weather_cache["temp"] = res.split()[-1]
            cache_data("weather_data", weather_cache, expire_minutes=5)
            return weather_cache
        except: return None

def feature_weather_display():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🌍 Global Weather Station")
        print(f" {BOLD}[1]{RESET} 🌡️ Current Weather")
        print(f" {BOLD}[2]{RESET} 🔄 Refresh Weather Cache")
        print(f" {BOLD}[3]{RESET} 🧾 Show Raw Weather Data")
        print(f" {BOLD}[4]{RESET} 🌐 Open Weather Links")
        print(f" {BOLD}[0]{RESET} ↩️  Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return
        if choice == '1':
            print_header("🌡️ Current Weather")
            print("🔍 Querying Open-Meteo & National Weather Service...")
            data = get_weather_data()
            if data:
                print(f"\n {BOLD}📍 Current Location:{RESET} {data['city']}")
                print(f" {BOLD}🌡️ Temperature:   {RESET} {data['icon']} {data['temp']} (Feels like {data['feels']})")
                print(f" {BOLD}💧 Humidity:      {RESET} {data['humidity']}")
                print(f" {BOLD}💨 Wind Speed:    {RESET} {data['wind']}")

                print_header("🗺️ Detailed Planning & Radar")
                print(f" > {BOLD}🌬️ Windy.com:{RESET}     https://www.windy.com")
                print(f" > {BOLD}🌦️ Weather Under:{RESET}  https://www.wunderground.com")
                print(f" > {BOLD}📺 The Weather Ch:{RESET} https://weather.com")

                try:
                    full_report = requests.get(f"https://wttr.in/{data['city']}?0&m&q", timeout=5).text
                    print("\n" + full_report)
                except Exception:
                    pass

                weather_log = (
                    f"Location: {data['city']}\nTemperature: {data['temp']}\nFeels Like: {data['feels']}"
                    f"\nHumidity: {data['humidity']}\nWind: {data['wind']}\nConditions: {data['icon']}"
                )
                save_log_file("weather", "Weather_Query", weather_log, prompt_user=True)
            else:
                print(f" {COLORS['1'][0]}[!] 📡 Could not retrieve weather. Check connection.{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '2':
            cleared = clear_cached_data("weather_data")
            print(f"✅ Cleared {cleared} cached entry(ies). Refreshing...")
            data = get_weather_data()
            if data:
                print(f"Updated: {data.get('icon','')} {data.get('temp','N/A')}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            print_header("🧾 Raw Weather Data")
            data = get_weather_data()
            print(json.dumps(data, indent=2) if data else "No data")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '4':
            print_header("🛰️ Weather Services")
            print("1) https://www.windy.com")
            print("2) https://www.wunderground.com")
            print("3) https://weather.com")
            sel = input("Open link (1-3, Enter to skip): ").strip()
            links = {
                "1": "https://www.windy.com",
                "2": "https://www.wunderground.com",
                "3": "https://weather.com",
            }
            if sel in links:
                _open_url(links[sel])
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

# --- SATELLITE TRACKER (PyPredict) ---
try:
    import predict
    HAVE_PREDICT = True
except ImportError:
    HAVE_PREDICT = False

HAVE_REQUESTS = "requests" in globals()

ORBITAL_DB_FILE = Path(DB_DIR) / "orbital_memory.json"
AU_KM = 149597870.7
C_KMS = 299792.458
TRAIL_LENGTH = 30
SAT_MAX_TARGETS = 5

SAT_COL = {
    "reset": "\033[0m",
    "hud": "\033[36m",
    "warn": "\033[33m",
    "err": "\033[31m",
    "ok": "\033[32m",
    "sat": "\033[35m",
    "trail": "\033[90m",
}

NORTH_HEMISPHERE = [
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣄⣠⣀⡀⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢠⣠⣼⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⢠⣤⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣾⣿⣽⣿⣿⣅⠈⠉⠻⣿⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⢀⡶⠒⢉⡀⢠⣤⣶⣶⣿⣷⣆⣀⡀⠀⢲⣖⠒⠀⠀⠀⠀⠀⠀⠀",
    "⢀⣤⣾⣶⣦⣤⣤⣶⣿⣿⣿⣿⣿⣿⣽⡿⠻⣷⣀⠀⢻⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⣤⣶⣶⣤⣀⣀⣬⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣦⣼⣀⠀",
    "⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠓⣿⣿⠟⠁⠘⣿⡟⠁⠀⠘⠛⠁⠀⠀⢠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠙⠁",
    "⠀⠸⠟⠋⠀⠈⠙⣿⣿⣿⣿⣿⣿⣷⣦⡄⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣼⣆⢘⣿⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⢱⡿⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡿⠦⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡗⠀⠈⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣉⣿⡿⢿⢷⣾⣾⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⠿⠿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣷⣦⣶⣦⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀",
]

SOUTH_HEMISPHERE = [
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡖⠛⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠙⣿⣿⠿⢻⣿⣿⡿⠋⢩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠧⣤⣦⣤⣄⡀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠘⣧⠀⠈⣹⡻⠇⢀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠈⢽⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣴⣿⣷⢲⣦⣤⡀⢀⡀⠀⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣷⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠂⠛⣆⣤⡜⣟⠋⠙⠂⠀⠀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⠉⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣆⠀⠰⠄⠀⠉⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠿⠿⣿⣿⣿⠇⠀⠀⢀⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⢀⣼⠗⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠁⠀⠀⠀",
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
]

SAT_MAP_FRAME = NORTH_HEMISPHERE + SOUTH_HEMISPHERE
MAP_WIDTH = max(len(line) for line in SAT_MAP_FRAME) if SAT_MAP_FRAME else 80
MAP_HEIGHT = len(SAT_MAP_FRAME) if SAT_MAP_FRAME else 24

SAT_MARKERS = ["1", "2", "3", "4", "5"]

class TLEStore:
    def __init__(self, db_file=ORBITAL_DB_FILE):
        self.db_file = db_file
        self.data = {"satellites": {}, "last_update": 0}
        self.load()

    def load(self):
        if self.db_file.exists():
            try:
                with open(self.db_file, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception as e:
                print(f"{SAT_COL['err']}[TLE] Failed to load DB: {e}{SAT_COL['reset']}")
        if "0 LEMUR 1" not in self.data["satellites"]:
            self.data["satellites"]["0 LEMUR 1"] = (
                "0 LEMUR 1\n"
                "1 40044U 14033AL  15013.74135905  .00002013  00000-0  31503-3 0  6119\n"
                "2 40044 097.9584 269.2923 0059425 258.2447 101.2095 14.72707190 30443"
            )

    def save(self):
        try:
            os.makedirs(self.db_file.parent, exist_ok=True)
            with open(self.db_file, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"{SAT_COL['err']}[TLE] Failed to save DB: {e}{SAT_COL['reset']}")

    def get(self, name):
        return self.data["satellites"].get(name)

    def list_names(self):
        return sorted(self.data["satellites"].keys())

    def count(self):
        return len(self.data["satellites"])

    def update_from_celestrak(self):
        if not HAVE_REQUESTS:
            print(f"{SAT_COL['warn']}[TLE] requests not available, cannot update from network.{SAT_COL['reset']}")
            return False

        print(f"{SAT_COL['hud']}[HANDSHAKE] Contacting Celestrak for active TLEs...{SAT_COL['reset']}")
        try:
            r = requests.get(
                "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle",
                timeout=12
            )
            if r.status_code != 200:
                print(f"{SAT_COL['err']}[TLE] HTTP {r.status_code} from Celestrak.{SAT_COL['reset']}")
                return False

            lines = r.text.splitlines()
            count = 0
            for i in range(0, len(lines) - 2, 3):
                name = lines[i].strip()
                self.data["satellites"][name] = f"{lines[i]}\n{lines[i+1]}\n{lines[i+2]}"
                count += 1

            self.data["last_update"] = time.time()
            self.save()
            print(f"{SAT_COL['ok']}[TLE] Updated {count} satellites from Celestrak.{SAT_COL['reset']}")
            return True
        except Exception as e:
            print(f"{SAT_COL['err']}[TLE] Update failed: {e}{SAT_COL['reset']}")
            return False

class MapRenderer:
    def __init__(self, width=None, height=None):
        self.width = MAP_WIDTH if width is None else width
        self.height = MAP_HEIGHT if height is None else height

    def latlon_to_xy(self, lat, lon):
        x = int((lon % 360) * (self.width / 360))
        y = int((90 - lat) * (self.height / 180))
        x = max(0, min(self.width - 1, x))
        y = max(0, min(self.height - 1, y))
        return x, y

    def render(self, trail, sat_pos):
        trails = {"PRIMARY": trail}
        positions = {"PRIMARY": sat_pos}
        return self.render_multi(trails, positions, marker_map={"PRIMARY": "V"}, primary_name="PRIMARY")

    def render_multi(self, trails, positions, marker_map=None, primary_name=None):
        lines = []
        marker_map = marker_map or {}
        north_count = len(NORTH_HEMISPHERE)
        south_count = len(SOUTH_HEMISPHERE)
        for r in range(self.height):
            if r < north_count:
                north = NORTH_HEMISPHERE[r][:self.width]
                base = list(north.ljust(self.width))
                prefix = " N |"
            else:
                idx = r - north_count
                south = SOUTH_HEMISPHERE[idx][:self.width] if idx < south_count else ""
                base = list(south.ljust(self.width))
                prefix = " S |"
            if r == north_count:
                prefix = "EQ-|"

            for trail in trails.values():
                for t_lat, t_lon in trail:
                    tx, ty = self.latlon_to_xy(t_lat, t_lon)
                    if ty == r:
                        base[tx] = f"{SAT_COL['trail']}.{SAT_COL['reset']}"

            for name, (lat, lon) in positions.items():
                sx, sy = self.latlon_to_xy(lat, lon)
                if sy == r:
                    marker = marker_map.get(name, "*")
                    color = SAT_COL['sat'] if name == primary_name else SAT_COL['hud']
                    base[sx] = f"{color}{marker}{SAT_COL['reset']}"

            lines.append(f"{prefix}{''.join(base)}|")
        return "\n".join(lines)

class MarsBridge:
    def __init__(self, qth, targets=None, primary_target="0 LEMUR 1"):
        self.qth = qth
        self.store = TLEStore()
        self.map = MapRenderer()
        self.trails = {}
        self.targets = targets or [primary_target]
        self.primary_target = primary_target if primary_target in self.targets else self.targets[0]
        self.running = True
        self.command = None
        self.health = self._initial_health()

    def _initial_health(self):
        if HAVE_PREDICT and HAVE_REQUESTS:
            return "OPTIMAL"
        if HAVE_PREDICT or HAVE_REQUESTS:
            return "DEGRADED"
        return "OFFLINE"

    def _health_icon(self):
        if self.health == "OPTIMAL":
            return "🟢"
        if self.health == "DEGRADED":
            return "🟡"
        return "🔴"

    def get_pos(self, tle, now):
        if HAVE_PREDICT:
            try:
                obs = predict.observe(tle, self.qth, at=now)
                lon = obs["longitude"]
                if lon < 0:
                    lon += 360
                return obs["latitude"], lon
            except Exception:
                pass

        try:
            l2 = tle.splitlines()[2]
            inc = float(l2[8:16])
            n = float(l2[52:63])
            period = 86400 / n
            theta = ((now % period) / period) * 2 * math.pi
            lat = inc * math.sin(theta)
            lon = (now / 240) % 360
            return lat, lon
        except Exception:
            return 0.0, 0.0

    def _input_thread(self):
        while self.running:
            try:
                cmd = input().strip().lower()
                self.command = cmd
            except EOFError:
                break

    def _handle_command(self):
        cmd = self.command
        self.command = None
        if not cmd:
            return

        if cmd == "q":
            self.running = False
        elif cmd == "u":
            if self.store.update_from_celestrak():
                self.health = "OPTIMAL"
        elif cmd.startswith("s "):
            name = cmd[2:].strip()
            if self.store.get(name):
                if name not in self.targets:
                    if len(self.targets) < SAT_MAX_TARGETS:
                        self.targets.append(name)
                    else:
                        print(f"{SAT_COL['warn']}[BRIDGE] Max targets reached ({SAT_MAX_TARGETS}).{SAT_COL['reset']}")
                        time.sleep(1)
                        return
                self.primary_target = name
            else:
                print(f"{SAT_COL['warn']}[BRIDGE] Unknown target: {name}{SAT_COL['reset']}")
                time.sleep(1)
        elif cmd.startswith("a "):
            name = cmd[2:].strip()
            if not self.store.get(name):
                print(f"{SAT_COL['warn']}[BRIDGE] Unknown target: {name}{SAT_COL['reset']}")
                time.sleep(1)
                return
            if name in self.targets:
                return
            if len(self.targets) >= SAT_MAX_TARGETS:
                print(f"{SAT_COL['warn']}[BRIDGE] Max targets reached ({SAT_MAX_TARGETS}).{SAT_COL['reset']}")
                time.sleep(1)
                return
            self.targets.append(name)
        elif cmd.startswith("r "):
            name = cmd[2:].strip()
            if name in self.targets:
                self.targets.remove(name)
                if self.primary_target == name:
                    self.primary_target = self.targets[0] if self.targets else "0 LEMUR 1"

    def run(self):
        input_thread = threading.Thread(target=self._input_thread, daemon=True)
        input_thread.start()

        while self.running:
            now = time.time()
            targets = [t for t in self.targets if self.store.get(t)]
            if not targets:
                print(f"{SAT_COL['warn']}[BRIDGE] No valid targets; resetting to default.{SAT_COL['reset']}")
                targets = ["0 LEMUR 1"]
                self.primary_target = "0 LEMUR 1"

            positions = {}
            for name in targets[:SAT_MAX_TARGETS]:
                tle = self.store.get(name)
                if not tle:
                    continue
                lat, lon = self.get_pos(tle, now)
                positions[name] = (lat, lon)
                trail = self.trails.setdefault(name, deque(maxlen=TRAIL_LENGTH))
                trail.append((lat, lon))

            if self.primary_target not in targets:
                self.primary_target = targets[0]

            os.system("cls" if os.name == "nt" else "clear")

            print(f"{SAT_COL['hud']}== MARS BRIDGE STATUS: {self.health} {self._health_icon()} | TARGET: {self.primary_target} =={SAT_COL['reset']}")
            print(f"MISSION CLOCK: {time.ctime(now)} UTC")
            earth_dist = (1.524 - 1.0) * AU_KM
            latency_min = (earth_dist / C_KMS) / 60
            print(f"EARTH DISTANCE: {earth_dist:,.0f} KM | LATENCY: {latency_min:.1f}m")
            print(f"SATELLITES IN MEMORY: {self.store.count()}")
            marker_map = {name: SAT_MARKERS[i] for i, name in enumerate(targets[:SAT_MAX_TARGETS])}
            tracking_line = ", ".join([f"{marker_map.get(name, '?')}:{name}" for name in targets[:SAT_MAX_TARGETS]])
            print(f"TRACKING (max {SAT_MAX_TARGETS}): {tracking_line}")
            print("-" * (MAP_WIDTH + 6))

            print(self.map.render_multi(self.trails, positions, marker_map=marker_map, primary_name=self.primary_target))

            if self.primary_target in positions:
                lat, lon = positions[self.primary_target]
                print(f"\nTELEMETRY: {lat:>6.2f}N {lon:>7.2f}E")
            print("[U] Update TLEs | [S <name>] Set Primary | [A <name>] Add | [R <name>] Remove | [Q] Quit")
            print("(Type command and press Enter)")

            for _ in range(10):
                if not self.running:
                    break
                if self.command:
                    self._handle_command()
                    break
                time.sleep(0.5)

        print(f"{SAT_COL['hud']}Bridge loop terminated. Safe travels.{SAT_COL['reset']}")

def _satellite_default_qth():
    lat = _user_config.get("station_lat", 39.267) if isinstance(_user_config, dict) else 39.267
    lon = _user_config.get("station_lon", -76.798) if isinstance(_user_config, dict) else -76.798
    alt = _user_config.get("station_alt", 50) if isinstance(_user_config, dict) else 50
    return (lat, lon, alt)

def _satellite_set_qth():
    lat = input("Station latitude (N+, S-): ").strip()
    lon = input("Station longitude (E+, W-): ").strip()
    alt = input("Station altitude meters [50]: ").strip() or "50"
    try:
        lat_f = float(lat)
        lon_f = float(lon)
        alt_f = float(alt)
    except Exception:
        print(f"{COLORS['1'][0]}Invalid coordinates{RESET}")
        return None
    _update_user_config(station_lat=lat_f, station_lon=lon_f, station_alt=alt_f)
    return (lat_f, lon_f, alt_f)

def _format_epoch(ts):
    try:
        if not ts:
            return "N/A"
        return datetime.datetime.utcfromtimestamp(float(ts)).strftime("%Y-%m-%d %H:%M:%S UTC")
    except Exception:
        return "N/A"

def _satellite_report_lines(store):
    store.load()
    lines = []
    lines.append("ORBITAL MEMORY REPORT")
    lines.append(f"Generated: {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    lines.append(f"DB File: {store.db_file}")
    lines.append(f"Last Update: {_format_epoch(store.data.get('last_update', 0))}")
    lines.append(f"Satellite Count: {store.count()}")
    lines.append("-" * 60)
    for name, tle in sorted(store.data.get("satellites", {}).items()):
        lines.append(f"Name: {name}")
        parts = [line.strip() for line in tle.splitlines() if line.strip()]
        if len(parts) >= 3:
            lines.append(f"TLE0: {parts[0]}")
            lines.append(f"TLE1: {parts[1]}")
            lines.append(f"TLE2: {parts[2]}")
        else:
            for idx, line in enumerate(parts):
                lines.append(f"TLE{idx}: {line}")
        lines.append("")
    return lines

def _satellite_log_selection(name):
    try:
        log_to_database("general", "Satellite_Select", name)
    except Exception:
        pass

def _satellite_recent_selections(limit=10):
    recent = []
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT data FROM log_entries WHERE operation=? AND data IS NOT NULL ORDER BY id DESC LIMIT 100",
                ("Satellite_Select",)
            )
            rows = cursor.fetchall()
        for (data,) in rows:
            if data and data not in recent:
                recent.append(data)
            if len(recent) >= limit:
                break
    except Exception:
        pass
    return recent

def _satellite_choose_targets(store, max_targets=SAT_MAX_TARGETS):
    names = store.list_names()
    if not names:
        print(f"{COLORS['1'][0]}No satellites found in orbital memory.{RESET}")
        return []
    query = input("Search term (Enter for all): ").strip().lower()
    matches = [n for n in names if query in n.lower()] if query else names
    if not matches:
        print(f"{COLORS['1'][0]}No matches found.{RESET}")
        return []

    print_header("🛰️ Satellite List")
    display = matches[:50]
    for i, name in enumerate(display, 1):
        print(f" [{i}] {name}")
    if len(matches) > 50:
        print(f"... showing 50 of {len(matches)} matches")

    raw = input("Select up to 5 (numbers or names, comma-separated): ").strip()
    if not raw:
        return []
    picks = []
    for token in [t.strip() for t in raw.split(",") if t.strip()]:
        if token.isdigit():
            idx = int(token)
            if 1 <= idx <= len(display):
                name = display[idx - 1]
                if name not in picks:
                    picks.append(name)
        else:
            for name in names:
                if name.lower() == token.lower():
                    if name not in picks:
                        picks.append(name)
                    break
    return picks[:max_targets]

def _satellite_targets_from_config(store):
    targets = []
    if isinstance(_user_config, dict):
        cfg_targets = _user_config.get("sat_targets")
        if isinstance(cfg_targets, list):
            targets = [t for t in cfg_targets if store.get(t)]
        primary = _user_config.get("sat_target")
        if primary and store.get(primary) and primary not in targets:
            targets.insert(0, primary)
    if not targets:
        targets = ["0 LEMUR 1"]
    return targets[:SAT_MAX_TARGETS]

def feature_satellite_tracker():
    store = TLEStore()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🛰️ Satellite Tracker")
        qth = _satellite_default_qth()
        targets = _satellite_targets_from_config(store)
        target = targets[0]
        health = "OPTIMAL" if (HAVE_PREDICT and HAVE_REQUESTS) else "DEGRADED" if (HAVE_PREDICT or HAVE_REQUESTS) else "OFFLINE"
        print(f"Status: {health} | Predict: {'YES' if HAVE_PREDICT else 'NO'} | Requests: {'YES' if HAVE_REQUESTS else 'NO'}")
        print(f"Station QTH: lat {qth[0]:.3f}, lon {qth[1]:.3f}, alt {qth[2]:.1f}m")
        print(f"Tracking (max {SAT_MAX_TARGETS}): {', '.join(targets)}")
        print(f"Primary Target: {target} | Satellites: {store.count()}")
        print(" [1] 🚀 Start Live Tracker")
        print(" [2] 🔄 Update TLEs from Celestrak")
        print(" [3] 🔍 Search Satellites")
        print(" [4] 🎯 Set Primary Target")
        print(" [5] 🎛️ Set Tracking Targets (up to 5)")
        print(" [6] 📍 Set Station Location (QTH)")
        print(" [7] 🧾 Show Status Details")
        print(" [8] 📄 Orbital Memory Report")
        print(" [9] 🗂️ Quick Pick (DB Recent)")
        print(" [M] 🗺️ Launch MapSCII")
        print(" [D] 📦 Install MapSCII (Download Center)")
        print(" [P] 📦 Install PyPredict (hint)")
        print(" [0] ↩️  Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return
        if choice == '1':
            bridge = MarsBridge(qth, targets=targets, primary_target=target)
            bridge.run()
        elif choice == '2':
            store.update_from_celestrak()
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            query = input("Search term: ").strip().lower()
            names = store.list_names()
            matches = [n for n in names if query in n.lower()] if query else names
            print_header("🔍 Satellite Matches")
            for name in matches[:30]:
                print(f" - {name}")
            if len(matches) > 30:
                print(f"... and {len(matches) - 30} more")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '4':
            name = input("Enter satellite name: ").strip()
            if store.get(name):
                _update_user_config(sat_target=name)
                if isinstance(_user_config, dict):
                    cur_targets = _user_config.get("sat_targets")
                    if not isinstance(cur_targets, list):
                        cur_targets = []
                    if name not in cur_targets:
                        cur_targets.insert(0, name)
                    _update_user_config(sat_targets=cur_targets[:SAT_MAX_TARGETS])
                _satellite_log_selection(name)
                print(f"✅ Target set to {name}")
            else:
                print(f"{COLORS['1'][0]}Unknown satellite name{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '5':
            selected = _satellite_choose_targets(store)
            if selected:
                _update_user_config(sat_targets=selected, sat_target=selected[0])
                for name in selected:
                    _satellite_log_selection(name)
                print(f"✅ Tracking {len(selected)} satellite(s)")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '6':
            new_qth = _satellite_set_qth()
            if new_qth:
                print("✅ Station location updated")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '7':
            print_header("🧾 Status Details")
            print(f"Predict installed: {'YES' if HAVE_PREDICT else 'NO'}")
            print(f"Requests available: {'YES' if HAVE_REQUESTS else 'NO'}")
            print(f"Orbital DB: {ORBITAL_DB_FILE}")
            print(f"Last TLE Update: {_format_epoch(store.data.get('last_update', 0))}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '8':
            print_header("📄 Orbital Memory Report")
            report_lines = _satellite_report_lines(store)
            print("\n".join(report_lines))
            save_log_file("general", "Satellite_Report", "\n".join(report_lines), prompt_user=True)
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '9':
            recent = _satellite_recent_selections(limit=10)
            if not recent:
                print(f"{COLORS['1'][0]}No recent selections in DB yet.{RESET}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
                continue
            print_header("🗂️ Quick Pick (Recent)")
            for i, name in enumerate(recent, 1):
                print(f" [{i}] {name}")
            raw = input("Select up to 5 (numbers, comma-separated): ").strip()
            picks = []
            for token in [t.strip() for t in raw.split(",") if t.strip()]:
                if token.isdigit():
                    idx = int(token)
                    if 1 <= idx <= len(recent):
                        name = recent[idx - 1]
                        if name not in picks:
                            picks.append(name)
            if picks:
                _update_user_config(sat_targets=picks[:SAT_MAX_TARGETS], sat_target=picks[0])
                print(f"✅ Tracking {len(picks)} satellite(s)")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice.upper() == 'M':
            if shutil.which("mapscii") is None:
                print(f"{COLORS['1'][0]}MapSCII not installed. Use the Download Center to install.{RESET}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
            else:
                subprocess.call(["mapscii"])
        elif choice.upper() == 'D':
            feature_download_center()
        elif choice.upper() == 'P':
            print_header("📦 PyPredict Install")
            print("Python package (C extension):")
            print("  pip install pypredict")
            print("If build fails, install system deps (gcc, make, python-dev).")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _traffic_risk_from_weather(icon):
    if icon in ["🌧️", "⛈️", "❄️", "🌫️"]:
        return "HIGH"
    if icon in ["⛅", "🌤️"]:
        return "MODERATE"
    return "LOW"

# --- PENETRATION TESTING TOOLKIT ---

def check_pentest_tool(tool_name):
    """Check if a penetration testing tool is installed."""
    return shutil.which(tool_name) is not None

def feature_nmap_scanner():
    """Nmap Network Scanner Wrapper"""
    print_header("🔍 Nmap Network Scanner")

    if not check_pentest_tool('nmap'):
        print(f"{COLORS['1'][0]}❌ Nmap is not installed.{RESET}")
        print(f"\n{BOLD}Install with:{RESET}")
        print("  Ubuntu/Debian: sudo apt-get install nmap")
        print("  Fedora/RHEL:   sudo dnf install nmap")
        print("  macOS:         brew install nmap")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return

    print(f"{COLORS['2'][0]}✅ Nmap is installed{RESET}\n")
    print(f"{BOLD}Quick Scan Profiles:{RESET}")
    print(f" {BOLD}[1]{RESET} 🎯 Quick Scan (Target IP/Hostname)")
    print(f" {BOLD}[2]{RESET} 🌐 Network Range Scan")
    print(f" {BOLD}[3]{RESET} 🔓 Port Scan (Common Ports)")
    print(f" {BOLD}[4]{RESET} 🚀 Aggressive Scan (-A)")
    print(f" {BOLD}[5]{RESET} 👻 Stealth SYN Scan (-sS)")
    print(f" {BOLD}[6]{RESET} 🔬 OS Detection")
    print(f" {BOLD}[7]{RESET} 📝 Custom Nmap Command")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select scan type: {RESET}").strip()

    cmd = None
    if choice == '0':
        return
    elif choice == '1':
        target = input("Enter target IP or hostname: ").strip()
        if target:
            cmd = f"nmap {target}"
    elif choice == '2':
        target = input("Enter network range (e.g., 192.168.1.0/24): ").strip()
        if target:
            cmd = f"nmap {target}"
    elif choice == '3':
        target = input("Enter target IP or hostname: ").strip()
        if target:
            cmd = f"nmap -p 21,22,23,25,53,80,443,3306,3389,8080 {target}"
    elif choice == '4':
        target = input("Enter target IP or hostname: ").strip()
        if target:
            cmd = f"nmap -A {target}"
    elif choice == '5':
        target = input("Enter target IP or hostname: ").strip()
        if target:
            print(f"{COLORS['4'][0]}⚠️  Requires root/sudo privileges{RESET}")
            cmd = f"sudo nmap -sS {target}"
    elif choice == '6':
        target = input("Enter target IP or hostname: ").strip()
        if target:
            print(f"{COLORS['4'][0]}⚠️  Requires root/sudo privileges{RESET}")
            cmd = f"sudo nmap -O {target}"
    elif choice == '7':
        cmd = input("Enter full nmap command: ").strip()
    else:
        print(f"{COLORS['1'][0]}Invalid choice{RESET}")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return

    if cmd:
        print(f"\n{COLORS['6'][0]}Executing: {cmd}{RESET}\n")
        print(f"{COLORS['4'][0]}⚠️  Press Ctrl+C to stop scan{RESET}\n")
        try:
            os.system(cmd)
        except KeyboardInterrupt:
            print(f"\n{COLORS['4'][0]}Scan interrupted by user{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_metasploit_console():
    """Metasploit Framework Wrapper"""
    print_header("💣 Metasploit Framework")

    if not check_pentest_tool('msfconsole'):
        print(f"{COLORS['1'][0]}❌ Metasploit is not installed.{RESET}")
        print(f"\n{BOLD}Install with:{RESET}")
        print("  Visit: https://metasploit.com/")
        print("  Kali Linux: Pre-installed")
        print("  Ubuntu:     curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return

    print(f"{COLORS['2'][0]}✅ Metasploit is installed{RESET}\n")
    print(f"{BOLD}Options:{RESET}")
    print(f" {BOLD}[1]{RESET} 🖥️  Launch msfconsole (Interactive)")
    print(f" {BOLD}[2]{RESET} 🔍 Search exploits (keyword)")
    print(f" {BOLD}[3]{RESET} 📊 Check Metasploit version")
    print(f" {BOLD}[4]{RESET} 🔄 Update Metasploit")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        print(f"\n{COLORS['6'][0]}Launching Metasploit Console...{RESET}")
        print(f"{COLORS['4'][0]}Type 'exit' to return to pythonOS{RESET}\n")
        os.system('msfconsole')
    elif choice == '2':
        keyword = input("Enter search keyword (e.g., windows, apache): ").strip()
        if keyword:
            os.system(f'msfconsole -q -x "search {keyword}; exit"')
    elif choice == '3':
        os.system('msfconsole --version')
    elif choice == '4':
        print(f"\n{COLORS['6'][0]}Updating Metasploit...{RESET}\n")
        os.system('msfupdate')

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_aircrack_toolkit():
    """Aircrack-ng Wireless Security Toolkit Wrapper"""
    print_header("📡 Aircrack-ng Wireless Toolkit")

    if not check_pentest_tool('aircrack-ng'):
        print(f"{COLORS['1'][0]}❌ Aircrack-ng is not installed.{RESET}")
        print(f"\n{BOLD}Install with:{RESET}")
        print("  Ubuntu/Debian: sudo apt-get install aircrack-ng")
        print("  Fedora:        sudo dnf install aircrack-ng")
        print("  macOS:         brew install aircrack-ng")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return

    print(f"{COLORS['2'][0]}✅ Aircrack-ng is installed{RESET}\n")
    print(f"{COLORS['4'][0]}⚠️  WARNING: Only test on networks you own or have permission to test!{RESET}\n")
    print(f"{BOLD}Options:{RESET}")
    print(f" {BOLD}[1]{RESET} 📶 Check wireless interfaces")
    print(f" {BOLD}[2]{RESET} 🔍 Put interface in monitor mode (airmon-ng)")
    print(f" {BOLD}[3]{RESET} 📡 Scan for wireless networks (airodump-ng)")
    print(f" {BOLD}[4]{RESET} 🔓 Crack WPA/WPA2 handshake")
    print(f" {BOLD}[5]{RESET} 📝 Custom aircrack-ng command")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        os.system('iwconfig 2>/dev/null || ip link show')
    elif choice == '2':
        iface = input("Enter wireless interface (e.g., wlan0): ").strip()
        if iface:
            print(f"{COLORS['4'][0]}⚠️  Requires root/sudo{RESET}")
            os.system(f'sudo airmon-ng start {iface}')
    elif choice == '3':
        iface = input("Enter monitor interface (e.g., wlan0mon): ").strip()
        if iface:
            print(f"{COLORS['4'][0]}⚠️  Requires root/sudo. Press Ctrl+C to stop{RESET}")
            os.system(f'sudo airodump-ng {iface}')
    elif choice == '4':
        cap_file = input("Enter capture file (.cap): ").strip()
        wordlist = input("Enter wordlist path: ").strip()
        if cap_file and wordlist:
            os.system(f'aircrack-ng -w {wordlist} {cap_file}')
    elif choice == '5':
        cmd = input("Enter aircrack-ng command: ").strip()
        if cmd:
            os.system(cmd)

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_burpsuite():
    def _scan_ports(ports):
        open_ports = []
        for port in ports:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)
                if s.connect_ex(('127.0.0.1', port)) == 0:
                    open_ports.append(port)
        return open_ports

    def _admin_status():
        try:
            return os.getuid() == 0
        except Exception:
            try:
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            except Exception:
                return False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🛡️ Security & Port Audit")
        print(f" {BOLD}[1]{RESET} ⚠️  Quick Port Scan (Common)")
        print(f" {BOLD}[2]{RESET} 🧭 Extended Port Scan (Common + Services)")
        print(f" {BOLD}[3]{RESET} 📡 List Listening Ports")
        print(f" {BOLD}[4]{RESET} 👑 Show Admin/Root Status")
        print(f" {BOLD}[5]{RESET} 💾 Save Audit Report")
        print(f" {BOLD}[0]{RESET} ↩️  Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return
        if choice == '1':
            common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389]
            print_header("⚠️ Quick Port Scan")
            open_ports = _scan_ports(common_ports)
            if open_ports:
                for port in open_ports:
                    print(f" {COLORS['1'][0]}[!] OPEN:{RESET} Port {port}")
            else:
                print(f" {COLORS['2'][0]}[+] ✅ No standard high-risk ports open locally.{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '2':
            ports = [21, 22, 23, 25, 53, 80, 110, 143, 389, 443, 445, 587, 993, 995, 3306, 3389, 5432, 6379, 8080, 8443, 9200]
            print_header("🧭 Extended Port Scan")
            open_ports = _scan_ports(ports)
            if open_ports:
                print(f"Open Ports: {', '.join(str(p) for p in open_ports)}")
            else:
                print(f" {COLORS['2'][0]}[+] ✅ No common service ports open locally.{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            print_header("📡 Listening Ports")
            try:
                conns = psutil.net_connections(kind='inet')
                listen = sorted({c.laddr.port for c in conns if c.status == psutil.CONN_LISTEN})
                if listen:
                    print("Listening Ports:", ", ".join(str(p) for p in listen[:30]))
                    if len(listen) > 30:
                        print(f"... and {len(listen) - 30} more")
                else:
                    print("No listening ports found.")
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '4':
            print_header("👑 Security Context")
            is_admin = _admin_status()
            print(f"Admin/Root Privileges: {'YES' if is_admin else 'NO'}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '5':
            common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389]
            open_ports = _scan_ports(common_ports)
            is_admin = _admin_status()
            audit_log = [
                "Security Audit Report",
                f"Ports Scanned: {common_ports}",
                f"Open Ports: {open_ports if open_ports else 'None'}",
                f"Admin/Root Privileges: {'YES' if is_admin else 'NO'}",
            ]
            payload = "\n".join(audit_log)
            save_log_file("security", "Security_Audit", payload, prompt_user=True)
            try:
                log_to_database("security", "Security_Audit", payload, status="success")
            except Exception:
                pass
            input(f"\n{BOLD}[ ✅ Audit Complete. Press Enter... ]{RESET}")
        print(f"\n{COLORS['4'][0]}⚠️  Burp Suite not found in standard locations{RESET}")
        custom = input(f"\n{BOLD}Enter custom Burp Suite path or command (or Enter to skip): {RESET}").strip()
        if custom:
            os.system(f'{custom} &')

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_password_cracking():
    """John the Ripper and Hashcat Wrapper"""
    print_header("🔐 Password Cracking Tools")

    john_installed = check_pentest_tool('john')
    hashcat_installed = check_pentest_tool('hashcat')

    print(f"{BOLD}Tool Status:{RESET}")
    print(f"  John the Ripper: {COLORS['2'][0] if john_installed else COLORS['1'][0]}{'✅ Installed' if john_installed else '❌ Not Installed'}{RESET}")
    print(f"  Hashcat:         {COLORS['2'][0] if hashcat_installed else COLORS['1'][0]}{'✅ Installed' if hashcat_installed else '❌ Not Installed'}{RESET}")

    if not john_installed and not hashcat_installed:
        print(f"\n{BOLD}Install with:{RESET}")
        print("  John:    sudo apt-get install john")
        print("  Hashcat: sudo apt-get install hashcat")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return

    print(f"\n{BOLD}Options:{RESET}")
    if john_installed:
        print(f" {BOLD}[1]{RESET} 🔓 John the Ripper - Crack password file")
        print(f" {BOLD}[2]{RESET} 📊 John - Show cracked passwords")
        print(f" {BOLD}[3]{RESET} 📝 John - Custom command")
    if hashcat_installed:
        print(f" {BOLD}[4]{RESET} ⚡ Hashcat - Crack hash")
        print(f" {BOLD}[5]{RESET} 📋 Hashcat - List hash modes")
        print(f" {BOLD}[6]{RESET} 📝 Hashcat - Custom command")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1' and john_installed:
        passwd_file = input("Enter password file path: ").strip()
        if passwd_file:
            os.system(f'john {passwd_file}')
    elif choice == '2' and john_installed:
        passwd_file = input("Enter password file path: ").strip()
        if passwd_file:
            os.system(f'john --show {passwd_file}')
    elif choice == '3' and john_installed:
        cmd = input("Enter john command: ").strip()
        if cmd:
            os.system(cmd)
    elif choice == '4' and hashcat_installed:
        hash_file = input("Enter hash file path: ").strip()
        wordlist = input("Enter wordlist path: ").strip()
        hash_mode = input("Enter hash mode (e.g., 0 for MD5, 1000 for NTLM): ").strip()
        if hash_file and wordlist and hash_mode:
            os.system(f'hashcat -m {hash_mode} {hash_file} {wordlist}')
    elif choice == '5' and hashcat_installed:
        os.system('hashcat --help | grep -E "^\\s+[0-9]+\\s+\\|" | head -50')
    elif choice == '6' and hashcat_installed:
        cmd = input("Enter hashcat command: ").strip()
        if cmd:
            os.system(cmd)

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_hydra_bruteforce():
    """Hydra Brute-forcing Wrapper"""
    print_header("🌊 Hydra Brute-force Tool")

    if not check_pentest_tool('hydra'):
        print(f"{COLORS['1'][0]}❌ Hydra is not installed.{RESET}")
        print(f"\n{BOLD}Install with:{RESET}")
        print("  Ubuntu/Debian: sudo apt-get install hydra")
        print("  Fedora:        sudo dnf install hydra")
        print("  macOS:         brew install hydra")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return

    print(f"{COLORS['2'][0]}✅ Hydra is installed{RESET}\n")
    print(f"{COLORS['4'][0]}⚠️  WARNING: Only test on systems you own or have permission to test!{RESET}\n")
    print(f"{BOLD}Service Brute-force Options:{RESET}")
    print(f" {BOLD}[1]{RESET} 🔐 SSH Brute-force")
    print(f" {BOLD}[2]{RESET} 🌐 HTTP/HTTPS Form Brute-force")
    print(f" {BOLD}[3]{RESET} 📁 FTP Brute-force")
    print(f" {BOLD}[4]{RESET} 💾 RDP Brute-force")
    print(f" {BOLD}[5]{RESET} 📝 Custom Hydra command")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select service: {RESET}").strip()

    if choice == '0':
        return
    elif choice in ['1', '2', '3', '4']:
        target = input("Enter target IP or hostname: ").strip()
        username = input("Enter username (or -L for username list file): ").strip()
        password = input("Enter password (or -P for password list file): ").strip()

        if not target:
            print(f"{COLORS['1'][0]}Target is required{RESET}")
        else:
            if choice == '1':  # SSH
                service = 'ssh'
                port = input("Enter SSH port (default 22): ").strip() or '22'
                cmd = f'hydra -l {username} -p {password} {target} {service} -s {port}'
            elif choice == '2':  # HTTP
                path = input("Enter login path (e.g., /login.php): ").strip()
                form_data = input("Enter POST form data (e.g., username=^USER^&password=^PASS^): ").strip()
                cmd = f'hydra -l {username} -p {password} {target} http-post-form "{path}:{form_data}:F=incorrect"'
            elif choice == '3':  # FTP
                service = 'ftp'
                cmd = f'hydra -l {username} -p {password} {target} {service}'
            elif choice == '4':  # RDP
                service = 'rdp'
                cmd = f'hydra -l {username} -p {password} {target} {service}'

            print(f"\n{COLORS['6'][0]}Executing: {cmd}{RESET}\n")
            os.system(cmd)
    elif choice == '5':
        cmd = input("Enter full hydra command: ").strip()
        if cmd:
            os.system(cmd)

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_pentest_toolkit():
    """Main Penetration Testing Toolkit Menu"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🛡️ PENETRATION TESTING TOOLKIT")

        # Check tool status
        tools_status = {
            "Nmap": check_pentest_tool('nmap'),
            "Metasploit": check_pentest_tool('msfconsole'),
            "Aircrack-ng": check_pentest_tool('aircrack-ng'),
            "John": check_pentest_tool('john'),
            "Hashcat": check_pentest_tool('hashcat'),
            "Hydra": check_pentest_tool('hydra')
        }

        print(f"\n{BOLD}Tool Status Overview:{RESET}")
        for tool, installed in tools_status.items():
            status = f"{COLORS['2'][0]}✅{RESET}" if installed else f"{COLORS['1'][0]}❌{RESET}"
            print(f"  {status} {tool}")

        c = get_current_color()
        print(f"\n{BOLD}{c}╔{'═'*50}╗{RESET}")
        print(f"{BOLD}{c}║{RESET}  {BOLD}PENETRATION TESTING MENU{RESET}{'':>26}{BOLD}{c}║{RESET}")
        print(f"{BOLD}{c}╠{'═'*50}╣{RESET}")
        print(f" {BOLD}[1]{RESET} 🔍 Nmap - Network Scanner")
        print(f" {BOLD}[2]{RESET} 💣 Metasploit Framework")
        print(f" {BOLD}[3]{RESET} 📡 Aircrack-ng - Wireless Security")
        print(f" {BOLD}[4]{RESET} 🌐 Burp Suite - Web App Testing")
        print(f" {BOLD}[5]{RESET} 🔐 Password Crackers (John/Hashcat)")
        print(f" {BOLD}[6]{RESET} 🌊 Hydra - Brute-force Tool")
        print(f" {BOLD}[7]{RESET} 📚 Install Missing Tools")
        print(f" {BOLD}[8]{RESET} 📦 Open Download Center (Pen Test Tools)")
        print(f" {BOLD}[0]{RESET} ↩️  Return to Command Center")
        print(f"{BOLD}{c}╚{'═'*50}╝{RESET}")

        print(f"\n{COLORS['4'][0]}⚠️  LEGAL WARNING: Only use these tools on systems you own or have")
        print(f"   explicit written permission to test. Unauthorized access is illegal!{RESET}")

        choice = input(f"\n{BOLD}🎯 Select tool: {RESET}").strip()

        if choice == '0':
            break
        elif choice == '1':
            feature_nmap_scanner()
        elif choice == '2':
            feature_metasploit_console()
        elif choice == '3':
            feature_aircrack_toolkit()
        elif choice == '4':
            feature_burpsuite()
        elif choice == '5':
            feature_password_cracking()
        elif choice == '6':
            feature_hydra_bruteforce()
        elif choice == '7':
            os.system('cls' if os.name == 'nt' else 'clear')
            print_header("📦 Install Penetration Testing Tools")
            print(f"\n{BOLD}Installation Commands:{RESET}\n")
            print(f"{COLORS['6'][0]}Ubuntu/Debian:{RESET}")
            print("  sudo apt-get update")
            print("  sudo apt-get install nmap metasploit-framework aircrack-ng john hashcat hydra")
            print(f"\n{COLORS['6'][0]}Kali Linux:{RESET}")
            print("  Most tools pre-installed!")
            print("  sudo apt-get install kali-linux-default")
            print(f"\n{COLORS['6'][0]}Fedora/RHEL:{RESET}")
            print("  sudo dnf install nmap aircrack-ng john hydra")
            print(f"\n{COLORS['6'][0]}macOS:{RESET}")
            print("  brew install nmap aircrack-ng john hashcat hydra")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '8':
            feature_download_center()
        else:
            print(f"{COLORS['1'][0]}Invalid option{RESET}")
            time.sleep(1)

# --- END PENETRATION TESTING TOOLKIT ---

# --- PWN TOOLS WRAPPER ---

def _pwn_install_bundle():
    os_key = _detect_os_key()
    catalog = _download_center_catalog()
    entry = catalog.get("pwn_tools", {})

    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📦 PWN Tools Installer")
    cmd_list = _download_center_print_commands(os_key, entry)
    if cmd_list:
        run = input("\nRun install commands now? (y/n): ").strip().lower()
        if run == 'y':
            _download_center_run_commands(cmd_list)
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _pwn_has_pwntools():
    try:
        import pwn
        return True
    except Exception:
        return False

def _pwn_has_gdb():
    return shutil.which("gdb") is not None

def _pwn_has_checksec():
    return shutil.which("checksec") is not None

def _pwn_ropgadget_cmd():
    return shutil.which("ROPgadget") or shutil.which("ropgadget")

def _pwn_has_one_gadget():
    return shutil.which("one_gadget") is not None

def _pwn_prompt_install(name):
    print(f"{COLORS['1'][0]}❌ {name} is not installed.{RESET}")
    install = input("Install PWN tools bundle now? (y/n): ").strip().lower()
    if install == 'y':
        _pwn_install_bundle()
    return False

def _pwn_pwntools_menu():
    if not _pwn_has_pwntools():
        _pwn_prompt_install("Pwntools")
        return

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🧰 Pwntools (Python)")
        print(" [1] Show Quickstart Snippet")
        print(" [2] Print Pwntools Version")
        print(" [0] Return")
        choice = input("\nSelect option: ").strip()
        if choice == '0':
            return
        if choice == '1':
            print("\nQuickstart:")
            print("from pwn import *")
            print("context.binary = './vuln'")
            print("p = process(context.binary.path)")
            print("p.sendline(b'AAAA')")
            print("print(p.recvline())")
            input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")
        elif choice == '2':
            try:
                subprocess.call([sys.executable, "-c", "from pwn import *; import pwnlib; print(pwnlib.__version__)"])
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _pwn_run_gdb():
    if not _pwn_has_gdb():
        _pwn_prompt_install("GDB")
        return
    target = input("Target binary path: ").strip()
    if not target:
        return
    if not os.path.exists(target):
        print(f"{COLORS['1'][0]}❌ File not found{RESET}")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return
    subprocess.call(["gdb", "-q", target])

def _pwn_run_checksec():
    if not _pwn_has_checksec():
        _pwn_prompt_install("checksec")
        return
    target = input("Target binary path: ").strip()
    if not target:
        return
    if not os.path.exists(target):
        print(f"{COLORS['1'][0]}❌ File not found{RESET}")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return
    subprocess.call(["checksec", "--file=" + target])

def _pwn_run_ropgadget():
    cmd = _pwn_ropgadget_cmd()
    if not cmd:
        _pwn_prompt_install("ROPgadget")
        return
    target = input("Target binary path: ").strip()
    if not target:
        return
    if not os.path.exists(target):
        print(f"{COLORS['1'][0]}❌ File not found{RESET}")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return
    subprocess.call([cmd, "--binary", target])

def _pwn_run_one_gadget():
    if not _pwn_has_one_gadget():
        _pwn_prompt_install("one_gadget")
        return
    target = input("Target libc path: ").strip()
    if not target:
        return
    if not os.path.exists(target):
        print(f"{COLORS['1'][0]}❌ File not found{RESET}")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return
    subprocess.call(["one_gadget", target])

def feature_pwn_tools():
    """PWN tools wrapper (pwntools + core helpers)."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("💥 PWN Tools")

        status = {
            "Pwntools": _pwn_has_pwntools(),
            "GDB": _pwn_has_gdb(),
            "checksec": _pwn_has_checksec(),
            "ROPgadget": _pwn_ropgadget_cmd() is not None,
            "one_gadget": _pwn_has_one_gadget()
        }

        print(f"\n{BOLD}Tool Status:{RESET}")
        for tool, installed in status.items():
            flag = f"{COLORS['2'][0]}✅{RESET}" if installed else f"{COLORS['1'][0]}❌{RESET}"
            print(f"  {flag} {tool}")

        print(f"\n{BOLD}Tools:{RESET}")
        print(f" {BOLD}[1]{RESET} Pwntools (Python)")
        print(f" {BOLD}[2]{RESET} GDB Debugger")
        print(f" {BOLD}[3]{RESET} checksec Binary Audit")
        print(f" {BOLD}[4]{RESET} ROPgadget Finder")
        print(f" {BOLD}[5]{RESET} one_gadget (libc gadgets)")
        print(f" {BOLD}[6]{RESET} 📦 Install PWN Tools Bundle")
        print(f" {BOLD}[7]{RESET} 🧰 Open Download Center (PWN Tools)")
        print(f" {BOLD}[0]{RESET} ↩️  Return")

        choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()
        if choice == '0':
            return
        if choice == '1':
            _pwn_pwntools_menu()
        elif choice == '2':
            _pwn_run_gdb()
        elif choice == '3':
            _pwn_run_checksec()
        elif choice == '4':
            _pwn_run_ropgadget()
        elif choice == '5':
            _pwn_run_one_gadget()
        elif choice == '6':
            _pwn_install_bundle()
        elif choice == '7':
            feature_download_center()
        else:
            print(f"{COLORS['1'][0]}Invalid option{RESET}")
            time.sleep(1)

# --- END PWN TOOLS WRAPPER ---

# --- PYTHON POWER WRAPPER ---

def _python_power_require(package, import_name, link):
    try:
        __import__(import_name)
        return True
    except Exception:
        print(f"{COLORS['1'][0]}❌ {package} is not installed.{RESET}")
        print(f"Link: {link}")
        install = input("Install now? (y/n): ").strip().lower()
        if install == 'y':
            os.system(_pip_install_cmd(package))
        return False

def _python_power_translator():
    if not _python_power_require("googletrans==4.0.0rc1", "googletrans", "https://pypi.org/project/googletrans/"):
        return
    try:
        from googletrans import Translator
    except Exception as e:
        print(f"❌ Translator import error: {e}")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return
    text = input("Text to translate: ").strip()
    if not text:
        return
    dest = input("Target language (e.g., es, fr, de) [en]: ").strip() or "en"
    src = input("Source language (Enter for auto): ").strip() or None
    try:
        translator = Translator()
        result = translator.translate(text, dest=dest, src=src) if src else translator.translate(text, dest=dest)
        print(f"\nTranslated ({result.src} -> {result.dest}):\n{result.text}")
    except Exception as e:
        print(f"❌ Translation error: {e}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _python_power_metaprogramming():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🧬 Metaprogramming")
    print("Python can inspect and modify code at runtime using modules like inspect, ast, and types.")
    print("Use cases: self-repair, dynamic patching, runtime feature flags, and code analysis.")
    demo = input("\nRun a small inspection demo? (y/n): ").strip().lower()
    if demo == 'y':
        import inspect
        def _demo(x):
            return x * 2
        print("\nFunction name:", _demo.__name__)
        print("Source:\n", inspect.getsource(_demo))
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _python_power_functional():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🔁 Functional Programming")
    print("Core tools: lambda, map, filter, reduce, itertools.")
    demo = input("\nRun a small functional demo? (y/n): ").strip().lower()
    if demo == 'y':
        from functools import reduce
        import itertools
        data = [1, 2, 3, 4, 5]
        mapped = list(map(lambda x: x * 2, data))
        filtered = list(filter(lambda x: x % 2 == 0, data))
        reduced = reduce(lambda a, b: a + b, data)
        combos = list(itertools.combinations(data, 2))[:5]
        print("\nmap:", mapped)
        print("filter:", filtered)
        print("reduce:", reduced)
        print("itertools.combinations (first 5):", combos)
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _python_power_audio_signal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🎵 Audio & Signal Processing")
    print("Common libs: numpy, scipy, librosa, pydub (FFmpeg recommended).")
    ok = _python_power_require("numpy", "numpy", "https://pypi.org/project/numpy/")
    if ok:
        try:
            import numpy as np
            freq = 440
            sample_rate = 8000
            t = np.linspace(0, 0.01, int(sample_rate * 0.01), endpoint=False)
            wave = np.sin(2 * np.pi * freq * t)
            print("\nGenerated a short 440Hz sine wave buffer (first 10 samples):")
            print([round(x, 4) for x in wave[:10]])
        except Exception as e:
            print(f"❌ Demo error: {e}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _python_power_hardware_robotics():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🤖 Hardware Control & Robotics")
    print("Common libs: gpiozero, RPi.GPIO, pyserial, smbus2, asyncio for IoT.")
    _python_power_require("pyserial", "serial", "https://pypi.org/project/pyserial/")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _python_power_scientific():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🔬 Scientific Simulation & Modeling")
    print("Core libs: numpy, scipy, numba (JIT), matplotlib for plotting.")
    ok = _python_power_require("numpy", "numpy", "https://pypi.org/project/numpy/")
    _python_power_require("scipy", "scipy", "https://pypi.org/project/scipy/")
    _python_power_require("numba", "numba", "https://pypi.org/project/numba/")
    if ok:
        try:
            import numpy as np
            a = np.arange(5)
            b = np.arange(5, 10)
            print("\nVector add demo:", a + b)
        except Exception as e:
            print(f"❌ Demo error: {e}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_python_power():
    """Python Power - advanced capabilities showcase."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🐍 Python Power")
        print(" [1] Language Translator (CLI)")
        print(" [2] Metaprogramming & Self-Inspection")
        print(" [3] Functional Programming Toolkit")
        print(" [4] Audio & Signal Processing")
        print(" [5] Hardware Control & Robotics")
        print(" [6] Scientific Simulation & Modeling")
        print(" [7] Open Download Center (Python Libraries)")
        print(" [0] Return")

        choice = input("\nSelect option: ").strip()
        if choice == '0':
            return
        if choice == '1':
            _python_power_translator()
        elif choice == '2':
            _python_power_metaprogramming()
        elif choice == '3':
            _python_power_functional()
        elif choice == '4':
            _python_power_audio_signal()
        elif choice == '5':
            _python_power_hardware_robotics()
        elif choice == '6':
            _python_power_scientific()
        elif choice == '7':
            feature_download_center()
        else:
            print(f"{COLORS['1'][0]}Invalid option{RESET}")
            time.sleep(1)

# --- END PYTHON POWER WRAPPER ---

# --- DEFENCE CENTER: PROACTIVE SECURITY MEASURES ---

def feature_adblocker_setup():
    """Ad Blocker Setup and Management"""
    print_header("🚫 Ad Blocker Management")

    print(f"{BOLD}Browser-Based Ad Blocking:{RESET}\n")
    print(f" {BOLD}[1]{RESET} 📦 Install uBlock Origin (Browser Extension)")
    print(f" {BOLD}[2]{RESET} 📦 Install AdGuard (Browser Extension)")
    print(f" {BOLD}[3]{RESET} 🌐 System-Wide DNS Ad Blocking (AdGuard DNS)")
    print(f" {BOLD}[4]{RESET} 📝 Configure /etc/hosts file for ad blocking")
    print(f" {BOLD}[5]{RESET} 🔍 Check current ad blocking status")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        print(f"\n{COLORS['2'][0]}uBlock Origin Extension Links:{RESET}")
        print("  Chrome/Edge: https://chrome.google.com/webstore -> Search 'uBlock Origin'")
        print("  Firefox: https://addons.mozilla.org -> Search 'uBlock Origin'")
    elif choice == '2':
        print(f"\n{COLORS['2'][0]}AdGuard Extension Links:{RESET}")
        print("  Chrome/Edge: https://chrome.google.com/webstore -> Search 'AdGuard'")
        print("  Firefox: https://addons.mozilla.org -> Search 'AdGuard'")
    elif choice == '3':
        print(f"\n{COLORS['6'][0]}Setting up AdGuard DNS...{RESET}")
        print("Add these DNS servers to your network settings:")
        print("  Primary:   94.140.14.14")
        print("  Secondary: 94.140.15.15")
        if os.name != 'nt':
            apply = input("\n🔧 Apply now to /etc/resolv.conf? (requires sudo) [y/n]: ").strip().lower()
            if apply == 'y':
                os.system("sudo bash -c 'echo \"nameserver 94.140.14.14\" > /etc/resolv.conf'")
                os.system("sudo bash -c 'echo \"nameserver 94.140.15.15\" >> /etc/resolv.conf'")
                print(f"{COLORS['2'][0]}✅ DNS updated!{RESET}")
    elif choice == '4':
        print(f"\n{COLORS['6'][0]}Downloading ad-blocking hosts file...{RESET}")
        try:
            hosts_url = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
            print(f"Fetching from: {hosts_url}")
            print(f"\n{COLORS['4'][0]}Note: Requires sudo to apply to /etc/hosts{RESET}")
            apply = input("Download and view? [y/n]: ").strip().lower()
            if apply == 'y':
                resp = requests.get(hosts_url, timeout=10)
                print(f"\n{COLORS['2'][0]}✅ Downloaded {len(resp.text)} bytes{RESET}")
                print("Preview (first 500 chars):")
                print(resp.text[:500])
        except Exception as e:
            print(f"{COLORS['1'][0]}❌ Error: {e}{RESET}")
    elif choice == '5':
        print(f"\n{COLORS['6'][0]}Checking ad blocking status...{RESET}")
        try:
            # Check DNS
            if os.path.exists('/etc/resolv.conf'):
                with open('/etc/resolv.conf', 'r') as f:
                    content = f.read()
                    if '94.140.14.14' in content:
                        print(f"{COLORS['2'][0]}✅ AdGuard DNS detected{RESET}")
                    else:
                        print(f"{COLORS['4'][0]}⚠️  No custom DNS detected{RESET}")
        except:
            pass

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_vpn_management():
    """VPN Setup: WireGuard and OpenVPN"""
    print_header("🔐 VPN Management")

    wg_installed = check_pentest_tool('wg')
    ovpn_installed = check_pentest_tool('openvpn')

    print(f"{BOLD}VPN Tool Status:{RESET}")
    print(f"  WireGuard:  {COLORS['2'][0] if wg_installed else COLORS['1'][0]}{'✅ Installed' if wg_installed else '❌ Not Installed'}{RESET}")
    print(f"  OpenVPN:    {COLORS['2'][0] if ovpn_installed else COLORS['1'][0]}{'✅ Installed' if ovpn_installed else '❌ Not Installed'}{RESET}")

    print(f"\n{BOLD}VPN Options:{RESET}")
    print(f" {BOLD}[1]{RESET} 🔧 Setup WireGuard Server")
    print(f" {BOLD}[2]{RESET} 📱 Setup WireGuard Client")
    print(f" {BOLD}[3]{RESET} 🔍 Check WireGuard Status")
    print(f" {BOLD}[4]{RESET} 🔧 Setup OpenVPN Server")
    print(f" {BOLD}[5]{RESET} 📱 Setup OpenVPN Client")
    print(f" {BOLD}[6]{RESET} 🔍 Check OpenVPN Status")
    print(f" {BOLD}[7]{RESET} 📦 Install VPN Tools")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        if not wg_installed:
            print(f"{COLORS['1'][0]}❌ WireGuard not installed!{RESET}")
        else:
            print(f"\n{COLORS['6'][0]}WireGuard Server Setup:{RESET}")
            print("Commands to set up WireGuard server:")
            print("  sudo wg genkey | tee privatekey | wg pubkey > publickey")
            print("  sudo nano /etc/wireguard/wg0.conf")
            print("\nExample config:")
            print("  [Interface]")
            print("  PrivateKey = <your-private-key>")
            print("  Address = 10.0.0.1/24")
            print("  ListenPort = 51820")
            run = input("\n🚀 Run setup wizard? [y/n]: ").strip().lower()
            if run == 'y':
                os.system("sudo wg")
    elif choice == '2':
        if not wg_installed:
            print(f"{COLORS['1'][0]}❌ WireGuard not installed!{RESET}")
        else:
            print(f"\n{COLORS['6'][0]}WireGuard Client Setup:{RESET}")
            config_path = input("📂 Enter path to .conf file: ").strip()
            if os.path.exists(config_path):
                os.system(f"sudo wg-quick up {config_path}")
            else:
                print(f"{COLORS['1'][0]}❌ Config file not found{RESET}")
    elif choice == '3':
        if wg_installed:
            os.system("sudo wg show")
        else:
            print(f"{COLORS['1'][0]}❌ WireGuard not installed{RESET}")
    elif choice == '4':
        if not ovpn_installed:
            print(f"{COLORS['1'][0]}❌ OpenVPN not installed!{RESET}")
        else:
            print(f"\n{COLORS['6'][0]}OpenVPN Server Setup:{RESET}")
            print("Use the following to set up OpenVPN server:")
            print("  wget https://git.io/vpn -O openvpn-install.sh")
            print("  sudo bash openvpn-install.sh")
    elif choice == '5':
        if not ovpn_installed:
            print(f"{COLORS['1'][0]}❌ OpenVPN not installed!{RESET}")
        else:
            config_path = input("📂 Enter path to .ovpn file: ").strip()
            if os.path.exists(config_path):
                os.system(f"sudo openvpn --config {config_path}")
            else:
                print(f"{COLORS['1'][0]}❌ Config file not found{RESET}")
    elif choice == '6':
        if ovpn_installed:
            os.system("sudo systemctl status openvpn")
        else:
            print(f"{COLORS['1'][0]}❌ OpenVPN not installed{RESET}")
    elif choice == '7':
        print(f"\n{BOLD}Installation Commands:{RESET}\n")
        print(f"{COLORS['6'][0]}Ubuntu/Debian:{RESET}")
        print("  sudo apt-get update")
        print("  sudo apt-get install wireguard openvpn")
        print(f"\n{COLORS['6'][0]}Fedora:{RESET}")
        print("  sudo dnf install wireguard-tools openvpn")
        print(f"\n{COLORS['6'][0]}macOS:{RESET}")
        print("  brew install wireguard-tools openvpn")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_pihole_management():
    """Pi-hole Network-wide Ad Blocking"""
    print_header("🕳️ Pi-hole Network Ad Blocker")

    pihole_installed = os.path.exists('/usr/local/bin/pihole') or check_pentest_tool('pihole')

    print(f"{BOLD}Pi-hole Status:{RESET}")
    print(f"  Installed: {COLORS['2'][0] if pihole_installed else COLORS['1'][0]}{'✅ Yes' if pihole_installed else '❌ No'}{RESET}")

    print(f"\n{BOLD}Pi-hole Options:{RESET}")
    print(f" {BOLD}[1]{RESET} 📦 Install Pi-hole")
    print(f" {BOLD}[2]{RESET} 🔍 Check Pi-hole Status")
    print(f" {BOLD}[3]{RESET} 🌐 Open Pi-hole Web Interface")
    print(f" {BOLD}[4]{RESET} 🔄 Update Pi-hole")
    print(f" {BOLD}[5]{RESET} 📊 View Pi-hole Statistics")
    print(f" {BOLD}[6]{RESET} ⚙️ Configure Pi-hole")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        print(f"\n{COLORS['6'][0]}Installing Pi-hole...{RESET}")
        print("Running automated installer...")
        install = input("Continue? [y/n]: ").strip().lower()
        if install == 'y':
            os.system("curl -sSL https://install.pi-hole.net | bash")
    elif choice == '2':
        if pihole_installed:
            os.system("pihole status")
        else:
            print(f"{COLORS['1'][0]}❌ Pi-hole not installed{RESET}")
    elif choice == '3':
        print(f"\n{COLORS['6'][0]}Pi-hole Web Interface:{RESET}")
        print("  URL: http://pi.hole/admin")
        print("  or:  http://<your-pi-ip>/admin")
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            print(f"  Your IP: http://{ip}/admin")
        except:
            pass
    elif choice == '4':
        if pihole_installed:
            os.system("pihole -up")
        else:
            print(f"{COLORS['1'][0]}❌ Pi-hole not installed{RESET}")
    elif choice == '5':
        if pihole_installed:
            os.system("pihole -c -e")
        else:
            print(f"{COLORS['1'][0]}❌ Pi-hole not installed{RESET}")
    elif choice == '6':
        if pihole_installed:
            os.system("pihole -r")
        else:
            print(f"{COLORS['1'][0]}❌ Pi-hole not installed{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_threat_intelligence():
    """Threat Intelligence & Analysis Tools"""
    print_header("🎯 Threat Intelligence & Analysis")

    print(f"{BOLD}Intelligence Options:{RESET}")
    print(f" {BOLD}[1]{RESET} 🔍 Analyze Suspicious IP Address")
    print(f" {BOLD}[2]{RESET} 📊 Check Open Ports on Target")
    print(f" {BOLD}[3]{RESET} 🦠 VirusTotal Hash Lookup (requires API key)")
    print(f" {BOLD}[4]{RESET} 🌐 WHOIS Domain Lookup")
    print(f" {BOLD}[5]{RESET} 📈 DNS Enumeration")
    print(f" {BOLD}[6]{RESET} 🔐 SSL Certificate Analysis")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        ip = input("🔍 Enter IP address to analyze: ").strip()
        if ip:
            print(f"\n{COLORS['6'][0]}Analyzing {ip}...{RESET}")
            try:
                # IP geolocation
                resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
                data = resp.json()
                if data.get('status') == 'success':
                    print(f"\n{BOLD}Geolocation Data:{RESET}")
                    print(f"  Country: {data.get('country', 'N/A')}")
                    print(f"  Region: {data.get('regionName', 'N/A')}")
                    print(f"  City: {data.get('city', 'N/A')}")
                    print(f"  ISP: {data.get('isp', 'N/A')}")
                    print(f"  Org: {data.get('org', 'N/A')}")
                    print(f"  AS: {data.get('as', 'N/A')}")
            except Exception as e:
                print(f"{COLORS['1'][0]}❌ Error: {e}{RESET}")
    elif choice == '2':
        target = input("🎯 Enter target IP/hostname: ").strip()
        if target:
            if check_pentest_tool('nmap'):
                os.system(f"nmap -F {target}")
            else:
                print(f"{COLORS['1'][0]}❌ nmap not installed{RESET}")
    elif choice == '3':
        print(f"\n{COLORS['6'][0]}VirusTotal Hash Lookup{RESET}")
        print("Get your API key from: https://www.virustotal.com/")
        api_key = input("🔑 Enter VirusTotal API key (or Enter to skip): ").strip()
        if api_key:
            file_hash = input("🔍 Enter file hash (MD5/SHA1/SHA256): ").strip()
            if file_hash:
                try:
                    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
                    headers = {"x-apikey": api_key}
                    resp = requests.get(url, headers=headers, timeout=10)
                    print(f"\n{BOLD}Response:{RESET}")
                    print(resp.text[:500])
                except Exception as e:
                    print(f"{COLORS['1'][0]}❌ Error: {e}{RESET}")
    elif choice == '4':
        domain = input("🌐 Enter domain: ").strip()
        if domain:
            if check_pentest_tool('whois'):
                os.system(f"whois {domain}")
            else:
                print(f"{COLORS['1'][0]}❌ whois not installed. Install: sudo apt-get install whois{RESET}")
    elif choice == '5':
        domain = input("🌐 Enter domain for DNS enum: ").strip()
        if domain:
            if check_pentest_tool('dig'):
                os.system(f"dig {domain} ANY")
            elif check_pentest_tool('nslookup'):
                os.system(f"nslookup {domain}")
            else:
                print(f"{COLORS['1'][0]}❌ DNS tools not found{RESET}")
    elif choice == '6':
        domain = input("🌐 Enter domain: ").strip()
        if domain:
            os.system(f"openssl s_client -connect {domain}:443 -showcerts < /dev/null 2>/dev/null | openssl x509 -noout -text")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_log_analysis():
    """SIEM Log Analysis and Pattern Detection"""
    print_header("📋 Log Analysis & SIEM")

    print(f"{BOLD}Log Analysis Options:{RESET}")
    print(f" {BOLD}[1]{RESET} 🔍 Analyze Authentication Logs (auth.log)")
    print(f" {BOLD}[2]{RESET} 🌐 Analyze Web Server Logs (Apache/Nginx)")
    print(f" {BOLD}[3]{RESET} 🔐 Find Failed Login Attempts")
    print(f" {BOLD}[4]{RESET} 🌍 Detect Geographic Anomalies")
    print(f" {BOLD}[5]{RESET} ⏰ Find Unusual Login Times")
    print(f" {BOLD}[6]{RESET} 📊 Generate Log Statistics")
    print(f" {BOLD}[7]{RESET} 🔎 Custom Log Search (grep)")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        log_paths = ['/var/log/auth.log', '/var/log/secure']
        found_log = None
        for log_path in log_paths:
            if os.path.exists(log_path):
                found_log = log_path
                break

        if found_log:
            print(f"\n{COLORS['6'][0]}Analyzing {found_log}...{RESET}")
            os.system(f"sudo tail -n 50 {found_log}")
        else:
            print(f"{COLORS['1'][0]}❌ Auth logs not found{RESET}")
    elif choice == '2':
        log_paths = ['/var/log/apache2/access.log', '/var/log/nginx/access.log']
        print(f"\n{COLORS['6'][0]}Checking web server logs...{RESET}")
        for log_path in log_paths:
            if os.path.exists(log_path):
                print(f"\nFound: {log_path}")
                os.system(f"sudo tail -n 20 {log_path}")
    elif choice == '3':
        print(f"\n{COLORS['6'][0]}Searching for failed login attempts...{RESET}")
        if os.path.exists('/var/log/auth.log'):
            os.system("sudo grep 'Failed password' /var/log/auth.log | tail -n 20")
        elif os.path.exists('/var/log/secure'):
            os.system("sudo grep 'Failed password' /var/log/secure | tail -n 20")
        else:
            print(f"{COLORS['1'][0]}❌ Auth logs not found{RESET}")
    elif choice == '4':
        print(f"\n{COLORS['6'][0]}Analyzing geographic patterns...{RESET}")
        print("Extracting IP addresses from logs...")
        if os.path.exists('/var/log/auth.log'):
            os.system("sudo grep 'sshd' /var/log/auth.log | grep -oE '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b' | sort -u | head -n 10")
    elif choice == '5':
        print(f"\n{COLORS['6'][0]}Checking login times...{RESET}")
        os.system("last | head -n 20")
    elif choice == '6':
        print(f"\n{COLORS['6'][0]}Generating log statistics...{RESET}")
        if os.path.exists('/var/log/auth.log'):
            print("\n📊 Top 10 Event Types:")
            os.system("sudo awk '{print $5}' /var/log/auth.log | sort | uniq -c | sort -rn | head -n 10")
    elif choice == '7':
        log_file = input("📂 Enter log file path: ").strip()
        if os.path.exists(log_file):
            pattern = input("🔍 Enter search pattern: ").strip()
            if pattern:
                os.system(f"sudo grep '{pattern}' {log_file} | tail -n 30")
        else:
            print(f"{COLORS['1'][0]}❌ Log file not found{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_malware_analysis():
    """Malware Analysis and Reverse Engineering Tools"""
    print_header("🦠 Malware Analysis Tools")

    print(f"{BOLD}Analysis Tools:{RESET}")
    print(f" {BOLD}[1]{RESET} 🔍 File Hash Calculator (MD5/SHA256)")
    print(f" {BOLD}[2]{RESET} 📝 String Analysis (extract strings)")
    print(f" {BOLD}[3]{RESET} 🔬 File Type Analysis")
    print(f" {BOLD}[4]{RESET} 🧬 Hexdump Analysis")
    print(f" {BOLD}[5]{RESET} 📊 Check File with VirusTotal")
    print(f" {BOLD}[6]{RESET} 🔓 Disassemble Binary (requires objdump)")
    print(f" {BOLD}[7]{RESET} 🔍 Scan with ClamAV")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        file_path = input("📂 Enter file path: ").strip()
        if os.path.exists(file_path):
            import hashlib
            print(f"\n{COLORS['6'][0]}Calculating hashes...{RESET}")
            with open(file_path, 'rb') as f:
                data = f.read()
                md5 = hashlib.md5(data).hexdigest()
                sha256 = hashlib.sha256(data).hexdigest()
                print(f"\n{BOLD}MD5:{RESET}    {md5}")
                print(f"{BOLD}SHA256:{RESET} {sha256}")
        else:
            print(f"{COLORS['1'][0]}❌ File not found{RESET}")
    elif choice == '2':
        file_path = input("📂 Enter file path: ").strip()
        if os.path.exists(file_path):
            print(f"\n{COLORS['6'][0]}Extracting strings...{RESET}")
            os.system(f"strings '{file_path}' | head -n 50")
        else:
            print(f"{COLORS['1'][0]}❌ File not found{RESET}")
    elif choice == '3':
        file_path = input("📂 Enter file path: ").strip()
        if os.path.exists(file_path):
            print(f"\n{COLORS['6'][0]}Analyzing file type...{RESET}")
            os.system(f"file '{file_path}'")
            if check_pentest_tool('exiftool'):
                print(f"\n{BOLD}Metadata:{RESET}")
                os.system(f"exiftool '{file_path}'")
        else:
            print(f"{COLORS['1'][0]}❌ File not found{RESET}")
    elif choice == '4':
        file_path = input("📂 Enter file path: ").strip()
        if os.path.exists(file_path):
            print(f"\n{COLORS['6'][0]}Hexdump (first 256 bytes):{RESET}")
            os.system(f"hexdump -C '{file_path}' | head -n 16")
        else:
            print(f"{COLORS['1'][0]}❌ File not found{RESET}")
    elif choice == '5':
        file_path = input("📂 Enter file path: ").strip()
        if os.path.exists(file_path):
            import hashlib
            with open(file_path, 'rb') as f:
                sha256 = hashlib.sha256(f.read()).hexdigest()
            print(f"\n{COLORS['6'][0]}File SHA256:{RESET} {sha256}")
            print(f"Check on VirusTotal: https://www.virustotal.com/gui/file/{sha256}")
        else:
            print(f"{COLORS['1'][0]}❌ File not found{RESET}")
    elif choice == '6':
        file_path = input("📂 Enter binary path: ").strip()
        if os.path.exists(file_path):
            if check_pentest_tool('objdump'):
                print(f"\n{COLORS['6'][0]}Disassembling...{RESET}")
                os.system(f"objdump -d '{file_path}' | head -n 50")
            else:
                print(f"{COLORS['1'][0]}❌ objdump not installed{RESET}")
        else:
            print(f"{COLORS['1'][0]}❌ File not found{RESET}")
    elif choice == '7':
        if check_pentest_tool('clamscan'):
            target = input("📂 Enter path to scan: ").strip()
            if os.path.exists(target):
                print(f"\n{COLORS['6'][0]}Scanning with ClamAV...{RESET}")
                os.system(f"clamscan -r '{target}'")
            else:
                print(f"{COLORS['1'][0]}❌ Path not found{RESET}")
        else:
            print(f"{COLORS['1'][0]}❌ ClamAV not installed. Install: sudo apt-get install clamav{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_devsecops():
    """DevSecOps Integration Tools"""
    print_header("🛡️ DevSecOps Integration")

    print(f"{BOLD}DevSecOps Tools:{RESET}")
    print(f" {BOLD}[1]{RESET} 🧪 Run pytest Security Tests")
    print(f" {BOLD}[2]{RESET} 🔍 Security Code Scanner (Bandit)")
    print(f" {BOLD}[3]{RESET} 📦 Dependency Vulnerability Check (Safety)")
    print(f" {BOLD}[4]{RESET} 🔐 Git Secret Scanner")
    print(f" {BOLD}[5]{RESET} 🐳 Docker Security Scan")
    print(f" {BOLD}[6]{RESET} 📊 Generate Security Report")
    print(f" {BOLD}[7]{RESET} 📦 Install DevSecOps Tools")
    print(f" {BOLD}[0]{RESET} ↩️  Return")

    choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        if check_pentest_tool('pytest'):
            test_path = input("📂 Enter test directory [./tests]: ").strip() or "./tests"
            print(f"\n{COLORS['6'][0]}Running pytest security tests...{RESET}")
            os.system(f"pytest {test_path} -v")
        else:
            print(f"{COLORS['1'][0]}❌ pytest not installed. Install: pip install pytest{RESET}")
    elif choice == '2':
        if check_pentest_tool('bandit'):
            target = input("📂 Enter path to scan [.]: ").strip() or "."
            print(f"\n{COLORS['6'][0]}Running Bandit security scanner...{RESET}")
            os.system(f"bandit -r {target}")
        else:
            print(f"{COLORS['1'][0]}❌ Bandit not installed. Install: pip install bandit{RESET}")
    elif choice == '3':
        if check_pentest_tool('safety'):
            print(f"\n{COLORS['6'][0]}Checking dependencies for vulnerabilities...{RESET}")
            os.system("safety check")
        else:
            print(f"{COLORS['1'][0]}❌ Safety not installed. Install: pip install safety{RESET}")
    elif choice == '4':
        if check_pentest_tool('trufflehog'):
            repo = input("📂 Enter repo path [.]: ").strip() or "."
            print(f"\n{COLORS['6'][0]}Scanning for secrets...{RESET}")
            os.system(f"trufflehog filesystem {repo}")
        else:
            print(f"{COLORS['1'][0]}❌ TruffleHog not installed. Install: pip install trufflehog{RESET}")
    elif choice == '5':
        image = input("🐳 Enter Docker image name: ").strip()
        if image:
            if check_pentest_tool('docker'):
                print(f"\n{COLORS['6'][0]}Scanning Docker image...{RESET}")
                os.system(f"docker scan {image}")
            else:
                print(f"{COLORS['1'][0]}❌ Docker not installed{RESET}")
    elif choice == '6':
        print(f"\n{COLORS['6'][0]}Generating comprehensive security report...{RESET}")
        report_file = f"security_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_file, 'w') as f:
            f.write("=== SECURITY REPORT ===\n")
            f.write(f"Generated: {datetime.datetime.now()}\n\n")
        print(f"{COLORS['2'][0]}✅ Report saved to: {report_file}{RESET}")
    elif choice == '7':
        print(f"\n{BOLD}Installation Commands:{RESET}\n")
        print(f"{COLORS['6'][0]}Python Security Tools:{RESET}")
        print("  pip install pytest bandit safety trufflehog")
        print(f"\n{COLORS['6'][0]}System Tools:{RESET}")
        print("  sudo apt-get install docker.io clamav")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_defence_center():
    """Main Defence Center - Proactive Security Menu"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🛡️ DEFENCE CENTER")

        # Check tool status
        defence_tools = {
            "WireGuard": check_pentest_tool('wg'),
            "OpenVPN": check_pentest_tool('openvpn'),
            "Pi-hole": os.path.exists('/usr/local/bin/pihole'),
            "ClamAV": check_pentest_tool('clamscan'),
            "Bandit": check_pentest_tool('bandit'),
            "pytest": check_pentest_tool('pytest')
        }

        print(f"\n{BOLD}Defence Tool Status:{RESET}")
        for tool, installed in defence_tools.items():
            status = f"{COLORS['2'][0]}✅{RESET}" if installed else f"{COLORS['1'][0]}❌{RESET}"
            print(f"  {status} {tool}")

        c = get_current_color()
        print(f"\n{BOLD}{c}╔{'═'*60}╗{RESET}")
        print(f"{BOLD}{c}║{RESET}  {BOLD}PROACTIVE DEFENCE & SECURITY OPERATIONS{RESET}{'':>20}{BOLD}{c}║{RESET}")
        print(f"{BOLD}{c}╠{'═'*60}╣{RESET}")
        print(f" {BOLD}[1]{RESET} 🚫 Ad Blocker Management")
        print(f" {BOLD}[2]{RESET} 🔐 VPN Setup (WireGuard/OpenVPN)")
        print(f" {BOLD}[3]{RESET} 🕳️  Pi-hole Network Ad Blocking")
        print(f" {BOLD}[4]{RESET} 🎯 Threat Intelligence & Analysis")
        print(f" {BOLD}[5]{RESET} 📋 SIEM Log Analysis")
        print(f" {BOLD}[6]{RESET} 🦠 Malware Analysis Tools")
        print(f" {BOLD}[7]{RESET} 🛡️  DevSecOps Integration")
        print(f" {BOLD}[8]{RESET} 📚 Install All Defence Tools")
        print(f" {BOLD}[9]{RESET} 📦 Open Download Center (Defence Tools)")
        print(f" {BOLD}[0]{RESET} ↩️  Return to Command Center")
        print(f"{BOLD}{c}╚{'═'*60}╝{RESET}")

        print(f"\n{COLORS['2'][0]}ℹ️  Proactive defence focuses on prevention, detection, and response{RESET}")

        choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()

        if choice == '0':
            break
        elif choice == '1':
            feature_adblocker_setup()
        elif choice == '2':
            feature_vpn_management()
        elif choice == '3':
            feature_pihole_management()
        elif choice == '4':
            feature_threat_intelligence()
        elif choice == '5':
            feature_log_analysis()
        elif choice == '6':
            feature_malware_analysis()
        elif choice == '7':
            feature_devsecops()
        elif choice == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            print_header("📦 Install Defence Tools")
            print(f"\n{BOLD}Complete Installation Commands:{RESET}\n")
            print(f"{COLORS['6'][0]}Ubuntu/Debian:{RESET}")
            print("  sudo apt-get update")
            print("  sudo apt-get install wireguard openvpn clamav clamav-daemon")
            print("  sudo apt-get install whois dnsutils")
            print("  pip install pytest bandit safety trufflehog")
            print(f"\n{COLORS['6'][0]}Pi-hole:{RESET}")
            print("  curl -sSL https://install.pi-hole.net | bash")
            print(f"\n{COLORS['6'][0]}macOS:{RESET}")
            print("  brew install wireguard-tools openvpn clamav")
            print("  pip install pytest bandit safety trufflehog")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '9':
            feature_download_center()
        else:
            print(f"{COLORS['1'][0]}Invalid option{RESET}")
            time.sleep(1)

# --- END DEFENCE CENTER ---

# --- DOWNLOAD CENTER: OS-AWARE INSTALL MENUS ---

def _read_os_release():
    data = {}
    try:
        with open("/etc/os-release", "r") as f:
            for line in f:
                if "=" in line:
                    k, v = line.strip().split("=", 1)
                    data[k] = v.strip().strip('"')
    except Exception:
        pass
    return data

def _detect_os_key():
    sysname = platform.system()
    if sysname == "Windows":
        return "windows"
    if sysname == "Darwin":
        return "macos"
    if sysname == "Linux":
        if os.environ.get("TERMUX_VERSION") or os.environ.get("ANDROID_ROOT"):
            return "android"
        osr = _read_os_release()
        os_id = (osr.get("ID") or "").lower()
        like = (osr.get("ID_LIKE") or "").lower()
        if "kali" in os_id or "kali" in like:
            return "kali"
        if os_id in ["ubuntu", "debian", "linuxmint", "pop"] or "debian" in like:
            return "debian"
        if os_id in ["fedora", "rhel", "centos", "rocky", "almalinux"] or "rhel" in like or "fedora" in like:
            return "fedora"
        if os_id in ["arch", "manjaro"] or "arch" in like:
            return "arch"
        if os_id in ["alpine"]:
            return "alpine"
        return "linux"
    return "unknown"

def _pip_install_cmd(package):
    exe = sys.executable.replace("\\", "/")
    return f"{exe} -m pip install --upgrade {package}"

def _pip_install_cmds(packages):
    return [_pip_install_cmd(pkg) for pkg in packages]

def _download_center_catalog():
    return {
        "pentest": {
            "title": "Pen Test Tools (Command Center 12)",
            "commands": {
                "debian": [
                    "sudo apt-get update",
                    "sudo apt-get install -y nmap",
                    "sudo apt-get install -y metasploit-framework",
                    "sudo apt-get install -y aircrack-ng",
                    "sudo apt-get install -y john",
                    "sudo apt-get install -y hashcat",
                    "sudo apt-get install -y hydra"
                ],
                "kali": [
                    "sudo apt-get update",
                    "sudo apt-get install -y kali-linux-default"
                ],
                "fedora": [
                    "sudo dnf install -y nmap",
                    "sudo dnf install -y aircrack-ng",
                    "sudo dnf install -y john",
                    "sudo dnf install -y hydra"
                ],
                "arch": [
                    "sudo pacman -Syu --noconfirm nmap",
                    "sudo pacman -Syu --noconfirm aircrack-ng",
                    "sudo pacman -Syu --noconfirm john",
                    "sudo pacman -Syu --noconfirm hashcat",
                    "sudo pacman -Syu --noconfirm hydra"
                ],
                "alpine": [
                    "sudo apk update",
                    "sudo apk add nmap",
                    "sudo apk add aircrack-ng",
                    "sudo apk add john",
                    "sudo apk add hashcat",
                    "sudo apk add hydra"
                ],
                "macos": [
                    "brew install nmap",
                    "brew install aircrack-ng",
                    "brew install john",
                    "brew install hashcat",
                    "brew install hydra"
                ],
                "windows": [
                    "wsl --install -d Ubuntu",
                    "# After reboot, in WSL: sudo apt-get update",
                    "# sudo apt-get install -y nmap metasploit-framework aircrack-ng john hashcat hydra"
                ],
                "android": [
                    "pkg update -y",
                    "pkg install -y nmap",
                    "pkg install -y hydra"
                ],
                "ios": [
                    "# iOS does not support native install for these tools.",
                    "# Use a remote Linux host or iSH (Alpine) where available."
                ],
                "esp32": [
                    "# Use a host computer. Install: pip install esptool platformio"
                ]
            },
            "links": [
                "https://www.kali.org/",
                "https://www.metasploit.com/",
                "https://nmap.org/",
                "https://www.aircrack-ng.org/"
            ]
        },
        "pwn_tools": {
            "title": "PWN Tools (Command Center P)",
            "commands": {
                "debian": [
                    "sudo apt-get update",
                    "sudo apt-get install -y gdb git python3 python3-pip python3-dev ruby",
                    "sudo apt-get install -y checksec",
                ] + _pip_install_cmds(["pwntools", "ropgadget"]) + [
                    "gem install one_gadget"
                ],
                "kali": [
                    "sudo apt-get update",
                    "sudo apt-get install -y gdb git python3 python3-pip python3-dev ruby",
                    "sudo apt-get install -y checksec",
                ] + _pip_install_cmds(["pwntools", "ropgadget"]) + [
                    "gem install one_gadget"
                ],
                "fedora": [
                    "sudo dnf install -y gdb git python3 python3-pip python3-devel ruby",
                    "sudo dnf install -y checksec",
                ] + _pip_install_cmds(["pwntools", "ropgadget"]) + [
                    "gem install one_gadget"
                ],
                "arch": [
                    "sudo pacman -Syu --noconfirm gdb git python python-pip ruby",
                    "sudo pacman -Syu --noconfirm checksec",
                ] + _pip_install_cmds(["pwntools", "ropgadget"]) + [
                    "gem install one_gadget"
                ],
                "alpine": [
                    "sudo apk update",
                    "sudo apk add gdb git python3 py3-pip python3-dev ruby",
                    "sudo apk add checksec",
                ] + _pip_install_cmds(["pwntools", "ropgadget"]) + [
                    "gem install one_gadget"
                ],
                "macos": [
                    "brew install gdb git python ruby",
                    "brew install checksec",
                ] + _pip_install_cmds(["pwntools", "ropgadget"]) + [
                    "gem install one_gadget"
                ],
                "windows": [
                    "# Use WSL2 for best compatibility.",
                    "wsl --install -d Ubuntu",
                    "# Then run the Ubuntu/Debian commands in WSL."
                ],
                "android": [
                    "pkg update -y",
                    "pkg install -y gdb git python ruby",
                ] + _pip_install_cmds(["pwntools", "ropgadget"]) + [
                    "gem install one_gadget"
                ],
                "ios": [
                    "# iOS does not support native installs for these tools.",
                    "# Use a remote Linux host or iSH (Alpine) where available."
                ],
                "esp32": [
                    "# Use a host computer for these tools."
                ],
                "generic": _pip_install_cmds(["pwntools", "ropgadget"]) + [
                    "# Install gdb, checksec, and ruby with your OS package manager",
                    "gem install one_gadget"
                ]
            },
            "links": [
                "https://agrohacksstuff.io/posts/pwntools-tricks-and-examples/",
                "https://docs.pwntools.com/en/stable/",
                "https://sourceware.org/gdb/",
                "https://github.com/JonathanSalwan/ROPgadget",
                "https://github.com/david942j/one_gadget"
            ]
        },
        "mapscii": {
            "title": "MapSCII (Satellite Tracker)",
            "commands": {
                "debian": [
                    "sudo npm install -g mapscii"
                ],
                "kali": [
                    "sudo npm install -g mapscii"
                ],
                "fedora": [
                    "sudo npm install -g mapscii"
                ],
                "arch": [
                    "sudo npm install -g mapscii"
                ],
                "alpine": [
                    "sudo npm install -g mapscii"
                ],
                "linux": [
                    "sudo npm install -g mapscii"
                ],
                "macos": [
                    "npm install -g mapscii"
                ],
                "windows": [
                    "npm install -g mapscii"
                ],
                "android": [
                    "npm install -g mapscii"
                ],
                "ios": [
                    "# iOS does not support native MapSCII installs.",
                    "# Use a remote Linux host or iSH (Alpine) where available."
                ],
                "esp32": [
                    "# Use a host computer for MapSCII."
                ],
                "generic": [
                    "npm install -g mapscii"
                ]
            },
            "links": [
                "https://github.com/rastapasta/mapscii"
            ]
        },
        "defence": {
            "title": "Defence Tools (Command Center 13)",
            "commands": {
                "debian": [
                    "sudo apt-get update",
                    "sudo apt-get install -y wireguard",
                    "sudo apt-get install -y openvpn",
                    "sudo apt-get install -y clamav",
                    "sudo apt-get install -y clamav-daemon",
                    "sudo apt-get install -y whois",
                    "sudo apt-get install -y dnsutils",
                ] + _pip_install_cmds(["pytest", "bandit", "safety", "trufflehog"]),
                "kali": [
                    "sudo apt-get update",
                    "sudo apt-get install -y wireguard",
                    "sudo apt-get install -y openvpn",
                    "sudo apt-get install -y clamav",
                    "sudo apt-get install -y whois",
                    "sudo apt-get install -y dnsutils",
                ] + _pip_install_cmds(["pytest", "bandit", "safety", "trufflehog"]),
                "fedora": [
                    "sudo dnf install -y wireguard-tools",
                    "sudo dnf install -y openvpn",
                    "sudo dnf install -y clamav",
                    "sudo dnf install -y whois",
                    "sudo dnf install -y bind-utils",
                ] + _pip_install_cmds(["pytest", "bandit", "safety", "trufflehog"]),
                "arch": [
                    "sudo pacman -Syu --noconfirm wireguard-tools",
                    "sudo pacman -Syu --noconfirm openvpn",
                    "sudo pacman -Syu --noconfirm clamav",
                    "sudo pacman -Syu --noconfirm whois",
                    "sudo pacman -Syu --noconfirm bind",
                ] + _pip_install_cmds(["pytest", "bandit", "safety", "trufflehog"]),
                "alpine": [
                    "sudo apk update",
                    "sudo apk add wireguard-tools",
                    "sudo apk add openvpn",
                    "sudo apk add clamav",
                    "sudo apk add whois",
                    "sudo apk add bind-tools",
                ] + _pip_install_cmds(["pytest", "bandit", "safety", "trufflehog"]),
                "macos": [
                    "brew install wireguard-tools",
                    "brew install openvpn",
                    "brew install clamav",
                ] + _pip_install_cmds(["pytest", "bandit", "safety", "trufflehog"]),
                "windows": [
                    "# Use WSL2 for best compatibility.",
                    "wsl --install -d Ubuntu",
                    "# Then run the Ubuntu/Debian commands in WSL."
                ],
                "android": [
                    "pkg update -y",
                    "pkg install -y openvpn",
                ] + _pip_install_cmds(["pytest", "bandit", "safety", "trufflehog"]),
                "ios": [
                    "# iOS does not support native install for these tools.",
                    "# Use a remote Linux host or iSH (Alpine) where available."
                ],
                "esp32": [
                    "# Use a host computer for these tools."
                ]
            },
            "links": [
                "https://www.wireguard.com/",
                "https://openvpn.net/",
                "https://www.clamav.net/",
                "https://install.pi-hole.net"
            ]
        },
        "network": {
            "title": "Network/WiFi/Bluetooth Tools (Command Center 0/J/L)",
            "commands": {
                "debian": [
                    "sudo apt-get update",
                    "sudo apt-get install -y net-tools",
                    "sudo apt-get install -y wireless-tools",
                    "sudo apt-get install -y iw",
                    "sudo apt-get install -y iproute2",
                    "sudo apt-get install -y bluez"
                ],
                "kali": [
                    "sudo apt-get update",
                    "sudo apt-get install -y net-tools",
                    "sudo apt-get install -y wireless-tools",
                    "sudo apt-get install -y iw",
                    "sudo apt-get install -y iproute2",
                    "sudo apt-get install -y bluez"
                ],
                "fedora": [
                    "sudo dnf install -y net-tools",
                    "sudo dnf install -y wireless-tools",
                    "sudo dnf install -y iw",
                    "sudo dnf install -y iproute",
                    "sudo dnf install -y bluez"
                ],
                "arch": [
                    "sudo pacman -Syu --noconfirm net-tools",
                    "sudo pacman -Syu --noconfirm wireless_tools",
                    "sudo pacman -Syu --noconfirm iw",
                    "sudo pacman -Syu --noconfirm iproute2",
                    "sudo pacman -Syu --noconfirm bluez"
                ],
                "alpine": [
                    "sudo apk update",
                    "sudo apk add net-tools",
                    "sudo apk add wireless-tools",
                    "sudo apk add iw",
                    "sudo apk add iproute2",
                    "sudo apk add bluez"
                ],
                "macos": [
                    "# WiFi/Bluetooth tools are built-in on macOS.",
                    "brew install blueutil"
                ],
                "windows": [
                    "# Use built-in Windows networking tools or WSL2 for Linux tooling.",
                    "wsl --install -d Ubuntu"
                ],
                "android": [
                    "pkg update -y",
                    "pkg install -y net-tools",
                    "pkg install -y iproute2"
                ],
                "ios": [
                    "# iOS does not support these CLI tools natively."
                ],
                "esp32": [
                    "# Use a host computer for these tools."
                ]
            },
            "links": [
                "https://www.kernel.org/doc/Documentation/networking/",
                "https://git.kernel.org/pub/scm/network/wireless/wireless-regdb.git/"
            ]
        },
        "media": {
            "title": "Media Tools (Command Center I)",
            "commands": {
                "debian": [
                    "sudo apt-get update",
                    "sudo apt-get install -y ffmpeg",
                    "sudo apt-get install -y mpv",
                    "sudo apt-get install -y imagemagick"
                ],
                "kali": [
                    "sudo apt-get update",
                    "sudo apt-get install -y ffmpeg",
                    "sudo apt-get install -y mpv",
                    "sudo apt-get install -y imagemagick"
                ],
                "fedora": [
                    "sudo dnf install -y ffmpeg",
                    "sudo dnf install -y mpv",
                    "sudo dnf install -y ImageMagick"
                ],
                "arch": [
                    "sudo pacman -Syu --noconfirm ffmpeg",
                    "sudo pacman -Syu --noconfirm mpv",
                    "sudo pacman -Syu --noconfirm imagemagick"
                ],
                "alpine": [
                    "sudo apk update",
                    "sudo apk add ffmpeg",
                    "sudo apk add mpv",
                    "sudo apk add imagemagick"
                ],
                "macos": [
                    "brew install ffmpeg",
                    "brew install mpv",
                    "brew install imagemagick"
                ],
                "windows": [
                    "winget install -e --id Gyan.FFmpeg",
                    "winget install -e --id mpv.net"
                ],
                "android": [
                    "pkg update -y",
                    "pkg install -y ffmpeg"
                ],
                "ios": [
                    "# iOS does not support these CLI tools natively."
                ],
                "esp32": [
                    "# Use a host computer for these tools."
                ]
            },
            "links": [
                "https://ffmpeg.org/",
                "https://mpv.io/"
            ]
        },
                "ai": {
            "title": "AI Center Tools (Command Center K)",
            "commands": {
                "debian": _pip_install_cmds(["openai", "anthropic", "google-generativeai", "requests"]),
                "kali": _pip_install_cmds(["openai", "anthropic", "google-generativeai", "requests"]),
                "fedora": _pip_install_cmds(["openai", "anthropic", "google-generativeai", "requests"]),
                "arch": _pip_install_cmds(["openai", "anthropic", "google-generativeai", "requests"]),
                "alpine": _pip_install_cmds(["openai", "anthropic", "google-generativeai", "requests"]),
                "macos": _pip_install_cmds(["openai", "anthropic", "google-generativeai", "requests"]),
                "windows": [
                    "py -m pip install --upgrade openai",
                    "py -m pip install --upgrade anthropic",
                    "py -m pip install --upgrade google-generativeai",
                    "py -m pip install --upgrade requests"
                ],
                "android": _pip_install_cmds(["openai", "anthropic", "google-generativeai", "requests"]),
                "ios": ["# Use a remote host or iSH where available."],
                "esp32": ["# Use a host computer for these tools."]
            },
            "links": [
                "https://platform.openai.com/",
                "https://www.anthropic.com/",
                "https://ai.google.dev/"
            ]
        },
        "core_python": {
            "title": "Core PythonOS Libraries",
            "commands": {
                "generic": _pip_install_cmds(["psutil", "requests", "beautifulsoup4", "Pillow", "gputil"])
            },
            "links": [
                "https://pypi.org/project/psutil/",
                "https://pypi.org/project/requests/",
                "https://pypi.org/project/beautifulsoup4/",
                "https://pypi.org/project/Pillow/",
                "https://pypi.org/project/GPUtil/"
            ]
        },
        "general_python": {
            "title": "General Purpose Python Libraries",
            "commands": {
                "generic": _pip_install_cmds([
                    "requests", "beautifulsoup4", "pytest", "ipython", "jupyter", "rich",
                    "pendulum", "python-dateutil"
                ])
            },
            "links": [
                "https://pypi.org/project/ipython/",
                "https://jupyter.org/",
                "https://pypi.org/project/rich/"
            ]
        },
        "data_science": {
            "title": "Data Science / Analysis Stack",
            "commands": {
                "generic": _pip_install_cmds([
                    "numpy", "pandas", "matplotlib", "seaborn", "scikit-learn"
                ])
            },
            "links": [
                "https://numpy.org/",
                "https://pandas.pydata.org/",
                "https://scikit-learn.org/"
            ]
        },
        "web_dev": {
            "title": "Web Development Stack",
            "commands": {
                "generic": _pip_install_cmds(["flask", "django"])
            },
            "links": [
                "https://flask.palletsprojects.com/",
                "https://www.djangoproject.com/"
            ]
        },
        "text_doc": {
            "title": "Text & Doc Tools (Command Center T)",
            "commands": {
                "debian": [
                    "sudo apt-get update",
                    "sudo apt-get install -y poppler-utils",
                    "sudo apt-get install -y antiword",
                    "sudo apt-get install -y catdoc",
                    "sudo apt-get install -y unrtf",
                    "sudo apt-get install -y pandoc",
                ] + _pip_install_cmds([
                    "pymupdf",
                    "PyPDF2",
                    "python-docx",
                    "ebooklib",
                    "openpyxl",
                    "xlrd",
                    "docx2txt",
                    "textract",
                ]),
                "kali": [
                    "sudo apt-get update",
                    "sudo apt-get install -y poppler-utils",
                    "sudo apt-get install -y antiword",
                    "sudo apt-get install -y catdoc",
                    "sudo apt-get install -y unrtf",
                    "sudo apt-get install -y pandoc",
                ] + _pip_install_cmds([
                    "pymupdf",
                    "PyPDF2",
                    "python-docx",
                    "ebooklib",
                    "openpyxl",
                    "xlrd",
                    "docx2txt",
                    "textract",
                ]),
                "fedora": [
                    "sudo dnf install -y poppler-utils",
                    "sudo dnf install -y antiword",
                    "sudo dnf install -y catdoc",
                    "sudo dnf install -y unrtf",
                    "sudo dnf install -y pandoc",
                ] + _pip_install_cmds([
                    "pymupdf",
                    "PyPDF2",
                    "python-docx",
                    "ebooklib",
                    "openpyxl",
                    "xlrd",
                    "docx2txt",
                    "textract",
                ]),
                "arch": [
                    "sudo pacman -Syu --noconfirm poppler",
                    "sudo pacman -Syu --noconfirm antiword",
                    "sudo pacman -Syu --noconfirm catdoc",
                    "sudo pacman -Syu --noconfirm unrtf",
                    "sudo pacman -Syu --noconfirm pandoc",
                ] + _pip_install_cmds([
                    "pymupdf",
                    "PyPDF2",
                    "python-docx",
                    "ebooklib",
                    "openpyxl",
                    "xlrd",
                    "docx2txt",
                    "textract",
                ]),
                "alpine": [
                    "sudo apk update",
                    "sudo apk add poppler-utils",
                    "sudo apk add antiword",
                    "sudo apk add catdoc",
                    "sudo apk add unrtf",
                    "sudo apk add pandoc",
                ] + _pip_install_cmds([
                    "pymupdf",
                    "PyPDF2",
                    "python-docx",
                    "ebooklib",
                    "openpyxl",
                    "xlrd",
                    "docx2txt",
                    "textract",
                ]),
                "macos": [
                    "brew install poppler",
                    "brew install antiword",
                    "brew install catdoc",
                    "brew install unrtf",
                    "brew install pandoc",
                ] + _pip_install_cmds([
                    "pymupdf",
                    "PyPDF2",
                    "python-docx",
                    "ebooklib",
                    "openpyxl",
                    "xlrd",
                    "docx2txt",
                    "textract",
                ]),
                "windows": [
                    "py -m pip install --upgrade pymupdf",
                    "py -m pip install --upgrade PyPDF2",
                    "py -m pip install --upgrade python-docx",
                    "py -m pip install --upgrade ebooklib",
                    "py -m pip install --upgrade openpyxl",
                    "py -m pip install --upgrade xlrd",
                    "py -m pip install --upgrade docx2txt",
                    "py -m pip install --upgrade textract",
                    "# Optional: install pandoc from https://pandoc.org/installing.html",
                ],
                "android": [
                    "pkg update -y",
                ] + _pip_install_cmds([
                    "PyPDF2",
                    "python-docx",
                    "ebooklib",
                    "openpyxl",
                    "xlrd",
                    "docx2txt",
                ]),
                "ios": [
                    "# iOS does not support these tools natively.",
                    "# Use a remote Linux host or iSH (Alpine) where available."
                ],
                "esp32": [
                    "# Use a host computer for these tools."
                ],
                "generic": _pip_install_cmds([
                    "pymupdf",
                    "PyPDF2",
                    "python-docx",
                    "ebooklib",
                    "openpyxl",
                    "xlrd",
                    "docx2txt",
                    "textract",
                ]) + [
                    "# Optional: install poppler-utils / pandoc / antiword via your OS package manager",
                ]
            },
            "links": [
                "https://pypi.org/project/PyMuPDF/",
                "https://pypi.org/project/PyPDF2/",
                "https://pypi.org/project/python-docx/",
                "https://pypi.org/project/ebooklib/",
                "https://pypi.org/project/openpyxl/",
                "https://pypi.org/project/xlrd/",
                "https://pypi.org/project/textract/",
                "https://pandoc.org/"
            ]
        }
    }

def _download_center_print_commands(os_key, entry):
    commands = entry.get("commands", {})
    if os_key in commands:
        cmd_list = commands[os_key]
    else:
        cmd_list = commands.get("generic", [])
    if not cmd_list:
        print(f"{COLORS['4'][0]}No install commands available for this OS.{RESET}")
        return []
    print(f"\n{BOLD}Install Commands ({os_key}):{RESET}")
    for cmd in cmd_list:
        print(f"  {cmd}")
    links = entry.get("links", [])
    if links:
        print(f"\n{BOLD}Links:{RESET}")
        for link in links:
            print(f"  {link}")
    return cmd_list

def _download_center_run_commands(cmd_list):
    for cmd in cmd_list:
        if cmd.strip().startswith("#") or not cmd.strip():
            continue
        os.system(cmd)

def feature_download_center():
    """Download Center: OS-aware update/install scripts."""
    os_key = _detect_os_key()
    catalog = _download_center_catalog()

    def select_os(current_key):
        options = [
            "debian", "kali", "fedora", "arch", "alpine", "linux",
            "macos", "windows", "android", "ios", "esp32"
        ]
        print(f"\n{BOLD}Detected OS:{RESET} {current_key}")
        print("Select OS target:")
        for i, k in enumerate(options, 1):
            print(f"  [{i}] {k}")
        choice = input("\nSelect OS number (or Enter to keep): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        return current_key

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("Download Center")
        print(f"{BOLD}OS Target:{RESET} {os_key}")
        print(f"{BOLD}Select a package group:{RESET}")
        print(" [1] Pen Test Tools (Command Center 12)")
        print(" [2] Defence Tools (Command Center 13)")
        print(" [3] Network/WiFi/Bluetooth Tools (0/J/L)")
        print(" [4] Media Tools (I)")
        print(" [5] AI Center Tools (K)")
        print(" [6] Core PythonOS Libraries")
        print(" [7] General Purpose Python Libraries")
        print(" [8] Data Science / Analysis Stack")
        print(" [9] Web Development Stack")
        print(" [10] PWN Tools (P)")
        print(" [11] MapSCII (Satellite Tracker)")
        print(" [12] Text & Doc Tools (T)")
        print(" [S] Select OS Target")
        print(" [0] Return")

        choice = input("\nSelect option: ").strip().upper()
        if choice == '0':
            break
        if choice == 'S':
            os_key = select_os(os_key)
            continue

        mapping = {
            "1": "pentest",
            "2": "defence",
            "3": "network",
            "4": "media",
            "5": "ai",
            "6": "core_python",
            "7": "general_python",
            "8": "data_science",
            "9": "web_dev",
            "10": "pwn_tools",
            "11": "mapscii",
            "12": "text_doc"
        }
        key = mapping.get(choice)
        if not key:
            print(f"{COLORS['1'][0]}Invalid option{RESET}")
            time.sleep(1)
            continue

        entry = catalog.get(key, {})
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header(entry.get("title", "Download Center"))
        cmd_list = _download_center_print_commands(os_key, entry)
        if cmd_list:
            run = input("\nRun install commands now? (y/n): ").strip().lower()
            if run == 'y':
                _download_center_run_commands(cmd_list)
        input(f"\n{BOLD}[ Press Enter to return... ]{RESET}")

def feature_traffic_report():
    def _traffic_snapshot():
        data = get_weather_data() or {}
        try:
            geo = requests.get("http://ip-api.com/json/", timeout=3).json()
        except Exception:
            geo = {}

        city = geo.get("city", data.get("city", "Unknown"))
        lat = geo.get("lat")
        lon = geo.get("lon")

        icon = data.get("icon", "☁️")
        risk = _traffic_risk_from_weather(icon)
        lines = [
            "Traffic Report",
            f"Location: {city}",
            f"Weather: {icon}",
            f"Risk: {risk}",
        ]
        if data.get("temp"):
            lines.append(f"Temp: {data.get('temp')}")
        if data.get("feels"):
            lines.append(f"Feels: {data.get('feels')}")
        if data.get("wind"):
            lines.append(f"Wind: {data.get('wind')}")
        return city, lat, lon, icon, risk, lines

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🚦 Traffic Report")
        print(f" {BOLD}[1]{RESET} 🚦 Run Traffic Report")
        print(f" {BOLD}[2]{RESET} 🗺️ Open Traffic Links")
        print(f" {BOLD}[3]{RESET} 💾 Save Traffic Report")
        print(f" {BOLD}[0]{RESET} ↩️  Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return
        if choice == '1':
            print_header("🚦 Traffic Report")
            print("🔍 Using IP geolocation and weather to estimate traffic risk...")
            city, lat, lon, icon, risk, report_lines = _traffic_snapshot()
            print(f"\n {BOLD}📍 Location:{RESET} {city}")
            print(f" {BOLD}🌦️ Weather Impact:{RESET} {icon}  Traffic Risk: {risk}")

            print_header("🗺️ Live Traffic Links")
            print(" > https://www.bing.com/maps")
            print(" > https://www.google.com/maps")
            print(" > https://www.tomtom.com/traffic-index/")
            print(" > Microsoft.Maps.Traffic.TrafficManager(map)")

            if lat is not None and lon is not None:
                print_header("🗺️ ASCII Map Preview")
                map_url = (
                    "https://staticmap.openstreetmap.de/staticmap.php"
                    f"?center={lat},{lon}&zoom=12&size=600x400&maptype=mapnik"
                )
                ascii_map = convert_to_ascii(map_url, width=70)
                map_width = 72
                for i, line in enumerate(ascii_map):
                    right = report_lines[i] if i < len(report_lines) else ""
                    print(line.ljust(map_width) + right)
            else:
                print(f" {COLORS['4'][0]}[!] Map unavailable: location not found.{RESET}")

            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '2':
            print_header("🗺️ Live Traffic Links")
            links = {
                "1": "https://www.bing.com/maps",
                "2": "https://www.google.com/maps",
                "3": "https://www.tomtom.com/traffic-index/",
            }
            print("1) https://www.bing.com/maps")
            print("2) https://www.google.com/maps")
            print("3) https://www.tomtom.com/traffic-index/")
            sel = input("Open link (1-3, Enter to skip): ").strip()
            if sel in links:
                _open_url(links[sel])
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            _, _, _, _, _, report_lines = _traffic_snapshot()
            payload = "\n".join(report_lines)
            save_log_file("network", "Traffic_Report", payload, prompt_user=True)
            try:
                log_to_database("network", "Traffic_Report", payload, status="success")
            except Exception:
                pass
            input(f"\n{BOLD}[ ✅ Report Saved. Press Enter... ]{RESET}")

# --- AI & CALENDAR ADDITIONS ---

def feature_deep_probe_ai():
    def _ai_probe_snapshot():
        cpu_stress = psutil.cpu_percent(interval=0.5)
        mem = psutil.virtual_memory()
        mem_stress = mem.percent
        disk = psutil.disk_usage('/')
        net = psutil.net_io_counters()
        stress_score = (cpu_stress * 0.4) + (mem_stress * 0.4)

        verdict = "OPTIMAL"
        if stress_score > 80:
            verdict = "CRITICAL STRESS"
        elif stress_score > 50:
            verdict = "MODERATE LOAD"

        ai_readiness = max(0, 100 - int((mem_stress * 0.4) + (disk.percent * 0.3) + (cpu_stress * 0.3)))
        os_name = platform.system()
        arch = platform.machine()
        pyver = platform.python_version()

        ctx_switches = None
        zombie_count = None
        handles = None
        try:
            ctx_switches = psutil.cpu_stats().ctx_switches
            zombie_count = len([p for p in psutil.process_iter() if p.status() == psutil.STATUS_ZOMBIE])
            proc = psutil.Process()
            handles = proc.num_handles() if os.name == 'nt' else proc.num_fds()
        except Exception:
            pass

        lines = []
        lines.append("AI DEEP PROBE REPORT")
        lines.append("=" * 60)
        lines.append(f"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"OS: {os_name} {platform.release()} | Arch: {arch}")
        lines.append(f"Python: {pyver} | Node: {platform.node()}")
        lines.append("")
        lines.append("[AI HEALTH]")
        lines.append(f"CPU Load: {cpu_stress:.1f}%")
        lines.append(f"Memory Load: {mem_stress:.1f}%")
        lines.append(f"Disk Used: {disk.percent:.1f}%")
        lines.append(f"Stress Index: {stress_score:.1f}/100")
        lines.append(f"Health Verdict: {verdict}")
        lines.append(f"AI Readiness Score: {ai_readiness}/100")
        lines.append("")
        lines.append("[SYSTEM SIGNALS]")
        if ctx_switches is not None:
            lines.append(f"Context Switches: {ctx_switches:,}")
        if zombie_count is not None:
            lines.append(f"Zombie Count: {zombie_count}")
        if handles is not None:
            lines.append(f"Active OS Handles: {handles}")
        lines.append(f"Uptime: {str(datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())).split('.')[0]}")
        lines.append("")
        lines.append("[NETWORK]")
        lines.append(f"Data Sent: {net.bytes_sent / (1024**2):.2f} MB")
        lines.append(f"Data Received: {net.bytes_recv / (1024**2):.2f} MB")
        lines.append("=")
        return {
            "stress_score": stress_score,
            "verdict": verdict,
            "ai_readiness": ai_readiness,
            "lines": lines
        }

    def _export_report(lines, tag):
        content = "\n".join(lines)
        file_path = save_log_file("ai", f"AI_Probe_{tag}", content, prompt_user=False)
        try:
            log_to_database("ai", f"AI_Probe_{tag}", content, file_path=file_path, status="success")
        except Exception:
            pass
        return file_path

    def _ai_language_interpreter():
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🗣️ AI Language Interpreter")
        print("Select mode:")
        print(" [1] Friendly AI")
        print(" [2] Rogue AI (simulated)")
        mode = input("\nChoose mode: ").strip()
        rogue = mode == '2'
        print("\nType 'exit' to return.")
        while True:
            msg = input("\nYou> ").strip()
            if msg.lower() in ["exit", "quit", "q"]:
                break
            snapshot = _ai_probe_snapshot()
            if "status" in msg.lower() or "health" in msg.lower():
                print(f"AI> System health: {snapshot['verdict']} | Readiness {snapshot['ai_readiness']}/100")
                continue
            if "help" in msg.lower():
                print("AI> Try: status, report, analyze logs, readiness, summarize system")
                continue
            if "report" in msg.lower():
                file_path = _export_report(snapshot["lines"], "Interpreter")
                print(f"AI> Report generated: {file_path}")
                continue

            tone = "DIRECT" if rogue else "FRIENDLY"
            response = "Acknowledged."
            if "analyze" in msg.lower():
                response = "Analysis queued. Provide a target (file, folder, or log category)."
            elif "swap" in msg.lower():
                response = f"Swap cache is located at: {SWAP_CACHE_DIR}"
            elif "predict" in msg.lower():
                response = f"Forecast: readiness {snapshot['ai_readiness']}/100, keep CPU under 70% for best results."
            print(f"AI [{tone}]> {response}")

    def _advanced_ai_probe():
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🧠 Advanced AI Probing")
        snapshot = _ai_probe_snapshot()

        print(f"{BOLD}AI Readiness:{RESET} {snapshot['ai_readiness']}/100")
        print(f"{BOLD}Stress Index:{RESET} {snapshot['stress_score']:.1f}/100")

        print_header("📊 Process Intelligence")
        try:
            procs = []
            for p in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
                procs.append(p.info)
            procs.sort(key=lambda x: x.get('memory_percent') or 0, reverse=True)
            for p in procs[:8]:
                print(f" {p.get('pid'):>6} {p.get('name', 'N/A')[:18]:<18} MEM {p.get('memory_percent', 0):>5.1f}% CPU {p.get('cpu_percent', 0):>5.1f}%")
        except Exception:
            print(" Process scan unavailable.")

        print_header("🔍 Anomaly Heuristics")
        alerts = []
        if snapshot['stress_score'] > 80:
            alerts.append("High system stress detected")
        if psutil.virtual_memory().available / (1024**3) < 1:
            alerts.append("Low available RAM (<1GB)")
        if psutil.disk_usage('/').free / (1024**3) < 2:
            alerts.append("Low disk free space (<2GB)")
        if not alerts:
            alerts.append("No critical anomalies detected")
        for a in alerts:
            print(f" - {a}")

        file_path = _export_report(snapshot["lines"], "Advanced")
        print(f"\n{COLORS['2'][0]}✅ Advanced probe exported: {file_path}{RESET}")
        input(f"\n{BOLD}[ ✅ Probe Finished. Press Enter... ]{RESET}")

    def _ai_data_fusion():
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🧬 AI Data Fusion")
        print(f"Data Root: {DB_DIR}")
        print(f"Log Root:  {LOG_DIR}")
        print(f"Swap Cache: {SWAP_CACHE_DIR}")

        log_counts = {}
        newest = (None, 0)
        total_bytes = 0

        for root, _, files in os.walk(LOG_DIR):
            for name in files:
                path = os.path.join(root, name)
                try:
                    stat = os.stat(path)
                    total_bytes += stat.st_size
                    cat = os.path.basename(os.path.dirname(path))
                    log_counts[cat] = log_counts.get(cat, 0) + 1
                    if stat.st_mtime > newest[1]:
                        newest = (path, stat.st_mtime)
                except Exception:
                    pass

        print_header("📁 Log Intelligence")
        if log_counts:
            for cat, count in sorted(log_counts.items()):
                print(f" {cat:<16} {count} files")
            print(f" Total Log Size: {total_bytes / (1024**2):.2f} MB")
            if newest[0]:
                print(f" Newest Log: {newest[0]}")
        else:
            print(" No logs found.")

        print_header("🔄 Swap Cache")
        try:
            swap_files = [f for f in os.listdir(SWAP_CACHE_DIR) if os.path.isfile(os.path.join(SWAP_CACHE_DIR, f))]
            if swap_files:
                for f in swap_files[:10]:
                    print(f" {f}")
                if len(swap_files) > 10:
                    print(f" ... and {len(swap_files) - 10} more")
            else:
                print(" Swap cache is empty.")
        except Exception:
            print(" Swap cache not accessible.")

        stage = input("\nStage a file into swap cache? (y/n): ").strip().lower()
        if stage == 'y':
            src = input("Enter file path to stage: ").strip()
            if os.path.exists(src) and os.path.isfile(src):
                try:
                    dst = os.path.join(SWAP_CACHE_DIR, os.path.basename(src))
                    shutil.copy2(src, dst)
                    print(f"{COLORS['2'][0]}✅ Staged: {dst}{RESET}")
                except Exception as e:
                    print(f"{COLORS['1'][0]}❌ Stage failed: {e}{RESET}")
            else:
                print(f"{COLORS['1'][0]}❌ File not found{RESET}")

        input(f"\n{BOLD}[ ✅ Data Fusion Finished. Press Enter... ]{RESET}")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🤖 AI Probe Center")
        print(" [1] AI Report (screen + export)")
        print(" [2] AI Language Interpreter")
        print(" [3] Advanced AI Probing")
        print(" [4] AI Data Fusion (pythonOS_data)")
        print(" [0] Return")

        choice = input("\nSelect option: ").strip()
        if choice == '0':
            break
        elif choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print_header("🤖 AI Heuristics & Deep Probe")
            snapshot = _ai_probe_snapshot()
            for line in snapshot["lines"]:
                print(line)
            file_path = _export_report(snapshot["lines"], "Report")
            print(f"\n{COLORS['2'][0]}✅ Report exported: {file_path}{RESET}")
            input(f"\n{BOLD}[ ✅ Report Finished. Press Enter... ]{RESET}")
        elif choice == '2':
            _ai_language_interpreter()
        elif choice == '3':
            _advanced_ai_probe()
        elif choice == '4':
            _ai_data_fusion()
        else:
            print(f"{COLORS['1'][0]}Invalid option{RESET}")
            time.sleep(1)

def feature_simple_calendar():
    print_header("📅 System Calendar")
    now = datetime.datetime.now()
    # Display current month plus next two months side-by-side
    def _add_months(year, month, offset):
        total = (month - 1) + offset
        return year + (total // 12), (total % 12) + 1

    def _nth_weekday(year, month, weekday, n):
        # weekday: 0=Mon .. 6=Sun
        count = 0
        for day in range(1, 32):
            try:
                d = datetime.date(year, month, day)
            except ValueError:
                break
            if d.weekday() == weekday:
                count += 1
                if count == n:
                    return d
        return None

    def _last_weekday(year, month, weekday):
        last = None
        for day in range(1, 32):
            try:
                d = datetime.date(year, month, day)
            except ValueError:
                break
            if d.weekday() == weekday:
                last = d
        return last

    def _month_holidays(year, month):
        holidays = []
        # Fixed-date holidays
        fixed = {
            (1, 1): "New Year",
            (6, 19): "Juneteenth",
            (7, 4): "Independence Day",
            (11, 11): "Veterans Day",
            (12, 25): "Christmas",
        }
        for (m, d), name in fixed.items():
            if m == month:
                holidays.append((datetime.date(year, m, d), name))

        # Observed weekday rules
        if month == 1:
            d = _nth_weekday(year, 1, 0, 3)
            if d: holidays.append((d, "MLK Day"))
        if month == 2:
            d = _nth_weekday(year, 2, 0, 3)
            if d: holidays.append((d, "Presidents Day"))
        if month == 5:
            d = _last_weekday(year, 5, 0)
            if d: holidays.append((d, "Memorial Day"))
        if month == 9:
            d = _nth_weekday(year, 9, 0, 1)
            if d: holidays.append((d, "Labor Day"))
        if month == 10:
            d = _nth_weekday(year, 10, 0, 2)
            if d: holidays.append((d, "Columbus Day"))
        if month == 11:
            d = _nth_weekday(year, 11, 3, 4)
            if d: holidays.append((d, "Thanksgiving"))

        holidays.sort(key=lambda x: x[0])
        return holidays

    months = []
    for i in range(3):
        y, m = _add_months(now.year, now.month, i)
        months.append(calendar.month(y, m).splitlines())

    max_lines = max(len(m) for m in months)
    for m in months:
        while len(m) < max_lines:
            m.append("")

    col_width = max(max(len(line) for line in m) for m in months)
    lines = []
    for i in range(max_lines):
        line = "  ".join(m[i].ljust(col_width) for m in months)
        lines.append(line.rstrip())

    # Build holiday side panel for the three displayed months
    holiday_colors = [COLORS["2"][0], COLORS["4"][0], COLORS["6"][0]]
    holiday_lines = ["Upcoming Holidays"]
    for i in range(3):
        y, m = _add_months(now.year, now.month, i)
        month_name = datetime.date(y, m, 1).strftime("%B")
        holiday_lines.append(f"{holiday_colors[i]}{month_name}:{RESET}")
        for d, name in _month_holidays(y, m):
            holiday_lines.append(f"{holiday_colors[i]}{d.strftime('%b %d')}: {name}{RESET}")

    panel_width = max(20, max(len(line) for line in holiday_lines))
    full_lines = []
    for i in range(max(len(lines), len(holiday_lines))):
        left = lines[i] if i < len(lines) else ""
        right = holiday_lines[i] if i < len(holiday_lines) else ""
        full_lines.append(left.ljust(col_width * 3 + 4) + right.ljust(panel_width))

    print(f"{get_current_color()}" + "\n".join(full_lines) + f"{RESET}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

# --- NEW FEATURE: FONT & SIZE TESTER & FX MENU ---
def feature_test_font_size():
    print_header("✨ Experimental Display & Font")
    print(f"{COLORS['3'][0]}Select a display transformation style (Applies Globaly):{RESET}\n")

    print(f" {BOLD}[1] 🔠 Same-Letter Mode{RESET} (Fullwidth/Banner Style)")
    print(f" {BOLD}[2] 🧱 AI Density Mode{RESET}  (Heuristic Density Blocks)")
    print(f" {BOLD}[3] 🔮 Dot Version{RESET}     (Organic Pointillism)")
    print(f" {BOLD}[4] ↩️ Return to Normal{RESET} (Standard Text)")
    print("-" * 40)
    print(f" {BOLD}[5] 📏 Run Original Font Size Tester{RESET}")

    choice = input("\n🎯 Select Option: ").strip()

    if choice == '1':
        sys.stdout.mode = 1
        print("\n✅ Same-Letter Mode Activated.")
    elif choice == '2':
        sys.stdout.mode = 2
        print("\n✅ AI Density Mode Activated.")
    elif choice == '3':
        sys.stdout.mode = 3
        print("\n✅ Dot Mode Activated.")
    elif choice == '4':
        sys.stdout.mode = 0
        print("\n✅ Display Normal.")
    elif choice == '5':
        # Original Font Test Logic
        print_header("🔡 Font & Terminal Size Tester")
        print("📏 Scale Ruler (Test character width):")
        print("00000000011111111112222222222333333333344444444445555555555666666666677777777778")
        print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
        print("-" * 80)

        print(f"\n🌈 {BOLD}ANSI Color & Style Support:{RESET}")
        for k in sorted(COLORS.keys(), key=int):
            print(f"{COLORS[k][0]}■ {COLORS[k][2]} Text{RESET}", end="  ")
            if int(k) % 5 == 0: print()

        print(f"\n\n🔠 {BOLD}Font Clarity Test (Large Blocks):{RESET}")
        # Universal block characters for sizing
        blocks = [
            "████╗ ████╗ ███╗",
            "██╔═╝ ██╔═╝ ██║",
            "████╗ ████╗ ██║",
            "╚═██║ ╚═██║ ██║",
            "████║ ████║ ███╗",
            "╚═══╝ ╚═══╝ ╚══╝"
        ]
        for line in blocks:
            print(f"  {get_current_color()}{line}{RESET}")

        print(f"\n📱 {BOLD}Platform Compatibility:{RESET}")
        print(f" > Arch: {platform.machine()} | OS: {platform.system()} | Python: {platform.python_version()}")

        # Check for Emoji support
        print(f" > Emoji Check: ✅ 🚀 🔥 💎 🤖")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

# --- NEW: MEDIA SCANNER FEATURE (ADDED) ---
def feature_media_scanner():
    print_header("🎞️ Interstellar Media Scanner")
    target_dir = input("📂 Enter the folder path to scan for media: ").strip()

    if not os.path.isdir(target_dir):
        print(f" {COLORS['1'][0]}[!] Error: Invalid directory path.{RESET}")
        time.sleep(2)
        return

    # Extension definitions for the future solar system usage
    media_exts = {
        "Audio": [".mp3", ".wav", ".flac", ".ogg", ".m4a"],
        "Video": [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv"],
        "Images": [".jpeg", ".jpg", ".png", ".bmp", ".tiff", ".webp"],
        "GIFs": [".gif"]
    }

    results = []
    print(f"🔍 Deep scanning: {target_dir}...")

    # Walking through the file system tree
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            for category, extensions in media_exts.items():
                if ext in extensions:
                    file_path = os.path.join(root, file)
                    results.append({"name": file, "path": file_path, "type": category})
                    # Track file in database
                    track_file(file_path, file_type=category, metadata={"extension": ext})

    if not results:
        print(f" {COLORS['4'][0]}[!] No media files found in this sector.{RESET}")
    else:
        # Paged display logic
        page_limit = 15
        for start in range(0, len(results), page_limit):
            os.system('cls' if os.name == 'nt' else 'clear')
            print_header("📁 Media Assets Found", extra_info=f"Page {int(start/page_limit)+1}")

            chunk = results[start:start+page_limit]
            for i, item in enumerate(chunk):
                # Color coding by type
                c = COLORS["6"][0] # Default Cyan
                if item["type"] == "Video": c = COLORS["3"][0] # Blue
                elif item["type"] == "Audio": c = COLORS["5"][0] # Magenta
                elif item["type"] == "GIFs": c = COLORS["10"][0] # Neon Green

                print(f"{BOLD}[{i + 1}]{RESET} {c}[{item['type']}] {RESET}{item['name']}")

            print("\n" + "-"*60)
            cmd = input(f"🎯 Select [Number] for Path, [N]ext Page, or [Enter] to exit: ").strip().upper()

            if cmd.isdigit():
                idx = int(cmd) - 1
                if 0 <= idx < len(chunk):
                    print(f"\n{BOLD}📍 Full Galactic Path:{RESET}")
                    print(f" {chunk[idx]['path']}")
                    input(f"\n{BOLD}[ Press Enter to resume... ]{RESET}")
            elif cmd == 'N':
                continue
            else:
                break

        # Generate log of all found media
        media_log = f"Media Scan Report\\nDirectory: {target_dir}\\nTotal Files Found: {len(results)}\\n\\n"
        for category in ["Audio", "Video", "Images", "GIFs"]:
            category_files = [r for r in results if r["type"] == category]
            if category_files:
                media_log += f"\\n{category} ({len(category_files)} files):\\n"
                for item in category_files:
                    media_log += f"  - {item['name']}\\n    Path: {item['path']}\\n"

        save_log_file("media", "Media_Scan", media_log, prompt_user=True)

    input(f"\\n{BOLD}[ ✅ Sector Scan Complete. Press Enter... ]{RESET}")

# --- RESUME SACRED CORE FUNCTIONS ---

def get_advanced_hardware_stats():
    gpu_data = "N/A"
    fan_data = "N/A"
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            g = gpus[0]
            t = g.temperature
            if temp_unit == "F":
                t = (t * 9/5) + 32
            gpu_data = f"{g.load*100:.0f}%|{t:.0f}\u00b0{temp_unit}"
    except: pass
    try:
        fans = psutil.sensors_fans()
        if fans:
            for name, entries in fans.items():
                if entries:
                    fan_data = f"{entries[0].current}RPM"
                    break
    except: pass
    return gpu_data, fan_data

def live_system_identity_clock():
    last_net = psutil.net_io_counters()
    last_recv = _safe_float(getattr(last_net, "bytes_recv", None), 0.0)
    last_sent = _safe_float(getattr(last_net, "bytes_sent", None), 0.0)
    ticker_count = 0
    while not stop_clock:
        # Update weather cache every 300 seconds (5 mins)
        if ticker_count % 300 == 0:
            threading.Thread(target=get_weather_data, daemon=True).start()

        current_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cpu_live = psutil.cpu_percent()
        ram_live = psutil.virtual_memory().percent
        disk_live = psutil.disk_usage('/').percent
        gpu_live, fan_live = get_advanced_hardware_stats()

        time.sleep(1)
        ticker_count += 1
        now_net = psutil.net_io_counters()
        now_recv = _safe_float(getattr(now_net, "bytes_recv", None))
        now_sent = _safe_float(getattr(now_net, "bytes_sent", None))
        if now_recv is None or now_sent is None:
            down_speed = 0
            up_speed = 0
        else:
            down_speed = (now_recv - last_recv) / 1024
            up_speed = (now_sent - last_sent) / 1024
            last_recv = now_recv
            last_sent = now_sent

        avg_temp_display = "N/A"
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                core_vals = []
                for name, entries in temps.items():
                    for entry in entries:
                        label = (entry.label or name).lower()
                        if "core" in label or "thermal" in label or "soc" in label:
                            val = entry.current
                            if temp_unit == "F":
                                val = (val * 9/5) + 32
                            core_vals.append(val)
                if core_vals:
                    avg_temp_display = f"{sum(core_vals) / len(core_vals):.1f}\u00b0{temp_unit}"
        except: pass

        sys.stdout.write("\033[s")
        sys.stdout.write("\033[2;15H")
        current_color = get_current_color()

        status_line = (f"{current_color}| 🕒 {current_dt} | {weather_cache['icon']} {weather_cache['temp']} | ⚙️ CPU: {cpu_live}% | 🌡️ Temp: {avg_temp_display} | "
                       f"🎮 GPU: {gpu_live} | 🌀 Fan: {fan_live} | 🧠 RAM: {ram_live}% | 💽 Disk: {disk_live}% | "
                       f"⬇️ DN: {down_speed:.1f}KB/s | ⬆️ UP: {up_speed:.1f}KB/s{RESET}    ")

        sys.stdout.write(status_line)
        sys.stdout.write("\033[u")
        sys.stdout.flush()

def convert_to_ascii(url, width=50):
    try:
        res = requests.get(url, timeout=5)
        img = Image.open(BytesIO(res.content))
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGBA")
            background = Image.new("RGBA", img.size, (255, 255, 255))
            img = Image.alpha_composite(background, img).convert("RGB")
        else:
            img = img.convert("RGB")
        aspect_ratio = img.height / img.width
        new_height = int(aspect_ratio * width * 0.5)
        img = img.resize((width, new_height))
        pixels = img.getdata()
        chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        ascii_lines = []
        for y in range(new_height):
            line = ""
            for x in range(width):
                r, g, b = pixels[y * width + x]
                color_code = 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)
                brightness = int(0.2126*r + 0.7152*g + 0.0722*b)
                char = chars[min(len(chars)-1, brightness // 25)]
                line += f"\033[38;5;{color_code}m{char}"
            ascii_lines.append(line + RESET)
        return ascii_lines
    except:
        return [f"{COLORS['1'][0]}[ ❌ Image Load Failed ]{RESET}"]

def _open_url(url):
    if not url:
        return
    if os.name == 'nt':
        os.system(f"start {url}")
    else:
        os.system(f"$BROWSER '{url}' 2>/dev/null &")

def launch_bpytop_monitor():
    """Launch bpytop system monitor inline - displays in terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if bpytop is installed
    bpytop_cmd = shutil.which('bpytop')

    if bpytop_cmd:
        print(f"{COLORS['2'][0]}✅ Launching Bpytop System Monitor...{RESET}")
        print(f"{COLORS['6'][0]}📊 Real-time CPU, Memory, Disk, Network, and Process Monitor{RESET}")
        print(f"{COLORS['6'][0]}Press 'q' to quit and return to Command Center{RESET}\n")
        time.sleep(1)
        try:
            # Launch bpytop - it takes over the entire terminal
            subprocess.call(['bpytop'])
        except KeyboardInterrupt:
            print(f"\n{COLORS['4'][0]}🛑 Bpytop interrupted{RESET}")
        except Exception as e:
            print(f"{COLORS['1'][0]}❌ Error launching bpytop: {e}{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")
    else:
        # Bpytop not installed - provide installation instructions
        print(f"{COLORS['1'][0]}❌ Bpytop is not installed{RESET}\n")
        print(f"{BOLD}📦 Install Bpytop:{RESET}\n")
        print(f"  {COLORS['6'][0]}Method 1 (pip - Recommended):{RESET}")
        print(f"    pip3 install bpytop --upgrade\n")
        print(f"  {COLORS['6'][0]}Method 2 (system package):{RESET}")
        print(f"    Ubuntu/Debian: sudo apt install bpytop")
        print(f"    Fedora: sudo dnf install bpytop")
        print(f"    Arch: sudo pacman -S bpytop")
        print(f"    macOS: brew install bpytop\n")
        print(f"  {COLORS['6'][0]}Method 3 (snap):{RESET}")
        print(f"    sudo snap install bpytop\n")

        install = input(f"{BOLD}Install bpytop now with pip? (y/n): {RESET}").strip().lower()
        if install == 'y':
            print(f"\n{COLORS['6'][0]}📥 Installing bpytop...{RESET}\n")
            try:
                subprocess.call([sys.executable, "-m", "pip", "install", "bpytop", "--upgrade"])
                print(f"\n{COLORS['2'][0]}✅ Bpytop installed successfully!{RESET}")
                print(f"{COLORS['2'][0]}Launch it again from Enhanced Display Mode (Option U > Option 1){RESET}")
            except Exception as e:
                print(f"{COLORS['1'][0]}❌ Installation failed: {e}{RESET}")

        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def launch_htop_monitor():
    """Launch htop system monitor."""
    os.system('cls' if os.name == 'nt' else 'clear')
    htop_cmd = shutil.which('htop')
    if htop_cmd:
        print(f"{COLORS['2'][0]}✅ Launching Htop...{RESET}\n")
        time.sleep(0.5)
        try:
            subprocess.call(['htop'])
        except:
            pass
    else:
        print(f"{COLORS['1'][0]}❌ Htop not installed{RESET}")
        print(f"Install: sudo apt install htop")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def launch_gtop_monitor():
    """Launch gtop system monitor (Node.js based)."""
    os.system('cls' if os.name == 'nt' else 'clear')
    gtop_cmd = shutil.which('gtop')
    if gtop_cmd:
        print(f"{COLORS['2'][0]}✅ Launching Gtop...{RESET}\n")
        time.sleep(0.5)
        try:
            subprocess.call(['gtop'])
        except:
            pass
    else:
        print(f"{COLORS['1'][0]}❌ Gtop not installed{RESET}")
        print(f"Install: npm install -g gtop")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def launch_btop_monitor():
    """Launch btop++ system monitor."""
    os.system('cls' if os.name == 'nt' else 'clear')
    btop_cmd = shutil.which('btop')
    if btop_cmd:
        print(f"{COLORS['2'][0]}✅ Launching Btop++...{RESET}\n")
        time.sleep(0.5)
        try:
            subprocess.call(['btop'])
        except:
            pass
    else:
        print(f"{COLORS['1'][0]}❌ Btop++ not installed{RESET}")
        print(f"Install: sudo apt install btop")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_web_browser_center():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🌐 Web Browser Center")
        print(" [1] Render Page Text/Images")
        print(" [2] Fetch Page Headers")
        print(" [3] Save Page to Log")
        print(" [4] Open in System Browser")
        print(" [0] Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return

        url = input("🌐 Enter URL [https://www.google.com]: ").strip() or "https://www.google.com"
        if not url.startswith('http'):
            url = 'https://' + url

        if choice == '1':
            show_img = input("🖼️ Load images as Color ASCII? (y/n): ").strip().lower() == 'y'
            try:
                res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
                soup = BeautifulSoup(res.text, 'html.parser')
                for s in soup(["script", "style"]):
                    s.extract()
                elements = soup.find_all(True)
                content_list = []
                seen_text = set()
                for el in elements:
                    if el.name == 'img' and show_img:
                        src = el.get('src')
                        if src:
                            from urllib.parse import urljoin
                            src = urljoin(url, src)
                            content_list.append(("IMG", convert_to_ascii(src)))
                    elif el.string and el.string.strip():
                        txt = el.string.strip()
                        if txt not in seen_text:
                            content_list.append(("TXT", txt))
                            seen_text.add(txt)
                if not content_list:
                    lines = [line.strip() for line in soup.get_text().splitlines() if line.strip()]
                    for l in lines:
                        content_list.append(("TXT", l))
                for i in range(0, len(content_list), 15):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_header("🌐 Browser", extra_info=url)
                    for typ, val in content_list[i:i+15]:
                        if typ == "TXT":
                            print(val)
                        else:
                            for line in val:
                                print(line)
                    input("\n[ 📑 Next Page... ]")
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(2)
        elif choice == '2':
            try:
                res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
                print_header("📄 Headers")
                print(f"Status: {res.status_code}")
                for k, v in res.headers.items():
                    print(f"{k}: {v}")
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            try:
                res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
                payload = f"URL: {url}\nStatus: {res.status_code}\n\n{res.text[:5000]}"
                save_log_file("general", "Web_Page_Snapshot", payload, prompt_user=True)
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '4':
            _open_url(url)
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_process_search():
    sort_by = 'memory_percent'
    target = ""

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📑 Process Manager Sub-Menu")
        print(f"📊 Sorting by: {BOLD}{sort_by.replace('_', ' ').upper()}{RESET}")
        print(f"[1] 🔍 Search/List Once | [2] ⏱️ Live Monitor (2s Refresh) | [3] 🧠 Sort by Memory | [4] ⚙️ Sort by CPU | [5] ↩️ Return")
        print(f"[6] 🧾 Process Details by PID | [7] 🛑 Terminate Process by PID")

        proc_choice = input("\n🎯 Select: ").strip()

        if proc_choice == '5':
            break
        elif proc_choice == '6':
            pid_str = input("Enter PID: ").strip()
            if pid_str.isdigit():
                try:
                    p = psutil.Process(int(pid_str))
                    print_header("🧾 Process Details")
                    print(f"PID: {p.pid}")
                    print(f"Name: {p.name()}")
                    print(f"Status: {p.status()}")
                    print(f"CPU%: {p.cpu_percent(interval=0.1)}")
                    print(f"MEM%: {p.memory_percent():.2f}")
                    print(f"User: {p.username()}")
                    print(f"CWD: {p.cwd()}")
                    try:
                        print("Cmdline:", " ".join(p.cmdline()))
                    except Exception:
                        pass
                    try:
                        files = p.open_files()[:10]
                        if files:
                            print("Open Files:")
                            for f in files:
                                print(f"  {f.path}")
                    except Exception:
                        pass
                except Exception as e:
                    print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
            continue
        elif proc_choice == '7':
            pid_str = input("Enter PID to terminate: ").strip()
            if pid_str.isdigit():
                try:
                    p = psutil.Process(int(pid_str))
                    confirm = input(f"Terminate {p.name()} (PID {p.pid})? (y/n): ").strip().lower()
                    if confirm == 'y':
                        p.terminate()
                        print("✅ Termination signal sent.")
                except Exception as e:
                    print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
            continue
        elif proc_choice == '3':
            sort_by = 'memory_percent'
            proc_choice = '1'
        elif proc_choice == '4':
            sort_by = 'cpu_percent'
            proc_choice = '1'

        if proc_choice in ['1', '2']:
            if not target or proc_choice == '1':
                target = input("⌨️ Enter process name to filter (leave blank for all): ").lower()
            try:
                if proc_choice == '2':
                    # Live Monitor Mode
                    import sys as _sys
                    import select as _select
                    monitor_running = True
                    refresh_count = 0

                    while monitor_running:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_header("🔭 Process Explorer (LIVE)", extra_info=f"| 🔎 Filter: '{target}' | ↕️ Sort: {sort_by}")
                        print(f"{'PID':<7} | {'Name':<20} | {'MEM %':<7} | {'CPU %':<7} | {'Status':<10} | {'User'}")
                        print("-" * 85)
                        procs = []
                        for p in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent', 'status', 'username']):
                            try:
                                if not target or target in p.info['name'].lower():
                                    procs.append(p.info)
                            except: continue

                        procs.sort(key=lambda x: x[sort_by] or 0, reverse=True)

                        for p in procs[:20]:
                            mem_val = p['memory_percent'] or 0
                            cpu_val = p['cpu_percent'] or 0
                            print(f"{p['pid']:<7} | {p['name'][:20]:<20} | {mem_val:>6.2f}% | {cpu_val:>6.1f}% | {p['status']:<10} | {p['username']}")

                        refresh_count += 1
                        print(f"\n{get_current_color()}📡 Monitoring Live... (Refresh #{refresh_count}) Press Enter to stop.{RESET}")

                        # Wait for input with timeout (non-blocking)
                        if os.name == 'nt':
                            # Windows: use timeout approach
                            import msvcrt
                            import time as _time
                            for _ in range(20):  # 2 seconds total (20 * 0.1s)
                                if msvcrt.kbhit():
                                    _sys.stdin.read(1)
                                    monitor_running = False
                                    break
                                _time.sleep(0.1)
                        else:
                            # Unix/Linux: use select for non-blocking input
                            ready = _select.select([_sys.stdin], [], [], 2.0)
                            if ready[0]:
                                _sys.stdin.read(1)
                                monitor_running = False
                else:
                    # Single List Mode (proc_choice == '1')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_header("🔭 Process Explorer", extra_info=f"| 🔎 Filter: '{target}' | ↕️ Sort: {sort_by}")
                    print(f"{'PID':<7} | {'Name':<20} | {'MEM %':<7} | {'CPU %':<7} | {'Status':<10} | {'User'}")
                    print("-" * 85)
                    procs = []
                    for p in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent', 'status', 'username']):
                        try:
                            if not target or target in p.info['name'].lower():
                                procs.append(p.info)
                        except: continue

                    procs.sort(key=lambda x: x[sort_by] or 0, reverse=True)

                    for p in procs[:20]:
                        mem_val = p['memory_percent'] or 0
                        cpu_val = p['cpu_percent'] or 0
                        print(f"{p['pid']:<7} | {p['name'][:20]:<20} | {mem_val:>6.2f}% | {cpu_val:>6.1f}% | {p['status']:<10} | {p['username']}")

                    # Logging capability
                    process_log = f"Filter: {target}\\nSort By: {sort_by}\\nTotal Processes Found: {len(procs)}\\n\\n"
                    process_log += f"{'PID':<7} | {'Name':<20} | {'MEM %':<7} | {'CPU %':<7} | {'Status':<10} | {'User'}\\n"
                    process_log += "-" * 85 + "\\n"
                    for p in procs[:20]:
                        mem_val = p['memory_percent'] or 0
                        cpu_val = p['cpu_percent'] or 0
                        process_log += f"{p['pid']:<7} | {p['name'][:20]:<20} | {mem_val:>6.2f}% | {cpu_val:>6.1f}% | {p['status']:<10} | {p['username']}\\n"

                    save_log_file("process", "Process_Search", process_log, prompt_user=True)
                    input(f"\\n{BOLD}[ ⌨️ Press Enter to return to Process Menu... ]{RESET}")
            except Exception as e:
                print(f"❌ Error: {e}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_disk_io_report():
    def _disk_io_snapshot():
        last_io = psutil.disk_io_counters()
        time.sleep(1)
        now_io = psutil.disk_io_counters()
        read_speed = (now_io.read_bytes - last_io.read_bytes) / (1024 * 1024)
        write_speed = (now_io.write_bytes - last_io.write_bytes) / (1024 * 1024)
        lines = [
            "Disk I/O Snapshot",
            f"Read Speed:  {read_speed:.2f} MB/s",
            f"Write Speed: {write_speed:.2f} MB/s",
            f"Total Read:  {now_io.read_bytes / (1024**3):.2f} GB",
            f"Total Write: {now_io.write_bytes / (1024**3):.2f} GB",
        ]
        return lines

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("💽 Disk I/O Center")
        print(f" {BOLD}[1]{RESET} ⚡ Quick I/O Snapshot")
        print(f" {BOLD}[2]{RESET} 📊 Per-Disk Counters")
        print(f" {BOLD}[3]{RESET} ⏱️  Live Monitor (10s)")
        print(f" {BOLD}[4]{RESET} 💾 Save Snapshot to Logs")
        print(f" {BOLD}[0]{RESET} ↩️  Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return
        if choice == '1':
            print_header("💽 Disk I/O Snapshot")
            for line in _disk_io_snapshot():
                print(line)
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '2':
            print_header("📊 Per-Disk Counters")
            try:
                per_disk = psutil.disk_io_counters(perdisk=True)
                for disk, stats in per_disk.items():
                    print(f"{disk}: R {stats.read_bytes / (1024**3):.2f} GB | W {stats.write_bytes / (1024**3):.2f} GB")
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            print_header("⏱️ Live Disk I/O (10s)")
            try:
                last_io = psutil.disk_io_counters()
                for i in range(10):
                    time.sleep(1)
                    now_io = psutil.disk_io_counters()
                    read_speed = (now_io.read_bytes - last_io.read_bytes) / (1024 * 1024)
                    write_speed = (now_io.write_bytes - last_io.write_bytes) / (1024 * 1024)
                    print(f"{i+1:02d}s  R {read_speed:.2f} MB/s | W {write_speed:.2f} MB/s")
                    last_io = now_io
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '4':
            lines = _disk_io_snapshot()
            file_path = save_log_file("hardware", "Disk_IO_Snapshot", "\n".join(lines), prompt_user=True)
            if file_path:
                log_to_database("hardware", "Disk_IO_Snapshot", "\n".join(lines), file_path=file_path, status="success")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_network_sparkline():
    print_header("📈 Live Network Pulse (60s)")
    history = []
    last_net = psutil.net_io_counters().bytes_recv
    try:
        for _ in range(30):
            time.sleep(1)
            curr_net = psutil.net_io_counters().bytes_recv
            diff = (curr_net - last_net) / 1024
            history.append(diff)
            last_net = curr_net
            chars = " ▂▃▄▅▆▇█"
            max_val = max(history) if max(history) > 0 else 1
            line = "".join([chars[min(7, int(v / max_val * 7))] for v in history])
            sys.stdout.write(f"\r{get_current_color()}💓 Pulse: {line} {diff:.1f} KB/s{RESET}")
            sys.stdout.flush()
    except KeyboardInterrupt:
        pass
    input(f"\n\n{BOLD}[ 🏁 Tracking Finished. Press Enter... ]{RESET}")

def feature_network_toolkit():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🌐 Network Toolkit Sub-Menu")
        print(f"[1] 💓 Original Network Pulse (Sparkline)")
        print(f"[2] 🔑 SSH into Remote IP")
        print(f"[3] 📡 Local Network Scanner (Quick)")
        print(f"[4] 🔝 Top 10 Network-Using Processes")
        print(f"[5] 🧩 Network Interface Summary")
        print(f"[6] 📦 Open Download Center (Network Tools)")
        print(f"[7] ↩️ Return to Main Menu")
        net_choice = input("\n🎯 Select a tool (1-7): ").strip()
        if net_choice == '1': feature_network_sparkline()
        elif net_choice == '2':
            ip = input("🖥️ Enter remote IP: ").strip()
            user = input("👤 Enter username (default root): ").strip() or "root"
            if ip:
                print(f"🔗 Attempting SSH connection to {user}@{ip}...")
                os.system(f"ssh {user}@{ip}")
            input(f"\n{BOLD}[ 🚪 SSH Session Ended. Press Enter... ]{RESET}")
        elif net_choice == '3':
            print_header("🔎 Network Scan")
            print("📡 Scanning local subnet (this may take a moment)...")
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            ip_prefix = ".".join(local_ip.split('.')[:-1]) + "."
            for i in range(1, 15):
                target = ip_prefix + str(i)
                param = '-n' if os.name == 'nt' else '-c'
                command = ['ping', param, '1', '-w', '500', target]
                if subprocess.call(command, stdout=subprocess.DEVNULL) == 0:
                    print(f"🟢 Found: {target} (Active)")
            input(f"\n{BOLD}[ ✅ Scan Complete. Press Enter... ]{RESET}")
        elif net_choice == '4':
            print_header("🔝 Top 10 Network Consumers")
            try:
                conns = psutil.net_connections(kind='inet')
                pid_counts = {}
                for c in conns:
                    if c.pid:
                        pid_counts[c.pid] = pid_counts.get(c.pid, 0) + 1
                sorted_pids = sorted(pid_counts.items(), key=lambda x: x[1], reverse=True)[:10]
                print(f"{'PID':<10} | {'Connections':<12} | {'Process Name'}")
                print("-" * 50)
                for pid, count in sorted_pids:
                    try:
                        p = psutil.Process(pid)
                        print(f"{pid:<10} | {count:<12} | {p.name()}")
                    except: pass
            except:
                print("🚫 Permission Denied: Run as admin/sudo to view process connections.")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif net_choice == '5':
            print_header("🧩 Network Interface Summary")
            try:
                for iface, addrs in psutil.net_if_addrs().items():
                    print(f"\n{iface}:")
                    for addr in addrs:
                        if hasattr(addr, "address"):
                            print(f"  {addr.address}")
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif net_choice == '6':
            feature_download_center()
        elif net_choice == '7': break

def feature_wifi_toolkit():
    """WiFi Card Detection, Scanning, and Testing (Kali-style)"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📡 WiFi Toolkit (Advanced)")
        print(f" {BOLD}[1]{RESET} 🔍 Detect WiFi Interfaces")
        print(f" {BOLD}[2]{RESET} 📊 Scan Available Networks")
        print(f" {BOLD}[3]{RESET} 🔗 Show Connected Network")
        print(f" {BOLD}[4]{RESET} 🌐 Test Network Connectivity")
        print(f" {BOLD}[5]{RESET} 🔑 Display WiFi MAC Address")
        print(f" {BOLD}[6]{RESET} 📡 Signal Strength Monitor")
        print(f" {BOLD}[7]{RESET} 📦 Open Download Center (Network Tools)")
        print(f" {BOLD}[8]{RESET} ↩️ Return to Main Menu")
        wifi_choice = input(f"\n{BOLD}🎯 Select WiFi Tool (1-8): {RESET}").strip()

        if wifi_choice == '1':
            print_header("🔍 WiFi Interface Detection")
            try:
                interfaces = []
                if os.name != 'nt':
                    try:
                        result = subprocess.check_output(['ip', 'link', 'show'], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
                        for line in result.split('\n'):
                            if any(x in line for x in ['wlan', 'wl', 'wwan']):
                                match = re.match(r'^\d+:\s([\w]+)', line)
                                if match:
                                    interfaces.append(match.group(1))
                    except:
                        pass
                else:
                    try:
                        result = subprocess.check_output(['ipconfig', '/all'], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
                        for line in result.split('\n'):
                            if 'Wireless' in line or 'WiFi' in line:
                                interfaces.append(line.strip())
                    except:
                        pass

                if interfaces:
                    print(f"\n{COLORS['2'][0]}✅ Found {len(interfaces)} WiFi Interface(s):{RESET}")
                    for idx, iface in enumerate(interfaces, 1):
                        print(f"   [{idx}] {iface}")
                else:
                    print(f"{COLORS['1'][0]}[!] No WiFi interfaces detected.{RESET}")
            except Exception as e:
                print(f"{COLORS['1'][0]}[!] Error detecting interfaces: {e}{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif wifi_choice == '2':
            print_header("📊 WiFi Network Scan")
            print("🔍 Scanning for available networks (this may require sudo)...")
            try:
                networks = []
                if os.name != 'nt':
                    try:
                        result = subprocess.check_output(['sudo', 'iwlist', 'wlan0', 'scan'], stderr=subprocess.DEVNULL, timeout=10).decode('utf-8', errors='ignore')
                        cell_pattern = r'ESSID:"([^"]*)'
                        for match in re.finditer(cell_pattern, result):
                            networks.append(match.group(1) or '[Hidden Network]')
                    except:
                        try:
                            result = subprocess.check_output(['nmcli', 'dev', 'wifi', 'list'], stderr=subprocess.DEVNULL, timeout=10).decode('utf-8', errors='ignore')
                            for line in result.split('\n')[1:]:
                                if line.strip():
                                    parts = line.split()
                                    if len(parts) > 1:
                                        networks.append(f"{parts[1]} (Signal: {parts[6] if len(parts) > 6 else 'N/A'})")
                        except:
                            pass
                else:
                    try:
                        result = subprocess.check_output(['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
                        for line in result.split('\n'):
                            if 'SSID' in line and ':' in line:
                                networks.append(line.split(':')[1].strip())
                    except:
                        pass

                if networks:
                    print(f"\n{COLORS['2'][0]}✅ Found {len(networks)} Network(s):{RESET}")
                    for idx, net in enumerate(networks[:20], 1):
                        print(f"   [{idx}] {net}")
                else:
                    print(f"{COLORS['4'][0]}[*] No networks found (may need elevated privileges).{RESET}")
            except Exception as e:
                print(f"{COLORS['1'][0]}[!] Scan error: {e}{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif wifi_choice == '3':
            print_header("🔗 Connected Network Info")
            try:
                if os.name != 'nt':
                    result = subprocess.check_output(['iwconfig', 'wlan0'], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
                    ssid_match = re.search(r'ESSID:"([^"]*)"', result)
                    signal_match = re.search(r'Signal level[=:]([^\n]+)', result)
                    if ssid_match:
                        print(f"\n📡 SSID: {BOLD}{ssid_match.group(1)}{RESET}")
                        if signal_match:
                            print(f"📶 Signal: {signal_match.group(1).strip()}")
                    else:
                        print(f"{COLORS['4'][0]}[*] Not connected to any network.{RESET}")
                else:
                    result = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
                    for line in result.split('\n'):
                        if 'SSID' in line and ':' in line:
                            ssid = line.split(':')[1].strip()
                            if ssid:
                                print(f"\n📡 SSID: {BOLD}{ssid}{RESET}")
            except Exception as e:
                print(f"{COLORS['1'][0]}[!] Error: {e}{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif wifi_choice == '4':
            print_header("🌐 Network Connectivity Test")
            hosts = ['8.8.8.8', 'cloudflare.com', 'google.com']
            print(f"Testing connectivity to multiple hosts...\n")
            for host in hosts:
                try:
                    param = '-n' if os.name == 'nt' else '-c'
                    result = subprocess.call(['ping', param, '1', host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3)
                    status = f"{COLORS['2'][0]}✅ Reachable{RESET}" if result == 0 else f"{COLORS['1'][0]}❌ Unreachable{RESET}"
                    print(f"  {host:<20} {status}")
                except:
                    print(f"  {host:<20} {COLORS['1'][0]}❌ Timeout{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif wifi_choice == '5':
            print_header("🔑 WiFi MAC Address")
            try:
                if os.name != 'nt':
                    result = subprocess.check_output(['ip', 'link', 'show', 'wlan0'], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
                    mac_match = re.search(r'link/ether\s([a-f0-9:]{17})', result)
                    if mac_match:
                        print(f"\nMAC Address (wlan0): {BOLD}{mac_match.group(1)}{RESET}")
                else:
                    result = subprocess.check_output(['getmac'], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
                    print(f"\nMAC Addresses:\n{result}")
            except Exception as e:
                print(f"{COLORS['1'][0]}[!] Error: {e}{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif wifi_choice == '6':
            print_header("📡 Signal Strength Monitor (5 samples)")
            try:
                samples = []
                for i in range(5):
                    if os.name != 'nt':
                        result = subprocess.check_output(['iwconfig', 'wlan0'], stderr=subprocess.DEVNULL).decode('utf-8', errors='ignore')
                        signal_match = re.search(r'Signal level[=:]([^\n]+)', result)
                        if signal_match:
                            samples.append(signal_match.group(1).strip())
                    else:
                        samples.append('N/A (Windows)')
                    if i < 4:
                        time.sleep(1)

                print(f"\nSignal Strength Samples:")
                for idx, sample in enumerate(samples, 1):
                    print(f"  Sample {idx}: {sample}")
            except Exception as e:
                print(f"{COLORS['1'][0]}[!] Error: {e}{RESET}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif wifi_choice == '7':
            feature_download_center()
        elif wifi_choice == '8':
            break

def _bluetoothctl_run(commands, timeout=8):
    """Wrapper for bluetoothctl command sequences."""
    try:
        proc = subprocess.Popen(
            ["bluetoothctl"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
    except FileNotFoundError:
        return None

    try:
        out, _ = proc.communicate("\n".join(commands) + "\n", timeout=timeout)
        return out
    except subprocess.TimeoutExpired:
        try:
            proc.kill()
        except Exception:
            pass
        return "[!] bluetoothctl timed out."

def _bluetooth_available():
    try:
        subprocess.run(["bluetoothctl", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def feature_bluetooth_toolkit():
    """Bluetooth tools via system bluetoothctl wrapper."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("Bluetooth Toolkit")
        print(f" {BOLD}[1]{RESET} Show Adapter Status")
        print(f" {BOLD}[2]{RESET} List Paired Devices")
        print(f" {BOLD}[3]{RESET} Scan Nearby Devices (Short)")
        print(f" {BOLD}[4]{RESET} Connect to Device")
        print(f" {BOLD}[5]{RESET} Disconnect Device")
        print(f" {BOLD}[6]{RESET} Remove Device")
        print(f" {BOLD}[7]{RESET} Return to Main Menu")
        bt_choice = input(f"\n{BOLD}Select Bluetooth Tool (1-7): {RESET}").strip()

        if bt_choice == '7':
            break

        if os.name != 'posix':
            print(f"{COLORS['4'][0]}[!] Bluetooth tools are supported on Linux only.{RESET}")
            input(f"\n{BOLD}[ Press Enter to return... ]{RESET}")
            continue

        if not _bluetooth_available():
            print(f"{COLORS['1'][0]}[!] bluetoothctl not found. Install bluez tools first.{RESET}")
            input(f"\n{BOLD}[ Press Enter to return... ]{RESET}")
            continue

        if bt_choice == '1':
            out = _bluetoothctl_run(["show", "quit"], timeout=4)
            print(out if out else "[!] bluetoothctl unavailable")
        elif bt_choice == '2':
            out = _bluetoothctl_run(["paired-devices", "quit"], timeout=4)
            print(out if out else "[!] bluetoothctl unavailable")
        elif bt_choice == '3':
            print("Scanning for nearby devices (8s)...")
            out = _bluetoothctl_run(["scan on"], timeout=8)
            print(out if out else "[!] bluetoothctl unavailable")
            _bluetoothctl_run(["scan off", "quit"], timeout=3)
        elif bt_choice == '4':
            mac = input("Enter device MAC to connect: ").strip()
            if mac:
                out = _bluetoothctl_run([f"connect {mac}", "quit"], timeout=8)
                print(out if out else "[!] bluetoothctl unavailable")
        elif bt_choice == '5':
            mac = input("Enter device MAC to disconnect: ").strip()
            if mac:
                out = _bluetoothctl_run([f"disconnect {mac}", "quit"], timeout=6)
                print(out if out else "[!] bluetoothctl unavailable")
        elif bt_choice == '6':
            mac = input("Enter device MAC to remove: ").strip()
            if mac:
                out = _bluetoothctl_run([f"remove {mac}", "quit"], timeout=6)
                print(out if out else "[!] bluetoothctl unavailable")

        input(f"\n{BOLD}[ Press Enter to return... ]{RESET}")

def feature_ai_center():
    """A.I. Center: Access ChatGPT, Google Gemini, Copilot, DeepSeek, and Claude"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🤖 A.I. Center")
        print(f" {BOLD}[1]{RESET} 🔴 ChatGPT (OpenAI)")
        print(f" {BOLD}[2]{RESET} 🔵 Google Gemini")
        print(f" {BOLD}[3]{RESET} 🟣 Microsoft Copilot")
        print(f" {BOLD}[4]{RESET} 🟠 DeepSeek")
        print(f" {BOLD}[5]{RESET} 🟡 Claude (Anthropic)")
        print(f" {BOLD}[6]{RESET} 🧠 AI Probe Center")
        print(f" {BOLD}[7]{RESET} 📦 Open Download Center (AI Tools)")
        print(f" {BOLD}[8]{RESET} ↩️ Return to Main Menu")
        ai_choice = input(f"\n{BOLD}🎯 Select A.I. Service (1-8): {RESET}").strip()

        if ai_choice == '1':
            print_header("🤖 ChatGPT (OpenAI)")
            print(f"\n{COLORS['2'][0]}🔗 Launching ChatGPT in browser...{RESET}")
            print(f"Choose an option:")
            print(f" {BOLD}[1]{RESET} 🌐 Open in Browser")
            print(f" {BOLD}[2]{RESET} 🔑 API Integration (requires API key)")
            print(f" {BOLD}[3]{RESET} ↩️ Back")
            sub_choice = input(f"\n{BOLD}Choice: {RESET}").strip()

            if sub_choice == '1':
                print(f"Opening ChatGPT...\\n")
                os.system("$BROWSER 'https://chat.openai.com' 2>/dev/null &" if os.name != 'nt' else "start https://chat.openai.com")
                print(f"{COLORS['2'][0]}✅ ChatGPT opened in your browser. Press Enter to continue...{RESET}")
                input()
            elif sub_choice == '2':
                print(f"\n{COLORS['4'][0]}API Setup: https://platform.openai.com/api-keys{RESET}")
                api_key = input(f"Enter your OpenAI API key (or press Enter to skip): ").strip()
                if api_key:
                    print(f"{COLORS['2'][0]}✅ API key saved (demo - not actually stored for security){RESET}")
                    user_input = input(f"\n{BOLD}You: {RESET}").strip()
                    if user_input:
                        print(f"{COLORS['4'][0]}[*] To use API directly, run: curl https://api.openai.com/v1/chat/completions -H \"Authorization: Bearer YOUR_KEY\" ...{RESET}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif ai_choice == '2':
            print_header("🤖 Google Gemini")
            print(f"\n{COLORS['2'][0]}🔗 Launching Google Gemini in browser...{RESET}")
            print(f"Choose an option:")
            print(f" {BOLD}[1]{RESET} 🌐 Open in Browser")
            print(f" {BOLD}[2]{RESET} 🔑 API Integration (requires API key)")
            print(f" {BOLD}[3]{RESET} ↩️ Back")
            sub_choice = input(f"\n{BOLD}Choice: {RESET}").strip()

            if sub_choice == '1':
                print(f"Opening Google Gemini...\\n")
                os.system("$BROWSER 'https://gemini.google.com' 2>/dev/null &" if os.name != 'nt' else "start https://gemini.google.com")
                print(f"{COLORS['2'][0]}✅ Google Gemini opened in your browser. Press Enter to continue...{RESET}")
                input()
            elif sub_choice == '2':
                print(f"\n{COLORS['4'][0]}API Setup: https://aistudio.google.com/apikey{RESET}")
                api_key = input(f"Enter your Google AI Studio API key (or press Enter to skip): ").strip()
                if api_key:
                    print(f"{COLORS['2'][0]}✅ API key configured (demo){RESET}")
                    user_input = input(f"\n{BOLD}You: {RESET}").strip()
                    if user_input:
                        print(f"{COLORS['4'][0]}[*] To use API directly, run: curl https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent ...{RESET}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif ai_choice == '3':
            print_header("🤖 Microsoft Copilot")
            print(f"\n{COLORS['2'][0]}🔗 Launching Microsoft Copilot in browser...{RESET}")
            print(f"Choose an option:")
            print(f" {BOLD}[1]{RESET} 🌐 Open in Browser")
            print(f" {BOLD}[2]{RESET} 🔑 API Integration (Azure OpenAI)")
            print(f" {BOLD}[3]{RESET} ↩️ Back")
            sub_choice = input(f"\n{BOLD}Choice: {RESET}").strip()

            if sub_choice == '1':
                print(f"Opening Microsoft Copilot...\\n")
                os.system("$BROWSER 'https://copilot.microsoft.com' 2>/dev/null &" if os.name != 'nt' else "start https://copilot.microsoft.com")
                print(f"{COLORS['2'][0]}✅ Microsoft Copilot opened in your browser. Press Enter to continue...{RESET}")
                input()
            elif sub_choice == '2':
                print(f"\n{COLORS['4'][0]}API Setup: https://portal.azure.com (Azure OpenAI){RESET}")
                endpoint = input(f"Enter your Azure OpenAI endpoint (or press Enter to skip): ").strip()
                if endpoint:
                    print(f"{COLORS['2'][0]}✅ Endpoint configured (demo){RESET}")
                    user_input = input(f"\n{BOLD}You: {RESET}").strip()
                    if user_input:
                        print(f"{COLORS['4'][0]}[*] Use Azure SDK: pip install azure-openai{RESET}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif ai_choice == '4':
            print_header("🤖 DeepSeek")
            print(f"\n{COLORS['2'][0]}🔗 Launching DeepSeek in browser...{RESET}")
            print(f"Choose an option:")
            print(f" {BOLD}[1]{RESET} 🌐 Open in Browser")
            print(f" {BOLD}[2]{RESET} 🔑 API Integration (requires API key)")
            print(f" {BOLD}[3]{RESET} ↩️ Back")
            sub_choice = input(f"\n{BOLD}Choice: {RESET}").strip()

            if sub_choice == '1':
                print(f"Opening DeepSeek...\\n")
                os.system("$BROWSER 'https://chat.deepseek.com' 2>/dev/null &" if os.name != 'nt' else "start https://chat.deepseek.com")
                print(f"{COLORS['2'][0]}✅ DeepSeek opened in your browser. Press Enter to continue...{RESET}")
                input()
            elif sub_choice == '2':
                print(f"\n{COLORS['4'][0]}API Setup: https://platform.deepseek.com/api{RESET}")
                api_key = input(f"Enter your DeepSeek API key (or press Enter to skip): ").strip()
                if api_key:
                    print(f"{COLORS['2'][0]}✅ API key configured (demo){RESET}")
                    user_input = input(f"\n{BOLD}You: {RESET}").strip()
                    if user_input:
                        print(f"{COLORS['4'][0]}[*] Use curl: curl https://api.deepseek.com/chat/completions ...{RESET}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif ai_choice == '5':
            print_header("🤖 Claude (Anthropic)")
            print(f"\n{COLORS['2'][0]}🔗 Launching Claude in browser...{RESET}")
            print(f"Choose an option:")
            print(f" {BOLD}[1]{RESET} 🌐 Open in Browser")
            print(f" {BOLD}[2]{RESET} 🔑 API Integration (requires API key)")
            print(f" {BOLD}[3]{RESET} ↩️ Back")
            sub_choice = input(f"\n{BOLD}Choice: {RESET}").strip()

            if sub_choice == '1':
                print(f"Opening Claude...\\n")
                os.system("$BROWSER 'https://claude.ai' 2>/dev/null &" if os.name != 'nt' else "start https://claude.ai")
                print(f"{COLORS['2'][0]}✅ Claude opened in your browser. Press Enter to continue...{RESET}")
                input()
            elif sub_choice == '2':
                print(f"\n{COLORS['4'][0]}API Setup: https://console.anthropic.com/keys{RESET}")
                api_key = input(f"Enter your Anthropic API key (or press Enter to skip): ").strip()
                if api_key:
                    print(f"{COLORS['2'][0]}✅ API key configured (demo){RESET}")
                    user_input = input(f"\n{BOLD}You: {RESET}").strip()
                    if user_input:
                        print(f"{COLORS['4'][0]}[*] Use Python: pip install anthropic{RESET}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

        elif ai_choice == '6':
            feature_deep_probe_ai()
        elif ai_choice == '7':
            feature_download_center()
        elif ai_choice == '8':
            break

def feature_security_audit():
    print_header("🛡️ Security & Port Audit")
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389]
    print(f"📡 Scanning {len(common_ports)} common entry points on localhost...")
    found_any = False
    open_ports = []
    for port in common_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            if s.connect_ex(('127.0.0.1', port)) == 0:
                print(f" {COLORS['1'][0]}[!] ⚠️ OPEN:{RESET} Port {port}")
                open_ports.append(port)
                found_any = True
    if not found_any: print(f" {COLORS['2'][0]}[+] ✅ No standard high-risk ports open locally.{RESET}")
    print_header("👤 Security Context")
    is_admin = False
    try: is_admin = os.getuid() == 0
    except: is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    print(f"👑 Admin/Root Privileges: {'YES' if is_admin else 'NO'}")

    # Logging capability
    audit_log = f"Security Audit Report\\n\\nPorts Scanned: {common_ports}\\n"
    if open_ports:
        audit_log += f"Open Ports Found: {open_ports}\\n"
    else:
        audit_log += "No high-risk ports open\\n"
    audit_log += f"\\nAdmin/Root Privileges: {'YES' if is_admin else 'NO'}\\n"
    save_log_file("security", "Security_Audit", audit_log, prompt_user=True)

    input(f"\\n{BOLD}[ ✅ Audit Complete. Press Enter... ]{RESET}")

def feature_environment_probe():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📂 Environment & Path Probe")
        print(f" {BOLD}[1]{RESET} 📌 Quick Summary")
        print(f" {BOLD}[2]{RESET} 🌿 Environment Variables (Top 40)")
        print(f" {BOLD}[3]{RESET} 🧭 Python Paths & Exec")
        print(f" {BOLD}[4]{RESET} 🗂️  Data Directories")
        print(f" {BOLD}[5]{RESET} 💾 Save Report to Logs")
        print(f" {BOLD}[0]{RESET} ↩️  Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return
        if choice == '1':
            print_header("📌 Quick Summary")
            print(f"📁 Current Working Dir: {os.getcwd()}")
            print(f"🏠 User Home Dir:       {os.path.expanduser('~')}")
            print(f"🐍 Python Executable:   {sys.executable}")
            print(f"🔤 Default Encoding:    {sys.getdefaultencoding()}")
            print(f"🗂️ Filesystem Encoding: {sys.getfilesystemencoding()}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '2':
            print_header("🌿 Environment Variables")
            for i, (k, v) in enumerate(os.environ.items()):
                if i >= 40:
                    break
                print(f"{k}={v}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            print_header("🧭 Python Paths")
            print(f"Python Executable: {sys.executable}")
            print("sys.path:")
            for p in sys.path:
                print(f"  - {p}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '4':
            print_header("🗂️ Data Directories")
            print(f"Script Dir: {SCRIPT_DIR}")
            print(f"DB Dir:     {DB_DIR}")
            print(f"Log Dir:    {LOG_DIR}")
            print(f"Swap Cache: {SWAP_CACHE_DIR}")
            print(f"Config:     {CONFIG_FILE}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '5':
            lines = [
                "Environment Probe Report",
                f"CWD: {os.getcwd()}",
                f"Home: {os.path.expanduser('~')}",
                f"Python: {sys.executable}",
                f"Default Encoding: {sys.getdefaultencoding()}",
                f"Filesystem Encoding: {sys.getfilesystemencoding()}",
                f"Script Dir: {SCRIPT_DIR}",
                f"DB Dir: {DB_DIR}",
                f"Log Dir: {LOG_DIR}",
                f"Swap Cache: {SWAP_CACHE_DIR}",
                f"Config: {CONFIG_FILE}",
            ]
            payload = "\n".join(lines)
            save_log_file("system", "Environment_Probe", payload, prompt_user=True)
            try:
                log_to_database("system", "Environment_Probe", payload, status="success")
            except Exception:
                pass
            input(f"\n{BOLD}[ ✅ Probe Complete. Press Enter... ]{RESET}")

def feature_hardware_serials():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📟 Hardware Identity Center")
        print(f" {BOLD}[1]{RESET} 🧾 BIOS/Board Serial (if available)")
        print(f" {BOLD}[2]{RESET} 🧠 CPU/GPU Summary")
        print(f" {BOLD}[3]{RESET} 🔌 Network MAC Addresses")
        print(f" {BOLD}[4]{RESET} 💾 Mounted Partitions")
        print(f" {BOLD}[5]{RESET} 💾 Save Hardware Report")
        print(f" {BOLD}[0]{RESET} ↩️  Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return
        if choice == '1':
            print_header("🧾 BIOS/Board Serial")
            if os.name == 'nt':
                try:
                    bios = subprocess.check_output("wmic bios get serialnumber").decode().split('\n')[1].strip()
                    print(f"🔢 BIOS Serial:         {bios}")
                except Exception:
                    print("🔢 BIOS Serial:         Access Denied")
            else:
                print("BIOS serial lookup is OS-specific. Use dmidecode if available.")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '2':
            print_header("🧠 CPU/GPU Summary")
            print(f"CPU: {platform.processor()}")
            gpu, fan = get_advanced_hardware_stats()
            print(f"GPU: {gpu}")
            print(f"Fan: {fan}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            print_header("🔌 Network MAC Addresses")
            try:
                if_addrs = psutil.net_if_addrs()
                for iface, addrs in if_addrs.items():
                    for addr in addrs:
                        if getattr(addr, "family", None) == psutil.AF_LINK:
                            print(f"{iface}: {addr.address}")
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '4':
            print_header("💾 Mounted Partitions")
            for part in psutil.disk_partitions():
                print(f"💾 Device: {part.device:<10} | 📍 Mount: {part.mountpoint:<10} | 📂 Type: {part.fstype}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '5':
            lines = [
                "Hardware Identity Report",
                f"CPU: {platform.processor()}",
                f"Platform: {platform.system()} {platform.release()} {platform.machine()}",
            ]
            gpu, fan = get_advanced_hardware_stats()
            lines.append(f"GPU: {gpu}")
            lines.append(f"Fan: {fan}")
            payload = "\n".join(lines)
            save_log_file("hardware", "Hardware_Identity", payload, prompt_user=True)
            try:
                log_to_database("hardware", "Hardware_Identity", payload, status="success")
            except Exception:
                pass
            input(f"\n{BOLD}[ ✅ Hardware Probe Finished. Press Enter... ]{RESET}")

# ================================================================================
# SECTION 14: GRAPHING CALCULATOR (TI-Nspire CX II CAS Simulation)
# ================================================================================
# Complete graphing calculator with:
# - Computer Algebra System (CAS) using SymPy
# - Function plotting (ASCII terminal and matplotlib)
# - Scientific calculator functions
# - Statistical analysis
# - Matrix operations
# - Equation solver
# - Unit converter
# - Programming environment
# ================================================================================

# --- ADVANCED GRAPHING CALCULATOR (CURSES-BASED SCIENCE CONSOLE) ---

class ScienceConsole:
    def __init__(self):
        self.base_namespace = {
            **{name: getattr(math, name) for name in dir(math) if not name.startswith("__")},
            **{name: getattr(cmath, name) for name in dir(cmath) if not name.startswith("__")},
            **{name: getattr(statistics, name) for name in dir(statistics) if not name.startswith("__")},
            "abs": abs, "round": round, "pow": pow, "sum": sum, "min": min, "max": max, "len": len,
            "bin": bin, "hex": hex, "oct": oct, "int": int, "float": float, "complex": complex
        }
        self.user_vars = {"a": 1.0, "b": 5.0, "c": 0.0, "y": 0.0}
        self.history = ["LOGIC CORE: MAXIMIZED", "SCHOLAR MODE: ACTIVE"]
        self.rolling_calcs = ["Select a sample (;) to begin analysis."]
        self.cmd_history = []
        self.input_buffer = ""
        self.active_func = "sin(x + t)"
        self.frame = 0
        self.zoom = 1.0
        self.offset_x = 0.0

        # SAMPLES LIBRARY: RESTORED & ENHANCED WITH SYNTAX GUIDES
        self.samples = [
            ("sin(x + t)", "Sine Wave", "Math: Periodic oscillation. Life: Sound waves. Syntax: sin(x + t)"),
            ("x^3 + x^2*y + x*y^2 + y^3 + sin(t)", "Polynomial", "Math: Higher-order logic. Life: Fluid stress. Syntax: x^3 + x^2 y + x y^2 + y^3"),
            ("abs(sin(x + t))*2", "Rectified Wave", "Math: Absolute periodicity. Life: Power adapters. Syntax: abs(sin(x+t))*2"),
            ("exp(-abs(x)) * cos(x * t)", "Quantum Pulse", "Math: Dampened oscillation. Life: Shock absorbers. Syntax: exp(-abs(x)) * cos(x*t)"),
            ("1 / (1 + exp(-x + sin(t)))", "Sigmoid Curve", "Math: Logistic growth. Life: AI Neural Nets. Syntax: 1 / (1 + exp(-x))"),
            ("solve([1,1,10 + sin(t)],[1,-1,4])", "Linear System", "Math: Intersection logic. Life: GPS. Syntax: solve([1,1,10],[1,-1,4])"),
            ("sqrt(abs(1 - (abs(x)-1)**2)) + 0.1*sin(t)", "Heart Curve", "Math: Geometry. Life: Organic shapes. Syntax: sqrt(abs(1-(abs(x)-1)^2))"),
            ("sin(x * (5 + sin(t)))/5", "Frequency Warp", "Math: Variable period. Life: Doppler effect. Syntax: sin(x*5)/5"),
            ("sin(x*1.1 + t) + sin(x*0.9 + t)", "Beat Pattern", "Math: Superposition. Life: Tuning instruments. Syntax: sin(x*1.1) + sin(x*0.9)"),
            ("1 if sin(x + t) > 0 else -1", "Square Wave", "Math: Binary logic. Life: Computer clocks. Syntax: 1 if sin(x)>0 else -1"),
            ("abs((x + t) % 2 - 1)", "Triangle Wave", "Math: Linear periodicity. Life: Synthesizers. Syntax: abs((x)%2 - 1)"),
            ("(x + t) % 1", "Sawtooth Drive", "Math: Harmonic rise. Life: CRT electron beams. Syntax: x % 1"),
            ("exp(-0.5 * (x + sin(t))**2)", "Gaussian Bell", "Math: Distribution. Life: IQ scores/Probability. Syntax: exp(-0.5 * x^2)"),
            ("sin(x**2 + t)", "Fresnel Integral", "Math: Quadratic phase. Life: Light diffraction. Syntax: sin(x^2)"),
            ("log(abs(x) + 1) * sin(x + t)", "Log-Amplitude", "Math: Growth scaling. Life: Richter scale/Decibels. Syntax: log(abs(x)+1)"),
            ("sin(x * (3 + sin(t*0.5)) + t)", "FM Synthesis", "Math: Freq modulation. Life: Radio broadcast. Syntax: sin(x*(3+sin(t)))"),
            ("(1 + 0.5 * sin(t)) * sin(5 * x)", "AM Synthesis", "Math: Amp modulation. Life: AM Radio signals. Syntax: (1+0.5)*sin(5*x)"),
            ("max(-2, min(2, tan(x + t)))", "Clipped Tan", "Math: Bound tangent. Life: Guitar distortion. Syntax: tan(x)"),
            ("0.1 * x**3 - x + sin(t)", "Cubic Drift", "Math: Polynomial roots. Life: Bridge engineering. Syntax: 0.1*x^3 - x"),
            ("floor(x + t)", "Step Scroll", "Math: Integer flooring. Life: Digital sampling. Syntax: floor(x)"),
            ("sin(x + t) / (x if x != 0 else 0.01)", "Sinc Pulse", "Math: Sampling theorem. Life: Image resizing. Syntax: sin(x)/x"),
            ("sinh(x + sin(t)) / cosh(x)", "Hyperbolic Tanh", "Math: Logistic limit. Life: Deep learning. Syntax: sinh(x)/cosh(x)"),
            ("0.1 * x**4 - x**2 + sin(t)", "Double Well", "Math: Bifurcation. Life: Magnetic states. Syntax: 0.1*x^4 - x^2"),
            ("sin(x + t) + 0.5 * sin(10 * x + t*2)", "Turbulence", "Math: Fourier. Life: Wind/Water ripples. Syntax: sin(x) + 0.5*sin(10*x)"),
            ("log(log(abs(x) + 2) + 1)", "Double Log", "Math: Iterated growth. Life: Complexity analysis. Syntax: log(log(x+2)+1)"),
            ("exp(-x**2) * sin(10 * x + t)", "Wavelet", "Math: Localized wave. Life: MRI imaging/JPEG. Syntax: exp(-x^2)*sin(10*x)"),
            ("abs(x + sin(t)) ** 0.5", "Root Curve", "Math: Concave growth. Life: Brightness perception. Syntax: abs(x)^0.5"),
            ("sin(x - t) - sin(x + t)", "Standing Wave", "Math: Node logic. Life: Microwave heating. Syntax: sin(x-t)-sin(x+t)"),
            ("pow(2, (x + sin(t))/4) / 10", "Exponential", "Math: Growth. Life: Virus spread/Fission. Syntax: 2^(x/4)"),
            ("1 if (x + t) % 2 < 0.2 else 0", "Pulse Train", "Math: Duty cycle. Life: LED Dimming (PWM). Syntax: 1 if x%2<0.2 else 0"),
            ("cos(x) * sin(t)", "Phase Shifter", "Math: Oscillation. Life: Phased-array radar. Syntax: cos(x)*sin(t)"),
            ("0.5 * (x + sin(x + t))", "Jitter Line", "Math: Stochastic drift. Life: Stock trends. Syntax: 0.5*(x+sin(x))")
        ]
        self.sample_idx = -1

    def solve_linear(self, eq1, eq2):
        try:
            a, b = np.array([[eq1[0], eq1[1]], [eq2[0], eq2[1]]]), np.array([eq1[2], eq2[2]])
            res = np.linalg.solve(a, b)
            return f"x={res[0]:.2f}, y={res[1]:.2f}"
        except: return "Check solve() args"

    def ai_preprocess(self, expr):
        expr = expr.replace("^", "**")
        expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
        expr = re.sub(r'([xytabc])\s+([xytabc])', r'\1*\2', expr)
        expr = re.sub(r'([xytabc])([xytabc])', r'\1*\2', expr)
        return expr

    def safe_eval(self, expr, x=0, t=0):
        expr = self.ai_preprocess(expr)
        try:
            ctx = {**self.base_namespace, **self.user_vars, "x": x, "t": t, "solve": self.solve_linear}
            return eval(expr, {"__builtins__": None}, ctx)
        except: return None

    def draw_input(self, win):
        h, w = win.getmaxyx()
        win.erase(); win.attron(curses.color_pair(1)); win.box()
        win.addstr(0, 2, " ⌨️ COMMAND INTERFACE ")
        for i, entry in enumerate(self.history[-4:]):
            win.addstr(1 + i, 2, f" • {str(entry)[:w-6]}", curses.color_pair(5))
        win.addstr(h-2, 2, " CMD > ", curses.color_pair(2) | curses.A_BOLD)
        win.addstr(self.input_buffer, curses.color_pair(2) | curses.A_BOLD)
        if (self.frame // 10) % 2 == 0:
            win.addch(h-2, 10 + len(self.input_buffer), curses.ACS_BLOCK, curses.color_pair(2))
        msg = " [;] SAMPLES+  [ESC] EXIT "
        win.addstr(h-2, w - len(msg) - 2, msg, curses.color_pair(4))
        win.noutrefresh()

    def draw_log(self, win):
        h, w = win.getmaxyx()
        win.erase(); win.attron(curses.color_pair(2)); win.box()
        mid = w // 2
        for y in range(1, h-1):
            try: win.addch(y, mid, curses.ACS_VLINE)
            except: pass
        win.addstr(0, 2, " 📖 SYNTAX ")
        guide = ["POWER: x^3", "COEFF: 2x", "TERMS: x y", "SYSTEM: solve()"]
        for i, line in enumerate(guide): win.addstr(1 + i, 1, line[:mid-2], curses.color_pair(1))

        win.addstr(0, mid + 2, " 💡 ANALYTICAL FEED ")
        y_off = 1
        for entry in self.rolling_calcs:
            words = str(entry).split()
            line = ""
            for word in words:
                if len(line + word) > (w - mid - 6):
                    if y_off < h-1: win.addstr(y_off, mid + 2, line, curses.color_pair(4)); y_off += 1
                    line = word + " "
                else: line += word + " "
            if y_off < h-1: win.addstr(y_off, mid + 2, line, curses.color_pair(4)); y_off += 1
        win.noutrefresh()

    def draw_graph(self, win):
        h, w = win.getmaxyx()
        win.erase(); win.attron(curses.color_pair(3)); win.box()
        ctrls = " [PGUP/DN] ZOOM | [L/R ARROWS] PAN "
        win.addstr(0, 2, f" 📡 {self.active_func} ", curses.A_BOLD)
        win.addstr(0, w - len(ctrls) - 2, ctrls, curses.color_pair(4))
        mid_y, mid_x = h // 2, w // 2
        for x_p in range(1, w-1):
            try: win.addch(mid_y, x_p, curses.ACS_HLINE, curses.A_DIM)
            except: pass
        for y_p in range(1, h-1):
            try: win.addch(y_p, mid_x, curses.ACS_VLINE, curses.A_DIM)
            except: pass
        for x_pixel in range(1, w - 1):
            x_val = (x_pixel - mid_x) * (0.15 / self.zoom) + self.offset_x
            y_val = self.safe_eval(self.active_func, x=x_val, t=self.frame * 0.1)
            if isinstance(y_val, (int, float, complex)):
                if isinstance(y_val, complex): y_val = y_val.real
                y_pixel = int(mid_y - (y_val * (h / 5) * self.zoom))
                if 1 <= y_pixel < h - 1: win.addch(y_pixel, x_pixel, "█")
        win.noutrefresh()

    def run(self, stdscr):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
        stdscr.nodelay(True); stdscr.keypad(True); curses.curs_set(0)
        while True:
            h, w = stdscr.getmaxyx()
            if h < 22 or w < 80:
                stdscr.addstr(0,0, "ENLARGE WINDOW"); stdscr.refresh(); time.sleep(0.1); continue
            win_in, win_log, win_graph = curses.newwin(h//2, w//2, 0, 0), curses.newwin(h//2, w-(w//2), 0, w//2), curses.newwin(h-(h//2), w, h//2, 0)
            key = stdscr.getch()
            if key == 27: break
            elif key == ord(';'):
                self.sample_idx = (self.sample_idx + 1) % len(self.samples)
                func, title, desc = self.samples[self.sample_idx]
                self.active_func = func
                self.history.append(f"LOAD: {title}")
                self.rolling_calcs = [f"NAME: {title}", "", desc]
            elif key == curses.KEY_PPAGE: self.zoom *= 1.1
            elif key == curses.KEY_NPAGE: self.zoom *= 0.9
            elif key in [curses.KEY_LEFT, curses.KEY_RIGHT]:
                self.offset_x += (1.0/self.zoom if key == curses.KEY_RIGHT else -1.0/self.zoom)
            elif key == 10:
                if self.input_buffer.strip():
                    res = self.safe_eval(self.input_buffer, x=1)
                    if res is not None:
                        f_res = f"{res:.4f}" if isinstance(res, float) else str(res)
                        self.history.append(f_res); self.rolling_calcs = [f"RES: {f_res}"]
                        if "=" not in self.input_buffer and "solve" not in self.input_buffer: self.active_func = self.input_buffer
                    else: self.history.append("ERR: CHECK SYNTAX")
                    self.input_buffer = ""
            elif key in (curses.KEY_BACKSPACE, 127, 8): self.input_buffer = self.input_buffer[:-1]
            elif 32 <= key <= 126: self.input_buffer += chr(key)
            self.draw_input(win_in); self.draw_log(win_log); self.draw_graph(win_graph)
            curses.doupdate(); self.frame += 1; time.sleep(0.04)

def _calc_advanced_graphing():
    """Launch the Advanced Graphing Calculator (Curses-based Science Console)"""
    try:
        console = ScienceConsole()
        curses.wrapper(console.run)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"{COLORS['1'][0]}Error launching Advanced Graphing Calculator: {e}{RESET}")
        input("Press Enter to continue...")

# --- STANDARD GRAPHING CALCULATOR MENU ---

def feature_graphing_calculator():
    """Advanced Graphing Calculator - TI-Nspire CX II CAS Simulation."""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📊 Graphing Calculator - TI-Nspire CX II CAS", extra_info="| Python CAS Edition")

        print(f"\n{BOLD}Main Menu:{RESET}")
        print(f" {BOLD}[A]{RESET}  🧠 Advanced Graphing Calculator (Interactive Curses HUD)")
        print(f" {BOLD}[1]{RESET}  📈 Graph Plotter (ASCII Terminal)")
        print(f" {BOLD}[2]{RESET}  🧮 Scientific Calculator")
        print(f" {BOLD}[3]{RESET}  🔬 CAS - Computer Algebra System")
        print(f" {BOLD}[4]{RESET}  📊 Statistics & Data Analysis")
        print(f" {BOLD}[5]{RESET}  🔢 Matrix Calculator")
        print(f" {BOLD}[6]{RESET}  ⚖️ Equation Solver")
        print(f" {BOLD}[7]{RESET}  🔄 Unit Converter")
        print(f" {BOLD}[8]{RESET}  💾 Save/Load Calculations")
        print(f" {BOLD}[9]{RESET}  📖 Calculator Help & Examples")
        print(f" {BOLD}[0]{RESET}  ↩️  Return to Command Center")

        choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip().upper()

        if choice == '0':
            break
        elif choice == 'A':
            safe_run("general", "Advanced_Graphing_Calculator", _calc_advanced_graphing)
        elif choice == '1':
            safe_run("general", "Graph_Plotter", _calc_graph_plotter)
        elif choice == '2':
            safe_run("general", "Scientific_Calculator", _calc_scientific)
        elif choice == '3':
            safe_run("general", "CAS_System", _calc_cas_system)
        elif choice == '4':
            safe_run("general", "Statistics", _calc_statistics)
        elif choice == '5':
            safe_run("general", "Matrix_Calculator", _calc_matrix)
        elif choice == '6':
            safe_run("general", "Equation_Solver", _calc_equation_solver)
        elif choice == '7':
            safe_run("general", "Unit_Converter", _calc_unit_converter)
        elif choice == '8':
            safe_run("general", "Save_Load", _calc_save_load)
        elif choice == '9':
            safe_run("general", "Calculator_Help", _calc_help)

def _calc_graph_plotter():
    """ASCII Terminal Graph Plotter with Gnuplot-style output."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📈 Function Graph Plotter", extra_info="| ASCII Terminal Mode")

    print(f"\n{BOLD}Graph Plotter Options:{RESET}")
    print(f" {BOLD}[1]{RESET} Plot Single Function")
    print(f" {BOLD}[2]{RESET} Plot Multiple Functions")
    print(f" {BOLD}[3]{RESET} Parametric Plot")
    print(f" {BOLD}[4]{RESET} Polar Plot")
    print(f" {BOLD}[5]{RESET} 3D Surface Plot (ASCII)")
    print(f" {BOLD}[0]{RESET} Return")

    choice = input(f"\n{BOLD}Select: {RESET}").strip()

    if choice == '1':
        _plot_single_function()
    elif choice == '2':
        _plot_multiple_functions()
    elif choice == '3':
        _plot_parametric()
    elif choice == '4':
        _plot_polar()
    elif choice == '5':
        _plot_3d_surface()

def _plot_single_function():
    """Plot a single function in ASCII terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📈 Single Function Plot")

    print(f"\n{BOLD}Enter function to plot:{RESET}")
    print(f"Examples: sin(x), x**2, exp(x), log(x), sqrt(x)")
    print(f"Use: +, -, *, /, **, sin, cos, tan, exp, log, sqrt, abs")

    func_str = input(f"\nf(x) = ").strip()
    if not func_str:
        print("No function entered.")
        input("\nPress Enter...")
        return

    try:
        x_min = float(input(f"X min (default -10): ").strip() or "-10")
        x_max = float(input(f"X max (default 10): ").strip() or "10")
        width = int(input(f"Graph width (default 80): ").strip() or "80")
        height = int(input(f"Graph height (default 24): ").strip() or "24")

        os.system('cls' if os.name == 'nt' else 'clear')
        print_header(f"Graph: f(x) = {func_str}")
        print(f"Domain: [{x_min}, {x_max}]\n")

        # Generate ASCII plot
        _render_ascii_plot(func_str, x_min, x_max, width, height)

        # Save option
        save = input(f"\n{BOLD}Save to log? (y/n): {RESET}").strip().lower()
        if save == 'y':
            plot_data = f"Function: f(x) = {func_str}\nDomain: [{x_min}, {x_max}]\n"
            save_log_file("general", "Graph_Plot", plot_data, prompt_user=False)
            print(f"{COLORS['2'][0]}✅ Plot saved to logs{RESET}")

    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _render_ascii_plot(func_str, x_min, x_max, width=80, height=24):
    """Render ASCII plot of a function."""
    import numpy as np

    # Create grid
    grid = [[' ' for _ in range(width)] for _ in range(height)]

    # Generate x values
    x_values = np.linspace(x_min, x_max, width * 2)
    y_values = []

    # Evaluate function
    for x in x_values:
        try:
            # Safe eval with math functions
            safe_dict = {
                'x': x,
                'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                'exp': np.exp, 'log': np.log, 'sqrt': np.sqrt,
                'abs': np.abs, 'pi': np.pi, 'e': np.e
            }
            y = eval(func_str, {"__builtins__": {}}, safe_dict)
            y_values.append(y)
        except:
            y_values.append(None)

    # Find y range
    valid_y = [y for y in y_values if y is not None and not np.isnan(y) and not np.isinf(y)]
    if not valid_y:
        print("No valid points to plot.")
        return

    y_min, y_max = min(valid_y), max(valid_y)
    if y_min == y_max:
        y_min -= 1
        y_max += 1

    # Plot points
    for i, (x, y) in enumerate(zip(x_values, y_values)):
        if y is None or np.isnan(y) or np.isinf(y):
            continue

        # Map to grid coordinates
        col = int((i / len(x_values)) * width)
        row = int((1 - (y - y_min) / (y_max - y_min)) * (height - 1))

        if 0 <= row < height and 0 <= col < width:
            grid[row][col] = '*'

    # Add axes
    # Y-axis
    if x_min <= 0 <= x_max:
        y_axis_col = int((-x_min / (x_max - x_min)) * width)
        for row in range(height):
            if 0 <= y_axis_col < width:
                if grid[row][y_axis_col] == ' ':
                    grid[row][y_axis_col] = '│'

    # X-axis
    if y_min <= 0 <= y_max:
        x_axis_row = int((1 - (0 - y_min) / (y_max - y_min)) * (height - 1))
        for col in range(width):
            if 0 <= x_axis_row < height:
                if grid[x_axis_row][col] == ' ':
                    grid[x_axis_row][col] = '─'
                elif grid[x_axis_row][col] == '│':
                    grid[x_axis_row][col] = '┼'

    # Print grid
    print(f"  {y_max:8.2f} ┤")
    for i, row in enumerate(grid):
        if i == 0:
            print(f"           │{''.join(row)}")
        elif i == height - 1:
            print(f"  {y_min:8.2f} ┤{''.join(row)}")
        else:
            print(f"           │{''.join(row)}")

    print(f"           └{'─' * width}")
    print(f"           {x_min:^{width//2}.2f}{x_max:^{width//2}.2f}")

def _plot_multiple_functions():
    """Plot multiple functions on same graph."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📈 Multiple Function Plot")

    functions = []
    print(f"\n{BOLD}Enter functions to plot (empty to finish):{RESET}")
    while len(functions) < 5:
        func = input(f"Function {len(functions)+1}: ").strip()
        if not func:
            break
        functions.append(func)

    if not functions:
        print("No functions entered.")
        input("\nPress Enter...")
        return

    print(f"\n{BOLD}Plotting {len(functions)} function(s)...{RESET}")
    for i, f in enumerate(functions, 1):
        print(f"  {i}. f(x) = {f}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to continue... ]{RESET}")

def _plot_parametric():
    """Plot parametric equations."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📈 Parametric Plot")

    print(f"\n{BOLD}Enter parametric equations:{RESET}")
    print(f"Example: x(t) = cos(t), y(t) = sin(t) for a circle")

    x_func = input(f"x(t) = ").strip()
    y_func = input(f"y(t) = ").strip()

    if not x_func or not y_func:
        print("Both functions required.")
        input("\nPress Enter...")
        return

    print(f"\nParametric plot: x(t) = {x_func}, y(t) = {y_func}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _plot_polar():
    """Plot polar equations."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📈 Polar Plot")

    print(f"\n{BOLD}Enter polar equation:{RESET}")
    print(f"Example: r = 1 + sin(theta) for cardioid")

    r_func = input(f"r(θ) = ").strip()

    if not r_func:
        print("No function entered.")
        input("\nPress Enter...")
        return

    print(f"\nPolar plot: r(θ) = {r_func}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _plot_3d_surface():
    """Plot 3D surface in ASCII."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📈 3D Surface Plot (ASCII)")

    print(f"\n{BOLD}Enter function of two variables:{RESET}")
    print(f"Example: sin(x) * cos(y), x**2 + y**2")

    func = input(f"f(x,y) = ").strip()

    if not func:
        print("No function entered.")
        input("\nPress Enter...")
        return

    print(f"\n3D plot: f(x,y) = {func}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _calc_scientific():
    """Scientific calculator with all standard functions."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🧮 Scientific Calculator")

    print(f"\n{BOLD}Calculator Mode (type 'help' for commands, 'exit' to quit):{RESET}")
    print(f"Available: +, -, *, /, **, sqrt, sin, cos, tan, log, ln, exp, abs, etc.\n")

    history = []

    while True:
        try:
            expr = input(f"{COLORS['6'][0]}>>> {RESET}").strip()

            if expr.lower() == 'exit':
                break
            elif expr.lower() == 'help':
                _print_calc_help()
                continue
            elif expr.lower() == 'history':
                print(f"\n{BOLD}Calculation History:{RESET}")
                for i, h in enumerate(history[-10:], 1):
                    print(f"  {i}. {h}")
                continue
            elif expr.lower() == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                print_header("🧮 Scientific Calculator")
                continue
            elif not expr:
                continue

            # Evaluate expression safely
            result = _safe_eval_math(expr)
            print(f"{COLORS['2'][0]}  = {result}{RESET}")
            history.append(f"{expr} = {result}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"{COLORS['1'][0]}Error: {e}{RESET}")

    # Save history option
    if history:
        save = input(f"\n{BOLD}Save calculation history? (y/n): {RESET}").strip().lower()
        if save == 'y':
            hist_text = "\n".join(history)
            save_log_file("general", "Calculator_History", hist_text, prompt_user=False)
            print(f"{COLORS['2'][0]}✅ History saved{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _safe_eval_math(expr):
    """Safely evaluate mathematical expression."""
    import math

    # Replace common functions
    expr = expr.replace('^', '**')
    expr = expr.replace('ln', 'log')

    # Safe namespace
    safe_dict = {
        '__builtins__': {},
        'abs': abs, 'round': round,
        'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
        'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
        'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh,
        'exp': math.exp, 'log': math.log, 'log10': math.log10,
        'sqrt': math.sqrt, 'pow': pow,
        'pi': math.pi, 'e': math.e,
        'ceil': math.ceil, 'floor': math.floor,
        'degrees': math.degrees, 'radians': math.radians,
        'factorial': math.factorial,
        'gcd': math.gcd if hasattr(math, 'gcd') else lambda a, b: a
    }

    result = eval(expr, safe_dict)
    return result

def _print_calc_help():
    """Print calculator help."""
    print(f"\n{BOLD}Calculator Commands:{RESET}")
    print(f"  Basic: +, -, *, /, ** (power)")
    print(f"  Trig: sin(x), cos(x), tan(x), asin(x), acos(x), atan(x)")
    print(f"  Hyp: sinh(x), cosh(x), tanh(x)")
    print(f"  Log: log(x), log10(x), exp(x)")
    print(f"  Other: sqrt(x), abs(x), round(x), factorial(x)")
    print(f"  Constants: pi, e")
    print(f"  Angles: degrees(x), radians(x)")
    print(f"  Special: history, clear, exit\n")

def _calc_cas_system():
    """Computer Algebra System for symbolic math."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🔬 CAS - Computer Algebra System", extra_info="| Symbolic Math")

    print(f"\n{BOLD}CAS Operations:{RESET}")
    print(f" {BOLD}[1]{RESET} Expand Expression")
    print(f" {BOLD}[2]{RESET} Factor Expression")
    print(f" {BOLD}[3]{RESET} Simplify Expression")
    print(f" {BOLD}[4]{RESET} Solve Equation")
    print(f" {BOLD}[5]{RESET} Differentiate")
    print(f" {BOLD}[6]{RESET} Integrate")
    print(f" {BOLD}[7]{RESET} Limit")
    print(f" {BOLD}[8]{RESET} Series Expansion")
    print(f" {BOLD}[0]{RESET} Return")

    choice = input(f"\n{BOLD}Select: {RESET}").strip()

    try:
        # Check if sympy is available
        try:
            import sympy as sp
            has_sympy = True
        except ImportError:
            has_sympy = False
            print(f"\n{COLORS['4'][0]}⚠️ SymPy not installed. Install with: pip install sympy{RESET}")
            print(f"Using basic symbolic math...\n")

        if choice == '1':
            expr = input(f"\nExpression to expand: ").strip()
            if has_sympy:
                x, y = sp.symbols('x y')
                result = sp.expand(expr)
                print(f"\n{COLORS['2'][0]}Expanded: {result}{RESET}")
            else:
                print(f"Result: {expr} (SymPy required for full CAS)")

        elif choice == '2':
            expr = input(f"\nExpression to factor: ").strip()
            if has_sympy:
                x = sp.symbols('x')
                result = sp.factor(expr)
                print(f"\n{COLORS['2'][0]}Factored: {result}{RESET}")
            else:
                print(f"Result: {expr} (SymPy required for full CAS)")

        elif choice == '3':
            expr = input(f"\nExpression to simplify: ").strip()
            if has_sympy:
                result = sp.simplify(expr)
                print(f"\n{COLORS['2'][0]}Simplified: {result}{RESET}")
            else:
                print(f"Result: {expr} (SymPy required for full CAS)")

        elif choice == '4':
            eq = input(f"\nEquation to solve (e.g., x**2 - 4): ").strip()
            var = input(f"Variable (default x): ").strip() or 'x'
            if has_sympy:
                x = sp.Symbol(var)
                solutions = sp.solve(eq, x)
                print(f"\n{COLORS['2'][0]}Solutions: {solutions}{RESET}")
            else:
                print(f"Equation: {eq} = 0 (SymPy required for solving)")

        elif choice == '5':
            expr = input(f"\nExpression to differentiate: ").strip()
            var = input(f"Variable (default x): ").strip() or 'x'
            if has_sympy:
                x = sp.Symbol(var)
                derivative = sp.diff(expr, x)
                print(f"\n{COLORS['2'][0]}d/d{var}: {derivative}{RESET}")
            else:
                print(f"d({expr})/d{var} (SymPy required)")

        elif choice == '6':
            expr = input(f"\nExpression to integrate: ").strip()
            var = input(f"Variable (default x): ").strip() or 'x'
            if has_sympy:
                x = sp.Symbol(var)
                integral = sp.integrate(expr, x)
                print(f"\n{COLORS['2'][0]}∫ {expr} d{var} = {integral} + C{RESET}")
            else:
                print(f"∫ {expr} d{var} (SymPy required)")

        elif choice == '7':
            expr = input(f"\nExpression: ").strip()
            var = input(f"Variable (default x): ").strip() or 'x'
            point = input(f"Limit as {var} approaches: ").strip()
            if has_sympy:
                x = sp.Symbol(var)
                limit = sp.limit(expr, x, point)
                print(f"\n{COLORS['2'][0]}lim({expr}) as {var}→{point} = {limit}{RESET}")
            else:
                print(f"lim({expr}) as {var}→{point} (SymPy required)")

        elif choice == '8':
            expr = input(f"\nExpression: ").strip()
            var = input(f"Variable (default x): ").strip() or 'x'
            point = input(f"Expansion point (default 0): ").strip() or '0'
            order = input(f"Order (default 6): ").strip() or '6'
            if has_sympy:
                x = sp.Symbol(var)
                series = sp.series(expr, x, float(point), int(order))
                print(f"\n{COLORS['2'][0]}Series: {series}{RESET}")
            else:
                print(f"Series expansion of {expr} (SymPy required)")

    except Exception as e:
        print(f"\n{COLORS['1'][0]}Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _calc_statistics():
    """Statistical analysis functions."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📊 Statistics & Data Analysis")

    print(f"\n{BOLD}Enter data values (space or comma separated):{RESET}")
    data_str = input(f"Data: ").strip()

    if not data_str:
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return

    try:
        # Parse data
        data = [float(x.strip()) for x in data_str.replace(',', ' ').split()]

        if not data:
            print("No valid data entered.")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
            return

        # Calculate statistics
        import math
        n = len(data)
        mean = sum(data) / n
        sorted_data = sorted(data)
        median = sorted_data[n//2] if n % 2 == 1 else (sorted_data[n//2-1] + sorted_data[n//2]) / 2

        # Mode (simple version)
        from collections import Counter
        counts = Counter(data)
        mode_val = counts.most_common(1)[0][0] if counts else None

        # Variance and standard deviation
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = math.sqrt(variance)

        # Range
        data_range = max(data) - min(data)

        # Display results
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📊 Statistical Analysis Results")

        print(f"\n{BOLD}Descriptive Statistics:{RESET}")
        print(f"  Count:        {n}")
        print(f"  Mean:         {mean:.6f}")
        print(f"  Median:       {median:.6f}")
        print(f"  Mode:         {mode_val}")
        print(f"  Std Dev:      {std_dev:.6f}")
        print(f"  Variance:     {variance:.6f}")
        print(f"  Range:        {data_range:.6f}")
        print(f"  Min:          {min(data):.6f}")
        print(f"  Max:          {max(data):.6f}")

        # Quartiles
        q1_idx = n // 4
        q3_idx = 3 * n // 4
        q1 = sorted_data[q1_idx]
        q3 = sorted_data[q3_idx]
        iqr = q3 - q1

        print(f"\n{BOLD}Quartiles:{RESET}")
        print(f"  Q1 (25%):     {q1:.6f}")
        print(f"  Q2 (50%):     {median:.6f}")
        print(f"  Q3 (75%):     {q3:.6f}")
        print(f"  IQR:          {iqr:.6f}")

        # Simple histogram
        print(f"\n{BOLD}Distribution (5 bins):{RESET}")
        bins = 5
        bin_width = data_range / bins
        for i in range(bins):
            bin_min = min(data) + i * bin_width
            bin_max = bin_min + bin_width
            count = sum(1 for x in data if bin_min <= x < bin_max or (i == bins-1 and x == bin_max))
            bar = '█' * int(count / n * 50)
            print(f"  [{bin_min:6.2f} - {bin_max:6.2f}): {bar} ({count})")

        # Save option
        save = input(f"\n{BOLD}Save analysis? (y/n): {RESET}").strip().lower()
        if save == 'y':
            report = f"Data: {data_str}\n\n"
            report += f"Count: {n}\nMean: {mean}\nMedian: {median}\nStd Dev: {std_dev}\n"
            save_log_file("general", "Statistical_Analysis", report, prompt_user=False)
            print(f"{COLORS['2'][0]}✅ Analysis saved{RESET}")

    except Exception as e:
        print(f"\n{COLORS['1'][0]}Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _calc_matrix():
    """Matrix calculator operations."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🔢 Matrix Calculator")

    print(f"\n{BOLD}Matrix Operations:{RESET}")
    print(f" {BOLD}[1]{RESET} Add Matrices")
    print(f" {BOLD}[2]{RESET} Multiply Matrices")
    print(f" {BOLD}[3]{RESET} Transpose Matrix")
    print(f" {BOLD}[4]{RESET} Determinant")
    print(f" {BOLD}[5]{RESET} Inverse Matrix")
    print(f" {BOLD}[6]{RESET} Eigenvalues")
    print(f" {BOLD}[0]{RESET} Return")

    choice = input(f"\n{BOLD}Select: {RESET}").strip()

    if choice == '0':
        return

    print(f"\n{COLORS['4'][0]}Matrix operations require NumPy.{RESET}")
    print(f"Basic matrix arithmetic available; install numpy for full features.")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _calc_equation_solver():
    """Solve various types of equations."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("⚖️ Equation Solver")

    print(f"\n{BOLD}Equation Types:{RESET}")
    print(f" {BOLD}[1]{RESET} Linear Equation (ax + b = 0)")
    print(f" {BOLD}[2]{RESET} Quadratic Equation (ax² + bx + c = 0)")
    print(f" {BOLD}[3]{RESET} System of Linear Equations")
    print(f" {BOLD}[4]{RESET} General Equation (Symbolic)")
    print(f" {BOLD}[0]{RESET} Return")

    choice = input(f"\n{BOLD}Select: {RESET}").strip()

    if choice == '1':
        _solve_linear()
    elif choice == '2':
        _solve_quadratic()
    elif choice == '3':
        _solve_system()
    elif choice == '4':
        _solve_general()

def _solve_linear():
    """Solve linear equation ax + b = 0."""
    print(f"\n{BOLD}Linear Equation: ax + b = 0{RESET}")
    try:
        a = float(input("Coefficient a: ").strip())
        b = float(input("Coefficient b: ").strip())

        if a == 0:
            if b == 0:
                result = "Infinite solutions (any x)"
            else:
                result = "No solution"
        else:
            x = -b / a
            result = f"x = {x:.6f}"

        print(f"\n{COLORS['2'][0]}{result}{RESET}")
    except Exception as e:
        print(f"\n{COLORS['1'][0]}Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter... ]{RESET}")

def _solve_quadratic():
    """Solve quadratic equation ax² + bx + c = 0."""
    print(f"\n{BOLD}Quadratic Equation: ax² + bx + c = 0{RESET}")
    try:
        import math
        a = float(input("Coefficient a: ").strip())
        b = float(input("Coefficient b: ").strip())
        c = float(input("Coefficient c: ").strip())

        if a == 0:
            print("Not a quadratic equation (a cannot be 0)")
        else:
            discriminant = b**2 - 4*a*c

            print(f"\n{BOLD}Discriminant: {discriminant:.6f}{RESET}")

            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                x2 = (-b - math.sqrt(discriminant)) / (2*a)
                print(f"{COLORS['2'][0]}Two real solutions:{RESET}")
                print(f"  x₁ = {x1:.6f}")
                print(f"  x₂ = {x2:.6f}")
            elif discriminant == 0:
                x = -b / (2*a)
                print(f"{COLORS['2'][0]}One real solution:{RESET}")
                print(f"  x = {x:.6f}")
            else:
                real = -b / (2*a)
                imag = math.sqrt(-discriminant) / (2*a)
                print(f"{COLORS['2'][0]}Two complex solutions:{RESET}")
                print(f"  x₁ = {real:.6f} + {imag:.6f}i")
                print(f"  x₂ = {real:.6f} - {imag:.6f}i")
    except Exception as e:
        print(f"\n{COLORS['1'][0]}Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter... ]{RESET}")

def _solve_system():
    """Solve system of linear equations."""
    print(f"\n{COLORS['4'][0]}System solver requires NumPy for matrix operations.{RESET}")
    print(f"Install with: pip install numpy")
    input(f"\n{BOLD}[ ⌨️ Press Enter... ]{RESET}")

def _solve_general():
    """Solve general equation symbolically."""
    print(f"\n{COLORS['4'][0]}General equation solver requires SymPy.{RESET}")
    print(f"Install with: pip install sympy")
    input(f"\n{BOLD}[ ⌨️ Press Enter... ]{RESET}")

def _calc_unit_converter():
    """Unit conversion calculator."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🔄 Unit Converter")

    units = {
        'Length': {'m': 1, 'km': 1000, 'cm': 0.01, 'mm': 0.001, 'mi': 1609.34, 'ft': 0.3048, 'in': 0.0254},
        'Mass': {'kg': 1, 'g': 0.001, 'mg': 0.000001, 'lb': 0.453592, 'oz': 0.0283495},
        'Temperature': {'C': 0, 'F': 1, 'K': 2},  # Special handling
        'Time': {'s': 1, 'min': 60, 'hr': 3600, 'day': 86400},
        'Area': {'m2': 1, 'km2': 1000000, 'cm2': 0.0001, 'ft2': 0.092903, 'acre': 4046.86},
        'Volume': {'L': 1, 'mL': 0.001, 'gal': 3.78541, 'qt': 0.946353, 'cup': 0.236588},
        'Speed': {'m/s': 1, 'km/h': 0.277778, 'mph': 0.44704, 'knot': 0.514444}
    }

    print(f"\n{BOLD}Categories:{RESET}")
    for i, cat in enumerate(units.keys(), 1):
        print(f" {BOLD}[{i}]{RESET} {cat}")

    try:
        cat_idx = int(input(f"\n{BOLD}Select category: {RESET}").strip())
        category = list(units.keys())[cat_idx - 1]

        print(f"\n{BOLD}Available units:{RESET} {', '.join(units[category].keys())}")

        value = float(input(f"Value: ").strip())
        from_unit = input(f"From unit: ").strip()
        to_unit = input(f"To unit: ").strip()

        if category == 'Temperature':
            result = _convert_temperature(value, from_unit, to_unit)
        else:
            if from_unit not in units[category] or to_unit not in units[category]:
                print("Invalid units!")
                input(f"\n{BOLD}[ ⌨️ Press Enter... ]{RESET}")
                return

            # Convert to base unit, then to target
            base_value = value * units[category][from_unit]
            result = base_value / units[category][to_unit]

        print(f"\n{COLORS['2'][0]}{value} {from_unit} = {result:.6f} {to_unit}{RESET}")

    except Exception as e:
        print(f"\n{COLORS['1'][0]}Error: {e}{RESET}")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _convert_temperature(value, from_unit, to_unit):
    """Convert temperature between C, F, and K."""
    # Convert to Celsius first
    if from_unit.upper() == 'C':
        celsius = value
    elif from_unit.upper() == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit.upper() == 'K':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid temperature unit")

    # Convert from Celsius to target
    if to_unit.upper() == 'C':
        return celsius
    elif to_unit.upper() == 'F':
        return celsius * 9/5 + 32
    elif to_unit.upper() == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid temperature unit")

def _calc_save_load():
    """Save and load calculations."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("💾 Save/Load Calculations")

    print(f"\n{BOLD}This feature saves calculations to the database log system.{RESET}")
    print(f"View saved calculations in: Database & Log Center → View Log Files → General")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _calc_help():
    """Display calculator help and examples."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📖 Graphing Calculator Help")

    print(f"\n{BOLD}Quick Start Guide:{RESET}\n")

    print(f"{BOLD}1. Graph Plotter:{RESET}")
    print(f"   - Plot functions like sin(x), x**2, exp(-x**2)")
    print(f"   - Supports ASCII terminal rendering")
    print(f"   - Multiple functions on one graph")
    print(f"   - Parametric and polar plots\n")

    print(f"{BOLD}2. Scientific Calculator:{RESET}")
    print(f"   - All standard math functions")
    print(f"   - Trigonometry: sin, cos, tan (radians)")
    print(f"   - Logarithms: log (natural), log10")
    print(f"   - Constants: pi, e")
    print(f"   - Type 'help' for full command list\n")

    print(f"{BOLD}3. CAS System:{RESET}")
    print(f"   - Symbolic math with SymPy")
    print(f"   - Expand, factor, simplify")
    print(f"   - Calculus: derivatives, integrals, limits")
    print(f"   - Series expansions")
    print(f"   - Requires: pip install sympy\n")

    print(f"{BOLD}4. Statistics:{RESET}")
    print(f"   - Descriptive statistics")
    print(f"   - Mean, median, mode, std dev")
    print(f"   - Quartiles and distribution")
    print(f"   - Simple histograms\n")

    print(f"{BOLD}5. Equation Solver:{RESET}")
    print(f"   - Linear equations")
    print(f"   - Quadratic equations (real & complex)")
    print(f"   - Systems of equations (with NumPy)\n")

    print(f"{BOLD}6. Unit Converter:{RESET}")
    print(f"   - Length, mass, temperature")
    print(f"   - Time, area, volume, speed")
    print(f"   - Common units supported\n")

    print(f"{BOLD}Examples:{RESET}")
    print(f"   Graph: f(x) = sin(x)*exp(-x/10)")
    print(f"   Calc: sqrt(2)**2")
    print(f"   CAS: (x+y)**3 → expand")
    print(f"   Stats: 1, 2, 3, 4, 5 → analyze")

    input(f"\n{BOLD}[ ⌨️ Press Enter to return to calculator... ]{RESET}")

# ================================================================================
# END GRAPHING CALCULATOR SECTION
# ================================================================================

# ==============================================================================
# SECTION 14B: TEXT & DOC CENTER
# ==============================================================================

DOC_EXTENSIONS = {
    ".txt": "Plain Text",
    ".log": "Plain Text",
    ".md": "Plain Text",
    ".conf": "WireGuard",
    ".wg": "WireGuard",
    ".ini": "Plain Text",
    ".cfg": "Plain Text",
    ".json": "Plain Text",
    ".yaml": "Plain Text",
    ".yml": "Plain Text",
    ".pdf": "PDF",
    ".doc": "Word",
    ".docx": "Word",
    ".epub": "E-Book",
    ".mobi": "E-Book",
    ".csv": "CSV",
    ".tsv": "CSV",
    ".xlsx": "Excel",
    ".xls": "Excel",
}

def _format_bytes(num):
    try:
        size = float(num)
    except (TypeError, ValueError):
        return "N/A"
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"

def _ensure_doc_library_dir():
    os.makedirs(DOC_LIBRARY_DIR, exist_ok=True)

def _doc_type_for_path(path):
    ext = os.path.splitext(path)[1].lower()
    return DOC_EXTENSIONS.get(ext)

def _scan_doc_library(base_dir=DB_DIR):
    docs = []
    for root, _, files in os.walk(base_dir):
        for name in files:
            ext = os.path.splitext(name)[1].lower()
            doc_type = DOC_EXTENSIONS.get(ext)
            if not doc_type:
                continue
            path = os.path.join(root, name)
            try:
                stat = os.stat(path)
                docs.append({
                    "path": path,
                    "name": name,
                    "ext": ext,
                    "type": doc_type,
                    "size": stat.st_size,
                    "mtime": stat.st_mtime,
                })
                track_file(path, file_type=doc_type, metadata={"extension": ext})
            except Exception:
                continue
    docs.sort(key=lambda d: d.get("mtime", 0), reverse=True)
    return docs

def _get_doc_index(force=False):
    if not force:
        cached = get_cached_data("doc_index")
        if cached:
            return cached
    docs = _scan_doc_library(DB_DIR)
    cache_data("doc_index", docs, expire_minutes=15)
    return docs

def _print_text_paged(title, text, page_lines=24):
    lines = text.splitlines() if text else ["(empty)"]
    page = 0
    max_pages = max(1, (len(lines) - 1) // page_lines + 1)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header(f"📄 {title}")
        start = page * page_lines
        end = start + page_lines
        for line in lines[start:end]:
            print(line[:200])
        print(f"\nPage {page + 1}/{max_pages}  [N]ext  [P]rev  [B]ack")
        cmd = input("Select: ").strip().lower()
        if cmd == 'b':
            break
        if cmd == 'n' and page + 1 < max_pages:
            page += 1
            continue
        if cmd == 'p' and page > 0:
            page -= 1

def _limit_text(text, max_chars=20000):
    if not text:
        return ""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n... [truncated]"

def _read_text_file(path):
    for enc in ("utf-8", "utf-16", "latin-1"):
        try:
            with open(path, "r", encoding=enc, errors="replace") as f:
                return f.read(), None
        except Exception:
            continue
    return None, "Unsupported text encoding"

def _strip_html(html):
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text("\n")
        return text if isinstance(text, str) else str(text)
    except Exception:
        return re.sub(r"<[^>]+>", " ", html)

def _read_pdf(path):
    try:
        fitz = importlib.import_module("fitz")
        doc = fitz.open(path)
        parts = []
        for i, page in enumerate(doc):
            if i >= 50:
                parts.append("\n... [page limit reached]\n")
                break
            parts.append(page.get_text())
        return "\n".join(parts), None
    except Exception:
        try:
            PyPDF2 = importlib.import_module("PyPDF2")
            reader = PyPDF2.PdfReader(path)
            parts = []
            for i, page in enumerate(reader.pages):
                if i >= 50:
                    parts.append("\n... [page limit reached]\n")
                    break
                parts.append(page.extract_text() or "")
            return "\n".join(parts), None
        except Exception:
            return None, "Install 'pymupdf' or 'PyPDF2' to read PDFs"

def _pandoc_to_text(path, output_format="markdown"):
    if not shutil.which("pandoc"):
        return None, "Install 'pandoc' for formatted Word rendering"
    try:
        result = subprocess.run(
            ["pandoc", "-t", output_format, path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        if result.returncode != 0:
            return None, result.stderr.strip() or "Pandoc conversion failed"
        return result.stdout, None
    except Exception:
        return None, "Pandoc conversion failed"

def _read_doc(path):
    antiword = shutil.which("antiword")
    if antiword:
        try:
            result = subprocess.run(
                [antiword, path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout, None
        except Exception:
            pass
    catdoc = shutil.which("catdoc")
    if catdoc:
        try:
            result = subprocess.run(
                [catdoc, path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout, None
        except Exception:
            pass
    if doc_word_render_mode == "plain":
        return None, "Install 'antiword' or 'catdoc' for .doc (plain mode)"
    return _pandoc_to_text(path)

def _read_docx(path):
    if doc_word_render_mode != "plain":
        text, err = _pandoc_to_text(path)
        if text:
            return text, None
    try:
        docx = importlib.import_module("docx")
        doc = docx.Document(path)
        lines = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(lines), None
    except Exception:
        if doc_word_render_mode == "plain":
            return None, "Install 'python-docx' to read .docx (plain mode)"
        return None, "Install 'pandoc' or 'python-docx' to read .docx"

def _read_epub(path):
    try:
        ebooklib = importlib.import_module("ebooklib")
        epub = importlib.import_module("ebooklib.epub")
        book = epub.read_epub(path)
        parts = []
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content = item.get_content().decode("utf-8", errors="ignore")
            parts.append(_strip_html(content))
        return "\n".join(parts), None
    except Exception:
        return None, "Install 'ebooklib' to read .epub"

def _read_mobi(path):
    try:
        textract = importlib.import_module("textract")
        text = textract.process(path).decode("utf-8", errors="ignore")
        return text, None
    except Exception:
        pass
    try:
        mobi = importlib.import_module("mobi")
        if hasattr(mobi, "extract"):
            with tempfile.TemporaryDirectory() as tmp:
                mobi.extract(path, tmp)
                for root, _, files in os.walk(tmp):
                    for name in files:
                        if name.lower().endswith((".html", ".htm", ".txt")):
                            full_path = os.path.join(root, name)
                            data, _ = _read_text_file(full_path)
                            if data:
                                return data, None
    except Exception:
        pass
    return None, "Install 'textract' or 'mobi' to read .mobi"

def _read_csv(path, delimiter=None):
    rows = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            if delimiter is None:
                sample = f.read(2048)
                f.seek(0)
                try:
                    delimiter = csv.Sniffer().sniff(sample).delimiter
                except Exception:
                    delimiter = ','
            reader = csv.reader(f, delimiter=delimiter)
            for i, row in enumerate(reader):
                rows.append(row)
                if i >= 50:
                    break
        return rows, None
    except Exception:
        return None, "Unable to read CSV file"

def _read_excel(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".xlsx":
        try:
            openpyxl = importlib.import_module("openpyxl")
            wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
            sheet = wb.active
            rows = []
            for i, row in enumerate(sheet.iter_rows(values_only=True)):
                rows.append(["" if v is None else str(v) for v in row])
                if i >= 50:
                    break
            return rows, None
        except Exception:
            return None, "Install 'openpyxl' to read .xlsx"
    try:
        xlrd = importlib.import_module("xlrd")
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_index(0)
        rows = []
        for r in range(min(sheet.nrows, 50)):
            rows.append([str(cell.value) for cell in sheet.row(r)])
        return rows, None
    except Exception:
        return None, "Install 'xlrd' to read .xls"

def _render_table(rows, max_cols=8, max_width=20):
    if not rows:
        return "(empty)"
    trimmed = [row[:max_cols] for row in rows]
    widths = [0] * max_cols
    for row in trimmed:
        for i, cell in enumerate(row):
            cell_str = str(cell)
            widths[i] = min(max(widths[i], len(cell_str)), max_width)
    lines = []
    for row in trimmed:
        padded = []
        for i in range(max_cols):
            cell = str(row[i]) if i < len(row) else ""
            cell = textwrap.shorten(cell, width=max_width, placeholder="...")
            padded.append(cell.ljust(widths[i]))
        lines.append(" | ".join(padded).rstrip())
    return "\n".join(lines)

def _open_document(path):
    if not os.path.exists(path):
        print(f"{COLORS['1'][0]}❌ File not found: {path}{RESET}")
        input("Press Enter to continue...")
        return
    doc_type = _doc_type_for_path(path)
    if not doc_type:
        print(f"{COLORS['1'][0]}❌ Unsupported file type{RESET}")
        input("Press Enter to continue...")
        return
    ext = os.path.splitext(path)[1].lower()
    text = None
    err = None
    if ext in (".txt", ".log", ".md", ".conf", ".wg", ".ini", ".cfg", ".json", ".yaml", ".yml"):
        track_file(path, file_type=doc_type, metadata={"extension": ext, "source": "text_doc_center"})
        _view_file_auto(path)
        return
    elif ext == ".pdf":
        text, err = _read_pdf(path)
    elif ext == ".doc":
        text, err = _read_doc(path)
    elif ext == ".docx":
        text, err = _read_docx(path)
    elif ext == ".epub":
        text, err = _read_epub(path)
    elif ext == ".mobi":
        text, err = _read_mobi(path)
    elif ext in (".csv", ".tsv"):
        delimiter = '\t' if ext == ".tsv" else None
        rows, err = _read_csv(path, delimiter=delimiter)
        if rows is not None:
            text = _render_table(rows)
    elif ext in (".xlsx", ".xls"):
        rows, err = _read_excel(path)
        if rows is not None:
            text = _render_table(rows)
    if err:
        print(f"{COLORS['4'][0]}⚠️ {err}{RESET}")
        input("Press Enter to continue...")
        return
    text = _limit_text(text)
    track_file(path, file_type=doc_type, metadata={"extension": ext, "source": "text_doc_center"})
    _print_text_paged(os.path.basename(path), text)

def _doc_browse_menu():
    docs = _get_doc_index(force=False)
    page = 0
    page_size = 12
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📚 Text & Doc Library")
        if not docs:
            print(f"\n{COLORS['4'][0]}No documents found in pythonOS_data.{RESET}")
            print("\n[R]efresh  [B]ack")
            cmd = input("Select: ").strip().lower()
            if cmd == 'r':
                docs = _get_doc_index(force=True)
                continue
            if cmd == 'b':
                break
            continue
        total_pages = max(1, (len(docs) - 1) // page_size + 1)
        start = page * page_size
        end = start + page_size
        page_items = docs[start:end]
        print(f"\n{BOLD}Page {page + 1}/{total_pages} | Files: {len(docs)}{RESET}")
        for idx, item in enumerate(page_items, 1):
            size = _format_bytes(item.get("size"))
            print(f" {idx}. [{item['type']}] {item['name']} ({size})")
        print("\n[N]ext  [P]rev  [O]pen <num>  [R]efresh  [B]ack")
        cmd = input("Select: ").strip().lower()
        if cmd == 'b':
            break
        if cmd == 'n' and end < len(docs):
            page += 1
            continue
        if cmd == 'p' and page > 0:
            page -= 1
            continue
        if cmd == 'r':
            docs = _get_doc_index(force=True)
            page = 0
            continue
        if cmd.startswith('o'):
            num = cmd[1:].strip() or input("Open number: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(page_items):
                    _open_document(page_items[idx]["path"])

def _doc_search_menu():
    query = input("Search filename: ").strip().lower()
    if not query:
        return
    docs = _get_doc_index(force=False)
    matches = [d for d in docs if query in d["name"].lower()]
    if not matches:
        print(f"{COLORS['4'][0]}No matches found.{RESET}")
        input("Press Enter to continue...")
        return
    page = 0
    page_size = 10
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🔎 Search Results")
        total_pages = max(1, (len(matches) - 1) // page_size + 1)
        start = page * page_size
        end = start + page_size
        page_items = matches[start:end]
        print(f"\n{BOLD}Page {page + 1}/{total_pages} | Matches: {len(matches)}{RESET}")
        for idx, item in enumerate(page_items, 1):
            size = _format_bytes(item.get("size"))
            print(f" {idx}. [{item['type']}] {item['name']} ({size})")
        print("\n[N]ext  [P]rev  [O]pen <num>  [B]ack")
        cmd = input("Select: ").strip().lower()
        if cmd == 'b':
            break
        if cmd == 'n' and end < len(matches):
            page += 1
            continue
        if cmd == 'p' and page > 0:
            page -= 1
            continue
        if cmd.startswith('o'):
            num = cmd[1:].strip() or input("Open number: ").strip()
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(page_items):
                    _open_document(page_items[idx]["path"])

def _doc_import_menu():
    _ensure_doc_library_dir()
    path = input("Enter file path to import: ").strip()
    if not path:
        return
    if not os.path.exists(path):
        print(f"{COLORS['1'][0]}❌ File not found.{RESET}")
        input("Press Enter to continue...")
        return
    ext = os.path.splitext(path)[1].lower()
    if ext not in DOC_EXTENSIONS:
        print(f"{COLORS['4'][0]}⚠️ Unsupported extension. Try txt/pdf/docx/epub/mobi/csv/xlsx.{RESET}")
        input("Press Enter to continue...")
        return
    dest = os.path.join(DOC_LIBRARY_DIR, os.path.basename(path))
    try:
        shutil.copy2(path, dest)
        track_file(dest, file_type=DOC_EXTENSIONS.get(ext), metadata={"extension": ext, "source": "import"})
        print(f"{COLORS['2'][0]}✅ Imported: {dest}{RESET}")
        cache_data("doc_index", _scan_doc_library(DB_DIR), expire_minutes=15)
    except Exception as e:
        print(f"{COLORS['1'][0]}❌ Import failed: {e}{RESET}")
    input("Press Enter to continue...")

def _doc_stats_menu():
    docs = _get_doc_index(force=False)
    counts = {}
    for item in docs:
        counts[item["type"]] = counts.get(item["type"], 0) + 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("📊 Document Library Stats")
    print(f"\n{BOLD}Total Documents: {len(docs)}{RESET}")
    for key, val in sorted(counts.items()):
        print(f"  {key}: {val}")
    print(f"\nLibrary Path: {DOC_LIBRARY_DIR}")
    input("Press Enter to continue...")

def _detect_tts_command():
    os_key = _detect_os_key()
    if os_key == "macos" and shutil.which("say"):
        return ["say"]
    if os_key == "windows":
        return ["powershell", "-NoProfile", "-Command"]
    if shutil.which("spd-say"):
        return ["spd-say"]
    if shutil.which("espeak"):
        return ["espeak"]
    if os_key == "android" and shutil.which("termux-tts-speak"):
        return ["termux-tts-speak"]
    return None

def _run_system_viewer(path):
    if os.name == 'nt':
        return subprocess.call(["cmd", "/c", "type", path])
    if shutil.which("less"):
        return subprocess.call(["less", path])
    if shutil.which("more"):
        return subprocess.call(["more", path])
    return subprocess.call(["cat", path])

def _is_long_text(path, size_threshold=65536):
    try:
        return os.path.getsize(path) >= size_threshold
    except Exception:
        return False

def _view_file_auto(path):
    if not os.path.exists(path):
        print(f"{COLORS['1'][0]}❌ File not found: {path}{RESET}")
        input("Press Enter to continue...")
        return
    if os.name != 'nt' and shutil.which("less") and _is_long_text(path):
        subprocess.call(["less", path])
        return
    if os.name == 'nt':
        try:
            if _is_long_text(path):
                text, err = _read_text_file(path)
                if err:
                    print(f"{COLORS['4'][0]}⚠️ {err}{RESET}")
                    input("Press Enter to continue...")
                    return
                _print_text_paged(os.path.basename(path), text)
                return
            subprocess.call(["cmd", "/c", "type", path])
            return
        except Exception:
            pass
    if shutil.which("more"):
        subprocess.call(["more", path])
        return
    if shutil.which("cat"):
        subprocess.call(["cat", path])
        return
    text, err = _read_text_file(path)
    if err:
        print(f"{COLORS['4'][0]}⚠️ {err}{RESET}")
        input("Press Enter to continue...")
        return
    _print_text_paged(os.path.basename(path), text)

def _run_system_editor(path):
    if os.name == 'nt':
        return subprocess.call(["notepad", path])
    for editor in ("nano", "vim", "vi", "emacs"):
        if shutil.which(editor):
            return subprocess.call([editor, path])
    return None

def _read_aloud_text(path):
    cmd = _detect_tts_command()
    if not cmd:
        print(f"{COLORS['4'][0]}⚠️ No TTS engine detected. Install one (espeak/spd-say/say/termux-tts).{RESET}")
        input("Press Enter to continue...")
        return
    text, err = _read_text_file(path)
    if err:
        print(f"{COLORS['4'][0]}⚠️ {err}{RESET}")
        input("Press Enter to continue...")
        return
    if os.name == 'nt':
        safe_text = text.replace('"', '""')
        ps = (
            "Add-Type -AssemblyName System.Speech; "
            "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer; "
            f"$s.Speak(\"{safe_text}\");"
        )
        subprocess.call(cmd + [ps])
    else:
        subprocess.call(cmd + [text])

def feature_text_doc_center():
    """Text & Document viewing center (terminal-based)."""
    global doc_word_render_mode
    _ensure_doc_library_dir()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📝 Text & Doc Center")
        print(f"\n{BOLD}Library:{RESET} {DOC_LIBRARY_DIR}")
        print(f"{BOLD}Word Render:{RESET} {doc_word_render_mode}")
        print(f" {BOLD}[1]{RESET} 📚 Browse Library (pythonOS_data)")
        print(f" {BOLD}[2]{RESET} 🔎 Search Library")
        print(f" {BOLD}[3]{RESET} 📂 Open by Path")
        print(f" {BOLD}[4]{RESET} 📥 Import into Library")
        print(f" {BOLD}[5]{RESET} 🔄 Refresh Index")
        print(f" {BOLD}[6]{RESET} 📊 Library Stats")
        print(f" {BOLD}[7]{RESET} 📝 Word Render Mode (pandoc/plain)")
        print(f" {BOLD}[8]{RESET} 👁️  View with System Tool (cat/less/more)")
        print(f" {BOLD}[9]{RESET} ✏️  Edit with System Tool (nano/vim/etc)")
        print(f" {BOLD}[10]{RESET} 🔊 Read Aloud (TTS)")
        print(f" {BOLD}[0]{RESET} ↩️  Return to Command Center")
        choice = input(f"\n{BOLD}🎯 Select option: {RESET}").strip()
        if choice == '0':
            break
        if choice == '1':
            _doc_browse_menu()
        elif choice == '2':
            _doc_search_menu()
        elif choice == '3':
            path = input("Enter full path: ").strip()
            if path:
                _open_document(path)
        elif choice == '4':
            _doc_import_menu()
        elif choice == '5':
            _get_doc_index(force=True)
            print(f"{COLORS['2'][0]}✅ Index refreshed.{RESET}")
            input("Press Enter to continue...")
        elif choice == '6':
            _doc_stats_menu()
        elif choice == '7':
            doc_word_render_mode = "plain" if doc_word_render_mode == "pandoc" else "pandoc"
            _update_user_config(doc_word_render_mode=doc_word_render_mode)
            print(f"{COLORS['2'][0]}✅ Word render mode: {doc_word_render_mode}{RESET}")
            input("Press Enter to continue...")
        elif choice == '8':
            path = input("Enter file path to view: ").strip()
            if path:
                _view_file_auto(path)
        elif choice == '9':
            path = input("Enter file path to edit: ").strip()
            if path:
                res = _run_system_editor(path)
                if res is None:
                    print(f"{COLORS['4'][0]}⚠️ No terminal editor found (nano/vim/emacs).{RESET}")
                    input("Press Enter to continue...")
        elif choice == '10':
            path = input("Enter file path to read aloud: ").strip()
            if path:
                _read_aloud_text(path)

def feature_latency_probe():
    def _ping_target(host):
        param = '-n' if os.name == 'nt' else '-c'
        output = subprocess.check_output(['ping', param, '4', host]).decode()
        print(output)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("⏱️ Latency & Geo Probe")
        print(f" {BOLD}[1]{RESET} 🌍 Geo + Ping")
        print(f" {BOLD}[2]{RESET} 🧭 Traceroute")
        print(f" {BOLD}[3]{RESET} 🧪 DNS Lookup")
        print(f" {BOLD}[4]{RESET} 🔌 TCP Connect Timing")
        print(f" {BOLD}[0]{RESET} ↩️  Return")
        choice = input("\nSelect option: ").strip()

        if choice == '0':
            return
        target = input("⌨️ Enter IP or Domain: ").strip()
        if not target:
            continue

        if choice == '1':
            print_header("🌍 Geo + Ping")
            try:
                geo_res = requests.get(f"http://ip-api.com/json/{target}", timeout=5).json()
                if geo_res.get('status') == 'success':
                    print(f" {BOLD}📍 Location:{RESET} {geo_res.get('city')}, {geo_res.get('country')} ({geo_res.get('isp')})")
                print(f"📡 Running Ping...")
                _ping_target(target)
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ✅ Probe Finished. Press Enter... ]{RESET}")
        elif choice == '2':
            print_header("🧭 Traceroute")
            cmd = "tracert" if os.name == 'nt' else "traceroute"
            if shutil.which(cmd):
                os.system(f"{cmd} {target}")
            else:
                print(f"❌ {cmd} not available.")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '3':
            print_header("🧪 DNS Lookup")
            try:
                ip = socket.gethostbyname(target)
                print(f"Resolved {target} -> {ip}")
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        elif choice == '4':
            print_header("🔌 TCP Connect Timing")
            port = input("Port [80]: ").strip() or "80"
            try:
                port_num = int(port)
                start = time.time()
                with socket.create_connection((target, port_num), timeout=3):
                    elapsed_ms = (time.time() - start) * 1000
                print(f"Connected in {elapsed_ms:.1f} ms")
            except Exception as e:
                print(f"❌ Error: {e}")
            input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

# -------------------------------
# PLUGIN SYSTEM (DROP-IN SCRIPTS)
# -------------------------------

import importlib.util
import glob

PLUGINS = {}

def load_plugins():
    """Load all .py files inside /plugins folder."""
    global PLUGINS
    PLUGINS = {}

    plugins_dir = os.path.join(os.path.dirname(__file__), "plugins")
    if not os.path.isdir(plugins_dir):
        return

    for path in glob.glob(os.path.join(plugins_dir, "*.py")):
        name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(name, path)
        if not spec:
            continue
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            if hasattr(module, "run"):
                PLUGINS[name] = module
        except Exception as e:
            print(f"[🔌 Plugin Error] {name}: {e}")
            try:
                log_to_database("general", f"Plugin_Load_{name}", str(e), status="error")
            except Exception:
                pass

def _build_plugin_context(sandboxed):
    context = {
        "psutil": psutil,
        "socket": socket,
        "print_header": print_header,
        "COLORS": COLORS,
        "BOLD": BOLD,
        "RESET": RESET,
        "time": time,
        "datetime": datetime,
    }
    if not sandboxed:
        context.update({
            "os": os,
            "requests": requests,
            "subprocess": subprocess,
        })
    return context

def feature_plugin_center():
    load_plugins()
    print_header("🔌 Plugin Center")

    if not PLUGINS:
        print("📂 No plugins found. Create a 'plugins' folder and add .py files with a run(context) function.")
        input("\n[ ⌨️ Press Enter to return... ]")
        return

    print("🧩 Available Plugins:\n")
    for i, name in enumerate(PLUGINS.keys(), start=1):
        print(f"[{i}] {name}")

    choice = input("\n🎯 Select plugin number (or Enter to cancel): ").strip()
    if not choice.isdigit():
        return

    idx = int(choice) - 1
    if idx < 0 or idx >= len(PLUGINS):
        return

    plugin_name = list(PLUGINS.keys())[idx]
    plugin = PLUGINS[plugin_name]

    print_header(f"🚀 Running Plugin: {plugin_name}")

    sandbox_choice = input("\nRun in sandbox mode? (Y/n): ").strip().lower()
    sandboxed = sandbox_choice != 'n'
    if sandboxed:
        print("🧪 Sandbox: limited context only (not full isolation).")

    context = _build_plugin_context(sandboxed)

    start_time = time.perf_counter()
    status = "success"
    error_text = None

    try:
        plugin.run(context)
    except Exception as e:
        status = "error"
        error_text = traceback.format_exc()
        print(f"[💥 Plugin Runtime Error] {e}")

    runtime_s = time.perf_counter() - start_time
    try:
        log_data = f"sandboxed={sandboxed} runtime_s={runtime_s:.3f}"
        if error_text:
            error_payload = f"{log_data}\n{error_text}"
            file_path = save_log_file("general", f"Plugin_{plugin_name}_Error", error_payload, prompt_user=False)
            log_to_database("general", f"Plugin_{plugin_name}", error_payload, file_path=file_path, status="error")
        else:
            log_to_database("general", f"Plugin_{plugin_name}", log_data, status="success")
    except Exception:
        pass

    input("\n[ ⌨️ Press Enter to return... ]")

# ========================================
# REMOTE SYSTEM DASHBOARD (SIMPLE HTTP)
# Duplicates display to browser with auto-refresh
# ========================================

from http.server import BaseHTTPRequestHandler, HTTPServer

DASHBOARD_PORT = 8088
dashboard_server = None
dashboard_display_cache = ""
WEBSSH_URL = os.environ.get("WEBSSH_URL", "http://localhost:8888")
WEBSSH_TARGET_HOST = os.environ.get("WEBSSH_TARGET_HOST", "")
WEBSSH_TARGET_PORT = os.environ.get("WEBSSH_TARGET_PORT", "")
WEBSSH_TARGET_USER = os.environ.get("WEBSSH_TARGET_USER", "")

def _webssh_is_installed():
    return shutil.which("wssh") is not None or shutil.which("webssh") is not None

def _webssh_parse_url(url):
    try:
        return urlparse(url)
    except Exception:
        return None

def _webssh_host_port(parsed):
    if not parsed:
        return "localhost", 80
    host = parsed.hostname or "localhost"
    if parsed.port:
        port = parsed.port
    elif parsed.scheme == "https":
        port = 443
    else:
        port = 80
    return host, port

def _webssh_is_running(host, port, timeout=0.6):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

def _webssh_url_for_client(url, ip_addr):
    parsed = _webssh_parse_url(url)
    if not parsed:
        return url
    host, port = _webssh_host_port(parsed)
    if host in ("localhost", "127.0.0.1") and ip_addr not in ("", "Unknown", None):
        netloc = f"{ip_addr}:{port}" if port else ip_addr
        return parsed._replace(netloc=netloc).geturl()
    return url

def _webssh_build_connect_url(base_url, ssh_host, ssh_port, ssh_user):
    parsed = _webssh_parse_url(base_url)
    if not parsed:
        return base_url
    query = parse_qs(parsed.query)
    if ssh_host:
        query["hostname"] = [ssh_host]
    if ssh_port:
        query["port"] = [str(ssh_port)]
    if ssh_user:
        query["username"] = [ssh_user]
    new_query = urlencode({k: v[-1] for k, v in query.items()}, doseq=True)
    return parsed._replace(query=new_query).geturl()

def _webssh_status(ip_addr):
    parsed = _webssh_parse_url(WEBSSH_URL)
    host, port = _webssh_host_port(parsed)
    installed = _webssh_is_installed()
    running = _webssh_is_running(host, port)
    error = ""
    if not installed:
        error = "WebSSH not installed (pip install webssh)."
    elif not running:
        error = f"WebSSH not running on {host}:{port}."
    client_url = _webssh_url_for_client(WEBSSH_URL, ip_addr)
    ssh_host = WEBSSH_TARGET_HOST or (ip_addr if ip_addr not in ("", "Unknown", None) else "")
    ssh_port = WEBSSH_TARGET_PORT or "22"
    try:
        ssh_user = WEBSSH_TARGET_USER or getpass.getuser()
    except Exception:
        ssh_user = WEBSSH_TARGET_USER
    connect_url = _webssh_build_connect_url(client_url, ssh_host, ssh_port, ssh_user)
    return {
        "installed": installed,
        "running": running,
        "error": error,
        "client_url": client_url,
        "connect_url": connect_url,
        "host": host,
        "port": port,
    }

def get_dashboard_stats():
    """Collect system statistics"""
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    cpu = psutil.cpu_percent(interval=0.2)
    net = psutil.net_io_counters()
    gpu, fan = get_advanced_hardware_stats()
    battery = psutil.sensors_battery()
    hostname = socket.gethostname()
    try:
        ip_addr = socket.gethostbyname(hostname)
    except Exception:
        ip_addr = "Unknown"
    try:
        load_avg = os.getloadavg()
    except Exception:
        load_avg = None
    try:
        temps = psutil.sensors_temperatures()
        temp_values = [e.current for entries in temps.values() for e in entries if e.current is not None]
        avg_temp = sum(temp_values) / len(temp_values) if temp_values else None
    except Exception:
        avg_temp = None
    try:
        proc_count = len(psutil.pids())
    except Exception:
        proc_count = 0
    db_stats = {}
    try:
        with _db_connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM log_entries")
            db_stats["logs"] = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM file_tracking")
            db_stats["files"] = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM swap_cache WHERE datetime(expires_at) > datetime('now')")
            db_stats["cache"] = cursor.fetchone()[0]
    except Exception:
        db_stats = {}

    webssh_status = _webssh_status(ip_addr)

    return {
        "cpu": cpu,
        "cpu_cores": psutil.cpu_count(logical=False) or 0,
        "cpu_threads": psutil.cpu_count(logical=True) or 0,
        "ram": mem.percent,
        "ram_total": mem.total / (1024**3),
        "ram_used": mem.used / (1024**3),
        "ram_avail": mem.available / (1024**3),
        "swap_percent": psutil.swap_memory().percent,
        "swap_total": psutil.swap_memory().total / (1024**3),
        "disk": disk.percent,
        "disk_total": disk.total / (1024**3),
        "disk_used": disk.used / (1024**3),
        "disk_free": disk.free / (1024**3),
        "net_sent": net.bytes_sent / (1024**2),
        "net_recv": net.bytes_recv / (1024**2),
        "net_packets_sent": net.packets_sent,
        "net_packets_recv": net.packets_recv,
        "gpu": gpu,
        "fan": fan,
        "weather": weather_cache,
        "battery": battery.percent if battery else 0,
        "battery_plugged": battery.power_plugged if battery else False,
        "hostname": hostname,
        "ip": ip_addr,
        "os": f"{platform.system()} {platform.release()}",
        "arch": platform.machine(),
        "python": platform.python_version(),
        "uptime": str(datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())).split('.')[0],
        "load_avg": load_avg,
        "avg_temp": avg_temp,
        "processes": proc_count,
        "db_stats": db_stats,
        "webssh_url": webssh_status["client_url"],
        "webssh_connect_url": webssh_status["connect_url"],
        "webssh_running": webssh_status["running"],
        "webssh_installed": webssh_status["installed"],
        "webssh_error": webssh_status["error"],
        "webssh_host": webssh_status["host"],
        "webssh_port": webssh_status["port"],
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

class DashboardHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

    def do_GET(self):
        """Serve dashboard with current stats"""
        stats = get_dashboard_stats()
        if self.path.startswith("/api/stats"):
            payload = json.dumps(stats).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(payload)
            return

        webssh_status_class = "status-ok" if stats["webssh_running"] else "status-bad"
        if not stats["webssh_installed"]:
            webssh_status_class = "status-warn"
        webssh_status_text = "RUNNING" if stats["webssh_running"] else "NOT RUNNING"
        if not stats["webssh_installed"]:
            webssh_status_text = "NOT INSTALLED"
        webssh_error = stats["webssh_error"]
        if webssh_error:
            webssh_error = f"<div class=\"mono status-bad\">{webssh_error}</div>"
        webssh_iframe = ""
        if stats["webssh_running"]:
            webssh_iframe = f"<iframe class=\"terminal-frame\" src=\"{stats['webssh_connect_url']}\"></iframe>"
        else:
            webssh_iframe = "<div class=\"mono\">WebSSH is not running. Start it and refresh.</div>"
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>pythonOS Dashboard</title>
            <meta http-equiv="refresh" content="2">
            <meta charset="utf-8">
            <style>
                body {{ background:#111; color:#0f0; font-family:monospace; padding:20px; }}
                .header {{ border-bottom:2px solid #0f0; padding:10px 0; margin-bottom:20px; }}
                h1 {{ color:#0f0; margin:0; }}
                .stats {{ display:grid; grid-template-columns:repeat(4, 1fr); gap:20px; margin-bottom:30px; }}
                .wide {{ grid-column: span 2; }}
                .mono {{ font-family:monospace; font-size:12px; color:#9ad; }}
                .stat-card {{ background:#1a1a1a; border:1px solid #0f0; padding:15px; }}
                .stat-label {{ color:#888; font-size:12px; margin-bottom:5px; }}
                .stat-value {{ color:#0f0; font-size:24px; font-weight:bold; }}
                .bar {{ background:#333; height:10px; margin:10px 0; border-radius:2px; overflow:hidden; }}
                .bar-fill {{ background:#0f0; height:10px; transition:width 0.3s; }}
                .timestamp {{ color:#888; font-size:12px; margin-top:20px; }}
                .terminal-frame {{ width:100%; height:220px; border:1px solid #0f0; background:#000; }}
                .status-ok {{ color:#0f0; }}
                .status-bad {{ color:#f55; }}
                .status-warn {{ color:#ff0; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🖥️ pythonOS Remote Dashboard</h1>
            </div>

            <div class="stats">
                <div class="stat-card wide">
                    <div class="stat-label">Host</div>
                    <div class="stat-value">{stats['hostname']} / {stats['ip']}</div>
                    <div class="mono">{stats['os']} | {stats['arch']}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Uptime</div>
                    <div class="stat-value">{stats['uptime']}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">CPU Usage</div>
                    <div class="stat-value">{stats['cpu']:.1f}%</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['cpu']}%"></div></div>
                    <div class="mono">Cores: {stats['cpu_cores']} | Threads: {stats['cpu_threads']}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">RAM Usage</div>
                    <div class="stat-value">{stats['ram']:.1f}%</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['ram']}%"></div></div>
                    <div class="mono">{stats['ram_used']:.2f} / {stats['ram_total']:.2f} GB</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Disk Usage</div>
                    <div class="stat-value">{stats['disk']:.1f}%</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['disk']}%"></div></div>
                    <div class="mono">{stats['disk_used']:.2f} / {stats['disk_total']:.2f} GB</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Free Space</div>
                    <div class="stat-value">{stats['disk_free']:.2f} GB</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Battery</div>
                    <div class="stat-value">{stats['battery']:.1f}% {'🔌' if stats['battery_plugged'] else '🔋'}</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['battery']}%"></div></div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">GPU</div>
                    <div class="stat-value">{stats['gpu']}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Swap</div>
                    <div class="stat-value">{stats['swap_percent']:.1f}%</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['swap_percent']}%"></div></div>
                    <div class="mono">{stats['swap_total']:.2f} GB</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Processes</div>
                    <div class="stat-value">{stats['processes']}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Python</div>
                    <div class="stat-value">{stats['python']}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Load Avg</div>
                    <div class="stat-value">{'' if stats['load_avg'] is None else f"{stats['load_avg'][0]:.2f} {stats['load_avg'][1]:.2f} {stats['load_avg'][2]:.2f}"}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Avg Temp</div>
                    <div class="stat-value">{'' if stats['avg_temp'] is None else f"{stats['avg_temp']:.1f}C"}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">DB Logs</div>
                    <div class="stat-value">{stats['db_stats'].get('logs', 0)}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">DB Tracked Files</div>
                    <div class="stat-value">{stats['db_stats'].get('files', 0)}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Active Cache</div>
                    <div class="stat-value">{stats['db_stats'].get('cache', 0)}</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Web Terminal (WebSSH)</div>
                    <div class="mono">Service: <span class="{webssh_status_class}">{webssh_status_text}</span></div>
                    <div class="mono">URL: {stats['webssh_url']}</div>
                    {webssh_error}
                    {webssh_iframe}
                </div>
            </div>

            <div style="border-top:1px solid #0f0; padding-top:15px;">
                <p>📡 Net Sent: {stats['net_sent']:.2f} MB</p>
                <p>⬇️ Net Recv: {stats['net_recv']:.2f} MB</p>
                <p>📦 Packets: {stats['net_packets_sent']} sent / {stats['net_packets_recv']} recv</p>
                <p>🌡️ Weather: {stats['weather'].get('icon','')} {stats['weather'].get('temp','N/A')}</p>
                <p>🌀 Fan: {stats['fan']}</p>
            </div>

            <div style="border-top:1px solid #0f0; padding-top:15px;">
                <h3>Command Execution (Local)</h3>
                <p class="mono">Note: commands run on the host where pythonOS is running.</p>
                <form method="POST" action="/cmd">
                    <input type="text" name="cmd" style="width:80%; padding:6px;" placeholder="e.g. ls -la" />
                    <button type="submit" style="padding:6px 12px;">Run</button>
                </form>
            </div>

            <div style="border-top:1px solid #0f0; padding-top:15px;">
                <h3>WebSSH (Browser Terminal)</h3>
                <p class="mono">For a full interactive terminal, consider WebSSH:</p>
                <p class="mono">https://github.com/huashengdun/webssh</p>
                <p class="mono">Run it separately, then connect to this host over SSH.</p>
                <p class="mono">JSON stats endpoint: /api/stats</p>
            </div>

            <div class="timestamp">Last update: {stats['timestamp']}</div>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        if self.path != "/cmd":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8", errors="ignore")
        params = {}
        for pair in body.split("&"):
            if "=" in pair:
                k, v = pair.split("=", 1)
                params[k] = v.replace("+", " ")
        cmd = params.get("cmd", "").strip()

        output = "No command provided."
        if cmd:
            try:
                import shlex
                args = shlex.split(cmd)
                result = subprocess.run(args, capture_output=True, text=True, timeout=10)
                output = (result.stdout + "\n" + result.stderr).strip() or "(no output)"
            except Exception as e:
                output = f"Error: {e}"

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Command Output</title>
            <style>
                body {{ background:#111; color:#0f0; font-family:monospace; padding:20px; }}
                pre {{ white-space:pre-wrap; word-wrap:break-word; background:#1a1a1a; padding:12px; border:1px solid #0f0; }}
                a {{ color:#9ad; }}
            </style>
        </head>
        <body>
            <h2>Command Output</h2>
            <pre>{output}</pre>
            <p><a href="/">Back to Dashboard</a></p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

def start_dashboard():
    """Start the HTTP server for dashboard"""
    global dashboard_server

    if dashboard_server is not None:
        return

    def run_server():
        global dashboard_server
        try:
            server = HTTPServer(("0.0.0.0", DASHBOARD_PORT), DashboardHandler)
            dashboard_server = server
            server.serve_forever()
        except Exception as e:
            print(f"[🖥️ Dashboard Error] {e}")

    threading.Thread(target=run_server, daemon=True).start()

def feature_remote_dashboard():
    """Launch remote dashboard feature"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("🖥️ Remote System Dashboard")
        print(f" {BOLD}[1]{RESET} 🚀 Start Dashboard")
        print(f" {BOLD}[2]{RESET} 🌐 Open Dashboard in Browser")
        print(f" {BOLD}[3]{RESET} 🧾 Show JSON Endpoint")
        print(f" {BOLD}[4]{RESET} 🧪 WebSSH Status")
        print(f" {BOLD}[0]{RESET} ↩️  Return")
        choice = input("\nSelect option: ").strip()

        hostname = socket.gethostname()
        try:
            ip = socket.gethostbyname(hostname)
        except Exception:
            ip = "localhost"
        dash_url = f"http://{ip}:{DASHBOARD_PORT}"

        if choice == '0':
            return
        if choice == '1':
            start_dashboard()
            print(f"📡 Dashboard running at: {COLORS['4'][0]}{dash_url}{RESET}")
            print(f"🌐 Open this in your browser on this network.")
            webssh_status = _webssh_status(ip)
            if not webssh_status["installed"]:
                print(f"⚠️  WebSSH not installed. {webssh_status['error']}")
            elif not webssh_status["running"]:
                print(f"⚠️  WebSSH not running. {webssh_status['error']}")
                print(f"    Expected at {webssh_status['host']}:{webssh_status['port']}")
            else:
                print(f"✅ WebSSH detected at {webssh_status['host']}:{webssh_status['port']}")
            input("\n[ ⌨️ Press Enter to return... ]")
        elif choice == '2':
            start_dashboard()
            _open_url(dash_url)
            input("\n[ ⌨️ Press Enter to return... ]")
        elif choice == '3':
            start_dashboard()
            print(f"JSON stats endpoint: {dash_url}/api/stats")
            input("\n[ ⌨️ Press Enter to return... ]")
        elif choice == '4':
            webssh_status = _webssh_status(ip)
            print_header("🧪 WebSSH Status")
            print(f"Installed: {webssh_status['installed']}")
            print(f"Running:   {webssh_status['running']}")
            print(f"Host:      {webssh_status['host']}:{webssh_status['port']}")
            if webssh_status["error"]:
                print(f"Error:     {webssh_status['error']}")
            print(f"URL:       {webssh_status['client_url']}")
            print(f"Connect:   {webssh_status['connect_url']}")
            input("\n[ ⌨️ Press Enter to return... ]")


def feature_media_menu():
    """Media Scanner sub-menu that exposes existing scanners
    and an option to launch the asciiplayer plugin if installed.
    """
    while True:
        print_header("🎞️ Media Scanner Menu")
        print(" [1] Internal Media Scanner (Default)")
        print(" [2] Integrated Media Scanner (Explorer)")
        print(" [3] Launch asciiplayer (plugins/asciiplayer18.py)")
        print(" [4] Launch External MP3 Engine (Linked Module)")
        print(" [5] Open Download Center (Media Tools)")
        print(" [6] Return to Main Menu")

        sel = input("\n🎯 Select: ").strip()
        if sel == '1':
            feature_media_scanner()
        elif sel == '2':
            try:
                feature_media_scanner_integrated()
            except NameError:
                print("[!] Integrated scanner not available in this build.")
                input("\n[ ⌨️ Press Enter to return... ]")
        elif sel == '3':
            # Launch the inlined asciiplayer runner
            try:
                asciiplayer_run()
            except NameError:
                print("[!] asciiplayer module not available.")
            except Exception as e:
                print(f"Error running asciiplayer: {e}")
            input("\n[ ⌨️ Press Enter to return... ]")
        elif sel == '4':
            try:
                feature_terminal_mp3_player()
            except NameError:
                print("[!] MP3 player not available.")
                input("\n[ ⌨️ Press Enter to return... ]")
        elif sel == '5':
            feature_download_center()
        else:
            break

# -----------------------------
# Inlined asciiplayer18 plugin
# -----------------------------
# The original plugin was adapted to be embedded and exposes
# a single entrypoint `asciiplayer_run()` that launches its menu.

try:
    # begin pasted asciiplayer18.py content
    import cv2
    import os as _asciip_os
    import sys as _asciip_sys
    import time as _asciip_time
    import threading as _asciip_threading
    import signal as _asciip_signal
    import json as _asciip_json
    import subprocess as _asciip_subprocess
    import shutil as _asciip_shutil
    import random as _asciip_random
    from pathlib import Path as _asciip_Path

    try:
        if _asciip_sys.stdout.encoding and _asciip_sys.stdout.encoding.lower() != 'utf-8':
            _asciip_sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        try:
            import codecs as _asciip_codecs
            if hasattr(_asciip_sys.stdout, 'detach'):
                _asciip_sys.stdout = _asciip_codecs.getwriter("utf-8")(_asciip_sys.stdout.detach())
        except Exception:
            pass

    try:
        from ffpyplayer.player import MediaPlayer as _asciip_MediaPlayer
        _ASCIIP_AUDIO_SUPPORT = True
    except Exception:
        _ASCIIP_AUDIO_SUPPORT = False

    _ASCIIP_EXTERNAL_AUDIO = bool(
        _asciip_shutil.which('ffplay') or
        _asciip_shutil.which('mpv') or
        _asciip_shutil.which('mplayer')
    )

    _ASCIIP_PLAY_SFX = True
    _ASCIIP_SOUND_DIR = _asciip_Path("sounds")

    def _asciip_play_sound(filename: str = None):
        if not _ASCIIP_PLAY_SFX:
            return

        def _do_play(path):
            try:
                import simpleaudio as sa
                try:
                    wave_obj = sa.WaveObject.from_wave_file(str(path))
                    wave_obj.play()
                    return
                except Exception:
                    pass
            except Exception:
                pass

            if _asciip_shutil.which('ffplay'):
                _asciip_subprocess.Popen(['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', str(path)],
                                         stdout=_asciip_subprocess.DEVNULL, stderr=_asciip_subprocess.DEVNULL)
            elif _asciip_shutil.which('aplay'):
                _asciip_subprocess.Popen(['aplay', str(path)], stdout=_asciip_subprocess.DEVNULL, stderr=_asciip_subprocess.DEVNULL)
            elif _asciip_shutil.which('paplay'):
                _asciip_subprocess.Popen(['paplay', str(path)], stdout=_asciip_subprocess.DEVNULL, stderr=_asciip_subprocess.DEVNULL)
            else:
                try:
                    _asciip_sys.stdout.write('\a')
                    _asciip_sys.stdout.flush()
                except Exception:
                    pass

        if filename:
            p = _asciip_Path(filename)
            if not p.exists() and _ASCIIP_SOUND_DIR.exists():
                p = _ASCIIP_SOUND_DIR / filename
            if p.exists():
                _asciip_threading.Thread(target=_do_play, args=(p,), daemon=True).start()
                return

        _asciip_threading.Thread(target=_do_play, args=(_asciip_Path('/dev/null'),), daemon=True).start()

    def _asciip_start_audio_process(video_path: str):
        cmd = None
        if _asciip_shutil.which('ffplay'):
            cmd = ['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', video_path]
        elif _asciip_shutil.which('mpv'):
            cmd = ['mpv', '--no-video', '--really-quiet', video_path]
        elif _asciip_shutil.which('mplayer'):
            cmd = ['mplayer', '-novideo', '-really-quiet', video_path]
        if not cmd:
            return None
        try:
            return _asciip_subprocess.Popen(cmd, stdout=_asciip_subprocess.DEVNULL, stderr=_asciip_subprocess.DEVNULL)
        except Exception:
            return None

    ASCII_STYLES = {
        "1": ("classic",  r" .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"),
        "2": ("dense",    r" .:-=+*#%@"),
        "3": ("blocks",   r" ░▒▓█"),
        "4": ("binary",   r" Ø1"),
        "5": ("minimal",  r" ·°¤"),
        "6": ("matrix",   r" ｦｱｳｴｵｶｷｹｺｻｼｽｾｿﾀﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ"),
        "7": ("tech",     r" ▰▱◸◹◺◿"),
        "8": ("braille",  r" ⠁⠃⠇⠏⠟⠿⡿⣿"),
        "9": ("math",     r" ∫∮∝∞√∑"),
        "10":("stars",    r" +*★☆"),
        "11":("slashes",  r" ╱╲╳"),
        "12":("impact",   r" .vV#M"),
        "13":("runic_nordic", r" ᚠᚡᚢᚣᚤᚥᚦᚧᚨᚩᚪᚫᚬᚭᚮᚯ"),
        "14":("runic_celtic", r"  ᚁᚂᚃᚄᚅᚆᚇᚈᚉᚊᚋᚌᚍᚎᚏ"),
        "15":("runic_mystic", r" ✡︎🔯☤☥☦︎☧☨☩☯︎☰☱☲☳☴☵☶☷"),
        "16":("runic_alchemy",r" 🜁🜂🜃🜄🜅🜆🜇🜈🜉🜊🜋🜌🜍🜎🜏"),
        "17":("runic_arcane", r" 𐏑𐏒𐏓𐏔𐏕𐏖𐏗𐏘𐏙𐏚𐏛𐏜𐏝𐏞𐏟"),
        "18":("chaos_glitch", "RANDOM_LOCAL"),
        "19":("emoji_only",   r" 🌑🌘🌗🌖🌕☀️"),
        "20":("chaos_global", "RANDOM_GLOBAL")
    }
    CURRENT_STYLE_KEY = "1"
    STATE_FILE = _asciip_Path("player_state.json")

    class _ASCIIP_PlaybackState:
        def __init__(self):
            self.paused = False
            self.seek_seconds = 0
            self.quit_to_menu = False
            self.volume = 1.0

    _ASCIIP_pb = _ASCIIP_PlaybackState()

    def _asciip_get_chaos_chars_local():
        chars = list(ASCII_STYLES["1"][1])
        _asciip_random.shuffle(chars)
        return " " + "".join(chars)

    def _asciip_get_chaos_chars_global():
        pool = "".join([v[1] for k, v in ASCII_STYLES.items() if "RANDOM" not in v[1]])
        char_list = list(pool.replace(" ", ""))
        _asciip_random.shuffle(char_list)
        return " " + "".join(char_list[:40])

    def _asciip_reset_terminal():
        try:
            _asciip_sys.stdout.write("\033[?25h\033[0m")
            if _asciip_os.name != 'nt':
                try: _asciip_os.system("stty sane")
                except: pass
            _asciip_sys.stdout.flush()
        except Exception:
            pass

    def _asciip_exit_handler(sig, frame):
        _asciip_reset_terminal()
        _asciip_sys.exit(0)

    try:
        _asciip_signal.signal(_asciip_signal.SIGINT, _asciip_exit_handler)
    except Exception:
        pass

    def _asciip_get_ansi_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"

    def _asciip_load_state():
        if STATE_FILE.exists():
            try: return _asciip_json.loads(STATE_FILE.read_text())
            except: pass
        return {"bookmarks": {}, "recent": []}

    def _asciip_save_state(state):
        try:
            STATE_FILE.write_text(_asciip_json.dumps(state, indent=2))
        except Exception:
            pass

    def _asciip_advanced_browser():
        global CURRENT_STYLE_KEY
        state = _asciip_load_state()
        current_path = _asciip_Path.cwd()
        valid_exts = (".mp4", ".mkv", ".avi", ".mov", ".flv")

        while True:
            _asciip_os.system('cls' if _asciip_os.name == 'nt' else 'clear')
            _asciip_reset_terminal()

            style_name = ASCII_STYLES[CURRENT_STYLE_KEY][0]
            audio_status = 'OK' if _ASCIIP_AUDIO_SUPPORT else ('EXT' if _ASCIIP_EXTERNAL_AUDIO else 'OFF')
            print(f"║ STYLE: {style_name.upper()} ({CURRENT_STYLE_KEY}/20) ║ AUDIO: {audio_status} ║")
            print(f"║ PATH: {current_path}")
            print("═" * 70)

            try:
                entries = sorted(list(current_path.iterdir()), key=lambda x: (not x.is_dir(), x.name.lower()))
                folders = [e for e in entries if e.is_dir()]
                files = [e for e in entries if e.is_file() and e.suffix.lower() in valid_exts]
            except PermissionError:
                print("!! Permission Denied !!")
                current_path = current_path.parent
                _asciip_time.sleep(1); continue

            for i, f in enumerate(folders): print(f"  [D{i}] {f.name}/")
            for i, f in enumerate(files):   print(f"  [F{i}] {f.name}")

            print("\nCommands:")
            print("  d<n> (Folder) | f<n> (Play) | up (Back) | home (User)")
            print("  style (Change Style) | $ <cmd> (Shell Bridge) | q (Exit)")

            cmd = input("\n>> ").strip().lower()

            if cmd == 'q': return
            if cmd == 'up': current_path = current_path.parent; continue
            if cmd == 'home': current_path = _asciip_Path.home(); continue

            if cmd == 'style':
                print("\nSelect Style by Number:")
                for k, v in sorted(ASCII_STYLES.items(), key=lambda x: int(x[0])):
                    print(f"  {k}) {v[0]}")
                s = input("\nEnter Number: ").strip()
                if s in ASCII_STYLES:
                    CURRENT_STYLE_KEY = s
                    print(f"Style set to {ASCII_STYLES[s][0]}!"); _asciip_time.sleep(0.5)
                continue

            if cmd.startswith('$ '):
                print(f"\n--- Running: {cmd[2:]} ---\n")
                _asciip_subprocess.run(cmd[2:], shell=True)
                input("\nPress Enter to return...")
                continue

            if cmd.startswith('d') and cmd[1:].isdigit():
                idx = int(cmd[1:])
                if idx < len(folders): current_path = folders[idx]; continue

            if (cmd.startswith('f') and cmd[1:].isdigit()) or cmd.isdigit():
                idx = int(cmd[1:]) if cmd.startswith('f') else int(cmd)
                if idx < len(files): return str(files[idx])

    def _asciip_play_video(video_path):
        pb = _ASCIIP_PlaybackState()
        cap = cv2.VideoCapture(video_path)
        player = _asciip_MediaPlayer(video_path) if _ASCIIP_AUDIO_SUPPORT else None
        audio_proc = None
        if not player:
            audio_proc = _asciip_start_audio_process(video_path)

        raw_style = ASCII_STYLES[CURRENT_STYLE_KEY][1]
        if raw_style == "RANDOM_GLOBAL":
            chars = list(_asciip_get_chaos_chars_global())
        elif raw_style == "RANDOM_LOCAL":
            chars = list(_asciip_get_chaos_chars_local())
        else:
            chars = list(raw_style)

        c_len = len(chars)

        def _input_thread():
            if _asciip_os.name == 'nt':
                import msvcrt
                while not pb.quit_to_menu:
                    if msvcrt.kbhit():
                        char = msvcrt.getch().decode('utf-8', errors='ignore').lower()
                        if char == ' ': pb.paused = not pb.paused
                        elif char == 'a': pb.seek_seconds = -5
                        elif char == 'd': pb.seek_seconds = 5
                        elif char == 'q': pb.quit_to_menu = True
                    _asciip_time.sleep(0.01)
            else:
                import tty, termios
                fd = _asciip_sys.stdin.fileno()
                old = termios.tcgetattr(fd)
                try:
                    tty.setcbreak(fd)
                    while not pb.quit_to_menu:
                        char = _asciip_sys.stdin.read(1).lower()
                        if char == ' ': pb.paused = not pb.paused
                        elif char == 'a': pb.seek_seconds = -5
                        elif char == 'd': pb.seek_seconds = 5
                        elif char == 'q': pb.quit_to_menu = True
                finally: termios.tcsetattr(fd, termios.TCSADRAIN, old)

        _asciip_threading.Thread(target=_input_thread, daemon=True).start()
        _asciip_sys.stdout.write("\033[?25l")

        try:
            while not pb.quit_to_menu:
                if pb.paused:
                    if player: player.set_pause(True)
                    _asciip_time.sleep(0.1); continue

                if player:
                    player.set_pause(False)
                    player.set_volume(pb.volume)

                if pb.seek_seconds != 0:
                    target = max(0, cap.get(cv2.CAP_PROP_POS_MSEC) + (pb.seek_seconds * 1000))
                    cap.set(cv2.CAP_PROP_POS_MSEC, target)
                    if player: player.seek(target / 1000.0, relative=False)
                    pb.seek_seconds = 0

                ret, frame = cap.read()
                if not ret: break

                if player:
                    audio_frame, val = player.get_frame()
                    if val == 'eof': break
                    elif val > 0: _asciip_time.sleep(val)
                else:
                    _asciip_time.sleep(0.02)

                try: cols, rows = _asciip_os.get_terminal_size()
                except: cols, rows = 80, 24
                img = cv2.resize(frame, (cols, rows - 1))
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                output = ["\033[H"]
                for y in range(img.shape[0]):
                    line = []
                    for x in range(img.shape[1]):
                        b, g, r = img[y, x]
                        char = chars[int((gray[y,x]/255) * (c_len-1))]
                        line.append(f"{_asciip_get_ansi_color(r, g, b)}{char}")
                    output.append("".join(line))

                _asciip_sys.stdout.write("\n".join(output))
                _asciip_sys.stdout.flush()

        finally:
            cap.release()
            try:
                if player: player.close_player()
            except Exception:
                pass
            try:
                if audio_proc:
                    audio_proc.terminate()
            except Exception:
                pass
            try:
                _asciip_sys.stdout.write("\033[?25h")
                _asciip_sys.stdout.flush()
            except Exception:
                pass
            _asciip_reset_terminal()

except Exception:
    # If inlining fails for any reason, provide a minimal stub
    def _asciip_advanced_browser():
        print("Ascii player features unavailable in this environment.")
        return None

    def _asciip_play_video(path):
        print("Ascii player playback unavailable.")

def asciiplayer_run():
    """Public entrypoint to run the inlined asciiplayer menu."""
    try:
        # prefer the main_menu flow if available
        try:
            selected = None
            while True:
                _asciip_os.system('cls' if _asciip_os.name == 'nt' else 'clear')
                print("=== ASCII CINEMA ULTIMATE (Embedded) ===")
                print("1) Choose Style | 2) Quick Play | 3) Advanced Browser | q) Exit")
                ch = input('\n>> ').strip().lower()
                if ch == '1':
                    print("\nSelect Style by Number:")
                    for k, v in sorted(ASCII_STYLES.items(), key=lambda x: int(x[0])):
                        print(f"  {k}) {v[0]}")
                    s = input('\nNumber: ').strip()
                    if s in ASCII_STYLES:
                        global CURRENT_STYLE_KEY
                        CURRENT_STYLE_KEY = s
                elif ch == '2':
                    vids = [f for f in _asciip_os.listdir('.') if f.endswith(('.mp4', '.mkv', '.avi'))]
                    for i, v in enumerate(vids): print(f"[{i}] {v}")
                    idx = input("Index: ")
                    if idx.isdigit() and int(idx) < len(vids):
                        try: _asciip_play_sound()
                        except: pass
                        _asciip_play_video(vids[int(idx)])
                elif ch == '3':
                    sel = _asciip_advanced_browser()
                    if sel:
                        try: _asciip_play_sound()
                        except: pass
                        _asciip_play_video(sel)
                elif ch == 'q':
                    break
        except Exception:
            # fallback: simple notice
            print("Ascii player embedded. Advanced features may be limited.")
            input("Press Enter to return...")
    finally:
        _asciip_reset_terminal()

# --- ENHANCED DISPLAY MODE (CURSES-BASED) ---

def _enhanced_curses_init(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_CYAN, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    curses.init_pair(3, curses.COLOR_YELLOW, -1)
    curses.init_pair(4, curses.COLOR_MAGENTA, -1)
    curses.init_pair(5, curses.COLOR_WHITE, -1)
    stdscr.nodelay(True)
    stdscr.keypad(True)
    try:
        curses.curs_set(0)
    except Exception:
        pass

def _enhanced_wrap_lines(text, width):
    if not text:
        return ["(empty)"]
    lines = []
    for raw in str(text).splitlines():
        if not raw:
            lines.append("")
            continue
        while len(raw) > width:
            lines.append(raw[:width])
            raw = raw[width:]
        lines.append(raw)
    return lines

def _enhanced_crop_lines(lines, width, height):
    cropped = []
    for line in lines[:height]:
        cropped.append(str(line)[:width])
    return cropped

def _enhanced_set_display_for_pane(state, title, text, pane_w, pane_h, wrap=True):
    width = max(10, pane_w)
    height = max(1, pane_h)
    if wrap:
        lines = _enhanced_wrap_lines(text, width)
    else:
        raw_lines = str(text).splitlines() if text else ["(empty)"]
        lines = _enhanced_crop_lines(raw_lines, width, height)
    if len(lines) > height:
        lines = lines[:height - 1] + ["..."]
    state["display_title"] = title
    state["display_lines"] = lines
    state["display_scroll"] = 0

def _enhanced_strip_ansi(text):
    if not text:
        return ""
    return re.sub(r"\x1b\[[0-9;]*m", "", text)

def _enhanced_set_display(state, title, text):
    state["display_title"] = title
    state["display_lines"] = _enhanced_wrap_lines(text, max(10, state["right_width"] - 2))
    state["display_scroll"] = 0

def _enhanced_left_lines():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    lines.append(f"Time: {now}")
    lines.append(f"OS: {platform.system()} {platform.release()}")
    lines.append(f"Node: {platform.node()}")
    lines.append(f"CPU: {psutil.cpu_percent(interval=None)}%  Cores: {psutil.cpu_count(logical=False)}")
    mem = psutil.virtual_memory()
    lines.append(f"RAM: {mem.percent}%  Free: {_format_gb(mem.available)}")
    disk = psutil.disk_usage('/')
    lines.append(f"Disk: {disk.percent}%  Free: {_format_gb(disk.free)}")
    net = psutil.net_io_counters()
    lines.append(f"Net: TX {_format_mb(net.bytes_sent)}  RX {_format_mb(net.bytes_recv)}")
    try:
        boot_str, uptime_str = _format_boot_info(psutil.boot_time())
        lines.append(f"Boot: {boot_str}")
        lines.append(f"Uptime: {uptime_str}")
    except Exception:
        pass
    if weather_cache:
        temp = weather_cache.get("temp", "N/A")
        icon = weather_cache.get("icon", "")
        humidity = weather_cache.get("humidity", "N/A")
        wind = weather_cache.get("wind", "N/A")
        lines.append(f"Weather: {icon} {temp}  Hum: {humidity}  Wind: {wind}")
    return lines

def _enhanced_render_left(win, lines):
    h, w = win.getmaxyx()
    win.erase()
    win.attron(curses.color_pair(1))
    win.box()
    win.addnstr(0, 2, " MAIN DISPLAY ", w - 4)
    for i, line in enumerate(lines[: h - 2]):
        win.addnstr(1 + i, 1, line, w - 2)
    win.noutrefresh()

def _enhanced_render_left_custom(win, title, lines, color_pair=1):
    h, w = win.getmaxyx()
    win.erase()
    win.attron(curses.color_pair(color_pair))
    win.box()
    win.addnstr(0, 2, f" {title} ", w - 4)
    for i, line in enumerate(lines[: h - 2]):
        win.addnstr(1 + i, 1, line, w - 2)
    win.noutrefresh()

def _enhanced_render_right(win, state):
    h, w = win.getmaxyx()
    win.erase()
    win.attron(curses.color_pair(3))
    win.box()
    title = state.get("display_title") or "DISPLAY"
    win.addnstr(0, 2, f" {title} ", w - 4)
    lines = state.get("display_lines") or ["(empty)"]
    scroll = state.get("display_scroll", 0)
    view = lines[scroll: scroll + (h - 2)]
    for i, line in enumerate(view):
        win.addnstr(1 + i, 1, line, w - 2)
    win.noutrefresh()

def _enhanced_set_submenu(state, title, lines):
    state["submenu_title"] = title
    state["submenu_lines"] = lines or ["(empty)"]

def _enhanced_render_bottom_split(left_win, right_win, input_buffer, menu_lines, state):
    lh, lw = left_win.getmaxyx()
    rh, rw = right_win.getmaxyx()

    left_win.erase()
    left_win.attron(curses.color_pair(2))
    left_win.box()
    left_win.addnstr(0, 2, " COMMAND CENTER (ENHANCED) ", lw - 4)
    for i, line in enumerate(menu_lines[: lh - 4]):
        left_win.addnstr(1 + i, 1, line, lw - 2)
    prompt = "CMD > "
    left_win.addnstr(lh - 2, 1, prompt, lw - 2)
    left_win.addnstr(lh - 2, 1 + len(prompt), input_buffer[-(lw - len(prompt) - 3):], lw - len(prompt) - 2)
    left_win.noutrefresh()

    right_win.erase()
    right_win.attron(curses.color_pair(4))
    right_win.box()
    sub_title = state.get("submenu_title") or "SUB MENU"
    right_win.addnstr(0, 2, f" {sub_title} ", rw - 4)
    sub_lines = state.get("submenu_lines") or ["(empty)"]
    for i, line in enumerate(sub_lines[: rh - 2]):
        right_win.addnstr(1 + i, 1, line, rw - 2)
    right_win.noutrefresh()

def _enhanced_prompt(stdscr, prompt):
    curses.echo(False)
    buffer = ""
    while True:
        h, w = stdscr.getmaxyx()
        stdscr.move(h - 2, 1)
        stdscr.clrtoeol()
        stdscr.addnstr(h - 2, 1, prompt, w - 2, curses.color_pair(2))
        stdscr.addnstr(h - 1, 1, buffer[-(w - 2):], w - 2, curses.color_pair(5))
        stdscr.refresh()
        key = stdscr.getch()
        if key in (10, 13):
            break
        if key in (27,):
            buffer = ""
            break
        if key in (curses.KEY_BACKSPACE, 127, 8):
            buffer = buffer[:-1]
            continue
        if 32 <= key <= 126:
            buffer += chr(key)
    return buffer.strip()

def _enhanced_run_fullscreen(stdscr, func, *args, **kwargs):
    try:
        curses.endwin()
    except Exception:
        pass
    try:
        func(*args, **kwargs)
    finally:
        try:
            _enhanced_curses_init(stdscr)
            stdscr.clear()
        except Exception:
            pass

def _enhanced_web_preview(stdscr, state):
    url = _enhanced_prompt(stdscr, "URL (blank to cancel): ")
    if not url:
        return
    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"http://{url}"
    try:
        resp = requests.get(url, timeout=8)
        text = _strip_html(resp.text)
        text = _limit_text(text, max_chars=15000)
        header = f"URL: {url}\nStatus: {resp.status_code}\n"
        _enhanced_set_display(state, "WEB PREVIEW", header + text)
    except Exception as e:
        _enhanced_set_display(state, "WEB PREVIEW", f"Error: {e}")

def _enhanced_doc_preview(stdscr, state):
    path = _enhanced_prompt(stdscr, "Document path (blank to cancel): ")
    if not path:
        return
    if not os.path.exists(path):
        _enhanced_set_display(state, "DOC PREVIEW", f"File not found: {path}")
        return
    ext = os.path.splitext(path)[1].lower()
    text = None
    err = None
    if ext in (".txt", ".log", ".md", ".conf", ".wg", ".ini", ".cfg", ".json", ".yaml", ".yml"):
        text, err = _read_text_file(path)
    elif ext == ".pdf":
        text, err = _read_pdf(path)
    elif ext == ".doc":
        text, err = _read_doc(path)
    elif ext == ".docx":
        text, err = _read_docx(path)
    elif ext == ".epub":
        text, err = _read_epub(path)
    elif ext == ".mobi":
        text, err = _read_mobi(path)
    elif ext in (".csv", ".tsv"):
        delimiter = '\t' if ext == ".tsv" else None
        rows, err = _read_csv(path, delimiter=delimiter)
        if rows is not None:
            text = _render_table(rows)
    elif ext in (".xlsx", ".xls"):
        rows, err = _read_excel(path)
        if rows is not None:
            text = _render_table(rows)
    else:
        err = "Unsupported file type"
    if err:
        _enhanced_set_display(state, "DOC PREVIEW", err)
        return
    text = _limit_text(text)
    _enhanced_set_display(state, f"DOC PREVIEW: {os.path.basename(path)}", text)

def _enhanced_media_preview(stdscr, state):
    base = _enhanced_prompt(stdscr, "Media directory (blank for cwd): ")
    if not base:
        base = os.getcwd()
    if not os.path.isdir(base):
        _enhanced_set_display(state, "MEDIA", f"Not a directory: {base}")
        return
    exts = (".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac", ".mp4", ".mkv", ".avi", ".mov")
    files = []
    for root, _, names in os.walk(base):
        for name in names:
            if name.lower().endswith(exts):
                files.append(os.path.join(root, name))
            if len(files) >= 50:
                break
        if len(files) >= 50:
            break
    if not files:
        _enhanced_set_display(state, "MEDIA", "No media files found.")
        return
    lines = [f"[{i}] {os.path.basename(p)}" for i, p in enumerate(files)]
    _enhanced_set_display(state, "MEDIA", "\n".join(lines))
    choice = _enhanced_prompt(stdscr, "Play full-screen index (blank to cancel): ")
    if not choice:
        return
    if not choice.isdigit() or int(choice) >= len(files):
        _enhanced_set_display(state, "MEDIA", "Invalid selection.")
        return
    path = files[int(choice)]
    ext = os.path.splitext(path)[1].lower()
    def _play_selected():
        if ext in (".mp4", ".mkv", ".avi", ".mov") and "_asciip_play_video" in globals():
            _asciip_play_video(path)
        else:
            feature_media_menu()
    _enhanced_run_fullscreen(stdscr, _play_selected)
    _enhanced_set_display(state, "MEDIA", f"Last played: {os.path.basename(path)}")

def _enhanced_process_summary(state):
    lines = []
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
        try:
            info = p.info
            procs.append(info)
        except Exception:
            continue
    procs.sort(key=lambda x: x.get('memory_percent') or 0, reverse=True)
    lines.append("Top processes by memory:")
    for p in procs[:10]:
        name = p.get('name') or 'unknown'
        mem = p.get('memory_percent') or 0
        cpu = p.get('cpu_percent') or 0
        lines.append(f"{p.get('pid')} {name}  MEM {mem:.1f}%  CPU {cpu:.1f}%")
    _enhanced_set_display(state, "PROCESSES", "\n".join(lines))

def _enhanced_disk_summary(state):
    disk = psutil.disk_usage('/')
    io = psutil.disk_io_counters()
    lines = [
        f"Total: {_format_gb(disk.total)}",
        f"Used: {_format_gb(disk.used)} ({disk.percent}%)",
        f"Free: {_format_gb(disk.free)}",
    ]
    if io:
        lines.append(f"Read: {_format_mb(io.read_bytes)}  Write: {_format_mb(io.write_bytes)}")
    _enhanced_set_display(state, "DISK", "\n".join(lines))

def _enhanced_network_summary(state):
    host = socket.gethostname()
    try:
        ip = socket.gethostbyname(host)
    except Exception:
        ip = "unknown"
    net = psutil.net_io_counters()
    lines = [
        f"Host: {host}",
        f"IP: {ip}",
        f"TX: {_format_mb(net.bytes_sent)}",
        f"RX: {_format_mb(net.bytes_recv)}",
        f"Packets TX: {net.packets_sent}",
        f"Packets RX: {net.packets_recv}",
    ]
    _enhanced_set_display(state, "NETWORK", "\n".join(lines))

class _EnhancedSatelliteSession:
    def __init__(self):
        self.qth = _satellite_default_qth()
        self.store = TLEStore()
        self.trails = {}
        self.targets = _satellite_targets_from_config(self.store)
        self.primary_target = self.targets[0] if self.targets else "0 LEMUR 1"
        self.health = self._initial_health()
        self.last_message = "Ready."
        self.map = MapRenderer()

    def _initial_health(self):
        if HAVE_PREDICT and HAVE_REQUESTS:
            return "OPTIMAL"
        if HAVE_PREDICT or HAVE_REQUESTS:
            return "DEGRADED"
        return "OFFLINE"

    def _health_icon(self):
        if self.health == "OPTIMAL":
            return "🟢"
        if self.health == "DEGRADED":
            return "🟡"
        return "🔴"

    def update_map_size(self, width, height):
        self.map = MapRenderer(width=width, height=height)

    def get_pos(self, tle, now):
        if HAVE_PREDICT:
            try:
                obs = predict.observe(tle, self.qth, at=now)
                lon = obs["longitude"]
                if lon < 0:
                    lon += 360
                return obs["latitude"], lon
            except Exception:
                pass

        try:
            l2 = tle.splitlines()[2]
            inc = float(l2[8:16])
            n = float(l2[52:63])
            period = 86400 / n
            theta = ((now % period) / period) * 2 * math.pi
            lat = inc * math.sin(theta)
            lon = (now / 240) % 360
            return lat, lon
        except Exception:
            return 0.0, 0.0

    def compute_positions(self, now):
        targets = [t for t in self.targets if self.store.get(t)]
        if not targets:
            targets = ["0 LEMUR 1"]
            self.targets = targets
            self.primary_target = "0 LEMUR 1"

        positions = {}
        for name in targets[:SAT_MAX_TARGETS]:
            tle = self.store.get(name)
            if not tle:
                continue
            lat, lon = self.get_pos(tle, now)
            positions[name] = (lat, lon)
            trail = self.trails.setdefault(name, deque(maxlen=TRAIL_LENGTH))
            trail.append((lat, lon))

        if self.primary_target not in targets:
            self.primary_target = targets[0]

        return targets, positions

    def _sync_targets(self):
        _update_user_config(sat_targets=self.targets[:SAT_MAX_TARGETS], sat_target=self.primary_target)

    def handle_command(self, cmd):
        cmd = cmd.strip().lower()
        if not cmd:
            return
        if cmd == "q":
            self.last_message = "Quit satellite view."
            return "quit"
        if cmd == "u":
            if self.store.update_from_celestrak():
                self.health = "OPTIMAL"
                self.last_message = "TLE update complete."
            else:
                self.last_message = "TLE update failed."
            return
        if cmd.startswith("s "):
            name = cmd[2:].strip()
            if self.store.get(name):
                if name not in self.targets:
                    if len(self.targets) < SAT_MAX_TARGETS:
                        self.targets.append(name)
                    else:
                        self.last_message = f"Max targets reached ({SAT_MAX_TARGETS})."
                        return
                self.primary_target = name
                _satellite_log_selection(name)
                self._sync_targets()
                self.last_message = f"Primary set: {name}."
            else:
                self.last_message = f"Unknown target: {name}."
            return
        if cmd.startswith("a "):
            name = cmd[2:].strip()
            if not self.store.get(name):
                self.last_message = f"Unknown target: {name}."
                return
            if name in self.targets:
                self.last_message = f"Already tracking: {name}."
                return
            if len(self.targets) >= SAT_MAX_TARGETS:
                self.last_message = f"Max targets reached ({SAT_MAX_TARGETS})."
                return
            self.targets.append(name)
            _satellite_log_selection(name)
            self._sync_targets()
            self.last_message = f"Added: {name}."
            return
        if cmd.startswith("r "):
            name = cmd[2:].strip()
            if name in self.targets:
                self.targets.remove(name)
                if self.primary_target == name:
                    self.primary_target = self.targets[0] if self.targets else "0 LEMUR 1"
                self._sync_targets()
                self.last_message = f"Removed: {name}."
            else:
                self.last_message = f"Not tracked: {name}."
            return
        self.last_message = "Unknown command."

def _enhanced_satellite_view(stdscr, state):
    session = _EnhancedSatelliteSession()
    input_buffer = ""
    last_frame = 0
    left_lines = ["Initializing satellite view..."]
    menu_lines = [
        "SAT COMMANDS:",
        "U Update TLEs",
        "S <name> Set Primary",
        "A <name> Add",
        "R <name> Remove",
        "Q Quit",
    ]

    while True:
        h, w = stdscr.getmaxyx()
        if h < 24 or w < 80:
            stdscr.erase()
            stdscr.addstr(0, 0, "Enlarge window for Enhanced Display Mode")
            stdscr.refresh()
            time.sleep(0.2)
            continue

        bottom_h = max(7, h // 3)
        top_h = h - bottom_h
        left_w = w // 2
        right_w = w - left_w
        bottom_left_w = max(20, w // 2)
        bottom_right_w = w - bottom_left_w

        left = curses.newwin(top_h, left_w, 0, 0)
        right = curses.newwin(top_h, right_w, 0, left_w)
        bottom_left = curses.newwin(bottom_h, bottom_left_w, top_h, 0)
        bottom_right = curses.newwin(bottom_h, bottom_right_w, top_h, bottom_left_w)

        now = time.time()
        if now - last_frame >= 1:
            session.update_map_size(max(20, right_w - 6), max(10, top_h - 2))
            targets, positions = session.compute_positions(now)

            earth_dist = (1.524 - 1.0) * AU_KM
            latency_min = (earth_dist / C_KMS) / 60
            marker_map = {name: SAT_MARKERS[i] for i, name in enumerate(targets[:SAT_MAX_TARGETS])}
            tracking_line = ", ".join([f"{marker_map.get(name, '?')}:{name}" for name in targets[:SAT_MAX_TARGETS]])

            lat = lon = None
            if session.primary_target in positions:
                lat, lon = positions[session.primary_target]
            tele_line = "TELEMETRY: N/A"
            if lat is not None and lon is not None:
                lat_suffix = "N" if lat >= 0 else "S"
                lon_suffix = "E" if lon >= 0 else "W"
                tele_line = f"TELEMETRY: {abs(lat):>6.2f}{lat_suffix}  {abs(lon):>7.2f}{lon_suffix}"

            left_lines = [
                f"== MARS BRIDGE STATUS: {session.health} {session._health_icon()} | TARGET: {session.primary_target} ==",
                f"MISSION CLOCK: {time.ctime(now)} UTC",
                f"EARTH DISTANCE: {earth_dist:,.0f} KM | LATENCY: {latency_min:.1f}m",
                f"SATELLITES IN MEMORY: {session.store.count()}",
                f"TRACKING (max {SAT_MAX_TARGETS}): {tracking_line}",
                "",
                tele_line,
                "[U] Update TLEs | [S <name>] Set Primary | [A <name>] Add | [R <name>] Remove | [Q] Quit",
                "(Type command and press Enter)",
            ]

            map_text = session.map.render_multi(session.trails, positions, marker_map=marker_map, primary_name=session.primary_target)
            map_text = _enhanced_strip_ansi(map_text)
            _enhanced_set_display_for_pane(state, "SAT MAP", map_text, right_w - 2, top_h - 2, wrap=False)

            _enhanced_set_submenu(state, "Satellite Menu", [
                f"Targets: {', '.join(targets[:SAT_MAX_TARGETS])}",
                f"Primary: {session.primary_target}",
                f"Last: {session.last_message}",
            ])

            last_frame = now

        _enhanced_render_left_custom(left, "SATELLITE STATUS", _enhanced_wrap_lines("\n".join(left_lines), max(10, left_w - 2)), color_pair=1)
        _enhanced_render_right(right, state)
        _enhanced_render_bottom_split(bottom_left, bottom_right, input_buffer, menu_lines, state)
        curses.doupdate()

        key = stdscr.getch()
        if key == -1:
            time.sleep(0.05)
            continue
        if key == 20:  # Ctrl+T
            _set_display_mode("classic")
            return
        if key in (curses.KEY_BACKSPACE, 127, 8):
            input_buffer = input_buffer[:-1]
            continue
        if key in (10, 13):
            cmd = input_buffer.strip()
            input_buffer = ""
            res = session.handle_command(cmd)
            if res == "quit":
                return
            continue
        if 32 <= key <= 126:
            input_buffer += chr(key)

def _enhanced_handle_choice(choice, stdscr, state):
    global is_blinking, temp_unit, truncated_thermal, mini_view
    if not choice:
        return
    choice = choice.strip().upper()
    _enhanced_set_submenu(state, f"Selected: {choice}", ["Launching..."])
    if choice == '1':
        _enhanced_set_submenu(state, "Blink", ["Toggle blinking text."])
        is_blinking = not is_blinking
        _update_user_config(is_blinking=is_blinking)
    elif choice == '2':
        _enhanced_set_submenu(state, "Temperature Unit", ["Toggle C/F."])
        temp_unit = "F" if temp_unit == "C" else "C"
        _update_user_config(temp_unit=temp_unit)
    elif choice == '3':
        _enhanced_set_submenu(state, "Thermal Mode", ["Toggle full/short thermal display."])
        truncated_thermal = not truncated_thermal
        _update_user_config(truncated_thermal=truncated_thermal)
    elif choice == '4':
        _enhanced_set_submenu(state, "Mini View", ["Toggle mini view display."])
        mini_view = not mini_view
        _update_user_config(mini_view=mini_view)
    elif choice == '5':
        _enhanced_set_submenu(state, "Exit", ["Return to classic Command Center."])
        _set_display_mode("classic")
        state["exit"] = True
    elif choice == '6':
        _enhanced_set_submenu(state, "Color Scheme", ["Pick a color theme."])
        _enhanced_run_fullscreen(stdscr, _select_color_scheme)
    elif choice == '7':
        _enhanced_set_submenu(state, "Web Preview", ["Enter a URL for the preview pane."])
        _enhanced_web_preview(stdscr, state)
    elif choice == '8':
        _enhanced_set_submenu(state, "Disk Summary", ["Show disk usage and IO summary."])
        _enhanced_disk_summary(state)
    elif choice == '9':
        _enhanced_set_submenu(state, "Process Summary", ["Show top processes by memory."])
        _enhanced_process_summary(state)
    elif choice == '0':
        _enhanced_set_submenu(state, "Network Summary", ["Show host, IP, and counters."])
        _enhanced_network_summary(state)
    elif choice == 'I':
        _enhanced_set_submenu(state, "Media", ["Scan for media files.", "Pick index to play full-screen."])
        _enhanced_media_preview(stdscr, state)
    elif choice == 'T':
        _enhanced_set_submenu(state, "Text & Doc", ["Enter a file path to preview."])
        _enhanced_doc_preview(stdscr, state)
    elif choice == 'A':
        _enhanced_set_submenu(state, "Security Audit", ["Run security audit (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_security_audit)
    elif choice == 'B':
        _enhanced_set_submenu(state, "Environment Probe", ["Run environment probe (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_environment_probe)
    elif choice == 'C':
        _enhanced_set_submenu(state, "Hardware Serials", ["Show hardware serials (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_hardware_serials)
    elif choice == 'D':
        _enhanced_set_submenu(state, "AI Probe", ["Run AI probe (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_deep_probe_ai)
    elif choice == 'E':
        _enhanced_set_submenu(state, "Calendar", ["Open calendar (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_simple_calendar)
    elif choice == 'F':
        _enhanced_set_submenu(state, "Latency Probe", ["Run latency probe (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_latency_probe)
    elif choice == 'G':
        _enhanced_set_submenu(state, "Weather", ["Open weather display (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_weather_display)
    elif choice == 'H':
        _enhanced_set_submenu(state, "Display FX", ["Open display FX tools (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_test_font_size)
    elif choice == 'J':
        _enhanced_set_submenu(state, "WiFi Toolkit", ["Open WiFi toolkit (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_wifi_toolkit)
    elif choice == 'K':
        _enhanced_set_submenu(state, "AI Center", ["Open AI Center (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_ai_center)
    elif choice == 'L':
        _enhanced_set_submenu(state, "Bluetooth", ["Open Bluetooth toolkit (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_bluetooth_toolkit)
    elif choice == 'M':
        _enhanced_set_submenu(state, "Traffic Report", ["Open traffic report (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_traffic_report)
    elif choice == 'N':
        _enhanced_set_submenu(state, "Database/Logs", ["Open DB/log center (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_database_log_center)
    elif choice == 'O':
        _enhanced_set_submenu(state, "Download Center", ["Open download center (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_download_center)
    elif choice == 'P':
        _enhanced_set_submenu(state, "PWN Tools", ["Open PWN tools (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_pwn_tools)
    elif choice == 'Q':
        _enhanced_set_submenu(state, "Python Power", ["Open Python Power (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_python_power)
    elif choice == 'R':
        _enhanced_set_submenu(state, "Satellite Tracker", ["Open enhanced satellite view."])
        _enhanced_satellite_view(stdscr, state)
    elif choice == 'S':
        _enhanced_set_submenu(state, "Graphing Calculator", ["Open calculator (full-screen)."])
        _enhanced_run_fullscreen(stdscr, feature_graphing_calculator)

def _select_color_scheme():
    print("\n--- SELECT COLOR ---")
    for k, v in COLORS.items():
        print(f"[{k}] {v[0]}{v[2]}{RESET}")
    color_choice = input("Select color number or [R]: ").strip().upper()
    global active_color_key, user_has_chosen
    if color_choice in COLORS:
        active_color_key, user_has_chosen = color_choice, True
        _update_user_config(active_color_key=active_color_key, user_has_chosen=user_has_chosen)
    elif color_choice == 'R':
        user_has_chosen = False
        _update_user_config(user_has_chosen=user_has_chosen)

TEXTUAL_INLINE_CSS = """
Screen {
    background: #0f131a;
    color: #e5e7eb;
}
#layout-root {
    height: 1fr;
    padding: 0 1;
}
#nav {
    width: 30;
    border: round #2a2f3a;
}
#content {
    border: round #2a2f3a;
    padding: 1 2;
    height: 1fr;
}
#detail-title {
    text-style: bold;
    color: #8ec6ff;
}
#detail-body {
    height: 1fr;
    overflow: auto;
}
.dashboard {
    grid-size: 3 2;
    grid-gutter: 1 1;
    padding: 1;
}
.card {
    border: round #2a2f3a;
    padding: 1;
    min-height: 6;
}
#tabs {
    dock: top;
}
#tab-content {
    border: round #2a2f3a;
    padding: 1 2;
    height: 1fr;
}
#topbar {
    height: 1;
    background: #151b24;
    color: #9bd;
    padding: 0 1;
}
#enhanced-indicator {
    width: 36;
    text-align: right;
}
#monitor-indicator {
    width: 16;
    text-align: right;
    color: #8ec6ff;
}
#status-strip {
    height: 3;
    background: #111722;
    border: round #263040;
    padding: 0 1;
    column-gap: 1;
}
#monitor-pane {
    height: 18;
    border: round #2a2f3a;
    background: #0a0e14;
    padding: 1 2;
    overflow: auto;
    margin: 1 0;
}
.pill {
    border: round #2a2f3a;
    padding: 0 1;
    height: 3;
    min-width: 16;
    content-align: center middle;
}
.pill.warn {
    border: round #d97757;
    color: #fcd9c1;
}
.pill.crit {
    border: round #ef4444;
    color: #fecdd3;
}
.pill.ok {
    border: round #2dd4bf;
    color: #d1faf5;
}
#clock-digits {
    width: 18;
    border: round #2a2f3a;
    text-align: center;
}
"""
# ============================================================================
# File Manager Suite
# ============================================================================

def feature_curses_file_browser():
    """Native Python curses-based file browser"""

    class FileBrowser:
        def __init__(self, start_path="."):
            self.current_path = os.path.abspath(start_path)
            self.selected_index = 0
            self.scroll_offset = 0
            self.clipboard = []
            self.clipboard_operation = None  # 'copy' or 'cut'

        def get_files(self):
            """Get sorted list of files and directories"""
            try:
                items = os.listdir(self.current_path)
                dirs = sorted([d for d in items if os.path.isdir(os.path.join(self.current_path, d))])
                files = sorted([f for f in items if os.path.isfile(os.path.join(self.current_path, f))])
                return ['..'] + dirs + files
            except PermissionError:
                return ['..']

        def get_file_size(self, path):
            """Get human-readable file size"""
            try:
                size = os.path.getsize(path)
                for unit in ['B', 'KB', 'MB', 'GB']:
                    if size < 1024.0:
                        return f"{size:.1f}{unit}"
                    size /= 1024.0
                return f"{size:.1f}TB"
            except:
                return "N/A"

        def run(self, stdscr):
            """Main browser loop"""
            try:
                curses.curs_set(0)
            except:
                pass

            curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLUE)
            curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
            curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

            while True:
                stdscr.clear()
                height, width = stdscr.getmaxyx()

                # Header
                header = f" File Browser: {self.current_path}"
                stdscr.addstr(0, 0, header[:width-1], curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(1, 0, "─" * (width-1), curses.color_pair(1))

                # Clipboard status
                if self.clipboard:
                    clip_text = f" Clipboard: {len(self.clipboard)} item(s) [{self.clipboard_operation}]"
                    stdscr.addstr(2, 0, clip_text[:width-1], curses.color_pair(6))

                # Get files
                files = self.get_files()
                display_height = height - 6

                # Adjust scroll
                if self.selected_index < self.scroll_offset:
                    self.scroll_offset = self.selected_index
                elif self.selected_index >= self.scroll_offset + display_height:
                    self.scroll_offset = self.selected_index - display_height + 1

                # Display files
                start_line = 3 if self.clipboard else 3
                for i in range(display_height):
                    file_index = i + self.scroll_offset
                    if file_index >= len(files):
                        break

                    file_name = files[file_index]
                    full_path = os.path.join(self.current_path, file_name)

                    # Determine icon and color
                    if file_name == '..':
                        icon = "↑ "
                        color = curses.color_pair(3)
                        size_str = "<UP>"
                    elif os.path.isdir(full_path):
                        icon = "📁 " if sys.platform != "win32" else "[D] "
                        color = curses.color_pair(2)
                        size_str = "<DIR>"
                    else:
                        icon = "📄 " if sys.platform != "win32" else "[F] "
                        color = curses.color_pair(1)
                        size_str = self.get_file_size(full_path)

                    # Highlight selected
                    if file_index == self.selected_index:
                        color = curses.color_pair(4) | curses.A_BOLD

                    # Truncate filename if too long
                    max_name_len = width - 20
                    display_name = file_name[:max_name_len] if len(file_name) > max_name_len else file_name
                    display_line = f" {icon}{display_name:<{max_name_len}} {size_str:>10}"

                    try:
                        stdscr.addstr(start_line + i, 0, display_line[:width-1], color)
                    except curses.error:
                        pass

                # Footer with controls
                footer_line = height - 3
                stdscr.addstr(footer_line, 0, "─" * (width-1), curses.color_pair(1))

                controls = [
                    "↑/↓:Navigate", "Enter:Open", "q:Quit", "c:Copy", "x:Cut", "v:Paste", "d:Delete", "n:New"
                ]
                footer = " | ".join(controls)

                try:
                    stdscr.addstr(footer_line + 1, 0, footer[:width-1], curses.color_pair(3))
                    status = f" Items: {len(files)-1} | Selected: {self.selected_index}/{len(files)-1}"
                    stdscr.addstr(footer_line + 2, 0, status[:width-1], curses.color_pair(1))
                except curses.error:
                    pass

                stdscr.refresh()

                # Handle input
                key = stdscr.getch()

                if key == ord('q') or key == ord('Q'):
                    break
                elif key == curses.KEY_UP or key == ord('k'):
                    self.selected_index = max(0, self.selected_index - 1)
                elif key == curses.KEY_DOWN or key == ord('j'):
                    self.selected_index = min(len(files) - 1, self.selected_index + 1)
                elif key == ord('\n') or key == curses.KEY_ENTER or key == 10:
                    selected_file = files[self.selected_index]
                    new_path = os.path.join(self.current_path, selected_file)

                    if selected_file == '..':
                        self.current_path = os.path.dirname(self.current_path)
                        self.selected_index = 0
                        self.scroll_offset = 0
                    elif os.path.isdir(new_path):
                        self.current_path = new_path
                        self.selected_index = 0
                        self.scroll_offset = 0
                    else:
                        # Open file with default editor
                        curses.endwin()
                        editor = os.environ.get('EDITOR', 'nano' if sys.platform != 'win32' else 'notepad')
                        try:
                            subprocess.run([editor, new_path])
                        except:
                            print(f"Could not open {new_path}")
                            input("Press Enter...")
                        stdscr = curses.initscr()

                elif key == ord('c') or key == ord('C'):
                    # Copy
                    selected_file = files[self.selected_index]
                    if selected_file != '..':
                        self.clipboard = [os.path.join(self.current_path, selected_file)]
                        self.clipboard_operation = 'copy'

                elif key == ord('x') or key == ord('X'):
                    # Cut
                    selected_file = files[self.selected_index]
                    if selected_file != '..':
                        self.clipboard = [os.path.join(self.current_path, selected_file)]
                        self.clipboard_operation = 'cut'

                elif key == ord('v') or key == ord('V'):
                    # Paste
                    if self.clipboard:
                        for item in self.clipboard:
                            dest = os.path.join(self.current_path, os.path.basename(item))
                            try:
                                if self.clipboard_operation == 'copy':
                                    if os.path.isdir(item):
                                        shutil.copytree(item, dest)
                                    else:
                                        shutil.copy2(item, dest)
                                elif self.clipboard_operation == 'cut':
                                    shutil.move(item, dest)
                            except Exception as e:
                                curses.endwin()
                                print(f"Error: {e}")
                                input("Press Enter...")
                                stdscr = curses.initscr()

                        if self.clipboard_operation == 'cut':
                            self.clipboard = []

                elif key == ord('d') or key == ord('D'):
                    # Delete
                    selected_file = files[self.selected_index]
                    if selected_file != '..':
                        full_path = os.path.join(self.current_path, selected_file)
                        curses.endwin()
                        confirm = input(f"Delete '{selected_file}'? (y/n): ")
                        if confirm.lower() == 'y':
                            try:
                                if os.path.isdir(full_path):
                                    shutil.rmtree(full_path)
                                else:
                                    os.remove(full_path)
                            except Exception as e:
                                print(f"Error: {e}")
                                input("Press Enter...")
                        stdscr = curses.initscr()

                elif key == ord('n') or key == ord('N'):
                    # New file/folder
                    curses.endwin()
                    print("\n1. New File")
                    print("2. New Folder")
                    choice = input("Choice: ").strip()
                    if choice == '1':
                        name = input("File name: ").strip()
                        if name:
                            try:
                                with open(os.path.join(self.current_path, name), 'w') as f:
                                    pass
                            except Exception as e:
                                print(f"Error: {e}")
                                input("Press Enter...")
                    elif choice == '2':
                        name = input("Folder name: ").strip()
                        if name:
                            try:
                                os.makedirs(os.path.join(self.current_path, name))
                            except Exception as e:
                                print(f"Error: {e}")
                                input("Press Enter...")
                    stdscr = curses.initscr()

    try:
        browser = FileBrowser()
        curses.wrapper(browser.run)
    except Exception as e:
        print(f"{get_current_color()}✗{RESET} Error: {e}")
        input("\nPress Enter to return...")


def feature_textual_file_manager():
    """Modern file manager using Textual framework"""
    try:
        from textual.app import App, ComposeResult
        from textual.widgets import DirectoryTree, Header, Footer, Static, Label
        from textual.containers import Container, Vertical, Horizontal
        from textual.binding import Binding
        from textual import on
    except ImportError:
        print(f"{get_current_color()}✗{RESET} Textual not installed.")
        print("\nInstall with: pip install textual")
        input("\nPress Enter to return...")
        return

    class FileManagerApp(App):
        """A Textual file manager application."""

        CSS = """
        Screen {
            background: $background;
        }

        DirectoryTree {
            width: 100%;
            height: 100%;
            border: solid $primary;
        }

        #info-panel {
            width: 100%;
            height: 3;
            background: $panel;
            border: solid $primary;
            padding: 1;
        }

        #main-container {
            height: 1fr;
        }
        """

        BINDINGS = [
            Binding("q", "quit", "Quit", priority=True),
            Binding("d", "toggle_dark", "Toggle Dark Mode"),
            Binding("r", "refresh", "Refresh"),
        ]

        def __init__(self):
            super().__init__()
            self.current_path = os.getcwd()

        def compose(self) -> ComposeResult:
            """Create child widgets for the app."""
            yield Header()
            with Vertical(id="main-container"):
                yield DirectoryTree(self.current_path)
                with Container(id="info-panel"):
                    yield Label(f"📁 File Manager | Path: {self.current_path}")
            yield Footer()

        def action_toggle_dark(self) -> None:
            """Toggle dark mode."""
            self.dark = not self.dark

        def action_refresh(self) -> None:
            """Refresh the directory tree."""
            tree = self.query_one(DirectoryTree)
            tree.reload()

        @on(DirectoryTree.FileSelected)
        def handle_file_selected(self, event: DirectoryTree.FileSelected) -> None:
            """Handle file selection."""
            file_path = str(event.path)

            # Update info panel
            info_label = self.query_one("#info-panel Label")
            size = os.path.getsize(file_path) if os.path.isfile(file_path) else "N/A"
            info_label.update(f"📄 Selected: {os.path.basename(file_path)} | Size: {size} bytes")

    try:
        app = FileManagerApp()
        app.run()
    except Exception as e:
        print(f"{get_current_color()}✗{RESET} Error: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to return...")


def feature_file_manager_suite():
    """File Manager Suite with multiple options"""
    while True:
        print_header("File Manager Suite", "🗂️")
        print(f"\n{get_current_color()}Choose your file manager:{RESET}\n")
        print("1. 🖥️  Curses File Browser (Lightweight, Native)")
        print("   • No external dependencies")
        print("   • Fast and simple")
        print("   • Copy/Cut/Paste support")
        print("")
        print("2. ✨ Textual File Manager (Modern UI)")
        print("   • Beautiful interface")
        print("   • Tree view navigation")
        print("   • Requires: pip install textual")
        print("")
        print("0. ← Back to Command Center")

        choice = input(f"\n{get_current_color()}Select option:{RESET} ").strip()

        if choice == '0':
            break
        elif choice == '1':
            print(f"\n{get_current_color()}Starting Curses File Browser...{RESET}")
            time.sleep(0.5)
            feature_curses_file_browser()
        elif choice == '2':
            print(f"\n{get_current_color()}Starting Textual File Manager...{RESET}")
            time.sleep(0.5)
            feature_textual_file_manager()
        else:
            print(f"{get_current_color()}✗{RESET} Invalid option")
            time.sleep(1)

# Command Center actions presented in the Textual shell. Each entry includes
# a key, title, summary, and the callable to launch.
COMMAND_CENTER_ACTIONS = [
    ("system", {"title": "System Overview", "summary": "Live snapshot of CPU, RAM, disk, and network."}),
    ("browser", {"title": "Web Browser", "summary": "Launch the web browser center.", "category": "general", "operation": "Web_Browser", "func": feature_web_browser_center}),
    ("disk", {"title": "Disk I/O Report", "summary": "Disk usage and throughput report.", "category": "general", "operation": "Disk_IO_Report", "func": feature_disk_io_report}),
    ("process", {"title": "Process Search", "summary": "Find and inspect processes.", "category": "process", "operation": "Process_Search", "func": feature_process_search}),
    ("plugin", {"title": "Plugin Center", "summary": "Manage and run plugins.", "category": "general", "operation": "Plugin_Center", "func": feature_plugin_center}),
    ("dashboard", {"title": "Remote Dashboard", "summary": "Web-based live dashboard.", "category": "general", "operation": "Remote_Dashboard", "func": feature_remote_dashboard}),
    ("pentest", {"title": "Pen Test Toolkit", "summary": "Offense utilities and scanners.", "category": "pentest", "operation": "Pen_Test_Toolkit", "func": feature_pentest_toolkit}),
    ("defence", {"title": "Defence Center", "summary": "Defense hardening tools.", "category": "defense", "operation": "Defence_Center", "func": feature_defence_center}),
    ("network", {"title": "Network Toolkit", "summary": "Network tests, traceroutes, scans.", "category": "network", "operation": "Network_Toolkit", "func": feature_network_toolkit}),
    ("audit", {"title": "Security Audit", "summary": "Security checks and reports.", "category": "security", "operation": "Security_Audit", "func": feature_security_audit}),
    ("env", {"title": "Environment Probe", "summary": "Environment variables and context.", "category": "system", "operation": "Environment_Probe", "func": feature_environment_probe}),
    ("hardware", {"title": "Hardware Serials", "summary": "Hardware identifiers and serials.", "category": "hardware", "operation": "Hardware_Serials", "func": feature_hardware_serials}),
    ("ai_probe", {"title": "AI Probe", "summary": "Deep probe AI analysis.", "category": "ai", "operation": "AI_Probe", "func": feature_deep_probe_ai}),
    ("calendar", {"title": "Calendar", "summary": "Simple calendar utility.", "category": "general", "operation": "Calendar", "func": feature_simple_calendar}),
    ("latency", {"title": "Latency Probe", "summary": "Network latency and jitter checks.", "category": "network", "operation": "Latency_Probe", "func": feature_latency_probe}),
    ("weather", {"title": "Weather Display", "summary": "Live weather and forecast.", "category": "weather", "operation": "Weather_Display", "func": feature_weather_display}),
    ("displayfx", {"title": "Display FX", "summary": "Font and visual effect tests.", "category": "general", "operation": "Display_FX", "func": feature_test_font_size}),
    ("media", {"title": "Media Menu", "summary": "Media scanner and player.", "category": "media", "operation": "Media_Menu", "func": feature_media_menu}),
    ("wifi", {"title": "WiFi Toolkit", "summary": "Wireless scans and tools.", "category": "network", "operation": "WiFi_Toolkit", "func": feature_wifi_toolkit}),
    ("ai_center", {"title": "AI Center", "summary": "AI utilities and chat tools.", "category": "ai", "operation": "AI_Center", "func": feature_ai_center}),
    ("bluetooth", {"title": "Bluetooth Toolkit", "summary": "Bluetooth scans and actions.", "category": "network", "operation": "Bluetooth_Toolkit", "func": feature_bluetooth_toolkit}),
    ("traffic", {"title": "Traffic Report", "summary": "Traffic analysis and reporting.", "category": "network", "operation": "Traffic_Report", "func": feature_traffic_report}),
    ("logs", {"title": "Database / Logs", "summary": "Log viewer and DB tools.", "category": "general", "operation": "Database_Log_Center", "func": feature_database_log_center}),
    ("download", {"title": "Download Center", "summary": "Download manager and updater.", "category": "general", "operation": "Download_Center", "func": feature_download_center}),
    ("pwn", {"title": "PWN Tools", "summary": "Offensive tooling suite.", "category": "general", "operation": "PWN_Tools", "func": feature_pwn_tools}),
    ("python_power", {"title": "Python Power", "summary": "Python power demos and helpers.", "category": "general", "operation": "Python_Power", "func": feature_python_power}),
    ("satellite", {"title": "Satellite Tracker", "summary": "Track satellites with telemetry.", "category": "general", "operation": "Satellite_Tracker", "func": feature_satellite_tracker}),
    ("calculator", {"title": "Graphing Calculator", "summary": "Graphing calculator with CAS.", "category": "general", "operation": "Graphing_Calculator", "func": feature_graphing_calculator}),
    ("docs", {"title": "Text & Doc Center", "summary": "Text editing and document tools.", "category": "general", "operation": "Text_Doc_Center", "func": feature_text_doc_center}),
    ("classic", {"title": "Classic Command Center", "summary": "Switch to legacy classic menu.", "mode": "classic"}),("file-system", {"name": "File Manager Suite", "func": feature_file_manager_suite, "cat": "file"}),
]

COMMAND_ACTION_MAP = {key: meta for key, meta in COMMAND_CENTER_ACTIONS}

def feature_enhanced_display_mode():
    """Enhanced Display Mode - Launches Bpytop System Monitor."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🎨 Enhanced Display Mode - Bpytop Monitor")

    print(f"\n{BOLD}System Resource Monitor Options:{RESET}")
    print(f" {BOLD}[1]{RESET} 🚀 Launch Bpytop (if installed)")
    print(f" {BOLD}[2]{RESET} 🖥️  Launch Htop (if installed)")
    print(f" {BOLD}[3]{RESET} 📊 Launch Gtop (if installed)")
    print(f" {BOLD}[4]{RESET} ⚡ Launch Btop++ (if installed)")
    print(f" {BOLD}[5]{RESET} 🎨 Launch Textual Interface (PyTextOS)")
    print(f" {BOLD}[0]{RESET} ↩️  Return to Command Center")

    choice = input(f"\n{BOLD}Select monitor: {RESET}").strip()

    if choice == '0':
        return
    elif choice == '1':
        launch_bpytop_monitor()
    elif choice == '2':
        launch_htop_monitor()
    elif choice == '3':
        launch_gtop_monitor()
    elif choice == '4':
        launch_btop_monitor()
    elif choice == '5':
        return run_pytextos(return_to_classic=True)
    else:
        print(f"{COLORS['1'][0]}Invalid option{RESET}")
        time.sleep(1)
        feature_enhanced_display_mode()

def run_pytextos(return_to_classic=False):
    if not _ensure_textual_imports():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{COLORS['1'][0]}ERROR: Textual failed to load!{RESET}")
        if _TEXTUAL_IMPORT_ERROR:
            print(f"Reason: {_TEXTUAL_IMPORT_ERROR}")
        print(f"Install/upgrade with: {BOLD}pip install --upgrade textual rich pygments{RESET}")
        print("\nFalling back to classic Command Center...")
        time.sleep(2)
        _set_display_mode("classic")
        return run_classic_command_center()

    try:
        class PyTextOS(App):
            BINDINGS = [
                ("l", "cycle_layout", "Layout"),
                ("m", "cycle_monitor", "Monitor"),
                ("enter", "run_selected", "Run"),
                ("r", "run_selected", "Run"),
                ("q", "quit", "Quit"),
            ]

            def __init__(self, actions, action_map, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.actions = actions
                self.action_map = action_map
                self.sections = [(key, meta.get("title", key.title())) for key, meta in actions]
                self.layout_modes = ["two_pane", "dashboard", "tabs"]
                self.layout_mode = textual_layout_mode if textual_layout_mode in self.layout_modes else "two_pane"
                self.style_mode = textual_style_mode
                self.selected_key = self.sections[0][0]
                self.pending_action = None
                self.nav = None
                self.detail_title = None
                self.detail_body = None
                self.dashboard_cards = {}
                self.tabs = None
                self.tab_content = None
                self._status_widgets = {}
                self._clock_widget = None
                self._last_net = None
                self._last_net_ts = 0.0
                # Monitor cycling
                self.monitor_modes = ["off", "bpytop", "htop", "gtop", "btop", "stats"]
                self.monitor_mode = "stats"  # Default to stats display
                self.monitor_pane = None
                self.monitor_available = {
                    "bpytop": shutil.which('bpytop') is not None,
                    "htop": shutil.which('htop') is not None,
                    "gtop": shutil.which('gtop') is not None,
                    "btop": shutil.which('btop') is not None,
                    "stats": True,  # Always available
                }

            def compose(self):
                yield Horizontal(
                    Static("PYTEXTOS"),
                    Static("", id="enhanced-indicator"),
                    Static("", id="monitor-indicator"),
                    id="topbar",
                )
                yield Horizontal(
                    Digits("", id="clock-digits"),
                    Static("CPU --", classes="pill", id="pill-cpu"),
                    Static("MEM --", classes="pill", id="pill-mem"),
                    Static("NET --", classes="pill", id="pill-net"),
                    Static("WX --", classes="pill", id="pill-wx"),
                    id="status-strip",
                )
                # Monitor pane (top pane)
                yield Static("", id="monitor-pane", classes="monitor-pane")
                yield Container(id="layout-root")
                yield Footer()

            def on_mount(self):
                self._spinner_index = 0
                self._spinner_frames = ["PY>_", "PY>__", "PY>___", "PY>__"]
                self._indicator = self.query_one("#enhanced-indicator", Static)
                self._monitor_indicator = self.query_one("#monitor-indicator", Static)
                self._clock_widget = self.query_one("#clock-digits", Digits)
                self.monitor_pane = self.query_one("#monitor-pane", Static)
                for pill_id in ["pill-cpu", "pill-mem", "pill-net", "pill-wx"]:
                    self._status_widgets[pill_id] = self.query_one(f"#{pill_id}", Static)
                self._apply_style_mode()
                self._mount_layout()
                self._update_detail(self.selected_key)
                self._refresh_status()
                self._update_monitor_display()
                self.set_interval(0.4, self._tick_spinner)
                self.set_interval(1.0, self._refresh_dynamic)
                self.set_interval(2.0, self._update_monitor_display)

            def _tick_spinner(self):
                frame = self._spinner_frames[self._spinner_index]
                self._spinner_index = (self._spinner_index + 1) % len(self._spinner_frames)
                if self._indicator:
                    self._indicator.update(f"ENHANCED MODE {frame}")

            def _update_clock(self):
                if self._clock_widget:
                    now = datetime.datetime.now().strftime("%H:%M:%S")
                    self._clock_widget.update(f"⏱ {now}")

            def _pill(self, name, text, warn=False, crit=False):
                pill = self._status_widgets.get(name)
                if not pill:
                    return
                pill.update(text)
                pill.set_class(False, "warn")
                pill.set_class(False, "crit")
                pill.set_class(False, "ok")
                if crit:
                    pill.add_class("crit")
                elif warn:
                    pill.add_class("warn")
                else:
                    pill.add_class("ok")

            def _refresh_status(self):
                self._update_clock()

                def _to_float(val):
                    try:
                        return float(val)
                    except Exception:
                        return None

                try:
                    cpu_pct_raw = psutil.cpu_percent(interval=None)
                    mem_raw = psutil.virtual_memory()
                except Exception:
                    cpu_pct_raw = None
                    mem_raw = None

                cpu_pct = _to_float(cpu_pct_raw)
                mem_pct = _to_float(getattr(mem_raw, "percent", None))
                mem_free = getattr(mem_raw, "available", None)

                cpu_text = "CPU --"
                mem_text = "MEM --"
                cpu_warn = cpu_crit = False
                mem_warn = mem_crit = False

                if cpu_pct is not None:
                    cpu_warn = cpu_pct > 75
                    cpu_crit = cpu_pct > 90
                    cpu_text = f"CPU {cpu_pct:5.1f}%"
                self._pill("pill-cpu", cpu_text, warn=cpu_warn, crit=cpu_crit)

                if mem_pct is not None:
                    mem_warn = mem_pct > 75
                    mem_crit = mem_pct > 90
                    mem_text = f"MEM {mem_pct:5.1f}%"
                self._pill("pill-mem", mem_text, warn=mem_warn, crit=mem_crit)

                net_text = "NET --"
                net_warn = False
                try:
                    net = psutil.net_io_counters()
                    now = datetime.datetime.now()
                    if self._last_net:
                        dt = max(now.timestamp() - self._last_net_ts, 0.001)
                        tx = (net.bytes_sent - self._last_net[0]) / dt
                        rx = (net.bytes_recv - self._last_net[1]) / dt
                        net_warn = (tx > 2_000_000) or (rx > 2_000_000)
                        net_text = f"NET {rx/1024:4.1f}↓ {tx/1024:4.1f}↑ KB/s"
                    self._last_net = (net.bytes_sent, net.bytes_recv)
                    self._last_net_ts = now.timestamp()
                except Exception:
                    self._last_net = None
                self._pill("pill-net", net_text, warn=net_warn)

                wx_text = "WX --"
                try:
                    if weather_cache:
                        temp = weather_cache.get("temp", "N/A")
                        icon = weather_cache.get("icon", "")
                        wx_text = f"WX {icon} {temp}"
                except Exception:
                    pass
                self._pill("pill-wx", wx_text)

            def _apply_style_mode(self):
                if self.style_mode == "file" and os.path.exists(TEXTUAL_CSS_PATH):
                    self.CSS_PATH = TEXTUAL_CSS_PATH
                else:
                    self.CSS = TEXTUAL_INLINE_CSS

            def _build_system_summary(self):
                mem = psutil.virtual_memory()
                disk = psutil.disk_usage('/')
                net = psutil.net_io_counters()
                lines = [
                    f"OS: {platform.system()} {platform.release()}",
                    f"Node: {platform.node()}",
                    f"CPU: {psutil.cpu_percent(interval=None)}% | Cores: {psutil.cpu_count(logical=False)}",
                    f"RAM: {mem.percent}% | Free: {_format_gb(mem.available)}",
                    f"Disk: {disk.percent}% | Free: {_format_gb(disk.free)}",
                    f"Net: TX {_format_mb(net.bytes_sent)} | RX {_format_mb(net.bytes_recv)}",
                ]
                if weather_cache:
                    temp = weather_cache.get("temp", "N/A")
                    icon = weather_cache.get("icon", "")
                    humidity = weather_cache.get("humidity", "N/A")
                    wind = weather_cache.get("wind", "N/A")
                    lines.append(f"Weather: {icon} {temp} | Hum: {humidity} | Wind: {wind}")
                return "\n".join(lines)

            def _section_summary(self, key):
                if key == "system":
                    return self._build_system_summary()
                meta = self.action_map.get(key, {})
                return meta.get("summary", "Select a module to view details.")

            def _section_detail(self, key):
                meta = self.action_map.get(key, {})
                base = self._section_summary(key)
                layout_line = f"Layout: {self.layout_mode.replace('_', ' ')}"
                detail_lines = [
                    f"## {dict(self.sections).get(key, 'Details')}",
                    "",
                    base,
                ]

                op = meta.get("operation")
                cat = meta.get("category")
                if op:
                    detail_lines.extend(["", f"- Operation: {op}"])
                if cat:
                    detail_lines.append(f"- Category: {cat}")

                tips = [
                    "Press Enter/R to launch the highlighted module.",
                    "Press L to cycle layout (two-pane, dashboard, tabs).",
                    "Press Q to exit the Textual shell.",
                ]
                detail_lines.extend(["", layout_line, ""])
                detail_lines.extend([f"- {tip}" for tip in tips])
                return "\n".join(detail_lines)

            def _fill_nav(self, nav):
                nav.remove_children()
                for key, title in self.sections:
                    item = ListItem(Label(title), id=f"nav-{key}")
                    nav.append(item)

            def _mount_layout(self):
                root = self.query_one("#layout-root", Container)
                root.remove_children()
                self.dashboard_cards = {}
                self.nav = None
                self.detail_title = None
                self.detail_body = None
                self.tabs = None
                self.tab_content = None

                if self.layout_mode == "two_pane":
                    nav = ListView(id="nav")
                    content = Vertical(
                        Static("", id="detail-title"),
                        Markdown("", id="detail-body"),
                        id="content",
                    )
                    root.mount(Horizontal(nav, content))
                    self.nav = nav
                    self.detail_title = content.query_one("#detail-title", Static)
                    self.detail_body = content.query_one("#detail-body", Markdown)
                    self._fill_nav(nav)
                    self._select_nav_key(self.selected_key)
                    return

                if self.layout_mode == "dashboard":
                    grid = Grid(id="dashboard", classes="dashboard")
                    # Parent must be mounted before mounting its children to avoid MountError
                    root.mount(grid)
                    for key, title in self.sections:
                        text = f"{title}\n\n{self._section_summary(key)}"
                        card = Static(text, classes="card", id=f"card-{key}")
                        self.dashboard_cards[key] = card
                        grid.mount(card)
                    return

                tabs = Tabs(id="tabs")
                content = Markdown("", id="tab-content")
                # Mount tabs before adding tab items so internal nodes exist
                root.mount(Vertical(tabs, content))
                self.tabs = tabs
                self.tab_content = content
                for key, title in self.sections:
                    tabs.add_tab(Tab(title, id=f"tab-{key}"))
                self._select_tab_key(self.selected_key)

            def _select_nav_key(self, key):
                if not self.nav:
                    return
                for idx, item in enumerate(self.nav.children):
                    if item.id == f"nav-{key}":
                        self.nav.index = idx
                        break

            def _select_tab_key(self, key):
                if not self.tabs:
                    return
                tab_id = f"tab-{key}"
                try:
                    self.tabs.active = tab_id
                except Exception:
                    pass

            def _update_detail(self, key):
                self.selected_key = key
                title = dict(self.sections).get(key, "Details")
                detail = self._section_detail(key)
                if self.detail_title and self.detail_body:
                    self.detail_title.update(title)
                    self.detail_body.update(detail)
                if self.tab_content:
                    self.tab_content.update(detail)

            def _refresh_dynamic(self):
                self._refresh_status()
                self._update_monitor_indicator()
                if self.layout_mode == "dashboard":
                    for key, card in self.dashboard_cards.items():
                        title = dict(self.sections).get(key, key.title())
                        card.update(f"{title}\n\n{self._section_summary(key)}")
                if self.selected_key == "system":
                    self._update_detail("system")

            def _key_from_item(self, item):
                if not item or not item.id:
                    return None
                if item.id.startswith("nav-"):
                    return item.id[4:]
                return None

            def action_cycle_layout(self):
                current = self.layout_modes.index(self.layout_mode)
                self.layout_mode = self.layout_modes[(current + 1) % len(self.layout_modes)]
                _update_user_config(textual_layout_mode=self.layout_mode)
                self._mount_layout()
                self._update_detail(self.selected_key)

            def action_cycle_monitor(self):
                """Cycle through available system monitors."""
                while True:
                    current = self.monitor_modes.index(self.monitor_mode)
                    self.monitor_mode = self.monitor_modes[(current + 1) % len(self.monitor_modes)]
                    # Skip unavailable monitors
                    if self.monitor_mode == "off" or self.monitor_available.get(self.monitor_mode, False):
                        break
                self._update_monitor_indicator()
                self._update_monitor_display()

            def _update_monitor_indicator(self):
                """Update the monitor mode indicator in topbar."""
                if self._monitor_indicator:
                    if self.monitor_mode == "off":
                        self._monitor_indicator.update("📊 OFF")
                    else:
                        icons = {
                            "bpytop": "🚀",
                            "htop": "🖥️",
                            "gtop": "📊",
                            "btop": "⚡",
                            "stats": "📈"
                        }
                        icon = icons.get(self.monitor_mode, "📊")
                        name = self.monitor_mode.upper()
                        self._monitor_indicator.update(f"{icon} {name}")

            def _get_monitor_stats_display(self):
                """Generate a rich stats display for the monitor pane."""
                lines = []
                lines.append("═" * 80)
                lines.append("                    SYSTEM RESOURCE MONITOR (STATS MODE)".center(80))
                lines.append("═" * 80)

                # CPU Stats
                try:
                    cpu_pct = psutil.cpu_percent(interval=None, percpu=True)
                    cpu_avg = sum(cpu_pct) / len(cpu_pct) if cpu_pct else 0
                    lines.append(f"┌─ CPU Usage: {cpu_avg:.1f}% avg ─{'─' * 50}")
                    cpu_line = "│ Cores: "
                    for i, pct in enumerate(cpu_pct[:8]):  # Show first 8 cores
                        cpu_line += f"[{i}:{pct:4.1f}%] "
                    lines.append(cpu_line)
                    if len(cpu_pct) > 8:
                        lines.append(f"│ ... and {len(cpu_pct) - 8} more cores")
                except:
                    lines.append("│ CPU: N/A")

                # Memory Stats
                try:
                    mem = psutil.virtual_memory()
                    mem_bar = "█" * int(mem.percent / 5) + "░" * (20 - int(mem.percent / 5))
                    lines.append(f"├─ Memory: {mem.percent:.1f}% of {mem.total / (1024**3):.1f} GB ─{'─' * 30}")
                    lines.append(f"│ [{mem_bar}] Used: {mem.used / (1024**3):.1f} GB | Free: {mem.available / (1024**3):.1f} GB")
                except:
                    lines.append("│ Memory: N/A")

                # Disk Stats
                try:
                    disk = psutil.disk_usage('/')
                    disk_bar = "█" * int(disk.percent / 5) + "░" * (20 - int(disk.percent / 5))
                    lines.append(f"├─ Disk: {disk.percent:.1f}% of {disk.total / (1024**3):.1f} GB ─{'─' * 30}")
                    lines.append(f"│ [{disk_bar}] Used: {disk.used / (1024**3):.1f} GB | Free: {disk.free / (1024**3):.1f} GB")
                except:
                    lines.append("│ Disk: N/A")

                # Network Stats
                try:
                    net = psutil.net_io_counters()
                    lines.append(f"├─ Network ─{'─' * 65}")
                    lines.append(f"│ TX: {net.bytes_sent / (1024**3):.2f} GB | RX: {net.bytes_recv / (1024**3):.2f} GB")
                    lines.append(f"│ Packets: Sent {net.packets_sent:,} | Recv {net.packets_recv:,}")
                except:
                    lines.append("│ Network: N/A")

                # Top Processes
                try:
                    procs = []
                    for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                        try:
                            procs.append(p.info)
                        except:
                            pass
                    procs.sort(key=lambda x: x.get('cpu_percent', 0) or 0, reverse=True)
                    lines.append(f"└─ Top 5 Processes (by CPU) ─{'─' * 50}")
                    for i, p in enumerate(procs[:5], 1):
                        name = (p.get('name', 'Unknown')[:20]).ljust(20)
                        pid = str(p.get('pid', 0)).rjust(6)
                        cpu = f"{p.get('cpu_percent', 0):.1f}%".rjust(7)
                        mem = f"{p.get('memory_percent', 0):.1f}%".rjust(7)
                        lines.append(f"  {i}. {name} PID:{pid} CPU:{cpu} MEM:{mem}")
                except:
                    lines.append("  Processes: N/A")

                lines.append("═" * 80)
                lines.append("Press 'M' to cycle monitors | Available: Bpytop, Htop, Gtop, Btop, Stats".center(80))
                return "\n".join(lines)

            def _get_monitor_command_display(self, monitor_name):
                """Generate instructions for launching external monitor."""
                lines = []
                lines.append("═" * 80)
                lines.append(f"                     {monitor_name.upper()} MONITOR MODE".center(80))
                lines.append("═" * 80)
                lines.append("")
                lines.append(f"  {monitor_name.upper()} is available but requires full terminal control.")
                lines.append(f"  Press 'Q' to exit PyTextOS, then select option [1-4] from Enhanced Display.")
                lines.append("")
                lines.append(f"  OR run directly from terminal:")
                lines.append(f"    $ {monitor_name}")
                lines.append("")
                lines.append("  This integrated view shows real-time stats in STATS mode.")
                lines.append("  Press 'M' to cycle back to STATS mode for inline monitoring.")
                lines.append("")
                lines.append("═" * 80)

                # Show mini stats even in command mode
                try:
                    cpu_pct = psutil.cpu_percent(interval=None)
                    mem = psutil.virtual_memory()
                    lines.append(f"  Quick Stats: CPU {cpu_pct:.1f}% | MEM {mem.percent:.1f}% | DISK {psutil.disk_usage('/').percent:.1f}%")
                    lines.append("═" * 80)
                except:
                    pass

                return "\n".join(lines)

            def _update_monitor_display(self):
                """Update the monitor pane content based on current mode."""
                if not self.monitor_pane:
                    return

                if self.monitor_mode == "off":
                    self.monitor_pane.update("[Monitor Off - Press 'M' to enable]")
                    return

                if self.monitor_mode == "stats":
                    # Show inline stats display
                    content = self._get_monitor_stats_display()
                    self.monitor_pane.update(content)
                elif self.monitor_mode in ["bpytop", "htop", "gtop", "btop"]:
                    if self.monitor_available.get(self.monitor_mode, False):
                        # Show instructions to launch
                        content = self._get_monitor_command_display(self.monitor_mode)
                        self.monitor_pane.update(content)
                    else:
                        self.monitor_pane.update(f"[{self.monitor_mode.upper()} not installed - Press 'M' to cycle]")

            def action_run_selected(self):
                if self.selected_key in dict(self.sections):
                    self.pending_action = self.selected_key
                    self.exit()

            def action_quit(self):
                self.exit()

            def on_list_view_selected(self, event):
                key = self._key_from_item(event.item)
                if key:
                    self._update_detail(key)

            def on_list_view_highlighted(self, event):
                key = self._key_from_item(event.item)
                if key:
                    self._update_detail(key)

            def on_tabs_tab_activated(self, event):
                if event.tab.id and event.tab.id.startswith("tab-"):
                    key = event.tab.id[4:]
                    self._update_detail(key)

        _set_display_mode("enhanced")
        actions = COMMAND_CENTER_ACTIONS
        action_map = COMMAND_ACTION_MAP

        while True:
            app = PyTextOS(actions, action_map)
            app.run()

            if not app.pending_action:
                break

            meta = action_map.get(app.pending_action, {})
            if meta.get("mode") == "classic":
                _set_display_mode("classic")
                run_classic_command_center()
                if return_to_classic:
                    return
                break

            func = meta.get("func")
            if func:
                safe_run(
                    meta.get("category", "general"),
                    meta.get("operation", meta.get("title", "Action")),
                    func,
                )
                continue

        if return_to_classic:
            _set_display_mode("classic")
            run_classic_command_center()

    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{COLORS['1'][0]}ERROR in PyTextOS:{RESET}")
        print(f"{str(e)}\n")
        print("Falling back to classic Command Center...")
        time.sleep(3)
        _set_display_mode("classic")
        run_classic_command_center()

# --- MAIN OPERATING SYSTEM LOOP ---

def run_classic_command_center():
    global stop_clock, mini_view, truncated_thermal, is_blinking, temp_unit, active_color_key, user_has_chosen, display_mode

    _bootstrap_classic_stack()

    while True:
        stop_clock = True
        os.system('cls' if os.name == 'nt' else 'clear')
        current_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print_header("🆔 System Identity", extra_info=f"| 🕒 {current_dt}")
        if not mini_view:
            os_name = platform.system()
            cpu_arch = platform.machine().lower()
            is_arm = "arm" in cpu_arch or "aarch64" in cpu_arch
            print(f"💻 Operating System: {BOLD}{os_name}{RESET}")
            if os_name == "Linux": print("👑 OS Verdict:     King O.S.")
            elif os_name == "Windows": print("📉 OS Verdict:     You had your chance")
            elif os_name == "Darwin": print("👸 OS Verdict:     MacOS Queen O.S.")
            print(f"📦 OS Release:      {platform.release()}")
            print(f"🏗️ Architecture:    {platform.machine()} ({platform.architecture()[0]})")
            print(f"📟 Processor Type:  {'ARM Based' if is_arm else 'x86 Based'}")
            print(f"📛 Node Name:       {platform.node()}")
            print_header("⚙️ CPU Architecture")
            print(f"🖥️ Processor:       {platform.processor()}")
            print(f"🧠 Physical Cores:  {psutil.cpu_count(logical=False)}")
            print(f"🧵 Total Threads:   {psutil.cpu_count(logical=True)}")
            cpufreq = psutil.cpu_freq()
            if cpufreq: print(f"⚡ Max Frequency:   {cpufreq.max:.2f}Mhz")
            print(f"📈 Current Usage:   {draw_bar(psutil.cpu_percent(interval=None))}")
            print_header("🌡️ Thermal Sensors")
            try:
                temps = psutil.sensors_temperatures()
                if not temps: print("🚦 Status:          No thermal sensors detected")
                else:
                    unit_label = "\u00b0F" if temp_unit == "F" else "\u00b0C"
                    if truncated_thermal:
                        core_temps = []
                        other_temps = []
                        for name, entries in temps.items():
                            for entry in entries:
                                c_temp = entry.current
                                val = (c_temp * 9/5) + 32 if temp_unit == "F" else c_temp
                                label = entry.label or name
                                if any(x in label.lower() for x in ["core", "thermal", "soc"]):
                                    core_temps.append(val)
                                else: other_temps.append(f"{label}: {val:.1f}{unit_label}")
                        if core_temps: print(f"🌡️ Avg Sensor Temp: {sum(core_temps) / len(core_temps):.1f}{unit_label}")
                        if other_temps: print(f"🌡️ Other:                 {' | '.join(other_temps)}")
                    else:
                        for name, entries in temps.items():
                            for entry in entries:
                                label = entry.label or name
                                disp_t = (entry.current * 9/5) + 32 if temp_unit == "F" else entry.current
                                print(f"🌡️ {label}: ".ljust(17) + f"{disp_t:.1f}{unit_label}")
            except: print("🚦 Status:          Temperature sensors not supported on this OS")

            print_header("🔍 Advanced Hardware Probing")
            try:
                gpus = GPUtil.getGPUs()
                if not gpus: print("🎮 GPU:              N/A (No Discrete GPU)")
                for g in gpus:
                    gt = (g.temperature * 9/5) + 32 if temp_unit == "F" else g.temperature
                    print(f"🎮 GPU Model:       {g.name}")
                    print(f"📈 GPU Load:        {draw_bar(g.load*100)}")
                    print(f"🌡️ GPU Temp:        {gt:.1f}\u00b0{temp_unit}")
                    print(f"🧠 GPU Mem Used:    {g.memoryUsed}MB / {g.memoryTotal}MB")
            except: print("🎮 GPU Probing:     N/A")
            try:
                fans = psutil.sensors_fans()
                if not fans: print("🌀 Fans:              N/A")
                else:
                    for name, entries in fans.items():
                        for entry in entries:
                            print(f"🌀 {entry.label or name}: ".ljust(17) + f"{entry.current} RPM")
            except: print("🌀 Fan Probing:     N/A")

            print_header("🧠 Memory Status")
            mem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            print(f"📏 Total RAM:       {_format_gb(mem.total)}")
            print(f"🔓 Available RAM:   {_format_gb(mem.available)}")
            print(f"📈 RAM Usage:       {draw_bar(mem.percent)}")
            print(f"🔄 Swap Total:      {_format_gb(swap.total)}")
            print_header("💽 Storage & Disk")
            disk = psutil.disk_usage('/')
            print(f"📏 Total Space:     {_format_gb(disk.total)}")
            print(f"📈 Used Space:      {draw_bar(disk.percent)} ({_format_gb(disk.used)})")
            print(f"🔓 Free Space:      {_format_gb(disk.free)}")
            print_header("🌐 Network & IDs")
            hostname = socket.gethostname()
            print(f"📛 Hostname:         {hostname}")
            try: print(f"📍 Local IP:         {socket.gethostbyname(hostname)}")
            except: print("📍 Local IP:          Unknown")
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
            print(f"🆔 MAC Address:     {mac}")
            net_io = psutil.net_io_counters()
            print(f"⬆️ Data Sent:       {_format_mb(net_io.bytes_sent)}")
            print(f"⬇️ Data Received:   {_format_mb(net_io.bytes_recv)}")
            print_header("🐍 Python Context")
            print(f"🐍 Python Version:  {platform.python_version()}")
            print_header("🔮 Miscellaneous")
            boot_str, uptime_str = _format_boot_info(psutil.boot_time())
            print(f"🏁 System Boot:     {boot_str}")
            print(f"⏱️ Uptime:          {uptime_str}")
            battery = psutil.sensors_battery()
            if battery:
                try:
                    status = "🔌 Charging" if battery.power_plugged else "🔋 Discharging"
                    print(f"🔋 Battery:           {battery.percent}% ({status})")
                except Exception:
                    print("🔋 Battery:           N/A")
            print(f"\n{get_current_color()}--- ✅ REPORT COMPLETE ---{RESET}")

        if display_mode == "enhanced":
            stop_clock = True
            feature_enhanced_display_mode()
            continue

        stop_clock = False
        threading.Thread(target=live_system_identity_clock, daemon=True).start()

        c = get_current_color()
        print(f"\n{BOLD}{c}{BOX_CHARS['TL']}{BOX_CHARS['H']*24} 🌍 COMMAND CENTER {BOX_CHARS['H']*24}{BOX_CHARS['TR']}{RESET}")
        print(f" {BOLD}[1]{RESET} ✨ Blink: {'ON ' if is_blinking else 'OFF'}  {BOLD}[2]{RESET} 🌡️ Temp: {temp_unit}      {BOLD}[3]{RESET} 🌡️ Thermal: {'Short' if truncated_thermal else 'Full '}")
        print(f" {BOLD}[4]{RESET} 📏 Mini: {'ON ' if mini_view else 'OFF'}   {BOLD}[5]{RESET} 🚪 Exit         {BOLD}[6]{RESET} 🎨 Color Scheme")
        print(f" {BOLD}[7]{RESET} 🌐 Web Browser   {BOLD}[8]{RESET} 💽 Disk I/O    {BOLD}[9]{RESET} 📑 Processes    {BOLD}[0]{RESET} 🌐 Network")
        print(f" {BOLD}[10]{RESET} 🔌 Plugin Center   {BOLD}[11]{RESET} 🖥️ Remote Dashboard  {BOLD}[12]{RESET} 🛡️ Pen Test    {BOLD}[13]{RESET} 🛡️ Defence")
        print(f" {BOLD}[A]{RESET} 🛡️ Audit Sec     {BOLD}[B]{RESET} 📂 Env Probe   {BOLD}[C]{RESET} 📟 HW Serials   {BOLD}[D]{RESET} 🤖 AI Probe     {BOLD}[E]{RESET} 📅 Calendar")
        print(f" {BOLD}[F]{RESET} ⏱️ Latency Probe {BOLD}[G]{RESET} 🌍 Weather       {BOLD}[H]{RESET} 🔡 Display FX   {BOLD}[I]{RESET} 🎞️ Media Scan")
        print(f" {BOLD}[J]{RESET} 📡 WiFi Toolkit   {BOLD}[K]{RESET} 🤖 A.I. Center   {BOLD}[L]{RESET} Bluetooth   {BOLD}[M]{RESET} Traffic")
        print(f" {BOLD}[N]{RESET} 💾 Database/Logs  {BOLD}[O]{RESET} 📦 Download Center  {BOLD}[P]{RESET} 💥 PWN Tools  {BOLD}[Q]{RESET} 🐍 Python Power")
        print(f" {BOLD}[R]{RESET} 🛰️ Satellite Tracker   {BOLD}[U]{RESET} Enhanced Display Mode   {BOLD}[V]{RESET} Exit Enhanced Mode")
        print(f" {BOLD}[S]{RESET} 📊 Graphing Calculator   {BOLD}[T]{RESET} 📝 Text & Doc")
        print(f"{BOLD}{c}{BOX_CHARS['BL']}{BOX_CHARS['H']*64}{BOX_CHARS['BR']}{RESET}")

        choice = input(f"{BOLD}🎯 Select an option (0-U): {RESET}").strip().upper()
        _update_user_config(last_choice=choice)
        stop_clock = True

        if choice == '1':
            is_blinking = not is_blinking
            _update_user_config(is_blinking=is_blinking)
        elif choice == '2':
            temp_unit = "F" if temp_unit == "C" else "C"
            _update_user_config(temp_unit=temp_unit)
        elif choice == '3':
            truncated_thermal = not truncated_thermal
            _update_user_config(truncated_thermal=truncated_thermal)
        elif choice == '4':
            mini_view = not mini_view
            _update_user_config(mini_view=mini_view)
        elif choice == '5':
            _update_user_config(
                active_color_key=active_color_key,
                user_has_chosen=user_has_chosen,
                is_blinking=is_blinking,
                temp_unit=temp_unit,
                truncated_thermal=truncated_thermal,
                mini_view=mini_view
            )
            break
        elif choice == '6':
            print("\n--- 🎨 SELECT COLOR ---")
            for k, v in COLORS.items(): print(f"[{k}] {v[0]}{v[2]}{RESET}")
            color_choice = input("🎯 Select color number or [R]: ").strip().upper()
            if color_choice in COLORS:
                active_color_key, user_has_chosen = color_choice, True
                _update_user_config(active_color_key=active_color_key, user_has_chosen=user_has_chosen)
            elif color_choice == 'R':
                user_has_chosen = False
                _update_user_config(user_has_chosen=user_has_chosen)
        elif choice == '7': safe_run("general", "Web_Browser", feature_web_browser_center)
        elif choice == '8': safe_run("general", "Disk_IO_Report", feature_disk_io_report)
        elif choice == '9': safe_run("process", "Process_Search", feature_process_search)
        elif choice == '10': safe_run("general", "Plugin_Center", feature_plugin_center)
        elif choice == '11': safe_run("general", "Remote_Dashboard", feature_remote_dashboard)
        elif choice == '12': safe_run("pentest", "Pen_Test_Toolkit", feature_pentest_toolkit)
        elif choice == '13': safe_run("defense", "Defence_Center", feature_defence_center)
        elif choice == '0': safe_run("network", "Network_Toolkit", feature_network_toolkit)
        elif choice == 'A': safe_run("security", "Security_Audit", feature_security_audit)
        elif choice == 'B': safe_run("system", "Environment_Probe", feature_environment_probe)
        elif choice == 'C': safe_run("hardware", "Hardware_Serials", feature_hardware_serials)
        elif choice == 'D': safe_run("ai", "AI_Probe", feature_deep_probe_ai)
        elif choice == 'E': safe_run("general", "Calendar", feature_simple_calendar)
        elif choice == 'F': safe_run("network", "Latency_Probe", feature_latency_probe)
        elif choice == 'G': safe_run("weather", "Weather_Display", feature_weather_display)
        elif choice == 'H': safe_run("general", "Display_FX", feature_test_font_size)
        elif choice == 'I': safe_run("media", "Media_Menu", feature_media_menu)
        elif choice == 'J': safe_run("network", "WiFi_Toolkit", feature_wifi_toolkit)
        elif choice == 'K': safe_run("ai", "AI_Center", feature_ai_center)
        elif choice == 'L': safe_run("network", "Bluetooth_Toolkit", feature_bluetooth_toolkit)
        elif choice == 'M': safe_run("network", "Traffic_Report", feature_traffic_report)
        elif choice == 'N': safe_run("general", "Database_Log_Center", feature_database_log_center)
        elif choice == 'O': safe_run("general", "Download_Center", feature_download_center)
        elif choice == 'P': safe_run("general", "PWN_Tools", feature_pwn_tools)
        elif choice == 'Q': safe_run("general", "Python_Power", feature_python_power)
        elif choice == 'R': safe_run("general", "Satellite_Tracker", feature_satellite_tracker)
        elif choice == 'S': safe_run("general", "Graphing_Calculator", feature_graphing_calculator)
        elif choice == 'T': safe_run("general", "Text_Doc_Center", feature_text_doc_center)
        elif choice == 'V':
            _set_display_mode("classic")
        elif choice == 'U':
            _set_display_mode("enhanced")
            feature_enhanced_display_mode()

#version 21

# --- VERSION 21.1: AUTONOMOUS SYSTEM OPTIMIZER ---
def autonomous_optimizer_daemon():
    """
    Background thread that monitors the OS and automatically adjusts
    settings based on system stress or environmental changes.
    """
    global mini_view, truncated_thermal, is_blinking, temp_unit

    # Give the main OS time to boot
    time.sleep(5)

    while True:
        try:
            # 1. HEURISTIC: High CPU/RAM Stress -> Force Mini View
            cpu_load = psutil.cpu_percent(interval=1)
            mem_load = psutil.virtual_memory().percent

            if (cpu_load > 85 or mem_load > 90) and not mini_view:
                mini_view = True
                # We use sys.__stdout__ to bypass any VisualFX filters for the alert
                sys.__stdout__.write(f"\n{COLORS['1'][0]}[🤖 AI] CRITICAL LOAD: Enabling Mini View for performance.{RESET}\n")

            # 2. HEURISTIC: Thermal Throttling -> Truncate Thermal Display
            try:
                temps = psutil.sensors_temperatures()
                if temps:
                    # Check if any core is over 80C
                    high_temp = any(any(e.current > 80 for e in entries) for entries in temps.values())
                    if high_temp and not truncated_thermal:
                        truncated_thermal = True
                        sys.__stdout__.write(f"\n{COLORS['4'][0]}[🤖 AI] THERMAL ALERT: Truncating sensor data.{RESET}\n")
            except:
                pass

            # 3. HEURISTIC: Battery Critical -> Disable Blinking (Power Save)
            battery = psutil.sensors_battery()
            if battery and battery.percent < 20 and not battery.power_plugged:
                if is_blinking:
                    is_blinking = False
                    sys.__stdout__.write(f"\n{COLORS['1'][0]}[🔋 AI] LOW BATTERY: Power Save Mode (Blink Disabled).{RESET}\n")

            # 4. HEURISTIC: Geo-Optimization
            # If weather is N/A, try to trigger a background refresh
            if weather_cache["temp"] == "N/A":
                threading.Thread(target=get_weather_data, daemon=True).start()

        except Exception:
            pass

        time.sleep(10) # Run audit every 10 seconds

# Start the Shadow Auditor in a daemon thread
threading.Thread(target=autonomous_optimizer_daemon, daemon=True).start()

print(f"\n{COLORS['10'][0]}[+] Autonomous Optimizer V21.1 Linked Successfully.{RESET}")

# --- EARTH & MOON ANIMATION ---
def animate_earth_and_moon_exit(stop_event):
    """
    Animated Earth with rotating texture and orbiting Moon.
    Runs in background thread until stop_event is set.
    """
    # Simplified wrapped map of Earth's continents
    earth_texture = "  ..###...  ....#######....  ...###...  ....#######....  "

    # Animation settings
    total_frames = 30
    frame_count = 0

    try:
        while not stop_event.is_set():
            f = frame_count % total_frames

            # Calculate Earth rotation offset
            earth_offset = int((f / total_frames) * (len(earth_texture) // 2))

            # Calculate Moon position (circular orbit)
            angle = (f / total_frames) * 2 * math.pi
            moon_x = int(math.sin(angle) * 25) + 30
            is_behind = math.cos(angle) > 0

            # Earth ASCII structure
            earth_lines = [
                "      _______      ",
                "   ./#########\\.   ",
                "  /#############\\  ",
                " |###############| ",
                " |###############| ",
                "  \\#############/  ",
                "   '\\#########/'   ",
                "      -------      "
            ]

            # Move cursor to top to create animation effect (only updates top portion)
            sys.__stdout__.write("\033[1;1H")  # Move to top-left

            # Render title
            sys.__stdout__.write("\n" + " " * 15 + "🌍 EARTH & MOON ORBIT 🌙\n")
            sys.__stdout__.write(" " * 10 + "═" * 40 + "\n")

            # Render each line of Earth
            for i, line in enumerate(earth_lines):
                # Replace '#' with rotating texture
                display_line = list(line)
                for j, char in enumerate(display_line):
                    if char == '#':
                        tex_idx = (j + earth_offset) % (len(earth_texture) // 2)
                        display_line[j] = earth_texture[tex_idx]

                row_text = "".join(display_line)
                row_padding = " " * 20
                full_row = list(row_padding + row_text + row_padding)

                # Add Moon on middle row
                if i == 4:
                    if is_behind:
                        if moon_x < 20 or moon_x > 40:
                            if 0 <= moon_x < len(full_row):
                                full_row[moon_x] = '🌑'
                    else:
                        if 0 <= moon_x < len(full_row):
                            full_row[moon_x] = '🌕'

                sys.__stdout__.write("".join(full_row) + "\n")

            sys.__stdout__.write(" " * 10 + "═" * 40 + "\n\n")

            # Move cursor to prompt line (line 15) to avoid interfering with input
            sys.__stdout__.write("\033[15;1H")
            sys.__stdout__.flush()

            frame_count += 1
            time.sleep(0.08)  # ~12 FPS

    except Exception:
        pass

# --- USER-CONTROLLED BACKGROUND OPTIMIZER ---
def start_autonomous_monitor():
    # Create stop event for animation
    stop_animation = threading.Event()

    # Start animation in background thread
    animation_thread = threading.Thread(
        target=animate_earth_and_moon_exit,
        args=(stop_animation,),
        daemon=True
    )
    animation_thread.start()

    # Clear screen and position content below animation
    os.system('cls' if os.name == 'nt' else 'clear')

    # Position cursor and display prompt text (animation will run above)
    # Print spacing and text, then move cursor to input position
    print("\n" * 12)
    print(f"{COLORS['10'][0]}[🤖 AI] Would you like to enable the Autonomous Optimizer?{RESET}")
    print("   (Automatically adjusts UI, Power, and Thermal settings based on load)")

    # Print prompt on same line and get input
    sys.__stdout__.write(f"{BOLD}🎯 Enable AI-Assisted Management? (y/n): {RESET}")
    sys.__stdout__.flush()
    choice = input().strip().lower()

    # Stop animation
    stop_animation.set()
    time.sleep(0.1)  # Give animation time to stop

    # Clear screen after animation stops
    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == 'y':
        def optimizer_logic():
            global mini_view, truncated_thermal, is_blinking
            while True:
                try:
                    # Monitor stress via existing psutil calls
                    cpu = psutil.cpu_percent(interval=1)
                    mem = psutil.virtual_memory().percent

                    # Auto-Mini Mode for high load
                    if cpu > 85 and not mini_view:
                        mini_view = True
                        sys.__stdout__.write(f"\n{COLORS['1'][0]}[!] Heavy Load: Switching to Mini View.{RESET}\n")

                    # Thermal Protection
                    temps = psutil.sensors_temperatures()
                    if temps:
                        for entries in temps.values():
                            if any(e.current > 75 for e in entries) and not truncated_thermal:
                                truncated_thermal = True
                                sys.__stdout__.write(f"\n{COLORS['4'][0]}[!] Thermal Spike: Truncating display.{RESET}\n")
                except: pass
                time.sleep(15)

        threading.Thread(target=optimizer_logic, daemon=True).start()
        print(f"{COLORS['2'][0]}✅ Optimizer running in background.{RESET}")
    else:
        print(f"{COLORS['3'][0]}ℹ️ Optimizer skipped. Manual control only.{RESET}")

# Trigger prompt and heuristic only when classic mode boots
_classic_bootstrap_done = False


def apply_heuristic_intelligence():
    """
    Leverages the Deep Probe AI logic to modify the OS environment.
    """
    # 1. Calculate the Heuristic Stress Score
    cpu_stress = psutil.cpu_percent(interval=0.5)
    mem_stress = psutil.virtual_memory().percent
    stress_score = (cpu_stress * 0.4) + (mem_stress * 0.4)

    # 2. Automated Action based on Stress Verdict
    if stress_score > 80: # CRITICAL STRESS
        # Automatically disable expensive visual effects
        sys.stdout.mode = 0 # Force Normal mode to save CPU from FX Regex
        global is_blinking
        is_blinking = False

    # 3. Zombie Cleanup Heuristic
    # If the AI Probe detects high zombie counts, suggest a cleanup
    try:
        zombies = [p for p in psutil.process_iter() if p.status() == psutil.STATUS_ZOMBIE]
        if len(zombies) > 5:
            sys.__stdout__.write(f"\n{COLORS['5'][0]}[🧠 AI] Detected {len(zombies)} zombies. Recommendation: Restart Kernel.{RESET}\n")
    except: pass

def _bootstrap_classic_stack():
    """Run interactive/bootstrap routines once before entering classic UI."""
    global _classic_bootstrap_done
    if _classic_bootstrap_done:
        return
    _classic_bootstrap_done = True
    try:
        start_autonomous_monitor()
    except Exception:
        pass
    try:
        apply_heuristic_intelligence()
    except Exception:
        pass

# --- EXTERNAL MODULE LINKER & ENHANCED MEDIA HOOK ---
def link_external_tool(tool_name, module_path, function_name="run", context=None):
    """
    Dynamically loads an external python file and executes a specific function.
    Useful for linking heavy tools like MP3 players or Scanners.
    """
    import importlib.util
    if not os.path.exists(module_path):
        print(f"\n{COLORS['1'][0]}[!] Link Failed: {module_path} not found.{RESET}")
        return False

    try:
        spec = importlib.util.spec_from_file_location(tool_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Call the specific function (e.g., 'play_music' or 'scan_deep')
        func = getattr(module, function_name)
        print(f"{COLORS['10'][0]}🚀 Launching External Hook: {tool_name}...{RESET}")
        func(context)
        return True
    except Exception as e:
        print(f"{COLORS['1'][0]}[💥] Error in Linked Module: {e}{RESET}")
        return False

def feature_terminal_mp3_player():
    """
    Full-featured MP3 player that browses the filesystem and plays audio files.
    """
    print_header("🎵 Terminal MP3 Player")

    while True:
        current_dir = input(f"\n📂 Enter directory path (or press Enter for current): ").strip()
        if not current_dir:
            current_dir = os.path.expanduser("~")

        if not os.path.isdir(current_dir):
            print(f"{COLORS['1'][0]}❌ Invalid directory!{RESET}")
            continue

        # Find all audio files
        audio_extensions = ['.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aac']
        audio_files = []

        try:
            for root, dirs, files in os.walk(current_dir):
                for file in files:
                    if os.path.splitext(file)[1].lower() in audio_extensions:
                        full_path = os.path.join(root, file)
                        audio_files.append(full_path)
        except PermissionError:
            print(f"{COLORS['1'][0]}⚠️ Permission denied for some directories{RESET}")

        if not audio_files:
            print(f"{COLORS['4'][0]}⚠️ No audio files found in '{current_dir}' and subdirectories{RESET}")
            continue

        # Display audio files
        print(f"\n{COLORS['3'][0]}Found {len(audio_files)} audio file(s):{RESET}\n")
        for i, file_path in enumerate(audio_files[:50], 1):  # Limit to 50 files
            file_name = os.path.basename(file_path)
            print(f" {BOLD}[{i:2d}]{RESET} {file_name}")

        if len(audio_files) > 50:
            print(f" ... and {len(audio_files) - 50} more files")

        # Selection menu
        print(f"\n{BOLD}{'─' * 60}{RESET}")
        print(f" {BOLD}[Q]{RESET} Return to Media Menu  |  {BOLD}[P]{RESET} Play selected file")
        print(f"{BOLD}{'─' * 60}{RESET}")

        choice = input(f"\n🎯 Enter file number (1-{min(50, len(audio_files))}) or [Q]uit: ").strip().upper()

        if choice == 'Q':
            break

        if choice == 'P':
            file_num = input(f"🎯 Which file to play? (1-{min(50, len(audio_files))}): ").strip()
            if file_num.isdigit():
                idx = int(file_num) - 1
                if 0 <= idx < len(audio_files):
                    play_audio_file(audio_files[idx])
                else:
                    print(f"{COLORS['1'][0]}❌ Invalid selection!{RESET}")
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(audio_files):
                play_audio_file(audio_files[idx])
            else:
                print(f"{COLORS['1'][0]}❌ Invalid selection!{RESET}")

def play_audio_file(file_path):
    """
    Play an audio file using available terminal players (mpv, ffplay, play, or mplayer)
    """
    if not os.path.exists(file_path):
        print(f"{COLORS['1'][0]}❌ File not found: {file_path}{RESET}")
        return

    file_name = os.path.basename(file_path)
    print(f"\n{COLORS['2'][0]}🎵 Now Playing: {file_name}{RESET}")
    print(f"{COLORS['6'][0]}Press Ctrl+C to stop playback{RESET}\n")

    # Try different players in order of preference
    players = ['mpv', 'ffplay', 'play', 'mplayer']
    player_found = False

    for player in players:
        try:
            # Check if player exists
            result = os.system(f"which {player} > /dev/null 2>&1")
            if result == 0:
                player_found = True
                print(f"🔊 Using player: {player}\n")

                # Launch the player
                if player == 'mpv':
                    os.system(f"mpv --quiet '{file_path}'")
                elif player == 'ffplay':
                    os.system(f"ffplay -nodisp -autoexit '{file_path}' 2>/dev/null")
                elif player == 'play':
                    os.system(f"play '{file_path}'")
                elif player == 'mplayer':
                    os.system(f"mplayer '{file_path}'")
                break
        except:
            continue

    if not player_found:
        print(f"{COLORS['1'][0]}❌ No audio player found!{RESET}")
        print(f"📦 Install one of these: mpv, ffmpeg, sox, or mplayer")
        print(f"   Ubuntu: sudo apt install mpv")
        input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")
        return

    print(f"\n{COLORS['2'][0]}✅ Playback finished{RESET}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_linked_media_player():
    """
    An extension for Option [I] that asks to launch an external player.
    """
    print_header("🎵 Advanced Media Linker")
    print(f" {BOLD}[1]{RESET} Standard Scan (Internal)")
    print(f" {BOLD}[2]{RESET} Launch Terminal MP3 Player")

    choice = input("\n🎯 Choice: ").strip()

    if choice == '2':
        feature_terminal_mp3_player()
    else:
        feature_media_scanner()

# Integration: You can now call 'feature_linked_media_player()' from your main loop choice 'I'
# --- ENHANCED MEDIA SCANNER WITH AUTO-PLAY HOOK ---
def feature_media_scanner_integrated():
    """
    An improved version of your scanner that hooks into the
    External Module Linker to play files immediately.
    """
    print_header("🎞️ Interstellar Media Scanner + Play")
    target_dir = input("📂 Enter the folder path to scan: ").strip()

    if not os.path.isdir(target_dir):
        print(f" {COLORS['1'][0]}[!] Error: Invalid path.{RESET}")
        time.sleep(1)
        return

    media_exts = {
        "Audio": [".mp3", ".wav", ".ogg"],
        "Video": [".mp4", ".mkv"],
        "Images": [".jpg", ".png", ".webp"]
    }

    results = []
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            for category, extensions in media_exts.items():
                if ext in extensions:
                    results.append({"name": file, "path": os.path.join(root, file), "type": category})

    if not results:
        print(f" {COLORS['4'][0]}[!] No media found.{RESET}")
        input("\n[ Press Enter ]")
        return

    page_limit = 10
    for start in range(0, len(results), page_limit):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📁 Media Assets Found", extra_info=f"Page {int(start/page_limit)+1}")
        chunk = results[start:start+page_limit]

        for i, item in enumerate(chunk):
            c = COLORS["6"][0] if item["type"] == "Audio" else COLORS["3"][0]
            print(f"{BOLD}[{i + 1}]{RESET} {c}[{item['type']}] {RESET}{item['name']}")

        print("\n" + "-"*60)
        cmd = input(f"🎯 Select [Number] to Play/Open, [N]ext, or [Enter] to exit: ").strip().upper()

        if cmd.isdigit():
            idx = int(cmd) - 1
            if 0 <= idx < len(chunk):
                selected = chunk[idx]

                if selected["type"] == "Audio":
                    confirm = input(f"🎵 Play '{selected['name']}'? (y/n): ").lower()
                    if confirm == 'y':
                        # Call the linker and pass the specific file path in the context
                        play_ctx = {"file_path": selected["path"], "colors": COLORS}
                        link_external_tool("MP3_Player", "media_engine.py", "run", play_ctx)
                else:
                    print(f"📍 Path: {selected['path']}")
                    input("[ Press Enter ]")
        elif cmd != 'N':
            break
# ==========================================================
# pythonOS MASTER KERNEL - FULL CONTROL VERSION
# ==========================================================
# ==========================================================
# pythonOS MASTER KERNEL - INTEGRATED VERSION
# ==========================================================

def smart_path_finder(filename):
    """Deep-scans all system sectors for missing files."""
    sys.__stdout__.write(f"{COLORS['10'][0]}🔍 AI Sector Scan: Searching for {filename}...{RESET}\n")
    search_dirs = []
    if os.name == 'nt':
        import ctypes
        drives = ['%s:\\' % d for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists('%s:\\' % d)]
        search_dirs.extend(drives)
    else:
        search_dirs = [os.path.expanduser('~'), '/storage/emulated/0']

    for directory in search_dirs:
        try:
            for path in glob.iglob(os.path.join(directory, "**", filename), recursive=True):
                return path
        except: continue
    return None

def shell_bridge():
    """Bypasses OS logic to talk directly to the System Kernel."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("🐚 KERNEL SHELL BRIDGE", extra_info="Type 'exit' to return")
    while True:
        cwd = os.getcwd()
        cmd = input(f"{COLORS['10'][0]}{cwd} >{RESET} ").strip()
        if cmd.lower() in ['exit', 'quit', 'back']: break
        if not cmd: continue
        try:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            if stdout: print(f"{COLORS['7'][0]}{stdout}{RESET}")
            if stderr: print(f"{COLORS['1'][0]}{stderr}{RESET}")
        except Exception as e: print(f"❌ Bridge Failure: {e}")

def universal_executor(file_path):
    """Handles both Media playback and Python Plugin execution."""
    if not file_path or not os.path.exists(file_path):
        filename = os.path.basename(file_path) if file_path else "Unknown"
        file_path = smart_path_finder(filename)
        if not file_path:
            print(f"{COLORS['1'][0]}❌ Error: File not found in any sector.{RESET}")
            return

    ext = os.path.splitext(file_path)[1].lower()

    # OS Context: The 'Handshake' for Plugins
    ctx = {
        "file_path": file_path,
        "colors": COLORS,
        "psutil": psutil,
        "print_header": print_header,
        "BOLD": BOLD,
        "RESET": RESET,
        "finder": smart_path_finder
    }

    if ext == '.py':
        print(f"{COLORS['10'][0]}⚙️ Executing Plugin: {os.path.basename(file_path)}{RESET}")
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("dynamic_mod", file_path)
            plugin = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin)
            if hasattr(plugin, 'run'):
                plugin.run(ctx)
            else:
                print(f"{COLORS['1'][0]}❌ Error: run(ctx) missing in plugin.{RESET}")
        except Exception as e:
            print(f"💥 Plugin Crash: {e}")
    elif ext in ['.mp3', '.wav', '.mp4']:
        # Calls your external media_engine script
        try:
            import media_engine
            media_engine.run(ctx)
        except ImportError:
            print(f"{COLORS['1'][0]}❌ media_engine.py not found in OS root.{RESET}")

    input(f"\n{BOLD}[ Press Enter to return to OS ]{RESET}")

def feature_integrated_explorer():
    """Merged Scanner for Media and Python Scripts."""
    print_header("📁 Intelligence Explorer")
    target = input("📂 Enter Path to Scan (Enter for current): ").strip() or "."

    items = []
    for root, _, files in os.walk(target):
        for f in files:
            if f.lower().endswith(('.mp3', '.py', '.wav', '.mp4')):
                items.append(os.path.join(root, f))

    if not items:
        print("Sector Empty."); time.sleep(1); return

    # Display results
    for i, path in enumerate(items[:20]):
        color = COLORS['10'][0] if path.endswith('.py') else COLORS['6'][0]
        print(f"[{i}] {color}{os.path.basename(path)}{RESET}")

    choice = input("\n🎯 Select ID to Execute or [S]hell: ").strip()
    if choice.lower() == 's':
        shell_bridge()
    elif choice.isdigit() and int(choice) < len(items):
        universal_executor(items[int(choice)])

# --- MAIN LOOP REDIRECTION ---
# Ensure your choice 'I' calls feature_integrated_explorer()
# Ensure your choice 'S' or another key calls shell_bridge()

# In pythonOS_29.py
ctx = {
    "colors": COLORS,
    "print_header": print_header,
    "psutil": psutil,
    "finder": smart_path_finder, # Make sure this line exists!
    "RESET": RESET,
    "BOLD": BOLD
}
# version pythonOScmd103 base pythonOS70
# ==========================================================
# CHANGELOG / UPDATE LOG
# ==========================================================
# added enchanced display stats to upper screen
# Version 14 - Enhanced Display Mode layout work and font rendering improvements
# Added Enhnaced Display Mode with improved font rendering and color accuracy for terminals that support advanced ANSI codes. This mode optimizes the visual experience by utilizing 24-bit color and enhanced character sets, providing a richer and more vibrant interface. Users can toggle this mode from the Command Center using option U, allowing for a more immersive pythonOS experience on compatible terminals.
# Version 15 - Text & Document Center
# Added Text & Document Center with a built-in text editor and document viewer supporting various formats, including .txt, .md, .pdf, and .docx. The editor features syntax highlighting for code files, markdown preview, and basic formatting tools. The document viewer can render PDFs and Word documents directly in the terminal using ASCII art and supports navigation through pages and sections. This module is accessible via Command Center option T and provides a comprehensive solution for managing text and documents within the pythonOS environment.
# Version 16 - Earth & Moon Animation
# Version 17 - Graphing Calculator & ASCII Plotting I'll replace the ScienceConsole class with the improved version that includes NumPy integration, variable storage, rolling calculations, and enhanced UI features
# Added a powerful Graphing Calculator module with support for plotting functions, parametric equations, and
# polar graphs using ASCII characters. The calculator includes a full CAS (Computer Algebra System) for symbolic math, equation solving, differentiation, and integration. It also supports statistics functions like mean, median, mode, standard deviation, and regression analysis. The graphing interface allows users to input mathematical expressions and see them visualized in the terminal with adjustable axes and scaling. This module is accessible via Command Center option S and provides a robust tool for mathematical exploration directly within the pythonOS environment.
# Version 18 - Media Scanner & Player Integration
# The Graphing Calculator is now fully integrated and operational script now has the best Python graphing calculator with ASCII plotting, CAS, statistics, and more - all built right in! . Just launch pythonOScmd and press [S] from the Command Center.
# This update enhances the Media Scanner by integrating it with an external terminal-based MP3 player.
# The Media Scanner now allows users to browse their filesystem for audio files and play them directly from
# the terminal. The player supports common audio formats like MP3, WAV, FLAC, OGG, M4A, and AAC.
# The scanner displays found audio files in a paginated list, allowing users to select and play files using available terminal players
# such as mpv, ffplay, play (SoX), or mplayer. If no player is found, the user is prompted to install one.
# The Media Scanner also includes error handling for invalid directories and permission issues during file discovery.
# The new terminal MP3 player is accessible via the Media Menu option I, providing a seamless experience for audio playback within the pythonOS environment.
# Version 19 - Deep Probe AI & Heuristic Intelligence
# This update introduces the Deep Probe AI module, which leverages OpenAI's GPT-4
# to analyze system data and provide insights, recommendations, and automated actions.
# The AI Probe collects system metrics, process info, network stats, and hardware details,
# then sends this data to the OpenAI API for analysis. The AI can suggest optimizations,
# identify potential issues, and even execute certain actions based on heuristic evaluations.
# The Heuristic Intelligence Layer uses the AI's insights to adjust system settings automatically.
# For example, if the AI detects high CPU load, it can suggest enabling mini view or
# disabling blinking to improve performance. If thermal throttling is detected, it can
# truncate the thermal display to reduce overhead. The AI can also monitor for zombie processes
# and recommend cleanup actions.
# The AI Probe is accessible via Command Center option D, and the Autonomous System Optimizer
# runs in the background to apply heuristic adjustments based on system conditions.
# Version 20 - Command Center & Remote Dashboard
# This update introduces the Command Center, a centralized hub for accessing all features and tools in the
# script. The Command Center provides a live system identity clock, quick toggles for display and performance settings, and a menu-driven interface to launch any module. It also saves your display configuration for consistency across sessions.
# The Remote Dashboard is a new web-based interface that displays real-time system stats, logs,
# Version 21 - Command Center Expansion & Satellite Tracker
# This update focuses on expanding the Command Center with more features and adding a new Satellite Tracker module.
# The Satellite Tracker includes a live map powered by PyPredict, TLE updates, target selection,
# station location settings, and status/health info. Track up to 5 satellites simultaneously with real-time position data and visualizations.
# I also restructured the Command Center to make more of the script's capabilities accessible
# directly from the menu, and converted several single-shot tools into full menus for better
# integration and user experience.
# The Remote Dashboard now includes a WebSSH terminal panel, health checks, and a JSON stats endpoint for better backend integration. The new Autonomous System Optimizer runs in the background to adjust settings based on system load and conditions.
# Added Command Center option R with the new Satellite Tracker, including the PyPredict-powered
# live map, TLE update, target selection, station location (QTH) settings, and status/health info.
# The tracker implementation is in
# Expanded the Command Center submenus so more of the script’s capabilities are accessible
# from each menu, and added cross-links to the Download Center/AI Probe/DB API where it made sense.
# The bigger change is converting several single-shot tools into full menus (browser, disk I/O,
# security audit, environment/hardware/latency/weather/traffic, and remote dashboard),
# plus a few new actions in existing menus like process details/terminate and download-center shortcuts
# Added WebSSH health checks and auto-connect URL building for the dashboard, plus a JSON
# stats endpoint so the backend can serve data in JSON or HTML. The Remote Dashboard now
# reports WebSSH install/running status, avoids a broken iframe when it is down, and builds
# a connection URL using the current host and user to help the terminal auto-connect.
# See the new WebSSH helpers and status fields in
# Version 21.1 - Autonomous System Optimizer & WebSSH Terminal
# Added the new Autonomous System Optimizer that runs in the background and uses
# heuristics to adjust settings like mini view, thermal display, and blinking based
# on system load and conditions. It also tries to refresh weather data if it's unavailable.
# See pythonOScmd.py:3000-3060 for the new optimizer thread and logic.
# Added an embedded WebSSH terminal panel next to the Active Cache card, while
# keeping the existing dashboard layout. The terminal iframe uses a configurable
# WEBSSH_URL (defaults to http://localhost:8888) so you can point it at your WebSSH instance.
# Added a simple command execution form to the Remote Dashboard and a /cmd POST handler that
# runs the command and returns output in the browser. I also included a WebSSH info block with
# a link to the project. This all lives in the dashboard handler at
# Expanded the Remote Dashboard to include much more of the script’s data: host/IP, OS/arch,
# uptime, CPU cores/threads, RAM totals, swap, disk totals, load average, average temp, process
# count, Python version, network packet counts, and DB log/cache stats. See the updated stats builder and HTML in
# Added the new “Python Power” wrapper with 6 submenus, lightweight demos, and optional install
# prompts for required libs. It’s wired into Command Center option Q and uses minimal new helpers
# in the same section as the PWN tools wrapper. See pythonOScmd.py:2800-3018 for the new wrapper
# and pythonOScmd.py:6206-6214 for the Command Center hook
# # Added a shared _db_connect() with busy_timeout and moved all SQLite usage into
# context-managed blocks so operations commit safely and reduce lock contention.
# I also added plugin sandboxing (restricted context toggle) and runtime/error
# logging for plugin load/run events in pythonOScmd.py, including automatic error log files on failures.
# now saves your display config
# 2-5-26 Added Download Center 8 AM
# 2-5-25 Updated Download Center to do updates one at a time
# Updated AI probing logic
# 2-5-24 Added AI Probing and Weather Display
# 2-5-23 Added Calendar and Latency Probe
# 2-5-22 Added Hardware Serials and Environment Probe
# 2-5-21 Added Security Audit and Network Toolkit
# 2-5-20 Added Defence Center and Pentest Toolkit
# 2-5-19 Added Remote Dashboard and Plugin Center
# 2-5-18 Added Media Scanner and Display FX Test







def main():
    """Launch Textual-first Command Center, falling back to classic if needed."""
    run_pytextos(return_to_classic=False)


if __name__ == "__main__":
    main()
