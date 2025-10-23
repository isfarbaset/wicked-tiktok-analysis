#!/bin/bash

# Wicked TikTok Analysis - Quick Setup Script

echo "=================================="
echo "Wicked TikTok Analysis Setup"
echo "=================================="

# Create virtual environment
echo "\n1. Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "\n2. Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create data directories if they don't exist
echo "\n3. Setting up directory structure..."
mkdir -p data/spotify data/tiktok data/processed
mkdir -p outputs/figures outputs/tables

# Instructions
echo "\n=================================="
echo "Setup Complete!"
echo "=================================="
echo "\nNext steps:"
echo "1. Edit spotify_config.py with your Spotify API credentials"
echo "   Get them from: https://developer.spotify.com/dashboard"
echo ""
echo "2. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "3. Run the analysis scripts in order:"
echo "   python scripts/01_collect_spotify_data.py"
echo "   python scripts/02_collect_tiktok_data.py"
echo "   python scripts/03_analyze_patterns.py"
echo ""
echo "4. Check the README.md for full documentation"
echo "=================================="
