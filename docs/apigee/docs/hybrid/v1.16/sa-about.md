---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about/
title: About service accounts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:47.934793+00:00
---

# About service accounts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  About service accounts Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-about.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/sa-about.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-about.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/sa-about.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/sa-about.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/sa-about.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/sa-about.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-about.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/sa-about.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/sa-about.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/sa-about.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/sa-about.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/sa-about.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/sa-about.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/sa-about.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/sa-about.html)



A _service account_ is a special type of account in Google Cloud that enables components and applications of a system to interact with each other and with other APIs. For more information about Google Cloud, see [About Google Cloud services](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/what-is-hybrid#about-gcp).

**SERVICE ACCOUNT FACTOID**  
Google Cloud projects have a limit of 100 service accounts—including the default service accounts (if any).

Apigee hybrid uses Google Cloud service accounts to perform a variety of tasks, including: 

  * Send log and metrics data
  * Pull trace requests
  * Connect to API gateway for administrative API requests
  * Execute back ups
  * Download proxy bundles



While one service account _could_ perform all of these operations, for production environments Apigee recommends that you create multiple service accounts, each assigned to a specific task and each with its own set of permissions. This enhances security by compartmentalizing access and limiting each service account's scope and access privileges. As with user accounts, these permissions are applied by assigning one or more roles to the service account.

## Service accounts and roles used by hybrid components

To operate properly, Apigee hybrid requires you to create several service accounts. Each service account requires a specific role or roles that enable it to perform its function. 

The following table describes the service accounts for the hybrid components. The names given for each service account are the default names. You can use any names you want, but the names should be easy to identify with each account's purpose.

Component* | Role | Required for basic install? | Description  
---|---|---|---  
`apigee-cassandra` | [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin)  
`roles/storage.objectAdmin` |  | Allows Cassandra backups to Cloud Storage, as described in [Backup and recovery](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/backup-recovery).  
`apigee-guardrails` | [Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer)  
`roles/serviceusage.serviceUsageViewer` |  | Allows the guardrails pod in the `apigee-operator` chart to check if required APIs are enabled in the project for successful installation of Apigee hybrid, as described in [Diagnosing issues with guardrails](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/guardrails).  
`apigee-logger` | [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter)  
`roles/logging.logWriter` |  | Allows logging data collection, as described in [Logging](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/logging). Only required for non-GKE cluster installations.  
`apigee-mart` | [Apigee Connect Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.Agent)  
`roles/apigeeconnect.Agent` |  | Allows MART service authentication. The Apigee Connect Agent role allows it to communicate securely with the Apigee Connect process, as described in [Using Apigee Connect](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-connect).  
`apigee-metrics` | [Monitoring Metric Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter)  
`roles/monitoring.metricWriter` |  | Allows metrics data collection, as described in [Metrics collection overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/metrics-collection).   
`apigee-mint-task-scheduler` | No role required |  | Serves as the identity the `apigee-mint-task-scheduler` image runs as, allowing it to generate recurring fees for Rate Plans that define them. See [Enabling monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid).   
`apigee-runtime` | No role required |  | Allows the Apigee hybrid runtime to connect to Google services and custom services on Google Cloud, such as [Google Authentication](https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview), [Google Cloud Trace](https://cloud.google.com/trace), and [Jaeger](https://www.jaegertracing.io/). **Note:** If you are using Google Cloud Trace or Jaeger, you must assign the Cloud Trace Agent IAM role (`roles/cloudtrace.agent`) to the `apigee-runtime` service account.  
`apigee-synchronizer` | [Apigee Synchronizer Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.synchronizerManager)  
`roles/apigee.synchronizerManager` |  | Allows the synchronizer to download proxy bundles and environment configuration data. Also enables operation of the trace feature.  
`apigee-watcher` | [Apigee Runtime Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.runtimeAgent)  
`roles/apigee.runtimeAgent` |  | Apigee Watcher pulls virtual hosts related changes for an org from synchronizer and makes necessary changes to configure istio ingress.  
* This name is used in the downloaded service account key's filename.  
  
As an alternative, for nonproduction, test, and demo environments, you can use a single service account with all the roles assigned to it. This is not recommended for production environments. 

Component* | Role | Required for basic install? | Description  
---|---|---|---  
`apigee-non-prod` | [Apigee Connect Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.Agent), [Apigee Runtime Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.runtimeAgent), [Apigee Synchronizer Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.synchronizerManager), [Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter), [Monitoring Metric Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter), [Service Usage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageViewer), [Storage Object Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) | Or all required SAs above | Single service account for demo or test environments. See [Install, Part 2, Step 4: Set up service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts).  
  
In addition to creating the service accounts listed in this table, you will use each accounts private keys to generate access tokens so that you can access the Apigee APIs. The `create-service-account` tool automatically downloads the key files into a directory on your local machine when it creates or updates the service accounts.

## Create the service accounts

**Deleting and recreating service accounts:** Note that reusing the name of a deleted service account may result in unexpected behavior. If you create a service account and delete it, always recreate it with a unique name. For details, see [ Deleting and recreating service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview#deleting-recreating). 

There are several ways to create service accounts, including:

  * (_Recommended_) `create-service-account` tool
  * Google Cloud console
  * gcloud SDK



Each of these is described in the following sections.

### Use the `create-service-account` tool

The `create-service-account` tool is available after you download and expand the [Apigee hybrid Helm Charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-download-charts). You can find the `create-service-account` tool in the following directory:
    
    
    APIGEE_HELM_CHARTS_HOME/
    └── apigee-operator/
        └── etc/
            └── tools/
                └── create-service-account
    

`create-service-account` creates hybrid component-specific service accounts and assigns the required roles for you. The tool also automatically downloads the service account keys and stores them on your local machine.

For example, the following command will create all the separate individual service accounts for a production environment, assign the appropriate IAM roles to each service account, and download each account's private key file to the `./service-accounts` directory:
    
    
    ./tools/create-service-account --env prod

The following command creates a single service account named `apigee-non-prod` with all IAM roles for all hybrid components, suitable for demo and test environments, but not for production environments: 
    
    
    ./tools/create-service-account --env non-prod

For more information on using `create-service-account`, see [create-service-account reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/create-service-account).

### Use the Google Cloud console

You can create service accounts with the Google Cloud console.

**Note:** To create service accounts in the Google Cloud console, you must have the Google Cloud Service Account Admin role or greater.

**To create a service account with the Google Cloud console and generate a key for the service account, do the following:**

  1. Create a service account:

     1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Select your project. 
     3. Click add**Create Service Account**. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

Apigee recommends that you use a name that reflects the service account's role; you can set the name of the service account to be the same name as the component that uses it. For example, set the name of the Logs Writer service account `apigee-logger`. 

For more information about the service accounts names and roles, see Service accounts and roles used by hybrid components. 

     5. Optional: In the **Service account description** field, enter a description for the service account. Descriptions are helpful at reminding you what a particular service account is used for. 
     6. Click **Create and continue**. 
     7. Click the **Select a role** field and select a role, as described in Service accounts and roles used by hybrid components. If the Apigee roles do not appear in the drop down list, refresh the page. 

For example, for the logging component, select the Logs Writer role.

If necessary, enter text to filter the list of roles by name. For example, to list only the Apigee roles, enter `Apigee` in the filter field. 

You can add more than one role to a service account, but Apigee recommends using only one role for each of the recommended service accounts. To change the roles of a service account after you have created it, use the **IAM** page in the Google Cloud console. 

**Note:** If you do not see the roles listed in Recommended service accounts, check with your Apigee account representative to be sure that your account was properly configured and that your organization was provisioned.
     8. Click **Continue**. 

Google Cloud displays the **Grant users access to this service account** view:

![Fields for Service account users role and Service account admins role, button for Create key](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.16/images/grant-users-access.png)

     9. Under **Create key (optional)** , click **Create Key**. 

Google Cloud gives you the option to download a JSON or P12 key:

![Select JSON or P12 key type](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.16/images/create-key-gcp.png)

     10. Select JSON (the default) and click **Create**. 

Google Cloud saves the key file in JSON format to your local machine and displays a confirmation when it is successful, as the following example shows:

![Example filename.json](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.16/images/private-key-saved.png)

You will later use some of the service account keys to configure hybrid runtime services. For example, when you configure the hybrid runtime, you will specify the location of the service account keys using the SERVICE_NAME`.serviceAccountPath` properties. 

These keys are used by the service accounts to get access tokens, which the service account then uses to make requests against the Apigee APIs on your behalf. (But that's not for a while yet; for now, just remember where you saved it.)

     11. Repeat steps 4 through 11 for each service account listed in Service accounts and roles used by hybrid components (except the `apigee-mart` account—which has no role associated with it—so do not assign it a role). 

When you're finished, you should have the following service accounts (in addition to the defaults, if any):

![List of service accounts. Column 1 selection box, column 2 Email, column 3 Status, column 4 service account name](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.16/images/service-account-list.png)

In the Google Cloud console, service accounts are indicated with the ![left side key, right side half rectangle, all underlined](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.16/images/gcp-icon-service-account.png) icon.

After you create a service account, if you want to add or remove a role to it, you must use the **IAM & Admin** view. You cannot manage roles for service accounts in the **Service accounts** view.

**Tip:** Apigee hybrid includes a validator that checks your service accounts' key files and permissions when you apply any configuration changes to the Apigee hybrid runtime components to your cluster. This validation is enabled by default. For more information, see [Service account validation](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-validation). 

### Use the gcloud service account creation APIs

You can create and manage service accounts with the Cloud Identity and Access Management API. 

For more information, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

##  Troubleshooting 

**Deleting and recreating service accounts:** Note that reusing the name of a deleted service account, may cause unexpected behavior. If you create a service account and delete it, always recreate it with a unique name. For details, see [ Deleting and recreating service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview#deleting-recreating). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
