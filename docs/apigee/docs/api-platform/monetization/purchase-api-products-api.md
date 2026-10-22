---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/purchase-api-products-api/
title: Purchasing and managing API product subscriptions using the API \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:07.012963+00:00
---

# Purchasing and managing API product subscriptions using the API  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/purchase-api-products-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Purchasing and managing API product subscriptions using the API Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

If you want to build your own custom portal or manage the purchasing process manually, the following sections describe how to purchase and manage API product subscriptions using the API. These examples describe how to manage subscriptions for app developers and AppGroups. 

See also [Integrate Apigee monetization in your Drupal-based developer portal](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/integrate-developer-portal). 

## App developer subscription management

###  App developer: Purchase API product subscriptions using the API 

**Note:** An app developer can purchase an API product subscription only once. Only after the API product subscription expires can the app developer purchase another subscription to the same API product.

To purchase an API product subscription, issue a `POST` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /subscriptions`

Configure the API product subscription request by passing the required fields in the request body, as described in [Resource: Subscriptions](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions). 

For example, the following API call purchases a subscription to the `HelloworldProduct` API product for the specified developer: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /subscriptions" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{"apiproduct":"HelloworldProduct"}'
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output. `startTime` is set to the current time.
    
    
    {
       "name": "69f8bb42-a8e4-4a2c-b932-d82b51d37b72",
       "apiproduct": "HelloworldProduct",
       "startTime": "1615987132000",
       "createdAt": "1615903252000",
       "lastModifiedAt": "1615903252000"
    }

For more information, see the [Purchase API product subscription API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/create)

###  App developer: Expire an API product subscription immediately 

To expire an API product subscription immediately, issue a `POST` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /subscriptions/$SUBSCRIPTION:expire`

For example, the following API call expires the API product subscription with the name `69f8bb42-a8e4-4a2c-b932-d82b51d37b72` for the specified developer: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /subscriptions/69f8bb42-a8e4-4a2c-b932-d82b51d37b72:expire" \
      -X POST \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output. `endTime` is set to the current time.
    
    
    {
      "name": "33f8dd42-c7x5-3s3f-b098-d=c93h22m36b47",
      "apiproduct": "WeatherReport",
      "startTime": "1613494852000",
      "endTime" : "1617894954000",
      "createdAt": "1613494852000",
      "lastModifiedAt": "1613494852000"
    }

###  App developer: List all API product subscriptions for a developer 

To list all API product subscriptions for a developer, issue a `GET` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /subscriptions`

Optionally, you can pass the following fields to support pagination:

  * `startKey` to specify the name of the API product subscription from which to start displaying the list of subscriptions. If omitted, the list starts from the first item. Use with `count` to provide more targeted filtering. For example, to view the API product subscriptions from 51-150, set the value of `startKey` to the name of the 51st subscription and set the value of `count` to 100.
  * `count` to specify the number of rate plans to return in the API call. Use with ` startKey` to provide more targeted filtering. The maximum limit is 1000. Defaults to 100.



For example, the following API call lists all API product subscriptions for the specified developer: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /subscriptions" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
      "developerSubscriptions": [
        {
          "name": "69f8bb42-a8e4-4a2c-b932-d82b51d37b72",
          "apiproduct": "HelloworldProduct",
          "startTime": "1615987132000",
          "createdAt": "1615903252000",
          "lastModifiedAt": "1615903252000"
        },
        {
          "name": "33f8dd42-c7x5-3s3f-b098-d=c93h22m36b47",
          "apiproduct": "WeatherReport",
          "startTime": "1614124552000",
          "createdAt": "1613494852000",
          "lastModifiedAt": "1613494852000"
        }
      ]
    }

For more information, see the [List API product subscriptions API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/list).

###  App developer: View details of an API product subscription 

To view details about an API product subscription for a developer, issue a `GET` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /subscriptions/$SUBSCRIPTION`

For example, the following API call retrieves details about an API product subscription for the specified developer: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /developers/**$DEVELOPER_EMAIL** /subscriptions/69f8bb42-a8e4-4a2c-b932-d82b51d37b72" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
       "name": "69f8bb42-a8e4-4a2c-b932-d82b51d37b72",
       "apiproduct": "HelloworldProduct",
       "startTime": "1615987132000",
       "createdAt": "1615903252000",
       "lastModifiedAt": "1615903252000"
    }

For more information, see the [Get API product subscription API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/get).

## AppGroup subscription management

This section provides examples for managing API product subscriptions for AppGroups. For additional information on the APIs used for managing AppGroup subscriptions, see [Resource: Subscriptions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions). 

### AppGroup: Purchase API product subscriptions using the API

**Note:** An AppGroup can purchase an API product subscription only once. Only after the API product subscription expires can the AppGroup purchase another subscription to the same API product.

See [ Use AppGroups to manage API product subscriptions](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview#use-appgroups-to-manage-api-product-subscriptions) for information on the requirements for using AppGroups with API product subscriptions.

To purchase an API product subscription, issue a `POST` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /appgroups/APPGROUP_ID/subscriptions`.

Configure the API product subscription request by passing the required fields in the request body, as described in [ Resource: Subscriptions](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions). 

For example, the following API call purchases a subscription to the `HelloworldProduct` API product for the specified AppGroup: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /appgroups/APPGROUP_ID/subscriptions" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{"apiproduct":"HelloworldProduct"}'
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output. `startTime` is set to the current time.
    
    
    {
       "name": "69f8bb42-a8e4-4a2c-b932-d82b51d37b72",
       "apiproduct": "HelloworldProduct",
       "startTime": "1615987132000",
       "createdAt": "1615903252000",
       "lastModifiedAt": "1615903252000"
    }

For more information, see the [Purchase API product subscription API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/create)

### AppGroup: Expire an API product subscription immediately

To expire an API product subscription immediately, issue a `POST` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /appgroups/APPGROUP_ID/subscriptions/$SUBSCRIPTION:expire`

For example, the following API call expires the API product subscription with the name `69f8bb42-a8e4-4a2c-b932-d82b51d37b72` for the specified AppGroup: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /appgroups/APPGROUP_ID/subscriptions/69f8bb42-a8e4-4a2c-b932-d82b51d37b72:expire" \
      -X POST \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output. `endTime` is set to the current time.
    
    
    {
      "name": "33f8dd42-c7x5-3s3f-b098-d=c93h22m36b47",
      "apiproduct": "WeatherReport",
      "startTime": "1613494852000",
      "endTime" : "1617894954000",
      "createdAt": "1613494852000",
      "lastModifiedAt": "1613494852000"
    }

### AppGroup: List all API product subscriptions

To list all API product subscriptions for an AppGroup, issue a `GET` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /appgroups/APPGROUP_ID/subscriptions`

Optionally, you can pass the following fields to support pagination:

  * `startKey` to specify the name of the API product subscription from which to start displaying the list of subscriptions. If omitted, the list starts from the first item. Use with `count` to provide more targeted filtering. For example, to view the API product subscriptions from 51-150, set the value of `startKey` to the name of the 51st subscription and set the value of `count` to 100.
  * `count` to specify the number of rate plans to return in the API call. Use with ` startKey` to provide more targeted filtering. The maximum limit is 1000. Defaults to 100.



For example, the following API call lists all API product subscriptions for the specified AppGroup: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /appgroups/APPGROUP_ID/subscriptions" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
      "appGroupSubscriptions": [
        {
          "name": "69f8bb42-a8e4-4a2c-b932-d82b51d37b72",
          "apiproduct": "HelloworldProduct",
          "startTime": "1615987132000",
          "createdAt": "1615903252000",
          "lastModifiedAt": "1615903252000"
        },
        {
          "name": "33f8dd42-c7x5-3s3f-b098-d=c93h22m36b47",
          "apiproduct": "WeatherReport",
          "startTime": "1614124552000",
          "createdAt": "1613494852000",
          "lastModifiedAt": "1613494852000"
        }
      ]
    }

For more information, see the [List API product subscriptions API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/list).

### AppGroup: View details about an API product subscription

To view details about an API product subscription for an AppGroup, issue a `GET` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /appgroups/APPGROUP_ID/subscriptions/$SUBSCRIPTION`

For example, the following API call lists information for an API product subscription for a specified AppGroup: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /appgroups/APPGROUP_ID/subscriptions/69f8bb42-a8e4-4a2c-b932-d82b51d37b72" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
       "name": "69f8bb42-a8e4-4a2c-b932-d82b51d37b72",
       "apiproduct": "HelloworldProduct",
       "startTime": "1615987132000",
       "createdAt": "1615903252000",
       "lastModifiedAt": "1615903252000"
    }

For more information, see the [Get API product subscription API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/get).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
