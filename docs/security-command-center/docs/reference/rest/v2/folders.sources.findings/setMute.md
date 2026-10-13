---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.sources.findings/setMute/
title: Method: folders.sources.findings.setMute \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:18.128278+00:00
---

# Method: folders.sources.findings.setMute  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.sources.findings/setMute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: folders.sources.findings.setMute Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Updates the mute state of a finding. If no location is specified, finding is assumed to be in global

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`POST https://securitycenter.googleapis.com/v2/{name=folders/*/sources/*/findings/*}:setMute`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The [relative resource name](https://cloud.google.com/apis/design/resource_names#relative_resource_name) of the finding. If no location is specified, finding is assumed to be in global. The following list shows some examples:\+ `organizations/{organizationId}/sources/{source_id}/findings/{findingId}` \+ `organizations/{organizationId}/sources/{source_id}/locations/{locationId}/findings/{findingId}` \+ `folders/{folder_id}/sources/{source_id}/findings/{findingId}` \+ `folders/{folder_id}/sources/{source_id}/locations/{locationId}/findings/{findingId}` \+ `projects/{projectId}/sources/{source_id}/findings/{findingId}` \+ `projects/{projectId}/sources/{source_id}/locations/{locationId}/findings/{findingId}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mute": enum ([Mute](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.sources.locations.findings#Finding.Mute))
    }  
  
Fields  
---  
`mute` |  `enum (`[Mute](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.sources.locations.findings#Finding.Mute)`)` Required. The desired state of the Mute.  
  
### Response body

If successful, the response body contains an instance of `[Finding](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.sources.locations.findings#Finding)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
