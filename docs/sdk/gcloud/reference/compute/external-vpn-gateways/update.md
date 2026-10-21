---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/update/
title: gcloud compute external-vpn-gateways update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:08:16.597519+00:00
---

# gcloud compute external-vpn-gateways update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute external-vpn-gateways update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute external-vpn-gateways update - update a Compute Engine external VPN gateway 
SYNOPSIS
    

`gcloud compute external-vpn-gateways update` `NAME` [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute external-vpn-gateways update` updates labels for a Compute Engine external VPN gateway. For example: 
    
    
    gcloud compute external-vpn-gateways update example-gateway --update-labels=k0=value1,k1=value2 --remove-labels=k3

will add/update labels ``k0`` and ``k1`` and remove labels with key ``k3``. 

Labels can be used to identify the External VPN gateway and to filter them as in 
    
    
    [gcloud compute external-vpn-gateways list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/list) --filter='labels.k1:value2'

To list existing labels 
    
    
    [gcloud compute external-vpn-gateways describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/external-vpn-gateways/describe) example-gateway --format="default(labels)"

EXAMPLES
     To update labels for an external VPN gateway, run: 
    
    
    gcloud compute external-vpn-gateways update my-external-gateway --update-labels=k0=value1,k1=value2

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the external VPN gateway to update. 
FLAGS
    

`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud compute external-vpn-gateways update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud compute external-vpn-gateways update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute external-vpn-gateways update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/external-vpn-gateways/update)
    
    
    [gcloud beta compute external-vpn-gateways update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/external-vpn-gateways/update)
    
    
    [gcloud preview compute external-vpn-gateways update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/external-vpn-gateways/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
