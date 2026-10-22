---
url: https://docs.cloud.google.com/compute/docs/instances/configure-machine-type-recommendations/
title: Configure machine type recommendations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:55.519617+00:00
---

# Configure machine type recommendations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/configure-machine-type-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure machine type recommendations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to view and modify the configuration of your machine type recommendations. You can modify which machine types are recommended, so the generated recommendations only include your preferred machine series. You can also change the metrics used to generate memory recommendations to improve the accuracy of the recommendations. The changes to the configuration are applied at the project level.

For more information about machine type recommendations, see [Apply machine type recommendations for VMs](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



### Required roles

To get the permissions that you need to modify machine type recommendations, ask your administrator to grant you the [Compute Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.computeAdmin) (`roles/recommender.computeAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to modify machine type recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to modify machine type recommendations:

  * View the machine type recommendation configuration: `recommender.computeInstanceMachineTypeRecommenderConfig.get` on the project 
  * Modify the machine type recommendation configuration: `recommender.computeInstanceMachineTypeRecommenderConfig.update` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure your recommendations

To configure your machine type recommendations, perform the following steps:

  1. Get the current configuration to obtain the JSON file of the configuration.
  2. Edit the configuration file in JSON format.
  3. Upload the new configuration file to apply the changes.



### Get the current configuration

You can obtain the current configuration for machine type recommendations for your project by using the Google Cloud CLI.

###  gcloud 

To get the current configuration parameters, use the [`gcloud beta recommender recommender-config describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/recommender-config/describe) and use `google.compute.instance.MachineTypeRecommender` as the Recommender ID:
    
    
    gcloud beta recommender recommender-config describe google.compute.instance.MachineTypeRecommender \
      --project=PROJECT_ID \
      --location=ZONE
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: the zone for which you want to obtain the current configuration.



The command returns the recommender configuration, including the modifiable subfields `preferred_machine_types` and `memory_metrics`.
    
    
    {
      "name": "projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.instance.MachineTypeRecommender/config",
      "recommenderGenerationConfig": {
        **"params": {
          "preferred_machine_types": "STANDARD_AND_CUSTOM",
          "memory_metrics": "MONITORING_AGENT_ONLY"
        }**
      },
      "etag": "\"2f3c9b65cda6a4ba\"",
      "updateTime": "2024-08-20T04:41:15.330351Z"
    }
    

If you want to save the configuration to a local file, so you can edit it and upload it later, run the following command:
    
    
    gcloud beta recommender recommender-config describe \
      google.compute.instance.MachineTypeRecommender \
      --project=PROJECT_ID \
      --location=ZONE > LOCAL_FILE_PATH_AND_NAME
    

### Edit the recommendation configuration

The configuration lets you customize the following parameters:

  * `preferred_machine_types`: The machine types recommendations that you receive.
  * `memory_metrics`: How memory metrics are used to generate recommendations.



#### Options for machine types recommendations

You can specify which machine types recommendations you get by changing the `preferred_machine_types` setting to one of the following values:

  * `DEFAULT`: The default value is `STANDARD_AND_CUSTOM`.
  * `STANDARD_AND_CUSTOM`: Recommends the best match from standard and custom machine types.
  * `STANDARD_ONLY`: Recommends the best match from standard machine types only.



#### Options for memory recommendations

For the memory metrics used to generate the recommendations, you can set the following values:

  * `MEMORY_METRICS_DEFAULT`: Use the default metrics to generate recommendations.
  * `MEMORY_METRICS_ALL`: Use all the available metrics to generate recommendations.
  * `MONITORING_AGENT_ONLY`: Use only metrics collected by the Cloud Monitoring Ops Agent.
  * If you don't use the Ops Agent, and prefer not to receive memory recommendations, use the `MEMORY_AGENT_ONLY` value to disable the recommendations.



To get more accurate recommendations about memory usage, use the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent).

### Update the configuration for a project

To update the configuration of your machine type recommendations, modify the configuration values and upload the new configuration for your project. You can change the preferred machine types, the memory metrics used for recommendations, or both values in the same request.

After you upload the new configuration, it takes approximately 48 hours for it to take effect. Until that time, any generated recommendations use the previous configuration.

###  gcloud 

To update the configuration parameters, use the [`gcloud beta recommender recommender-config update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/recommender-config/update) and use `google.compute.instance.MachineTypeRecommender` as the Recommender ID:
    
    
    gcloud beta recommender recommender-config update google.compute.instance.MachineTypeRecommender\
      --project=PROJECT_ID \
      --location=ZONE \
      --config-file=LOCAL_FILE_PATH_AND_NAME \
      --etag=ETAG
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: the zone for which you want to obtain the current configuration.
  * `LOCAL_FILE_PATH_AND_NAME`: the path to the JSON file with the current configuration.
  * `ETAG`: the etag value of the current configuration. You can find this value in the output of the previous command.



In your configuration file, specify only the `recommenderGenerationConfig` object with the updated configuration parameters. If you saved the configuration to a local file, make sure you copy the `etag` value, then remove all the fields except the `recommenderGenerationConfig` value.

For example, to get recommendations with standard machine types only, use the following configuration file:
    
    
    {
      "params": {
        "preferred_machine_types": "STANDARD_ONLY"
      }
    }
    

If the command is successful, it returns a response body similar to the following, showing the new configuration with the parameters you just modified.
    
    
    {
      "name": "projects/PROJECT_ID/locations/ZONE/recommenders/google.compute.instance.MachineTypeRecommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "preferred_machine_types": "STANDARD_ONLY"
        }
      },
      "etag": "\"1245f9435cd01ea8\"",
      "updateTime": "2024-08-20T05:00:05Z"
    }
    

**Note:** the `etag` value changes from the previous configuration. You must use the new value if you update the configuration again.

## What's next

  * Learn how to [Apply machine type recommendations to instances](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances).
  * Learn how to [Apply machine type recommendations to managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/apply-machine-type-recommendations-managed-instance-groups).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
