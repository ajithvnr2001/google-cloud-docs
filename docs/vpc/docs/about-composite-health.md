---
url: https://docs.cloud.google.com/vpc/docs/about-composite-health/
title: About Composite Health for automatic cross-region failover \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:11.744622+00:00
---

# About Composite Health for automatic cross-region failover  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-composite-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About Composite Health for automatic cross-region failover

Composite Health lets service producers define criteria that determine health states for regional published services. These health states support automatic cross-region failover for service consumers that use Private Service Connect backends. The health states are based on the aggregated health of the service producer's backends (VMs or network endpoints), providing consumers with a more accurate failover signal than [outlier detection](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#outlier-detection), which infers health from response failures.

To enable cross-region failover, both the service producer and consumer must use a multi-region deployment. When you configure Composite Health, the health state of each regional published service is automatically propagated to the consumer's load balancer. If a published service in one region becomes unhealthy, the consumer's load balancer stops routing traffic to that service and instead routes traffic to a healthy instance of the published service that is in an alternate region.

## Deployment requirements

This section describes how service producers and service consumers can configure their resources for a multi-region deployment that supports automatic cross-region failover with Composite Health.

For more information about requirements for load balancer and backend types, see Specifications.

**Producer configuration** :

  * Deploy the service in each region. Each regional instance of the service must be configured on a regional load balancer that [supports access by a backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#producer-configuration-backends). 
  * [Create a service attachment](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service) to publish each regional instance of the service.



**Consumer configuration** :

  * [Create a Private Service Connect backend to access published services](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls). The backend must be based on a [load balancer that supports cross-region failover](https://docs.cloud.google.com/vpc/docs/private-service-connect-compatibility#consumer-configuration-backends) and includes the following configuration: 
    * A [ Private Service Connect NEG](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls#create-neg) in each region that points to that region's service attachment
    * A global backend service that contains the Private Service Connect NEG backends



The following diagram shows a multi-region deployment:

[ ![A multi-region deployment consists of a
  consumer load balancer that connects to services published in multiple regions
  using Private Service Connect.](https://docs.cloud.google.com/static/vpc/images/private-service-connect-global-xlb-services.png)](https://docs.cloud.google.com/static/vpc/images/private-service-connect-global-xlb-services.png)

This example shows a consumer global external Application Load Balancer that connects to a service that is published in multiple regions. Accessing a multi-region service with a supported global or cross-regional load balancer lets the service consumer take advantage of Composite Health for automatic cross-region failover (click to enlarge).

## Composite Health components

Composite Health uses the following components to support automatic cross-region failover.

[ ![Multiple health sources, each with a health aggregation policy,
  are combined in a composite health check, which updates the Health Destination.](https://docs.cloud.google.com/static/vpc/images/service-health-component.svg)](https://docs.cloud.google.com/static/vpc/images/service-health-component.svg)

The preceding diagram shows the key components of Composite Health. Health aggregation policies define conditions for health sources to be considered healthy. Health states for individual health sources are combined into a single state by a composite health check, and the result is delivered to a health destination. 

### Health aggregation policy

A _health aggregation policy_ is a resource that you create to define the conditions that a backend service must meet to be considered healthy. A policy aggregates the health states of a backend service's backends (VMs in an instance group or network endpoints in a NEG), as determined by regular [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

A backend service is considered healthy if two configurable conditions are met:

  * **Percentage of healthy endpoints** : The minimum percentage of backends that must be healthy. The default is 60%.

  * **Minimum number of healthy endpoints** : The minimum number of backends that must be healthy. The default value is 1.




For example, you can create a policy that specifies a backend service must have at least 75% of its backends healthy and at least three healthy backends. If the number of healthy backends falls below either of those thresholds, the backend service is considered unhealthy.

### Health source

A _health source_ is a resource that makes the health of a single backend service available for aggregation as part of a composite health check. When you create a health source, you specify the following:

  * A backend service to monitor
  * A health aggregation policy that determines the backend service's health



The health source uses the conditions defined in the health aggregation policy to determine the health state of the associated backend service.

### Composite health check

A _composite health check_ is a resource that aggregates the health states of one or more health sources to produce a single composite health state for a regional published service. The published service is considered healthy if each of the associated health sources are healthy. If any of the health sources are unhealthy, the service is considered unhealthy.

### Health destination

A _health destination_ receives the final composite health state from a composite health check. For a published service, the health destination is the forwarding rule of the producer's load balancer. The health state is automatically propagated to consumer load balancers that connect to this forwarding rule.

## Specifications

Composite Health has the following specifications.

  * **Behavior** :

    * The health of individual backends within a backend service is determined by standard health checks.
    * A configurable health aggregation policy determines the overall health state of a backend service based on the health of its individual backends.
    * A composite health check aggregates the health states from one or more backend services that are configured as health sources, creating a composite health state.
    * The composite health state is provided to a health destination, which must be the forwarding rule of a published service.
    * The composite health state is automatically propagated to connected consumer load balancers, where unhealthy states trigger automatic cross-region failover.
    * By default, health state transitions are recorded by [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). Producers can view logs for health sources and composite health checks. Consumers can view logs for Private Service Connect NEGs that connect to published services that use Composite Health. For more information, see [Monitor Composite Health](https://docs.cloud.google.com/vpc/docs/monitor-composite-health).
  * **Configuration** :

    * The service producer and consumer must configure resources in a multi-region deployment.
    * Each regional published service must use a [load balancer that supports Composite Health](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#producer-configuration-backends).
    * Backend services that you use as health sources must have a load balancing scheme of `INTERNAL` or `INTERNAL_MANAGED`.
    * Published services must have one of the following backend types: 
      * [Network endpoint group of type `GCE_VM_IP_PORT`](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#gce-vm-ip-port-endpoint-spec)
      * [Network endpoint group of type `GCE_VM_IP`](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#gce-vm-ip-endpoint-spec)
      * [Managed or unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups)
    * The published services must be accessed by Private Service Connect backends that use [load balancers that support cross-region failover](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#consumer-configuration-backends).
    * All Composite Health resources are regional and must be in the same region as the published service that you are monitoring.
    * A health source resource must reference exactly one backend service.
    * A composite health check resource must reference from 1 to 10 health sources.
    * A forwarding rule can be the health destination for only one composite health check.



## Health states

Composite Health uses the following states to represent the health of published services and backend services.

Health state | Monitored resource | Description  
---|---|---  
`HEALTHY` | Health source | The associated backend service is healthy as defined by its health aggregation policy.  
Composite health check | The published service is healthy because each of its associated health sources is healthy.  
Private Service Connect NEG | The associated published service is healthy as defined by the producer's composite health check.  
`UNHEALTHY` | Health source | The backend service does not meet the criteria defined by its health aggregation policy.  
Composite health check | The published service is unhealthy because one or more of the associated health sources are unhealthy.  
Private Service Connect NEG | The associated published service is unhealthy as defined by the producer's composite health check; this status can trigger cross-region failover.  
`UNKNOWN` | Health source | The health state is not available yet. This is a transient state that occurs when resources are newly created or configured.  
Composite health check | No associated health sources are unhealthy, but one or more health sources are unknown.  
Private Service Connect NEG | The health state of the associated published service is not available yet.  
  
## Limitations

Composite Health has the following limitations:

  * All Composite Health resources, including the backend services and forwarding rules they reference, must exist in the same project.
  * You can't use the composite health state of one service as a health source for another service.
  * There is no mode to test a health check configuration that doesn't affect connected consumers. Any configured composite health checks can immediately trigger failover.
  * Composite Health only supports Private Service Connect backends that access published services.



## Pricing

For information about pricing, see [VPC pricing](https://cloud.google.com/vpc/pricing).

## What's next

  * To configure Composite Health, see [Configure Composite Health for automatic cross-region failover](https://docs.cloud.google.com/vpc/docs/configure-composite-health-failover).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
