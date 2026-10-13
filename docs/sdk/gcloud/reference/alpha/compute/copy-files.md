---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/copy-files/
title: gcloud alpha compute copy-files \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:54.769723+00:00
---

# gcloud alpha compute copy-files  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/copy-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute copy-files Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute copy-files - copy files to and from Google Compute Engine virtual machines via scp 
SYNOPSIS
    

`gcloud alpha compute copy-files` [[`USER`@]`INSTANCE`:]`SRC` [[[`USER`@]`INSTANCE`:]`SRC` …] [[`USER`@]`INSTANCE`:]`DEST` [`--dry-run`] [`--force-key-file-overwrite`] [`--plain`] [`--ssh-key-file`=`SSH_KEY_FILE`] [`--strict-host-key-checking`=`STRICT_HOST_KEY_CHECKING`] [`--zone`=`ZONE`] [`--ssh-key-expiration`=`SSH_KEY_EXPIRATION` | `--ssh-key-expire-after`=`SSH_KEY_EXPIRE_AFTER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute copy-files` copies files between a virtual machine instance and your local machine using the scp command. This command does not work for Windows VMs. 

To denote a remote file, prefix the file name with the virtual machine instance name (e.g., `example-instance`:~/`FILE`). To denote a local file, do not add a prefix to the file name (e.g., ~/`FILE`). 

If a file contains a colon (``:´´), you must specify it by either using an absolute path or a path that begins with ``./´´. 

Under the covers, `scp(1)` or pscp (on Windows) is used to facilitate the transfer. 

When the destination is local, all sources must be the same virtual machine instance. When the destination is remote, all sources must be local. 

EXAMPLES
     To copy a remote directory '~/REMOTE-DIR' on the instance of 'example-instance' to '~/LOCAL-DIR' on the local host, run: 
    
    
    gcloud alpha compute copy-files example-instance:~/REMOTE-DIR ~/LOCAL-DIR --zone=us-central1-a

To copy files from your local host to a virtual machine, run: 
    
    
    gcloud alpha compute copy-files ~/LOCAL-FILE-1 ~/LOCAL-FILE-2 example-instance:~/REMOTE-DIR --zone=us-central1-a

POSITIONAL ARGUMENTS
    

[[`USER`@]`INSTANCE`:]`SRC` [[[`USER`@]`INSTANCE`:]`SRC` …]
     Specifies the files to copy. 
[[`USER`@]`INSTANCE`:]`DEST`
     Specifies a destination for the source files. 
FLAGS
    

`--dry-run`
     Print the equivalent scp/ssh command that would be run to stdout, instead of executing it. 
`--force-key-file-overwrite`
     If enabled, the gcloud command-line tool will regenerate and overwrite the files associated with a broken SSH key without asking for confirmation in both interactive and non-interactive environments. 

If disabled, the files associated with a broken SSH key will not be regenerated and will fail in both interactive and non-interactive environments. 

`--plain`
     Suppress the automatic addition of `ssh(1)`/`scp(1)` flags. This flag is useful if you want to take care of authentication yourself or use specific ssh/scp features. 
`--ssh-key-file`=`SSH_KEY_FILE`
     The path to the SSH key file. By default, this is ``~/.ssh/google_compute_engine``. 
`--strict-host-key-checking`=`STRICT_HOST_KEY_CHECKING`
     Override the default behavior of StrictHostKeyChecking for the connection. By default, StrictHostKeyChecking is set to 'no' the first time you connect to an instance, and will be set to 'yes' for all subsequent connections. `STRICT_HOST_KEY_CHECKING` must be one of: `yes`, `no`, `ask`. 
`--zone`=`ZONE`
     The zone of the instance to copy files to/from. 

If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

At most one of these can be specified: 

`--ssh-key-expiration`=`SSH_KEY_EXPIRATION`
     The time when the ssh key will be valid until, such as "2017-08-29T18:52:51.142Z." This is only valid if the instance is not using OS Login. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--ssh-key-expire-after`=`SSH_KEY_EXPIRE_AFTER`
     The maximum length of time an SSH key is valid for once created and installed, e.g. 2m for 2 minutes. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute copy-files](https://docs.cloud.google.com/sdk/gcloud/reference/compute/copy-files)
    
    
    [gcloud beta compute copy-files](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/copy-files)
    
    
    [gcloud preview compute copy-files](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/copy-files)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
