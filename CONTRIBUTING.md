# Development Guide

## Setting Up Your Development Environment

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/discord-emoji-downloader
cd discord-emoji-downloader
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
pip install pyinstaller  # For building EXE
```

## Testing Changes

Run the script directly:
```bash
python emoji_downloader.py
```

## Building the EXE

```bash
build_exe.bat
```

The `.exe` will be in the `dist` folder.

## Code Style

- Use clear variable names
- Add comments for complex logic
- Follow PEP 8 where possible
- Test on Windows before committing

## Making Pull Requests

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## Areas for Contribution

- Support for other platforms (Mac, Linux)
- Batch downloading from multiple servers
- GUI interface
- Better error handling
- Documentation improvements

Thanks for contributing! 🎉
