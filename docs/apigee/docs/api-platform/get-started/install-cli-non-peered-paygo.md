---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo/
title: Provision a paid org without VPC peering \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:46.368283+00:00
---

# Provision a paid org without VPC peering  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-non-peered-paygo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provision a paid org without VPC peering Stay organized with collections  Save and categorize content based on your preferences. 

Provision a paid org without VPC peering

 _This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document describes how to install and configure Apigee from the command line [without VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options). These steps apply to both Subscription and Pay-as-you-go pricing models for paid organizations with or without [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) enabled.

**Note:** We also support using [Terraform](https://www.terraform.io/) to provision Apigee. See [Terraform overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview).**Note:** If your project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints), not every feature in Apigee utilizes CMEK for encryption of sensitive data. See [ Using organization policy constraints in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies) for a description of how Apigee handles organization policy constraints and see [ Organization policy constraints](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts#organization-policy-constraint) for a description of which Apigee features are currently CMEK-compliant.  See also [Provisioning options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro#provisioning-options). **Important** : These steps are for the **non-VPC peering** setup. If you want to use the VPC peering setup, see [Command line provisioning with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli). If you are unsure which to use, see [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

## Limitations

The non-VPC peering installation option described in this document has some limitations: 

  * [ VPC Service Controls](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) are not supported.



For a complete list of features and networking approaches that are and are not supported for non-VPC peering, see [How to choose a networking option](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options#how-to-choose-a-networking-option). 

## Summary of steps

The provisioning steps are as follows:

  * Step 1: Define environment variables: Set up `gcloud` and define environment variables. The Google Cloud CLI manages authentication, local configuration, developer workflow,and interactions with the Google Cloud APIs. 
  * Step 2: Enable APIs: Apigee requires you to enable several Google Cloud APIs. 
  * Step 3: Create the Apigee service identity: This [service account](https://cloud.google.com/run/docs/securing/service-identity) is used by the [ Google Cloud client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries) to authenticate with Google Cloud APIs. 
  * Step 4: Create an organization: An Apigee organization (sometimes referred to as an org) is the top-level container in Apigee. It includes all of your environments and environment groups, users, API proxies, and related resources. 
  * Step 5: Create a runtime instance: An instance, or runtime is where your project and related services are stored; it provides the user-facing endpoint for your services. 
  * Step 6: Create an environment: An API proxy must be deployed to an environment, and added to an environment group, before the APIs it exposes are accessible over the network. 
  * Step 7: Configure routing: Allow external access or internal only access to your API. 
  * Step 8: Deploy a sample proxy: Test the provisioning by deploying and calling an API proxy. 



## Step 1: Define environment variables

Set up `gcloud` and define environment variables for use in later steps:

  1. Be sure you have completed the setup requirements listed in [ Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites). 
  2. You must have the Cloud SDK installed. If you need to install it, see [ Installing Cloud SDK](https://cloud.google.com/sdk/docs/install).
  3. Initialize the Cloud SDK, as described in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize), or otherwise ensure that the Google Cloud project you created in [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites) is the default project for `gcloud`. 
  4. Define the following environment variables in your command terminal. Select the tab that corresponds to the type of organization you need: **No data residency** or with [ **Data residency**](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts): **Tip:** Save your environment variables in a text file so that you can easily restore them if needed.

### No data residency
         
         AUTH="$(gcloud auth print-access-token)"
         PROJECT_ID="YOUR_PROJECT_ID"
         PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
         RUNTIME_LOCATION="YOUR_RUNTIME_LOCATION"
         ANALYTICS_REGION="YOUR_ANALYTICS_REGION"
         BILLING_TYPE="YOUR_BILLING_TYPE"

**Note** : If you are provisioning a new Apigee organization within a Google Cloud project with a [resource location constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) applied in an organization policy, confirm that the location constraint is set to `global`. Because the Apigee control plane is a global entity by default, provisioning will fail if a constraint other than `global` is applied. For more information, see [Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). 

Where:

     * **AUTH** defines the `Authentication` header with a bearer token. You will use this header when calling Apigee APIs. Note that the token expires after a period of time and when it does, you can simply regenerate it using the same command. For more information, see the reference page for the [ print-access-token command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token). 
     * **PROJECT_ID** is the Cloud project ID that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites). 
     * **PROJECT_NUMBER** is the Cloud project number that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites). 
     * **RUNTIME_LOCATION** is the physical location where the Apigee instance you will create later is located. For a list of available runtime locations, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

**Note:** For `**RUNTIME_LOCATION**`, be sure to use a _**region**_ name and not a zone name. For example, `us-west1` is a region name, while `us-west1-a` is a zone in the region. See also [ Identifying a region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#identifying_a_region_or_zone). 
     * **ANALYTICS_REGION** is the physical location at which Apigee analytics data will be stored. For a list of available Apigee API Analytics regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

Both **RUNTIME_LOCATION** and **ANALYTICS_REGION** can be the same region, but they do not have to be the same.

     * **BILLING_TYPE** is the billing type for the organization you create. Valid values are:

       * `PAYG` for [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-entitlements) organizations.
       * `SUBSCRIPTION` for [Subscription](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) organizations.

### Data residency
    
    **AUTH** ="$(gcloud auth print-access-token)"
    **PROJECT_ID** ="YOUR_PROJECT_ID"
    **PROJECT_NUMBER** =$(gcloud projects describe $PROJECT_ID --format="value(projectNumber)")
    **RUNTIME_LOCATION** ="YOUR_RUNTIME_LOCATION"
    **CONTROL_PLANE_LOCATION** ="YOUR_CONTROL_PLANE_LOCATION"
    **CONSUMER_DATA_REGION** ="YOUR_CONSUMER_DATA_REGION"
    **BILLING_TYPE** ="YOUR_BILLING_TYPE"

**Important:** When using data residency, the control plane location is the containing region. All other regions must be within the control plane location; when the control plane location is `us`, the consumer data region and the runtime location must also be within `us`. For example, `us-west1` is acceptable, where `europe-west1` is not. 

Where:

     * **AUTH** defines the `Authentication` header with a bearer token. You will use this header when calling Apigee APIs. Note that the token expires after a period of time and when it does, you can simply regenerate it using the same command. For more information, see the reference page for the [ print-access-token command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token). 
     * **PROJECT_ID** is the Cloud project ID that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites). 
     * **PROJECT_NUMBER** is the Cloud project number that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites). 
     * **RUNTIME_LOCATION** is the physical location where the Apigee instance you will create later is located. For a list of available runtime locations, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations).

**Note:** For `**RUNTIME_LOCATION**`, be sure to use a _**region**_ name and not a zone name. For example, `us-west1` is a region name, while `us-west1-a` is a zone in the region. See also [ Identifying a region or zone](https://docs.cloud.google.com/compute/docs/regions-zones#identifying_a_region_or_zone).  The runtime location must be within the control plane location. 
     * **CONTROL_PLANE_LOCATION** is the physical location at which Apigee control plane data will be stored. For a list of available control plane locations, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#control-plane-location). 
     * **CONSUMER_DATA_REGION** is a sub-region of the control plane region. You must specify both the CONTROL_PLANE_LOCATION and the CONSUMER_DATA_REGION. For a list of available consumer data regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#consumer-data-region). 
     * **BILLING_TYPE** is the billing type for the organization you create. Valid values are:

       * `PAYG` for [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-entitlements) organizations.
       * `SUBSCRIPTION` for [Subscription](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) organizations.

  5. (Optional) Check your work by echoing the values you just set. Note that when you want to use a variable in your commands, precede the variable's name with a dollar sign (**$**). 

### No data residency
         
         echo **$AUTH**
         echo **$PROJECT_ID**
         echo $PROJECT_NUMBER
         echo $RUNTIME_LOCATION
         echo $ANALYTICS_REGION
         echo $BILLING_TYPE
         

The responses to your `echo` commands should look something like the following:
         
         YOUR_TOKEN
         my-cloud-project
         1234567890
         us-west1
         us-west1
         SUBSCRIPTION
         

### Data residency
         
         echo **$AUTH**
         echo **$PROJECT_ID**
         echo **$PROJECT_NUMBER**
         echo **$RUNTIME_LOCATION**
         echo **$CONTROL_PLANE_LOCATION**
         echo **$CONSUMER_DATA_REGION**
         echo $BILLING_TYPE
         

The responses to your `echo` commands should look something like the following:
         
         YOUR_TOKEN
         my-cloud-project
         1234567890
         us-west1
         us
         us-west1
         SUBSCRIPTION
         




## Step 2: Enable APIs

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ API enablement permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#api-enablement-permissions). 

  1. Apigee requires you to enable several Google Cloud APIs. Enable them by executing the following [`services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command:
         
         gcloud services enable apigee.googleapis.com \
             apihub.googleapis.com \
             compute.googleapis.com \
             cloudkms.googleapis.com --project=**$PROJECT_ID**

  2. (Optional) To check your work, use the [`services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command to show all the enabled APIs:
         
         gcloud services list

The response shows all enabled services, including the APIs that you just enabled. 




## Step 3: Create the Apigee service identity

**Warning:** [Service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) are special accounts required by Apigee to provision your runtime instances. Deleting service accounts will render your runtime instances unusable. 

  1. Create the Apigee [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity):
         
         gcloud beta services identity create --service=apigee.googleapis.com \
           --project=$PROJECT_ID

  2. Verify that the agent was successfully created. The response should show the name of the agent in the following format: `service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com`. for example: 
         
         Service identity created: service-1234567890@gcp-sa-apigee.iam.gserviceaccount.com




## Step 4: Create an organization

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See:

  * [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles)
  * [ Provisioning wizard permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#provisioning-wizard-permissions)
  * [ Organization creation permissions (paid org)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#organizationcreationpermissionspaid).



Before you can create an organization, you must create a runtime database encryption key ring and key (see step 1) and, if you are using [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), control plane encryption key rings and keys (see step 2). These [ Cloud KMS](https://docs.cloud.google.com/kms/docs#docs) keys encrypt data that is stored and replicated across runtime and control plane locations. Apigee uses these entities to encrypt application data such as KVMs, cache, and client secrets, which is then stored in the database. For more information, see [ About the Apigee encryption keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys). 

  1. Create a runtime database encryption key ring and key.

     1. Define an environment variable for the location of your runtime database encryption ring and key. This helps ensure consistency when you create them and makes it easier for you to follow along in the documentation.

The value is the physical location where your runtime database encryption key ring and key are stored.

### Single region

**Single region configurations** (in which you have just one instance in one region): Choose from the supported [KMS regional locations](https://docs.cloud.google.com/kms/docs/locations#regional).

For example:
            
            **RUNTIMEDBKEY_LOCATION** =YOUR_RUNTIMEDBKEY_LOCATION

The value can be the same as your $RUNTIME_LOCATION (also a region) but it does not have to be. However, there may be a performance benefit if they are the same.

### Multi-region

**Multi-region configurations:** Choose from the supported [multi-regional locations](https://docs.cloud.google.com/kms/docs/locations#multi_regional) (such as `us` or `europe`) or [dual-regional locations](https://docs.cloud.google.com/kms/docs/locations#dual_regional).

For example:
            
            **RUNTIMEDBKEY_LOCATION** =YOUR_RUNTIMEDBKEY_LOCATION

We recommend that if you have a multi-region configuration in the US, use `us` for your location if possible. Otherwise, use `nam4`.

     2. Define environment variables for database key rings and key names. 

The key ring's name must be unique to your organization. If you create a second or subsequent region, the name cannot be the same as other key rings' names.
            
            **RUNTIMEDB_KEY_RING_NAME** =YOUR_DB_KEY_RING_NAME
            **RUNTIMEDB_KEY_NAME** =YOUR_DB_KEY_NAME

     3. (Optional) Check your work by echoing the values you just set. Remember that when you want to use a variable in your commands, precede the variable's name with a dollar sign (**$**). 
            
            echo **$RUNTIMEDBKEY_LOCATION**
            echo **$RUNTIMEDB_KEY_RING_NAME**
            echo **$RUNTIMEDB_KEY_NAME**

     4. Create a new key ring: 
            
            gcloud kms keyrings create **$RUNTIMEDB_KEY_RING_NAME** \
              --location $RUNTIMEDBKEY_LOCATION --project **$PROJECT_ID**

The Apigee runtime database encryption key's location supports all Cloud KMS locations that support [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) and [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm).

     5. Create a key:
            
            gcloud kms keys create **$RUNTIMEDB_KEY_NAME** \
              --keyring **$RUNTIMEDB_KEY_RING_NAME** \
              --location $RUNTIMEDBKEY_LOCATION \
              --purpose "encryption" \
              --project **$PROJECT_ID**

This command creates the key and adds it to the key ring.

Get the key ID:
            
            gcloud kms keys list \
              --location=**$RUNTIMEDBKEY_LOCATION** \
              --keyring=**$RUNTIMEDB_KEY_RING_NAME** \
              --project=**$PROJECT_ID**

The key ID has the following syntax (similar to a file path):
            
            projects/PROJECT_ID/locations/RUNTIMEDBKEY_LOCATION/keyRings/RUNTIMEDB_KEY_RING_NAME/cryptoKeys/RUNTIMEDB_KEY_NAME

     6. Put the key ID in an environment variable. You will use this variable in a later command:
            
            **RUNTIMEDB_KEY_ID** =YOUR_RUNTIMEDB_KEY_ID

     7. Grant access for the Apigee Service Agent to use the new key:
            
            gcloud kms keys add-iam-policy-binding **$RUNTIMEDB_KEY_NAME** \
              --location **$RUNTIMEDBKEY_LOCATION** \
              --keyring **$RUNTIMEDB_KEY_RING_NAME** \
              --member serviceAccount:service-**$PROJECT_NUMBER** @gcp-sa-apigee.iam.gserviceaccount.com \
              --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project **$PROJECT_ID**

This command binds the key to the Apigee Service Agent.

On successful completion of this request, `gcloud` responds with something similar to the following:
            
            Updated IAM policy for key [runtime].
            bindings:
            - members:
              - serviceAccount:service-1234567890@gcp-sa-apigee.iam.gserviceaccount.com
              role: roles/cloudkms.cryptoKeyEncrypterDecrypter
            etag: BwWqgEuCuwk=
            version: 1

If you get an error like the following:
            
            INVALID_ARGUMENT: Role roles/cloudkms.cryptokms.cryptoKeyEncrypterDecrypter is not supported for this resource.

Be sure that you used the project _number_ and not the project name in the service account email address.

  2. If you are using [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), create a control plane encryption key ring and key. If you are not using data residency, go to step 3. **Note** : This step is only required if you selected `us (multiple regions in us)` or `eu (multiple regions in European Union)` as your control plane hosting jurisdiction. If you selected another region, go to step 3.

Perform the following steps to create a control plane encryption key ring and key. 

     1. Define an environment variable for the location of your control plane database encryption ring and key: 
            
            **CONTROL_PLANE_LOCATION** =YOUR_CONTROL_PLANE_LOCATION
            **CONSUMER_DATA_REGION** =YOUR_CONSUMER_DATA_REGION

Where:

        * **CONTROL_PLANE_LOCATION** is the physical location at which Apigee control plane data will be stored. For a list of available control plane locations, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#control-plane-location). 
        * **CONSUMER_DATA_REGION** is a sub-region of the control plane region. You must specify both the CONTROL_PLANE_LOCATION and the CONSUMER_DATA_REGION. For a list of available consumer data regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#consumer-data-region). 
     2. Define environment variables for control plane database key rings and key names.

The key ring's name must be unique to your organization.
            
            **CONTROL_PLANE_KEY_RING_NAME** =YOUR_CONTROL_PLANE_KEY_RING_NAME
            **CONTROL_PLANE_KEY_NAME** =YOUR_CONTROL_PLANE_KEY_NAME
            **CONSUMER_DATA_KEY_RING_NAME** =YOUR_CONSUMER_DATA_KEY_RING_NAME
            **CONSUMER_DATA_KEY_NAME** =YOUR_CONSUMER_DATA_REGION_KEY_NAME

Where:

        * **CONTROL_PLANE_KEY_RING_NAME** is the name of the key ring you will use to identify your control plane encryption [key ring](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_rings).
        * **CONTROL_PLANE_KEY_NAME** is the name of the key you will use to identify your control plane [encryption key](https://docs.cloud.google.com/kms/docs/cmek#cmek).
        * **CONSUMER_DATA_KEY_RING_NAME** is the name of the key ring you will use to identify your consumer data region encryption [key ring](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_rings).
        * **CONSUMER_DATA_KEY_NAME** is the name of the key you will use to identify your consumer data region [encryption key](https://docs.cloud.google.com/kms/docs/cmek#cmek).
     3. Create a new key ring: 
            
            gcloud kms keyrings create **$CONTROL_PLANE_KEY_RING_NAME** \
              --location **$CONTROL_PLANE_LOCATION** \
              --project **$PROJECT_ID**
            
            gcloud kms keyrings create **$CONSUMER_DATA_KEY_RING_NAME** \
              --location **$CONSUMER_DATA_REGION** \
              --project **$PROJECT_ID**

     4. Create a key: 
            
            gcloud kms keys create **$CONTROL_PLANE_KEY_NAME** \
              --keyring **$CONTROL_PLANE_KEY_RING_NAME** \
              --location **$CONTROL_PLANE_LOCATION** \
              --purpose "encryption" \
              --project **$PROJECT_ID**
            
            gcloud kms keys create **$CONSUMER_DATA_KEY_NAME** \
              --keyring **$CONSUMER_DATA_KEY_RING_NAME** \
              --location **$CONSUMER_DATA_REGION** \
              --purpose "encryption" \
              --project **$PROJECT_ID**

This command creates the key and adds it to the key ring.

Get the key ID:
            
            gcloud kms keys list \
            --location=**$CONTROL_PLANE_LOCATION** \
            --keyring=**$CONTROL_PLANE_KEY_RING_NAME** \
            --project=**$PROJECT_ID**
            
            gcloud kms keys list \
            --location=**$CONSUMER_DATA_REGION** \
            --keyring=**$CONSUMER_DATA_KEY_RING_NAME** \
            --project=**$PROJECT_ID**

The key ID has the following syntax (similar to a file path):
            
            projects/PROJECT_ID/locations/CONTROL_PLANE_LOCATION/keyRings/CONTROL_PLANE_KEY_RING_NAME/cryptoKeys/CONTROL_PLANE_KEY_NAME
            
            projects/PROJECT_ID/locations/CONSUMER_DATA_REGION/keyRings/CONSUMER_DATA_KEY_RING_NAME/cryptoKeys/CONSUMER_DATA_KEY_NAME

     5. Put the key ID in an environment variable. You will use this variable in a later command: 
            
            **CONTROL_PLANE_KEY_ID** =YOUR_CONTROL_PLANE_KEY_ID
            
            
            **CONSUMER_DATA_KEY_ID** =YOUR_CONSUMER_DATA_KEY_ID

     6. Grant access for the Apigee Service Agent to use the new key: 
            
            gcloud kms keys add-iam-policy-binding **$CONTROL_PLANE_KEY_NAME** \
              --location **$CONTROL_PLANE_LOCATION** \
              --keyring **$CONTROL_PLANE_KEY_RING_NAME** \
              --member "serviceAccount:service-**$PROJECT_NUMBER** @gcp-sa-apigee.iam.gserviceaccount.com" \
              --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project **$PROJECT_ID**
            
            
            gcloud kms keys add-iam-policy-binding **$CONSUMER_DATA_KEY_NAME** \
             --location **$CONSUMER_DATA_REGION** \
             --keyring **$CONSUMER_DATA_KEY_RING_NAME** \
             --member "serviceAccount:service-**$PROJECT_NUMBER** @gcp-sa-apigee.iam.gserviceaccount.com" \
             --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
             --project **$PROJECT_ID**
            

This command binds the key to the Apigee Service Agent. On successful completion of this request, gcloud responds with something similar to the following:
            
            Updated IAM policy for key [runtime].
            bindings:
            - members:
              - serviceAccount:service-1234567890@gcp-sa-apigee.iam.gserviceaccount.com
              role: roles/cloudkms.cryptoKeyEncrypterDecrypter
            etag: BwWqgEuCuwk=
            version: 1

If you get an error like the following:
            
            INVALID_ARGUMENT: Role roles/cloudkms.cryptokms.cryptoKeyEncrypterDecrypter is not supported for this resource.

Be sure that you used the project number and not the project name in the service account email address.

See also: [ CMEK troubleshooting](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts#cmek-troubleshooting). 

  3. Create the organization by sending the following request to the Apigee [organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations):

### No data residency
         
         curl "https://apigee.googleapis.com/v1/organizations?parent=projects/$PROJECT_ID"  \
           -H "Authorization: Bearer **$AUTH** " \
           -X POST \
           -H "Content-Type:application/json" \
           -d '{
             "name":"'"**$PROJECT_ID** "'",
             "analyticsRegion":"'"$ANALYTICS_REGION"'",
             "runtimeType":"CLOUD",
             "billingType":"'"**$BILLING_TYPE** "'",
             "disableVpcPeering":"true",
             "runtimeDatabaseEncryptionKeyName":"'"**$RUNTIMEDB_KEY_ID** "'"
           }'

Where:

     * `-d` defines the data payload for the request. This payload must include the following: 
       * `name`: Identifies your new organization. It must be the same name as your project ID. 

       * `analyticsRegion`: Specifies the physical location where your analytics data will be stored.

       * `runtimeType`: Set this value to `CLOUD`.
       * `billingType`: Specifies the billing type of the organization created.
       * `disableVpcPeering`: Set to `true` if you do not want to use VPC peering. Default: `false`
       * `runtimeDatabaseEncryptionKeyName`: The ID of the application encryption key that you created in the previous step. Recall that the ID is structured like a file path. For example:   
`projects/PROJECT_ID/locations/YOUR_RUNTIMEDBKEY_LOCATION/keyRings/YOUR_DB_KEY_RING_NAME/cryptoKeys/YOUR_DB_KEY_NAME`

### Data residency

[ Create an organization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/create) using the API:
    
    curl "https://REGIONAL_ENDPOINT/v1/organizations?parent=projects/**$PROJECT_ID** "  \
      -H "Authorization: Bearer **$AUTH** " \
      -X POST \
      -H "Content-Type:application/json" \
      -d '{
        "name":"'"**$PROJECT_ID** "'",
        "runtimeType":"CLOUD",
        "billingType":"'"**$BILLING_TYPE** "'",
        "controlPlaneEncryptionKeyName":"'"**$CONTROL_PLANE_KEY_ID** "'",
        "apiConsumerDataLocation":"'"**$CONSUMER_DATA_REGION** "'",
        "apiConsumerDataEncryptionKeyName":"'"**$CONSUMER_DATA_KEY_ID** "'",
        "disableVpcPeering":"true",
        "runtimeDatabaseEncryptionKeyName":"'"**$RUNTIMEDB_KEY_ID** "'"
      }'

Where:

     * REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#regional-endpoint) required to support data residency
     * `-d` defines the data payload for the request. This payload must include the following: 
       * `name`: Identifies your new organization. It must be the same name as your project ID. 
       * `runtimeType`: Set this value to `CLOUD`.
       * `billingType`: Specifies the billing type of the organization created.
       * `controlPlaneEncryptionKeyName`: Is your control plane key ID.
       * `apiConsumerDataLocation`: You must also specify a sub-region for use by internal resources. See [ Data residency regions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regions) for supported values. 
       * `apiConsumerDataEncryptionKeyName`: Is your consumer data region key ID.
       * `disableVpcPeering`: Set to `true` if you do not want to use VPC peering. Default: `false`
       * `runtimeDatabaseEncryptionKeyName`: The ID of the application encryption key that you created in the previous step. Recall that the ID is structured like a file path. For example:   
`projects/your-project/locations/your_runtime_db_key_location/keyRings/your-key-ring/cryptoKeys/your-key`

After you execute this command, Apigee starts a _long-running operation_ , which can take a few minutes to complete.

If you get an error, check your use of quotation marks around the variable values in the data payload. Be sure that you have double-single-double quotes around the **$PROJECT_ID** variable, as the following example shows:
    
    "'"**$PROJECT_ID** "'"

If you use plain strings (not environment variables) for request values, you can wrap them in double quotes within the single-quoted payload string, as the following example shows:
    
    '{ "name":"my-gcp-project", ... }'

  4. Wait a few minutes.
  5. To check the status of your creation request, you can send a `GET` request to the Apigee [List organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/list), as the following example shows: 

### No data residency
         
         curl -H "Authorization: Bearer **$AUTH** " "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** "

### Data residency
         
         curl -H "Authorization: Bearer **$AUTH** " "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** "

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

If you see this response, then the organization creation has not completed yet: 
         
         {
           "error": {
             "code": 403,
             "message": "Permission denied on resource \"organizations/apigee-docs-m\" (or it may not exist)",
             "status": "PERMISSION_DENIED"
           }
         }

On success, the response object will indicate `"state": "ACTIVE"`, and you can go on to the next step. 

If Apigee returns an HTTP error response, then see [ Creating an Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install#create-org).


**Tip:** To list the Apigee organizations and associated Google Cloud projects that you have permission to access, send a `GET` request to the following endpoint using the [organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations): 

  * No data residency:
        
        curl -H "Authorization: Bearer **$AUTH** " https://apigee.googleapis.com/v1/organizations/

  * Data residency:
        
        curl -H "Authorization: Bearer **$AUTH** " https://REGIONAL_ENDPOINT/v1/organizations/

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.




Apigee returns a list of projects, as the following example shows:
    
    
    {
      "organizations": [
        {
          "organization": "my-cloud-project",
          "projectIds": [
            "my-cloud-project"
          ],
          "projectId": "my-cloud-project",
          "location": "northamerica-northeast1"
        },
        {
          "organization": "my-cloud-project-2",
          "projectIds": [
            "my-cloud-project-2"
          ],
          "projectId": "my-cloud-project-2",
          "location": "northamerica-northeast1"
        }
      ]
    }

## Step 5: Create a runtime instance

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ Runtime instance permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#runtime-instance-permissions). 

A runtime instance is where your Apigee project and related services are stored; it provides the user-facing endpoint for your services. To create a new runtime instance:

  1. Check that Apigee has finished creating your organization. You submitted a request to create a new organization in Create an Apigee organization, but you need to be sure it's done before you continue.

To do this, send the following request to the [organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations):

### No data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** "

### Data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** "

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

If the organization exists (and you have the proper permissions to view it), Apigee responds with details about it. If Apigee responds with an error, wait a couple of minutes and send the request again.

  2. Similar to the preceding task where you created an encryption key for the database, now you need to create a [ Cloud KMS](https://docs.cloud.google.com/kms/docs#docs) key used to encrypt data on the server side. To get started, define the following environment variables: 
         
         **INSTANCE_NAME** =YOUR_INSTANCE_NAME
         **RUNTIME_LOCATION** =YOUR_RUNTIME_LOCATION
         **DISK_KEY_RING_NAME** =YOUR_DISK_KEY_RING_NAME
         **DISK_KEY_NAME** =YOUR_DISK_KEY_NAME

Where:

     * **INSTANCE_NAME** : Your new instance's name. For example, `my-runtime-instance`. The name must start with a lowercase letter, can be up to 32 characters long, and can include only lowercase letters, numbers and hyphens. It cannot start or end with a hyphen and must be at least two characters long. **Tip:** Your instance name must match the following regular expression: 
           
           ^[a-z][a-z\-\d]{0,30}[a-z\d]$

     * **RUNTIME_LOCATION** is the physical place in which your cluster is hosted. Valid values are any location allowed by Compute Engine. (See [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).) This example uses `us-west1`.
     * **DISK_KEY_RING_NAME** is the name of the disk encryption key ring.
     * **DISK_KEY_NAME** is the name of the disk encryption key.
  3. Create a disk encryption key: 
     1. Create a new disk key ring: 
            
            gcloud kms keyrings create **$DISK_KEY_RING_NAME** \
              --location **$RUNTIME_LOCATION** \
              --project **$PROJECT_ID**

Your disk key ring must be set to the same location as the instance. Each instance and key ring should have its own location.

     2. Create a new disk key: 
            
            gcloud kms keys create **$DISK_KEY_NAME** \
              --keyring **$DISK_KEY_RING_NAME** \
              --location **$RUNTIME_LOCATION** \
              --purpose "encryption" \
              --project **$PROJECT_ID**

The key can be referenced by its _key path_. You can get the key path with the following command:
            
            gcloud kms keys list \
              --location=**$RUNTIME_LOCATION** \
              --keyring=**$DISK_KEY_RING_NAME** \
              --project=**$PROJECT_ID**

The key path looks something like the following:
            
            projects/_PROJECT_ID_ /locations/_RUNTIME_LOCATION_ /keyRings/my-disk-key-ring/cryptoKeys/my-disk-key

     3. Put the key path in an environment variable. You will use this variable in a later command:
            
            **DISK_KEY_ID** =YOUR_DISK_KEY_ID

For example: `DISK_KEY_ID=projects/my-project/locations/us-west1/keyRings/my-key-ring/cryptoKeys/my-key`

     4. Grant access for the Apigee Service Agent to use the new key:
            
            gcloud kms keys add-iam-policy-binding **$DISK_KEY_NAME** \
              --location **$RUNTIME_LOCATION** \
              --keyring **$DISK_KEY_RING_NAME** \
              --member serviceAccount:service-**$PROJECT_NUMBER** @gcp-sa-apigee.iam.gserviceaccount.com \
              --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
              --project **$PROJECT_ID**

This command binds the key to the Apigee Service Agent.

For more information, see [About the Apigee encryption keys](https://docs.cloud.google.com/apigee/docs/api-platform/security/encryption-keys).

  4. Create a new runtime instance for your project by sending a `POST` request to the Apigee [Instances API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances): 

### No data residency
         
         curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances" \
           -X POST -H "Authorization: Bearer **$AUTH** " \
           -H "Content-Type:application/json" \
           -d '{
             "name":"'"**$INSTANCE_NAME** "'",
             "location":"'"$RUNTIME_LOCATION"'",
             "diskEncryptionKeyName":"'"**$DISK_KEY_ID** "'",
             "consumerAcceptList":["'"**$PROJECT_ID** "'"]
           }'

### Data residency
         
         curl "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances" \
           -X POST -H "Authorization: Bearer **$AUTH** " \
           -H "Content-Type:application/json" \
           -d '{
             "name":"'"**$INSTANCE_NAME** "'",
             "location":"'"$RUNTIME_LOCATION"'",
             "diskEncryptionKeyName":"'"**$DISK_KEY_ID** "'",
             "consumerAcceptList":["'"**$PROJECT_ID** "'"]
           }'

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

Where: 

     * `consumerAcceptList` (Optional) Specifies a list of Google Cloud project IDs that can privately connect to the Apigee VPC's [ service attachment](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments). Service attachment is an entity used with Google Cloud [ Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to allow service producers (in this case, Apigee) to expose services to consumers (in this case, one or more Cloud projects that you own). By default, we use the Cloud project that is already associated with your Apigee organization. For example: `"consumerAcceptList": ["project1", "project2", "project3"]`

Note that you can also set and change the list of accepted projects in the Instance UI. For details, see [ Managing instances](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances). 

This request can take up to 20 minutes to complete because Apigee must create and launch a new Kubernetes cluster, install the Apigee resources on that cluster, and set up load balancing.

If Apigee returns an error, see [ Creating a new instance](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install#create-instance).

  5. To check the status of your runtime instance creation request, execute the following command. When the state is **ACTIVE** , you can go on to the next step.

### No data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances/**$INSTANCE_NAME** "

### Data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/$PROJECT_ID/instances/**$INSTANCE_NAME** "

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.




## Step 6: Create an environment

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See: 

  * [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles)
  * [Provisioning wizard permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#provisioning-wizard-permissions)



To create an environment and attach it to the runtime on the command line:

  1. Define environment variables to use in this section.

For a Pay-as-you-go environment, create these variables:
         
         **ENVIRONMENT_NAME** ="YOUR_ENV_NAME"
         **ENVIRONMENT_TYPE** ="YOUR_ENV_TYPE"
         **ENV_GROUP_NAME** ="YOUR_ENV_GROUP_NAME"
         **ENV_GROUP_HOSTNAME** ="YOUR_ENV_GROUP_HOSTNAME"

Where:

     * `**ENVIRONMENT_NAME**` is a string name. For example: `test`
     * `**ENVIRONMENT_TYPE**` is the [environment type](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types) for this environment and is only applicable for [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) users, who must specify one of these values: `BASE`, `INTERMEDIATE`, or `COMPREHENSIVE`. Other users should omit the environment type.
     * `**ENV_GROUP_NAME**` is a string name. For example: `test-group`
     * `**ENV_GROUP_HOSTNAME**` is a valid domain host name. For example: `foo.example.com`
  2. Create a new environment with the [Environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments). 

For a new [Pay-as-you-go environment](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-nodes), use the following command:

### No data residency
         
         curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments" \
             -H "Authorization: Bearer **$AUTH** " \
             -X POST \
             -H "Content-Type:application/json" \
             -d '{
               "name":"'"**$ENVIRONMENT_NAME** "'",
               "type":"'"**$ENVIRONMENT_TYPE** "'"
           }'

### Data residency
         
         curl "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /environments" \
             -H "Authorization: Bearer **$AUTH** " \
             -X POST \
             -H "Content-Type:application/json" \
             -d '{
               "name":"'"**$ENVIRONMENT_NAME** "'",
               "type":"'"**$ENVIRONMENT_TYPE** "'"
           }'

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

Apigee creates a new environment.

  3. Before you continue, check that Apigee finished creating the new environment by calling the [Environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments): 

### No data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments"

### Data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /environments"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

Apigee responds with a list of available environments; for example, if your environment name is `test`, Apigee responds with the following:
         
         [
           "test"
         ]

**Tip:** You can check the status of a specific environment by sending a command like the following: 
     * No data residency:
           
           curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/environments/**$ENVIRONMENT_NAME** "

     * Data residency:
           
           curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /environments/**$ENVIRONMENT_NAME** "

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

Apigee responds with details about that environment only; for example:
    
    {
      "name": "my-cloud-project",
      "createdAt": "1592589683002",
      "lastModifiedAt": "1592589683002",
      "state": "ACTIVE"
    }

  4. Attach the new environment to the runtime instance: 

### No data residency
         
         curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances/**$INSTANCE_NAME** /attachments" \
             -X POST -H "Authorization: Bearer **$AUTH** " \
             -H "content-type:application/json" \
             -d '{
               "environment":"'"**$ENVIRONMENT_NAME** "'"
             }'

### Data residency
         
         curl "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances/**$INSTANCE_NAME** /attachments" \
             -X POST -H "Authorization: Bearer **$AUTH** " \
             -H "content-type:application/json" \
             -d '{
               "environment":"'"**$ENVIRONMENT_NAME** "'"
             }'

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

This operation can take several minutes to complete. To check to see if the attachment is completed, execute this command:

### No data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
           "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances/**$INSTANCE_NAME** /attachments"

### Data residency
         
         curl -i -H "Authorization: Bearer $AUTH" \
           "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances/**$INSTANCE_NAME** /attachments"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

When you see output like the following, you can go to the next step: 
         
         {
           "attachments": [
             {
               "name": "ed628782-c893-4095-b71c-f4731805290a",
               "environment": "test",
               "createdAt": "1641604447542"
             }
           ]
         }

  5. Create a new environment group using the following command. For more information, see [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview): 

### No data residency
         
         curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/envgroups" \
             -H "Authorization: Bearer **$AUTH** " \
             -X POST \
             -H "Content-Type:application/json" \
             -d '{
               "name": "'"**$ENV_GROUP_NAME** "'",
               "hostnames":["'"**$ENV_GROUP_HOSTNAME** "'"]
           }'

### Data residency
         
         curl "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /envgroups" \
             -H "Authorization: Bearer **$AUTH** " \
             -X POST \
             -H "Content-Type:application/json" \
             -d '{
               "name": "'"**$ENV_GROUP_NAME** "'",
               "hostnames":["'"**$ENV_GROUP_HOSTNAME** "'"]
           }'

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

**Tip:** Attaching an environment _to the group_ just makes the proxies in that environment routable via the hostnames in the group.
  6. Wait for the operation to complete. You can check the status of your new group using a request like the following: 

### No data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/envgroups/$ENV_GROUP_NAME"

### Data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /envgroups/**$ENV_GROUP_NAME"**

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

  7. Attach the new environment to the new environment group with the following command: 

### No data residency
         
         curl "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /envgroups/**$ENV_GROUP_NAME** /attachments" \
             -X POST \
             -H "Authorization: Bearer **$AUTH** " \
             -H "content-type:application/json" \
             -d '{
               "environment":"'"**$ENVIRONMENT_NAME** "'"
           }'

### Data residency
         
         curl "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /envgroups/**$ENV_GROUP_NAME** /attachments" \
             -X POST \
             -H "Authorization: Bearer **$AUTH** " \
             -H "content-type:application/json" \
             -d '{
               "environment":"'"**$ENVIRONMENT_NAME** "'"
           }'

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

  8. To check the status of the operation, call this API: 

### No data residency
         
         curl -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /envgroups/**$ENV_GROUP_NAME** /attachments"

### Data residency
         
         curl -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /envgroups/**$ENV_GROUP_NAME** /attachments"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.




## Step 7: Configure routing

In this step, you configure how client applications communicate with Apigee. Client to Apigee traffic is also called "northbound" traffic. Northbound configuration options include the following. Go to the configuration option you wish to use and perform the steps for that option:

Access type | Description of the configuration and deployment process  
---|---  
Internal with Private Service Connect (New) |  Allow only internal access to your API proxies from any of your Google Cloud projects using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). Private Service Connect enables private connection between a service producer (Apigee) and a service consumer (the peered VPC project and/or one or more other Cloud projects that you control). With this method, requests pass through either a service endpoint or a regional internal load balancer to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments). This configuration lets your internal clients send Apigee API proxy requests from any network-enabled machine.  
External with Private Service Connect (New) |  Allow external access to your API proxies using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). Use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to enable private connection between a service producer (Apigee) and a service consumer (the peered VPC project and/or one or more other Cloud projects that you control). With this method, requests pass through either a global external load balancer or a regional external load balancer to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments). This configuration lets you send Apigee API proxy requests from any network-enabled machine. **Important:** Recommended routing access configuration if you are using [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). To meet data residency requirements, use Private Service Connect with a **regional external load balancer** and a **self-managed SSL certificate**.  
  
Each of these routing approaches is presented in the instructions below.

### Internal routing (Private Service Connect)

This section explains how to allow only internal access to your API proxies from any of your Google Cloud projects using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).

You have two options for configuring internal access with Private Service Connect:

  * **Service endpoint** : Requests pass through a service endpoint to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments).
  * **Internal regional load balancer** : Requests pass through a regional internal HTTP(S) load balancer. See also [Global vs regional load balancing](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#global-regional). 



Select the tab below for your configuration choice and follow the steps:

### Service endpoint

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

#### Create a Private Service Connect service endpoint for the service attachment

  1. Get the service attachment from the instance you created previously: 

### No data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
         "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances"

### Data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
         "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

In the following sample output, the `serviceAttachment` value is shown in bold type: 
         
         {
           "instances": [
             {
               "name": "us-west1",
               "location": "us-west1",
               "createdAt": "1645731488019",
               "lastModifiedAt": "1646504754219",
               "diskEncryptionKeyName": "projects/my-project/locations/us-west1/keyRings/us-west1/cryptoKeys/dek",
               "state": "ACTIVE",
               "runtimeVersion": "1-7-0-20220228-190814",
               "consumerAcceptList": [
                 "my-project"
               ],
               "serviceAttachment": "**projects/bfac74a67a320c43a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw1** "
             }
           ]
         }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  2. Create a Private Service Connect Service Endpoint that points to the service attachment that you obtained from the instance response body in the previous step, as explained in [Create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint). 
  3. Apigee provisioning is complete. Go to Deploy a sample proxy. 



### Internal regional LB

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

**Restrictions:** Note the following restrictions for Private Service Connect configuration: 

  * [Global external HTTP(S) load balancer (classic)](https://docs.cloud.google.com/load-balancing/docs/https) is not supported for this configuration.
  * Limits apply to the number of Google Cloud projects that can connect to an Apigee instance through Private Service Connect, and to the number of Private Service Connect NEG connections that you can have per project. For details, see [ Private Service Connect Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#private-service-connect-psc).
  * If a Google cloud project is removed from `consumerAcceptList`, the existing Private Service Connect NEGs in that removed project will continue to work. However, any new NEGs will be rejected. You must delete existing NEGs if you remove their associated projects from the `consumerAcceptList`. Alternatively, you can recreate the Apigee instance, which recreates the service attachment in the Apigee project.



#### Step 7a: Set up environment variables

The instructions in this section use environment variables to refer to repeatedly used strings. Be sure you have set the variables in [Define environment variables](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#define-variables).

In addition, set the following environment variables:

**Tip:** Save your environment variables in a text file so that you can easily restore them if needed.
    
    
    NEG_NAME=YOUR_NEG_NAME
    NETWORK_NAME=YOUR_NETWORK_NAME
    SUBNET_NAME=YOUR_SUBNET_NAME
    TARGET_SERVICE=TARGET_SERVICE_ATTACHMENT
    

Where:

  * **NEG_NAME** : a name for the network endpoint group.
  * **NETWORK_NAME** : (Optional) Name of the network in which the NEG is created. If you omit this parameter, the `default` project network is used.
  * **SUBNET_NAME** : Name of the subnet used for private connectivity to the producer. The subnet size can be small: the Private Service Connect NEG only needs one IP from the subnet. For Apigee, only one Private Service Connect NEG is needed per region. The subnet can be shared and used by VMs or other entities. If a subnet is not specified, network endpoints may belong to any subnetwork in the region where the network endpoint group is created. **Note:** If you specify the `--network` parameter,you must also specify `--subnet`.
  * **TARGET_SERVICE** : The service attachment that you want to connect to. For example: `projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7`
**Note:** The `TARGET_SERVICE` is obtained in this step.


#### Step 7b: Create a proxy-only subnet

**Note:** This is a one-time only operation. This proxy-only subnet is required only once for any Envoy-based regional load balancer. See also [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).
    
    
    gcloud compute networks subnets create testproxyonlysubnet \
    --purpose=REGIONAL_MANAGED_PROXY --role=ACTIVE --region=**$RUNTIME_REGION** --network=**$NETWORK_NAME** \
    --range=100.0.0.0/24 --project=**$PROJECT_ID**

#### Step 7c: Create a network endpoint group (NEG)

  1. Get the service attachment from the instance you created previously: 

### No data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
         "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances"

### Data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
         "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

In the following sample output, the `serviceAttachment` value is shown in bold type: 
         
         {
           "instances": [
             {
               "name": "us-west1",
               "location": "us-west1",
               "createdAt": "1645731488019",
               "lastModifiedAt": "1646504754219",
               "diskEncryptionKeyName": "projects/my-project/locations/us-west1/keyRings/us-west1/cryptoKeys/dek",
               "state": "ACTIVE",
               "runtimeVersion": "1-7-0-20220228-190814",
               "consumerAcceptList": [
                 "my-project"
               ],
               "serviceAttachment": "**projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7** "
             }
           ]
           }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  2. Create a Private Service Connect NEG that points to the service attachment that you obtained from the instance response body in the previous step. 

**Note:** The following command explicitly specifies the network and subnet to be used when creating the NEG. If these values are not specified, the default network is used. If the default network has been deleted and the network and subnet are not specified, the command will fail. 
         
         gcloud compute network-endpoint-groups create **$NEG_NAME** \
         --network-endpoint-type=private-service-connect \
         --psc-target-service=**$TARGET_SERVICE** \
         --region=**$RUNTIME_LOCATION** \
         --project=**$PROJECT_ID**
         --network=$NETWORK_NAME
         --subnet=$SUBNET_NAME
         

Where

     * **$PROJECT_ID** can be the Cloud project that is already associated with your Apigee organization, or a Cloud project included in the `consumerAcceptlist` when the Apigee runtime instance was created. 



#### Step 7d: Configure the regional internal load balancer

  1. Reserve an internal IPv4 address for the load balancer. 
         
         gcloud compute addresses create ADDRESS_NAME \
         --ip-version=IPV4 --subnet=**$SUBNET_NAME** \
         --region=**$RUNTIME_LOCATION** --project=**$PROJECT_ID**

Replace ADDRESS_NAME with a name for the IP address resource. 

Run this command to view the reserved IP address: 
         
         gcloud compute addresses describe ADDRESS_NAME \
         --format="get(address)" --region=**$RUNTIME_LOCATION** --project=**$PROJECT_ID**

  2. Create a backend service for the NEG. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
         --load-balancing-scheme=INTERNAL_MANAGED \
         --protocol=HTTPS \
         --region=**$RUNTIME_LOCATION** \
         --project=**$PROJECT_ID**

Replace BACKEND_SERVICE_NAME with the name of the backend service. 

  3. Add the NEG to the backend service: 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
         --network-endpoint-group=$NEG_NAME \
         --region=**$RUNTIME_LOCATION** \
         --project=**$PROJECT_ID**

Replace the following:

     * NEG_NAME: the name of the network endpoint group.
     * BACKEND_SERVICE_NAME with the name of the backend service.
  4. To create an HTTPS load balancer, you must have an [SSL certificate resource](https://cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. 

Use this command to create a self-managed SSL certificate resource. To create a self-managed SSL certificate, you need a local private key file and a local certificate file. If you need to create these files, see [step 1 of using self-managed SSL certificates](https://cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).

**Note:** Google-managed certificates are not supported by the internal regional load balancer.
         
         gcloud compute ssl-certificates create CERTIFICATE \
         --certificate LB_CERT \
         --private-key LB_PRIVATE_KEY
         --region=**$RUNTIME_LOCATION** --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * LB_CERT: the path to the PEM-formatted certificate file for your self-managed certificate.
     * LB_PRIVATE_KEY: the path to the PEM-formatted private key file for your self-managed certificate.
  5. Create a URL map for the load balancer.

A URL map must reference a default backend service. Set the backend service you just created as the default.
         
         gcloud compute url-maps create URL_MAP_NAME \
         --default-service=DEFAULT_BACKEND_SERVICE_NAME \
         --region=**$RUNTIME_REGION** \
         --project=**$PROJECT_ID**

Replace the following:

     * URL_MAP_NAME: a name for the URL map.
     * DEFAULT_BACKEND_SERVICE_NAME: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.
  6. Use the SSL certificate resource to create a target HTTPS proxy.
         
         gcloud compute target-https-proxies create PROXY_NAME \
         --url-map=URL_MAP_NAME \
         --ssl-certificates=CERTIFICATE \
         --region=**$RUNTIME_LOCATION** --project=**$PROJECT_ID**

Replace the following:

     * PROXY_NAME: a name for the target HTTPS proxy.
     * URL_MAP_NAME: the name of the URL map.
     * CERTIFICATE: the name of the certificate resource.
  7. Create the forwarding rule. 
         
         gcloud compute forwarding-rules create FWD_RULE \
         --load-balancing-scheme=INTERNAL_MANAGED \
         --address=ADDRESS_NAME \
         --target-https-proxy=PROXY_NAME \
         --ports=443 \
         --target-https-proxy-region=**$RUNTIME_REGION** \
         --region=**$RUNTIME_REGION** \
         --project=**$PROJECT_ID** \
         --network=$NETWORK_NAME \
         --subnet=$SUBNET_NAME
         

Replace the following:

     * FWD_RULE: a name for the forwarding rule.
     * ADDRESS_NAME: the IP address resource that you reserved to use for the forwarding rule.
     * PROXY_NAME: the name of the target HTTPS proxy.
     * **NETWORK_NAME** : (Optional) Name of the network in which the NEG is created. If you omit this parameter, the `default` project network is used.
     * **SUBNET_NAME** : Name of the subnet used for private connectivity to the producer. **Note:** If you specify the `--network` parameter,you must also specify `--subnet`.
  8. Apigee provisioning is complete. Go to Deploy a sample proxy.



### External routing (Private Service Connect)

This section describes how to configure external routing using [ Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) to allow communication between Apigee and VPCs that you control. You must do this before you can send a request from an external client to your Apigee runtime instance. 

**Important:** Recommended routing access configuration if you are using [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). To meet data residency requirements, use PSC with a **regional external load balancer** and a **self-managed SSL certificate**.

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

**Restrictions:** Note the following restrictions for Private Service Connect configuration: 

  * [Global external HTTP(S) load balancer (classic)](https://docs.cloud.google.com/load-balancing/docs/https) is not supported for this configuration.
  * Limits apply to the number of Google Cloud projects that can connect to an Apigee instance through Private Service Connect, and to the number of Private Service Connect NEG connections that you can have per project. For details, see [ Private Service Connect Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#private-service-connect-psc).
  * If a Google cloud project is removed from `consumerAcceptList`, the existing Private Service Connect NEGs in that removed project will continue to work. However, any new NEGs will be rejected. You must delete existing NEGs if you remove their associated projects from the `consumerAcceptList`. Alternatively, you can recreate the Apigee instance, which recreates the service attachment in the Apigee project.



#### Step 7b: Create a NEG and configure the load balancer

You can create a global or regional load balancer.

### Global external LB

Configure a [global external HTTP(S) load balancer](https://cloud.google.com/load-balancing/docs/https) (load balancing scheme set to `EXTERNAL_MANAGED`).

Although the Private Service Connect NEG is regional, all other load balancing components in this configuration are global.

  1. Make sure you have set the environment variables in Define environment variables.
  2. Get the service attachment from the instance you created previously: 

### No data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances"

### Data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

In the following sample output, the `serviceAttachment` value is shown in bold type: 
         
         {
           "instances": [
             {
               "name": "us-west1",
               "location": "us-west1",
               "host": "10.82.192.2",
               "port": "443",
               "createdAt": "1645731488019",
               "lastModifiedAt": "1646504754219",
               "diskEncryptionKeyName": "projects/my-project/locations/us-west1/keyRings/us-west1/cryptoKeys/dek",
               "state": "ACTIVE",
               "peeringCidrRange": "SLASH_22",
               "runtimeVersion": "1-7-0-20220228-190814",
               "ipRange": "10.82.192.0/22,10.82.196.0/28",
               "consumerAcceptList": [
                 "875609189304"
               ],
               "serviceAttachment": "**projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7** "
             }
           ]
         }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  3. Create a Private Service Connect NEG that points to the service attachment that you obtained from the instance response body in the previous step. 
         
         gcloud compute network-endpoint-groups create NEG_NAME \
             --network-endpoint-type=private-service-connect \
             --psc-target-service=TARGET_SERVICE \
             --region=**$RUNTIME_LOCATION** \
             --network=NETWORK_NAME \
             --subnet=SUBNET_NAME \
             --project=**$PROJECT_ID**
         

Replace the following:

     * NEG_NAME: a name for the network endpoint group.
     * TARGET_SERVICE: the service attachment that you want to connect to. Use the service attachment value returned by the previous command. For example: `projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7`
     * NETWORK_NAME: (Optional) Name of the network in which the NEG is created. If you omit this parameter, the `default` project network is used.
     * SUBNET_NAME: Name of the subnet used for private connectivity to the producer. The subnet size can be small: the Private Service Connect NEG only needs one IP from the subnet. For Apigee, only one Private Service Connect NEG is needed per region. The subnet can be shared and used by VMs or other entities. If a subnet is not specified, network endpoints may belong to any subnetwork in the region where the network endpoint group is created. **Note:** If you specify the `--network` parameter,you must also specify `--subnet`.
     * **$PROJECT_ID** : The Cloud project that is already associated with your Apigee organization, or a Cloud project included in the `consumerAcceptlist` when the Apigee runtime instance was created. If you haven't already, create an environment variable to hold the project ID, because it is used in most of the following commands. 
  4. Reserve a global external IPv4 address for the load balancer. 
         
         gcloud compute addresses create ADDRESS_NAME \
             --ip-version=IPV4 --global --project=**$PROJECT_ID**

Replace ADDRESS_NAME with a name for the IP address resource. 

Run this command to view the reserved IP address: 
         
         gcloud compute addresses describe ADDRESS_NAME \
             --format="get(address)" --global --project=**$PROJECT_ID**

  5. Create a backend service for the NEG. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --protocol=HTTPS \
             --global --project=**$PROJECT_ID**

Replace BACKEND_SERVICE_NAME with the name of the backend service. 

  6. Add the NEG to the backend service. 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --network-endpoint-group=NEG_NAME \
             --network-endpoint-group-region=REGION \
             --global --project=**$PROJECT_ID**

Replace the following:

     * BACKEND_SERVICE_NAME: the name of the backend service.
     * NEG_NAME: the name of the network endpoint group.
     * REGION: the region of the network endpoint group.
  7. Create a URL map for the load balancer.

A URL map must reference a default backend service. Set the backend service you just created as the default.
         
         gcloud compute url-maps create URL_MAP_NAME \
             --default-service=DEFAULT_BACKEND_SERVICE_NAME \
             --global --project=**$PROJECT_ID**

Replace the following:

     * URL_MAP_NAME: a name for the URL map.
     * DEFAULT_BACKEND_SERVICE_NAME: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.
  8. Create the target HTTPS proxy.

To create an HTTPS load balancer, you must have an [SSL certificate resource](https://cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. You can create an SSL certificate resource using either a Google-managed SSL certificate or a self-managed SSL certificate. Using Google-managed certificates is recommended because Google Cloud obtains, manages, and renews these certificates automatically. 

To create a Google-managed certificate, [you must have a domain](https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#before_you_begin). 

Use this command to create a Google-managed SSL certificate resource: 
         
         gcloud compute ssl-certificates create CERTIFICATE \
             --domains DOMAIN --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * DOMAIN: the domain name of your load balancer.

Use this command to create a self-managed SSL certificate resource. To create a self-managed SSL certificate, you need a local private key file and a local certificate file. If you need to create these files, see [step 1 of using self-managed SSL certificates](https://cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).
    
    gcloud compute ssl-certificates create CERTIFICATE \
        --certificate LB_CERT \
        --private-key LB_PRIVATE_KEY --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * LB_CERT: the path to the PEM-formatted certificate file for your self-managed certificate.
     * LB_PRIVATE_KEY: the path to the PEM-formatted private key file for your self-managed certificate.

Use the SSL certificate resource to create a target HTTPS proxy.
    
    gcloud compute target-https-proxies create PROXY_NAME \
        --url-map=URL_MAP_NAME \
        --ssl-certificates=CERTIFICATE --project=**$PROJECT_ID**

Replace the following:

     * PROXY_NAME: a name for the target HTTPS proxy.
     * URL_MAP_NAME: the name of the URL map.
     * CERTIFICATE: the name of the certificate resource.
  9. Create the forwarding rule. 
         
         gcloud compute forwarding-rules create FWD_RULE \
             --load-balancing-scheme=EXTERNAL_MANAGED \
             --network-tier=PREMIUM \
             --address=ADDRESS_NAME \
             --target-https-proxy=PROXY_NAME \
             --ports=443 \
             --global --project=**$PROJECT_ID**

Replace the following:

     * FWD_RULE: a name for the forwarding rule.
     * ADDRESS_NAME: the IP address resource that you reserved to use for the forwarding rule.
     * PROXY_NAME: the name of the target HTTPS proxy.



### Regional external LB

Configure a regional external HTTP(S) load balancer. See also [External HTTP(S) load balancer overview](https://docs.cloud.google.com/load-balancing/docs/https).

  1. Be sure you have set the variables in [Define environment variables](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#define-variables).
  2. Create a proxy-only subnet: **Note:** This is a one-time only operation. This proxy-only subnet is required only once per Google Cloud project for any Envoy-based regional load balancer. See also [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets). 
         
         gcloud compute networks subnets create SUBNET_NAME \
               --purpose=REGIONAL_MANAGED_PROXY --role=ACTIVE \
               --region=**$RUNTIME_LOCATION** --network=NETWORK_NAME \
               --range=100.0.0.0/24 --project=**$PROJECT_ID**

Replace the following:

     * SUBNET_NAME: the name of the subnet.
     * (Optional) NETWORK_NAME: Name of the network in which the subnet is created. If you omit this parameter, the default project network is used.
  3. Get the service attachment from the instance you created previously: 

### No data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /instances"

### Data residency
         
         curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

In the following sample output, the `serviceAttachment` value is shown in bold type: 
         
         {
           "instances": [
             {
               "name": "us-west1",
               "location": "us-west1",
               "host": "10.82.192.2",
               "port": "443",
               "createdAt": "1645731488019",
               "lastModifiedAt": "1646504754219",
               "diskEncryptionKeyName": "projects/my-project/locations/us-west1/keyRings/us-west1/cryptoKeys/dek",
               "state": "ACTIVE",
               "peeringCidrRange": "SLASH_22",
               "runtimeVersion": "1-7-0-20220228-190814",
               "ipRange": "10.82.192.0/22,10.82.196.0/28",
               "consumerAcceptList": [
                 "875609189304"
               ],
               "serviceAttachment": "**projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7** "
             }
           ]
         }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  4. Create a network endpoint group. 
         
         gcloud compute network-endpoint-groups create NEG_NAME \
             --network-endpoint-type=private-service-connect \
             --psc-target-service=TARGET_SERVICE \
             --region=**$RUNTIME_LOCATION** --project=**$PROJECT_ID**

Replace the following:

     * NEG_NAME: the name of the network endpoint group.
     * TARGET_SERVICE: the name of the service attachment that you want to connect to. For example: `projects/bfac7497a40c32a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw7`
  5. Create a backend service for the NEG. 
         
         gcloud compute backend-services create BACKEND_SERVICE_NAME \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --protocol=HTTPS \
           --region=**$RUNTIME_LOCATION**  \
           --project=**$PROJECT_ID**

Replace BACKEND_SERVICE_NAME with the name of the backend service. 

  6. Add the NEG to the backend service. 
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
           --network-endpoint-group=NEG_NAME \
           --region=**$RUNTIME_LOCATION**  \
           --project=**$PROJECT_ID**

Replace the following:

     * BACKEND_SERVICE_NAME: the name of the backend service.
     * NEG_NAME: the name of the network endpoint group. 
  7. Create a URL map for the load balancer.

A URL map must reference a default backend service. Set the backend service you just created as the default.
         
         gcloud compute url-maps create URL_MAP_NAME \
           --default-service=DEFAULT_BACKEND_SERVICE_NAME \
           --region=**$RUNTIME_LOCATION**  \
           --project=**$PROJECT_ID**

Replace the following:

     * URL_MAP_NAME: a name for the URL map.
     * DEFAULT_BACKEND_SERVICE_NAME: the name of the load balancer's default backend service. The default is used when no host rule matches the requested hostname.
  8. Create the target HTTPS proxy.

To create an HTTPS load balancer, you must have an [SSL certificate resource](https://cloud.google.com/load-balancing/docs/ssl-certificates) to use in the HTTPS target proxy. 

Use this command to create a self-managed SSL certificate resource. To create a self-managed SSL certificate, you need a local private key file and a local certificate file. If you need to create these files, see [step 1 of using self-managed SSL certificates](https://cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs).

**Note:** Google-managed certificates are not supported by the internal regional load balancer.
         
         gcloud compute ssl-certificates create CERTIFICATE \
           --certificate LB_CERT \
           --private-key LB_PRIVATE_KEY --region=**$RUNTIME_LOCATION** \
           --project=**$PROJECT_ID**

Replace the following:

     * CERTIFICATE: a name for the certificate.
     * LB_CERT: the path to the PEM-formatted certificate file for your self-managed certificate.
     * LB_PRIVATE_KEY: the path to the PEM-formatted private key file for your self-managed certificate.

Use the SSL certificate resource to create a target HTTPS proxy.
    
    gcloud compute target-https-proxies create PROXY_NAME \
      --url-map=URL_MAP_NAME --region=**$RUNTIME_LOCATION** \
      --ssl-certificates=CERTIFICATE --project=**$PROJECT_ID**

Replace the following:

     * PROXY_NAME: a name for the target HTTPS proxy.
     * URL_MAP_NAME: the name of the URL map.
     * CERTIFICATE: the name of the certificate resource.
  9. Reserve a regional external address for the load balancer. Note that the network tier must be set to `STANDARD`. 
         
         gcloud compute addresses create ADDRESS_NAME \
               --region=**$RUNTIME_LOCATION** --network-tier=STANDARD \
               --project=**$PROJECT_ID**

Replace ADDRESS_NAME with a name for the IP address resource. 

Run this command to view the reserved IP address: 
         
         gcloud compute addresses describe ADDRESS_NAME \
               --format="get(address)" --region=**$RUNTIME_LOCATION** \
               --project=**$PROJECT_ID**

  10. Create the forwarding rule. 
         
         gcloud compute forwarding-rules create FWD_RULE \
           --load-balancing-scheme=EXTERNAL_MANAGED \
           --network-tier=STANDARD \
           --address=ADDRESS_NAME \
           --target-https-proxy=PROXY_NAME \
           --ports=443  --region=**$RUNTIME_LOCATION** \
           --target-https-proxy-region=**$RUNTIME_LOCATION** --project=**$PROJECT_ID**

Replace the following:

     * FWD_RULE: a name for the forwarding rule.
     * ADDRESS_NAME: the IP address resource that you reserved to use for the forwarding rule.
     * PROXY_NAME: the name of the target HTTPS proxy.



Apigee provisioning is complete. Go to Deploy a sample proxy. 

## Step 8: Deploy a sample proxy

#### Permissions required for this task

Creating and deploying proxies requires a minimum set of permissions. If you have Apigee Org Admin role, you can complete this task. To learn about other roles you can employ, see [ Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles). 

Follow these steps if you completed the configuration for:

  * External routing (Private Service Connect)
  * Internal routing (Private Service Connect)



  1. Download the [ sample proxy](https://github.com/apigee/api-platform-samples/tree/master/sample-proxies/apigee-quickstart) from GitHub. The target of the proxy is the [httpbin.org](https://httpbin.org/) service, which is a commonly used public request and response service. 
  2. Upload the API proxy bundle to the runtime using the Apigee [ `apis`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis) API: 

### No data residency
         
         curl -i -X POST -H "Authorization: Bearer **$AUTH** " \
             -H "Content-Type:multipart/form-data" \
             "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/apis?name=httpbin&action=import" \
             -F 'file=@PATH_TO_ZIP_FILE/httpbin_rev1_2020_02_02.zip'

### Data residency
         
         curl -i -X POST -H "Authorization: Bearer **$AUTH** " \
             -H "Content-Type:multipart/form-data" \
             "https://REGIONAL_ENDPOINT/v1/organizations/$PROJECT_ID/apis?name=httpbin&action=import" \
             -F 'file=@PATH_TO_ZIP_FILE/httpbin_rev1_2020_02_02.zip'

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

Where PATH_TO_ZIP_FILE is the path to the directory containing the downloaded ZIP file. 

  3. [ Deploy the API Proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new#apigee-api) to the environment you created previously: 

### No data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " -X POST \
             "https://apigee.googleapis.com/v1/organizations/****$PROJECT_ID**** /environments/**$ENVIRONMENT_NAME** /apis/httpbin/revisions/1/deployments"

### Data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " -X POST \
             "https://REGIONAL_ENDPOINT/v1/organizations/****$PROJECT_ID**** /environments/**$ENVIRONMENT_NAME** /apis/httpbin/revisions/1/deployments"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

  4. Confirm the deployment completed successfully with this API call: 

### No data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /environments/**$ENVIRONMENT_NAME** /apis/httpbin/revisions/1/deployments"

### Data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /environments/**$ENVIRONMENT_NAME** /apis/httpbin/revisions/1/deployments"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

  5. Call the API proxy:

Send a request to the API proxy from any network-enabled machine by executing the following command:
         
         curl -i -H "Host: ENV_GROUP_HOSTNAME" \
             "https://ENV_GROUP_HOSTNAME/httpbin/headers"

If needed, you can use this API to get the ENV_GROUP_HOSTNAME value: 

### No data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://apigee.googleapis.com/v1/organizations/**$PROJECT_ID** /envgroups"

### Data residency
         
         curl -i -H "Authorization: Bearer **$AUTH** " \
             "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /envgroups"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

If you get an error like this: `CONNECT_CR_SRVR_HELLO:sslv3 alert handshake failure`, check to be sure the SSL certificate you created previously has been provisioned. Use this command to check the [ provisioning status](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting?&_ga=2.79964887.-1787387761.1640983931#certificate-managed-status). When the cert is provisioned, its status is `ACTIVE`. 
         
         gcloud compute ssl-certificates describe CERTIFICATE \
             --global \
             --format="get(name,managed.status, managed.Status)"

Upon success, the sample API proxy returns a response similar to this: 
         
         {
             "headers": {
               "Accept": "*/*",
               "Grpc-Trace-Bin": "AAD/8WC/I4AUSrMEch0E9yj+AYck1x9afwckAgA",
               "Host": "httpbin.org",
               "Traceparent": "00-fff160bf2380144ab304721d04f728fe-8724d71f5a7f0724-00",
               "User-Agent": "curl/7.77.0",
               "X-Amzn-Trace-Id": "Root=1-61d785ef-7613aa8a7fde7a910441fab9",
               "X-B3-Sampled": "0",
               "X-B3-Spanid": "8724d71f5a7f0724",
               "X-B3-Traceid": "fff160bf2380144ab304721d04f728fe",
               "X-Cloud-Trace-Context": "fff160bf2380144ab304721d04f728fe/9738144823944087332;o=0",
               "X-Envoy-Attempt-Count": "1"
             }
         }




For more information about deploying proxies, including additional troubleshooting information, see [ Deploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
