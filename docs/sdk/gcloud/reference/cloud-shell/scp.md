---
url: https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell/scp/
title: gcloud cloud-shell scp \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:07:53.027072+00:00
---

# gcloud cloud-shell scp  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/cloud-shell/scp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud cloud-shell scp Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud cloud-shell scp - copies files between Cloud Shell and the local machine 
SYNOPSIS
    

`gcloud cloud-shell scp` (`cloudshell`|`localhost`):`SRC` [(`cloudshell`|`localhost`):`SRC` …] (`cloudshell`|`localhost`):`DEST` [`--dry-run`] [`--force-key-file-overwrite`] [`--recurse`] [`--scp-flag`=`SCP_FLAG`] [`--ssh-key-file`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud cloud-shell scp` copies files between your Cloud Shell instance and your local machine using the scp command. 
EXAMPLES
     To denote a file in Cloud Shell, prefix the file name with the string "cloudshell:" (e.g. `cloudshell:`~/`FILE`). To denote a local file, prefix the file name with the string "localhost:" (e.g. `localhost:`~/`FILE`). For example, to copy a remote directory to your local machine, run: 
    
    
    gcloud cloud-shell scp cloudshell:~/REMOTE-DIR localhost:~/LOCAL-DIR

In the above example, ``~/REMOTE-DIR`` from your Cloud Shell instance is copied into the ~/`LOCAL-DIR` directory. 

Conversely, files from your local computer can be copied into Cloud Shell: 
    
    
    gcloud cloud-shell scp localhost:~/LOCAL-FILE-1 localhost:~/LOCAL-FILE-2 cloudshell:~/REMOTE-DIR

Under the covers, `scp(1)` or pscp (on Windows) is used to facilitate the transfer. 

POSITIONAL ARGUMENTS
    

cloudshell|`localhost`):`SRC`-[(`cloudshell`|`localhost`):`SRC`-…]">(`cloudshell`|`localhost`):`SRC` [(`cloudshell`|`localhost`):`SRC` …]
     Specifies the files to copy. 
cloudshell|`localhost`):`DEST`">(`cloudshell`|`localhost`):`DEST`
     Specifies a destination for the source files. 
FLAGS
    

`--dry-run`
     If provided, prints the command that would be run to standard out instead of executing it. 
`--force-key-file-overwrite`
     If enabled gcloud will regenerate and overwrite the files associated with a broken SSH key without asking for confirmation in both interactive and non-interactive environment. 

If disabled gcloud will not attempt to regenerate the files associated with a broken SSH key and fail in both interactive and non-interactive environment. 

`--recurse`
     Upload directories recursively. 
`--scp-flag`=`SCP_FLAG`
     Extra flag to be sent to scp. This flag may be repeated. 
`--ssh-key-file`
     The path to the SSH key file. By default, this is `~/.ssh/google_compute_engine`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha cloud-shell scp](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell/scp)
    
    
    [gcloud beta cloud-shell scp](https://docs.cloud.google.com/sdk/gcloud/reference/beta/cloud-shell/scp)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
