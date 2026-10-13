---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ExecuteSqlPayload
title: Class ExecuteSqlPayload (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:02.292053+00:00
---

# Class ExecuteSqlPayload (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ExecuteSqlPayload

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ExecuteSqlPayload (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 
    
    
    ExecuteSqlPayload(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request payload used to execute SQL statements.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`user` |  `str`   
Optional. The name of an existing database user to connect to the database. When `auto_iam_authn` is set to true, this field is ignored and the API caller's IAM user is used.   
`sql_statement` |  `str`   
Required. SQL statements to run on the database. It can be a single statement or a sequence of statements separated by semicolons.   
`database` |  `str`   
Optional. Name of the database on which the statement will be executed.   
`password_secret_version` |  `str`   
Optional. The resource name of the Secret Manager secret holding the password for the user to log into the database. The secret should be created using the regional endpoint (for API) or from the Regional Secrets page (for UI), and stored in the same region as the Cloud SQL instance. The expected resource name format is `projects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}`. This field is used together with the `user` field. The secret resource name will not be stored. This field is a member of `oneof`_ `user_password`.   
`auto_iam_authn` |  `bool`   
Optional. When set to true, the API caller identity associated with the request is used for database authentication. The API caller must be an IAM user in the database. This field is a member of `oneof`_ `user_password`.   
`row_limit` |  `int`   
Optional. The maximum number of rows returned per SQL statement.   
`partial_result_mode` |  `[google.cloud.sqladmin_v1beta4.types.ExecuteSqlPayload.PartialResultMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.ExecuteSqlPayload.PartialResultMode)`   
Optional. Controls how the API should respond when the SQL execution result is incomplete due to the size limit or another error. The default mode is to throw an error.   
`application` |  `str`   
Optional. Specifies the name of the application that is making the request. This field is used for telemetry. Only alphanumeric characters, dashes, and underscores are allowed. The maximum length is 32 characters.   
  
## Classes 

### PartialResultMode
    
    
    PartialResultMode(value)

Controls how the API should respond when the SQL execution result exceeds 10 MB.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
