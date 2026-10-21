---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoint-associations/update/
title: gcloud beta network-security firewall-endpoint-associations update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:55:51.771478+00:00
---

# gcloud beta network-security firewall-endpoint-associations update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoint-associations/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security firewall-endpoint-associations update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security firewall-endpoint-associations update - update a Firewall Plus endpoint association 
SYNOPSIS
    

`gcloud beta network-security firewall-endpoint-associations update` (`FIREWALL_ENDPOINT_ASSOCIATION` : `--zone`=`ZONE`) [`--async`] [`--location`=`LOCATION`] [`--max-wait`=`MAX_WAIT`; default="60m"] [`--disabled` | `--update-labels`=[`KEY`=`VALUE`,…] `--clear-labels` | `--remove-labels`=[`KEY`,…] `--no-tls-inspection-policy` | [`--tls-inspection-policy`=`TLS_INSPECTION_POLICY` : `--tls-inspection-policy-project`=`TLS_INSPECTION_POLICY_PROJECT` `--tls-inspection-policy-region`=`TLS_INSPECTION_POLICY_REGION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a firewall endpoint association. Check the progress of association update by using `[gcloud network-security firewall-endpoint-associations describe](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/describe)`. 

For more examples, refer to the EXAMPLES section below. 

EXAMPLES
     To update labels k1 and k2, run: 
    
    
    [gcloud beta network-security firewall-endpoint-associations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoint-associations) update my-assoc --zone=us-central1-a --project=my-proj --update-labels=k1=v1,k2=v2

To remove labels k3 and k4, run: 
    
    
    [gcloud beta network-security firewall-endpoint-associations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoint-associations) update my-assoc --zone=us-central1-a --project=my-proj --remove-labels=k3,k4

To clear all labels from the firewall endpoint association, run: 
    
    
    [gcloud beta network-security firewall-endpoint-associations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoint-associations) update my-assoc --zone=us-central1-a --project=my-proj --clear-labels

POSITIONAL ARGUMENTS
    

Firewall endpoint association resource - Firewall Plus. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `FIREWALL_ENDPOINT_ASSOCIATION` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FIREWALL_ENDPOINT_ASSOCIATION`
     ID of the firewall endpoint association or fully qualified identifier for the firewall endpoint association. 

To set the `association-name` attribute: 

  * provide the argument `FIREWALL_ENDPOINT_ASSOCIATION` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     Zone of the firewall endpoint association. 

To set the `zone` attribute: 

  * provide the argument `FIREWALL_ENDPOINT_ASSOCIATION` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--location`=`LOCATION`
     Location of the firewall endpoint association 
`--max-wait`=`MAX_WAIT`; default="60m"
     Time to synchronously wait for the operation to complete, after which the operation continues asynchronously. Ignored if --no-async isn't specified. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
At most one of these can be specified: 

`--disabled`
     Disable a firewall endpoint association. To enable a disabled association, use: 
    
    
    [gcloud beta network-security firewall-endpoint-associations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoint-associations) update MY-ASSOCIATION --no-disabled

Or at least one of these can be specified: 

`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    [gcloud beta network-security firewall-endpoint-associations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoint-associations) update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    [gcloud beta network-security firewall-endpoint-associations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoint-associations) update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--no-tls-inspection-policy`
     Remove TLS inspection policy from this association. 
Or at least one of these can be specified: 

TLS Inspection Policy resource - Path to TLS Inspection Policy configuration to use for intercepting TLS-encrypted traffic in this network. The arguments in this group can be used to specify the attributes of this resource. 
`--tls-inspection-policy`=`TLS_INSPECTION_POLICY`
     ID of the TLS Inspection Policy or fully qualified identifier for the TLS Inspection Policy. 

To set the `tls_inspection_policy` attribute: 

  * provide the argument `--tls-inspection-policy` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--tls-inspection-policy-project`=`TLS_INSPECTION_POLICY_PROJECT`
     Project of the TLS Inspection Policy. 

To set the `tls-inspection-policy-project` attribute: 

  * provide the argument `--tls-inspection-policy` on the command line with a fully specified name; 
  * provide the argument `--tls-inspection-policy-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * provide the argument `FIREWALL_ENDPOINT_ASSOCIATION` on the command line with a fully specified name. 


`--tls-inspection-policy-region`=`TLS_INSPECTION_POLICY_REGION`
     Region of the TLS Inspection Policy. NOTE: TLS Inspection Policy needs to be in the same region as Firewall Plus endpoint resource. To set the `tls-inspection-policy-region` attribute: 

  * provide the argument `--tls-inspection-policy` on the command line with a fully specified name; 
  * provide the argument `--tls-inspection-policy-region` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-security firewall-endpoint-associations update](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update)
    
    
    [gcloud alpha network-security firewall-endpoint-associations update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/firewall-endpoint-associations/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
