---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure/
title: MongoDB (version 2) \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:05.371296+00:00
---

# MongoDB (version 2)  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MongoDB (version 2)

The MongoDB connector lets you perform insert, delete, update, and read operations on a [MongoDB database](https://www.mongodb.com/).

## Supported versions

  * MongoDB versions 3.6 to 6.1
  * Mongo Atlas deployed on Google Cloud.



## Before you begin

Before using the MongoDB connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private). For information about how to set up network connectivity for MongoDB Atlas cluster, see [Private connectivity for a MongoDB Atlas cluster](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb). 
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

For information about enabling services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 

    * Restrict network access to your Atlas cluster with a firewall: 

To restrict network access to your Atlas cluster, configure the MongoDB connector to use a set of static IP addresses for the traffic originating from the connections. To understand how to allow your connection to connect through a firewall, see [Connect to your public backend application through a firewall](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-public#connect-to-your-public-backend-application-through-a-firewall). 




## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.
  4. In the **Connection Details** section, complete the following: 
     1. **Connector** : Select **MongoDB** from the drop down list of available Connectors.
     2. **Connector version** : Select the version `2` from the version list. 
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
     8. **Database** : The name of the MongoDB database to connect to. 
     9. **Connection Timeout** : Specify the time in seconds to wait for an operation to complete before canceling it. 
     10. **Connection Pool max size** : Specify the maximum number of connections allowed in the connection pool. 
     11. **Connection Pool min size** : Specify the minimum number of connections maintained in the connection pool. 
     12. **Connection Idle time in secs** : Specify the maximum idle time in seconds that a connection can exist in the pool before being closed. 
     13. **Connection Lifetime in secs** : Specify the maximum lifetime of a connection in seconds. After this time limit, the connection is closed. 
     14. **Use SSL** : Specify if SSL is enabled or not.
     15. **App Name** : Custom App Name for Mongo. 
     16. **Max Staleness Seconds** : Time in seconds how stale a secondary can be before the client stops using it for read operations.
     17. **Write Concern(w Option)** : Option to request acknowledgment that the write operation has propagated to a specified number of instances with specific tags.
     18. **Write Concern(wtimeoutMS Option)** : Specifies a time limit, in milliseconds, for the write concern.
     19. **Write Concern(journal Option)** : Requests acknowledgement from MongoDB that the write operation has been written to the journal.
     20. **Read Preference** : Set this to a strategy for reading from a replica set. Accepted values are primary, primaryPreferred, secondary, secondaryPreferred, and nearest. 
     21. **Cluster Type** : Specify the type of MongoDB cluster.
     22. **Enable Encryption** : Specify whether encryption is enabled.
     23. **Encryption Type** : Specify the type of encryption enabled. Currently only `Local Encryption` type is supported.
     24. **Encryption Schema** : Specify the encryption schema information, including the fields and encryption algorithm, key alt name, query type and contention factor. For example: 
            
            {
              "database.collection": {
                "encryptMetadata": {
                  "algorithm": "parentAlgo"
                },
                "properties": {
                  "passportId": {},
                  "medicalRecords": {
                    "encryptMetadata": {
                      "algorithm": "medicalRecordParentAlgo"
                    },
                    "properties": {
                      "medicalRecord1": {},
                      "medicalRecord2": {
                        "encrypt": {
                          "algorithm": "medicalRecord2Algo",
                          "keyAltName": "medicalRecord2Altkey",
                          "queryType": "equality",
                          "contentionFactor": 3
                        }
                      }
                    }
                  },
                  "insuranceProperties": {
                    "properties": {
                      "policyNumber": {},
                      "insuranceRecord1": {
                        "encrypt": {
                          "algorithm": "insuranceRecord1Algo",
                          "keyAltName": "insuranceRecord1AltKey"
                        }
                      },
                      "insuranceRecord2": {
                        "encrypt": {
                          "algorithm": "insuranceRecord2Algo",
                          "keyAltName": "insuranceRecord2AltKey",
                          "contentionFactor": 5
                        }
                      }
                    }
                  }
                }
              }
            }

     25. **encryption_master_key** : Secret Manager Secret containing the encryption master key.
     26. **encryption_key_vault** : Encryption key vault value.
     27. **Auth Database** : Specify the name of the MongoDB database for authentication.
     28. Optionally, click **\+ ADD LABEL** to add a label to the Connection in the form of a key/value pair.
     29. Click **NEXT**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. **Destination Type** : You can specify the destination details as a host address, which can be any of the following: 
        * Single Mongo SRV string. For example, `mongodb+srv://cluster2.2f.mongodb.net`
        * Individual replicas. For example, `dasdsf.2f.mongodb01.net`
        * IP address. For example,`10.23.123.12`

The `mongodb://` prefix will be added to final URL after combining all the replicas in connection string if `mongodb+srv` isn't specified.

        * **Host address** : Specify the hostname or IP address of the destination. 

If you want to establish a private connection to your backend, do the following:

          * Create a [PSC service attachment](https://docs.cloud.google.com/integration-connectors/docs/configure-psc).
          * Create an [endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/create-ep-attachment) and then enter the details of the endpoint attachment in the **Host address** field.
**Note:** If you want to connect to a MongoDB Atlas cluster running on a private network within Google Cloud, see [Private connectivity for an Atlas cluster](https://docs.cloud.google.com/integration-connectors/docs/configure-mongo-atlas-psc).

To enter additional destinations, click **+ADD DESTINATION**.

     2. Click **NEXT**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the MongoDB connection:

        * Username and password

To understand how to configure these authentication types, see Configure authentication.

     2. Click **NEXT**.
  7. **Review** : Review your connection and authentication details.
  8. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **Username and password**
    * **Username** : Username for connector
    * **Password** : Secret Manager Secret containing the user's password.
    * **Auth Scheme** : The scheme used for authentication. 

The following Auth Scheme are supported by the MongoDB connection:

      * Plain
      * SCRAM-SHA-1
      * SCRAM-SHA-256



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

**Note:** All entities and actions will have a schema associated with them. For example, an action schema will have the parameter details such as; the parameter names, and its corresponding data type. The schema (metadata) for entities and actions is fetched by the connection at runtime from your backend. If there are any updates to the schema, such updates won't be automatically reflected in your existing connections; you must manually refresh the schema. To refresh the schema for a connection, open the **Connection details** page of the connection, and then click **Refresh connection schema**. **Note:** The MongoDB connector doesn't support any entity operations.

## System limitations

The MongoDB connector can process a maximum of 70 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Supported data types

The following are the supported data types for this connector:

  * BIGINT
  * BINARY
  * BIT
  * BOOLEAN
  * CHAR
  * DATE
  * DECIMAL
  * DOUBLE
  * FLOAT
  * INTEGER
  * LONGN VARCHAR
  * LONG VARCHAR
  * NCHAR
  * NUMERIC
  * NVARCHAR
  * REAL
  * SMALL INT
  * TIME
  * TIMESTAMP
  * TINY INT
  * VARBINARY
  * VARCHAR



## Configuration for the MongoDB Atlas cluster

The authentication configuration for a MongoDB Atlas cluster differ slightly from the previously documented steps. To authenticate against an Atlas cluster, you must first get the Atlas connection string. To obtain the Atlas connection string, perform the following steps: 

  1. In the Clusters view, click Connect for the cluster you want to connect to.
  2. Click Connect Your Application.
  3. Select either driver option to display a connection string.



To authenticate against an Atlas cluster, use the following configuration:

  * **Auth Database** : Set the value to **admin** , as all MongoDB Atlas users are associated with the **admin** database. 
  * **Use SSL** : Set the value to **true**. 
  * **Server** : Set the value to **mongodb+srv:// MongoDB INSTANCE SERVER NAME** without including the username and password. 



## Actions

This section lists all the actions supported by the MongoDB connection.

**Note:** The results of all the actions will be available as a JSON response in the `Connectors` task's `connectorOutputPayload` response parameter after you run your integration.

### AggregatePipeline action

This action aggregates the pipeline changes in a collection.

#### Input parameters of the AggregatePipeline action

Parameter name | Data type | Required | Description  
---|---|---|---  
collection | String | Yes | The name of MongoDB collection.  
pipeline | String | Yes | Aggregation pipeline containing field stages as list of strings.  
page_size | Integer | No | The number of items to be included in each page of the result set.  
page_no | Integer | No | The index of the page to be retrieved from the result set. Index starts from 0.  
  
For example on how to configure the `AggregatePipeline` action, see Examples.

### CountDocuments action

This action counts all the documents that satisfy a given condition in a collection.

#### Input parameters of the CountDocuments action

Parameter name | Data type | Required | Description  
---|---|---|---  
collection | String | Yes | The name of MongoDB collection.  
filter | String | No | A filter condition expressed in MongoDB query format. This condition can contain encrypted fields if encryption schema is enabled for querytype equality.  
  
#### Output parameters of the CountDocuments action

This action returns the count of all the documents that satisfy a given condition.

For example on how to configure the `CountDocuments` action, see Examples.

### DeleteDocuments action

This action deletes documents in a collection.

#### Input parameters of the DeleteDocuments action

Parameter name | Data type | Required | Description  
---|---|---|---  
collection | String | Yes |  The Name of MongoDB collection.  
filter | String | No | A filter condition expressed in MongoDB query format. This condition can contain encrypted fields if encryption schema is enabled for query-type equality.  
  
#### Output parameters of the DeleteDocuments action

The action returns the count of documents that were deleted.

For example on how to configure the `DeleteDocuments` action, see Examples.

### DistinctValues action

This action returns the distinct values of a field in a collection.

#### Input parameters of the DistinctValues action

Parameter name | Data type | Required | Description  
---|---|---|---  
collection | String | Yes | The name of MongoDB collection.  
field | String | Yes | Field name to query for distinct values.  
filter | String | No | A filter condition expressed in MongoDB query format. This condition can contain encrypted fields if encryption schema is enabled for querytype equality.  
  
For example on how to configure the `DistinctValues` action, see Examples.

### InsertDocument action

This action inserts a document in a collection.

The following tables describe the input and output parameters of the `InsertDocument` action.

#### Input parameters of the InsertDocument action

Parameter name | Data type | Required | Description  
---|---|---|---  
collection | String | Yes |  The Name of MongoDB collection.  
document | String | No | Document to be added to a MongoDB collection.  
  
#### Output parameters of the InsertDocument action

This action returns the ID of the inserted document.

For example on how to configure the `InsertDocument` action, see Examples.

### ListDocuments action

The following tables describe the input and output parameters of the ListDocuments action.

#### Input parameters of the ListDocuments action

Parameter name | Data type | Required | Description  
---|---|---|---  
collection | String | Yes |  The name of MongoDB collection.  
filter | String | No | A filter condition expressed in MongoDB query format. This condition can contain encrypted fields if encryption schema is enabled for querytype equality.  
page_size | Integer | No | The number of items to be included in each page of the result set.  
page_no | Integer | No | The index of the page to be retrieved from the result set. Index starts from 0.  
projection | String | No | The set of fields or properties to be included in the query projection in the Mongo format.  
sort_by | String | No | The specification of the query result ordering using MongoDB's Binary JSON (BSON) format.  
  
#### Output parameters of the ListDocuments action

The action returns the list of documents satisfying the filter condition as per the page size. The default page size is 25 and maximum page size is 50000.

For example on how to configure the `ListDocuments` action, see Examples.

### UpdateDocuments action

The following tables describe the input and output parameters of the `UpdateDocuments` action.

#### Input parameters of the UpdateDocuments action

Parameter name | Data type | Required | Description  
---|---|---|---  
collection | String | Yes |  The Name of MongoDB collection.  
values | String | No | Values to be updated in the Mongo format.  
filter | String | No | A filter condition expressed in MongoDB query format. This condition can contain encrypted fields if encryption schema is enabled for query-type equality.  
upsert | Boolean | No | Operation is upsert or not.  
  
#### Output parameters of the UpdateDocuments action

The action returns the number of documents that were updated.

For example on how to configure the `UpdateDocuments` action, see Examples.

### UpdateDocumentsWithEncryption action

This action allows the user to update the encrypted values.The following tables describe the input and output parameters of the `UpdateDocumentsWithEncryption` action.

#### Input parameters of the UpdateDocumentsWithEncryption action

Parameter name | Data type | Required | Description  
---|---|---|---  
collection | String | Yes |  The Name of MongoDB collection.  
document | String | No | Document containing values to be updated. Values can contain fields that will be encrypted using CSFLE.  
filter | String | No | A filter condition expressed in MongoDB query format. This condition can contain encrypted fields if encryption schema is enabled for querytype equality.  
upsert | Boolean | No | Specifies if the operation is `upsert`.  
  
#### Output parameters of the UpdateDocumentsWithEncryption action

The action returns the number of documents that were updated.

For example on how to configure the `UpdateDocumentsWithEncryption` action, see Examples.

## Examples

This section describes how to perform some of the entity operations and actions in this connector.

### Example - Aggregate pipeline changes

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `AggregatePipeline` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
           "collection": "restaurants",
           "pipeline": {
             "stages": [
               "{$addFields: { \"new_menu_item\": \"tea\"}}"
             ]
           },
           "page_size": 1,
           "page_no": 0
         }

This example adds a new menu item to all the documents in the `restaurant` collection and returns the first page of the result.




### Example - Count documents

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `CountDocuments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "collection":"restaurants",
         "filter": "{\"name\": \"CarvelIceCream1\"}"
         }

This example returns the count of documents that match the filter criteria. If the action is successful, the `Connectors` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
      "results": [
       {
        "count": 5
       }
      ]
    }




### Example - Delete documents

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DeleteDocuments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         {
           "collection": "Insurancedocuments",
           "filter": "{\"insurance.provider\":\"ABC\"}"}

This example deletes all the documents that have the insurance provider as `ABC`.




### Example - Find distinct values in a collection

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `DistinctValues` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {"collection":"restaurants","field":"contact"}

This example returns the distinct values in the `restaurants` collection. If the action is successful, the `Connectors` task's `connectorOutputPayload` response parameter will have a value similar to the following:
    
    {
     "results": [
      {
       "DistinctValues": [
        "3217902323",
        "8747479023",
        "3492619023"
       ]
      }
     ]
    }




### Example - Insert a document

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `InsertDocument` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         { {
         "collection": "Insurancedocuments",
         "document": "{\"fname\":\"firstName\",
         \"lname\":\"lastName\",
         \"passportId\":\"ABCD1234\",
         \"bloodType\":\"A\",
         \"medicalRecords\":[{\"item\":\"name1\"},{\"item\":\"name2\"}],
         \"insurance\":{\"policyNumber\":\"12345\",\"provider\":\"provider2\"}}"
         } }

This example inserts a document in the `Insurancedocuments` collection. The content of the document is specified in the `document` field. If the insert is successful, you will get the ID of inserted document in the `Connectors` task's `connectorOutputPayload` response parameter.




### Example - List documents

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `ListDocuments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {
         "collection": "Insurancedocuments",
         "filter": "{\"insurance.provider\":\"ABC\"}",
         "page_size": 10
         }

This example returns documents in the `Insurancedocuments` collection where the insurance provider is `ABC`. The result set's page size is set to 10 and list of files will be available to you in JSON format in the `Connectors` task's `connectorOutputPayload` response parameter.




### Example - Update documents

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateDocuments` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter a value similar to the following in the `Default Value` field: 
         
         {"collection":"Insurancedocuments",
         "values":" {$set: { lname:\"Smith\" }}",
         "filter":"{\"insurance.provider\":\"ABC\"}"}

This example updates the last name to `Smith` in the documents that match the filter criteria. If the update is successful, you will get the count of the number of documents that were updated. The response will be available in the `Connectors` task's `connectorOutputPayload` response parameter.




### Example - Update documents with encryption

  1. In the `Configure connector task` dialog, click `Actions`.
  2. Select the `UpdateDocumentsWithEncryption` action, and then click **Done**.
  3. In the **Task Input** section of the **Connectors** task, click `connectorInputPayload` and then enter the following in the `Default Value` field: 
         
         { {"collection":"Insurancedocuments",
         "document":" { \"insurance.provider\":\"XYZ\" }",
         "filter":"{\"insurance.provider\":\"ABC\"}"}

This example updates the insurance provider to `XYZ` in all the documents that have the insurance provider as `ABC`.




## Create connections using Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integration_connectors_connection) to create a new connection.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

To view a sample terraform template for connection creation, see [sample template](https://docs.cloud.google.com/integration-connectors/docs/sample-terraform-template).

When creating this connection by using Terraform, you must set the following variables in your Terraform configuration file:

Parameter name | Data type | Required | Description  
---|---|---|---  
database | STRING | True | The name of the MongoDB database.   
timeout | INTEGER | False | Connection timeout in secs.   
enable_ssl | BOOLEAN | False | This field sets whether SSL is enabled.   
app_name | STRING | False | Custom app name for MongoDB.   
max_staleness_seconds | INTEGER | False | Time in seconds how stale a secondary can be, before the client stops using it for read operations.   
write_concern | STRING | False | Option to request acknowledgment that the write operation has propagated to a specified number of instances with specified tags.   
write_concern_timeout | INTEGER | False | Specifies a time limit, in milliseconds, for the write concern.   
write_concern_journal | BOOLEAN | False | Requests acknowledgement from MongoDB that the write operation has been written to the journal.   
read_preference | ENUM | False | Read preferences for this connection. Supported values are: primary, primaryPreferred, secondary, secondaryPreferred, nearest  
cluster_type | ENUM | False | Specifies the type of MongoDB cluster. Supported values are: REPLICA_SET, STANDALONE, SHARDED, UNKNOWN  
enable_encryption | BOOLEAN | False | This field sets whether Encryption is enabled.   
encryption_type | ENUM | False | This field sets type of encryption enabled. Supported values are: local  
encryption_schema | STRING | False | Encryption schema information, including the fields and encryption algorithm used.   
encryption_master_key | SECRET | False | Secret Manager Secret containing the encryption master key.   
encryption_key_vault | STRING | False | Encryption Key Vault value.   
auth_database | STRING | True | The name of the MongoDB database for authentication.   
  
## Use the MongoDB connection in an integration

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
