---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/insight-type-config/describe/
title: gcloud beta recommender insight-type-config describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:23:37.479356+00:00
---

# gcloud beta recommender insight-type-config describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/insight-type-config/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta recommender insight-type-config describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta recommender insight-type-config describe - describe an insight type configuration 
SYNOPSIS
    

`gcloud beta recommender insight-type-config describe` `INSIGHT_TYPE` `--location`=`LOCATION` (`--billing-account`=`BILLING_ACCOUNT` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Describe an insight type configuration based on a given entity (project, organization, billing account), location, and insight type. 
EXAMPLES
     To describe an insight type configuration, run: 
    
    
    gcloud beta recommender insight-type-config describe ${INSIGHT_TYPE} --project=${PROJECT} --location=${LOCATION}

POSITIONAL ARGUMENTS
    

`INSIGHT_TYPE`
     Insight type to use for this invocation. 
REQUIRED FLAGS
    

`--location`=`LOCATION`
     Location to use for this invocation. 
Resource that is associated with cloud entity type. 

Exactly one of these must be specified: 

`--billing-account`=`BILLING_ACCOUNT`
     The Google Cloud billing account ID to use for this invocation. 
`--organization`=`ORGANIZATION_ID`
     The Google Cloud organization ID to use for this invocation. 
`--project`=`PROJECT_ID`
     The Google Cloud project ID. Overrides the default `core/project` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud recommender insight-type-config describe](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
