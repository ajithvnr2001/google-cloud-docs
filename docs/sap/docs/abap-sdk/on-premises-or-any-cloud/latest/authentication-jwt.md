---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt/
title: Authenticate with JSON Web Tokens \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:34.308295+00:00
---

# Authenticate with JSON Web Tokens  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authenticate with JSON Web Tokens Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication-jwt)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt)



This document shows how to set up authentication to access Google Cloud APIs when your SAP system is running on a host that is on premises, on another cloud provider, in another environment outside of Google Cloud, or managed by SAP through the [SAP RISE](https://www.sap.com/hk/products/erp/rise.html) program. For authentication to Google Cloud, you use Google Cloud signed JSON Web Tokens (JWT) to obtain access tokens from Google Cloud.

For information about other supported authentication methods, see [Authentication overview for the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

The high-level configuration steps are as follows:

  * Create a service account for JWT based token retrieval. 
    * Create a service account.
    * Create a service account key (P12).
    * Specify the service account for JWT signing.
  * Configure security settings for Google Cloud on the SAP host. 
    * Create a new SSF application and enable `STRUST` node for the SSF application.
    * Import the service account key into `STRUST`.
  * Enable the Google Cloud APIs.
  * Create another service account for authorization to access Google Cloud APIs. 
    * Grant the service account the IAM roles that are required to access particular APIs.
    * Add the service account created to access APIs as a principal to the Google Cloud project.
  * Create SAP configurations. 
    * Specify access settings in the client key table.
    * Create new RFC destinations.
    * Specify RFC destinations in the service map table.
  * Validate authentication configuration.



## Prerequisites

For your SAP application server to connect to Google Cloud APIs through HTTPS, ensure the following:

  * Confirm that the HTTPS port is active in the transaction `SMICM`.

  * On the SAP host, configure firewall rules or proxies to allow egress traffic from the HTTPS port to the required Google Cloud APIs. Specifically, your SAP system must be able to access the following API endpoints:

    * `https://iamcredentials.googleapis.com`
    * API endpoints for the APIs that you want to consume using the SDK.



## Create a service account for JWT based token retrieval

For JWT based authentication to Google Cloud, ABAP SDK for Google Cloud needs an IAM service account.

### Create a service account

Create a service account and grant the `Service Account Token Creator` IAM role to the service account.

To create a service account, perform the following steps:

  1. In the Google Cloud console, create an IAM service account for JWT based token retrieval.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

For information about how to create a service account, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

  2. Grant the [`Service Account Token Creator`](https://docs.cloud.google.com/compute/docs/access/iam#iam.serviceAccountTokenCreator) role to the service account. For instructions, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).




### Create a service account key

You need to create a P12 service account key for the service account used for JWT based token retrieval.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

To create a service account key, perform the following steps:

  1. In the Google Cloud console, go to the IAM & Admin **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select your Google Cloud project.

  3. Click the email address of the service account that you created for JWT based token retrieval in the previous section, Create a service account.

  4. Under the service account name, click the **Keys** tab.

  5. Click the **Add Key** drop-down menu, and then select **Create new key** to create [a service account key](https://docs.cloud.google.com/iam/docs/service-account-creds#key-types).

  6. Accept **P12** as the key type and click **Create**.

A private key is downloaded to your computer.

  7. Make a note of the password for the private key file, `notasecret`.

Provide the private key and password to your SAP administrator to import the private key into `STRUST`, as described in Import the service account key into STRUST.




### Specify the service account for JWT signing

To specify the service account for JWT signing, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Parameters**.

  3. Click **New Entries**.

  4. In the **Parameter Name** field, enter `JWT_SERVC_ACCT`. The parameter description is automatically populated.

  5. In the **Parameter Value** field, enter the name of the service account.

  6. Save the new entry.




## Configure security settings for Google Cloud on the SAP host system

To enable JWT signing for the service account that you created for JWT based token retrieval, you need to configure security settings for Google Cloud on the SAP host system.

### Create a new Secure Store and Forward (SSF) Application

Each `SSFAPPLIC` entry lets you save a single service account key. To save service account keys for multiple projects, you need to create multiple `SSFAPPLIC` entries by following the same steps.

To create a new entry in the table `SSFAPPLIC`, perform the following steps:

  1. In the SAP GUI, enter transaction code `SE16`.
  2. In the **Table Name** field, enter `SSFAPPLIC`, and create a new entry.
  3. In the **APPLIC** field, enter a name for your SSF application, such as `ZG_JWT`.
  4. Except the **B_INCCERTS** , **B_DETACHED** , **B_ASKPWD** , and **B_DISTRIB** fields, select all other fields.
  5. In the **DESCRIPT** field, enter `JWT Signature for GCP`.
  6. Save the new entry.

This entry becomes a new node in transaction `STRUST`, where you import the service account key.




### Enable the `STRUST` node

Use transaction `SSFA` to enable the `STRUST` node for `JWT Signature for GCP`.

To enable the `STRUST` node, perform the following steps:

  1. In the SAP GUI, enter transaction code `SSFA`.
  2. Click **New Entries**.
  3. In the **SSF Application** drop-down list, select `JWT Signature for GCP`. This is the new entry that you created in the table `SSFAPPLIC`.

The application specific SSF parameters are automatically populated.

  4. Save the new entry.

A new node `SSF JWT Signature for GCP` is enabled in transaction `STRUST`.




### Import the service account key into `STRUST`

To import the service account key into `STRUST`, perform the following steps:

  1. In the SAP GUI, enter transaction code `STRUST`.

Verify the new node in transaction `STRUST` is `SSF JWT Signature for GCP`.

  2. Import the private key file:

     1. Select **PSE > Import** from the menu bar.
     2. Depending on your SAP system, select the appropriate private key: 
        * SAP S/4HANA 
          1. Select the P12 private key.
          2. Enter the file password `notasecret`, and then click **OK**.
        * SAP ECC 
          1. Select the PSE private key. You need to convert the P12 private key that you downloaded earlier into a PSE private key. For more information about converting a P12 key into a PSE key, see Convert P12 key into PSE key.
          2. Enter the file PIN that you created during the private key conversion from P12 key to PSE key, and then click **OK**.
  3. Select **PSE > Save as**.

  4. Select **SSF Application** , and in the corresponding input field, select the new SSF Application node that you created in Create a new Secure Store and Forward (SSF) Application.

  5. Save the new entry.

The service key is attached to the SSF application node `SSF JWT Signature for GCP`.




### Convert the P12 private key into PSE key

If your SAP system is SAP NetWeaver 7.0x (SAP ECC), then you need to convert the P12 key into a PSE key.

To convert the P12 key into a PSE key, perform the following steps:

  1. Go to the path: 
         
         /usr/sap/SID/SYS/exe/run/

Replace SID with the SAP system ID.

  2. Run the following command after replacing the placeholders: 
         
         sapgenpse import_p12 -p PSE_PATH_AND_FILE_NAME P12_PATH_AND_FILE_NAME.p12

Replace the following:

     * `PSE_PATH_AND_FILE_NAME`: specify the path and filename for the PSE file
     * `P12_PATH_AND_FILE_NAME`: specify the path and filename for the P12 key file
  3. Enter the password of P12 private key file, `notasecret`.

  4. Create a new PIN for the PSE private key and re-enter your PIN.

  5. Make a note of the PIN, you need to provide this PIN when importing the PSE private key file into `STRUST`.




For information from SAP about about how to convert a P12 key into a PSE key, see:

  * [SAP Note 2148457 - How to convert the keypair of a PKCS#12 / PFX container into a PSE file](https://launchpad.support.sap.com/#/notes/2148457)

  * [SAP Note 2976401 - "import_p12: Error creating PSE" error during converting keypair of PKCS#12 / PFX container into PSE file](https://launchpad.support.sap.com/#/notes/2976401)




## Enable the Google Cloud APIs

In the Google Cloud console, enable the [IAM Service Account Credentials API](https://console.cloud.google.com/project/_/apis/library/iamcredentials.googleapis.com) for your Google Cloud project that requires authentication. Along with the IAM Service Account Credentials API, you need to enable any other [supported APIs](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#sdk_overview) that you plan to access using the SDK.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/iamcredentials.googleapis.com)

For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/docs/getting-started#enabling_apis).

## Create a service account for authorization to access Google Cloud APIs

For authentication and authorization to access Google Cloud APIs, the ABAP SDK for Google Cloud needs an IAM service account.

### Create a service account

In the Google Cloud console, create an IAM service account. This service account must be a principal in the Google Cloud project that contains the Google Cloud APIs that you plan to consume using the SDK. If you create the service account in the same project that contains the Google Cloud APIs, then the service account is added as a principal to the project automatically.

If you create the service account in a project other than the project where the Google Cloud APIs are enabled, then you need to add the service account to that project in an additional step.

  1. In the Google Cloud console, create an IAM service account for authentication and authorization to access Google Cloud APIs.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

For information about how to create a service account, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

  2. In the Google Cloud console, grant the service account the required IAM roles to access the API functionality. To understand the role requirement for Google Cloud APIs, see the individual API documentation and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege). For more information about API specific predefined roles, see [Find IAM roles for Google Cloud APIs](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#iam-role-finder).

  3. If you created the service account in a different project than the project that contains the Google Cloud APIs that you plan to consume using the SDK, then note the name of the service account. You specify the name when you add the service account to that project. For more information, see Add the service account to the Google Cloud project.




### Add the service account to the Google Cloud project

If you created the service account for ABAP SDK for Google Cloud in a project other than the project that contains the Google Cloud APIs that you plan to consume using the SDK, then you need to add the service account to the Google Cloud project that contains the Google Cloud APIs.

If you created the service account in the same project that contains the Google Cloud APIs, then you can skip this step.

To add an existing service account to the Google Cloud project that contains the Google Cloud APIs, perform the following steps:

  1. In the Google Cloud console, go to the IAM Permissions page:

[Go to IAM permissions](https://console.cloud.google.com/iam-admin/iam)

  2. Confirm that the name of the project that contains the target Google Cloud APIs is displayed near the top of the page. For example:

**Permissions for project "` PROJECT_NAME`"**

If it is not, then switch projects.

  3. On the IAM page, click person_add**Grant access**. The **Grant access to "` PROJECT_NAME`"** dialog opens.

  4. In the **Grant access to "` PROJECT_NAME`"** dialog, perform the following steps:

     1. In the **New principals** field, specify the name of the service account.
     2. In the **Select a role** field, specify a relevant role. For example, for Pub/Sub, to modify topics and subscriptions, and access to publish and consume messages, you can specify the role Pub/Sub Editor (`roles/pubsub.editor`).

For more details about API specific predefined roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

     3. Add additional roles as required for your API usage. Implement Google recommended best practices by applying the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

     4. Click **Save**. The service account appears in the list of project principals on the **IAM** page.




The service account can now be used to access Google Cloud APIs in this project.

## Create SAP configurations

For JWT based authentication, create the required SAP configurations.

### Specify access settings in the client key table

To specify the access settings, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration.  
**Google Cloud Service Account Name** |  Specify the name of the service account, in email address format, that was created for ABAP SDK for Google Cloud in the step Create a service account. For example: `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.   
**Google Cloud Scope** | The default and mandatory scope is `https://www.googleapis.com/auth/cloud-platform`. If you need to specify additional scopes, then provide them as a comma-separated list.   
**Project ID** | Specify the ID of the Google Cloud project that contains your target APIs.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the authorization class, `/GOOG/CL_AUTH_JWT`.   
**Authorization Field** | Leave this field blank.  
**Token Refresh Seconds** | Leave this field blank.  
**Authorization Parameter 1** | Specify the name of the SSF application that you created in the section Create a new Secure Store and Forward (SSF) Application.  
  5. Save the new entry.




### Create new RFC destinations

Create RFC destinations for IAM API and other APIs that you plan to consume using the ABAP SDK for Google Cloud, for example, Pub/Sub API v1.

RFC destination name | Notes  
---|---  
`ZGOOG_IAMCREDENTIALS` | This RFC destination targets the IAM API .  
`ZGOOG_OAUTH2_TOKEN` | This RFC destination targets Google Cloud endpoint for token based authentication.  
`ZGOOG_PUBSUB_V1` | This RFC destination targets the Pub/Sub API.  
`ZGOOG_BIGQUERY_V2` | This RFC destination targets the BigQuery API v2.  
  
For information about creating RFC destinations, see [RFC destinations](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#create_rfc_destinations).

### Specify RFC destinations in the service mapping table

In the service mapping table, specify the RFC destinations for IAM API and other APIs that you plan to consume using the ABAP SDK for Google Cloud.

To specify the RFC destinations, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Service Mapping**.

  3. Click **New Entries**.

  4. Specify RFC destinations for IAM API and other APIs. For example:

Name | Service Name | RFC Destination  
---|---|---  
**Google Cloud Key Name** | `iamcredentials:v1` | `ZGOOG_IAMCREDENTIALS`  
**Google Cloud Key Name** | `googleapis.com/oauth2` | `ZGOOG_OAUTH2_TOKEN`  
**Google Cloud Key Name** | `pubsub.googleapis.com` | `ZGOOG_PUBSUB_V1`  
**Google Cloud Key Name** | `bigquery:v2` | `ZGOOG_BIGQUERY_V2`  
**Note:** You must create your own RFC destinations using the sample RFC destinations as templates.
  5. Save the new entry.




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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
