---
url: https://docs.cloud.google.com/sdk/gcloud/reference/secrets/enable-managed-rotation/
title: gcloud secrets enable-managed-rotation \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:20.477119+00:00
---

# gcloud secrets enable-managed-rotation  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/secrets/enable-managed-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud secrets enable-managed-rotation Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud secrets enable-managed-rotation - enable managed rotation for a secret 
SYNOPSIS
    

`gcloud secrets enable-managed-rotation` `SECRET` `--location`=`LOCATION` (`--instance-id`=`INSTANCE_ID` `--username`=`USERNAME` : `--password`=`PASSWORD`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Enable managed rotation for the specified secret. This command is used for the initial setup of managed rotation, currently supporting Cloud SQL single-user credentials. 
EXAMPLES
     To enable managed rotation for a secret `my-secret` targeting a Cloud SQL instance: 
    
    
    gcloud secrets enable-managed-rotation my-secret --location=us-central1 --instance-id=my-project:my-instance --username=db-user

To enable managed rotation and set an initial password: 
    
    
    gcloud secrets enable-managed-rotation my-secret --location=us-central1 --instance-id=my-project:my-instance --username=db-user --password="s3cr3tPassword"

POSITIONAL ARGUMENTS
    

Secret resource - The secret to enable managed rotation for. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `SECRET` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SECRET`
     ID of the secret or fully qualified identifier for the secret. 

To set the `secret` attribute: 

  * provide the argument `SECRET` on the command line. 


REQUIRED FLAGS
    

Location resource - The location of the secret. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


Cloud SQL single-user credential settings. 

This must be specified. 

`--instance-id`=`INSTANCE_ID`
     The Cloud SQL instance ID. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--username`=`USERNAME`
     The database username. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--password`=`PASSWORD`
     The initial password to set for the database user. If not provided, a random password will be generated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
