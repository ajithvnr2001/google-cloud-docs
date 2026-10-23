---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif/
title: Authenticate with access tokens through Workload Identity Federation \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:12.500423+00:00
---

# Authenticate with access tokens through Workload Identity Federation  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authenticate with access tokens through Workload Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication-wif)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif)



This document describes how to authenticate to Google Cloud by using tokens through Workload Identity Federation. With [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), you can grant on-premises or multicloud SAP workloads access to Google Cloud resources without using a service account key.

Workload Identity Federation follows the [OAuth 2.0 token exchange](https://tools.ietf.org/html/rfc8693) specification. You provide a credential from your IdP to the [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest), which verifies the identity on the credential, and then returns a [federated access token](https://docs.cloud.google.com/docs/authentication/token-types#fed-access-tokens) in exchange. You can use this federated access token directly with [supported services](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services) or use it to impersonate a service account and [obtain a short-lived access token](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#sa-credentials-oauth). The short-lived access token lets you call any Google Cloud APIs that the service account has access to.

You can use Workload Identity Federation with [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) or external identity provider (IdPs).

For information about other supported authentication methods, see [Authentication overview for the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

## Workload Identity Federation with VM metadata

If your SAP system is hosted on Google Cloud but managed by SAP, then you can use Workload Identity Federation to securely access resources in other Google Cloud projects from your SAP system. Workload Identity Federation lets your SAP system authenticate to other Google Cloud projects by using the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview). This eliminates the need to manage service account keys, enhancing security and simplifying authentication.

The high-level configuration steps are as follows:

  1. In Google Cloud, configure Workload Identity Federation.
  2. In Google Cloud, create a service account.
  3. In Google Cloud, grant the service account access to the Workload Identity Federation pool.
  4. In ABAP SDK for Google Cloud, configure client key.



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

  4. Under **Add a provider to pool** , add the metadata server as a provider:

     1. In the **Select a provider** field, select **OpenID Connect (OIDC)**.
     2. Enter the following provider details:

        * **Provider name** : enter a name for the provider.
        * **Issuer(URL)** : enter the metadata server token URL, `https://accounts.google.com`.
        * **Audience** : select **Allowed audience** and enter the Google Cloud project number of the Google Cloud project that you need to access. For information about how to get the project number, see Gather details of Google metadata server instance.
  5. Click **Continue**.

  6. Under **Configure provider attributes** , do the following:

     * In the **Google 1** field, make sure the value is `google.subject`.
     * In the **OIDC 1** field, enter `assertion.email`.
  7. Click **Save**.

  8. Make a note of the following:

     * Pool ID
     * Provider ID

You need these IDs when configuring the client key.




#### Gather details of Google metadata server instance

To get the Google metadata server instance details that you need to configure the Workload Identity Federation, perform the following steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`. 

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Utilities > Get specific metadata values for Google Metadata Server Instance**.
  3. Select the options as appropriate: 
     * **Numeric Project ID**
     * **Default Service Account Email**
  4. Click **Execute** to view the details.
  5. Make a note of the details. You need them when configuring Workload Identity Federation in the Google Cloud console.



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

### Grant the service account access to the Workload Identity Federation pool

To impersonate service accounts from federated workloads, grant the [Workload Identity User (`roles/iam.workloadIdentityUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityUser) on the service account. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** Although granting IAM roles directly to a federated principal (`principal://`) is the recommended best practice for [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/best-practices-for-using-workload-identity-federation), ABAP SDK for Google Cloud requires IAM service account impersonation because the SDK client key configuration requires an IAM service account email address and exchanges federated tokens using the IAM Service Account Credentials API.

To grant the service account access to the Workload Identity Federation pool, perform the following:

  1. In the Google Cloud console, go to the **Workload Identity Pools** page.

[Go to Workload Identity Pools](https://console.cloud.google.com/iam-admin/workload-identity-pools)

  2. Select the workload identity pool that you created in the configure Workload Identity Federation section.

  3. To grant access to the workload identity pool, click add_box **Grant access**.

  4. In the **Service account** list, select the service account that has access to Google Cloud APIs. If you use multiple service accounts, then add them all here.

  5. In the **Attribute name** field, select **Subject**.

  6. In the **Attribute value** field, enter the service account email address retrieved from the metadata server, in double quotes. For example, `"svc-acct-compute@example-project-123456.iam.gserviceaccount.com"`.

For information about how to retrieve the service account email address from the metadata server, see Gather details of Google metadata server instance.

  7. In the **Configure your application** dialog that appears, click **Dismiss**.




### Configure client key

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`. 

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.
  3. Click **New Entries**.
  4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration.  
**Google Cloud Service Account Name** | Specify the name of the service account, in email address format, that was created to access Google Cloud APIs in the step Create a service account. For example: `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.   
**Google Cloud Scope** | Specify the API access scope, `https://www.googleapis.com/auth/cloud-platform`.  
**Google Cloud Project Identifier** | Specify the ID of the Google Cloud project where you created the workload identity pool.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the authentication class as appropriate: 
     * `/GOOG/CL_AUTH_WIF_META_ACCESS`: Generates Google-signed OAuth tokens.
     * `/GOOG/CL_AUTH_WIF_META_IDTOKEN`: Generates Google-signed ID tokens.  
**Token Caching** | The flag that determines whether or not the access tokens retrieved from Google Cloud are cached. We recommend that you enable token caching after you are done configuring and testing your connection to Google Cloud.  
**Token Refresh Seconds** | Leave this field blank.  
**Authorization Parameter 1** | Specify the workload identity pool ID.  
**Authorization Parameter 2** | Specify the workload identity provider ID.  
  5. Save the entry.




## Workload Identity Federation with external IdPs

You can use Workload Identity Federation with external IdPs such as Amazon Web Services (AWS) or with any identity provider (IdP) that supports OpenID Connect (OIDC), such as Microsoft Azure or SAML 2.0.

For authentication using tokens through Workload Identity Federation, the high-level configuration steps are as follows:

  1. Prepare your external IdP.
  2. In Google Cloud, configure Workload Identity Federation.
  3. In Google Cloud, create a service account.
  4. In Google Cloud, allow the external workload to impersonate the service account.
  5. In ABAP SDK for Google Cloud, implement ABAP code to retrieve security tokens from your IdP.
  6. In ABAP SDK for Google Cloud, configure client key.



Not all Google Cloud products support Workload Identity Federation. Before setting up authentication using Workload Identity Federation, review the list of supported products and limitations. For more information, see [Workforce identity federation: supported products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

### Prepare your external IdP

You need to prepare your IdP so that your SAP workload can obtain credentials that can be exchanged for a Google OAuth 2.0 security token.

To prepare your external IdP, perform the steps depending on your IdP:

  * If you're using AWS or Azure as your IdP, then follow the instructions to [prepare your external IdP](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#prepare).
  * If you're using other IdPs, then follow the instructions to [prepare your external IdP](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#prepare).



### Configure Workload Identity Federation

In Google Cloud, configure workload identity pool and providers.

You configure an identity pool, which is an entity that lets you manage external identities. You also configure a workload identity pool provider, which is an entity that describes a relationship between Google Cloud and your IdP.

To configure Workload Identity Federation, perform the steps depending on your external IdP:

  * If you're using AWS or Azure as your IdP, then follow the instructions to [create the workload identity pool and provider](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#create_the_workload_identity_pool_and_provider).
  * If you're using other IdPs, then follow the instructions to [create the workload identity pool and provider](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#create_the_workload_identity_pool_and_provider).



Make a note of the following:

  * **Project number** : the project number of the Google Cloud project where you created the workload identity pool.
  * **Pool ID** : a unique ID that identifies the workload identity pool.
  * **Provider ID** : an ID that identifies the workload identity pool provider.



You need them for the ABAP SDK client key configuration.

### Create a service account

In Google Cloud console, create a dedicated IAM service account to access Google Cloud APIs. This service account must be a principal in the Google Cloud project that contains the Google Cloud APIs that you plan to consume using the SDK.

  1. In the Google Cloud console, enable the [IAM Service Account Credentials API](https://console.cloud.google.com/project/_/apis/library/iamcredentials.googleapis.com), [Security Token Service API](https://console.cloud.google.com/project/_/apis/library/sts.googleapis.com), and any other [supported APIs](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#sdk_overview) that you plan to access using the SDK.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/iamcredentials.googleapis.com)

For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/docs/getting-started#enabling_apis).

  2. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) that represents the workload.

  3. [Grant the service account the required IAM roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to access the API functionality. To understand the role requirement for Google Cloud APIs, see the individual API documentation and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege). For more information about API specific predefined roles, see [Find IAM roles for Google Cloud APIs](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#iam-role-finder).




### Allow the external workload to impersonate the service account

To allow the external workload to impersonate the service account, perform the steps depending on your external IdP:

  * If you're using AWS or Azure as your IdP, then follow the instructions to [allow the external workload to impersonate the service account](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#allow_the_external_workload_to_impersonate_the_service_account).
  * If you're using other IdPs, then follow the instructions to [allow the external workload to impersonate the service account](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#impersonation).



### Implement ABAP code to retrieve security tokens from your IdP

ABAP SDK for Google Cloud provides an abstract class `/GOOG/CL_AUTH_WIF_BASE`, which has the logic to retrieve OAuth 2.0 security tokens from the Security Token Service and OAuth 2.0 access tokens from the IAM Service Account Credentials API. As a developer, you need to create a child class in your namespace that inherits from the abstract class `/GOOG/CL_AUTH_WIF_BASE`.

To invoke Cloud Run functions from the ABAP SDK for Google Cloud by using Workload Identity Federation, the SDK provides another abstract class `/GOOG/CL_AUTH_WIF_ID_TOKEN`. If you set up authentication by using Workload Identity Federation, then you need to create one more child class in your namespace that inherits from the abstract class `/GOOG/CL_AUTH_WIF_ID_TOKEN`. You specify this child class in the **Authorization Class** field while [configuring client key to invoke Cloud Run functions](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-cloud-functions#configure-client-key-cf-invoke-off-gc).

Make sure to implement the method `GET_EXT_IDP_TOKEN` in the child class and write the logic to get the security token from your IdP. Populate the following fields:

  * `CV_TOKEN`: the token retrieved from your IdP in the `string` format.
  * `CV_TOKEN_TYPE`: the type of the security token retrieved from your IdP. The supported token types are: 
    * `urn:ietf:params:oauth:token-type:jwt`
    * `urn:ietf:params:oauth:token-type:id_token`
    * `urn:ietf:params:aws:token-type:aws4_request`
    * `urn:ietf:params:oauth:token-type:access_token`
    * `urn:ietf:params:oauth:token-type:saml2`



The values populated in `CV_TOKEN` and `CV_TOKEN_TYPE` are then used by methods of the abstract class `/GOOG/CL_AUTH_WIF_BASE` to exchange and retrieve the final OAuth 2.0 token, which is used in the API calls.

The following example shows the sample implementations of method `GET_EXT_IDP_TOKEN` for other Cloud providers such as AWS and Azure.

###  AWS 
    
    
    class ZCL_AUTH_WIF_AWS definition
      public
      inheriting from /GOOG/CL_AUTH_WIF_BASE
      final
      create public .
    
    public section.
    
      types:
        BEGIN OF t_header_field,
          key type string,
          value TYPE string,
        END OF t_header_field .
      types:
        tt_header_field type STANDARD TABLE OF t_header_field WITH DEFAULT KEY .
      types:
        BEGIN OF t_token_request,
         url type string,
         method type string,
         headers type tt_header_field,
       END OF t_token_request ,
    
       BEGIN OF t_aws_creds_fetch,
          access_key_id TYPE string,
          secret_access_key TYPE string,
       END OF t_aws_creds_fetch.
    protected section.
    
      methods GET_EXT_IDP_TOKEN
        redefinition .
    private section.
    
      class-methods FETCH_DYNAMIC_AWS_CREDS
        changing
          !PC_AWS_CREDS type T_AWS_CREDS_FETCH
        returning
          value(RV_SUCCESS) type FLAG .
    ENDCLASS.
    
    
    
    CLASS ZCL_AUTH_WIF_AWS IMPLEMENTATION.
    
    
    * <SIGNATURE>---------------------------------------------------------------------------------------+
    * | Instance Protected Method ZCL_AUTH_WIF_AWS->GET_EXT_IDP_TOKEN
    * +-------------------------------------------------------------------------------------------------+
    * | [--->] IV_SERVICE_ACCOUNT             TYPE        /GOOG/SERVICE_ACCOUNT_NAME
    * | [--->] IV_KEYNAME                     TYPE        /GOOG/KEYNAME
    * | [--->] IT_QUERY_PARAMS                TYPE        /GOOG/T_HTTP_KEYS
    * | [<---] EV_RET_CODE                    TYPE        /GOOG/RETCO
    * | [<---] EV_ERR_TEXT                    TYPE        STRING
    * | [<---] EV_ERR_RESP                    TYPE        /GOOG/ERR_RESP
    * | [<---] EV_LOGTIME                     TYPE        TIMESTAMP
    * | [<-->] CV_TOKEN                       TYPE        /GOOG/REFRESH_TOKEN
    * | [<-->] CV_TOKEN_TYPE                  TYPE        STRING
    * +--------------------------------------------------------------------------------------</SIGNATURE>
    METHOD get_ext_idp_token.
    **********************************************************************
    *  Copyright 2024 Google LLC                                         *
    *                                                                    *
    *  Licensed under the Apache License, Version 2.0 (the "License");   *
    *  you may not use this file except in compliance with the License.  *
    *  You may obtain a copy of the License at                           *
    *      https://www.apache.org/licenses/LICENSE-2.0                   *
    *  Unless required by applicable law or agreed to in writing,        *
    *  software distributed under the License is distributed on an       *
    *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,      *
    *  either express or implied.                                        *
    *  See the License for the specific language governing permissions   *
    *  and limitations under the License.                                *
    **********************************************************************
    
      DATA: ls_key       TYPE /goog/client_key.
    
      /goog/cl_utility=>get_client_key( EXPORTING iv_keyname    = iv_keyname
                                            IMPORTING es_client_key = ls_key ).
    
    
      DATA: lv_awsdate TYPE string.
    
      DATA: lv_date         TYPE dats,
            lv_time         TYPE tims,
            lv_timestamp    TYPE timestampl,
            lv_tz_utc       TYPE timezone VALUE 'UTC',
            lv_awsts        TYPE string,
            lv_timechar(32) TYPE c.
    
      GET TIME STAMP FIELD lv_timestamp.
    
      CONVERT TIME STAMP lv_timestamp TIME ZONE lv_tz_utc INTO DATE lv_date TIME lv_time.
      MOVE lv_timestamp TO lv_timechar.
      CONDENSE lv_timechar.
    
      lv_awsdate = lv_date(4) &&
                   lv_date+4(2) &&
                   lv_date+6(2) &&
                   'T' &&
                   lv_time(2) &&
                   lv_time+2(2) &&
                   lv_time+4(2) &&
                   'Z'.
    
      TRANSLATE lv_awsdate TO UPPER CASE.
    
      DATA: lv_lf TYPE string.
      DATA: lv_secret_key TYPE string.
      DATA: lv_accesskey TYPE string.
      DATA: lv_datepart TYPE string.
      DATA: lv_service TYPE string.
      DATA: lv_method TYPE string.
    
      lv_lf = cl_abap_char_utilities=>newline.
    
      DATA: ls_aws_creds TYPE t_aws_creds_fetch.
    
      fetch_dynamic_aws_creds(
        CHANGING
          pc_aws_creds = ls_aws_creds ).
    
      lv_accesskey =  ls_aws_creds-access_key_id.
      lv_secret_key = ls_aws_creds-secret_access_key.
      lv_datepart = lv_awsdate(8).
      lv_service = 'sts'.
      lv_method = 'GET'.
    
    
      DATA: lv_canonical_query_params TYPE string.
      DATA: lv_host TYPE string.
      DATA: lv_region TYPE string.
      DATA: lv_canonical_resource_path TYPE string.
    
      lv_canonical_query_params = 'Action=GetCallerIdentity&Version=2011-06-15'.
      lv_host = 'sts.amazonaws.com'.
      lv_region = '<Populate your AWS Region>'.   "Example: 'us-east-1'
      lv_canonical_resource_path = '/'.
    
      DATA: lv_canonical_header_names TYPE string.
      DATA: lv_canonical_headers TYPE string.
    
      lv_canonical_header_names = 'host;x-amz-date'.
      lv_canonical_headers = 'host:' && lv_host && lv_lf && 'x-amz-date:' && lv_awsdate && lv_lf.
    
      DATA: lv_canonical_request TYPE string.
    
      CONCATENATE lv_method lv_lf
                  lv_canonical_resource_path lv_lf
                  lv_canonical_query_params lv_lf
                  lv_canonical_headers lv_lf
                  lv_canonical_header_names
                  INTO lv_canonical_request.
    
      DATA: lv_canonical_request_hash TYPE string.
    
      TRY.
          cl_abap_message_digest=>calculate_hash_for_char(
           EXPORTING
             if_algorithm = 'SHA-256'
             if_data = lv_canonical_request
           IMPORTING
             ef_hashstring = lv_canonical_request_hash ).
        CATCH cx_abap_message_digest.
          "Handle error
          RETURN.
      ENDTRY.
    
      TRANSLATE lv_canonical_request_hash TO LOWER CASE.
    
      DATA: lv_algorithm TYPE string.
    
      lv_algorithm = 'AWS4-HMAC-SHA256'.
    
      DATA: lv_credential_scope TYPE string.
    
      CONCATENATE lv_datepart '/' lv_region '/' lv_service '/' 'aws4_request' INTO lv_credential_scope.
    
      DATA: lv_string_to_sign TYPE string.
    
      CONCATENATE lv_algorithm lv_lf
                  lv_awsdate lv_lf
                  lv_credential_scope lv_lf
                  lv_canonical_request_hash
                  INTO lv_string_to_sign.
    
      DATA: lv_awskey TYPE string.
    
      CONCATENATE 'AWS4' lv_secret_key INTO lv_awskey.
    
      DATA: lv_ksecret TYPE xstring.
    
      TRY.
          lv_ksecret = cl_abap_hmac=>string_to_xstring( lv_awskey ).
        CATCH cx_abap_message_digest .
          "Handle error
          RETURN.
      ENDTRY.
    
      DATA: lv_kdate  TYPE xstring.
      TRY.
          cl_abap_hmac=>calculate_hmac_for_char(
            EXPORTING
               if_algorithm = 'SHA256'
               if_key = lv_ksecret
               if_data = lv_datepart
            IMPORTING
               ef_hmacxstring = lv_kdate ).
        CATCH cx_abap_message_digest. "
          "Handle error
          RETURN.
      ENDTRY.
    
      DATA: lv_kregion TYPE xstring.
      TRY.
          cl_abap_hmac=>calculate_hmac_for_char(
            EXPORTING
               if_algorithm = 'SHA256'
               if_key = lv_kdate
               if_data = lv_region
            IMPORTING
                 ef_hmacxstring = lv_kregion ).
        CATCH cx_abap_message_digest.
          "Handle error
          RETURN.
      ENDTRY.
    
      DATA: lv_kservice TYPE xstring.
      TRY.
          cl_abap_hmac=>calculate_hmac_for_char(
             EXPORTING
               if_algorithm = 'SHA256'
               if_key = lv_kregion
               if_data = lv_service
               IMPORTING
                 ef_hmacxstring = lv_kservice ).
        CATCH cx_abap_message_digest.
          "Handle error
          RETURN.
      ENDTRY.
    
      DATA: lv_ksigningkey TYPE xstring.
      TRY.
          cl_abap_hmac=>calculate_hmac_for_char(
             EXPORTING
               if_algorithm = 'SHA256'
               if_key = lv_kservice
               if_data = 'aws4_request'
             IMPORTING
                 ef_hmacxstring = lv_ksigningkey ).
        CATCH cx_abap_message_digest.
          "Handle error
          RETURN.
      ENDTRY.
    
      DATA: lv_stringtosign TYPE string.
    
      lv_stringtosign = 'AWS4-HMAC-SHA256' && lv_lf &&
                       lv_awsdate && lv_lf &&
                       lv_datepart && '/' &&
                       lv_region && '/' &&
                       lv_service && '/aws4_request' && lv_lf &&
                       lv_canonical_request_hash.
    
      DATA: lv_ssignature TYPE string.
    
      TRY.
          cl_abap_hmac=>calculate_hmac_for_char(
             EXPORTING
               if_algorithm = 'SHA256'
               if_key = lv_ksigningkey
               if_data = lv_stringtosign
             IMPORTING
               ef_hmacstring = lv_ssignature ).
        CATCH cx_abap_message_digest.
          "Handle error
          RETURN.
      ENDTRY.
    
      TRANSLATE lv_ssignature TO LOWER CASE.
    
      DATA: lv_authorization_header TYPE string.
    
      lv_authorization_header = 'AWS4-HMAC-SHA256 Credential=' &&
                                lv_accesskey && '/' &&
                                lv_credential_scope &&
                                ', SignedHeaders=' &&
                                lv_canonical_header_names &&
                                ', Signature=' &&
                                lv_ssignature.
    
      DATA: ls_token_request TYPE t_token_request.
    
      ls_token_request-url = 'https://sts.amazonaws.com?Action=GetCallerIdentity&Version=2011-06-15'.
      ls_token_request-method = 'POST'.
    
      DATA: ls_header_field TYPE t_header_field.
      ls_header_field-key = 'Authorization'.
      ls_header_field-value = lv_authorization_header.
      APPEND ls_header_field TO ls_token_request-headers.
    
      CLEAR: ls_header_field.
      ls_header_field-key = 'host'.
      ls_header_field-value = 'sts.amazonaws.com'.
      APPEND ls_header_field TO ls_token_request-headers.
    
      CLEAR: ls_header_field.
      ls_header_field-key = 'x-amz-date'.
      ls_header_field-value = lv_awsdate.
      APPEND ls_header_field TO ls_token_request-headers.
    
      CLEAR: ls_header_field.
      ls_header_field-key = 'x-goog-cloud-target-resource'.
      ls_header_field-value = '//iam.googleapis.com/projects/' &&
                                   ls_key-project_id &&
                                   '/locations/global/workloadIdentityPools/' &&
                                   ls_key-auth_param1 &&
                                   '/providers/' &&
                                   ls_key-auth_param2.
      APPEND ls_header_field TO ls_token_request-headers.
    
      cv_token = /ui2/cl_json=>serialize(  ls_token_request ).
      cv_token_type = 'urn:ietf:params:aws:token-type:aws4_request'.
    
    ENDMETHOD.
    
    
    * <SIGNATURE>---------------------------------------------------------------------------------------+
    * | Static Private Method ZCL_AUTH_WIF_AWS=>FETCH_DYNAMIC_AWS_CREDS
    * +-------------------------------------------------------------------------------------------------+
    * | [<-->] PC_AWS_CREDS                   TYPE        T_AWS_CREDS_FETCH
    * | [<-()] RV_SUCCESS                     TYPE        FLAG
    * +--------------------------------------------------------------------------------------</SIGNATURE>
      METHOD fetch_dynamic_aws_creds.
        DATA: lo_http       TYPE REF TO if_http_client,
              lv_imds_token TYPE string,
              lv_role       TYPE string.
    
        " Phase 1: Get IMDSv2 Session Token (Security Requirement)
        cl_http_client=>create_by_url( EXPORTING url = 'http://169.254.169.254/latest/api/token'
                                       IMPORTING client = lo_http ).
        lo_http->request->set_method( 'PUT' ).
        lo_http->request->set_header_field( name = 'X-aws-ec2-metadata-token-ttl-seconds' value = '21600' ).
        lo_http->send( ). lo_http->receive( ).
        lv_imds_token = lo_http->response->get_cdata( ). lo_http->close( ).
    
        " Phase 2: Get IAM Role name
        cl_http_client=>create_by_url( EXPORTING url = 'http://169.254.169.254/latest/meta-data/iam/security-credentials/'
                                       IMPORTING client = lo_http ).
        lo_http->request->set_header_field( name = 'X-aws-ec2-metadata-token' value = lv_imds_token ).
        lo_http->send( ). lo_http->receive( ).
        lv_role = lo_http->response->get_cdata( ). lo_http->close( ).
    
        " Phase 3: Retrieve actual credentials into me->gs_aws_creds
        cl_http_client=>create_by_url( EXPORTING url = |http://169.254.169.254/latest/meta-data/iam/security-credentials/{ lv_role }|
                                       IMPORTING client = lo_http ).
        lo_http->request->set_header_field( name = 'X-aws-ec2-metadata-token' value = lv_imds_token ).
        lo_http->send( ). lo_http->receive( ).
    
        /ui2/cl_json=>deserialize( EXPORTING json = lo_http->response->get_cdata( )
                                   CHANGING data = pc_aws_creds ).
        lo_http->close( ).
        rv_success = abap_true.
    
      ENDMETHOD.
    ENDCLASS.
    

###  Azure 
    
    
    class ZCL_AUTH_WIF_AZURE definition
      public
      inheriting from /GOOG/CL_AUTH_WIF_BASE
      final
      create public .
    
    public section.
    protected section.
    
      methods GET_EXT_IDP_TOKEN
        redefinition .
    private section.
    ENDCLASS.
    
    
    
    CLASS ZCL_AUTH_WIF_AZURE IMPLEMENTATION.
    
    
      METHOD GET_EXT_IDP_TOKEN.
    **********************************************************************
    *  Copyright 2024 Google LLC                                         *
    *                                                                    *
    *  Licensed under the Apache License, Version 2.0 (the "License");   *
    *  you may not use this file except in compliance with the License.  *
    *  You may obtain a copy of the License at                           *
    *      https://www.apache.org/licenses/LICENSE-2.0                   *
    *  Unless required by applicable law or agreed to in writing,        *
    *  software distributed under the License is distributed on an       *
    *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,      *
    *  either express or implied.                                        *
    *  See the License for the specific language governing permissions   *
    *  and limitations under the License.                                *
    **********************************************************************
    
        TYPES:
          BEGIN OF t_azure_resp,
            access_token TYPE string,
          END OF t_azure_resp.
    
        DATA: lo_client TYPE REF TO if_http_client.
    
        DATA: lv_url type string.
        lv_url = 'http://169.254.169.254/metadata/identity/oauth2/token?resource=<APP_ID_URI>&api-version=2018-02-01'.
        "Replace <APP_ID_URI> with the value of Application ID URI of the application that you've configured for workload identity federation.
    
        cl_http_client=>create_by_url(
           EXPORTING
             url                        = lv_url
           IMPORTING
             client                     = lo_client
           EXCEPTIONS
             argument_not_found         = 1
             plugin_not_active          = 2
             internal_error             = 3
             pse_not_found              = 4
             pse_not_distrib            = 5
             pse_errors                 = 6
             oa2c_set_token_error       = 7
             oa2c_missing_authorization = 8
             oa2c_invalid_config        = 9
             oa2c_invalid_parameters    = 10
             oa2c_invalid_scope         = 11
             oa2c_invalid_grant         = 12
             OTHERS                     = 13 ).
    
        IF sy-subrc <> 0.
          RETURN.
        ENDIF.
    
        lo_client->request->set_method( 'GET' ).
        lo_client->request->set_header_field( name = 'Metadata' value = 'true' ).
    
        lo_client->send(
          EXCEPTIONS
            http_communication_failure = 1
            http_invalid_state         = 2
            http_processing_failed     = 3
            http_invalid_timeout       = 4
            OTHERS                     = 5 ).
    
        lo_client->propertytype_logon_popup = lo_client->co_disabled.
    
        lo_client->receive(
          EXCEPTIONS
          http_communication_failure = 1
          http_invalid_state         = 2
          http_processing_failed     = 3 ).
    
        DATA: lv_json TYPE string.
    
        lv_json = lo_client->response->get_cdata( ).
    
        DATA: ls_azure_resp TYPE t_azure_resp.
    
        /goog/cl_json=>deserialize(
          EXPORTING
            json             = lv_json
          CHANGING
            data             = ls_azure_resp ).
        cv_token = ls_azure_resp-access_token.
        cv_token_type = 'urn:ietf:params:oauth:token-type:jwt'.
    
      ENDMETHOD.
    ENDCLASS.
    

### Configure client key

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`. 

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.
  3. Click **New Entries**.
  4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration.  
**Google Cloud Service Account Name** | Specify the name of the service account, in email address format, that was created to access Google Cloud APIs in the step Create a service account. For example: `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.   
**Google Cloud Scope** | Specify the API access scope, `https://www.googleapis.com/auth/cloud-platform`.  
**Google Cloud Project Identifier** | Specify the ID of the Google Cloud project where you created the workload identity pool.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the child class, which contains the implementation of class `/GOOG/CL_AUTH_WIF_BASE`. For more information, see [Implement ABAP code to retrieve security tokens from your IdP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif#implement_abap_code_to_retrieve_token).  
**Token Caching** | The flag that determines whether or not the access tokens retrieved from Google Cloud are cached. We recommend that you enable token caching after you are done configuring and testing your connection to Google Cloud.  
**Token Refresh Seconds** | Leave this field blank.  
**Authorization Parameter 1** | Specify the workload identity pool ID.  
**Authorization Parameter 2** | Specify the workload identity provider ID.  
  5. Save the entry.




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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
