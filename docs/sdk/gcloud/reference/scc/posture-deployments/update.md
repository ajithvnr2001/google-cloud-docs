---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update/
title: gcloud scc posture-deployments update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:41:53.549887+00:00
---

# gcloud scc posture-deployments update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc posture-deployments update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc posture-deployments update - update the given Cloud Security Command Center posture deployment 
SYNOPSIS
    

`gcloud scc posture-deployments update` (`POSTURE_DEPLOYMENT` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--update-mask`=`UPDATE_MASK`] [`--posture-id`=`POSTURE_ID` `--posture-revision-id`=`POSTURE_REVISION_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Cloud Security Command Center (SCC) posture deployment. 

Fields specified in update-mask flag are updated. Updatable fields are description and posture_name with posture_revision-id. The target_resource for a posture deployment cannot be updated. The posture deployment to be updated should be in ACTIVE State. An empty or "`" update-mask implies that posture-id and posture-revision-id are to be updated. If posture details of posture deployment need to be updated, then the desired posture needs to be in ACTIVE state. LRO operation ID is returned as the response of the command. `

EXAMPLES
     Update the description of the posture deployment named `foo-posture-deployment` in the organization `organizations/123/locations/global`:
    
    
    gcloud scc posture-deployments update organizations/123/locations/global/postureDeployments/foo-posture-deployment --update-mask=description --description="updated-description"

Update posture deployment named `foo-posture-deployment` with the posture named `foo-posture` and revision_id `abcdefgh` in the organization `organizations/123/locations/global`:
    
    
    gcloud scc posture-deployments update organizations/123/locations/global/postureDeployments/foo-posture-deployment --update-mask=posture_id,posture_revision-id --posture-id=foo-posture --posture-revision-id=abcdefgh
    
    
    Update posture deployment named `foo-posture-deployment` with the posture named `foo-posture` and revision_id `abcdefgh` in the organization `organizations/123/locations/global`:
    gcloud scc posture-deployments update organizations/123/locations/global/postureDeployments/foo-posture-deployment --posture-id=foo-posture --posture-revision-id=abcdefgh

POSITIONAL ARGUMENTS
    

Posture deployment resource - The posture deployment to update. For example organizations/<organizationID>/locations/<location>/postureDeployments/<postureDeploymentID>. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`POSTURE_DEPLOYMENT`
     ID of the posture_deployment or fully qualified identifier for the posture_deployment. 

To set the `posture_deployment` attribute: 

  * provide the argument `posture_deployment` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     ID of the location where the resource exists (for example, global). To set the `location` attribute: 

  * provide the argument `posture_deployment` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     ID of the organization which is the parent of the resource. To set the `organization` attribute: 

  * provide the argument `posture_deployment` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Updated description of posture deployment. 
`--etag`=`ETAG`
     Etag is an optional flag. If the provided Etag doesn't match the server generated Etag, the update operation won't proceed. 
`--update-mask`=`UPDATE_MASK`
     Comma-separated string containing list of fields to be updated. 
`--posture-id`=`POSTURE_ID`
     Relative name of the posture to be updated, like `organizations/<organizationID>/locations/<location>/postures/<postureID>`. 
`--posture-revision-id`=`POSTURE_REVISION_ID`
     Revision ID of the posture to be updated. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securityposture/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc posture-deployments update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/posture-deployments/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
