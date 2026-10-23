---
url: https://docs.cloud.google.com/vpc/docs/manage-composite-health/
title: View, update, and delete Composite Health resources \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:31.128579+00:00
---

# View, update, and delete Composite Health resources  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/manage-composite-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View, update, and delete Composite Health resources

This page describes how to manage your Composite Health resources after you have created them. You can list, describe, update, and delete health aggregation policies, health sources, and composite health checks.

## Manage health aggregation policies

This section describes how to manage health aggregation policies.

### List health aggregation policies

You can list the health aggregation policies that you have configured.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health aggregation policies**.




###  gcloud 

To list all health aggregation policies in a region, use the [`gcloud compute health-aggregation-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-aggregation-policies/list).
    
    
    gcloud compute health-aggregation-policies list \
        --regions=REGION
    

Replace `REGION` with the region of the health aggregation policies.

###  API 

To list all health aggregation policies in a region, send a request to the [`regionHealthAggregationPolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/list).

HTTP method and URL:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthAggregationPolicies
    

Replace the following:

  * `PROJECT_ID`: the project ID for the health aggregation policy.
  * `REGION`: the region of the health aggregation policies.



### Describe a health aggregation policy

You can describe a health aggregation policy to view its details.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health aggregation policies**.

  3. Click the name of the health aggregation policy that you want to describe.




###  gcloud 

Use the [`gcloud compute health-aggregation-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-aggregation-policies/describe).
    
    
    gcloud compute health-aggregation-policies describe POLICY \
        --region=REGION
    

Replace the following:

  * `POLICY`: the name of the health aggregation policy
  * `REGION`: the region of the health aggregation policy



###  API 

Send a request to the [`regionHealthAggregationPolicies.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/get).

HTTP method and URL:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthAggregationPolicies/POLICY
    

Replace the following:

  * `PROJECT_ID`: the project ID for the health aggregation policy.
  * `REGION`: the region of the health aggregation policy.
  * `POLICY`: the name of the health aggregation policy.



### Update a health aggregation policy

You can update the description, percentage healthy threshold, or minimum healthy threshold of a health aggregation policy.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health aggregation policies**.

  3. Click the name of the health aggregation policy that you want to update.

  4. Click edit **Edit**.

  5. Update the fields that you want to change.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud compute health-aggregation-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-aggregation-policies/update). Omit the flags for properties that you don't want to update.
    
    
    gcloud compute health-aggregation-policies update POLICY \
        --region=REGION \
        --description="DESCRIPTION" \
        --healthy-percent-threshold=PERCENT_HEALTHY \
        --min-healthy-threshold=MINIMUM_HEALTHY
    

Replace the following:

  * `POLICY`: the name of the health aggregation policy to update
  * `REGION`: the region of the health aggregation policy
  * `DESCRIPTION`: an updated description for the policy
  * `PERCENT_HEALTHY`: the updated minimum percentage of endpoints in a backend service that must be healthy for the health source to be considered healthy—for example, `75`
  * `MINIMUM_HEALTHY`: the updated minimum number of endpoints in a backend service that must be healthy for the health source to be considered healthy—for example, `2`



###  API 

  1. [Describe the health aggregation policy](https://docs.cloud.google.com/vpc/docs/manage-composite-health#describe-policy) and note the value for the `fingerprint` key, which you will use in the next step.

  2. Send a request to the [`regionHealthAggregationPolicies.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/patch). Omit the fields for properties that you don't want to update.

HTTP method and URL:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthAggregationPolicies/POLICY
         

Request JSON body:
         
         {
           "description": "DESCRIPTION",
           "healthyPercentThreshold": PERCENT_HEALTHY,
           "minHealthyThreshold": MINIMUM_HEALTHY,
           "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID for the health aggregation policy.
     * `REGION`: the region of the health aggregation policy.
     * `POLICY`: the name of the health aggregation policy to update.
     * `DESCRIPTION`: an updated description for the policy.
     * `PERCENT_HEALTHY`: the updated minimum percentage of endpoints in a backend service that must be healthy for the health source to be considered healthy—for example, `75`.
     * `MINIMUM_HEALTHY`: the updated minimum number of endpoints in a backend service that must be healthy for the health source to be considered healthy—for example, `2`.
     * `FINGERPRINT`: the up-to-date value for the `fingerprint` key that you found in the previous step.



### Delete a health aggregation policy

You can delete a health aggregation policy if it isn't associated with an existing health source.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health aggregation policies**.

  3. Select the checkbox next to the health aggregation policy that you want to delete.

  4. Click delete **Delete**.

  5. To confirm, click **Delete**.




###  gcloud 

Use the [`gcloud compute health-aggregation-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-aggregation-policies/delete).
    
    
    gcloud compute health-aggregation-policies delete POLICY \
        --region=REGION
    

Replace the following:

  * `POLICY`: the name of the health aggregation policy to delete
  * `REGION`: the region of the health aggregation policy



###  API 

Send a request to the [`regionHealthAggregationPolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthAggregationPolicies/delete).

HTTP method and URL:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthAggregationPolicies/POLICY
    

Replace the following:

  * `PROJECT_ID`: the project ID for the health aggregation policy.
  * `REGION`: the region of the health aggregation policy.
  * `POLICY`: the name of the health aggregation policy to delete.



## Manage health sources

The following sections describe how to manage your health sources.

### List health sources

You can list the health sources that you have configured.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health sources**.




###  gcloud 

To list all health sources in a region, use the [`gcloud compute health-sources list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-sources/list).
    
    
    gcloud compute health-sources list \
        --regions=REGION
    

Replace `REGION` with the region of the health sources.

###  API 

To list all health sources in a region, send a request to the [`regionHealthSources.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthSources/list).

HTTP method and URL:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthSources
    

Replace the following:

  * `PROJECT_ID`: the project ID for the health source.
  * `REGION`: the region of the health sources.



### Describe a health source

You can describe a health source to view its details.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health sources**.

  3. Click the name of the health source that you want to describe.




###  gcloud 

Use the [`gcloud compute health-sources describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-sources/describe).
    
    
    gcloud compute health-sources describe HEALTH_SOURCE \
        --region=REGION
    

Replace the following:

  * `HEALTH_SOURCE`: the name of the health source
  * `REGION`: the region of the health source



###  API 

Send a request to the [`regionHealthSources.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthSources/get).

HTTP method and URL:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthSources/HEALTH_SOURCE
    

Replace the following:

  * `PROJECT_ID`: the project ID for the health source.
  * `REGION`: the region of the health source.
  * `HEALTH_SOURCE`: the name of the health source.



### Update a health source

You can update the description, backend service, or health aggregation policy of an existing health source.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health sources**.

  3. Click the name of the health source that you want to update.

  4. Click edit **Edit**.

  5. Update the fields that you want to change.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud compute health-sources update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-sources/update). Omit the flags for properties that you don't want to update.
    
    
    gcloud compute health-sources update HEALTH_SOURCE \
        --region=REGION \
        --description="DESCRIPTION" \
        --sources=BACKEND_SERVICE \
        --health-aggregation-policy=POLICY
    

Replace the following:

  * `HEALTH_SOURCE`: the name of the health source to update
  * `REGION`: the region of the health source
  * `DESCRIPTION`: an updated description for the health source
  * `BACKEND_SERVICE`: the name of a backend service to use as the source of health

The backend service must fulfill the following requirements:

    * It must have a load balancing scheme of `INTERNAL` or `INTERNAL_MANAGED`.
    * It must be in the same region as the health source you are creating.
    * Its backends must be instance groups or network endpoint groups of type `GCE_VM_IP` or `GCE_VM_IP_PORT`.
  * `POLICY`: the name of an updated health aggregation policy to apply to this health source.




###  API 

  1. [Describe the health source](https://docs.cloud.google.com/vpc/docs/manage-composite-health#describe-source) and note the value for the `fingerprint` key, which you will use in the next step.
  2. Send a request to the [`regionHealthSources.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthSources/patch). Omit the fields for properties that you don't want to update.

HTTP method and URL:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthSources/HEALTH_SOURCE
         

Request JSON body:
         
         {
           "description": "DESCRIPTION",
           "sources": [
             "projects/PROJECT_ID/regions/REGION/backendServices/BACKEND_SERVICE"
           ],
           "healthAggregationPolicy": "projects/PROJECT_ID/regions/REGION/healthAggregationPolicies/POLICY",
           "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID for the health source.
     * `REGION`: the region of the health source.
     * `HEALTH_SOURCE`: the name of the health source to update.
     * `DESCRIPTION`: an updated description for the health source.
     * `BACKEND_SERVICE`: the name of a backend service to use as the source of health.

The backend service must fulfill the following requirements:

       * It must have a load balancing scheme of `INTERNAL` or `INTERNAL_MANAGED`.
       * It must be in the same region as the health source you are creating.
       * Its backends must be instance groups or network endpoint groups of type `GCE_VM_IP` or `GCE_VM_IP_PORT`.
     * `POLICY`: an updated health aggregation policy to apply to this health source.

     * `FINGERPRINT`: the up-to-date value for the `fingerprint` key that you found in the previous step.




### Delete a health source

You can delete a health source if it isn't associated with an existing composite health check.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Health sources**.

  3. Select the checkbox next to the health source that you want to delete.

  4. Click delete **Delete**.

  5. To confirm, click **Delete**.




###  gcloud 

Use the [`gcloud compute health-sources delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-sources/delete).
    
    
    gcloud compute health-sources delete HEALTH_SOURCE \
        --region=REGION
    

Replace the following:

  * `HEALTH_SOURCE`: the name of the health source to delete
  * `REGION`: the region of the health source



###  API 

Send a request to the [`regionHealthSources.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthSources/delete).

HTTP method and URL:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthSources/HEALTH_SOURCE
    

Replace the following:

  * `PROJECT_ID`: the project ID for the health source.
  * `REGION`: the region of the health source.
  * `HEALTH_SOURCE`: the name of the health source to delete.



## Manage composite health checks

The following sections describe how to manage your composite health checks.

### List composite health checks

You can list the composite health checks that you have configured.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Composite health checks**.




###  gcloud 

To list all composite health checks in a region, use the [`gcloud compute composite-health-checks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/composite-health-checks/list).
    
    
    gcloud compute composite-health-checks list \
        --regions=REGION
    

Replace `REGION` with the region of the composite health checks.

###  API 

To list all composite health checks in a region, send a request to the [`regionCompositeHealthChecks.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCompositeHealthChecks/list).

HTTP method and URL:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/compositeHealthChecks
    

Replace the following:

  * `PROJECT_ID`: the project ID for the composite health check.
  * `REGION`: the region of the composite health checks.



### Describe a composite health check

You can describe a composite health check to view its details.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Composite health checks**.

  3. Click the name of the composite health check that you want to describe.




###  gcloud 

Use the [`gcloud compute composite-health-checks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/composite-health-checks/describe).
    
    
    gcloud compute composite-health-checks describe COMPOSITE_HEALTH_CHECK \
        --region=REGION
    

Replace the following:

  * `COMPOSITE_HEALTH_CHECK`: the name of the composite health check
  * `REGION`: the region of the composite health check



###  API 

Send a request to the [`regionCompositeHealthChecks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCompositeHealthChecks/get).

HTTP method and URL:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/compositeHealthChecks/COMPOSITE_HEALTH_CHECK
    

Replace the following:

  * `PROJECT_ID`: the project ID for the composite health check.
  * `REGION`: the region of the composite health check.
  * `COMPOSITE_HEALTH_CHECK`: the name of the composite health check.



### Update a composite health check

You can update the description, health sources, or health destination of a composite health check.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Composite health checks**.

  3. Click the name of the composite health check that you want to update.

  4. Click edit **Edit**.

  5. Update the fields that you want to change.

  6. Click **Save**.




###  gcloud 

Use the [`gcloud compute composite-health-checks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/composite-health-checks/update). Omit the flags for properties that you don't want to update.
    
    
    gcloud compute composite-health-checks update COMPOSITE_HEALTH_CHECK \
        --region=REGION \
        --description="DESCRIPTION" \
        --health-sources=HEALTH_SOURCES \
        --health-destination=HEALTH_DESTINATION
    

Replace the following:

  * `COMPOSITE_HEALTH_CHECK`: the name of the composite health check to update
  * `REGION`: the region of the composite health check
  * `DESCRIPTION`: an updated description
  * `HEALTH_SOURCES`: the names of one or more health sources to associate with the composite health check

You can include multiple health sources in a comma-separated list.

  * `HEALTH_DESTINATION`: the URI of the forwarding rule that receives the composite health state from this composite health check—for example, `projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE`.

The forwarding rule must be associated with a producer load balancer that supports Composite Health and fulfills the following requirements:

    * It must have a load balancing scheme of `INTERNAL` or `INTERNAL_MANAGED`.
    * It must be in the same region as the composite health check.



###  API 

  1. [Describe the composite health check](https://docs.cloud.google.com/vpc/docs/manage-composite-health#describe-checks) and note the value for the `fingerprint` key, which you will use in the next step.

  2. Send a request to the [`regionCompositeHealthChecks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCompositeHealthChecks/patch). Omit the fields for properties that you don't want to update.

HTTP method and URL:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/compositeHealthChecks/COMPOSITE_HEALTH_CHECK
         

Request JSON body:
         
         {
           "description": "DESCRIPTION",
           "healthSources": [
             "projects/PROJECT_ID/regions/REGION/healthSources/HEALTH_SOURCE"
           ],
           "healthDestination": "projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE",
           "fingerprint": "FINGERPRINT"
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID for the composite health check.
     * `REGION`: the region of the composite health check.
     * `COMPOSITE_HEALTH_CHECK`: the name of the composite health check to update.
     * `DESCRIPTION`: an updated description.
     * `HEALTH_SOURCE`: the name of a health source to associate with the composite health check. To associate multiple health sources, add each source to the `healthSources` array.
     * `FORWARDING_RULE`: the forwarding rule that receives the composite health state from this composite health check.
     * `FINGERPRINT`: the up-to-date value for the `fingerprint` key that you found in the previous step.



### Delete a composite health check

You can delete a composite health check.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/composite-health/list)

  2. Click **Composite health checks**.

  3. Select the checkbox next to the composite health check that you want to delete.

  4. Click delete **Delete**.

  5. To confirm, click **Delete**.




###  gcloud 

Use the [`gcloud compute composite-health-checks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/composite-health-checks/delete).
    
    
    gcloud compute composite-health-checks delete COMPOSITE_HEALTH_CHECK \
        --region=REGION
    

Replace the following:

  * `COMPOSITE_HEALTH_CHECK`: the name of the composite health check to delete
  * `REGION`: the region of the composite health check



###  API 

Send a request to the [`regionCompositeHealthChecks.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCompositeHealthChecks/delete).

HTTP method and URL:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/compositeHealthChecks/COMPOSITE_HEALTH_CHECK
    

Replace the following:

  * `PROJECT_ID`: the project ID for the composite health check.
  * `COMPOSITE_HEALTH_CHECK`: the name of the composite health check to delete.
  * `REGION`: the region of the composite health check.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
