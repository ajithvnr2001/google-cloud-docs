---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/
title: gcloud alpha compute instance-groups \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:57:30.710064+00:00
---

# gcloud alpha compute instance-groups  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute instance-groups Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute instance-groups - read and manipulate Compute Engine instance groups 
SYNOPSIS
    

`gcloud alpha compute instance-groups` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Read and manipulate Compute Engine instance groups. 

To accommodate the differences between managed and unmanaged instances, some commands (such as `delete`) are in the managed or unmanaged subgroups. 

For more information about instance groups, see the [instance groups documentation](https://cloud.google.com/compute/docs/instance-groups/). 

See also: [Instance groups API](https://cloud.google.com/compute/docs/reference/rest/v1/instanceGroups). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[managed](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed)`
     `(ALPHA)` Read and manipulate Compute Engine managed instance groups. 
`[unmanaged](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/unmanaged)`
     `(ALPHA)` Read and manipulate Compute Engine unmanaged instance group. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/describe)`
     `(ALPHA)` Display detailed information about an instance group. 
`[get-named-ports](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/get-named-ports)`
     `(ALPHA)` Lists the named ports for an instance group resource. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list)`
     `(ALPHA)` List Google Compute Engine instance groups. 
`[list-instances](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/list-instances)`
     `(ALPHA)` List instances present in the instance group. 
`[set-named-ports](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/set-named-ports)`
     `(ALPHA)` Sets the list of named ports for an instance group. 
`[ssh](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/ssh)`
     `(ALPHA)` SSH into instances of a Compute Engine instance group. 
`[test-iam-permissions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/test-iam-permissions)`
     `(ALPHA)` Test IAM permissions for a Compute Engine instance group. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instance-groups](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups)
    
    
    [gcloud beta compute instance-groups](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups)
    
    
    [gcloud preview compute instance-groups](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
