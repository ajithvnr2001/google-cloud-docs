---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-login/ssh-keys/add/
title: gcloud alpha compute os-login ssh-keys add \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:07:49.547124+00:00
---

# gcloud alpha compute os-login ssh-keys add  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-login/ssh-keys/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute os-login ssh-keys add Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute os-login ssh-keys add - add an SSH public key to an OS Login profile 
SYNOPSIS
    

`gcloud alpha compute os-login ssh-keys add` (`--key`=`KEY` | `--key-file`=`KEY_FILE`) [`--ttl`=`TTL`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute os-login ssh-keys add` accepts either a string containing an SSH public key or a filename for an SSH public key and adds that key to the user's OS Login profile. 
EXAMPLES
     To add the key in `/home/user/.ssh/id_rsa.pub` to your OS Login profile, run: 
    
    
    gcloud alpha compute os-login ssh-keys add --key-file=/home/user/.ssh/id_rsa.pub

To add the same key, but with a one year expiration time, run: 
    
    
    gcloud alpha compute os-login ssh-keys add --key-file=/home/user/.ssh/id_rsa.pub --ttl=1y

To add a key not stored in a file, run: 
    
    
    gcloud alpha compute os-login ssh-keys add --key='ssh-rsa AAAAB3NzaC1yc2EAAA…MTg+InRG47+/O4/uWEOy6gIQEF
     user@example.com'

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--key`=`KEY`
     The SSH public key to add to the OS Login Profile. 
`--key-file`=`KEY_FILE`
     The path to a file containing an SSH public key to add to the OS Login Profile. 
OPTIONAL FLAGS
    

`--ttl`=`TTL`
     The amount of time before the SSH key expires. For example, specifying ``30m`` will set the expiration time on the SSH key for 30 minutes from the current time. A value of 0 will result in no expiration time. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute os-login ssh-keys add](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/add)
    
    
    [gcloud beta compute os-login ssh-keys add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-login/ssh-keys/add)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
