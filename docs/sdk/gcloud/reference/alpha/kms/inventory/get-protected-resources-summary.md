---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/inventory/get-protected-resources-summary/
title: gcloud alpha kms inventory get-protected-resources-summary \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:08:59.915840+00:00
---

# gcloud alpha kms inventory get-protected-resources-summary  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/inventory/get-protected-resources-summary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms inventory get-protected-resources-summary Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms inventory get-protected-resources-summary - gets the protected resources summary 
SYNOPSIS
    

`gcloud alpha kms inventory get-protected-resources-summary` (`--keyname`=`KEYNAME` : `--keyring`=`KEYRING` `--location`=`LOCATION`) [`--fallback-scope`=`FALLBACK_SCOPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha kms inventory get-protected-resources-summary` returns a summary of the resources a key is protecting. 

The summary includes how many projects contain protected resources, how many protected resources there are, what are the types of protected resources, and the count for each type of protected resource. 

EXAMPLES
     To view the summary of protected resources for the key `projects/test-prj/locations/us/keyRings/us-keyring/cryptoKeys/us-key`, run: 
    
    
    gcloud alpha kms inventory get-protected-resources-summary --keyname=projects/test-prj/locations/us/keyRings/us-keyring/cryptoKeys/us-key

REQUIRED FLAGS
    

Key resource - The KMS key resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--keyname` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`--keyname`=`KEYNAME`
     ID of the key or fully qualified identifier for the key. 

To set the `key` attribute: 

  * provide the argument `--keyname` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--keyring`=`KEYRING`
     The KMS keyring of the key. 

To set the `keyring` attribute: 

  * provide the argument `--keyname` on the command line with a fully specified name; 
  * provide the argument `--keyring` on the command line. 


`--location`=`LOCATION`
     The Google Cloud location for the key. 

To set the `location` attribute: 

  * provide the argument `--keyname` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


OPTIONAL FLAGS
    

`--fallback-scope`=`FALLBACK_SCOPE`
     If permission is denied at the organization level, fall back to the project level scope. `FALLBACK_SCOPE` must be one of: `FALLBACK_SCOPE_UNSPECIFIED`, `FALLBACK_SCOPE_PROJECT`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms inventory get-protected-resources-summary](https://docs.cloud.google.com/sdk/gcloud/reference/kms/inventory/get-protected-resources-summary)
    
    
    [gcloud beta kms inventory get-protected-resources-summary](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/inventory/get-protected-resources-summary)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
