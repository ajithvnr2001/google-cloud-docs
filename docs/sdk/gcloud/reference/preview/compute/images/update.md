---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/images/update/
title: gcloud preview compute images update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:18:22.373338+00:00
---

# gcloud preview compute images update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/images/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute images update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute images update - update a Compute Engine image 
SYNOPSIS
    

`gcloud preview compute images update` `IMAGE_NAME` [`--architecture`=`ARCHITECTURE`] [`--description`=`DESCRIPTION`] [`--family`=`FAMILY`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute images update` updates labels for a Compute Engine image. 
EXAMPLES
     To update labels ``k0`` and ``k1`` and remove labels with key ``k3``, run: 
    
    
    gcloud preview compute images update example-image --update-labels=k0=value1,k1=value2 --remove-labels=k3
    
    
    k0 and k1 will be added as new labels if not already present.

Labels can be used to identify the image and to filter them like: 
    
    
    [gcloud preview compute images list](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/images/list) --filter='labels.k1:value2'

To list only the labels when describing a resource, use --format: 
    
    
    [gcloud preview compute images describe](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/images/describe) example-image --format="default(labels)"

POSITIONAL ARGUMENTS
    

`IMAGE_NAME`
     Name of the disk image to update. 
FLAGS
    

`--architecture`=`ARCHITECTURE`
     Specifies the architecture or processor type that this image can support. For available processor types on Compute Engine, see <https://cloud.google.com/compute/docs/cpu-platforms>. `ARCHITECTURE` must be one of: `ARM64`, `X86_64`. 
`--description`=`DESCRIPTION`
     An optional text description for the image. 
`--family`=`FAMILY`
     Name of the image family to use. If an image family is specified when you create an instance or disk, the latest non-deprecated image in the family is used. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud preview compute images update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud preview compute images update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute images update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/update)
    
    
    [gcloud alpha compute images update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/images/update)
    
    
    [gcloud beta compute images update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/images/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
