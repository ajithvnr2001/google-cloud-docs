---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/custom-modules/etd/get/
title: gcloud alpha scc custom-modules etd get \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:12.525590+00:00
---

# gcloud alpha scc custom-modules etd get  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/custom-modules/etd/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc custom-modules etd get Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc custom-modules etd get - get the details of an Event Threat Detection custom module 
SYNOPSIS
    

`gcloud alpha scc custom-modules etd get` `CUSTOM_MODULE` [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Get the details of an Event Threat Detection custom module. It does not resolve `INHERITED` enablement states to `ENABLED` or `DISABLED` for modules created at ancestor levels. For example, if the module is enabled at the ancestor level, modules for all child resources will have the enablement state set to `INHERITED`. Use `[gcloud alpha scc custom-modules etd get-effective](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/custom-modules/etd/get-effective)` to retrieve a custom module with its effective enablement state. 
EXAMPLES
     To get the details of an Event Threat Detection custom module with ID `123456` for organization `123`, run: 
    
    
    gcloud alpha scc custom-modules etd get 123456 --organization=organizations/123

To get the details of an Event Threat Detection custom module with ID `123456` for folder `456`, run: 
    
    
    gcloud alpha scc custom-modules etd get 123456 --folder=folders/456

To get the details of an Event Threat Detection custom module with ID `123456` for project `789`, run: 
    
    
    gcloud alpha scc custom-modules etd get 123456 --project=projects/789

POSITIONAL ARGUMENTS
    

`CUSTOM_MODULE`
     ID or the full resource name of the Event Threat Detection custom module. If you specify the full resource name, you do not need to specify the --organization, \--folder, or --project flags. 
FLAGS
    

At most one of these can be specified: 

`--folder`=`FOLDER`
     Folder from which to get the custom module details. Formatted as `folders/456` or just `456`. 
`--organization`=`ORGANIZATION`
     Organization from which to get the custom module details. Formatted as `organizations/123` or just `123`. 
`--project`=`PROJECT`
     ID or number of the project from which to get the custom module details. Formatted as `projects/789` or just `789`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securitycenter/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
