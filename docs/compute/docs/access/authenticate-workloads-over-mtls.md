---
url: https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls/
title: Authenticate workloads to other workloads over mTLS \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:57:30.001735+00:00
---

# Authenticate workloads to other workloads over mTLS  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Authenticate workloads to other workloads over mTLS Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up automatic provisioning and lifecycle management of managed workload identities for Compute Engine. You configure CA pools to issue certificates using [Certificate Authority Service (CA)](https://docs.cloud.google.com/certificate-authority-service), which is a highly-available, scalable Google Cloud service that simplifies and automates the deployment, management, and security of CA services. Each VM is provisioned with X.509 credentials from the configured CA pool. These credentials can then be used to establish mTLS connections.

## Before you begin

  * Review the [Managed workload identities overview](https://docs.cloud.google.com/iam/docs/managed-workload-identity) documentation. 
  * Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable compute.googleapis.com




### Required roles

To get the permissions that you need to create VMs that use managed workload identity certificates for authentication to other workloads, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

With managed workload identities for Compute Engine, you can implement mutually authenticated and encrypted communications between any two Compute Engine VMs. Workload applications running on the configured VMs can use the X.509 credentials for per-VM [mTLS](https://docs.cloud.google.com/load-balancing/docs/mtls). The [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) automatically rotates these mTLS certificates and refreshes credentials on the VM.

By using managed workload identities, you can centrally administer identity for your workloads. Compute Engine VMs can be authorized to receive a workload identity that is based on key attributes, such as the instance ID, instance name, or the attached service account. For the workloads to be attested, the compute administrator or developer must create VM instances for the workload with a matching instance name, instance ID, service account name, or service account ID.

Managed workload identities conforms to the open source [Secure Production Identity Framework for Everyone (SPIFFE) standard](https://spiffe.io/docs/latest/spiffe-about/overview/). SPIFFE IDs for Google Cloud workloads are in the following format: `spiffe://<TRUST_DOMAIN/ns/NAMESPACE/sa/WORKLOAD_ID`. The `TRUST_DOMAIN` corresponds to an Identity and Access Management (IAM) workload identity pool.

Managed workload identities are defined within a [_workload identity pool_](https://docs.cloud.google.com/iam/docs/managed-workload-identity#workload_identity_pools), which acts as a top-level container to hold workload identities that have a common trust boundary. Under a workload identity pool, identities are organized into administrative boundaries called _namespaces_. For a workload to get a managed identity, you must define attestation policies to authorize it. A workload attestation policy ensures that only trusted workloads can assert a managed identity.

To use managed workload identities for your applications, you must perform the following tasks:

  1. **Security Administrator** :

     * [Create managed workload identities](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute#configure_identities) in a workload identity pool.
     * [Define the workload attestation policy](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute#define_the_workload_attestation_policy).
     * [Configure Certificate Authority Service to issue certificates for managed workload identities](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute#configure_ca).
     * [Authorize managed workload identities to request certificates from the CA pool](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute#grant-role-ca-pool).
     * [Define the trust and certificate issuance configuration within the workload identity pool](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute#define_partner_metadata).
  2. **Compute Administrator** :

     * Configure instances to use workload identities for individual Compute Engine instances
     * Access workload credentials on a Linux instance.



## Configure managed workload identities in Identity and Access Management

  * Follow the instructions in [Configure managed workload identities authentication ](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities).

These instructions detail how to complete the following:

    * Create a workload identity pool.
    * Create namespaces in the workload identity pool. You use the namespaces to create administrative boundaries for your managed workload identities, for example, a namespace for each of the applications owned by your organization.
    * Create a managed workload identity in a namespace in the workload identity pool. For example, you might create a namespace for an application and create managed identities within that namespace for the microservices that support that application.
    * Optional: Create a service account to create attestation rules based on service account ID.
    * Create a workload attestation policy that allows your workload to be issued credentials for the managed workload identity. Compute Engine VMs can be authorized to receive a managed workload identity based on key attributes such as the instance ID, instance name, or the attached service account.
    * Configure Certificate Authority Service to issue certificates for managed workload identities: 
      * Configure the root CA pool
      * Configure the subordinate CAs
      * Authorize the managed workload identity pool to request certificates from the CA pool



## Enable managed workload identities for individual compute instances

You can enable managed workload identities for a compute instance either when creating the instance or by updating the configuration for an existing instance.

### Create instances with managed workload identities enabled

When you create a compute instance, to enable the managed workload identities feature for the instance, you must do the following:

  * If the attestation of the instance for the workload identity is based on a service account, then specify that service account
  * Include the `--identity` and `--identity-certificate` flags




###  gcloud 

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/create) to create a new instance.

  1. If you're using a service account for attestation, include the service account information when creating the instance.

You can add additional lines to the command to configure the instance, such as the machine type and image, instead of using the default values. For more information, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
         
         gcloud compute instances create INSTANCE_NAME \
            --zone=INSTANCE_ZONE \
            --service-account SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
            --identity=TRUST_DOMAIN/ns/NAMESPACE/sa/WORKLOAD_IDENTIFIER \
         
            --identity-certificate \
         ...
         

Replace the following:

     * `INSTANCE_NAME`: a unique name for the instance. For details on valid instance names, see [Name resources](https://docs.cloud.google.com/compute/docs/naming-resources).
     * `INSTANCE_ZONE`: the zone to create the instance in.
     * `SERVICE_ACCOUNT_NAME`: the name of the service account that is allowed to receive the managed workload identity.
     * `PROJECT_ID`: the ID of the project where the service account was created.
     * `TRUST_DOMAIN`: the ID for the trust domain, in the following format: 
           
           $POOL_ID.global.$PROJECT_NUMBER.workload.id.goog
             

The trust domain value uses the following placeholders:

       * `POOL_ID`: the name of the workload identity pool
       * `PROJECT_NUMBER`: the project number for the project in which the workload identity pool was created
     * `NAMESPACE`: the name of the namespace that contains the workload attestation policy that authorizes the workload to assert a managed workload identity
     * `WORKLOAD_IDENTIFIER`: the name of the managed workload identity that was created in the namespace of the workload identity pool
  2. Enable automatic managed workload identities provisioning using the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) by updating the setting in the [guest agent configuration file](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#mwlid).




### Enable managed workload identities on existing instances

To enable managed workload identities for an existing compute instance, update the instance to configure the following:

  * If the attestation of the instance for the workload identity is based on a service account and the instance doesn't already have an attached service account, then create and attach a service account to the instance.
  * Enable the feature using the `--identity-certificate` flag and specify which managed workload identity to use with the `--identity` flag.
  * Restart the VM.




###  gcloud 

Use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update) to update the configuration for an instance.

  1. If the instance doesn't already have an attached service account, [attach the service account to the instance](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes).

  2. Update the configuration for an existing instance to enable managed workload identities.
         
         gcloud compute instances update INSTANCE_NAME \
            --zone=ZONE \
            --identity-certificate \
            --identity=TRUST_DOMAIN/ns/NAMESPACE/sa/WORKLOAD_IDENTIFIER
         

Replace the following:

     * `INSTANCE_NAME`: the instance name
     * `ZONE`: the zone where the instance is located
     * `TRUST_DOMAIN`: the ID for the trust domain, in the following format: `none $POOL_ID.global.$PROJECT_NUMBER.workload.id.goog`

The trust domain value uses the following placeholders: * `POOL_ID`: the name of the workload identity pool * `PROJECT_NUMBER`: the project number for the project in which the workload identity pool was created \+ `NAMESPACE`: the name of the namespace that contains the workload attestation policy that authorizes the workload to assert a managed workload identity \+ `WORKLOAD_IDENTIFIER`: the name of the managed workload identity that was created in the namespace of the workload identity pool

  3. Enable automatic managed workload identities provisioning using the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) by updating the setting in the [guest agent configuration file](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#mwlid).

  4. Stop the VM.
         
         gcloud compute instances stop INSTANCE_NAME \
            --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the instance name
     * `ZONE`: the zone where the instance is located
  5. Start the VM.
         
         gcloud compute instances start INSTANCE_NAME \
            --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the instance name
     * `ZONE`: the zone where the instance is located



## Access workload credentials on a Linux VM

After you create and start a compute instance that uses managed workload identities, the Google Cloud infrastructure (including the [Guest Agent](https://docs.cloud.google.com/compute/docs/images/guest-agent)) automatically provisions and manages the rotation of the credentials for the instance.

The workload certificates, including the private key and trust bundles, are placed into a specific directory on the VM's file system: `/var/run/secrets/workload-spiffe-credentials`. Applications can read the certificates, private key and the trust bundle from the file system directly to establish mTLS connections.

**Note:** Your application code must verify that the private key and certificate file are consistent before using them to establish mTLS connection. A mismatch between the private key and certificate can happen if the Compute Engine guest agent refreshes the credentials from the metadata server (MDS) in the time between the app reading the private key PEM file and the certificates PEM file or the other way around. For example, apps written in Golang can use the [`tls.LoadX509KeyPair` method](https://pkg.go.dev/crypto/tls#LoadX509KeyPair) to check for consistency between the public and private key pair.

The Compute Engine guest agent on the guest OS runs a workload refresh job and, if needed, creates the directory `/var/run/secrets/workload-spiffe-credentials`. The directory permissions are set to `0755 (rwxr-xr-x)`.

The directory contains the following files created with `0644 (rw-r--r--)` permissions:

  * `private_key.pem`: a PEM-formatted private key
  * `certificates.pem`: a bundle of PEM-formatted X.509 certificates that can be presented to other VMs as the client certificate chain, or used as a server certificate chain.
  * `ca_certificates.pem`: a bundle of PEM-formatted X.509 certificates to use as trust anchors when validating the certificates of peers.

**Note:** `ca_certificates.pem` contains certificates for the local SPIFFE trust domain for the VM, which is:
        
        spiffe://POOL_ID.global.PROJECT_NUMBER.workload.id.goog
        

  * `config_status`: a log file containing error messages.




## Refreshing the credentials and trust bundle

The Compute Engine control plane automatically rotates the managed workload identity credentials and the trust anchors periodically.

If your applications use the file system to access the workload credentials and trust bundle, the Compute Engine guest agent automatically refreshes the credentials and the trust bundle, for example, when the mTLS certificates are rotated.

## Update certificate issuance and trust config

You can modify the certificate issuance config and trust config for a VM that uses managed workload identities.

**Caution:** Updating the certificate issuance config and trust config for a workload identity pool affects all VMs in the workload identity pool.

### Update the workload identity pool configs for a set of VMs

**Note:** Only the certificate issuance config and trust config values can be updated. The managed workload identity can't be changed after you create a compute instance.

To update the certificate issuance config and trust config for a set of VMs, you update the workload identity pool. Use the [`gcloud iam workload-identity-pools update` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update), as shown in the following example:
    
    
    gcloud iam workload-identity-pools update WORKLOAD_IDENTITY_POOL_ID \
        --location="global" \
        --inline-certificate-issuance-config-file=CIC_JSON_FILE_PATH \
        --inline-trust-config-file=TC_JSON_FILE_PATH \
        --project=PROJECT_ID
    

Replace the following:

  * `WORKLOAD_IDENTITY_POOL_ID`: The ID of the workload identity pool.
  * `CIC_JSON_FILE_PATH`: The path to the new JSON-formatted certificate issuance config file (`cic.json`).
  * `TC_JSON_FILE_PATH`: Optional: The path to the new JSON-formatted trust config file (`tc.json`). If your workloads authenticate across different trust domains, you must specify this file. Otherwise you can omit the `--inline-trust-config` setting.
  * `PROJECT_ID`: Your Google Cloud project name.



Updates to the workload identity pool's certificate issuance config and trust config roll out gradually across the Compute Engine VMs and MIGs participating in the workload identity pool.

## Troubleshoot

To find methods for diagnosing and resolving common errors related to retrieving workload credentials, refer to the [Troubleshoot workload to workload authentication](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-workload-to-workload-auth) documentation.

To troubleshoot issues with misconfigured pools or attestation policies, see the [audit logs for workload identity pools](https://docs.cloud.google.com/iam/docs/audit-logging#google.iam.v1.WorkloadIdentityPools).

## What's next

  * Learn more about the following concepts: 
    * [Authenticate to Compute Engine](https://docs.cloud.google.com/compute/docs/authentication)
    * [Configure managed workload identity authentication](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities)
    * [Compute Engine guest agent](https://docs.cloud.google.com/compute/docs/images/guest-environment)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
