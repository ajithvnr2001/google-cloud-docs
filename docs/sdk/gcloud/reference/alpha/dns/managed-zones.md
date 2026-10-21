---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/
title: gcloud alpha dns managed-zones \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:30.045109+00:00
---

# gcloud alpha dns managed-zones  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dns managed-zones Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dns managed-zones - manage your Cloud DNS managed-zones 
SYNOPSIS
    

`gcloud alpha dns managed-zones` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Manage your Cloud DNS managed-zones. See [Managing Zones](https://cloud.google.com/dns/zones/) for details. 
EXAMPLES
     To create a managed-zone, run: 
    
    
    [gcloud alpha dns managed-zones create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/create) my-zone --description="My Zone" --dns-name="my.zone.com."

To delete a managed-zone, run: 
    
    
    [gcloud alpha dns managed-zones delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/delete) my-zone

To view the details of a managed-zone, run: 
    
    
    [gcloud alpha dns managed-zones describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/describe) my-zone

To see the list of all managed-zones, run: 
    
    
    [gcloud alpha dns managed-zones list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/config)`
     `(ALPHA)` Manage Dns managed zone configurations. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/create)`
     `(ALPHA)` Create a Cloud DNS managed-zone. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/delete)`
     `(ALPHA)` Delete an empty Cloud DNS managed-zone. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/describe)`
     `(ALPHA)` View the details of a Cloud DNS managed-zone. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/get-iam-policy)`
     `(ALPHA)` Get the IAM policy for a Cloud DNS managed-zone. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/list)`
     `(ALPHA)` View the list of all your managed-zones. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/set-iam-policy)`
     `(ALPHA)` Set the IAM policy for a Cloud DNS managed-zone. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/update)`
     `(ALPHA)` Update an existing Cloud DNS managed-zone. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud dns managed-zones](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones)
    
    
    [gcloud beta dns managed-zones](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/managed-zones)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
