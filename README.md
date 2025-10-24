# What Made Wicked Go Viral 
## A Retrospective Data Analysis Study

A complete data science project analyzing what audio features and cultural factors drove Wicked's viral success on TikTok following the November 2024 movie release.

## Project Overview

This project uses real TikTok performance data to understand what makes musical theatre songs go viral. By analyzing Spotify audio features alongside actual TikTok metrics, we discover which characteristics truly matter for virality.

## Key Features

- Spotify API integration for audio feature collection
- TikTok performance analysis (video counts, trends, content types)
- Statistical correlation analysis
- Random Forest predictive modeling
- Interactive visualizations with Wicked color theme
- Professional Quarto report

## Quick Start

```bash
# Clone repository
git clone [your-repo-url]
cd wicked-tiktok-analysis

# Install dependencies
pip install -r requirements.txt

# Set up Spotify API credentials
# Edit spotify_config.py with your credentials

# Run analysis scripts in order
python scripts/01_collect_spotify_data.py
python scripts/02_collect_tiktok_data.py  # Creates template - fill manually
python scripts/03_analyze_patterns.py
python scripts/04_build_model.py
python scripts/05_create_visualizations.py

# Generate report
quarto render analysis_report.qmd
```

## Project Structure

```
wicked-tiktok-analysis/
├── data/                           # All data files
│   ├── spotify/                    # Spotify audio features
│   ├── tiktok/                     # TikTok performance data
│   └── processed/                  # Processed/merged data
├── scripts/                        # Analysis scripts
│   ├── 01_collect_spotify_data.py
│   ├── 02_collect_tiktok_data.py
│   ├── 03_analyze_patterns.py
│   ├── 04_build_model.py
│   └── 05_create_visualizations.py
├── outputs/                        # Generated outputs
│   ├── figures/                    # Visualizations (HTML & PNG)
│   └── tables/                     # Analysis tables
├── spotify_config.py               # API credentials
├── analysis_report.qmd             # Quarto report template
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Key Findings (Preview)

1. Defying Gravity dominated TikTok with 287,000+ videos
2. Energy and danceability showed strongest correlation with virality
3. Vocal showcase/lip sync was the most successful content format
4. Songs with celebrity boost performed significantly better
5. What Is This Feeling? was the biggest surprise hit (comedy/duet format)

## Requirements

- Python 3.8+
- Spotify Developer Account (free)
- Quarto (for report generation)

See requirements.txt for Python package dependencies.

## Data Collection Notes

**Spotify Data:** Fully automated via API

**TikTok Data:** Manual collection required due to API restrictions
- Template provided in scripts/02_collect_tiktok_data.py
- Example data included for reference
- Instructions in data/tiktok/INSTRUCTIONS.txt

## Visualizations

All visualizations use Wicked-themed colors:
- Emerald Green: #00A86B
- Pink/Magenta: #E91E8C
- Gold: #FFD700

Output formats:
- Interactive HTML (for web/presentation)
- High-resolution PNG (for papers/posters)

## Analysis Pipeline

1. **Data Collection** (Scripts 1-2)
   - Gather Spotify audio features
   - Collect TikTok performance metrics

2. **Pattern Analysis** (Script 3)
   - Correlation analysis
   - Content type performance
   - Surprise hit identification

3. **Predictive Modeling** (Script 4)
   - Train Random Forest model
   - Feature importance extraction
   - Test on comparison musicals

4. **Visualization** (Script 5)
   - 7 publication-quality visualizations
   - Interactive and static formats

5. **Reporting** (Quarto)
   - Comprehensive HTML report
   - All findings and insights
   - Reproducible analysis

## Portfolio Highlights

This project demonstrates:
- API integration (Spotify)
- Manual data collection methodology
- Statistical analysis (correlation, modeling)
- Machine learning (Random Forest)
- Data visualization (Plotly, Matplotlib)
- Technical writing (Quarto)
- Project organization

## Future Enhancements

- Automate TikTok data collection (if API access improves)
- Expand to more Broadway musicals
- Track longitudinal trends
- Add lyrics sentiment analysis
- Build web dashboard (Streamlit/Dash)

## License

This project is for educational and portfolio purposes.

## Contact

Isfar Baset  
[LinkedIn](https://www.linkedin.com/in/isfarbaset/)  
[GitHub](https://github.com/isfarbaset)

## Acknowledgments

- Spotify Web API for audio features
- TikTok community for trend data
- Wicked creative team for the amazing music

---

Last Updated: October 2025
