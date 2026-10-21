---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/packet-mirrorings/test-iam-permissions/
title: gcloud alpha compute packet-mirrorings test-iam-permissions \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:00:17.804205+00:00
---

# gcloud alpha compute packet-mirrorings test-iam-permissions  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/packet-mirrorings/test-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute packet-mirrorings test-iam-permissions Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute packet-mirrorings test-iam-permissions - test IAM permissions for a Compute Engine packet mirroring policy 
SYNOPSIS
    

`gcloud alpha compute packet-mirrorings test-iam-permissions` `NAME` `--permissions`=[`PERMISSION`,…] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute packet-mirrorings test-iam-permissions` tests the IAM permissions that a caller has on a Compute Engine packet mirroring policy. 

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. 

EXAMPLES
     To test if the caller has `compute.packetMirrorings.get` permission on a packet mirroring policy `my-pm` in region `us-central1`, run: 
    
    
    gcloud alpha compute packet-mirrorings test-iam-permissions my-pm --region=us-central1 --permissions=compute.packetMirrorings.get

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the packet mirroring to test IAM permissions for. 
REQUIRED FLAGS
    

`--permissions`=[`PERMISSION`,…]
     The set of permissions to check for the resource. 
OPTIONAL FLAGS
    

`--region`=`REGION`
     Region of the packet mirroring to test IAM permissions for. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute packet-mirrorings test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/compute/packet-mirrorings/test-iam-permissions)
    
    
    [gcloud beta compute packet-mirrorings test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/packet-mirrorings/test-iam-permissions)
    
    
    [gcloud preview compute packet-mirrorings test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/packet-mirrorings/test-iam-permissions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
