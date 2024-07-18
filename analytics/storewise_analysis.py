import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

def storewise_1(df):
    df = df[df['Suburb']=='Mission Hill']
    df = df.groupby('Product line')[['Quantity','cogs','Total amount with Tax', 'net profit']].sum().reset_index()
    df=df.rename(columns={'Product line':'ProductLine','Total amount with Tax':'TotalAmountWithTax','net profit':'NetProfit'})

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].astype(int)
    df['NetProfit']=df['NetProfit'].astype(int)
    df['cogs']=df['cogs'].astype(int)

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].apply(lambda x: '{:,.2f}'.format(x))
    df['cogs']=df['cogs'].apply(lambda x: '{:,.2f}'.format(x))
    df['NetProfit']=df['NetProfit'].apply(lambda x: '{:,.2f}'.format(x))

    return df.to_json(orient='records')

def storewise_2(df):
    df = df[df['Suburb']=='Fenway']
    df = df.groupby('Product line')[['Quantity','cogs','Total amount with Tax', 'net profit']].sum().reset_index()
    df=df.rename(columns={'Product line':'ProductLine','Total amount with Tax':'TotalAmountWithTax','net profit':'NetProfit'})

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].astype(int)
    df['NetProfit']=df['NetProfit'].astype(int)
    df['cogs']=df['cogs'].astype(int)

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].apply(lambda x: '{:,.2f}'.format(x))
    df['cogs']=df['cogs'].apply(lambda x: '{:,.2f}'.format(x))
    df['NetProfit']=df['NetProfit'].apply(lambda x: '{:,.2f}'.format(x))

    return df.to_json(orient='records')

def storewise_3(df):
    df = df[df['Suburb']=='Roxbury']
    df = df.groupby('Product line')[['Quantity','cogs','Total amount with Tax', 'net profit']].sum().reset_index()
    df=df.rename(columns={'Product line':'ProductLine','Total amount with Tax':'TotalAmountWithTax','net profit':'NetProfit'})

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].astype(int)
    df['NetProfit']=df['NetProfit'].astype(int)
    df['cogs']=df['cogs'].astype(int)

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].apply(lambda x: '{:,.2f}'.format(x))
    df['cogs']=df['cogs'].apply(lambda x: '{:,.2f}'.format(x))
    df['NetProfit']=df['NetProfit'].apply(lambda x: '{:,.2f}'.format(x))

    return df.to_json(orient='records')

def storewise_img_1(df):
    df = df[df['Suburb']=='Mission Hill']
    df = df.groupby('Customer type')['Total amount with Tax'].mean().reset_index()

    fig=plt.figure(figsize=(2,4))

    sns.barplot(x='Customer type', y='Total amount with Tax', data=df)

    plt.xlabel('Customer type')
    plt.ylabel('Mean Revenue ($)')
    plt.title('Customer type vs Mean Revenue')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf

def storewise_img_2(df):
    df = df[df['Suburb']=='Fenway']
    df = df.groupby('Customer type')['Total amount with Tax'].mean().reset_index()

    fig=plt.figure(figsize=(2,4))

    sns.barplot(x='Customer type', y='Total amount with Tax', data=df)

    plt.xlabel('Customer type')
    plt.ylabel('Mean Revenue ($)')
    plt.title('Customer type vs Mean Revenue')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf

def storewise_img_3(df):
    df = df[df['Suburb']=='Roxbury']
    df = df.groupby('Customer type')['Total amount with Tax'].mean().reset_index()

    fig=plt.figure(figsize=(2,4))

    sns.barplot(x='Customer type', y='Total amount with Tax', data=df)

    plt.xlabel('Customer type')
    plt.ylabel('Mean Revenue ($)')
    plt.title('Customer type vs Mean Revenue')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf



