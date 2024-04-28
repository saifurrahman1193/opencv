### Docker
#### Docker: 

#### CMD
```
docker exec -it opencv-container sh
```

#### Access container to container
```
docker exec wintext-portal-container ping 103.134.89.185


docker exec ms-rmq-container ping opencv-container
docker exec ms-rmq-container ping otl-erp-db-container

docker exec opencv-container ping ms-rmq-container 
docker exec opencv-container telnet ms-rmq-container 5673
docker exec opencv-container ping otl-erp-db-container 

docker exec otl-erp-db-container ping ms-rmq-container
docker exec otl-erp-db-container ping opencv-container
```




#### Command: docker 
```
sudo docker-compose down
sudo docker-compose build && docker-compose up -d
```

#### Command: docker  : Services
```
docker-compose exec export sh

npm run development -- --watch
npm run watch
```

#### Browser: 
- browser: http://localhost:85