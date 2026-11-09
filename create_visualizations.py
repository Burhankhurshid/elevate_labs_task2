"""Task 2: Data Visualization and Storytelling. Run: python create_visualizations.py"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent
df=pd.read_csv(p/"superstore_sales_practice.csv",parse_dates=["Order_Date"])
df["Month"]=df.Order_Date.dt.month
monthly=df.groupby("Month").Sales.sum()
region=df.groupby("Region").Sales.sum().sort_values()
category=df.groupby("Category")[["Sales","Profit"]].sum()
plt.figure(figsize=(9,4.5)); monthly.plot(marker="o"); plt.title("Monthly Sales Trend — 2025"); plt.xlabel("Month"); plt.ylabel("Sales"); plt.grid(alpha=.25); plt.tight_layout(); plt.savefig(p/"monthly_sales_trend.png"); plt.close()
plt.figure(figsize=(8,4.5)); region.plot(kind="barh"); plt.title("Sales by Region"); plt.xlabel("Sales"); plt.tight_layout(); plt.savefig(p/"sales_by_region.png"); plt.close()
plt.figure(figsize=(8,4.5)); category.Sales.plot(kind="bar"); plt.title("Sales by Category"); plt.ylabel("Sales"); plt.tight_layout(); plt.savefig(p/"sales_by_category.png"); plt.close()
plt.figure(figsize=(8,4.5)); category.Profit.plot(kind="bar"); plt.title("Profit by Category"); plt.ylabel("Profit"); plt.tight_layout(); plt.savefig(p/"profit_by_category.png"); plt.close()
print("Four charts generated.")
