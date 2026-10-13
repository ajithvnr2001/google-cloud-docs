---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-biglake/latest/google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.SnowflakeCatalogInfo
title: Class SnowflakeCatalogInfo (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:41.245910+00:00
---

# Class SnowflakeCatalogInfo (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-biglake/latest/google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.SnowflakeCatalogInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SnowflakeCatalogInfo (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.0  0.1.1 
    
    
    SnowflakeCatalogInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Snowflake Catalog info.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`account_identifier` |  `str`   
Required. The account identifier in Snowflake (See: https://docs.snowflake.com/en/user-guide/admin-account-identifier). It is the prefix to log into your Snowflake deployment URL. For example: https://  
`warehouse` |  `str`   
Required. The warehouse to connect to in Snowflake REST Catalog. https://  
`snowflake_role` |  `str`   
Optional. The specific Snowflake role name to request in the OAuth token scope (via session:role:$ROLE) for the Iceberg REST Catalog session. This role grants the GCP BigLake service account the necessary permissions to interact with the Iceberg catalog, namespaces, and tables. Note: The role provided here must be the DEFAULT_ROLE or be granted to, the Snowflake service user mapped to the BigLake service account. This field is a member of `oneof`_ `_snowflake_role`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
