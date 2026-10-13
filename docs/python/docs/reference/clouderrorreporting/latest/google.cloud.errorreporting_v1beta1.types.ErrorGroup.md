---
url: https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.errorreporting_v1beta1.types.ErrorGroup
title: Class ErrorGroup (1.17.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:30.215689+00:00
---

# Class ErrorGroup (1.17.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.errorreporting_v1beta1.types.ErrorGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ErrorGroup (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.1  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.2  1.8.2  1.7.0  1.6.3  1.5.3  1.4.1  1.3.0  1.2.3  1.1.2  1.0.0  0.34.0  0.33.0  0.32.1 
    
    
    ErrorGroup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Description of a group of similar error events.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The group resource name. Written as `projects/{projectID}/groups/{group_id}` or `projects/{projectID}/locations/{location}/groups/{group_id}` Examples: `projects/my-project-123/groups/my-group`, `projects/my-project-123/locations/us-central1/groups/my-group` In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see `Google Cloud Privacy Notice   
`group_id` |  `str`   
An opaque identifier of the group. This field is assigned by the Error Reporting system and always populated. In the group resource name, the `group_id` is a unique identifier for a particular error group. The identifier is derived from key parts of the error-log content and is treated as Service Data. For information about how Service Data is handled, see `Google Cloud Privacy Notice   
`tracking_issues` |  `MutableSequence[[google.cloud.errorreporting_v1beta1.types.TrackingIssue](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.errorreporting_v1beta1.types.TrackingIssue)]`   
Associated tracking issues.   
`resolution_status` |  `[google.cloud.errorreporting_v1beta1.types.ResolutionStatus](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.errorreporting_v1beta1.types.ResolutionStatus)`   
Error group's resolution status. An unspecified resolution status will be interpreted as OPEN   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
