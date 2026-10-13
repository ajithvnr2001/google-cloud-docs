---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/remediation-intents/delete/
title: gcloud alpha scc remediation-intents delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:27.588617+00:00
---

# gcloud alpha scc remediation-intents delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/remediation-intents/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc remediation-intents delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc remediation-intents delete - deletes a remediation intent resource 
SYNOPSIS
    

`gcloud alpha scc remediation-intents delete` (`REMEDIATIONINTENT` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--async`] [`--etag`=`ETAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Deletes a Cloud Security Command Center (SCC) RemediationIntent resource. 
EXAMPLES
     Sample usage: Delete a remediation intent resource of name organizations/123456789/locations/global/remediationIntents/123: $ {command} scc remediation-intents delete \
    
    
    organizations/123456789/locations/global/remediationIntents/123

POSITIONAL ARGUMENTS
    

RemediationIntent resource - The remediation intent resource. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`REMEDIATIONINTENT`
     ID of the remediationIntent or fully qualified identifier for the remediationIntent. 

To set the `remediation-intent` attribute: 

  * provide the argument `remediationintent` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Google Cloud location for the remediationIntent. 

To set the `location` attribute: 

  * provide the argument `remediationintent` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The Google Cloud organization for the remediationIntent. 

To set the `organization` attribute: 

  * provide the argument `remediationintent` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `False`. 
`--etag`=`ETAG`
     Etag is an optional flag. If the provided Etag doesn't match the server generated Etag, the operation won't proceed. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
