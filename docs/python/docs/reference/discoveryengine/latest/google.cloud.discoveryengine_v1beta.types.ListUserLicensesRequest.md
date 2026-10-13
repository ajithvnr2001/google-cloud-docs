---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListUserLicensesRequest
title: Class ListUserLicensesRequest (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:49.850541+00:00
---

# Class ListUserLicensesRequest (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ListUserLicensesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListUserLicensesRequest (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    ListUserLicensesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for UserLicenseService.ListUserLicenses.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent UserStore resource name, format: `projects/{project}/locations/{location}/userStores/{user_store_id}`.   
`page_size` |  `int`   
Optional. Requested page size. Server may return fewer items than requested. If unspecified, defaults to 10. The maximum value is 50; values above 50 will be coerced to 50. If this field is negative, an INVALID_ARGUMENT error is returned.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ListUserLicenses` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListUserLicenses` must match the call that provided the page token.   
`filter` |  `str`   
Optional. Filter for the list request. Supported fields: \- `license_assignment_state` \- `user_principal` \- Examples: \- `license_assignment_state = ASSIGNED` to list assigned user licenses. \- `license_assignment_state = NO_LICENSE` to list not licensed users. \- `license_assignment_state = NO_LICENSE_ATTEMPTED_LOGIN` to list users who attempted login but no license assigned. \- `license_assignment_state != NO_LICENSE_ATTEMPTED_LOGIN` to filter out users who attempted login but no license assigned. \- `user_principal = user1@example.com` to list user license for `user1@example.com`.   
`order_by` |  `str`   
Optional. The order in which the UserLicenses are listed. The value must be a comma-separated list of fields. Default sorting order is ascending. To specify descending order for a field, append a " desc" suffix. Redundant space characters in the syntax are insignificant. Supported fields (only `user_principal` is supported for now): \- `user_principal` If not set, the default ordering is by `user_principal`. Examples: \- `user_principal` to order by `user_principal` in ascending order. \- `user_principal desc` to order by `user_principal` in descending order.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
