---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/
title: gcloud beta composer environments \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:13:00.513475+00:00
---

# gcloud beta composer environments  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta composer environments Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta composer environments - create and manage Cloud Composer environments 
SYNOPSIS
    

`gcloud beta composer environments` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` The gcloud beta composer environments command group lets you create Cloud Composer environments containing an Apache Airflow setup. Additionally, the command group supports environment updates including varying number of machines used to run Airflow, setting Airflow configs, or installing Python dependencies used in Airflow DAGs. The command group can also be used to delete Composer environments. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/snapshots)`
     `(BETA)` Save and load snapshots of environment. 
`[storage](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/storage)`
     `(BETA)` Manage Cloud Storage objects stored as part of Cloud Composer environments. 
`[user-workloads-config-maps](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/user-workloads-config-maps)`
     `(BETA)` Create and manage user workloads ConfigMaps of environment. 
`[user-workloads-secrets](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/user-workloads-secrets)`
     `(BETA)` Create and manage user workloads Secrets of environment. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[check-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/check-upgrade)`
     `(BETA)` Check that upgrading a Cloud Composer environment does not result in PyPI module conflicts. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/create)`
     `(BETA)` Create and initialize a Cloud Composer environment. 
`[database-failover](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/database-failover)`
     `(BETA)` Run a database failover operation. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/delete)`
     `(BETA)` Delete one or more Cloud Composer environments. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/describe)`
     `(BETA)` Get details about a Cloud Composer environment. 
`[fetch-database-properties](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/fetch-database-properties)`
     `(BETA)` Fetch database properties. 
`[hibernate](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/hibernate)`
     `(BETA)` Hibernate a Cloud Composer environment. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/list)`
     `(BETA)` List the Cloud Composer environments under a project and location. 
`[list-packages](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/list-packages)`
     `(BETA)` List all PyPI modules installed in an Airflow worker. 
`[list-upgrades](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/list-upgrades)`
     `(BETA)` List the Cloud Composer image version upgrades for a specific environment. 
`[list-workloads](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/list-workloads)`
     `(BETA)` List Composer workloads, supported in Composer 3 environments or greater. 
`[restart-web-server](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/restart-web-server)`
     `(BETA)` Restart web server for a Cloud Composer environment. 
`[resume](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/resume)`
     `(BETA)` Resume a Cloud Composer environment. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/run)`
     `(BETA)` Run an Airflow sub-command remotely in a Cloud Composer environment. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments/update)`
     `(BETA)` Update properties of a Cloud Composer environment. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud composer environments](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments)
    
    
    [gcloud alpha composer environments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
