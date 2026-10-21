---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/domains/registrations/configure/management/
title: gcloud alpha domains registrations configure management \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:38.152663+00:00
---

# gcloud alpha domains registrations configure management  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/domains/registrations/configure/management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha domains registrations configure management Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha domains registrations configure management - configure management settings of a Cloud Domains registration 
SYNOPSIS
    

`gcloud alpha domains registrations configure management` `REGISTRATION` [`--async`] [`--preferred-renewal-method`=`PREFERRED_RENEWAL_METHOD`] [`--transfer-lock-state`=`TRANSFER_LOCK_STATE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Configure management settings of a registration. This includes settings related to transfers, billing and renewals of a registration. 
EXAMPLES
     To start an interactive flow to configure management settings for ``example.com``, run: 
    
    
    gcloud alpha domains registrations configure management example.com

To unlock a transfer lock of a registration for ``example.com``, run: 
    
    
    gcloud alpha domains registrations configure management example.com --transfer-lock-state=unlocked

To disable automatic renewals for ``example.com``, run: 
    
    
    gcloud alpha domains registrations configure management example.com --preferred-renewal-method=renewal-disabled

POSITIONAL ARGUMENTS
    

Registration resource - The domain registration to configure management settings for. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `registration` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `registration` on the command line with a fully specified name; 
  * location is always global. 



This must be specified. 

`REGISTRATION`
     ID of the registration or fully qualified identifier for the registration. 

To set the `registration` attribute: 

  * provide the argument `registration` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--preferred-renewal-method`=`PREFERRED_RENEWAL_METHOD`
     Preferred Renewal Method of a registration. It defines how the registration should be renewed. The actual Renewal Method can be set to renewal-disabled in case of e.g. problems with the Billing Account or reporeted domain abuse. `PREFERRED_RENEWAL_METHOD` must be one of: 

`automatic-renewal`
     The domain is automatically renewed each year. 
`renewal-disabled`
     The domain won't be renewed and will expire at its expiration time. 
`--transfer-lock-state`=`TRANSFER_LOCK_STATE`
     Transfer Lock of a registration. It needs to be unlocked in order to transfer the domain to another registrar. `TRANSFER_LOCK_STATE` must be one of: 

`locked`
     The transfer lock is locked. 
`unlocked`
     The transfer lock is unlocked. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud domains registrations configure management](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management)
    
    
    [gcloud beta domains registrations configure management](https://docs.cloud.google.com/sdk/gcloud/reference/beta/domains/registrations/configure/management)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
