## ML-Model-Flask-Deployment
This is a demostration project to explain how Machine Learning Models are deployed on production using Flask API , docker and HEROKU 

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) , Flask (for API) installed , Docker ( for deployement )a and a heroku account .

### Project Structure
This project has six major parts :
1. model.py - This contains code for our Machine Learning model to predict house prices absed on trainign data in 'HousePricing.csv' file.
2. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter house detail and displays the predicted house price.
5. requirements.txt ; procfile - necessary files for the deployement of the heroku app .
6. Visual.ipynb - This contains the visualisations of the data on a dash application.

### Running the project on Flask
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

You should be able to view the homepage as below :
![alt text](https://user-images.githubusercontent.com/77074782/106214031-3f69fd00-61ce-11eb-9c69-4ee17812be35.PNG)

Enter valid numerical values in all 5 input boxes and hit Predict.

If everything goes well, you should  be able to see the predcited house price vaule on the HTML page!
![alt text](http://www.thepythonblog.com/wp-content/uploads/2019/02/Result.png)

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```

### Running the project on Docker 
1. Ensure that you have Docker installed and that you're in the project home directory . Create the dockerized image by running the following command -
```
docker image build -t flask
```
2. To make sure that your image has been created , run the following command 
```
docker image ls 
```
3. Now we should run our image :
```
docker run -it  -p 5000:5000 -d flask 
```


### Deploying the app to Heroku 
1. Ensure that you have a heroku account -
2. Deploy the app on heroku using the git repository -
3. You should be able to have the following app :

![alt text](https://user-images.githubusercontent.com/77074782/106214837-eef39f00-61cf-11eb-9cad-7f421d3662d6.PNG)

### Data Visualisation on Dash 
1. Run the visual.ipynb file
2. Navigate to the generated URL : http://127.0.0.1:8050/
3 . Here's what your visualisations app will look like :

 ![alt text](https://user-images.githubusercontent.com/77074782/106214837-eef39f00-61cf-11eb-9cad-7f421d3662d6.PNG)(https://user-images.githubusercontent.com/77074782/106250877-82e75a00-6214-11eb-8834-527a2cc2d9ab.PNG)
