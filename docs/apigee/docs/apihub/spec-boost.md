---
url: https://docs.cloud.google.com/apigee/docs/apihub/spec-boost/
title: Specification boost add-on \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:07.662354+00:00
---

# Specification boost add-on  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/spec-boost/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Specification boost add-on Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

**Preview — Specification boost add-on**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Specification boost is an AI-powered add-on that lets you automatically enhance the readability and discoverability of your API specifications in API hub. It analyzes your existing specification files and generates _boosted_ versions enriched with richer details, including additional examples, clearer descriptions, better error documentation, and more. 

A key benefit of using the specification boost add-on is that it makes your specification files _agent ready_. Boosting your specifications makes them more accessible to developers, API consumers, and AI agents. 

**Note:** AI can make mistakes. Review all boosted specifications carefully before using them in production. 

## Enable specification boost

To start using specification boost, you must first enable and configure it in the **Add-on management** page in API hub. 

**Note:** Specification boost add-on enablement can take 10 minutes to complete. 

### Before you begin

  * Grant the **API hub Add-on Admin** (`roles/apihub.addonsAdmin`) IAM role to your principal account. For information about granting IAM roles, see [Grant or revoke multiple IAM roles using the Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#multiple-roles-console). 



### Console

To enable the specification boost add-on, do the following:

  1. In the Google Cloud console, go to the **API hub > Add-on management** page. 

[Go to Add-on management](https://console.cloud.google.com/apigee/api-hub/add-on-management)

  2. Locate the **Specification boost** add-on card and click **Enable add-on**. 

Enabling the add-on triggers an asynchronous operation that automatically processes and boosts all your API specification files in API hub. 




### REST API

To enable the specification boost add-on, submit this request:
    
    
    curl --location 'https://apihub.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/addons/system-specboost:manageConfig' \
      --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
      --header 'Content-Type: application/json' \
      --data '{
        "name": "projects/PROJECT_ID/locations/LOCATION/addons/system-specboost",
        "config": {
          "allDataAddonConfig": {
            "enabled": true
          }
        }
      }'

Where: 

  * `PROJECT_ID` is the ID of the host project for your API hub instance.
  * `LOCATION` is the location where your API hub instance is hosted.



## View boosted specifications

Boosted specifications are generated asynchronously. Depending on the number of specification files and their size, it may take some time for the asynchronous operation to complete. Once the asynchronous operation completes, you can view the boosted specifications as an additional version of the original specification. 

**Note:** Specification boost doesn't overwrite any of your original specification files. All boosted versions of a specification file are created as versions of the same specification file. 

### Console

To view the boosted specification files, do the following: 

  1. In the Google Cloud console, go to the **API hub** page.

[ Go to API hub](https://console.cloud.google.com/apigee/api-hub/apis)
  2. Click **APIs**.
  3. Use [Filter](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes#filter-resources) to specify keywords to filter the list of APIs. If needed, use [Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis) to locate an API.
  4. Click an API to view its details.
  5. Go to the **Versions** tab, and select the API version for which you want to view the boosted specifications.
  6. Scroll to the **Specification file** section to view the list of specifications linked to the version. 

The **Boosted specification** column displays the boosted specification files if they are available. 

  7. To view the details of a boosted specification, click the name of the boosted specification file. 

![Boosted specification column screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/boosted-spec.png)![Boosted specification column screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/boosted-spec-column.png)

  8. To see the differences in the boosted specification, click **View diff** in the tridot menu in the row for that specification file.



## Disable specification boost

To disable the specification boost add-on, do the following: 

**Note:** Disabling the specification boost add-on doesn't delete any boosted specifications that you have already generated. 

### Console

To disable the specification boost add-on, do the following:

  1. In the Google Cloud console, go to the **API hub > Add-on management** page. 

[Go to Add-on management](https://console.cloud.google.com/apigee/api-hub/add-on-management)

  2. Locate the **Specification boost** add-on card and click **Disable add-on**. 
  3. In the **Disable specification boost** confirmation dialog, enter `disable`, and then click **Disable**. 

The specification boost add-on is disabled in a few minutes. 




### REST API

To disable the specification boost add-on, submit this request:
    
    
    curl --location 'https://apihub.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/addons/system-specboost:manageConfig' \
      --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
      --header 'Content-Type: application/json' \
      --data '{
        "name": "projects/PROJECT_ID/locations/LOCATION/addons/system-specboost",
        "config": {
          "allDataAddonConfig": {
            "enabled": false
          }
        }
      }'

Where: 

  * `PROJECT_ID` is the ID of the host project for your API hub instance.
  * `LOCATION` is the location where your API hub instance is hosted.



## Supported regions

Specification boost is only available for API hub instances provisioned in the following regions: 

  * `us-central1`
  * `us-east4`
  * `us-west1`
  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `europe-west4`
  * `europe-southwest1`
  * `asia-east1`
  * `asia-northeast1`
  * `asia-south1`
  * `asia-southeast1`
  * `australia-southeast2`



## Considerations

  * AI can make mistakes. Review all boosted specifications carefully before using them in production.
  * Boosted specifications are generated asynchronously. Depending on the number of specification files and their size, it may take some time for the asynchronous operation to complete.
  * Once the add-on is enabled, any new or updated specification file is automatically boosted asynchronously.



## Limitations

  * Specification boost is only available for API hub instances provisioned in specific regions. For a list of supported regions, see Supported regions.
  * You can't select specific specification files to boost. All specification files are boosted asynchronously after the add-on is enabled.
  * Specification boost doesn't support replacing or merging the boosted content into your original specification file.
  * At this time, specification boost is not available for customers using VPC-SC.



## What's next

  * Learn about [API specifications](https://docs.cloud.google.com/apigee/docs/apihub/specs-intro).
  * Learn about [API versions](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
