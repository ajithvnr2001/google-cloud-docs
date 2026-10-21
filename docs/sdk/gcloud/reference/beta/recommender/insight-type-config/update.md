---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/insight-type-config/update/
title: gcloud beta recommender insight-type-config update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:23:37.591276+00:00
---

# gcloud beta recommender insight-type-config update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/insight-type-config/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta recommender insight-type-config update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta recommender insight-type-config update - update an insight type configuration 
SYNOPSIS
    

`gcloud beta recommender insight-type-config update` `INSIGHT_TYPE` `--etag`=`ETAG` `--location`=`LOCATION` (`--billing-account`=`BILLING_ACCOUNT` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`--annotations`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]] [`--config-file`=`CONFIG_FILE`] [`--display-name`=`DISPLAY_NAME`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an insight type configuration based on a given entity (project, organization, billing account), location, and insight type. 
EXAMPLES
     To update an insight type configuration, run: 
    
    
    gcloud beta recommender insight-type-config update ${INSIGHT_TYPE} --project=${PROJECT} --location=${LOCATION} --etag=\"123\" --config-file=config.yaml

POSITIONAL ARGUMENTS
    

`INSIGHT_TYPE`
     Insight type to use for this invocation. 
REQUIRED FLAGS
    

`--etag`=`ETAG`
     Etag of the insight type configuration. 
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
OPTIONAL FLAGS
    

`--annotations`=`KEY`=`VALUE`,[`KEY`=`VALUE`,…]
     Store small amounts of arbitrary data on the insight type configuration. 
`--config-file`=`CONFIG_FILE`
     Generation configuration file for the insight type configuration. 
`--display-name`=`DISPLAY_NAME`
     Display name of the insight type configuration. 
`--validate-only`
     If true, validate the request and preview the change, but do not actually update it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud recommender insight-type-config update](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insight-type-config/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
