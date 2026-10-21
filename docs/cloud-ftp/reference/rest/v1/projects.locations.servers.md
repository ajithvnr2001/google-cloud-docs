---
url: https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers
title: REST Resource: projects.locations.servers \u00a0|\u00a0 Cloud FTP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:15:32.930145+00:00
---

# REST Resource: projects.locations.servers  |  Cloud FTP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ APIs & Reference ](https://docs.cloud.google.com/cloud-ftp/apis)



Send feedback 

#  REST Resource: projects.locations.servers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Server
    * JSON representation
  * ExternalServerConfig
    * JSON representation
  * InternalServerConfig
    * JSON representation
  * AllowedConsumer
    * JSON representation
  * DeniedConsumer
    * JSON representation
  * PscEndpoint
    * JSON representation
  * AccessType
  * State
  * ServerCredential
    * JSON representation
  * Methods



## Resource: Server

Message describing Server object

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
      "accessType": enum ([AccessType](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#AccessType)),
      "state": enum ([State](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#State)),
      "googleManagedServerCredential": {
        object ([ServerCredential](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#ServerCredential))
      },
      "serviceAgent": string,
    
      // Union field access_config can be only one of the following:
      "externalConfig": {
        object ([ExternalServerConfig](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#ExternalServerConfig))
      },
      "internalConfig": {
        object ([InternalServerConfig](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#InternalServerConfig))
      }
      // End of list of possible types for union field access_config.
    }  
  
Fields  
---  
`name` |  `string` Identifier. name of resource  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` Optional. Display name of the Server  
`accessType` |  `enum (`[AccessType](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#AccessType)`)` Required. The access type of the Server.  
`state` |  `enum (`[State](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#State)`)` Output only. The state of the server.  
`googleManagedServerCredential` |  `object (`[ServerCredential](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#ServerCredential)`)` Output only. Credentials of the FTP Server.  
`serviceAgent` |  `string` Output only. Service agent used to access the customer bucket.  
Union field `access_config`. Configuration for server access. If this is set, it must match the value in the `access_type` field. `access_config` can be only one of the following:  
`externalConfig` |  `object (`[ExternalServerConfig](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#ExternalServerConfig)`)` Configuration for external access.  
`internalConfig` |  `object (`[InternalServerConfig](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#InternalServerConfig)`)` Configuration for internal access.  
  
## ExternalServerConfig

Configuration for external server.

JSON representation  
---  
      
    
    {
      "ipAddress": string,
      "allowedCidrBlocks": [
        string
      ]
    }  
  
Fields  
---  
`ipAddress` |  `string` Output only. IP address of the LB via which clients will connect.  
`allowedCidrBlocks[]` |  `string` Optional. List of CIDR blocks that are allowed to access the Server. A CIDR range consists of an IP Address and a prefix length to construct the subnet mask. By default, the prefix length is 32 (i.e. matches a single IP address). For now, only IPV4 addresses are supported. Examples: "203.0.113.0/24" - matches with the IP addresses in the range 203.0.113.0 - 203.0.113.255. "0.0.0.0/0" - matches against any IP address. This field must contain at least one entry if the access type is EXTERNAL. The number of allowed CIDR blocks cannot exceed 500. Example: 192.168.0.0/16  
  
## InternalServerConfig

Configuration for private server accessible via PSC.

JSON representation  
---  
      
    
    {
      "serviceAttachment": string,
      "consumerAcceptList": [
        {
          object ([AllowedConsumer](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#AllowedConsumer))
        }
      ],
      "consumerRejectList": [
        {
          object ([DeniedConsumer](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#DeniedConsumer))
        }
      ],
      "pscEndpoints": [
        {
          object ([PscEndpoint](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#PscEndpoint))
        }
      ]
    }  
  
Fields  
---  
`serviceAttachment` |  `string` Output only. The resource name of the service attachment. Format: `projects/{project}/regions/{region}/serviceAttachments/{serviceAttachment}`  
`consumerAcceptList[]` |  `object (`[AllowedConsumer](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#AllowedConsumer)`)` Required. A list of projects that are permitted to connect. At least one project is required in the allow list.  
`consumerRejectList[]` |  `object (`[DeniedConsumer](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#DeniedConsumer)`)` Optional. A list of projects that are denied connection. Format: "projects/sample_project_id" or "projects/1234567890" Projects in this list will be denied access, even if they are included in the `allow_list`. If this list is empty, no projects are explicitly rejected.  
`pscEndpoints[]` |  `object (`[PscEndpoint](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers#PscEndpoint)`)` Output only. Details of endpoints created by the customer.  
  
## AllowedConsumer

A consumer project or network that is permitted to connect to the server via PSC.

JSON representation  
---  
      
    
    {
      "connectionLimit": string,
    
      // Union field consumer_type can be only one of the following:
      "project": string
      // End of list of possible types for union field consumer_type.
    }  
  
Fields  
---  
`connectionLimit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The connection limit for the consumer. Value must be greater than 0.  
Union field `consumer_type`. Required. Specifies the type of consumer. `consumer_type` can be only one of the following:  
`project` |  `string` The project ID or number of the consumer project. Must be in the format: `projects/{project}`.  
  
## DeniedConsumer

A consumer project or network that is denied to connect to the server via PSC.

JSON representation  
---  
      
    
    {
    
      // Union field consumer_type can be only one of the following:
      "project": string
      // End of list of possible types for union field consumer_type.
    }  
  
Fields  
---  
Union field `consumer_type`. Required. Specifies the type of consumer. `consumer_type` can be only one of the following:  
`project` |  `string` The project ID or number of the consumer project. Must be in the format: `projects/{project}`.  
  
## PscEndpoint

Details of PSC endpoint created by customer.

JSON representation  
---  
      
    
    {
      "endpoint": string,
      "network": string,
      "status": string
    }  
  
Fields  
---  
`endpoint` |  `string` Output only. This is a Resource name for Private Service Connect endpoint. Format: `projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}`  
`network` |  `string` Output only. The consumer network. Format: `projects/{project}/locations/{location}/networks/{network}`  
`status` |  `string` Output only. The status of the connected endpoint.  
  
## AccessType

The access type of the Server.

Enums  
---  
`ACCESS_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`EXTERNAL` | Server is assigned a public IP.  
`INTERNAL` | Server is assigned an internal IP.  
  
## State

Tracks Server status.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`CREATING` | Server is being created.  
`STARTING` | Server is starting.  
`ACTIVE` | Server is ready to be used.  
`STOPPING` | Server is stopping.  
`STOPPED` | Server is stopped.  
`DELETING` | Server is being deleted.  
`ERROR` | Server is in error state.  
`UPDATING` | Server is being updated.  
  
## ServerCredential

Represents credentials of an FTP Server.

JSON representation  
---  
      
    
    {
      "fingerprint": string,
      "asymmetricAlgorithm": string
    }  
  
Fields  
---  
`fingerprint` |  `string` Output only. The fingerprint is a hash of the public key, and is displayed when clients access the server for the first time to verify the server's identity.  
`asymmetricAlgorithm` |  `string` Output only. Asymmetric algorithm used by the public key. Possible values (can be expanded in future): - ssh-ed25519  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/create)`

|  Creates a new Server in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/delete)`

|  Deletes a single Server.  
  
### `[get](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/get)`

|  Gets details of a single Server.  
  
### `[list](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/list)`

|  Lists Servers in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/patch)`

|  Updates the parameters of a single Server.  
  
### `[start](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/start)`

|  Starts a stopping/stopped Server.  
  
### `[stop](https://docs.cloud.google.com/cloud-ftp/reference/rest/v1/projects.locations.servers/stop)`

|  Stops an active Server.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
