---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisRequest
title: Class ListApisRequest (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:48.367875+00:00
---

# Class ListApisRequest (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListApisRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    ListApisRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The ListApis method's request.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent, which owns this collection of API resources. Format: `projects/{project}/locations/{location}`  
`filter` |  `str`   
Optional. An expression that filters the list of ApiResources. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: ``, `>`, `:` or `=`. Filters are not case sensitive. The following fields in the `ApiResource` are eligible for filtering: \- `owner.email` \- The email of the team which owns the ApiResource. Allowed comparison operators: `=`. \- `create_time` \- The time at which the ApiResource was created. The value should be in the (RFC3339)[https://tools.ietf.org/html/rfc3339] format. Allowed comparison operators: `>` and ``. \- `display_name` \- The display name of the ApiResource. Allowed comparison operators: `=`. \- `target_user.enum_values.values.id` \- The allowed value id of the target users attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `target_user.enum_values.values.display_name` \- The allowed value display name of the target users attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `team.enum_values.values.id` \- The allowed value id of the team attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `team.enum_values.values.display_name` \- The allowed value display name of the team attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `business_unit.enum_values.values.id` \- The allowed value id of the business unit attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `business_unit.enum_values.values.display_name` \- The allowed value display name of the business unit attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `maturity_level.enum_values.values.id` \- The allowed value id of the maturity level attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `maturity_level.enum_values.values.display_name` \- The allowed value display name of the maturity level attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `api_style.enum_values.values.id` \- The allowed value id of the api style attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `api_style.enum_values.values.display_name` \- The allowed value display name of the api style attribute associated with the ApiResource. Allowed comparison operator is `:`. \- `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.id` \- The allowed value id of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-id is a placeholder that can be replaced with any user defined enum attribute name. \- `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.enum_values.values.display_name` \- The allowed value display name of the user defined enum attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-enum-display-name is a placeholder that can be replaced with any user defined enum attribute enum name. \- `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.string_values.values` \- The allowed value of the user defined string attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-string is a placeholder that can be replaced with any user defined string attribute name. \- `attributes.projects/test-project-id/locations/test-location-id/ attributes/user-defined-attribute-id.json_values.values` \- The allowed value of the user defined JSON attribute associated with the Resource. Allowed comparison operator is `:`. Here user-defined-attribute-json is a placeholder that can be replaced with any user defined JSON attribute name. A filter function is also supported in the filter string. The filter function is `id(name)`. The `id(name)` function returns the id of the resource name. For example, `id(name) = \"api-1\"` is equivalent to `name = \"projects/test-project-id/locations/test-location-id/apis/api-1\"` provided the parent is `projects/test-project-id/locations/test-location-id`. Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples: \- `owner.email = \"apihub@google.com\"` \- - The owner team email is *apihub@google.com*. \- `owner.email = \"apihub@google.com\" AND create_time < \"2021-08-15t14:50:00z\"="" and="" create_time=""> \"2021-08-10T12:00:00Z\"` \- The owner team email is *apihub@google.com* and the api was created before *2021-08-15 14:50:00 UTC* and after *2021-08-10 12:00:00 UTC*. \- `owner.email = \"apihub@google.com\" OR team.enum_values.values.id: apihub-team-id` \- The filter string specifies the APIs where the owner team email is *apihub@google.com* or the id of the allowed value associated with the team attribute is *apihub-team-id*. \- `owner.email = \"apihub@google.com\" OR team.enum_values.values.display_name: ApiHub Team` \- The filter string specifies the APIs where the owner team email is *apihub@google.com* or the display name of the allowed value associated with the team attribute is `ApiHub Team`. \- `owner.email = \"apihub@google.com\" AND attributes.projects/test-project-id/locations/test-location-id/ attributes/17650f90-4a29-4971-b3c0-d5532da3764b.enum_values.values.id: test_enum_id AND attributes.projects/test-project-id/locations/test-location-id/ attributes/1765\0f90-4a29-5431-b3d0-d5532da3764c.string_values.values: test_string_value` \- The filter string specifies the APIs where the owner team email is *apihub@google.com* and the id of the allowed value associated with the user defined attribute of type enum is *test_enum_id* and the value of the user defined attribute of type string is *test*..   
`page_size` |  `int`   
Optional. The maximum number of API resources to return. The service may return fewer than this value. If unspecified, at most 50 Apis will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.   
`page_token` |  `str`   
Optional. A page token, received from a previous `ListApis` call. Provide this to retrieve the subsequent page. When paginating, all other parameters (except page_size) provided to `ListApis` must match the call that provided the page token.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
