---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh/
title: gcloud alpha cloud-shell ssh \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:25:55.357031+00:00
---

# gcloud alpha cloud-shell ssh  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha cloud-shell ssh Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha cloud-shell ssh - allows you to establish an interactive SSH session with Cloud Shell 
SYNOPSIS
    

`gcloud alpha cloud-shell ssh` [`--authorize-session`] [`--command`=`COMMAND`] [`--dry-run`] [`--force-key-file-overwrite`] [`--ssh-flag`=`SSH_FLAG`] [`--ssh-key-file`] [`GCLOUD_WIDE_FLAG …`] [-- `SSH_ARGS` …]
DESCRIPTION
     `(ALPHA)` `gcloud alpha cloud-shell ssh` lets you remotely log in to Cloud Shell. If your Cloud Shell is not currently running, this will cause it to be started before establishing the SSH session. 
EXAMPLES
     To SSH into your Cloud Shell, run: 
    
    
    gcloud alpha cloud-shell ssh

To run a remote command in your Cloud Shell, run: 
    
    
    gcloud alpha cloud-shell ssh --command=ls

POSITIONAL ARGUMENTS
    

[-- `SSH_ARGS` …]
     Flags and positionals passed to the underlying ssh implementation. The '--' argument must be specified between gcloud specific args on the left and SSH_ARGS on the right. Example: 
    
    
    gcloud alpha cloud-shell ssh -- -vvv

FLAGS
    

`--authorize-session`
     If provided, sends OAuth credentials to the current Cloud Shell session on behalf of the user. When this completes, the session will be authorized to run various Google Cloud command-line tools without requiring the user to manually authenticate. 
`--command`=`COMMAND`
     A command to run in Cloud Shell. 

Runs the command in Cloud Shell and then exits. 

`--dry-run`
     If provided, prints the command that would be run to standard out instead of executing it. 
`--force-key-file-overwrite`
     If enabled gcloud will regenerate and overwrite the files associated with a broken SSH key without asking for confirmation in both interactive and non-interactive environment. 

If disabled gcloud will not attempt to regenerate the files associated with a broken SSH key and fail in both interactive and non-interactive environment. 

`--ssh-flag`=`SSH_FLAG`
     Additional flags to be passed to `ssh(1)`. 
`--ssh-key-file`
     The path to the SSH key file. By default, this is `~/.ssh/google_compute_engine`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud cloud-shell ssh](https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell/ssh)
    
    
    [gcloud beta cloud-shell ssh](https://docs.cloud.google.com/sdk/gcloud/reference/beta/cloud-shell/ssh)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
