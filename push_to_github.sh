#!/bin/bash

echo "🎭 Wicked TikTok Analysis - GitHub Setup"
echo "========================================"
echo ""

# Check if repository exists on GitHub
echo "📋 Step 1: Create GitHub Repository"
echo ""
echo "Please go to: https://github.com/new"
echo ""
echo "Repository Settings:"
echo "  - Name: wicked-tiktok-analysis"
echo "  - Description: Data science analysis of what made Wicked songs go viral on TikTok"
echo "  - Visibility: Public ✅"
echo "  - ❌ DO NOT initialize with README, .gitignore, or license (we have them)"
echo ""
read -p "Press ENTER after you've created the repository on GitHub..."

echo ""
echo "📤 Step 2: Pushing Code to GitHub"
echo ""

# Push to GitHub
git branch -M main
echo "Pushing code to GitHub..."

if git push -u origin main; then
    echo ""
    echo "✅ SUCCESS! Your project is now on GitHub!"
    echo ""
    echo "🌐 Repository URL: https://github.com/isfarbaset/wicked-tiktok-analysis"
    echo ""
    echo "📋 Next Steps (Optional):"
    echo "  1. Enable GitHub Pages:"
    echo "     → Go to: https://github.com/isfarbaset/wicked-tiktok-analysis/settings/pages"
    echo "     → Source: main branch, / (root)"
    echo "     → Your site will be at: https://isfarbaset.github.io/wicked-tiktok-analysis/"
    echo ""
    echo "  2. Add topics/tags to your repo for discoverability:"
    echo "     → data-science, spotify-api, tiktok, machine-learning, python"
    echo ""
    echo "  3. Update your portfolio site and push those changes too!"
    echo ""
else
    echo ""
    echo "❌ Push failed. Common issues:"
    echo "  1. Repository doesn't exist on GitHub yet"
    echo "  2. Need to authenticate - may need Personal Access Token"
    echo "  3. Repository URL is incorrect"
    echo ""
    echo "To create a Personal Access Token:"
    echo "  → Go to: https://github.com/settings/tokens"
    echo "  → Generate new token (classic)"
    echo "  → Select: repo (full control)"
    echo "  → Use this token as your password when pushing"
    echo ""
fi
