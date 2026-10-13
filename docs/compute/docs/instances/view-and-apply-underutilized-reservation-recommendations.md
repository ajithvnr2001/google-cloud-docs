---
url: https://docs.cloud.google.com/compute/docs/instances/view-and-apply-underutilized-reservation-recommendations/
title: View and apply underutilized reservation recommendations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:06.009361+00:00
---

# View and apply underutilized reservation recommendations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-and-apply-underutilized-reservation-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View and apply underutilized reservation recommendations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how you can use reservation recommendations to identify and delete underutilized on-demand reservations, so you can avoid charges for resources that you're not using.

  * For more information on how to configure the reservations recommender to receive more or fewer recommendations, see [Configure underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-underutilized-reservation-recommendations) or [Configure idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-idle-reservation-recommendations). 

## Before you begin

    * Review the [limitations](https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview#limitations) to check if your reservation supports underutilized reservation recommendations.
    * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

      1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
             
             gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
      2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## View underutilized reservation recommendations

To view recommendations about underutilized reservations, use one of the following options.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

    * `recommender.computeRightSizeResourceRecommender.get` on the project.

Complete this task using one of the following methods.

###  Console 

    1. In the Google Cloud console, go to the **FinOps hub**.

[Go to FinOps hub](https://console.cloud.google.com/billing/optimize)

Under the **Top Recommendations** section, you can view underutilized reservation recommendations.

![A view of the Top Recommendations list](https://docs.cloud.google.com/static/compute/docs/images/top_recommendations.png)

    2. In the **Top Recommendations** section, click the recommendation tied to your underutilized reservations.

When you click the recommendation, it shows extent of underutilization in the **Insight** section.

The page with the details of the recommendation opens. In the **Insight** section, you can view the extent of the underutilization.

    3. To view the details of the reservation, click **View reservations**.

Clicking **View Reservation Details** shows the **Utilization** section, which displays the reservation size and your actual utilization.

Clicking **Edit** enables the **Configuration** section, where you can set a new value for the number of VMs that better matches your intended usage.

If you don't need the reservation anymore, then [delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-delete).

###  gcloud 

To view recommendations about underutilized reservations, use the [`gcloud recommender recommendations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) with the `--recommender=google.compute.RightSizeResourceRecommender` flag:
    
    gcloud recommender recommendations list \
      --location=ZONE \
      --recommender=google.compute.RightSizeResourceRecommender \
      --format=yaml \
      --project=PROJECT_ID
    

Replace the following:

    * `ZONE` with the zone that contains reservations to list recommendations for.
    * `PROJECT_ID` with the ID of your project.

For example:
    
    gcloud recommender recommendations list \
      --location=us-central1-c \
      --recommender=google.compute.RightSizeResourceRecommender \
      --format=yaml \
      --project=my-project
    

If there are no underutilized reservations in the location, the response is empty. Otherwise, the response includes the following fields for each recommendation:

    * `operationGroups`: groups of operations that you can perform to apply the recommendation
    * `description`: an explanation of the recommendation
    
    ---
    associatedInsights:
    - insight: projects/953727763714/locations/us-central1-f/insightTypes/google.compute.RightSizeResourceRecommender/insights/ecf77776-4a2a-4e6e-aad2-b7f9c632e5f9
    content:
    operationGroups:
    - operations:
      - action: remove
        path: /
        resource: //compute.googleapis.com/projects/committed-use-discount-test/zones/us-central1-f/reservations/test-reservation
        resourceType: compute.googleapis.com/Reservation
    overview:
      currentReservation:
        machineType: n1-standard-1
        reservationName: test-reservation
        reservedMachineCount: '1'
        zone: us-central1-f
    description: Save cost by deleting the underutilized reservation test-reservation
    etag: '"aff724ab8e40e1ef"'
    lastRefreshTime: '2024-06-10T07:00:00Z'
    name: projects/953727763714/locations/us-central1-f/recommenders/google.compute.RightSizeResourceRecommender/recommendations/56f8ac5d-8380-4cb8-a76f-bbc270fb4b8e
    primaryImpact:
    category: COST
    costProjection:
      cost:
        currencyCode: USD
        nanos: -199820000
        units: '-1072'
      costInLocalCurrency:
        currencyCode: USD
        nanos: -199820000
        units: '-1072'
      duration: 2592000s
    priority: P2
    recommenderSubtype: DELETE_RESERVATION
    stateInfo:
    state: ACTIVE
    targetResources:
    - //compute.googleapis.com/projects/committed-use-discount-test/zones/us-central1-f/reservations/test-reservation
    

Learn more about working with recommendations using Google Cloud CLI in [gcloud examples](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations).

###  REST 

To view recommendations about underutilized reservations, make a `GET` request to the [`recommendations.list` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) and use the following recommendation type:

    * **google.compute.RightSizeResourceRecommender**

The API call looks like:
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.RightSizeResourceRecommender/recommendations
    

Replace the following: \- `PROJECT_ID`: the ID of your project. \- `ZONE`: the zone that contains instances to list recommendations for.

The following example shows out to send a request with `curl`, and the associated sample response.
    
    PROJECT_ID=my-project
    ZONE=us-central1-c
    RECOMMENDER_ID=google.compute.RightSizeResourceRecommender
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "x-goog-user-project: $PROJECT_ID" \
      https://recommender.googleapis.com/v1/projects/$PROJECT_ID/locations/$ZONE/recommenders/$RECOMMENDER_ID/recommendations
    

Example JSON response for an underutilized reservation recommendation:
    
    {
      "associatedInsights": [
        {
          "insight": "projects/9531234763714/locations/us-central1-f/insightTypes/google.compute.RightSizeResourceRecommender/insights/ecf77776-4a2a-4e6e-aad2-b7f9c632e5f9"
        }
      ],
      "content": {
        "operationGroups": [
          {
            "operations": [
              {
                "action": "remove",
                "path": "/",
                "resource": "//compute.googleapis.com/projects/committed-use-discount-test/zones/us-central1-f/reservations/test-reservation",
                "resourceType": "compute.googleapis.com/Reservation"
              }
            ]
          }
        ],
        "overview": {
          "currentReservation": {
            "machineType": "n1-standard-1",
            "reservationName": "test-reservation",
            "reservedMachineCount": "1",
            "zone": "us-central1-f"
          }
        }
      },
      "description": "Save cost by deleting the underutilized reservation test-reservation",
      "etag": "\"8d5603cac8fa9342\"",
      "lastRefreshTime": "2024-06-11T07:00:00Z",
      "name": "projects/9531234763714/locations/us-central1-f/recommenders/google.compute.RightSizeResourceRecommender/recommendations/56f8ac5d-8380-4cb8-a76f-bbc270fb4b8e",
      "primaryImpact": {
        "category": "COST",
        "costProjection": {
          "cost": {
            "currencyCode": "USD",
            "nanos": -199820000,
            "units": "-1072"
          },
          "costInLocalCurrency": {
            "currencyCode": "USD",
            "nanos": -199820000,
            "units": "-1072"
          },
          "duration": "2592000s"
        }
      },
      "priority": "P2",
      "recommenderSubtype": "DELETE_RESERVATION",
      "stateInfo": {
        "state": "ACTIVE"
      },
      "targetResources": [
        "//compute.googleapis.com/projects/committed-use-discount-test/zones/us-central1-f/reservations/test-reservation"
      ]
    }
    

You can find more details about each field in the [Recommender API documentation](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations).

### Interpreting the recommendation response

Each recommendation that you receive through the gcloud CLI or REST contains an operations group, with operations that you can perform in serial to apply the recommendation. For underutilized reservations, the operation groups include a `remove` operation to delete the reservation:
    
    {
      "action": "remove",
      "path": "/",
      "resource": "//compute.googleapis.com/projects/committed-use-discount-test/zones/us-central1-f/reservations/test-reservation",
      "resourceType": "compute.googleapis.com/Reservation"
    }
    

## Apply underutilized reservation recommendations

Based on underutilized reservation recommendations, either [adjust the reservation size](https://docs.cloud.google.com/compute/docs/instances/reservations-modify) or [delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-delete) if you no longer need it.

## What's next

    * [Learn more about how Compute Engine reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).
    * Learn how to [configure underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-underutilized-reservation-recommendations).
    * Learn how to [configure idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/configure-idle-reservation-recommendations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
