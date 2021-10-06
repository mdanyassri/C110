import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("data.csv")
data = df ["temp"].tolist()

population_mean = statistics.mean(data)
population_stddev = statistics.stdev(data)

#print("mean of population: ",population_mean)
#print("stddev of population: ",population_stddev)

#fig = ff.create_distplot([data], ["temp"], show_hist=False)
#fig.show()

#dataset = []

#for i in range(0, 100):
    #random_index = random.randint(0,len(data))
    #value = data[random_index]
    #dataset.append(value)

#sample_mean = statistics.mean(dataset)
#sample_stddev = statistics.stdev(dataset)

#print("mean of sample: ",mean)
#print("stddev of sample: ",stddev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()