---
url: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListProjectDataProfilesRequest
title: Class ListProjectDataProfilesRequest (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:30.577990+00:00
---

# Class ListProjectDataProfilesRequest (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListProjectDataProfilesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListProjectDataProfilesRequest (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.1  3.24.0  3.23.0  3.22.0  3.20.0  3.19.0  3.18.1  3.17.0  3.16.0  3.15.3  3.14.0  3.13.0  3.12.3  3.11.1  3.10.1  3.9.2  3.8.1  3.7.1  3.6.2  3.5.0  3.4.0  3.3.1  3.2.4  3.1.1  3.0.1  2.0.2  1.0.2  0.15.2  0.14.0  0.13.0  0.12.1 
    
    
    ListProjectDataProfilesRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request to list the profiles generated for a given organization or project.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. organizations/{org_id}/locations/{loc_id}   
`page_token` |  `str`   
Page token to continue retrieval.   
`page_size` |  `int`   
Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.   
`order_by` |  `str`   
Comma-separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: \- `project_id` \- `sensitivity_level desc` Supported fields: \- `project_id`: Google Cloud project ID \- `sensitivity_level`: How sensitive the data in a project is, at most \- `data_risk_level`: How much risk is associated with this data \- `profile_last_generated`: Date and time (in epoch seconds) the profile was last generated   
`filter` |  `str`   
Allows filtering. Supported syntax: \- Filter expressions are made up of one or more restrictions. \- Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`. \- A restriction has the form of `{field} {operator} {value}`. \- Supported fields: \- `project_id`: the Google Cloud project ID \- `sensitivity_level`: HIGH|MODERATE|LOW \- `data_risk_level`: HIGH|MODERATE|LOW \- `status_code`: an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto \- `profile_last_generated`: Date and time the profile was last generated \- The operator must be `=` or `!=`. The `profile_last_generated` filter also supports `` and `>`. The syntax is based on https://google.aip.dev/160. Examples: \- `project_id = 12345 AND status_code = 1` \- `project_id = 12345 AND sensitivity_level = HIGH` \- `profile_last_generated <>` The length of this field should be no more than 500 characters.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
