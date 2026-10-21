---
url: https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/
title: gcloud composer environments \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:57:05.241925+00:00
---

# gcloud composer environments  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud composer environments Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud composer environments - create and manage Cloud Composer environments 
SYNOPSIS
    

`gcloud composer environments` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The gcloud composer environments command group lets you create Cloud Composer environments containing an Apache Airflow setup. Additionally, the command group supports environment updates including varying number of machines used to run Airflow, setting Airflow configs, or installing Python dependencies used in Airflow DAGs. The command group can also be used to delete Composer environments. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/snapshots)`
     Save and load snapshots of environment. 
`[storage](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/storage)`
     Manage Cloud Storage objects stored as part of Cloud Composer environments. 
`[user-workloads-config-maps](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-config-maps)`
     Create and manage user workloads ConfigMaps of environment. 
`[user-workloads-secrets](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/user-workloads-secrets)`
     Create and manage user workloads Secrets of environment. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[check-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/check-upgrade)`
     Check that upgrading a Cloud Composer environment does not result in PyPI module conflicts. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/create)`
     Create and initialize a Cloud Composer environment. 
`[database-failover](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/database-failover)`
     Run a database failover operation. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/delete)`
     Delete one or more Cloud Composer environments. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/describe)`
     Get details about a Cloud Composer environment. 
`[fetch-database-properties](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/fetch-database-properties)`
     Fetch database properties. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/list)`
     List the Cloud Composer environments under a project and location. 
`[list-packages](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/list-packages)`
     List all PyPI modules installed in an Airflow worker. 
`[list-upgrades](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/list-upgrades)`
     List the Cloud Composer image version upgrades for a specific environment. 
`[list-workloads](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/list-workloads)`
     List Composer workloads, supported in Composer 3 environments or greater. 
`[restart-web-server](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/restart-web-server)`
     Restart web server for a Cloud Composer environment. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/run)`
     Run an Airflow sub-command remotely in a Cloud Composer environment. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/update)`
     Update properties of a Cloud Composer environment. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha composer environments](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments)
    
    
    [gcloud beta composer environments](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
