# SPM Task




## installation steps:

1. Clone the repository:

```bash
git clone https://github.com/usamashehab/spm_task.git
```

2. Change into the project directory:

```bash
cd spm_task
```

3. Build the docker image:

```bash
docker-compose -f local.yml build
```

4. Run the docker container:

```bash
docker-compose -f local.yml up
```

5. Create super user:

```bash
docker-compose -f local.yml run django python manage.py createsuperuser
```


٦. Open a web browser and navigate to `http://localhost:8000/api/docs/` to access the comprehensive API documentation.or
   navigate to `http://localhost:8000/` see the home page.
