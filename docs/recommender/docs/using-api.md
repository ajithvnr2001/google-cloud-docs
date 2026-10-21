---
url: https://docs.cloud.google.com/recommender/docs/using-api/
title: Use the API - Recommendations \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:55.416545+00:00
---

# Use the API - Recommendations  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/using-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the API - Recommendations

This page explains how to view and manage [recommendations](https://docs.cloud.google.com/recommender/docs/key-concepts#recommendations) in Recommender by using [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/recommender) or the [REST API](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations).

A typical recommendation interaction with the Recommender API is:

  1. List the recommendations for a specific project.

  2. Mark a recommendation that you intend to apply as `claimed`, or mark a recommendation that you don't intend to apply as `dismissed`.

  3. Apply the recommendation. You can do this automatically [using Active Assist](https://docs.cloud.google.com/recommender/docs/active-assist/apply-dismiss-restore-recommendations) in the Google Cloud console, or manually using the Google Cloud CLI commands, REST API calls, or other tools.

When you manually apply the recommendation, the commands or calls that you use are specific to the resource type. For example, to change the size of a VM instance in response to a recommendation from the VM instance sizing recommender, you use Compute Engine [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances) or calls to the Compute Engine [REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

When you perform these operations, you identify the target resource by using the value of the `resource` field in the `OperationsGroup` array in the returned [`Recommendation`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#resource:-recommendation) entity. This field is in the following format:
         
         //API_NAME/RESOURCE_PATH

For example:
         
         //compute.googleapis.com/projects/example-project/zones/us-central1-a/instances/instance-1

  4. Mark the recommendation as `succeeded` or `failed`.




Note that only recommendations retrieved through the API can be interacted with using the API or [BigQuery Export](https://docs.cloud.google.com/bq-export/export-recommendations-to-bq).

For information about changing the state of recommendations in the Google Cloud console, refer to the documentation for [Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist) or for the appropriate [recommender](https://docs.cloud.google.com/recommender/docs/recommenders).

**Warning:**

Before applying recommendations in the Google Cloud console or using the API, ensure that impacts are assessed by a reviewer within your organization. The reviewer should have the knowledge to assess impacts identified in recommendations, as well as impacts specific to your infrastructure and business. Applying recommendations without proper assessment could result in unexpected changes, such as issues with system performance, poor reliability, or loss of required permissions. If you choose to apply recommendations without human review, ensure that you have set up a rollback process before making any changes.

## Set the default project

Set the default project if you haven't done so already:
    
    
    gcloud config set project PROJECT_ID
    

where PROJECT_ID is the ID of your project.

## Set environment variables

Set environment variables for Recommender interactions:
    
    
    PROJECT=TARGET_PROJECT_ID
    LOCATION=LOCATION_ID
    RECOMMENDER=RECOMMENDER_ID
    

where:

  * TARGET_PROJECT_ID is the project whose recommendations you want to list. This can be a different project than your current project.

    * For `gcloud` commands, you must use the project ID
    * For API requests, you can use the project number or project ID. Project number is recommended.

The project number is returned in responses from both the API and `gcloud` commands.

  * LOCATION_ID is the Google Cloud [location](https://cloud.google.com/about/locations) where resources associated with the recommendations are located (for example, `global` or `us-central1-a`).

  * RECOMMENDER_ID is the fully-qualified [recommender ID](https://docs.cloud.google.com/recommender/docs/recommenders#recommenders) (for example, `google.compute.instance.MachineTypeRecommender`).




See [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders) for a table of links to information about each recommender, including supported locations and recommender IDs.

## Set permissions

You must have permissions to access recommendations in the target project.

  * For requesters who include a [billing project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project) in their request. The project used in the request must be in good standing, and the user must have a role in the project that contains the `serviceusage.services.use` permission. The **Service Usage Consumer** role contains the required permission.
  * Each recommender requires specific permissions. See [Recommenders](https://docs.cloud.google.com/recommender/docs/recommenders) for a table of links to information about each recommender, including the required permissions.

**Note:** If you use the [`x-goog-user-project` header or `userProject` query string parameter](https://docs.cloud.google.com/apis/docs/system-parameters#definitions) in your request, you must have the `serviceusage.services.use` permission for the project ID that you specify, in addition to the normal IAM permissions required to make the request.

## List recommendations

As shown in the **gcloud Beta** tab, you can list all of your project's recommendations without having to specify a location and recommender. This feature is in Preview.

The GA feature requires that you specify a project, location, and recommender. For details, see the **gcloud** tab.

###  gcloud Beta

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Enter the following:
    
    
    gcloud beta recommender recommendations list \
        --project=${PROJECT} \
        --format=FORMAT
    

where FORMAT is a supported `gcloud` [output format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats), such as `json`.

For example:
    
    
    gcloud beta recommender recommendations list \
        --project=example-project \
        --format=json
    

**Note:** Unlike the following output for the **gcloud** and **REST** tabs, which is limited to recommendations for a location and recommender, the output will include all recommendations for the project.

###  gcloud 

Enter the following:
    
    
    gcloud recommender recommendations list \
        --project=${PROJECT} \
        --location=${LOCATION} \
        --recommender=${RECOMMENDER} \
        --format=FORMAT
    

where FORMAT is a supported `gcloud` [output format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats) (for example, `json`).

For example:
    
    
    gcloud recommender recommendations list \
        --project=example-project \
        --location=us-central1-a \
        --recommender=google.compute.instance.MachineTypeRecommender \
        --format=json
    

###  REST 

Enter the following:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
        -H "x-goog-user-project: ${PROJECT}" \
        "https://recommender.googleapis.com/v1/projects/${PROJECT}/locations/${LOCATION}/recommenders/${RECOMMENDER}/recommendations"
    

For example:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
        -H "x-goog-user-project: example-project" \
        "https://recommender.googleapis.com/v1/projects/example-project/locations/us-central1-a/recommenders/google.compute.instance.MachineTypeRecommender/recommendations"
    

This operation outputs the current VM instance sizing recommendations in the target project as a list of [`Recommendation`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#resource:-recommendation) entities in the specified format.

The output is similar to the following:
    
    
    [
      {
        "content": {
          "operationGroups": [
            {
              "operations": [
                {
                  "action": "test",
                  "path": "/machineType",
                  "resource": "//compute.googleapis.com/projects/example-project/zones/us-central1-a/instances/instance-1",
                  "resourceType": "compute.googleapis.com/Instance",
                  "valueMatcher": {
                    "matchesPattern": ".*zones/us-central1-a/machineTypes/n1-standard-4"
                  }
                },
                {
                  "action": "replace",
                  "path": "/machineType",
                  "resource": "//compute.googleapis.com/projects/example-project/zones/us-central1-a/instances/instance-1",
                  "resourceType": "compute.googleapis.com/Instance",
                  "value": "zones/us-central1-a/machineTypes/custom-2-5120"
                }
              ]
            }
          ]
        },
        "description": "Save cost by changing machine type from n1-standard-4 to custom-2-5120.",
        "etag": "\"280b34810bba8a1a\"",
        "lastRefreshTime": "2019-06-28T06:49:21Z",
        "name": "projects/32428390823/locations/us-central1-a/recommenders/google.compute.instance.MachineTypeRecommender/recommendations/a523ff7e-ed03-4143-a3a5-5b396b99cba9",
        "primaryImpact": { ... },
        "stateInfo": {
          "state": "ACTIVE"
        },
        "recommenderSubtype": "CHANGE_MACHINE_TYPE"
      }
    ]
    

Note that the returned recommendations include the following fields:

  * A `name` field in the following format:
        
        projects/PROJECT_ID/locations/LOCATION/recommenders/RECOMMENDER_ID/recommendations/RECOMMENDATION_ID

where RECOMMENDATION_ID uniquely identifies the recommendation

  * An `etag` field that is associated with the current recommendation state.




When you reference a recommendation using subsequent `Google Cloud CLI` commands or REST API calls, you reference both the recommendation ID and etag, which makes sure that any operations are performed only if the recommendation has not been modified since you last retrieved it.

## Change the state of a recommendation

You can mark a recommendation as claimed to indicate that you intend to apply the recommended changes to the associated resource. When a recommendation is claimed, your username is assigned as the actor for the recommendation, and Recommender does not update the recommendation with newer content.

You can mark a recommendation as dismissed to indicate that you don't intend to apply the recommended changes to the associated resource or that you don't want to continue to see the recommendation. When a recommendation is dismissed, it will no longer appear as an ACTIVE recommendation. Recommender might continue to update the recommendation with newer content.

After you have applied a recommendation, you can mark it as succeeded or failed.

To change the state of a recommendation, complete the following steps:

###  gcloud 

Enter the following:
    
    
    gcloud recommender recommendations STATE_CHANGE \
        RECOMMENDATION_ID \
        --project=${PROJECT} \
        --location=${LOCATION} \
        --recommender=${RECOMMENDER} \
        --etag=ETAG \
        --state-metadata=STATE_METADATA \
        --format=FORMAT
    

Where

  * STATE_CHANGE is the change you want to make to a recommendation. Valid values are: 
    * `mark-claimed` to mark the recommendation as claimed.
    * `mark-dismissed` to mark the recommendation as dismissed.
    * `mark-succeeded` to mark the recommendation as succeeded.
    * `mark-failed` to mark the recommendation as failed.
  * RECOMMENDATION_ID is the ID of a recommendation that you retrieved from a previous call to list recommendations.
  * ETAG is the returned etag representing the recommendation state
  * STATE_METADATA is optional metadata about the operation. Specify the metadata as a comma-separated list of KEY=VALUE pairs. This option is available when you mark a recommendation as claimed, succeeded, or failed.



For example:
    
    
    gcloud recommender recommendations mark-succeeded \
        a523ff7e-ed03-4143-a3a5-5b396b99cba9 \
        --project=example-project \
        --location=us-central1-a \
        --recommender=google.compute.instance.MachineTypeRecommender \
        --etag='"5e3a63cccf1e0964"' \
        --state-metadata=priority=high,tracking_number=12345 \
        --format=json
    

###  REST 

Enter the following
    
    
    curl -X POST \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "x-goog-user-project: ${PROJECT}" \
        --data-binary @- \
        https://recommender.googleapis.com/v1/projects/${PROJECT}/locations/${LOCATION}/recommenders/${RECOMMENDER}/recommendations/RECOMMENDATION_ID:STATE_CHANGE \
    << EOM
    {
      "etag": "ETAG"
      "stateMetadata": STATE_METADATA
    }
    EOM
    
    

where:

  * RECOMMENDATION_ID is the ID of a recommendation that you retrieved from a previous call to list recommendations.
  * STATE_CHANGE is the change you want to make to a recommendation. Valid values are: 
    * `markClaimed` to mark the recommendation as claimed.
    * `markDismissed` to mark the recommendation as dismissed.
    * `markSucceeded` to mark the recommendation as succeeded.
    * `markFailed` to mark the recommendation as failed.
  * ETAG is the returned etag representing the recommendation state
  * STATE_METADATA is an optional field with additional metadata about the operation. Specify the metadata as `key:value` pairs. This field is available when you mark a recommendation as claimed, succeeded, or failed.



For example:
    
    
    curl -X POST \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "x-goog-user-project: example-project" \
        --data-binary @- \
        https://recommender.googleapis.com/v1/projects/example-project/locations/us-central1-a/recommenders/google.compute.instance.MachineTypeRecommender/recommendations/8f20d509-83d2-45d2-8152-1b8d5d7d5831:markSucceeded \
    << EOM
    {
      "etag": "\"280b34810bba8a1a\""
      "stateMetadata": {
        "priority" : "high",
        "tracking_number": "12345"
      }
    }
    EOM
    

This operation returns the [`Recommendation`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations#resource:-recommendation) entity in the specified format after the operation has taken place.

The output is similar to the following:
    
    
    {
      "content": {
        "operationGroups": [ ... ]
      },
      "description": "Save cost by changing machine type from n1-standard-4 to custom-2-5120.",
      "etag": "\"5e3a63cccf1e053c\"",
      "lastRefreshTime": "2019-06-28T06:49:21Z",
      "name": "projects/32428390823/locations/us-central1-a/recommenders/google.compute.instance.MachineTypeRecommender/recommendations/a523ff7e-ed03-4143-a3a5-5b396b99cba9",
      "primaryImpact": { ... },
      "stateInfo": {
        "state": "SUCCEEDED",
        "stateMetadata": {
          "priority" : "high",
          "tracking_number": "12345"
        }
      }
    }
    

Note that the value of the `state` field has changed to `SUCCEEDED`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
