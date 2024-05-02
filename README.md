# SPM Task


Click [here](https://lucid.app/lucidchart/f655101e-45a8-4686-9cb0-dfc2295d0c84/edit?viewport_loc=272%2C-638%2C1541%2C1352%2C0_0&invitationId=inv_8cebdaba-842d-4172-b9e4-eebab81f4c58) to view a database schema.

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


6. Open a web browser and navigate to `http://localhost:8000/api/docs/` to access the comprehensive API documentation.or
   navigate to `http://localhost:8000/` see the home page.
