---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instance-configs/update/
title: gcloud beta spanner instance-configs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:42.481681+00:00
---

# gcloud beta spanner instance-configs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/instance-configs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner instance-configs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner instance-configs update - update a Cloud Spanner instance configuration 
SYNOPSIS
    

`gcloud beta spanner instance-configs update` `INSTANCE_CONFIG` [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--etag`=`ETAG`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--validate-only`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Cloud Spanner instance configuration. 
EXAMPLES
     To update display name of a custom Cloud Spanner instance configuration 'custom-instance-config', run: 
    
    
    gcloud beta spanner instance-configs update custom-instance-config --display-name=nam3-RO-us-central1

To modify the instance config 'custom-instance-config' by adding label 'k0', with value 'value1' and label 'k1' with value 'value2' and removing labels with key 'k3', run: 
    
    
    gcloud beta spanner instance-configs update custom-instance-config --update-labels=k0=value1,k1=value2 --remove-labels=k3

To clear all labels of a custom Cloud Spanner instance configuration 'custom-instance-config', run: 
    
    
    gcloud beta spanner instance-configs update custom-instance-config --clear-labels

To remove an existing label of a custom Cloud Spanner instance configuration 'custom-instance-config', run: 
    
    
    gcloud beta spanner instance-configs update custom-instance-config --remove-labels=KEY1,KEY2

POSITIONAL ARGUMENTS
    

`INSTANCE_CONFIG`
     Cloud Spanner instance config. The 'custom-' prefix is required to avoid name conflicts with Google-managed configurations. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     The name of this instance configuration as it appears in UIs. 
`--etag`=`ETAG`
     Used for optimistic concurrency control. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--validate-only`
     Use this flag to validate that the request will succeed before executing it. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta spanner instance-configs update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta spanner instance-configs update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner instance-configs update](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update)
    
    
    [gcloud alpha spanner instance-configs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/instance-configs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
