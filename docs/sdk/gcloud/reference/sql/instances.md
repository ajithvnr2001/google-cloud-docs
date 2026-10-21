---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/
title: gcloud sql instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:19:24.432167+00:00
---

# gcloud sql instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql instances - provide commands for managing Cloud SQL instances 
SYNOPSIS
    

`gcloud sql instances` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Provide commands for managing Cloud SQL instances including creating, configuring, restarting, and deleting instances. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[acquire-ssrs-lease](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/acquire-ssrs-lease)`
     Acquires a SQL Server Reporting Services lease on a Cloud SQL instance. 
`[clone](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/clone)`
     Clones a Cloud SQL instance. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create)`
     Creates a new Cloud SQL instance. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete)`
     Deletes a Cloud SQL instance. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe)`
     Displays configuration and metadata about a Cloud SQL instance. 
`[execute-sql](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/execute-sql)`
     Executes a statement on a Cloud SQL instance. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/export)`
     `(DEPRECATED)` Exports data from a Cloud SQL instance. 
`[failover](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/failover)`
     Causes a high-availability Cloud SQL instance to failover. 
`[get-latest-recovery-time](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/get-latest-recovery-time)`
     Displays the latest recovery time to which a Cloud SQL instance can be restored to. 
`[get-storage-shrink-config](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/get-storage-shrink-config)`
     Displays the minimum storage size to which a Cloud SQL instance can be decreased. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/import)`
     `(DEPRECATED)` Imports data into a Cloud SQL instance from Google Cloud Storage. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/list)`
     Lists Cloud SQL instances in a given project. 
`[patch](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch)`
     Updates the settings of a Cloud SQL instance. 
`[perform-storage-shrink](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/perform-storage-shrink)`
     Performs a storage size decrease of a Cloud SQL instance. 
`[point-in-time-restore](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/point-in-time-restore)`
     Performs a point in time restore for a Cloud SQL instance managed by Google Cloud Backup and Disaster Recovery (DR) Service. 
`[pre-check-major-version-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/pre-check-major-version-upgrade)`
     Performs pre-checks for a major version upgrade of a Cloud SQL instance. 
`[promote-replica](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/promote-replica)`
     Promotes Cloud SQL read replica to a stand-alone instance. 
`[reencrypt](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/reencrypt)`
     Reencrypts a Cloud SQL CMEK instance. 
`[release-ssrs-lease](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/release-ssrs-lease)`
     Releases a SQL Server Reporting Services lease on a Cloud SQL instance. 
`[reset-ssl-config](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/reset-ssl-config)`
     Reset SSL materials according to the reset SSL mode. 
`[restart](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/restart)`
     Restarts a Cloud SQL instance. 
`[restore-backup](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/restore-backup)`
     Restores a backup of a Cloud SQL instance. 
`[switchover](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/switchover)`
     Switches over a Cloud SQL instance to one of its replicas. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances)
    
    
    [gcloud beta sql instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
