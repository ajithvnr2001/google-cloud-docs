---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/update/
title: gcloud beta iam workforce-pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:53.660311+00:00
---

# gcloud beta iam workforce-pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam workforce-pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam workforce-pools update - update a workforce pool 
SYNOPSIS
    

`gcloud beta iam workforce-pools update` (`WORKFORCE_POOL` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--disable-programmatic-signin`] [`--disabled`] [`--display-name`=`DISPLAY_NAME`] [`--session-duration`=`SESSION_DURATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a workforce pool. 
EXAMPLES
     The following command updates a workforce pool with ID ``my-workforce-pool`` with explicit values for all required and optional parameters: 
    
    
    gcloud beta iam workforce-pools update my-workforce-pool --location=global --display-name="My Workforce Pool" --description="My workforce pool description." --session-duration="7200s" --disabled

POSITIONAL ARGUMENTS
    

Workforce pool resource - The workforce pool to update. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`WORKFORCE_POOL`
     ID of the workforce pool or fully qualified identifier for the workforce pool. 

To set the `workforce_pool` attribute: 

  * provide the argument `workforce_pool` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the workforce pool. 

To set the `location` attribute: 

  * provide the argument `workforce_pool` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A description for the workforce pool. Cannot exceed 256 characters in length. 
`--disable-programmatic-signin`
     Disables the programmatic sign-in for workforce pool users. Specify `--no-disable-security-token-exchange` to enable programmatic sign-in. For more information, refer to Obtain short-lived tokens for workforce identity federation at <https://cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials>
`--disabled`
     Disables the workforce pool. You cannot use a disabled workforce pool to perform new token exchanges or sign-ins using any provider in the workforce pool. Specify `--no-disabled` to enable a disabled pool. 
`--display-name`=`DISPLAY_NAME`
     A display name for the workforce pool. Cannot exceed 32 characters in length. 
`--session-duration`=`SESSION_DURATION`
     How long the Google Cloud access tokens, console sign-in sessions, and gcloud sign-in sessions from this workforce pool are valid. Must be greater than 15 minutes (900s) and less than 12 hours (43200s). If not configured, minted credentials will have a default duration of one hour (3600s). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iam workforce-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/update)
    
    
    [gcloud alpha iam workforce-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
