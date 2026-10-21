---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/test-iam-permissions/
title: gcloud compute snapshots test-iam-permissions \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:19:37.062097+00:00
---

# gcloud compute snapshots test-iam-permissions  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/test-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute snapshots test-iam-permissions Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute snapshots test-iam-permissions - test IAM permissions for a Compute Engine standard or archive snapshot 
SYNOPSIS
    

`gcloud compute snapshots test-iam-permissions` `SNAPSHOT_NAME` `--permissions`=[`PERMISSION`,…] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute snapshots test-iam-permissions` tests the IAM permissions that a caller has on a Compute Engine standard or archive snapshot. 
EXAMPLES
     To test if the caller has the `compute.snapshots.get` permission on a snapshot `my-snapshot`, run: 
    
    
    gcloud compute snapshots test-iam-permissions my-snapshot --permissions=compute.snapshots.get

POSITIONAL ARGUMENTS
    

Snapshot resource - The snapshot for which to test permissions. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `snapshot_name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SNAPSHOT_NAME`
     ID of the snapshot or fully qualified identifier for the snapshot. 

To set the `snapshot_name` attribute: 

  * provide the argument `snapshot_name` on the command line. 


REQUIRED FLAGS
    

`--permissions`=[`PERMISSION`,…]
     The permissions to test. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute snapshots test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/test-iam-permissions)
    
    
    [gcloud beta compute snapshots test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshots/test-iam-permissions)
    
    
    [gcloud preview compute snapshots test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/test-iam-permissions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
