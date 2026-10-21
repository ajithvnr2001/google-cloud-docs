---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatapolicy/
title: BigQuery Data Policy roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:58:34.100713+00:00
---

# BigQuery Data Policy roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerydatapolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  BigQuery Data Policy roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for BigQuery Data Policy. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## BigQuery Data Policy roles

Role | Permissions  
---|---  
  
#### BigQuery Data Policy Admin 

(`roles/bigquerydatapolicy.admin`) Role for managing Data Policies in BigQuery  This role can only be granted on Resource Manager resources (projects, folders, and organizations). |  `bigquery.dataPolicies.attach` `bigquery.dataPolicies.create` `bigquery.dataPolicies.delete` `bigquery.dataPolicies.get` `bigquery.dataPolicies.getIamPolicy` `bigquery.dataPolicies.list` `bigquery.dataPolicies.setIamPolicy` `bigquery.dataPolicies.update`  
  
#### BigQuery Data Policy Editor 

(`roles/bigquerydatapolicy.editor`) Editor role for BigQuery Data Policy  |  `bigquery.bireservations.*`

  * `bigquery.bireservations.get`
  * `bigquery.bireservations.update`

`bigquery.capacityCommitments.get` `bigquery.capacityCommitments.list` `bigquery.capacityCommitments.update` `bigquery.config.*`

  * `bigquery.config.get`
  * `bigquery.config.update`

`bigquery.connections.create` `bigquery.connections.delete` `bigquery.connections.get` `bigquery.connections.getIamPolicy` `bigquery.connections.list` `bigquery.connections.update` `bigquery.connections.updateTag` `bigquery.connections.use` `bigquery.dataPolicies.attach` `bigquery.dataPolicies.create` `bigquery.dataPolicies.delete` `bigquery.dataPolicies.get` `bigquery.dataPolicies.getIamPolicy` `bigquery.dataPolicies.list` `bigquery.dataPolicies.update` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.datasets.getIamPolicy` `bigquery.datasets.listEffectiveTags` `bigquery.datasets.listTagBindings` `bigquery.datasets.updateTag` `bigquery.jobs.create` `bigquery.jobs.createGlobalQuery` `bigquery.jobs.delete` `bigquery.jobs.get` `bigquery.jobs.list` `bigquery.jobs.listExecutionMetadata` `bigquery.models.*`

  * `bigquery.models.create`
  * `bigquery.models.delete`
  * `bigquery.models.export`
  * `bigquery.models.getData`
  * `bigquery.models.getMetadata`
  * `bigquery.models.list`
  * `bigquery.models.updateData`
  * `bigquery.models.updateMetadata`
  * `bigquery.models.updateTag`

`bigquery.objectRefs.*`

  * `bigquery.objectRefs.read`
  * `bigquery.objectRefs.write`

`bigquery.propertyGraphs.*`

  * `bigquery.propertyGraphs.create`
  * `bigquery.propertyGraphs.delete`
  * `bigquery.propertyGraphs.get`
  * `bigquery.propertyGraphs.list`
  * `bigquery.propertyGraphs.update`

`bigquery.readsessions.*`

  * `bigquery.readsessions.create`
  * `bigquery.readsessions.getData`
  * `bigquery.readsessions.update`

`bigquery.reservationAssignments.*`

  * `bigquery.reservationAssignments.create`
  * `bigquery.reservationAssignments.delete`
  * `bigquery.reservationAssignments.list`
  * `bigquery.reservationAssignments.search`

`bigquery.reservationGroups.*`

  * `bigquery.reservationGroups.create`
  * `bigquery.reservationGroups.delete`
  * `bigquery.reservationGroups.get`
  * `bigquery.reservationGroups.list`
  * `bigquery.reservationGroups.update`

`bigquery.reservations.create` `bigquery.reservations.delete` `bigquery.reservations.get` `bigquery.reservations.getIamPolicy` `bigquery.reservations.list` `bigquery.reservations.listFailoverDatasets` `bigquery.reservations.update` `bigquery.reservations.use` `bigquery.routines.*`

  * `bigquery.routines.create`
  * `bigquery.routines.delete`
  * `bigquery.routines.get`
  * `bigquery.routines.list`
  * `bigquery.routines.update`
  * `bigquery.routines.updateTag`

`bigquery.rowAccessPolicies.create` `bigquery.rowAccessPolicies.delete` `bigquery.rowAccessPolicies.get` `bigquery.rowAccessPolicies.getIamPolicy` `bigquery.rowAccessPolicies.list` `bigquery.rowAccessPolicies.update` `bigquery.savedqueries.*`

  * `bigquery.savedqueries.create`
  * `bigquery.savedqueries.delete`
  * `bigquery.savedqueries.get`
  * `bigquery.savedqueries.list`
  * `bigquery.savedqueries.update`

`bigquery.tables.createIndex` `bigquery.tables.createSnapshot` `bigquery.tables.deleteIndex` `bigquery.tables.getIamPolicy` `bigquery.tables.listEffectiveTags` `bigquery.tables.listTagBindings` `bigquery.tables.replicateData` `bigquery.tables.restoreSnapshot` `bigquery.tables.updateIndex` `bigquery.transfers.*`

  * `bigquery.transfers.get`
  * `bigquery.transfers.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### BigQuery Data Policy Viewer 

(`roles/bigquerydatapolicy.viewer`) Role for viewing Data Policies in BigQuery  This role can only be granted on Resource Manager resources (projects, folders, and organizations). |  `bigquery.dataPolicies.get` `bigquery.dataPolicies.list`  
  
#### Masked Reader 

(`roles/bigquerydatapolicy.maskedReader`) Masked read access to sub-resources tagged by the policy tag associated with a data policy, for example, BigQuery columns  This role can only be granted on Resource Manager resources (projects, folders, and organizations). |  `bigquery.dataPolicies.maskedGet`  
  
#### Raw Data Reader Beta

(`roles/bigquerydatapolicy.rawDataReader`) Raw read access to sub-resources associated with a data policy, for example, BigQuery columns  This role can only be granted on Resource Manager resources (projects, folders, and organizations). |  `bigquery.dataPolicies.getRawData`  
  
## BigQuery Data Policy permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
