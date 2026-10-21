---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases/
title: REST Resource: databases \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:37.266577+00:00
---

# REST Resource: databases  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  REST Resource: databases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Database
    * JSON representation
  * SqlServerDatabaseDetails
    * JSON representation
  * Methods



## Resource: Database

Represents a SQL database on the Cloud SQL instance.

JSON representation  
---  
      
    
    {
      "kind": string,
      "charset": string,
      "collation": string,
      "etag": string,
      "name": string,
      "instance": string,
      "selfLink": string,
      "project": string,
    
      // Union field database_details can be only one of the following:
      "sqlserverDatabaseDetails": {
        object ([SqlServerDatabaseDetails](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases#SqlServerDatabaseDetails))
      }
      // End of list of possible types for union field database_details.
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#database`.  
`charset` |  `string` The Cloud SQL charset value.  
`collation` |  `string` The Cloud SQL collation value.  
`etag` |  `string` This field is deprecated and will be removed from a future version of the API.  
`name` |  `string` The name of the database in the Cloud SQL instance. This does not include the project ID or instance name.  
`instance` |  `string` The name of the Cloud SQL instance. This does not include the project ID.  
`selfLink` |  `string` The URI of this resource.  
`project` |  `string` The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable.  
Union field `database_details`.`database_details` can be only one of the following:  
`sqlserverDatabaseDetails` |  `object (`[SqlServerDatabaseDetails](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases#SqlServerDatabaseDetails)`)`  
  
## SqlServerDatabaseDetails

Represents a Sql Server database on the Cloud SQL instance.

JSON representation  
---  
      
    
    {
      "compatibilityLevel": integer,
      "recoveryModel": string
    }  
  
Fields  
---  
`compatibilityLevel` |  `integer` The version of SQL Server with which the database is to be made compatible  
`recoveryModel` |  `string` The recovery model of a SQL Server database  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases/delete)`

|  Deletes a database from a Cloud SQL instance.  
  
### `[get](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases/get)`

|  Retrieves a resource containing information about a database inside a Cloud SQL instance.  
  
### `[insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases/insert)`

|  Inserts a resource containing information about a database inside a Cloud SQL instance.  
  
### `[list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases/list)`

|  Lists databases in the specified Cloud SQL instance.  
  
### `[patch](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases/patch)`

|  Partially updates a resource containing information about a database inside a Cloud SQL instance.  
  
### `[update](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/databases/update)`

|  Updates a resource containing information about a database inside a Cloud SQL instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
