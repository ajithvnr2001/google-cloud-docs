---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/vpc-peerings/get-vpc-service-controls/
title: gcloud beta services vpc-peerings get-vpc-service-controls \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:44.026738+00:00
---

# gcloud beta services vpc-peerings get-vpc-service-controls  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/vpc-peerings/get-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta services vpc-peerings get-vpc-service-controls Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta services vpc-peerings get-vpc-service-controls - get VPC state of Service Controls for the peering connection 
SYNOPSIS
    

`gcloud beta services vpc-peerings get-vpc-service-controls` `--network`=`NETWORK` [`--service`=`SERVICE`; default="servicenetworking.googleapis.com"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command provides the state of the VPC Service Controls for a connection. The state can be enabled or disabled. 

When enabled, Google Cloud makes the following route configuration changes in the service producer VPC network: Google Cloud removes the IPv4 default route (destination 0.0.0.0/0, next hop default internet gateway), Google Cloud then creates an IPv4 route for destination 199.36.153.4/30 using the default internet gateway next hop. 

When enabled, Google Cloud also creates Cloud DNS managed private zones and authorizes those zones for the service producer VPC network. The zones include googleapis.com, gcr.io, pkg.dev, notebooks.cloud.google.com, kernels.googleusercontent.com, backupdr.cloud.google.com, and backupdr.googleusercontent.com as necessary domains or host names for Google APIs and services that are compatible with VPC Service Controls. Record data in the zones resolves all host names to 199.36.153.4, 199.36.153.5, 199.36.153.6, and 199.36.153.7. 

When disabled, Google Cloud makes the following route configuration changes in the service producer VPC network: Google Cloud restores a default route (destination 0.0.0.0/0, next hop default internet gateway), Google Cloud also deletes the Cloud DNS managed private zones that provided the host name overrides. 

While enabled, the service producer VPC network can still import static and dynamic routes from the peered customer network if you enable custom route export. These custom routes can include a default route. For this reason, this command is not to be used solely as a means for preventing access to the internet. 

EXAMPLES
     To get the status of the VPC Service Controls for a connection peering a network called `my-network` on the current project to a service called `your-service`, run: 
    
    
    gcloud beta services vpc-peerings get-vpc-service-controls --network=my-network --service=your-service

REQUIRED FLAGS
    

`--network`=`NETWORK`
     The network in the current project that is peered with the service. 
OPTIONAL FLAGS
    

`--service`=`SERVICE`; default="servicenetworking.googleapis.com"
     The service to get VPC service controls for. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud services vpc-peerings get-vpc-service-controls](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/get-vpc-service-controls)
    
    
    [gcloud alpha services vpc-peerings get-vpc-service-controls](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/vpc-peerings/get-vpc-service-controls)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
