from fastapi import FastAPI
import uvicorn
from config import file_path
from data.data_cleaning_saving import data_cleaner_saver
from data.data_extracting import data_extractor
from data.data_deleting import data_deleter
from data.data_exist_checking import data_checker
from analytics.general_overview import gen_overview_1, gen_overview_2, gen_overview_3,gen_overview_img_1, gen_overview_img_2, gen_overview_img_3
from analytics.timeframe_analysis import timeframe_1, timeframe_img_1, timeframe_2, timeframe_3
from analytics.storewise_analysis import storewise_1, storewise_2, storewise_3, storewise_img_1, storewise_img_2, storewise_img_3
from aws_handling import aws_img_saver

app = FastAPI()

#-------------------------------------------------------#

#To check if data exists
@app.get('/')
def home_route():
    return {"msg":"This route works!"}

#-------------------------------------------------------#

#To check if data exists
@app.get('/show/check')
def check_data():
    ct = data_checker()
    return {"msg":ct}

#-------------------------------------------------------#

@app.get('/show/size')
def show_size():
    df = data_extractor()
    data_size = df.shape[0]
    return {"size": data_size}

#-------------------------------------------------------#

#To clean the i/p data
@app.get('/show/clean')
def save_data():
    data_deleter()
    msg  = data_cleaner_saver(file_path)
    return msg

#-------------------------------------------------------#

@app.get('/show/general/1')
def general_analytics_1():
    df = data_extractor()
    img_buffer = gen_overview_img_1(df)
    aws_img_saver(img_buffer, 'general_1.png')
    gen_1 = gen_overview_1(df)
    
    data_json = gen_1
    return data_json

#-------------------------------------------------------#

@app.get('/show/general/2')
def general_analytics_2():
    df = data_extractor()
    img_buffer = gen_overview_img_2(df)
    aws_img_saver(img_buffer, 'general_2.png')
    gen_2 = gen_overview_2(df)

    data_json = gen_2
    return data_json

#-------------------------------------------------------#

@app.get('/show/general/3')
def general_analytics_3():
    df = data_extractor()
    img_buffer = gen_overview_img_3(df)
    aws_img_saver(img_buffer, 'general_3.png')
    gen_3 = gen_overview_3(df)

    data_json = gen_3
    return data_json

#-------------------------------------------------------#

@app.get('/show/timeframe/1')
def timeframe_analytics_1():
    df = data_extractor()
    img_buffer = timeframe_img_1(df)
    aws_img_saver(img_buffer, 'timeframe_1.png')
    tim_1 = timeframe_1(df)

    data_json = tim_1
    return data_json

#-------------------------------------------------------#

@app.get('/show/timeframe/2')
def timeframe_analytics_2():
    df = data_extractor()
    tim_2 = timeframe_2(df)

    data_json = tim_2
    return data_json

#-------------------------------------------------------#

@app.get('/show/timeframe/3')
def timeframe_analytics_3():
    df = data_extractor()
    tim_3 = timeframe_3(df)

    data_json = tim_3
    return data_json

#-------------------------------------------------------#

@app.get('/show/storewise/1')
def storewise_analytics_1():
    df = data_extractor()
    img_buffer = storewise_img_1(df)
    aws_img_saver(img_buffer, 'storewise_1.png')
    store_1 = storewise_1(df)

    data_json = store_1
    return data_json

#-------------------------------------------------------#

@app.get('/show/storewise/2')
def storewise_analytics_2():
    df = data_extractor()
    img_buffer = storewise_img_2(df)
    aws_img_saver(img_buffer, 'storewise_2.png')
    store_2 = storewise_2(df)

    data_json = store_2
    return data_json

#-------------------------------------------------------#

@app.get('/show/storewise/3')
def storewise_analytics_3():
    df = data_extractor()
    img_buffer = storewise_img_3(df)
    aws_img_saver(img_buffer, 'storewise_3.png')
    store_3 = storewise_3(df)

    data_json = store_3
    return data_json

#-------------------------------------------------------#

if __name__ == '__main__':
	uvicorn.run(app, host='0.0.0.0', port=5000)