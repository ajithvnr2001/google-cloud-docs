---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config/
title: Install and configure the SAP BTP edition of ABAP SDK for Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:17.896960+00:00
---

# Install and configure the SAP BTP edition of ABAP SDK for Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install and configure the SAP BTP edition of ABAP SDK for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config)



This document describes how to install and configure SAP BTP edition of ABAP SDK for Google Cloud in the [SAP BTP, ABAP environment](https://www.sap.com/india/products/technology-platform/abap.html#overview).

This document is intended for SAP administrators, Google Cloud administrators, and other SAP and Google Cloud security professionals.

## Overview

ABAP SDK for Google Cloud provides client libraries in the form of ABAP classes for developers to programmatically access Google Cloud APIs. By encapsulating essential functions such as security, authentication, data serialization and deserialization, and error handling as reusable components, these client libraries reduce the amount of code that developers need to write. For a complete list of client libraries that the ABAP SDK for Google Cloud provides, see [ABAP SDK for Google Cloud client libraries](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview).

As an ABAP developer, you can build and deploy ML and AI-driven solutions using a wide range of Google Cloud services such as [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs), [Document AI Warehouse](https://docs.cloud.google.com/document-warehouse/docs/overview), [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview), [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), [Google Workspace APIs](https://developers.google.com/workspace), and [Google Maps Platform](https://mapsplatform.google.com/).

From version 1.1, the SAP BTP edition of ABAP SDK for Google Cloud offers a dedicated tool, Agent Platform SDK for ABAP, for seamless interaction with Google Cloud's [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) platform. For information about Agent Platform SDK for ABAP, see [Overview of the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview).

For communication between SAP and Google Cloud APIs, the ABAP SDK for Google Cloud uses HTTPS protocol with SSL.

## Before you begin

Before you install the SAP BTP edition of ABAP SDK for Google Cloud, do the following:

  1. Subscribe to the [SAP BTP Landscape Portal](https://help.sap.com/docs/btp/sap-business-technology-platform/landscape-portal). For information about subscribing to the Landscape portal, see [Subscribing to the Landscape Portal in the SAP BTP cockpit](https://help.sap.com/docs/btp/sap-business-technology-platform/accessing-landscape-portal#subscribing-to-the-landscape-portal-in-the-sap-btp-cockpit).

  2. You have a valid S-User ID associated with a customer number that has an active SAP support contract.

  3. If you're new to Google Cloud, then create an account on [https://cloud.google.com](https://cloud.google.com/).

  4. If you don't have a Google Cloud project already, then create a project:

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Make sure billing is enabled for your project. For more information, see [Verify the billing status of your project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  6. Enable the [supported APIs](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/overview) that you plan to access using the SDK. For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/docs/getting-started#enabling_apis).




## Upload the Google certificates

To secure communication between [SAP BTP, ABAP environment](https://www.sap.com/india/products/technology-platform/abap.html#overview) and Google servers, you need to upload the required Google certificates into the [Maintain Certificate Trust List](https://help.sap.com/docs/btp/sap-business-technology-platform/maintain-certificate-trust-list) app of your SAP BTP, ABAP environment.

To upload the certificates into the SAP Maintain Certificate Trust List app, you must have access to the business catalog `SAP_CORE_BC_SEC`. This business catalog is included in the predefined business role `SAP_BR_ADMINISTRATOR`.

To upload the Google certificates, perform the following steps:

  1. Download the following certificates from the [Google Trust Services repository](https://pki.goog/repository/):

     * GTS Root R1
     * GTS CA 1C3
  2. Sign in to the SAP BTP Cockpit. For more information, see the SAP page [Access the Cockpit](https://help.sap.com/docs/btp/sap-business-technology-platform/access-cockpit).

  3. Select the subaccount where your ABAP environment is hosted.

  4. Go to **Instances and Subscriptions > Instances**, and click your ABAP instance.

  5. In your ABAP environment that opens, go to **All spaces > Administration > Security**.

  6. Open the **Maintain Certificate Trust List** app.

  7. Click **Add**.

  8. Select the certificates that you downloaded from the Google Trust Services repository.

  9. Click **Upload**. The certificates are added to the trust list.




## Install the SAP BTP edition of ABAP SDK for Google Cloud

You install the SAP BTP edition of ABAP SDK for Google Cloud using [SAP BTP Landscape Portal](https://help.sap.com/docs/btp/sap-business-technology-platform/landscape-portal).

To install the SAP BTP edition of ABAP SDK for Google Cloud, perform the following steps:

  1. Get the **ABAP SDK for Google Cloud** product available in your Landscape Portal.

     1. Under the component **BC-CP-ABA** , open a medium priority case with SAP using one the following options:

        * Open a case through the [SAP for Me](https://launchpad.support.sap.com/#incident/create) application. For guidelines to open a case, see the SAP page [Submitting a Case](https://help.sap.com/docs/SAP_COMMERCE/76585cf1d1b54b238f730bcf056f3c2a/2d42670d4a07477f8a553c26e89dae3f.html).

![create case SAP for Me application](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-btp-sap-me-1.png)![create case SAP for Me application](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-btp-sap-me-2.png)

        * Open a case through the Landscape Portal. For guidelines to open a case, see the SAP page [Create Support Tickets](https://help.sap.com/docs/btp/sap-business-technology-platform/create-support-tickets).

![create case - Landscape Portal](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-btp-sap-cockpit.png)

     2. In the case description, enter the following details:
            
            We would like the following product registered to our Landscape Portal:
            * Product: /GOOG/ABAP_SDK
            * Publisher: Google
            

     3. Provide other details as appropriate and submit the case.

After SAP has confirmed that the product is registered to your Landscape Portal, proceed to the next step.

It can take up to 3 business days for the ABAP SDK for Google Cloud to be registered in your Landscape Portal. If the SDK is still not registered after this time, then contact Cloud Customer Care for assistance. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

**Note:** The requirement to submit a case to SAP for obtaining the ABAP SDK for Google Cloud is only a temporary approach until a permanent distribution mechanism is established.
  2. Deploy the **ABAP SDK for Google Cloud** product:

     1. In the Landscape Portal, open the **Deploy** app.
     2. In the **Product** field, select `/GOOG/ABAP_SDK`.
     3. In the **Target version** field, select `1.1.0`.
     4. Under **Available systems** , select the ABAP instance where you need to install the SDK.
     5. Click **Deploy**. The **Product Version Deployment Status** section shows the deployment completion status.



## Add the Fiori apps to the launchpad

From version 1.1, the SAP BTP edition of ABAP SDK for Google Cloud is packaged with SAP [Fiori apps](https://help.sap.com/docs/SAP_FIORI_OVERVIEW/f42cbf488a3c4f18a570b20c57b77cfa/d88d371a9aa54fb89fe19a16d8eb527b.html) for SDK configurations and application logging. As an administrator or developer, you use these Fiori apps to configure the SDK and configure application logging. The SDK also provides dedicated Fiori apps only for viewing authentication configurations, logging configurations, and analyzing the SDK logs.

Administrators or developers who configure the SDK and logging, or those users who only need to view the SDK configurations and logs, must have access to the relevant Fiori apps. To grant access to SDK Fiori apps, you need to add the business catalogs of ABAP SDK for Google Cloud to the business role of users who perform the SDK configuration or need to view the configurations and logging. The SAP BTP edition of ABAP SDK for Google Cloud includes business role templates that contain business catalogs required for accessing the Fiori apps.

The following table lists the business role templates and related Fiori apps that they provide access to.

Business role template | App name | Description  
---|---|---  
`/GOOG/BRT_SDK` | **Google SDK: Main Configuration** | Use this app to configure authentication to securely connect with Google Cloud APIs.  
**Google SDK: Application Log Configurations** | Use this app to configure logging to capture errors, warnings, and info messages into SAP application logs.  
**Google SDK: Application Logs Display** | Use this app to view the SDK application logs.  
**Vertex AI SDK: Configure Model Gen Parameters** | Use this app to configure model generation parameters.  
**Vertex AI SDK: Vector Search Configuration** | Use this app to configure Vector Search parameters.  
`/GOOG/BRT_SDK_DISPLAY` | **Google SDK: Display Main Configuration** | Use this app to view the SDK configurations.  
**Google SDK: Display Log Configuration** | Use this app to view the application log configurations.  
**Google SDK: Application Logs Display** | Use this app to view the SDK application logs.  
**Vertex AI SDK: Display Model Gen Parameters** | Use this app to view the model generation parameters.  
**Vertex AI SDK: Display Vector Search Config** | Use this app to view the Vector Search parameter configuration.  
  
To add the business catalogs of ABAP SDK for Google Cloud to the business role of users using the provided business role templates, you must have access to the business catalog `SAP_CORE_BC_SEC`. This business catalog is included in the predefined business role `SAP_BR_ADMINISTRATOR`.

### Create a business role and assign it to users

From version 1.1, the SAP BTP edition of ABAP SDK for Google Cloud is shipped with the predefined space `/GOOG/SDK_CONFIG_SPACE` and predefined page `/GOOG/SDK_CONFIG_PAGE`, which make it easier for you to provide your users with access to SAP Fiori apps.

To create a business role and assign it to users, perform the following steps:

  1. In your ABAP environment, go to **All spaces > Administration > Identity and Access Management**.
  2. Open the **Maintain Business Roles** app.
  3. Click **Create from template**.
  4. In the **Create Business Role from Template** dialog that appears, enter values for the following fields: 
     1. **Template** : enter `/GOOG/BRT_SDK`.
     2. **New Business Role ID** :enter a business role ID.
     3. **New business role description** : enter a description for the business role.
     4. **Option for Spaces** : verify that **Use Predefined Spaces** is selected.
     5. Click **OK**.
  5. Under **Access categories** , for the **Read, Write, Value Help** field, select **Unrestricted**.
  6. Go to the **Business Users** tab, and click **Edit** and then **Add**.
  7. In the **Add Business Users** dialog that appears, search for and select the required users who need access the SDK Fiori apps.
  8. Click **OK**. The users can see the assigned space and page with the SDK Fiori apps.
  9. Click **Save**.
  10. If you want to provide some users view-only access to the SDK Fiori apps, then repeat the steps in this section by using the following details: 
     * Create a business role by using the `/GOOG/BRT_SDK_DISPLAY` template.
     * Under **Access categories** , for the **Read, Write, Value Help** field, select **No access**.



## Configure authentication

To use the Google Cloud APIs, you must confirm your identity by authentication. For information about authentication options to Google Cloud and setup steps, see [Authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication).

## Configure logging

The SAP BTP edition of ABAP SDK for Google Cloud uses SAP application logs to save all messages raised during the execution of client library classes. Once you define a default log configuration, the SDK starts logging the messages.

The log object `/GOOG/LOG_OBJECT` and subobject `/GOOG/LOG_SUBOBJECT` are shipped with the SDK that you can use for creating your default log configuration.

You use the **Google SDK: Application Log configurations** app to create a log configuration.

You can view application logs using the **Google SDK: Application Logs Display** app. For more information, see [View logs](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting#view_logs).

To create a log configuration, perform the following steps:

  1. Access the SAP Fiori launchpad.
  2. Go to the space that contains the Fiori apps for SDK configuration.
  3. Open the **Google SDK: Application Log Configuration** app.
  4. Click **Create**.
  5. In the **Create** dialog that appears, enter a value for the following fields:

     * **Log config type** : select `OBJ_SUBOBJ`.
     * **Object** : select `/GOOG/LOG_OBJECT`.
     * **Subobject** : select `/GOOG/LOG_SUBOBJECT`.
  6. Click **Continue**.

  7. Provide the following details:

     * **Retention days** : specify the number of days the logs are going to be retained.
     * **Log level** : specify the minimum log level. The supported values are:

       * `I`: Information, Warnings, and Errors
       * `W`: Warnings and Errors
       * `E`: Errors Only We recommend that you set the log level to `I`, so that most of the log messages are logged.
     * **End at** : specify the end date till which this log configuration is going to be active. The default end date is `9999/12/31`.

     * **Is default** : To make this your default log configuration, select the checkbox.

  8. Click **Create**.




### Manage log configuration

If a log configuration is no longer required, then you can disable it.

To disable a log configuration, perform the following steps:

  1. Open the **Google SDK: Application Log Configuration** app.
  2. In the **Editing status** field, select a status as appropriate, and then click **Go**.
  3. Click the log configuration entry that you need to disable.
  4. Click **Edit**.
  5. Set the **End At** to a past date.
  6. Click **Save**.



## Specify Google Cloud API endpoint

The SAP BTP edition of ABAP SDK for Google Cloud provides the following options for specifying the API endpoint when calling a Google Cloud API using the API client library class:

  * Default endpoints
  * Custom endpoint



### Default endpoints

By default, each API class hardcodes global endpoints as a constant value. The client library uses these endpoints when a method is called to perform an operation on API resources. To use the default endpoints, no additional configuration is required.

### Custom endpoints

In scenarios, where you need the flexibility to define your own endpoints, you can create custom endpoints. For example, you create a custom endpoint to establish connection to Google Cloud when you need to do the following:

  * Access region-specific endpoints of an API for regulatory or latency-sensitive applications.
  * Use specific APIs such as Agent Platform API, which only offer regional endpoints.



To create a custom endpoint, you use the communication scenario `/GOOG/COM_SDK_SRV` that is shipped with the ABAP SDK for Google Cloud.

The following procedure illustrates how to create a regional endpoint for Pub/Sub API. You can follow the same procedure to create custom endpoints for other supported Google Cloud services.

  1. Access the SAP Fiori launchpad of the BTP ABAP system where the ABAP SDK for Google Cloud is installed.
  2. Go to **All spaces > Administration > Communication Management**.
  3. Create a communication system: 
     1. Open the **Communication Systems** app.
     2. Click **New**.
     3. In the **New Communication System** dialog that appears, enter a value for the following fields: 
        * **System ID** : enter a system ID.
        * **System name** : enter a system name.
     4. Click **Create**.
     5. In the **Host name** field, enter your custom endpoint. For example, enter a regional endpoint for the Pub/Sub service: `https://asia-east1-pubsub.googleapis.com`.
     6. In the **Port** field, enter `443`.
     7. On the **Users for Outbound Communication** tab, click **Add**.
     8. In the **Authentication method** field, select **None**.
     9. Click **Create**.
     10. To save the communication system, click **Save**.
  4. Create a communication arrangement:

     1. Open the **Communication Arrangement** app.
     2. Click **New**.
     3. In the **New Communication Arrangement** dialog that appears, enter the following details:

        * **Scenario** : select **Outbound Communication for any API** (`/GOOG/COM_SDK_SRV`).
        * **Arrangement name** : enter a name for the communication arrangement.
     4. Click **Create**.

     5. For the communication arrangement that appears, in the **Communication System** field, select the communication system that you created in the previous step.

     6. Under **Outbound communication** , in the **User name** field, select **None**.

     7. Click **Save**.

  5. Create a communication map for an API service:

     1. Go to the space that contains the Fiori apps for SDK configuration.
     2. Open the **Google SDK: Main Configuration** app.
     3. Select the client key against which you need to create a custom endpoint. It is assumed that you have already created a client key and a communication map for authentication. If not, then create a client key and a communication map for authentication. For more information, see the [Authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication).
     4. Click **Create**.
     5. In the **Create** dialog that appears, select a service name. For example, select `pubsub:v1`.
     6. Click **Continue**.
     7. For the communication map that appears, in the **Communication arrangement** field, select the communication arrangement that you created in the previous step. The other communication artifacts are autopopulated.
     8. Click **Apply**.
     9. Click **Save**.
     10. To validate the custom endpoint configuration, click **Check connection**. A green check for an entry indicates successful configuration. In case of any errors, visit the [troubleshooting](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting) page for guidance to resolve common errors.



## Usage metrics

The SAP BTP edition of ABAP SDK for Google Cloud collects usage metrics and sends them to Google for support purposes, in compliance with [Google Cloud Privacy Notice (Service Data We Collect)](https://cloud.google.com/terms/cloud-privacy-notice). These usage metrics are collected every time a Google Cloud API is called from the ABAP SDK for Google Cloud.

The SDK collects the following usage metrics:

  * Authentication method: information about the authentication method used for calling Google Cloud services.
  * ABAP SDK version: version no. of the SAP BTP edition of ABAP SDK for Google Cloud.
  * SAP_ABA release: version of the SAP_ABA software component.



## Licensing

The SAP BTP edition of ABAP SDK for Google Cloud is made available as "Software" under the agreement governing your use of Google Cloud Platform, including the Service Specific Terms available at <https://cloud.google.com/terms/service-terms>. Without limiting the generality of the preceding terms, you may not modify or distribute ABAP SDK for Google Cloud without express written permission from Google.

ABAP SDK for Google Cloud software is offered at no cost. For clarity, your use of other "Software" and "Services" under the agreement governing your use of Google Cloud Platform, such as Cloud Translation API and Pub/Sub API may incur a cost.

ABAP SDK for Google Cloud does not include any license to SAP software, you need to separately procure an appropriate license to SAP software.

## Support lifecycle

Google Cloud supports and maintains the current major version of the SAP BTP edition of ABAP SDK for Google Cloud for a period of at least 12 months following the publication of a notice of deprecation for the prior major version at [Release Notes page for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/release-notes).

## Get support

If you need help resolving problems with the SAP BTP edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ SAP BTP edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
