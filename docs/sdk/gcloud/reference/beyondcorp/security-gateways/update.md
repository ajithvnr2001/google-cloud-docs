---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beyondcorp/security-gateways/update/
title: gcloud beyondcorp security-gateways update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:04:32.076709+00:00
---

# gcloud beyondcorp security-gateways update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beyondcorp/security-gateways/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beyondcorp security-gateways update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beyondcorp security-gateways update - update securityGateways 
SYNOPSIS
    

`gcloud beyondcorp security-gateways update` (`SECURITY_GATEWAY` : `--location`=`LOCATION`) [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--request-id`=`REQUEST_ID`] [`--clear-proxy-protocol-config` `--[no-]proxy-protocol-config-client-ip` `--proxy-protocol-config-gateway-identity`=`PROXY_PROTOCOL_CONFIG_GATEWAY_IDENTITY` `--contextual-headers-output-type`=`CONTEXTUAL_HEADERS_OUTPUT_TYPE` `--device-info-output-type`=`DEVICE_INFO_OUTPUT_TYPE` `--group-info-output-type`=`GROUP_INFO_OUTPUT_TYPE` `--user-info-output-type`=`USER_INFO_OUTPUT_TYPE` `--proxy-protocol-config-allowed-client-headers`=[`PROXY_PROTOCOL_CONFIG_ALLOWED_CLIENT_HEADERS`,…] | `--add-proxy-protocol-config-allowed-client-headers`=[`ADD_PROXY_PROTOCOL_CONFIG_ALLOWED_CLIENT_HEADERS`,…] `--clear-proxy-protocol-config-allowed-client-headers` | `--remove-proxy-protocol-config-allowed-client-headers`=[`REMOVE_PROXY_PROTOCOL_CONFIG_ALLOWED_CLIENT_HEADERS`,…] `--proxy-protocol-config-metadata-headers`=[`PROXY_PROTOCOL_CONFIG_METADATA_HEADERS`,…] | `--update-proxy-protocol-config-metadata-headers`=[`UPDATE_PROXY_PROTOCOL_CONFIG_METADATA_HEADERS`,…] `--clear-proxy-protocol-config-metadata-headers` | `--remove-proxy-protocol-config-metadata-headers`=`REMOVE_PROXY_PROTOCOL_CONFIG_METADATA_HEADERS`] [`--hubs`=[`HUBS`,…] | `--update-hubs`=[`UPDATE_HUBS`,…] `--clear-hubs` | `--remove-hubs`=`REMOVE_HUBS`] [`--service-discovery`=[`apiGateway`=`APIGATEWAY`] | `--clear-service-discovery` `--resource-override-path`=`RESOURCE_OVERRIDE_PATH`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a securityGateway 
EXAMPLES
     To update the securityGateway, run: 
    
    
    gcloud beyondcorp security-gateways update

POSITIONAL ARGUMENTS
    

SecurityGateway resource - Identifier. Name of the resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `security_gateway` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SECURITY_GATEWAY`
     ID of the securityGateway or fully qualified identifier for the securityGateway. 

To set the `security_gateway` attribute: 

  * provide the argument `security_gateway` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the securityGateway resource. We support only global location. 

To set the `location` attribute: 

  * provide the argument `security_gateway` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     An arbitrary user-provided name for the SecurityGateway. Cannot exceed 64 characters. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. 

For example, consider a situation where you make an initial request and the request timed out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

The configuration for the proxy. 
`--clear-proxy-protocol-config`
     Set googleCloudBeyondcorpSecuritygatewaysV1SecurityGateway.proxyProtocolConfig back to default value. 
`--[no-]proxy-protocol-config-client-ip`
     Client IP configuration. The client IP address is included if true. Use `--proxy-protocol-config-client-ip` to enable and `--no-proxy-protocol-config-client-ip` to disable. 
`--proxy-protocol-config-gateway-identity`=`PROXY_PROTOCOL_CONFIG_GATEWAY_IDENTITY`
     The security gateway identity configuration. `PROXY_PROTOCOL_CONFIG_GATEWAY_IDENTITY` must be (only one value is supported): 

`resource-name`
     Resource name for gateway identity, in the format: projects/{project_id}/locations/{location_id}/securityGateways/{security_gateway_id} 
Contextual headers configuration. 
`--contextual-headers-output-type`=`CONTEXTUAL_HEADERS_OUTPUT_TYPE`
     Default output type for all enabled headers. `CONTEXTUAL_HEADERS_OUTPUT_TYPE` must be one of: 

`json`
     JSON output type. 
`none`
     Explicitly disable header output. 
`protobuf`
     Protobuf output type. 
The delegated device information configuration. 
`--device-info-output-type`=`DEVICE_INFO_OUTPUT_TYPE`
     The output type details for the delegated device. `DEVICE_INFO_OUTPUT_TYPE` must be one of: 

`json`
     JSON output type. 
`none`
     Explicitly disable header output. 
`protobuf`
     Protobuf output type. 
The delegated group configuration details. 
`--group-info-output-type`=`GROUP_INFO_OUTPUT_TYPE`
     The output type of the delegated group information. `GROUP_INFO_OUTPUT_TYPE` must be one of: 

`json`
     JSON output type. 
`none`
     Explicitly disable header output. 
`protobuf`
     Protobuf output type. 
The configuration information for the delegated user. 
`--user-info-output-type`=`USER_INFO_OUTPUT_TYPE`
     The delegated user's information. `USER_INFO_OUTPUT_TYPE` must be one of: 

`json`
     JSON output type. 
`none`
     Explicitly disable header output. 
`protobuf`
     Protobuf output type. 
Update proxy_protocol_config_allowed_client_headers. 

At most one of these can be specified: 

`--proxy-protocol-config-allowed-client-headers`=[`PROXY_PROTOCOL_CONFIG_ALLOWED_CLIENT_HEADERS`,…]
     Set proxy_protocol_config_allowed_client_headers to new value. 
Or at least one of these can be specified: 

`--add-proxy-protocol-config-allowed-client-headers`=[`ADD_PROXY_PROTOCOL_CONFIG_ALLOWED_CLIENT_HEADERS`,…]
     Add new value to proxy_protocol_config_allowed_client_headers list. 
At most one of these can be specified: 

`--clear-proxy-protocol-config-allowed-client-headers`
     Clear proxy_protocol_config_allowed_client_headers value and set to empty list. 
`--remove-proxy-protocol-config-allowed-client-headers`=[`REMOVE_PROXY_PROTOCOL_CONFIG_ALLOWED_CLIENT_HEADERS`,…]
     Remove existing value from proxy_protocol_config_allowed_client_headers list. 
Update proxy_protocol_config_metadata_headers. 

At most one of these can be specified: 

`--proxy-protocol-config-metadata-headers`=[`PROXY_PROTOCOL_CONFIG_METADATA_HEADERS`,…]
     Set proxy_protocol_config_metadata_headers to new value. Custom resource specific headers along with the values. The names should conform to RFC 9110: >Field names can contain alphanumeric characters, hyphens, and periods, can contain only ASCII-printable characters and tabs, and must start with a letter. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --proxy-protocol-config-metadata-headers=string=string

`JSON Example:`
    
    
    --proxy-protocol-config-metadata-headers='{"string": "string"}'

`File Example:`
    
    
    --proxy-protocol-config-metadata-headers=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-proxy-protocol-config-metadata-headers`=[`UPDATE_PROXY_PROTOCOL_CONFIG_METADATA_HEADERS`,…]
     Update proxy_protocol_config_metadata_headers value or add key value pair. Custom resource specific headers along with the values. The names should conform to RFC 9110: >Field names can contain alphanumeric characters, hyphens, and periods, can contain only ASCII-printable characters and tabs, and must start with a letter. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-proxy-protocol-config-metadata-headers=string=string

`JSON Example:`
    
    
    --update-proxy-protocol-config-metadata-headers='{"string": "string"}'

`File Example:`
    
    
    --update-proxy-protocol-config-metadata-headers=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-proxy-protocol-config-metadata-headers`
     Clear proxy_protocol_config_metadata_headers value and set to empty map. 
`--remove-proxy-protocol-config-metadata-headers`=`REMOVE_PROXY_PROTOCOL_CONFIG_METADATA_HEADERS`
     Remove existing value from map proxy_protocol_config_metadata_headers. Sets `remove_proxy_protocol_config_metadata_headers` value. `Shorthand Example:`
    
    
    --remove-proxy-protocol-config-metadata-headers=string,string

`JSON Example:`
    
    
    --remove-proxy-protocol-config-metadata-headers=["string"]

`File Example:`
    
    
    --remove-proxy-protocol-config-metadata-headers=path_to_file.(yaml|json)

Update hubs. 

At most one of these can be specified: 

`--hubs`=[`HUBS`,…]
     Set hubs to new value. Map of Hubs that represents regional data path deployment with Google Cloud Platform region as a key. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --hubs=string

`JSON Example:`
    
    
    --hubs='{"string": {}}'

`File Example:`
    
    
    --hubs=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-hubs`=[`UPDATE_HUBS`,…]
     Update hubs value or add key value pair. Map of Hubs that represents regional data path deployment with Google Cloud Platform region as a key. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-hubs=string

`JSON Example:`
    
    
    --update-hubs='{"string": {}}'

`File Example:`
    
    
    --update-hubs=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-hubs`
     Clear hubs value and set to empty map. 
`--remove-hubs`=`REMOVE_HUBS`
     Remove existing value from map hubs. Sets `remove_hubs` value. `Shorthand Example:`
    
    
    --remove-hubs=string,string

`JSON Example:`
    
    
    --remove-hubs=["string"]

`File Example:`
    
    
    --remove-hubs=path_to_file.(yaml|json)

Set the value of googleCloudBeyondcorpSecuritygatewaysV1SecurityGateway.serviceDiscovery by using flag [service-discovery] or flags []. 

At most one of these can be specified: 

`--service-discovery`=[`apiGateway`=`APIGATEWAY`]
     Settings related to the Service Discovery. `Shorthand Example:`
    
    
    --service-discovery=apiGateway={resourceOverride={path=string}}

`JSON Example:`
    
    
    --service-discovery='{"apiGateway": {"resourceOverride": {"path": "string"}}}'

`File Example:`
    
    
    --service-discovery=path_to_file.(yaml|json)

Or at least one of these can be specified: 

Settings related to the Service Discovery. 
`--clear-service-discovery`
     Set googleCloudBeyondcorpSecuritygatewaysV1SecurityGateway.serviceDiscovery back to default value. 
If Service Discovery is done through API, defines its settings. 
API operation descriptor. 
`--resource-override-path`=`RESOURCE_OVERRIDE_PATH`
     Contains the URI path fragment where HTTP request is sent. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `beyondcorp/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/>
NOTES
     This variant is also available: 
    
    
    [gcloud beta beyondcorp security-gateways update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/security-gateways/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
