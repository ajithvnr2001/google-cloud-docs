---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/hosts/describe/
title: gcloud compute reservations hosts describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:23:59.446094+00:00
---

# gcloud compute reservations hosts describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/hosts/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute reservations hosts describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute reservations hosts describe - describe a Google Compute Engine host in a reservation 
SYNOPSIS
    

`gcloud compute reservations hosts describe` (`HOST_NAME` : `--association`=`ASSOCIATION` `--zone`=`ZONE`) [`--reservation`=`RESERVATION`] [`--reservation-block`=`RESERVATION_BLOCK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe a Google Compute Engine host in a reservation. 
EXAMPLES
     To describe a host named `my-host` in reservation `my-reservation` and zone `us-central1-a`: 
    
    
    gcloud compute reservations hosts describe my-host --reservation=my-reservation --zone=us-central1-a

POSITIONAL ARGUMENTS
    

Host resource - The name of the host to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `host_name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`HOST_NAME`
     ID of the host or fully qualified identifier for the host. 

To set the `host_name` attribute: 

  * provide the argument `host_name` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--association`=`ASSOCIATION`
     The association of the host. 

To set the `association` attribute: 

  * provide the argument `host_name` on the command line with a fully specified name; 
  * provide the argument `--association` on the command line; 
  * Fallback for association. 


`--zone`=`ZONE`
     The name of the Google Compute Engine zone. 

To set the `zone` attribute: 

  * provide the argument `host_name` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * set the property `compute/zone`. 


FLAGS
    

`--reservation`=`RESERVATION`
     Name of the reservation the host is associated with. 
`--reservation-block`=`RESERVATION_BLOCK`
     Name of the reservation block the host is associated with. This argument requires `--reservation` to be specified. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute reservations hosts describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/reservations/hosts/describe)
    
    
    [gcloud beta compute reservations hosts describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/hosts/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
