# class4-homework
Docker
======
A. Building the Dockerfile into an image
	docker build -t my_csv_reader:latest .

B. Running the image 
	docker run my_csv_reader:latest "/app/wdbc.data"

Continuous Integration
======================
Continuous integration is a development practice that requires developers to integrate code
into a shared repository as Github several times per day. Each check-in (commit/push) is then 
verified by an automated build letting teams to detect problems early. (Thoughtworks)
