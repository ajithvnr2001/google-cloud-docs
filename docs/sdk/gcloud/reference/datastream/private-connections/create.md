---
url: https://docs.cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create/
title: gcloud datastream private-connections create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:28:01.659183+00:00
---

# gcloud datastream private-connections create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/datastream/private-connections/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud datastream private-connections create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud datastream private-connections create - create a Datastream private connection 
SYNOPSIS
    

`gcloud datastream private-connections create` (`PRIVATE_CONNECTION` : `--location`=`LOCATION`) `--display-name`=`DISPLAY_NAME` (`--network-attachment`=`NETWORK_ATTACHMENT` | `--subnet`=`SUBNET` `--vpc`=`VPC`) [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Datastream private connection 
EXAMPLES
     To create a privateConnection with VPC Peering called 'my-privateConnection', run: 
    
    
    gcloud datastream private-connections create my-privateConnection --location=us-central1 --display-name=my-privateConnection --vpc=vpc-example --subnet=10.0.0.0/29

To create a privateConnection with PSC Interface called 'my-privateConnection', run: 
    
    
    gcloud datastream private-connections create my-privateConnection --location=us-central1 --display-name=my-privateConnection --network-attachment=network-attachment-example

POSITIONAL ARGUMENTS
    

Private connection resource - The private connection to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `private_connection` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`PRIVATE_CONNECTION`
     ID of the private_connection or fully qualified identifier for the private_connection. 

To set the `private_connection` attribute: 

  * provide the argument `private_connection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the private_connection. 

To set the `location` attribute: 

  * provide the argument `private_connection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Friendly name for the private connection. 
Exactly one of these must be specified: 

Arguments for Private Service Connect Interface configuration. 
`--network-attachment`=`NETWORK_ATTACHMENT`
     Full URI of the network attachment that datastream will connect to.For example, this would be of the form:`network-attachment=projects/test-project/regions/us-central1/networkAttachments/my-na`
Arguments for VPC Peering configuration. 
`--subnet`=`SUBNET`
     A free subnet for peering. (CIDR of /29). 

This flag argument must be specified if any of the other arguments in this group are specified. 

Vpc resource - Resource ID of the VPC network to peer with. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--vpc` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--vpc`=`VPC`
     ID of the vpc or fully qualified identifier for the vpc. 

To set the `vpc` attribute: 

  * provide the argument `--vpc` on the command line. 


OPTIONAL FLAGS
    

`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--validate-only`
     If set, the request will retrieve the project id to allow in the network attachment Datastream will connect to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This variant is also available: 
    
    
    [gcloud beta datastream private-connections create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/datastream/private-connections/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
