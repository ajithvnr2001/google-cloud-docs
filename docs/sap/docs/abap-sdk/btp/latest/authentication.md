---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication/
title: Set up authentication for the SAP BTP edition of ABAP SDK for Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:18.115070+00:00
---

# Set up authentication for the SAP BTP edition of ABAP SDK for Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Set up authentication for the SAP BTP edition of ABAP SDK for Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication)



This document describes how to authenticate to Google Cloud from the SAP BTP edition of ABAP SDK for Google Cloud.

Applications developed using the SAP BTP edition of ABAP SDK for Google Cloud require authentication to connect to Google Cloud APIs.

For authentication and authorization to access Google Cloud APIs, the SDK mainly uses [tokens](https://docs.cloud.google.com/docs/authentication/tokens). In addition, the SDK also supports [API keys](https://docs.cloud.google.com/docs/authentication/api-keys) to authenticate to Google Cloud APIs that use API keys. Only a few Google Cloud APIs use API keys for authentication. For example, Google Maps Platform. Review the authentication documentation for the service or API that you want to use to determine whether it supports API keys.

Depending on the Google Cloud APIs that you need to access, you can choose an appropriate method of authentication. The following list summarizes different methods of authentication supported by the SDK:

  * Authentication using tokens through Workload Identity Federation
  * Authentication using API key stored in Secret Manager



## Authentication using tokens through Workload Identity Federation

[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) follows the [OAuth 2.0 token exchange](https://tools.ietf.org/html/rfc8693) specification. You provide a credential from your identity provider (IdP) to the [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest), which verifies the identity on the credential, and then returns a [federated access token](https://docs.cloud.google.com/docs/authentication/token-types#fed-access-tokens) in exchange. You can use this federated access token directly with [supported services](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services) or use it to impersonate a service account and [obtain a short-lived access token](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#sa-credentials-oauth). The short-lived access token lets you call any Google Cloud APIs that the service account has access to.

For authentication using tokens through Workload Identity Federation, enable the following Google Cloud APIs:

  * [IAM Service Account Credentials API](https://console.cloud.google.com/project/_/apis/library/iamcredentials.googleapis.com)
  * [Security Token Service API](https://console.cloud.google.com/project/_/apis/library/sts.googleapis.com)



For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/docs/getting-started#enabling_apis).

For authentication using tokens through Workload Identity Federation, the high-level configuration steps are as follows:

  1. In SAP BTP, create an Authorization and Trust (XSUAA) service instance.
  2. In Google Cloud, create a service account.
  3. In Google Cloud, configure Workload Identity Federation.
  4. In SAP BTP, configure ABAP SDK for Google Cloud to use Workload Identity Federation.



### Create an Authorization and Trust (XSUAA) service instance

To provide the necessary services to the back-end application, create an [Authorization and Trust (XSUAA) service instance](https://learning.sap.com/courses/exploring-sap-business-technology-platform/illustrating-sap-authorization-and-trust-management-service-xsuaa-_b9fde282-4cff-4dca-b146-7c8f8dde9955) by performing the following steps:

  1. Sign in to the SAP BTP Cockpit. For more information, see the SAP page [Access the Cockpit](https://help.sap.com/docs/btp/sap-business-technology-platform/access-cockpit).
  2. Select your subaccount.
  3. Create an XSUAA service instance:

     1. Go to **Services > Service Marketplace**.
     2. Search for and select **Authorization & Trust Management Service (XSUAA)**.
     3. Click **Create**.
     4. In the **New Instance or Subscription** dialog that appears, enter a value for the following fields:

        * **Plan** : select **Application**.
        * **Runtime environment** : select **Cloud Foundry**.
        * **Space** : select a space name.
        * **Instance name** : enter a name for the XSUAA service instance.
     5. Click **Create**.

  4. Create a service key:

     1. Go to **Instances and Subscription > Instances**.
     2. Select the XSUAA service instance that you created in the previous step, and click the **Service keys** tab.
     3. Click **Create**.
     4. Enter a service key name and click **Create**.
     5. For the newly created service key, click the **Actions** (more_horiz) menu, and select **View**.
     6. From the service key credentials, make a note of the following:

        * `url`
        * `clientid`
        * `clientsecret`

You need these service key credentials when configuring authentication to Google Cloud.




### Create a service account

In the Google Cloud console, create an IAM service account. This service account must be a principal in the Google Cloud project that contains the Google Cloud APIs that you plan to consume using the SDK.

  1. In the Google Cloud console, select the project where you want to create the service account.

     * If you create the service account in the same project that contains the Google Cloud APIs, then the service account is added as a principal to the project automatically.

     * If you create the service account in a project other than the project where the Google Cloud APIs are enabled, then you need to add the service account to that project in an additional step. For more information, see Add the service account to the Google Cloud project.

  2. Create a service account for authentication and authorization to access Google Cloud APIs.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

For information about how to create a service account, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

  3. In the Google Cloud console, grant the service account the required IAM roles to access the API functionality. To understand the role requirement for Google Cloud APIs, see the individual API documentation and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege). For more information about API specific predefined roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

  4. If you created the service account in a different project than the project that contains the Google Cloud APIs that you plan to consume using the SDK, then note the name of the service account. You specify the name when you add the service account to that project.




#### Add the service account to the Google Cloud project

If you created the service account for ABAP SDK for Google Cloud in a project other than the project that contains the Google Cloud APIs that you plan to consume using the SDK, then you need to add the service account to the Google Cloud project that contains the Google Cloud APIs.

If you created the service account in the same project that contains the Google Cloud APIs, then you can skip this step.

To add an existing service account to the Google Cloud project that contains the Google Cloud APIs, perform the following steps:

  1. In the Google Cloud console, go to the IAM **Permissions** page.

[Go to IAM permissions](https://console.cloud.google.com/iam-admin/iam)

  2. Confirm that the name of the project that contains the target Google Cloud APIs is displayed near the top of the page. For example:

**Permissions for project '` PROJECT_NAME`'**

If it is not, then switch projects.

  3. On the IAM **Permissions** page, click person_add**Grant access**.

  4. In the **Grant access to '` PROJECT_NAME`'** dialog that appears, perform the following steps:

     1. In the **New principals** field, specify the name of the service account.
     2. In the **Select a role** field, specify a relevant role. For example, for Pub/Sub, to modify topics and subscriptions, and access to publish and consume messages, you can specify the role Pub/Sub Editor (`roles/pubsub.editor`).

For more details about API specific predefined roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles).

     3. Add additional roles as required for your API usage. We recommend implementing the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

     4. Click **Save**. The service account appears in the list of project principals on the **IAM** page.




The service account can now be used to access Google Cloud APIs in this project.

### Configure Workload Identity Federation

To get the permissions that you need to configure Workload Identity Federation, ask your administrator to grant you the following IAM roles on the project:

  * [Workload Identity Pool Admin (`roles/iam.workloadIdentityPoolAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin)
  * [Service Account Admin (`roles/iam.serviceAccountAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin)



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To configure Workload Identity Federation, perform the following steps:

  1. In the Google Cloud console, go to the **New workload provider and pool** page.

[Go to New workload provider and pool](https://console.cloud.google.com/iam-admin/workload-identity-pools/create)

  2. In the **Create an identity pool** section, enter a value for the following fields:

     * **Name** : name for the pool. The name is also used as the pool ID. You can't change the pool ID later.
     * **Description** : text that describes the purpose of the pool.
  3. Click **Continue**.

  4. Under **Add a provider to pool** , add the provider settings:

     1. In the **Select a provider** field, select **OpenID Connect (OIDC)**.
     2. Enter the following provider details:

        * **Provider name** : enter a name for the provider.
        * **Issuer(URL)** : enter the URL from the service key credentials that you noted when you created the XSUAA service instance. Append `/oauth/token` to the URL.
        * **Audience** : select **Allowed audience** and enter the client ID from the service key credentials that you noted when you created the XSUAA service instance.
  5. Click **Continue**.

  6. Under **Configure provider attributes** , in the **OIDC 1** field, enter `assertion.email`.

  7. Click **Save**.

  8. Make a note of the following:

     * Pool ID
     * Provider ID

You need these IDs when configuring authentication in the SDK configuration Fiori app.




### Allow external identities to impersonate the service account

To impersonate service accounts from federated workloads, grant the [Workload Identity User (`roles/iam.workloadIdentityUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityUser) on the service account. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** Although granting IAM roles directly to a federated principal (`principal://`) is the recommended best practice for [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation), SAP BTP edition of ABAP SDK for Google Cloud requires IAM service account impersonation because the SDK client key configuration requires an IAM service account email address and exchanges federated tokens using the IAM Service Account Credentials API.

To allow external identities to impersonate a service account, perform the following:

  1. In the Google Cloud console, go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)

  2. Select the workload identity pool that you created in the configure Workload Identity Federation section.

  3. To grant access to the workload identity pool, click add_box **Grant access**.

  4. In the **Service account** list, select the service account that has access to Google Cloud APIs. If you use multiple service accounts, then add them all here.

  5. In the **Attribute name** field, select **Subject**.

  6. In the **Attribute value** field, enter the client ID from the service key credentials that you noted when you created the XSUAA service instance.

  7. Click **Save**.

  8. In the **Configure your application** dialog that appears, click **Dismiss**.




### Configure ABAP SDK for Google Cloud to use Workload Identity Federation

You create communication management artifacts using the SAP [communication management](https://help.sap.com/docs/btp/sap-business-technology-platform/com-communication-management) apps.

To create communication management artifacts for authentication using the XSUAA service and Workload Identity Federation, you use the communication scenario `/GOOG/COM_SDK_WIF` that is shipped with the ABAP SDK for Google Cloud.

Later, you use the SDK configuration Fiori app to create a communication map. In the communication map, you define a unique client key that you use in your ABAP program for authentication to Google Cloud.

  1. Access the SAP Fiori launchpad of the BTP ABAP system where the ABAP SDK for Google Cloud is installed.
  2. Go to **All spaces > Administration > Communication Management**.
  3. Create a communication system: 
     1. Open the **Communication Systems** app.
     2. Click **New**.
     3. In the **New Communication System** dialog that appears, enter a value for the following fields: 
        * **System ID** : enter a system ID.
        * **System name** : enter a system name.
     4. Click **Create**.
     5. In the **Host name** field, enter the URL without `https://` from the service key credentials that you noted when you created the XSUAA service instance.
     6. In the **Port** field, enter `443`.
     7. On the **Users for Outbound Communication** tab, click **Add**.
     8. Provide the following details: 
        * **Authentication method** : select **User Name and Password**.
        * **User name/client ID** : enter the client ID from the service key credentials that you noted when you created the XSUAA service instance.
        * **Password** : enter the client secret from the service key credentials that you noted when you created the XSUAA service instance.
     9. Click **Save**.
  4. Create a communication arrangement:

     1. Open the **Communication Arrangement** app.
     2. Click **New**.
     3. In the **New Communication Arrangement** dialog that appears, enter a value for the following fields:

        * **Scenario** : select **Authentication using Workload Identity Federation** (`/GOOG/COM_SDK_WIF`).
        * **Arrangement name** : enter a name for the communication arrangement.
     4. Click **Create**.

     5. For the communication arrangement that appears, in the **Communication System** field, select the communication system that you created in the previous step.

     6. Provide the following details from the Configure Workload Identity Federation section:

        * **Workload Identity Federation Pool ID** : enter the workload identity federation pool ID.
        * **Workload Identity Federation Provider ID** : enter the workload identity federation provider ID.
     7. Under **Outbound services** , in the **Path** field, enter `/oauth/token`.

     8. Click **Save**.

  5. Create a client key and a communication map:

     1. Go to the space that contains the Fiori apps for SDK configuration.
     2. Open the **Google SDK: Main Configuration** app.
     3. Click **Create**.
     4. In the **Create** dialog that appears, enter a client key name.
     5. Click **Continue**.
     6. Provide the following details: 
        * **Service account** : enter the service account that is granted access to Google Cloud APIs.
        * **Project ID** : enter the Google Cloud project ID. For information about project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Project number** : enter the Google Cloud project number. For information about project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Authentication type** : select **`W` (Workload Identity Federation)**.
     7. For the communication map that appears, in the **Communication arrangement** field, select the communication arrangement that you created in the previous step.
     8. Click **Create**. A dialog appears confirming that you agree to use ABAP SDK for Google Cloud under standard Google Cloud terms.
     9. To validate the authentication configuration, click **Check connection**. A green check for an entry indicates successful configuration. In case of any errors, visit the [troubleshooting](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting) page for guidance to resolve common errors.



## Authentication using API key stored in Secret Manager

When using API keys for authentication to Google Cloud, you can securely store your API keys with the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) service of Google Cloud.

For authentication using API key stored in Secret Manager, enable the following Google Cloud APIs:

  * [Secret Manager API](https://console.cloud.google.com/project/_/apis/library/secretmanager.googleapis.com)
  * [IAM Service Account Credentials API](https://console.cloud.google.com/project/_/apis/library/iamcredentials.googleapis.com)
  * [Security Token Service API](https://console.cloud.google.com/project/_/apis/library/sts.googleapis.com)



For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/docs/getting-started#enabling_apis).

To get the permissions that you need to configure Secret Manager and Workload Identity Federation, ask your administrator to grant you the following IAM roles on the project:

  * [Secret Manager Admin role (`roles/secretmanager.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin)
  * [Workload Identity Pool Admin (`roles/iam.workloadIdentityPoolAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin)
  * [Service Account Admin (`roles/iam.serviceAccountAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin)



For authentication using API key stored in Secret Manager, the high-level configuration steps are as follows:

  1. In SAP BTP, create an Authorization and Trust (XSUAA) service instance.
  2. In Google Cloud, create a service account.
  3. In Google Cloud, configure Workload Identity Federation.
  4. In Google Cloud, create an API key.
  5. In Google Cloud, create a secret and store the API key.
  6. In SAP BTP, configure ABAP SDK for Google Cloud to use API key from Secret Manager.



When you're authenticating using an API key stored in Secret Manager, you can reuse the XSUAA service instance, service account, and Workload Identity Federation pool and provider that you created for authentication using tokens.

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

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Create secret**.

  3. On the **Create secret** page, under **Name** , enter a name for the secret. A secret name can contain uppercase and lowercase letters, numerals, hyphens, and underscores. The maximum allowed length for a name is 255 characters.

  4. In the **Secret value** field, enter the API key that you created in the Create an API key section.

  5. Click **Create secret**. The contents of your secret are stored in a [secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version).

  6. Click the name of the secret that you created.

  7. On the **Versions** tab that opens, make a note of the following:

     * Secret name
     * Version

You need these secret details when configuring authentication to Google Cloud.




### Configure ABAP SDK for Google Cloud to use API key from Secret Manager

You create communication management artifacts using the SAP [communication management](https://help.sap.com/docs/btp/sap-business-technology-platform/com-communication-management) apps.

To create communication management artifacts for authentication using XSUAA service and Workload Identity Federation, you use the communication scenario `/GOOG/COM_SDK_APIKSM` that is shipped with the ABAP SDK for Google Cloud.

Later, you use the SDK configuration Fiori app to create a communication map. In the communication map, you define a unique client key that you use in your ABAP program for authentication to Google Cloud.

  1. Access the SAP Fiori launchpad of the BTP ABAP system where the ABAP SDK for Google Cloud is installed.
  2. Go to **All spaces > Administration > Communication Management**.
  3. Create a communication system: 
     1. Open the **Communication Systems** app.
     2. Click **New**.
     3. In the **New Communication System** dialog that appears, enter a value for the following fields: 
        * **System ID** : enter a system ID.
        * **System name** : enter a system name.
     4. Click **Create**.
     5. In the **Host name** field, enter the URL without `https://` from the service key credentials that you noted when you created the XSUAA service instance.
     6. In the **Port** field, enter `443`.
     7. On the **Users for Outbound Communication** tab, click **Add**.
     8. Provide the following details: 
        * **Authentication method** : select **User Name and Password**.
        * **User name/client ID** : enter the client ID from the service key credentials that you noted when you created the XSUAA service instance.
        * **Password** : enter the client secret from the service key credentials that you noted when you created the XSUAA service instance.
     9. Click **Save**.
  4. Create a communication arrangement:

     1. Open the **Communication Arrangement** app.
     2. Click **New**.
     3. In the **New Communication Arrangement** dialog that appears, enter the following details:

        * **Scenario** : select **Authentication using API Key with Secret Manager** (`/GOOG/COM_SDK_APIKSM`).
        * **Arrangement name** : enter a name for the communication arrangement.
     4. Click **Create**.

     5. For the communication arrangement that appears, in the **Communication System** field, select the communication system that you created in the previous step.

     6. Under **Additional properties** , provide a value for the following properties:

        * **Secret name** : enter the name of the secret from the Create a secret and store the API key section.
        * **Secret version** : optionally, enter the version of the secret from the Create a secret and store the API key section. If you do not provide a version, then the API key from the latest secret version is used.
        * **Workload Identity Federation Pool ID** : enter the workload identity federation pool ID from the Configure Workload Identity Federation section.
        * **Workload Identity Federation Provider ID** : enter the workload identity federation provider ID from the Configure Workload Identity Federation section.
     7. Under **Outbound services** , in the **Path** field, enter `/oauth/token`.

     8. Click **Save**.

  5. Create a client key and a communication map:

     1. Go to the space that contains the Fiori apps for SDK configuration.
     2. Open the **Google SDK: Main Configuration** app.
     3. Click **Create**.
     4. In the **Create** dialog that appears, enter a client key name.
     5. Click **Continue**.
     6. Provide the following details:

        * **Service account** : enter the service account that is granted access to Google Cloud APIs.
        * **Project ID** : enter the Google Cloud project ID. For information about project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Project number** : enter the Google Cloud project number. For information about project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
        * **Authentication type** : select **`V` (API Key using Secret Manager)**.
     7. For the communication map that appears, in the **Communication arrangement** field, select the communication arrangement that you created in the previous step.

     8. Click **Create**. A dialog appears confirming that you agree to use ABAP SDK for Google Cloud under standard Google Cloud terms.

     9. To validate the authentication configuration, click **Check connection**. A green check for an entry indicates successful configuration. In case of any errors, visit the [troubleshooting](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting) page for guidance to resolve common errors.




## Get support

If you need help resolving problems with the SAP BTP edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ SAP BTP edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
