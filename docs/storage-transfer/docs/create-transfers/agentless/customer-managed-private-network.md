---
url: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/customer-managed-private-network/
title: Transfer from AWS or Azure over a customer-managed private network \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:00.368287+00:00
---

# Transfer from AWS or Azure over a customer-managed private network  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/docs/create-transfers/agentless/customer-managed-private-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)



Send feedback 

#  Transfer from AWS or Azure over a customer-managed private network Stay organized with collections  Save and categorize content based on your preferences. 

A private network connection, established using either Google Cloud Cross-Cloud Interconnect or Partner Interconnect, can offer significant advantages for data transfer between AWS or Azure and Cloud Storage:

  * **Potential cost optimization** : Potentially achieve egress cost savings. This can be beneficial for customers with existing interconnects or those performing large or recurring data transfers, leading to substantial long-term savings.
  * **Dedicated network bandwidth** : Using an interconnect can offer consistent, high-capacity throughput and lower latency, which is crucial for large, time-sensitive migrations and real-time data synchronization.
  * **Meet compliance needs** : Ideal for workloads where regulatory requirements mandate keeping data off the public internet. This feature helps you transfer data privately using the interconnect to achieve compliance, support data sovereignty, and simplify audits.



## Overview

This document walks you through the steps to:

  * Order and configure a Cross-Cloud Interconnect
  * Create an endpoint in S3 or Azure
  * Set up a regional internal proxy Network Load Balancer with hybrid connectivity
  * Register your load balancer with Service Directory
  * Create a transfer
  * Confirm that traffic is using the interconnect



## Required permissions

You'll need specific permissions to complete each of the following sections. These permissions are listed in the documentation for that set of steps.

## Interconnect options

Storage Transfer Service can transfer data from AWS and Azure over [Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview) (CCI) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview).

The steps below are specific to CCI, but also apply when configuring networking for Partner Interconnect.

## Order and configure a Cross-Cloud Interconnect

A Cross-Cloud Interconnect is a dedicated physical connection between Google Cloud and other cloud providers.

If you already have a CCI connection, skip to the next section.

###  AWS 

Follow the instructions to [Connect to Amazon Web Services](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/connectivity-overview) to order and configure a new Cross-Cloud Interconnect. You'll need the correct permissions to configure networking in Google Cloud as well as in AWS.

Watch a video covering the steps to order and configure a CCI [between AWS and Google Cloud](https://www.youtube.com/watch?v=W-fVLyCQ2kA).

###  Azure 

Follow the instructions to [Connect to Microsoft Azure](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/azure/connectivity-overview) to order and configure a new Cross-Cloud Interconnect. You'll need the correct permissions to configure networking in Google Cloud as well as in Azure.

Watch a video covering the steps to order and configure a CCI [between Azure and Google Cloud](https://www.youtube.com/watch?v=etFWwgrGU8g).

If your Cloud Storage bucket is a regional bucket, you should configure the CCI in the same region as your bucket to reduce network latency.

## Create an endpoint in S3 or Azure

Create an endpoint in your S3 or Azure account.

###  AWS 

In your Amazon Web Services account, create a VPC endpoint that connects to S3.

Follow these AWS instructions: [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) to create the endpoint.

###  Azure 

Configure a Private Endpoint on the Storage Account in Azure following [these steps](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints).

Storage Transfer Service requires the `*.blob.core.windows.net` endpoint. The `*.dfs.core.windows.net` endpoint is not supported.

Once created, note the endpoint's IP address. You'll need to specify the IP address when creating your load balancer in the next section.

## Set up a regional internal proxy Network Load Balancer with hybrid connectivity

In Google Cloud, set up a regional internal proxy Network Load Balancer with hybrid connectivity. This provides an internal IP address that's restricted to clients running in the same VPC network as the load balancer, and that routes traffic to the S3 VPC endpoints or Azure Storage private endpoints that you created in the previous section.

You should create the load balancer in the same project and VPC network as the VLAN attachment which interfaces with the Cloud Interconnect. While the interconnect itself can be in a different project within the same organization, the attachment must be in the same VPC and region as the load balancer.

  * [Set up a regional internal proxy Network Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid#setup-google-environment)



Specify the S3 VPC endpoint or Azure Storage private endpoint IP address when you reach the steps labeled **Add endpoints to the hybrid connectivity NEG**.

Note the NLB's frontend IP address and port, as you'll need to specify them in the next section.

### Validate the connection

Before proceeding, we recommend that you validate that the load balancer can connect to the remote storage endpoint.

To do so:

  1. Create a Compute Engine VM in the same VPC network as your load balancer.
  2. From the VM, use `curl` to test connectivity to the load balancer's IP address and port:
         
         curl -v --resolve HOSTNAME:PORT:LOAD_BALANCER_IP https://HOSTNAME
         

Replace the following:

     * HOSTNAME is the hostname of your source storage provider. 
       * For AWS S3, use the S3 API endpoint for your bucket's region, for example `s3.us-west-1.amazonaws.com`.
       * For Azure Storage, use your storage account's blob endpoint, for example `mystorageaccount.blob.core.windows.net`.
     * PORT is the port you configured on the load balancer's forwarding rule, typically `443`.
     * LOAD_BALANCER_IP is the frontend IP address of your load balancer.



A response from the remote endpoint, even an error, indicates that connectivity is successful. A connection timeout indicates a misconfiguration in your network setup that you should resolve before continuing.

## Register your NLB with Service Directory

Register the NLB in Service Directory. Storage Transfer Service uses Service Directory to resolve the address of the load balancer and connect to it directly.

Follow the instructions to [register an internal load balancer](https://docs.cloud.google.com/service-directory/docs/configuring-ilb-in-sd). Use the IP address and port of the load balancer that you created when specifying the forwarding rule.

Once created, note the self-link of the service. It uses the format `projects/{project_id}/locations/{location}/namespaces/{namespace}/services/{service}`. You'll need this value when creating the transfer job.

## Create a transfer

Grant the following permissions to the [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents). For instructions on retrieving the service agent, and granting permissions to the service agent, see [Service agent permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud#service_agent_permissions).

  * Service Directory Viewer ([roles/servicedirectory.viewer](https://docs.cloud.google.com/service-directory/docs/access-control#servicedirectory.viewer)) at the project level, on the project containing the Service Directory Resources.
  * Private Service Connect Authorized Service ([roles/servicedirectory.pscAuthorizedService](https://docs.cloud.google.com/service-directory/docs/access-control#servicedirectory.pscAuthorizedService)) at the project level, on the project containing the VPC.
  * Storage Legacy Bucket Writer ([roles/storage.legacyBucketWriter](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.legacyBucketWiter)) on the destination bucket.

**Note:** If you're [delegating service agent permissions to a user-managed service account](https://docs.cloud.google.com/storage-transfer/docs/delegate-service-agent-permissions#gcloud_1), grant these permissions to the user-managed service account.

To create a transfer job that uses a Cross-Cloud Interconnect, you must use the Storage Transfer Service REST API. Send a request as follows. Note the `privateNetworkService` field, which is where you'll specify your Service Directory service's selfLink.

###  AWS 
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    
    {
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
        "awsS3DataSource": {
            "privateNetworkService": "SERVICE_SELF_LINK",
            "bucketName": "S3_BUCKET_NAME",
            "awsAccessKey": {
              "accessKeyId": "ACCESS_KEY_ID",
              "secretAccessKey": "SECRET_ACCESS_KEY"
            }
        },
        "gcsDataSink": {
            "bucketName": "GCS_BUCKET_NAME"
        }
      }
    }
    

###  Azure 
    
    
    POST https://storagetransfer.googleapis.com/v1/transferJobs
    
    {
      "status": "ENABLED",
      "projectId": "PROJECT_ID",
      "transferSpec": {
          "azureBlobStorageDataSource": {
              "privateNetworkService": "SERVICE_SELF_LINK",
              "storageAccount": "AZURE_SOURCE_NAME",
              "container": "AZURE_CONTAINER",
              "azureCredentials": {
                  "sasToken": "AZURE_SAS_TOKEN",
              }
          },
          "gcsDataSink": {
              "bucketName": "GCS_BUCKET_NAME"
          }
      }
    }
    

Replace the following:

  * SERVICE_SELF_LINK is the self-link of the Service Directory service. It uses the format `projects/{project_id}/locations/{location}/namespaces/{namespace}/services/{service}`.



For information about other fields, see the [transferSpec reference documentation](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/TransferSpec).

## Confirm that traffic is using the interconnect

Use **Cloud Monitoring** to verify traffic flowing through your interconnect from AWS or Azure.

  1. In the Google Cloud Console, go to **Hybrid Connectivity > Cloud Interconnect**.
  2. Select the VLAN attachment that connects to your AWS/Azure environment.
  3. On the details page for your connection, select the **Monitoring** tab. Look for metrics that indicate data transfer. Specifically: 
     * **Ingress Bytes:** This metric shows the data coming from AWS or Azure into your Google Cloud VPC.
     * **Operational Status:** Ensure that both the physical connection and the BGP session are in a healthy, operational state.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
