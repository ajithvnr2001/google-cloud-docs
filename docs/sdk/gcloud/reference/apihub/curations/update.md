---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apihub/curations/update/
title: gcloud apihub curations update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:49:27.078575+00:00
---

# gcloud apihub curations update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apihub/curations/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apihub curations update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apihub curations update - update a Curation 
SYNOPSIS
    

`gcloud apihub curations update` (`CURATION` : `--location`=`LOCATION`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--clear-endpoint` `--application-integration-endpoint-details-trigger-id`=`APPLICATION_INTEGRATION_ENDPOINT_DETAILS_TRIGGER_ID` `--application-integration-endpoint-details-uri`=`APPLICATION_INTEGRATION_ENDPOINT_DETAILS_URI`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a curation 
EXAMPLES
     To update a curation with the ID `my-curation`, run: 
    
    
    gcloud apihub curations update my-curation --display-name="New Curation Name" --project=my-project --location=us-central1

POSITIONAL ARGUMENTS
    

Curation resource - Identifier. The name of the curation. 

Format: `projects/{project}/locations/{location}/curations/{curation}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `curation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CURATION`
     ID of the curation or fully qualified identifier for the curation. 

To set the `curation` attribute: 

  * provide the argument `curation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the curation resource. 

To set the `location` attribute: 

  * provide the argument `curation` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     The description of the curation. 
`--display-name`=`DISPLAY_NAME`
     The display name of the curation. 
The endpoint to be triggered for curation. The endpoint will be invoked with a request payload containing [ApiMetadata][google.cloud.apihub.v1.ApiHub.ApiMetadata]. Response should contain curated data in the form of [ApiMetadata][google.cloud.apihub.v1.ApiHub.ApiMetadata]. 
`--clear-endpoint`
     Set googleCloudApihubV1Curation.endpoint back to default value. 
Arguments for the endpoint details. 
The details of the Application Integration endpoint to be triggered for curation. 
`--application-integration-endpoint-details-trigger-id`=`APPLICATION_INTEGRATION_ENDPOINT_DETAILS_TRIGGER_ID`
     The API trigger ID of the Application Integration workflow. 
`--application-integration-endpoint-details-uri`=`APPLICATION_INTEGRATION_ENDPOINT_DETAILS_URI`
     The endpoint URI should be a valid REST URI for triggering an Application Integration. Format: `https://integrations.googleapis.com/v1/{name=projects/*/locations/*/integrations/*}:execute` or `https://{location}-integrations.googleapis.com/v1/{name=projects/*/locations/*/integrations/*}:execute`
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `apihub/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/apigee/docs/api-hub/what-is-api-hub>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha apihub curations update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apihub/curations/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
