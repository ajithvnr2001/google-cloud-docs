---
url: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Connection
title: Class Connection (3.46.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:17.645593+00:00
---

# Class Connection (3.46.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Connection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Connection (3.46.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.46.1 (latest)  3.46.0  3.45.2  3.44.0  3.43.0  3.42.3  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.31.0  3.30.0  3.29.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.1  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.2  3.16.0  3.15.0  3.14.1  3.13.0  3.12.0  3.11.4  3.4.0  3.3.6  3.2.0  3.1.0  3.0.1  2.34.4  2.33.0  2.32.0  2.31.0  2.30.1  2.29.0  2.28.1  2.27.1  2.26.0  2.25.2  2.24.1  2.23.3  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.0  1.28.2  1.27.2  1.26.1  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0 
    
    
    Connection(client=None, bqstorage_client=None, prefer_bqstorage_client=True)

DB-API Connection to Google BigQuery.

## Parameters  
  
---  
**Name** | **Description**  
`client` |  `Optional[google.cloud.bigquery.Client]`   
A REST API client used to connect to BigQuery. If not passed, a client is created using default options inferred from the environment.  
`bqstorage_client` |  `Optional[google.cloud.bigquery_storage_v1.BigQueryReadClient]`   
A client that uses the faster BigQuery Storage API to fetch rows from BigQuery. If not passed, it is created using the same credentials as `client` (provided that BigQuery Storage dependencies are installed).  
`prefer_bqstorage_client` |  `Optional[bool]`   
Prefer the BigQuery Storage client over the REST client. If Storage client isn't available, fall back to the REST client. Defaults to `True`.  
  
## Methods 

### close
    
    
    close()

Close the connection and any cursors created from it.

Any BigQuery clients explicitly passed to the constructor are _not_ closed, only those created by the connection instance itself.

### commit
    
    
    commit()

No-op, but for consistency raise an error if connection is closed.

### cursor
    
    
    cursor()

Return a new cursor object.

**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery.dbapi.Cursor](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dbapi.Cursor)` | A DB-API cursor that uses this connection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
