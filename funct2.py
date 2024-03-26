import seaborn as sns
import matplotlib.pyplot as plt
# EDA
#writting helper function to help us make x-axis countplots in our EDA process
def sns_xcount(column , data):
    sns.countplot(x = column, data = data)
    plt.title(f"{column} count in our data set")
    plt.show();

#writting helper function to help us make y-axis countplots in our EDA process
def sns_ycount(column , data):
    sns.countplot(y = column, data = data)
    plt.title(f"{column} count in our data set")
    plt.show();
    
#helper function for plotting multivariate countplots
def multivariate_ycountplot(column, data):
    sns.countplot(y = column, data = data, hue= "status_group", palette= "bright");
    plt.legend(loc= "best")

def multivariate_xcountplot(column, data):
    sns.countplot(x = column, data = data,  hue= "status_group", palette= "bright");
    plt.xticks(rotation = 45)
    plt.legend(loc= "best")