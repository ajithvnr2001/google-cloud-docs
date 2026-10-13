---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/update/
title: gcloud network-connectivity multicloud-data-transfer-configs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:19.697032+00:00
---

# gcloud network-connectivity multicloud-data-transfer-configs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-connectivity multicloud-data-transfer-configs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-connectivity multicloud-data-transfer-configs update - update a multicloudDataTransferConfig 
SYNOPSIS
    

`gcloud network-connectivity multicloud-data-transfer-configs update` (`MULTICLOUD_DATA_TRANSFER_CONFIG` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--request-id`=`REQUEST_ID`] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`--services`=[`SERVICES`,…] | `--update-services`=[`UPDATE_SERVICES`,…] `--clear-services` | `--remove-services`=`REMOVE_SERVICES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a multicloudDataTransferConfig 
EXAMPLES
     To update the multicloudDataTransferConfig, run: 

$ [gcloud network-connectivity multicloud-data-transfer-configs](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs) \
    
    
    update config-1 --location=europe-west1 \
    --description="Multicloud Data Transfer Config description \
    updated" --update-services=cloud-run

POSITIONAL ARGUMENTS
    

MulticloudDataTransferConfig resource - Identifier. The name of the `MulticloudDataTransferConfig` resource. Format: `projects/{project}/locations/{location}/multicloudDataTransferConfigs/{multicloud_data_transfer_config}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `multicloud_data_transfer_config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MULTICLOUD_DATA_TRANSFER_CONFIG`
     ID of the multicloudDataTransferConfig or fully qualified identifier for the multicloudDataTransferConfig. 

To set the `multicloud_data_transfer_config` attribute: 

  * provide the argument `multicloud_data_transfer_config` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the multicloudDataTransferConfig resource. 

To set the `location` attribute: 

  * provide the argument `multicloud_data_transfer_config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A description of this resource. 
`--etag`=`ETAG`
     The etag is computed by the server, and might be sent with update and delete requests so that the client has an up-to-date value before proceeding. 
`--request-id`=`REQUEST_ID`
     A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server waits for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, can ignore the second request. This prevents clients from accidentally creating duplicate `MulticloudDataTransferConfig` resources. 

The request ID must be a valid UUID with the exception that zero UUID (00000000-0000-0000-0000-000000000000) isn't supported. 

Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. User-defined labels. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. User-defined labels. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

Update services. 

At most one of these can be specified: 

`--services`=[`SERVICES`,…]
     Set services to new value. Maps services to their current or planned states. Service names are keys, and the associated values describe the state of the service. If a state change is expected, the value is either `ADDING` or `DELETING`, depending on the actions taken. 

Sample output: "services": { "big-query": { "states": [ { "effectiveTime": "2024-12-12T08:00:00Z" "state": "ADDING", }, ] }, "cloud-storage": { "states": [ { "state": "ACTIVE", } ] } }. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --services=string

`JSON Example:`
    
    
    --services='{"string": {}}'

`File Example:`
    
    
    --services=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-services`=[`UPDATE_SERVICES`,…]
     Update services value or add key value pair. Maps services to their current or planned states. Service names are keys, and the associated values describe the state of the service. If a state change is expected, the value is either `ADDING` or `DELETING`, depending on the actions taken. 

Sample output: "services": { "big-query": { "states": [ { "effectiveTime": "2024-12-12T08:00:00Z" "state": "ADDING", }, ] }, "cloud-storage": { "states": [ { "state": "ACTIVE", } ] } }. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-services=string

`JSON Example:`
    
    
    --update-services='{"string": {}}'

`File Example:`
    
    
    --update-services=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-services`
     Clear services value and set to empty map. 
`--remove-services`=`REMOVE_SERVICES`
     Remove existing value from map services. Sets `remove_services` value. `Shorthand Example:`
    
    
    --remove-services=string,string

`JSON Example:`
    
    
    --remove-services=["string"]

`File Example:`
    
    
    --remove-services=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This variant is also available: 
    
    
    [gcloud beta network-connectivity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity) multicloud-data-transfer-configs update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
