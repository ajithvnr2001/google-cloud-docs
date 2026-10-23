---
url: https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc/
title: Version 2.0: Install and configure BigQuery Connector for SAP on a Compute Engine VM \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:48.722596+00:00
---

# Version 2.0: Install and configure BigQuery Connector for SAP on a Compute Engine VM  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Version 2.0: Install and configure BigQuery Connector for SAP on a Compute Engine VM Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows how to install and configure **version 2.0 or 2.1** of the BigQuery Connector for SAP in an SAP LT Replication Server that is running on a Compute Engine virtual machine (VM) on Google Cloud.

This guide covers how to prepare BigQuery, SAP Landscape Transformation Replication Server (SAP LT Replication Server), and BigQuery Connector for SAP to replicate SAP data from SAP applications directly and securely to BigQuery in real time.

This guide is intended for SAP administrators, Google Cloud administrators, and other SAP and Google Cloud security and data professionals.

## Prerequisites

Before you install BigQuery Connector for SAP, make sure that the following prerequisites have been satisfied:

  * You have read the [BigQuery Connector for SAP planning guide](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning). The planning guide explains BigQuery Connector for SAP options, performance considerations, field mapping, and other information that you need for the optimal configuration of BigQuery Connector for SAP.
  * If you don't have a Google Cloud project already, create one:

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * Billing is enabled for your project. [Learn how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project). A billing account is required for BigQuery streaming API, BigQuery, and to download BigQuery Connector for SAP.

  * Maintenance for the installed SAP software is current and the versions of all of the SAP software are compatible with each other, as documented in the [SAP Product Availability Matrix](https://support.sap.com/en/release-upgrade-maintenance.html#section_1969201630).

  * The versions of the SAP software you are using are supported by the BigQuery Connector for SAP, as documented in [Software requirements](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#reqs-software).

  * You have the correct SAP licenses that are required to replicate data to any target via the SAP LT Replication Server SDK. For more information about SAP licensing, see [SAP Note 2707835](https://launchpad.support.sap.com/#/notes/2707835).

  * SAP LT Replication Server is installed. For information about installing SAP LT Replication Server, see the [SAP documentation](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

  * The RFC or database connection between SAP LT Replication Server and the source system is configured. If necessary, test the RFC connections by using SAP transaction `SM59`. Test database connections by using SAP transaction `DBACOCKPIT`.




## Overview of the installation and configuration process

The following table shows procedures covered in this guide and the roles that typically perform them.

**Note:** Depending on your version of SAP LT Replication Server, some of the details in the procedures that are documented in this guide might differ from the details that you see when you perform the steps.Procedure | Role  
---|---  
If necessary, after validating all appropriate licenses from SAP, follow the SAP instructions to [install an SAP Landscape Transformation Replication Server](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US). | SAP administrator.   
If necessary, install the user interface (UI) add-on for SAP NetWeaver. For more information, see [SAP software version requirements](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#reqs-software-sap). | SAP administrator.   
Enable the required Google Cloud APIs.  | Google Cloud administrator.  
If necessary, install the gcloud CLI on the SAP LT Replication Server host.  | SAP administrator.   
Create a BigQuery dataset. | Google Cloud administrator or data engineer.  
Set up Google Cloud authentication and authorization. | Google Cloud security administrator.  
Download the BigQuery Connector for SAP installation package. | Google Cloud billing account holder.  
Install BigQuery Connector for SAP. | SAP administrator.  
Create SAP roles and permissions for BigQuery Connector for SAP.  | SAP administrator.  
Configure replication.  | Data engineers or administrators.  
Test replication.  | Data engineers or administrators.  
Validate replication.  | Data engineers or administrators.  
  
## Enable the required Google Cloud APIs

Before BigQuery Connector for SAP can access BigQuery, you need to enable the following Google Cloud APIs:

  * The BigQuery API
  * The IAM Service Account Credentials API



For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

## Install the gcloud CLI

For replication to BigQuery, the `sidadm` user account must have access to the Google Cloud CLI (gcloud CLI) on the SAP LT Replication Server host.

The gcloud CLI is installed on most Compute Engine VMs by default. You can confirm its installation by issuing `gcloud components list`. If the command is unrecognized, you need to install the gcloud CLI. 

An SAP administrator can install the gcloud CLI.

To install the gcloud CLI, complete the following steps:

  1. Follow the [gcloud CLI installation instructions](https://docs.cloud.google.com/sdk/docs/install#installation_instructions).

  2. Authorize the `sidadm` user account to access the gcloud CLI installation directory.

  3. Optionally, as `sidadm`, set the default project for the gcloud CLI:
         
         [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) PROJECT_ID

Replace `PROJECT_ID` with the ID of the project that contains your BigQuery data set. For example, `example-project-123456`.

If you don't set a default project for the gcloud CLI, the `--project` property must be specified on each `gcloud` command that is issued.




For more information about BigQuery Connector for SAP requirement for the gcloud CLI, see [gcloud CLI requirement](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#reqs-software-cloud-sdk).

## Create a BigQuery dataset

Before you can test Google Cloud authentication and authorization for BigQuery or create target BigQuery tables, you or a data engineer or administrator needs to create a BigQuery dataset.

To create a BigQuery dataset, your user account must have the proper IAM permissions for BigQuery. For more information, see [Required permissions](https://docs.cloud.google.com/bigquery/docs/datasets#required_permissions).

  1. In the Google Cloud console, go to the BigQuery page:

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Next to your project ID, click the **View actions** icon, more_vert, and then **Create dataset**.

![Diagram is described in the preceding text](https://docs.cloud.google.com/sap/docs/images/bqc4sap-dataset-create.png)

  3. In the **Dataset ID** field, enter a unique name. For more information, see [Name datasets](https://docs.cloud.google.com/bigquery/docs/datasets#dataset-naming).




After you set up Google Cloud authentication and authorization, you test access to Google Cloud by retrieving information about this dataset.

For more information about creating BigQuery datasets, see [Creating datasets](https://docs.cloud.google.com/bigquery/docs/datasets).

## Set up Google Cloud authentication and authorization

For authentication to Google Cloud and authorization to access BigQuery, a Google Cloud security administrator and an SAP administrator need to:

  * Create a service account for the BigQuery Connector for SAP.
  * Grant the service account the IAM roles that are required to access BigQuery. 
  * Add the BigQuery Connector for SAP service account as a principal in the BigQuery project.
  * Configure security settings for Google Cloud on the SAP LT Replication Server host: 
    * Grant the host VM permission to obtain access tokens.
    * If necessary, modify API access scopes of host VM. 



### Create a service account

BigQuery Connector for SAP needs an IAM service account for authentication and authorization to access BigQuery.

This service account must be a principal in the Google Cloud project that contains your BigQuery dataset. If you create the service account in the same project as the BigQuery dataset, the service account is added as a principal to the project automatically.

If you create the service account in a project other than the project that contains the BigQuery dataset, you need to add the service account to the BigQuery dataset project in an additional step.

To create a service account, complete the following steps:

  1. In the Google Cloud console, go to the IAM & Admin **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. If prompted, select your Google Cloud project.

  3. Click **Create Service Account**.

  4. Specify a name for the service account and, optionally, a description.

  5. Click **Create and Continue**.

  6. If you are creating the service account in the same project as the BigQuery dataset, in the **Grant this service account access to project** panel, select the following roles:

     * **BigQuery Data Editor**
     * **BigQuery Job User**

If you are creating the service account in a different project than the BigQuery dataset, do not grant any roles to the service account.

  7. Click **Continue**.

  8. As appropriate, grant other users access to the service account.

  9. Click **Done**. The service account appears in the list of service accounts for the project.

  10. If you created the service account in a different project than the project that contains the BigQuery dataset, note the name of the service account. You specify the name when you add the service account to the BigQuery project. For more information, see Add the service account to the BigQuery project.




The service account is now listed as a principal on the [IAM Permissions](https://console.cloud.google.com/iam-admin/iam) page of the Google Cloud project in which the service account was created.

### Add the service account to the BigQuery project

If you created the service account for BigQuery Connector for SAP in a project other than the project that contains the target BigQuery dataset, you need to add the service account to the BigQuery dataset project.

If you created the service account in the same project as the BigQuery dataset, you can skip this step.

To add an existing service account to the BigQuery dataset project, complete the following steps:

  1. In the Google Cloud console, go to the IAM Permissions page:

[Go to IAM permissions](https://console.cloud.google.com/iam-admin/iam)

  2. Confirm that the name of the project that contains the target BigQuery dataset is displayed near the top of the page. For example:

**Permissions for project "` PROJECT_NAME`"**

If it is not, switch projects.

  3. On the IAM page, click addperson**Add**. The **Add principals to "` PROJECT_NAME`"** dialog opens.

  4. In the **Add principals to "` PROJECT_NAME`"** dialog, complete the following steps:

     1. In the **New principals** field, specify the name of the service account.
     2. In the **Select a role** field, specify **BigQuery Data Editor**.
     3. Click **ADD ANOTHER ROLE**. The **Select a role** field displays again.
     4. In the **Select a role** field, specify **BigQuery Job User**.
     5. Click **Save**. The service account appears in the list of project principals on the **IAM** page.



The service account can now be used to access the BigQuery dataset in this project.

### Configure security on the host VM

BigQuery Connector for SAP requires that the Compute Engine VM that is hosting SAP LT Replication Server be configured with the following security options:

  * The access scopes of the host VM must be set to allow full access to the Cloud APIs.
  * The service account of the host VM must include the IAM **Service Account Token Creator** role.



If these options are not configured on the host VM, you need to configure them.

To change a VM's access scopes, you need to stop the VM.

#### Check the API access scopes of the host VM

Check the current access scope setting of the SAP LT Replication Server host VM. If the VM already has full access to all Cloud APIs, you do not need to change the access scopes.

To check the access scope of a host VM, complete the following steps:

###  Google Cloud console 

  1. In the Google Cloud console, open the VM instances page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If necessary, select the Google Cloud project that contains the SAP LT Replication Server host.

  3. On the VM instances page, click the name of the host VM. The VM details page opens.

  4. Under **API and identity management** on the host VM details page, check the current setting of **Cloud API access scopes** :

     * If the setting is **Allow full access to all Cloud APIs** , the setting is correct and you do not need to change it.
     * If the setting is not **Allow full access to all Cloud APIs** , you need to stop the VM and change the setting. For instructions, see the next section.



###  gcloud CLI 

  1. Display the current access scopes of the host VM:
         
         gcloud compute instances describe VM_NAME --zone=VM_ZONE --format="yaml(serviceAccounts)"

If the access scopes do not include `https://www.googleapis.com/auth/cloud-platform`, you need to change the access scopes of the host VM. For example, if you were to create a VM instance with a default Compute Engine service account, you would need to change the following default access scopes:
         
         serviceAccounts:
         - email: 600915385160-compute@developer.gserviceaccount.com
           scopes:
           - https://www.googleapis.com/auth/devstorage.read_only
           - https://www.googleapis.com/auth/logging.write
           - https://www.googleapis.com/auth/monitoring.write
           - https://www.googleapis.com/auth/servicecontrol
           - https://www.googleapis.com/auth/service.management.readonly
           - https://www.googleapis.com/auth/trace.append

If the only scope listed under `scopes` is `https://www.googleapis.com/auth/cloud-platform`, as in the following example, you do not need to change the scopes:
         
         serviceAccounts:
         - email: 600915385160-compute@developer.gserviceaccount.com
           scopes:
           - https://www.googleapis.com/auth/cloud-platform




#### Change API access scopes of the host VM

If the SAP LT Replication Server host VM does not have full access to the Google Cloud APIs, change the access scopes to allow full access to all Cloud APIs.

**Caution:** The following instructions remove restrictions on the API access scopes of the host VM. If you currently use access scopes to limit the access of the host VM to Google Cloud APIs, [which is not recommended](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice), consider limiting access instead by restricting the IAM permissions that are granted to the service account of the host VM. 

Changing the permissions of a host VM service account changes the permissions of any program or process on the host VM that is not configured to use its own dedicated service account. 

To change the setting of **Cloud API access scopes** for a host VM, complete the following steps:

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

  1. If necessary, adjust the IAM roles that are granted to the VM service account to ensure that access to Google Cloud services from the host VM is appropriately restricted.

For information about how to change the roles that are granted to a service account, see [Updating a service account](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit#updating).

  2. If necessary, stop any SAP software that is running on the host VM.

  3. Stop the VM:
         
         gcloud compute instances stop VM_NAME --zone=VM_ZONE

  4. Change the access scopes of the VM:
         
         gcloud compute instances set-service-account VM_NAME --scopes=cloud-platform --zone=VM_ZONE

  5. Start the VM:
         
         gcloud compute instances start VM_NAME --zone=VM_ZONE

  6. If necessary, start the SAP software that is running on the host VM.




#### Enable the host VM to obtain access tokens

You need to grant the service account of the host VM permission to obtain the access tokens that the BigQuery Connector for SAP requires to access BigQuery.

To grant permission to create access tokens, complete the following steps:

  1. In the Google Cloud console, open the VM instances page:

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. On the VM instance page, click the name of the host VM to open the VM details page.

  3. On the VM details page under **API and identity management** , make a note of the name of the service account. The following example name is for a default Compute Engine service account:
         
         SVC-ACCT-NUMBER-compute@developer.gserviceaccount.com

  4. In the Google Cloud console, go to the IAM page:

[Go to IAM permissions](https://console.cloud.google.com/iam-admin/iam)

  5. In the list of project principals, find the service account name and click edit **Edit principal**. The **Edit permissions** dialog opens.

  6. In the **Edit permissions** dialog, click **ADD ANOTHER ROLE**. The **Select a role** field displays.

  7. In the **Select a role** field, specify **Service Account Token Creator**.

  8. Click **Save**. You are returned to the **IAM** permissions page.




The host VM now has permission to create access tokens.

### Set up SSL certificates and HTTPS

Communication between BigQuery Connector for SAP and the BigQuery API is secured by using SSL and HTTPS.

  1. Download the following certificates from the [Google Trust Services repository](https://pki.goog/repository/):

     * `GTS Root R1`
     * `GTS CA 1C3`
  2. In the SAP GUI, use the `STRUST` transaction to import both the root and subordinate certificate into the `SSL client SSL Client (Standard)` PSE folder.

For more information from SAP, see [SAP Help - Maintain PSE Certification list](https://help.sap.com/viewer/e73bba71770e4c0ca5fb2a3c17e8e229/LATEST/en-US/49250a3467cd3895e10000000a421937.html).

  3. On the SAP LT Replication Server host, confirm that any firewall rules or proxies are configured to allow egress traffic from the HTTPS port to the BigQuery API.

Specifically, SAP LT Replication Server needs to be able to access the following Google Cloud APIs:

     * https://bigquery.googleapis.com
     * https://iamcredentials.googleapis.com



For more information from SAP about setting up SSL, see [SAP Note 510007 - Additional considerations for setting up SSL on Application Server ABAP](https://launchpad.support.sap.com/#/notes/510007).

### Test Google Cloud authentication and authorization

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
         
         curl --request POST \
          'https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT:generateAccessToken' \
         --header 'Authorization: Bearer ACCESS_TOKEN_STRING_1' \
           --header 'Accept: application/json' \
           --header 'Content-Type: application/json' \
           --data '{"scope":["https://www.googleapis.com/auth/bigquery"],"lifetime":"300s"}' \
           --compressed
         

Replace the following:

     * `SERVICE_ACCOUNT`: the service account that you created for BigQuery Connector for SAP in an earlier step.
     * `ACCESS_TOKEN_STRING_1`: the first access token string from the preceding step.

The IAM API returns a second access token, ACCESS_TOKEN_STRING_2, that is similar to the following example. In the next step, you copy this second token string into a request to the BigQuery API.
    
    {"access_token":"ACCESS_TOKEN_STRING_2","expires_in":3599,"token_type":"Bearer"}

  5. Retrieve information about your BigQuery dataset from the BigQuery API by issuing the following command after replacing the placeholder values:
         
         curl "https://bigquery.googleapis.com/bigquery/v2/projects/PROJECT_ID/datasets/DATASET_NAME" \
          -H "Accept: application/json" -H "Authorization: Bearer ACCESS_TOKEN_STRING_2"
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains your BigQuery dataset.
     * `DATASET_NAME`: the name of the target dataset as defined in BigQuery.
     * `ACCESS_TOKEN_STRING_2`: the access token string returned by IAM API in the preceding step.

If your Google Cloud authentication is configured correctly, then information about the dataset is returned.

If it is not configured correctly, see [BigQuery Connector for SAP troubleshooting](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/troubleshooting).




## Download the installation package

Download the BigQuery Connector for SAP installation package from [BigQuery Connector for SAP download portal](https://bq-slt-connector.appspot.com/bqconnectorforsap/).

You need your Cloud Billing number to complete the download. For information about billing accounts, see [Cloud Billing & payments profile](https://docs.cloud.google.com/billing/docs/concepts#billing_account).

The installation package includes transport files that you copy into the appropriate transport directory for SAP LT Replication Server.

## Install BigQuery Connector for SAP

After you receive the installation package that contains the BigQuery Connector for SAP transport files, your SAP administrator can install BigQuery Connector for SAP by importing the transport files into SAP LT Replication Server.

The SAP transport for BigQuery Connector for SAP contains all of the objects that are required for BigQuery Connector for SAP, including the `/GOOG/` namespace, DDIC objects, the SLT SDK BADI implementation and classes, report programs, and more.

Before importing the transport files into SAP LT Replication Server, verify that your SAP LT Replication Server is supported by BigQuery Connector for SAP, as documented in [Software requirements](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#reqs-software).

In spite of using a supported version of SAP LT Replication Server, in some cases, while importing the transport files, you might see the error message, `Requests do not match the component version of the target system`. In such cases, you need to re-import the transport files into SAP LT Replication Server and while re-importing, on the Import Transport Request screen > Options tab, select the **Ignore Invalid Component Version** checkbox.

The following procedure is a general procedure. Each SAP system is different, so work with your SAP administrator to determine any changes to the procedure that might be required for your SAP system:

  1. Copy BigQuery Connector for SAP transport files into the following SAP LT Replication Server transport import directories:

     * `/usr/sap/trans/cofiles/KXXXXXX.ED1`
     * `/usr/sap/trans/data/RXXXXXX.ED1`

In the preceding examples, `XXXXXX` represents the numbered file name.

  2. In the SAP GUI, use transaction code `STMS_IMPORT` or `STMS` to import the files into the SAP system.

  3. Make sure all objects in `/GOOG/SLT_SDK` package are active and consistent:

     1. In the SAP interface, enter transaction code `SE80`.
     2. In the package selector, select `/GOOG/SLT_SDK`.
     3. In the **Object name** field, right-click on the package `/GOOG/SLT_SDK`, and then choose **Check > Package Check > Objects of Package**.

A green check in the **Result** column indicates that all objects passed the package check.




### Confirm that BigQuery Connector for SAP is ready to configure

To further confirm that the transport files have been imported correctly and that BigQuery Connector for SAP is ready to configure, confirm that BigQuery Connector for SAP Business Add-In (BAdI) implementation is active and that BigQuery Connector for SAP replication applications have entries in the `IUUC_REPL_APPL` table.

  1. Check the BAdI implementation: 
     1. Use the transaction **SE80** to navigate to and select the `/GOOG/EI_IUUC_REPL_RUNTIME_BQ` enhancement object folder.
     2. Select **Enh. Implementation Elements** on the right side of the page.
     3. Under **Runtime Behavior** , confirm that **Implementation is active** is checked.
  2. Check the replication applications: 
     1. Using the SAP **Data Browser** or transaction `SE16`, display the `IUUC_REPL_APPL` table.
     2. Confirm that the following applications appear in the `IUUC_REPL_APPL` table: 
        * `/GOOG/SLT_BQ`
        * `ZGOOG_SLT_BQ`, for use when the `/GOOG/` namespace isn't registered



## Create SAP roles and authorizations for BigQuery Connector for SAP

To work with BigQuery Connector for SAP, in addition to the standard SAP LT Replication Server authorizations, users need access to the custom transactions that are provided with BigQuery Connector for SAP: `/GOOG/SLT_SETTINGS` and `/GOOG/REPLIC_VALID`.

By default, users that have access to the custom transactions can modify the settings of any configuration, so if you need to, you can restrict access to specific configurations.

The BigQuery Connector for SAP transport files include the `Google BigQuery Settings Authorization` object, `ZGOOG_MTID`, for authorizations that are specific to BigQuery Connector for SAP.

To grant access to the custom transactions and restrict access to specific configurations:

  1. Using SAP transaction code `PFCG`, define a role for the BigQuery Connector for SAP.

  2. Grant the role access to the custom transactions `/GOOG/SLT_SETTINGS` and `/GOOG/REPLIC_VALID`.

  3. To limit the access of a role, specify the authorization group of each configuration that the role can access by using the `ZGOOG_MTID` authorization object. For example:

     * Authorization object for BigQuery Connector for SAP (`ZGOOG_MTID`): 
       * `Activity 01`
       * `Authorization Group AUTH_GROUP_1,AUTH_GROUP_N`

The `AUTH_GROUP_01` and `AUTH_GROUP_N` are values that are defined in the SAP LT Replication Server configuration.

The authorization groups specified for `ZGOOG_MTID` must match the authorization groups that are specified for the role in the SAP `S_DMIS_SLT` authorization object.




## Configure replication

To configure replication, you specify both BigQuery Connector for SAP and SAP LT Replication Server settings.

### Specify access settings in `/GOOG/CLIENT_KEY`

Use transaction `SM30` to specify settings for access to BigQuery. BigQuery Connector for SAP stores the settings as a record in the `/GOOG/CLIENT_KEY` custom configuration table.

To specify the access settings:

  1. In the SAP GUI, enter transaction code `SM30`.

  2. Select the `/GOOG/CLIENT_KEY` configuration table.

  3. Enter values for the following table fields:

Field | Data type | Description  
---|---|---  
Name | String | Specify a descriptive name for the `CLIENT_KEY` configuration, such as `ABAP_SDK_CKEY`. A client key name is a unique identifier that is used by the BigQuery Connector for SAP to identify the configurations for accessing BigQuery.  
Service Account Name | String |  The name of the service account, in email address format, that was created for BigQuery Connector for SAP in the step Create a service account. For example: `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.   
Scope | String |  Specify the `https://www.googleapis.com/auth/cloud-platform` API access scope, as [recommended by Compute Engine](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). This access scope corresponds to the setting **`Allow full access to all Cloud APIs`** on the host VM. For more information, see Set access scopes on the host VM.   
Project ID | String | The ID of the project that contains your target BigQuery dataset.  
Command name | String |  Leave this field blank.   
Authorization Class | String | The authorization class to use for replication.  Specify `/GOOG/CL_GCP_AUTH_GOOGLE`.   
Authorization Field | Not applicable | Leave this field blank.  
Token Refresh Seconds | Integer |  Specifies the amount of time in seconds before an access token expires and must be refreshed. The default is `3600` (one hour).  Specifying a value of `1` to `3599` overrides the default expiration time of `3600` seconds. If you specify `0`, BigQuery Connector for SAP uses the default value, `3600`.   



### Create an SAP LT Replication Server replication configuration

Use SAP transaction `LTRC` to create an SAP LT Replication Server replication configuration.

If SAP LT Replication Server is running on a different server than the source SAP system, before you create a replication configuration, confirm that you have an RFC connection between the two systems.

Some of the settings in the replication configuration affect performance. To determine appropriate setting values for your installation, see the _Performance Optimization Guide_ for your version of SAP LT Replication Server in the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).

The interface and configuration options for SAP LT Replication Server might be slightly different depending on which version you are using.

To configure replication, use the procedure for your version of SAP LT Replication Server:

  * Configure replication in DMIS 2011 SP17, DMIS 2018 SP02, or later
  * Configure replication in DMIS 2011 SP16, DMIS 2018 SP01, or earlier



#### Configure replication in DMIS 2011 SP17, DMIS 2018 SP02, or later

The following steps configure replication in later versions of SAP LT Replication Server. If you are using an earlier version, see Configure replication in DMIS 2011 SP16, DMIS 2018 SP01, or earlier.

  1. In the SAP GUI, enter transaction code `LTRC`.

  2. Click the **Create configuration** icon. The **Create Configuration** wizard opens.

  3. In the **Configuration Name** and **Description** fields, enter a name and a description for the configuration, and then click **Next**.

You can specify the **Authorization Group** for restricting access to a specific authorization group now or specify it later.

  4. In the **Source System Connection Details** panel:

     * Select the **RFC Connection** radio button.
     * In the **RFC Destination** field, specify the name of the RFC connection to the source system.
     * Select the checkboxes for **Allow Multiple Usage** and **Read from Single Client** as appropriate. For more information, see the [SAP LT Replication Server documentationl](https://help.sap.com/viewer/product/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/LATEST/en-US).
     * Click **Next**.

These steps are for an RFC connection, but if your source is a database, you can select **DB Connection** if you have already defined a connection by using transaction `DBACOCKPIT` instead.

  5. In the **Target System Connection Details** panel:

     * Select the radio button for **Other**.
     * In the **Scenario** field, select **SLT SDK** from the drop-down menu.
     * Click **Next**.
  6. On the **Specify Transfer Settings** panel:

     1. In the **Application** field of the **Data Transfer Settings** section, enter `/GOOG/SLT_BQ` or `ZGOOG_SLT_BQ`.

     2. In the **Job options** section, enter starting values in each of the following fields:

        * **Number of Data Transfer Jobs**
        * **Number of Initial Load Jobs**
        * **Number of Calculation Jobs**
     3. In the **Replication Options** section, select the **Real Time** radio button.

     4. Click **Next**.

  7. After reviewing the configuration, click **Save**.

  8. Make a note of the three-digit ID in the **Mass Transfer** column. You use it in a later step.




For more information, see the PDF attached to [SAP Note 2652704](https://launchpad.support.sap.com/#/notes/2652704): _Replicating Data Using SLT SDK - DMIS 2011 SP17, DMIS 2018 SP02.pdf_.

#### Configure replication in DMIS 2011 SP16, DMIS 2018 SP01, or earlier

The following steps configure replication in earlier versions of SAP LT Replication Server. If you are using a later version, see Configure replication in DMIS 2011 SP17, DMIS 2018 SP02, or later.

  1. In the SAP GUI, enter transaction code `LTRC`.
  2. Click **New**. A dialog opens for specifying a new configuration.
  3. In the step **Specify Source System** : 
     * Choose **RFC Connection** as the connection type.
     * Enter the RFC connection name.
     * Ensure that the field **Allow Multiple Usage** is selected.
  4. In the step **Specify Target System** : 
     * Enter the connection data to the target system.
     * Choose **RFC Connection** as the connection type.
     * In the field **Scenario for RFC Communication** , select the value **Write Data to Target Using BAdI** from the drop-down list. The RFC connection is automatically set to **NONE**.
  5. In the step **Specify Transfer Settings** , press **F4 Help**. The application that you defined previously is displayed in the **Application** field.
  6. Make a note of the three-digit ID in the **Mass Transfer** column. You use it in a later step.



For more information, see the PDF attached to [SAP Note 2652704](https://launchpad.support.sap.com/#/notes/2652704): _Replicating Data Using SLT SDK - DMIS 2011 SP15, SP16, DMIS 2018 SP00, SP01.pdf_.

### Create a mass transfer configuration for BigQuery

Use the custom `/GOOG/SLT_SETTINGS` transaction to configure a mass transfer for BigQuery and specify the table and field mappings.

#### Select the initial mass transfer options

When you first enter the `/GOOG/SLT_SETTINGS` transaction, you select which part of the BigQuery mass transfer configuration you need to edit.

To select the part of the mass transfer configuration:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. From the **Settings Table** drop-down menu in the launch screen for the `/GOOG/SLT_SETTINGS` transaction, select **Mass Transfers**.

For a new mass transfer configuration, leave the **Mass Transfer Key** field blank.

  3. Click the **Execute** icon. The **BigQuery Settings Maintenance - Mass Transfers** screen displays.




#### Specify table creation and other general attributes

In the initial section of a BigQuery mass transfer configuration, you identify the mass transfer configuration and specify the associated client key, as well as certain properties related to the creation of the target BigQuery table.

SAP LT Replication Server saves the mass transfer configuration as a record in the `/GOOG/BQ_MASTR` custom configuration table.

The fields that you specify in the following steps are required.

  1. In the **BigQuery Settings Maintenance - Mass Transfers** screen, click the **Append Row** icon.

  2. In the displayed row, specify the following settings:

     1. In the **Mass Transfer Key** field, define a name for this transfer. This name becomes the primary key of the mass transfer.
     2. In the **Mass Transfer ID** field, enter the three-digit ID that was generated when you create the corresponding SAP LT Replication Server replication configuration.
     3. To use the labels or short descriptions of the source fields as the names for the target fields in BigQuery, click the **Use Custom Names Flag** checkbox. For more information about field names, see [Default naming options for fields](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#default-field-names).
     4. To store the type of change that triggered an insert and to enable the validation of record counts between the source table, SAP LT Replication Server statistics, and the BigQuery table, select the **Extra Fields Flag** checkbox.

When this flag is set, BigQuery Connector for SAP adds columns to the BigQuery table schema. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#add-fields-for-changes-and-counts).

     5. To stop sending data when a record with a data error is encountered, click the **Break at First Error Flag** checkbox, which is recommended. For more information, see [The BREAK flag](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#break-flag).

     6. When a record with a data error is encountered, to skip the record and continue inserting records into the BigQuery table, click the **Skip Invalid Records Flag** checkbox. We recommend leaving this unchecked. For more information, see [The SKIP flag](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#skip-flag).

     7. In the **Google Cloud Key Name** field, enter the name of the corresponding `/GOOG/CLIENT_KEY` configuration.

BigQuery Connector for SAP retrieves the Google Cloud Project Identifier automatically from the `/GOOG/CLIENT_KEY` configuration.

     8. In the **BigQuery Dataset** field, enter the name of the target BigQuery dataset that you created earlier in this procedure.

     9. In the **Is Setting Active Flag** field, enable the mass transfer configuration by clicking the checkbox.

     10. Click **Save**.

A mass transfer record is appended in the `/GOOG/BQ_MASTR` table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.

     11. Click **Display Table**.

The new mass transfer record is displayed followed by the table attribute entry panel.




### Specify table attributes

You can specify table attributes, such as table name and table partitioning, as well as the number of records to include in each transmission or _chunk_ that is sent to BigQuery, in the second section of the `/GOOG/SLT_SETTINGS` transaction.

The settings that you specify are stored as a record in the `/GOOG/BQ_TABLE` configuration table.

These settings are optional.

To specify table attributes:

  1. Click the **Append row** icon.

  2. In the **SAP Table Name** field, enter the name of the source SAP table.

  3. In the **External Table Name** field, enter the name of the target BigQuery table. If the target table doesn't already exist, BigQuery Connector for SAP creates the table with this name. For the BigQuery naming conventions for tables, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming).

  4. The **Send Uncompressed Flag** field disables record compression. Specify this flag only if you need BigQuery Connector for SAP to replicate any empty fields in the source records with the values that the fields were initialized with in the source table. For better performance, do not specify this flag. For more information, see [Record compression](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#record_compression).

  5. Optionally, in the **Chunk Size** field, specify the maximum number of records to include in each chunk that is sent to BigQuery. If you can, use the maximum chunk size that BigQuery Connector for SAP allows, which is currently 10,000 records and the default value. If the source records have a large number of fields, the number of fields can increase the overall byte size of the chunks, which can cause chunk errors. If this occurs, try reducing the chunk size to reduce the byte size. For more information, see [Chunk size in the BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#chunk-size-bqc4sap).

  6. Optionally, in the **Partition Type** field, specify an increment of time to use for partitioning. Valid values are `HOUR`, `DAY`, `MONTH`, or `YEAR`. For more information, see [Table partitioning](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#table_partitioning).

  7. Optionally, in the **Partition Field** field, specify the name of a field in the target BigQuery table that contains a timestamp to use for partitioning. When you specify **Partition Field** , you must also specify **Partition Type**. For more information, see [Table partitioning](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#table_partitioning).

  8. In the **Is Setting Active Flag** field, enable the table attributes by clicking the checkbox. If the **Is Setting Active Flag** box is not checked, BigQuery Connector for SAP creates the BigQuery table with the name of the SAP source table, the default chunk size, and no partitioning.

  9. Click **Save**.

Your attributes are stored as a record in the `/GOOG/BQ_TABLE` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.

  10. Click **Display Fields**.

The new table attribute record is displayed, followed by the field mapping entry panel.




### Customize the default field mapping

If the source SAP table contains timestamp fields or booleans, change the default data type mapping to accurately reflect the data type in the target BigQuery table.

You can also change other data types, as well as the names that are used for target fields.

You can edit the default mapping directly in the SAP GUI or you can export the default mapping to a spreadsheet or a text file so that others can edit the values without requiring access to SAP LT Replication Server.

For more information about the default field mapping and the changes you can make, see [Field mapping](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#field_mapping).

To customize the default mapping for the target BigQuery fields:

  1. In the **BigQuery Settings Maintenance - Fields** page of transaction `/GOOG/SLT_SETTINGS`, display the default field mappings for the mass transfer you are currently configuring.

  2. Edit the default target data types in the **External Data Element** column as needed. In particular, change the target data type for the following data types:

     * **Timestamps.** Change the default target data type from `NUMERIC` to `TIMESTAMP` or `TIMESTAMP (LONG)`.
     * **Booleans.** Change the default target data type from `STRING` to `BOOLEAN`.
     * **Hexadecimals.** Change the default target data type from `STRING` to `BYTES`.

To edit the default data type mapping:

     1. On the row of the field that you need to edit, click the **External Data Element** field. 
     2. In the dialog for data types, select the BigQuery data type that you need.
     3. Confirm your changes, and then click **Save**.
  3. If you specified the **Custom Names** flag in the **BigQuery Settings Maintenance** page, edit the default target field names in the **Temporary Field Name** column as needed.

The values that you specify override the default names that are shown in the **External Field Name** column.

  4. Edit the default target field descriptions in the **Field Description** column as needed.

  5. Optionally, export the field map for external editing. For instructions, see [Edit the BigQuery field map in a CSV file](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#edit_the_field_map_in_a_csv_file).

  6. After all changes are complete and any externally edited values have been uploaded, confirm that the **Is Setting Active Flag** checkbox is selected. If **Is Setting Active Flag** is not selected, BigQuery Connector for SAP creates target tables with the default values.

  7. Click **Save**.

The changes are stored in the `/GOOG/BQ_FIELD` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.




## Test replication

Test the replication configuration by starting data provisioning:

  1. Open the SAP LT Replication Server Cockpit (transaction `LTRC`) in the SAP GUI.

  2. Click on the mass transfer configuration for the table replication that you are testing.

  3. Click **Data Provisioning**.

  4. In the **Data Provisioning** panel, start data provisioning:

     1. Enter the name of the source table.
     2. Click the radio button for the type of data provisioning that you want to test. For example, **Start Load**.
     3. Click the **Execute** icon. The data transfer begins and the progress is displayed on the **Participating objects** screen.

If the table doesn't exist in BigQuery, the BigQuery Connector for SAP creates the table from a schema that it builds from the table and field attributes that you previously defined with the `/GOOG/SLT_SETTINGS` transaction.

The length of time that an initial load of a table takes depends on the size of the table and its records.

Messages are written to the SAP LT Replication Server **Application Logs** section in transaction `LTRC`.




## Validate replication

You can validate replication using the following methods:

  * In SAP LT Replication Server: 
    * Monitor the replication on the **Data Provisioning** screen.
    * Check for error messages in the **Application Logs** screen.
  * On the table information tab in BigQuery: 
    * Check the **Schema** tab to ensure that the schema looks right.
    * Check the **Preview** tab to see a preview of the inserted rows.
    * Check the **Details** tab for the number of rows inserted, the size of the table, and other information.
  * If the **Extra Fields Flag** checkbox was selected when the BigQuery table was configured, run the Replication Validation tool by entering the `/GOOG/REPLIC_VALID` custom transaction.



### Check replication in SAP LT Replication Server

Use transaction `LTRC` to see the progress of initial load or replication jobs after you start them and to check for error messages.

You can see the status of the load under the **Load Statistics** tab and the progress of the job under the **Data Transfer Monitor** tab in SAP LT Replication Server.

On the **Application Logs** screen of transaction `LTRC`, you can see all of the messages that are returned by BigQuery, the BigQuery Connector for SAP, and SAP LT Replication Server.

Messages that are issued by BigQuery Connector for SAP code in SAP LT Replication Server start with the prefix `/GOOG/SLT`. Messages that are returned from the BigQuery API start with the prefix `/GOOG/MSG`.

Messages that are returned by SAP LT Replication Server do not start with a `/GOOG/` prefix.

### Check replication in BigQuery

In the Google Cloud console, confirm that the table was created and that BigQuery is inserting data into it.

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the search field of the **Explorer** section, type the name of the target BigQuery table, and then press `Enter`.

The table information is displayed under a tab in the content pane on the right side of the page.

  3. In the table information section, click the following headings to check the table and row insertion:

     * **Preview** , which shows the rows and fields that are inserted into the BigQuery table.
     * **Schema** , which shows the field names and data types.
     * **Details** , which shows the table size, the total number of rows, and other details.



### Run the Replication Validation tool

If the **Extra Fields Flag** was selected when the BigQuery table was configured, you can use the Replication Validation tool to generate reports that compare the number of records in the BigQuery table with record counts in the SAP LT Replication Server statistics or the source table.

To run the Replication Validation tool:

  1. In the SAP GUI, enter the `/GOOG/REPLIC_VALID` transaction preceded by `/n`:
         
         /n/GOOG/REPLIC_VALID

  2. In the **Processing Options** section, click the **Execute Validation** radio button.

  3. In the **Selection Options** section, enter the following specifications:

     * From the drop-down menu in the **GCP Partner Identifier** field, select **BigQuery**.
     * From the drop-down menu in the **Check Type** field, select the type of report to generate: 
       * Initial Load Counts
       * Replication Counts
       * Current Counts
     * If the **Check Date** field is displayed, specify the date that you need the counts for.
     * In the **Mass Transfer Key** field, enter the mass transfer configuration name.
  4. Run the Replication Validation tool by clicking the **Execute** icon.

  5. After the validation check is complete, in the **Processing Options** section, display the report by clicking the **Display Report** radio button and then clicking the **Execute** icon.




**BigQuery record counts:** The Replication Validation tool flags any mismatched record counts with a red circle; however, a mismatch in replication counts does not always indicate a problem. 

A record count in BigQuery that is moderately higher than the record count in the source table is normal. 

For more information, see [Unequal record counts](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#rvt-status-field). 

For more information, see [Replication Validation tool](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations#replication_validation_tool).

## Troubleshooting

For information about diagnosing and resolving issues that you might encounter when you configure and run loads or replications between SAP and BigQuery with BigQuery Connector for SAP, see [BigQuery Connector for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/troubleshooting).

## Get support

If you need help resolving problems with replication and the BigQuery Connector for SAP, collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
