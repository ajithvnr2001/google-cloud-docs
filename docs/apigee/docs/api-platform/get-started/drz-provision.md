---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision/
title: Provision your organization with data residency \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:47.432462+00:00
---

# Provision your organization with data residency  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-provision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provision your organization with data residency Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to provision your Apigee organization with data residency at rest only or with advanced data residency. 

See also [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). 

## Provision your organization with data residency at rest only

As an Apigee admin, to provision your organization with data residency at rest only, to restrict where data is stored, use one of the available paid organization [provisioning options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-options). Be sure to select the **Enable data residency** checkbox during provisioning. 

## Provision your organization with advanced data residency

As an Apigee admin, to provision your organization with advanced data residency, including data storage (at rest), processing (in use), and transmission (in transit), you need to do the following steps. 

**#** | **Step** | **Description** | **Performed by**  
---|---|---|---  
1  | Create an Assured Workloads folder | Create an Assured Workload folder in your Google Cloud organization to set and enforce the required organization policies that restrict resource usage only in allowed locations.  | Google Cloud admin with **Assured Workloads Administration** permission   
2  | Provision with advanced data residency | Provision your paid organization with advanced data residency by using one of the available paid organization [provisioning options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-options).  You must use the jurisdictional console to access the Apigee UI or regional endpoint to access the Apigee APIs based on your control plane location.  | Apigee Organization admin   
  
### Create an Assured Workload folder

**Note** : You must be a Google Cloud admin with **[Assured Workloads Administration permission](https://docs.cloud.google.com/assured-workloads/docs/iam-roles)** to set up an Assured Workload folder. 

Assured Workloads allow organizations to apply and enforce regulatory, regional, and sovereignty controls on Google Cloud resources. 

Using the Google Cloud console, you [create an Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder) in your Google Cloud organization and select a control package based on your regulation requirements. A [control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) is a set of controls that, when combined together, supports the baseline for a compliance framework, statute, or regulation. The control package sets and enforces the required [organization policy constraints](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-org-policy) to:  


  * Restrict resource usage to only the supported products 
  * Allow creating or using resources only in allowed locations 



For more information about Assured Workloads, see [Overview of Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview). 

### Provision with advanced data residency

**Note** : You must be an [Apigee Organization admin](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) to provision a paid organization with advanced data residency. 

As an Apigee admin, when provisioning your paid organization using one of the [provisioning options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-options), you'll need to use the jurisdictional console to access the Apigee UI or regional endpoint when using the CLI. 

#### Use the jurisdictional console

When provisioning your organization with advanced data residency, you'll need to use the location-based jurisdictional console to access the Apigee UI. When provisioning the Apigee organization using the jurisdictional console, the following fields are configured automatically:  


  * **Enable data residency** is selected (and can't be deselected) 
  * **Control plane hosting jurisdiction** options are filtered based on the jurisdictional console in use 
  * All other region selectors are filtered to only show locations within the selected control plane hosting jurisdiction

**Before provisioning your Apigee organization using the EU jurisdictional console** , you must manually create customer-managed encryption (CMEK) keys with external protection level using the Google Cloud CLI. You can't use the EU jurisdictional console to create externally backed CMEK keys. See How to create CMEK keys with external protection level using the gcloud CLI. 

For information about how to access the jurisdictional console, see [Jurisdictional Google Cloud console](https://cloud.google.com/assured-workloads/docs/jurisdictional-console) and [Shared responsibility in Assured Workloads](https://cloud.google.com/assured-workloads/docs/shared-responsibility). 

#### Use the regional endpoint

When provisioning your organization with advanced data residency, use the following regional endpoint:

`apigee.CONTROL_PLANE_LOCATION.rep.googleapis.com`

Where CONTROL_PLANE_LOCATION is the physical location where Apigee control plane data will be stored. For a list of available control plane locations, see [Use regional endpoints for advanced data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint-advanced).

During provisioning, you are responsible for selecting the appropriate values. If you use a location that is prohibited by the [organization policies](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-org-policy) that are in place, you'll receive a `Permission Denied` error. 

For example, the following command creates an Apigee organization in the US region with CMEK enabled. See also [Apigee organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations). 
    
    
    curl "https://**apigee.us.rep.googleapis.com** /v1/organizations?parent=projects/**$PROJECT_ID** " \
      -X POST
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "$PROJECT_ID",
        "runtimeType": "CLOUD", # Hybrid organizations aren't supported
        "billingType": "**$BILLING_TYPE** ", # Eval organizations aren't supported
        "controlPlaneEncryptionKeyName" : "'"**$CONTROL_PLANE_KEY_ID** "'",
        "apiConsumerDataLocation" : "'"**$CONSUMER_DATA_REGION** "'",  # Must be single region in US
        "apiConsumerDataEncryptionKeyName" : "'"**$CONSUMER_DATA_KEY_ID** "'",
        "authorizedNetwork" : "'"$NETWORK_NAME"'", # Must be created in the US region
        "runtimeDatabaseEncryptionKeyName" : "'"**$RUNTIMEDB_KEY_ID** "'"
      }'
    

#### How to create CMEK keys with external protection level using the gcloud CLI

When provisioning your Apigee organization with advanced data residency in the EU region, you need to create customer-managed encryption (CMEK) keys with **external** protection level. You must use the Google Cloud CLI to create the CMEK keys because the EU jurisdictional console doesn't support setting up externally backed CMEK keys. In addition, you'll need to set up an External Key Manager (EKM).

To create the CMEK keys and set up an EKM, follow the steps described in the following sections:

  * Set up an EKM
  * Create the CMEK keys



##### Set up an EKM

The CMEK keys created for the EU region must be created with external protection level, requiring that you set up an EKM. To set up an EKM, follow the instructions provided in the following sections: 

  * [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm)
  * [Set up Cloud EKM via the internet](https://docs.cloud.google.com/kms/docs/set-up-ekm-internet)



##### Create the CMEK keys for the EU region

Create the following CMEK keys required for the EU region using the gcloud CLI commands described below:

  * Control plane encryption key
  * API consumer data encryption key
  * Runtime database encryption key
  * Runtime disk encryption key



For more information about creating CMEK keys, see [About the Apigee encryption keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys#generating-new-keys-on-the-command-line). 

**Repeat the following steps to create each of the required CMEK keys** : 

  1. Create a key ring in the EU region using the following command:  

         
         gcloud kms keyrings create DATA_KEY_RING \
               **--location LOCATION** \
               --project=PROJECT_ID
             

  2. Create an _external_ key using the following command:  

         
         gcloud kms keys create DATA_KEY_NAME \
               --keyring=DATA_KEY_RING \
               **--location LOCATION** \
               --purpose encryption \
               **--protection-level external \
               --skip-initial-version-creation \
               --default-algorithm external-symmetric-encryption** \
               --project PROJECT_ID
             

  3. Create a key version that points to the EKM set up in the previous step using the following command:  

         
         gcloud kms keys versions create \
           --key DATA_KEY_NAME \
           --keyring DATA_KEY_RING \
           --location LOCATION \
           **--external-key-uri " EKM_URI"** \
           --primary \
           --project PROJECT_ID
             

  4. Grant permissions to the Apigee service agent using the following command:  

         
         gcloud kms keys add-iam-policy-binding DATA_KEY_NAME \
               --location LOCATION \
               --keyring DATA_KEY_RING \
               **--member serviceAccount:service-$(gcloud projects describe $project --format="value(projectNumber)")@gcp-sa-apigee.iam.gserviceaccount.com \
               --role roles/cloudkms.cryptoKeyEncrypterDecrypter** \
               --project PROJECT_ID
             




Where:

  * DATA_KEY_RING: The name of the control plane, API consumer data, runtime database, or runtime disk key ring.
  * DATA_KEY_NAME: The name of the control plane, API consumer data, runtime database, or runtime disk key.
  * LOCATION: The Cloud KMS location of the key ring. Set this value as follows: 
    * For Control plane encryption key, set to one of the following multi-region keys: `us` or `europe`.
    * For API consumer data encryption key, runtime database encryption key, and runtime disk encryption key, set to one of the following single-region keys: `europe-*` or `us-*`. For example, `europe-west1`, `us-central1`, and so on.
  * EKM_URI: The EKM URI.
  * PROJECT_ID: The Google Cloud project ID.



## Configure the gcloud CLI to use the regional endpoint (Optional)

You can manage your Apigee organization using the gcloud CLI. For most organizations, the gcloud CLI automatically detects the appropriate regional endpoint. This works seamlessly if you Apigee organization name matches the Google Cloud project name.

In some cases, however, the names might not match. For example, if you migrated the Apigee organization from one Google Cloud project to another, the names of the Apigee organization and the Google Cloud project where it resides might be different. In this case, you'll need to do one of the following when using the gcloud CLI: 

  * Pass the `--organization` flag with each gcloud CLI command to specify the target Apigee organization. 
  * Configure the gcloud CLI to override the Apigee endpoint and force all commands to use the new regional endpoint. 

For example, to use the US regional endpoint the gcloud CLI command is as follows:  
  
`gcloud config set api_endpoint_overrides/apigee https://apigee.us.rep.googleapis.com/`




## View the control plane location for an organization

If you have already provisioned your organization (PROJECT_ID) for use with data residency, you can use the [ getProjectMapping API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/getProjectMapping) to view the control plane location associated with a project by performing the following steps:

  1. Authorize [gcloud](https://docs.cloud.google.com/sdk/docs) to access the Cloud Platform with your Google user credentials: 
         
         gcloud auth login

  2. Call the getProjectMapping API. 

Since the information being accessed is metadata and not customer core content, you can use the global or regional endpoint to call the API. The following command uses the global endpoint:
         
         curl -X GET https://apigee.googleapis.com/v1/organizations/PROJECT_ID:getProjectMapping \
             -H "Authorization: Bearer $(gcloud auth print-access-token)"

Where PROJECT_ID is your Apigee organization name.

The following provides an example of the response:
         
         {
           "organization": "my-project",
           "projectIds": [
             "my-project"
           ],
           "projectId": "my-project"
           **"location": "us"**
         }




## Migrate an Apigee organization to support advanced data residency

To migrate an existing Apigee organization that supports data residency at rest to support advanced data residency, do the following:

  1. Move the Google Cloud project where Apigee is provisioned to an Assured Workload folder. For more information, see [Migrate a workload](https://docs.cloud.google.com/assured-workloads/docs/migrate-workload). 
  2. If you created your Apigee organization before advanced data residency was generally available, you'll need to reconfigure your global networking resources to migrate them to within the required jurisdiction. Otherwise, you can skip this step. 

**Note:** You can't migrate a global Apigee organization. You'll need to create a new Apigee organization in the Assured Workload folder. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
