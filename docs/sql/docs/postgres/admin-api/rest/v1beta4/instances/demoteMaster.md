---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster/
title: Method: instances.demoteMaster \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:31.638620+00:00
---

# Method: instances.demoteMaster  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  Method: instances.demoteMaster Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * InstancesDemoteMasterRequest
    * JSON representation
  * DemoteMasterContext
    * JSON representation
  * DemoteMasterConfiguration
    * JSON representation
  * DemoteMasterMySqlReplicaConfiguration
    * JSON representation
  * Examples
  * Try it!



Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.

### HTTP request

`POST https://sqladmin.googleapis.com/sql/v1beta4/projects/{project}/instances/{instance}/demoteMaster`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` ID of the project that contains the instance.  
`instance` |  `string` Cloud SQL instance name.  
  
### Request body

The request body contains an instance of `[InstancesDemoteMasterRequest](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster#InstancesDemoteMasterRequest)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## InstancesDemoteMasterRequest

Database demote primary instance request.

JSON representation  
---  
      
    
    {
      "demoteMasterContext": {
        object ([DemoteMasterContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster#DemoteMasterContext))
      }
    }  
  
Fields  
---  
`demoteMasterContext` |  `object (`[DemoteMasterContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster#DemoteMasterContext)`)` Contains details about the demoteMaster operation.  
  
## DemoteMasterContext

Database instance demote primary instance context.

JSON representation  
---  
      
    
    {
      "kind": string,
      "verifyGtidConsistency": boolean,
      "masterInstanceName": string,
      "replicaConfiguration": {
        object ([DemoteMasterConfiguration](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster#DemoteMasterConfiguration))
      },
      "skipReplicationSetup": boolean
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#demoteMasterContext`.  
`verifyGtidConsistency` |  `boolean` Verify the GTID consistency for demote operation. Default value: `True`. Setting this flag to `false` enables you to bypass the GTID consistency check between on-premises primary instance and Cloud SQL instance during the demotion operation but also exposes you to the risk of future replication failures. Change the value only if you know the reason for the GTID divergence and are confident that doing so will not cause any replication issues.  
`masterInstanceName` |  `string` The name of the instance which will act as on-premises primary instance in the replication setup.  
`replicaConfiguration` |  `object (`[DemoteMasterConfiguration](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster#DemoteMasterConfiguration)`)` Configuration specific to read-replicas replicating from the on-premises primary instance.  
`skipReplicationSetup` |  `boolean` Flag to skip replication setup on the instance.  
  
## DemoteMasterConfiguration

Read-replica configuration for connecting to the on-premises primary instance.

JSON representation  
---  
      
    
    {
      "kind": string,
      "mysqlReplicaConfiguration": {
        object ([DemoteMasterMySqlReplicaConfiguration](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster#DemoteMasterMySqlReplicaConfiguration))
      }
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#demoteMasterConfiguration`.  
`mysqlReplicaConfiguration` |  `object (`[DemoteMasterMySqlReplicaConfiguration](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/demoteMaster#DemoteMasterMySqlReplicaConfiguration)`)` MySQL specific configuration when replicating from a MySQL on-premises primary instance. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named `master.info` in the data directory.  
  
## DemoteMasterMySqlReplicaConfiguration

Read-replica configuration specific to MySQL databases.

JSON representation  
---  
      
    
    {
      "kind": string,
      "username": string,
      "password": string,
      "clientKey": string,
      "clientCertificate": string,
      "caCertificate": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#demoteMasterMysqlReplicaConfiguration`.  
`username` |  `string` The username for the replication connection.  
`password` |  `string` The password for the replication connection.  
`clientKey` |  `string` PEM representation of the replica's private key. The corresponding public key is encoded in the client's certificate. The format of the replica's private key can be either PKCS #1 or PKCS #8.  
`clientCertificate` |  `string` PEM representation of the replica's x509 certificate.  
`caCertificate` |  `string` PEM representation of the trusted CA's x509 certificate.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
