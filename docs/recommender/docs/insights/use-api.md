---
url: https://docs.cloud.google.com/recommender/docs/insights/use-api/
title: Use the API - Insights \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:58.490099+00:00
---

# Use the API - Insights  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/insights/use-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the API - Insights

This page explains how to view and manage [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights#insights) in Recommender using [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/recommender) or the [REST API](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights).

A typical insight interaction with the Recommender API is:

  * List the insights for a specific project
  * Mark an insight that you intend to take action on as accepted



## Set the default project

Set the default project if you haven't done so already:
    
    
    gcloud config set project PROJECT_ID
    

where PROJECT_ID is the ID of your project.

## Set environment variables

Set environment variables for Recommender interactions:
    
    
    PROJECT=TARGET_PROJECT_ID
    LOCATION=LOCATION_ID
    INSIGHT_TYPE=INSIGHT_TYPE_ID
    

where:

  * TARGET_PROJECT_ID is the project whose insights you want to list. This can be a different project than your current project.

    * For `gcloud` commands, you must use the project ID
    * For API requests, you can use the project number or project ID. Project number is recommended.

The project number is returned in responses from both the API and `gcloud` commands.

  * LOCATION_ID is the Google Cloud [location](https://cloud.google.com/about/locations) where resources associated with the insights are located (for example, `global` or `us-central1-a`).

  * INSIGHT_TYPE_ID is the fully-qualified [insight type ID](https://docs.cloud.google.com/recommender/docs/insights/insight-types) (for example, `google.iam.policy.Insight`).




See [Insight types](https://docs.cloud.google.com/recommender/docs/insights/insight-types) for a table of links to information about each insight type, including supported locations and insight type IDs.

## Set permissions

You must have permissions to access insights in the target project.

  * For requesters who include a [billing project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project) in their request. The project used in the request must be in good standing, and the user must have a role in the project that contains the `serviceusage.services.use` permission. The **Service Usage Consumer** role contains the required permission.
  * Each insight type requires specific permissions. See [Insight types](https://docs.cloud.google.com/recommender/docs/insights/insight-types) for a table of links to information about each insight type, including the required permissions.

**Note:** If you use the [`x-goog-user-project` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgooguserproject) or [`userProject` query string parameter](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#userProject) in your request, you must have `serviceusage.services.use` permission for the project ID that you specify, in addition to the normal IAM permissions required to make the request.

## List insights

As shown in the **gcloud Beta** tab, you can list all of your project's insights without having to specify a location and recommender. This feature is in Preview.

The GA feature requires that you specify a project, location, and recommender. For details, see the **gcloud** tab.

###  gcloud Beta

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Enter the following:
    
    
    gcloud beta recommender insights list \
        --project=${PROJECT} \
        --format=FORMAT
    

where FORMAT is a supported `Google Cloud CLI` [output format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats), such as `json`.

For example:
    
    
    gcloud beta recommender insights list \
        --project=example-project \
        --format=json
    

**Note:** Unlike the following output for the **gcloud** and **REST** tabs, which is limited to insights for a location and recommender, the output will include all insights for the project.

###  gcloud 

Enter the following:
    
    
    gcloud recommender insights list \
        --project=${PROJECT} \
        --location=${LOCATION} \
        --insight-type=${INSIGHT_TYPE} \
        --format=FORMAT
    

where FORMAT is a supported `gcloud` [output format](https://docs.cloud.google.com/sdk/gcloud/reference/topic/formats) (for example, `json`).

For example:
    
    
    gcloud recommender insights list \
        --project=example-project \
        --location=global \
        --insight-type=google.iam.policy.Insight \
        --format=json
    

###  REST 

Enter the following:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
        -H "x-goog-user-project: ${PROJECT}" \
        "https://recommender.googleapis.com/v1/projects/${PROJECT}/locations/${LOCATION}/insightTypes/${INSIGHT_TYPE}/insights"
    

For example:
    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
        -H "x-goog-user-project: example-project" \
        "https://recommender.googleapis.com/v1/projects/example-project/locations/us-central1-a/insightTypes/google.iam.policy.Insight/insights"
    

This operation outputs the current IAM policy insights in the target project as a list of [`Insight`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights#resource:-insight) entities in the specified format.

The output is similar to the following:
    
    
    [
      {
        "category": "SECURITY",
        "content": {
          "condition": {
            "description": "",
            "expression": "",
            "location": "",
            "title": ""
          },
          "exercisedPermissions": [],
          "inferredPermissions": [],
          "member": "user:my-service-account@example-project.iam.gserviceaccount.com",
          "role": "roles/iam.securityReviewer"
        },
        "description": "0 permission checks were authorized by this policy binding tuple.",
        "etag": "\"45f4e2c63f6952e8\"",
        "insightSubtype": "PERMISSIONS_USAGE",
        "lastRefreshTime": "2020-03-06T08:00:00Z",
        "name": "projects/32428390823/locations/global/insightTypes/google.iam.policy.Insight/insights/a523ff7e-ed03-4143-a3a5-5b396b99cba9",
        "observationPeriod": "7776000s",
        "stateInfo": {
          "state": "ACTIVE",
        },
        "targetResources": [
          "//cloudresourcemanager.googleapis.com/projects/32428390823"
        ],
      }
    ]
    

Note that the returned insights include the following fields:

  * A `name` field in the following format:
        
        projects/PROJECT_ID/locations/LOCATION/insightTypes/INSIGHT_TYPE_ID/insights/INSIGHT_ID

where INSIGHT_ID uniquely identifies the insight

  * An `etag` field that is associated with the current insight state.




When you reference an insight using subsequent `gcloud` commands or REST API calls, you reference both the insight ID and etag, which makes sure that any operations are performed only if the insight has not been modified since you last retrieved it.

## Mark an insight as accepted

You can mark an insight as accepted to indicate that you intend to take or have taken an action on an associated resource based on the information provided in the insight. When an insight is accepted, your user name is assigned as the actor for the insight, and Recommender will not update the insight with newer content.

To mark an insight as accepted:

###  gcloud 

Enter the following:
    
    
    gcloud recommender insights mark-accepted \
        INSIGHT_ID \
        --project=${PROJECT} \
        --location=${LOCATION} \
        --insight-type=${INSIGHT_TYPE} \
        --etag=etag \
        --state-metadata=STATE_METADATA
        --format=FORMAT
    

where:

  * INSIGHT_ID is the ID of an insight retrieved from a previous call to list insights
  * etag is the returned etag representing the insight state
  * STATE_METADATA is an optional metadata about the operation. Specify the metadata as a comma-separated list of KEY=VALUE pairs.



For example:
    
    
    gcloud recommender insights mark-accepted \
        a523ff7e-ed03-4143-a3a5-5b396b99cba9 \
        --project=example-project \
        --location=global \
        --insight-type=google.iam.policy.Insight \
        --etag='"280b34810bba8a1a"' \
        --state-metadata=priority=high,tracking_number=12345
        --format=json
    

###  REST 

Enter the following:
    
    
    curl -X POST \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
        -H "x-goog-user-project: ${PROJECT}" \
        --data-binary @- \
        https://recommender.googleapis.com/v1/projects/${PROJECT}/locations/${LOCATION}/insightTypes/${INSIGHT_TYPE}/insights/INSIGHT_ID:markAccepted \
    << EOM
    {
      "etag": "etag",
      "stateMetadata": STATE_METADATA
    }
    EOM
    
    

where:

  * INSIGHT_ID is the ID of an insight retrieved from a previous call to list insights
  * etag is the returned etag representing the insight state
  * STATE_METADATA is an optional field with additional metadata about the operation. Specify the metadata as `key:value` pairs.



For example:
    
    
    curl -X POST \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
        -H "x-goog-user-project: example-project" \
        --data-binary @- \
        https://recommender.googleapis.com/v1/projects/example-project/locations/global/insightTypes/google.iam.policy.Insight/insights/a523ff7e-ed03-4143-a3a5-5b396b99cba9:markAccepted \
    << EOM
    {
      "etag": "\"280b34810bba8a1a\""
      "stateMetadata": {
        "priority" : "high",
        "tracking_number": "12345"
      }
    }
    EOM
    

This operation returns the [`Insight`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights#resource:-insight) entity in the specified format after the operation has taken place.

The output is similar to the following:
    
    
    {
      "category": "SECURITY",
      "content": { ...  },
      "description": "0 permission checks were authorized by this policy binding tuple.",
      "etag": "\"356ae51165729f38\"",
      "insightSubtype": "PERMISSIONS_USAGE",
      "lastModifiedUser": "admin123@example-project.iam.gserviceaccount.com",
      "lastRefreshTime": "2020-03-06T08:00:00Z",
      "name": "projects/32428390823/locations/global/insightTypes/google.iam.policy.Insight/insights/a523ff7e-ed03-4143-a3a5-5b396b99cba9",
      "observationPeriod": "7776000s",
      "stateInfo": {
        "state": "ACCEPTED",
        "stateMetadata": {
          "priority" : "high",
          "tracking_number": "12345"
        }
      },
      "targetResources": [
        "//cloudresourcemanager.googleapis.com/projects/32428390823"
      ],
      "userLastUpdateTime": "2020-03-31T20:57:50.509855Z"
    }
    
    

Note that the value of the `state` field has changed to `ACCEPTED`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
