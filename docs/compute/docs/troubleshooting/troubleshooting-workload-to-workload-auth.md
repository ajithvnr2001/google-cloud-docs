---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-workload-to-workload-auth/
title: Troubleshoot workload to workload authentication \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:46.693919+00:00
---

# Troubleshoot workload to workload authentication  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-workload-to-workload-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot workload to workload authentication Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to troubleshoot common errors related to [Authenticate workloads to other workloads over mTLS](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls).

For additional information, see [Troubleshoot Workload Identity Federation](https://docs.cloud.google.com/iam/docs/troubleshooting-workload-identity-federation).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## The generated credentials directory doesn't exist

If you get an error that the `/var/run/secrets/workload-spiffe-credentials` directory doesn't exist, do the following:

  1. Ensure that your compute instance supports workload-to-workload authentication by using one of the following interfaces to verify that managed workload identities are enabled:

###  Console 

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. In the **Name** column of the **VM instances** page, click the instance name to view additional details about the instance.

     3. In the **Security and access** section of the **Details** page, verify that "Workload identity certificates" has a value of "Enabled".

###  gcloud 

To view whether the managed workload identities feature is enabled for a compute instance, use the [`gcloud alpha compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/describe).
    
    gcloud alpha compute instances describe INSTANCE_NAME \
        --zone=ZONE \
        --format="table(name,zone,identityCertificate)"
    

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

     * `ZONE`: the zone where the instance is located.

###  REST 

To view the details of a compute instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/alpha/instances/get). By appending a `$fields` query parameter to the request, you can restrict the output to just the fields of interest.
    
    GET https://compute.googleapis.com/compute/alpha/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME$fields=name,identityCertificate,identity
    

Replace the following:

     * `PROJECT_ID`: the ID of the project where the instance is located

     * `ZONE`: the zone where the instance is located

     * `INSTANCE_NAME`: the name of the instance

  2. Review the instance values for `identityCertificate` and `identity`.

  3. If the `identityCertificate` property is set to `false`, then this compute instance doesn't support this feature.

To resolve this issue, create a new instance that supports workload-to-workload authentication. For details, see [Enable managed workload identities on existing VMs](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#add-workload-id-existing-vms).

  4. Ensure that the VM is running a guest OS with Compute Engine guest agent version 20231103.01 or newer. Use the gcloud CLI to [view the serial-port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output) to determine the current Compute Engine guest agent version:
         
         gcloud compute instances get-serial-port-output INSTANCE_NAME | grep "GCE Agent Started"
         

Replace INSTANCE_NAME with the name of the compute instance.

To update the Compute Engine guest agent, see [Updating the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest).

  5. Check the service logs to verify that the `gce-workload-cert-refresh.timer` systemd timer was able to successfully fetch the workload credentials and the trust bundle.

**Note:** For guest agent version `20250901.00` and later, the workload refresh service is included with the guest agent's core plugin, not a separate service. For more information about this version, see the [Guest environment release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#September_03_2025).
         
         # View timer logs to see when the gce-workload-cert-refresh.timer last ran
         journalctl -u gce-workload-cert-refresh.timer
         
         # View service logs from gce-workload-cert-refresh.service
         journalctl -u gce-workload-cert-refresh.service
         




## The generated credentials directory contains only the config_status file

The generated credentials directory, `/var/run/secrets/workload-spiffe-credentials`, might contain only the `config_status` for a variety of reasons. Use the following steps to troubleshoot this issue.

  1. Check the contents of the `config_status` file to ensure that the managed workload identities feature is enabled. If the feature is not enabled using the appropriate values, the log file contains the error message `workload certificate feature not enabled`.

To resolve this issue, create a new compute instance that supports workload to workload authentication, using one of the following methods:

     * [Enable managed workload identities for a MIG](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#create-workload-id-migs).
     * [Enable managed workload identities for individual VMs](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#enable-workload-id-vms).
  2. Check the contents of the `config_status` file to ensure that there are no errors due to missing attribute values or invalid configuration for the certificate issuance or the trust config. If such errors exist, update the configuration values by following the steps in [Update certificate issuance and trust config](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#update_trust_config).

  3. Ensure that the correct permissions were granted to the managed workload identities in the workload identity pool for accessing the subordinate CA pools. Use the following command:
         
         gcloud privateca pools get-iam-policy SUBORDINATE_CA_POOL_ID \
            --location=SUBORDINATE_CA_POOL_REGION
         

Replace the following:

     * SUBORDINATE_CA_POOL_ID: the ID for the subordinate CA pool.
     * SUBORDINATE_CA_POOL_REGION: the region of the subordinate CA pool.

The output of this command should contain the following:
    
    bindings:
    - members:
      - principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/POOL_ID/*
      -
      role: roles/privateca.poolReader
    - members:
      - principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/name/locations/global/workloadIdentityPools/POOL_ID/*
      role: roles/privateca.workloadCertificateRequester
    

In the previous example:

     * PROJECT_NUMBER is the project number of your project.
     * POOL_ID is the ID of the workload identity pool.

If you don't see output similar to the preceding example, grant the required permissions as described in [Authorize managed workload identities to request certificates from the CA pool](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute#grant-role-ca-pool).

  4. If the `config_status` file contains no error messages, then check the value of `iam.googleapis.com/workload-identity` within the file.The value should match the following:
         
         spiffe://POOL_ID.global.PROJECT_NUMBER.workload.id.goog/ns/NAMESPACE_ID/sa/MANAGED_IDENTITY_ID
         

In the previous example:

     * PROJECT_NUMBER is the project number for the project that contains the managed workload identity pool.
     * POOL_ID is the ID of the workload identity pool.
     * NAMESPACE_ID is the ID of the namespace in the workload identity pool.
     * MANAGED_IDENTITY_ID is the ID of the managed workload identity.

If the value for `iam.googleapis.com/workload-identity` is incorrect, then you must create a new compute instance with the correct value because the managed identity value can only be updated during instance creation.

  5. If the `config_status` file contains no error messages, then ensure that the trust config contains a valid entry for the SPIFFE trust domain `POOL_ID.global.PROJECT_NUMBER.workload.id.goog`, which corresponds to the SPIFFE trust domain on the managed identity assigned to the compute instance. For more information, see [Define the trust config](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-compute#define_trust_config).

  6. If the `config_status` file contains any error messages with the error code `INTERNAL_ERROR`, reach out to Cloud Customer Care or your Google Cloud contact with the error message.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
