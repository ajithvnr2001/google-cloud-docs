---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/create/
title: gcloud alpha sql blue-green-deployments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:00.718094+00:00
---

# gcloud alpha sql blue-green-deployments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/blue-green-deployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql blue-green-deployments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql blue-green-deployments create - creates a Cloud SQL blue-green deployment 
SYNOPSIS
    

`gcloud alpha sql blue-green-deployments create` `DEPLOYMENT` `--source-instance`=`SOURCE_INSTANCE` [`--async`] [`--description`=`DESCRIPTION`] [`--region`=`REGION`] [`--target-database-version`=`TARGET_DATABASE_VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a Cloud SQL blue-green deployment. 
EXAMPLES
     To create a blue-green deployment named `my-deployment` from source instance `my-instance` in region `us-central1`: 
    
    
    gcloud alpha sql blue-green-deployments create my-deployment --source-instance=my-instance --region=us-central1

To create a blue-green deployment with a target database version for a major version upgrade: 
    
    
    gcloud alpha sql blue-green-deployments create my-deployment --source-instance=my-instance --target-database-version=POSTGRES_15 --region=us-central1

POSITIONAL ARGUMENTS
    

`DEPLOYMENT`
     The ID of the blue-green deployment. 
REQUIRED FLAGS
    

`--source-instance`=`SOURCE_INSTANCE`
     Cloud SQL instance to be used as source for the blue-green deployment. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     User-provided description for the blue-green deployment. 
`--region`=`REGION`
     Regional location (e.g. asia-east1, us-east1). See the full list of regions at <https://cloud.google.com/sql/docs/instance-locations>. 
`--target-database-version`=`TARGET_DATABASE_VERSION`
     Database version for the target instance, for major version upgrade. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta sql blue-green-deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/blue-green-deployments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
