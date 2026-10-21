---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/multicast-domain-activations/create/
title: gcloud alpha network-services multicast-domain-activations create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:29.557220+00:00
---

# gcloud alpha network-services multicast-domain-activations create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/multicast-domain-activations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-services multicast-domain-activations create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-services multicast-domain-activations create - create a multicast domain activation 
SYNOPSIS
    

`gcloud alpha network-services multicast-domain-activations create` (`MULTICAST_DOMAIN_ACTIVATION` : `--location`=`LOCATION`) `--multicast-domain`=`MULTICAST_DOMAIN` [`--async`] [`--description`=`DESCRIPTION`] [`--disable-placement-policy`] [`--labels`=[`KEY`=`VALUE`,…]] [`--aggr-egress-pps`=`AGGR_EGRESS_PPS` : `--aggr-ingress-pps`=`AGGR_INGRESS_PPS` `--avg-packet-size`=`AVG_PACKET_SIZE` `--max-per-group-ingress-pps`=`MAX_PER_GROUP_INGRESS_PPS` `--max-per-group-subscribers`=`MAX_PER_GROUP_SUBSCRIBERS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a multicast domain activation in the specified location of the current project. 
EXAMPLES
     Create a multicast domain activation with the name 'my-multicast-domain-activation', multicast-domain 'path-to-md', and location 'zone'. 
    
    
    [gcloud alpha network-services multicast-domain-activations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/multicast-domain-activations) create my-multicast-domain-activation --multicast-domain=path-to-md --location=zone

POSITIONAL ARGUMENTS
    

Multicast domain activation resource - Name of the multicast domain activation to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `multicast_domain_activation` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MULTICAST_DOMAIN_ACTIVATION`
     ID of the multicast domain activation or fully qualified identifier for the multicast domain activation. 

To set the `multicast_domain_activation` attribute: 

  * provide the argument `multicast_domain_activation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. 

To set the `location` attribute: 

  * provide the argument `multicast_domain_activation` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--multicast-domain`=`MULTICAST_DOMAIN`
     The multicast domain to be used. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description for the multicast domain activation. 
`--disable-placement-policy`
     True to disable the use of the placement policy for this multicast domain activation. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--aggr-egress-pps`=`AGGR_EGRESS_PPS`
     Aggregated egress Packet-Per-Second for all multicast groups in the domain in this zone. 
`--aggr-ingress-pps`=`AGGR_INGRESS_PPS`
     Aggregated ingress Packet-Per-Second for all multicast groups in the domain in this zone. 
`--avg-packet-size`=`AVG_PACKET_SIZE`
     Average packet size (defaults to 512 bytes). 
`--max-per-group-ingress-pps`=`MAX_PER_GROUP_INGRESS_PPS`
     Maximum ingress Packet-Per-Second for a single multicast group in this zone. 
`--max-per-group-subscribers`=`MAX_PER_GROUP_SUBSCRIBERS`
     Maximum number of subscribers for a single multicast group in this zone. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud network-services multicast-domain-activations create](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-activations/create)
    
    
    [gcloud beta network-services multicast-domain-activations create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/multicast-domain-activations/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
