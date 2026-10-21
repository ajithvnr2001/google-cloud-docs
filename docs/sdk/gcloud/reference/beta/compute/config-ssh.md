---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/config-ssh/
title: gcloud beta compute config-ssh \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:41.030209+00:00
---

# gcloud beta compute config-ssh  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/config-ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute config-ssh Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute config-ssh - populate SSH config files with Host entries from each instance 
SYNOPSIS
    

`gcloud beta compute config-ssh` [`--dry-run`] [`--force-key-file-overwrite`] [`--remove`] [`--ssh-config-file`=`SSH_CONFIG_FILE`] [`--ssh-key-file`=`SSH_KEY_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute config-ssh` makes SSHing to virtual machine instances easier by adding an alias for each instance to the user SSH configuration (`~/.ssh/config`) file. 

In most cases, it is sufficient to run: 
    
    
    gcloud beta compute config-ssh

Each instance will be given an alias of the form `NAME.ZONE.PROJECT`. For example, if `example-instance` resides in `us-central1-a`, you can SSH to it by running: 
    
    
    ssh example-instance.us-central1-a.MY-PROJECT

On some platforms, the host alias can be tab-completed, making the long alias less daunting to type. 

The aliases created interface with SSH-based programs like `scp(1)`, so it is possible to use the aliases elsewhere: 
    
    
    scp ~/MY-FILE example-instance.us-central1-a.MY-PROJECT:~

Whenever instances are added, removed, or their external IP addresses are changed, the remove command must be run to clear the existing configuration and then the command can set executed to set the configuration to the current state. 

This command ensures that the user's public SSH key is present in the project's metadata. If the user does not have a public SSH key, one is generated using `ssh-keygen(1)` (if the `--quiet` flag is given, the generated key will have an empty passphrase). 

EXAMPLES
     To populate SSH config file with Host entries from each running instance, run: 
    
    
    gcloud beta compute config-ssh

To remove the change to the SSH config file by this command, run: 
    
    
    gcloud beta compute config-ssh --remove

FLAGS
    

`--dry-run`
     If provided, the proposed changes to the SSH config file are printed to standard output and no actual changes are made. 
`--force-key-file-overwrite`
     If enabled, the gcloud command-line tool will regenerate and overwrite the files associated with a broken SSH key without asking for confirmation in both interactive and non-interactive environments. 

If disabled, the files associated with a broken SSH key will not be regenerated and will fail in both interactive and non-interactive environments. 

`--remove`
     If provided, any changes made to the SSH config file by this tool are reverted. 
`--ssh-config-file`=`SSH_CONFIG_FILE`
     Specifies an alternative per-user SSH configuration file. By default, this is ``~/.ssh/config``. 
`--ssh-key-file`=`SSH_KEY_FILE`
     The path to the SSH key file. By default, this is ``~/.ssh/google_compute_engine``. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute config-ssh](https://docs.cloud.google.com/sdk/gcloud/reference/compute/config-ssh)
    
    
    [gcloud alpha compute config-ssh](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/config-ssh)
    
    
    [gcloud preview compute config-ssh](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/config-ssh)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
