---
url: https://docs.cloud.google.com/compute/docs/instances/configure-idle-reservation-recommendations/
title: Configure idle reservation recommendations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:38.512479+00:00
---

# Configure idle reservation recommendations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/configure-idle-reservation-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure idle reservation recommendations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to view and modify the configuration of your idle, on-demand reservation recommendations. You might want to modify the configuration to increase the number of recommendations that you receive, or to get fewer recommendations to delete reservations that you plan to use.

  * For more information on the parameters you can use to customize the recommendations, see [Choose the right configuration parameters](https://docs.cloud.google.com/compute/docs/instances/reservation-recommendations-overview#choose-configuration).
  * For more information on how to identify idle on-demand reservation and take action, see [View and apply idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/view-and-apply-idle-reservation-recommendations).



## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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




## Configure your recommendations

To configure your idle reservation recommendations, do the following:

  1. Get the current configuration to obtain the JSON file of the configuration.
  2. Edit the configuration file in JSON format.
  3. Upload the new configuration file to apply the changes.



### Get the current configuration

You can obtain the current configuration for idle reservation recommendations for your project by using the Google Cloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `recommender.computeIdleResourceRecommendations.get` on the project.



Complete this task using one of the following methods.

###  gcloud 

To get the current configuration parameters, use the [`gcloud recommender recommender-config describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe) and use `google.compute.IdleResourceRecommender` as the Recommender ID:
    
    
    gcloud recommender recommender-config describe google.compute.IdleResourceRecommender \
      --location=ZONE --billing-account=BILLING_ACCOUNT_ID
    

Replace `ZONE` with the zone for which you want to get the current configuration.

For example:
    
    
    gcloud recommender recommender-config describe google.compute.IdleResourceRecommender \
      --location=us-central1-c --billing-account=my-billing-account-id
    

The command returns the recommender configuration, including the modifiable subfield `params.idle_reservation_lookback_period`.
    
    
    {
      "name": "projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.IdleResourceRecommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "idle_reservation_lookback_period": "P7D"
        }
      },
      "etag": "\"2f3c9b65cda6a4ba\"",
      "updateTime": "2024-06-03T04:41:15.330351Z"
    }
    

###  REST 

To retrieve the current configuration, use the [`recommenders.getConfig`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders/getConfig) method and specify `google.compute.IdleResourceRecommender` as the Recommender ID:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.IdleResourceRecommender/config
    

Replace `ZONE` with the zone that contains your project.

From the command line, execute the following command to get the recommender configuration for a project:
    
    
    PROJECT_ID=PROJECT_ID
    ZONE=ZONE
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "x-goog-user-project: ${PROJECT_ID}" \
    https://recommender.googleapis.com/v1/projects/$PROJECT_ID/locations/$ZONE/recommenders/google.compute.IdleResourceRecommender/config
    

The command returns the recommender configuration, including the subfield that you can modify: `params.idle_reservation_lookback_period`.
    
    
    {
      "name": "projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.IdleResourceRecommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "idle_reservation_lookback_period": "P7D"
        }
      },
      "etag": "\"2f3c9b65cda6a4ba\"",
      "updateTime": "2024-06-03T04:41:15.330351Z"
    }
    

**Note:** When you submit the new configuration, remove the `updateTime` parameter.

### Update the configuration for a project

To update the configuration of your idle reservation recommendations, modify the value for `idle_reservation_lookback_period` and upload the new configuration for your project.

You can set the observation period to a value of 7 days up to 30 days, using a string beginning with `P`, then an integer for the number of days (`7` minimum and `30` maximum), followed by `D`, for example:

  * For an observation period of 7 days, use `"P7D"`.
  * For an observation period of 30 days, use `"P30D"`.



After you upload the new configuration, it takes approximately 48 hours for it to take effect. Until that time, any generated recommendations use the previous configuration.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `recommender.computeIdleResourceRecommenderConfig.get` on the project to view the configuration.
  * `recommender.computeIdleResourceRecommenderConfig.update` on the project to modify the configuration. 



###  gcloud 

To update the configuration parameters, use the [`gcloud recommender recommender-config update` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/update) and use `google.compute.IdleResourceRecommender` as the Recommender ID:
    
    
    gcloud recommender recommender-config update google.compute.IdleResourceRecommender\
      --location=ZONE \
      --config-file=CONFIG_FILE_PATH \
      --etag=ETAG \
      --billing-account=BILLING_ACCOUNT_ID
    

Replace the following:

  * `ZONE`: the zone for which you want to obtain the current configuration
  * `CONFIG_FILE_PATH`: the path to the JSON file with the current configuration
  * `ETAG`: the etag value of the current configuration
  * `BILLING_ACCOUNT_ID`: the ID of the billing account



In your configuration file, specify only the `recommenderGenerationConfig` object with the updated configuration parameters. For example, to specify an observation period of 21 days, use the following configuration file:
    
    
    {
      "params": {
        "idle_reservation_lookback_period": "P21D"
      }
    }
    

If the command is successful, it returns a response body similar to the following, showing the new configuration with the parameters you just modified.
    
    
    {
      "name": "projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.IdleResourceRecommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "idle_reservation_lookback_period": "P21D"
        }
      },
      "etag": "\"1245f9435cd01ea8\"",
      "updateTime": "2024-06-03T05:00:05Z"
    }
    

**Note:** the `etag` value changes from the previous configuration. You must use the new value if you update the configuration again.

###  REST 

To update the configuration, make a `PATCH` request to the [`recommenders.updateConfig`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders/updateConfig) method and specify `google.compute.IdleResourceRecommender` as the Recommender ID:
    
    
    PATCH https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.IdleResourceRecommender/config
    
    {
      "name": "projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.IdleResourceRecommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "idle_reservation_lookback_period": "P21D"
        }
      },
      "etag": "\"2f3c9b65cda6a4ba\""
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project for which you want to modify the recommender configuration.
  * `ZONE`: the zone that contains your project.



Save the request body in a file, for example `config.json`. You can then reference the file when you update the recommender configuration for your project, using a command similar to the following:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
    -H "x-goog-user-project: ${PROJECT_ID}" \
    -d @config.json \
    https://recommender.googleapis.com/v1/projects/$PROJECT_ID/locations/$ZONE/recommenders/google.compute.IdleResourceRecommender/config
    

The `POST` command returns a response body similar to the following, showing the new configuration with the parameters you just modified.
    
    
    {
      "name": "projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.IdleResourceRecommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "idle_reservation_lookback_period": "P21D"
        }
      },
      "etag": "\"1245f9435cd01ea8\"",
      "updateTime": "2024-06-03T05:00:05Z"
    }
    

**Note:** the `etag` value changes from the previous configuration. You must use the new value if you update the configuration again.

## What's next

  * Learn how to [view and apply idle reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/view-and-apply-idle-reservation-recommendations).
  * Learn how to [view and apply underutilized reservation recommendations](https://docs.cloud.google.com/compute/docs/instances/view-and-apply-underutilized-reservation-recommendations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
