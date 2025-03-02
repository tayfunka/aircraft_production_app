# Aircraft Production App

## Getting Started

The Aircraft Production App is deployed and accessible via the following public IP address:

You can use this to access the deployed application:

Public IP: https://51.20.173.125

### API Documentation

The API documentation is available via Swagger. You can access it at:
```
http://localhost:8000/api/docs/
```
or
```
http://51.20.173.125/api/docs/
```


Use one of [these](#users) accounts for logging in.


## General Info

The Aircraft Production App is structured into several key components:

- **Backend**: The backend is built using Django and DRF, It handles the business logic, database interactions, and API endpoints.
- **Database**: PostgreSQL is used as the database to store all the application data, including user information, aircraft details, and production records.
- **Containers**: Docker and Docker Compose are used to containerize the application, making it easy to set up and run in any environment.

This modular structure ensures that each component can be developed, and scaled independently.


### Prerequisites

Ensure you have the following installed on your system:
- Docker
- Docker Compose

### Steps to Run the Application

1. **Clone the Repository**

    Clone the repository to your local machine:
    ```sh
    git clone https://github.com/tayfunka/aircraft_production_app.git
    cd aircraft_production_app
    ```

2. **Build the Docker Images**

    Build the Docker images using Docker Compose:
    ```sh
    docker-compose build
    ```

3. **Start the Application**

    Start the application using Docker Compose:
    ```sh
    docker-compose up
    ```

    This command will:
    - Start the PostgreSQL database container.
    - Build and start the Django application container.
    - Initialize the database with the necessary tables and data.
    - Start the Nginx container to serve the application.



    ```sh
    nginx-1  | 2025/02/28 18:19:41 [emerg] 1#1: cannot load certificate "/etc/nginx/certs/nginx.crt": BIO_new_file() failed (SSL: error:80000002:system library::No such file or directory:calling fopen(/etc/nginx/certs/nginx.crt, r) error:10000080:BIO routines::no such file)
    nginx-1  | nginx: [emerg] cannot load certificate "/etc/nginx/certs/nginx.crt": BIO_new_file() failed (SSL: error:80000002:system library::No such file or directory:calling fopen(/etc/nginx/certs/nginx.crt, r) error:10000080:BIO routines::no such file)
    ```

    Note: Skipping this error log because the certificate files are stored on the server, not locally.


4. **Initialize Teams and Responsibilities**

    The application will automatically initialize teams, responsibilities, users, and aircraft types when it starts. The following management commands are executed during the startup process:
    - `python manage.py init_teams`
    - `python manage.py init_responsibilities`
    - `python manage.py init_users`
    - `python manage.py init_aircraft`

    This process creates objects such as `person_wing`, `person_tail`, `Wing Team`, and `Tail Team`. Additionally, it sets up the conditions required for each team's responsibilities and aircraft production. This initialization is done to facilitate testing for users.

    For more detailed information about the initialization process, you can refer to the attached files in the `personnel/management/commands/` directory. These files include:

    - `init_teams.py`
    - `init_responsibilities.py`
    - `init_users.py`
    - `init_aircraft.py`

    Each file contains specific commands and logic to set up the initial data required for the application.

    ### Example Data

    Here are some examples of the data that will be initialized during the startup process:

    #### Users
    - **Username**: `admin`
        - **Password**: `Baykar.,12`
    - **Username**: `person_wing`
        - **Password**: `Baykar.,12`
        - **Team**: `Wing Team`
    - **Username**: `person_fuselage`
        - **Password**: `Baykar.,12`
        - **Team**: `Fuselage Team`
    - **Username**: `person_tail`
        - **Password**: `Baykar.,12`
        - **Team**: `Tail Team`
    - **Username**: `person_avionics`
        - **Password**: `Baykar.,12`
        - **Team**: `Avionics Team`
    - **Username**: `person_assembly`
        - **Password**: `Baykar.,12`
        - **Team**: `Assembly Team`

    #### Teams
    - `Wing Team`
    - `Fuselage Team`
    - `Tail Team`
    - `Avionics Team`
    - `Assembly Team`

    #### Responsibilities
    - **Team**: `Wing Team`
        - **Part**: `Wing`
    - **Team**: `Fuselage Team`
        - **Part**: `Fuselage`
    - **Team**: `Tail Team`
        - **Part**: `Tail`
    - **Team**: `Avionics Team`
        - **Part**: `Avionics`

    #### Aircraft Types
    - `TB2`
    - `TB3`
    - `AKINCI`
    - `KIZILELMA`
    
    
### Accessing the Application

Once the application is up and running, you can access it in your web browser at:
```
http://localhost:8000
```
You can also reach the app via:
```
https://51.20.173.125
```

### Deployment Information

- The Aircraft Production App is deployed on an AWS EC2 instance with the following infrastructure:
- Operating System: Linux Fedora
- Public IP: Elastic IP (51.20.173.125) for a static address
- Containerization: Docker and Docker Compose used for deploying services
- Reverse Proxy: Nginx configured as a reverse proxy for managing requests
- SSL Certificates: Generated using OpenSSL, but currently not fully recognized as secure by browsers.
- Hosting: Deployed entirely on the EC2 instance using Dockerized services

### Requirements Status

- Server-Side Datatable Usage: The datatable retrieves and processes data on the server using the endpoint:
```
/aircraft/api/aircraft-list-datatable/
```
-  Asynchronous Front-End Requests: The front-end uses AJAX and Fetch API to retrieve data asynchronously from:
```
/aircraft/aircraft-list/
```

#### Completed Requirements
- Personnel login screen.
- Personnel's team: Multiple personnel can belong to the same team.
- Teams must be able to create, list, and recycle (CRUD) their own parts. Note: "recycle" means "delete."
- Teams cannot produce parts outside their responsibility. (e.g., the Avionics team cannot produce the tail.)
- The Assembly Team must assemble one aircraft by combining all compatible parts.
- Each part is specific to an aircraft; a TB2 wing cannot be used for a TB3.
- The Assembly Team should be able to list the aircraft produced.
- The system should give a warning if any part is missing from the inventory (e.g., the fuselage for Akinci is missing).
- A part used in one aircraft cannot be used in another, and the stock count must be decreased.
- After creating and assembling all parts for an aircraft, the system should store information about the parts used and in which aircraft they were used.
- Deploying the project using Docker.
- Well-prepared documentation and comments.
- Using additional libraries for Django.
- Using front-end technologies like Bootstrap, Tailwind, jQuery.
- API docs (Swagger).

#### Incomplete Requirements
- Unit testing.
- Using datatables for listing pages.

### Extra Note

A domain named `tayfunkarakavuz.me` was acquired for that app purpose but never used. Instead I decided to use Elastic IP address: `51.20.173.125`