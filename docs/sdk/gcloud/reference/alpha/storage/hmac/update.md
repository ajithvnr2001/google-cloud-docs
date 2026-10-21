---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/hmac/update/
title: gcloud alpha storage hmac update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:43.194988+00:00
---

# gcloud alpha storage hmac update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/hmac/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage hmac update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage hmac update - change the status of a service account HMAC 
SYNOPSIS
    

`gcloud alpha storage hmac update` `ACCESS_ID` (`--activate` | `--deactivate`) [`--etag`=`ETAG`, `-e` `ETAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha storage hmac update` sets the state of the specified key. Valid state arguments are ``ACTIVE`` and ``INACTIVE``. To set a key to state ``DELETED``, use `[gcloud alpha storage hmac delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/hmac/delete)` on an ``INACTIVE`` key. If an etag is set in the command, it will only succeed if the provided etag matches the etag of the stored key. 
EXAMPLES
     To activate an HMAC key: 
    
    
    gcloud alpha storage hmac update GOOG56JBMFZX6PMPTQ62VD2 --activate

To set the state of an HMAC key to ``INACTIVE`` provided its etag is ``M42da=``: 
    
    
    gcloud alpha storage hmac update GOOG56JBMFZX6PMPTQ62VD2 --deactivate --etag=M42da=

POSITIONAL ARGUMENTS
    

`ACCESS_ID`
     Access ID for HMAC key to update. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--activate`
     Sets the state of the specified key to ``ACTIVE``. 
`--deactivate`
     Sets the state of the specified key to ``INACTIVE``. 
OPTIONAL FLAGS
    

`--etag`=`ETAG`, `-e` `ETAG`
     If provided, the update will only be performed if the specified etag matches the etag of the stored key. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud storage hmac update](https://docs.cloud.google.com/sdk/gcloud/reference/storage/hmac/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
