---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/trust-configs/update/
title: gcloud beta certificate-manager trust-configs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:16.024458+00:00
---

# gcloud beta certificate-manager trust-configs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/trust-configs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta certificate-manager trust-configs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta certificate-manager trust-configs update - update TrustConfig 
SYNOPSIS
    

`gcloud beta certificate-manager trust-configs update` (`TRUST_CONFIG` : `--location`=`LOCATION`) [`--add-allowlisted-certificates`=[`ADD_ALLOWLISTED_CERTIFICATES`,…]] [`--async`] [`--description`=`DESCRIPTION`] [`--trust-store`=[`intermediate-cas`=`INTERMEDIATE-CAS`],[`trust-anchors`=`TRUST-ANCHORS`]] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-allowlisted-certificates` | `--remove-allowlisted-certificates`=[`REMOVE_ALLOWLISTED_CERTIFICATES`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a TrustConfig. 
EXAMPLES
     To update a TrustConfig, run: 
    
    
    gcloud beta certificate-manager trust-configs update my-trust-config --description="updated description" --trust-store=trust-anchors=ta.pem,intermediate-cas="ica1.pem;ica2.pem" --update-labels=my-key1=my-updated-value1 --remove-labels=my-key2

POSITIONAL ARGUMENTS
    

TrustConfig resource - Name of the TrustConfig to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `trust_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TRUST_CONFIG`
     ID of the trustConfig or fully qualified identifier for the trustConfig. 

To set the `trust_config` attribute: 

  * provide the argument `trust_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Certificate Manager location. 

To set the `location` attribute: 

  * provide the argument `trust_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * default value of location is [global]. 


FLAGS
    

`--add-allowlisted-certificates`=[`ADD_ALLOWLISTED_CERTIFICATES`,…]
     Add allowlisted PEM-encoded certificates. Certificates should be provided in files. For multiple file names, separate them by a comma (','). One file can contain multiple certificates. 

Examples: 
    
    
    Single file: --add-allowlisted-certificates=ac.pem
    
    
    Multiple files: --add-allowlisted-certificates=ac1.pem,ac2.pem

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Human-readable description of the resource. 
`--trust-store`=[`intermediate-cas`=`INTERMEDIATE-CAS`],[`trust-anchors`=`TRUST-ANCHORS`]
     Trust Store with the given trust anchor and intermediate CA PEM-encoded certificates. Certificates should be provided in files. For multiple file names, separate them by a semicolon (';') and quote them ('"'). One file can contain multiple certificates. Intermediate CAs are optional. 

Examples: 
    
    
    Single files: --trust-store trust-anchors=ta.pem,intermediate-cas=ica.pem
    
    
    No intermediate CAs: --trust-store trust-anchors=ta.pem
    
    
    Multiple files: --trust-store trust-anchors="ta1.pem;ta2.pem",intermediate-cas="ica1.pem;ica2.pem"

`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-allowlisted-certificates`
     Clear all allowlisted certificates. 
`--remove-allowlisted-certificates`=[`REMOVE_ALLOWLISTED_CERTIFICATES`,…]
     Remove allowlisted PEM-encoded certificates. Certificates should be provided in files. For multiple file names, separate them by a comma (','). One file can contain multiple certificates. 

Examples: 
    
    
    Single file: --remove-allowlisted-certificates=ac.pem
    
    
    Multiple files: --remove-allowlisted-certificates=ac1.pem,ac2.pem

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta certificate-manager trust-configs update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta certificate-manager trust-configs update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `certificatemanager/v1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/certificate-manager/docs/overview>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud certificate-manager trust-configs update](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/trust-configs/update)
    
    
    [gcloud alpha certificate-manager trust-configs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/trust-configs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
