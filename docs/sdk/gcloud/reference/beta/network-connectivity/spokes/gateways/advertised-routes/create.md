---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/gateways/advertised-routes/create/
title: gcloud beta network-connectivity spokes gateways advertised-routes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:42:23.465981+00:00
---

# gcloud beta network-connectivity spokes gateways advertised-routes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/gateways/advertised-routes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-connectivity spokes gateways advertised-routes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-connectivity spokes gateways advertised-routes create - create a new gateway advertised route 
SYNOPSIS
    

`gcloud beta network-connectivity spokes gateways advertised-routes create` (`GATEWAY_ADVERTISED_ROUTE` : `--region`=`REGION` `--spoke`=`SPOKE`) `--advertise-to-hub` `--ip-range`=`IP_RANGE` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--priority`=`PRIORITY`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new gateway advertised route with the given name. 
EXAMPLES
     Create an advertised route with name ``my-route`` for gateway spoke ``my-gateway`` in region ``us-central1``: 
    
    
    [gcloud beta network-connectivity spokes gateways](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/gateways) advertised-routes create my-route --spoke=my-gateway --region=us-central1 --ip-range=10.0.1.0/24

POSITIONAL ARGUMENTS
    

GatewayAdvertisedRoute resource - Name of the gateway advertised route to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `gateway_advertised_route` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GATEWAY_ADVERTISED_ROUTE`
     ID of the gatewayAdvertisedRoute or fully qualified identifier for the gatewayAdvertisedRoute. 

To set the `gateway_advertised_route` attribute: 

  * provide the argument `gateway_advertised_route` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The location Id. To set the `region` attribute: 

  * provide the argument `gateway_advertised_route` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


`--spoke`=`SPOKE`
     Id of the spoke. 

To set the `spoke` attribute: 

  * provide the argument `gateway_advertised_route` on the command line with a fully specified name; 
  * provide the argument `--spoke` on the command line. 


REQUIRED FLAGS
    

`--advertise-to-hub`
     The gateway should advertise this route toward the hub. 
`--ip-range`=`IP_RANGE`
     Advertise this IP range. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the advertised route to be created. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
`--priority`=`PRIORITY`
     This route's priority. Must be between 0 and 65335. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud network-connectivity spokes gateways advertised-routes](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/gateways/advertised-routes) create

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-09 UTC."],[],[]] 
