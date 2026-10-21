---
url: https://docs.cloud.google.com/database-migration/docs/postgres/use-the-cloud-sdk/
title: Use the gcloud CLI \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:23.360533+00:00
---

# Use the gcloud CLI  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/use-the-cloud-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ API and references ](https://docs.cloud.google.com/database-migration/docs/postgres/use-the-database-migration-service-api)



Send feedback 

#  Use the gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get started with the [ Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) so you can use it to manage Database Migration Service connection profiles and migration jobs for PostgreSQL migrations.

The Google Cloud CLI provides the Google Cloud CLI to interact with Database Migration Service and other Google Cloud services. The gcloud CLI uses the API to access Database Migration Service, so you must enable the API before you can use the tool. 

## Get started with the Google Cloud CLI

To start with the gcloud CLI, review the [ Google Cloud CLI Documentation](https://docs.cloud.google.com/sdk/docs). You can get help for the tool, resources, and commands by using the `--help` flag: 
    
    
    gcloud database-migration --help
    gcloud database-migration connection-profiles create postgresql --help
    gcloud database-migration migration-jobs create --help
    gcloud database-migration migration-jobs promote --help

Finally, configure a project as your default project with two commands. The first command below lists the configuration for the gcloud CLI, including any default project already set. The second command sets the default project. 
    
    
    gcloud config list
    gcloud config set project [PROJECT_ID]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
