# NVIDIA GPU Web Scraper

A Selenium-based web scraping project that extracts GPU information from **NVIDIA’s official website**, covering the **RTX 50, 40, 30, 20, and 16 series** graphics cards.
This project automates data collection for GPU specifications and structures it for further analysis or storage.

## Features
- Scrapes GPU data directly from the official NVIDIA website
- Supports RTX 50, 40, 30, 20, and 16 series GPUs
- Automated browser interaction using Selenium
- Structured and clean data extraction
- Easy to extend for additional GPU series or fields

## Data Engineering
after scrapping all different data,i clubbed the data into 1 single file and kept only required columns.
and i did some feature engineering to clean up the data

## Tech Stack
- Python
- numpy/pandas
- Selenium
- WebDriver (Chrome)
