---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ImportContext
title: Class ImportContext (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:46.001837+00:00
---

# Class ImportContext (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ImportContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImportContext (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 
    
    
    ImportContext(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Database instance import context.

## Attributes  
  
---  
**Name** | **Description**  
`uri` |  `str`   
Path to the import file in Cloud Storage, in the form `gs://bucketName/fileName`. Compressed gzip files (.gz) are supported when `fileType` is `SQL`. The instance must have write permissions to the bucket and read access to the file.   
`database` |  `str`   
The target database for the import. If `fileType` is `SQL`, this field is required only if the import file does not specify a database, and is overridden by any database specification in the import file. For entire instance parallel import operations, the database is overridden by the database name stored in subdirectory name. If `fileType` is `CSV`, one database must be specified.   
`kind` |  `str`   
This is always `sql#importContext`.   
`file_type` |  `[google.cloud.sqladmin_v1beta4.types.SqlFileType](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.SqlFileType)`   
The file type for the specified uri. \- `SQL`: The file contains SQL statements. \- `CSV`: The file contains CSV data. \- `BAK`: The file contains backup data for a SQL Server instance.   
`csv_import_options` |  `[google.cloud.sqladmin_v1beta4.types.ImportContext.SqlCsvImportOptions](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ImportContext.SqlCsvImportOptions)`   
Options for importing data as CSV.   
`import_user` |  `str`   
The PostgreSQL user for this import operation. PostgreSQL instances only.   
`bak_import_options` |  `[google.cloud.sqladmin_v1beta4.types.ImportContext.SqlBakImportOptions](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ImportContext.SqlBakImportOptions)`   
Import parameters specific to SQL Server .BAK files   
`sql_import_options` |  `[google.cloud.sqladmin_v1beta4.types.ImportContext.SqlImportOptions](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ImportContext.SqlImportOptions)`   
Optional. Options for importing data from SQL statements.   
`tde_import_options` |  `[google.cloud.sqladmin_v1beta4.types.ImportContext.SqlTdeImportOptions](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ImportContext.SqlTdeImportOptions)`   
Optional. Import parameters specific to SQL Server .TDE files Import parameters specific to SQL Server TDE certificates   
  
## Classes 

### SqlBakImportOptions
    
    
    SqlBakImportOptions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

### SqlCsvImportOptions
    
    
    SqlCsvImportOptions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

### SqlImportOptions
    
    
    SqlImportOptions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

### SqlTdeImportOptions
    
    
    SqlTdeImportOptions(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
