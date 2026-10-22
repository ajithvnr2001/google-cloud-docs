---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration/
title: Salesforce configuration \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:06.247405+00:00
---

# Salesforce configuration  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Salesforce configuration Stay organized with collections  Save and categorize content based on your preferences. 

**Private preview:** Creating and using a data store using data ingestion is in private preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). **Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the [General Service Terms section of the Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). 

## Before you begin

Use either a Salesforce enterprise or a Salesforce developer edition. Trial accounts are not supported.

## Configure Salesforce for federated data store

To configure Salesforce for a federated data store, you must obtain authentication credentials by using the OAuth 2.0 Web Server Flow authentication method. The following sections guide you through setting up the necessary components and obtaining these credentials.

### Create and configure an external client app

  1. In your Salesforce app, click the setup icon, and select **Setup**.
  2. Enter **Apps** in the quick find box and select **App manager**.
  3. Select **New external client app**.
  4. Enter the required basic information (**Name** , **API name** , and **Contact email**).
  5. In the **API (Enable OAuth settings)** section, configure the following OAuth settings. For more information, see [Enable OAuth Settings for API Integration](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create_api_integration.htm&type=5). 
     1. Select the **Enable OAuth** checkbox.
     2. Enter the **Callback URL** as `https://vertexaisearch.cloud.google.com/oauth-redirect`.
     3. In the **Selected OAuth scopes** section, add the **Manage user data via APIs (api)** , and **Perform requests at any time (refresh_token, offline_access)** scopes. For more information, see [OAuth Tokens and Scopes](https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5).
     4. In the **Flow enablement** section, select the following checkboxes: 
        1. **Enable Authorization Code and Credentials flow**
        2. **Require user credentials in the POST body for authorization code and credentials flow**
     5. In the **Security** section, select the following checkboxes: 
        1. **Require secret for Web Server Flow**
        2. **Require secret for Refresh Token Flow**
  6. Click **Create**.



### Pre-authorize external client app access

After creating the external client app, authorize specific users or permission sets to access it.

  1. In your Salesforce app, enter **External client app** in the quick find box and select **External client app manager**.
  2. Click the name of your external client app that you created. 
  3. Select the **Policies** tab and click **Edit**.
  4. In the **OAuth policies** section: 
     1. In the **Permitted users** field, select **Admin approved users are pre-authorized**.
     2. In the **App Authorization** section, in the **Refresh token policy** field, select **Refresh token is valid until revoked**.
  5. In the **App policies** section, select the profiles or permission sets authorized for this connection.
  6. Click **Save**.
  7. Navigate to the **Settings > OAuth settings**, click **Consumer key and secret** , and copy and store the consumer key and consumer secret to be used as authentication credentials.



### Find your Salesforce base URL

  1. In your Salesforce app, click the setup icon, and select **Setup**.
  2. In the quick find box, search for and select **My Domain**.
  3. From the **Current My Domain URL** field, copy and store the URL. This is the base URL of your Salesforce instance and is required as an authentication credential when you create a data store.



### Configure permissions

To verify that the user configuring the connector has the required minimum data fetching permissions, complete the following steps:

  1. In your Salesforce app, enter **Profiles** in the Quick Find box and select **Profiles**.
  2. Select the user profile running the connector.
  3. Navigate to the **Standard object permissions** section and verify the permissions.
  4. Verify that the selected user has access to the required permissions. This process must be repeated for each entity you intend to ingest. 

     * **Note:** Check whether the default access at the user's profile level is set to **Private**. When an entity's access is set to **Private** , your Google Cloud connector cannot access the required object and logs an error. 
  5. To allow access to the object, create a permission set and share it with the user:

     1. Enter **Permission sets** in the Quick Find box and select **Permission sets**.
     2. Click **New**.
     3. Enter a name and save the permission set.
     4. Open the created permission set and navigate to the **Apps** section.
     5. Select **Object settings**.
     6. Select the **View all records** checkbox.
     7. In the **Field permissions** section, grant **Read** access to all fields you want to synchronize.
     8. Save the settings and navigate back.
  6. Enable system permissions:

     1. In the **System** section, select **System permissions**.
     2. Enable the **API enabled** permission.
  7. Assign the user to the permission set:

     1. Enter **Users** in the Quick find box and select **Users**.
     2. Select the user.
     3. In the **Permission set assignments** section, select **Edit assignments**.
     4. Add the recently created permission set to the **Enabled permission sets** section.



For more information, see [Data access in Salesforce](https://developer.salesforce.com/docs/atlas.en-us.salesforce_record_access_under_the_hood.meta/salesforce_record_access_under_the_hood/uth_intro.htm) and [Organization-Wide Sharing Defaults](https://trailhead.salesforce.com/content/learn/modules/lex_implementation_user_setup_mgmt/lex_implementation_user_setup_mgmt_configure_user_access-hoc).

## Configure Salesforce for data ingestion data store

To configure Salesforce for a data ingestion data store, follow the steps in this section.

### Supported versions

The Salesforce V2 connector supports SOAP API version 30.0 or later.

### Generate a service attachment

To generate a service attachment, perform the following steps:

  * For **Public** endpoint: If the Salesforce data center **Destination type** is **Public** , you are not required to create the setup for service attachment. Instead, you can use your public URL in the **Domain URL** field of the Google Cloud console.
  * For **Private** endpoint: 
    1. Use [PSC](https://docs.cloud.google.com/vpc/docs/private-service-connect) to enable connections from private instances to Google Cloud.
    2. Create a Virtual Private Cloud network and the required subnets.
    3. Create a Virtual Machine (VM) instance and install the backend service.
    4. Optional: Set up a [health check](https://docs.cloud.google.com/load-balancing/docs/internal#health-checking) probe to monitor backend health.
    5. Add a load balancer to route traffic to the VM or backend.
    6. Define firewall rules to allow traffic between the PSC endpoint and the backend.
    7. [Publish the endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) by creating a PSC service attachment.

**Note:** Creating a PSC setup is not mandatory for VPC-SC enabled projects.

### Generate authentication credentials

Data ingestion data stores can use any of the following supported authentication types:

  * OAuth 2.0 - Client credentials
  * OAuth 2.0 - JWT bearer
  * Username and password

**Note:** If you are using OAuth authentication, you must install the external client app in your Salesforce account after creating the connection. See Install the OAuth connected app.

### Set up for OAuth 2.0 - Client credentials authentication

You must set up Gemini Enterprise as an external client app ([connected app](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create.htm&type=5)) in Salesforce to obtain the following authentication information:

  * Consumer ID or client ID
  * Consumer secret or client key



#### Create and configure an external client app

  1. In your Salesforce app, click the setup icon, and select **Setup**.
  2. Enter **Apps** in the quick find box and select **App manager**.
  3. Select **New external client app**.
  4. Enter the required basic information (**Name** , **API name** , and **Contact email**).
  5. In the **API (Enable OAuth settings)** section, configure the following OAuth settings. For more information, see [Enable OAuth Settings for API Integration](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create_api_integration.htm&type=5). 
     1. Select the **Enable OAuth** checkbox.
     2. Enter the **Callback URL** as `https://vertexaisearch.cloud.google.com/oauth-redirect`.
     3. In the **Selected OAuth scopes** section, add the **Full access (full)** , **Manage user data via APIs (api)** , and **Perform requests at any time (refresh_token, offline_access)** scopes. For more information, see [OAuth Tokens and Scopes](https://help.salesforce.com/s/articleView?language=en_US&id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5).
     4. In the **Flow enablement** section, select the **Enable client credentials flow** checkbox.
  6. Click **Create**.



#### Pre-authorize external client app access

After creating the external client app, authorize specific users or permission sets to access it.

  1. In your Salesforce app, enter **External client app** in the quick find box and select **External client app manager**.
  2. Click the name of your external client app that you created. 
  3. Select the **Policies** tab and click **Edit**.
  4. In the **OAuth policies** section: 
     1. In the **Permitted users** field, select **Admin approved users are pre-authorized**.
     2. Under **OAuth flow and external client enhancement** , select **Enable client credentials flow** and enter the user's email ID.
     3. In the **Refresh token policy** field, select **Refresh token is valid until revoked**.
  5. In the **App policies** section, select the profiles or permission sets authorized for this connection.
  6. Click **Save**.
  7. Navigate to the **Settings > OAuth settings**, click **Consumer key and secret** , and copy and store the consumer key and consumer secret to be used as authentication credentials.



#### Configure permissions

To verify that the user configuring the connector has the required minimum data fetching permissions, complete the following steps:

  1. In your Salesforce app, enter **Profiles** in the Quick Find box and select **Profiles**.
  2. Select the user profile running the connector.
  3. Navigate to the **Standard object permissions** section and verify the permissions.
  4. Verify that the selected user has access to the required permissions. This process must be repeated for each entity you intend to ingest. **Note:** Check whether the default access at the user's profile level is set to **Private**. When an entity's access is set to **Private** , your Google Cloud connector cannot access the required object and logs an error.
  5. To allow access to the object, create a permission set and share it with the user: 
     1. Enter **Permission sets** in the Quick Find box and select **Permission sets**.
     2. Click **New**.
     3. Enter a name and save the permission set.
     4. Open the created permission set and navigate to the **Apps** section.
     5. Select **Object settings**.
     6. Select the **View all records** checkbox.
     7. In the **Field permissions** section, grant **Read** access to all fields you want to synchronize.
     8. Save the settings and navigate back.
  6. Enable system permissions: 
     1. In the **System** section, select **System permissions**.
     2. Enable the following minimum permissions: 
        * **API enabled**
        * **View all users**
        * **View roles and role hierarchy**
        * **View setup and configuration**
  7. Assign the user to the permission set: 
     1. Enter **Users** in the Quick find box and select **Users**.
     2. Select the user.
     3. In the **Permission set assignments** section, select **Edit assignments**.
     4. Add the recently created permission set to the **Enabled permission sets** section.



For more information, see [Data access in Salesforce](https://developer.salesforce.com/docs/atlas.en-us.salesforce_record_access_under_the_hood.meta/salesforce_record_access_under_the_hood/uth_intro.htm) and [Organization-Wide Sharing Defaults](https://trailhead.salesforce.com/content/learn/modules/lex_implementation_user_setup_mgmt/lex_implementation_user_setup_mgmt_configure_user_access-hoc).

### Set up for OAuth 2.0 - JWT bearer authentication

You must set up Gemini Enterprise as an external client app (connected app) in Salesforce to obtain the following authentication information:

  * Customer key
  * Public key
  * Username



#### Generate private key and public certificate

  1. Generate a 2048-bit RSA private key by executing the following command: **openssl genrsa -out server.key 2048**

This command creates a file named **server.key** , which contains your private key. Keep this file secure and confidential.

  2. Generate a self-signed public certificate by executing the following command: **openssl req -new -x509 -sha256 -days 3650 -key server.key -out server.crt**

This command generates a file named **server.crt** , which is your public certificate. You can upload this certificate to Salesforce during the external client app (connected app) configuration.




#### Create and configure external client app

  1. In your Salesforce app, click the setup icon, and then select **Setup**.
  2. Enter **Apps** in the quick find box and select **App manager**.
  3. Select **New external client app**.
  4. Enter the required basic information for your external client app (connected app), such as the **External client app name** , **API name** , and **Contact email**.
  5. In the **API (Enable OAuth settings)** section, configure the following OAuth settings. For more information, see [Enable OAuth Settings for API Integration](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create_api_integration.htm&type=5). 
     1. Select the **Enable OAuth** checkbox.
     2. Enter the **Callback URL** as `https://vertexaisearch.cloud.google.com/oauth-redirect`.
     3. In the **Selected OAuth scopes** section, add **Full access (full)** , **Manage user data via APIs (api)** , and **Perform requests at any time (refresh_token, offline_access)**. For more information, see [OAuth Tokens and Scopes](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5).
     4. In the Flow enablement section: 
        1. Select **Enable JWT bearer flow**.
        2. Upload the **server.crt** generated in the Generate private key and public certificate section. 



#### Get login URL

To get the login URL for your Salesforce instance, do the following:

  1. In your Salesforce app, enter **My domain** in the quick find box and select **My domain**.
  2. Copy the domain ending in **my.salesforce.com**.
  3. Add **https://** to the beginning of the copied domain. This is the instance URL that you need to create the Salesforce connector in Gemini Enterprise. The instance URL must be in the following format: **https://DOMAIN_NAME.my.salesforce.com**.



### Install the OAuth connected app

You must install the external client app that you created. Navigate to the **Connected Apps OAuth Usage** page in your Salesforce account and install the app. For more information, see [Connected App Usage Restrictions Change](https://help.salesforce.com/s/articleView?id=005132365&type=1).

### Set up for username and password authentication

For username and password authentication, use an existing security token, or reset the security token to receive a new one in your registered email.

To reset your security token:

  1. In your Salesforce app, click your profile icon and select **Settings**. ![Settings](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/salesforce-v2/settings.png)Settings
  2. Navigate to **Reset my security token** and click **Reset security token**. ![Reset Security Token button](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/salesforce-v2/resetsecuritytoken.png)Reset security token



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
