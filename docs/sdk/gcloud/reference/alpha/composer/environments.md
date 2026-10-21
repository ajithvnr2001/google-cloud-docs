---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/
title: gcloud alpha composer environments \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:17:10.707346+00:00
---

# gcloud alpha composer environments  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha composer environments Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha composer environments - create and manage Cloud Composer environments 
SYNOPSIS
    

`gcloud alpha composer environments` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The gcloud alpha composer environments command group lets you create Cloud Composer environments containing an Apache Airflow setup. Additionally, the command group supports environment updates including varying number of machines used to run Airflow, setting Airflow configs, or installing Python dependencies used in Airflow DAGs. The command group can also be used to delete Composer environments. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/snapshots)`
     `(ALPHA)` Save and load snapshots of environment. 
`[storage](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/storage)`
     `(ALPHA)` Manage Cloud Storage objects stored as part of Cloud Composer environments. 
`[user-workloads-config-maps](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/user-workloads-config-maps)`
     `(ALPHA)` Create and manage user workloads ConfigMaps of environment. 
`[user-workloads-secrets](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/user-workloads-secrets)`
     `(ALPHA)` Create and manage user workloads Secrets of environment. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[check-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/check-upgrade)`
     `(ALPHA)` Check that upgrading a Cloud Composer environment does not result in PyPI module conflicts. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/create)`
     `(ALPHA)` Create and initialize a Cloud Composer environment. 
`[database-failover](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/database-failover)`
     `(ALPHA)` Run a database failover operation. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/delete)`
     `(ALPHA)` Delete one or more Cloud Composer environments. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/describe)`
     `(ALPHA)` Get details about a Cloud Composer environment. 
`[fetch-database-properties](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/fetch-database-properties)`
     `(ALPHA)` Fetch database properties. 
`[hibernate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/hibernate)`
     `(ALPHA)` Hibernate a Cloud Composer environment. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/list)`
     `(ALPHA)` List the Cloud Composer environments under a project and location. 
`[list-packages](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/list-packages)`
     `(ALPHA)` List all PyPI modules installed in an Airflow worker. 
`[list-upgrades](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/list-upgrades)`
     `(ALPHA)` List the Cloud Composer image version upgrades for a specific environment. 
`[list-workloads](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/list-workloads)`
     `(ALPHA)` List Composer workloads, supported in Composer 3 environments or greater. 
`[restart-web-server](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/restart-web-server)`
     `(ALPHA)` Restart web server for a Cloud Composer environment. 
`[resume](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/resume)`
     `(ALPHA)` Resume a Cloud Composer environment. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/run)`
     `(ALPHA)` Run an Airflow sub-command remotely in a Cloud Composer environment. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/composer/environments/update)`
     `(ALPHA)` Update properties of a Cloud Composer environment. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud composer environments](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments)
    
    
    [gcloud beta composer environments](https://docs.cloud.google.com/sdk/gcloud/reference/beta/composer/environments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
