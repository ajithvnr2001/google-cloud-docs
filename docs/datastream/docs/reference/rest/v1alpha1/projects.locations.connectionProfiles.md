---
url: https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles
title: REST Resource: projects.locations.connectionProfiles \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:23.006404+00:00
---

# REST Resource: projects.locations.connectionProfiles  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)



Send feedback 

#  REST Resource: projects.locations.connectionProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConnectionProfile
    * JSON representation
  * OracleProfile
    * JSON representation
  * GcsProfile
    * JSON representation
  * MysqlProfile
    * JSON representation
  * MysqlSslConfig
    * JSON representation
  * NoConnectivitySettings
  * StaticServiceIpConnectivity
  * ForwardSshTunnelConnectivity
    * JSON representation
  * PrivateConnectivity
    * JSON representation
  * Methods



## Resource: ConnectionProfile

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
      "displayName": string,
    
      // Union field profile can be only one of the following:
      "oracleProfile": {
        object ([OracleProfile](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#OracleProfile))
      },
      "gcsProfile": {
        object ([GcsProfile](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#GcsProfile))
      },
      "mysqlProfile": {
        object ([MysqlProfile](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#MysqlProfile))
      }
      // End of list of possible types for union field profile.
    
      // Union field connectivity can be only one of the following:
      "noConnectivity": {
        object ([NoConnectivitySettings](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#NoConnectivitySettings))
      },
      "staticServiceIpConnectivity": {
        object ([StaticServiceIpConnectivity](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#StaticServiceIpConnectivity))
      },
      "forwardSshConnectivity": {
        object ([ForwardSshTunnelConnectivity](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity))
      },
      "privateConnectivity": {
        object ([PrivateConnectivity](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#PrivateConnectivity))
      }
      // End of list of possible types for union field connectivity.
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource's name.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The create time of the resource.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. The update time of the resource.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` Required. Display name.  
Union field `profile`. Connection configuration for the ConnectionProfile. `profile` can be only one of the following:  
`oracleProfile` |  `object (`[OracleProfile](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#OracleProfile)`)` Oracle ConnectionProfile configuration.  
`gcsProfile` |  `object (`[GcsProfile](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#GcsProfile)`)` Cloud Storage ConnectionProfile configuration.  
`mysqlProfile` |  `object (`[MysqlProfile](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#MysqlProfile)`)` MySQL ConnectionProfile configuration.  
Union field `connectivity`. Connectivity options used to establish a connection to the profile. `connectivity` can be only one of the following:  
`noConnectivity` |  `object (`[NoConnectivitySettings](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#NoConnectivitySettings)`)` No connectivity option chosen.  
`staticServiceIpConnectivity` |  `object (`[StaticServiceIpConnectivity](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#StaticServiceIpConnectivity)`)` Static Service IP connectivity.  
`forwardSshConnectivity` |  `object (`[ForwardSshTunnelConnectivity](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#ForwardSshTunnelConnectivity)`)` Forward SSH tunnel connectivity.  
`privateConnectivity` |  `object (`[PrivateConnectivity](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#PrivateConnectivity)`)` Private connectivity.  
  
## OracleProfile

Oracle database profile.

JSON representation  
---  
      
    
    {
      "hostname": string,
      "port": integer,
      "username": string,
      "password": string,
      "databaseService": string,
      "connectionAttributes": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`hostname` |  `string` Required. Hostname for the Oracle connection.  
`port` |  `integer` Port for the Oracle connection, default value is 1521.  
`username` |  `string` Required. Username for the Oracle connection.  
`password` |  `string` Required. Password for the Oracle connection.  
`databaseService` |  `string` Required. Database for the Oracle connection.  
`connectionAttributes` |  `map (key: string, value: string)` Connection string attributesAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## GcsProfile

Cloud Storage bucket profile.

JSON representation  
---  
      
    
    {
      "bucketName": string,
      "rootPath": string
    }  
  
Fields  
---  
`bucketName` |  `string` Required. The full project and resource path for Cloud Storage bucket including the name.  
`rootPath` |  `string` The root path inside the Cloud Storage bucket.  
  
## MysqlProfile

MySQL database profile.

JSON representation  
---  
      
    
    {
      "hostname": string,
      "port": integer,
      "username": string,
      "password": string,
      "sslConfig": {
        object ([MysqlSslConfig](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#MysqlSslConfig))
      }
    }  
  
Fields  
---  
`hostname` |  `string` Required. Hostname for the MySQL connection.  
`port` |  `integer` Port for the MySQL connection, default value is 3306.  
`username` |  `string` Required. Username for the MySQL connection.  
`password` |  `string` Required. Input only. Password for the MySQL connection.  
`sslConfig` |  `object (`[MysqlSslConfig](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles#MysqlSslConfig)`)` SSL configuration for the MySQL connection.  
  
## MysqlSslConfig

MySQL SSL configuration information.

JSON representation  
---  
      
    
    {
      "clientKey": string,
      "clientKeySet": boolean,
      "clientCertificate": string,
      "clientCertificateSet": boolean,
      "caCertificate": string,
      "caCertificateSet": boolean
    }  
  
Fields  
---  
`clientKey` |  `string` Input only. PEM-encoded private key associated with the Client Certificate. If this field is used then the 'clientCertificate' and the 'caCertificate' fields are mandatory.  
`clientKeySet` |  `boolean` Output only. Indicates whether the clientKey field is set.  
`clientCertificate` |  `string` Input only. PEM-encoded certificate that will be used by the replica to authenticate against the source database server. If this field is used then the 'clientKey' and the 'caCertificate' fields are mandatory.  
`clientCertificateSet` |  `boolean` Output only. Indicates whether the clientCertificate field is set.  
`caCertificate` |  `string` Input only. PEM-encoded certificate of the CA that signed the source database server's certificate.  
`caCertificateSet` |  `boolean` Output only. Indicates whether the caCertificate field is set.  
  
## NoConnectivitySettings

No connectivity settings.

## StaticServiceIpConnectivity

Static IP address connectivity.

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

Private Connectivity

JSON representation  
---  
      
    
    {
      "privateConnectionName": string
    }  
  
Fields  
---  
`privateConnectionName` |  `string`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles/create)   
**(deprecated)**`

|  Use this method to create a connection profile in a project and location.  
  
### `[delete](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles/delete)   
**(deprecated)**`

|  Use this method to delete a connection profile..  
  
### `[discover](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles/discover)   
**(deprecated)**`

|  Use this method to discover a connection profile.  
  
### `[get](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles/get)   
**(deprecated)**`

|  Use this method to get details about a connection profile.  
  
### `[list](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles/list)   
**(deprecated)**`

|  Use this method to list connection profiles created in a project and location.  
  
### `[patch](https://docs.cloud.google.com/datastream/docs/reference/rest/v1alpha1/projects.locations.connectionProfiles/patch)   
**(deprecated)**`

|  Use this method to update the parameters of a connection profile.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
