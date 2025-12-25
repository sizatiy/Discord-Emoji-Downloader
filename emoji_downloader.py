import aiohttp
from pathlib import Path
import json
import os
from datetime import datetime

class EmojiDownloader:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": self.token
        }
        
    async def download_emojis(self, server_id):
        """Download all emojis from a server"""
        
        async with aiohttp.ClientSession() as session:
            try:
                # Get guild info
                guild_url = f"https://discord.com/api/v10/guilds/{server_id}"
                async with session.get(guild_url, headers=self.headers) as resp:
                    if resp.status == 401:
                        print("❌ Invalid token! Make sure you copied the entire token correctly.")
                        return
                    elif resp.status == 403:
                        print("❌ You don't have permission to access this server")
                        return
                    elif resp.status == 404:
                        print(f"❌ Could not find server with ID: {server_id}")
                        return
                    elif resp.status != 200:
                        print(f"❌ Error: {resp.status} - {await resp.text()}")
                        return
                    
                    guild_data = await resp.json()
                    guild_name = guild_data.get("name", "unknown")
                
                print(f"✓ Found server: {guild_name}")
                
                # Get emojis from guild
                emoji_url = f"https://discord.com/api/v10/guilds/{server_id}/emojis"
                async with session.get(emoji_url, headers=self.headers) as resp:
                    if resp.status != 200:
                        print(f"❌ Could not fetch emojis: {resp.status}")
                        return
                    
                    emojis = await resp.json()
                
                print(f"✓ Total emojis: {len(emojis)}")
                
                if not emojis:
                    print("⚠️  No emojis found in this server")
                    return
                
                # Create folder for emojis on Desktop
                desktop = Path.home() / "Desktop"
                # Clean up folder name (remove invalid characters)
                safe_guild_name = "".join(c for c in guild_name if c not in '<>:"|?*')
                emoji_folder = desktop / f"emojis_{safe_guild_name}_{server_id}"
                emoji_folder.mkdir(exist_ok=True)
                print(f"✓ Created folder: {emoji_folder}")
                
                # Download each emoji
                for emoji in emojis:
                    try:
                        emoji_name = emoji.get("name", "unknown")
                        emoji_id = emoji.get("id")
                        is_animated = emoji.get("animated", False)
                        
                        # Build emoji URL
                        extension = "gif" if is_animated else "png"
                        emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.{extension}"
                        
                        filename = emoji_folder / f"{emoji_name}.{extension}"
                        
                        # Download the emoji
                        async with session.get(emoji_url) as resp:
                            if resp.status == 200:
                                with open(filename, 'wb') as f:
                                    f.write(await resp.read())
                                print(f"  ✓ Downloaded: {emoji_name}.{extension}")
                            else:
                                print(f"  ❌ Failed to download {emoji_name} (status: {resp.status})")
                    
                    except Exception as e:
                        print(f"  ❌ Error downloading {emoji_name}: {e}")
                
                print(f"\n✅ All emojis downloaded to: {emoji_folder}")
            
            except Exception as e:
                print(f"❌ Error: {e}")

async def main():
    print("=" * 60)
    print("Discord Emoji Downloader")
    print("=" * 60)
    
    # Get token from user
    token = input("\n📋 Paste your Discord user token: ").strip()
    
    if not token:
        print("❌ Token cannot be empty!")
        return
    
    # Get server ID from user
    server_id = input("\n🏢 Enter the server ID: ").strip()
    
    if not server_id:
        print("❌ Server ID cannot be empty!")
        return
    
    print("\n⏳ Connecting to Discord...\n")
    
    # Create downloader and start
    downloader = EmojiDownloader(token)
    await downloader.download_emojis(server_id)
    
    print("\n" + "=" * 60)
    desktop = Path.home() / "Desktop"
    print(f"📁 Emoji folder is on your Desktop!")
    print("=" * 60)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
