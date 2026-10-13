---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-oauth-client-credentials/
title: Authenticate to Google Workspace APIs with OAuth 2.0 client credentials \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:32.628999+00:00
---

# Authenticate to Google Workspace APIs with OAuth 2.0 client credentials  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-oauth-client-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authenticate to Google Workspace APIs with OAuth 2.0 client credentials Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication-oauth-client-credentials)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-oauth-client-credentials)



This document shows how to set up authentication to access [Google Workspace APIs](https://developers.google.com/workspace) with OAuth 2.0 client credentials. OAuth 2.0 client credentials let you retrieve a token in the context of an end user, such as a token required to access [Google Sheets](https://developers.google.com/sheets/api/reference/rest). Regardless of where your SAP system is hosted, you can use OAuth 2.0 client credentials for authentication to Google Workspace APIs as long as the system supports OAuth 2.0.

To authenticate to Google Workspace APIs using OAuth 2.0 client credentials, you need to complete the following configurations in your Google Cloud project and your SAP landscape:

**Google Cloud console configurations**

  * Create OAuth 2.0 consent
  * Create OAuth 2.0 client ID credentials



**SAP landscape configurations**

The ABAP SDK for Google Cloud is shipped with the following core components, which are required for the OAuth 2.0 client credentials based authentication:

  * OAuth 2.0 service provider type `/GOOG/ABAP_SDK` that you specify for your OAuth 2.0 client profile configuration.
  * Authentication class `/GOOG/CL_OAUTH_GOOGLE` that you specify for the client key configuration.
  * SAP [Business Add-Ins (BAdIs)](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/8f/f2e540f8648431e10000000a1550b0/frameset.htm) implementations that pre-populate Google specific OAuth parameters such as endpoints and required parameter settings.



However, you also need to complete the following configurations in your SAP landscape:

  * Create OAuth 2.0 client profile
  * Configure OAuth 2.0 client
  * Configure client key
  * Request OAuth 2.0 access tokens



## Create OAuth 2.0 consent

The _OAuth consent screen_ is a prompt that tells users who's requesting access to their data and what kind of data users are allowing your app to access.

  1. In the Google Cloud console, go to **Menu menu > APIs & Services > OAuth consent screen**.

[Go to OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent)

  2. Select the **External** user type for your app, and click **Create**.

  3. To complete the app registration form, specify the following details:

     * **App name** : the name of the application that requires consent.
     * **User support email** : a support email for users to contact you with questions about their consent.
     * **Authorized domains** : the domains to be used during OAuth consent.
     * **Developer contact information** : the email addresses for Google to notify you about any changes to your project.
  4. Click **Save and Continue**.




## Create OAuth 2.0 client ID credentials

To authenticate as an end user and access user data in your app, you need to create one or more OAuth 2.0 Client IDs. A client ID is used to identify a single app to Google's OAuth servers.

  1. In the Google Cloud console, go to **Menu menu > APIs & Services > Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create Credentials > OAuth client ID**.

  3. In the **Application type** field, select **Web application**.

  4. In the **Name** field, type a name for the credentials. This name is shown only in the Google Cloud console.

  5. Under **Authorized redirect URIs** , click **Add URI**. Then, enter your SAP redirection URI to which the OAuth 2.0 server can send responses.

You can get the SAP redirection URI from the OAuth 2.0 settings in your `SICF` transaction.

  6. Click **Create**.

  7. Make a note of the **Client ID** and the **Client secret**.




## Create OAuth 2.0 client profile

As an ABAP developer, you create an OAuth client profile with the OAuth 2.0 scopes that are required for your business requirements. For information about the OAuth 2.0 scopes for the Google APIs, see [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes).

The SDK includes a sample OAuth client profile named `/GOOG/OAUTH_PROFILE_SAMPLE`. This profile provides OAuth 2.0 scopes configured for commonly used Google Workspace APIs, such as Drive and Sheets.

  1. In the SAP GUI, enter transaction code `SE80`.
  2. From the drop down list, select **Development Object**.
  3. To create a development object in the custom namespace, select **Create > Others > OAuth 2.0 Client Profile** in the context menu of the object name.
  4. Enter the following details:

     * In the **Client Profile** field, enter a name of the client profile.
     * In the **Type** field, select `/GOOG/ABAP_SDK`. This is the default provider type shipped with the ABAP SDK for Google Cloud.
  5. Add the necessary scopes to your client profile. For information about the OAuth 2.0 scopes, see [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes).

  6. Save the client profile to your development package. Include the client profile in a transport request, which can be transported to higher environments.




## Configure OAuth 2.0 client

As an SAP administrator, you associate the OAuth client profile with the Google Cloud client credentials.

This is a onetime activity that you need to perform on every SAP system in your SAP landscape (Development, Testing, and Production).

  1. In the SAP GUI, enter transaction code `OA2C_CONFIG`. The SAP login page opens in your default browser.
  2. Log in with your SAP credentials.
  3. To create an OAuth 2.0 client, click **Create**.
  4. In the **Create a new OAuth 2.0 client** dialog box: 
     1. Select the OAuth 2.0 client profile that you created earlier in Create OAuth 2.0 client profile in your SAP system.
     2. Enter a configuration name.
     3. Enter the OAuth 2.0 Client ID from Google Cloud credentials that you created earlier in Create OAuth 2.0 client ID credentials.
     4. Click **OK**.
  5. On the **Administration** tab, in the **General Setting** section, enter the client secret from the Google Cloud credentials that you created earlier in Create OAuth 2.0 client ID credentials.
  6. If you are using a proxy server to route the outbound HTTP/HTTPS traffic from your SAP system, then you need to maintain the following proxy host details in the **Access Settings** section:

     * Proxy host
     * Proxy port
     * Proxy user
     * Proxy password
  7. Click **Save**.




## Configure client key

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`. 

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.
  3. Click **New Entries**.
  4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration.  
**Google Cloud Service Account Name** | Leave this field blank.  
**Google Cloud Scope** | Leave this field blank.  
**Google Cloud Project Identifier** | Specify the ID of the Google Cloud project that contains your target APIs.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the authentication class, `/GOOG/CL_OAUTH_GOOGLE`.  
**Token Caching** | Leave this field blank.  
**Token Refresh Seconds** | Leave this field blank.  
**Authorization Parameter 1** | Specify the name of the OAuth client profile that you created earlier in Create OAuth 2.0 client profile in your SAP system.  
**Authorization Parameter 2** | Specify the configuration name that you defined in the OAuth 2.0 client for a client ID. This field is mandatory if you have associated a single OAuth client profile with more than one client ID. For more information, see Multiple Google Cloud projects scenario.  
  5. Save the new entry.




## Request OAuth 2.0 access tokens

As an end user, you need to request an OAuth 2.0 access token to allow access to the API resources.

This is a onetime activity that each user needs to perform on every SAP system in your SAP landscape (Development, Testing, and Production). In case the OAuth scopes are modified, then users need to repeat this activity.

  1. In the SAP GUI, enter transaction code `OA2C_GRANT`. The SAP login page opens in your default browser.
  2. Log in with your SAP credentials.
  3. Select the client ID with which you want to access the APIs.
  4. Click **Request OAuth 2.0 Tokens**.
  5. In the **Sign in with Google** consent screen, enter your Google account credentials and click **Allow**.

A green indicator in the **Access Status** column indicates access to the API resources is allowed as per the OAuth 2.0 client profile.




## Multiple Google Cloud projects scenario

If you have enabled your Google Cloud APIs in more than one Google Cloud project, then follow this guidance for setting up authentication using OAuth 2.0 client credentials:

  * In all the Google Cloud projects: 
    * Create OAuth 2.0 consent
    * Create OAuth 2.0 client ID credentials
  * In your SAP system: 
    * Create an OAuth 2.0 client profile.
    * Configure OAuth 2.0 client for each client ID.
  * If you need to associate a single OAuth client profile against more than one client ID, then follow these additional instructions: 
    * Configure OAuth 2.0 client for each client ID. When configuring an OAuth 2.0 client, in the **Create a new OAuth 2.0 client** dialog box, specify a unique configuration name for each client ID. For more information, see Configure OAuth 2.0 client.
    * Configure separate client keys for each OAuth 2.0 client with its own configuration name in **Authorization Parameter 2**. For more information, see Configure client key.



## Validate authentication configuration

To validate the authentication configuration for its readiness, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Utilities > Validate Authentication Configuration**.

  3. Enter the client key name.

  4. Click **Execute**.

A green check in the **Result** column indicates that all configurations steps are completed successfully.




## Get support

If you need help resolving problems with the on-premises or any cloud edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ on-premises or any cloud edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
