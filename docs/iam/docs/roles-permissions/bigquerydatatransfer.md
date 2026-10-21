---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer/
title: BigQuery Data Transfer Service roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:04.368745+00:00
---

# BigQuery Data Transfer Service roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatatransfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  BigQuery Data Transfer Service roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for BigQuery Data Transfer Service. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## BigQuery Data Transfer Service roles

BigQuery Data Transfer Service offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### BigQuery Data Transfer Service Agent 

(`roles/bigquerydatatransfer.serviceAgent`) Gives BigQuery Data Transfer Service access to start BigQuery jobs in consumer project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.config.get` `bigquery.connections.delegate` `bigquery.jobs.create` `cloudaicompanion.topics.create` `compute.networkAttachments.get` `compute.networkAttachments.update` `compute.regionOperations.get` `compute.subnetworks.use` `dataform.folders.create` `dataform.locations.*`

  * `dataform.locations.get`
  * `dataform.locations.list`

`dataform.repositories.create` `dataform.repositories.list` `dataplex.entryGroups.get` `dataplex.entryGroups.useContactsAspect` `dataplex.entryGroups.useDataProfileAspect` `dataplex.entryGroups.useDatabaseDataPolicyAspect` `dataplex.entryGroups.useManagedConnectorTypes` `dataplex.entryGroups.useMySQLConnectorTypes` `dataplex.entryGroups.useOracleConnectorTypes` `dataplex.entryGroups.useOverviewAspect` `dataplex.entryGroups.usePostgreSQLConnectorTypes` `dataplex.entryGroups.useSQLAccessAspect` `dataplex.entryGroups.useSQLServerConnectorTypes` `dataplex.entryGroups.useSQLTriggersAspect` `dataplex.entryGroups.useSchemaAspect` `dataplex.entryGroups.useSecondaryIndexesAspect` `dataplex.entryGroups.useStorageAspect` `dataplex.metadataJobs.create` `dataplex.metadataJobs.get` `dataplex.metadataJobs.list` `geminidataanalytics.locations.chat` `iam.serviceAccounts.getAccessToken` `logging.logEntries.create` `logging.logEntries.route` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.services.use`  
  
## BigQuery Data Transfer Service permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
