---
url: https://docs.cloud.google.com/integration-connectors/docs/connectors/apigee_api_hub/configure/
title: Apigee API hub \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:12.868774+00:00
---

# Apigee API hub  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/connectors/apigee_api_hub/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Apigee API hub

The Apigee API hub connector lets you manage, discover, and govern APIs within your organization's portfolio.

## Supported versions

This connector supports the Apigee API hub version v1.

## Before you begin

  * In your Google Cloud project, do the following tasks:

    * Ensure that network connectivity is set up. For information about network patterns, see [Network connectivity](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private).
    * Grant the [roles/connectors.admin](https://docs.cloud.google.com/integration-connectors/docs/connectors-access-permissions#iam-roles-for-integration-connectors) IAM role to the user configuring the connector.
    * Enable the following services: 
      * `secretmanager.googleapis.com` (Secret Manager API)
      * `connectors.googleapis.com` (Connectors API)

To understand how to enable services, see [Enabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling). If these services or permissions have not been enabled for your project previously, you are prompted to enable them when you configure the connector.

  * If you are using the service account authentication instead of OAuth 2.0 authentication, ensure that appropriate permissions are given to the service account. For more information, see [Predefined IAM roles](https://docs.cloud.google.com/apigee/docs/apihub/iam-roles). 



## Create an Apigee API hub connection

A connection is specific to a data source. It means that if you have many data sources, you must create a separate connection for each data source. To create a connection, do the following:

  1. In the [Cloud console](https://console.cloud.google.com), go to the **Integration Connectors > Connections** page and then select or create a Google Cloud project. 

[ Go to the Connections page ](https://console.cloud.google.com/connectors/connections)

  2. Click **\+ Create new** to open the **Create Connection** page.
  3. In the **Location** section, select a location from the **Region** list and then click **Next**. 

For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/integration-connectors/docs/locations).

  4. In the **Connection Details** section, do the following: 
     1. Select the **Apigee API hub** from the **Connector** list.
     2. Select a connector version from the **Connector version** list. 
     3. In the **Connection Name** field, enter a name for the connection instance. The connection name can contain lower-case letters, numbers, or hyphens. The name must begin with a letter and end with a letter or number and the name must not exceed 49 characters. 
     4. Optionally, enter a **Description** for the connection instance.
     5. Optionally, enable [Cloud logging](https://docs.cloud.google.com/integration-connectors/docs/view-connector-logs), and then select a log level. By default, the log level is set to `Error`. 
     6. **Service Account** : Select a service account that has the required roles.
     7. (Optional) Configure the **Connection node settings**.
        * **Minimum number of nodes** : Enter the minimum number of connection nodes.
        * **Maximum number of nodes** : Enter the maximum number of connection nodes.

A node is a unit (or replica) of a connection that processes transactions. More nodes are required to process more transactions for a connection and conversely, fewer nodes are required to process fewer transactions. To understand how the nodes affect your connector pricing, see [ Pricing for connection nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes). If you don't enter any values, by default the minimum nodes are set to 2 (for better availability) and the maximum nodes are set to 50.

**Note:** You can customize the connection node values only if you are a Pay-as-you-go customer.
     8. Click **Next**.
  5. In the **Destinations** section, enter details of the remote host (backend system) you want to connect to. 
     1. In the **Destination Type** field, select a destination.
     2. In the **Host address** field, specify the hostname or IP address of the destination.
     3. Optionally, to enter additional destinations, click **+ADD DESTINATION**.

     4. Click **Next**.
  6. In the **Authentication** section, enter the authentication details. 
     1. Select an **Authentication type** and enter the relevant details. 

The following authentication types are supported by the Apigee API hub connection:

        * OAuth 2.0 - Authorization code
        * Service account authentication

To understand how to configure these authentication types, see Configure authentication.

     2. Click **Next**.
  7. Review your connection and authentication details, and then click **Create**.



### Configure authentication

Enter the details based on the authentication you want to use.

  * **OAuth 2.0 - Authorization code** : Select this option to authenticate using a web-based user login flow. Specify the following details:
    * **Client ID:** The client ID required to connect to your backend Apigee API hub service.
    * **Scopes:** A comma-separated list of desired scopes. To view all the supported OAuth 2.0 scopes for your required Google service, see the relevant section in the [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes) page. 
    * **Client secret:** Select the [Secret Manager secret](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart). You must have created the Secret Manager secret prior to configuring this authorization.
    * **Secret version:** Secret Manager secret version for client secret.

For the `Authorization code` authentication type, after creating the connection, you must authorize the connection.

  * **Service account authentication** : Select this option to authenticate using the service account that you provided in the preceding steps when configuring this connection. Ensure that you have provided the service account with the relevant IAM roles and permissions required for authentication. 
    * **Scopes:** Select the required OAuth 2.0 scopes from the drop-down. For more information, see [Access scopes](https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam).



### Authorize the connection

If you use OAuth 2.0 - authorization code to authenticate the connection, complete the following tasks after you create the connection.

  1. In the [Connections page](https://console.cloud.google.com//connectors/connections), locate the newly created connection. 

Notice that the **Status** for the new connector will be **Authorization required**.

  2. Click **Authorization required**. 

This shows the **Edit authorization** pane.

  3. Copy the **Redirect URI** value to your external application.
When you configure your third-party OAuth application, use this **authorized redirect URI** (callback URL): 

`https://console.cloud.google.com//connectors/oauth?project=PROJECT_ID`

Replace `PROJECT_ID` with your Google Cloud project ID.

  4. Verify the authorization details.
  5. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




### Re-authorization for authorization code

If you are using `Authorization code` authentication type and have made any configuration changes in the Apigee API hub, you must re-authorize your Apigee API hub connection. To re-authorize a connection, perform the following steps:

  1. Click on the required connection in the [Connections page](https://console.cloud.google.com/connectors/connections). 

This opens the connection details page.

  2. Click **Edit** to edit the connection details. 
  3. Verify the **OAuth 2.0 - Authorization code** details in the **Authentication** section. 

If required, make the necessary changes.

  4. Click **Save**. This takes you to the connection details page.
  5. Click **Edit authorization** in the **Authentication** section. This shows the **Authorize** pane.
  6. Click **Authorize**. 

If the authorization is successful, the connection status will be set to **Active** in the [Connections page](https://console.cloud.google.com//connectors/connections).




## System limitations

The Apigee API hub connector can process a maximum of 20 transactions per second, per [node](https://docs.cloud.google.com/integration-connectors/docs/pricing#payg), and [throttles](https://docs.cloud.google.com/integration-connectors/docs/rate-limiting) any transactions beyond this limit. By default, Integration Connectors allocates 2 nodes (for better availability) for a connection. 

For information on the limits applicable to Integration Connectors, see [Limits](https://docs.cloud.google.com/integration-connectors/docs/quotas).

**Note:** The number of [Integration Connectors nodes](https://docs.cloud.google.com/integration-connectors/docs/pricing#pricing-for-connection-nodes) will autoscale dynamically based on your usage. However, if you want to reserve capacity for large volumes without waiting for autoscaling, you can adjust the minimum node value for a connection. More nodes are required to process more transactions for a connection. Conversely, fewer nodes are required if a connection processes fewer transactions. To configure the node values, do the following: 

  * If you are a pay-as-you-go customer, configure the minimum and maximum node value in the edit connection page. 
  * If you are a subscription based customer, [contact support](https://docs.cloud.google.com/integration-connectors/docs/getting-support).



The maximum transactions that a node can handle depends on various factors. So, before adjusting the minimum nodes for better throughput, it is recommended you check if your backend systems are set up optimally to handle the required traffic.

## Use the Apigee API hub connection in an integration

After you create the connection, it becomes available in Application Integration. You can use the connection in an integration through the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).

### Actions

This connector provides a layer of abstraction for the objects of the connected backend service. You can access the backend's objects only through this abstraction. The abstraction is exposed to you as actions. An `Action` is a first class function that is made available to the integration through the connector interface. An action lets you make changes to an entity or entities, and varies from connector to connector. However, it is possible that a connector doesn't support any action, in which case the `Actions` list will be empty.

## Known issues

The Apigee API hub connector has configuration limits. Searchable resources are limited to 2.5 MB, and API specification files have a 10 MB limit. For more information, see [Limits on Apigee API hub](https://cloud.google.com/apigee/docs/apihub/limits).

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
