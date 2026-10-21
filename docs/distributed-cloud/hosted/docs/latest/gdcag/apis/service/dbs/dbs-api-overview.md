---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/dbs/dbs-api-overview/
title: Overview of Database Service API \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:22.771950+00:00
---

# Overview of Database Service API  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/dbs/dbs-api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Overview of Database Service API Stay organized with collections  Save and categorize content based on your preferences. 

Database Service API uses Kubernetes custom resources and relies on the Kubernetes Resource Model (KRM). It is used to create and manage database clusters in Google Distributed Cloud (GDC) air-gapped.

Use the `kubectl` CLI for the Database Service APIs.

## Service endpoint

The following URLs are the API endpoints for the Database Service KRM APIs:

  * https://MANAGEMENT_API_SERVER_ENDPOINT/apis/fleet.dbadmin.gdc.goog/v1
  * https://MANAGEMENT_API_SERVER_ENDPOINT/apis/oracle.dbadmin.gdc.goog/v1
  * https://MANAGEMENT_API_SERVER_ENDPOINT/apis/postgresql.dbadmin.gdc.goog/v1



Replace `MANAGEMENT_API_SERVER_ENDPOINT` with the endpoint of the Management API server.

## Discovery document

Use the `kubectl proxy --port=8001` command to open a proxy to the API server on your local machine. From there, you can access the discovery document at one of the following URLs:

  * http://127.0.0.1:8001/apis/fleet.dbadmin.gdc.goog/v1
  * http://127.0.0.1:8001/apis/oracle.dbadmin.gdc.goog/v1
  * http://127.0.0.1:8001/apis/postgresql.dbadmin.gdc.goog/v1



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
