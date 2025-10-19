# 🤝 DataMate

**Your Friendly Data Analysis Companion**

DataMate is an interactive, menu-driven command-line tool that makes data exploration and manipulation effortless. Built with Pandas, it transforms complex data operations into simple menu selections - perfect for beginners and professionals alike.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Pandas](https://img.shields.io/badge/pandas-required-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🌟 Why DataMate?

- **No Coding Required**: Interactive menu system - just select and execute
- **Beginner Friendly**: Color-coded interface with helpful prompts
- **Time Saver**: Common Pandas operations in seconds
- **Safe Operations**: Built-in validations and confirmations
- **Beautiful CLI**: Vibrant, organized interface with real-time status

## ✨ Features

### 📊 Data Inspection
- View data with `head()` and `tail()` with custom ranges
- Generate statistical summaries with `describe()`
- Check data types and memory usage with `info()`
- View shape, columns, index, and transpose

### 📈 Statistical Analysis
- Find maximum and minimum value indices (`idxmax`, `idxmin`)
- Calculate mean, sum, and standard deviation
- Automatic numeric column validation

### 🧹 Data Cleaning
- Identify null values across columns
- Fill missing data with custom values
- Drop rows with missing values (with confirmation)
- Sort data by any column

### 💾 Export Options
- Save as CSV
- Save as JSON
- Save as Excel (.xlsx)

### 🎨 User Experience
- Colorful, interactive CLI interface
- Real-time data status display
- Error handling and validation
- Clear screen navigation

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/codewithjatin70/datamate.git
cd datamate
```

2. **Install dependencies:**
```bash
pip install pandas colorama openpyxl
```

### First Run

```bash
python datamate.py
```

That's it! DataMate will guide you through the rest.

## 📋 Requirements

```
pandas>=1.3.0
colorama>=0.4.4
openpyxl>=3.0.0  # For Excel export
```

Or simply:
```bash
pip install -r requirements.txt
```

## 💻 Usage Guide

### Step 1: Load Your Data
```
Enter your CSV file name (e.g., data.csv): sales_data.csv
```

### Step 2: Choose Output Location
```
Enter Your Folder Name to save output: results
```

### Step 3: Explore the Menu
DataMate presents a beautiful, organized menu with all available operations. Simply enter the number of your choice!

## 📖 Menu Options

### 🔍 File Recognition (1-8)
| Option | Function | Description |
|--------|----------|-------------|
| 1 | head() | Display first N rows |
| 2 | tail() | Display last N rows |
| 3 | describe() | Statistical summary |
| 4 | info() | Data types and memory |
| 5 | shape | Dimensions of dataset |
| 6 | columns | List all columns |
| 7 | index | Display index |
| 8 | T | Transpose data |

### 📊 Aggregation & Stats (9-13)
| Option | Function | Description |
|--------|----------|-------------|
| 9 | idxmax() | Row with maximum value |
| 10 | idxmin() | Row with minimum value |
| 11 | mean() | Calculate average |
| 12 | sum() | Calculate sum |
| 13 | std() | Standard deviation |

### 🧼 Data Cleaning (14-17)
| Option | Function | Description |
|--------|----------|-------------|
| 14 | isnull() | Check null values |
| 15 | fillna() | Fill missing data |
| 16 | dropna() | Remove null rows |
| 17 | sort_values() | Sort by column |

### 💾 Save File (18-20)
| Option | Format | Description |
|--------|--------|-------------|
| 18 | CSV | Export as CSV |
| 19 | JSON | Export as JSON |
| 20 | Excel | Export as XLSX |

## 🎯 Real-World Example

**Scenario**: You have a sales dataset with missing values that needs cleaning and analysis.

```bash
# Load data
Enter your CSV file name: sales_2024.csv
Enter Your Folder Name to save output: cleaned_data

# Check the data
Choice: 1  # View first 10 rows
Range: 10

# Find missing values
Choice: 14  # Shows null count per column

# Fill missing prices with 0
Choice: 15
Fill value: 0
Apply in place: True

# Check highest sales
Choice: 9
Column: total_sales

# Sort by date
Choice: 17
Column: date
Ascending: True

# Save cleaned data
Choice: 18
Filename: sales_cleaned
```

**Result**: Clean, analyzed data in seconds! 🎉

## 🛡️ Smart Error Handling

DataMate protects you from common mistakes:

- ✅ **File validation**: Checks if file exists before processing
- ✅ **Column validation**: Ensures column names are correct
- ✅ **Type checking**: Prevents math operations on text columns
- ✅ **Confirmation prompts**: Asks before deleting data
- ✅ **Helpful messages**: Clear, color-coded error explanations

## 🎨 Screenshots

```
================= PANDAS AUTOMATION TOOL =================
Data Loaded: sales_data.csv 1000 rows, 8 cols
----------------------------------------------------------
  1-8. FILE RECONIZE (Inspect Data)
1. head()   | 2. tail() | 3. describe() | 4. info()
...
```

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🔧 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. ✍️ Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. 📤 Push to branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

### Ideas for Contributions:
- Add more Pandas operations
- Create data visualization features
- Add support for more file formats
- Improve the UI/UX
- Write tests

## 🐛 Found a Bug?

Open an issue with:
- Description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your Python and Pandas versions

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Built With

- **[Pandas](https://pandas.pydata.org/)** - Data manipulation powerhouse
- **[Colorama](https://pypi.org/project/colorama/)** - Beautiful colored terminal output
- **[Python](https://python.org/)** - The language we love

## 👨‍💻 Author

**Your Name**
- GitHub: [@codewithjatin70](https://github.com/codewithjatin70)

## 🙏 Acknowledgments

- Inspired by the need to make data analysis accessible to everyone
- Thanks to the Pandas community for amazing documentation
- Shoutout to all contributors who help improve DataMate

## 📞 Support

- ⭐ Star this repo if you find it helpful
- 📧 Reach out for questions or suggestions

---

<div align="center">

**Made with ❤️ for the Data Community**

[Report Bug](https://github.com/codewithjatin70/datamate/issues) · [Request Feature](https://github.com/yourusername/datamate/issues) · [Documentation](https://github.com/codewithjatin70/datamate/wiki)

</div>
