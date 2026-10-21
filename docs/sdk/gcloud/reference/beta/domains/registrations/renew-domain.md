---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/domains/registrations/renew-domain/
title: gcloud beta domains registrations renew-domain \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:04:28.016991+00:00
---

# gcloud beta domains registrations renew-domain  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/domains/registrations/renew-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta domains registrations renew-domain Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta domains registrations renew-domain - renew a recently expired Cloud Domains registration 
SYNOPSIS
    

`gcloud beta domains registrations renew-domain` `REGISTRATION` [`--validate-only`] [`--async`] [`--yearly-price`=`YEARLY_PRICE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Use this method to renew domains that expired within the last 30 days. Renewing your domain extends it for one year from the previous expiration date and you are charged the yearly renewal price. 
EXAMPLES
     To renew a registration for ``example.com`` interactively, run: 
    
    
    gcloud beta domains registrations renew-domain example.com

To renew ``example.com`` with interactive prompts disabled, provide the --yearly-price flag. For example, run: 
    
    
    gcloud beta domains registrations renew-domain example.com --yearly-price="12.00 USD" --quiet

POSITIONAL ARGUMENTS
    

Registration resource - The domain registration to renew. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


COMMONLY USED FLAGS
    

`--validate-only`
     Don't actually renew registration. Only validate arguments. 
OTHER FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--yearly-price`=`YEARLY_PRICE`
     Accept the domain's yearly price in the interactive flow or by using this flag. Use a number followed by a currency code, for example, "12.00 USD". Get the price by calling the renew-domain command without the --yearly-price flag. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud domains registrations renew-domain](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/renew-domain)
    
    
    [gcloud alpha domains registrations renew-domain](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/domains/registrations/renew-domain)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
