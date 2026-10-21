---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/multicloud-data-transfer-configs/destinations/update/
title: gcloud beta network-connectivity multicloud-data-transfer-configs destinations update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:42:20.902405+00:00
---

# gcloud beta network-connectivity multicloud-data-transfer-configs destinations update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/multicloud-data-transfer-configs/destinations/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-connectivity multicloud-data-transfer-configs destinations update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-connectivity multicloud-data-transfer-configs destinations update - update destinations 
SYNOPSIS
    

`gcloud beta network-connectivity multicloud-data-transfer-configs destinations update` (`DESTINATION` : `--location`=`LOCATION` `--multicloud-data-transfer-config`=`MULTICLOUD_DATA_TRANSFER_CONFIG`) [`--async`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--request-id`=`REQUEST_ID`] [`--endpoints`=[`asn`=`ASN`],[`csp`=`CSP`] | `--add-endpoints`=[`asn`=`ASN`],[`csp`=`CSP`] `--clear-endpoints` | `--remove-endpoints`=[`asn`=`ASN`],[`csp`=`CSP`]] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a destination 
EXAMPLES
     To update the destination, run: 
    
    
    [gcloud beta network-connectivity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity) multicloud-data-transfer-configs destinations update

POSITIONAL ARGUMENTS
    

Destination resource - Identifier. The name of the `Destination` resource. Format: `projects/{project}/locations/{location}/multicloudDataTransferConfigs/{multicloud_data_transfer_config}/destinations/{destination}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `destination` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DESTINATION`
     ID of the destination or fully qualified identifier for the destination. 

To set the `destination` attribute: 

  * provide the argument `destination` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the destination resource. 

To set the `location` attribute: 

  * provide the argument `destination` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--multicloud-data-transfer-config`=`MULTICLOUD_DATA_TRANSFER_CONFIG`
     The multicloudDataTransferConfig id of the destination resource. 

To set the `multicloud-data-transfer-config` attribute: 

  * provide the argument `destination` on the command line with a fully specified name; 
  * provide the argument `--multicloud-data-transfer-config` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A description of this resource. 
`--etag`=`ETAG`
     The etag is computed by the server, and might be sent with update and delete requests so that the client has an up-to-date value before proceeding. 
`--request-id`=`REQUEST_ID`
     A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server can ignore the request if it has already been completed. The server waits for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, can ignore the second request. 

The request ID must be a valid UUID with the exception that zero UUID (00000000-0000-0000-0000-000000000000) isn't supported. 

Update endpoints. 

At most one of these can be specified: 

`--endpoints`=[`asn`=`ASN`],[`csp`=`CSP`]
     Set endpoints to new value. The list of `DestinationEndpoint` resources configured for the IP prefix. 

`asn`
     The ASN of the remote IP prefix. 
`csp`
     The CSP of the remote IP prefix. 
`Shorthand Example:`
    
    
    --endpoints=asn=int,csp=string --endpoints=asn=int,csp=string

`JSON Example:`
    
    
    --endpoints='[{"asn": int, "csp": "string"}]'

`File Example:`
    
    
    --endpoints=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-endpoints`=[`asn`=`ASN`],[`csp`=`CSP`]
     Add new value to endpoints list. The list of `DestinationEndpoint` resources configured for the IP prefix. 

`asn`
     The ASN of the remote IP prefix. 
`csp`
     The CSP of the remote IP prefix. 
`Shorthand Example:`
    
    
    --add-endpoints=asn=int,csp=string --add-endpoints=asn=int,csp=string

`JSON Example:`
    
    
    --add-endpoints='[{"asn": int, "csp": "string"}]'

`File Example:`
    
    
    --add-endpoints=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-endpoints`
     Clear endpoints value and set to empty list. 
`--remove-endpoints`=[`asn`=`ASN`],[`csp`=`CSP`]
     Remove existing value from endpoints list. The list of `DestinationEndpoint` resources configured for the IP prefix. 

`asn`
     The ASN of the remote IP prefix. 
`csp`
     The CSP of the remote IP prefix. 
`Shorthand Example:`
    
    
    --remove-endpoints=asn=int,csp=string --remove-endpoints=asn=int,csp=string

`JSON Example:`
    
    
    --remove-endpoints='[{"asn": int, "csp": "string"}]'

`File Example:`
    
    
    --remove-endpoints=path_to_file.(yaml|json)

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

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud network-connectivity multicloud-data-transfer-configs](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/multicloud-data-transfer-configs) destinations update

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
