---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-paygo/
title: Provision a paid org with VPC peering \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:42.681380+00:00
---

# Provision a paid org with VPC peering  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli-paygo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provision a paid org with VPC peering Stay organized with collections  Save and categorize content based on your preferences. 

Provision a paid org with VPC peering

 _This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document describes how to install and configure Apigee from the command line [ with VPC peering](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options). These steps apply to both Subscription and Pay-as-you-go pricing models for paid organizations with or without [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) enabled.

**Note:** We also support using [Terraform](https://www.terraform.io/) to provision Apigee. See [Terraform overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview).**Note:** If your project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints), not every feature in Apigee utilizes CMEK for encryption of sensitive data. See [ Using organization policy constraints in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies) for a description of how Apigee handles organization policy constraints and see [ Organization policy constraints](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts#organization-policy-constraint) for a description of which Apigee features are currently CMEK-compliant. 

## Summary of steps

The provisioning steps are as follows:

  * Step 1: Define environment variables: Set up `gcloud` and define environment variables. The Google Cloud CLI manages authentication, local configuration, developer workflow,and interactions with the Google Cloud APIs. 
  * Step 2: Enable APIs: Apigee requires you to enable several Google Cloud APIs. 
  * Step 3: Create the Apigee service identity: This [service account](https://cloud.google.com/run/docs/securing/service-identity) is used by the [ Google Cloud client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries) to authenticate with Google Cloud APIs. 
  * Step 4: Configure service networking: Service networking automates the private connectivity set up (using VPC Network Peering) between your network and Apigee. 
  * Step 5: Create an organization: An Apigee organization (sometimes referred to as an org) is the top-level container in Apigee. It includes all of your environments and environment groups, users, API proxies, and related resources. 
  * Step 6: Create a runtime instance: An instance, or runtime is where your project and related services are stored; it provides the user-facing endpoint for your services. 
  * Step 7: Create an environment: An API proxy must be deployed to an environment, and added to an environment group, before the APIs it exposes are accessible over the network. 
  * Step 8: Configure routing: Allow external access or internal only access to your API. 
  * Step 9: Deploy a sample proxy: Test the provisioning by deploying and calling an API proxy. 



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
             servicenetworking.googleapis.com \
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




## Step 4: Configure service networking

In this step, you allocate a pair of IP Address Ranges (a /22 and /28 CIDR range) to Apigee and perform the VPC peering between your network and Apigee's network. Each Apigee instance requires a non-overlapping CIDR range of /22 and /28. The Apigee runtime plane is assigned IP addresses from within this CIDR range. As a result, it's important that the range is reserved for Apigee and not used by other applications in your VPC network. For more information and important considerations, see [Understanding peering ranges](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges). 

Note that you are creating sufficient network IP range for **one Apigee instance**. If you plan to create additional Apigee instances, you have to repeat this step for each one. The ranges cannot be shared between instances. See also [Expanding Apigee to multiple regions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/multi-region). 

**Important:** If you already have a peering range and private connection with `servicenetworking.googleapis.com`, and your range is big enough to handle another `/22` and `/28` CIDR range, you can skip this step. Apigee will create the needed CIDR blocks for you. This step is only required if you do not already have a space created that has room to create a `/22` and `/28` block, or if you want to use a specific `/22` and `/28` that is currently not present. 

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [ Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [ Service networking permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#service-networking-permissions). 

  1. Create these environment variables: 
         
         **RANGE_NAME** =YOUR_RANGE_NAME
         **NETWORK_NAME** =YOUR_NETWORK_NAME
         

Where:

     * **RANGE_NAME** is the name of the IP address range you are creating. You can name the range anything you want. For example: `google-svcs`
     * **NETWORK_NAME** is the name of the network resource in which the addresses should be reserved. 

Google creates a [default network](https://docs.cloud.google.com/vpc/docs/vpc#default-network) (named `default`) for each new project, so you can use that. However, Google does not recommend using the default network for anything other than testing.

**Note:** Google does not recommend using `default` unless you are testing this setup process. You should not use an organization with a default network in production.
  2. Create a network IP range with a CIDR length of /22: 
         
         gcloud compute addresses create **$RANGE_NAME** \
           --global \
           --prefix-length=22 \
           --description="Peering range for Apigee services" \
           --network=**$NETWORK_NAME** \
           --purpose=VPC_PEERING \
           --addresses=OPTIONAL_ADDRESSES \
           --project=**$PROJECT_ID**

Where `--addresses` lets you optionally specify an address range. For example, to allocate the CIDR block `192.168.0.0/22`, specify `192.168.0.0` for the address and `22` for the prefix length. See also [ Creating an IP allocation](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#procedure). 

If you do not provide the `--addresses` parameter, then gcloud selects an available address range for you. 

On success, `gcloud` responds with the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/global/addresses/google-svcs].

After you create a range of IP addresses, the addresses are associated with the project until you release them.

  3. Verify the network IP range was created with a CIDR length of /22: 
         
         gcloud compute addresses list --global --project=**$PROJECT_ID**
         gcloud compute addresses describe **$RANGE_NAME** --global --project=**$PROJECT_ID**

  4. Create a network IP range with a CIDR length of /28. This range is required and is used by Apigee for troubleshooting purposes and cannot be customized or changed. 
         
         gcloud compute addresses create google-managed-services-support-1 \
           --global \
           --prefix-length=28 \
           --description="Peering range for supporting Apigee services" \
           --network=**$NETWORK_NAME** \
           --purpose=VPC_PEERING \
           --addresses=OPTIONAL_ADDRESSES \
           --project=**$PROJECT_ID**

Where `--addresses` lets you optionally specify an address range. For example, to allocate the CIDR block `192.168.0.0/28`, specify `192.168.0.0` for the address and `28` for the prefix length. See also [ Creating an IP allocation](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#procedure). 

If you do not provide the `--addresses` parameter, then gcloud selects an available address range for you. 

  5. Verify the network IP range was created with a CIDR length of /28: 
         
         gcloud compute addresses list --global --project=**$PROJECT_ID**
         gcloud compute addresses describe google-managed-services-support-1 --global \
           --project=**$PROJECT_ID**

  6. Connect your services to the network using the following command: 
         
         gcloud services vpc-peerings connect \
           --service=servicenetworking.googleapis.com \
           --network=**$NETWORK_NAME** \
           --ranges=**$RANGE_NAME,google-managed-services-support-1** \
           --project=**$PROJECT_ID**

This operation can take several minutes to complete. On success, `gcloud` responds with the following, where OPERATION_ID is the UUID of the LRO.
         
         Operation "operations/OPERATION_ID" finished successfully.

Apigee creates a connection between your network and Google's services; specifically, Apigee connects your project to the Service Networking API through VPC peering. Apigee also associates IP addresses with your project.

  7. After few minutes, verify whether VPC peering succeeded: 
         
         gcloud services vpc-peerings list \
           --network=**$NETWORK_NAME** \
           --service=servicenetworking.googleapis.com \
           --project=**$PROJECT_ID**




## Step 5: Create an organization

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
             "authorizedNetwork":"'"**$NETWORK_NAME** "'",
             "runtimeDatabaseEncryptionKeyName":"'"**$RUNTIMEDB_KEY_ID** "'"
           }'

Where:

     * `-d` defines the data payload for the request. This payload must include the following: 
       * `name`: Identifies your new organization. It must be the same name as your project ID. 

       * `analyticsRegion`: Specifies the physical location where your analytics data will be stored.

       * `runtimeType`: Set this value to `CLOUD`.
       * `billingType`: Specifies the billing type of the organization created.
       * `authorizedNetwork`: Identifies the peering network that you specified in Configure service networking. **Note:** Apigee also supports [ using shared VPC](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs) (that is, the host network project is not the same as the one that is peering with Apigee). To use a shared VPC network, use the following format: `projects/HOST_PROJECT_ID/REGION/networks/NETWORK_NAME`. For example:   
`projects/my-sharedvpc-host/global/networks/mynetwork`

See also [VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc) and [REST Resource: organizations](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#Organization).

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
        "authorizedNetwork":"'"**$NETWORK_NAME** "'",
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
       * `authorizedNetwork`: Identifies the peering network that you specified in Configure service networking. **Note:** Apigee also supports [ using shared VPC](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs) (that is, the host network project is not the same as the one that is peering with Apigee). To use a shared VPC network, use the following format: `projects/HOST_PROJECT_ID/REGION/networks/NETWORK_NAME`. For example:   
`projects/my-sharedvpc-host/global/networks/mynetwork`

See also [VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc) and [REST Resource: organizations](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#Organization).

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

If Apigee has successfully created a new organization, you will receive a response that is similar to the following:

### No data residency
         
         {
           "name": "my-cloud-project",
           "createdAt": "1592586495539",
           "lastModifiedAt": "1592586495539",
           "environments": [],
           "properties": {
             "property": [
               {
                 "name": "features.hybrid.enabled",
                 "value": "true"
               },
               {
                 "name": "features.mart.connect.enabled",
                 "value": "true"
               }
             ]
           },
           "analyticsRegion": "us-west1",
           "runtimeType": "CLOUD",
           "subscriptionType": "PAID",
           "caCertificate": "YOUR_CERTIFICATE",
           "authorizedNetwork": "my-network",
           "projectId": "my-cloud-project"
         }

### Data residency
         
         {
             "name": "my-cloud-project",
             "createdAt": "1681412783749",
             "lastModifiedAt": "1681412783749",
             "environments": [
               "test-env"
             ],
             "properties": {
               "property": [
                 {
                   "name": "features.mart.connect.enabled",
                   "value": "true"
                 },
                 {
                   "name": "features.hybrid.enabled",
                   "value": "true"
                 }
               ]
             },
             "authorizedNetwork": "default",
             "runtimeType": "CLOUD",
             "subscriptionType": "PAID",
             "caCertificate": "YOUR_CERTIFICATE",
             "runtimeDatabaseEncryptionKeyName": "projects/my-cloud-project/locations/us/keyRings/my-key-ring/cryptoKeys/my-key-name",
             "projectId": "my-cloud-project",
             "state": "ACTIVE",
             "billingType": "PAYG",
             "addonsConfig": {
               "advancedApiOpsConfig": {},
               "integrationConfig": {},
               "monetizationConfig": {},
               "connectorsPlatformConfig": {}
             },
             "apiConsumerDataEncryptionKeyName": "projects/my-cloud-project/locations/us-central1/keyRings/my-key-ring/cryptoKeys/my-key-name",
             "controlPlaneEncryptionKeyName": "projects/my-cloud-project/locations/us/keyRings/my-key-ring/cryptoKeys/my-key-name",
             "apiConsumerDataLocation": "us-central1",
             "apigeeProjectId": "i0c2a37e80f9850ab-tp"
           }
         
         

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

## Step 6: Create a runtime instance

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

**Note:** By default, Apigee automatically allocates the existing /22 and /28 network IP ranges reserved previously in Step 4: Configure service networking to the instance. 

In advanced use cases, like where you have reserved multiple /22 and /28 ranges or a larger block of ranges like /16 in Step 4: Configure service networking and you want to control the ranges allocated to the instance, you may need to specify exactly which IP range you want Apigee to use. For these cases, you specify a custom IP range with the prefix of /22 or /28 or both. The ranges must be available as part of a private connection between your project and Apigee. 

To customize IP range(s), use the `ipRange` request parameter as described in the [ Instances API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances#Instance) reference document, as explained below:

     1. Create an environment variable that holds the IP ranges in CIDR format: 
            
            **MY_IP_RANGES= CIDR_RANGES**

For example: 
            
            MY_IP_RANGES=10.0.0.1/22             // To specify only /22 range.
            MY_IP_RANGES=10.0.0.1/22,10.0.0.2/28 // To specify both /22 and /28 ranges.
            

**Note:** You can customize just /22 or /28 or both. If you're providing one of /22 or /28, then Apigee automatically allocates the other range from the IP range reserved at Step 4: Configure service networking. 
     2. Create the instance with the `ipRange` parameter: 
        * No data residency:
              
              curl "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances" \
                -X POST -H "Authorization: Bearer **$AUTH** " \
                -H "Content-Type:application/json" \
                -d '{
                  "name":"'"**$INSTANCE_NAME** "'",
                  "location":"'"$RUNTIME_LOCATION"'",
                  "diskEncryptionKeyName":"'"**$DISK_KEY_ID** "'",
                  "ipRange":"'"**$MY_IP_RANGES** "'",
                  "consumerAcceptList":[ARRAY_OF_PROJECT_IDS]
                }'

        * Data residency:
              
              curl "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances" \
                -X POST -H "Authorization: Bearer **$AUTH** " \
                -H "Content-Type:application/json" \
                -d '{
                  "name":"'"**$INSTANCE_NAME** "'",
                  "location":"'"$RUNTIME_LOCATION"'",
                  "diskEncryptionKeyName":"'"**$DISK_KEY_ID** "'",
                  "ipRange":"'"**$MY_22_RANGE,$MY_28_RANGE** "'",
                  "consumerAcceptList":[ARRAY_OF_PROJECT_IDS]
                }'

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

Note that once created, you cannot change the IP range later. If you ever need to change the range, you will have to create a new instance.

While the /22 IP range is used for running Apigee core workloads, the /28 range is used by Apigee to access the instance for troubleshooting purposes. See also [ Creating instances](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances). 

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




## Step 7: Create an environment

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




## Step 8: Configure routing

In this step, you configure how client applications communicate with Apigee. Client to Apigee traffic is also called "northbound" traffic. Northbound configuration options include the following. Go to the configuration option you wish to use and perform the steps for that option:

Access type | Description of the configuration and deployment process  
---|---  
Internal with VPC peering |  Allow only internal access to your API proxies.  You must create a new VM inside the network and connect to it. From the new VM, you can send a request to an Apigee API proxy.  
External with MIG |  Allow external access to your API proxies. Use a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) (MIG) to send API traffic from a global load balancer's backend service to Apigee. With this configuration, Apigee is only able to connect to the peered VPC. This configuration lets you send Apigee API proxy requests from any network-enabled machine.   
Internal with Private Service Connect (New) |  Allow only internal access to your API proxies from any of your Google Cloud projects using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). Private Service Connect enables private connection between a service producer (Apigee) and a service consumer (the peered VPC project and/or one or more other Cloud projects that you control). With this method, requests pass through either a service endpoint or a regional internal load balancer to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments). This configuration lets your internal clients send Apigee API proxy requests from any network-enabled machine.  
External with Private Service Connect (New) |  Allow external access to your API proxies using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). Use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to enable private connection between a service producer (Apigee) and a service consumer (the peered VPC project and/or one or more other Cloud projects that you control). With this method, requests pass through either a global external load balancer or a regional external load balancer to a single point of attachment, called a [service attachment](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments). This configuration lets you send Apigee API proxy requests from any network-enabled machine. **Important:** Recommended routing access configuration if you are using [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). To meet data residency requirements, use Private Service Connect with a **regional external load balancer** and a **self-managed SSL certificate**.  
  
Each of these routing approaches is presented in the instructions below.

### Internal routing (VPC)

For routing of traffic from internal clients to Apigee, you can choose to use TLS termination or not: 

  * **TLS Options:** You have two choices if you want to make API proxy calls from internal clients with TLS enabled: 
    * (Option 1) Configure an internal load balancer (ILB): 
      1. Create a managed instance group (MIG) in your project. To create the MIG, follow the steps **8a** , **8b** , and **8c** in the [External routing (MIG)](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#externalmig) tab.
      2. Create and configure an internal HTTPS(S) load balancer (ILB), and attach the MIG you created to the backend service of the ILB, as explained in [ Set up Internal HTTP(S) Load Balancing with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal). With the ILB configuration, you have full control over the CA certificates used with the ILB. **Note:** When [configuring your ILB](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#lb-config), make sure to specify `HTTPS` as the protocol and provide an SSL certificate so that your load balancer can communicate with the Apigee backend. 
      3. Go to [ Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies) to test the setup.
    * (Option 2) Use the internal, default fully qualified domain name and the internal load balancer IP of the Apigee instance. This case is recommended only for testing purposes, and not for a production environment. In this case, Apigee-created self-signed certificates are used, with Apigee's internal load balancer, and you cannot change them. See [ Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies).
  * **Non-TLS option:** If you don't require TLS termination, API proxy invocation can be performed by bypassing TLS certificate validation. For example, the `curl` command-line tool's `-k` option disables certificate verification; however, the TLS protocol remains active during the connection. Note that accessing the Apigee ingress over plain HTTP on port 80 is not supported, similar to Apigee hybrid. See [ Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies). 



### External routing (MIG)

This section describes how to configure routing to allow _external_ access to API proxies using a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) (MIG) to send API traffic from a global load balancer's backend service to Apigee. You must do this before you can send a request from an external client to your Apigee runtime instance. 

#### Permissions required for this task

You can give the Apigee provisioner a predefined role that includes the permissions needed to complete this task, or give more fine-grained permissions to provide the least privilege necessary. See [Predefined roles](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#predefined-roles) and [Access routing permissions](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/permissions#access-routing-permissions). 

**Note:** For a multi-region setup, you **must** use the command line steps described here. The provisioning UI only allows you to add one MIG to the global load balancer. MIGs are not global, they are regional. Therefore, for multi-region, you must create one MIG for each region and add them to the global load balancer's backend service.

The general process is as follows:

Step 8a: Enable Private Google Access for a subnet of your VPC network  
Step 8b: Set up environment variables  
Step 8c: Create a managed instance group  
Step 8d: Create an SSL certificate and key for the load balancer  
Step 8e: Create a global load balancer  
Step 8f: Get a reserved IP address and create firewall rules

Each of these steps is described in the sections that follow.

#### Step 8a: Enable Private Google Access for a subnet of your VPC network

To enable [Private Google Access](https://cloud.google.com/vpc/docs/private-google-access) for a subnet of your VPC network, follow the steps listed in [Enabling Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga).

**Note:** If you are doing a multi-region setup, you must do this step once for each region.

#### Step 8b: Set up environment variables

**Multi-region** : A multi-region setup requires a separate MIG for each region. If you are configuring multiple regions, repeat Steps 8b and 8c for each region, substituting the appropriate variables for each region.

The instructions in this section use environment variables to refer to repeatedly used strings. We recommend that you set these before continuing:
    
    
    MIG_NAME=apigee-mig-MIG_NAME   # You can choose a different name if you like
    VPC_NAME=default       # If you are using a [shared VPC](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/shared-vpcs), use the shared VPC name
    VPC_SUBNET=default     # Private Google Access must be enabled for this subnet
    REGION=RUNTIME_REGION        # The same region as your Apigee runtime instance
    APIGEE_ENDPOINT=APIGEE_INSTANCE_IP     # See the tip below for details on getting this IP address value

You'll use these variables several times during the remaining processes. If you wish to configure multiple regions, then create variables with values specific for each region.

**Tip:** To get the correct Apigee instance IP address, use the [Instances API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances), as the following example shows: 

  * No data residency:
        
        curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
          "https://apigee.googleapis.com/v1/organizations/$PROJECT_ID/instances"

  * Data residency:
        
        curl -i -X GET -H "Authorization: Bearer **$AUTH** " \
          "https://REGIONAL_ENDPOINT/v1/organizations/**$PROJECT_ID** /instances"

Where REGIONAL_ENDPOINT is the [regional endpoint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#drz-regional-endpoint) required to support data residency.

Apigee responds with details about the instance; for example:
    
    {
    "instances": [
      {
        "name": "my-runtime-instance",
        "location": "us-west1",
        "host": "10.16.0.2",
        "port": "443"
      },
      ...
    ]
    }

The instance IP address, which you can assign to the $APIGEE_ENDPOINT environment variable, is the value of the `host` field. In this example, the value is `10.16.0.2`.

In a multi-region installation, the API call returns instance details for each regional location. In that case, you need to create a separate managed instance group (MIG) for each location when following the steps in the next section.




#### Step 8c: Create a managed instance group

**Multi-region** : A multi-region setup requires a separate MIG for each region. If you are configuring multiple regions, repeat Steps 8b and 8c for each region, substituting the appropriate variables for each region.

In this step, you create and configure a managed instance group (MIG). In a later step, you add the MIG to a backend service which is attached to a global load balancer. A MIG is required to send API traffic from the global load balancer's backend service to Apigee.

**Note:** These VMs are managed by you, not by Apigee. You are responsible for scaling, patching, and maintaining these VMs. Apigee only provides the startup script used to configure the VMs to route traffic.

**To create a MIG:**

  1. Create an [instance template](https://cloud.google.com/compute/docs/instance-templates) by executing the following command. 
         
         gcloud compute instance-templates create $MIG_NAME \
         --project **$PROJECT_ID** \
         --region $REGION \
         --network $VPC_NAME \
         --subnet $VPC_SUBNET \
         --tags=https-server,apigee-mig-proxy,gke-apigee-proxy \
         --machine-type e2-medium --image-family debian-12 \
         --image-project debian-cloud --boot-disk-size 20GB \
         --no-address \
         --metadata ENDPOINT=$APIGEE_ENDPOINT,startup-script-url=gs://apigee-5g-saas/apigee-envoy-proxy-release/latest/conf/startup-script.sh

As you can see from this command, machines are of type `e2-medium`. They run Debian 12 and have 20GB of disk. The `startup-script.sh` script configures the MIG to route inbound traffic from the load balancer to the Apigee instance.

  2. Create a [managed instance group](https://cloud.google.com/compute/docs/instance-groups) by executing the following command: 
         
         gcloud compute instance-groups managed create $MIG_NAME \
         --project **$PROJECT_ID** --base-instance-name apigee-mig \
         --size 2 --template $MIG_NAME --region $REGION

  3. Configure [autoscaling](https://cloud.google.com/compute/docs/instance-groups#autoscaling) for the group by executing the following command: **Note:** A regional MIG with e2-medium instances can support a maximum of 6 Gbps. If that is not sufficient for your throughput needs, consider upsizing the VM and/or increasing the number of replicas.
         
         gcloud compute instance-groups managed set-autoscaling $MIG_NAME \
         --project **$PROJECT_ID** --region $REGION --max-num-replicas 3 \
         --target-cpu-utilization 0.75 --cool-down-period 90

  4. Define a named port by executing the following command: 
         
         gcloud compute instance-groups managed set-named-ports $MIG_NAME \
         --project **$PROJECT_ID** --region $REGION --named-ports https:443




#### Step 8d: Create an SSL certificate and key for the load balancer

You only need to create the credentials once, whether you are installing in single or multi regions. In a later step, you will associate these credentials with the load balancer's target HTTPS proxy.

You can create the credentials with:

  * Your own certificate from a certificate authority
  * A [Google-managed SSL certificate](https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)
  * A [self-signed certificate](https://docs.cloud.google.com/apigee/docs/hybrid/latest/environment-self-signed-tls) (not recommended for production).



For more information on creating and using SSL certificates for Google Cloud load balancer, see [SSL certificates](https://cloud.google.com/load-balancing/docs/https#ssl_certificates#ssl-certificates) and [SSL certificate overview](https://cloud.google.com/load-balancing/docs/ssl-certificates).

In the following example, we create a Google-managed SSL certificate: 

  1. Create these environment variables: 
         
         **CERTIFICATE_NAME** =YOUR_CERT_NAME
         **DOMAIN_HOSTNAME** =YOUR_DOMAIN_HOSTNAME 

Set `DOMAIN_HOSTNAME` to a valid domain hostname that you have registered. In a later step, you will obtain the load balancer's IP address and update the domain A record to point to that address. For example, a domain hostname might look like this: `foo.example.com`. 

  2. Execute the [ gcloud compute ssl-certificates create](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/create) command: 
         
         gcloud compute ssl-certificates create **$CERTIFICATE_NAME** \
           --domains=**$DOMAIN_HOSTNAME** \
           --project **$PROJECT_ID** \
           --global

The certificate can take up to an hour to be provisioned. To check the status of the provisioning, execute this command:
         
         gcloud compute ssl-certificates describe **$CERTIFICATE_NAME** \
          --global \
          --format="get(name,managed.status, managed.Status)"

**Note:** You can create multiple DNS A records for your environment group hostnames that all point to the same load balancer IP address. 



#### Step 8e: Create a global load balancer

  1. Create a [health check](https://cloud.google.com/load-balancing/docs/health-checks): 
         
         gcloud compute health-checks create https HEALTH_CHECK_NAME \
         --project **$PROJECT_ID** --port 443 --global \
         --request-path /healthz/ingress

You'll use this health check to ensure that the backend service is running. For configuring more advanced health checks against a specific proxy, see [Performing health checks](https://docs.cloud.google.com/apigee/docs/api-platform/debug/health-check).

**Note:** If you get the following error while trying to create a health check: 
         
         ERROR: unrecognized arguments: --global,

Try updating `gcloud` using the `gcloud components update` command.

  2. (Optional) Configure auto-healing for the MIG by using the newly created health check. This ensures that any VM in your MIG that becomes unresponsive is automatically recreated. 
         
         gcloud compute instance-groups managed update $MIG_NAME \
         --health-check HEALTH_CHECK_NAME \
         --initial-delay 300 \
         --region $REGION \
         --project **$PROJECT_ID**

  3. Create a [backend service](https://cloud.google.com/load-balancing/docs/backend-service): 
         
         gcloud compute backend-services create PROXY_BACKEND_NAME \
         --project **$PROJECT_ID** \
         --protocol HTTPS \
         --health-checks HEALTH_CHECK_NAME \
         --port-name https \
         --timeout 302s \
         --connection-draining-timeout 300s \
         --global

**Note:** As documented in the Apigee [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference#cloud-timeouts), Apigee's ingress (internal load balancer) has a default 300 seconds timeout. Setting the load balancer's backend-services timeout to 302 seconds will allow the backend-services command to fully complete within Apigee in the event there are long running transactions. Setting this value to something less, such as 60 seconds, may cause the load balancer to time out before the request has completed, resulting in 502 responses.
  4. Add the MIG to your backend service with the following command: **Multi-region:** For a multi-region setup, you must create a separate MIG for each region, then repeat this step to add each MIG to the backend service. Be sure to substitute the appropriate `REGION` and `MIG_NAME` variables for each region.
         
         gcloud compute backend-services add-backend PROXY_BACKEND_NAME \
         --project **$PROJECT_ID** --instance-group $MIG_NAME \
         --instance-group-region $REGION \
         --balancing-mode UTILIZATION --max-utilization 0.8 --global

  5. Create a [load balancing URL map](https://cloud.google.com/load-balancing/docs/url-map) with the following command: 
         
         gcloud compute url-maps create MIG_PROXY_MAP_NAME \
         --project **$PROJECT_ID** --default-service PROXY_BACKEND_NAME

  6. Create a [load balancing target HTTPS proxy](https://cloud.google.com/load-balancing/docs/target-proxies) with the following command: 
         
         gcloud compute target-https-proxies create MIG_HTTPS_PROXY_NAME \
         --project **$PROJECT_ID** --url-map MIG_PROXY_MAP_NAME \
         --ssl-certificates **$CERTIFICATE_NAME**




#### Step 8f: Get a reserved IP address and create firewall rules

You must assign an IP address to the load balancer and then create rules that allow the load balancer to access the MIG. You only need to do this step once, whether you are installing in single or multi regions.

  1. [Reserve an IP address](https://cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#reserve_new_static) for the load balancer: 
         
         gcloud compute addresses create ADDRESSES_NAME \
         --project **$PROJECT_ID** \
         --ip-version=IPV4 \
         --global

  2. Create a [global forwarding rule](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts) with the following command: 
         
         gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
         --project **$PROJECT_ID** --address ADDRESSES_NAME --global \
         --target-https-proxy MIG_HTTPS_PROXY_NAME --ports 443

  3. Get the reserved IP address by executing the following command: 
         
         gcloud compute addresses describe ADDRESSES_NAME \
         --project **$PROJECT_ID** --format="get(address)" --global

  4. **Important step:** Go to the site, DNS host, or ISP where your DNS records are managed, and make sure your domain's DNS record resolves to the IP address of the Google Cloud load balancer. This address is the IP value returned in the last step. For more detail, see [ Update the DNS A and AAAA records to point to the load balancer's IP address](https://cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#update-dns).
  5. Create a firewall rule that lets the load balancer access the MIG by using the following command: 
         
         gcloud compute firewall-rules create FIREWALL_RULE_NAME \
         --description "Allow incoming from GLB on TCP port 443 to Apigee Proxy" \
         --project **$PROJECT_ID** --network $VPC_NAME --allow=tcp:443 \
         --source-ranges=130.211.0.0/22,35.191.0.0/16 --target-tags=gke-apigee-proxy

Note that the IP address ranges `130.211.0.0/22` and `35.191.0.0/16` are the source IP address ranges for Google Load Balancing. This firewall rule allows Google Cloud Load Balancing to make health check requests to the MIG.




Apigee provisioning is complete. Go to Deploy a sample proxy. 

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
               "serviceAttachment": "**projects/bfac74a67a320c43a12p-tp/regions/us-west1/serviceAttachments/apigee-us-west1-crw1** "
             }
           ]
         }

**Note:** The ID for the project that you used to [create your Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org) always appears in the `consumerAcceptList` list. In the example output shown above, it is the only project in the list.
  2. Create a Private Service Connect Service Endpoint that points to the service attachment that you obtained from the instance response body in the previous step, as explained in [Create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint). 
  3. To test the setup, go to [ Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies). 



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

## Step 9: Deploy a sample proxy

#### Permissions required for this task

Creating and deploying proxies requires a minimum set of permissions. If you have Apigee Org Admin role, you can complete this task. To learn about other roles you can employ, see [ Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles). 

Follow these steps if you completed the configuration for:

  * External routing (MIG)
  * External routing (Private Service Connect)
  * Internal routing (Private Service Connect)



If you configured Internal routing (VPC), skip these steps and go to [ Calling an API proxy with internal-only access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/accessing-internal-proxies). 

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

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


  *[LRO]: Long-Running Operation
  *[VPC]: Virtual Private Cloud
