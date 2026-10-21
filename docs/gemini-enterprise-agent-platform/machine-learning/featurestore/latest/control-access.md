---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/control-access/
title: Control access to resources \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:08.653372+00:00
---

# Control access to resources  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/control-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Control access to resources Stay organized with collections  Save and categorize content based on your preferences. 

You can set Identity and Access Management (IAM) policies to control access to the following Vertex AI Feature Store resources:

  * Feature groups

  * Online store instances

  * Feature views




An IAM policy is a collection of bindings, which associates one or more members, or principals, to an IAM role. You can include the following types of members in an IAM policy binding:

  * Individual user accounts

  * Google groups

  * Domains

  * Service accounts




## Before you begin

Authenticate to Gemini Enterprise Agent Platform, unless you've done so already. 

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## Set an IAM policy for a feature group

Use the following sample to set an IAM policy for an existing feature group.

### REST

To assign an IAM policy to a [`FeatureGroup`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups#resource:-featureGroup) resource, send a `POST` request by using the [featureGroups.setIamPolicy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups/setIamPolicy) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the online store instance is located, such as `us-central1`.
  * PROJECT_ID: Your project ID.
  * FEATUREGROUP_NAME: The name of the online store instance for which you want to set the IAM policy.
  * IAM_ROLE_NAME: The name of the IAM role to assign to the members. For a complete list of IAM roles for Gemini Enterprise Agent Platform, see [Access control with IAM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control).
  * USER_EMAIL: Optional. The email address of the user account to whom the role is assigned.
  * GROUP_EMAIL: Optional. The email address of the Google group to which the role is assigned.
  * DOMAIN_NAME: Optional. The domain name to which the role is assigned.
  * SERVICE_ACCOUNT_EMAIL: Optional. The email address of the service account to which the role is assigned..



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureGroups/FEATUREGROUP_NAME:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "IAM_ROLE_NAME",
            "members": [
              "user:USER_EMAIL",
              "group:GROUP_EMAIL",
              "domain:DOMAIN_NAME",
              "serviceAccount:SERVICE_ACCOUNT_EMAIL"
            ]
          }
        ]
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureGroups/FEATUREGROUP_NAME:setIamPolicy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureGroups/FEATUREGROUP_NAME:setIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "bindings": [
      {
        "role": "IAM_ROLE_NAME",
        "members": [
          "user:USER_EMAIL",
          "group:GROUP_EMAIL",
          "domain:DOMAIN_NAME",
          "serviceAccount:SERVICE_ACCOUNT_EMAIL"
        ]
      }
      ],
      "etag": "etag"
    }
    

## Set an IAM policy for an online store

Use the following sample to set an IAM policy for an existing online store instance.

### REST

To assign an IAM policy to a [`FeatureOnlineStore`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores#resource:-featureOnlineStore) resource, send a `POST` request by using the [featureOnlineStores.setIamPolicy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores/setIamPolicy) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the online store instance is located, such as `us-central1`.
  * PROJECT_ID: Your project ID.
  * FEATUREONLINESTORE_NAME: The name of the online store instance for which you want to set the IAM policy.
  * IAM_ROLE_NAME: The name of the IAM role to assign to the members. For a complete list of IAM roles for Gemini Enterprise Agent Platform, see [Access control with IAM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control).
  * USER_EMAIL: Optional. The email address of the user account to whom the role is assigned.
  * GROUP_EMAIL: Optional. The email address of the Google group to which the role is assigned.
  * DOMAIN_NAME: Optional. The domain name to which the role is assigned.
  * SERVICE_ACCOUNT_EMAIL: Optional.The email address of the service account to which the role is assigned..



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureOnlineStores/FEATUREONLINESTORE_NAME:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "IAM_ROLE_NAME",
            "members": [
              "user:USER_EMAIL",
              "group:GROUP_EMAIL",
              "domain:DOMAIN_NAME",
              "serviceAccount:SERVICE_ACCOUNT_EMAIL"
            ]
          }
        ]
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureOnlineStores/FEATUREONLINESTORE_NAME:setIamPolicy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureOnlineStores/FEATUREONLINESTORE_NAME:setIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "bindings": [
      {
        "role": "IAM_ROLE_NAME",
        "members": [
          "user:USER_EMAIL",
          "group:GROUP_EMAIL",
          "domain:DOMAIN_NAME",
          "serviceAccount:SERVICE_ACCOUNT_EMAIL"
        ]
      }
      ],
      "etag": "etag"
    }
    

## Set an IAM policy for a feature view

Use the following sample to set an IAM policy for an existing feature view.

### REST

To assign an IAM policy to a [`FeatureView`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews#resource:-featureView) resource, send a `POST` request by using the [featureViews.setIamPolicy](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureOnlineStores.featureViews/setIamPolicy) method. 

Before using any of the request data, make the following replacements: 

  * LOCATION_ID: Region where the feature view is located, such as `us-central1`.
  * PROJECT_ID: Your project ID.
  * FEATUREONLINESTORE_NAME: The name of the online store instance containing the feature view.
  * FEATUREVIEW_NAME: The name of the feature view for which you want to set the IAM policy.
  * IAM_ROLE_NAME: The name of the IAM role to assign to the members. For a complete list of IAM roles for Gemini Enterprise Agent Platform, see [Access control with IAM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control).
  * USER_EMAIL: Optional. The email address of the user account to whom the role is assigned.
  * GROUP_EMAIL: Optional. The email address of the Google group to which the role is assigned.
  * DOMAIN_NAME: Optional. The domain name to which the role is assigned.
  * SERVICE_ACCOUNT_EMAIL: Optional.The email address of the service account to which the role is assigned..



HTTP method and URL: 
    
    
    POST https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureOnlineStores/FEATUREONLINESTORE_NAME/featureViews/FEATUREVIEW_NAME:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "IAM_ROLE_NAME",
            "members": [
              "user:USER_EMAIL",
              "group:GROUP_EMAIL",
              "domain:DOMAIN_NAME",
              "serviceAccount:SERVICE_ACCOUNT_EMAIL"
            ]
          }
        ]
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureOnlineStores/FEATUREONLINESTORE_NAME/featureViews/FEATUREVIEW_NAME:setIamPolicy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/featureOnlineStores/FEATUREONLINESTORE_NAME/featureViews/FEATUREVIEW_NAME:setIamPolicy" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "bindings": [
      {
        "role": "IAM_ROLE_NAME",
        "members": [
          "user:USER_EMAIL",
          "group:GROUP_EMAIL",
          "domain:DOMAIN_NAME",
          "serviceAccount:SERVICE_ACCOUNT_EMAIL"
        ]
      }
      ],
      "etag": "etag"
    }
    

## What's next

  * Learn how to [list all features in a feature group](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/list-features).

  * Learn how to [update a feature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/update-feature).

  * Learn how to [delete a feature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/delete-feature).

  * Learn how to [update a feature group](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/update-featuregroup).

  * [Online serving types](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/online-serving-types) in Vertex AI Feature Store.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
