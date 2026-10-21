---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ConnectSettings/
title: ConnectSettings \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:00.200318+00:00
---

# ConnectSettings  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ConnectSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  ConnectSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * CaMode
  * ConnectPoolNodeConfig
    * JSON representation
  * MdxProtocolSupport



Connect settings retrieval response.

JSON representation  
---  
      
    
    {
      "kind": string,
      "serverCaCert": {
        object ([SslCert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts#SslCert))
      },
      "ipAddresses": [
        {
          object ([IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.IpMapping))
        }
      ],
      "region": string,
      "databaseVersion": enum ([SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion)),
      "backendType": enum ([SqlBackendType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.SqlBackendType)),
      "pscEnabled": boolean,
      "dnsName": string,
      "serverCaMode": enum ([CaMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ConnectSettings#CaMode)),
      "customSubjectAlternativeNames": [
        string
      ],
      "dnsNames": [
        {
          object ([DnsNameMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.DnsNameMapping))
        }
      ],
      "nodes": [
        {
          object ([ConnectPoolNodeConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ConnectSettings#ConnectPoolNodeConfig))
        }
      ],
      "mdxProtocolSupport": [
        enum ([MdxProtocolSupport](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ConnectSettings#MdxProtocolSupport))
      ],
      "connectionName": string,
      "nodeCount": integer
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#connectSettings`.  
`serverCaCert` |  `object (`[SslCert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts#SslCert)`)` SSL configuration.  
`ipAddresses[]` |  `object (`[IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.IpMapping)`)` The assigned IP addresses for the instance.  
`region` |  `string` The cloud region for the instance. For example, `us-central1`, `europe-west1`. The region cannot be changed after instance creation.  
`databaseVersion` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion)`)` The database engine type and version. The `databaseVersion` field cannot be changed after instance creation. MySQL instances: `MYSQL_8_0`, `MYSQL_5_7` (default), or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12` (default), `POSTGRES_13`, or `POSTGRES_14`. SQL Server instances: `SQLSERVER_2017_STANDARD` (default), `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`.  
`backendType` |  `enum (`[SqlBackendType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.SqlBackendType)`)` `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google. This property is read-only; use the `tier` property in the `settings` object to determine the database type.  
`pscEnabled` |  `boolean` Whether PSC connectivity is enabled for this instance.  
`dnsName` |  `string` The dns name of the instance.  
`serverCaMode` |  `enum (`[CaMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ConnectSettings#CaMode)`)` Specify what type of CA is used for the server certificate.  
`customSubjectAlternativeNames[]` |  `string` Custom subject alternative names for the server certificate.  
`dnsNames[]` |  `object (`[DnsNameMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.DnsNameMapping)`)` Output only. The list of DNS names used by this instance.  
`nodes[]` |  `object (`[ConnectPoolNodeConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ConnectSettings#ConnectPoolNodeConfig)`)` Output only. Entries containing information about each read pool node of the read pool.  
`mdxProtocolSupport[]` |  `enum (`[MdxProtocolSupport](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/ConnectSettings#MdxProtocolSupport)`)` Optional. Output only. mdxProtocolSupport controls how the client uses metadata exchange when connecting to the instance. The values in the list representing parts of the MDX protocol that are supported by this instance. When the list is empty, the instance does not support MDX, so the client must not send an MDX request. The default is empty.  
`connectionName` |  `string` Optional. Output only. Connection name of the Cloud SQL instance used in connection strings, in the format project:region:instance.  
`nodeCount` |  `integer` The number of read pool nodes in a read pool.  
  
## CaMode

Various Certificate Authority (CA) modes for certificate signing.

Enums  
---  
`CA_MODE_UNSPECIFIED` | CA mode is unknown.  
`GOOGLE_MANAGED_INTERNAL_CA` | Google-managed self-signed internal CA.  
`GOOGLE_MANAGED_CAS_CA` | Google-managed regional CA part of root CA hierarchy hosted on Google Cloud's Certificate Authority Service (CAS).  
`CUSTOMER_MANAGED_CAS_CA` | Customer-managed CA hosted on Google Cloud's Certificate Authority Service (CAS).  
  
## ConnectPoolNodeConfig

Details of a single read pool node of a read pool.

JSON representation  
---  
      
    
    {
      "ipAddresses": [
        {
          object ([IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.IpMapping))
        }
      ],
      "dnsNames": [
        {
          object ([DnsNameMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.DnsNameMapping))
        }
      ],
      "name": string,
      "dnsName": string
    }  
  
Fields  
---  
`ipAddresses[]` |  `object (`[IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.IpMapping)`)` Output only. Mappings containing IP addresses that can be used to connect to the read pool node.  
`dnsNames[]` |  `object (`[DnsNameMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.DnsNameMapping)`)` Output only. The list of DNS names used by this read pool node.  
`name` |  `string` Output only. The name of the read pool node. Doesn't include the project ID.  
`dnsName` |  `string` Output only. The DNS name of the read pool node.  
  
## MdxProtocolSupport

MdxProtocolSupport describes parts of the MDX protocol supported by this instance.

Enums  
---  
`MDX_PROTOCOL_SUPPORT_UNSPECIFIED` | Not specified.  
`CLIENT_PROTOCOL_TYPE` | Client should send the client protocol type in the MDX request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
