---
url: https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1beta1.types.CreateMembershipRequest
title: Class CreateMembershipRequest (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:04.805921+00:00
---

# Class CreateMembershipRequest (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1beta1.types.CreateMembershipRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateMembershipRequest (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.1  1.24.0  1.23.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.3  1.16.0  1.15.1  1.14.2  1.13.1  1.12.1  1.11.0  1.10.2  1.9.0  1.8.1  1.7.1  1.6.0  1.5.3  1.4.3  1.3.0  1.2.0  1.1.0  1.0.0  0.2.2  0.1.2 
    
    
    CreateMembershipRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for the `GkeHubMembershipService.CreateMembership` method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent (project and location) where the Memberships will be created. Specified in the format `projects/*/locations/*`.   
`membership_id` |  `str`   
Required. Client chosen ID for the membership. `membership_id` must be a valid RFC 1123 compliant DNS label: 1\. At most 63 characters in length 2\. It must consist of lower case alphanumeric characters or `-` 3\. It must start and end with an alphanumeric character Which can be expressed as the regex: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`, with a maximum length of 63 characters.   
`resource` |  `[google.cloud.gkehub_v1beta1.types.Membership](https://docs.cloud.google.com/python/docs/reference/gkehub/latest/google.cloud.gkehub_v1beta1.types.Membership)`   
Required. The membership to create.   
`request_id` |  `str`   
Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
