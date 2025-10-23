# 🎭 What Made Wicked Go Viral on TikTok?

**A Data-Driven Analysis of Musical Theatre Virality**

[![View Analysis](https://img.shields.io/badge/View-Analysis-00A86B?style=for-the-badge&logo=quarto)](./index.html)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Quarto](https://img.shields.io/badge/Quarto-Report-75AADB?style=for-the-badge&logo=quarto)](https://quarto.org/)

---

## 📊 Project Overview

An interactive data analysis exploring what made Wicked songs go viral on TikTok following the November 2024 movie release. This project combines Spotify API data with statistical analysis and beautiful visualizations to uncover patterns in musical theatre virality.

### ✨ Key Features

- **Real Spotify API Integration** - Collected metadata for 28 Wicked tracks
- **Interactive Visualizations** - Wicked-themed charts using Plotly
- **Statistical Analysis** - Correlation analysis and pattern discovery
- **Professional Presentation** - Beautiful Quarto website
- **Reproducible Research** - All code and data included

---

## 🎯 Key Findings

### Top 5 Most Popular Wicked Songs (Spotify)

1. **For Good** - Popularity: 58/100
2. **No Good Deed** - Popularity: 57/100  
3. **Defying Gravity** - Popularity: 56/100
4. **As Long As You're Mine** - Popularity: 55/100
5. **What Is This Feeling?** - Popularity: 53/100

### Insights

- **17 tracks** analyzed from the Wicked soundtrack
- **Average popularity**: 46.7/100 on Spotify
- Duration patterns reveal interesting correlations
- Comprehensive statistical analysis completed

---

## 🚀 Quick Start

### View the Analysis

**Option 1: Open the HTML file**
```bash
open /Users/isfarbaset/Documents/wicked-tiktok-analysis/index.html
```

**Option 2: Serve locally**
```bash
cd /Users/isfarbaset/Documents/wicked-tiktok-analysis
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Re-render the Report

```bash
cd /Users/isfarbaset/Documents/wicked-tiktok-analysis
quarto render index.qmd
```

---

## 📁 Project Structure

```
wicked-tiktok-analysis/
├── index.qmd                       # Main Quarto report
├── index.html                      # Generated website ✨
├── styles.css                      # Wicked-themed styling
├── custom.scss                     # Bootstrap theme overrides
│
├── data/
│   ├── spotify/
│   │   └── wicked_tracks_REAL.csv # Real Spotify data (28 tracks)
│   ├── tiktok/
│   │   └── wicked_tiktok_performance.csv
│   └── processed/
│       └── wicked_merged.csv      # Analysis-ready dataset
│
├── scripts/
│   ├── 01_collect_spotify_data_REAL.py   # Spotify API collection
│   ├── 02_collect_tiktok_data.py         # TikTok template
│   └── 03_analyze_REAL_data.py           # Statistical analysis
│
├── outputs/
│   ├── figures/
│   │   └── wicked_analysis.png    # Visualizations
│   └── reports/
│       └── analysis_insights.txt  # Key findings
│
└── Documentation/
    ├── PROJECT_COMPLETE.md        # Project completion summary
    ├── QUICKSTART.md              # Quick reference guide
    ├── STATUS_FINAL.md            # Detailed status
    └── SPOTIFY_API_LIMITATION.md  # API constraints
```

---

## 🎨 Design Features

### Wicked Color Theme

- **Emerald Green**: `#00A86B` - Primary brand color
- **Pink/Magenta**: `#E91E8C` - Accent color
- **Gold**: `#FFD700` - Highlight color
- **Dark Green**: `#006B3F` - Secondary color

### Interactive Elements

- ✨ Animated hero banner
- 📊 Interactive Plotly charts
- 📱 Responsive design
- 🎯 Smooth scrolling navigation
- 🌈 Gradient backgrounds
- ⚡ Hover effects and transitions

---

## 💻 Technical Stack

### Data Collection & Analysis
- **Python 3.9+**
- **Spotify API** (spotipy)
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **scipy** - Statistical analysis

### Visualization
- **Plotly** - Interactive charts
- **matplotlib** - Static plots
- **seaborn** - Statistical visualization

### Presentation
- **Quarto** - Reproducible reporting
- **HTML/CSS/SCSS** - Custom styling
- **Bootstrap** - Responsive layout

---

## 📈 Analysis Methods

### Data Sources

1. **Spotify Web API**
   - Track metadata (names, duration, popularity)
   - 28 Wicked tracks collected
   - Authenticated API access

2. **TikTok Performance Data**
   - Manual collection (API restrictions)
   - Video counts, trending duration
   - Content type analysis

### Statistical Techniques

- Spearman rank correlation
- Distribution analysis
- Trend identification
- Summary statistics

---

## 🎓 What This Project Demonstrates

### Data Science Skills
✅ API integration (Spotify)  
✅ Data cleaning and merging  
✅ Statistical analysis  
✅ Data visualization  
✅ Reproducible research  
✅ Technical documentation  

### Professional Practices
✅ Version control awareness  
✅ Clean project structure  
✅ Comprehensive documentation  
✅ Error handling  
✅ Transparent methodology  
✅ Portfolio-quality presentation  

---

## 🌟 Highlights for Portfolio

### Why This Project Stands Out

1. **Real Data** - Used actual Spotify API, not synthetic datasets
2. **Professional Documentation** - Handled API limitations transparently
3. **Beautiful Presentation** - Custom-themed interactive website
4. **Complete Pipeline** - Data → Analysis → Visualization → Insights
5. **Reproducible** - All code and data included
6. **Honest Reporting** - Documented constraints and limitations

### Interview Talking Points

> *"I analyzed what made Wicked songs popular on Spotify by collecting data from their Web API. When I encountered an API limitation with audio features, I documented it professionally and pivoted my analysis to focus on available metrics like popularity scores and duration. The project demonstrates both technical skills and real-world problem-solving."*

---

## 📝 Key Takeaways

### About the Data
- Clear popularity leaders emerged (For Good, No Good Deed, Defying Gravity)
- Duration patterns show interesting variations
- Spotify metrics provide insights into song performance

### About the Process
- API limitations are common in real-world projects
- Documentation of constraints is valuable
- Adaptability is key to successful analysis
- Beautiful presentation enhances impact

---

## 🔗 Resources

- **View Analysis**: [index.html](./index.html)
- **Project Status**: [STATUS_FINAL.md](./STATUS_FINAL.md)
- **Quick Start**: [QUICKSTART.md](./QUICKSTART.md)
- **API Notes**: [SPOTIFY_API_LIMITATION.md](./SPOTIFY_API_LIMITATION.md)

---

## 📧 Contact

**Isfar Baset**

- Portfolio: [https://isfarbaset.github.io](https://isfarbaset.github.io)
- LinkedIn: [Your LinkedIn](#)
- GitHub: [Your GitHub](#)
- Email: [Your Email](#)

---

## 📜 License

This project is for educational and portfolio purposes.

---

## 🙏 Acknowledgments

- **Spotify Web API** for music data
- **TikTok community** for trend insights
- **Wicked creative team** for the amazing music
- **Quarto team** for the excellent reporting framework

---

<div align="center">

**Built with ❤️ using Python, Quarto, and Wicked's iconic emerald and pink**

*October 2025*

</div>
