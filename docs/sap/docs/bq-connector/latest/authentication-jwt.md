---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt/
title: Authenticate with JSON Web Tokens (JWT) \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:47.671267+00:00
---

# Authenticate with JSON Web Tokens (JWT)  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authenticate with JSON Web Tokens (JWT) Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to set up authentication to access Google Cloud when your SAP system is running on a host that is on premises, on another cloud provider, in another environment outside of Google Cloud, or managed by SAP through the [SAP RISE](https://www.sap.com/hk/products/erp/rise.html) program.

For authentication to Google Cloud, you use Google Cloud signed JSON Web Tokens (JWT) to obtain access tokens from Google Cloud.

**Note:** If you need to use a separate service account for each target project to ensure individual security and billing isolation, see [Authenticate with JWT by using project-specific service accounts to multiple projects](https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-jwt-project-specific-sa).

To set up JWT authentication, follow these steps:

  1. Enable the Google Cloud APIs.
  2. Create a service account for JWT based token retrieval. 
     1. Grant the service account the IAM role that is required to create tokens.
     2. Create a service account key (P12).
     3. Enable JWT signing for the service account on the SAP LT Replication Server host.
  3. Configure security settings for Google Cloud on the SAP LT Replication Server host. 
     1. Create a new SSF application and enable `STRUST` node for the SSF application.
     2. Import the service account key into `STRUST`.
  4. Create another service account for authorization. 
     1. Grant the service account the IAM roles that are required to access BigQuery.
     2. Add the BigQuery Connector for SAP service account to the target project.
  5. Create a BigQuery dataset.
  6. Set up TLS/SSL certificates and HTTPS.
  7. Specify access settings in `/GOOG/CLIENT_KEY`. 
     1. Configure new RFC destinations.



## Enable the Google Cloud APIs

In your Google Cloud project, enable the required Google Cloud APIs.

  * For CDC replication through Pub/Sub, enable the following APIs:

    * Pub/Sub API
    * BigQuery API
    * IAM Service Account Credentials API
  * For streaming data replication, enable the following APIs:

    * BigQuery API
    * IAM Service Account Credentials API
  * For file-based replication to Cloud Storage, enable the following APIs:

    * Cloud Storage JSON API
    * IAM Service Account Credentials API



For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

## Create a service account for JWT based token retrieval

For JWT based authentication to Google Cloud, BigQuery Connector for SAP needs an IAM service account.

### Create a service account

To create a service account for JWT based token retrieval, complete the following steps:

  1. In the Google Cloud console, go to the IAM & Admin **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. If prompted, select your Google Cloud project.

  3. Click **Create Service Account**.

  4. Specify a name for the service account and, optionally, a description.

  5. Click **Create and Continue**.

  6. In the **Grant this service account access to project** panel, select the **Service Account Token Creator** role.

  7. Click **Continue**.

  8. As appropriate, grant other users access to the service account.

  9. Click **Done**. The service account appears in the list of service accounts for the Google Cloud project.




### Create a service account key

You need to create a P12 service account key for the service account used for JWT based token retrieval.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

To create a service account key, complete the following steps:

  1. In the Google Cloud console, go to the IAM & Admin **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select your Google Cloud project.

  3. Click the email address of the service account that you created for JWT based token retrieval in the previous section, Create a service account.

  4. Under the service account name, click the **Keys** tab.

  5. Click the **Add Key** drop-down menu, and then select **Create new key** to create [a service account key](https://docs.cloud.google.com/iam/docs/service-account-creds#key-types).

  6. Accept **P12** as the key type and click **Create**.

A private key is saved to your computer.

  7. Make a note of the password for the private key file, `notasecret`.

Provide the private key and password to your SAP administrator to import the private key into `STRUST`, as described in Import the service account key into STRUST.




### Enable JWT signing for the service account on the SAP LT Replication Server host

To enable JWT signing for the service account that you created for JWT based token retrieval, you need to add the parameter `JWT_SERVC_ACCT` to the table `/GOOG/BQ_PARAM` and configure the service account.

To enable JWT signing for a service account, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. From the **Settings Table** drop-down menu in the launch screen for the `/GOOG/SLT_SETTINGS` transaction, select **Parameters**.

  3. Click the **Execute** icon. The **BigQuery Settings Maintenance - Parameters** screen displays.

  4. Click the **Insert Row** icon.

  5. In the displayed row, specify the following settings:

     1. In the **Parameter Name** field, enter `JWT_SERVC_ACCT`. The parameter description is automatically populated.
     2. In the **Parameter Value** field, enter the email address of the service account that you created for JWT based token retrieval in the previous section, Create a service account.
  6. Click **Save**.

Your settings are stored as a record in the `/GOOG/BQ_PARAM` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.




## Configure security settings for Google Cloud on the SAP LT Replication Server host

This section describes how to configure security settings for Google Cloud on the SAP LT Replication Server host, which involves creating an SSF Application entry and importing the service account key into `STRUST`.

### Create a new Secure Store and Forward (SSF) Application

Each `SSFAPPLIC` entry lets you save a single service account key. To save service account keys for multiple Google Cloud projects, you need to create multiple `SSFAPPLIC` entries by following the same steps.

To create a new entry in the table `SSFAPPLIC`, complete the following steps:

  1. In the SAP GUI, enter transaction code `SE16`.
  2. In the **Table Name** field, enter `SSFAPPLIC`, and then create a new entry.
  3. For the **APPLIC** field, enter a name for your SSF application, such as `ZG_JWT`.
  4. Except the **B_INCCERTS** , **B_DETACHED** , **B_ASKPWD** , and **B_DISTRIB** fields, select all other fields.
  5. In the **DESCRIPT** field, enter `JWT Signature for GCP`.
  6. Save the new entry.

This entry becomes a new node in transaction `STRUST`, where you import the service account key.




### Enable the `STRUST` node

Use transaction `SSFA` to enable the `STRUST` node for `JWT Signature for GCP`.

To enable the `STRUST` node, complete the following steps:

  1. In the SAP GUI, enter transaction `SSFA`.
  2. Click **New Entries**.
  3. In the **SSF Application** drop-down list, select `JWT Signature for GCP`. This is the new entry that you created in the table `SSFAPPLIC`.

The following screenshot shows the application-specific SSF parameters that are automatically populated by SAP.

![Application specific SSF parameters](https://docs.cloud.google.com/static/sap/docs/images/bqc-ssf-parameters.png)

  4. Save the new entry.

A new node `SSF JWT Signature for GCP` is enabled in transaction `STRUST`. Now you import the service account key into this node.




### Import the service account key into `STRUST`

To import the service account key into `STRUST`, complete the following steps:

  1. In the SAP GUI, enter transaction code `STRUST`.

Verify the new node in transaction `STRUST` is `SSF JWT Signature for GCP`.

  2. Import the private key file:

     1. Select **PSE > Import** from the menu bar.
     2. Depending on your source system type, select the appropriate private key: 
        * S4/HANA 
          1. Select the P12 private key.
          2. Enter the file password `notasecret`, and then click **OK**.
        * ECC 
          1. Select the PSE private key. You need to convert the P12 private key that you downloaded earlier into a PSE private key. For more information about converting a P12 key into a PSE key, see Convert P12 key into PSE key.
          2. Enter the file PIN that you created during the private key conversion from P12 key to PSE key, and then click **OK**.
  3. Select **PSE > Save as**.

  4. Select the **SSF Application** option button, and in the corresponding field, select the new SSF Application node that you created in Create a new Secure Store and Forward (SSF) Application.

  5. Save the new entry.

The service key is attached to the SSF application node `SSF JWT Signature for GCP`.




### Convert the P12 private key into PSE key

If your source system is SAP NetWeaver 7.0x (SAP ECC), then you need to convert the P12 key into a PSE key.

To convert the P12 key into a PSE key, complete the following steps:

  1. Go to the path: 
         
         /usr/sap/SID/SYS/exe/run/

Replace SID with the SAP system ID.

  2. Run the following command after replacing the placeholders: 
         
         sapgenpse import_p12 -p PSE_PATH_AND_FILE_NAME P12_PATH_AND_FILE_NAME.p12

Replace the following:

     * `PSE_PATH_AND_FILE_NAME`: Specify the path and filename for the PSE file.
     * `P12_PATH_AND_FILE_NAME`: Specify the path and filename for the P12 key file.
  3. Enter the password of P12 private key file, `notasecret`.

  4. Create a new PIN for the PSE private key and re-enter your PIN.

  5. Make a note of the PIN, you need to provide this PIN when importing the PSE private key file into `STRUST`.




For information from SAP about about how to convert a P12 key into a PSE key, see:

  * [SAP Note 2148457 - How to convert the keypair of a PKCS#12 / PFX container into a PSE file](https://launchpad.support.sap.com/#/notes/2148457)
  * [SAP Note 2976401 - "import_p12: Error creating PSE" error during converting keypair of PKCS#12 / PFX container into PSE file](https://launchpad.support.sap.com/#/notes/2976401)



## Create a service account for authorization

The section describes the process of creating a service account for authorization.

### Create a service account

BigQuery Connector for SAP needs an IAM service account for authentication and authorization to access Google Cloud resources.

This service account must be a principal in the Google Cloud project that contains your enabled Google Cloud APIs. If you create the service account in the same project as the Google Cloud APIs, the service account is added as a principal to the project automatically.

If you create the service account in a project other than the project that contains the enabled Google Cloud APIs, then you need to add the service account to the enabled Google Cloud APIs project in an additional step.

To create a service account, do the following:

  1. In the Google Cloud console, go to the IAM & Admin **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. If prompted, select your Google Cloud project.

  3. Click **Create Service Account**.

  4. Specify a name for the service account and, optionally, a description.

  5. Click **Create and Continue**.

  6. If you are creating the service account in the same project as the enabled Google Cloud APIs, in the **Grant this service account access to project** panel, select the roles as appropriate:

For CDC replication through Pub/Sub, select the following roles:

     * **Pub/Sub Editor**
     * **BigQuery Data Editor**
     * **BigQuery Job User**

In addition, make sure to grant the required IAM roles to the Pub/Sub service agent. For more information, see Assign BigQuery roles to the Pub/Sub service agent. 

For streaming data replication, select the following roles:

     * **BigQuery Data Editor**
     * **BigQuery Job User**

For file-based replication to Cloud Storage, select the following roles:

     * **Storage Object Creator**
     * **Storage Object Viewer**

If you are creating the service account in a different project than the enabled Google Cloud APIs project, don't grant any roles to the service account.

  7. Click **Continue**.

  8. As appropriate, grant other users access to the service account.

  9. Click **Done**. The service account appears in the list of service accounts for the project.

  10. If you created the service account in a different project than the project that contains the enabled Google Cloud APIs, note the name of the service account. You specify the name when you add the service account to the enabled Google Cloud APIs project. For more information, see Add the service account to the BigQuery project. 




The service account is now listed as a principal on the [IAM Permissions](https://console.cloud.google.com/iam-admin/iam) page of the Google Cloud project in which the service account was created.

### Add the service account to the target project

If you created the service account for BigQuery Connector for SAP in a project other than the project that contains the enabled Google Cloud APIs, then you need to add the service account to the enabled Google Cloud APIs project.

If you created the service account in the same project as the enabled Google Cloud APIs, then you can skip this step.

To add an existing service account to the BigQuery dataset project, complete the following steps:

  1. In the Google Cloud console, go to the IAM Permissions page:

[Go to IAM permissions](https://console.cloud.google.com/iam-admin/iam)

  2. Confirm that the name of the project that contains the enabled Google Cloud APIs is displayed near the top of the page. For example:

**Permissions for project "` PROJECT_NAME`"**

If it is not, switch projects.

  3. On the IAM page, click addperson**Add**. The **Add principals to "` PROJECT_NAME`"** dialog opens.

  4. In the **Add principals to "` PROJECT_NAME`"** dialog, complete the following steps:

     1. In the **New principals** field, specify the name of the service account.
     2. In the **Select a role** field, specify **BigQuery Data Editor**.
     3. Click **ADD ANOTHER ROLE**. The **Select a role** field displays again.
     4. In the **Select a role** field, specify **BigQuery Job User**.
     5. For CDC replication through Pub/Sub, repeat the preceding step, and specify **Pub/Sub Editor**.
     6. Click **Save**. The service account appears in the list of project principals on the **IAM** page.



## Assign BigQuery roles to the Pub/Sub service agent

If you are using CDC replication through Pub/Sub, for Pub/Sub to write messages to BigQuery by using a BigQuery subscription, and forward undeliverable messages to a [dead-letter topic](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#create-dead-letter-topic), you must assign the required IAM roles to the Pub/Sub service agent.

To grant the required IAM roles, do the following:

  1. Identify the service agent. The Pub/Sub service agent follows this pattern: `service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`, where `PROJECT_NUMBER` is your Google Cloud project number.

  2. Assign the following IAM roles to the service agent:

     * [BigQuery Data Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor)
     * [Pub/Sub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher)
     * [Pub/Sub Subscriber](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.subscriber)



For more information, see [Assign BigQuery roles to the Pub/Sub service agent](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#assign_bigquery_service_account).

## Create a BigQuery dataset

**Note:** If you're configuring file-based replication to Cloud Storage, then skip this section. You need to create a BigQuery dataset only when replicating data to BigQuery.

To create a BigQuery dataset, your user account must have the proper IAM permissions for BigQuery. For more information, see [Required permissions](https://docs.cloud.google.com/bigquery/docs/datasets#required_permissions).

  1. In the Google Cloud console, go to the BigQuery page:

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Next to your project ID, click the **View actions** icon, more_vert, and then click **Create dataset**.

![Diagram is described in the preceding text](https://docs.cloud.google.com/sap/docs/images/bqc4sap-dataset-create.png)

  3. In the **Dataset ID** field, enter a unique name. For more information, see [Name datasets](https://docs.cloud.google.com/bigquery/docs/datasets#dataset-naming).




For more information about creating BigQuery datasets, see [Creating datasets](https://docs.cloud.google.com/bigquery/docs/datasets).

## Set up TLS/SSL certificates and HTTPS

Communication between BigQuery Connector for SAP and Google services is secured by using TLS/SSL and HTTPS.

  1. For connecting to Google services, follow the [Google Trust Services advice](https://pki.goog/faq/#connecting-to-google). At a minimum, you must download all root CA certificates from the [Google Trust Services repository](https://pki.goog/repository/).

To make sure that you're using the latest trusted root CA certificates, we recommend that you update your system's root certificate store every six months. Google announces new and removed root CA certificates at [Google Trust Services](https://pki.goog/updates/). For receiving automatic notifications, subscribe to the RSS feed on [Google Trust Services](https://pki.goog/updates/).

  2. In the SAP GUI, use the `STRUST` transaction to import the root CA certificates into the `SSL client SSL Client (Standard)` PSE folder.

For more information from SAP, see [SAP Help - Maintain PSE Certification list](https://help.sap.com/viewer/e73bba71770e4c0ca5fb2a3c17e8e229/LATEST/en-US/49250a3467cd3895e10000000a421937.html).

  3. On the SAP LT Replication Server host, confirm that any firewall rules or proxies are configured to allow egress traffic from the HTTPS port to the BigQuery API.

Specifically, SAP LT Replication Server needs to be able to access the following Google Cloud APIs:

     * For CDC replication through Pub/Sub: 
       * `https://pubsub.googleapis.com`
       * `https://bigquery.googleapis.com`
       * `https://iamcredentials.googleapis.com`
     * For streaming data replication: 
       * `https://bigquery.googleapis.com`
       * `https://iamcredentials.googleapis.com`
     * For file-based replication to Cloud Storage: 
       * `https://storage.googleapis.com`
       * `https://iamcredentials.googleapis.com`

If you want BigQuery Connector for SAP to access Google Cloud APIs through Private Service Connect endpoints in your VPC network, then you must configure RFC destinations and specify your Private Service Connect endpoints in those RFC destinations. For more information, see [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations).




For more information from SAP about setting up TLS/SSL, see [SAP Note 510007 - Additional considerations for setting up TLS/SSL on Application Server ABAP](https://launchpad.support.sap.com/#/notes/510007).

## Specify access settings in `/GOOG/CLIENT_KEY`

Use transaction `SM30` to specify settings for access to Google Cloud. BigQuery Connector for SAP stores the settings as a record in the `/GOOG/CLIENT_KEY` custom configuration table.

To specify the access settings, do the following:

  1. In the SAP GUI, enter transaction code `SM30`.

  2. Select the `/GOOG/CLIENT_KEY` configuration table.

  3. Enter values for the following table fields:

Field | Data type | Description  
---|---|---  
**Name** | String | Specify a descriptive name for the `CLIENT_KEY` configuration, such as `BQC_CKEY`. A client key name is a unique identifier that is used by the BigQuery Connector for SAP to identify the configurations for accessing Google Cloud.  
**Service Account Name** | String |  The name of the service account, in email address format, that you created for BigQuery Connector for SAP in the step Create a service account. For example: `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.   
**Scope** | String |  The access scope. Specify the `https://www.googleapis.com/auth/cloud-platform` API access scope, as [recommended by Compute Engine](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice).   
**Project ID** | String | The ID of the project that contains your target BigQuery dataset.  
**Command name** | String |  Leave this field blank.  
**Authorization Class** | String | `/GOOG/CL_GCP_AUTH_JWT`  
**Authorization Field** | Not applicable | Leave this field blank.  
**Token Caching** | Boolean |  Leave this field blank.   
**Token Refresh Seconds** | Integer |  Leave this field blank.   
**Authorization Parameter 1** | String |  Leave this field blank.   
**Authorization Parameter 2** | String | Leave this field blank.  



### Configure RFC destinations

To connect the BigQuery Connector for SAP to Google Cloud, we recommend that you use [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations).

Sample RFC destinations `GOOG_OAUTH2_TOKEN`, `GOOG_IAMCREDENTIALS`, and `GOOG_BIGQUERY` are imported as part of the BigQuery Connector for SAP transport.

You need to create new RFC destinations by copying the sample RFC destinations.

To configure the RFC destinations, do the following:

  1. In the SAP GUI, enter transaction code `SM59`.

  2. (Recommended) Create new RFC destinations by copying the sample RFC destinations, and then make a note of the new RFC destination names. You use them in later steps.

The BigQuery Connector for SAP uses RFC destinations to connect to Google Cloud APIs.

     1. For the RFC destinations that you created, make sure the **Connection Type** field is set to `G - HTTP connection to external server`.

     2. Go to the **Technical Settings** tab and enter the following details:

        * **Target Host** : enter the Google Cloud API hostname.

To avoid inter-region data transfer costs for CDC replication through Pub/Sub, we recommend that you create an RFC destination for the [regional Pub/Sub endpoint](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#list_regional_endpoints) where your SAP system and BigQuery dataset are located.

        * **Path Prefix** : enter the resource path. For information about the required path prefix, see [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations).

        * **Service No.** : enter `443`. This port number is used for secure communication.

     3. Go to the **Logon & Security** tab and make sure that the **SSL Certificate** field is set with the option **DFAULT SSL Client (Standard)**.

     4. Optionally, you can configure proxy settings, enable HTTP compression, and specify Private Service Connect endpoints.

     5. Save your changes.

     6. To test the connection, click **Connection Test**.

A response containing `404 Not Found` is acceptable and expected because the endpoint specified in the RFC destination corresponds to a Google Cloud service and not a specific resource hosted by the service. Such a response indicates that the target Google Cloud service is reachable and that no target resource was found.

  3. In the SAP GUI, enter transaction code `SM30`.

  4. In the `/GOOG/CLIENT_KEY` table that you created in the preceding section, note the value for the **Name** field.

  5. In the table `/GOOG/SERVIC_MAP`, create entries with the following field values:

Google Cloud Key Name | Google Service Name | RFC Destination  
---|---|---  
`CLIENT_KEY_NAME` | `bigquery.googleapis.com` | Specify the name of your RFC destination that targets BigQuery. If you're using the sample RFC destination for testing purposes, then specify `GOOG_BIGQUERY`.  
`CLIENT_KEY_NAME` | `pubsub:v1` | Specify the name of your RFC destination that targets Pub/Sub. If you're using the sample RFC destination for testing purposes, then specify `GOOG_PUBSUB`.  
`CLIENT_KEY_NAME` | `storage.googleapis.com` | Specify the name of your RFC destination that targets Cloud Storage. If you're using the sample RFC destination for testing purposes, then specify `GOOG_STORAGE`.  
`CLIENT_KEY_NAME` | `iamcredentials.googleapis.com` | Specify the name of your RFC destination that targets IAM. If you're using the sample RFC destination for testing purposes, then specify `GOOG_IAMCREDENTIALS`.  
`CLIENT_KEY_NAME` | `googleapis.com/oauth2` | Specify the name of your RFC destination that targets the Google OAuth 2.0 Token endpoint, used for exchanging JWTs for access tokens. If you're using the sample RFC destination for testing purposes, then specify `GOOG_OAUTH2_TOKEN`.   
  
Replace `CLIENT_KEY_NAME` with the client key name that you noted in the preceding step.




### Configure proxy settings

When you use RFC destinations to connect to Google Cloud, you can route communication from BigQuery Connector for SAP through the proxy server that you're using in your SAP landscape.

If you don't want to use a proxy server or don't have one in your SAP landscape, then you can skip this step.

To configure proxy server settings for BigQuery Connector for SAP, complete the following steps:

  1. In the SAP GUI, enter transaction code `SM59`.

  2. Select your RFC destination that targets IAM.

  3. Go to the **Technical Settings** tab, and then enter values for the fields in the **HTTP Proxy Options** section.

  4. Repeat the previous step for your RFC destination that targets BigQuery.




### Enable HTTP compression

When you use RFC destinations to connect to Google Cloud, you can enable [HTTP compression](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#http_compression).

If you don't want to enable this feature, then you can skip this step.

To enable HTTP compression, do the following:

  1. In the SAP GUI, enter transaction code `SM59`.

  2. Select your RFC destination that targets BigQuery.

  3. Go to the **Special Options** tab.

  4. For the **HTTP Version** field, select **HTTP 1.1**.

  5. For the **Compression** field, select an appropriate value.

For information about the compression options, see [SAP Note 1037677 - HTTP compression compresses certain documents only](https://launchpad.support.sap.com/#/notes/1037677)




### Specify Private Service Connect endpoints

If you want the BigQuery Connector for SAP to use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) endpoints to allow private consumption of BigQuery and IAM, then you need to create those endpoints in your Google Cloud project and specify them in the respective RFC destinations.

If you want the BigQuery Connector for SAP to continue using the default, public API endpoints to connect to BigQuery and IAM, then skip this step.

To configure BigQuery Connector for SAP to use your Private Service Connect endpoints, do the following:

  1. In the SAP GUI, enter transaction code `SM59`.

  2. Validate that you have created new RFC destinations for BigQuery and IAM. For instructions to create these RFC destinations, see Configure RFC destinations.

  3. Select the RFC destination that targets BigQuery and then do the following:

     1. Go to the **Technical Settings** tab.

     2. For the **Target Host** field, enter the name of the Private Service Connect endpoint that you created to access BigQuery.

     3. Go to the **Logon and Security** tab.

     4. For the **Service No.** field, make sure that value `443` is specified.

     5. For the **SSL Certificate** field, make sure that the option **DFAULT SSL Client (Standard)** is selected.

  4. Select the RFC destination that targets IAM and then do the following:

     1. Go to the **Technical Settings** tab.

     2. For the **Target Host** field, enter the name of the Private Service Connect endpoint that you created to access IAM.

     3. Go to the **Logon and Security** tab.

     4. For the **Service No.** field, make sure that value `443` is specified.

     5. For the **SSL Certificate** field, make sure that the option **DFAULT SSL Client (Standard)** is selected.




## What's next

  * [Configure the connector for CDC replication through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api)

  * [Configure the connector for streaming data replication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api)

  * [Configure the connector for file-based replication to Cloud Storage](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
