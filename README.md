## Workflow
    1. PIL (Pillow) => open an image
    2. OpenCV : Change an image
    3. Tesserect (PyTesserect) : OCR an image

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
- browser: 
    - http://localhost:85
    - http://localhost:85/docs 
- Follow Codebase:
    - https://github.dev/tiangolo/full-stack-fastapi-template/tree/master/backend/
- Follow Tutorials:
    - https://www.youtube.com/watch?v=tQGgGY8mTP0&list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i
    