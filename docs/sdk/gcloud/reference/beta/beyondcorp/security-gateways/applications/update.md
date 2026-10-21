---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/security-gateways/applications/update/
title: gcloud beta beyondcorp security-gateways applications update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:29:31.564105+00:00
---

# gcloud beta beyondcorp security-gateways applications update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/security-gateways/applications/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta beyondcorp security-gateways applications update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta beyondcorp security-gateways applications update - update applications 
SYNOPSIS
    

`gcloud beta beyondcorp security-gateways applications update` (`APPLICATION` : `--location`=`LOCATION` `--security-gateway`=`SECURITY_GATEWAY`) [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--request-id`=`REQUEST_ID`] [`--schema`=`SCHEMA`] [`--endpoint-matchers`=[`hostname`=`HOSTNAME`],[`ports`=`PORTS`] | `--add-endpoint-matchers`=[`hostname`=`HOSTNAME`],[`ports`=`PORTS`] `--clear-endpoint-matchers` | `--remove-endpoint-matchers`=[`hostname`=`HOSTNAME`],[`ports`=`PORTS`]] [`--upstreams`=[`egressPolicy`=`EGRESSPOLICY`],[`external`=`EXTERNAL`],[`network`=`NETWORK`],[`proxyProtocol`=`PROXYPROTOCOL`] | `--add-upstreams`=[`egressPolicy`=`EGRESSPOLICY`],[`external`=`EXTERNAL`],[`network`=`NETWORK`],[`proxyProtocol`=`PROXYPROTOCOL`] `--clear-upstreams` | `--remove-upstreams`=[`egressPolicy`=`EGRESSPOLICY`],[`external`=`EXTERNAL`],[`network`=`NETWORK`],[`proxyProtocol`=`PROXYPROTOCOL`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an application 
EXAMPLES
     To update the application, run: 
    
    
    gcloud beta beyondcorp security-gateways applications update

POSITIONAL ARGUMENTS
    

Application resource - Identifier. Name of the resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `application` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`APPLICATION`
     ID of the application or fully qualified identifier for the application. 

To set the `application` attribute: 

  * provide the argument `application` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the application resource. We support only global location. 

To set the `location` attribute: 

  * provide the argument `application` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--security-gateway`=`SECURITY_GATEWAY`
     The securityGateway id of the application resource. 

To set the `security-gateway` attribute: 

  * provide the argument `application` on the command line with a fully specified name; 
  * provide the argument `--security-gateway` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     An arbitrary user-provided name for the application resource. Cannot exceed 64 characters. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. 

For example, consider a situation where you make an initial request and the request timed out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

`--schema`=`SCHEMA`
     Type of the external application. `SCHEMA` must be one of: 

`api-gateway`
     Service Discovery API endpoint when Service Discovery is enabled in Gateway. 
`proxy-gateway`
     Proxy which routes traffic to actual applications, like Netscaler Gateway. 
Update endpoint_matchers. 

At most one of these can be specified: 

`--endpoint-matchers`=[`hostname`=`HOSTNAME`],[`ports`=`PORTS`]
     Set endpoint_matchers to new value. An array of conditions to match the application's network endpoint. Each element in the array is an EndpointMatcher object, which defines a specific combination of a hostname pattern and one or more ports. The application is considered matched if at least one of the EndpointMatcher conditions in this array is met (the conditions are combined using OR logic). Each EndpointMatcher must contain a hostname pattern, such as "example.com", and one or more port numbers specified as a string, such as "443". 

Hostname and port number examples: "`.example.com", "443" "example.com" and "22" "example.com" and "22,33". 

`hostname``

     Hostname of the application. 
ports``
     The ports of the application. 
Shorthand Example:`
    
    
    --endpoint-matchers=hostname=string,ports=[int] --endpoint-matchers=hostname=string,ports=[int]

`JSON Example:`
    
    
    --endpoint-matchers='[{"hostname": "string", "ports": [int]}]'

`File Example:`
    
    
    --endpoint-matchers=path_to_file.(yaml|json)

`
Or at least one of these can be specified: 

\--add-endpoint-matchers`=[`hostname`=`HOSTNAME`],[`ports`=`PORTS`]`
     Add new value to endpoint_matchers list. An array of conditions to match the application's network endpoint. Each element in the array is an EndpointMatcher object, which defines a specific combination of a hostname pattern and one or more ports. The application is considered matched if at least one of the EndpointMatcher conditions in this array is met (the conditions are combined using OR logic). Each EndpointMatcher must contain a hostname pattern, such as "example.com", and one or more port numbers specified as a string, such as "443". 

Hostname and port number examples: ".example.com", "443" "example.com" and "22" "example.com" and "22,33". 

`hostname`
     Hostname of the application. 
`ports`
     The ports of the application. 
`Shorthand Example:`
    
    
    --add-endpoint-matchers=hostname=string,ports=[int] --add-endpoint-matchers=hostname=string,ports=[int]

`JSON Example:`
    
    
    --add-endpoint-matchers='[{"hostname": "string", "ports": [int]}]'

`File Example:`
    
    
    --add-endpoint-matchers=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-endpoint-matchers`
     Clear endpoint_matchers value and set to empty list. 
`--remove-endpoint-matchers`=[`hostname`=`HOSTNAME`],[`ports`=`PORTS`]
     Remove existing value from endpoint_matchers list. An array of conditions to match the application's network endpoint. Each element in the array is an EndpointMatcher object, which defines a specific combination of a hostname pattern and one or more ports. The application is considered matched if at least one of the EndpointMatcher conditions in this array is met (the conditions are combined using OR logic). Each EndpointMatcher must contain a hostname pattern, such as "example.com", and one or more port numbers specified as a string, such as "443". 

Hostname and port number examples: "`.example.com", "443" "example.com" and "22" "example.com" and "22,33". 

`hostname``

     Hostname of the application. 
ports``
     The ports of the application. 
Shorthand Example:`
    
    
    --remove-endpoint-matchers=hostname=string,ports=[int] --remove-endpoint-matchers=hostname=string,ports=[int]

`JSON Example:`
    
    
    --remove-endpoint-matchers='[{"hostname": "string", "ports": [int]}]'

`File Example:`
    
    
    --remove-endpoint-matchers=path_to_file.(yaml|json)

`
Update upstreams. 

At most one of these can be specified: 

\--upstreams`=[`egressPolicy`=`EGRESSPOLICY`],[`external`=`EXTERNAL`],[`network`=`NETWORK`],[`proxyProtocol`=`PROXYPROTOCOL`]`
     Set upstreams to new value. Which upstream resources to forward traffic to. 

egressPolicy``
     Routing policy information. 

regions``
     List of the regions where the application sends traffic. 
external``
     List of the external endpoints to forward traffic to. 

endpoints``
     List of the endpoints to forward traffic to. 

hostname``
     Hostname of the endpoint. 
port``
     Port of the endpoint. 
network``
     Network to forward traffic to. 

name``
     Network name is of the format: `projects/{project}/global/networks/{network}. `
proxyProtocol``
     Enables proxy protocol configuration for the upstream. 

allowedClientHeaders``
     List of the allowed client header names. 
clientIp``
     Client IP configuration. The client IP address is included if true. 
contextualHeaders``
     Configuration for the contextual headers. 

deviceInfo``
     The device information configuration. 

outputType``
     The output type details for the delegated device. 
groupInfo``
     Group details. 

outputType``
     The output type of the delegated group information. 
outputType``
     Default output type for all enabled headers. 
userInfo``
     User details. 

outputType``
     The delegated user's information. 
gatewayIdentity``
     The security gateway identity configuration. 
metadataHeaders``
     Custom resource specific headers along with the values. The names should conform to RFC 9110: >Field names can contain alphanumeric characters, hyphens, and periods, can contain only ASCII-printable characters and tabs, and must start with a letter. 

KEY``
     Sets KEY` value. `
VALUE``
     Sets VALUE` value. `
Shorthand Example:`
    
    
    --upstreams=egressPolicy={regions=[string]},external={endpoints=[{hostname=string,port=int}]},network={name=string},proxyProtocol={allowedClientHeaders=[string],clientIp=boolean,contextualHeaders={deviceInfo={outputType=string},groupInfo={outputType=string},outputType=string,userInfo={outputType=string}},gatewayIdentity=string,metadataHeaders={string=string}} --upstreams=egressPolicy={regions=[string]},external={endpoints=[{hostname=string,port=int}]},network={name=string},proxyProtocol={allowedClientHeaders=[string],clientIp=boolean,contextualHeaders={deviceInfo={outputType=string},groupInfo={outputType=string},outputType=string,userInfo={outputType=string}},gatewayIdentity=string,metadataHeaders={string=string}}

`JSON Example:`
    
    
    --upstreams='[{"egressPolicy": {"regions": ["string"]}, "external": {"endpoints": [{"hostname": "string", "port": int}]}, "network": {"name": "string"}, "proxyProtocol": {"allowedClientHeaders": ["string"], "clientIp": boolean, "contextualHeaders": {"deviceInfo": {"outputType": "string"}, "groupInfo": {"outputType": "string"}, "outputType": "string", "userInfo": {"outputType": "string"}}, "gatewayIdentity": "string", "metadataHeaders": {"string": "string"}}}]'

`File Example:`
    
    
    --upstreams=path_to_file.(yaml|json)

`
Or at least one of these can be specified: 

\--add-upstreams`=[`egressPolicy`=`EGRESSPOLICY`],[`external`=`EXTERNAL`],[`network`=`NETWORK`],[`proxyProtocol`=`PROXYPROTOCOL`]`
     Add new value to upstreams list. Which upstream resources to forward traffic to. 

egressPolicy``
     Routing policy information. 

regions``
     List of the regions where the application sends traffic. 
external``
     List of the external endpoints to forward traffic to. 

endpoints``
     List of the endpoints to forward traffic to. 

hostname``
     Hostname of the endpoint. 
port``
     Port of the endpoint. 
network``
     Network to forward traffic to. 

name``
     Network name is of the format: projects/{project}/global/networks/{network}. 
proxyProtocol``
     Enables proxy protocol configuration for the upstream. 

allowedClientHeaders``
     List of the allowed client header names. 
clientIp``
     Client IP configuration. The client IP address is included if true. 
contextualHeaders``
     Configuration for the contextual headers. 

deviceInfo``
     The device information configuration. 

outputType``
     The output type details for the delegated device. 
groupInfo``
     Group details. 

outputType``
     The output type of the delegated group information. 
outputType``
     Default output type for all enabled headers. 
userInfo``
     User details. 

outputType``
     The delegated user's information. 
gatewayIdentity``
     The security gateway identity configuration. 
metadataHeaders``
     Custom resource specific headers along with the values. The names should conform to RFC 9110: >Field names can contain alphanumeric characters, hyphens, and periods, can contain only ASCII-printable characters and tabs, and must start with a letter. 

KEY``
     Sets `KEY` value. 
VALUE``
     Sets `VALUE` value. 
Shorthand Example:`
    
    
    --add-upstreams=egressPolicy={regions=[string]},external={endpoints=[{hostname=string,port=int}]},network={name=string},proxyProtocol={allowedClientHeaders=[string],clientIp=boolean,contextualHeaders={deviceInfo={outputType=string},groupInfo={outputType=string},outputType=string,userInfo={outputType=string}},gatewayIdentity=string,metadataHeaders={string=string}} --add-upstreams=egressPolicy={regions=[string]},external={endpoints=[{hostname=string,port=int}]},network={name=string},proxyProtocol={allowedClientHeaders=[string],clientIp=boolean,contextualHeaders={deviceInfo={outputType=string},groupInfo={outputType=string},outputType=string,userInfo={outputType=string}},gatewayIdentity=string,metadataHeaders={string=string}}

`JSON Example:`
    
    
    --add-upstreams='[{"egressPolicy": {"regions": ["string"]}, "external": {"endpoints": [{"hostname": "string", "port": int}]}, "network": {"name": "string"}, "proxyProtocol": {"allowedClientHeaders": ["string"], "clientIp": boolean, "contextualHeaders": {"deviceInfo": {"outputType": "string"}, "groupInfo": {"outputType": "string"}, "outputType": "string", "userInfo": {"outputType": "string"}}, "gatewayIdentity": "string", "metadataHeaders": {"string": "string"}}}]'

`File Example:`
    
    
    --add-upstreams=path_to_file.(yaml|json)

`
At most one of these can be specified: 

\--clear-upstreams``
     Clear upstreams value and set to empty list. 
\--remove-upstreams`=[`egressPolicy`=`EGRESSPOLICY`],[`external`=`EXTERNAL`],[`network`=`NETWORK`],[`proxyProtocol`=`PROXYPROTOCOL`]`
     Remove existing value from upstreams list. Which upstream resources to forward traffic to. 

egressPolicy``
     Routing policy information. 

regions``
     List of the regions where the application sends traffic. 
external``
     List of the external endpoints to forward traffic to. 

endpoints``
     List of the endpoints to forward traffic to. 

hostname``
     Hostname of the endpoint. 
port``
     Port of the endpoint. 
network``
     Network to forward traffic to. 

name``
     Network name is of the format: `projects/{project}/global/networks/{network}. `
proxyProtocol``
     Enables proxy protocol configuration for the upstream. 

allowedClientHeaders``
     List of the allowed client header names. 
clientIp``
     Client IP configuration. The client IP address is included if true. 
contextualHeaders``
     Configuration for the contextual headers. 

deviceInfo``
     The device information configuration. 

outputType``
     The output type details for the delegated device. 
groupInfo``
     Group details. 

outputType``
     The output type of the delegated group information. 
outputType``
     Default output type for all enabled headers. 
userInfo``
     User details. 

outputType``
     The delegated user's information. 
gatewayIdentity``
     The security gateway identity configuration. 
metadataHeaders``
     Custom resource specific headers along with the values. The names should conform to RFC 9110: >Field names can contain alphanumeric characters, hyphens, and periods, can contain only ASCII-printable characters and tabs, and must start with a letter. 

KEY``
     Sets KEY` value. `
VALUE``
     Sets VALUE` value. `
Shorthand Example:`
    
    
    --remove-upstreams=egressPolicy={regions=[string]},external={endpoints=[{hostname=string,port=int}]},network={name=string},proxyProtocol={allowedClientHeaders=[string],clientIp=boolean,contextualHeaders={deviceInfo={outputType=string},groupInfo={outputType=string},outputType=string,userInfo={outputType=string}},gatewayIdentity=string,metadataHeaders={string=string}} --remove-upstreams=egressPolicy={regions=[string]},external={endpoints=[{hostname=string,port=int}]},network={name=string},proxyProtocol={allowedClientHeaders=[string],clientIp=boolean,contextualHeaders={deviceInfo={outputType=string},groupInfo={outputType=string},outputType=string,userInfo={outputType=string}},gatewayIdentity=string,metadataHeaders={string=string}}

`JSON Example:`
    
    
    --remove-upstreams='[{"egressPolicy": {"regions": ["string"]}, "external": {"endpoints": [{"hostname": "string", "port": int}]}, "network": {"name": "string"}, "proxyProtocol": {"allowedClientHeaders": ["string"], "clientIp": boolean, "contextualHeaders": {"deviceInfo": {"outputType": "string"}, "groupInfo": {"outputType": "string"}, "outputType": "string", "userInfo": {"outputType": "string"}}, "gatewayIdentity": "string", "metadataHeaders": {"string": "string"}}}]'

`File Example:`
    
    
    --remove-upstreams=path_to_file.(yaml|json)

`
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `beyondcorp/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud beyondcorp security-gateways applications update](https://docs.cloud.google.com/sdk/gcloud/reference/beyondcorp/security-gateways/applications/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
