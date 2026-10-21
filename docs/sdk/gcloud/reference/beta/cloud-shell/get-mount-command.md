---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/cloud-shell/get-mount-command/
title: gcloud beta cloud-shell get-mount-command \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:20:03.342688+00:00
---

# gcloud beta cloud-shell get-mount-command  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/cloud-shell/get-mount-command/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta cloud-shell get-mount-command Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta cloud-shell get-mount-command - prints a command to mount the Cloud Shell home directory via sshfs 
SYNOPSIS
    

`gcloud beta cloud-shell get-mount-command` `MOUNT_DIR` [`--force-key-file-overwrite`] [`--ssh-key-file`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta cloud-shell get-mount-command` starts your Cloud Shell if it is not already running, then prints out a command that allows you to mount the Cloud Shell home directory onto your local file system using `sshfs`. You must install and run sshfs yourself. 

After mounting the Cloud Shell home directory, any changes you make under the mount point on your local file system will be reflected in Cloud Shell and vice-versa. 

EXAMPLES
     To print a command that mounts a remote directory onto your local file system, run: 
    
    
    gcloud beta cloud-shell get-mount-command REMOTE-DIR

POSITIONAL ARGUMENTS
    

`MOUNT_DIR`
     Local directory onto which the Cloud Shell home directory should be mounted. 
FLAGS
    

`--force-key-file-overwrite`
     If enabled gcloud will regenerate and overwrite the files associated with a broken SSH key without asking for confirmation in both interactive and non-interactive environment. 

If disabled gcloud will not attempt to regenerate the files associated with a broken SSH key and fail in both interactive and non-interactive environment. 

`--ssh-key-file`
     The path to the SSH key file. By default, this is `~/.ssh/google_compute_engine`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud cloud-shell get-mount-command](https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell/get-mount-command)
    
    
    [gcloud alpha cloud-shell get-mount-command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/get-mount-command)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
