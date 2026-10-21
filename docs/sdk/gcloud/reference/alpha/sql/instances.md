---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/
title: gcloud alpha sql instances \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:04.065902+00:00
---

# gcloud alpha sql instances  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql instances Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql instances - provide commands for managing Cloud SQL instances 
SYNOPSIS
    

`gcloud alpha sql instances` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Provide commands for managing Cloud SQL instances including creating, configuring, restarting, and deleting instances. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/config)`
     `(ALPHA)` Manage Sqladmin instance configurations. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[clone](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/clone)`
     `(ALPHA)` Clones a Cloud SQL instance. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/create)`
     `(ALPHA)` Creates a new Cloud SQL instance. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/delete)`
     `(ALPHA)` Deletes a Cloud SQL instance. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/describe)`
     `(ALPHA)` Displays configuration and metadata about a Cloud SQL instance. 
`[execute-sql](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/execute-sql)`
     `(ALPHA)` Executes a statement on a Cloud SQL instance. 
`[export](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/export)`
     `(ALPHA)` `(DEPRECATED)` Exports data from a Cloud SQL instance. 
`[failover](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/failover)`
     `(ALPHA)` Causes a high-availability Cloud SQL instance to failover. 
`[get-latest-recovery-time](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/get-latest-recovery-time)`
     `(ALPHA)` Displays the latest recovery time to which a Cloud SQL instance can be restored to. 
`[get-storage-shrink-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/get-storage-shrink-config)`
     `(ALPHA)` Displays the minimum storage size to which a Cloud SQL instance can be decreased. 
`[import](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/import)`
     `(ALPHA)` `(DEPRECATED)` Imports data into a Cloud SQL instance from Google Cloud Storage. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/list)`
     `(ALPHA)` Lists Cloud SQL instances in a given project. 
`[patch](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/patch)`
     `(ALPHA)` Updates the settings of a Cloud SQL instance. 
`[perform-storage-shrink](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/perform-storage-shrink)`
     `(ALPHA)` Performs a storage size decrease of a Cloud SQL instance. 
`[point-in-time-restore](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/point-in-time-restore)`
     `(ALPHA)` Performs a point in time restore for a Cloud SQL instance managed by Google Cloud Backup and Disaster Recovery (DR) Service. 
`[promote-replica](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/promote-replica)`
     `(ALPHA)` Promotes Cloud SQL read replica to a stand-alone instance. 
`[reencrypt](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/reencrypt)`
     `(ALPHA)` Reencrypts a Cloud SQL CMEK instance. 
`[reset-ssl-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/reset-ssl-config)`
     `(ALPHA)` Reset SSL materials according to the reset SSL mode. 
`[restart](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/restart)`
     `(ALPHA)` Restarts a Cloud SQL instance. 
`[restore-backup](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/restore-backup)`
     `(ALPHA)` Restores a backup of a Cloud SQL instance. 
`[switchover](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/switchover)`
     `(ALPHA)` Switches over a Cloud SQL instance to one of its replicas. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql instances](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances)
    
    
    [gcloud beta sql instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
