---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys/
title: Run your own certificate authorities and keys in GKE \u00a0|\u00a0 Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:48:30.224224+00:00
---

# Run your own certificate authorities and keys in GKE  |  Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Run your own certificate authorities and keys in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** This document uses a [general availability](https://cloud.google.com/products#product-launch-stages) feature named _GKE control plane authority_ that's only available for eligible Google Cloud customers. To request access to this feature, contact your Google Cloud account team.

This document shows you how to configure your Google Kubernetes Engine (GKE) cluster control plane with certificate authorities (CAs) and keys that you manage. This guidance is intended for security administrators who have specific organizational compliance or policy requirements for control over credential issuance and signing.

This page describes one part of a set of optional control plane features in GKE that lets you perform tasks like verifying your control plane security posture or configuring encryption and credential signing in the control plane using keys that you manage. For details, see [About GKE control plane authority](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority).

By default, Google Cloud applies various security measures to the managed control plane. This page describes _optional_ capabilities that give you more visibility or control over the GKE control plane.

You should already be familiar with the following concepts:

  * [Certificate Signing Requests (CSRs)](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/)
  * [Certificate authorities (CAs)](https://wikipedia.org/wiki/Certificate_authority)
  * [etcd](https://kubernetes.io/docs/concepts/architecture/#etcd)
  * [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)



## Control plane credential components

GKE clusters use specific CAs and keys to issue credentials in the cluster, like X.509 certificates or ServiceAccount tokens. You can create keys in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service) (Cloud KMS) and CAs in [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview) (CA Service) and configure your clusters to use these resources instead of Google Cloud-managed CAs and keys.

To learn more about the specific components that you create, see [Self-managed CAs and keys](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority#self-managed-cas-keys).

## Usage with other GKE control plane authority features

GKE control plane authority provides the following features related to self-managed keys:

  * Run your own certificate authorities (CAs) and keys (this document)
  * [Encrypt control plane components](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypt-etcd-control-plane-disks)

**Note:** You can only enable these features when you create a new GKE cluster. You can't update existing clusters to use these features. To use both of these features in the same cluster, perform all of the key and CA configuration procedures in **both guides** , and then run the cluster creation command that enables both sets of features as described in the Create a cluster section.

## Objectives

  * Create keys in Cloud KMS
  * Create CAs in CA Service
  * Grant Identity and Access Management (IAM) roles to the GKE service agent
  * Create a GKE cluster that uses your CAs and keys
  * Verify that the cluster uses your CAs and keys



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [ Cloud KMS](https://docs.cloud.google.com/kms/pricing)
  * [ CA Service](https://docs.cloud.google.com/certificate-authority-service/pricing)
  * [ Cloud Logging](https://docs.cloud.google.com/stackdriver/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Kubernetes Engine, Certificate Authority Service, and Cloud Key Management Service APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com privateca.googleapis.com cloudkms.googleapis.com

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the Kubernetes Engine, Certificate Authority Service, and Cloud Key Management Service APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com privateca.googleapis.com cloudkms.googleapis.com

  12. Ensure that your environment is eligible to use GKE control plane authority features. To opt-in to these features, contact your Google Cloud sales team.
  13. To reliably track credential issuance and usage, ensure that the following Data Access audit logs are enabled: 
     * Cloud Key Management Service (KMS) API: `DATA_READ`
     * Certificate Authority Service: `ADMIN_READ`

To enable these log types, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).




### Required roles and permissions

To get the permissions that you need to run your own CAs and keys, ask your administrator to grant you the following IAM roles: 

  * Create Cloud KMS keys: [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) on your key project 
  * Create CA pools and root CAs: [CA Service Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.admin) (`roles/privateca.admin`) on your key project 
  * Create GKE clusters: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) on your cluster project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Requirements

You must meet the following requirements:

  * Your cluster must run GKE version 1.31.1-gke.1846000 or later.
  * To set up control plane disk encryption with your own keys in addition to configuring your own CAs, create your cluster in one of the following regions:

    * `asia-east1`
    * `asia-northeast1`
    * `asia-southeast1`
    * `europe-west1`
    * `europe-west4`
    * `us-central1`
    * `us-central2`
    * `us-east1`
    * `us-east4`
    * `us-east5`
    * `us-south1`
    * `us-west1`
    * `us-west3`
    * `us-west4`
**Note:** Separately from GKE control plane authority, you can use [Confidential mode for Hyperdisk Balanced for your node disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes). If you plan to use Confidential mode for Hyperdisk Balanced for your nodes in addition to encrypting your control plane disks with your own keys, you must create the cluster in a [region that supports Confidential mode for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/disk-encryption#conf_hdb_regions). If you create the cluster in a different region, you won't be able to use Confidential mode for Hyperdisk Balanced for your nodes.



### Limitations

The following limitations apply:

  * You can only use keys from Cloud KMS. You can't use another KMS provider or another encryption provider.
  * Cloud External Key Manager (Cloud EKM) keys aren't supported.
  * You can only use CAs from CA Service.



## Prepare the environment

In this section, you identify Google Cloud projects that you'll use in this tutorial, and you create a key ring in Cloud KMS to hold your keys.

### Identify projects

We recommend that you use separate Google Cloud projects as follows:

  * **Key project** : contains all keys and CAs.
  * **Cluster project** : contains your GKE clusters.



You can optionally use the same project for your keys, CAs, and GKE clusters, but we recommend that you use separate projects so that the teams that manage cryptographic operations in your organization are separated from the teams that manage cluster operations.

### Create a key ring

Create a key ring in the key project to hold all of the keys for a specific cluster. You must create the key ring in the same location as your GKE cluster.

**Note:** You can't delete a key ring after creation. Key rings don't incur additional costs. However, having too many key rings in a project might make managing your resources in Cloud KMS more tedious.

Run the following command:
    
    
    gcloud kms keyrings create KEY_RING_NAME \
        --location=LOCATION \
        --project=KEY_PROJECT_ID
    

Replace the following:

  * `KEY_RING_NAME`: a name for your key ring.
  * `KEY_PROJECT_ID`: the project ID of your key project.
  * `LOCATION`: the Google Cloud region where you want to create the key ring. This must be the same region where your GKE cluster is located.



## Create keys

For each of the credential authorities like service account keys and CAs, you create a key using Cloud KMS. This section shows you how to create the keys that GKE uses to sign and verify credentials in the cluster. You can specify your own properties for these keys depending on your organization's needs. For details, see the [Create a key](https://docs.cloud.google.com/kms/docs/create-key) page and the [`projects.locations.keyRings.cryptoKeys`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys) API reference.

**Caution:** Don't enable automatic key rotation with Cloud KMS. Rotating your encryption keys requires additional steps to ensure that your control plane resources are re-encrypted with new key versions before the original key versions are destroyed.

Consider the following when you create these resources in Cloud KMS:

  * If you have a existing key ring in your key project, you can use that key ring to store all of the keys that you create for use with your cluster.
  * Your key ring must be in the same Google Cloud location as your cluster to minimize latency.
  * Keys must specify `asymmetric-signing` as the key purpose.
  * Use the following algorithms based on the type of key: 
    * ServiceAccount signing keys: a strong RSA signing PKCS1 algorithm, like `rsa-sign-pkcs1-4096-sha256` or `rsa-sign-pkcs1-3072-sha256`.
    * Certificate authority keys: a strong algorithm like `ec-sign-p256-sha256`.
  * Cloud HSM hardware keys are supported, but the `software` protection level is sufficient for most use cases. For details about hardware keys, see [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm).
  * Don't modify the [default duration for key destruction](https://docs.cloud.google.com/kms/docs/create-key#soft_delete).
  * GKE doesn't prevent you from deleting Cloud KMS keys, including CA Service keys, that are in use by the cluster. Before you delete keys or CAs, ensure that the resources are unused.



To create your keys, run the following commands:

  1. Create the Kubernetes ServiceAccount signing key, which you also specify as the service account verification key during cluster creation:
         
         gcloud kms keys create sa-signing-key \
             --keyring=KEY_RING_NAME \
             --location=LOCATION \
             --purpose="asymmetric-signing" \
             --protection-level=hsm \
             --default-algorithm=rsa-sign-pkcs1-4096-sha256 \
             --project=KEY_PROJECT_ID
         

Replace `KEY_PROJECT_ID` with the project ID for your dedicated key project.

  2. Create the cluster root CA key:
         
         gcloud kms keys create cluster-ca-key \
             --keyring=KEY_RING_NAME \
             --location=LOCATION \
             --purpose="asymmetric-signing" \
             --protection-level=hsm \
             --default-algorithm=ec-sign-p256-sha256 \
             --project=KEY_PROJECT_ID
         

  3. Create the etcd peer root CA key:
         
         gcloud kms keys create etcd-peer-ca-key \
             --keyring=KEY_RING_NAME \
             --location=LOCATION \
             --purpose="asymmetric-signing" \
             --protection-level=hsm \
             --default-algorithm=ec-sign-p256-sha256 \
             --project=KEY_PROJECT_ID
         

  4. Create the etcd API root CA key:
         
         gcloud kms keys create etcd-api-ca-key \
             --keyring=KEY_RING_NAME \
             --location=LOCATION \
             --purpose="asymmetric-signing" \
             --protection-level=hsm \
             --default-algorithm=ec-sign-p256-sha256 \
             --project=KEY_PROJECT_ID
         

  5. Create the aggregation root CA key:
         
         gcloud kms keys create aggregation-ca-key \
             --keyring=KEY_RING_NAME \
             --location=LOCATION \
             --purpose="asymmetric-signing" \
             --protection-level=hsm \
             --default-algorithm=ec-sign-p256-sha256 \
             --project=KEY_PROJECT_ID
         




## Create the CAs

After creating the keys for each of the control plane functions, use each key to create the CA pools and corresponding root CAs using CA Service:

  1. Create the cluster CA pool:
         
         gcloud privateca pools create cluster-ca-pool \
             --location=LOCATION \
             --tier=enterprise \
             --project=KEY_PROJECT_ID \
             --no-publish-crl --no-publish-ca-cert
         

The `--no-publish-crl` flag and the `--no-publish-ca-cert` flag are optional. Omitting these flags publishes certificates to a Cloud Storage bucket. For details, see [Enable CA certificate and CRL publication for CAs in a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/managed-resources#enable-crl-publication).

  2. Create the cluster root CA:
         
         gcloud privateca roots create cluster-root-ca \
             --pool=cluster-ca-pool \
             --location=LOCATION \
             --kms-key-version=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/cluster-ca-key/cryptoKeyVersions/1 \
             --subject="CN=cluster-ca, O=ORGANIZATION" \
             --project=KEY_PROJECT_ID \
             --auto-enable
         

Replace `ORGANIZATION` with your organization name.

  3. Create the etcd peer CA pool:
         
         gcloud privateca pools create etcd-peer-ca-pool \
             --location=LOCATION \
             --tier=enterprise \
             --project=KEY_PROJECT_ID \
             --no-publish-crl --no-publish-ca-cert
         

  4. Create the etcd peer root CA:
         
         gcloud privateca roots create etcd-peer-root-ca \
             --pool=etcd-peer-ca-pool \
             --location=LOCATION \
             --kms-key-version=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/etcd-peer-ca-key/cryptoKeyVersions/1 \
             --subject="CN=etcd-peer-ca, O=ORGANIZATION" \
             --project=KEY_PROJECT_ID \
             --auto-enable
         

  5. Create the etcd API CA pool:
         
         gcloud privateca pools create etcd-api-ca-pool \
             --location=LOCATION \
             --tier=enterprise \
             --project=KEY_PROJECT_ID \
             --no-publish-crl --no-publish-ca-cert
         

  6. Create the etcd API root CA:
         
         gcloud privateca roots create etcd-api-root-ca \
             --pool=etcd-api-ca-pool \
             --location=LOCATION \
             --kms-key-version=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/etcd-api-ca-key/cryptoKeyVersions/1 \
             --subject="CN=etcd-api-ca, O=ORGANIZATION" \
             --project=KEY_PROJECT_ID \
             --auto-enable
         

  7. Create the aggregation CA pool:
         
         gcloud privateca pools create aggregation-ca-pool \
             --location=LOCATION \
             --tier=enterprise \
             --project=KEY_PROJECT_ID \
             --no-publish-crl --no-publish-ca-cert
         

  8. Create the aggregation root CA:
         
         gcloud privateca roots create aggregation-root-ca \
             --pool=aggregation-ca-pool \
             --location=LOCATION \
             --kms-key-version=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/aggregation-ca-key/cryptoKeyVersions/1 \
             --subject="CN=aggregation-ca, O=ORGANIZATION" \
             --project=KEY_PROJECT_ID \
             --auto-enable
         




## Grant IAM roles to the GKE service agent

The [GKE service agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#gke-service-agents) requires access to the resources that you created in Cloud KMS and in CA Service. The service agent uses these resources to sign, verify, and issue credentials in the cluster. You can use the following predefined IAM roles:

  * [Kubernetes Engine KMS Crypto Key User](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.cloudKmsKeyUser) (`roles/container.cloudKmsKeyUser`)
  * [CA Service Certificate Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.certificateManager) (`roles/privateca.certificateManager`)



To grant these roles to the GKE service agent, do the following:

  1. Find the project number of your cluster project:
         
         gcloud projects describe CLUSTER_PROJECT_ID \
             --format='value(projectNumber)'
         

Replace `CLUSTER_PROJECT_ID` with the project ID of your cluster project.

  2. Grant the Kubernetes Engine KMS Crypto Key User role on the service account signing key that you created in Create keys:
         
         gcloud kms keys add-iam-policy-binding sa-signing-key \
           --location=LOCATION \
           --keyring=KEY_RING_NAME \
           --member="serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
           --role=roles/container.cloudKmsKeyUser \
           --project=KEY_PROJECT_ID
         

Replace `CLUSTER_PROJECT_NUMBER` with the project number of the cluster project.

  3. Grant the CA Service Certificate Manager role on the CA pools that you created in Create the CAs:
         
         gcloud privateca pools add-iam-policy-binding cluster-ca-pool \
             --location=LOCATION \
             --member="serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
             --role=roles/privateca.certificateManager \
             --project=KEY_PROJECT_ID
         
         gcloud privateca pools add-iam-policy-binding etcd-peer-ca-pool \
             --location=LOCATION \
             --member="serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
             --role=roles/privateca.certificateManager \
             --project=KEY_PROJECT_ID
         
         gcloud privateca pools add-iam-policy-binding etcd-api-ca-pool \
             --location=LOCATION \
             --member="serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
             --role=roles/privateca.certificateManager \
             --project=KEY_PROJECT_ID
         
         gcloud privateca pools add-iam-policy-binding aggregation-ca-pool \
             --location=LOCATION \
             --member="serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com" \
             --role=roles/privateca.certificateManager \
             --project=KEY_PROJECT_ID
         




### Grant additional roles when not using the gcloud CLI

This section describes additional configuration steps that you must perform if you plan to configure your CAs and keys by using a client like Terraform or the Google Cloud console instead of using the gcloud CLI. If you use the gcloud CLI, skip this section and go to the Set up CAs and keys on a new cluster section.

When you use the gcloud CLI to set up your CAs and keys, as described in this document, the gcloud CLI automatically creates and configures a service agent for CA Service and grants IAM roles to the service agent. However, if you use a client like Terraform or the Google Cloud console to configure your Google Cloud environment, you must perform these configuration steps manually as follows for your key project:

  1. Trigger creation of the CA Service service agent.

**Preview — triggering service agent creation**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
         
         gcloud beta services identity create --service=privateca.googleapis.com \
             --project=KEY_PROJECT_ID
         

  2. Find the project number of your key project:
         
         gcloud projects describe KEY_PROJECT_ID \
             --format='value(projectNumber)'
         

  3. Grant the [Viewer](https://docs.cloud.google.com/iam/docs/understanding-roles#viewer) (`roles/viewer`) role and the [Cloud KMS CryptoKey Signer/Verifier](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.signerVerifier) (`roles/cloudkms.signerVerifier`) role on all of the root CA keys that you created in the Create keys section:
         
         for key in cluster-ca-key etcd-peer-ca-key etcd-api-ca-key aggregation-ca-key
         do
         gcloud kms keys add-iam-policy-binding $key \
             --keyring=KEY_RING_NAME \
             --location=LOCATION \
             --role=roles/viewer \
             --member="serviceAccount:service-KEY_PROJECT_NUMBER@gcp-sa-privateca.iam.gserviceaccount.com" \
             --project=KEY_PROJECT_ID
         
         gcloud kms keys add-iam-policy-binding $key \
             --keyring=KEY_RING_NAME \
             --location=LOCATION \
             --role=roles/cloudkms.signerVerifier \
             --member="serviceAccount:service-KEY_PROJECT_NUMBER@gcp-sa-privateca.iam.gserviceaccount.com" \
             --project=KEY_PROJECT_ID
         done
         

Replace `KEY_PROJECT_NUMBER` with the key project number from the output of the previous step.

This command is a `for` loop that iterates through the root CA keys, granting each role on that key to the CA Service service agent. If you used different names for the root CA keys, run these commands manually for each key.




## Set up CAs and keys on a new cluster

**Warning:** Deleting keys or CAs that are in use by the cluster might lead to irrecoverable clusters. Before you delete keys or CAs, ensure that your cluster no longer uses the resources.

After you create keys, CA pools, root CAs, and grant IAM roles to the GKE service agent, create a new cluster that uses these resources.

The flags that you specify in the cluster creation command require the following resource paths as values:

  * Path to a key version in Cloud KMS for the service account signing key that you created in Create keys. You specify this path for the `service-account-signing-keys` flag and for the `service-account-verification-keys` flag.
  * Path to each of the CA pools that you created in Create the CAs.

**Note:** Before you perform these steps, decide on whether you also want to encrypt your control plane boot disks and etcd disks with keys that you manage. If you do, perform all of the key configuration steps in [Encrypt etcd and control plane boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypt-etcd-control-plane-disks) and specify the optional flags described in the cluster creation command in this section.

To configure a new cluster to use your keys and CAs, do the following steps:

  1. Find the path to the latest enabled service account signing key version:
         
         gcloud kms keys versions list \
             --key=sa-signing-key \
             --keyring=KEY_RING_NAME \
             --location=LOCATION \
             --project=KEY_PROJECT_ID \
             --filter="STATE=ENABLED" --sort-by=~ --format="value(name)" | sed 1q
         

Replace `KEY_PROJECT_ID` with the project ID of the key project.

The output is similar to the following:
         
         projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1
         

  2. Find the paths to each of the CA pools that you created:
         
         gcloud privateca pools list --format="get(name)" \
             --project=KEY_PROJECT_ID
         

The output is similar to the following:
         
         projects/KEY_PROJECT_ID/locations/LOCATION/caPools/cluster-ca-pool
         projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-peer-ca-pool
         projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-api-ca-pool
         projects/KEY_PROJECT_ID/locations/LOCATION/caPools/aggregation-ca-pool
         

Ensure that the output contains all of the CA pools that you created for GKE.




### Create a cluster

In this section, you create a cluster with different options specified depending on which GKE control plane authority features you want to configure. You can only configure these features on a cluster during cluster creation. The following commands create Standard mode clusters. To create Autopilot mode clusters instead, use the same flags with the [`gcloud container clusters create-auto`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) command.

  * To only configure the CAs and keys that you created in this tutorial, run the following command:
        
        gcloud container clusters create example-cluster \
            --location=LOCATION \
            --project=CLUSTER_PROJECT_ID \
            --cluster-version=VERSION \
            --service-account-signing-keys=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1 \
            --service-account-verification-keys=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1 \
            --cluster-ca=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/cluster-ca-pool \
            --etcd-peer-ca=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-peer-ca-pool \
            --etcd-api-ca=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-api-ca-pool \
            --aggregation-ca=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/aggregation-ca-pool
        

Replace the following:

    * `CLUSTER_PROJECT_ID`: the project ID of the cluster project.
    * `VERSION`: the GKE version of the cluster. Must be 1.31.1-gke.1846000 or later.
  * To configure the CAs and keys as well as control plane boot disk encryption and etcd encryption, do the following:

    1. Perform all of the key configuration steps in [Encrypt etcd and control plane boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypt-etcd-control-plane-disks).
    2. Find the paths to each of the keys by using the instructions in [Use encryption keys in a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypt-etcd-control-plane-disks#use-encryption-keys-cluster).
    3. Create a cluster:
           
           gcloud container clusters create example-cluster \
               --location=LOCATION \
               --project=CLUSTER_PROJECT_ID \
               --cluster-version=VERSION \
               --service-account-signing-keys=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1 \
               --service-account-verification-keys=projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1 \
               --cluster-ca=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/cluster-ca-pool \
               --etcd-peer-ca=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-peer-ca-pool \
               --etcd-api-ca=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-api-ca-pool \
               --aggregation-ca=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/aggregation-ca-pool \
               --control-plane-disk-encryption-key=PATH_TO_DISK_KEY \
               --gkeops-etcd-backup-encryption-key=PATH_TO_ETCD_BACKUP_KEY
           

Replace the following:

       * `CLUSTER_PROJECT_ID`: the project ID of the cluster project.
       * `VERSION`: the GKE version of the cluster. Must be 1.31.1-gke.1846000 or later.
       * `PATH_TO_DISK_KEY`: the path to your disk encryption key.
       * `PATH_TO_ETCD_BACKUP_KEY`: the path to your etcd internal backup encryption key.

You can also use these flags when you create a new Standard mode cluster.




## Verify that the cluster uses your specified keys and CAs

This section shows you how to verify the keys and CAs that were used during cluster creation. You can perform this verification using Cloud Logging or by using the Google Cloud CLI.

### Use Logging to verify keys and CAs

To verify the keys and CAs using Logging, do the following:

  1. In the Google Cloud console, go to the **Logs Explorer** page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Specify the following query:
         
         resource.type="gke_cluster"
         resource.labels.cluster_name="CLUSTER_NAME"
         resource.labels.location="CLUSTER_LOCATION"
         protoPayload.serviceName="container.googleapis.com"
         protoPayload.methodName=~"google.container.v(1|1alpha1|1beta1).ClusterManager.CreateCluster"
         protoPayload.request.cluster.userManagedKeysConfig:*
         

`protoPayload.request.cluster.userManagedKeysConfig:*` filters the results for cluster creation logs that include keys and CAs that you manage.

  3. Click **Run query**.




In the results, expand your cluster creation log. Verify that the paths to keys and CAs are the same as those that you created for that cluster, like in the following example:
    
    
    # lines omitted for clarity
    userManagedKeysConfig: {
      aggregationCa: "projects/KEY_PROJECT_ID/locations/LOCATION/caPools/aggregation-ca-pool"
      clusterCa: "projects/KEY_PROJECT_ID/locations/LOCATION/caPools/cluster-ca-pool"
      etcdApiCa: "projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-api-ca-pool"
      etcdPeerCa: "projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-peer-ca-pool"
      serviceAccountSigningKeys: [
        0: "projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1"
      ]
      serviceAccountVerificationKeys: [
        0: "projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1"
      ]
    }
    

### Use the gcloud CLI to verify keys and CAs

To verify that the cluster uses the CAs and keys that you created, run the following command:
    
    
    gcloud container clusters describe example-cluster \
        --location=LOCATION \
        --project=CLUSTER_PROJECT_ID
    

The output should include the `userManagedKeysConfig` field like in the following example:
    
    
    # lines omitted for clarity
    userManagedKeysConfig:
      sa-signing-key: projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1
      sa-verification-key: projects/KEY_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/sa-signing-key/cryptoKeyVersions/1
      cluster-ca: projects/KEY_PROJECT_ID/locations/LOCATION/caPools/cluster-ca-pool
      etcd-peer-ca: projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-peer-ca-pool
      etcd-api-ca: projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-api-ca-pool
      aggregation-ca: projects/KEY_PROJECT_ID/locations/LOCATION/caPools/aggregation-ca-pool
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the projects

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

  1. Delete the cluster:
         
         gcloud container clusters delete example-cluster \
             --location=LOCATION \
             --project=CLUSTER_PROJECT_ID
         

  2. Disable the root CAs:
         
         gcloud privateca roots disable cluster-root-ca \
             --location=LOCATION \
             --pool=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/cluster-ca-pool \
             --project=KEY_PROJECT_ID
         
         gcloud privateca roots disable etcd-peer-root-ca \
             --location=LOCATION \
             --pool=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-peer-ca-pool \
             --project=KEY_PROJECT_ID
         
         gcloud privateca roots disable etcd-api-root-ca \
             --location=LOCATION \
             --pool=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-api-ca-pool \
             --project=KEY_PROJECT_ID
         
         gcloud privateca roots disable aggregation-root-ca \
             --location=LOCATION \
             --pool=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/aggregation-ca-pool \
             --project=KEY_PROJECT_ID
         

  3. Delete the root CAs:
         
         gcloud privateca roots delete cluster-root-ca \
             --location=LOCATION \
             --pool=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/cluster-ca-pool \
             --project=KEY_PROJECT_ID
         
         gcloud privateca roots delete etcd-peer-root-ca \
             --location=LOCATION \
             --pool=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-peer-ca-pool \
             --project=KEY_PROJECT_ID
         
         gcloud privateca roots delete etcd-api-root-ca \
             --location=LOCATION \
             --pool=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/etcd-api-ca-pool \
             --project=KEY_PROJECT_ID
         
         gcloud privateca roots delete aggregation-root-ca \
             --location=LOCATION \
             --pool=projects/KEY_PROJECT_ID/locations/LOCATION/caPools/aggregation-ca-pool \
             --project=KEY_PROJECT_ID
         

  4. Delete the CA pools:
         
         gcloud privateca pools delete cluster-ca-pool --location=LOCATION \
             --project=KEY_PROJECT_ID
         
         gcloud privateca pools delete etcd-peer-ca-pool --location=LOCATION \
             --project=KEY_PROJECT_ID
         
         gcloud privateca pools delete etcd-api-ca-pool --location=LOCATION \
             --project=KEY_PROJECT_ID
         
         gcloud privateca pools delete aggregation-ca-pool --location=LOCATION \
             --project=KEY_PROJECT_ID
         

  5. Delete the keys:
         
         gcloud kms keys versions destroy 1 \
             --location=LOCATION \
             --keyring=KEY_RING_NAME \
             --key=sa-signing-key \
             --project=KEY_PROJECT_ID
         
         gcloud kms keys versions destroy 1 \
             --location=LOCATION \
             --keyring=KEY_RING_NAME \
             --key=cluster-ca-key \
             --project=KEY_PROJECT_ID
         
         gcloud kms keys versions destroy 1 \
             --location=LOCATION \
             --keyring=KEY_RING_NAME \
             --key=etcd-peer-ca-key \
             --project=KEY_PROJECT_ID
         
         gcloud kms keys versions destroy 1 \
             --location=LOCATION \
             --keyring=KEY_RING_NAME \
             --key=etcd-api-ca-key \
             --project=KEY_PROJECT_ID
         
         gcloud kms keys versions destroy 1 \
             --location=LOCATION \
             --keyring=KEY_RING_NAME \
             --key=aggregation-ca-key \
             --project=KEY_PROJECT_ID
         




You can't delete key rings from Cloud KMS. However, key rings don't incur additional costs.

## What's next

  * [Track identity usage from the moment of issuance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-identity-issuance-usage)
  * [Rotate the CAs and service account signing keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-control-plane-cas-keys)
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
