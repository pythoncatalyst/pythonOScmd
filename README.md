# What It Is
# A monolithic "Terminal Operating System" — essentially a mega-menu TUI application that bundles dozens of features: system monitoring, media playback (ASCII video, MP3 streaming), security/pentest tools, satellite tracking, AI probing, a graphing calculator, a file manager, a web dashboard, plugin management, and more. It's ambitious and creative — a personal project.


**A Unified Terminal Operating System** — 54,000+ lines of Python powering a fully self-contained TUI with 500+ tools for system monitoring, security, media, AI analytics, and more.

```
╔══════════════════════════════════════════════════════════╗
║            pythonOScmd — Terminal OS v26                  ║
║     "Where code and creativity intertwine"               ║
╚══════════════════════════════════════════════════════════╝
```

## Features

### System Monitoring & Diagnostics
- Real-time CPU, memory, disk, and thermal sensor readouts
- Hardware diagnostics with visual bar graphs
- Autonomous system optimizer and efficiency indexing
- Deep Probe AI analytics

### Network & Connectivity
- WiFi toolkit and Bluetooth scanning
- Network diagnostics and connectivity tools
- Remote web dashboard
- Server/client bridge

### Security & Penetration Testing
- Penetration testing toolkit
- Defence and protection systems
- Security scanning and auditing

### Media & Entertainment
- Full-color ASCII video playback in the terminal
- Media scanner and lounge
- Audio playback support (pygame)

### AI & Physics Engine (pyAI)
- Built-in physics and math accelerator
- Rocket delta-v, orbital mechanics, ballistic calculations
- Aerodynamics (drag, lift, Reynolds number, Bernoulli)
- Thermodynamics, radar/sonar equations, and more
- NumPy / SciPy / SymPy integration (optional)

### Developer Tools
- Plugin system with sandboxed execution
- PWN tools and Python power utilities
- Download center and package management
- Graphing calculator

### Weather & Space
- Weather and environmental monitoring
- Satellite and orbital tracking

### Display Modes
- **Textual TUI** — Rich interactive dashboard with multiple layouts (requires `textual`)
- **Classic Command Center** — Works on any terminal, no extra dependencies
- **Minimal Mode** — Ultra-fast startup via `PYTHONOS_FAST_START` env var

## Installation

### From PyPI

```bash
pip install pythonoscmd
```

### From Source

```bash
git clone https://github.com/ahmedsayyed/pythonoscmd.git
cd pythonoscmd
pip install .
```

### Optional Dependencies

Install the full experience with all features enabled:

```bash
pip install pythonoscmd[full]
```

Or install only the core:

```bash
pip install pythonoscmd[minimal]
```

| Dependency group | Packages |
|---|---|
| **Core** | `requests`, `beautifulsoup4`, `psutil` |
| **Full** | Core + `Pillow`, `rich`, `textual`, `pygments`, `numpy` |
| **Minimal** | `requests`, `beautifulsoup4` |

## Usage

After installation, three entry points are available:

```bash
pythonoscmd          # Full terminal OS
pythonos             # Alias (shorter)
pos                  # Quick alias
```

Or run the script directly:

```bash
python pythonOScmd.py
```

### Command-Line Flags

| Flag | Description |
|---|---|
| `--classic` | Launch in classic command center mode |
| `--textual` | Launch in Textual TUI mode |
| `--fast` | Minimal mode, skip initialization |

### Environment Variables

| Variable | Description |
|---|---|
| `PYTHONOS_FAST_START` | Set to any value to bypass all initialization and launch the minimal classic interface instantly |

## Architecture

pythonOScmd is a **completely self-contained** single-file application. On first run it automatically extracts embedded modules:

| Extracted File | Purpose |
|---|---|
| `logger_system.py` | Advanced centralized logging with rotation, JSON output, and analysis |
| `pyAI.py` | Physics & math accelerator plugin |
| `plugin_system.py` | Plugin management, validation, sandboxing, and dependency resolution |

### Code Sections

| # | Section | Description |
|---|---|---|
| 1 | Imports & Core Dependencies | Standard library and optional package imports |
| 2 | Configuration & Constants | System-wide settings and configuration |
| 3 | Core System Utilities | Boot loader, audio initialization |
| 4 | Database & Logging System | Complete logging suite with rotation |
| 5 | UI & Display System | Colors, visual effects, headers |
| 6 | Weather & Environmental Monitoring | Weather data and environmental tools |
| 7 | Satellite & Orbital Tracking | Orbital mechanics and satellite tracking |
| 8 | Network & Connectivity | WiFi, Bluetooth, network tools |
| 9 | Security & Penetration Testing | Security tooling suite |
| 10 | Defence & Protection Systems | Defensive security measures |
| 11 | Media & Entertainment | ASCII video player, media scanner |
| 12 | Hardware Monitoring & Diagnostics | CPU, memory, thermal sensors |
| 13 | AI & Analytics | Deep Probe AI, autonomous optimizer |
| 14 | System Management Tools | System administration utilities |
| 15 | Web & Remote Dashboard | Web-based remote dashboard |
| 16 | Plugin System & Extensibility | Plugin loading and sandboxing |
| 17 | Download Center & Package Management | Package installation tools |
| 18 | Developer Tools | PWN tools, Python power |
| 19 | Integration & Bridge Functions | Cross-module integration |
| 20 | Main Application Logic | Primary application flow |
| 21 | Startup & Initialization | Boot sequence and entry points |

### Plugin System

Plugins are Python files placed in `~/.pythonos/plugins/` or `pythonOS_data/plugins/`. Each plugin is:

1. **Discovered** — scanned and metadata extracted
2. **Validated** — syntax checked, metadata verified, size limits enforced
3. **Loaded** — imported with optional sandboxing
4. **Executed** — called through a registered entry point

Plugins support dependency resolution, checksums, and a restricted-builtins sandbox mode.

### Failsafe System

Every feature has an intelligent fallback chain. If a feature fails (e.g., Textual not installed), the system automatically degrades to the next available alternative — all the way down to a minimal command-line interface.

## Project Structure

```
pythonOScmdSUPER/
├── pythonOScmd.py          # Main application (self-contained, 54k+ lines)
├── logger_system.py        # Extracted: centralized logging
├── plugin_system.py        # Extracted: plugin management
├── _core.py                # Core helpers
├── pyproject.toml          # Build configuration (PEP 621)
├── LICENSE                 # MIT License
├── run.sh                  # Quick launch script
├── de421.bsp               # JPL ephemeris for satellite tracking
├── pythonOS_data/          # Runtime data, swap files, API modules
├── plugins/                # User plugins directory
├── programs/               # Additional program modules
```

## Requirements

- **Python** >= 3.9
- **OS**: Linux, macOS (Windows supported with limited features)

## License

MIT License — see [LICENSE](LICENSE) for details.

## Author

**Ahmed Sayyed**

---

> *"By the power of Python, I summon forth the Terminal OS! Let it be a realm of endless possibilities, where code and creativity intertwine. May it run with the speed of light and the wisdom of ages. So mote it be!"*
