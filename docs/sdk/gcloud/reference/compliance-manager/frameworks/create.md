---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/frameworks/create/
title: gcloud compliance-manager frameworks create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:28:56.114633+00:00
---

# gcloud compliance-manager frameworks create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/frameworks/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compliance-manager frameworks create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compliance-manager frameworks create - create a framework 
SYNOPSIS
    

`gcloud compliance-manager frameworks create` (`FRAMEWORK` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`--category`=[`CATEGORY`,…]] [`--cloud-control-details`=[`majorRevisionId`=`MAJORREVISIONID`],[`name`=`NAME`],[`parameters`=`PARAMETERS`]] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a framework for a given organization and location. 
EXAMPLES
     To create a framework `my-framework-id` in organization `my-organization-id` and location `global`, run: 
    
    
    gcloud compliance-manager frameworks create my-framework-id --organization=my-organization-id --location=global --description="My framework description" --display-name="My framework display name" --controls='[{"name":
     "organizations/my-organization-id/locations/global/cloudControls/my\
    -control-1", "majorRevisionId": "1", "parameters": []}]' \

To create a framework `my-framework-id` in project `my-project-number` and location `global`, run: 
    
    
    gcloud compliance-manager frameworks create my-framework-id --project=my-project-number --location=global --description="My framework description" --display-name="My framework display name" --controls='[{"name":
     "projects/my-project-number/locations/global/cloudControls/my-contr\
    ol-1", "majorRevisionId": "1", "parameters": []}]' \

POSITIONAL ARGUMENTS
    

Framework resource - Identifier. The name of the framework, in one of the following formats: `organizations/{organization}/locations/{location}/frameworks/{framework}` or `projects/{project}/locations/{location}/frameworks/{framework}`. 

The only supported location is `global`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `framework` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [cloudsecuritycompliance.organizations.locations.frameworks, cloudsecuritycompliance.projects.locations.frameworks]. 



This must be specified. 

`FRAMEWORK`
     ID of the framework or fully qualified identifier for the framework. 

To set the `framework` attribute: 

  * provide the argument `framework` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the framework resource. 

To set the `location` attribute: 

  * provide the argument `framework` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization id of the framework resource. 

To set the `organization` attribute: 

  * provide the argument `framework` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [cloudsecuritycompliance.organizations.locations.frameworks]. 


FLAGS
    

`--category`=[`CATEGORY`,…]
     The category of the framework. `CATEGORY` must be one of: 

`assured-workloads`
     An Assured Workloads framework. 
`custom-framework`
     A user-created framework. 
`data-security`
     A data security posture framework. 
`google-best-practices`
     A Google's best practices framework. 
`industry-defined-standard`
     An industry-defined framework. 
`--cloud-control-details`=[`majorRevisionId`=`MAJORREVISIONID`],[`name`=`NAME`],[`parameters`=`PARAMETERS`]
     The cloud control details that are directly added without any grouping in the framework. 

`majorRevisionId`
     The major version of the cloud control. 
`name`
     The name of the cloud control, in one of the following formats: `organizations/{organization}/locations/{location}/cloudControls/{cloud_control}` or `projects/{project}/locations/{location}/cloudControls/{cloud_control}`. 

The only supported location is `global`. 

`parameters`
     Parameters are key-value pairs that let you provide your custom location requirements, environment requirements, or other settings that are relevant to the cloud control. An example parameter is `{"name": "location","value": "us-west-1"}`. 

`name`
     The name or key of the parameter. 
`Shorthand Example:`
    
    
    --cloud-control-details=majorRevisionId=int,name=string,parameters=[{name=string}] --cloud-control-details=majorRevisionId=int,name=string,parameters=[{name=string}]

`JSON Example:`
    
    
    --cloud-control-details='[{"majorRevisionId": int, "name": "string", "parameters": [{"name": "string"}]}]'

`File Example:`
    
    
    --cloud-control-details=path_to_file.(yaml|json)

`--description`=`DESCRIPTION`
     The description of the framework. The maximum length is 2000 characters. 
`--display-name`=`DISPLAY_NAME`
     The friendly name of the framework. The maximum length is 200 characters. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudsecuritycompliance/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center#compliance-management>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
