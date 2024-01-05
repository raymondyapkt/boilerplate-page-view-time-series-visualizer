import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.set_index('date')
# Clean data
df = df[(df.value > df.value.quantile(0.025)) & 
        (df.value < df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


# Average daily page views for each month grouped by year.
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    dfB1  = df.copy()
    dfB1['year'], dfB1['month'] = df.index.year, df.index.strftime('%B')

    # grouping and orgenizing the df
    dfB2 = dfB1.groupby(['year', 'month'])['value'].mean()
    dfB2 = dfB2.unstack(level='month')
    dfB2 = dfB2[['January', 'February', 'March', 'April', 'May','June', 'July', 'August', 'September', 'October', 'November', 'December']]

    # Draw bar plot
    fig  = dfB2.plot.bar(figsize=(7,7)).figure
    plt.xlabel('Years');plt.ylabel('Average Page Views');plt.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
 
    fig, _ = plt.subplots(1, 2, figsize=(25,8))

    # Drawing first plot
    plt.subplot(1,2,1)
    sns.boxplot(x=df_box['year'], y=df_box['value'], data=df_box)

    plt.title('Year-wise Box Plot (Trend)');plt.xlabel('Year');plt.ylabel('Page Views')

    # Drawing second plot
    plt.subplot(1,2,2)
    sns.boxplot(x=df_box['month'], y=df_box['value'], data=df_box,
                         order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                        'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    plt.title('Month-wise Box Plot (Seasonality)');
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    '''
    '''
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

