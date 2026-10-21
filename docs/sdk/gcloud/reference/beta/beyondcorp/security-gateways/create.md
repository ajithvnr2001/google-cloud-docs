---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/security-gateways/create/
title: gcloud beta beyondcorp security-gateways create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:29:31.647836+00:00
---

# gcloud beta beyondcorp security-gateways create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/security-gateways/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta beyondcorp security-gateways create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta beyondcorp security-gateways create - create securityGateways 
SYNOPSIS
    

`gcloud beta beyondcorp security-gateways create` (`SECURITY_GATEWAY` : `--location`=`LOCATION`) [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--hubs`=[`HUBS`,…]] [`--request-id`=`REQUEST_ID`] [`--proxy-protocol-config-allowed-client-headers`=[`PROXY_PROTOCOL_CONFIG_ALLOWED_CLIENT_HEADERS`,…] `--proxy-protocol-config-client-ip` `--proxy-protocol-config-gateway-identity`=`PROXY_PROTOCOL_CONFIG_GATEWAY_IDENTITY` `--proxy-protocol-config-metadata-headers`=[`PROXY_PROTOCOL_CONFIG_METADATA_HEADERS`,…] `--contextual-headers-output-type`=`CONTEXTUAL_HEADERS_OUTPUT_TYPE` `--device-info-output-type`=`DEVICE_INFO_OUTPUT_TYPE` `--group-info-output-type`=`GROUP_INFO_OUTPUT_TYPE` `--user-info-output-type`=`USER_INFO_OUTPUT_TYPE`] [`--resource-override-path`=`RESOURCE_OVERRIDE_PATH` | `--service-discovery`=[`apiGateway`=`APIGATEWAY`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a securityGateway 
EXAMPLES
     To create the securityGateway, run: 
    
    
    gcloud beta beyondcorp security-gateways create

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
`--hubs`=[`HUBS`,…]
     Map of Hubs that represents regional data path deployment with Google Cloud Platform region as a key. 

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

`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 
The configuration for the proxy. 
`--proxy-protocol-config-allowed-client-headers`=[`PROXY_PROTOCOL_CONFIG_ALLOWED_CLIENT_HEADERS`,…]
     List of the allowed client header names. 
`--proxy-protocol-config-client-ip`
     Client IP configuration. The client IP address is included if true. 
`--proxy-protocol-config-gateway-identity`=`PROXY_PROTOCOL_CONFIG_GATEWAY_IDENTITY`
     The security gateway identity configuration. `PROXY_PROTOCOL_CONFIG_GATEWAY_IDENTITY` must be (only one value is supported): 

`resource-name`
     Resource name for gateway identity, in the format: projects/{project_id}/locations/{location_id}/securityGateways/{security_gateway_id} 
`--proxy-protocol-config-metadata-headers`=[`PROXY_PROTOCOL_CONFIG_METADATA_HEADERS`,…]
     Custom resource specific headers along with the values. The names should conform to RFC 9110: >Field names can contain alphanumeric characters, hyphens, and periods, can contain only ASCII-printable characters and tabs, and must start with a letter. 

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
Set the value of googleCloudBeyondcorpSecuritygatewaysV1SecurityGateway.serviceDiscovery by using flag [service-discovery] or flags []. 

At most one of these can be specified: 

Settings related to the Service Discovery. 

If Service Discovery is done through API, defines its settings. 
API operation descriptor. 
`--resource-override-path`=`RESOURCE_OVERRIDE_PATH`
     Contains the URI path fragment where HTTP request is sent. 
`--service-discovery`=[`apiGateway`=`APIGATEWAY`]
     Settings related to the Service Discovery. `Shorthand Example:`
    
    
    --service-discovery=apiGateway={resourceOverride={path=string}}

`JSON Example:`
    
    
    --service-discovery='{"apiGateway": {"resourceOverride": {"path": "string"}}}'

`File Example:`
    
    
    --service-discovery=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `beyondcorp/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud beyondcorp security-gateways create](https://docs.cloud.google.com/sdk/gcloud/reference/beyondcorp/security-gateways/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
