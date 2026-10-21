---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/framework-deployments/create/
title: gcloud compliance-manager framework-deployments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:28:54.954447+00:00
---

# gcloud compliance-manager framework-deployments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compliance-manager/framework-deployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compliance-manager framework-deployments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compliance-manager framework-deployments create - create a framework deployment 
SYNOPSIS
    

`gcloud compliance-manager framework-deployments create` `FRAMEWORK_DEPLOYMENT` `--cloud-control-metadata`=[`cloudControlDetails`=`CLOUDCONTROLDETAILS`],[`enforcementMode`=`ENFORCEMENTMODE`] (`--framework`=`FRAMEWORK` : `--framework-major-revision-id`=`FRAMEWORK_MAJOR_REVISION_ID`) (`--target-resource-config-existing`=`TARGET_RESOURCE_CONFIG_EXISTING` | `--target-resource-creation-config-folder-display-name`=`TARGET_RESOURCE_CREATION_CONFIG_FOLDER_DISPLAY_NAME` `--target-resource-creation-config-folder-parent`=`TARGET_RESOURCE_CREATION_CONFIG_FOLDER_PARENT` | `--target-resource-creation-config-project-billing-account-id`=`TARGET_RESOURCE_CREATION_CONFIG_PROJECT_BILLING_ACCOUNT_ID` `--target-resource-creation-config-project-display-name`=`TARGET_RESOURCE_CREATION_CONFIG_PROJECT_DISPLAY_NAME` `--target-resource-creation-config-project-parent`=`TARGET_RESOURCE_CREATION_CONFIG_PROJECT_PARENT`) [`--async`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--location`=`LOCATION`] [`--organization`=`ORGANIZATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a framework deployment for a given project or organization and location. 
EXAMPLES
     To create a framework deployment `my-framework-deployment-id` in organization `my-organization-id` and location `global`, targeting `folders/my-folder-id` and using framework `my-framework-name`, run: 
    
    
    gcloud compliance-manager framework-deployments create my-framework-deployment-id --organization=my-organization-id --location=global --target-resource-config-existing=folders/my-folder-id --framework='organizations/my-organization-id/locations/global/frameworks/my-framework-name' --framework-major-revision-id='1' --cloud-control-metadata='[{"cloudControlDetails": {"name":
     "organizations/my-organization-id/locations/global/cloudControls/my\
    -control-1", "majorRevisionId": "1", "parameters": []},
     "enforcementMode": "DETECTIVE"}]'

To create a framework deployment `my-framework-deployment-id` in project `my-project-number` and location `global`, targeting `projects/my-project-number` and using framework `my-framework-name`, run: 
    
    
    gcloud compliance-manager framework-deployments create my-framework-deployment-id --project=my-project-number --location=global --target-resource-config-existing=projects/my-project-number --framework='projects/my-project-number/locations/global/frameworks/my-framework-name' --framework-major-revision-id='1' --cloud-control-metadata='[{"cloudControlDetails": {"name":
     "projects/my-project-number/locations/global/cloudControls/my-contr\
    ol-1", "majorRevisionId": "1", "parameters": []},
     "enforcementMode": "DETECTIVE"}]'

POSITIONAL ARGUMENTS
    

FrameworkDeployment resource - Identifier. The name of the framework deployment, in the format `organizations/{organization}/locations/{location}/frameworkDeployments/{framework_deployment}` or `projects/{project}/locations/{location}/frameworkDeployments/{framework_deployment}`. The only supported location is `global`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `organization` attribute: 

  * provide the argument `framework_deployment` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 



To set the `project` attribute: 

  * provide the argument `framework_deployment` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `framework_deployment` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. This resource can be one of the following types: [cloudsecuritycompliance.organizations.locations.frameworkDeployments, cloudsecuritycompliance.projects.locations.frameworkDeployments]. 



This must be specified. 

`FRAMEWORK_DEPLOYMENT`
     ID of the frameworkDeployment or fully qualified identifier for the frameworkDeployment. 

To set the `framework_deployment` attribute: 

  * provide the argument `framework_deployment` on the command line. 


REQUIRED FLAGS
    

`--cloud-control-metadata`=[`cloudControlDetails`=`CLOUDCONTROLDETAILS`],[`enforcementMode`=`ENFORCEMENTMODE`]
     Required, The deployment mode and parameters for each of the cloud controls in the framework. Every cloud control in the framework includes metadata. 

`cloudControlDetails`
     The cloud control name and parameters. 

`majorRevisionId`
     The major version of the cloud control. 
`name`
     The name of the cloud control, in one of the following formats: `organizations/{organization}/locations/{location}/cloudControls/{cloud_control}` or `projects/{project}/locations/{location}/cloudControls/{cloud_control}`. 

The only supported location is `global`. 

`parameters`
     Parameters are key-value pairs that let you provide your custom location requirements, environment requirements, or other settings that are relevant to the cloud control. An example parameter is `{"name": "location","value": "us-west-1"}`. 

`name`
     The name or key of the parameter. 
`enforcementMode`
     The enforcement mode of the cloud control. 
`Shorthand Example:`
    
    
    --cloud-control-metadata=cloudControlDetails={majorRevisionId=int,name=string,parameters=[{name=string}]},enforcementMode=string --cloud-control-metadata=cloudControlDetails={majorRevisionId=int,name=string,parameters=[{name=string}]},enforcementMode=string

`JSON Example:`
    
    
    --cloud-control-metadata='[{"cloudControlDetails": {"majorRevisionId": int, "name": "string", "parameters": [{"name": "string"}]}, "enforcementMode": "string"}]'

`File Example:`
    
    
    --cloud-control-metadata=path_to_file.(yaml|json)

The reference of a framework, in one of the following formats: 

  * `organizations/{organization}/locations/{location}/frameworks/{framework}`
  * `projects/{project}/locations/{location}/frameworks/{framework}`. 



The only supported location is `global`. 

This must be specified. 

Framework resource - The major version of the framework. If not specified, the version corresponds to the latest version of the framework. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `organization` attribute: 

  * provide the argument `--framework` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 



To set the `project` attribute: 

  * provide the argument `--framework` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--framework` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. This resource can be one of the following types: [cloudsecuritycompliance.organizations.locations.frameworks, cloudsecuritycompliance.projects.locations.frameworks]. 



This must be specified. 

`--framework`=`FRAMEWORK`
     ID of the framework or fully qualified identifier for the framework. 

To set the `framework` attribute: 

  * provide the argument `--framework` on the command line. 


Arguments for the major revision id. 
`--framework-major-revision-id`=`FRAMEWORK_MAJOR_REVISION_ID`
     The major version of the framework. If not specified, the version corresponds to the latest version of the framework. 
The name of the target resource or the configuration that's required to create a new target resource. 

This must be specified. 

Arguments for the resource config. 

At most one of these can be specified: 

`--target-resource-config-existing`=`TARGET_RESOURCE_CONFIG_EXISTING`
     The resource hierarchy node, in one of the following formats: 

  * `organizations/{organizationID}`
  * `folders/{folderID}`
  * `projects/{projectID}`


Or at least one of these can be specified: 

The configuration that's required to create a target resource. 
Arguments for the resource creation config. 

At most one of these can be specified: 

The configuration that's required to create a folder to be used as the target resource for a deployment. 
`--target-resource-creation-config-folder-display-name`=`TARGET_RESOURCE_CREATION_CONFIG_FOLDER_DISPLAY_NAME`
     The display name of the folder. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--target-resource-creation-config-folder-parent`=`TARGET_RESOURCE_CREATION_CONFIG_FOLDER_PARENT`
     The parent of the folder, in the format `organizations/{organizationID}` or `folders/{folderID}`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

The configuration that's required to create a project to be used as the target resource of a deployment. 
`--target-resource-creation-config-project-billing-account-id`=`TARGET_RESOURCE_CREATION_CONFIG_PROJECT_BILLING_ACCOUNT_ID`
     The billing account ID for the project. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--target-resource-creation-config-project-display-name`=`TARGET_RESOURCE_CREATION_CONFIG_PROJECT_DISPLAY_NAME`
     The display name of the project. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--target-resource-creation-config-project-parent`=`TARGET_RESOURCE_CREATION_CONFIG_PROJECT_PARENT`
     The parent of the project, in the format `organizations/{organizationID}` or `folders/{folderID}`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A user-provided description of the framework deployment. 
`--etag`=`ETAG`
     To prevent concurrent updates from overwriting each other, always provide the `etag` when you update a framework deployment. You can also provide the `etag` when you delete a framework deployment, to help ensure that you're deleting the intended version of the framework deployment. 
`--location`=`LOCATION`
     For resources [framework, framework_deployment], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--organization`=`ORGANIZATION`
     For resources [framework, framework_deployment], provides fallback value for resource organization attribute. When the resource's full URI path is not provided, organization will fallback to this flag value. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudsecuritycompliance/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center#compliance-management>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
