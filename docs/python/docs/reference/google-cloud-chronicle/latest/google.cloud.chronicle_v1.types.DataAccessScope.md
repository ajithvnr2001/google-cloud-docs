---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DataAccessScope
title: Class DataAccessScope (0.6.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:53.470992+00:00
---

# Class DataAccessScope (0.6.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DataAccessScope

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataAccessScope (0.6.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.4 (latest)  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DataAccessScope(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A DataAccessScope is a boolean expression of data access labels used to restrict access to data for users.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The unique full name of the data access scope. The name should comply with https://google.aip.dev/122 standards.   
`allowed_data_access_labels` |  `MutableSequence[[google.cloud.chronicle_v1.types.DataAccessLabelReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DataAccessLabelReference)]`   
Optional. The allowed labels for the scope. Either allow_all or allowed_data_access_labels needs to be provided. When provided, there has to be at least one label allowed for the scope to be valid. The logical operator for evaluation of the allowed labels is OR. E.g.: A customer with scope with allowed labels A and B will be able to see data with labeled with A or B or (A and B).   
`denied_data_access_labels` |  `MutableSequence[[google.cloud.chronicle_v1.types.DataAccessLabelReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.DataAccessLabelReference)]`   
Optional. The denied labels for the scope. The logical operator for evaluation of the denied labels is AND. E.g.: A customer with scope with denied labels A and B won't be able to see data labeled with A and data labeled with B and data with labels A and B.   
`display_name` |  `str`   
Output only. The name to be used for display to customers of the data access scope.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the data access scope was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the data access scope was last updated.   
`author` |  `str`   
Output only. The user who created the data access scope.   
`last_editor` |  `str`   
Output only. The user who last updated the data access scope.   
`description` |  `str`   
Optional. A description of the data access scope for a human reader.   
`allow_all` |  `bool`   
Optional. Whether or not the scope allows all labels, allow_all and allowed_data_access_labels are mutually exclusive and one of them must be present. denied_data_access_labels can still be used along with allow_all. When combined with denied_data_access_labels, access will be granted to all data that doesn't have labels mentioned in denied_data_access_labels. E.g.: A customer with scope with denied labels A and B and allow_all will be able to see all data except data labeled with A and data labeled with B and data with labels A and B.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
