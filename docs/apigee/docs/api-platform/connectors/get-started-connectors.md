---
url: https://docs.cloud.google.com/apigee/docs/api-platform/connectors/get-started-connectors/
title: Get started with connectors \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:37.455672+00:00
---

# Get started with connectors  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/connectors/get-started-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Get started with connectors Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This tutorial shows you how to use Application Integration and connectors to create a sample integration that triggers the publication of a Cloud Pub/Sub message. The tutorial assumes that you have a working knowledge of [Application Integration](https://docs.cloud.google.com/apigee/docs/api-platform/integration/what-is-apigee-integration).

In this example, calling an API endpoint triggers the publication of a message to a Cloud Pub/Sub topic. The steps below describe how to configure the API trigger and Pub/Sub connection required to run a successful integration.

## Before you begin

Before beginning this tutorial, confirm your Google Cloud login credentials and organization details. This information is required to access connectors UI. Your Apigee credentials are required to access the connectors task within the Application Integration designer. Additional prerequisite steps are described below: 

  * Before creating a connection _for the first time_ , complete the following steps: **Note** : These steps are only required if you are enabling the Application Integration and Connectors add-ons for the first time for use with Apigee.

    1. Create a new Apigee instance. New Apigee instances can be provisioned with the [Provisioning UI](https://apigee.google.com/setup?project=). 

For the list of regions supporting connectors, see [Supported connector regions](https://docs.cloud.google.com/apigee/docs/api-platform/connectors/manage-connections#supported-regions).

    2. Confirm that the Application Integration and connectors features are entitled to your Apigee subscription.
    3. Enable the Application Integration and connectors features using the following command: 
           
           curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H \
           "content-type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/PROJECT_ID:setAddons" -XPOST \
           -d '{"addonsConfig": {"integrationConfig": {"enabled": true}, "connectorsPlatformConfig": {"enabled": true}}}'

**Warning** : When you run an add-on command, it overwrites any existing add-ons. Therefore, if you have any existing add-ons, include them in the add-on command. Otherwise, the command to enable Application Integration and connectors will disable all other add-ons in your existing organization. And if an add-on is disabled, Apigee deletes all configurations of the add-on (feature). For example, if you disable the Integrations add-on, all integrations are deleted. 
    4. If you don't have a service account, create a service account. 

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating).

## Enable required services

Connectors requires that you enable the following Google services: 

Name | Title  
---|---  
`apigee.googleapis.com` | Apigee API  
`secretmanager.googleapis.com` | Secret Manager API  
`connectors.googleapis.com` | Connectors API  
  
If these services have not been enabled for your project previously, you are prompted to enable them when creating the connection in the Create Connection page. 

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

## What's next 

    * Learn how to [create and use a Pub/Sub connection in your integration](https://docs.cloud.google.com/apigee/docs/api-platform/integration/get-started-connectors).
    * See the list of [supported connectors](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors).
    * Learn how to [create and manage connections](https://docs.cloud.google.com/integration-connectors/docs/manage-connectors).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
