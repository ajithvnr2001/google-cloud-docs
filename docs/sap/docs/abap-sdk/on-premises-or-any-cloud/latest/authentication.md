---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication/
title: Authentication overview for the on-premises or any cloud edition of ABAP SDK for Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:30.942139+00:00
---

# Authentication overview for the on-premises or any cloud edition of ABAP SDK for Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authentication overview for the on-premises or any cloud edition of ABAP SDK for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication)



This document describes the methods that you can use to authenticate to Google Cloud from the on-premises or any cloud edition of ABAP SDK for Google Cloud.

Applications developed using the ABAP SDK for Google Cloud require authentication to connect to Google Cloud APIs. The SDK enables the usage of Google Cloud recommended best practices for [authentication](https://docs.cloud.google.com/docs/authentication).

For authentication and authorization to access Google Cloud APIs, the SDK mainly uses [tokens](https://docs.cloud.google.com/docs/authentication/tokens). The SDK also supports [API keys](https://docs.cloud.google.com/docs/authentication/api-keys) to authenticate to Google Cloud APIs that use API keys.

## Choose an authentication method

Depending on the Google Cloud APIs that you need to access, the environment where your SAP system is hosted, and the security requirements of your SAP system, you can choose an appropriate authentication method.

The following table summarizes the token-based authentication methods, depending on where your SAP system is hosted:

SAP system location | Authentication method | Instructions  
---|---|---  
SAP RISE, regardless of where the servers are hosted | [JSON Web Token (JWT)](https://docs.cloud.google.com/docs/authentication/token-types#sa-jwts) | [Authenticate with JSON Web Tokens (JWT)](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt)  
[Access tokens](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) | [Authenticate with tokens through Workload Identity Federation](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif)  
SAP system hosted on Compute Engine VMs | [Access tokens](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) | [Authenticate with access tokens for Compute Engine VMs](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-access-token)  
[Access tokens](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens) | [Authenticate with access tokens through Workload Identity Federation (VM metadata)](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif#wif_with_vm_metadata)  
SAP system hosted outside Google Cloud | [JSON Web Token (JWT)](https://docs.cloud.google.com/docs/authentication/token-types#sa-jwts) | [Authenticate with JSON Web Tokens (JWT)](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt)  
[Access tokens](https://docs.cloud.google.com/docs/authentication/token-types) | [Authenticate with access tokens through Workload Identity Federation (external IdPs)](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif#wif-with-external-idp)  
  
In addition, the SDK supports the following authentication methods for Google Cloud APIs that require specific authentication:

**Authenticate with API keys to invoke Google Cloud APIs**

Only a few Google Cloud APIs use API keys for authentication, for example, Google Maps Platform. Review the authentication documentation for the service or API that you want to use to determine whether it supports API keys. Regardless of where your SAP system is hosted, you can use API keys for authentication as long as the API that you want to use supports API keys.

To authenticate to Google Cloud API using API keys, use one of the following methods:

  * [Authenticate with API keys stored in SAP SSF](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys#ssf_use_apikey)
  * [Authenticate with API keys stored in Secret Manager](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys#scm_use_apikey)



**Authenticate with OAuth 2.0 client credentials to invoke Google Workspace APIs**

To access [Google Workspace APIs](https://developers.google.com/workspace), you can use OAuth 2.0 client credentials. OAuth 2.0 client credentials let you retrieve a token in the context of an end user, such as a token required to access [Google Sheets](https://developers.google.com/sheets/api/reference/rest). Regardless of where your SAP system is hosted, you can use OAuth 2.0 client credentials for authentication to Google Workspace APIs as long as the system supports OAuth 2.0.

For information about setting up authentication to Google Workspace APIs, see [Authenticate to Google Workspace APIs with OAuth 2.0 client credentials](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-oauth-client-credentials).

**Authenticate with ID tokens for Cloud Run functions**

Authentication to [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) requires an [ID token](https://cloud.google.com/docs/authentication/token-types#id). Depending on the environment where your SAP system is hosted, you set up authentication to the Cloud Run functions API, and then configure a client key to invoke Cloud Run functions.

For information about setting up authentication to invoke Cloud Run functions, see [Authenticate with ID tokens for Cloud Run functions](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-cloud-functions).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
