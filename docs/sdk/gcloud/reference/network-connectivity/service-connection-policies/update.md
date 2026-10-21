---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update/
title: gcloud network-connectivity service-connection-policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:52:30.524120+00:00
---

# gcloud network-connectivity service-connection-policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-connectivity service-connection-policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-connectivity service-connection-policies update - update a service connection policy 
SYNOPSIS
    

`gcloud network-connectivity service-connection-policies update` `SERVICE_CONNECTION_POLICY` [`--allowed-google-producers-resource-hierarchy-level`=[`ALLOWED_GOOGLE_PRODUCERS_RESOURCE_HIERARCHY_LEVEL`,…]] [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--producer-instance-location`=`PRODUCER_INSTANCE_LOCATION`] [`--psc-connection-limit`=`PSC_CONNECTION_LIMIT`] [`--region`=`REGION`] [`--subnets`=[`SUBNETS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Service Connection Policy with the given name. 
EXAMPLES
     Update a Service Connection Policy with name `my-service-conn-policy` in region `us-central1`. 
    
    
    gcloud network-connectivity service-connection-policies update my-service-conn-policy --region=us-central1 --psc-connection-limit=5 --subnets=my-subnet --producer-instance-location=custom-resource-hierarchy-levels --allowed-google-producers-resource-hierarchy-level=projects/my-project

POSITIONAL ARGUMENTS
    

Service connection policy resource - Name of the Service Connection Policy to be updated. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service_connection_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `service_connection_policy` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 



This must be specified. 

`SERVICE_CONNECTION_POLICY`
     ID of the service connection policy or fully qualified identifier for the service connection policy. 

To set the `service_connection_policy` attribute: 

  * provide the argument `service_connection_policy` on the command line. 


FLAGS
    

`--allowed-google-producers-resource-hierarchy-level`=[`ALLOWED_GOOGLE_PRODUCERS_RESOURCE_HIERARCHY_LEVEL`,…]
     List of projects, folders, or orgs where the producer instance can be located in the form "projects/123456789", folders/123456789", or "organizations/123456789". 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the Service Connection Policy to be updated. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
`--producer-instance-location`=`PRODUCER_INSTANCE_LOCATION`
     Option that determines where the producer instances can be located for which connections can be created in the network controlled by this policy. `PRODUCER_INSTANCE_LOCATION` must be one of: 

`custom-resource-hierarchy-levels`
     The producer instance must be located in one of the values provided in the allowed-google-producers-resource-hierarchy-level flag. 
`none`
     The producer instance must be within the same project as this connection policy. 
`--psc-connection-limit`=`PSC_CONNECTION_LIMIT`
     Max number of PSC connections for this policy. 
`--region`=`REGION`
     For resources [service_connection_policy, subnets], provides fallback value for resource region attribute. When the resource's full URI path is not provided, region will fallback to this flag value. 
Subnetwork resource - Subnetwork to use for IP address management. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--subnets` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `--subnets` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


`--subnets`=[`SUBNETS`,…]
     IDs of the subnetworks or fully qualified identifiers for the subnetworks. 

To set the `subnetwork` attribute: 

  * provide the argument `--subnets` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
