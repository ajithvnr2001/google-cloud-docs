---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/install-configure-storage-cli/
title: Install and configure storage CLI \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:32:55.281081+00:00
---

# Install and configure storage CLI  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/install-configure-storage-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Install and configure storage CLI Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through how to install and configure the gdcloud CLI for managing object storage when working with Google Distributed Cloud (GDC) air-gapped projects. It covers how to download, install, and configure the necessary components and settings essential for effectively using storage buckets and objects in this isolated environment.

This page is for audiences such as IT admins within the infrastructure operator group or developers within the application operator group who are looking to provision and manage object storage buckets for projects within GDC air-gapped environments. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To install and configure the storage CLI, contact your Organization IAM Admin to request the **Org Network Policy Admin** (`org-network-policy-admin`) role, which lets you create, edit, and delete organization network policies.

## Download the gdcloud CLI

Follow the instructions to [download the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download).

## Install the gdcloud CLI

To use the storage command tree, the storage dependencies component must be installed.

  1. Follow [Install gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).

  2. To install the storage dependencies component, run the following commands:
         
         gdcloud components install storage-cli-dependencies
         

For more information on the `components install` command, see [Install gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).


**Note:** This command only installs the dependencies onto the client machine. For configuring the gdcloud CLI follow Configure gdcloud CLI for object storage.

## Configure the gdcloud CLI for object storage

The following configurations must be set to use the gdcloud CLI for object storage.

  1. Replace `ACCESS_KEY_ID` with the access key ID obtained from the secret in [getting access credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#getting_bucket_access_credentials):
         
         gdcloud config set storage/s3_access_key_id ACCESS_KEY_ID
         

  2. Replace `SECRET_ACCESS_KEY` with the secret key obtained from the secret in [getting access credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#getting_bucket_access_credentials):
         
         gdcloud config set storage/s3_secret_access_key SECRET_ACCESS_KEY
         

  3. Replace `CA_BUNDLE_FILE` with the path to the CA Certificate. This is a digital certificate that belongs to a Certificate Authority (CA), a trusted organization that vouches for identities. You can request the GDC CA trust bundle from a member of your infrastructure operator (IO) group. For more information on obtaining GDC CA certificates, see [Fetch GDC trust bundles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/fetch-trust-bundles).
         
         gdcloud config set storage/s3_custom_ca_certs_file CA_BUNDLE_FILE
         

**Note:** If the CA Certs for GDC are already installed on the environment then you can set this to `/etc/ssl/certs/ca-certificates.crt`
  4. Replace `ENDPOINT` with the endpoint your Infrastructure Operator (IO) provides:
         
         gdcloud config set storage/s3_endpoint ENDPOINT
         

**Note:** This is the full endpoint beginning with `https://`.

This step differs slightly for dual-zone buckets. Each dual-zone bucket provides three endpoints that you can choose to access the bucket. For most situations, the global endpoint is appropriate in order to take advantage of automatic failovers:

     * Zone1 endpoint: This endpoint is always received by zone1. If using this endpoint, you have read-after-write consistency for any objects written to zone1. However, if zone1 goes down, a client needs to change to using either the zone2 or global endpoint to continue reading/writing to this bucket. If the client is coming from a user cluster, then this endpoint will only be accessible from within zone1.
     * Zone2 endpoint: This endpoint is always received by zone2. If using this endpoint, you have read-after-write consistency for any objects written to zone2. However, if zone2 goes down, a client needs to change to using either the zone1 or global endpoint to continue reading/writing to this bucket. If the client is coming from a user cluster, then this endpoint will only be accessible from within zone2.
     * Global endpoint: This endpoint results in your request being routed to either zone1 or zone2. This option doesn't provide session affinity, meaning that requests made using the same session may arrive in either zone1 or zone2. This means that there is no read-after-write guarantee for requests made to the global endpoint. The global endpoint provides automatic failover in the event that a zone goes down, so users won't have to change endpoints in their workloads the way they would need to if using the zonal endpoint. In addition, this endpoint is accessible from user clusters in all zones.

Run the following commands against the management API server to view the global and zonal endpoints for your bucket and choose the one you want to use:
    
    kubectl get buckets BUCKET_NAME -n PROJECT_NAME -o jsonpath="{.status.globalEndpoint}" --kubeconfig MANAGEMENT_API_SERVER
    
    kubectl get buckets BUCKET_NAME -n PROJECT_NAME -o jsonpath="{.status.zonalEndpoints}" --kubeconfig MANAGEMENT_API_SERVER
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
