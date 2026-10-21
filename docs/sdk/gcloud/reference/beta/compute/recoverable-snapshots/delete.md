---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/delete/
title: gcloud beta compute recoverable-snapshots delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:01:21.411150+00:00
---

# gcloud beta compute recoverable-snapshots delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute recoverable-snapshots delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute recoverable-snapshots delete - delete Compute Engine recoverable snapshots 
SYNOPSIS
    

`gcloud beta compute recoverable-snapshots delete` `RECOVERABLE_SNAPSHOT_NAME` [`RECOVERABLE_SNAPSHOT_NAME` …] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute recoverable-snapshots delete` deletes one or more Compute Engine recoverable snapshots. 
EXAMPLES
     To delete Compute Engine recoverable snapshots with the names 'recoverable-snapshot-1' and 'recoverable-snapshot-2', run: 
    
    
    gcloud beta compute recoverable-snapshots delete recoverable-snapshot-1 recoverable-snapshot-2

To list all recoverable snapshots that were created before a specific date, use the --filter flag with the `[gcloud beta compute recoverable-snapshots list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/list)` command. 
    
    
    [gcloud beta compute recoverable-snapshots list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/list) --filter="creationTimestamp<'2017-01-01'"

For more information on how to use --filter with the list command, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). 

POSITIONAL ARGUMENTS
    

`RECOVERABLE_SNAPSHOT_NAME` [`RECOVERABLE_SNAPSHOT_NAME` …]
     Names of the recoverable-snapshots to delete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha compute recoverable-snapshots delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/recoverable-snapshots/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
