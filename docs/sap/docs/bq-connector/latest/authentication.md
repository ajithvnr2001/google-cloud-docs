---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication/
title: Authentication overview for the BigQuery Connector for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:23.773330+00:00
---

# Authentication overview for the BigQuery Connector for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authentication overview for the BigQuery Connector for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the methods that you can use to authenticate to Google Cloud from BigQuery Connector for SAP.

## Choose an authentication method

Depending on the environment where your SAP system is hosted, you can choose an appropriate authentication method.

The following table summarizes the authentication methods, depending on where your SAP system is hosted:

SAP system location | Authentication method | Instructions  
---|---|---  
SAP RISE, regardless of where the servers are hosted | [JSON Web Token (JWT)](https://docs.cloud.google.com/docs/authentication/token-types#sa-jwts) | [Authenticate with JSON Web Tokens (JWT)](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt)  
SAP system hosted on Compute Engine VM | [Access tokens](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) | [Authenticate with access tokens](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token)  
SAP system hosted outside Google Cloud | [JSON Web Token (JWT)](https://docs.cloud.google.com/docs/authentication/token-types#sa-jwts) | [Authenticate with JSON Web Tokens (JWT)](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
