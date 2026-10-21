---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/maps/entries/update/
title: gcloud beta certificate-manager maps entries update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:56:10.690108+00:00
---

# gcloud beta certificate-manager maps entries update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/maps/entries/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta certificate-manager maps entries update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta certificate-manager maps entries update - update a certificate map entry 
SYNOPSIS
    

`gcloud beta certificate-manager maps entries update` (`ENTRY` : `--location`=`LOCATION` `--map`=`MAP`) [`--description`=`DESCRIPTION`] [`--async`] [`--certificates`=[`CERTIFICATES`,…]] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command updates existing certificate map entry. 
EXAMPLES
     To update a certificate map entry with name simple-entry, run: 
    
    
    gcloud beta certificate-manager maps entries update simple-entry --map="simple-map" --description="desc" --update-labels="key=value" --certificates="simple-cert"

POSITIONAL ARGUMENTS
    

Certificate map entry resource - The certificate map entry to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENTRY`
     ID of the certificate map entry or fully qualified identifier for the certificate map entry. 

To set the `entry` attribute: 

  * provide the argument `entry` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the certificate map entry. 

To set the `location` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * default value of location is [global]. 


`--map`=`MAP`
     The certificate map for the certificate map entry. 

To set the `map` attribute: 

  * provide the argument `entry` on the command line with a fully specified name; 
  * provide the argument `--map` on the command line. 


COMMONLY USED FLAGS
    

`--description`=`DESCRIPTION`
     Text description of a certificate map entry. 
OTHER FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Certificate resource - The certificates to be attached to the entry. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--certificates` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--certificates` on the command line with a fully specified name; 
  * default value of location is [global]. 


`--certificates`=[`CERTIFICATES`,…]
     IDs of the certificates or fully qualified identifiers for the certificates. 

To set the `certificate` attribute: 

  * provide the argument `--certificates` on the command line. 


`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta certificate-manager maps entries update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta certificate-manager maps entries update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud certificate-manager maps entries update](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/update)
    
    
    [gcloud alpha certificate-manager maps entries update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
