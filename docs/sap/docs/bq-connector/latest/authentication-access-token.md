---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token/
title: Authenticate with access tokens \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:47.911164+00:00
---

# Authenticate with access tokens  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/authentication-access-token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authenticate with access tokens Stay organized with collections  Save and categorize content based on your preferences. 

To authenticate your SAP systems that run on a Compute Engine instance, you can configure access token-based authentication for the BigQuery Connector for SAP. This setup enables your SAP applications to securely interact with Google Cloud services.

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

## Create a service account

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

## Configure security on the host VM

BigQuery Connector for SAP requires that the Compute Engine VM that is hosting SAP LT Replication Server be configured with the following security options:

  * The access scopes of the host VM must be set to allow full access to the Cloud APIs.
  * The service account of the host VM must include the IAM **Service Account Token Creator** role.



If these options are not configured on the host VM, you need to configure them.

### Check the API access scopes of the host VM

Check the current access scope setting of the SAP LT Replication Server host VM. If the VM already has full access to all Cloud APIs, then you don't need to change the access scopes.

To check the access scope of a host VM, do the following:

###  Google Cloud console 

  1. In the Google Cloud console, open the VM instances page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If necessary, select the Google Cloud project that contains the SAP LT Replication Server host.

  3. On the VM instances page, click the name of the host VM. The VM details page opens.

  4. Under **API and identity management** on the host VM details page, check the current setting of **Cloud API access scopes** :

     * If the setting is **Allow full access to all Cloud APIs** , the setting is correct and you don't need to change it.
     * If the setting is not **Allow full access to all Cloud APIs** , you need to stop the VM and change the setting. For instructions, see the next section.



###  gcloud CLI 

  1. Display the current access scopes of the host VM:
         
         gcloud compute instances describe VM_NAME --zone=VM_ZONE --format="yaml(serviceAccounts)"

If the access scopes don't include `https://www.googleapis.com/auth/cloud-platform`, you need to change the access scopes of the host VM. For example, if you were to create a VM instance with a default Compute Engine service account, you would need to change the following default access scopes:
         
         serviceAccounts:
         - email: 600915385160-compute@developer.gserviceaccount.com
           scopes:
           - https://www.googleapis.com/auth/devstorage.read_only
           - https://www.googleapis.com/auth/logging.write
           - https://www.googleapis.com/auth/monitoring.write
           - https://www.googleapis.com/auth/servicecontrol
           - https://www.googleapis.com/auth/service.management.readonly
           - https://www.googleapis.com/auth/trace.append

If the only scope listed under `scopes` is `https://www.googleapis.com/auth/cloud-platform`, as in the following example, you don't need to change the scopes:
         
         serviceAccounts:
         - email: 600915385160-compute@developer.gserviceaccount.com
           scopes:
           - https://www.googleapis.com/auth/cloud-platform




### Change API access scopes of the host VM

If the SAP LT Replication Server host VM does not have full access to the Google Cloud APIs, change the access scopes to allow full access to all Cloud APIs.

**Caution:** The following instructions remove restrictions on the API access scopes of the host VM. If you use access scopes to limit the access of the host VM to Google Cloud APIs, [which is not recommended](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice), consider limiting access instead by restricting the IAM permissions that are granted to the service account of the host VM. 

Changing the permissions of a host VM service account changes the permissions of any program or process on the host VM that is not configured to use its own dedicated service account. 

To change the setting of **Cloud API access scopes** for a host VM, do the following:

###  Google Cloud console 

  1. If necessary, limit the roles that are granted to the security account of the host VM.

You can find the security account name on the details page of the host VM under **API and identity management**. You can change the roles that are granted to a service account in the Google Cloud console on the [IAM page](https://console.cloud.google.com/iam-admin/iam) under **Principals**.

  2. If necessary, stop any workloads that are running on the host VM.

  3. In the Google Cloud console, open the VM instances page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. On the VM instance page, click the name of the host VM to open the VM details page.

  5. At the top of the host VM details page, stop the host VM by clicking stop **STOP**.

  6. After the VM is stopped, click edit **EDIT**.

  7. Under **Security and access** > **Access scopes** , select **Allow full access to all Cloud APIs**.

  8. Click **Save**.

  9. At the top of the host VM details page, start the host VM by clicking play_arrow **START/RESUME**.

  10. If necessary, restart any workloads that are stopped on the host VM.




###  gcloud CLI 

  1. If necessary, adjust the IAM roles that are granted to the VM service account to make sure that access to Google Cloud services from the host VM is appropriately restricted.

For information about how to change the roles that are granted to a service account, see [Updating a service account](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit#updating).

  2. If necessary, stop any SAP software that is running on the host VM.

  3. Stop the VM:
         
         gcloud compute instances stop VM_NAME --zone=VM_ZONE

  4. Change the access scopes of the VM:
         
         gcloud compute instances set-service-account VM_NAME --scopes=cloud-platform --zone=VM_ZONE

  5. Start the VM:
         
         gcloud compute instances start VM_NAME --zone=VM_ZONE

  6. If necessary, start the SAP software that is running on the host VM.




### Enable the host VM to obtain access tokens

You need to create a dedicated service account for the host VM and grant the service account permission to obtain the access tokens that the BigQuery Connector for SAP requires to access Google Cloud.

To enable the host VM to obtain access tokens, do the following:

  1. In the Google Cloud console, create an IAM service account for the host VM instance.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

For information about how to create a service account, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

  2. Grant the [`Service Account Token Creator`](https://docs.cloud.google.com/compute/docs/access/iam#iam.serviceAccountTokenCreator) role to the service account. For information about how to grant a role, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

  3. Attach the service account to the VM instance where your SAP workload is running.

For information about how to attach a service account to a VM instance, see [Create a VM and attach the service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using).




The host VM now has permission to create access tokens.

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
**Scope** | String |  The access scope. Specify the `https://www.googleapis.com/auth/cloud-platform` API access scope, as [recommended by Compute Engine](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). This access scope corresponds to the setting **`Allow full access to all Cloud APIs`** on the host VM. For more information, see Set access scopes on the host VM.   
**Project ID** | String | The ID of the project that contains your target BigQuery dataset.  
**Command name** | String |  Leave this field blank.  
**Authorization Class** | String | Specify `/GOOG/CL_GCP_AUTH_GOOGLE`  
**Authorization Field** | Not applicable | Leave this field blank.  
**Token Caching** | Boolean |  The flag that determines whether or not the access tokens retrieved from Google Cloud are cached.  We recommend that you enable token caching after you are done configuring BigQuery Connector for SAP and testing your connection to Google Cloud. For more information about token caching, see [Enable token caching](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#enable-token-caching).   
**Token Refresh Seconds** | Integer |  The amount of time, in seconds, before an access token expires and must be refreshed. The default value is `3500`. You can overwrite this default value by setting a value for the `CMD_SECS_DEFLT` parameter in the [advanced settings](https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations#advanced-settings).  Specifying a value from `1` to `3599` overrides the default expiration time. If you specify `0`, then the BigQuery Connector for SAP uses the default value.   
**Authorization Parameter 1** | String |  Leave this field blank.   
**Authorization Parameter 2** | String | Leave this field blank.  



### Configure RFC destinations

To connect the BigQuery Connector for SAP to Google Cloud, we recommend that you use [RFC destinations](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#rfc_destinations).

Sample RFC destinations `GOOG_IAMCREDENTIALS` and `GOOG_BIGQUERY` are imported as part of the BigQuery Connector for SAP transport.

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




## Validate HTTP and HTTPS ports in Internet Communication Manager (ICM)

The [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) is stored on a metadata server, which is only accessible through an HTTP port. Therefore, you must validate that an HTTP port along with an HTTPS port is created and active in order to access the VM metadata.

  1. In the SAP GUI, enter transaction code `SMICM`.
  2. On the menu bar, click **Goto** > **Services**. A green check in the **Actv** column indicates that the HTTP and HTTPS ports are active.



For information about configuring the HTTP and HTTPS ports, see [HTTP(S) Settings in ICM](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-US/4c/5bdafa97817511e10000000a42189b/frameset.htm).

## Test Google Cloud authentication and authorization

Confirm that you have configured Google Cloud authentication correctly by requesting an access token and retrieving information about your BigQuery dataset.

Use the following procedure to test your Google Cloud authentication and authorization from the SAP LT Replication Server host VM:

  1. On the SAP LT Replication Server host VM, open a command-line shell.

  2. Switch to the `sidadm` user.

  3. Request the first access token from the metadata server of the host VM:
         
         curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" -H "Metadata-Flavor: Google"

The metadata server returns an access token that is similar to the following example, in which ACCESS_TOKEN_STRING_1 is an access token string that you copy into the command in the following step:
         
         {"access_token":"ACCESS_TOKEN_STRING_1",
         "expires_in":3599,"token_type":"Bearer"}

  4. Request the second access token from the IAM API by issuing the following command after replacing the placeholder values:

###  Linux 
         
         curl --request POST \
         "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT:generateAccessToken" \
           --header "Authorization: Bearer ACCESS_TOKEN_STRING_1" \
           --header "Accept: application/json" \
           --header "Content-Type: application/json" \
           --data "{"scope":["https://www.googleapis.com/auth/bigquery"],"lifetime":"300s"}" \
           --compressed
         

###  Windows 
         
         curl --request POST `
         "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT:generateAccessToken" `
           --header "Authorization: Bearer ACCESS_TOKEN_STRING_1" `
           --header "Accept: application/json" `
           --header "Content-Type: application/json" `
           --data "{"scope":["https://www.googleapis.com/auth/bigquery"],"lifetime":"300s"}" `
           --compressed
         

Replace the following:

     * `SERVICE_ACCOUNT`: the service account that you created for BigQuery Connector for SAP in an earlier step.
     * `ACCESS_TOKEN_STRING_1`: the first access token string from the preceding step.

The IAM API returns a second access token, ACCESS_TOKEN_STRING_2, that is similar to the following example. In the next step, you copy this second token string into a request to the BigQuery API.
    
    {"access_token":"ACCESS_TOKEN_STRING_2","expires_in":3599,"token_type":"Bearer"}

  5. Retrieve information about your BigQuery dataset by issuing the following command after replacing the placeholder values.

If you're configuring replication to Cloud Storage, then skip this step.

###  Linux 
         
         curl "https://bigquery.googleapis.com/bigquery/v2/projects/PROJECT_ID/datasets/DATASET_NAME" \
         -H "Accept: application/json" -H "Authorization: Bearer ACCESS_TOKEN_STRING_2"
         

###  Windows 
         
         curl "https://bigquery.googleapis.com/bigquery/v2/projects/PROJECT_ID/datasets/DATASET_NAME" `
         -H "Accept: application/json" -H "Authorization: Bearer ACCESS_TOKEN_STRING_2"
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains your BigQuery dataset.
     * `DATASET_NAME`: the name of the target dataset as defined in BigQuery.
     * `ACCESS_TOKEN_STRING_2`: the access token string returned by IAM API in the preceding step.

If your Google Cloud authentication is configured correctly, then information about the dataset is returned.

If it is not configured correctly, see [BigQuery Connector for SAP troubleshooting](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting).




## What's next

  * [Configure the connector for CDC replication through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api)

  * [Configure the connector for streaming data replication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api)

  * [Configure the connector for file-based replication to Cloud Storage](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
