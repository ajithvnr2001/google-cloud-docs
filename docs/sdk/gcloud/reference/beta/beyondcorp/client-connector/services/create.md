---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/client-connector/services/create/
title: gcloud beta beyondcorp client-connector services create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:29:29.561201+00:00
---

# gcloud beta beyondcorp client-connector services create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/beyondcorp/client-connector/services/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta beyondcorp client-connector services create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta beyondcorp client-connector services create - create a new BeyondCorp client connector service (Deprecated)
SYNOPSIS
    

`gcloud beta beyondcorp client-connector services create` (`CLIENT_CONNECTOR_SERVICE` : `--location`=`LOCATION`) (`--config-from-file`=`CONFIG_FROM_FILE` | [`--egress-peered-vpc`=`EGRESS_PEERED_VPC` `--ingress-config`=`INGRESS_CONFIG` : `--display-name`=`DISPLAY_NAME`]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new BeyondCorp client connector service. 
EXAMPLES
     The following command creates a client connector service with ID ``my-service-resource`` using ingress/egress config provided: 
    
    
    gcloud beta beyondcorp client-connector services create my-service-resource --location=us-central1 --project=consumer-project-id --ingress-config='{"transportProtocol":"TCP",
     "destinationRoutes":[{"address":"196.0.0.1",
     "netmask":"255.255.255.0"}]}' \
        --egress-peered-vpc='{"networkVpc":"projects/consumer-project-id\
    /global/networks/my-vpc-network"}'

The following command creates a client connector service with ID ``my-service-resource`` with configuration from file: 
    
    
    gcloud beta beyondcorp client-connector services create my-service-resource --project=consumer-project-id --location=us-central1 --config-from-file=/path/to/file/configJson.txt

POSITIONAL ARGUMENTS
    

Client connector service resource - The BeyondCorp client connector service you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `client_connector_service` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLIENT_CONNECTOR_SERVICE`
     ID of the client_connector_service or fully qualified identifier for the client_connector_service. 

To set the `client_connector_service` attribute: 

  * provide the argument `client_connector_service` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the BeyondCorp Enterprise client connector. To set the `location` attribute: 

  * provide the argument `client_connector_service` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

Client connector service configuration. 

Exactly one of these must be specified: 

`--config-from-file`=`CONFIG_FROM_FILE`
     Path to json file containing client connector service configuration. Example - "/file/path/configJson.txt" where configJson.txt contains -
    
    
    {
      "ingress":{
        "config":{
          "transportProtocol":"TCP",
          "destinationRoutes":[{
            "address":"196.0.0.0",
            "netmask":"255.255.255.0"
          }]
        }
      },
      "egress":{
        "peeredVpc":{
          "networkVpc":"projects/consumer-project-id/global/networks/my-vpc-network"
        }
      },
      "displayName":"my-service-resource"
    }

Or at least one of these can be specified: 

`--egress-peered-vpc`=`EGRESS_PEERED_VPC`
     The peered VPC owned by the consumer project. Example - {"networkVpc": "projects/consumer-project-id/global/networks/my-vpc-network"}. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--ingress-config`=`INGRESS_CONFIG`
     The basic ingress config for client gateways. Example - {"transportProtocol": "TCP","destinationRoutes":[{"address":"196.0.0.1", "netmask":"255.255.255.0"}]}. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--display-name`=`DISPLAY_NAME`
     An arbitrary user-provided name for the client connector service. The display name should follow format - 

  * Must be 6 to 30 characters in length. 
  * Can only contain lowercase letters, numbers and hyphens. 
  * Must start with a letter. 


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
