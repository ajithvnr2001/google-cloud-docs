---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/change-quorum/
title: gcloud alpha spanner databases change-quorum \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:51:31.440260+00:00
---

# gcloud alpha spanner databases change-quorum  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/databases/change-quorum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha spanner databases change-quorum Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha spanner databases change-quorum - change quorum of a Cloud Spanner database 
SYNOPSIS
    

`gcloud alpha spanner databases change-quorum` (`DATABASE` : `--instance`=`INSTANCE`) (`--dual-region` | `--serving-location`=`SERVING_LOCATION` `--single-region`) [`--etag`=`ETAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Change quorum of a Cloud Spanner database. 
EXAMPLES
     To trigger change quorum from single-region mode to dual-region mode, run: 
    
    
    gcloud alpha spanner databases change-quorum my-database-id --instance=my-instance-id --dual-region

To trigger change quorum from dual-region mode to single-region mode with serving location as `asia-south1`, run: 
    
    
    gcloud alpha spanner databases change-quorum my-database-id --instance=my-instance-id --single-region --serving-location=asia-south1

To trigger change quorum using etag specified, run: 
    
    
    gcloud alpha spanner databases change-quorum my-database-id --instance=my-instance-id --dual-region --etag=ETAG

POSITIONAL ARGUMENTS
    

Database resource - The Cloud Spanner database to change quorum. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATABASE`
     ID of the database or fully qualified identifier for the database. 

To set the `database` attribute: 

  * provide the argument `database` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The Cloud Spanner instance for the database. 

To set the `instance` attribute: 

  * provide the argument `database` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

Command-line flag for dual-region quorum change: 
`--dual-region`
     Switch to dual-region quorum type. 
Command-line flags for single-region quorum change: 
`--serving-location`=`SERVING_LOCATION`
     The cloud Spanner location. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--single-region`
     Switch to single-region quorum type. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--etag`=`ETAG`
     Used for optimistic concurrency control. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud spanner databases change-quorum](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/change-quorum)
    
    
    [gcloud beta spanner databases change-quorum](https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/databases/change-quorum)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
