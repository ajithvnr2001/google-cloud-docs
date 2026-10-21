---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/connect-to-serial-port/
title: gcloud preview compute connect-to-serial-port \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:47.004557+00:00
---

# gcloud preview compute connect-to-serial-port  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/connect-to-serial-port/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute connect-to-serial-port Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute connect-to-serial-port - connect to the serial port of an instance 
SYNOPSIS
    

`gcloud preview compute connect-to-serial-port` [`USER`@]`INSTANCE` [`--dry-run`] [`--extra-args`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--force-key-file-overwrite`] [`--location`=`LOCATION`] [`--port`=`PORT`; default=1] [`--ssh-key-file`=`SSH_KEY_FILE`] [`--zone`=`ZONE`] [`--ssh-key-expiration`=`SSH_KEY_EXPIRATION` | `--ssh-key-expire-after`=`SSH_KEY_EXPIRE_AFTER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute connect-to-serial-port` allows users to connect to, and interact with, a VM's virtual serial port using ssh as the secure, authenticated transport protocol. 

The user must first enable serial port access to a given VM by setting the 'serial-port-enable=true' metadata key-value pair. Setting 'serial-port-enable' on the project-level metadata enables serial port access to all VMs in the project. 

This command uses the same SSH key pair as the `[gcloud compute ssh](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh)` command and also ensures that the user's public SSH key is present in the project's metadata. If the user does not have a public SSH key, one is generated using ssh-keygen. 

EXAMPLES
     To connect to the serial port of the instance 'my-instance' in zone 'us-central1-f', run: 
    
    
    gcloud preview compute connect-to-serial-port my-instance --zone=us-central1-f

POSITIONAL ARGUMENTS
    

[`USER`@]`INSTANCE`
     Specifies the user/instance for the serial port connection. 

``USER`` specifies the username to authenticate as. If omitted, the current OS user is selected. 

FLAGS
    

`--dry-run`
     If provided, the ssh command is printed to standard out rather than being executed. 
`--extra-args`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     Optional arguments can be passed to the serial port connection by passing key-value pairs to this flag, such as max-connections=N or replay-lines=N. See <https://cloud.google.com/compute/docs/instances/interacting-with-serial-console> for additional options. 
`--force-key-file-overwrite`
     If enabled, the gcloud command-line tool will regenerate and overwrite the files associated with a broken SSH key without asking for confirmation in both interactive and non-interactive environments. 

If disabled, the files associated with a broken SSH key will not be regenerated and will fail in both interactive and non-interactive environments. 

`--location`=`LOCATION`
     If provided, the region in which the serial console connection will occur. Must be the region of the VM to connect to. 
`--port`=`PORT`; default=1
     The number of the requested serial port. Can be 1-4, default is 1. 

Instances can support up to four serial ports. By default, this command will connect to the first serial port. Setting this flag will connect to the requested serial port. 

`--ssh-key-file`=`SSH_KEY_FILE`
     The path to the SSH key file. By default, this is ``~/.ssh/google_compute_engine``. 
`--zone`=`ZONE`
     Zone of the instance to connect to. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

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
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute connect-to-serial-port](https://docs.cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port)
    
    
    [gcloud alpha compute connect-to-serial-port](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/connect-to-serial-port)
    
    
    [gcloud beta compute connect-to-serial-port](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/connect-to-serial-port)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
