---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles
title: REST Resource: projects.locations.connectionProfiles \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:48.560534+00:00
---

# REST Resource: projects.locations.connectionProfiles  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles

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
  * MySqlConnectionProfile
    * JSON representation
  * SslConfig
    * JSON representation
  * SslType
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
      "state": enum ([State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#State)),
      "displayName": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "provider": enum ([DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/DatabaseProvider)),
    
      // Union field connection_profile can be only one of the following:
      "mysql": {
        object ([MySqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#MySqlConnectionProfile))
      },
      "cloudsql": {
        object ([CloudSqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#CloudSqlConnectionProfile))
      }
      // End of list of possible types for union field connection_profile.
    }  
  
Fields  
---  
`name` |  `string` The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#State)`)` The current connection profile state (e.g. DRAFT, READY, or FAILED).  
`displayName` |  `string` The connection profile display name.  
`error` |  `object (`[Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. The error details in case of state FAILED.  
`provider` |  `enum (`[DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/DatabaseProvider)`)` The database provider.  
Union field `connection_profile`. The connection profile definition. `connection_profile` can be only one of the following:  
`mysql` |  `object (`[MySqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#MySqlConnectionProfile)`)` A MySQL database connection profile.  
`cloudsql` |  `object (`[CloudSqlConnectionProfile](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#CloudSqlConnectionProfile)`)` A CloudSQL database connection profile.  
  
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
  
## MySqlConnectionProfile

Specifies connection parameters required specifically for MySQL databases.

JSON representation  
---  
      
    
    {
      "host": string,
      "port": integer,
      "username": string,
      "password": string,
      "ssl": {
        object ([SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SslConfig))
      },
      "cloudSqlId": string,
      "hasPassword": boolean
    }  
  
Fields  
---  
`host` |  `string` Required. The IP or hostname of the source MySQL database.  
`port` |  `integer` Required. The network port of the source MySQL database.  
`username` |  `string` Required. The username that Database Migration Service will use to connect to the database. The value is encrypted when stored in Database Migration Service.  
`password` |  `string` Required. Input only. The password for the user that Database Migration Service will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Database Migration Service.  
`ssl` |  `object (`[SslConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SslConfig)`)` SSL configuration for the destination to connect to the source database.  
`cloudSqlId` |  `string` If the source is a Cloud SQL database, use this field to provide the Cloud SQL instance ID of the source.  
`hasPassword` |  `boolean` Output only. Indicates If this connection profile password is stored.  
  
## SslConfig

SSL configuration information.

JSON representation  
---  
      
    
    {
      "type": enum ([SslType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SslType)),
      "clientKey": string,
      "clientCertificate": string,
      "caCertificate": string
    }  
  
Fields  
---  
`type` |  `enum (`[SslType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SslType)`)` Output only. The ssl config type according to 'clientKey', 'clientCertificate' and 'caCertificate'.  
`clientKey` |  `string` Input only. The unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client Certificate. If this field is used then the 'clientCertificate' field is mandatory.  
`clientCertificate` |  `string` Input only. The x509 PEM-encoded certificate that will be used by the replica to authenticate against the source database server.If this field is used then the 'clientKey' field is mandatory.  
`caCertificate` |  `string` Required. Input only. The x509 PEM-encoded certificate of the CA that signed the source database server's certificate. The replica will use this certificate to verify it's connecting to the right host.  
  
## SslType

Specifies The kind of ssl configuration used.

Enums  
---  
`SSL_TYPE_UNSPECIFIED` | Unspecified.  
`SERVER_ONLY` | Only 'caCertificate' specified.  
`SERVER_CLIENT` | Both server ('caCertificate'), and client ('clientKey', 'clientCertificate') specified.  
  
## CloudSqlConnectionProfile

Specifies required connection parameters, and, optionally, the parameters required to create a Cloud SQL destination database instance.

JSON representation  
---  
      
    
    {
      "cloudSqlId": string,
      "settings": {
        object ([CloudSqlSettings](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#CloudSqlSettings))
      },
      "privateIp": string,
      "publicIp": string
    }  
  
Fields  
---  
`cloudSqlId` |  `string` Output only. The Cloud SQL instance ID that this connection profile is associated with.  
`settings` |  `object (`[CloudSqlSettings](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#CloudSqlSettings)`)` Immutable. Metadata used to create the destination Cloud SQL database.  
`privateIp` |  `string` Output only. The Cloud SQL database instance's private IP.  
`publicIp` |  `string` Output only. The Cloud SQL database instance's public IP.  
  
## CloudSqlSettings

Settings for creating a Cloud SQL database instance.

JSON representation  
---  
      
    
    {
      "databaseVersion": enum ([SqlDatabaseVersion](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlDatabaseVersion)),
      "userLabels": {
        string: string,
        ...
      },
      "tier": string,
      "storageAutoResizeLimit": string,
      "activationPolicy": enum ([SqlActivationPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlActivationPolicy)),
      "ipConfig": {
        object ([SqlIpConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlIpConfig))
      },
      "autoStorageIncrease": boolean,
      "databaseFlags": {
        string: string,
        ...
      },
      "dataDiskType": enum ([SqlDataDiskType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlDataDiskType)),
      "dataDiskSizeGb": string,
      "zone": string,
      "sourceId": string,
      "rootPassword": string,
      "hasRootPassword": boolean
    }  
  
Fields  
---  
`databaseVersion` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlDatabaseVersion)`)` The database engine type and version.  
`userLabels` |  `map (key: string, value: string)` The resource labels for a Cloud SQL instance to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.Example: `{ "name": "wrench", "mass": "18kg", "count": "3" }`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`tier` |  `string` The tier (or machine type) for this instance, for example: `db-n1-standard-1` (MySQL instances). For more information, see [Cloud SQL Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings).  
`storageAutoResizeLimit` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit.  
`activationPolicy` |  `enum (`[SqlActivationPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlActivationPolicy)`)` The activation policy specifies when the instance is activated; it is applicable only when the instance state is 'RUNNABLE'. Valid values:'ALWAYS': The instance is on, and remains so even in the absence of connection requests.`NEVER`: The instance is off; it is not activated, even if a connection request arrives.  
`ipConfig` |  `object (`[SqlIpConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlIpConfig)`)` The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled.  
`autoStorageIncrease` |  `boolean` [default: ON] If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 30 TB.  
`databaseFlags` |  `map (key: string, value: string)` The database flags passed to the Cloud SQL instance at startup. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`dataDiskType` |  `enum (`[SqlDataDiskType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlDataDiskType)`)` The type of storage: `PD_SSD` (default) or `PD_HDD`.  
`dataDiskSizeGb` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The storage capacity available to the database, in GB. The minimum (and default) size is 10GB.  
`zone` |  `string` The Google Cloud Platform zone where your Cloud SQL database instance is located.  
`sourceId` |  `string` The Database Migration Service source connection profile ID, in the format: `projects/my_project_name/locations/us-central1/connectionProfiles/connection_profile_ID`  
`rootPassword` |  `string` Input only. Initial root password.  
`hasRootPassword` |  `boolean` Output only. Indicates If this connection profile root password is stored.  
  
## SqlDatabaseVersion

The database engine type and version.

Enums  
---  
`SQL_DATABASE_VERSION_UNSPECIFIED` | Unspecified version.  
`MYSQL_5_6` | MySQL 5.6.  
`MYSQL_5_7` | MySQL 5.7.  
`MYSQL_8_0` | MySQL 8.0.  
  
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
      "requireSsl": boolean,
      "authorizedNetworks": [
        {
          object ([SqlAclEntry](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlAclEntry))
        }
      ]
    }  
  
Fields  
---  
`enableIpv4` |  `boolean` Whether the instance is assigned a public IP address or not.  
`privateNetwork` |  `string` The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, `/projects/myProject/global/networks/default`. This setting can be updated, but it cannot be removed after it is set.  
`requireSsl` |  `boolean` Whether SSL connections over IP should be enforced or not.  
`authorizedNetworks[]` |  `object (`[SqlAclEntry](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles#SqlAclEntry)`)` The list of external networks that are allowed to connect to the instance using the IP. See <https://en.wikipedia.org/wiki/CIDR_notation#CIDR_notation>, also known as 'slash' notation (e.g. `192.168.100.0/24`).  
  
## SqlAclEntry

An entry for an Access Control list.

JSON representation  
---  
      
    
    {
      "value": string,
      "expireTime": string,
      "label": string
    }  
  
Fields  
---  
`value` |  `string` The allowlisted value for the access control list.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when this access control entry expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example: `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`label` |  `string` A label to identify this entry.  
  
## SqlDataDiskType

The storage options for Cloud SQL databases.

Enums  
---  
`SQL_DATA_DISK_TYPE_UNSPECIFIED` | Unspecified.  
`PD_SSD` | SSD disk.  
`PD_HDD` | HDD disk.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/create)`

|  Creates a new connection profile in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/delete)`

|  Deletes a single Database Migration Service connection profile.  
  
### `[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/get)`

|  Gets details of a single connection profile.  
  
### `[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/list)`

|  Retrieve a list of all connection profiles in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/patch)`

|  Update the configuration of a single connection profile.  
  
### `[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
