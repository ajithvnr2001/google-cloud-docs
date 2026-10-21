---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/describe/
title: gcloud network-management vpc-flow-logs-configs describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:53.969009+00:00
---

# gcloud network-management vpc-flow-logs-configs describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-management vpc-flow-logs-configs describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-management vpc-flow-logs-configs describe - describe the details of a specific VPC Flow Logs configuration 
SYNOPSIS
    

`gcloud network-management vpc-flow-logs-configs describe` (`VPC_FLOW_LOGS_CONFIG` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describes the details of a specific VPC Flow Logs configuration. 
EXAMPLES
     To get the details of a VPC Flow Logs configuration `my-config`, within the organization `my-org-number`, run: 
    
    
    gcloud network-management vpc-flow-logs-configs describe my-config --location=global --organization=<my-org-number>

To get the details of a VPC Flow Logs configuration `my-config`, run: 
    
    
    gcloud network-management vpc-flow-logs-configs describe my-config --location=global

POSITIONAL ARGUMENTS
    

VpcFlowLogsConfig resource - The resource name of the VpcFlowLogsConfig, in one of the following formats: 

  * For project-level resources: `projects/{project_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}`


  * For organization-level resources: `organizations/{organization_id}/locations/global/vpcFlowLogsConfigs/{vpc_flow_logs_config_id}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 



To set the `project` attribute: 

  * provide the argument `vpc_flow_logs_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [networkmanagement.organizations.locations.vpcFlowLogsConfigs, networkmanagement.projects.locations.vpcFlowLogsConfigs]. 



This must be specified. 

`VPC_FLOW_LOGS_CONFIG`
     ID of the vpcFlowLogsConfig or fully qualified identifier for the vpcFlowLogsConfig. 

To set the `vpc_flow_logs_config` attribute: 

  * provide the argument `vpc_flow_logs_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the vpcFlowLogsConfig resource. 

To set the `location` attribute: 

  * provide the argument `vpc_flow_logs_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The organization id of the vpcFlowLogsConfig resource. 

To set the `organization` attribute: 

  * provide the argument `vpc_flow_logs_config` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [networkmanagement.organizations.locations.vpcFlowLogsConfigs]. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkmanagement/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/>
NOTES
     This variant is also available: 
    
    
    [gcloud beta network-management vpc-flow-logs-configs describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-management/vpc-flow-logs-configs/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
