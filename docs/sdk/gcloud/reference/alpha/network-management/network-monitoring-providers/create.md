---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/create/
title: gcloud alpha network-management network-monitoring-providers create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:12:43.939336+00:00
---

# gcloud alpha network-management network-monitoring-providers create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-management network-monitoring-providers create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-management network-monitoring-providers create - create a Network Monitoring Provider 
SYNOPSIS
    

`gcloud alpha network-management network-monitoring-providers create` (`NETWORK_MONITORING_PROVIDER` : `--location`=`LOCATION`) `--provider-type`=`PROVIDER_TYPE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Network Monitoring Provider. 

To create this resource for the first time in a Google Cloud project, you must use the Cloud Console to accept the Broadcom Terms of Service (TOS). 

Note: The only supported location for these resources is `global`. 

EXAMPLES
     To create a Network Monitoring Provider `my-provider-id` of type `EXTERNAL`, run: 
    
    
    [gcloud alpha network-management network-monitoring-providers](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-management/network-monitoring-providers) create my-provider-id --location=global --provider-type=EXTERNAL

POSITIONAL ARGUMENTS
    

NetworkMonitoringProvider resource - Identifier. Name of the resource. Format: `projects/{project}/locations/{location}/networkMonitoringProviders/{network_monitoring_provider}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `network_monitoring_provider` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`NETWORK_MONITORING_PROVIDER`
     ID of the networkMonitoringProvider or fully qualified identifier for the networkMonitoringProvider. 

To set the `network_monitoring_provider` attribute: 

  * provide the argument `network_monitoring_provider` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the networkMonitoringProvider resource. 

To set the `location` attribute: 

  * provide the argument `network_monitoring_provider` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--provider-type`=`PROVIDER_TYPE`
     Type of the NetworkMonitoringProvider. `PROVIDER_TYPE` must be (only one value is supported): 

`external`
     External provider. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkmanagement/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud network-management network-monitoring-providers create](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/network-monitoring-providers/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
