import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

def gen_overview_1(df):
    df = pd.concat([df.groupby('Suburb')[['Total amount with Tax','Tax 5%', 'net profit']].sum().reset_index(), df.groupby('Suburb')['Customer Rating'].mean().reset_index()], axis=1)
    df = df.loc[:, ~df.columns.duplicated(keep='first')]
    df=df.rename(columns={'Total amount with Tax':'TotalAmountWithTax','Tax 5%':'Tax','net profit':'NetProfit','Customer Rating':'CustomerRating'})
    df['CustomerRating'] = df['CustomerRating'].round(2)
    
    df['TotalAmountWithTax']=df['TotalAmountWithTax'].astype(int)
    df['Tax']=df['Tax'].astype(int)
    df['NetProfit']=df['NetProfit'].astype(int)

    df['TotalAmountWithTax']=df['TotalAmountWithTax'].apply(lambda x: '{:,.2f}'.format(x))
    df['Tax']=df['Tax'].apply(lambda x: '{:,.2f}'.format(x))
    df['NetProfit']=df['NetProfit'].apply(lambda x: '{:,.2f}'.format(x))
    
    return df.to_json(orient='records')

def gen_overview_2(df):
    df=pd.concat([df.groupby(['Product line'])[['Quantity','cogs']].sum().reset_index(),df.groupby(['Product line'])[['gross margin percentage']].mean().reset_index()],axis=1)
    df = df.loc[:, ~df.columns.duplicated(keep='first')]
    df=df.rename(columns={'Product line':'Product','gross margin percentage':'gmp'})
    df['gmp']=df['gmp'].round(2)

    df['cogs']=df['cogs'].astype(int)

    df['cogs']=df['cogs'].apply(lambda x: '{:,.2f}'.format(x))

    return df.to_json(orient='records')

def gen_overview_3(df):
    df=pd.concat([df['Customer type'].value_counts().reset_index(),df.groupby('Customer type')['Customer Rating'].mean().reset_index()],axis=1)
    df = df.loc[:, ~df.columns.duplicated(keep='first')]
    df=df.rename(columns={'Customer type':'Ctype','Customer Rating':'CustomerRating'})

    df['CustomerRating'] = df['CustomerRating'].round(2)

    return df.to_json(orient='records')

def gen_overview_img_1(df):
    fig = plt.figure(figsize=(3.5,8))
    ax = sns.barplot(x="Suburb", y="Total amount with Tax", color='#0000FF',saturation=0.5, data=df, errorbar=None, estimator=sum, label='Total Revenue')
    ax = sns.barplot(x="Suburb", y="cogs", color='#007FFF', saturation=0.2, data=df, errorbar=None, estimator=sum, label='Cost of goods')
    ax = sns.barplot(x="Suburb", y="gross profit", color='#89CFF0', saturation=0.5, data=df, errorbar=None, estimator=sum, label='Gross Profit')
    ax.set(xlabel="Suburbs", ylabel="Financial Parameters")
    plt.legend(loc=3)
    # fig.savefig('.././Main-Project/backend/public/images/general/general_1.png') #Ideally store to AWS s3
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf


def gen_overview_img_2(df):
    fig = plt.figure(figsize=(4,6))
    ax=sns.countplot(x='Customer type',hue='Suburb',palette=['#89CFF0', '#0000FF', '#0066b2'],data=df)
    ax.set(xlabel="Customer Type", ylabel="Count")
    plt.legend(loc=8)
    # fig.savefig('.././Main-Project/backend/public/images/general/general_3.png') #Ideally store to AWS s3
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf
    
def gen_overview_img_3(df):
    pie_df=df.groupby('Product line')['Quantity'].sum().reset_index()
    # sns.set(style="whitegrid")
    fig = plt.figure(figsize=(5,3))
    plt.pie(pie_df['Quantity'], labels=pie_df['Product line'], autopct='%1.1f%%', startangle=140, colors=['#7CB9E8','#318CE7','#72A0C1','#007FFF','#89CFF0','#0000FF'])
    plt.title('Product category units sold Breakdown')
    # fig.savefig('.././Main-Project/backend/public/images/general/general_2.png') #Ideally store to AWS s3
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)
    return buf



    