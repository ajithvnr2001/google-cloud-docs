---
url: https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting-connectivity/
title: Troubleshooting Dataproc Metastore Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:38.323317+00:00
---

# Troubleshooting Dataproc Metastore Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Troubleshooting Dataproc Metastore Connectivity Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on diagnosing and resolving common connectivity issues when connecting Dataproc clusters or Dataproc Serverless workloads to a managed Dataproc Metastore service.

## Common Symptoms and Error Messages

When Dataproc encounters connectivity problems with Dataproc Metastore, you might see errors such as:

  * `Unable to connect to Hive Metastore`
  * `Connection refused`
  * `Host unreachable`
  * `javax.jdo.JDOException` or similar database connection errors
  * Timeout errors when attempting to list databases or tables, or when submitting Spark or Hive jobs that interact with the Metastore.



## Common Causes and Troubleshooting Steps

This section outlines common reasons why Dataproc Metastore connectivity issues occur and provides specific troubleshooting steps for each.

### 1\. Network Configuration Issues

Network misconfigurations are the most frequent cause of connectivity failures between Dataproc workloads and Dataproc Metastore.

  * **Virtual Private Cloud Network Peering or Private Service Access:**

    * Dataproc Metastore instances are typically accessed using a private IP address range using a Virtual Private Cloud network peering connection (specifically, [Private Service Access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access)).
    * **Verify Peering Status:** Verify the Virtual Private Cloud peering connection between your Dataproc workload's Virtual Private Cloud network and the service producer network for Dataproc Metastore is active and healthy. You can check this in the Google Cloud console under **VPC Network > VPC Network Peering**.
    * **IP Range Allocation:** Confirm that a sufficient IP range has been allocated for Private Service Access in your Virtual Private Cloud network.
  * **Firewall Rules:**

    * Verify that firewall rules in your Dataproc workload's Virtual Private Cloud network allow outbound traffic on the port used by Dataproc Metastore (default is 9083).
    * Verify there are no overly restrictive ingress rules on the service producer network side that would block traffic from your Dataproc workload.
  * **DNS Resolution:**

    * Confirm that the Metastore endpoint hostname (e.g., `your-metastore-endpoint.us-central1.dataproc.cloud.google.com`) resolves correctly to a private IP address from your Dataproc cluster or Dataproc Serverless environment.
    * Issues with Cloud DNS private zones or DNS forwarding can cause resolution failures.



**Troubleshooting Steps (Network):**

  1. **Check Dataproc Metastore Connectivity Information:**
     * In the Google Cloud console, navigate to **Dataproc Metastore** and select your instance.
     * Note the **Endpoint URI** and the **Network** it's connected to.
  2. **Verify Virtual Private Cloud Peering or Private Service Access:**
     * Go to **VPC Network > VPC Network Peering**. Confirm the peering connection to `servicenetworking-googleapis-com` is `ACTIVE`.
  3. **Use Connectivity Tests:** Use Google Cloud's [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) to diagnose the network path from a Compute Engine VM in your Dataproc workload's subnet to the Dataproc Metastore endpoint IP address and port.
  4. **Check Firewall Logs:** If firewall rules are suspected, analyze [Cloud Firewall logs](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) for denied connections.



### 2\. IAM Permissions

The service account used by your Dataproc workload needs appropriate IAM roles to access Dataproc Metastore.

  * **Required Role:** The service account must have the **Dataproc Metastore User** role (`roles/datametastore.user`) on the Dataproc Metastore instance or project.
  * **Service Agent Permissions:** Verify the Dataproc service agent has sufficient permissions if Dataproc is implicitly accessing the Metastore.



**Troubleshooting Steps (IAM):**

  1. **Identify Service Account:** Determine the service account used by your Dataproc cluster or Dataproc Serverless batch.
  2. **Verify IAM Roles:** Go to **IAM & Admin > IAM** in the Google Cloud console. Check the roles assigned to the service account on the Dataproc Metastore project or instance. Grant `roles/datametastore.user` if missing.
  3. For more details on service account configuration, refer to: 
     * [Dataproc service accounts](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts)
     * [Dataproc Serverless service accounts](https://docs.cloud.google.com/dataproc-serverless/docs/concepts/service-account)



### 3\. Incorrect Endpoint Configuration

The Dataproc workload must be configured with the correct Dataproc Metastore endpoint URI.

**Troubleshooting Steps (Endpoint):**

  1. **Verify Endpoint URI:** Double-check the `hive.metastore.uris` Spark property or any other configuration used to specify the Dataproc Metastore endpoint in your workload submission. Verify it matches the **Endpoint URI** from your Dataproc Metastore instance details.



### 4\. Other Considerations

  * **Metastore Status:** Verify that your Dataproc Metastore instance is in a `HEALTHY` state in the Google Cloud console. If it's unhealthy, address the Metastore's internal issues first.
  * **Version Compatibility:** While rare, verify there are no known compatibility issues between your Dataproc image version and the Dataproc Metastore version.
  * **SQL Proxy versus Managed Service:** If you are using Cloud SQL as a Metastore using the `cloud-sql-proxy.sh` initialization action, refer to its specific troubleshooting in the [Cloud SQL Proxy initialization action README](https://github.com/GoogleCloudDataproc/initialization-actions/blob/main/cloud-sql-proxy/README.md).



## What's next

  * Review the [Dataproc Metastore documentation](https://docs.cloud.google.com/dataproc-metastore/docs).
  * See [Connectivity and networking error scenarios](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting#connectivity-and-networking-error-scenarios).
  * Refer to general troubleshooting guides for network issues: 
    * [Troubleshooting Dataproc Cluster Creation Failures](https://docs.cloud.google.com/dataproc/docs/support/cluster-creation-failures)
    * [Troubleshooting Dataproc Serverless Batch Creation Failures](https://docs.cloud.google.com/dataproc-serverless/docs/support/batch-creation-failures)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
