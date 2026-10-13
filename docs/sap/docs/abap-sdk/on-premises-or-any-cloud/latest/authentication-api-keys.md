---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys/
title: Authenticate with API keys \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:08.079109+00:00
---

# Authenticate with API keys  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authenticate with API keys Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication-api-keys)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-api-keys)



This document shows how to set up authentication to access Google Cloud APIs with API keys. Only a few Google Cloud APIs use API keys for authentication, for example, Google Maps Platform. Review the authentication documentation for the service or API that you want to use to determine whether it supports API keys. Regardless of where your SAP system is hosted, you can use API keys for authentication as long as the API that you want to use supports API keys.

To authenticate to Google Cloud API using API keys, use one of the following methods:

  * Authenticate with API keys stored in SAP SSF
  * Authenticate with API keys stored in Secret Manager



For information about other supported authentication methods, see [Authentication overview for the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

## Authenticate with API key stored in SAP SSF

The high-level configuration steps are as follows:

  * Create an API key
  * Store the API key in SSF
    * Set up SSF application
    * Create SSF parameters
    * Create a Personal Security Environment (PSE)
    * Store the API key
  * Configure client key
  * Create new RFC destinations
  * Configure service mapping
  * Validate authentication configuration



### Create an API key

For authentication using API key, you need to create an API key. An API key string is an encrypted string, for example, `AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe`. ABAP SDK for Google Cloud uses the API key string in HTTP request to securely authenticate when calling a Google Cloud API.

Google Cloud provides multiple ways to [create API keys](https://docs.cloud.google.com/docs/authentication/api-keys).

To create API keys using the Google Cloud console, perform the following steps:

  1. In the Google Cloud console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create Credentials** and select **API key** from the menu.

     * The **API key created** dialog displays the API key string. Copy your key string and keep it secure. You need this API key to configure authentication to Google Cloud.

     * By default, API keys are unrestricted. We recommended that you restrict API keys by selecting the APIs to which this API key can be used. For more information about adding API restrictions, see [Add API restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#adding-api-restrictions).




### Store the API key in SSF

The ABAP SDK for Google Cloud provides an option to securely store API keys using the [SAP Secure Store and Forward mechanism (SSF)](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/4d/bf6f77a2c5446a86e0152f1b309db6/content.htm?no_cache=true).

By using the SSF option, you can store the API Key in an encrypted format in the table `/GOOG/APIKEY_BIN`. When an API is called, the API key would be retrieved from the table `/GOOG/APIKEY_BIN`, decrypted, and appended to the API endpoint URI.

For security purposes, you cannot view the contents of `/GOOG/APIKEY_BIN` using standard tools, transactions such as `SE16`, `SE16N`, or `SE11`.

  * Using API key from SAP SSF is a secure way of **locally** storing API key strings (encrypted) with SAP Cryptographic Library.
  * You need to set up SSF application in every SAP system.



#### Prerequisites

For authentication using API key stored in SAP SSF, you must have version 8.5 and above of the SAP Cryptographic Library installed in your SAP system. For more information about SAP Cryptographic Library, see [1848999 - Central Note for CommonCryptoLib 8 (SAPCRYPTOLIB)](https://launchpad.support.sap.com/#/notes/1848999) and [397175 - SAP Cryptographic software - export control](https://launchpad.support.sap.com/#/notes/397175).

To verify the version of SAP Cryptographic Library, perform the following steps:

  1. In the SAP GUI, enter transaction code `STRUST`.
  2. Go to the **Environment** menu, and then click **Display SSF Version**.



#### Set up SSF application

In the table `SSFAPPLIC`, create a new SSF application `ZG_APK` that encrypts the API key. `ZG_APK` is the default SSF application name.

Alternatively, you can create an SSF application with your preferred name or use an existing SSF application that has a different name. If you want to use a different SSF application for encryption, then you need to configure the SSF application name in `Authorization Parameter 1` of the client key table.

To create a new entry in the table `SSFAPPLIC`, perform the following steps:

  1. In the SAP GUI, enter transaction code `SE16`.
  2. In the **Table Name** field, enter `SSFAPPLIC`, and then create a new entry.
  3. In the `APPLIC` field, enter `ZG_APK`.
  4. Specify values in the following fields.

Field | Value  
---|---  
`APPLIC` | `ZG_APK`  
`B_TOOLKIT` | Select the flag.  
`B_FORMAT` | Select the flag.  
`B_PAB` | Select the flag.  
`B_PROFID` | Select the flag.  
`B_PROFILE` | Select the flag.  
`B_HASHALG` | Leave this field blank.  
`B_ENCRALG` | Leave this field blank.  
`B_INCCERTS` | Leave this field blank.  
`B_DETACHED` | Leave this field blank.  
`B_ASKPWD` | Leave this field blank.  
`B_DISTRIB` | Select the flag.  
`DESCRIPT` | `API Key Encryption for GCP`  
  5. Save the new entry.




##### Create SSF parameters

  1. In the SAP GUI, enter transaction code `SM30`.

  2. Open the view `VSSFARGS`.

  3. For application `ZG_APK` (`API Key Encryption for GCP`), create a new entry. The application specific SSF parameters are automatically populated.

  4. Save the new entry.




#### Create a Personal Security Environment (PSE)

  1. In the SAP GUI, enter transaction code `STRUST`.

  2. Under node **SSF API Key Encryption for GCP** , right-click and select **Create**.

  3. In the **Algorithm** field, select `RSA`. Leave other fields with system-populated default values.

  4. Save the new entry.




#### Store the API key

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure API Key (Using SSF)**.

  3. In the **Google Key Name** , enter the name of the client key configuration.

  4. In the **API Key** field, enter the API key that you created earlier in Create an API key.

  5. Select **Save**.

  6. Click **Execute** to store the API key.




### Configure client key

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration. For example, `DEMO_API_KEY`.  
**Google Cloud Service Account Name** | Leave this field blank.  
**Google Cloud Scope** | Specify the API access scope, `https://www.googleapis.com/auth/cloud-platform`.  
**Project ID** | Specify the ID of the Google Cloud project that contains your target APIs.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the authorization class, `/GOOG/CL_AUTH_API_KEY_SSF`.  
**Token Caching** |  The flag that determines whether or not the access tokens retrieved from Google Cloud are cached. We recommend that you enable token caching after you are done configuring and testing your connection to Google Cloud. For more information about token caching, see [Enable token caching](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#token_caching).  
**Token Refresh Seconds** | Specify the amount of time, in seconds, before an access token expires and must be refreshed. The default value is `3500`.  
**Authorization Parameter 1** | If the SSF application name is different from `ZG_APK`, then specify your SSF application name.  
**Authorization Parameter 2** | Leave this field blank.  
  5. Save the new entry.




### Create new RFC destinations

For the APIs that you plan to consume using the ABAP SDK for Google Cloud, create new RFC destinations.

For information about creating RFC destinations, see [RFC destinations](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#create_rfc_destinations).

If RFC destinations are not created and configured, the ABAP SDK for Google Cloud functions using the default API endpoints maintained in individual API client stubs.

### Configure service mapping

Configure the service mapping table for the APIs that you plan to consume using the ABAP SDK for Google Cloud.

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Service Mapping**.

  3. Click **New Entries**.

  4. Specify RFC destinations for the APIs that you plan to use, for example, `addressvalidation v1`. If you're going to consume other APIs, then specify RFC destinations for those APIs.

Name | Service Name | RFC Destination  
---|---|---  
**Google Cloud Key Name** | `addressvalidation:v1` | `ZGOOG_ADDRVALDN_V1`  
  5. Save the new entry.




### Delete an API key

If an API key is no longer used, then you can delete the API key from your SAP system.

To delete an API key, peRForm the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure API Key (Using SSF)**.

  3. In the **Google Key Name** field, enter the name of the client key configuration.

  4. Select **Delete**.

  5. Click **Execute** to delete the API key.




## Authenticate with API key stored in Secret Manager

The high-level configuration steps are as follows:

  * Create an API key
  * Create a secret and store the API key
  * Configure client key for Secret Manager access
  * Configure client key for the secret
  * Create new RFC destinations
  * Configure service mapping
  * Validate API key retrieval from Secret Manager
  * Validate authentication configuration



### Create an API key

For authentication using API key, you need to create an API key. An API key string is an encrypted string, for example, `AIzaSyDaGmWKa4JsXZ-HjGw7ISLn_3namBGewQe`. ABAP SDK for Google Cloud uses the API key string in HTTP request to securely authenticate when calling a Google Cloud API.

Google Cloud provides multiple ways to [create API keys](https://docs.cloud.google.com/docs/authentication/api-keys).

To create API keys using the Google Cloud console, perform the following steps:

  1. In the Google Cloud console, go to the **Credentials** page:

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **Create Credentials** and select **API key** from the menu.

     * The **API key created** dialog displays the API key string. Copy your key string and keep it secure. You need this API key to configure authentication to Google Cloud.

     * By default, API keys are unrestricted. We recommended that you restrict API keys by selecting the APIs to which this API key can be used. For more information about adding API restrictions, see [Add API restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#adding-api-restrictions).




### Create a secret and store the API key

The ABAP SDK for Google Cloud provides an option to securely store API keys using the [Secret Manager service](https://docs.cloud.google.com/secret-manager/docs/overview) of Google Cloud. For securely storing API key strings, Secret Manager enables you to follow the [best practices for securely using API keys](https://support.google.com/googleapi/answer/6310037).

Using Secret Manager for storing API keys provides the following benefits: 

  * Offers a central way of managing and maintaining the API keys.
  * Allows you to set automated rotation policies.
  * Offers more features, such as, CMEK, Replication Policy.



To create a secret and store the API key, perform the following steps:

  1. Enable the Secret Manager API.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/secretmanager.googleapis.com)

  2. In Google Cloud console, create a secret, and store the API key as the latest version.

[Go to Secret manager](https://console.cloud.google.com/security/secret-manager)




For information about how to create a secret, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

The ABAP SDK for Google Cloud by default retrieves only the latest version of a secret.

### Configure client key for Secret Manager access

Secret Manager APIs use tokens for authentication. So you need to set up token based authentication to access Secret Manager APIs depending on your SAP deployment.

Use one of the following methods to set up token based authentication to access Secret Manager APIs:

  * [Authenticate with access tokens](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-access-token)
  * [Authenticate with JSON Web Tokens (JWT)](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt)
  * [Authenticate with tokens through Workload Identity Federation](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif)



Note down the client key name that you created for Secret Manager access.

### Configure client key for the secret

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration. For example, `DEMO_API_KEY`.  
**Google Cloud Service Account Name** | Leave this field blank.  
**Google Cloud Scope** | Specify the API access scope, `https://www.googleapis.com/auth/cloud-platform`.  
**Project ID** | Specify the ID of the Google Cloud project that contains your target APIs.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify `/GOOG/CL_AUTH_API_KEY_SM`.  
**Token Caching** |  The flag that determines whether or not the access tokens retrieved from Google Cloud are cached. We recommend that you enable token caching after you are done configuring and testing your connection to Google Cloud. For more information about token caching, see [Enable token caching](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#token_caching).  
**Token Refresh Seconds** | Specify the amount of time, in seconds, before an access token expires and must be refreshed. The default value is `3500`.  
**Authorization Parameter 1** | Specify the name of the client key that you've created for Secret Manager access. For example, `CLIENT_KEY_SM`.  
**Authorization Parameter 2** | Specify the name of the secret, which has the API key stored. For example, `TEST_SECRET`.  
  5. Save the new entry.




### Create new RFC destinations

For the APIs that you plan to consume using the ABAP SDK for Google Cloud, create new RFC destinations.

For information about creating RFC destinations, see [RFC destinations](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#create_rfc_destinations).

If RFC destinations are not created and configured, the ABAP SDK for Google Cloud functions using the default API endpoints maintained in individual API client stubs.

### Configure service mapping

Configure the service mapping table for the APIs that you plan to consume using the ABAP SDK for Google Cloud.

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Service Mapping**.

  3. Click **New Entries**.

  4. Specify RFC destinations for the APIs that you plan to use, for example, `addressvalidation v1`. If you're going to consume other APIs, then specify RFC destinations for those APIs.

Name | Service Name | RFC Destination  
---|---|---  
**Google Cloud Key Name** | `addressvalidation:v1` | `ZGOOG_ADDRVALDN_V1`  
  5. Save the new entry.




### Validate API key retrieval from Secret Manager

To validate API key retrieval from Secret Manager, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`. 

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Utilities > Validate API key retrieval (Using Secret Manager)**.
  3. Specify the client key name.
  4. Click **Execute** to check if the API key is retrieved successfully from Secret Manager.



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
