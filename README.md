# 🎣 PHISHX - Ultimate Phishing Framework

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS%20%7C%20Termux-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-GPL%20v3-red?style=for-the-badge">
  <img src="https://img.shields.io/github/stars/zeennxx/phishx?style=for-the-badge">
  <img src="https://img.shields.io/github/forks/zeennxx/phishx?style=for-the-badge">
</p>

<p align="center">
  <b>🚀 The Most Advanced Open-Source Phishing Framework</b><br>
  <i>20 Templates •  Website Cloning • Cross-Platform • Auto-Tunneling</i>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-templates">Templates</a> •
  <a href="#-contact">Contact</a> •
  <a href="#-license">License</a> •
</p>

---
<p align="center">
  <strong> DISCLAIMER </strong>
</p>

<p align="center">

*Any actions and or activities related to **PHISHX** is solely your responsibility. The misuse of this toolkit can result in **criminal charges** brought against the persons in question. **The contributors will not be held responsible** in the event any criminal charges be brought against any individuals misusing this toolkit to break the law.*

*This toolkit contains materials that can be potentially damaging or dangerous for social media. Refer to the laws in your province/country before accessing, using, or in any other way utilizing this in a wrong way.*

***This Tool is made for educational purposes only.** Do not attempt to violate the law with anything contained here. **If this is your intention, then Get the hell out of here!***

*It only demonstrates "how phishing works". You shall not misuse the information to gain unauthorized access to someone's social media. However you may try this out at your own risk.*

---

## 🔥 Features

### 🎯 **20 Templates**

```
├─ Facebook (email/pass)      ├─ Instagram (user/pass)    ├─ Google (2-step)
├─ Twitter/X (text/pass)      ├─ LinkedIn (prof)          ├─ GitHub (dev)
├─ Microsoft (enterprise)     ├─ Netflix (streaming)      ├─ Spotify (music)
├─ Amazon (e-commerce)        ├─ Apple ID (minimal)       ├─ PayPal (finance)
├─ Discord (gaming)           ├─ Telegram Web (phone)     ├─ WhatsApp Web (QR)
├─ Snapchat (multi)           ├─ TikTok (viral)           ├─ Reddit (community)
├─ Pinterest (visual)         ├─ Yahoo (mail)             └─ + Custom URL Clone
```

### 🌐 **Website Cloning Engine**

```
• Clone ANY website with single command
• Preserves original CSS, JavaScript, and images
• Automatic asset downloading (CSS, JS, images, fonts)
• Works with modern frameworks (React, Vue, Angular)
• Maintains original site functionality and appearance
```

### 🚇 **Advanced Auto-Tunneling**

```
• Cloudflared integration (no configuration needed)
• Auto-downloads appropriate version for your platform
• Generates public HTTPS URLs instantly
• No port forwarding or router configuration required
• Automatic fallback to localhost if tunnel fails
```

### 🕵️ **Stealth Data Capture**

```
• Zero notification to victim during submission
• Silent AJAX form processing
• Automatic redirect to legitimate website after capture
• Captures: IP address, User-Agent, Timestamp, All form data
• Saves credentials in readable JSON format with metadata
```

### 💻 **Universal Compatibility**

```
✅ Windows 7/8/10/11     ✅ Kali Linux          ✅ Ubuntu/Debian
✅ Arch Linux            ✅ macOS (Intel/M1/M2) ✅ Termux (Android)
✅ Raspberry Pi          ✅ Any VPS             ✅ Python 3.6+ environment
```

### 🔄 **Auto-Recovery System**

```
• Self-healing mechanism on crash
• Automatic port conflict resolution
• Retry failed connections (3x attempts)
• Memory optimization and cache cleanup
• Persistent uptime with minimal intervention
```

### ⚡ **Performance**

```
• Startup Time: < 2 seconds
• Clone Speed: 3-10 seconds per website
• Concurrent Users: 50+ threads supported
• Memory Usage: ~50MB average
• Disk Space: ~100MB for all templates
```

---

## 🚀 Installation

### 📦 **Method 1: Clone & Run**

```bash
# Clone the repository
git clone --depth=1 https://github.com/zeennxx/phishx.git

# Enter directory
cd phishx

# Run (dependencies auto-install)
python phishx.py
```

### 📱 **Method 2: Termux (Android)**

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone --depth=1 https://github.com/zeennxx/phishx.git
cd phishx
python phishx.py
```

### 🪟 **Method 3: Windows**

```powershell
# Download Python 3.8+ from python.org first
git clone https://github.com/zeennxx/phishx.git
cd phishx
pip install requests
python phishx.py
```

### 🐳 **Method 4: Docker**

```bash
docker pull zeennxx/phishx:latest
docker run -it --rm -p 8080:8080 zeennxx/phishx
```

### 🔧 **Method 5: Direct Download**

```bash
# Linux/macOS
wget https://raw.githubusercontent.com/zeennxx/phishx/main/phishx.py
python phishx.py

# Windows (PowerShell)
Invoke-WebRequest -Uri https://raw.githubusercontent.com/zeennxx/phishx/main/phishx.py -OutFile phishx.py
python phishx.py
```

---

## 📂 Templates

| # | Platform | Type | Captured Fields |
|---|----------|------|-----------------|
| 1 | Facebook | Social | email, password |
| 2 | Instagram | Social | username, password |
| 3 | Google | Email | email, password |
| 4 | Twitter/X | Social | text, password |
| 5 | LinkedIn | Professional | session_key, session_password |
| 6 | GitHub | Dev | login, password |
| 7 | Microsoft | Email | loginfmt, passwd |
| 8 | Netflix | Streaming | userLoginId, password |
| 9 | Spotify | Music | username, password |
| 10 | Amazon | E-commerce | email, password |
| 11 | Apple ID | Tech | accountName, password |
| 12 | PayPal | Finance | email, password |
| 13 | Discord | Social | email, password |
| 14 | Telegram Web | Messaging | phone, password |
| 15 | WhatsApp Web | Messaging | qr_scan |
| 16 | Snapchat | Social | username, password |
| 17 | TikTok | Social | username, password |
| 18 | Reddit | Social | username, password |
| 19 | Pinterest | Social | id, password |
| 20 | Yahoo | Email | username, password |
| 21 | Custom | Any | Any (auto-detected) |

---

## 📞 Contact

### **Author:** zennx

• <img src="https://img.icons8.com/ios-filled/50/ffffff/github.png" width="16"> **GitHub:** [@zeennxx](https://github.com/zeennxx)

• <img src="https://facebook.com/favicon.ico" width="16"> **Facebook:** [@Zennnxx](https://web.facebook.com/Zennnxx/)

---

### Community Guidelines

```
✅ Ask questions about usage
✅ Report bugs and issues
✅ Share ideas for improvements
✅ Help other community members
❌ No discussions about illegal activities
❌ No sharing of captured data
❌ No harassment or toxic behavior
```

---

## ⚠️ Disclaimer

```
╔══════════════════════════════════════════════════════════════╗
║                    IMPORTANT LEGAL NOTICE                    ║
╚══════════════════════════════════════════════════════════════╝

This tool is for EDUCATIONAL and DEMONSTRATION purposes ONLY.

• Use ONLY on systems you OWN or have EXPLICIT PERMISSION to test
• Unauthorized use is ILLEGAL and UNETHICAL
• The author assumes NO LIABILITY for any misuse
• You are SOLELY RESPONSIBLE for your actions
• By using this software, you agree to these terms

Permitted Use:
✓ Authorized security audits
✓ Educational demonstrations
✓ Personal learning
✓ Testing your own systems

Prohibited Use:
✗ Any illegal activity
✗ Unauthorized access
✗ Stealing credentials
✗ Violating any laws
```

---

## 🌟 Show Your Support

<p align="center">
  <b>If PHISHX has helped you, don't forget to show some love! ❤️</b>
</p>

<p align="center">
  <a href="https://github.com/zeennxx/phishx/stargazers">
    <img src="https://img.shields.io/github/stars/zeennxx/phishx?style=for-the-badge&logo=github&color=yellow&label=STARS" alt="GitHub stars">
  </a>
  <a href="https://github.com/zeennxx/phishx/network/members">
    <img src="https://img.shields.io/github/forks/zeennxx/phishx?style=for-the-badge&logo=github&color=blue&label=FORKS" alt="GitHub forks">
  </a>
  <a href="https://github.com/zeennxx/phishx/watchers">
    <img src="https://img.shields.io/github/watchers/zeennxx/phishx?style=for-the-badge&logo=github&color=green&label=WATCHERS" alt="GitHub watchers">
  </a>
</p>

<p align="center">
  <a href="https://github.com/zeennxx/phishx/issues">
    <img src="https://img.shields.io/github/issues/zeennxx/phishx?style=for-the-badge&logo=github&color=red&label=ISSUES" alt="GitHub issues">
  </a>
  <a href="https://github.com/zeennxx/phishx/pulls">
    <img src="https://img.shields.io/github/issues-pr/zeennxx/phishx?style=for-the-badge&logo=github&color=orange&label=PULL%20REQUESTS" alt="GitHub pull requests">
  </a>
  <a href="https://github.com/zeennxx/phishx/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/zeennxx/phishx?style=for-the-badge&logo=gnu&color=red&label=LICENSE" alt="License">
  </a>
</p>

---

<p align="center">
  
## 📢 Spread the Word

<p align="center">
  <b>Share PHISHX with the world! 🌎</b>
</p>

<p align="center">
  <a href="https://twitter.com/intent/tweet?text=Check%20out%20PHISHX%20-%20The%20most%20advanced%20open-source%20phishing%20framework!%20%F0%9F%8E%A3%0A%0Ahttps%3A//github.com/zeennxx/phishx">
    <img src="https://img.shields.io/badge/Tweet-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
  </a>
  <a href="https://www.facebook.com/sharer/sharer.php?u=https://github.com/zeennxx/phishx">
    <img src="https://img.shields.io/badge/Share-1877F2?style=for-the-badge&logo=facebook&logoColor=white">
  </a>
  <a href="https://www.reddit.com/submit?url=https://github.com/zeennxx/phishx&title=PHISHX%20-%20Ultimate%20Phishing%20Framework">
    <img src="https://img.shields.io/badge/Post-FF4500?style=for-the-badge&logo=reddit&logoColor=white">
  </a>
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/zeennxx/phishx">
    <img src="https://img.shields.io/badge/Share-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white">
  </a>
</p>

<p align="center">
  <b>Or copy this link:</b><br>
  <code>https://github.com/zeennxx/phishx</code>
</p>

---

## 🏆 Top Contributors

<p align="center">
  <a href="https://github.com/zeennxx/phishx/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=zeennxx/phishx" alt="Contributors">
  </a>
</p>

<p align="center">
  <i>Join these amazing people who made PHISHX better!</i>
</p>

---

## 🔔 Stay Updated

<p align="center">
  <a href="https://github.com/zeennxx/phishx/subscription">
    <img src="https://img.shields.io/badge/Watch-Notifications-red?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="https://github.com/zeennxx">
    <img src="https://img.shields.io/badge/Follow%20@zeennxx-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="https://web.facebook.com/Zennnxx/">
    <img src="https://img.shields.io/badge/Follow%20on%20Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white">
  </a>
</p>

---

## ⭐ Star History

<a href="https://www.star-history.com/?repos=zeennxx%2Fphishx&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=zeennxx/phishx&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=zeennxx/phishx&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=zeennxx/phishx&type=date&legend=top-left" />
 </picture>
</a>

---

## 💝 Support with a Star

<p align="center">
  <b>One star = One motivation to keep updating! ⭐</b>
</p>

<p align="center">
  <a href="https://github.com/zeennxx/phishx">
  </a>
</p>

<p align="center">
  <a href="https://github.com/zeennxx/phishx">
    <img src="https://img.shields.io/badge/⭐-CLICK%20TO%20STAR-yellow?style=for-the-badge&logo=github&logoColor=black&labelColor=white&color=yellow" width="200">
  </a>
</p>

---

## 📜 License

**GNU General Public License v3.0**

```
Copyright (C) 2026 zennx (https://github.com/zeennxx)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
```

---

## 🙏 Credits

```text
• Cloudflare - For cloudflared tunneling
• Python Community - For awesome libraries
• All Contributors - Who help improve this tool
• GitHub - For hosting and community
```

---

<p align="center">
  <b>Made with ❤️ by zennx</b><br>
  <i>Copyright © 2026 | All rights reserved</i>
</p>
