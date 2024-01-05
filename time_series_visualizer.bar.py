import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=["date"])

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]



def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar["Months"] = df_bar.index.month
    df_bar["tahun"] = df_bar.index.year
    df_bar["bulan_angka"] = df_bar.index.month
    df_bar = pd.DataFrame(df_bar.groupby(["tahun", "Months", "bulan_angka"])["value"].mean())
    df_bar.reset_index(inplace=True)

    # Draw bar plot

    fig, ax = plt.subplots(figsize = (14,10))
    ax = sns.barplot(data = df_bar, 
            x = "tahun", 
            y = "value", 
            hue = "Months",
            hue_order=['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December'],
            palette = "bright")

    sns.move_legend(ax, "upper left")

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy(deep=True)
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box["month_angka"] = [d.strftime("%m") for d in df_box["date"]]



    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))
    p = sns.boxplot(data = df_box, 
                x = "year", 
                y = "value", ax=ax[0])
    p.set_title("Year-wise Box Plot (Trend)")
    p.set_xlabel("Year")
    p.set_ylabel("Page Views")


    q = sns.boxplot(data = df_box.sort_values(by="month_angka"), 
                    x = "month", 
                    y = "value", 
                    ax=ax[1])
    q.set_title("Month-wise Box Plot (Seasonality)")
    q.set_xlabel("Month")
    q.set_ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig