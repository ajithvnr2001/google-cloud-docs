---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/groups/test-iam-permissions/
title: gcloud preview compute interconnects attachments groups test-iam-permissions \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:37:08.921583+00:00
---

# gcloud preview compute interconnects attachments groups test-iam-permissions  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/groups/test-iam-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute interconnects attachments groups test-iam-permissions Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute interconnects attachments groups test-iam-permissions - test IAM permissions for a Compute Engine interconnect attachment group 
SYNOPSIS
    

`gcloud preview compute interconnects attachments groups test-iam-permissions` `INTERCONNECT_ATTACHMENT_GROUP` `--permissions`=[`PERMISSIONS`,…] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` Returns permissions that a caller has on the specified interconnect attachment group. 
EXAMPLES
     To test if the caller has `compute.interconnectAttachmentGroups.get` permission on an interconnect attachment group, run: 
    
    
    [gcloud preview compute interconnects attachments groups](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/interconnects/attachments/groups) test-iam-permissions my-interconnect-attachment-group --permissions=compute.interconnectAttachmentGroups.get

POSITIONAL ARGUMENTS
    

Interconnect attachment group resource - The interconnect attachment group for which to test permissions. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `interconnect_attachment_group` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INTERCONNECT_ATTACHMENT_GROUP`
     ID of the interconnect_attachment_group or fully qualified identifier for the interconnect_attachment_group. 

To set the `interconnect_attachment_group` attribute: 

  * provide the argument `interconnect_attachment_group` on the command line. 


REQUIRED FLAGS
    

`--permissions`=[`PERMISSIONS`,…]
     Permissions to be tested. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute interconnects attachments groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/groups) test-iam-permissions
    
    
    [gcloud alpha compute interconnects attachments groups](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/attachments/groups) test-iam-permissions
    
    
    [gcloud beta compute interconnects attachments groups](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/interconnects/attachments/groups) test-iam-permissions

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
