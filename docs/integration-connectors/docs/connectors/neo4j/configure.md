---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/neo4j/configure/
title: Neo4j \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:35.987913+00:00
---

# Neo4j  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/neo4j/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Neo4j

The Neo4j connector lets you perform insert, delete, update, and read operations on Neo4j database.

## Before you begin

Before using the Neo4J connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 

  * Neo4j 5 requires the Java 17 runtime.



## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ CREATE NEW** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **NEXT**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **Neo4J** from the drop down list of available Connectors.
     2. **Connector version** : Select the Connector version from the drop down list of available versions. 
     3. In the **Connection Name** field, enter a name for the Connection instance. 

Connection names must meet the following criteria: 

        * Connection names can use letters, numbers, or hyphens.
        * Letters must be lower-case.
        * Connection names must begin with a letter and end with a letter or number.
        * Connection names cannot exceed 49 characters.
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. Optionally, configure the **Connection node settings** : 

        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. **User Defined Views** : A filepath pointing to the JSON configuration file containing your custom views. 
     9. (Optional) In the **Advanced settings** section, select the **Use proxy** checkbox to configure a proxy server for the connection and configure the following values: 
        * **Proxy Auth Scheme** : Select the authentication type to authenticate with the proxy server. The following authentication types are supported: 
          * **Basic** : Basic HTTP authentication.
          * **Digest** : Digest HTTP authentication.
        * **Proxy User** : A user name to be used to authenticate with the proxy server. 
        * **Proxy Password** : The Secret manager secret of the user's password. 
        * **Proxy SSL Type** : The SSL type to use when connecting to the proxy server. The following authentication types are supported: 
          * **Auto** : Default setting. If the URL is an HTTPS URL, then the Tunnel option is used. If the URL is an HTTP URL, then the NEVER option is used.
          * **Always** : The connection is always SSL enabled.
          * **Never** : The connection is not SSL enabled.
          * **Tunnel** : The connection is through a tunneling proxy. The proxy server opens a connection to the remote host and traffic flows back and forth through the proxy.
        * In the **Proxy Server** section, enter details of the proxy server. 
          1. Click **\+ Add destination**.
          2. Select a **Destination Type**. 
             * **Host address** : Specify the hostname or IP address of the destination. 

If you want to establish a private connection to your backend system, do the following:

               * Create a [PSC service attachment](https://docs.cloud.google.com/integration-connectors/docs/configure-psc).
               * Create an [endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-ep-attachment) and then enter the details of the endpoint attachment in the **Host address** field.
     10. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     11. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : Select a **Destination Type**. 
        * To specify the destination hostname or IP address, select **Host address** and enter the address in the **host 1** field.
        * To establish a private connection, select **Endpoint attachment**. In the **Endpoint Attachment** list, select the endpoint attachment created for your backend system.
**Note:** To learn how to create an endpoint attachment, see [Private network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). After creating the endpoint attachment, it is visible in the **Endpoint Attachment** list.

If you want to establish a public connection to your backend systems with additional security, you can consider [configuring static outbound IP addresses for your connections](https://docs.cloud.google.com/integration-connectors/docs/configure-static-ip), and then configure your firewall rules to allowlist only the specific static IP addresses. 

To enter additional destinations, click **+ADD DESTINATION**.

  6. Click **NEXT**.


* In the **Authentication** section, enter the authentication details. 

  1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Neo4J connection:

     * Username and password 

To understand how to configure these authentication types, see Configure authentication.

  2. Click **NEXT**.


* **Review** : Review your connection and authentication details.
* Click **Create**.

## Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the password associated with the connector.



### Neo4j configuration

To configure authentication for Neo4J, do the following:

  * Install Java
  * Install Neo4j Community Edition
  * Access the Neo4j browser
  * Enable HTTPS



#### Install Java

  1. Download the Java SE Development Kit (JDK) 17.0.10.
  2. Install the adapter using the following command: `sudo yum install https://neo4j.com/docs/operations-manual/current/installation/linux/rpm/`
  3. To verify the installation, run the following command from the terminal: 
         
         java --version
             




#### Install Neo4j Community Edition

  1. Install Neo4j as root using the following command: `zypper install neo4j-5.18.0`.
  2. Verify the installation status with the following command: `sudo service neo4j status` after installation.
  3. Before you start the database for the first time, set the password for the initial user using the following command: `bin/neo4j-admin dbms set-initial-password`.

If you don't set the initial password, a default password is set for Neo4j.

  4. Change the default password at first login.
  5. Start the Neo4j with the following command: `systemctl start neo4j`
  6. Check the status of Neo4j by running the command `systemctl status neo4j`



#### Access the Neo4j browser

  1. Open the following URL from the Neo4j browser: `http://your-vm-name:7474`
  2. Enter the username and password as `neo4j/neo4j`.
  3. Click the **+** button and select **Create**.
  4. Select **Relationship** and click **Create**.
  5. Specify **KNOWS** for the relationship name.



#### Enable HTTPS

  1. Open the terminal and run the command to generate the self-signed certificate.
  2. Run the following command to start the server with HTTPS enabled: 
         
         sudo /opt/neo4j/bin/neo4j start --enable-browser --alsologtostderr --dbms-options=dbms.security.https_port=7473
             

For more information, see [SSL Framework](https://neo4j.com/docs/operations-manual/current/security/ssl-framework/).




### Set up a host address

Access the following URL in the Neo4j browser: `https://your-vm-name:7473`

Host address is a combination of IP address and port, such as `https://{IP_ADDRESS}:7473`. The port address depends on the specific service you want to access.

The following tables lists the port details:

Service | Default port | Configuration setting | Example  
---|---|---|---  
Bolt Protocol (for database connections) | 7687 | server.bolt.listen_address | bolt://127.0.0.1:7687  
HTTP (for web interface) | 7474 | server.http.listen_address | http://127.0.0.1:7474  
HTTPS (secure web interface) | 7473 | server.https.listen_address | https://127.0.0.1:7473  
  
For more information, see [Port details](https://neo4j.com/docs/operations-manual/current/configuration/ports/).

## Connection configuration samples

This section lists the sample values for the various fields that you configure when creating the Neo4J connection.

####  SSL connection type

Fieldname | Details  
---|---  
Location | europe-west1  
Connector | neo4j  
Connector version | 1  
Connection Name | google-cloud-neo4j-conn  
Service Account | my-service-account@my-project.iam.gserviceaccount.com  
Minimum number of nodes | 2  
Maximum number of nodes | 50  
Custom Trust Store | neo4j_Private_Cert  
Secret version | 1  
Destination Type | Host Address  
host | https://192.0.2.0/td>  
port | PORT  
Username | USERNAME  
Password | PASSWORD  
Secret Version | 3  
  
## Entities, operations, and actions

All the Integration Connectors provide a layer of abstraction for the objects of the connected application. You can access an application's objects only through this abstraction. The abstraction is exposed to you as entities, operations, and actions.

**Note:** You can view the entities, operations, and actions of a connector in the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).

  * **Entity:** An entity can be thought of as an object, or a collection of properties, in the connected application or service. The definition of an entity differs from a connector to a connector. For example, in a database connector, tables are the entities, in a file server connector, folders are the entities, and in a messaging system connector, queues are the entities. 

However, it is possible that a connector doesn't support or have any entities, in which case the `Entities` list will be empty.

  * **Operation:** An operation is the activity that you can perform on an entity. You can perform any of the following operations on an entity: 
    * [List](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Get](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Create](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Update](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)
    * [Delete](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#config-prop)

Selecting an entity from the available list, generates a list of operations available for the entity. For a detailed description of the operations, see the Connectors task's [entity operations](https://docs.cloud.google.com/application-integration/docs/connectors-task#config-prop). However, if a connector doesn't support any of the entity operations, such unsupported operations aren't listed in the `Operations` list.

  * **Action:** An action is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and vary from connector to connector. Normally, an action will have some input parameters, and an output parameter. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty. 

**Note:** All entities and actions will have a schema associated with them. For example, an action schema will have the parameter details such as; the parameter names, and its corresponding data type. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To refresh the schema for a connection, open the **Connection details** page of the connection, and then click **Refresh connection schema**. 

## System limitations

The Neo4j connector can process 5 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Actions

This section lists the actions supported by the connector. To understand how to configure the actions, see Action examples.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### ExecuteCustomQuery action

This action lets you execute a custom query.

To create a custom query, follow these steps: 

  1. Follow the detailed instructions to [ add a connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#add-a-connectors-task).
  2. When you [configure the connector task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#configure-the-connectors-task), in the type of action you want to perform, select **Actions**.
  3. In the **Action** list, select **Execute custom query** , and then click **Done**. 

![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)![image showing execute-custom-query-action](https://docs.cloud.google.com/static/application-integration/images/execute-custom-query-action.png)

  4. Expand the **Task input** section, and then do the following: 
     1. In the **Timeout after** field, enter the number of seconds to wait till the query executes. 

Default value: `180` seconds.

     2. In the **Maximum number of rows** field, enter the maximum number of rows to be returned from the database.

Default value: `25`.

     3. To update the custom query, click **Edit Custom Script**. The **Script editor** dialog opens. 

![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)![image showing custom-sql-query](https://docs.cloud.google.com/static/application-integration/images/add-custom-sql-query.png)

     4. In the **Script editor** dialog, enter the SQL query and click **Save**. 

You can use a question mark (?) in a SQL statement to represent a single parameter that must be specified in the query parameters list. For example, the following SQL query selects all rows from the `Employees` table that matches the values specified for the `LastName` column: 
            
            SELECT * FROM Employees where LastName=?

**Note:** Data manipulation language (DML) and data definition language (DDL) statements are supported.
     5. If you've used question marks in your SQL query, you must add the parameter by clicking **\+ Add Parameter Name** for each question mark. While executing the integration, these parameters replace the question marks (?) in the SQL query sequentially. For example, if you have added three question marks (?), then you must add three parameters in order of sequence. 

![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)![image showing add-query-param](https://docs.cloud.google.com/static/application-integration/images/add-query-param.png)

To add query parameters, do the following:

        1. From the **Type** list, select the data type of the parameter.
        2. In the **Value** field, enter the value of the parameter.
        3. To add multiple parameters, click **\+ Add Query Parameter**.

The **Execute custom query** action does not support array variables.




On successful execution, this action returns the status 200 (OK) with a response body that has the query results.

## Action examples

This section describes how to perform some of the actions in this connector.

### Example - Create a node

This example shows how to create a new node.

  1. In the `Configure Connector` dialog, select `Region, Connection, and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         CREATE (:Movie {title: 'Hey', release_year: 2010})

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter gives a blank payload [ ]. 




### Example - Update a node

This example shows how to update a node.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         match(m:Movie{title: 'Inception'}) set m.release_year=2011 return m

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter value is similar to the following:
    
    [{ "m": "{\"release_year\":2011,\"title\":\"Inception\"}" }]




### Example - Delete a node

This example shows how to delete a node.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         match(m:Movie{title: 'hey'}) delete m

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter gives a blank payload [ ]. 




### Example - Create a relationship

This example shows how to create a relationship.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         CREATE(movie:Movie {title: 'bcon'}), (actor:Actor {name: 'leo'})
         CREATE(actor)-[:ACTED_IN]->(movie)

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter gives a blank payload [ ]. 




### Example - Update a relationship

This example shows how to update a relationship.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         match(movie:Movie {title: 'demo'}), (actor:Actor {name: 'first'})
         match(actor)-[r:ACTED_IN]->(movie) set actor.name='second',r.year=2024 return actor,r,movie

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter value is similar to the following:
    
    [{   "actor": "{\"name\":\"second\"}",   "r": "{\"year\":2024}",   "movie": "{\"title\":\"demo\"}" }]




### Example - Delete a relationship

This example shows how to delete a relationship.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         MATCH(movie:Movie {title: 'bcon44'}), (actor:Actor {name: 'jacky'})
         MATCH(actor)-[r:ACTED_IN]->(movie) delete r

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter gives a blank payload [ ]. 




### Example - Update a node label

This example shows how to update a node label.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         MATCH (n:Person) where id(n)=18 set n:Actor RETURN n

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter value is similar to the following:
    
    [{ "n": "{\"born\":1962,\"name\":\"Demi Moore\"}" }]




### Example - Update relationship type

This example shows how to update a relationship type.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         MATCH (n:Person) where id(n)=18 set n.born=1963 RETURN n

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter value is similar to the following:
    
    [{ "n": "{\"born\":1963,\"name\":\"Demi Moore\"}" }]




### Example - Create a datatype

This example shows how to create a datatype.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         CREATE (:Product {unitPrice: 109.50,
         unitsInStock: 390,
         supplierID: "1",
         productID: "dumy-2",
         discontinued: false,
         quantityPerUnit: "10 boxes x 20 bags",
         productName: "productName-1",
         unitsOnOrder: 0,
         reorderLevel: 10,
         supplier: ["1"],
         expiry: Duration("P14DT18H12M"),
         categoryID: "1",
         updatedAt: DateTime("1984-11-11T12:31:14Z")})

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter gives a blank payload [ ]. 




### Example - Update a datatype

This example shows how to update a datatype.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         match(p:Product{productID: "dumy-1"}) set p.duration = Duration("P15DT19H12M"), p.updatedAt=DateTime("1984-11-12T12:31:14Z") return p

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter value is similar to the following:
    
    [{ "p": "{\"unitPrice\":109.5,
    \"unitsInStock\":390,
    \"supplierID\":\"1\",
    \"productID\":\"dumy-1\",
    \"discontinued\":false,
    \"quantityPerUnit\":\"10 boxes x 20 bags\",
    \"productName\":\"productName-1\",
    \"unitsOnOrder\":0,
    \"duration\":\"P15DT19H12M\",
    \"reorderLevel\":10,
    \"supplier\":[\"1\"],
    \"expiry\":\"P14DT18H12M\",
    \"categoryID\":\"1\",
    \"updatedAt\":\"1984-11-12T12:31:14Z\"}" }, 
    { "p":"{\"unitPrice\":109.5,
    \"unitsInStock\":390,
    \"supplierID\":\"1\",
    \"productID\":\"dumy-1\",
    \"discontinued\":false,
    \"quantityPerUnit\":\"10 boxes x 20 bags\",
    \"productName\":\"productName-1\",
    \"unitsOnOrder\":0,
    \"duration\":\"P15DT19H12M\",
    \"reorderLevel\":10,
    \"supplier\":[\"1\"],
    \"expiry\":\"P14DT18H12M\",
    \"categoryID\":\"1\",
    \"updatedAt\":\"1984-11-12T12:31:14Z\"}" }]




### Example - Delete a datatype

This example shows how to delete a datatype.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         match(p:Product{productID: "dumy-2"}) delete p

This example shows how to delete a datatype. If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter gives a blank payload [ ]. 




### Example - Get the count of nodes

This example shows how to get the count of nodes.

  1. In the `Configure Connector` dialog, select `Region, Connection and Actions`.
  2. Select `Execute Custom Query` from the actions, and then click **Done**.
  3. In the **Task Input** section of **Connector** , click on `Edit Custom Script` and then enter a value similar to the following in the `Custom Query` field: 
         
         MATCH ()  
         RETURN count(*) AS numNodes

If the action is successful, the `Execute Custom Query` task's `connectorOutputPayload` response parameter gives the payload which is similar to the following:
    
    [{
      "numNodes": 6267.0
    }]




## Entity operation examples

This section shows how to perform some of the entity operations in this connector.

### Example - List all languages

This example shows how to list all languages.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select multilanguage_table from the `Entity` list.
  3. Select the `List` operation, and then click **Done**.
  4. In the **Data Mapper** section click on **Open Data Mapping Editor** and, there you can set the **filterClause** as per your requirement.

**Note:** The value for the filter clause must always be passed within single quotes (') whenever there is a string. You can skip the singles quotes (') whenever there is a number, such as, "Id_= 58.0". Here "Id_" is the column name and "58.0" is the value.

### Example - Get a language

This example shows how to get a language.

  1. In the `Configure connector task` dialog, click `Entities`.
  2. Select multilanguage_table from the `Entity` list.
  3. Select the `Get` operation, and then click **Done**.
  4. Set the entity ID to Get single Language. To set the entity ID, in the **Data Mapper** section, click on **Open Data Mapping Editor** , and then enter `58.0` in the **Input Value** field and choose the **entityId** as Local variable. 

**Note:**

  * You must pass the value for the Entity Id,such as, 58.0. Here 58.0 is the unique primary key value, which you must pass.
  * You might encounter an error if you pass an Entity Id because of Composite Business or Primary Keys.  
In such cases, you can use a filter clause and pass a value, such as, Id_= 58.0 AND name = "Alex Noam" using LIST operation on the given entity.



## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
proxy_enabled | BOOLEAN | False | Select this checkbox to configure a proxy server for the connection.   
proxy_auth_scheme | ENUM | False | The authentication type to use to authenticate to the ProxyServer proxy. Supported values are: BASIC, DIGEST, NONE  
proxy_user | STRING | False | A user name to be used to authenticate to the ProxyServer proxy.   
proxy_password | SECRET | False | A password to be used to authenticate to the ProxyServer proxy.   
proxy_ssltype | ENUM | False | The SSL type to use when connecting to the ProxyServer proxy. Supported values are: AUTO, ALWAYS, NEVER, TUNNEL  
user_defined_views | STRING | False | A filepath pointing to the JSON configuration file containing your custom views.   
  
## Use the Neo4J connection in an integration

After you create the connection, it becomes available in both Apigee Integration and Application Integration. You can use the connection in an integration through the Connectors task.

  * To understand how to create and use the Connectors task in Apigee Integration, see [Connectors task](https://docs.cloud.google.com/apigee/docs/api-platform/integration/connectors-task#configure-the-connectors-task).
  * To understand how to create and use the Connectors task in Application Integration, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).



## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
