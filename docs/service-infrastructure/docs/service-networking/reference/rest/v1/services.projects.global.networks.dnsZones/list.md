---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones/list/
title: Method: services.projects.global.networks.dnsZones.list \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:39.167395+00:00
---

# Method: services.projects.global.networks.dnsZones.list  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.projects.global.networks.dnsZones.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * DnsZonePair
    * JSON representation
  * Try it!



* Service producers can use this method to retrieve a list of available DNS zones in the shared producer host project and the matching peering zones in the consumer project.

### HTTP request

`GET https://servicenetworking.googleapis.com/v1/{parent=services/*/projects/*/global/networks/*}/dnsZones:list`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent resource identifying the connection that owns this collection of DNS zones in the format services/{service}/projects/{project}/global/networks/{network} Service: The service that is managing connectivity for the service producer's organization. For Google services that support this functionality, this value is `servicenetworking.googleapis.com`. Projects: the consumer project containing the consumer network. Network: The consumer network accessible from the tenant project. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `servicenetworking.services.listDnsZones`

  
  
### Request body

The request body must be empty.

### Response body

Represents all DNS zones in the shared producer host project and the matching peering zones in the consumer project.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dnsZonePairs": [
        {
          object ([DnsZonePair](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones/list#DnsZonePair))
        }
      ]
    }  
  
Fields  
---  
`dnsZonePairs[]` |  `object (`[DnsZonePair](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones/list#DnsZonePair)`)` All pairs of private DNS zones in the shared producer host project and the matching peering zones in the consumer project..  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## DnsZonePair

  * Represents a pair of private and peering DNS zone resources. *

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
`producerPrivateZone` |  `object (`[DnsZone](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones#DnsZone)`)` The private DNS zone in the shared producer host project.  
`consumerPeeringZone` |  `object (`[DnsZone](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.projects.global.networks.dnsZones#DnsZone)`)` The DNS peering zone in the consumer project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
