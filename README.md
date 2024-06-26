
#Assignment: Client-Project Management System
This project involves building a Client-Project Management System using Django REST Framework. The system allows for the management of clients, projects, and user assignments within the context of a web-based REST API.

###Entities
1. User: Represents a registered user in the system.
2. Client: Represents a client entity associated with projects.
3. Project: Represents a project assigned to a client and users.

###Functional Requirements
The project has several functional requirements that need to be implemented:

1. Client Management:
     Register a new client.
     Retrieve information about clients.
     Edit or delete client information.
2. Project Management:
     Add new projects for a client and assign users to those projects.
     Retrieve projects assigned to the logged-in user.
     Delete projects.
###System Considerations
1. The system supports multiple users, clients, and projects.
2. A client can have multiple associated projects.
3. Projects are assigned to specific clients and users.
4. Multiple clients cannot share the same project.
5. A project can be assigned to multiple users.

###Technical Requirements
1. Use Django REST Framework to build the RESTful APIs.
2. Utilize MySQL or PostgreSQL as the database backend (SQLite is not permitted).
3. Implement CRUD (Create, Read, Update, Delete) operations for clients and projects.
4. Ensure proper authentication and authorization mechanisms for user access.

###REST API Endpoints
#####Clients: 
1. List all clients: /clients/
2. Create a new client: P/clients/
3. Retrieve client info with assigned projects:/clients/id/
4. Update client info: /clients/id/
5. Delete a client: /clients/id/
#####Projects: 
Create a new project for a client:  /projects/
List projects assigned to the logged-in user: /projects/
Delete a project: /projects/id/