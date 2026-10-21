---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/describe/
title: gcloud alpha compute snapshots describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:07:21.425034+00:00
---

# gcloud alpha compute snapshots describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute snapshots describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute snapshots describe - describe a Compute Engine snapshot 
SYNOPSIS
    

`gcloud alpha compute snapshots describe` `SNAPSHOT_NAME` [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute snapshots describe` displays all data associated with a Compute Engine snapshot in a project. 

Given an existing snapshot is queried, successful output of this command looks like the following: 
    
    
    creationTimestamp: '2018-05-07T10:45:46.988-07:00'
    diskSizeGb: '500'
    id: '1234567891234567890'
    kind: compute#snapshot
    labelFingerprint: 12345abcdWW=
    name: zs9utdhb8r1x
    selfLink: <https://www.googleapis.com/compute/v1/projects/test-project-name/global/snapshots/snapshot-number>
    sourceDisk: <https://www.googleapis.com/compute/v1/projects/test-project-name/zones/us-central1-c/disks/test>
    sourceDiskId: '1234567891234567890'
    status: READY
    storageBytes: '0'
    storageBytesStatus: UP_TO_DATE

EXAMPLES
     To run `gcloud alpha compute snapshots describe`, you'll need the name of a snapshot. To list existing snapshots by name, run: 
    
    
    [gcloud alpha compute snapshots list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/list)

To display specific details of an existing Compute Engine snapshot (like its creation time, status, and storage details), run: 
    
    
    gcloud alpha compute snapshots describe SNAPSHOT_NAME --format="table(creationTimestamp, status, storageBytesStatus)"

POSITIONAL ARGUMENTS
    

`SNAPSHOT_NAME`
     Name of the snapshot to describe. 
FLAGS
    

At most one of these can be specified: 

`--global`
     If set, the snapshot is global. 
`--region`=`REGION`
     Region of the snapshot to describe. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute snapshots describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/describe)
    
    
    [gcloud beta compute snapshots describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshots/describe)
    
    
    [gcloud preview compute snapshots describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
