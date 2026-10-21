---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/add/
title: Method: services.dnsRecordSets.add \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:37.900375+00:00
---

# Method: services.dnsRecordSets.add  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.dnsRecordSets.add Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Service producers can use this method to add DNS record sets to private DNS zones in the shared producer host project.

### HTTP request

`POST https://servicenetworking.googleapis.com/v1/{parent=services/*}/dnsRecordSets:add`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The service that is managing peering connectivity for a service producer's organization. For Google services that support this functionality, this value is `services/servicenetworking.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `servicenetworking.services.addDnsRecordSet`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "consumerNetwork": string,
      "zone": string,
      "dnsRecordSet": {
        object ([DnsRecordSet](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/DnsRecordSet))
      }
    }  
  
Fields  
---  
`consumerNetwork` |  `string` Required. The network that the consumer is using to connect with services. Must be in the form of projects/{project}/global/networks/{network} {project} is the project number, as in '12345' {network} is the network name.  
`zone` |  `string` Required. The name of the private DNS zone in the shared producer host project to which the record set will be added.  
`dnsRecordSet` |  `object (`[DnsRecordSet](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/DnsRecordSet)`)` Required. The DNS record set to add.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
