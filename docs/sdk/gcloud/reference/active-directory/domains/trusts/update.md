---
url: https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/update/
title: gcloud active-directory domains trusts update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:33.919412+00:00
---

# gcloud active-directory domains trusts update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/trusts/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud active-directory domains trusts update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud active-directory domains trusts update - update target DNS IP addresses for a Managed Microsoft AD trust 
SYNOPSIS
    

`gcloud active-directory domains trusts update` `DOMAIN` `--target-dns-ip-addresses`=[`TARGET_DNS_IP_ADDRESSES`,…] `--target-domain-name`=`TARGET_DOMAIN_NAME` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update target DNS IP addresses for a Managed Microsoft AD trust between the managed domain and the target domain. 
    
    
    This command can fail for the following reasons:
      * The domain specified does not exist.
      * The active account does not have permission to access the given
        domain.
      * The AD trust specified does not exist.
      * The active account does not have permission to access the given
        AD trust.

EXAMPLES
     The following command updates the target DNS IP address for the AD trust between `my-domain.com` and ` my-target-domain.com` to `10.177.0.3`. 
    
    
    gcloud active-directory domains trusts update my-domain.com --target-domain-name=my-target-domain.com --target-dns-ip-addresses=10.177.0.3

POSITIONAL ARGUMENTS
    

Domain resource - Name of the Managed Microsoft AD trust for which you want to update target DNS IP Addresses. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `domain` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DOMAIN`
     ID of the domain or fully qualified identifier for the domain. 

To set the `domain` attribute: 

  * provide the argument `domain` on the command line. 


REQUIRED FLAGS
    

`--target-dns-ip-addresses`=[`TARGET_DNS_IP_ADDRESSES`,…]
     DNS server IP addresses that can resolve the target domain. 

Only IPv4 is supported. 

`--target-domain-name`=`TARGET_DOMAIN_NAME`
     Target domain name for the Managed Microsoft AD trust you want to update. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedidentities/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-microsoft-ad/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha active-directory domains trusts update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/trusts/update)
    
    
    [gcloud beta active-directory domains trusts update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/trusts/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
