---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones
title: REST Resource: organizations.dnsZones \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:40.360892+00:00
---

# REST Resource: organizations.dnsZones  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.dnsZones Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DnsZone
    * JSON representation
  * PeeringConfig
    * JSON representation
  * Methods



## Resource: DnsZone

A DNS zone is a resource under an Apigee organization that is used to create a DNS peering with Apigee's network. DNS peering will let Apigee instances resolve the hostnames created in a peered network.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "domain": string,
      "peeringConfig": {
        object ([PeeringConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones#PeeringConfig))
      },
      "state": enum (State)
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name for the resource. Defined by the server Format: "organizations/{organization}/dnsZones/{dnsZone}".  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that this resource was created on the server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time that this resource was updated on the server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Required. Description of the resource. String of at most 1024 characters associated with this resource for the user's convenience.  
`domain` |  `string` Required. The domain name for hosts in this private zone, for instance "example.com.".  
`peeringConfig` |  `object (`[PeeringConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones#PeeringConfig)`)` DNS PEERING zone configuration.  
`state` |  `enum (`State`)` Output only. State of the DNS Peering. Values other than `ACTIVE` mean the resource is not ready to use.  
  
## PeeringConfig

Fields for DNS PEERING zone.

JSON representation  
---  
      
    
    {
      "targetProjectId": string,
      "targetNetworkId": string
    }  
  
Fields  
---  
`targetProjectId` |  `string` Required. The ID of the project that contains the producer VPC network.  
`targetNetworkId` |  `string` Required. The VPC network where the records for that private DNS zone's namespace are available. Apigee will be performing DNS peering with this VPC network.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/create)`

|  Creates a new DNS zone.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/delete)`

|  Deletes a previously created DNS zone.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/get)`

|  Fetches the representation of an existing DNS zone.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.dnsZones/list)`

|  Enumerates DNS zones that have been created but not yet deleted.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
