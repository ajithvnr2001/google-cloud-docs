---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/capability-configs/create/
title: gcloud beta resource-manager capability-configs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:27:31.057108+00:00
---

# gcloud beta resource-manager capability-configs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/capability-configs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta resource-manager capability-configs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta resource-manager capability-configs create - create a CapabilityConfig under a parent Organization, Folder, or Project 
SYNOPSIS
    

`gcloud beta resource-manager capability-configs create` (`CAPABILITY_CONFIG` : `--folder`=`FOLDER` `--organization`=`ORGANIZATION` `--project`=`PROJECT`) `--types`=[`TYPES`,…] [`--async`] [`--boundaries`=[`BOUNDARIES`,…]] [`--display-name`=`DISPLAY_NAME`] [`--management-project`=`MANAGEMENT_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Creating a CapabilityConfig triggers the creation of a Management Project if one is not supplied via `--management-project`. 
EXAMPLES
     To create a CapabilityConfig `my-config` with type `app-management` under organization `123456789`: 
    
    
    gcloud beta resource-manager capability-configs create my-config --organization=123456789 --types=app-management

To create a CapabilityConfig with display name and pre-existing management project: 
    
    
    gcloud beta resource-manager capability-configs create my-config --folder=456789012 --types=app-management --display-name="App Hub Config" --management-project=projects/123456789012

POSITIONAL ARGUMENTS
    

Capability config resource - The CapabilityConfig to create. The arguments in this group can be used to specify the attributes of this resource. This resource can be one of the following types: [cloudresourcemanager.organizations.capabilityConfigs, cloudresourcemanager.folders.capabilityConfigs, cloudresourcemanager.projects.capabilityConfigs]. 

This must be specified. 

`CAPABILITY_CONFIG`
     ID of the capability_config or fully qualified identifier for the capability_config. 

To set the `capability_config` attribute: 

  * provide the argument `capability_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     Folder ID or full resource name of the capability_config. 

To set the `folder` attribute: 

  * provide the argument `capability_config` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [cloudresourcemanager.folders.capabilityConfigs]. 


`--organization`=`ORGANIZATION`
     Organization ID or full resource name of the capability_config. 

To set the `organization` attribute: 

  * provide the argument `capability_config` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [cloudresourcemanager.organizations.capabilityConfigs]. 


`--project`=`PROJECT`
     Project number or full resource name of the capability_config. 

To set the `project` attribute: 

  * provide the argument `capability_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line. Must be specified for resource of type [cloudresourcemanager.projects.capabilityConfigs]. 


REQUIRED FLAGS
    

`--types`=[`TYPES`,…]
     Comma-separated list of CapabilityConfig types (e.g. app-management, agent-management). `TYPES` must be one of: `app-management`, `agent-management`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--boundaries`=[`BOUNDARIES`,…]
     List of Boundaries associated with this CapabilityConfig. 
`--display-name`=`DISPLAY_NAME`
     Human-readable display name of the CapabilityConfig (4 to 30 characters). 
`--management-project`=`MANAGEMENT_PROJECT`
     Management Project associated with this CapabilityConfig (e.g. projects/123456789012). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud resource-manager capability-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/capability-configs/create)
    
    
    [gcloud alpha resource-manager capability-configs create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/capability-configs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
