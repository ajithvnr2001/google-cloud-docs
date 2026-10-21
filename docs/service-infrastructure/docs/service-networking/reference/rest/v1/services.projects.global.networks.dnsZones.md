---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones
title: REST Resource: services.projects.global.networks.dnsZones \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:38.841926+00:00
---

# REST Resource: services.projects.global.networks.dnsZones  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.projects.global.networks.dnsZones Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GetDnsZoneResponse
    * JSON representation
  * DnsZone
    * JSON representation
  * Methods



## Resource: GetDnsZoneResponse

Represents managed DNS zones created in the shared Producer host and consumer projects.

JSON representation  
---  
      
    
    {
      "producerPrivateZone": {
        object ([DnsZone](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones#DnsZone))
      },
      "consumerPeeringZone": {
        object ([DnsZone](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones#DnsZone))
      }
    }  
  
Fields  
---  
`producerPrivateZone` |  `object (`[DnsZone](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones#DnsZone)`)` The private DNS zone created in the shared producer host project.  
`consumerPeeringZone` |  `object (`[DnsZone](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones#DnsZone)`)` The DNS peering zone created in the consumer project.  
  
## DnsZone

Represents a DNS zone resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "dnsSuffix": string
    }  
  
Fields  
---  
`name` |  `string` User assigned name for this resource. Must be unique within the project. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes.  
`dnsSuffix` |  `string` The DNS name suffix of this zone e.g. `example.com.`. Cloud DNS requires that a DNS suffix ends with a trailing dot.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones/get)`

|  Service producers can use this method to retrieve a DNS zone in the shared producer host project and the matching peering zones in consumer project  
  
### `[list](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones/list)`

|  Service producers can use this method to retrieve a list of available DNS zones in the shared producer host project and the matching peering zones in the consumer project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
