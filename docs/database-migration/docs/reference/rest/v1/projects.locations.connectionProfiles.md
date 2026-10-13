---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles
title: REST Resource: projects.locations.connectionProfiles \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:28.837332+00:00
---

# REST Resource: projects.locations.connectionProfiles  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  REST Resource: projects.locations.connectionProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConnectionProfile
    * JSON representation
  * State
  * Role
  * MySqlConnectionProfile
    * JSON representation
  * SslConfig
    * JSON representation
  * SslType
  * PostgreSqlConnectionProfile
    * JSON representation
  * NetworkArchitecture
  * PrivateServiceConnectConnectivity
    * JSON representation
  * ForwardSshTunnelConnectivity
    * JSON representation
  * PrivateConnectivity
    * JSON representation
  * SqlServerConnectionProfile
    * JSON representation
  * SqlServerBackups
    * JSON representation
  * OracleConnectionProfile
    * JSON representation
  * StaticServiceIpConnectivity
  * OracleAsmConfig
    * JSON representation
  * CloudSqlConnectionProfile
    * JSON representation
  * CloudSqlSettings
    * JSON representation
  * SqlDatabaseVersion
  * SqlActivationPolicy
  * SqlIpConfig
    * JSON representation
  * SqlAclEntry
    * JSON representation
  * SqlDataDiskType
  * SqlAvailabilityType
  * Edition
  * DataCacheConfig
    * JSON representation
  * AlloyDbConnectionProfile
    * JSON representation
  * AlloyDbSettings
    * JSON representation
  * UserPassword
    * JSON representation
  * PrimaryInstanceSettings
    * JSON representation
  * MachineConfig
    * JSON representation
  * InstanceNetworkConfig
    * JSON representation
  * AuthorizedNetwork
    * JSON representation
  * EncryptionConfig
    * JSON representation
  * DatabaseVersion
  * Methods



## Resource: ConnectionProfile

A connection profile definition.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#State)),
      "displayName": string,
      "role": enum ([Role](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#Role)),
      "error": {
        object ([Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "provider": enum ([DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider)),
    
      // Union field connection_profile can be only one of the following:
      "mysql": {
        object ([MySqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#MySqlConnectionProfile))
      },
      "postgresql": {
        object ([PostgreSqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PostgreSqlConnectionProfile))
      },
      "sqlserver": {
        object ([SqlServerConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlServerConnectionProfile))
      },
      "oracle": {
        object ([OracleConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#OracleConnectionProfile))
      },
      "cloudsql": {
        object ([CloudSqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#CloudSqlConnectionProfile))
      },
      "alloydb": {
        object ([AlloyDbConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#AlloyDbConnectionProfile))
      }
      // End of list of possible types for union field connection_profile.
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#State)`)` The current connection profile state (e.g. DRAFT, READY, or FAILED).  
`displayName` |  `string` The connection profile display name.  
`role` |  `enum (`[Role](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#Role)`)` Optional. The connection profile role.  
`error` |  `object (`[Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. The error details in case of state FAILED.  
`provider` |  `enum (`[DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider)`)` The database provider.  
Union field `connection_profile`. The connection profile definition. `connection_profile` can be only one of the following:  
`mysql` |  `object (`[MySqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#MySqlConnectionProfile)`)` A MySQL database connection profile.  
`postgresql` |  `object (`[PostgreSqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PostgreSqlConnectionProfile)`)` A PostgreSQL database connection profile.  
`sqlserver` |  `object (`[SqlServerConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlServerConnectionProfile)`)` Connection profile for a SQL Server data source.  
`oracle` |  `object (`[OracleConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#OracleConnectionProfile)`)` An Oracle database connection profile.  
`cloudsql` |  `object (`[CloudSqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#CloudSqlConnectionProfile)`)` A CloudSQL database connection profile.  
`alloydb` |  `object (`[AlloyDbConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#AlloyDbConnectionProfile)`)` An AlloyDB cluster connection profile.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
  
## State

The current connection profile state (e.g. DRAFT, READY, or FAILED).

Enums  
---  
`STATE_UNSPECIFIED` | The state of the connection profile is unknown.  
`DRAFT` | The connection profile is in draft mode and fully editable.  
`CREATING` | The connection profile is being created.  
`READY` | The connection profile is ready.  
`UPDATING` | The connection profile is being updated.  
`DELETING` | The connection profile is being deleted.  
`DELETED` | The connection profile has been deleted.  
`FAILED` | The last action on the connection profile failed.  
  
## Role

The connection profile role.

Enums  
---  
`ROLE_UNSPECIFIED` | The role is unspecified.  
`SOURCE` | The role is source.  
`DESTINATION` | The role is destination.  
  
## MySqlConnectionProfile

Specifies connection parameters required specifically for MySQL databases.

JSON representation  
---  
      
    
    {
      "host": string,
      "port": integer,
      "username": string,
      "password": string,
      "passwordSet": boolean,
      "ssl": {
        object ([SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig))
      },
      "cloudSqlId": string
    }  
  
Fields  
---  
`host` |  `string` Required. The IP or hostname of the source MySQL database.  
`port` |  `integer` Required. The network port of the source MySQL database.  
`username` |  `string` Required. The username that Database Migration Service will use to connect to the database. The value is encrypted when stored in Database Migration Service.  
`password` |  `string` Required. Input only. The password for the user that Database Migration Service will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Database Migration Service.  
`passwordSet` |  `boolean` Output only. Indicates If this connection profile password is stored.  
`ssl` |  `object (`[SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig)`)` SSL configuration for the destination to connect to the source database.  
`cloudSqlId` |  `string` If the source is a Cloud SQL database, use this field to provide the Cloud SQL instance ID of the source.  
  
## SslConfig

SSL configuration information.

JSON representation  
---  
      
    
    {
      "type": enum ([SslType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslType)),
      "clientKey": string,
      "clientCertificate": string,
      "caCertificate": string,
      "sslFlags": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`type` |  `enum (`[SslType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslType)`)` Optional. The ssl config type according to 'clientKey', 'clientCertificate' and 'caCertificate'.  
`clientKey` |  `string` Input only. The unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate. If this field is used then the 'clientCertificate' field is mandatory.  
`clientCertificate` |  `string` Input only. The x509 PEM-encoded certificate that will be used by the replica to authenticate against the source database server.If this field is used then the 'clientKey' field is mandatory.  
`caCertificate` |  `string` Required. Input only. The x509 PEM-encoded certificate of the CA that signed the source database server's certificate. The replica will use this certificate to verify it's connecting to the right host.  
`sslFlags` |  `map (key: string, value: string)` Optional. SSL flags used for establishing SSL connection to the source database. Only source specific flags are supported. An object containing a list of "key": "value" pairs. Example: { "server_certificate_hostname": "server.com"}.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## SslType

Specifies The kind of ssl configuration used.

Enums  
---  
`SSL_TYPE_UNSPECIFIED` | Unspecified.  
`SERVER_ONLY` | Only 'caCertificate' specified.  
`SERVER_CLIENT` | Both server ('caCertificate'), and client ('clientKey', 'clientCertificate') specified.  
`REQUIRED` | Mandates SSL encryption for all connections. This does not require certificate verification.  
`NONE` | Connection is not encrypted.  
  
## PostgreSqlConnectionProfile

Specifies connection parameters required specifically for PostgreSQL databases.

JSON representation  
---  
      
    
    {
      "host": string,
      "port": integer,
      "username": string,
      "password": string,
      "database": string,
      "passwordSet": boolean,
      "ssl": {
        object ([SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig))
      },
      "cloudSqlId": string,
      "alloydbClusterId": string,
      "networkArchitecture": enum ([NetworkArchitecture](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#NetworkArchitecture)),
      "enableIamAuthentication": boolean,
    
      // Union field connectivity can be only one of the following:
      "staticIpConnectivity": {
        object ([StaticIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/StaticIpConnectivity))
      },
      "privateServiceConnectConnectivity": {
        object ([PrivateServiceConnectConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateServiceConnectConnectivity))
      },
      "forwardSshConnectivity": {
        object ([ForwardSshTunnelConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity))
      },
      "privateConnectivity": {
        object ([PrivateConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateConnectivity))
      }
      // End of list of possible types for union field connectivity.
    }  
  
Fields  
---  
`host` |  `string` Required. The IP or hostname of the source PostgreSQL database.  
`port` |  `integer` Required. The network port of the source PostgreSQL database.  
`username` |  `string` Required. The username that Database Migration Service will use to connect to the database. The value is encrypted when stored in Database Migration Service.  
`password` |  `string` Required. Input only. The password for the user that Database Migration Service will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Database Migration Service.  
`database` |  `string` Optional. The name of the specific database within the host.  
`passwordSet` |  `boolean` Output only. Indicates If this connection profile password is stored.  
`ssl` |  `object (`[SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig)`)` SSL configuration for the destination to connect to the source database.  
`cloudSqlId` |  `string` If the source is a Cloud SQL database, use this field to provide the Cloud SQL instance ID of the source.  
`alloydbClusterId` |  `string` Optional. If the destination is an AlloyDB database, use this field to provide the AlloyDB cluster ID.  
`networkArchitecture` |  `enum (`[NetworkArchitecture](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#NetworkArchitecture)`)` Output only. If the source is a Cloud SQL database, this field indicates the network architecture it's associated with.  
`enableIamAuthentication` |  `boolean` Optional. If true, Database Migration Service will use IAM database authentication to connect to the database.  
Union field `connectivity`. Connectivity options used to establish a connection to the database server. `connectivity` can be only one of the following:  
`staticIpConnectivity` |  `object (`[StaticIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/StaticIpConnectivity)`)` Static ip connectivity data (default, no additional details needed).  
`privateServiceConnectConnectivity` |  `object (`[PrivateServiceConnectConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateServiceConnectConnectivity)`)` Private service connect connectivity.  
`forwardSshConnectivity` |  `object (`[ForwardSshTunnelConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity)`)` Forward SSH tunnel connectivity.  
`privateConnectivity` |  `object (`[PrivateConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateConnectivity)`)` Private connectivity.  
  
## NetworkArchitecture

Enums  
---  
`NETWORK_ARCHITECTURE_UNSPECIFIED` |   
`NETWORK_ARCHITECTURE_OLD_CSQL_PRODUCER` | Instance is in Cloud SQL's old producer network architecture.  
`NETWORK_ARCHITECTURE_NEW_CSQL_PRODUCER` | Instance is in Cloud SQL's new producer network architecture.  
  
## PrivateServiceConnectConnectivity

[Private Service Connect connectivity](https://cloud.google.com/vpc/docs/private-service-connect#service-attachments)

JSON representation  
---  
      
    
    {
      "serviceAttachment": string
    }  
  
Fields  
---  
`serviceAttachment` |  `string` Required. A service attachment that exposes a database, and has the following format: projects/{project}/regions/{region}/serviceAttachments/{service_attachment_name}  
  
## ForwardSshTunnelConnectivity

Forward SSH Tunnel connectivity.

JSON representation  
---  
      
    
    {
      "hostname": string,
      "username": string,
      "port": integer,
    
      // Union field authentication_method can be only one of the following:
      "password": string,
      "privateKey": string
      // End of list of possible types for union field authentication_method.
    }  
  
Fields  
---  
`hostname` |  `string` Required. Hostname for the SSH tunnel.  
`username` |  `string` Required. Username for the SSH tunnel.  
`port` |  `integer` Port for the SSH tunnel, default value is 22.  
Union field `authentication_method`.`authentication_method` can be only one of the following:  
`password` |  `string` Input only. SSH password.  
`privateKey` |  `string` Input only. SSH private key.  
  
## PrivateConnectivity

Private Connectivity.

JSON representation  
---  
      
    
    {
      "privateConnection": string
    }  
  
Fields  
---  
`privateConnection` |  `string` Required. The resource name (URI) of the private connection.  
  
## SqlServerConnectionProfile

Specifies connection parameters required specifically for SQL Server databases.

JSON representation  
---  
      
    
    {
      "host": string,
      "port": integer,
      "dbmPort": integer,
      "username": string,
      "password": string,
      "passwordSet": boolean,
      "ssl": {
        object ([SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig))
      },
      "cloudSqlProjectId": string,
      "cloudSqlId": string,
      "backups": {
        object ([SqlServerBackups](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlServerBackups))
      },
      "database": string,
    
      // Union field connectivity can be only one of the following:
      "staticIpConnectivity": {
        object ([StaticIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/StaticIpConnectivity))
      },
      "forwardSshConnectivity": {
        object ([ForwardSshTunnelConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity))
      },
      "privateConnectivity": {
        object ([PrivateConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateConnectivity))
      },
      "privateServiceConnectConnectivity": {
        object ([PrivateServiceConnectConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateServiceConnectConnectivity))
      }
      // End of list of possible types for union field connectivity.
    }  
  
Fields  
---  
`host` |  `string` Required. The IP or hostname of the source SQL Server database.  
`port` |  `integer` Required. The network port of the source SQL Server database.  
`dbmPort` |  `integer` Optional. The Database Mirroring (DBM) port of the source SQL Server instance.  
`username` |  `string` Required. The username that Database Migration Service will use to connect to the database. The value is encrypted when stored in Database Migration Service.  
`password` |  `string` Required. Input only. The password for the user that Database Migration Service will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Database Migration Service.  
`passwordSet` |  `boolean` Output only. Indicates whether a new password is included in the request.  
`ssl` |  `object (`[SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig)`)` SSL configuration for the destination to connect to the source database.  
`cloudSqlProjectId` |  `string` Optional. The project id of the Cloud SQL instance. If not provided, the project id of the connection profile will be used.  
`cloudSqlId` |  `string` If the source is a Cloud SQL database, use this field to provide the Cloud SQL instance ID of the source.  
`backups` |  `object (`[SqlServerBackups](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlServerBackups)`)` The backup details in Cloud Storage for homogeneous migration to Cloud SQL for SQL Server.  
`database` |  `string` Required. The name of the specific database within the host.  
Union field `connectivity`. Connectivity options used to establish a connection to the database server. `connectivity` can be only one of the following:  
`staticIpConnectivity` |  `object (`[StaticIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/StaticIpConnectivity)`)` Static IP connectivity data (default, no additional details needed).  
`forwardSshConnectivity` |  `object (`[ForwardSshTunnelConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity)`)` Forward SSH tunnel connectivity.  
`privateConnectivity` |  `object (`[PrivateConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateConnectivity)`)` Private connectivity.  
`privateServiceConnectConnectivity` |  `object (`[PrivateServiceConnectConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateServiceConnectConnectivity)`)` Private Service Connect connectivity.  
  
## SqlServerBackups

Specifies the backup details in Cloud Storage for homogeneous migration to Cloud SQL for SQL Server.

JSON representation  
---  
      
    
    {
      "gcsBucket": string,
      "gcsPrefix": string
    }  
  
Fields  
---  
`gcsBucket` |  `string` Required. The Cloud Storage bucket that stores backups for all replicated databases.  
`gcsPrefix` |  `string` Optional. Cloud Storage path inside the bucket that stores backups.  
  
## OracleConnectionProfile

Specifies connection parameters required specifically for Oracle databases.

JSON representation  
---  
      
    
    {
      "host": string,
      "port": integer,
      "username": string,
      "password": string,
      "passwordSet": boolean,
      "databaseService": string,
      "ssl": {
        object ([SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig))
      },
      "oracleAsmConfig": {
        object ([OracleAsmConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#OracleAsmConfig))
      },
    
      // Union field connectivity can be only one of the following:
      "staticServiceIpConnectivity": {
        object ([StaticServiceIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#StaticServiceIpConnectivity))
      },
      "forwardSshConnectivity": {
        object ([ForwardSshTunnelConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity))
      },
      "privateConnectivity": {
        object ([PrivateConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateConnectivity))
      }
      // End of list of possible types for union field connectivity.
    }  
  
Fields  
---  
`host` |  `string` Required. The IP or hostname of the source Oracle database.  
`port` |  `integer` Required. The network port of the source Oracle database.  
`username` |  `string` Required. The username that Database Migration Service will use to connect to the database. The value is encrypted when stored in Database Migration Service.  
`password` |  `string` Required. Input only. The password for the user that Database Migration Service will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Database Migration Service.  
`passwordSet` |  `boolean` Output only. Indicates whether a new password is included in the request.  
`databaseService` |  `string` Required. Database service for the Oracle connection.  
`ssl` |  `object (`[SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig)`)` SSL configuration for the connection to the source Oracle database.

  * Only `SERVER_ONLY` configuration is supported for Oracle SSL.
  * SSL is supported for Oracle versions 12 and above.

  
`oracleAsmConfig` |  `object (`[OracleAsmConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#OracleAsmConfig)`)` Optional. Configuration for Oracle ASM connection.  
Union field `connectivity`. Connectivity options used to establish a connection to the database server. `connectivity` can be only one of the following:  
`staticServiceIpConnectivity` |  `object (`[StaticServiceIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#StaticServiceIpConnectivity)`)` Static Service IP connectivity.  
`forwardSshConnectivity` |  `object (`[ForwardSshTunnelConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity)`)` Forward SSH tunnel connectivity.  
`privateConnectivity` |  `object (`[PrivateConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrivateConnectivity)`)` Private connectivity.  
  
## StaticServiceIpConnectivity

This type has no fields.

Static IP address connectivity configured on service project.

## OracleAsmConfig

Configuration for Oracle Automatic Storage Management (ASM) connection.

JSON representation  
---  
      
    
    {
      "hostname": string,
      "port": integer,
      "username": string,
      "password": string,
      "passwordSet": boolean,
      "asmService": string,
      "ssl": {
        object ([SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig))
      }
    }  
  
Fields  
---  
`hostname` |  `string` Required. Hostname for the Oracle ASM connection.  
`port` |  `integer` Required. Port for the Oracle ASM connection.  
`username` |  `string` Required. Username for the Oracle ASM connection.  
`password` |  `string` Required. Input only. Password for the Oracle ASM connection.  
`passwordSet` |  `boolean` Output only. Indicates whether a new password is included in the request.  
`asmService` |  `string` Required. ASM service name for the Oracle ASM connection.  
`ssl` |  `object (`[SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SslConfig)`)` Optional. SSL configuration for the Oracle connection.  
  
## CloudSqlConnectionProfile

Specifies required connection parameters, and, optionally, the parameters required to create a Cloud SQL destination database instance.

JSON representation  
---  
      
    
    {
      "cloudSqlId": string,
      "settings": {
        object ([CloudSqlSettings](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#CloudSqlSettings))
      },
      "privateIp": string,
      "publicIp": string,
      "additionalPublicIp": string
    }  
  
Fields  
---  
`cloudSqlId` |  `string` Output only. The Cloud SQL instance ID that this connection profile is associated with.  
`settings` |  `object (`[CloudSqlSettings](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#CloudSqlSettings)`)` Immutable. Metadata used to create the destination Cloud SQL database.  
`privateIp` |  `string` Output only. The Cloud SQL database instance's private IP.  
`publicIp` |  `string` Output only. The Cloud SQL database instance's public IP.  
`additionalPublicIp` |  `string` Output only. The Cloud SQL database instance's additional (outgoing) public IP. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available).  
  
## CloudSqlSettings

Settings for creating a Cloud SQL database instance.

JSON representation  
---  
      
    
    {
      "databaseVersion": enum ([SqlDatabaseVersion](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlDatabaseVersion)),
      "databaseVersionName": string,
      "userLabels": {
        string: string,
        ...
      },
      "tier": string,
      "storageAutoResizeLimit": string,
      "activationPolicy": enum ([SqlActivationPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlActivationPolicy)),
      "ipConfig": {
        object ([SqlIpConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlIpConfig))
      },
      "autoStorageIncrease": boolean,
      "databaseFlags": {
        string: string,
        ...
      },
      "dataDiskType": enum ([SqlDataDiskType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlDataDiskType)),
      "dataDiskSizeGb": string,
      "zone": string,
      "secondaryZone": string,
      "sourceId": string,
      "rootPassword": string,
      "rootPasswordSet": boolean,
      "collation": string,
      "cmekKeyName": string,
      "availabilityType": enum ([SqlAvailabilityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlAvailabilityType)),
      "edition": enum ([Edition](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#Edition)),
      "dataCacheConfig": {
        object ([DataCacheConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#DataCacheConfig))
      },
      "dataDiskProvisionedIops": string,
      "dataDiskProvisionedThroughput": string
    }  
  
Fields  
---  
`databaseVersion` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlDatabaseVersion)`)` The database engine type and version. Deprecated. Use databaseVersionName instead.  
`databaseVersionName` |  `string` Optional. The database engine type and version name.  
`userLabels` |  `map (key: string, value: string)` The resource labels for a Cloud SQL instance to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.Example: `{ "name": "wrench", "mass": "18kg", "count": "3" }`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`tier` |  `string` The tier (or machine type) for this instance, for example: `db-n1-standard-1` (MySQL instances) or `db-custom-1-3840` (PostgreSQL instances). For more information, see [Cloud SQL Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings).  
`storageAutoResizeLimit` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit.  
`activationPolicy` |  `enum (`[SqlActivationPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlActivationPolicy)`)` The activation policy specifies when the instance is activated; it is applicable only when the instance state is 'RUNNABLE'. Valid values:'ALWAYS': The instance is on, and remains so even in the absence of connection requests.`NEVER`: The instance is off; it is not activated, even if a connection request arrives.  
`ipConfig` |  `object (`[SqlIpConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlIpConfig)`)` The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled.  
`autoStorageIncrease` |  `boolean` [default: ON] If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 30 TB.  
`databaseFlags` |  `map (key: string, value: string)` The database flags passed to the Cloud SQL instance at startup. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`dataDiskType` |  `enum (`[SqlDataDiskType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlDataDiskType)`)` The type of storage: `PD_SSD` (default) or `PD_HDD` or `HYPERDISK_BALANCED`.  
`dataDiskSizeGb` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The storage capacity available to the database, in GB. The minimum (and default) size is 10GB.  
`zone` |  `string` The Google Cloud Platform zone where your Cloud SQL database instance is located.  
`secondaryZone` |  `string` Optional. The Google Cloud Platform zone where the failover Cloud SQL database instance is located. Used when the Cloud SQL database availability type is REGIONAL (i.e. multiple zones / highly available).  
`sourceId` |  `string` The Database Migration Service source connection profile ID, in the format: `projects/my_project_name/locations/us-central1/connectionProfiles/connection_profile_ID`  
`rootPassword` |  `string` Input only. Initial root password.  
`rootPasswordSet` |  `boolean` Output only. Indicates If this connection profile root password is stored.  
`collation` |  `string` The Cloud SQL default instance level collation.  
`cmekKeyName` |  `string` The KMS key name used for the csql instance.  
`availabilityType` |  `enum (`[SqlAvailabilityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlAvailabilityType)`)` Optional. Availability type. Potential values: * `ZONAL`: The instance serves data from only one zone. Outages in that zone affect data availability. * `REGIONAL`: The instance can serve data from more than one zone in a region (it is highly available).  
`edition` |  `enum (`[Edition](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#Edition)`)` Optional. The edition of the given Cloud SQL instance.  
`dataCacheConfig` |  `object (`[DataCacheConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#DataCacheConfig)`)` Optional. Data cache is an optional feature available for Cloud SQL for MySQL Enterprise Plus edition only. For more information on data cache, see [Data cache overview](https://cloud.google.com/sql/help/mysql-data-cache) in Cloud SQL documentation.  
`dataDiskProvisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Provisioned number of I/O operations per second for the data disk. This field is only used for hyperdisk-balanced disk types.  
`dataDiskProvisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Provisioned throughput measured in MiB per second for the data disk. This field is only used for hyperdisk-balanced disk types.  
  
## SqlDatabaseVersion

The database engine type and version.

Enums  
---  
`SQL_DATABASE_VERSION_UNSPECIFIED` | Unspecified version.  
`MYSQL_5_6` | MySQL 5.6.  
`MYSQL_5_7` | MySQL 5.7.  
`MYSQL_8_0` | MySQL 8.0.  
`MYSQL_8_0_18` | The database major version is MySQL 8.0 and the minor version is 18.  
`MYSQL_8_0_26` | The database major version is MySQL 8.0 and the minor version is 26.  
`MYSQL_8_0_27` | The database major version is MySQL 8.0 and the minor version is 27.  
`MYSQL_8_0_28` | The database major version is MySQL 8.0 and the minor version is 28.  
`MYSQL_8_0_30` | The database major version is MySQL 8.0 and the minor version is 30.  
`MYSQL_8_0_31` | The database major version is MySQL 8.0 and the minor version is 31.  
`MYSQL_8_0_32` | The database major version is MySQL 8.0 and the minor version is 32.  
`MYSQL_8_0_33` | The database major version is MySQL 8.0 and the minor version is 33.  
`MYSQL_8_0_34` | The database major version is MySQL 8.0 and the minor version is 34.  
`MYSQL_8_0_35` | The database major version is MySQL 8.0 and the minor version is 35.  
`MYSQL_8_0_36` | The database major version is MySQL 8.0 and the minor version is 36.  
`MYSQL_8_0_37` | The database major version is MySQL 8.0 and the minor version is 37.  
`MYSQL_8_4` | MySQL 8.4.  
`POSTGRES_9_6` | PostgreSQL 9.6.  
`POSTGRES_11` | PostgreSQL 11.  
`POSTGRES_10` | PostgreSQL 10.  
`POSTGRES_12` | PostgreSQL 12.  
`POSTGRES_13` | PostgreSQL 13.  
`POSTGRES_14` | PostgreSQL 14.  
`POSTGRES_15` | PostgreSQL 15.  
`POSTGRES_16` | PostgreSQL 16.  
  
## SqlActivationPolicy

Specifies when the instance should be activated.

Enums  
---  
`SQL_ACTIVATION_POLICY_UNSPECIFIED` | unspecified policy.  
`ALWAYS` | The instance is always up and running.  
`NEVER` | The instance should never spin up.  
  
## SqlIpConfig

IP Management configuration.

JSON representation  
---  
      
    
    {
      "enableIpv4": boolean,
      "privateNetwork": string,
      "allocatedIpRange": string,
      "requireSsl": boolean,
      "authorizedNetworks": [
        {
          object ([SqlAclEntry](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlAclEntry))
        }
      ]
    }  
  
Fields  
---  
`enableIpv4` |  `boolean` Whether the instance should be assigned an IPv4 address or not.  
`privateNetwork` |  `string` The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, `projects/myProject/global/networks/default`. This setting can be updated, but it cannot be removed after it is set.  
`allocatedIpRange` |  `string` Optional. The name of the allocated IP address range for the private IP Cloud SQL instance. This name refers to an already allocated IP range address. If set, the instance IP address will be created in the allocated range. Note that this IP address range can't be modified after the instance is created. If you change the VPC when configuring connectivity settings for the migration job, this field is not relevant.  
`requireSsl` |  `boolean` Whether SSL connections over IP should be enforced or not.  
`authorizedNetworks[]` |  `object (`[SqlAclEntry](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#SqlAclEntry)`)` The list of external networks that are allowed to connect to the instance using the IP. See <https://en.wikipedia.org/wiki/CIDR_notation#CIDR_notation>, also known as 'slash' notation (e.g. `192.168.100.0/24`).  
  
## SqlAclEntry

An entry for an Access Control list.

JSON representation  
---  
      
    
    {
      "value": string,
      "label": string,
    
      // Union field expiration can be only one of the following:
      "expireTime": string,
      "ttl": string
      // End of list of possible types for union field expiration.
    }  
  
Fields  
---  
`value` |  `string` The allowlisted value for the access control list.  
`label` |  `string` A label to identify this entry.  
Union field `expiration`. The access control entry entry expiration. `expiration` can be only one of the following:  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when this access control entry expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example: `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Input only. The time-to-leave of this access control entry.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## SqlDataDiskType

The storage options for Cloud SQL databases.

Enums  
---  
`SQL_DATA_DISK_TYPE_UNSPECIFIED` | Unspecified.  
`PD_SSD` | SSD disk.  
`PD_HDD` | HDD disk.  
`HYPERDISK_BALANCED` | A Hyperdisk Balanced data disk.  
  
## SqlAvailabilityType

The availability type of the given Cloud SQL instance.

Enums  
---  
`SQL_AVAILABILITY_TYPE_UNSPECIFIED` | This is an unknown Availability type.  
`ZONAL` | Zonal availablility instance.  
`REGIONAL` | Regional availability instance.  
  
## Edition

The edition of the given Cloud SQL instance. Can be ENTERPRISE or ENTERPRISE_PLUS.

Enums  
---  
`EDITION_UNSPECIFIED` | The instance did not specify the edition.  
`ENTERPRISE` | The instance is an enterprise edition.  
`ENTERPRISE_PLUS` | The instance is an enterprise plus edition.  
  
## DataCacheConfig

Data cache is an optional feature available for Cloud SQL for MySQL Enterprise Plus edition only. For more information on data cache, see [Data cache overview](https://cloud.google.com/sql/help/mysql-data-cache) in Cloud SQL documentation.

JSON representation  
---  
      
    
    {
      "dataCacheEnabled": boolean
    }  
  
Fields  
---  
`dataCacheEnabled` |  `boolean` Optional. Whether data cache is enabled for the instance.  
  
## AlloyDbConnectionProfile

Specifies required connection parameters, and the parameters required to create an AlloyDB destination cluster.

JSON representation  
---  
      
    
    {
      "clusterId": string,
      "settings": {
        object ([AlloyDbSettings](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#AlloyDbSettings))
      }
    }  
  
Fields  
---  
`clusterId` |  `string` Required. The AlloyDB cluster ID that this connection profile is associated with.  
`settings` |  `object (`[AlloyDbSettings](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#AlloyDbSettings)`)` Immutable. Metadata used to create the destination AlloyDB cluster.  
  
## AlloyDbSettings

Settings for creating an AlloyDB cluster.

JSON representation  
---  
      
    
    {
      "initialUser": {
        object ([UserPassword](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#UserPassword))
      },
      "vpcNetwork": string,
      "labels": {
        string: string,
        ...
      },
      "primaryInstanceSettings": {
        object ([PrimaryInstanceSettings](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrimaryInstanceSettings))
      },
      "encryptionConfig": {
        object ([EncryptionConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#EncryptionConfig))
      },
      "databaseVersion": enum ([DatabaseVersion](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#DatabaseVersion))
    }  
  
Fields  
---  
`initialUser` |  `object (`[UserPassword](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#UserPassword)`)` Required. Input only. Initial user to setup during cluster creation. Required.  
`vpcNetwork` |  `string` Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: "projects/{projectNumber}/global/networks/{network_id}". This is required to create a cluster.  
`labels` |  `map (key: string, value: string)` Labels for the AlloyDB cluster created by DMS. An object containing a list of 'key', 'value' pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`primaryInstanceSettings` |  `object (`[PrimaryInstanceSettings](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#PrimaryInstanceSettings)`)` Settings for the cluster's primary instance  
`encryptionConfig` |  `object (`[EncryptionConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#EncryptionConfig)`)` Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.  
`databaseVersion` |  `enum (`[DatabaseVersion](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#DatabaseVersion)`)` Optional. The database engine major version. This is an optional field. If a database version is not supplied at cluster creation time, then a default database version will be used.  
  
## UserPassword

The username/password for a database user. Used for specifying initial users at cluster creation time.

JSON representation  
---  
      
    
    {
      "user": string,
      "password": string,
      "passwordSet": boolean
    }  
  
Fields  
---  
`user` |  `string` The database username.  
`password` |  `string` The initial password for the user.  
`passwordSet` |  `boolean` Output only. Indicates if the initialUser.password field has been set.  
  
## PrimaryInstanceSettings

Settings for the cluster's primary instance

JSON representation  
---  
      
    
    {
      "id": string,
      "machineConfig": {
        object ([MachineConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#MachineConfig))
      },
      "databaseFlags": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      },
      "privateIp": string,
      "instanceNetworkConfig": {
        object ([InstanceNetworkConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#InstanceNetworkConfig))
      },
      "outboundPublicIpAddresses": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. The ID of the AlloyDB primary instance. The ID must satisfy the regex expression "[a-z0-9-]+".  
`machineConfig` |  `object (`[MachineConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#MachineConfig)`)` Configuration for the machines that host the underlying database engine.  
`databaseFlags` |  `map (key: string, value: string)` Database flags to pass to AlloyDB when DMS is creating the AlloyDB cluster and instances. See the AlloyDB documentation for how these can be used.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Labels for the AlloyDB primary instance created by DMS. An object containing a list of 'key', 'value' pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`privateIp` |  `string` Output only. The private IP address for the Instance. This is the connection endpoint for an end-user application.  
`instanceNetworkConfig` |  `object (`[InstanceNetworkConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#InstanceNetworkConfig)`)` Optional. Metadata related to instance level network configuration.  
`outboundPublicIpAddresses[]` |  `string` Output only. All outbound public IP addresses configured for the instance.  
  
## MachineConfig

MachineConfig describes the configuration of a machine.

JSON representation  
---  
      
    
    {
      "cpuCount": integer,
      "machineType": string
    }  
  
Fields  
---  
`cpuCount` |  `integer` The number of CPU's in the VM instance.  
`machineType` |  `string` Optional. Machine type of the VM instance. E.g. "n2-highmem-4", "n2-highmem-8", "c4a-highmem-4-lssd". cpuCount must match the number of vCPUs in the machine type.  
  
## InstanceNetworkConfig

Metadata related to instance level network configuration.

JSON representation  
---  
      
    
    {
      "authorizedExternalNetworks": [
        {
          object ([AuthorizedNetwork](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#AuthorizedNetwork))
        }
      ],
      "enablePublicIp": boolean,
      "enableOutboundPublicIp": boolean
    }  
  
Fields  
---  
`authorizedExternalNetworks[]` |  `object (`[AuthorizedNetwork](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles#AuthorizedNetwork)`)` Optional. A list of external network authorized to access this instance.  
`enablePublicIp` |  `boolean` Optional. Enabling public ip for the instance.  
`enableOutboundPublicIp` |  `boolean` Optional. Enabling an outbound public IP address to support a database server sending requests out into the internet.  
  
## AuthorizedNetwork

AuthorizedNetwork contains metadata for an authorized network.

JSON representation  
---  
      
    
    {
      "cidrRange": string
    }  
  
Fields  
---  
`cidrRange` |  `string` Optional. CIDR range for one authorzied network of the instance.  
  
## EncryptionConfig

EncryptionConfig describes the encryption config of a cluster that is encrypted with a CMEK (customer-managed encryption key).

JSON representation  
---  
      
    
    {
      "kmsKeyName": string
    }  
  
Fields  
---  
`kmsKeyName` |  `string` The fully-qualified resource name of the KMS key. Each Cloud KMS key is regionalized and has the following format: projects/[PROJECT]/locations/[REGION]/keyRings/[RING]/cryptoKeys/[KEY_NAME]  
  
## DatabaseVersion

The supported database engine versions.

Enums  
---  
`DATABASE_VERSION_UNSPECIFIED` | This is an unknown database version.  
`POSTGRES_14` | The database version is Postgres 14.  
`POSTGRES_15` | The database version is Postgres 15.  
`POSTGRES_16` | The database version is Postgres 16.  
`POSTGRES_17` | The database version is Postgres 17.  
`POSTGRES_18` | The database version is Postgres 18.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/create)`

|  Creates a new connection profile in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/delete)`

|  Deletes a single Database Migration Service connection profile.  
  
### `[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/get)`

|  Gets details of a single connection profile.  
  
### `[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/list)`

|  Retrieves a list of all connection profiles in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/patch)`

|  Update the configuration of a single connection profile.  
  
### `[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
