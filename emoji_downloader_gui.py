import sys
import os
import traceback

if __name__ == "__main__":
    try:
        import tkinter as tk
        from tkinter import messagebox
    except Exception as e:
        print(f"Error importing tkinter: {e}")
        traceback.print_exc()
        sys.exit(1)

    try:
        import aiohttp
    except Exception as e:
        print(f"Error importing aiohttp: {e}")
        traceback.print_exc()
        sys.exit(1)

    from pathlib import Path
    import asyncio
    import threading

class EmojiDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Discord Emoji Downloader")
        self.root.geometry("550x620")
        self.root.resizable(False, False)
        
        # Modern color scheme
        self.bg_color = "#0f1419"
        self.secondary_bg = "#1e2228"
        self.primary_color = "#5865F2"
        self.accent_color = "#43b581"
        self.text_color = "#ffffff"
        self.muted_color = "#72767d"
        self.root.configure(bg=self.bg_color)
        
        # Main container
        container = tk.Frame(root, bg=self.bg_color)
        container.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        # Title
        title = tk.Label(container, text="Discord Emoji Downloader", 
                        font=("Segoe UI", 22, "bold"), bg=self.bg_color, fg=self.text_color)
        title.pack(pady=(0, 8))
        
        # Subtitle
        subtitle = tk.Label(container, text="Download all custom emojis from your Discord server", 
                           font=("Segoe UI", 9), bg=self.bg_color, fg=self.muted_color)
        subtitle.pack(pady=(0, 25))
        
        # ===== TOKEN SECTION =====
        token_header_frame = tk.Frame(container, bg=self.bg_color)
        token_header_frame.pack(fill=tk.X, pady=(0, 8))
        
        token_label = tk.Label(token_header_frame, text="Discord Token", 
                              font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg=self.text_color)
        token_label.pack(side=tk.LEFT)
        
        token_help = tk.Label(token_header_frame, text="ℹ️ How to get?", 
                             font=("Segoe UI", 8, "underline"), bg=self.bg_color, fg=self.primary_color,
                             cursor="hand2")
        token_help.pack(side=tk.RIGHT)
        token_help.bind("<Button-1>", lambda e: self.show_token_help())
        
        self.token_entry = tk.Entry(container, font=("Segoe UI", 11), show="•", 
                                    bg=self.secondary_bg, fg=self.text_color, bd=0, 
                                    highlightthickness=2, highlightcolor=self.primary_color, 
                                    highlightbackground="#2c2f33", insertbackground=self.primary_color)
        self.token_entry.pack(fill=tk.X, pady=(0, 18), ipady=11)
        
        # ===== SERVER ID SECTION =====
        server_header_frame = tk.Frame(container, bg=self.bg_color)
        server_header_frame.pack(fill=tk.X, pady=(0, 8))
        
        server_label = tk.Label(server_header_frame, text="Server ID", 
                               font=("Segoe UI", 11, "bold"), bg=self.bg_color, fg=self.text_color)
        server_label.pack(side=tk.LEFT)
        
        server_help = tk.Label(server_header_frame, text="ℹ️ How to get?", 
                              font=("Segoe UI", 8, "underline"), bg=self.bg_color, fg=self.primary_color,
                              cursor="hand2")
        server_help.pack(side=tk.RIGHT)
        server_help.bind("<Button-1>", lambda e: self.show_server_help())
        
        self.server_id_entry = tk.Entry(container, font=("Segoe UI", 11), 
                                        bg=self.secondary_bg, fg=self.text_color, bd=0, 
                                        highlightthickness=2, highlightcolor=self.primary_color,
                                        highlightbackground="#2c2f33", insertbackground=self.primary_color)
        self.server_id_entry.pack(fill=tk.X, pady=(0, 22), ipady=11)
        
        # Download button
        self.download_btn = tk.Button(container, text="Download Emojis", 
                                     command=self.start_download,
                                     font=("Segoe UI", 12, "bold"), 
                                     bg=self.primary_color, fg="white", 
                                     bd=0, highlightthickness=0, 
                                     padx=20, pady=13, cursor="hand2",
                                     activebackground="#4752c4", activeforeground="white")
        self.download_btn.pack(fill=tk.X, pady=(0, 15))
        
        # Progress bar background
        progress_bg = tk.Frame(container, bg=self.secondary_bg, height=6)
        progress_bg.pack(fill=tk.X, pady=(0, 15), ipady=3)
        progress_bg.pack_propagate(False)
        
        # Progress bar
        self.progress_bar = tk.Frame(progress_bg, bg=self.accent_color, height=6)
        self.progress_bar.pack(side=tk.LEFT)
        self.progress_bar.pack_propagate(False)
        self.progress_width = 0
        
        # Status section
        status_frame = tk.Frame(container, bg=self.secondary_bg)
        status_frame.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)
        
        # Status label
        self.status_label = tk.Label(status_frame, text="Ready to download", 
                                    font=("Segoe UI", 10), bg=self.secondary_bg, fg=self.muted_color)
        self.status_label.pack(anchor=tk.W, pady=(5, 0))
        
        # Info label
        self.info_label = tk.Label(status_frame, text="", 
                                  font=("Segoe UI", 9), bg=self.secondary_bg, fg=self.muted_color)
        self.info_label.pack(anchor=tk.W, pady=(2, 5))
    
    def show_token_help(self):
        help_text = """How to get your Discord Token:

1. Open Discord in your web browser
2. Press F12 to open Developer Tools
3. Go to Console tab
4. Paste: window.localStorage.token.replaceAll('"', '')
5. Copy the token that appears

⚠️ Keep your token SECRET! Never share it!"""
        messagebox.showinfo("How to Get Token", help_text)
    
    def show_server_help(self):
        help_text = """How to get your Server ID:

1. Right-click on your Discord server name
2. Click "Copy Server ID"
3. Paste it in the Server ID field

Note: Developer Mode must be enabled in Discord settings!"""
        messagebox.showinfo("How to Get Server ID", help_text)
    
    def update_progress(self, current, total):
        """Update progress bar"""
        if total > 0:
            percentage = (current / total)
            self.progress_width = int(percentage * 500)
        self.progress_bar.config(width=max(self.progress_width, 2))
        self.root.update()
    
    def update_status(self, message, info=""):
        """Update status labels"""
        self.status_label.config(text=message)
        self.info_label.config(text=info)
        self.root.update()
    
    def start_download(self):
        """Start download in a separate thread"""
        token = self.token_entry.get().strip()
        server_id = self.server_id_entry.get().strip()
        
        if not token:
            messagebox.showerror("Missing Token", "Please paste your Discord token!")
            return
        
        if not server_id:
            messagebox.showerror("Missing Server ID", "Please enter the server ID!")
            return
        
        self.update_status("Connecting to Discord...", "")
        self.download_btn.config(state=tk.DISABLED)
        self.progress_width = 0
        
        thread = threading.Thread(target=self.download_thread, args=(token, server_id))
        thread.daemon = True
        thread.start()
    
    def download_thread(self, token, server_id):
        """Run the download in a thread"""
        try:
            asyncio.run(self.download_emojis(token, server_id))
        except Exception as e:
            self.update_status(f"Error: {str(e)[:50]}...", "")
        finally:
            self.download_btn.config(state=tk.NORMAL)
    
    async def download_emojis(self, token, server_id):
        """Download all emojis from a server"""
        
        headers = {"Authorization": token}
        
        async with aiohttp.ClientSession() as session:
            try:
                # Get guild info
                guild_url = f"https://discord.com/api/v10/guilds/{server_id}"
                async with session.get(guild_url, headers=headers) as resp:
                    if resp.status == 401:
                        self.update_status("Error: Invalid token!", "Check your Discord token")
                        messagebox.showerror("Error", "Invalid token! Check your Discord token.")
                        return
                    elif resp.status == 403:
                        self.update_status("Error: No permission!", "You can't access this server")
                        messagebox.showerror("Error", "You don't have permission to access this server.")
                        return
                    elif resp.status == 404:
                        self.update_status("Error: Server not found!", "Check the server ID")
                        messagebox.showerror("Error", f"Could not find server with ID: {server_id}")
                        return
                    elif resp.status != 200:
                        self.update_status(f"Error: {resp.status}", "")
                        return
                    
                    guild_data = await resp.json()
                    guild_name = guild_data.get("name", "unknown")
                
                # Get emojis from guild
                emoji_url = f"https://discord.com/api/v10/guilds/{server_id}/emojis"
                async with session.get(emoji_url, headers=headers) as resp:
                    if resp.status != 200:
                        self.update_status(f"Error fetching emojis", "")
                        return
                    
                    emojis = await resp.json()
                
                if not emojis:
                    self.update_status("No emojis found", "This server has no custom emojis")
                    messagebox.showinfo("Info", "No emojis found in this server.")
                    return
                
                # Create folder for emojis on Desktop
                desktop = Path.home() / "Desktop"
                safe_guild_name = "".join(c for c in guild_name if c not in '<>:"|?*')
                emoji_folder = desktop / f"emojis_{safe_guild_name}"
                emoji_folder.mkdir(exist_ok=True)
                
                # Download each emoji
                downloaded = 0
                failed = 0
                
                for i, emoji in enumerate(emojis):
                    try:
                        emoji_name = emoji.get("name", "unknown")
                        emoji_id = emoji.get("id")
                        is_animated = emoji.get("animated", False)
                        
                        extension = "gif" if is_animated else "png"
                        emoji_url = f"https://cdn.discordapp.com/emojis/{emoji_id}.{extension}"
                        
                        filename = emoji_folder / f"{emoji_name}.{extension}"
                        
                        async with session.get(emoji_url) as resp:
                            if resp.status == 200:
                                with open(filename, 'wb') as f:
                                    f.write(await resp.read())
                                downloaded += 1
                            else:
                                failed += 1
                        
                        # Update progress
                        self.update_progress(i + 1, len(emojis))
                        self.update_status(f"Downloading... {i + 1}/{len(emojis)}", 
                                         f"Downloaded: {downloaded} | Failed: {failed}")
                    
                    except Exception:
                        failed += 1
                
                # Success message
                msg = f"Successfully downloaded {downloaded} emojis!\n\n📁 Saved to:\n{emoji_folder}"
                if failed > 0:
                    msg += f"\n\n⚠️ Failed: {failed}"
                
                self.update_progress(len(emojis), len(emojis))
                self.update_status(f"Complete! {downloaded}/{len(emojis)} emojis", "Click folder button to open")
                messagebox.showinfo("Success", msg)
            
            except Exception as e:
                self.update_status(f"Error: {str(e)[:50]}...", "")

def main():
    try:
        root = tk.Tk()
        app = EmojiDownloaderGUI(root)
        root.mainloop()
    except Exception as e:
        error_msg = f"Error starting application:\n\n{str(e)}\n\n{traceback.format_exc()}"
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Application Error", error_msg)
        except:
            pass
        sys.exit(1)

if __name__ == "__main__":
    main()
