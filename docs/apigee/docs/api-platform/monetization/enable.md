---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enable/
title: Enable Apigee monetization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:54:45.922246+00:00
---

# Enable Apigee monetization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Enable Apigee monetization Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Before you can use Apigee monetization, you must purchase and enable it in your organization. Apigee monetization is supported for Apigee and Apigee hybrid environments.

**Note:** See [Known issue 355714868](https://cloud.google.com/apigee/docs/release/known-issues) for an issue related to Apigee monetization recurring, setup, and top-up fee data in hybrid environments.

##  Purchase Apigee monetization 

To purchase Apigee monetization for **Subscription organizations** , contact [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html), then enable Apigee monetization in your organization. 

Apigee monetization is not available with **Pay-as-you-go organizations**. 

Apigee **eval organizations** automatically include an Apigee monetization trial for the trial period. You do not need to contact Apigee Sales to add monetization. Proceed to Enable Apigee monetization in your organization. 

##  Enable Apigee monetization in your organization 

To enable Apigee monetization in an existing organization, issue a `POST` request to the following API, passing the add-on configuration in your request body:
    
    
    https://apigee.googleapis.com/v1/organizations/ORG_NAME:setAddons

**Caution:** The add-on configuration that you pass in the request body will **overwrite** the existing add-on configuration. [ View the existing add-on configuration](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) in the Apigee organization profile and be sure to include it in the request payload. 

For example: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME:setAddons" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "addonsConfig": {
          **"monetizationConfig": {
              "enabled": "true"
          } <_Include existing add-on configuration_ >**
        }
      }'

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response showing that the operation is in progress: 
    
    
    {
      "name": "organizations/ORG_NAME/operations/1ae3ed56-b38f-4cc1-ba33-e7d89557075d",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/ORG_NAME",
        "state": "IN_PROGRESS"
      }
    }

For more information, see the [ Configure organization add-ons API](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setAddons). 

[ View the organization profile](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) to confirm that monetization has been enabled. For example: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"

The following provides an example of the response showing monetization is enabled. 
    
    
    {
        "name": ORG_NAME,
        ...
        "addonsConfig": {
        "monetizationConfig": {
          **"enabled": true**
        }
      }
    }

##  Disable Apigee monetization in your organization 

To disable Apigee monetization in your organization, issue a `POST` request to the following API, passing the add-on configuration in your request body:
    
    
    https://apigee.googleapis.com/v1/organizations/ORG_NAME:setAddons

**Caution:** The add-on configuration that you pass in the request body will **overwrite** the existing add-on configuration. [ View the existing add-on configuration](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) in the Apigee organization profile and be sure to include it in the request payload. 

For example: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME:setAddons" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        **"addonsConfig": {
          "monetizationConfig": {
              "enabled": "false"
          } <_Include existing add-on configuration_ >**
        }
      }'

The following provides an example of the response showing that the operation is in progress: 
    
    
    {
      "name": "organizations/ORG_NAME/operations/06274ffb-8940-41da-836d-781cba190437",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/ORG_NAME",
        "state": "IN_PROGRESS"
      }
    }

For more information, see the [Configure organization add-ons API](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setAddons). 

[View the organization profile](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/get) to confirm that monetization has been disabled. For example: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/ORG_NAME" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"

The following provides an example of the response showing monetization is enabled. 
    
    
    {
        "name": ORG_NAME,
        ...
        "addonsConfig": {
        "monetizationConfig": {
          **"enabled": false**
        }
      }
    }

##  Troubleshoot Apigee monetization enablement 

If you have not purchased Apigee monetization and you attempt to enable it, the following error is returned:
    
    
    {
      "error": {
        "code": 400,
        "message": "failed to validate addons config: [Apigee Monetization] addon(s) are not entitled to the subscription",
        "status": "FAILED_PRECONDITION"
      }
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
