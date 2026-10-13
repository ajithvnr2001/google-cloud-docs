---
url: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable_admin_v2.types.CreateTableFromSnapshotRequest
title: Class CreateTableFromSnapshotRequest (2.50.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:25.314122+00:00
---

# Class CreateTableFromSnapshotRequest (2.50.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable_admin_v2.types.CreateTableFromSnapshotRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CreateTableFromSnapshotRequest (2.50.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.50.0 (latest)  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.26.0  2.25.0  2.24.0  2.23.1  2.22.0  2.21.0  2.20.0  2.19.0  2.18.1  2.17.0  2.16.0  2.15.0  2.14.1  2.13.2  2.12.0  2.11.3  2.10.1  2.9.0  2.8.1  2.7.1  2.6.0  2.5.2  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.7.3  1.6.1  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.0  0.34.0 
    
    
    CreateTableFromSnapshotRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Request message for `google.bigtable.admin.v2.BigtableTableAdmin.CreateTableFromSnapshot][google.bigtable.admin.v2.BigtableTableAdmin.CreateTableFromSnapshot]`

Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The unique name of the instance in which to create the table. Values are of the form `projects/{project}/instances/{instance}`.   
`table_id` |  `str`   
Required. The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`.   
`source_snapshot` |  `str`   
Required. The unique name of the snapshot from which to restore the table. The snapshot and the table must be in the same instance. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
