# import libraries
import streamlit as st

# import local app libraries
import pandas
from pandas.plotting import scatter_matrix
from sklearn.linear_model import LinearRegression
import numpy
import matplotlib.pyplot as plt


# add title
st.title("Make predictions web app")

# add a instruction
st.text("Please, upload your file in the sidebar")

# add a instruction
st.sidebar.text("Upload your file here")

# add uploader file
uploadFile = st.sidebar.file_uploader("Upload your excel file", type = [".xlsx"])

# user input
userToPredict = st.sidebar.number_input("Temperature to predict")

# start analusis button
startAnalysis = st.sidebar.button("Start analysis")

# if strt the analysis
if startAnalysis:

    ##### copy and paste the local code that we developed using jupyter ######
    
    # read dataset
    dataset = pandas.read_excel(uploadFile)

    # print(dataset.shape)

    # add a user message
    st.text("Here is a description of your dataset")

    # add a general description
    st.write(dataset.describe())


    # add a user message
    st.info("Here is a plot to see distributions and correlations")


    # display scatter matrix
    scatter_matrix(
        dataset,
        diagonal="hist",
        figsize=(8, 8)
    )

    # hidde warning message
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # display the plot
    st.pyplot()

    # train model section 

    # get the data
    x = dataset.loc[:, ["Temperature"]]
    y = dataset.loc[:, ["Power Electric"]]  # labels

    # define model
    regressor = LinearRegression()

    # train model
    regressor.fit(x, y)

    # naive test
    # print("model fit is ok")

    # data to predict
    xPredict = numpy.array([[
        # 30
        userToPredict,
    ]])

    # get the prediction
    prediction = regressor.predict(xPredict)

    # print(prediction)

    # user message
    st.success("With temperature " +
          str(xPredict[0][0]) + " the power electric generation is: " + str(prediction[0][0]))

    
    # display plot

    # user message
    st.info("Here you can see your data (blue), the model (red line) and the prediction (yellow)")

    # create the figure
    fix, ax = plt.subplots()

    # add labels to the plot
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Power Electric")

    # add dataset
    ax.scatter(x, y)

    # plot the model
    ax.plot(
        x,
        regressor.intercept_[0] + regressor.coef_[0]*x,
        c="r"
    )


    # add the prediction
    ax.scatter(
        xPredict,
        prediction,
        c="y",
        lineWidth=12
    )

    # display plot
    st.pyplot(fix)


