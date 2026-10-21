---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/service-lb-policies/create/
title: gcloud beta network-services service-lb-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:50:42.768786+00:00
---

# gcloud beta network-services service-lb-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/service-lb-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-services service-lb-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-services service-lb-policies create - create a service LB policy 
SYNOPSIS
    

`gcloud beta network-services service-lb-policies create` (`SERVICE_LB_POLICY` : `--location`=`LOCATION`) [`--async`] [`--auto-capacity-drain`] [`--description`=`DESCRIPTION`] [`--failover-health-threshold`=`FAILOVER_HEALTH_THRESHOLD`] [`--isolation-config-granularity`=`ISOLATION_CONFIG_GRANULARITY`; default="unspecified"] [`--isolation-config-mode`=`ISOLATION_CONFIG_MODE`; default="unspecified"] [`--load-balancing-algorithm`=`LOAD_BALANCING_ALGORITHM`; default="waterfall-by-region"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new service LB policy with the given name. 
EXAMPLES
     Create a service LB policy with the name 'my-service-lb-policy', load balancing algorithm 'waterfall-by-region', and location 'global'. 
    
    
    gcloud beta network-services service-lb-policies create my-service-lb-policy --load-balancing-algorithm=waterfall-by-region --location="global"

POSITIONAL ARGUMENTS
    

Service lb policy resource - Name of the service LB policy to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `service_lb_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SERVICE_LB_POLICY`
     ID of the service lb policy or fully qualified identifier for the service lb policy. 

To set the `service_lb_policy` attribute: 

  * provide the argument `service_lb_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. 

To set the `location` attribute: 

  * provide the argument `service_lb_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--auto-capacity-drain`
     If specified, an unhealthy MIG/NEG will be removed from Global load balancing and traffic routing for the service. A MIG/NEG is considered to be unhealthy if less than 25%% of the instance/endpoints in the MIG/NEG are healthy. autoCapacityDrain will never drain more than 50%% of the configured MIGs/NEGs of a Backend Service. 
`--description`=`DESCRIPTION`
     The description for the service LB policy. 
`--failover-health-threshold`=`FAILOVER_HEALTH_THRESHOLD`
     The percentage threshold that a load balancer will begin to send traffic to failover backends. If the percentage of endpoints in a MIG/NEG is smaller than this value, traffic would be sent to failover backends if possible. This field should be set to a value between 1 and 99. The default value is 50 for Proxyless service mesh, and 70 for others. 
`--isolation-config-granularity`=`ISOLATION_CONFIG_GRANULARITY`; default="unspecified"
     The granularity of the isolation. `ISOLATION_CONFIG_GRANULARITY` must be one of: 

`region`
     Traffic for this service will be isolated at the nearest cloud region. 
`unspecified`
     No isolation is configured for the backend service. Traffic can overflow based on the load balancing algorithm. 
`--isolation-config-mode`=`ISOLATION_CONFIG_MODE`; default="unspecified"
     The granularity of the isolation. `ISOLATION_CONFIG_MODE` must be one of: 

`nearest`
     Traffic will be sent to the nearest location. 
`strict`
     Traffic will fail if no serving backends are available in the same region as the load balancer. 
`unspecified`
     No isolation mode is configured for the backend service. 
`--load-balancing-algorithm`=`LOAD_BALANCING_ALGORITHM`; default="waterfall-by-region"
     The global load balancing algorithm to be used. `LOAD_BALANCING_ALGORITHM` must be one of: 

`spray-to-region`
     Spread the traffic from each client to all the MIGs/NEGs in a region. 
`spray-to-world`
     Balance traffic across all backends across the world proportionally based on capacity. 
`waterfall-by-region`
     Direct traffic to the nearest region with endpoints and capacity before spilling over to other regions. 
`waterfall-by-zone`
     Attempt to keep traffic in a single zone closest to the client, before spilling over to other zones. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-services service-lb-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/create)
    
    
    [gcloud alpha network-services service-lb-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/service-lb-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
