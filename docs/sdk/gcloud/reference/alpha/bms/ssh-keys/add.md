---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bms/ssh-keys/add/
title: gcloud alpha bms ssh-keys add \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:45.691365+00:00
---

# gcloud alpha bms ssh-keys add  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/bms/ssh-keys/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha bms ssh-keys add Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha bms ssh-keys add - add a public SSH key to the project in Bare Metal Solution 
SYNOPSIS
    

`gcloud alpha bms ssh-keys add` `SSH_KEY` (`--key`=`KEY` | `--key-file`=`KEY_FILE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Add a public SSH key to the project in Bare Metal Solution. 
EXAMPLES
     To add an SSH key called ``my-ssh-key`` in project ``my-project`` with a public key ``ABC6695``
    
    
    gcloud alpha bms ssh-keys add my-ssh-key --project=my-project --key=ABC6695

To add an SSH key called ``my-ssh-key`` in project ``my-project`` with a public key stored in /home/user/.ssh/id_rsa.pub 
    
    
    gcloud alpha bms ssh-keys add my-ssh-key --project=my-project --key-file=/home/user/.ssh/id_rsa.pub

POSITIONAL ARGUMENTS
    

SSH key resource - ssh_key. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `ssh_key` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `ssh_key` on the command line with a fully specified name; 
  * global is the only supported location. 



This must be specified. 

`SSH_KEY`
     ID of the SSH key or fully qualified identifier for the SSH key. 

To set the `ssh_key` attribute: 

  * provide the argument `ssh_key` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--key`=`KEY`
     The SSH public key to add 
`--key-file`=`KEY_FILE`
     The path to a file containing an SSH public key to add 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud bms ssh-keys add](https://docs.cloud.google.com/sdk/gcloud/reference/bms/ssh-keys/add)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
