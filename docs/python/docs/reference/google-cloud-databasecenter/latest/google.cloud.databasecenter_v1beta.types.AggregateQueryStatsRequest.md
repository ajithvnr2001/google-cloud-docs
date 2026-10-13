---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-databasecenter/latest/google.cloud.databasecenter_v1beta.types.AggregateQueryStatsRequest
title: Class AggregateQueryStatsRequest (0.9.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:33.448692+00:00
---

# Class AggregateQueryStatsRequest (0.9.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-databasecenter/latest/google.cloud.databasecenter_v1beta.types.AggregateQueryStatsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AggregateQueryStatsRequest (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    AggregateQueryStatsRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

AggregateQueryStatsRequest represents the input to the AggregateQueryStats method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. Parent can be a project, a folder, or an organization. The search is limited to the resources within the `parent`. The allowed values are: \- projects/{PROJECT_ID} (e.g., "projects/foo-bar") \- projects/{PROJECT_NUMBER} (e.g., "projects/12345678") \- folders/{FOLDER_NUMBER} (e.g., "folders/1234567") \- organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")   
`order_by` |  `str`   
Optional. The expression to order the results by. Example: `order_by="execution_count"` Example: `order_by="execution_count desc"` Supported order by fields are `execution_count`, `rows_processed`, `total_cpu_time`, `avg_cpu_time`.   
`filter` |  `str`   
Optional. The expression to filter resources. Supported fields are: `full_resource_name`, `resource_type`, `container`, `product.type`, `product.engine`, `product.version`, `location`, `labels`, `issues`, fields of availability_info, data_protection_info,'resource_name', etc. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations. Example: `location="us-east1"` Example: `container="projects/123" OR container="projects/456"` Example: `(container="projects/123" OR container="projects/456") AND location="us-east1"` Additional specific fields for query stats are: `metric_window`, `query_hash`, `normalized_query`. Example: `metric_window="LAST_ONE_DAY"` (Possible values for `metric_window` are: `LAST_ONE_DAY`, `LAST_ONE_WEEK`, `LAST_TWO_WEEKS`) Example: `query_hash="12345678"` Example: `normalized_query="SELECT * FROM table"`  
`page_size` |  `int`   
Optional. If unspecified, at most 100 query stats will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.   
`page_token` |  `str`   
Optional. A page token, received from a previous `AggregateQueryStatsRequest` call. Provide this to retrieve the subsequent page. All parameters except page_token should match the parameters in the call that provided the page token.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
