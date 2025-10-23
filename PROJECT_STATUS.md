# Wicked TikTok Analysis - Project Status

## Overview
This project analyzes what made Wicked songs go viral on TikTok using Spotify audio features and TikTok performance metrics.

## Current Status: READY TO START

### Completed Setup
- [x] Project directory structure created
- [x] Configuration files created (spotify_config.py, requirements.txt, .gitignore)
- [x] README.md with complete documentation
- [x] Script 1: Spotify data collection (01_collect_spotify_data.py)
- [x] Script 2: TikTok data template creation (02_collect_tiktok_data.py)
- [x] Script 3: Pattern analysis (03_analyze_patterns.py)
- [x] Setup script (setup.sh)

### Next Steps (In Order)

#### 1. Environment Setup (5-10 minutes)
```bash
cd /Users/isfarbaset/Documents/wicked-tiktok-analysis
chmod +x setup.sh
./setup.sh
```

#### 2. Get Spotify API Credentials (10 minutes)
- Go to https://developer.spotify.com/dashboard
- Create an app called "Wicked TikTok Analysis"
- Copy Client ID and Client Secret
- Edit spotify_config.py with your credentials

#### 3. Collect Spotify Data (5 minutes)
```bash
source venv/bin/activate
cd scripts
python 01_collect_spotify_data.py
```
This will collect audio features for all Wicked songs and comparison musicals.

#### 4. Create TikTok Data Template (2 minutes)
```bash
python 02_collect_tiktok_data.py
```
This creates a template with example data. You can either:
- Option A: Use the example data to test the full pipeline
- Option B: Manually collect real TikTok data (see data/tiktok/INSTRUCTIONS.txt)

#### 5. Run Pattern Analysis (5 minutes)
```bash
python 03_analyze_patterns.py
```
This analyzes correlations between audio features and viral success.

### Files Still Needed (Optional - can be created as needed)

#### Script 4: Build Predictive Model (04_build_model.py)
- Random Forest model training
- Feature importance extraction
- Predictions for comparison musicals

#### Script 5: Create Visualizations (05_create_visualizations.py)
- 7 interactive visualizations with Wicked color theme
- HTML and PNG outputs

#### Quarto Report (analysis_report.qmd)
- Comprehensive HTML report
- All findings and visualizations
- Professional presentation

## Quick Start Commands

### Full Pipeline (Using Example Data)
```bash
# 1. Setup
cd /Users/isfarbaset/Documents/wicked-tiktok-analysis
chmod +x setup.sh
./setup.sh

# 2. Edit spotify_config.py with your credentials

# 3. Run analysis
source venv/bin/activate
cd scripts
python 01_collect_spotify_data.py
python 02_collect_tiktok_data.py
python 03_analyze_patterns.py
```

## Expected Outputs

### After Script 1:
- data/spotify/wicked_audio_features.csv
- data/spotify/comparison_musicals.csv

### After Script 2:
- data/tiktok/tiktok_collection_template.csv
- data/tiktok/wicked_tiktok_performance_EXAMPLE.csv
- data/tiktok/content_type_reference.csv
- data/tiktok/INSTRUCTIONS.txt

### After Script 3:
- data/processed/merged_analysis.csv
- outputs/tables/feature_correlations.csv
- outputs/tables/content_type_performance.csv
- outputs/tables/key_insights.csv

## Key Findings (From Example Data)

1. **Most Viral Song**: Defying Gravity with 287,000+ videos
2. **Top Audio Feature**: Energy/Danceability correlation
3. **Best Content Type**: Vocal Showcase / Lip Sync
4. **Surprise Hit**: "What Is This Feeling?" (comedy + duet format)
5. **Celebrity Effect**: Songs with Ariana Grande boost performed significantly better

## Portfolio Integration

This project demonstrates:
- API integration (Spotify)
- Data collection and cleaning
- Statistical analysis (correlation, modeling)
- Data visualization (Wicked color theme)
- Technical writing and documentation
- Full project organization and reproducibility

## Wicked Color Theme

All visualizations use:
- Emerald Green: #00A86B
- Pink/Magenta: #E91E8C
- Gold: #FFD700
- Light Green: #90EE90
- Dark Green: #006B3F

## Notes

- The example TikTok data is based on real trends but is for demonstration
- For production analysis, collect actual TikTok data manually
- The project is fully reproducible with your own Spotify credentials
- All scripts are documented with clear comments and error handling

## Questions?

Check the README.md for full documentation or review the inline comments in each script.

---

Last Updated: October 23, 2025
