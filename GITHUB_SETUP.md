# GitHub Setup Instructions

## Quick Setup (5 minutes)

### 1. Create GitHub Repository

Go to: https://github.com/new

**Settings:**
- Repository name: `wicked-tiktok-analysis`
- Description: `Data science analysis of what made Wicked songs go viral on TikTok using Spotify API and machine learning`
- Visibility: **Public** (for portfolio visibility)
- ✅ Add README file: **NO** (we already have one)
- ✅ Add .gitignore: **NO** (already included)
- ✅ Choose a license: **MIT License** (or your preference)

### 2. Push Your Code

After creating the repository, run these commands:

```bash
cd /Users/isfarbaset/Documents/wicked-tiktok-analysis

# Add the GitHub remote
git remote add origin https://github.com/isfarbaset/wicked-tiktok-analysis.git

# Push your code
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages (Optional)

To host the project website on GitHub Pages:

1. Go to: `https://github.com/isfarbaset/wicked-tiktok-analysis/settings/pages`
2. Under "Source", select: `main` branch, `/` (root) folder
3. Click "Save"
4. Your site will be live at: `https://isfarbaset.github.io/wicked-tiktok-analysis/`

### 4. Update Portfolio Link (Optional)

If you enable GitHub Pages, you can update the portfolio link to point directly to the hosted site instead of the repo.

---

## Important: Protect Your Credentials

Before pushing, make sure `spotify_config.py` is in `.gitignore` (it already is!).

Your credentials will NOT be pushed to GitHub. ✅

---

## Verification

After pushing, verify:
- ✅ Code is visible on GitHub
- ✅ README displays correctly
- ✅ No sensitive credentials exposed
- ✅ All visualizations and data files are included

Your project is now publicly available for portfolio showcasing! 🎉
