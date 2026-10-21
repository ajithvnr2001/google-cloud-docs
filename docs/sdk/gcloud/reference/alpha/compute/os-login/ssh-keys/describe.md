---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-login/ssh-keys/describe/
title: gcloud alpha compute os-login ssh-keys describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:26:59.806703+00:00
---

# gcloud alpha compute os-login ssh-keys describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/os-login/ssh-keys/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute os-login ssh-keys describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute os-login ssh-keys describe - describe an SSH Public Key from an OS Login Profile 
SYNOPSIS
    

`gcloud alpha compute os-login ssh-keys describe` (`--key`=`KEY` | `--key-file`=`KEY_FILE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute os-login ssh-keys describe` accepts either a string containing an SSH Public Key or a filename for an SSH Public key and displays that key from the user's OS Login Profile. The key value used can either be the full SSH key or the OS Login fingerprint for that key. 
EXAMPLES
     To show all of the information for the key stored in your OS Login profile that matches the key in `/home/user/.ssh/id_rsa.pub`, run: 
    
    
    gcloud alpha compute os-login ssh-keys describe --key-file=/home/user/.ssh/id_rsa.pub

To show all of the information about the key with a fingerprint of 'e0d96d6fad35a61a0577f467940509b5aa08b6dea8d99456ec19a6e47126bc52', run: 
    
    
    gcloud alpha compute os-login ssh-keys describe --key='e0d96d6fad35a61a0577f467940509b5aa08b6dea8d99456ec19a6e47126bc52'

REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--key`=`KEY`
     The SSH public key to describe from the OS Login Profile. Key value can either be the SSH key or the OS Login fingerprint of the key. 
`--key-file`=`KEY_FILE`
     The path to a file containing an SSH public key to describe from the OS Login Profile. Key value can either be the SSH key or the OS Login fingerprint of the key. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute os-login ssh-keys describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-login/ssh-keys/describe)
    
    
    [gcloud beta compute os-login ssh-keys describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/os-login/ssh-keys/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
