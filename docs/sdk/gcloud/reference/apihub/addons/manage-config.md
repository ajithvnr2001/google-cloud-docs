---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apihub/addons/manage-config/
title: gcloud apihub addons manage-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:49:22.552424+00:00
---

# gcloud apihub addons manage-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apihub/addons/manage-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apihub addons manage-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apihub addons manage-config - manage the Config of an Addon 
SYNOPSIS
    

`gcloud apihub addons manage-config` (`ADDON` : `--location`=`LOCATION`) [`--async`] [`--[no-]all-data-addon-config-enabled` | `--gateway-plugin-addon-config-configs`=[`apigeeEdgeConfig`=`APIGEEEDGECONFIG`],[`apigeeOpdkConfig`=`APIGEEOPDKCONFIG`],[`apigeeXHybridConfig`=`APIGEEXHYBRIDCONFIG`],[`pluginInstance`=`PLUGININSTANCE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Manage the config of an addon 
EXAMPLES
     To manage the config of an addon with the ID `system-advanced-api-security`, run: 
    
    
    gcloud apihub addons manage-config system-advanced-api-security --gateway-plugin-addon-config-configs="pluginInstance=projects/my-project/locations/us-central1/plugins/system-apigee-x-and-hybrid/instances/my-instance-1,apigeeXHybridConfig={environmentFilter={allEnvironments=true}}" --gateway-plugin-addon-config-configs="pluginInstance=projects/my-project/locations/us-central1/plugins/system-edge-public-cloud/instances/my-instance-2,apigeeEdgeConfig={environmentFilter={environments=['env1']}}" --project=my-project --location=us-central1

POSITIONAL ARGUMENTS
    

Addon resource - The name of the addon for which the config is to be managed. Format: `projects/{project}/locations/{location}/addons/{addon}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `addon` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ADDON`
     ID of the addon or fully qualified identifier for the addon. 

To set the `addon` attribute: 

  * provide the argument `addon` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the addon resource. 

To set the `location` attribute: 

  * provide the argument `addon` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Arguments for the config. 

At most one of these can be specified: 

Configuration for addons which act on all data in the API hub. This is used to specify if the addon is enabled for all data in the API hub. 
`--[no-]all-data-addon-config-enabled`
     If true, the addon is enabled for all data in the API hub. Use `--all-data-addon-config-enabled` to enable and `--no-all-data-addon-config-enabled` to disable. 
Configuration for gateway plugin addons. This is used to specify the list of gateway plugin configs for which the addon is enabled. 
`--gateway-plugin-addon-config-configs`=[`apigeeEdgeConfig`=`APIGEEEDGECONFIG`],[`apigeeOpdkConfig`=`APIGEEOPDKCONFIG`],[`apigeeXHybridConfig`=`APIGEEXHYBRIDCONFIG`],[`pluginInstance`=`PLUGININSTANCE`]
     Required, The list of gateway plugin configs for which the addon is enabled. Each gateway plugin config should have a unique plugin instance. 

`apigeeEdgeConfig`
     Configuration for Apigee Edge gateways. 

`environmentFilter`
     The filter to apply on the resources managed by the gateway plugin instance. If provided this filter applies environment specific filtering. 

`allEnvironments`
     Indicates if this filter should match all environments or only a subset of environments. If set to true, all environments are matched. 
`environments`
     If provided, only environments in this list are matched. This field is ignored if `all_environments` is true. 
`apigeeOpdkConfig`
     Configuration for Apigee OPDK gateways. 

`environmentFilter`
     The filter to apply on the resources managed by the gateway plugin instance. If provided this filter applies environment specific filtering. 

`allEnvironments`
     Indicates if this filter should match all environments or only a subset of environments. If set to true, all environments are matched. 
`environments`
     If provided, only environments in this list are matched. This field is ignored if `all_environments` is true. 
`apigeeXHybridConfig`
     Configuration for Apigee X and Apigee Hybrid gateways. 

`environmentFilter`
     The filter to apply on the resources managed by the gateway plugin instance. If provided this filter applies environment specific filtering. 

`allEnvironments`
     Indicates if this filter should match all environments or only a subset of environments. If set to true, all environments are matched. 
`environments`
     If provided, only environments in this list are matched. This field is ignored if `all_environments` is true. 
`pluginInstance`
     The name of the gateway plugin instance for which the config is to be specified. Format: projects/{project}/locations/{location}/plugins/{plugin}/pluginInstances/{plugin_instance}. 
`Shorthand Example:`
    
    
    --gateway-plugin-addon-config-configs=apigeeEdgeConfig={environmentFilter={allEnvironments=boolean,environments=[string]}},apigeeOpdkConfig={environmentFilter={allEnvironments=boolean,environments=[string]}},apigeeXHybridConfig={environmentFilter={allEnvironments=boolean,environments=[string]}},pluginInstance=string --gateway-plugin-addon-config-configs=apigeeEdgeConfig={environmentFilter={allEnvironments=boolean,environments=[string]}},apigeeOpdkConfig={environmentFilter={allEnvironments=boolean,environments=[string]}},apigeeXHybridConfig={environmentFilter={allEnvironments=boolean,environments=[string]}},pluginInstance=string

`JSON Example:`
    
    
    --gateway-plugin-addon-config-configs='[{"apigeeEdgeConfig": {"environmentFilter": {"allEnvironments": boolean, "environments": ["string"]}}, "apigeeOpdkConfig": {"environmentFilter": {"allEnvironments": boolean, "environments": ["string"]}}, "apigeeXHybridConfig": {"environmentFilter": {"allEnvironments": boolean, "environments": ["string"]}}, "pluginInstance": "string"}]'

`File Example:`
    
    
    --gateway-plugin-addon-config-configs=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `apihub/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/apigee/docs/api-hub/what-is-api-hub>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha apihub addons manage-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apihub/addons/manage-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
