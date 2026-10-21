---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/linked-producer-vpc-network/create/
title: gcloud beta network-connectivity spokes linked-producer-vpc-network create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:42:24.442738+00:00
---

# gcloud beta network-connectivity spokes linked-producer-vpc-network create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes/linked-producer-vpc-network/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-connectivity spokes linked-producer-vpc-network create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-connectivity spokes linked-producer-vpc-network create - create a new Producer VPC spoke 
SYNOPSIS
    

`gcloud beta network-connectivity spokes linked-producer-vpc-network create` `SPOKE` `--hub`=`HUB` `--network`=`NETWORK` `--peering`=`PEERING` [`--async`] [`--description`=`DESCRIPTION`] [`--exclude-export-ranges`=[`CIDR_RANGE`,…]] [`--global`] [`--group`=`GROUP`] [`--include-export-ranges`=[`CIDR_RANGE`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new Producer VPC spoke. 
EXAMPLES
     To create a Producer VPC spoke named ``myspoke``, run: 
    
    
    [gcloud beta network-connectivity spokes](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/spokes) linked-producer-vpc-network create myspoke --hub=https://www.googleapis.com/networkconnectivity/v1/projects/my-project/locations/global/hubs/my-hub --global --network=https://www.googleapis.com/compute/v1/projects/my-project/global/networks/my-vpc --peering=my-peering-name

POSITIONAL ARGUMENTS
    

Spoke resource - Name of the spoke to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `spoke` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `spoke` on the command line with a fully specified name; 
  * provide the argument `--global` on the command line. 



This must be specified. 

`SPOKE`
     ID of the spoke or fully qualified identifier for the spoke. 

To set the `spoke` attribute: 

  * provide the argument `spoke` on the command line. 


REQUIRED FLAGS
    

`--hub`=`HUB`
     Hub that the spoke will attach to. The hub must already exist. 
`--network`=`NETWORK`
     Your VPC network that contains the peering to the Producer VPC, which this spoke connects to the Hub. The peering must already exist and be in the ACTIVE state. 
`--peering`=`PEERING`
     Peering between your network and the Producer VPC, which this spoke connects to the Hub. The peering must already exist and be in the ACTIVATE state. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the spoke to create. 
`--exclude-export-ranges`=[`CIDR_RANGE`,…]
     Subnet IP address range(s) to hide from other VPC networks that are connected through Network Connectivity Center. 
`--global`
     Indicates that the spoke is global. 
`--group`=`GROUP`
     Group that the spoke will be part of. The group must already exist. 
`--include-export-ranges`=[`CIDR_RANGE`,…]
     Subnet IP address range(s) to export to other VPC networks that are connected through Network Connectivity Center. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the networkconnectivity/v1 API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud network-connectivity spokes linked-producer-vpc-network](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network) create

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
