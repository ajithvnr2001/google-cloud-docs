---
url: https://docs.cloud.google.com/gemini/enterprise/docs/delete-app/
title: Delete an app \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:27.093977+00:00
---

# Delete an app  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/delete-app/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Delete an app Stay organized with collections  Save and categorize content based on your preferences. 

This page describes best practices and instructions for safely deleting an app.

## Steps to delete an app

The following instructions are for the Google Cloud console.

### Console

To delete an app, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/apps)

  2. For the app that you want to delete, click more_vert, and then click **Delete**.

  3. In the **Delete the app?** dialog, enter your app name, and then click **Confirm**.




## Best practices for deleting an app with an IAM policy

Deleting an app is an irreversible action. Therefore, if your app has [configured access controls](https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps), you can remove all users from its IAM policy before deleting the app. Follow these steps:

  1. **Clear the IAM policy:** Before deleting the app, clear its IAM policy to remove user access. You can do this by setting an empty `bindings` array.

     1. Get the current IAM policy of your app using the [`getIamPolicy`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.iam.v1#getiampolicyrequest) method.

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
      

     2. To remove all existing bindings, use the [`setIamPolicy`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.iam.v1#setiampolicyrequest) method with an empty `bindings` array in the request body.

### REST

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
            
            curl -X POST \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            -d '{
                  "policy": {
                    "etag": "ETAG",
                    "bindings": []
                  }
                }' \
            "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID:setIamPolicy"
            

Replace the following:

        * `ETAG`: the `etag` value you got as the response when you used the `getIamPolicy` method.
        * `PROJECT_ID`: the ID of your project.
        * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
          * `us` for the US multi-region
          * `eu` for the EU multi-region
          * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
        * `LOCATION`: the multi-region of your data store: `global`, `us`, or `eu`
        * `APP_ID`: the ID of the app that you want to configure.

#### Example command and result
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
          "policy": {
            "etag": "1234567890",
            "bindings": []
          }
        }' \
    "https://global-discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines/my-app:setIamPolicy"
    
    
    * * *
    
    
    {
      "version": 1,
      "etag": "3456789012"
    }
      

  2. **Confirm user impact:** After clearing the policy and allowing for [propagation time](https://docs.cloud.google.com/iam/docs/access-change-propagation), confirm that the access revocation hasn't caused any unintended issues for users.

  3. **Delete the app:** After you've confirmed the impact, proceed with deleting the app as described in the Steps to delete an app section.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
