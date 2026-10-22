---
url: https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps/
title: Configure access controls for apps \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:38.869475+00:00
---

# Configure access controls for apps  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure access controls for apps Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how a Gemini Enterprise admin can use the API to manage fine-grained access control for individual Gemini Enterprise apps.

If you need to configure granular, resource-level access controls across both apps and data stores, see [Configure granular access controls for apps and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores).

By default, IAM permissions are often managed at the project level. App-level IAM allows for more granular control, enabling admins to:

  * Restrict user access to specific apps within the same Google Cloud project.
  * Align permissions with organizational needs and data silos for your Gemini Enterprise deployments.

**Important:** Project-level IAM permissions take precedence over app-level policies. If a user is granted the Gemini Enterprise User (`roles/discoveryengine.agentspaceUser`) role at the project level, they can access all apps in that project, regardless of any app-level permissions. To restrict a user to specific apps, replace their project-level Gemini Enterprise User role with the Gemini Enterprise Restricted User (`roles/discoveryengine.agentspaceRestrictedUser`) role, and then grant the Gemini Enterprise User role on each app that they need to access.**Note:** Users with app-level IAM permissions for a Gemini Enterprise app can access and use only that specific app. These are user-level permissions that don't include admin capabilities.

For example, consider an organization with an HR app and a company-wide app. An HR team member with project-level permissions can access both the apps. By contrast, using an app-level IAM policy, you can grant a sales team member access to only the company-wide app, thereby preventing them from accessing the HR app.

![Diagram of app-level IAM policy examples.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/app-level-iam-policy/app-level-policy-examples.png)

## Before you begin

  * Confirm that you have the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) role.

  * Confirm that all Gemini Enterprise users have a valid license and are granted the [Gemini Enterprise Restricted User](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceRestrictedUser) (`roles/discoveryengine.agentspaceRestrictedUser`) role at the project level. For instructions, see [Grant permissions to your users](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#grant-role).

This role doesn't grant access to any app on its own. It provides the project-level access that users need, and you then grant access to individual apps. If you use a custom project-level role instead of the predefined `roles/discoveryengine.agentspaceRestrictedUser` role, ensure that your custom role includes the `discoveryengine.locations.buildAuthorizationUrl`, `discoveryengine.dataStores.get`, `discoveryengine.collections.get`, and `discoveryengine.devToolsConfigs.get` permissions. Omitting `discoveryengine.devToolsConfigs.get` causes a `403 PERMISSION_DENIED` error in Cloud Audit Logs when the web app checks `devToolsConfig`.




## Transition from project-level to app-level access

To restrict users to specific apps, you must replace their project-level Gemini Enterprise User role with the Gemini Enterprise Restricted User role, and then grant the Gemini Enterprise User role at the individual app level.

To transition a user from project-level access to app-level access, follow these steps. You use the Google Cloud console for the project-level changes, and the API for the app-level grant, which the Google Cloud console doesn't support.

  1. In the Google Cloud console, go to the **IAM** page.
  2. Find the user and remove the Gemini Enterprise User (`roles/discoveryengine.agentspaceUser`) role from their project-level permissions.
  3. If you haven't already, grant the user the Gemini Enterprise Restricted User (`roles/discoveryengine.agentspaceRestrictedUser`) role at the project level.
  4. Use the `setIamPolicy` method to grant the user the Gemini Enterprise User (`roles/discoveryengine.agentspaceUser`) role for each specific app that they need to access. For more information, see Manage IAM policies for apps.



## Manage IAM policies for apps

To manage access to your Gemini Enterprise app, you can use the `getIamPolicy` and `setIamPolicy` API methods.

The following steps show you how to retrieve the current policy and then update it to grant or revoke user access.

### Get the app IAM policy

Get the current IAM policy of your app using the [`getIamPolicy`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.iam.v1#getiampolicyrequest) method. It's recommended to fetch the existing policy first to avoid overwriting any current permissions.

### REST

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID:getIamPolicy"
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
  * `APP_ID`: the ID of the app that you want to configure.

**Note:** Copy the `etag` value from the response. This value is required to update the IAM policy. The `etag` value changes with each policy update.



#### Example command and result
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://global-discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app:getIamPolicy"
    
    
    * * *
    
    
    {
      "version": 1,
      "etag": "1234567890"
    }
      

### Update the app IAM policy

To grant or revoke user access to the app, update the app's IAM policy using the [`setIamPolicy`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.iam.v1#setiampolicyrequest) method.

**Important:** The `setIamPolicy` method replaces the existing policy. To avoid removing existing permissions, your request must include all the policy bindings you want to retain, in addition to any new or modified bindings.

The IAM policy uses the [Gemini Enterprise User](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`) role to grant users direct access to the app.

**Note:** Changes to IAM policies, such as those made using `setIamPolicy`, are subject to propagation delays. It can take several minutes for permissions to fully propagate. For more information, see [IAM propagation delay](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### REST

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
          "policy": {
             "etag": "ETAG",
             "bindings": [
              {
                "role": "roles/discoveryengine.agentspaceUser",
                "members": [
                  "user:USER_EMAIL",
                  "group:GROUP_EMAIL",
                  "principal://iam.googleapis.com/locations/global/workloadIdentityPools/POOL_ID/subject/SUBJECT_ID",
                  "principalSet://iam.googleapis.com/locations/global/workloadIdentityPools/POOL_ID/attribute.NAME/VALUE"
                ]
              }
            ]
          }
        }' \
    "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID:setIamPolicy"
    

Replace the following:

  * `ETAG`: the `etag` value you got as the response when you used the `getIamPolicy` method.

  * `USER_EMAIL`, `GROUP_EMAIL`: one or more user or group email addresses. In addition to `user` and `group`, `principal` and `principalSet` are valid member types for Workload Identity Federation.

    * To grant access, add principals to the `members` array. For example, `"user:cloudysanfrancisco@gmail.com"` or `"group:mcymbalgroup@google.com"`.

**Note:** Avoid extra spaces before or after the email address.
    * To revoke access, remove principals from the `members` array.

  * `POOL_ID`: The ID of your workload identity pool.

  * `SUBJECT_ID`: The subject identifier for a specific identity.

  * `NAME`: The name of an attribute.

  * `VALUE`: The value of an attribute.

  * `PROJECT_ID`: the ID of your project.

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 

    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`.

  * `APP_ID`: the ID of the app that you want to configure.

**Note:** The `etag` value changes with each policy update. To update the policy again, you must first get the new `etag` by following Get the app IAM policy.



#### Example command and result
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
          "policy": {
             "etag": "1234567890",
             "bindings": [
              {
                "role": "roles/discoveryengine.user",
                "members": [
                  "user:cloudysanfrancisco@gmail.com",
                  "group:cymbalgroup@google.com"
                ]
              }
            ]
          }
        }' \
    "https://global-discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app:setIamPolicy"
    
    
    * * *
    
    
    {
      "version": 1,
      "etag": "2345678901",
      "bindings": [
        {
          "role": "roles/discoveryengine.user",
          "members": [
            "user:cloudysanfrancisco.com",
            "group:cymbalgroup@google.com"
          ]
        }
      ]
    }
      

## What's next?

If you want to delete an app with an IAM policy, you can remove the users from the policy before deleting the app. For more information, see [Best practices for deleting an app with an IAM policy](https://docs.cloud.google.com/gemini/enterprise/docs/delete-app#best-practices-for-deleting-an-app-with-an-iam-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
