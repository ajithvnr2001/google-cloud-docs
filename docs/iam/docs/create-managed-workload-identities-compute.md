---
url: https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute/
title: Configure managed workload identity authentication for Compute Engine \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:02.421721+00:00
---

# Configure managed workload identity authentication for Compute Engine  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure managed workload identity authentication for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure [managed workload identities](https://docs.cloud.google.com/iam/docs/managed-workload-identity) for Compute Engine by using the gcloud CLI. It also describes how to set up automatic provisioning and lifecycle management of managed workload identities for Compute Engine by using [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service), which lets you establish mutual TLS (mTLS) connections between workloads.

## Before you begin

  1. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  2. Understand [managed workload identities](https://docs.cloud.google.com/iam/docs/managed-workload-identity).

  3. Learn about certificate issuance using [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service).

  4. Learn how to [authenticate Compute Engine workloads using managed workload identities](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls).

  5. Enable the IAM and Certificate Authority Service APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable iam.googleapis.com privateca.googleapis.com

  6. Configure Google Cloud CLI to use a project for billing and quota.
         
         gcloud config set billing/quota_project PROJECT_ID
         

Replace PROJECT_ID with the ID of the project.




### Required roles

To get the permissions that you need to create managed workload identities and provision managed workload identity certificates, ask your administrator to grant you the following IAM roles on the project: 

  * To create and configure managed workload identities: 
    * [IAM Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`)
    * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * To create and configure CA pools: [CA Service Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.admin) (`roles/privateca.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, the IAM Owner (`roles/owner`) basic role also includes permissions to configure managed workload identities. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Overview

To use managed workload identities for your applications, you must perform the following tasks:

  1. **Security Administrator** :

     * Create a workload identity pool.
     * Configure a CA (to choose a CA option, configure CAs, and update the pool).
     * Create managed workload identities in the workload identity pool.
     * Define a workload attestation policy and create a service account.
  2. **Compute Administrator** :

Enable managed workload identities for workloads running in Compute Engine:

     * For [individual VMs](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#enable-workload-id-vms).
     * For [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#create-workload-id-migs).



## Create a workload identity pool

  1. To configure managed workload identities, you must create a pool in `TRUST_DOMAIN` mode.
         
         gcloud iam workload-identity-pools create POOL_ID \
           --location="global" \
           --mode="TRUST_DOMAIN"
         

Replace POOL_ID with the unique ID for the pool. The ID must be between 4 and 32 characters long, contain only lowercase alphanumeric characters and dashes, and start and end with an alphanumeric character. After you create a workload identity pool, you can't change its ID.

  2. To verify that your workload identity pool was created in `TRUST_DOMAIN` mode, run the `workload-identity-pools describe` command.
         
         gcloud iam workload-identity-pools describe POOL_ID \
           --location="global"
         

The output is similar to the following:
         
         mode: TRUST_DOMAIN
         name: projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID
         state: ACTIVE
         

If `mode: TRUST_DOMAIN` isn't present in the command output, verify that you've correctly configured your gcloud CLI to use the correct project for billing and quota. Ensure that you have updated to the latest version of the gcloud CLI.




## Choose a CA option

To sign your workload certificates, choose the certificate authority (CA) option that best fits your use case:

  * **Google-managed default CA** : Use this option for a fully managed, no-cost solution. The default CA provides a shared root of trust for all Google Cloud users.

  * **Custom CA** : Use this option to configure your own public key infrastructure (PKI) through Certificate Authority Service. This option is appropriate if you require a custom root of trust or if you must store signing keys in a hardware security module (HSM) to meet compliance requirements. Certificate Authority Service is charged separately from managed workload identity. For more information, see [CA Service pricing](https://cloud.google.com/certificate-authority-service/pricing).




## Configure a CA

### Default CA

To bind the default CA to the workload identity pool, update the workload identity pool with the `use-default-shared-ca` flag.
    
    
    gcloud iam workload-identity-pools update TRUST_DOMAIN_NAME \
        --location="global" \
        --use-default-shared-ca \
        --project=PROJECT_ID
    

Replace the following:

  * `TRUST_DOMAIN_NAME`: The name of the trust domain.
  * `PROJECT_ID`: The project ID.



### Custom CA

To configure managed workload identities by using a custom CA, complete the following steps:

  1. Configure CA Service to issue certificates for managed workload identities.
  2. Bind the CAs to the workload identity pool.
  3. Authorize managed workload identities to request certificates from the CA pool.



### Configure CA Service to issue certificates for managed workload identities

Create the recommended configuration for root and subordinate certificate authorities (CAs) by using [Certificate Authority Service pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool). The subordinate CA pool issues the X.509 workload identity certificates to VMs.

The CA pools configured to issue certificates for Compute Engine VMs by using managed workload identities must reside in the same region as the VM. If you want to design a [multi-region architecture for resilience to regional outages](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional#reference_architecture), we recommend that you configure a subordinate Certificate Authority Service CA pool for each of your workload's regions. This way, each of your Compute Engine VMs can reference an in-region subordinate Certificate Authority Service CA pool.

**Caution:** If you also [attach certificate issuance policies to your CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy), the issuance policy must [comply with certificate requirements for mTLS](https://docs.cloud.google.com/load-balancing/docs/mtls#certificate-requirements) to ensure that the provisioned certificates can be used for mTLS. Otherwise, the certificates might be provisioned successfully but fail when used for mTLS connections.

After configuring the CA pools, you then authorize the managed workload identities to request and receive the signed certificates from the CA pools.

#### Configure your root CA pool

Use the Google Cloud CLI interface to Certificate Authority Service to configure a root CA pool.

You can't move or export a CA pool after it's created.

  1. Create the root CA pool in the **Enterprise** tier by running the [`gcloud privateca pools create` command](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/create). The **Enterprise** tier is intended for long-lived, low-volume certificate issuance.
         
         gcloud privateca pools create ROOT_CA_POOL_ID \
            --location=REGION \
            --tier=enterprise
         

Replace the following:

     * ROOT_CA_POOL_ID: A unique ID for the root CA pool. The ID can be up to 64 characters long and must contain only lower and uppercase alphanumeric characters, underscores, or hyphens. The pool ID must be unique within the region.
     * REGION: the region where the root CA pool is located.

For more information, see [Creating CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

  2. Create a root CA in the root CA pool by running the [`gcloud privateca roots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/create). You might be prompted to [enable the root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#enable-root) if this is the only CA in the root CA pool.

For example, you might use a command similar to the following to create a root CA.
         
         gcloud privateca roots create ROOT_CA_ID \
            --pool=ROOT_CA_POOL_ID \
            --subject "CN=ROOT_CA_CN, O=ROOT_CA_ORGANIZATION" \
            --key-algorithm="ec-p256-sha256" \
            --max-chain-length=1 \
            --location=REGION
         

Replace the following:

     * ROOT_CA_ID: A unique name for the root CA. The CA name can be up to 64 characters long and must contain only lower and uppercase alphanumeric characters, underscores, or hyphens. The CA name must be unique within the region.
     * ROOT_CA_POOL_ID: the ID of the root CA pool.
     * ROOT_CA_CN: the common name of the root CA.
     * ROOT_CA_ORGANIZATION: the organization of the root CA.
     * REGION: the region where the root CA pool is located.

For more information, see [Create a root certificate authority](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities). For more information about the `subject` fields for the CA, see [Subject](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel#subject).

  3. Optional: Repeat the previous steps to create an additional root CA in the root CA pool. This can be useful for [root CA rotation](https://docs.cloud.google.com/certificate-authority-service/docs/managing-ca-rotation).




#### Configure the subordinate CAs

Use the Google Cloud CLI interface to Certificate Authority Service to create a subordinate CA pool and subordinate CA.

If you have multiple certificate issuance scenarios, you can create a subordinate CA for each of those scenarios. Also, adding multiple subordinate CAs in a CA pool helps you achieve better load-balancing of certificate requests.

Use the [`gcloud privateca pools create` command](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/create) to create a subordinate CA pool.

  1. Create the subordinate CA pool in the **DevOps** tier. This tier is intended for high-volume, short-lived certificate issuance.
         
         gcloud privateca pools create SUBORDINATE_CA_POOL_ID \
           --location=REGION \
           --tier=devops
         

Replace the following:

     * SUBORDINATE_CA_POOL_ID: A unique ID for the subordinate CA pool. The ID can be up to 64 characters long and must contain only lowercase and uppercase alphanumeric characters, underscores, or hyphens. The pool ID must be unique within the region.
     * REGION: the region in which to create the subordinate CA pool.

For more information, see [Creating CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

  2. Create a subordinate CA in the subordinate CA pool by running the [`gcloud privateca subordinates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/subordinates/create). Don't change the default [config-based issuance mode](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools#issuancemodes).

For example, you might use a command similar to the following to create a subordinate CA.
         
         gcloud privateca subordinates create SUBORDINATE_CA_ID \
           --pool=SUBORDINATE_CA_POOL_ID \
           --location=REGION \
           --issuer-pool=ROOT_CA_POOL_ID \
           --issuer-location=REGION \
           --subject="CN=SUBORDINATE_CA_CN, O=SUBORDINATE_CA_ORGANIZATION" \
           --key-algorithm="ec-p256-sha256" \
           --use-preset-profile=subordinate_mtls_pathlen_0
         

Replace the following:

     * SUBORDINATE_CA_ID: A unique name for the subordinate CA. The name can be up to 64 characters long and must contain only lowercase and uppercase alphanumeric characters, underscores, or hyphens. The CA name must be unique within the region.
     * SUBORDINATE_CA_POOL_ID: the name of the subordinate CA pool.
     * REGION: the region where the subordinate CA pool is located.
     * ROOT_CA_POOL_ID: the ID of the root CA pool.
     * REGION: the region of the root CA pool.
     * SUBORDINATE_CA_CN: the common name of the subordinate CA.
     * SUBORDINATE_CA_ORGANIZATION: the name of the subordinate CA issuing organization.

For more information, see [Creating CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool). For more information about the `subject` fields for the CA, see [Subject](https://docs.cloud.google.com/certificate-authority-service/docs/using-cel#subject).




### Bind the CAs to the workload identity pool

After you create your CA hierarchy, you bind the CAs to the workload identity pool by updating the pool with each of the CA's certificate issuance config.

  1. Create an `issuance-config.yaml` file with the following content:
         
         inlineCertificateIssuanceConfig:
         caPools:
         REGION: projects/PROJECT_ID/locations/REGION/caPools/SUBORDINATE_CA_POOL_ID
         keyAlgorithm: RSA_2048
         lifetime: 86400s
         rotationWindowPercentage: 50

Replace the following in the file:

     * `REGION`: The region where the subordinate CA pool is located.
     * `PROJECT_ID`: The ID of the project that contains the subordinate CA pool.
     * `SUBORDINATE_CA_POOL_ID`: The ID of the subordinate CA pool.
  2. Run the following command to update the workload identity pool:
         
         gcloud iam workload-identity-pools update POOL_ID \
            --location="global" \
            --inline-certificate-issuance-config-file=ISSUANCE_CONFIG_FILE
         

Replace the following:

     * `POOL_ID`: The unique ID for the pool.
     * `ISSUANCE_CONFIG_FILE`: The path to the `issuance-config.yaml` file.



### Authorize managed workload identities to request certificates from the CA pool

The managed workload identities require permissions to request certificates from the CA Service and get the public certificates.

  1. Grant the [CA Service Workload Certificate Requester (`roles/privateca.workloadCertificateRequester`)](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.workloadCertificateRequester) IAM role on each subordinate CA pool to the managed workload identity. The following [`gcloud privateca pools add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/add-iam-policy-binding) authorizes the managed workload identity to request certificates from the CA Service certificate chains.
         
         gcloud privateca pools add-iam-policy-binding SUBORDINATE_CA_POOL_ID \
           --location=REGION \
           --role=roles/privateca.workloadCertificateRequester \
           --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/POOL_ID/*"
         

Replace the following:

     * SUBORDINATE_CA_POOL_ID: the ID for the subordinate CA pool.
     * REGION: the region of the subordinate CA pool.
     * PROJECT_NUMBER: the project number of the project that contains the workload identity pool.
     * POOL_ID: the ID of the workload identity pool.
  2. Grant the [CA Service Pool Reader (`roles/privateca.poolReader`)](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.poolReader) IAM role on the subordinate CA pools to the managed workload identity. This authorizes the managed workload identity to get the signed X.509 certificates from the CA's certificate chains.
         
         gcloud privateca pools add-iam-policy-binding SUBORDINATE_CA_POOL_ID \
           --location=REGION \
           --role=roles/privateca.poolReader \
           --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/POOL_ID/*"
         

Replace the following:

     * SUBORDINATE_CA_POOL_ID: the ID for the subordinate CA pool.
     * REGION: the region of the subordinate CA pool.
     * PROJECT_NUMBER: the project number of the project that contains the workload identity pool.
     * POOL_ID: the ID of the workload identity pool.



## Create managed workload identities

Managed workload identities enable Google Cloud to automatically provision credentials for workload identity pool identities onto your workloads. Workload identities are defined within a workload identity pool, and are organized into administrative boundaries called _namespaces_.

### Create a namespace

The `workload-identity-pools namespaces create` command lets you create a namespace in a workload identity pool.
    
    
    gcloud iam workload-identity-pools namespaces create NAMESPACE_ID \
        --workload-identity-pool="POOL_ID" \
        --location="global"
    

Replace the following:

  * `NAMESPACE_ID`: the unique ID for the namespace. The ID must be between 2 and 63 characters long, contain only lowercase alphanumeric characters and dashes, and start and end with an alphanumeric character. After you create a namespace, you cannot change its ID.
  * `POOL_ID`: the workload identity pool ID that you created earlier.



### Create a managed workload identity

The `workload-identity-pools managed-identities create` command lets you create a managed workload identity in a workload identity pool namespace.
    
    
    gcloud iam workload-identity-pools managed-identities create MANAGED_IDENTITY_ID \
        --namespace="NAMESPACE_ID" \
        --workload-identity-pool="POOL_ID" \
        --location="global"
    

Replace the following:

  * `MANAGED_IDENTITY_ID`: the unique ID for the managed identity. The ID must be between 2 and 63 characters long, contain only lowercase alphanumeric characters and dashes, and start and end with an alphanumeric character. After you create a managed workload identity, you cannot change its ID.
  * `NAMESPACE_ID`: the namespace ID that you created earlier.
  * `POOL_ID`: the workload identity pool ID that you created earlier.



Your managed workload identity ID is the SPIFFE identifier, which is formatted as follows:
    
    
    spiffe://POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID
    

## Define a workload attestation policy

This section describes how to set up an [attestation policy](https://docs.cloud.google.com/iam/docs/managed-workload-identity#resources). This policy determines which attributes are used by [Google Cloud IAM](https://docs.cloud.google.com/iam/docs/managed-workload-identity) to verify the identity of the workload. After verification, the calling workload can receive a credential.

Verification is based on one of the following attributes of the workload:

  * Attached service account email address
  * Attached service account UID
  * VM instance name
  * VM instance ID

**Deprecated:** Workload sources are deprecated as of October 11, 2024. As of this date, you can no longer create new workload sources. Existing workload sources will be removed on or after April 24, 2025. Attestations based on workload sources will fail. To prevent disruption, we recommend that you attest using another method described later in this document. To learn how to list previously configured workload sources, use the following command: `gcloud iam workload-identity-pools managed-identities workload-sources list --help`.

### Define a workload attestation policy with attestation rules

To create an attestation policy that lets your workload use the managed identity, do the following:

  1. Decide whether you want to create an attestation policy that lets your workload attest the managed identity by using its attached service account, by using its instance name, or by using its instance ID.

  2. Create a JSON-formatted attestation policy file.

     1. Optional: To receive X.509 credentials on your Compute Engine instance, you must enable an attached service account. We recommend that you attach a new service account to your workload by first creating it using the following command:
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME
            

Replace `SERVICE_ACCOUNT_NAME` with the name of the service account

     2. Create a JSON-formatted attestation policy file that attests based on the service account email address, service account UID, the instance name, or the instance ID.

### Service account email address

To create an attestation policy file that attests based on the service account email address, create a file with the following contents:
            
            {
               "attestationRules": [
                  {
                     "googleCloudResource": "//compute.googleapis.com/projects/WORKLOAD_PROJECT_NUMBER/type/Instance/attached_service_account.email/SERVICE_ACCOUNT_EMAIL"
                  }
               ],
            }
            

Replace the following:

        * `WORKLOAD_PROJECT_NUMBER`: the number of the project that contains the VM instance or service account

To get the project number of the project that contains the managed identity or the service account that you just created, run the following command:
              
              gcloud projects describe $(gcloud config get-value project) \
                --format="value(projectNumber)"
              

        * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account attached to the VM

### Service account UID

To create an attestation policy file that attests based on the service account UID, create a file with the following contents:
    
    {
       "attestationRules": [
          {
             "googleCloudResource": "//compute.googleapis.com/projects/WORKLOAD_PROJECT_NUMBER/type/Instance/attached_service_account.uid/SERVICE_ACCOUNT_UID"
          }
       ],
    }
    

Replace the following:

        * `WORKLOAD_PROJECT_NUMBER`: the number of the project that contains the VM instance or service account

To get the project number of the project that contains the managed identity or the service account that you just created, run the following command:
              
              gcloud projects describe $(gcloud config get-value project) \
                --format="value(projectNumber)"
              

        * `SERVICE_ACCOUNT_UID`: the UID of the service account attached to the VM

To get the Unique ID of the service account, run the following command:
    
    gcloud iam service-accounts describe SERVICE_ACCOUNT_EMAIL\
          --format="value(uniqueId)"
    

### Instance name

To create an attestation policy file that attests based on the instance name, create a file with the following contents:
    
    {
       "attestationRules": [
          {
             "googleCloudResource": "//compute.googleapis.com/projects/WORKLOAD_PROJECT_NUMBER/name/zones/ZONE/instances/INSTANCE_NAME"
          }
       ],
    }
    

Replace the following:

        * `WORKLOAD_PROJECT_NUMBER`: the number of the project that contains the VM instance or service account

To get the project number of the project that contains the managed identity or the service account that you just created, run the following command:
              
              gcloud projects describe $(gcloud config get-value project) \
                --format="value(projectNumber)"
              

        * `ZONE`: the Compute Engine VM zone

        * `INSTANCE_NAME`: the name of a new or existing Compute Engine VM instance

### Instance ID

To create an attestation policy file that attests based on the instance ID, create a file with the following contents:
    
    {
       "attestationRules": [
          {
             "googleCloudResource": "//compute.googleapis.com/projects/WORKLOAD_PROJECT_NUMBER/uid/zones/ZONE/instances/INSTANCE_ID"
          }
       ],
    }
    

Replace the following:

        * `WORKLOAD_PROJECT_NUMBER`: the number of the project that contains the VM instance or service account

To get the project number of the project that contains the managed identity or the service account that you just created, run the following command:
              
              gcloud projects describe $(gcloud config get-value project) \
                --format="value(projectNumber)"
              

        * `INSTANCE_ID`: the Compute Engine VM instance ID

The value for an instance ID must come from an existing Compute Engine instance. To obtain your instance ID, run the following command:
              
              gcloud compute instances describe INSTANCE_NAME --zone=ZONE --format="get(id)"
              

        * `INSTANCE_NAME`: the Compute Engine VM instance name

        * `ZONE`: the Compute Engine VM zone

  3. Create the attestation policy using the policy JSON file that you created earlier in this document:
         
         gcloud iam workload-identity-pools managed-identities set-attestation-rules MANAGED_IDENTITY_ID \
            --namespace=NAMESPACE_ID \
            --workload-identity-pool=POOL_ID \
            --policy-file=PATH_TO_POLICY_JSON_FILE \
            --location=global
         

Replace the following:

     * `MANAGED_IDENTITY_ID`: the unique ID for the managed identity. The ID must be between 2 and 63 characters long, contain only lowercase alphanumeric characters and dashes, and start and end with an alphanumeric character. After you create a managed workload identity, you cannot change its ID.
     * `NAMESPACE_ID`: the namespace ID that you created earlier.
     * `POOL_ID`: the workload identity pool ID that you created earlier.
     * `PATH_TO_POLICY_JSON_FILE`: Path to the JSON file representing the attestation policy that you created earlier.

You can also update the policy by adding or removing attestation rules individually. To add an attestation to your attestation policy, run the following command:
    
    gcloud iam workload-identity-pools managed-identities add-attestation-rule MANAGED_IDENTITY_ID \
       --namespace=NAMESPACE_ID \
       --workload-identity-pool=POOL_ID \
       --google-cloud-resource='//compute.googleapis.com/projects/WORKLOAD_PROJECT_NUMBER/type/Instance/attached_service_account.uid/SERVICE_ACCOUNT_UID' \
       --location=global
    

  4. To learn about how to list or remove the attestation rules, run the following commands:
         
         gcloud iam workload-identity-pools managed-identities list-attestation-rules --help
         gcloud iam workload-identity-pools managed-identities remove-attestation-rule --help
         




## Optional: Enable trust federation between workload identity pools

To enable mutual authentication for workloads in different trust domains, you can configure trust federation.

  1. Create a `trust-config.yaml` file with the following content:
         
         inlineTrustConfig:
         additionalTrustBundles:
           POOL_ID.global.PROJECT_NUMBER.workload.id.goog:
              trustAnchors:
              - pemCertificate: "-----BEGIN CERTIFICATE-----\nPEM_ENCODED_CERTIFICATE\n-----END CERTIFICATE-----"

Replace the following in the file:

     * `POOL_ID`: The ID of the workload identity pool that you want to federate with.
     * `PROJECT_NUMBER`: The project number of the workload identity pool that you want to federate with.
     * `PEM_ENCODED_CERTIFICATE`: The PEM-encoded root CA certificate of the workload identity pool that you want to federate with.
  2. To update the workload identity pool with the trust configuration, run the following command:
         
         gcloud iam workload-identity-pools update POOL_ID \
           --location="global" \
           --inline-trust-config-file=TRUST_CONFIG_FILE
         

Replace the following:

     * `POOL_ID`: the unique ID for the pool.
     * `TRUST_CONFIG_FILE`: the path to the `trust-config.yaml` file.



## What's next

  * [Troubleshoot managed workload identity authentication for Compute Engine](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-workload-to-workload-auth).
  * [Configure workload to workload authentication using mTLS](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls).
  * [Set up load balancing with backend mTLS using managed workload identity](https://docs.cloud.google.com/load-balancing/docs/set-up-backend-mtls-managed-identity).
  * Learn more about [creating CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
