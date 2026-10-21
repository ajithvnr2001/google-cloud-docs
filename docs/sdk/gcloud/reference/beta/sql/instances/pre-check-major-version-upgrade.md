---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/pre-check-major-version-upgrade/
title: gcloud beta sql instances pre-check-major-version-upgrade \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:24.330954+00:00
---

# gcloud beta sql instances pre-check-major-version-upgrade  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/pre-check-major-version-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta sql instances pre-check-major-version-upgrade Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta sql instances pre-check-major-version-upgrade - performs pre-checks for a major version upgrade of a Cloud SQL instance 
SYNOPSIS
    

`gcloud beta sql instances pre-check-major-version-upgrade` `INSTANCE` `--target-database-version`=`TARGET_DATABASE_VERSION` [`--async`] [`--max-runtime`=`MAX_RUNTIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta sql instances pre-check-major-version-upgrade` performs pre-checks for a major version upgrade of a Cloud SQL instance. 
EXAMPLES
     To perform pre-checks before upgrading a PostgreSQL instance to a target version (supported in both GA and Beta): 
    
    
    gcloud beta sql instances pre-check-major-version-upgrade test-instance --target-database-version=POSTGRES_15

To perform pre-checks before upgrading a MySQL instance to a target version (supported in Beta only): 
    
    
    gcloud beta sql instances pre-check-major-version-upgrade test-instance --target-database-version=MYSQL_8_0

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
REQUIRED FLAGS
    

`--target-database-version`=`TARGET_DATABASE_VERSION`
     Target database version for the upgrade. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--max-runtime`=`MAX_RUNTIME`
     Maximum runtime for the pre-check, for example, 10m or 2h. Only applicable to Cloud SQL for MySQL instances. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud sql instances pre-check-major-version-upgrade](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/pre-check-major-version-upgrade)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
