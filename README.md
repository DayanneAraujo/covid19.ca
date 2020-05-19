# covid19.ca
Rest API to provide numbers for COVID 19 situation on Canada and its provinces. 
The data is provided by the Canadian government on its website: 
https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html

How to use it? 

- Access https://covid19-ca.herokuapp.com/api/
- This request lists all the data: http://localhost:8000/api/canada/ 

You can filter by provinces making requests like:
- http://localhost:8000/api/canada/?prname=Ontario
- http://localhost:8000/api/canada/?prname=British Columbia

Available provinces are: 
['Ontario', 'British Columbia', 'Canada', 'Quebec', 'Alberta', 
'Repatriated Travellers', 'Saskatchewan', 'Manitoba', 'New Brunswick', 
'Newfoundland and Labrador', 'Prince Edward Island', 'Nova Scotia', 
'Northwest Territories', 'Nunavut', 'Yukon', 'Repatriated travellers']

How to run:
- Inside the project folder, create and activate your Venv
python -m venv venv
source venv/bin/activate

- Install requirements
pip install requirements.txt

- Database
python manage.py migrate
# If you need to update data
run python manage.py runscript update_data 
# If you need to bring all the data
run python manage.py runscript populate_db 

- Run local server
python manage.py runserver


