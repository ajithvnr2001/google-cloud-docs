---
url: https://docs.cloud.google.com/vpc/docs/about-service-connection-policies/
title: About service connection policies \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:54.047901+00:00
---

# About service connection policies  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/about-service-connection-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About service connection policies

This document explains how network administrators can use service connection policies to provide connectivity to supported managed service instances through service connectivity automation. Before reading this document, ensure that you're familiar with the concepts explained in [About service connectivity automation](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation).

## Specifications

Service connection policies have the following specifications:

  * You can create only one service connection policy for each combination of network, region, and [service class](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#service-class). For example, you can have only one service connection policy for `vpc1` in `us-central1` for `google-cloud-sql`. This validation means that only one service connection policy governs a given Private Service Connect endpoint.

  * Service instance administrators can use the service's administrative API or UI to deploy that service and configure connectivity by using service connectivity automation.

  * If the creation or deletion of an endpoint through service connectivity automation is blocked, an [automated process periodically retries the operation](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#endpoint-automation) until the blocking issue is resolved.

  * The subnets that are included in the service connection policy configuration provide IP addresses that are assigned to Private Service Connect endpoints. These IP addresses are automatically allocated and returned to the subnet's pool as managed service instances are created and deleted.

The subnets must be [regular subnets](https://docs.cloud.google.com/vpc/docs/subnets#purpose), and they must be in the same region as the service connection policy. Regular subnets are different from Private Service Connect subnets.

As a best practice, we recommend that you avoid using the subnets for other resources. If other resources consume IP addresses from the subnet, you might run out of IP addresses to assign to endpoints.

  * Managed services that use service connection policies might support connecting to service instances by using IPv4 endpoints, IPv6 endpoints, or both. If the service supports both IPv4 and IPv6, service instance administrators can choose an IP version when deploying a service instance.

  * You can use service connection policies with Shared VPC.

  * By default, the service instance and the endpoints that connect to the service instance must be in the same project (or in the case of Shared VPC, in connected projects).

Supported Google services let you configure a custom service instance scope.

  * Endpoints that are created through service connectivity automation might have labels applied to them by the service producer. For more information about labels, see [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources).

  * If you want to use Private Service Connect service automation with multiple VPC networks that are in the same project, create a service connection policy for each network.

  * You can optionally configure a connection limit to specify the maximum number of Private Service Connect connections that a given service producer can create in the policy's VPC network and region.

  * Endpoints that are created through service connection policies can be made available in other VPC networks through [connection propagation](https://docs.cloud.google.com/vpc/docs/about-propagated-connections).




## Authorization

Service connection policies let consumers delegate the deployment of connectivity to managed services. The service producer doesn't have direct access or IAM privileges for the consumer project. Instead, the producer configures a service connection map in their own project.

When the service connection map is created or updated, typically in response to a request from a consumer service administrator to the managed service's administrative API or UI, service connectivity automation performs a series of authorization checks. If all of the checks pass, Private Service Connect endpoints are created as specified in the request.

For information about authorization, see [Authorization model](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#authorization).

## Connection policies in Shared VPC networks

Service connection policies can automate connectivity to service instances that are located in host projects or in attached service projects.

If you're using Shared VPC, you must create the service connection policy in the host project. Endpoints are created in the project that is specified in the service instance configuration.

If you create a service connection policy in a Shared VPC network and deploy a service instance in a service project, service connectivity automation shares the subnets that are associated with the service connection policy by updating the service project's [Network Connectivity Service Account](https://docs.cloud.google.com/iam/docs/service-agents#network-connectivity-service-account). This service account is granted the [Compute Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) on the shared subnets.

For a deployment example, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#shared-vpc).

## Connection policies with custom service instance scope

By default, service connectivity automation creates endpoints for service instances and associated service connection policies that are in the same Google Cloud project (or in the case of Shared VPC, in connected projects). For supported Google services, service instances and connecting endpoints can also be in different projects or organizations.

Not all Google services support configuring a custom service instance scope. To determine whether a service supports a custom service instance scope, see the documentation for the specific service.

Use the **Service instance scope** (`--producer-instance-location`) setting to configure connectivity to service instances that are in other Resource Manager nodes (projects, folders, and organizations).

  * If it's set to `no_producer_instance_location`, endpoints are created in the same project only. This is the default value.
  * If it's set to `custom_resource_hierarchy_levels`, you specify the list of Resource Manager nodes in the `--allowed-google-producers-resource-hierarchy-level` field.



If you update the service instance scope for a service connection policy, existing endpoints aren't affected.

For a deployment example, see [Google services with custom service instance scope](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation#google-custom-scope).

## Endpoint IP versions

The possible IP versions of endpoints that connect to service instances (IPv4, IPv6, or both) is determined by the service producer, not by service connectivity automation. If the service supports both IPv4 and IPv6, service instance administrators can choose an IP version when deploying an instance through a service's administrative API. For information about a service's supported IP versions, see the service's documentation.

When a service instance administrator chooses an IP version, service connectivity automation checks the service connection policy for compatible subnets to use for creating endpoint IP addresses:

  * IPv4-only subnets support IPv4 endpoints.
  * Dual-stack subnets support both IPv4 and IPv6 endpoints.
  * IPv6-only subnets support IPv6 endpoints.



If the service connection policy doesn't have a compatible subnet, the request fails, and no endpoint is created.

Additionally, the IP version of the endpoint must be compatible with the IP version of the service instance, which is determined by the associated service attachment's forwarding rule. Private Service Connect supports the following IP version combinations:

  * IPv4 endpoint to IPv4 service attachment
  * IPv6 endpoint to IPv6 service attachment
  * IPv6 endpoint to IPv4 service attachment

In this configuration, Private Service Connect automatically translates between the two IP versions.




Connecting an IPv4 endpoint to an IPv6 service attachment isn't supported.

If you want to let both IPv4 and IPv6 clients access a managed service instance, configure connectivity for separate IPv4 and IPv6 endpoints that connect to the same service.

## Limitations

  * Service connection policies only support automating the creation of Private Service Connect endpoints. Creating Private Service Connect backends or service attachments isn't supported.
  * You cannot directly delete Private Service Connect endpoints that are created through service connectivity automation. To trigger deletion of these endpoints, [decommission service connectivity](https://docs.cloud.google.com/vpc/docs/deploy-service-instance-service-connection-policies#decommission-service).
  * You can only update the subnets and connection limit for a service connection policy. If you want to update other fields, [delete the policy](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#delete-policy) and [create a new one](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies#create-policy).



## Pricing

Pricing for Private Service Connect is described on the [VPC pricing page](https://cloud.google.com/vpc/pricing#psc-automation).

## What's next

  * [Configure service connection policies](https://docs.cloud.google.com/vpc/docs/configure-service-connection-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
