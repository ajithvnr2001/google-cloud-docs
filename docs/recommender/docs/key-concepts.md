---
url: https://docs.cloud.google.com/recommender/docs/key-concepts/
title: Recommendations \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:52.507325+00:00
---

# Recommendations  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/key-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Recommendations

## Recommenders

A _recommender_ is a service on Google Cloud that provides optimization recommendations for Google Cloud products and resources.

Each recommender lets you view and manage its recommendations and insights using the REST API and Google Cloud CLI. Some recommenders also let you view and manage their recommendations and insights using one or more of the following options:

  * Active Assist
  * [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub), which provides cost-optimization recommendations for billing account managers.
  * The Optimization page in [Cloud Hub](https://docs.cloud.google.com/hub/docs/optimize), which provides cost-optimization recommendations for developers and platform administrators.
  * _In context_ using the service's user interface (UI) in the Google Cloud console



For details about recommenders and supported clients, see [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders).

Each recommender has a unique recommender ID that identifies the service. You use the recommender ID when interacting with recommendations using the Recommender [`gcloud`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender) commands, or the [REST](https://docs.cloud.google.com/recommender/docs/reference/rest) or [RPC](https://docs.cloud.google.com/recommender/docs/reference/rpc) APIs.

For more information, see [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders).

## Recommendations

A _recommendation_ is a machine-generated suggestion for optimizing your usage of Cloud resources. It includes the steps required to take action on the recommendation. Recommenders provide recommendations based on your resource usage, using machine learning or heuristics. Recommender stores recommendations using the [`Recommendation`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#resource-recommendation) entity.

A recommendation has the following core attributes:

  * Name
  * Description
  * Recommender subtype
  * Impact
  * Operation
  * Operation groups
  * State info
  * etag
  * Priority
  * State metadata
  * Last refresh time
  * Insight reference
  * Configuration



### Name

The recommendation name is stored in the `name` field of the `Recommendation` entity. This is the name for the recommendation in the following format:
    
    
    projects/TARGET_PROJECT_ID/locations/LOCATION/recommenders/RECOMMENDER_ID/recommendations/RECOMMENDATION_ID
    

where:

  * TARGET_PROJECT_ID is the ID of the project where the recommendation was made.
  * LOCATION is the Google Cloud [location](https://cloud.google.com/about/locations) where resources associated with the recommendations are located (for example, `global` or `us-central1-a`).
  * RECOMMENDER_ID is the fully-qualified [recommender ID](https://docs.cloud.google.com/recommender/docs/recommenders#recommenders) (for example, `google.compute.instance.MachineTypeRecommender`).
  * RECOMMENDATION_ID is a unique ID for the recommendation.



### Description

The recommendation description is stored in the `description` field of the `Recommendation` entity. It is only available in English. This is human-readable text that describes the recommendation. In the Google Cloud console, the description appears when you click to view additional recommendation details.

### Recommender subtype

A recommender might have subtypes for specific kinds of recommendations. For example, the Identity and Access Management role recommender has the subtypes `REPLACE_ROLE` and `REMOVE_ROLE`. New subtypes might be introduced to the existing recommenders over time. This [overview](https://docs.cloud.google.com/recommender/docs/recommenders) provides a list of all available recommenders. Refer to the recommender documentation to get more information about the recommendation subtypes available. 

### Recommender impact

An impact quantifies the projected benefits of performing the recommended action. Each recommendation can have the following types of impact that represent outcomes that can occur as a result of applying the recommendation:

  * The primary impact is mandatory and is stored in the `primaryImpact` field of the `Recommendation` entity.

  * Secondary impact(s) are optional and stored in the `additionalImpact` field.




There are the following types of primary and secondary impact:

  * **`COST`** : Estimated amount of money that you are projected to save (or incur) if you apply a given recommendation. Refer to the `cost` field under [_CostProjection_](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/billingAccounts.locations.recommenders.recommendations#costprojection) for details.

  * **`PERFORMANCE`** : Estimated increase or decrease in performance. Please note that some performance recommendations can result in additional cost (for example, if a recommendation is to increase CPU or memory allocation on an overutilized VM).

  * **`SECURITY`** : Estimated improvement in security posture. Refer to the `details` field under [_SecurityProjection_](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/billingAccounts.locations.recommenders.recommendations#costprojection) for details.

  * **`MANAGEABILITY`** : Estimated reduction in manual toil.

  * **`SUSTAINABILITY`** : Estimated reduction in carbon emissions. Refer to the `carbon_footprint_kg_co2` field under [_SustainabilityProjection_](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/billingAccounts.locations.recommenders.recommendations#sustainabilityprojection) and [Carbon Footprint reporting methodology](https://docs.cloud.google.com/carbon-footprint/docs/methodology) for details.




### Operation

An [`Operation`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#operation) is the individual action that must be performed as one of the atomic steps in a suggested recommendation. Operations can represent the following changes:

  * Add, remove, or replace JSON object fields in a Google Cloud resource.
  * Add, remove, or replace JSON array fields in a Google Cloud resource. JSON array elements are identified by defining a filter on the path.
  * Add a new Google Cloud resource.
  * Delete a Google Cloud resource.
  * Test operations to indicate the original state of the resource. The test operations can also be used to verify the current state of a resource before applying the recommendation.
  * Copy and move Google Cloud resources and fields.



Each `Operation` is loosely based on the [JSON Path (RFC 6902)](https://tools.ietf.org/html/rfc6902) format for patches. This RFC was selected because it provides a more consistent way to reflect resource changes, including complex scenarios commonly found in Google Cloud. For example, IAM recommendations involve nested arrays to reflect moving a principal's role binding to a different role.

For each resource, a changelist (diff-based view) can be generated in the following way:

  * **Original state** : Test operations represent the original value of a field. This represents the left-hand side of the diff view.
  * **Recommended state** : Non-test operations represent the recommended changes per field. This represents the right-hand side of the diff view.



### Operation groups

An _operation group_ is a set of one or more operations that must be performed in a specific order when you apply a recommendation. A recommendation can have one or more operation groups. Operation groups are stored in the `operationGroups` field in the `Recommendation` entity.

For example, a recommendation suggesting that you change the VM instance machine type for a Compute Engine instance group has two operation groups: one where you change the machine type in the instance template, and another where you apply the change to a particular instance group.

Because the first set of operations must complete before the second can be started, these are defined as two separate instance groups in the recommendation.

An operation group can include a _test_ operation. Test operations perform checks to ensure that a recommendation is still valid. The recommendation that suggests changing the VM instance machine type has a test operation that checks whether the current machine type is the same as when the recommendation was made.

### State

Recommendations go through many state transitions after they are proposed. A recommendation can have the following states:

  * `ACTIVE`, which means that the recommendation has been made, but no actions have been taken in response to it. The recommendation can be applied by claiming it. Active recommendations can be updated when resources change.
  * `CLAIMED`, which means that you or another process has claimed the recommendation and that a response to it is in-progress. When a recommendation is claimed, Recommender does not update it when resources change.
  * `SUCCEEDED`, which means that you or another process has applied the recommendation to the associated resource.
  * `FAILED`, which means that an attempt to apply the recommendation has failed.
  * `DISMISSED`, which means that you or another process has dismissed the recommendation without applying it to the associate resource. This state prevents the recommendation from appearing in the list of recommendations, and is typically applied by an administrator who has invalidated it for various reasons. It also prevents a recommendation from moving to the `CLAIMED` state.



Information about the state of the recommendation is stored in the `stateInfo` field of the `Recommendation` entity. This includes the state itself of the recommendation and any additional per-recommender state metadata.

When a recommendation is changed to `CLAIMED`, `SUCCEEDED`, or `FAILED` state, the content of the recommendation is not updated, and recommendation has a lifespan of 90 days from the time of the state change.

**Note:** You cannot dismiss a recommendation or change the recommendation state to active from the API. Individual recommenders provide the option to set these states in Google Cloud console.

### etag

An _etag_ is a unique fingerprint that identifies the current state of a recommendation. Each time the recommendation changes, a new etag value is assigned. This value is stored in the `etag` field of the `Recommender` entity.

After you retrieve a recommendation from Recommender using `gcloud` commands or API calls, you reference it in subsequent operations using both the recommendation ID and the etag. This makes sure that any operations are performed only if the recommendation has not changed since you last retrieved it.

### Priority

A [_priority_](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/billingAccounts.locations.recommenders.recommendations#priority) for a recommendation helps give an indication of what actions must be tackled first. This field comes with values `P1`, `P2`, `P3`, and `P4` with `P4` set as the default priority. Each [recommender](https://docs.cloud.google.com/recommender/docs/recommenders) can have its own prioritization strategy defined.

### State metadata

When you claim a recommendation or mark it as succeeded or failed, you can include additional metadata about the operation with state metadata.

The metadata is specified as `key:value` pairs. For example:
    
    
    {
      "stateMetadata": {
        "priority" : "high",
        "tracking_number": "12345" }
    }
    

Updates to the `stateMetadata` field overwrites an existing state metadata.

### Last refresh time

The last refresh time indicates when the recommendation was last refreshed by the generation process. The content of the recommendation reflects the state of the resources at the last refresh time.

### Examples

The following example shows a sizing recommendation for a VM instance in Compute Engine.
    
    
    {
      "content": {
        "operationGroups": [
          {
            "operations": [
              {
                "action": "test",
                "path": "/machineType",
                "resource": "//compute.googleapis.com/projects/example-project/zones/us-central1-a/instances/instance-rightsizing-2",
                "resourceType": "compute.googleapis.com/Instance",
                "valueMatcher": {
                  "matchesPattern": ".*zones/us-central1-a/machineTypes/n1-standard-4"
                }
              },
              {
                "action": "replace",
                "path": "/machineType",
                "resource": "//compute.googleapis.com/projects/example-project/zones/us-central1-a/instances/instance-rightsizing-2",
                "resourceType": "compute.googleapis.com/Instance",
                "value": "zones/us-central1-a/machineTypes/custom-2-5120"
              }
            ]
          }
        ]
      },
      "description": "Save cost by changing machine type from n1-standard-4 to custom-2-5120.",
      "etag": "\"923daeebe926c12f\"",
      "recommenderSubtype": "CHANGE_MACHINE_TYPE",
      "lastRefreshTime": "2019-06-13T06:44:58Z",
      "name": "projects/32428390823/locations/us-central1-a/recommenders/google.compute.instance.MachineTypeRecommender/recommendations/a523ff7e-ed03-4143-a3a5-5b396b99cba9",
      "primaryImpact": {
        "category": "COST",
        "costProjection": {
          "cost": {
            "currencyCode": "USD",
            "units": "-73"
          },
          "duration": "2592000s"
        }
      },
      "stateInfo": {
        "state": "ACTIVE"
      }
    }
    

For more examples of recommendations, see the documentation for individual recommenders in [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders).

### Insight reference

Reference to an associated [insight](https://docs.cloud.google.com/recommender/docs/insights/using-insights#insights). References link recommendations with their associated insights, if any.

### Configuration

Through the recommender configuration, you can do the following:

  * Customize the way in which insights and recommendations are generated. This is done by modifying some of the configuration parameters that are used to generate these insights and recommendations.
  * Each recommender configuration starts with some default values for each parameter. Each parameter has a range of values that you can use to customize the configuration.
  * The active configuration is the one you last modified. For every change made to the configuration, it takes up to 48 hours for the configuration to take effect.

**Note:** You can retrieve the configuration details for a recommender or insight type only if they support this configuration setting.

An example for a recommender configuration is setting a default CPU threshold or an observation period to create recommendations that better fit your workloads, applications, and infrastructure needs.

With the configuration API, you can retrieve the configuration for a recommender or insight type. You have the option to update the configuration parameters for a single project. Each recommender config or insight type requires specific permissions to view and modify the configuration parameters.

Here's an example response containing configuration parameters for an Idle VM recommender:
    
    
    {
      "name": "projects/project-number/locations/global/recommenders/google.iam.policy.Recommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "minimum_observation_period": "P90D",
        }
      },
      "etag": "\"2f3c9b65cda6a4ba\"",
      "updateTime": "2020-11-03T04:41:15.330351Z"
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
