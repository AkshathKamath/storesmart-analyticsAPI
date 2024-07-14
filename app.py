import os
from flask import Flask,jsonify
import pandas as pd
from config import file_path
from data.data_cleaning_saving import data_cleaner_saver
from data.data_extracting import data_extractor
from data.data_deleting import data_deleter
from data.data_exist_checking import data_checker
from analytics.general_overview import gen_overview_1, gen_overview_2, gen_overview_3,gen_overview_img_1, gen_overview_img_2, gen_overview_img_3
from analytics.timeframe_analysis import timeframe_1, timeframe_img_1, timeframe_2, timeframe_3
from aws_handling import aws_img_saver

app = Flask(__name__)

#-------------------------------------------------------#

#To check if data exists
@app.route('/', methods=['GET'])
def home_route():
    return "This route works!"

#-------------------------------------------------------#

#To check if data exists
@app.route('/show/check', methods=['GET'])
def check_data():
    ct= data_checker()
    return jsonify({"msg":ct})

#-------------------------------------------------------#

@app.route('/show/size', methods=['GET'])
def show_size():
    df = data_extractor()
    data_size = df.shape[0]
    gen_1 = {"size": data_size}

    data_json = gen_1
    return jsonify(data_json)

#-------------------------------------------------------#

#To clean the i/p data
@app.route('/show/clean', methods=['GET'])
def save_data():
    data_deleter()
    msg  = data_cleaner_saver(file_path)
    return msg

#-------------------------------------------------------#

@app.route('/show/general/1', methods=['GET'])
def general_analytics_1():
    df = data_extractor()
    img_buffer = gen_overview_img_1(df)
    aws_img_saver(img_buffer, 'general_1.png')
    gen_1 = gen_overview_1(df)
    
    data_json = gen_1
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/general/2', methods=['GET'])
def general_analytics_2():
    df = data_extractor()
    img_buffer = gen_overview_img_2(df)
    aws_img_saver(img_buffer, 'general_2.png')
    gen_2 = gen_overview_2(df)

    data_json = gen_2
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/general/3', methods=['GET'])
def general_analytics_3():
    df = data_extractor()
    img_buffer = gen_overview_img_3(df)
    aws_img_saver(img_buffer, 'general_3.png')
    gen_3 = gen_overview_3(df)

    data_json = gen_3
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/timeframe/1', methods=['GET'])
def timeframe_analytics_1():
    df = data_extractor()
    img_buffer = timeframe_img_1(df)
    aws_img_saver(img_buffer, 'timeframe_1.png')
    tim_1 = timeframe_1(df)

    data_json = tim_1
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/timeframe/2', methods=['GET'])
def timeframe_analytics_2():
    df = data_extractor()
    tim_2 = timeframe_2(df)

    data_json = tim_2
    return jsonify(data_json)

#-------------------------------------------------------#

@app.route('/show/timeframe/3', methods=['GET'])
def timeframe_analytics_3():
    df = data_extractor()
    tim_3 = timeframe_3(df)

    data_json = tim_3
    return jsonify(data_json)

#-------------------------------------------------------#


@app.errorhandler(500)
def internal_error(error):
    return "500: Something went wrong"

@app.errorhandler(404)
def not_found(error):
    return "404: Page not found",404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)