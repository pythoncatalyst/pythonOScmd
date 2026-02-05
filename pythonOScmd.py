#pythonOS By Ahmed Dragonclaw Suche Orangatang Washington Sayyed
#ATerminal Operating System that gives you an easy way to control you computer with a easy interface.
#Iincluded a lot of basic computer data to display right of the bat and some power tools.
#It will even runs video in terminal with full color support in ascii!
#Option 3 and 13 is the most like a T.V. I will be #explanding this and this will be updated.
#There is a fix in need to make in Command Center in Option 9 and selection 2.
#When iuse control c the whole OS quits. Need to change to another key.
#Code Starts Below. .py at end of pythonOS and run if not alredy there
#pythonOS - simple command line OS that I made so that I use on my PC to
#monitor the computer, view stats of a remote computer
#With the option of using SSH to another computer pythonOS.py
#-*- coding: utf-8 -*-
#Simple System Monitor By: Ahmed Sayyed
import sys
import subprocess
import os
import time
import ctypes # Added for Admin/Root probing
import calendar # Added for AI/Calendar expansion

# --- SELF-HEALING DEPENDENCY CHECK (UPDATED) ---
def boot_loader():
    # Fix for UnicodeEncodeError: Force UTF-8 encoding for stdout if possible
    if sys.stdout.encoding != 'utf-8':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 1. Define required libraries
    required = {'psutil', 'requests', 'beautifulsoup4', 'Pillow', 'gputil'}
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
                else:
                    sys.modules[lib] = MockModule()

# Run the bootloader before importing the main libraries
boot_loader()

# --- ORIGINAL CODE STARTS HERE (UNTOUCHED LOGIC) ---
import platform
import psutil
import socket
import uuid
import datetime
import threading
import random
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import GPUtil
import re # Added for Visual FX Regex

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

# Global weather cache for live ticker
weather_cache = {"temp": "N/A", "icon": "☁️", "humidity": "N/A", "wind": "N/A"}

def get_current_color():
    standard, blink, name = COLORS[active_color_key]
    return blink if is_blinking else standard

def draw_bar(pct):
    width = 15
    filled = int(width * pct / 100)
    bar = BOX_CHARS["BAR"] * filled + "░" * (width - filled)
    return f"{bar} {pct}%"

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
        return weather_cache
    except:
        # Fallback to wttr.in if Open-Meteo fails
        try:
            res = requests.get("https://wttr.in/?format=%C+%t", timeout=5).text.strip()
            weather_cache["temp"] = res.split()[-1]
            return weather_cache
        except: return None

def feature_weather_display():
    print_header("🌍 Global Weather Station")
    print("🔍 Querying Open-Meteo & National Weather Service...")
    data = get_weather_data()

    if data:
        print(f"\n {BOLD}📍 Current Location:{RESET} {data['city']}")
        print(f" {BOLD}🌡️ Temperature:   {RESET} {data['icon']} {data['temp']} (Feels like {data['feels']})")
        print(f" {BOLD}💧 Humidity:      {RESET} {data['humidity']}")
        print(f" {BOLD}💨 Wind Speed:    {RESET} {data['wind']}")

        # External Planning Links
        print_header("🗺️ Detailed Planning & Radar")
        print(f" > {BOLD}🌬️ Windy.com:{RESET}     https://www.windy.com")
        print(f" > {BOLD}🌦️ Weather Under:{RESET}  https://www.wunderground.com")
        print(f" > {BOLD}📺 The Weather Ch:{RESET} https://weather.com")

        try:
            # Quick ASCII graph from wttr.in for visual flair
            full_report = requests.get(f"https://wttr.in/{data['city']}?0&m&q", timeout=5).text
            print("\n" + full_report)
        except: pass
    else:
        print(f" {COLORS['1'][0]}[!] 📡 Could not retrieve weather. Check connection.{RESET}")
    input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def _traffic_risk_from_weather(icon):
    if icon in ["🌧️", "⛈️", "❄️", "🌫️"]:
        return "HIGH"
    if icon in ["⛅", "🌤️"]:
        return "MODERATE"
    return "LOW"

def feature_traffic_report():
    print_header("🚦 Traffic Report")
    print("🔍 Using IP geolocation and weather to estimate traffic risk...")
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

    print(f"\n {BOLD}📍 Location:{RESET} {city}")
    print(f" {BOLD}🌦️ Weather Impact:{RESET} {icon}  Traffic Risk: {risk}")
    if data.get("temp"):
        print(f" {BOLD}🌡️ Temp:{RESET} {data.get('temp')} (Feels {data.get('feels', 'N/A')})")
    if data.get("wind"):
        print(f" {BOLD}💨 Wind:{RESET} {data.get('wind')}")

    print_header("🗺️ Live Traffic Links")
    print(" > https://www.bing.com/maps")
    print(" > https://www.google.com/maps")
    print(" > https://www.tomtom.com/traffic-index/")
    print(" > Microsoft.Maps.Traffic.TrafficManager(map)")

    if lat is not None and lon is not None:
        print_header("🗺️ ASCII Map Preview")
        report_lines = [
            "Traffic Report",
            f"Location: {city}",
            f"Weather: {icon}",
            f"Risk: {risk}",
        ]
        if data.get("temp"):
            report_lines.append(f"Temp: {data.get('temp')}")
        if data.get("feels"):
            report_lines.append(f"Feels: {data.get('feels')}")
        if data.get("wind"):
            report_lines.append(f"Wind: {data.get('wind')}")
        report_lines.extend([
            "",
            "Links:",
            "bing.com/maps",
            "google.com/maps",
            "tomtom.com/traffic-index",
            "Microsoft.Maps.Traffic",
        ])
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

    input(f"\n{BOLD}[ ⌨️ Press Enter to exit... ]{RESET}")

# --- AI & CALENDAR ADDITIONS ---

def feature_deep_probe_ai():
    print_header("🤖 AI Heuristics & Deep Probe")
    cpu_stress = psutil.cpu_percent(interval=0.5)
    mem_stress = psutil.virtual_memory().percent
    stress_score = (cpu_stress * 0.4) + (mem_stress * 0.4)

    verdict = f"{COLORS['2'][0]}OPTIMAL{RESET}"
    if stress_score > 80: verdict = f"{COLORS['1'][0]}CRITICAL STRESS{RESET}"
    elif stress_score > 50: verdict = f"{COLORS['4'][0]}MODERATE LOAD{RESET}"

    print(f" {BOLD}🧠 AI Predictive Verdict:{RESET}")
    print(f" > Stress Index: {stress_score:.1f}/100")
    print(f" > Health State:  {verdict}")

    print_header("💾 Kernel & Latency Probe")
    try:
        ctx = psutil.cpu_stats().ctx_switches
        zombies = len([p for p in psutil.process_iter() if p.status() == psutil.STATUS_ZOMBIE])
        print(f" > 🔄 Context Switches: {ctx:,}")
        print(f" > 🧟 Zombie Count:      {zombies}")
        proc = psutil.Process()
        handles = proc.num_handles() if os.name == 'nt' else proc.num_fds()
        print(f" > 🗝️ Active OS Handles: {handles}")
    except:
        print(" > 🚫 Deep Probe: Restricted by OS Kernel")
    input(f"\n{BOLD}[ ✅ Probe Finished. Press Enter... ]{RESET}")

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
                    results.append({"name": file, "path": os.path.join(root, file), "type": category})

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

    input(f"\n{BOLD}[ ✅ Sector Scan Complete. Press Enter... ]{RESET}")

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
        down_speed = (now_net.bytes_recv - last_net.bytes_recv) / 1024
        up_speed = (now_net.bytes_sent - last_net.bytes_sent) / 1024
        last_net = now_net

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

def feature_process_search():
    sort_by = 'memory_percent'
    target = ""

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_header("📑 Process Manager Sub-Menu")
        print(f"📊 Sorting by: {BOLD}{sort_by.replace('_', ' ').upper()}{RESET}")
        print(f"[1] 🔍 Search/List Once | [2] ⏱️ Live Monitor (2s Refresh) | [3] 🧠 Sort by Memory | [4] ⚙️ Sort by CPU | [5] ↩️ Return")

        proc_choice = input("\n🎯 Select: ").strip()

        if proc_choice == '5':
            break
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

                    input(f"\n{BOLD}[ ⌨️ Press Enter to return to Process Menu... ]{RESET}")
            except Exception as e:
                print(f"❌ Error: {e}")
                input(f"\n{BOLD}[ ⌨️ Press Enter to return... ]{RESET}")

def feature_disk_io_report():
    print_header("💽 Disk I/O Real-Time Report")
    last_io = psutil.disk_io_counters()
    time.sleep(1)
    now_io = psutil.disk_io_counters()
    read_speed = (now_io.read_bytes - last_io.read_bytes) / (1024 * 1024)
    write_speed = (now_io.write_bytes - last_io.write_bytes) / (1024 * 1024)
    print(f"📖 Read Speed:  {read_speed:.2f} MB/s")
    print(f"✍️ Write Speed: {write_speed:.2f} MB/s")
    print(f"📚 Total Read:  {now_io.read_bytes / (1024**3):.2f} GB")
    print(f"📝 Total Write: {now_io.write_bytes / (1024**3):.2f} GB")
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
        print(f"[5] ↩️ Return to Main Menu")
        net_choice = input("\n🎯 Select a tool (1-5): ").strip()
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
        elif net_choice == '5': break

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
        print(f" {BOLD}[7]{RESET} ↩️ Return to Main Menu")
        wifi_choice = input(f"\n{BOLD}🎯 Select WiFi Tool (1-7): {RESET}").strip()

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
        print(f" {BOLD}[6]{RESET} Return to Main Menu")
        bt_choice = input(f"\n{BOLD}Select Bluetooth Tool (1-6): {RESET}").strip()

        if bt_choice == '6':
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
        print(f" {BOLD}[6]{RESET} ↩️ Return to Main Menu")
        ai_choice = input(f"\n{BOLD}🎯 Select A.I. Service (1-6): {RESET}").strip()

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
            break

def feature_security_audit():
    print_header("🛡️ Security & Port Audit")
    common_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389]
    print(f"📡 Scanning {len(common_ports)} common entry points on localhost...")
    found_any = False
    for port in common_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.1)
            if s.connect_ex(('127.0.0.1', port)) == 0:
                print(f" {COLORS['1'][0]}[!] ⚠️ OPEN:{RESET} Port {port}")
                found_any = True
    if not found_any: print(f" {COLORS['2'][0]}[+] ✅ No standard high-risk ports open locally.{RESET}")
    print_header("👤 Security Context")
    is_admin = False
    try: is_admin = os.getuid() == 0
    except: is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    print(f"👑 Admin/Root Privileges: {'YES' if is_admin else 'NO'}")
    input(f"\n{BOLD}[ ✅ Audit Complete. Press Enter... ]{RESET}")

def feature_environment_probe():
    print_header("📂 Environment & Path Probe")
    print(f"📁 Current Working Dir: {os.getcwd()}")
    print(f"🏠 User Home Dir:       {os.path.expanduser('~')}")
    print(f"🐍 Python Executable:   {sys.executable}")
    print_header("📊 System Metadata")
    print(f"🔤 Default Encoding:    {sys.getdefaultencoding()}")
    print(f"🗂️ Filesystem Encoding: {sys.getfilesystemencoding()}")
    input(f"\n{BOLD}[ ✅ Probe Complete. Press Enter... ]{RESET}")

def feature_hardware_serials():
    print_header("📟 Low-Level Hardware Identity")
    if os.name == 'nt':
        try:
            bios = subprocess.check_output("wmic bios get serialnumber").decode().split('\n')[1].strip()
            print(f"🔢 BIOS Serial:         {bios}")
        except: print("🔢 BIOS Serial:         Access Denied")
    print_header("🗄️ All Mounted Partitions")
    for part in psutil.disk_partitions():
        print(f"💾 Device: {part.device:<10} | 📍 Mount: {part.mountpoint:<10} | 📂 Type: {part.fstype}")
    input(f"\n{BOLD}[ ✅ Hardware Probe Finished. Press Enter... ]{RESET}")

def feature_latency_probe():
    print_header("⏱️ Latency & Geo Probe")
    target = input("⌨️ Enter IP or Domain to probe (e.g. 8.8.8.8): ").strip()
    if not target: return

    print(f"📡 Probing {target}...")
    try:
        # 1. Geo Check via Public API
        geo_res = requests.get(f"http://ip-api.com/json/{target}", timeout=5).json()
        if geo_res.get('status') == 'success':
            print(f" {BOLD}📍 Location:{RESET} {geo_res.get('city')}, {geo_res.get('country')} ({geo_res.get('isp')})")

        # 2. Latency Test
        param = '-n' if os.name == 'nt' else '-c'
        print(f"📡 Running Ping...")
        output = subprocess.check_output(['ping', param, '4', target]).decode()
        print(output)
    except Exception as e:
        print(f"❌ Error: {e}")
    input(f"\n{BOLD}[ ✅ Probe Finished. Press Enter... ]{RESET}")

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

    context = {
        "psutil": psutil,
        "os": os,
        "socket": socket,
        "requests": requests,
        "print_header": print_header,
        "COLORS": COLORS,
        "BOLD": BOLD,
        "RESET": RESET,
    }

    try:
        plugin.run(context)
    except Exception as e:
        print(f"[💥 Plugin Runtime Error] {e}")

    input("\n[ ⌨️ Press Enter to return... ]")

# ========================================
# REMOTE SYSTEM DASHBOARD (SIMPLE HTTP)
# Duplicates display to browser with auto-refresh
# ========================================

from http.server import BaseHTTPRequestHandler, HTTPServer

DASHBOARD_PORT = 8088
dashboard_server = None
dashboard_display_cache = ""

def get_dashboard_stats():
    """Collect system statistics"""
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    cpu = psutil.cpu_percent(interval=0.2)
    net = psutil.net_io_counters()
    gpu, fan = get_advanced_hardware_stats()
    battery = psutil.sensors_battery()

    return {
        "cpu": cpu,
        "ram": mem.percent,
        "disk": disk.percent,
        "disk_free": disk.free / (1024**3),
        "net_sent": net.bytes_sent / (1024**2),
        "net_recv": net.bytes_recv / (1024**2),
        "gpu": gpu,
        "fan": fan,
        "weather": weather_cache,
        "battery": battery.percent if battery else 0,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

class DashboardHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

    def do_GET(self):
        """Serve dashboard with current stats"""
        stats = get_dashboard_stats()
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
                .stats {{ display:grid; grid-template-columns:repeat(3, 1fr); gap:20px; margin-bottom:30px; }}
                .stat-card {{ background:#1a1a1a; border:1px solid #0f0; padding:15px; }}
                .stat-label {{ color:#888; font-size:12px; margin-bottom:5px; }}
                .stat-value {{ color:#0f0; font-size:24px; font-weight:bold; }}
                .bar {{ background:#333; height:10px; margin:10px 0; border-radius:2px; overflow:hidden; }}
                .bar-fill {{ background:#0f0; height:10px; transition:width 0.3s; }}
                .timestamp {{ color:#888; font-size:12px; margin-top:20px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🖥️ pythonOS Remote Dashboard</h1>
            </div>

            <div class="stats">
                <div class="stat-card">
                    <div class="stat-label">CPU Usage</div>
                    <div class="stat-value">{stats['cpu']:.1f}%</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['cpu']}%"></div></div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">RAM Usage</div>
                    <div class="stat-value">{stats['ram']:.1f}%</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['ram']}%"></div></div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Disk Usage</div>
                    <div class="stat-value">{stats['disk']:.1f}%</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['disk']}%"></div></div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Free Space</div>
                    <div class="stat-value">{stats['disk_free']:.2f} GB</div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">Battery</div>
                    <div class="stat-value">{stats['battery']:.1f}%</div>
                    <div class="bar"><div class="bar-fill" style="width:{stats['battery']}%"></div></div>
                </div>

                <div class="stat-card">
                    <div class="stat-label">GPU</div>
                    <div class="stat-value">{stats['gpu']}</div>
                </div>
            </div>

            <div style="border-top:1px solid #0f0; padding-top:15px;">
                <p>📡 Net Sent: {stats['net_sent']:.2f} MB</p>
                <p>⬇️ Net Recv: {stats['net_recv']:.2f} MB</p>
                <p>🌡️ Weather: {stats['weather'].get('icon','')} {stats['weather'].get('temp','N/A')}</p>
                <p>🌀 Fan: {stats['fan']}</p>
            </div>

            <div class="timestamp">Last update: {stats['timestamp']}</div>
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
    print_header("🖥️ Remote System Dashboard")
    start_dashboard()

    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "localhost"

    print(f"📡 Dashboard running at: {COLORS['4'][0]}http://{ip}:{DASHBOARD_PORT}{RESET}")
    print(f"🌐 Open this in your browser on this network.")
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
        print(" [5] Return to Main Menu")

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

# --- MAIN OPERATING SYSTEM LOOP ---

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
        print(f"📏 Total RAM:       {mem.total / (1024**3):.2f} GB")
        print(f"🔓 Available RAM:   {mem.available / (1024**3):.2f} GB")
        print(f"📈 RAM Usage:       {draw_bar(mem.percent)}")
        print(f"🔄 Swap Total:      {swap.total / (1024**3):.2f} GB")
        print_header("💽 Storage & Disk")
        disk = psutil.disk_usage('/')
        print(f"📏 Total Space:     {disk.total / (1024**3):.2f} GB")
        print(f"📈 Used Space:      {draw_bar(disk.percent)} ({disk.used / (1024**3):.2f} GB)")
        print(f"🔓 Free Space:      {disk.free / (1024**3):.2f} GB")
        print_header("🌐 Network & IDs")
        hostname = socket.gethostname()
        print(f"📛 Hostname:         {hostname}")
        try: print(f"📍 Local IP:         {socket.gethostbyname(hostname)}")
        except: print("📍 Local IP:          Unknown")
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
        print(f"🆔 MAC Address:     {mac}")
        net_io = psutil.net_io_counters()
        print(f"⬆️ Data Sent:       {net_io.bytes_sent / (1024**2):.2f} MB")
        print(f"⬇️ Data Received:   {net_io.bytes_recv / (1024**2):.2f} MB")
        print_header("🐍 Python Context")
        print(f"🐍 Python Version:  {platform.python_version()}")
        print_header("🔮 Miscellaneous")
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
        uptime = datetime.datetime.now() - boot_time
        print(f"🏁 System Boot:     {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️ Uptime:          {str(uptime).split('.')[0]}")
        battery = psutil.sensors_battery()
        if battery:
            status = "🔌 Charging" if battery.power_plugged else "🔋 Discharging"
            print(f"🔋 Battery:           {battery.percent}% ({status})")
        print(f"\n{get_current_color()}--- ✅ REPORT COMPLETE ---{RESET}")

    stop_clock = False
    threading.Thread(target=live_system_identity_clock, daemon=True).start()

    c = get_current_color()
    print(f"\n{BOLD}{c}{BOX_CHARS['TL']}{BOX_CHARS['H']*24} 🌍 COMMAND CENTER {BOX_CHARS['H']*24}{BOX_CHARS['TR']}{RESET}")
    print(f" {BOLD}[1]{RESET} ✨ Blink: {'ON ' if is_blinking else 'OFF'}  {BOLD}[2]{RESET} 🌡️ Temp: {temp_unit}      {BOLD}[3]{RESET} 🌡️ Thermal: {'Short' if truncated_thermal else 'Full '}")
    print(f" {BOLD}[4]{RESET} 📏 Mini: {'ON ' if mini_view else 'OFF'}   {BOLD}[5]{RESET} 🚪 Exit         {BOLD}[6]{RESET} 🎨 Color Scheme")
    print(f" {BOLD}[7]{RESET} 🌐 Web Browser   {BOLD}[8]{RESET} 💽 Disk I/O    {BOLD}[9]{RESET} 📑 Processes    {BOLD}[0]{RESET} 🌐 Network")
    print(f" {BOLD}[10]{RESET} 🔌 Plugin Center   {BOLD}[11]{RESET} 🖥️ Remote Dashboard")
    print(f" {BOLD}[A]{RESET} 🛡️ Audit Sec     {BOLD}[B]{RESET} 📂 Env Probe   {BOLD}[C]{RESET} 📟 HW Serials   {BOLD}[D]{RESET} 🤖 AI Probe     {BOLD}[E]{RESET} 📅 Calendar")
    print(f" {BOLD}[F]{RESET} ⏱️ Latency Probe {BOLD}[G]{RESET} 🌍 Weather       {BOLD}[H]{RESET} 🔡 Display FX   {BOLD}[I]{RESET} 🎞️ Media Scan")
    print(f" {BOLD}[J]{RESET} 📡 WiFi Toolkit   {BOLD}[K]{RESET} 🤖 A.I. Center   {BOLD}[L]{RESET} Bluetooth   {BOLD}[M]{RESET} Traffic")
    print(f"{BOLD}{c}{BOX_CHARS['BL']}{BOX_CHARS['H']*64}{BOX_CHARS['BR']}{RESET}")

    choice = input(f"{BOLD}🎯 Select an option (0-M): {RESET}").strip().upper()
    stop_clock = True

    if choice == '1': is_blinking = not is_blinking
    elif choice == '2': temp_unit = "F" if temp_unit == "C" else "C"
    elif choice == '3': truncated_thermal = not truncated_thermal
    elif choice == '4': mini_view = not mini_view
    elif choice == '5': break
    elif choice == '6':
        print("\n--- 🎨 SELECT COLOR ---")
        for k, v in COLORS.items(): print(f"[{k}] {v[0]}{v[2]}{RESET}")
        color_choice = input("🎯 Select color number or [R]: ").strip().upper()
        if color_choice in COLORS: active_color_key, user_has_chosen = color_choice, True
        elif color_choice == 'R': user_has_chosen = False
    elif choice == '7':
        url = input("🌐 Enter URL [google.com]: ").strip() or "https://www.google.com"
        if not url.startswith('http'): url = 'https://' + url
        show_img = input("🖼️ Load images as Color ASCII? (y/n): ").strip().lower() == 'y'
        try:
            res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            for s in soup(["script", "style"]): s.extract()
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
                for l in lines: content_list.append(("TXT", l))
            for i in range(0, len(content_list), 15):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_header("🌐 Browser", extra_info=url)
                for type, val in content_list[i:i+15]:
                    if type == "TXT": print(val)
                    else:
                        for line in val: print(line)
                input("\n[ 📑 Next Page... ]")
        except Exception as e: print(f"❌ Error: {e}"); time.sleep(2)
    elif choice == '8': feature_disk_io_report()
    elif choice == '9': feature_process_search()
    elif choice == '10':feature_plugin_center()
    elif choice == '11':feature_remote_dashboard()
    elif choice == '0': feature_network_toolkit()
    elif choice == 'A': feature_security_audit()
    elif choice == 'B': feature_environment_probe()
    elif choice == 'C': feature_hardware_serials()
    elif choice == 'D': feature_deep_probe_ai()
    elif choice == 'E': feature_simple_calendar()
    elif choice == 'F': feature_latency_probe()
    elif choice == 'G': feature_weather_display()
    elif choice == 'H': feature_test_font_size()
    elif choice == 'I': feature_media_menu()
    elif choice == 'J': feature_wifi_toolkit()
    elif choice == 'K': feature_ai_center()
    elif choice == 'L': feature_bluetooth_toolkit()
    elif choice == 'M': feature_traffic_report()

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

# --- USER-CONTROLLED BACKGROUND OPTIMIZER ---
def start_autonomous_monitor():
    print(f"\n{COLORS['10'][0]}[🤖 AI] Would you like to enable the Autonomous Optimizer?{RESET}")
    print("   (Automatically adjusts UI, Power, and Thermal settings based on load)")
    choice = input(f"{BOLD}🎯 Enable AI-Assisted Management? (y/n): {RESET}").strip().lower()

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

# Trigger the prompt
start_autonomous_monitor()
# --- HEURISTIC INTELLIGENCE LAYER ---
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

# Inject the Heuristic check into the main loop by wrapping the start
apply_heuristic_intelligence()

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

# version pythonOScmd9 base
