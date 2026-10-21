---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/delete/
title: gcloud compliance-manager cloud-controls delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:28:58.199017+00:00
---

# gcloud compliance-manager cloud-controls delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/cloud-controls/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compliance-manager cloud-controls delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compliance-manager cloud-controls delete - delete a cloud control 
SYNOPSIS
    

`gcloud compliance-manager cloud-controls delete` (`CLOUD_CONTROL` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete a specific cloud control. 
EXAMPLES
     To delete cloud control `my-cloud-control-id` in organization `my-organization-id` and location `global`, run: 
    
    
    gcloud compliance-manager cloud-controls delete my-cloud-control-id --organization=my-organization-id --location=global

To delete cloud control `my-cloud-control-id` in project `my-project-number` and location `global`, run: 
    
    
    gcloud compliance-manager cloud-controls delete my-cloud-control-id --project=my-project-number --location=global

POSITIONAL ARGUMENTS
    

CloudControl resource - The name of the cloud control to delete, in one of the following formats: `organizations/{organization}/locations/{location}/CloudControls/{CloudControl}` or `projects/{project}/locations/{location}/CloudControls/{CloudControl}`. 

The only supported location is `global`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cloud_control` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [cloudsecuritycompliance.organizations.locations.cloudControls, cloudsecuritycompliance.projects.locations.cloudControls]. 



This must be specified. 

`CLOUD_CONTROL`
     ID of the cloudControl or fully qualified identifier for the cloudControl. 

To set the `cloud_control` attribute: 

  * provide the argument `cloud_control` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the cloudControl resource. 

To set the `location` attribute: 

  * provide the argument `cloud_control` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization id of the cloudControl resource. 

To set the `organization` attribute: 

  * provide the argument `cloud_control` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [cloudsecuritycompliance.organizations.locations.cloudControls]. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudsecuritycompliance/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center#compliance-management>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
