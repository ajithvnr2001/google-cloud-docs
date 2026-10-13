---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesRequest
title: Class ListAttributesRequest (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:48.707130+00:00
---

# Class ListAttributesRequest (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListAttributesRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    ListAttributesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The ListAttributes method's request.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent resource for Attribute. Format: `projects/{project}/locations/{location}`  
`filter` |  `str`   
Optional. An expression that filters the list of Attributes. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string or a boolean. The comparison operator must be one of: ``, `>` or `=`. Filters are not case sensitive. The following fields in the `Attribute` are eligible for filtering: \- `display_name` \- The display name of the Attribute. Allowed comparison operators: `=`. \- `definition_type` \- The definition type of the attribute. Allowed comparison operators: `=`. \- `scope` \- The scope of the attribute. Allowed comparison operators: `=`. \- `data_type` \- The type of the data of the attribute. Allowed comparison operators: `=`. \- `mandatory` \- Denotes whether the attribute is mandatory or not. Allowed comparison operators: `=`. \- `create_time` \- The time at which the Attribute was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and ``. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: \- `display_name = production` \- - The display name of the attribute is *production*. \- `(display_name = production) AND (create_time < \"2021-08-15t14:50:00z\")="" and="" (create_time=""> \"2021-08-10T12:00:00Z\")` \- The display name of the attribute is *production* and the attribute was created before *2021-08-15 14:50:00 UTC* and after *2021-08-10 12:00:00 UTC*. \- `display_name = production OR scope = api` \- The attribute where the display name is *production* or the scope is *api*.   
`page_size` |  `int`   
Optional. The maximum number of attribute resources to return. The service may return fewer than this value. If unspecified, at most 50 attributes will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ListAttributes` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListAttributes` must match the call that provided the page token.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
