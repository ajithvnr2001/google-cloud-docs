---
url: https://docs.cloud.google.com/vpc/docs/configure-composite-health-failover/
title: Configure Composite Health for automatic cross-region failover \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:59:13.304610+00:00
---

# Configure Composite Health for automatic cross-region failover  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-composite-health-failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Composite Health for automatic cross-region failover

This page describes how service producers can configure Composite Health to support automatic cross-region failover for published services.

## Before you begin

  * Read about [Composite Health](https://docs.cloud.google.com/vpc/docs/about-composite-health).

  * In each region that you want to support, identify or create a [target service](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#lb-types) that meets the following requirements.

    * It must use one of the following internal load balancers: 
      * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)
      * [Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
      * [Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
    * It must use one of the following backend types: 
      * A [zonal network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts) with network endpoint type `GCE_VM_IP` or `GCE_VM_IP_PORT`
      * An [instance group](https://docs.cloud.google.com/compute/docs/instance-groups)

The steps to create your target services depend on the load balancer and backend types that you choose. For information on creating target services, see your load balancer's documentation.

  * Publish each target service by [creating a service attachment](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service).

  * Understand that to use Composite Health for failover, consumers must access your services with [load balancers that support cross-region failover](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#consumer-configuration-backends).

  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your project.

  * Verify that you have the permissions required to complete this guide.




### Required roles

To get the permissions that you need to configure Composite Health, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to configure Composite Health. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure Composite Health:

  * `compute.regionHealthAggregationPolicies.list`
  * `compute.regionHealthAggregationPolicies.get`
  * `compute.regionHealthAggregationPolicies.create`
  * `compute.regionHealthAggregationPolicies.update`
  * `compute.regionHealthAggregationPolicies.delete`
  * `compute.regionHealthSources.list`
  * `compute.regionHealthSources.get`
  * `compute.regionHealthSources.create`
  * `compute.regionHealthSources.update`
  * `compute.regionHealthSources.delete`
  * `compute.regionCompositeHealthChecks.list`
  * `compute.regionCompositeHealthChecks.get`
  * `compute.regionCompositeHealthChecks.create`
  * `compute.regionCompositeHealthChecks.update`
  * `compute.regionCompositeHealthChecks.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure Composite Health to support automatic cross-region failover

The following sections describe how to configure Composite Health for automatic cross-region failover.

While Composite Health doesn't require configuration by the service consumer, the feature only works if the consumer configures supported Private Service Connect backends in a multi-region deployment. For information about how a service consumer can configure their VPC network to use health Composite Health, see [Automatic cross-region failover](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends#failover).

### Create a health aggregation policy

Create at least one health aggregation policy in every region where you want to support cross-region failover.

A health aggregation policy is a reusable resource that defines the criteria for a backend service to be considered healthy. You can apply the same policy to multiple backend services, or create different policies for services that have different health requirements.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health aggregation policies**.

  3. Click **Create health aggregation policy**.

  4. Enter a name for the health aggregation policy.

  5. Optional: Enter a description of the policy.

  6. Click **Region** , and then select a region for the health aggregation policy.

  7. Click **Next**.

  8. In the **Healthy percent threshold** box, enter the minimum percentage of endpoints in a backend service that must be healthy for the health source to be considered healthy—for example, `75`.

  9. In the **Minimum healthy threshold** box, enter the minimum number of endpoints in a backend service that must be healthy for the health source to be considered healthy.

  10. Click **Create**.




###  gcloud 

Use the [`gcloud compute health-aggregation-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-aggregation-policies/create).
    
    
    gcloud compute health-aggregation-policies create POLICY \
        --region=REGION \
        --healthy-percent-threshold=PERCENT_HEALTHY \
        --min-healthy-threshold=MINIMUM_HEALTHY
    

Replace the following:

  * `POLICY`: the name of the health aggregation policy
  * `REGION`: the region of the health aggregation policy
  * `PERCENT_HEALTHY`: the minimum percentage of endpoints in a backend service that must be healthy for the health source to be considered healthy—for example, `75`

The default is `60`. Endpoints can be VMs in an instance group or network endpoints in a network endpoint group (NEG).

  * `MINIMUM_HEALTHY`: the minimum number of endpoints in a backend service that must be healthy for the health source to be considered healthy

The default is `1`.




###  API 

Send a request to the [`regionHealthAggregationPolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/insert).

HTTP method and URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthAggregationPolicies
    

Request JSON body:
    
    
    {
      "name": "POLICY",
      "policyType": "BACKEND_SERVICE_POLICY",
      "healthyPercentThreshold": PERCENT_HEALTHY,
      "minHealthyThreshold": MINIMUM_HEALTHY
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the health aggregation policy.
  * `REGION`: the region of the health aggregation policy.
  * `POLICY`: the name of the health aggregation policy.
  * `PERCENT_HEALTHY`: the minimum percentage of endpoints in a backend service that must be healthy for the health source to be considered healthy—for example, `75`.

The default is `60`. Endpoints can be VMs in an instance group or network endpoints in a network endpoint group (NEG).

  * `MINIMUM_HEALTHY`: the minimum number of endpoints in a backend service that must be healthy for the health source to be considered healthy.

The default is `1`.




### Create a health source

Create a health source for each regional instance of your published service. If an instance of your published service depends on the health of multiple backend services, create a separate health source for each of those backend services.

A health source is the resource that links a health aggregation policy to a specific backend service. A composite health check aggregates the health states from one or more health sources to produce a final composite health state for your service.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health sources**.

  3. Click **Create health source**.

  4. Enter a name for the health source.

  5. Optional: Enter a description of the health source.

  6. Click **Region** , and then select a region for the health source.

  7. Click **Next**.

  8. Click **Source** , and then select a backend service to associate with the health source.

  9. Click **Next**.

  10. Click **Health aggregation policy** , and then select the health aggregation policy to apply to this health source.

  11. Click **Create**.




###  gcloud 

Use the [`gcloud compute health-sources create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-sources/create).
    
    
    gcloud compute health-sources create HEALTH_SOURCE \
        --region=REGION \
        --source-type=BACKEND_SERVICE \
        --sources=BACKEND_SERVICE \
        --health-aggregation-policy=POLICY
    

Replace the following:

  * `HEALTH_SOURCE`: the name of the health source
  * `REGION`: the region of the health source

The health aggregation policy must be in the same region as the health source.

  * `BACKEND_SERVICE`: the name of a single backend service to associate with the health source

The backend service must fulfill the following requirements:

    * It must have a load balancing scheme of `INTERNAL` or `INTERNAL_MANAGED`.
    * It must be in the same region as the health source you are creating.
    * Its backends must be instance groups or network endpoint groups of type `GCE_VM_IP` or `GCE_VM_IP_PORT`.
  * `POLICY`: the name of the health aggregation policy to apply to this health source




###  API 

Send a request to the [`regionHealthSources.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthSources/insert).

HTTP method and URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthSources
    

Request JSON body:
    
    
    {
      "name": "HEALTH_SOURCE",
      "sourceType": "BACKEND_SERVICE",
      "sources": [
        "projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE"
      ],
      "healthAggregationPolicy": "projects/PROJECT_ID/regions/REGION/healthAggregationPolicies/POLICY"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the health source.
  * `REGION`: the region of the health source.

The health aggregation policy must be in the same region as the health source.

  * `HEALTH_SOURCE`: the name of the health source.

  * `BACKEND_SERVICE`: the name of a single backend service to associate with the health source.

The backend service must fulfill the following requirements:

    * It must have a load balancing scheme of `INTERNAL` or `INTERNAL_MANAGED`.
    * It must be in the same region as the health source you are creating.
    * Its backends must be instance groups or network endpoint groups of type `GCE_VM_IP` or `GCE_VM_IP_PORT`.
  * `POLICY`: the name of the health aggregation policy to apply to this health source.




### Create a composite health check

Create a composite health check for each regional instance of your published service.

A composite health check aggregates the health states of its associated health sources, creating a final composite health state. The final health state is applied to the regional published service that is associated with the forwarding rule that you specify as a health destination.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Composite health checks**.

  3. Click **Create composite health check**.

  4. Enter a name for the composite health check.

  5. Optional: Enter a description of the composite health check.

  6. Click **Region** , and then select a region for the composite health check.

  7. Click **Next**.

  8. Click **Health source** , and then select a health source to associate with the composite health check. You can add more health sources by clicking **Add health source** and then selecting another health source.

  9. Click **Next**.

  10. Click **Load balancer type** , and then select the type of load balancer to use as the health destination.

  11. Click **Load balancer** , and then select the load balancer to use as the health destination.

  12. If your load balancer is associated with multiple forwarding rules, click **Forwarding rule** , and then select the forwarding rule to use as the health destination.

  13. Click **Create**.




###  gcloud 

Use the [`gcloud compute composite-health-checks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/composite-health-checks/create).
    
    
    gcloud compute composite-health-checks create COMPOSITE_HEALTH_CHECK \
        --region=REGION \
        --health-sources=HEALTH_SOURCES \
        --health-destination=HEALTH_DESTINATION
    

Replace the following:

  * `COMPOSITE_HEALTH_CHECK`: the name of the composite health check
  * `REGION`: the region of the composite health check
  * `HEALTH_SOURCES`: the names of one or more health sources to associate with the composite health check

You can include multiple health sources in a comma-separated list.

  * `HEALTH_DESTINATION`: the URI of the forwarding rule that receives the composite health state from this composite health check—for example, `projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE`

The forwarding rule must be associated with a producer load balancer that supports Composite Health and fulfills the following requirements:

    * It must have a load balancing scheme of `INTERNAL` or `INTERNAL_MANAGED`.
    * It must be in the same region as the composite health check.



###  API 

Send a request to the [`regionCompositeHealthChecks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCompositeHealthChecks/insert).

HTTP method and URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/compositeHealthChecks
    

Request JSON body:
    
    
    {
      "name": "COMPOSITE_HEALTH_CHECK",
      "healthSources": [
        "projects/PROJECT_ID/regions/REGION/healthSources/HEALTH_SOURCE"
      ],
      "healthDestination": "HEALTH_DESTINATION"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the composite health check.
  * `REGION`: the region of the composite health check.
  * `COMPOSITE_HEALTH_CHECK`: the name of the composite health check.
  * `HEALTH_SOURCE`: the name of a health source to associate with the composite health check. You can include multiple health sources in the `healthSources` array.

  * `HEALTH_DESTINATION`: the URI of the forwarding rule that receives the composite health state from this composite health check—for example, `projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE`

The forwarding rule must be associated with a producer load balancer that supports Composite Health and fulfills the following requirements:

    * It must have a load balancing scheme of `INTERNAL` or `INTERNAL_MANAGED`.
    * It must be in the same region as the composite health check.



## What's next

  * To monitor your published service with Composite Health, see [Monitor Composite Health](https://docs.cloud.google.com/vpc/docs/monitor-composite-health).
  * To manage Composite Health configuration, see [View, update, and delete Composite Health configuration](https://docs.cloud.google.com/vpc/docs/manage-composite-health).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
