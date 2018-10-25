# Creating a dockerised REST API using python flask
- Base container used is Python
- To create a docker image, run the build.sh. This will always create a v1.0 image testrest
- To spin up a container run 
	docker run -d -p5000:5000 testrest:v1.0

