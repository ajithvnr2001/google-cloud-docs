---
url: https://docs.cloud.google.com/dataproc-metastore/docs/network-access/
title: Configuring Network Access for Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:21.342259+00:00
---

# Configuring Network Access for Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/network-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Configuring Network Access for Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

This page provides detailed guidance on configuring network access for your Dataproc Metastore instances. Correct network setup is essential for Managed Service for Apache Spark clusters and Managed Service for Apache Spark workloads to securely and privately communicate with your managed Dataproc Metastore service.

For a more general overview of networking concepts, see [Networking Overview](https://docs.cloud.google.com/dataproc-metastore/docs/networking)

## Key Networking Concepts

Dataproc Metastore instances typically reside within a Google-managed service producer network and communicate with your Virtual Private Cloud (VPC) network using private connectivity. Understanding the following concepts is crucial for a successful setup:

  * **Shared Virtual Private Cloud:** If your Managed Service for Apache Spark clusters or Managed Service for Apache Spark workloads are in a service project that uses a Shared VPC network from a host project, verify the appropriate network configurations are made in the host project. For more information, see [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc).
  * **Private Google Access:** Dataproc Metastore instances often rely on Private Google Access for private communication with your VPC network. This allows Virtual Machine (VM) instances in your VPC to connect to Google APIs and services using internal IP addresses. For more information, see [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).
  * **VPC Network Peering:** This mechanism enables private IP connectivity between two VPC networks, allowing resources in one network to communicate with resources in the other using internal IP addresses. Dataproc Metastore establishes a managed VPC Network Peering connection to your VPC network as part of its setup. For more information, see [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).
  * **Firewall Rules:** Proper firewall rules are necessary to permit traffic between your Managed Service for Apache Spark workloads and the Dataproc Metastore instance.
  * **Cloud DNS Resolution:** Verify that DNS resolution is correctly configured within your VPC network to resolve the Dataproc Metastore endpoint URI to its private IP address.



## Configuration Steps

To verify proper network access for your Dataproc Metastore instance, follow these steps:

### 1\. Configure Private Service Access

Dataproc Metastore uses Private Service Access to establish a private connection between your VPC network and the Google-managed service producer network where your Dataproc Metastore instance resides.

  * **Verify Private Service Access Connection:**
    1. In the Google Cloud console, go to **Virtual Private Cloud network > VPC Network Peering**.
    2. Verify that a peering connection named `servicenetworking-googleapis-com` exists and its state is `ACTIVE`.
    3. If this connection is missing or not active, follow the instructions in [Configuring Private Service Access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access). This includes allocating an IP address range for the service producer network.



### 2\. Configure Firewall Rules

Verify that firewall rules in your VPC network (or the Shared VPC host project, if applicable) allow necessary traffic.

  * **Egress Rule from Workload to Metastore:**
    * Verify that an egress firewall rule allows outbound TCP traffic from your Managed Service for Apache Spark cluster or Managed Service for Apache Spark workloads to the IP address range of your Dataproc Metastore instance on port `9083`. This is the default port for Hive Metastore.
    * If using Private Service Access, this traffic will be routed privately.
  * **Ingress Rules (less common for client-to-Metastore):**
    * Generally, you don't need to configure ingress rules on your VPC for traffic _from_ the Dataproc Metastore instance _to_ your workload, as communication typically originates from the workload. However, verify no overly restrictive ingress rules are inadvertently blocking necessary responses.



### 3\. Verify DNS Resolution

Your Managed Service for Apache Spark workloads need to resolve the Dataproc Metastore endpoint URI to its private IP address.

  * **DNS Peering or Private Zones:** If you are using custom DNS servers or private Cloud DNS zones, verify that DNS queries for the Dataproc Metastore endpoint (for example, `your-metastore-endpoint.us-central1.dataproc.cloud.google.com`) are correctly forwarded or resolved to the private IP range used by Private Service Access.
  * **Testing DNS Resolution:** From a VM within the same subnet as your Managed Service for Apache Spark workload, use `nslookup` or `dig` to verify that the Dataproc Metastore endpoint resolves to a private IP address.



## Troubleshooting Network Connectivity

If you encounter connectivity issues after configuring network access, consider the following troubleshooting steps:

  * **Review Dataproc Metastore Status:** Verify that your Dataproc Metastore instance is in a `HEALTHY` state in the Google Cloud console.
  * **Check Cloud Logging:** Examine Cloud Logging for your Dataproc Metastore instance and related Managed Service for Apache Spark workloads for network-related error messages or connection timeouts.
  * **Use Network Intelligence Center Connectivity Tests:** Use Google Cloud's [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) to diagnose the network path from your Managed Service for Apache Spark workload's VMs to the Dataproc Metastore endpoint.
  * **Refer to General Troubleshooting:** For more detailed network diagnostics, refer to: 
    * [Troubleshooting Managed Service for Apache Spark Cluster Creation Failures](https://docs.cloud.google.com/dataproc/docs/cluster-creation-failures)
    * [Troubleshooting Managed Service for Apache Spark Batch Creation Failures](https://docs.cloud.google.com/dataproc-serverless/docs/batch-creation-failures)
    * [Troubleshooting Dataproc Metastore Connectivity](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting-connectivity)



## What's next

  * Learn more about [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs).
  * Review [Managed Service for Apache Spark networking options](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network).
  * Understand [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
