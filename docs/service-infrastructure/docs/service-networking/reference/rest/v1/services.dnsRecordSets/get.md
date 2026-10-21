---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/get/
title: Method: services.dnsRecordSets.get \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:37.820343+00:00
---

# Method: services.dnsRecordSets.get  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.dnsRecordSets/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.dnsRecordSets.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Producers can use this method to retrieve information about the DNS record set added to the private zone inside the shared tenant host project associated with a consumer network.

### HTTP request

`GET https://servicenetworking.googleapis.com/v1/{parent=services/*}/dnsRecordSets:get`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent resource identifying the connection which owns this collection of DNS zones in the format services/{service}. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/roles-permissions/servicenetworking) permission on the specified resource `parent`:

  * `servicenetworking.services.getDnsRecordSet`

  
  
### Query parameters

Parameters  
---  
`consumerNetwork` |  `string` Required. The consumer network containing the record set. Must be in the form of projects/{project}/global/networks/{network}  
`zone` |  `string` Required. The name of the zone containing the record set.  
`domain` |  `string` Required. The domain name of the zone containing the recordset.  
`type` |  `string` Required. RecordSet Type eg. type='A'. See the list of [Supported DNS Types](https://cloud.google.com/dns/records/json-record).  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[DnsRecordSet](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/DnsRecordSet)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
