---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest
title: Class FetchDataSourceReferencesForResourceTypeRequest (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:58.914139+00:00
---

# Class FetchDataSourceReferencesForResourceTypeRequest (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FetchDataSourceReferencesForResourceTypeRequest (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    FetchDataSourceReferencesForResourceTypeRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request for the FetchDataSourceReferencesForResourceType method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The parent resource name. Format: projects/{project}/locations/{location}   
`resource_type` |  `str`   
Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance   
`page_size` |  `int`   
Optional. The maximum number of DataSourceReferences to return. The service may return fewer than this value. If unspecified, at most 50 DataSourceReferences will be returned. The maximum value is 100; values above 100 will be coerced to 100.   
`page_token` |  `str`   
Optional. A page token, received from a previous call of `FetchDataSourceReferencesForResourceType`. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `FetchDataSourceReferencesForResourceType` must match the call that provided the page token.   
`filter` |  `str`   
Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields: \- data_source \- data_source_gcp_resource_info.gcp_resourcename \- data_source_backup_config_state \- data_source_backup_count \- data_source_backup_config_info.last_backup_state \- data_source_gcp_resource_info.gcp_resourcename \- data_source_gcp_resource_info.type \- data_source_gcp_resource_info.location \- data_source_gcp_resource_info.cloud_sql_instance_properties.instance_create_time   
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: \- name   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
