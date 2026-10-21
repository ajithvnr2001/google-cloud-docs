---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable/
title: gcloud alpha active-directory domains migration enable \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:18.676037+00:00
---

# gcloud alpha active-directory domains migration enable  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/migration/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha active-directory domains migration enable Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha active-directory domains migration enable - enable domain migration permissions on a Managed Microsoft AD domain 
SYNOPSIS
    

`gcloud alpha active-directory domains migration enable` `DOMAIN` `--onprem-domains`=[`ONPREM_DOMAINS`,…] [`--async`] [`--disable-sid-filtering-domains`=[`DISABLE_SID_FILTERING_DOMAINS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Enable domain migration permissions on a Managed Microsoft AD domain. 

This command can fail for the following reasons: 

  * The specified domain doesn't exist. 
  * The specified domain is either being created or updated. 
  * The active account doesn't have permission to enable migration permissions on the specified domain. 


EXAMPLES
     The following command enables migration permissions on the domain `my-domain.com` in project `my-project` for two on-premises domains `onprem-domain-1.com` and `onprem-domain-2.com`, with SID Filtering disabled for `onprem-domain-1.com`. 
    
    
    gcloud alpha active-directory domains migration enable my-domain.com --onprem-domains=onprem-domain-1.com,onprem-domain-2.com --disable-sid-filtering-domains=onprem-domain-1.com --project=my-project --async

POSITIONAL ARGUMENTS
    

Domain resource - Name of the Managed Microsoft AD domain on which you want to enable migration permissions. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--onprem-domains`=[`ONPREM_DOMAINS`,…]
     List of trusted domains that are being migrated. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--disable-sid-filtering-domains`=[`DISABLE_SID_FILTERING_DOMAINS`,…]
     List of migrating domains on which SID Filtering must be disabled. The list is empty by default. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedidentities/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-microsoft-ad/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta active-directory domains migration enable](https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/migration/enable)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
