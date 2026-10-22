---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_search_ads_360/configure/
title: Search Ads 360 \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:10.942099+00:00
---

# Search Ads 360  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_search_ads_360/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Search Ads 360

The Search Ads 360 connector lets you perform the supported operations on [Search Ads 360](https://developers.google.com/search-ads).

## Before you begin

Before using the Search Ads 360 connector, do the following tasks:

  * In your Google Cloud project: 
    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private).
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Grant the following IAM roles to the service account that you want to use for the connector: 
      * `roles/secretmanager.viewer`
      * `roles/secretmanager.secretAccessor`

A service account is a special type of Google account intended to represent a non-human user that needs to authenticate and be authorized to access data in Google APIs. If you don't have a service account, you must create a service account. The connector and the service account must belong to the same project. For more information, see [Creating a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating). 

    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

If these services or permissions have not been enabled for your project previously, you are prompted to enable them when configuring the connector. 

  * If you are using the service account authentication instead of OAuth 2.0 authentication, ensure that appropriate permissions are given to the service account. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/integration-connectors/docs/connectors/gsc_search_ads_360/configure/).



## Configure the connector

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, choose the location for the connection. 
     1. **Region** : Select a location from the drop-down list. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

     2. Click **Next**.


* In the **Connection Details** section, set the following fields: 

  1. **Connector** : Select **Search Ads 360** from the drop down list of available connectors.
  2. **Connector version** : Select the connector version from the drop down list of available versions. 
  3. In the **Connection Name** field, enter a name for the connection instance. 

Connection names must meet the following criteria: 

     * Connection names can use letters, numbers, or hyphens.
     * Letters must be lower-case.
     * Connection names must begin with a letter and end with a letter or number.
     * Connection names cannot exceed 49 characters.
  4. Optionally, enter a **Description** for the connection instance.
  5. Optionally, select **Enable cloud logging** if you want to log the connector execution details.
  6. **Service Account** : Select a service account that has the required roles.
  7. Optionally, configure the **Connection node settings** : 

     * **Minimum number of nodes** : Enter the minimum number of connection nodes.
     * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
  8. Optionally, click **\+ Add label** to add a label to the connection in the form of a key-value pair.
  9. Click **Next**.
  10. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

You can choose any of the following authentication types:

        * OAuth 2.0 - Authorization code 

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  11. **Review** : Review your connection and authentication details.
  12. Click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 - Authorization code**
    * **Client ID** : The client ID required to connect to your backend Google service.
    * **Scopes** : Select the required OAuth 2.0 scopes from the drop-down. To view all the supported OAuth 2.0 scopes for your required Google service, see the relevant section in the [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes) page.
    * **Client Secret** : Select the Secret Manager secret containing the password associated with the client secret.
    * **Secret version** : Select the secret version.



## Actions

This connector provides a layer of abstraction for the objects of the connected backend service. You can access the backend's objects only through this abstraction. The abstraction is exposed to you as actions. An `Action` is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and varies from connector to connector. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty.

**Note:** You can view the actions of the connector in the [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task).

## Use the Search Ads 360 connection in an integration

After you create the connection, it becomes available in Application Integration. You can use the connection in an integration through the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).

## Get help from the Google Cloud community

You can post your questions and discuss this connector in the Google Cloud community at [Cloud Forums](https://www.googlecloudcommunity.com/gc/Integration-Services/bd-p/cloud-integration-services). 

## What's next

  * Understand how to [suspend and resume a connection](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection).
  * Understand how to [monitor connector usage](https://docs.cloud.google.com/integration-connectors/docs/cloud-monitoring).
  * Understand how to [view connector logs](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
