---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/operations/describe/
title: gcloud alpha scc operations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:22.135049+00:00
---

# gcloud alpha scc operations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/operations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc operations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc operations describe - describe a Cloud SCC's long running scan operation 
SYNOPSIS
    

`gcloud alpha scc operations describe` (`OPERATION` : `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describe a Cloud SCC's long running scan operation. 
EXAMPLES
     Return long running scan operation status for operation id (9c5fa5e5-e368-439a-baa4-08c17b77ec23) and organization 123456. Operation id is obtained using run-discovery command: 
    
    
    gcloud alpha scc operations describe 9c5fa5e5-e368-439a-baa4-08c17b77ec23 --organization=123456

POSITIONAL ARGUMENTS
    

Operation resource - Cloud SCC's API operation to describe. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`OPERATION`
     ID of the operation or fully qualified identifier for the operation. 

To set the `operation` attribute: 

  * provide the argument `operation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     (Optional) If the full resource name isn't provided e.g. organizations/123, then provide the organization id which is the suffix of the organization. Example: organizations/123, the id is 123. To set the `organization` attribute: 

  * provide the argument `operation` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * Set the organization property in configuration using `gcloud config set scc/organization` if it is not specified in command line.. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securitycenter/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud scc operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/scc/operations/describe)
    
    
    [gcloud beta scc operations describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/operations/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
