---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create/
title: gcloud scc posture-deployments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:07.324893+00:00
---

# gcloud scc posture-deployments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-deployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc posture-deployments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc posture-deployments create - create a Cloud Security Command Center posture deployment 
SYNOPSIS
    

`gcloud scc posture-deployments create` (`POSTURE_DEPLOYMENT` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) `--posture-name`=`POSTURE_NAME` `--posture-revision-id`=`POSTURE_REVISION_ID` `--target-resource`=`TARGET_RESOURCE` [`--async`] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Cloud Security Command Center (SCC) posture deployment. First argument is the parent of the posture deployment to be created. Second argument is the name of the posture deployment to be created. It is followed by details of the posture to be deployed and the target_resource to be deployed on. 

LRO operation ID is returned as the response of the command. 

EXAMPLES
     Create a posture deployment named `posture-deployment-foo-1` within parent `organizations/123/locations/global` on resource `folders/456` (i.e. a posture-deployment in organization `123`, location `global`, with id `posture-deployment-foo-1`, which deploys posture `organizations/123/locations/foo-posture` with revision-id `foo-posture-revision-id` on `folders/456`): 
    
    
    gcloud scc posture-deployments create organizations/123/locations/global/postureDeployments/posture-deployment-foo-1 --posture-name=organizations/123/locations/global/foo-posture --posture-revision-id=foo-posture-revision-id --target-resource=projects/456

POSITIONAL ARGUMENTS
    

Posture deployment resource - The name of the posture deployment to be created. For example organizations/<organizationID>/locations/<location>/postureDeployments/<postureDeploymentID>. The arguments in this group can be used to specify the attributes of this resource. 

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


REQUIRED FLAGS
    

`--posture-name`=`POSTURE_NAME`
     Posture that needs to be deployed. Format: organizations/<organizationID>/locations/<location>/postures/<postureID>
`--posture-revision-id`=`POSTURE_REVISION_ID`
     Posture revision that needs to be deployed. 
`--target-resource`=`TARGET_RESOURCE`
     Name of the workload on which posture deployment is to be created. It could be an organization, folder or a project. Possible formats: | organizations/<organizationID> | folders/<folderID> | projects/<projectID> The above mentioned IDs need to have numeric format. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     User-provided description of the posture deployment. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `securityposture/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc posture-deployments create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/posture-deployments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
