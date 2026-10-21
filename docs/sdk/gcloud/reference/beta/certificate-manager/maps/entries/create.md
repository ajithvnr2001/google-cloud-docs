---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/maps/entries/create/
title: gcloud beta certificate-manager maps entries create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:14.137138+00:00
---

# gcloud beta certificate-manager maps entries create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/maps/entries/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta certificate-manager maps entries create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta certificate-manager maps entries create - create a certificate map entry 
SYNOPSIS
    

`gcloud beta certificate-manager maps entries create` (`ENTRY` : `--location`=`LOCATION` `--map`=`MAP`) (`--hostname`=`HOSTNAME` | `--set-primary`) [`--description`=`DESCRIPTION`] [`--async`] [`--certificates`=[`CERTIFICATES`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command creates a certificate map entry. 
EXAMPLES
     To create a certificate map entry with name simple-entry, run: 
    
    
    gcloud beta certificate-manager maps entries create simple-entry --map=simple-map --certificates=simple-cert

POSITIONAL ARGUMENTS
    

Certificate map entry resource - The certificate map entry to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

Arguments to configure matcher for the certificate map entry. 

Exactly one of these must be specified: 

`--hostname`=`HOSTNAME`
     A domain name (FQDN), which controls when list of certificates specified in the resource will be taken under consideration for certificate selection. 
`--set-primary`
     The certificate will be used as the default cert if no other certificate in the map matches on SNI. 
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


`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud certificate-manager maps entries create](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/maps/entries/create)
    
    
    [gcloud alpha certificate-manager maps entries create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/maps/entries/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
