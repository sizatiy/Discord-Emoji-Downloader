#!/bin/bash
# This is an example for users who want to run it on Linux/Mac
# (Not officially supported, but could work)

echo "Discord Emoji Downloader - Quick Start"
echo "======================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

# Install requirements
pip3 install -r requirements.txt

# Run the script
python3 emoji_downloader.py
