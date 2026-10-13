---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties
title: Class GoldengateOracleConnectionProperties (0.6.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:37.482744+00:00
---

# Class GoldengateOracleConnectionProperties (0.6.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GoldengateOracleConnectionProperties (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    GoldengateOracleConnectionProperties(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The properties of Goldengate Oracle Database Connection.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`password` |  `str`   
Optional. Input only. The password Oracle Goldengate uses in plain text. This field is a member of `oneof`_ `connection_password_options`.   
`password_secret_version` |  `str`   
Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses. Format: projects/{project}/secrets/{secret}/versions/{version}. This field is a member of `oneof`_ `connection_password_options`.   
`technology_type` |  `str`   
Optional. The technology type.   
`username` |  `str`   
Optional. The username Oracle Goldengate uses to connect.   
`authentication_mode` |  `[google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties.OracleAuthenticationMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties.OracleAuthenticationMode)`   
Optional. Authentication mode.   
`connection_string` |  `str`   
Optional. Connect descriptor or Easy Connect Naming method used to connect to a database.   
`session_mode` |  `[google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties.SessionMode](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.GoldengateOracleConnectionProperties.SessionMode)`   
Optional. The mode of the database connection session to be established by the data client.   
`gcp_oracle_database_id` |  `str`   
Optional. Autonomous AI Database instance id of database in Oracle Database @ Google Cloud. If gcp_oracle_database_id is provided, connection_string must be empty. Format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database}   
`wallet_file` |  `str`   
Optional. The wallet contents Oracle Goldengate uses to make connections to a database. This attribute is expected to be base64 encoded.   
  
## Classes 

### OracleAuthenticationMode
    
    
    OracleAuthenticationMode(value)

Enum for Authentication mode.

### SessionMode
    
    
    SessionMode(value)

The various session modes of the GoldengateConnection.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
