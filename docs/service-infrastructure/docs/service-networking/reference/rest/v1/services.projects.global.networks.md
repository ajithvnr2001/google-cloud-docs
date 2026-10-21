---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks
title: REST Resource: services.projects.global.networks \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:38.908657+00:00
---

# REST Resource: services.projects.global.networks  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.projects.global.networks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConsumerConfig
    * JSON representation
  * ReservedRange
    * JSON representation
  * CloudSQLConfig
    * JSON representation
  * Methods



## Resource: ConsumerConfig

Configuration information for a private service access connection.

JSON representation  
---  
      
    
    {
      "producerNetwork": string,
      "consumerImportCustomRoutes": boolean,
      "consumerExportCustomRoutes": boolean,
      "producerImportCustomRoutes": boolean,
      "producerExportCustomRoutes": boolean,
      "consumerImportSubnetRoutesWithPublicIp": boolean,
      "consumerExportSubnetRoutesWithPublicIp": boolean,
      "producerImportSubnetRoutesWithPublicIp": boolean,
      "producerExportSubnetRoutesWithPublicIp": boolean,
      "reservedRanges": [
        {
          object ([ReservedRange](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks#ReservedRange))
        }
      ],
      "vpcScReferenceArchitectureEnabled": boolean,
      "usedIpRanges": [
        string
      ],
      "cloudsqlConfigs": [
        {
          object ([CloudSQLConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks#CloudSQLConfig))
        }
      ],
      "consumerPeeringActive": boolean
    }  
  
Fields  
---  
`producerNetwork` |  `string` Output only. The VPC network that is used to host managed service instances. In the format, projects/{project}/global/networks/{network} where {project} is the project number e.g. '12345' and {network} is the network name.  
`consumerImportCustomRoutes` |  `boolean` Import custom routes flag value for peering from consumer to producer.  
`consumerExportCustomRoutes` |  `boolean` Export custom routes flag value for peering from consumer to producer.  
`producerImportCustomRoutes` |  `boolean` Import custom routes flag value for peering from producer to consumer.  
`producerExportCustomRoutes` |  `boolean` Export custom routes flag value for peering from producer to consumer.  
`consumerImportSubnetRoutesWithPublicIp` |  `boolean` Import subnet routes with public ip flag value for peering from consumer to producer.  
`consumerExportSubnetRoutesWithPublicIp` |  `boolean` Export subnet routes with public ip flag value for peering from consumer to producer.  
`producerImportSubnetRoutesWithPublicIp` |  `boolean` Import subnet routes with public ip flag value for peering from producer to consumer.  
`producerExportSubnetRoutesWithPublicIp` |  `boolean` Export subnet routes with public ip flag value for peering from producer to consumer.  
`reservedRanges[]` |  `object (`[ReservedRange](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks#ReservedRange)`)` Output only. The reserved ranges associated with this private service access connection.  
`vpcScReferenceArchitectureEnabled` |  `boolean` Output only. Indicates whether the VPC Service Controls reference architecture is configured for the producer VPC host network.  
`usedIpRanges[]` |  `string` Output only. The IP ranges already in use by consumer or producer  
`cloudsqlConfigs[]` |  `object (`[CloudSQLConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks#CloudSQLConfig)`)` Represents one or multiple Cloud SQL configurations.  
`consumerPeeringActive` |  `boolean` Output only. If this is true, consumer peering is active.  
  
## ReservedRange

Allocated IP address ranges for this private service access connection.

JSON representation  
---  
      
    
    {
      "name": string,
      "ipPrefixLength": integer,
      "address": string
    }  
  
Fields  
---  
`name` |  `string` The name of the reserved range.  
`ipPrefixLength` |  `integer` The prefix length of the reserved range.  
`address` |  `string` The starting address of the reserved range. The address must be a valid IPv4 address in the x.x.x.x format. This value combined with the IP prefix length is the CIDR range for the reserved range.  
  
## CloudSQLConfig

Cloud SQL configuration.

JSON representation  
---  
      
    
    {
      "service": string,
      "umbrellaProject": string,
      "umbrellaNetwork": string
    }  
  
Fields  
---  
`service` |  `string` Required. Peering service used for peering with the Cloud SQL project.  
`umbrellaProject` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The project number of the Cloud SQL umbrella project.  
`umbrellaNetwork` |  `string` Required. The name of the umbrella network in the Cloud SQL umbrella project.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks/get)`

|  Service producers use this method to get the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP.  
  
### `[getVpcServiceControls](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks/getVpcServiceControls)`

|  Consumers use this method to find out the state of VPC Service Controls.  
  
### `[updateConsumerConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks/updateConsumerConfig)`

|  Service producers use this method to update the configuration of their connection including the import/export of custom routes and subnetwork routes with public IP.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-24 UTC."],[],[]] 
