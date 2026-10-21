---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/client-connector/gateways/create/
title: gcloud beta beyondcorp client-connector gateways create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:29:28.343094+00:00
---

# gcloud beta beyondcorp client-connector gateways create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/client-connector/gateways/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta beyondcorp client-connector gateways create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta beyondcorp client-connector gateways create - create a new BeyondCorp client gateway (Deprecated)
SYNOPSIS
    

`gcloud beta beyondcorp client-connector gateways create` (`CLIENT_GATEWAY` : `--location`=`LOCATION`) `--client-connector-service`=`CLIENT_CONNECTOR_SERVICE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new BeyondCorp client gateway. 
EXAMPLES
     The following command creates a client gateway with ID ``my-client-gateway`` in the default user project and location us-central1: 
    
    
    gcloud beta beyondcorp client-connector gateways create my-client-gateway --location=us-central1 --client-connector-service=projects/consumer-project-id/locations/us-central1/clientConnectorServices/my-service-resource

The following command creates a client gateway with ID ``my-client-gateway`` with explicit values for all required and optional parameters: 
    
    
    gcloud beta beyondcorp client-connector gateways create my-client-gateway --project=consumer-project-id --location=us-central1 --client-connector-service=projects/consumer-project-id/locations/us-central1/clientConnectorServices/my-service-resource

POSITIONAL ARGUMENTS
    

Client gateway resource - The BeyondCorp client gateway you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `client_gateway` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLIENT_GATEWAY`
     ID of the client_gateway or fully qualified identifier for the client_gateway. 

To set the `client_gateway` attribute: 

  * provide the argument `client_gateway` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the BeyondCorp Enterprise client connector. To set the `location` attribute: 

  * provide the argument `client_gateway` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--client-connector-service`=`CLIENT_CONNECTOR_SERVICE`
     The client connector service that the client gateway is associated with. Example \- `projects/consumer-project-id/locations/us-central1/clientConnectorServices/my-service-resource`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `beyondcorp/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/>
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
