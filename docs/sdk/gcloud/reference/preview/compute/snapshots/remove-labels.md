---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/remove-labels/
title: gcloud preview compute snapshots remove-labels \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:13:34.827614+00:00
---

# gcloud preview compute snapshots remove-labels  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/remove-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute snapshots remove-labels Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute snapshots remove-labels - remove labels from Google Compute Engine snapshots 
SYNOPSIS
    

`gcloud preview compute snapshots remove-labels` `SNAPSHOT_NAME` (`--all` | `--labels`=`KEY`,[`KEY`,…]) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute snapshots remove-labels` removes labels from a Google Compute Engine snapshot. 
EXAMPLES
     To remove existing labels with key ``k0`` and ``k1`` from 'example-snapshot' 
    
    
    gcloud preview compute snapshots remove-labels example-snapshot --labels=k0,k1

Labels can be used to identify the snapshot and to filter them. To find a snapshot labeled with key-value pair ``k1``, ``v2``
    
    
    [gcloud preview compute snapshots list](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/list) --filter='labels.k1:v2'

To list only the labels when describing a resource, use --format 
    
    
    [gcloud preview compute snapshots describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/describe) example-snapshot --format='default(labels)'

POSITIONAL ARGUMENTS
    

`SNAPSHOT_NAME`
     Name of the snapshot to operate on. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--all`
     Remove all labels from the resource. 
`--labels`=`KEY`,[`KEY`,…]
     A comma-separated list of label keys to remove from the resource. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute snapshots remove-labels](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/remove-labels)
    
    
    [gcloud alpha compute snapshots remove-labels](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/remove-labels)
    
    
    [gcloud beta compute snapshots remove-labels](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshots/remove-labels)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
