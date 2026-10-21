---
url: https://docs.cloud.google.com/apigee/docs/apihub/provision-cli/
title: Provision API hub from the command line \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:49:30.908573+00:00
---

# Provision API hub from the command line  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/provision-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provision API hub from the command line Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page explains how to provision API hub from the command line. To provision API hub using the wizard-style UI, see [Provision API hub in the Cloud console](https://docs.cloud.google.com/apigee/docs/apihub/provision). To provision API hub using a Terraform configuration, see [Provision API hub using Terraform](https://docs.cloud.google.com/apigee/docs/apihub/provision-terraform). 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Make sure that you have the following role or roles on the project: 

     * `roles/serviceusage.serviceUsageAdmin`
     * `roles/serviceusage.serviceUsageViewer`
     * `roles/cloudkms.admin`
     * `roles/apihub.provisioningAdmin`
     * `roles/resourcemanager.projectIamAdmin`

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  7. Ensure that your Google Cloud project doesn't have the `Google Cloud Platform - Resource Location Restriction` [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) added. **Important:** API hub uses Cloud Scheduler for some of its features. Cloud Scheduler is not available in all Google Cloud locations. If you are provisioning API hub in a location where Cloud Scheduler is not available, it will be provisioned in a fallback location. For a list of these locations and their fallbacks, see [API hub locations](https://docs.cloud.google.com/apigee/docs/apihub/locations). If your organization has a `Resource Location Restriction` policy that prevents resources from being created in the fallback location, provisioning will fail. 
  8. Optional: [Configure VPC Service Controls](https://docs.cloud.google.com/apigee/docs/apihub/vpc-service-control).



## Summary of steps

The provisioning steps are as follows:

  * Step 1: Enable APIs. You must enable a set of Google Cloud APIs for Apigee API hub to operate.
  * Step 2: Create the Apigee API hub service identity. The service identity allows the API hub instance to call the Google Cloud APIs it requires to perform its operations.
  * Step 3. Grant the roles and permissions to the default service account.
  * Step 4. Configure encryption. You can choose whether to use a Google-owned and Google-managed encryption key (GMEK) or Customer-managed encryption key (CMEK) approach to encrypt and decrypt your API data at rest. See [ Comparison of CMEK and Google-owned and Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek). 
  * Step 5: Create the API hub instance. To finish up, you must register the host project and create the API hub instance.

**Note:** If you haven't already provisioned Apigee in your project, API hub provisioning also creates an Apigee organization in your project. 

## Provisioning steps

Ensure that you have met the prerequisites described in Before you begin.

**Caution:** If you have recently deprovisioned API hub, you must wait **7 days** before provisioning a new instance in the same Google Cloud project. This is because deprovisioning moves the associated Apigee organization (if any) to a soft-delete state for **7 days** , and API hub can only be reprovisioned after the Apigee org is permanently deleted. 

### Step 1: Enable APIs

To provision API hub, you must enable the following APIs in your Google Cloud project:

#### Permissions required for this task

You can give the Apigee API hub provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ API enablement permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#api-enablement-permissions). 

  1. Enable the required Google Cloud APIs by executing the following [`services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command:
         
         gcloud services enable apihub.googleapis.com \
             cloudkms.googleapis.com --project=YOUR_PROJECT_ID

Where `YOUR_PROJECT_ID` is the Cloud project ID that you created in Before you begin. **Important:** Enabling the API hub API also automatically enables the Apigee API (`apigee.googleapis.com`) for your Google Cloud project. This applies to all projects, regardless of whether Apigee has been provisioned or if the Apigee API was previously disabled. 

Note that API hub remains a free service. Auto-enablement of the Apigee API during the API hub provisioning process has no pricing or billing implications for your project. 




### Step 2: Create the Apigee API hub service identity

The [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) allows the API hub instance to call the Google Cloud APIs it requires to perform its operations.

  1. Create the service identity:
         
         gcloud beta services identity create --service=apihub.googleapis.com \
           --project=YOUR_PROJECT_ID

Where `YOUR_PROJECT_ID` is the Cloud project ID that you created in Before you begin.

  2. Verify that the agent was successfully created. The response includes the name of the agent in the following format: `service-PROJECT_NUMBER@gcp-sa-apihub.iam.gserviceaccount.com`. For example: 
         
         Service identity created: service-1234567890@gcp-sa-apihub.iam.gserviceaccount.com

Note that you will need to use this service identity in a later step.




### Step 3: Grant the roles and permissions to the default service account

In this step, you grant the `apihub.admin` and `apihub.runtimeProjectServiceAgent` roles to the API hub default service account. These permissions are required to use [API hub plugins](https://docs.cloud.google.com/apigee/docs/apihub/plugins).
    
    
    gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
      --member=serviceAccount:SERVICE_ACCOUNT \
      --role="roles/apihub.admin"
        
    
    
    gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
      --member=serviceAccount:SERVICE_ACCOUNT \
      --role="roles/apihub.runtimeProjectServiceAgent"
        

Where:

  * `YOUR_PROJECT_ID`: The Cloud project ID that you created in Before you begin.
  * `SERVICE_ACCOUNT`: The ID of the service account you created in Step 2. The ID will look something like this: `service-1234567890@gcp-sa-apihub.iam.gserviceaccount.com`.



### Step 4: Configure encryption

In this step, you configure how the encryption of data in your API hub instance is managed. You can use a Google-owned and Google-managed encryption key (GMEK) or create your own customer-managed encryption key (CMEK). See [ Comparison of CMEK and Google-owned and Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek).

**Caution:** If you use CMEK to encrypt your API hub data, ensure the key remains enabled and available. If the key is disabled or becomes unavailable for more than **7 days** , all data in your API hub instance will be permanently deleted and the instance will enter an unrecoverable state. 

### CMEK steps

Follow these steps if you wish to use CMEK for data encryption:

  1. Create a runtime database encryption key ring and key. You can use an existing CMEK key and key ring if you wish. Note that the key must be created in the same location where you plan to create the API hub instance. 

     1. Create a new key ring:

The key ring's name must be unique to your organization. If you create a second or subsequent region, the name cannot be the same as any other key ring.
            
            gcloud kms keyrings create KEY_RING_NAME \
              --location KEY_RING_LOCATION --project YOUR_PROJECT_ID

Where:

        * `KEY_RING_NAME`: The name of the key ring to create.
        * `KEY_RING_LOCATION`: The physical location of the key ring. This location must be the same as you plan to use for the API hub instance you will create in a later step. For the list of available locations, see [API hub locations](https://docs.cloud.google.com/apigee/docs/apihub/locations).
        * `YOUR_PROJECT_ID`: The Cloud project ID that you created in Before you begin.
     2. Create the encryption key and add it to the key ring:
            
            gcloud kms keys create KEY_NAME \
              --keyring KEY_RING_NAME \
              --location KEY_LOCATION \
              --purpose "encryption" \
              --project YOUR_PROJECT_ID

Where:

        * `KEY_NAME`: The name of the database key you are creating.
        * `KEY_RING_NAME`: The name of the key ring you just created.
        * `KEY_LOCATION`: The physical location of the key. Use the same location you used to create the key ring.
     3. Get the key ID: 
            
            gcloud kms keys list \
              --location=KEY_LOCATION \
              --keyring=KEY_RING_NAME \
              --project=YOUR_PROJECT_ID

The key ID has the following syntax (similar to a file path). Retain this key ID, as you will need to use it in a later step:
            
            projects/YOUR_PROJECT_ID/locations/KEY_LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME

     4. Grant access for the Apigee Service Agent to use the new key:
            
            gcloud kms keys add-iam-policy-binding KEY_NAME \
              --location KEY_LOCATION \
              --keyring KEY_RING_NAME \
              --member serviceAccount:SERVICE_ACCOUNT \
              --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project YOUR_PROJECT_ID

Where: SERVICE_ACCOUNT is the ID of the service account you created in Step 2. The ID will look something like this: `service-1234567890@gcp-sa-apihub.iam.gserviceaccount.com`.

This command binds the key to the Apigee API hub Service Agent.

On successful completion of this request, `gcloud` responds with something similar to the following:
            
            Updated IAM policy for key [runtime].
            bindings:
            - members:
              - serviceAccount:service-1234567890@gcp-sa-apihub.iam.gserviceaccount.com
              role: roles/cloudkms.cryptoKeyEncrypterDecrypter
            etag: BwWqgEuCuwk=
            version: 1

If you get an error like the following:
            
            INVALID_ARGUMENT: Role roles/cloudkms.cryptokms.cryptoKeyEncrypterDecrypter is not supported for this resource.

Be sure that you used the project _number_ and not the project name in the service account email address.




### GMEK steps

If you wish to use GMEK for data encryption, go to the next step, Step 5: Create the API hub instance, now. No further key configuration is required.

### Step 5: Create the API hub instance

A _host project_ is the Google Cloud project in which you will provision Apigee API hub. You can provision only one API hub instance per host project.

  1. Register the host project: 
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" -d '{
           "gcpProject": "projects/YOUR_PROJECT_ID"
           }' https://apihub.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/PROJECT_LOCATION/hostProjectRegistrations?host_project_registration_id=HOST_ID

Where:

     * `YOUR_PROJECT_ID`: The Cloud project ID that you created in Before you begin.
     * `PROJECT_LOCATION`: The physical location (region) where you'd like to host your Apigee API hub instance. You must use the same location you used to create the CMEK key and key ring. For the list of available locations, see [API hub locations](https://docs.cloud.google.com/apigee/docs/apihub/locations).
  2. `HOST_ID`: The name of your Google Cloud project where you'd like to provision Apigee API hub.
  3. Create the API hub instance: 

### With CMEK

If you used CMEK for data encryption, execute the following command:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" -H "X-Google-GFE-Can-Retry: yes" -d '{
           "config":{
             "cmekKeyName":"KEY_NAME",
             "vertexLocation":"VERTEX_LOCATION",
             "disableSearch":false,
             "encryptionType":"CMEK"
             }
           }' https://apihub.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/PROJECT_LOCATION/apiHubInstances?api_hub_instance_id=INSTANCE_ID

Where:

     * `KEY_NAME` (Required): The fully qualified name of the CMEK key. This name was returned when the key was created. For example: `projects/YOUR_PROJECT_ID/locations/HOST_LOCATION/hostProjectRegistrations/HOST_ID`.
     * `VERTEX_LOCATION` (Optional): Specifies the [multi-region location](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations) in which to store your Vertex AI-based search data, the data associated with the [Semantic Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis#semantic-search) feature of API hub. You can use either `us` or `eu` for this value. **Note:** If you don't specify a location for Vertex AI-based search data, omit this parameter and set the `disableSearch` parameter to `true`.
     * `encryptionType` (Required) You must use `CMEK`. 
     * `YOUR_PROJECT_ID` is the Cloud project ID that you created in Before you begin.
     * `PROJECT_LOCATION`: You must use the same location you used to register the host project.
     * `INSTANCE_ID`: The name of the API hub instance. This value should be 4-40 characters, and valid characters are `/[a-z][A-Z][0-9]-_/`. 

### With GMEK

If you are using GMEK for data encryption, execute the following command:
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" -H "X-Google-GFE-Can-Retry: yes" -d '{
      "config":{
        "vertexLocation":"VERTEX_LOCATION",
        "disableSearch":false,
        "encryptionType":"GMEK"
        }
      }' https://apihub.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/PROJECT_LOCATION/apiHubInstances?api_hub_instance_id=INSTANCE_ID

Where:

     * `VERTEX_LOCATION` (Optional): Specifies the [multi-region location](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations) in which to store your Vertex AI-based search data, the data associated with the [Semantic Search](https://docs.cloud.google.com/apigee/docs/apihub/search-apis#semantic-search) feature of API hub. You can use either `us` or `eu` for this value. **Note:** If you don't specify a location for Vertex AI-based search data, omit this parameter and set the `disableSearch` parameter to `true`.
     * `encryptionType` must be `GMEK`. If you do not provide an encryption type, GMEK is the default. 
     * `YOUR_PROJECT_ID` is the Cloud project ID that you created in Before you begin.
     * `PROJECT_LOCATION`: You must use the same location you used to register the host project.
     * `INSTANCE_ID`: The name of the API hub instance. This value should be 4-40 characters, and valid characters are `/[a-z][A-Z][0-9]-_/`. 

### Step 5: (Optional) Create a runtime project attachment

If you provisioned API hub in a project that has Apigee proxies, perform this optional step to automatically register the proxies in API hub.
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" -H "X-Google-GFE-Can-Retry: yes" \
      -d '{
        "runtimeProject": "projects/YOUR_PROJECT_ID"
      }' \
      "https://apihub.googleapis.com/v1/projects/YOUR_PROJECT_ID/locations/PROJECT_LOCATION/runtimeProjectAttachments?runtimeProjectAttachmentId=YOUR_PROJECT_ID"
      

Where:

     * `YOUR_PROJECT_ID` is the Cloud project ID that you created in Before you begin.
     * `PROJECT_LOCATION`: You must use the same location you used to register the host project.

## Considerations

If you have recently deprovisioned API hub, you must wait **7 days** before provisioning a new instance in the same Google Cloud project. This is because deprovisioning moves the associated Apigee organization (if any) to a soft-delete state for **7 days** , and API hub can only be reprovisioned after the Apigee org is permanently deleted. 

## What's next

Now, you are ready to begin using API hub:

     * Learn about the [Get started with API hub](https://docs.cloud.google.com/apigee/docs/apihub/getting-started-apihub) page.
     * Review the [roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/iam-roles) required to use API hub
     * Configure API hub attributes: 
       * [Manage attributes](https://docs.cloud.google.com/apigee/docs/apihub/manage-attributes)
       * [Quickstart: Create and edit attributes](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-settings)
     * Register an API resource: 
       * [Manage API resources](https://docs.cloud.google.com/apigee/docs/apihub/manage-apis)
       * [Quickstart: Register an API](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-api)
     * Add an API version: 
       * [Versions overview](https://docs.cloud.google.com/apigee/docs/apihub/versions-intro)
       * [Quickstart: Create an API version](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
