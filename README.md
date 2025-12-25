# Discord Emoji Downloader

A simple tool to backup all custom emojis from a Discord server using your user account token.

> **Perfect for:** Recovering lost emoji collections, backing up server emojis, or archiving custom emoji sets.

## Quick Start (Windows Users)

### Option 1: Simple (Recommended)
1. [Download the latest release](https://github.com/sizatiy/Discord-Emoji-Downloader/releases/tag/emojis) (`.exe` file)
2. Double-click the `.exe` file
3. Paste your Discord token
4. Paste your server ID
5. Done! Emojis appear on your Desktop

### Option 2: From Source
1. Clone this repo: `git clone https://github.com/sizatiy/Discord-Emoji-Downloader`
2. `cd discord-emoji-downloader`
3. `pip install -r requirements.txt`
4. `python emoji_downloader.py`

## Setup Instructions

### Step 1: Get Your Discord User Token

⚠️ **IMPORTANT SECURITY WARNING:**
- **NEVER share your token** - it gives full access to your Discord account
- **NEVER upload it to GitHub** or any public place
- If you leak it, change your Discord password immediately

**How to get your token:**

1. Open Discord in a web browser (discord.com)
2. Press `F12` to open Developer Tools
3. Go to the **Console** tab
4. Copy and paste this code:
   ```javascript
   (function() {
     let token = document.body.appendChild(document.createElement(`iframe`)).contentWindow.localStorage.token;
     console.log(token);
   })()
   ```
5. Press Enter and copy the token that appears

### Step 2: Get Your Server ID

1. Enable Developer Mode in Discord:
   - Settings → App Settings → Advanced → Developer Mode (toggle ON)
2. Right-click on the server name
3. Click "Copy Server ID"

### Step 3: Run the Downloader

- **Windows (.exe):** Just double-click it
- **Python:** Run `python emoji_downloader.py`

Then paste your token and server ID when prompted.

## Where Are My Emojis?

All downloaded emojis go to your **Desktop** in a folder named:
```
emojis_[ServerName]_[ServerID]
```

Files are saved as:
- `.png` files for regular emojis
- `.gif` files for animated emojis

## Building Your Own .EXE (For Developers)

Want to create the `.exe` file yourself?

### Windows:
1. Clone the repo
2. Run `build_exe.bat`
3. Your `.exe` will be in the `dist` folder

### Requirements:
- Python 3.8+
- `pip install -r requirements.txt`

## Troubleshooting

| Error | Solution |
|-------|----------|
| **"Invalid token"** | Make sure you copied the ENTIRE token correctly. Tokens are very long strings. |
| **"Could not find server"** | Verify you've actually joined the server and the ID is correct. |
| **"No emojis found"** | The server doesn't have custom emojis, or you don't have permission to view them. |
| **.EXE won't run** | Your antivirus might block it. Try building it yourself with `build_exe.bat`. |

## How It Works

This tool:
- ✓ Only reads emoji data from your server
- ✓ Does NOT store your token anywhere
- ✓ Does NOT upload anything (except to Discord's API to verify your account)
- ✓ Runs entirely on your computer
- ✓ Saves emojis to your Desktop automatically

## Requirements

- **Windows users:** Just the `.exe` file (no installation needed!)
- **Python users:** Python 3.8+ and `pip install -r requirements.txt`

## License

MIT License - Use at your own risk. This is for personal emoji backup only.

## Disclaimer

This tool uses Discord's official API. Using your user token for automation may violate Discord's Terms of Service. Use at your own risk.

---

**Need help?** Open an issue or check the troubleshooting section above.
