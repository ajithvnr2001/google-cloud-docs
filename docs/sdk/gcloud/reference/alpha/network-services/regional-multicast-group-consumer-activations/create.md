---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/regional-multicast-group-consumer-activations/create/
title: gcloud alpha network-services regional-multicast-group-consumer-activations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:37.661920+00:00
---

# gcloud alpha network-services regional-multicast-group-consumer-activations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/regional-multicast-group-consumer-activations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-services regional-multicast-group-consumer-activations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-services regional-multicast-group-consumer-activations create - create a regional multicast group consumer activation 
SYNOPSIS
    

`gcloud alpha network-services regional-multicast-group-consumer-activations create` (`REGIONAL_MULTICAST_GROUP_CONSUMER_ACTIVATION` : `--location`=`LOCATION`) `--regional-multicast-consumer-association`=`REGIONAL_MULTICAST_CONSUMER_ASSOCIATION` `--regional-multicast-group-range-activation`=`REGIONAL_MULTICAST_GROUP_RANGE_ACTIVATION` [`--async`] [`--description`=`DESCRIPTION`] [`--[no-]enable-logging`] [`--interconnect-attachments`=[`INTERCONNECT_ATTACHMENTS`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a regional multicast group consumer activation in the specified location of the current project. 
EXAMPLES
     Create a regional multicast group consumer activation with the name 'my-rmgca', regional-multicast-group-range-activation 'path-to-rmgra', multicast-consumer-association 'path-to-rmca', and location 'region'. 
    
    
    [gcloud alpha network-services](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services) regional-multicast-group-consumer-activations create my-rmgca --regional-multicast-group-range-activation=path-to-rmgra --regional-multicast-consumer-association=path-to-rmca --location=region

POSITIONAL ARGUMENTS
    

Regional multicast group consumer activation resource - Name of the regional multicast group consumer activation to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `regional_multicast_group_consumer_activation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REGIONAL_MULTICAST_GROUP_CONSUMER_ACTIVATION`
     ID of the regional multicast group consumer activation or fully qualified identifier for the regional multicast group consumer activation. 

To set the `regional_multicast_group_consumer_activation` attribute: 

  * provide the argument `regional_multicast_group_consumer_activation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. 

To set the `location` attribute: 

  * provide the argument `regional_multicast_group_consumer_activation` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--regional-multicast-consumer-association`=`REGIONAL_MULTICAST_CONSUMER_ASSOCIATION`
     The regional multicast consumer association to be used. 
`--regional-multicast-group-range-activation`=`REGIONAL_MULTICAST_GROUP_RANGE_ACTIVATION`
     The regional multicast group range activation to be used. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description for the regional multicast group consumer activation. 
`--[no-]enable-logging`
     Whether to enable logging for this regional multicast group consumer activation. Use `--enable-logging` to enable and `--no-enable-logging` to disable. 
`--interconnect-attachments`=[`INTERCONNECT_ATTACHMENTS`,…]
     The interconnect attachments to be used. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
