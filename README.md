# 💄 Cosmetic Sales Segmentation Analysis

A comprehensive data science project analyzing cosmetic sales data using advanced clustering techniques including K-Means, HDBSCAN, UMAP, and PCA for customer and product segmentation.

## 📊 Project Overview

This project performs detailed segmentation analysis on cosmetic sales data to identify:
- **Customer segments** based on sales performance, behavior, and geographic reach
- **Product segments** based on revenue patterns, sales volume, and market penetration
- **Sales trends** and patterns across different dimensions

## 🎯 Key Features

- ✅ **Multiple Clustering Algorithms**: K-Means, HDBSCAN, DBSCAN
- ✅ **Advanced Dimensionality Reduction**: UMAP and PCA for visualization
- ✅ **Comprehensive EDA**: Sales distributions, trends, and patterns
- ✅ **Customer Segmentation**: Group salespeople by performance metrics
- ✅ **Product Segmentation**: Categorize products by revenue and demand
- ✅ **Beautiful Visualizations**: Interactive and static plots with Matplotlib and Seaborn

## 🛠️ Technologies Used

### Core Libraries
- **Python 3.12+**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib & Seaborn** - Data visualization

### Machine Learning
- **Scikit-learn** - Preprocessing, clustering (K-Means), and metrics
- **UMAP** - Uniform Manifold Approximation and Projection for dimensionality reduction
- **HDBSCAN** - Hierarchical Density-Based Spatial Clustering
- **SciPy & Numba** - Scientific computing and performance optimization

## 📁 Project Structure

```
Cosmetic_Sales_Segementation/
├── cosmetics_sales.ipynb      # Main analysis notebook
├── cosmetics_sales_data.csv   # Dataset (375+ transactions)
├── test_imports.py            # Library verification script
├── pyproject.toml             # Project dependencies (uv)
├── uv.lock                    # Dependency lock file
├── main.py                    # Main Python script (optional)
├── .gitignore                 # Git ignore rules
├── .python-version            # Python version specification
└── README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/alyeemalik0472-bot/Cosmetic_segmentation_sales.git
   cd Cosmetic_segmentation_sales
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   ```bash
   python test_imports.py
   ```

### Running the Analysis

1. **Launch Jupyter Notebook/Lab or VS Code**
   ```bash
   jupyter notebook cosmetics_sales.ipynb
   ```
   
   Or open in VS Code with the Jupyter extension

2. **Run all cells** sequentially or use "Run All"

3. **Explore the results** - visualizations, cluster assignments, and insights

## 📊 Dataset Information

The dataset contains **375+ sales transactions** with the following features:

| Column | Description |
|--------|-------------|
| `Sales Person` | Name of the salesperson |
| `Country` | Country where the sale occurred |
| `Product` | Cosmetic product name |
| `Date` | Transaction date |
| `Amount ($)` | Sales amount in USD |
| `Boxes Shipped` | Number of boxes shipped |

**Products include**: Aloe Vera Gel, Body Butter Cream, Vitamin C Cream, Hair Repair Oil, SPF Sunscreen, Face Sheet Masks, and more.

**Countries**: USA, UK, Canada, Australia, India, New Zealand

## 🔍 Analysis Workflow

1. **Data Loading & Exploration**
   - Load CSV data
   - Examine structure and summary statistics
   - Check for missing values

2. **Data Preprocessing**
   - Date feature extraction (year, month, quarter, day of week)
   - Handle categorical variables
   - Create aggregated features

3. **Exploratory Data Analysis**
   - Sales distributions
   - Country and product performance
   - Temporal trends

4. **Feature Engineering**
   - Customer-level aggregations (total sales, average transaction, etc.)
   - Product-level aggregations (revenue, volume, market reach)

5. **Customer Segmentation**
   - K-Means clustering with elbow method
   - HDBSCAN for density-based clustering
   - Silhouette score evaluation

6. **Dimensionality Reduction**
   - UMAP for 2D visualization
   - PCA for comparison
   - Cluster visualization

7. **Product Segmentation**
   - Similar clustering approach for products
   - Performance-based grouping

8. **Insights & Recommendations**
   - Cluster interpretation
   - Business insights
   - Actionable recommendations

## 📈 Key Results

### Customer Segments
The analysis identifies distinct customer segments based on:
- Total sales volume
- Average transaction value
- Number of transactions
- Geographic diversity
- Product portfolio breadth

### Product Segments
Products are categorized into clusters representing:
- High-revenue, high-volume products
- Niche/specialty products
- Emerging products

### Visualizations
- UMAP and PCA projections showing clear cluster separation
- Elbow curves for optimal K selection
- Silhouette scores for cluster quality assessment
- Comparative analysis of different algorithms

## 🎨 Sample Visualizations

The notebook generates multiple visualizations including:
- Distribution plots (sales amounts, boxes shipped)
- Bar charts (sales by country, top products)
- Time series (monthly sales trends)
- Scatter plots (UMAP/PCA projections with cluster colors)
- Cluster characteristic comparisons

## 📝 Dependencies

All dependencies are managed via `pyproject.toml`:

```toml
[project]
dependencies = [
    "hdbscan>=0.8.41",
    "ipykernel>=7.1.0",
    "matplotlib>=3.10.8",
    "numba>=0.63.1",
    "pandas>=2.3.3",
    "scikit-learn>=1.8.0",
    "scipy>=1.17.0",
    "seaborn>=0.13.2",
    "umap-learn>=0.5.11",
]
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Alyeem Malik**
- GitHub: [@alyeemalik0472-bot](https://github.com/alyeemalik0472-bot)

## 🙏 Acknowledgments

- Dataset: Cosmetic sales transaction data
- Libraries: Scikit-learn, UMAP, HDBSCAN, Pandas, Matplotlib, Seaborn
- Inspiration: Customer and product segmentation for business intelligence

## 📞 Contact

For questions or feedback, please open an issue on GitHub.

---

**⭐ If you find this project useful, please consider giving it a star!**
