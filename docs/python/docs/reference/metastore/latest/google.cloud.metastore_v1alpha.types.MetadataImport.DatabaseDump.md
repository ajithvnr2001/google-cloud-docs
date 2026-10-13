---
url: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.MetadataImport.DatabaseDump
title: Class DatabaseDump (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:45.104754+00:00
---

# Class DatabaseDump (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.MetadataImport.DatabaseDump

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DatabaseDump (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.3  1.17.0  1.16.1  1.15.5  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.3  1.5.1  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.3.3  0.2.2  0.1.0 
    
    
    DatabaseDump(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A specification of the location of and metadata about a database dump from a relational database management system.

## Attributes  
  
---  
**Name** | **Description**  
`database_type` |  `[google.cloud.metastore_v1alpha.types.MetadataImport.DatabaseDump.DatabaseType](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.MetadataImport.DatabaseDump.DatabaseType)`   
The type of the database.   
`gcs_uri` |  `str`   
A Cloud Storage object or folder URI that specifies the source from which to import metadata. It must begin with `gs://`.   
`source_database` |  `str`   
The name of the source database.   
`type_` |  `[google.cloud.metastore_v1alpha.types.DatabaseDumpSpec.Type](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1alpha.types.DatabaseDumpSpec.Type)`   
Optional. The type of the database dump. If unspecified, defaults to `MYSQL`.   
  
## Classes 

### DatabaseType
    
    
    DatabaseType(value)

The type of the database.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
