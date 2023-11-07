## Deploying ML Model using Flask (Prerequisites)
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

Flask installation:
``````
conda install flask  (or) pip install flask

Scikit Learn installation:
```
pip install scikit-learn==1.3.0
```

Numpy installation:
pip install numpy
``````

### Project Structure
This project has four major parts :
1. 5g_resource_allocation.py - This contains code fot our Machine Learning model to predict percentage of resource to be allocated to an user based on training data in 'Quality of Service 5G.csv' file.
2. application.py - This contains Flask APIs that receives user details through GUI or API calls, computes the precited value based on our model and returns it.
3. templates - This folder contains the HTML templates (index.html, about.html, pred.html) 
4. static - This folder contains the css folder with style.css file which has the styling required for out index.html file and it also contains images folder which contain .

### Running the project
1. It is recommended to use VSCode to run this project. Open the directory of the project , right click and select open with code. The open terminal of VSCode and enter these commands to create a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

2. Ensure that you are in the project home directory. Create the machine learning model by running below command from command prompt or VS code terminal -
```
python 5g_resource_allocation.py
```
This would create a serialized version of our model into a file 5G_Quality.pkl

3. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

4. Navigate to URL http://127.0.0.1:5000/ (or) http://localhost:5000

You should be able to view the homepage.

Enter valid numerical values in all input boxes and hit Predict on prediction page.

If everything goes well, you should  be able to see the predcited salary vaule on the HTML page!
check the output here: http://127.0.0.1:5000/predict