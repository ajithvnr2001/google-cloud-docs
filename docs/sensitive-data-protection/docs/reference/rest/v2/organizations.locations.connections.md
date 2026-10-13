---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections
title: REST Resource: organizations.locations.connections \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:22.507520+00:00
---

# REST Resource: organizations.locations.connections  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.connections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Connection
    * JSON representation
    * ConnectionState
    * CloudSqlProperties
      * JSON representation
    * SecretManagerCredential
      * JSON representation
    * CloudSqlIamCredential
    * DatabaseEngine
  * Methods



## Resource: Connection

A data connection to allow the DLP API to profile data in locations that require additional configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([ConnectionState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.ConnectionState)),
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cloudSql": {
        object ([CloudSqlProperties](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.CloudSqlProperties))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the connection: `projects/{project}/locations/{location}/connections/{name}`.  
`state` |  `enum (`[ConnectionState](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.ConnectionState)`)` Required. The connection's state in its lifecycle.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` Output only. Set if status == ERROR, to provide additional details. Will store the last 10 errors sorted with the most recent first.  
Type of connection. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cloudSql` |  `object (`[CloudSqlProperties](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.CloudSqlProperties)`)` Connect to a Cloud SQL instance.  
End of mutually exclusive fields.  
  
### ConnectionState

State of the connection. New values may be added over time.

Enums  
---  
`CONNECTION_STATE_UNSPECIFIED` | Unused  
`MISSING_CREDENTIALS` | The DLP API automatically created this connection during an initial scan, and it is awaiting full configuration by a user.  
`AVAILABLE` | A configured connection that has not encountered any errors.  
`ERROR` | A configured connection that encountered errors during its last use. It will not be used again until it is set to AVAILABLE.If the resolution requires external action, then the client must send a request to set the status to AVAILABLE when the connection is ready for use. If the resolution doesn't require external action, then any changes to the connection properties will automatically mark it as AVAILABLE.  
  
### CloudSqlProperties

Cloud SQL connection properties.

JSON representation  
---  
      
    
    {
      "connectionName": string,
      "maxConnections": integer,
      "databaseEngine": enum ([DatabaseEngine](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.DatabaseEngine)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "usernamePassword": {
        object ([SecretManagerCredential](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.SecretManagerCredential))
      },
      "cloudSqlIam": {
        object ([CloudSqlIamCredential](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.CloudSqlIamCredential))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`connectionName` |  `string` Optional. Immutable. The Cloud SQL instance for which the connection is defined. Only one connection per instance is allowed. This can only be set at creation time, and cannot be updated.It is an error to use a connectionName from different project or region than the one that holds the connection. For example, a Connection resource for Cloud SQL connectionName `project-id:us-central1:sql-instance` must be created under the parent `projects/project-id/locations/us-central1`  
`maxConnections` |  `integer` Required. The DLP API will limit its connections to maxConnections. Must be 2 or greater.  
`databaseEngine` |  `enum (`[DatabaseEngine](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.DatabaseEngine)`)` Required. The database engine used by the Cloud SQL instance that this connection configures.  
How to authenticate to the instance. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`usernamePassword` |  `object (`[SecretManagerCredential](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.SecretManagerCredential)`)` A username and password stored in Secret Manager.  
`cloudSqlIam` |  `object (`[CloudSqlIamCredential](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections#Connection.CloudSqlIamCredential)`)` Built-in IAM authentication (must be configured in Cloud SQL).  
End of mutually exclusive fields.  
  
### SecretManagerCredential

A credential consisting of a username and password, where the password is stored in a Secret Manager resource. Note: Secret Manager [charges apply](https://cloud.google.com/secret-manager/pricing).

JSON representation  
---  
      
    
    {
      "username": string,
      "passwordSecretVersionName": string
    }  
  
Fields  
---  
`username` |  `string` Required. The username.  
`passwordSecretVersionName` |  `string` Required. The name of the Secret Manager resource that stores the password, in the form `projects/project-id/secrets/secret-name/versions/version`.  
  
### CloudSqlIamCredential

This type has no fields.

Use IAM authentication to connect. This requires the Cloud SQL IAM feature to be enabled on the instance, which is not the default for Cloud SQL. See <https://docs.cloud.google.com/sql/docs/postgres/authentication> and <https://docs.cloud.google.com/sql/docs/mysql/authentication>.

### DatabaseEngine

Database engine of a Cloud SQL instance. New values may be added over time.

Enums  
---  
`DATABASE_ENGINE_UNKNOWN` | An engine that is not currently supported by Sensitive Data Protection.  
`DATABASE_ENGINE_MYSQL` | Cloud SQL for MySQL instance.  
`DATABASE_ENGINE_POSTGRES` | Cloud SQL for PostgreSQL instance.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/create)`

|  Create a Connection to an external data source.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/delete)`

|  Delete a Connection.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/get)`

|  Get a Connection by name.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/list)`

|  Lists Connections in a parent.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/patch)`

|  Update a Connection.  
  
### `[search](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/search)`

|  Searches for Connections in a parent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
