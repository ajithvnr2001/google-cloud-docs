---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/transports/update/
title: gcloud beta network-connectivity transports update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:57:02.438763+00:00
---

# gcloud beta network-connectivity transports update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/transports/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-connectivity transports update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-connectivity transports update - update a transport 
SYNOPSIS
    

`gcloud beta network-connectivity transports update` (`TRANSPORT` : `--region`=`REGION`) [`--advertised-routes`=[`CIDR_RANGE`,…]] [`--async`] [`--bandwidth`=`BANDWIDTH`] [`--description`=`DESCRIPTION`] [`--stack-type`=`STACK_TYPE`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a transport with the given name to a remote provider. 
EXAMPLES
     To update a transport named ``mytransport`` in the ``us-east4`` region, run: 
    
    
    gcloud beta network-connectivity transports update mytransport --region=us-east4 --description="new description" --advertised-routes="10.0.0.0/8,10.1.0.0/16" --bandwidth=1G

POSITIONAL ARGUMENTS
    

Transport resource - Name of the Transport to be updated. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `transport` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TRANSPORT`
     ID of the transport or fully qualified identifier for the transport. 

To set the `transport` attribute: 

  * provide the argument `transport` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The location Id. To set the `region` attribute: 

  * provide the argument `transport` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


FLAGS
    

`--advertised-routes`=[`CIDR_RANGE`,…]
     List of routes to advertise from the VPC `network` toward the provider. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--bandwidth`=`BANDWIDTH`
     Bandwidth of the transport to create. Must be a supported bandwidth on the remote profile. `BANDWIDTH` must be one of: `100g`, `100m`, `10g`, `1g`, `200m`, `20g`, `2g`, `300m`, `400m`, `500m`, `50g`, `50m`, `5g`. 
`--description`=`DESCRIPTION`
     Description of the transport. 
`--stack-type`=`STACK_TYPE`
     IP version of the routes to be exchanged. `STACK_TYPE` must be one of: `ipv4-ipv6`, `ipv4-only`. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta network-connectivity transports update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta network-connectivity transports update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud network-connectivity transports update](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/transports/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
