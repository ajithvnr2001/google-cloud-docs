---
url: https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/importAdminOverrides/
title: Method: services.consumerQuotaMetrics.importAdminOverrides \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:01.890698+00:00
---

# Method: services.consumerQuotaMetrics.importAdminOverrides  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/services.consumerQuotaMetrics/importAdminOverrides/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage)
  * [ Reference ](https://docs.cloud.google.com/service-usage/docs/apis)



Send feedback 

#  Method: services.consumerQuotaMetrics.importAdminOverrides Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



Creates or updates multiple admin overrides atomically, all on the same consumer, but on many different metrics or limits. The name field in the quota override message should not be set.

### HTTP request

`POST https://serviceusage.googleapis.com/v1beta1/{parent=*/*/services/*}/consumerQuotaMetrics:importAdminOverrides`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The resource name of the consumer.An example name would be: `projects/123/services/compute.googleapis.com` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `serviceusage.quotas.update`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "force": boolean,
      "forceOnly": [
        enum ([QuotaSafetyCheck](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/QuotaSafetyCheck))
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inlineSource": {
        object ([OverrideInlineSource](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/OverrideInlineSource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`force` |  `boolean` Whether to force the creation of the quota overrides. Setting the force parameter to 'true' ignores all quota safety checks that would fail the request. QuotaSafetyCheck lists all such validations. If force is set to true, it is recommended to include a case id in "X-Goog-Request-Reason" header when sending the request.  
`forceOnly[]` |  `enum (`[QuotaSafetyCheck](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/QuotaSafetyCheck)`)` The list of quota safety checks to ignore before the override mutation. Unlike 'force' field that ignores all the quota safety checks, the 'forceOnly' field ignores only the specified checks; other checks are still enforced. The 'force' and 'forceOnly' fields cannot both be set. If forceOnly is specified, it is recommended to include a case id in "X-Goog-Request-Reason" header when sending the request.  
Source of import data The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inlineSource` |  `object (`[OverrideInlineSource](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1beta1/OverrideInlineSource)`)` The import data is specified in the request message itself  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
