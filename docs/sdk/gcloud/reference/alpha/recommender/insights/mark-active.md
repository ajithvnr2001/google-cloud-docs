---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recommender/insights/mark-active/
title: gcloud alpha recommender insights mark-active \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:25:20.597549+00:00
---

# gcloud alpha recommender insights mark-active  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/recommender/insights/mark-active/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha recommender insights mark-active Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha recommender insights mark-active - mark an insight's state as ACTIVE 
SYNOPSIS
    

`gcloud alpha recommender insights mark-active` `INSIGHT` `--etag`=`etag` `--insight-type`=`INSIGHT_TYPE` `--location`=`LOCATION` (`--billing-account`=`BILLING_ACCOUNT` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Mark an insight's state as ACTIVE. Can be applied to insights in DISMISSED state. The following are currently supported: project, billing_account, folder, and organization. 
EXAMPLES
     To mark an insight as ACTIVE: 
    
    
    gcloud alpha recommender insights mark-active abcd-1234 --project=project-id --location=global --insight-type=google.compute.firewall.Insight --etag=abc123

POSITIONAL ARGUMENTS
    

`INSIGHT`
     Insight id which will be marked as active 
REQUIRED FLAGS
    

`--etag`=`etag`
     Etag of a insight 
`--insight-type`=`INSIGHT_TYPE`
     Insight Type of the insights 
`--location`=`LOCATION`
     Location 
Resource that is associated with cloud entity type. Currently four mutually exclusive flags are supported, --project, --billing-account, --folder, \--organization. 

Exactly one of these must be specified: 

`--billing-account`=`BILLING_ACCOUNT`
     The Google Cloud Platform billing account ID to use for this invocation. 
`--folder`=`FOLDER_ID`
     The Google Cloud Platform folder ID to use for this invocation. 
`--organization`=`ORGANIZATION_ID`
     The Google Cloud Platform organization ID to use for this invocation. 
`--project`=`PROJECT_ID`
     The Google Cloud Platform project ID. Overrides the default `core/project` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
