---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/feature-configs/create/
title: gcloud alpha storage feature-configs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:39.867518+00:00
---

# gcloud alpha storage feature-configs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/feature-configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage feature-configs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage feature-configs create - create a new Feature Config 
SYNOPSIS
    

`gcloud alpha storage feature-configs create` `CONFIG_ID` (`--auto-annotate-models`=[`AUTO_ANNOTATE_MODELS`,…] `--auto-annotate-processing-location`=`AUTO_ANNOTATE_PROCESSING_LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--exclude-bucket-id-regexes`=[`EXCLUDE_BUCKET_ID_REGEXES`,…] | `--include-bucket-id-regexes`=[`INCLUDE_BUCKET_ID_REGEXES`,…]] [`--exclude-locations`=[`EXCLUDE_LOCATIONS`,…] | `--include-locations`=[`INCLUDE_LOCATIONS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Feature Config. 
EXAMPLES
     To create a Feature Config with config ID "sample_config", auto-annotate model "face-detector", and specified processing location: 
    
    
    gcloud alpha storage feature-configs create sample_config --auto-annotate-models=face-detector --auto-annotate-processing-location=us

POSITIONAL ARGUMENTS
    

`CONFIG_ID`
     The ID of the feature configuration to create. 
REQUIRED FLAGS
    

This must be specified. 

`--auto-annotate-models`=[`AUTO_ANNOTATE_MODELS`,…]
     Comma-separated list of models to configure. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--auto-annotate-processing-location`=`AUTO_ANNOTATE_PROCESSING_LOCATION`
     Specifies the geographic location (case-sensitive) where data is processed. Must be a supported location. See public documentation for supported locations. 

This flag argument must be specified if any of the other arguments in this group are specified. 

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description of the feature configuration. 
BUCKET REGEXES FLAGS
    

Specify bucket ID regexes to include or exclude. 

At most one of these can be specified: 

`--exclude-bucket-id-regexes`=[`EXCLUDE_BUCKET_ID_REGEXES`,…]
     Comma-separated list of bucket ID regexes to exclude. 
`--include-bucket-id-regexes`=[`INCLUDE_BUCKET_ID_REGEXES`,…]
     Comma-separated list of bucket ID regexes to include. 
LOCATIONS FLAGS
    

Specify locations to include or exclude. 

At most one of these can be specified: 

`--exclude-locations`=[`EXCLUDE_LOCATIONS`,…]
     Comma-separated list of locations to exclude. 
`--include-locations`=[`INCLUDE_LOCATIONS`,…]
     Comma-separated list of locations to include. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
