import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

def timeframe_1(df):
    df = df.groupby('Month')[['Quantity','Tax 5%','cogs']].sum().reset_index()
    df=df.rename(columns={'Tax 5%':'Tax'})
    df['Tax']=df['Tax'].astype(int)
    df['Tax']=df['Tax'].apply(lambda x: '{:,.2f}'.format(x))
    df['cogs']=df['cogs'].apply(lambda x: '{:,.2f}'.format(x))

    return df.to_json(orient='records')

def timeframe_2(df):
    df = df.groupby('Week of Month')[['Quantity','Total amount with Tax','gross profit','Customer Rating']].mean().reset_index()

    df=df.rename(columns={'Total amount with Tax':'TotalAmountWithTax','gross profit':'GrossProfit','Customer Rating':'CustomerRating', 'Week of Month':'WoM'})

    df['CustomerRating'] = df['CustomerRating'].round(2)
    df['TotalAmountWithTax']=df['TotalAmountWithTax'].astype(int)
    df['GrossProfit']=df['GrossProfit'].astype(int)
    df['Quantity']=df['Quantity'].astype(int)

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].apply(lambda x: '{:,.2f}'.format(x))
    df['GrossProfit']=df['GrossProfit'].apply(lambda x: '{:,.2f}'.format(x))
    df['Quantity']=df['Quantity'].apply(lambda x: '{:,.2f}'.format(x))

    return df.to_json(orient='records')

def timeframe_3(df):
    df = df.groupby('Time Slot')[['Quantity','Total amount with Tax','gross profit', 'Customer Rating']].mean().reset_index()

    df=df.rename(columns={'Total amount with Tax':'TotalAmountWithTax','gross profit':'GrossProfit','Customer Rating':'CustomerRating', 'Time Slot':'Slot'})

    df['CustomerRating'] = df['CustomerRating'].round(2)
    df['TotalAmountWithTax']=df['TotalAmountWithTax'].astype(int)
    df['GrossProfit']=df['GrossProfit'].astype(int)
    df['Quantity']=df['Quantity'].astype(int)

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].apply(lambda x: '{:,.2f}'.format(x))
    df['GrossProfit']=df['GrossProfit'].apply(lambda x: '{:,.2f}'.format(x))
    df['Quantity']=df['Quantity'].apply(lambda x: '{:,.2f}'.format(x))

    return df.to_json(orient='records')

def timeframe_img_1(df):
    fig = plt.figure(figsize=(3, 4))

    sns.lineplot(x=df['Month'].unique(), y=df.groupby('Month')['gross profit'].sum().values, marker='o', label='Gross Profit')
    sns.lineplot(x=df['Month'].unique(), y=df.groupby('Month')['Total amount with Tax'].sum().values, marker='o', label='Total Revenue')

    plt.title('Total Revenue and Profit vs Month')
    plt.xlabel('Month')
    plt.ylabel('k $')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf
    