from lib.data_manipulation import *
import shutil
# Remove any manually created/left over files before running tests
try:
    os.remove("AirQualityMarch.csv")
except FileNotFoundError:
    pass
dir = os.path.dirname(os.path.realpath(__file__))
shutil.rmtree(dir + "/../monthly_responses", ignore_errors=True)

def test_does_file_exist():
    assert does_file_exist("doesnotexist") == False
    assert does_file_exist("AirQuality.csv") == True

def test_get_file_contents():
    assert get_file_contents("doesnotexist") == "This file cannot be found!"
    assert get_file_contents("AirQuality.csv")[0][:4] == "Date"

def test_christmas_day_air_quality():
    assert christmas_day_air_quality("AirQuality.csv", True)[0][:4] == "Date"
    assert christmas_day_air_quality("AirQuality.csv", True)[1][:43] == "25/12/2004;00.00.00;5,9;1505;-200;15,6;1168"
    assert christmas_day_air_quality("AirQuality.csv", False)[0][:43] == "25/12/2004;00.00.00;5,9;1505;-200;15,6;1168"

def test_christmas_day_average_air_quality():
    assert christmas_day_average_air_quality("AirQuality.csv") == 1439.21

def test_get_averages_for_month():
    assert get_averages_for_month("AirQuality.csv")[1] == 1003.47
    assert get_averages_for_month("AirQuality.csv")[3] == 1175.76
    assert get_averages_for_month("AirQuality.csv")[12] == 948.71

def test_create_march_data():
    create_march_data("AirQuality.csv")
    assert os.path.exists("AirQualityMarch.csv")
    fh = open("AirQualityMarch.csv", "r")
    c = fh.readlines()
    assert c[0][:4] == "Date"
    assert "10/03/2004;18.00.00;2,6;1360;150" in c[1]
    assert "31/03/2005;23.00.00;0,8;886;-200" in c[-1]
    fh.close()

def test_create_monthly_responses():
    create_monthly_responses("AirQuality.csv")
    assert os.path.isdir("monthly_responses")
    for i in range(3,13):
        j = '%02d' % i
        path = os.getcwd() + "/monthly_responses/" + str(j) + "-2004.csv"
        assert os.path.exists(path)
    for i in range(1,5):
        j = '%02d' % i
        path = os.getcwd() + "/monthly_responses/" + str(j) + "-2005.csv"
        assert os.path.exists(path)
    assert not os.path.exists(os.getcwd() + "/monthly_responses/02-2004.csv")
    assert not os.path.exists(os.getcwd() + "/monthly_responses/05-2005.csv")
    fh = open(os.getcwd() + "/monthly_responses/07-2004.csv", "r")
    c = fh.readlines()
    assert c[0][:4] == "Date"
    assert "01/07/2004;09.00.00;2,9;1276;-200;14,6;1138;246;628;134;2021;1430;28,2;47,1;1,7752;;" in c[10]
