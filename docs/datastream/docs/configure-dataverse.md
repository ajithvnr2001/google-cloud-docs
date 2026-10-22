---
url: https://docs.cloud.google.com/datastream/docs/configure-dataverse/
title: Configure a Microsoft Dataverse source for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:16.271992+00:00
---

# Configure a Microsoft Dataverse source for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-dataverse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a Microsoft Dataverse source for CDC Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Datastream lets you stream change data from a Microsoft Dataverse environment to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage. To prepare your source, you register an OAuth 2.0 client in Microsoft Entra ID, configure a Dataverse application user, and allow Datastream public IP addresses if needed.

## Before you begin

Before you start configuring Dataverse for use with Datastream, you need to:

  * Have access to an active Microsoft Azure subscription with permissions to manage Azure Active Directory (AAD) and Dataverse.
  * Have an active Dataverse environment.
  * Have knowledge of how to navigate and change settings in the Microsoft Azure Portal, Dataverse, and Dynamics 365.
  * Have permissions to register applications in AAD and create or assign roles in Dataverse.



## Configure a Microsoft Dataverse environment for use with Datastream

To establish a connection between your Dataverse environment and Datastream, you need to authenticate using the OAuth 2.0 client credentials flow. This requires registering an application in AAD and configuring an application user within Dataverse.

### Register an application in Azure Active Directory

Dataverse uses AAD for authentication. To register an application, follow these steps:

  1. Sign in to the Azure Portal with an administrator account.
  2. In the portal, go to **Azure Active Directory > App registrations > New registration**.
  3. Register the application:

     1. Under **Application name** , provide the name for your application, for example, `DatastreamDataverseConnector`.
     2. Select the account type, typically, **Accounts in this organizational directory only**.
     3. Click **Register**.
  4. After registration, copy the **Application (client) ID** and the **Directory (tenant) ID** from the **Overview** page to a safe location for later use. These IDs are required for the Datastream connection profile.

  5. Generate the client secret:

     1. In your registered application settings, go to **Certificates & secrets > New client secret**.
     2. Provide a description and set an expiration date for your secret.
     3. Click **Add**.
  6. Copy the generated secret value, because it's only displayed once. You need the secret when you create the Datastream connection profile.

  7. Assign API permissions:

     1. Go to **API permissions > Add a permission**.
     2. Select **Microsoft APIs > Dynamics CRM**.
     3. Select **Application permissions**.
     4. Click **Grant admin consent for your directory**.



### Configure the Dataverse application user

Create an application user in Dataverse to represent the AAD application.

  1. Sign in to your Microsoft Dataverse environment with administrator privileges.
  2. Go to **Settings > Security > Users**.
  3. Change the view from **Enabled users** to **Application users**.
  4. Click **New** to create a new application user.
  5. Paste the **Application (client) ID** copied from AAD into the **Application ID** field. Other details, such as **User name** are automatically populated.
  6. Save the record.
  7. Assign security roles:

     1. Open the newly created application user record.
     2. Click **Manage roles**.
     3. Assign the appropriate security roles that grant the necessary read permissions for the tables that you want Datastream to replicate. We recommend using a custom role with minimum required read permissions on the specific tables rather than a broad role, such as **System administrator**. Ensure that the role has access to read table metadata.



### IP Restrictions

If your Dataverse environment or network has IP address restrictions, ensure that the [Datastream public IP addresses](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions) are allowed to connect to your Dataverse environment URL (for example, `ORGANIZATION_NAME.crm.dynamics.com`).

## What's next

  * Learn how to create a [connection profile for a Dataverse source](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4dataverse).
  * Learn more about how Datastream works with [Dataverse sources](https://docs.cloud.google.com/datastream/docs/sources-dataverse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
