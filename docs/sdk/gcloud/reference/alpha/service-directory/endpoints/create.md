---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-directory/endpoints/create/
title: gcloud alpha service-directory endpoints create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:55:05.956015+00:00
---

# gcloud alpha service-directory endpoints create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-directory/endpoints/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha service-directory endpoints create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha service-directory endpoints create - creates an endpoint 
SYNOPSIS
    

`gcloud alpha service-directory endpoints create` (`ENDPOINT` : `--location`=`LOCATION` `--namespace`=`NAMESPACE` `--service`=`SERVICE`) [`--address`=`ADDRESS`] [`--metadata`=[`KEY`=`VALUE`,…]] [`--network`=`NETWORK`] [`--port`=`PORT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates an endpoint. 
EXAMPLES
     To create a Service Directory endpoint, run: 
    
    
    gcloud alpha service-directory endpoints create my-endpoint --service=my-service --namespace=my-namespace --location=us-east1 --address=1.2.3.4 --port=5 --metadata=a=b,c=d --network=projects/123456789/locations/global/networks/default

POSITIONAL ARGUMENTS
    

Endpoint resource - The Service Directory endpoint to create. The endpoint id must be 1-63 characters long and match the regular expression `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`ENDPOINT`
     ID of the endpoint or fully qualified identifier for the endpoint. 

To set the `endpoint` attribute: 

  * provide the argument `endpoint` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The name of the region for the endpoint. 

To set the `location` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--namespace`=`NAMESPACE`
     The name of the namespace for the endpoint. 

To set the `namespace` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--namespace` on the command line. 


`--service`=`SERVICE`
     The name of the service for the endpoint. 

To set the `service` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--service` on the command line. 


FLAGS
    

`--address`=`ADDRESS`
     IPv4 or IPv6 address of the endpoint. The default is empty string. 
`--metadata`=[`KEY`=`VALUE`,…]
     Metadata for the endpoint. 

Metadata takes the form of key/value string pairs. Keys are composed of an optional prefix and a name segment, separated by a slash(/). Prefixes and names must be composed of alphanumeric characters, dashes, and dots. Names may also use underscores. There are no character restrictions on what may go into the value of a metadata. The entire dictionary is limited to 512 characters, spread across all key-value pairs. 

`--network`=`NETWORK`
     Specifies the Google Compute Engine Network (VPC) of the Endpoint. Network and Project existence is not checked. Example: `projects/<PROJECT_NUM>/locations/global/networks/<NETWORK_NAME>` The default is empty string. 
`--port`=`PORT`
     Port that the endpoint is running on, must be in the range of [0, 65535]. The default is 0. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud service-directory endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory/endpoints/create)
    
    
    [gcloud beta service-directory endpoints create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-directory/endpoints/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
