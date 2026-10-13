---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/list-featuregroups/
title: List feature groups \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:46.067674+00:00
---

# List feature groups  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/list-featuregroups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  List feature groups Stay organized with collections  Save and categorize content based on your preferences. 

You can retrieve a list of all the feature groups created for a specific location in your Google Cloud project, along with the URI of the BigQuery source table or view associated with each feature group.

If a feature group is configured to use a dedicated service account, then the details for that feature group also include the associated service account email address. For more information about creating feature groups with dedicated service account configurations, see [Configure the service account for a feature group](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/create-featuregroup#serviceaccount).

## Before you begin

Authenticate to Gemini Enterprise Agent Platform, unless you've done so already.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## List feature groups

Use the following samples to retrieve a list of all feature groups for a specific location in your project.

### Console

Use the following instructions to view the list of feature groups for a specific location using the Google Cloud console.

  1. In the Agent Platform section of the Google Cloud console, go to the **Feature Store** page.

[Go to the Feature Store page](https://console.cloud.google.com/agent-platform/feature-store)

  2. In the **Feature groups** section, you can view the list of all the feature groups for the selected location.




### REST

To retrieve a list of all the [`FeatureGroup`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups#resource:-featuregroup) resources for a specific location in your project, send a `GET` request by using the [featureGroups.list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups/list) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region for which you want to view the list of feature groups, such as `us-central1`.
  * PROJECT_ID: Your project ID.



HTTP method and URL: 
    
    
    GET https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureGroups

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureGroups"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureGroups" | Select-Object -Expand Content

You should receive a JSON response similar to the following. BIGQUERY_URI_1 is the BigQuery source table or view registered via FEATURE_GROUP_NAME_1 and BIGQUERY_URI_2 is the BigQuery source table or view registered with FEATURE_GROUP_NAME_2.  
If any of the feature groups listed in the response has a dedicated service account configuration, then the service account email address is also listed in its details. In this example, SERVICE_ACCOUNT_EMAIL is the service account email address associated with the feature group FEATURE_GROUP_NAME_1. 
    
    
    {
      "featureGroups": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featureGroups/FEATURE_GROUP_NAME_1",
          "createTime": "2023-09-07T00:57:00.142639Z",
          "updateTime": "2023-09-07T00:57:00.142639Z",
          "etag": "AMEw9yOY0byP8qKsDY0DoZyouAtX23zDru2l422C0affZZPYNFOGgIrONELNrM49uH4=",
          "bigQuery": {
            "bigQuerySource": {
              "inputUri": "BIGQUERY_URI_1"
            }
          }
          "serviceAccountEmail": "SERVICE_ACCOUNT_EMAIL"
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/featureGroups/FEATURE_GROUP_NAME_2",
          "createTime": "2023-09-06T23:14:30.795502Z",
          "updateTime": "2023-09-06T23:14:30.795502Z",
          "etag": "AMEw9yO5UfrPWobGR2Ry-PnbJUQoklW5lX0uW4JmKqj6OgQui6p-rMdUHfuENpQjbJ3t",
          "bigQuery": {
            "bigQuerySource": {
              "inputUri": "BIGQUERY_URI_2"
            }
          }
        }
      ]
    }
    

## What's next

  * Learn how to [create a feature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/create-feature).

  * Learn how to [update a feature group](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/update-featuregroup).

  * Learn how to [delete a feature group](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/delete-featuregroup).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
