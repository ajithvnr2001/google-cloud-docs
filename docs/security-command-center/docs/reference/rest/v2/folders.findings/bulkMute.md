---
url: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.findings/bulkMute/
title: Method: folders.findings.bulkMute \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:09.645195+00:00
---

# Method: folders.findings.bulkMute  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/folders.findings/bulkMute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Reference ](https://docs.cloud.google.com/security-command-center/docs/vulnerability-findings-index)



Send feedback 

#  Method: folders.findings.bulkMute Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Kicks off an LRO to bulk mute findings for a parent based on a filter. If no location is specified, findings are muted in global. The parent can be either an organization, folder, or project. The findings matched by the filter will be muted after the LRO is done.

### HTTP request

Choose an endpoint:

globalme-central2useu

  
`POST https://securitycenter.googleapis.com/v2/{parent=folders/*}/findings:bulkMute`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, at which bulk action needs to be applied. If no location is specified, findings are updated in global. The following list shows some examples:

  * `organizations/[organizationId]`
  * `organizations/[organizationId]/locations/[locationId]`
  * `folders/[folder_id]`
  * `folders/[folder_id]/locations/[locationId]`
  * `projects/[projectId]`
  * `projects/[projectId]/locations/[locationId]`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": string,
      "muteState": enum ([MuteState](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/MuteState))
    }  
  
Fields  
---  
`filter` |  `string` Expression that identifies findings that should be updated. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. Parentheses are supported, and `OR` has higher precedence than `AND`.Restrictions have the form `<field> <operator> <value>` and may have a `-` character in front of them to indicate negation. The fields map to those defined in the corresponding resource.The supported operators are:

  * `=` for all value types.
  * `>`, `<`, `>=`, `<=` for integer values.
  * `:`, meaning substring matching, for strings.

The supported value types are:

  * string literals in quotes.
  * integer literals without quotes.
  * boolean literals `true` and `false` without quotes.

  
`muteState` |  `enum (`[MuteState](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/MuteState)`)` Optional. All findings matching the given filter will have their mute state set to this value. The default value is `MUTED`. Setting this to `UNDEFINED` will clear the mute state on all matching findings.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/security-command-center/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/securitycenter`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
