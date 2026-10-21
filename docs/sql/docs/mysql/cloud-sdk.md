---
url: https://docs.cloud.google.com/sql/docs/mysql/cloud-sdk/
title: About the gcloud CLI \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:26.589347+00:00
---

# About the gcloud CLI  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/cloud-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  About the gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/cloud-sdk "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/cloud-sdk "View this page for the SQL Server database engine")

This page describes how to get started with the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) so you can use it to manage Cloud SQL instances. The gcloud CLI uses the Cloud SQL Admin API to access Cloud SQL, so you must enable the API before you can use the gcloud CLI to access Cloud SQL. 

For `gcloud` examples, see the [How-to page](https://docs.cloud.google.com/sql/docs/mysql/how-to) for the task.

## Getting started with the gcloud CLI

To start with the gcloud CLI, review the [](https://docs.cloud.google.com/sdk/docs)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) Documentation. You can get help for the tool, resources, and commands by using the `--help` flag: 
    
    
    gcloud sql --help
    gcloud sql instances --help
    gcloud sql instances create --help

The help displayed with the `--help` flag is also available in the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) reference for [gcloud sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql). 

Finally, configure a project as your default project with two commands. The first command below lists the configuration for the gcloud CLI, including any default project already set. The second command sets the default project. 
    
    
    gcloud config list
    gcloud config set project [PROJECT_ID]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
