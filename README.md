# Face Recognition

This contains face recognition task which system architecture is microservices which divided into following services:
- Video Input Service: Read video file and send making pre-process on raw frame and
then send processed frames to the second service.
- Face Detection Service: Receive pre-processed frames NumPy data and detect faces of
that frame and then Send faces to third service.
- Data Processing Service: Receive detected faces and make similarity check to existing
face embedding data. If specific person finds in that frame send face data and the time of
frame to next service.
- Data Forwarding Service: Save a log when data is received from the previous service.

Communication methods between services utilized gRPC, vector database had been used qdrant and web app is created with fastapi.
For running this repo you need copy your data to files directory and then run below code:

`sudo docker-compose run -d`

After running docker compose send a get request to 
`http://localhost:5000/quickstart/` and if data exsits in files directory it should be run perfectly.

Or after running docker compose you can run ` python services/webapp/client/client.py`

For more information in persian please read report.pdf in docs directory.

