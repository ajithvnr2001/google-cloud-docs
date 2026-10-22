---
url: https://docs.cloud.google.com/alloydb/docs/auth-proxy/troubleshoot/
title: Troubleshoot AlloyDB Auth Proxy connections \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:15.800738+00:00
---

# Troubleshoot AlloyDB Auth Proxy connections  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/auth-proxy/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot AlloyDB Auth Proxy connections Stay organized with collections  Save and categorize content based on your preferences. 

To resolve connection, authentication, or network errors when connecting to your AlloyDB for PostgreSQL instance with the AlloyDB Auth Proxy, check the following common issues and solutions:

  * Check the AlloyDB Auth Proxy output carefully and look for errors. Often, the error messages provide the information you need to determine the source of the problem and how to solve it.

  * If you are getting a `403 Forbidden` error, and you are using a service account to authenticate the AlloyDB Auth Proxy, make sure the service account has the correct permissions.

The predefined AlloyDB Identity and Access Management (IAM) roles that provide these permissions are AlloyDB Client (`roles/alloydb.client`) and AlloyDB Admin (`roles/alloydb.admin`). In addition, you must add the Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`) role.

  * Make sure to enable the AlloyDB API.

If it is not enabled, you see output like `Error 403: Access Not Configured` in your AlloyDB Auth Proxy logs.

  * If you are connecting using UNIX sockets, confirm that the sockets were created by listing the directory you provided when you started the AlloyDB Auth Proxy.

  * If you have an outbound firewall policy, make sure it allows connections to port `5433` on the target AlloyDB instance.

**Note:** The Auth Proxy client uses port `5433` to connect to the Auth Proxy server. Port `5432` is the default port for the PostgreSQL protocol over a direct TCP connection.
  * Quota issues: If you see errors related to quotas being exceeded, either identify the source of the quota problem (for example, an application is misusing the connector and unnecessarily creating new connections) or contact support to request an increase to the AlloyDB API quota.

  * If you get a `400 Bad Request` response with an error message containing `reauth related error`, refresh your Application Default Credentials by using the Google Cloud CLI:
        
        gcloud auth application-default login

For more information, see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
