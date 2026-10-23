---
url: https://docs.cloud.google.com/managed-spark/docs/support/troubleshoot-connectivity/
title: Troubleshoot batch and session connectivity \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:16.266287+00:00
---

# Troubleshoot batch and session connectivity  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/support/troubleshoot-connectivity/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Troubleshoot batch and session connectivity Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance on diagnosing and resolving common network connectivity issues for Managed Service for Apache Spark batch workloads and interactive sessions. These issues can prevent your workloads from accessing required data sources, external services, or Google Cloud APIs.

## Common symptoms and error messages

When Managed Service for Apache Spark encounters connectivity problems, you might encounter errors such as:

  * `Unable to connect to service_name.googleapis.com`
  * `Could not reach required Google APIs`
  * `Connection refused`
  * `Host unreachable`
  * `Operation timed out`
  * `Permission denied` (often network-related if blocking API calls)



You might also encounter errors related to accessing data in Cloud Storage, BigQuery, or other databases.

## Common causes and troubleshooting tips

This section lists common causes of Managed Service for Apache Spark connectivity issues, and provides troubleshooting tips to help you resolve them.

### Network configuration

Network misconfigurations are a frequent cause of connectivity failures. Managed Service for Apache Spark workloads and sessions run on VMs with internal IP addresses, with [Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) automatically enabled on the workload or session subnet to access to Google APIs and services. For more information, see [Managed Service for Apache Spark network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network).

  * Access options:

    * Private Service Connect (PSC): You can [create private endpoints](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints) within your VPC network to access specific Google APIs.

      * In the Google Cloud console, go to [**Private Service Connect > Endpoints**](https://console.cloud.google.com/net-services/psc/list/consumers). Connect endpoints or confirm that endpoints are connected for all required APIs, such as `storage.googleapis.com` and `dataproc.googleapis.com` and that they connect to the batch workload or session Virtual Private Cloud network.
    * Cloud NAT: If your workload needs to access the public internet, you can configure Cloud NAT for your batch workload or session subnet:

      * In the Google Cloud console, go to the [**Cloud NAT**](https://console.cloud.google.com/net-services/nat/list) page. [Configure a gateway](https://docs.cloud.google.com/nat/docs/gce-example) or confirm that a gateway is configured for the batch workload or session VPC network, region, and subnet. Also make sure firewall rules allow egress to `0.0.0.0/0`. For more information, see [Set up Cloud NAT](https://docs.cloud.google.com/nat/docs/gce-example).
  * Firewall rules:

    * Egress firewall rules in your VPC network (or shared VPC network host project, if applicable) must not block outbound traffic to required destinations. 
      * If applicable, egress rules must allow traffic to external services, such as public APIs and databases outside of Google Cloud. If your batch workload or session needs internet access, you can use a [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to provide subnet egress.
    * Although not a common cause of connectivity issues, overly restrictive ingress rules might inadvertently block necessary return traffic or internal communications.
  * DNS resolution:

    * DNS resolution must be configured within the VPC network. Workloads and sessions must be able to resolve hostnames for Google APIs, such as `storage.googleapis.com` or`bigquery.googleapis.com` and external services.
    * Custom DNS servers and Cloud DNS private zones must forward or resolve queries for Google domains.
    * If you are using Private Service Connect for private access to Google APIs, DNS records for Google services must resolve to private IP addresses within your VPC network using the PSC endpoint.



Troubleshooting tips:

  * Identify network and subnet configuration:

    * From Managed Service for Apache Spark batch or session details, review the `networkUri` and `subnetUri`.
    * In the Google Cloud console, review the settings for the VPC network and subnet.
  * Test connectivity from a Proxy VM:

    * Launch a test Compute Engine VM in the batch or session subnet using the batch or session service account.
    * From the test VM, perform the following connectivity tests: 
      * `nslookup storage.googleapis.com` to verify DNS resolution. Lookup other Google API domains, such as `bigquery.googleapis.com`and `dataproc.googleapis.com`. With Private Google Access, which is automatically enabled on Managed Service for Apache Spark subnets, or Private Service Connect, the domains must resolve to private IP addresses.
      * `curl -v https://storage.googleapis.com` to verify HTTPS connectivity to Google APIs. Also try connecting to other Google services.
      * `ping 8.8.8.8` to test internet connectivity if required by your batch or session. Try `curl -v https://example.com` if Cloud NAT is expected.
    * Run Google Cloud [Network Intelligence Center connectivity tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) to diagnose network paths from your subnet to relevant endpoints, such as Google APIs and external IP addresses.
  * Review Cloud Logging for network errors:

    * Review Logging for your Managed Service for Apache Spark workload or session. Look for `ERROR` or `WARNING` messages related to network timeouts, connection refusals, or API call failures. Filter by `jsonPayload.component="driver"` or `jsonPayload.component="executor"` for Spark-specific network issues.



### IAM permissions

Insufficient IAM permissions can prevent workloads or sessions from accessing resources, resulting in network failures if API calls are denied.

The service account used by your batch workload or session must have required roles:

  * **Managed Service for Apache Spark Worker role** (`roles/dataproc.worker`).
  * Data access roles, such as `roles/storage.objectViewer` or `roles/bigquery.dataViewer`).
  * Logging: (`roles/logging.logWriter`).



Troubleshooting tips:

  * Identify the batch workload or session [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account). If not specified, it defaults to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).
  * Go to the [**IAM & Admin > IAM**](https://console.cloud.google.com/iam-admin/iam) page in the Google Cloud console, find the batch workload or session service account, and then verify that it has the necessary roles needed for workload operations. Grant any missing roles.



### External service configuration

If your workload connects to databases or services outside of Google Cloud, verify their configuration:

  * Verify the external service firewall or security group allows inbound connections from your VPC network IP ranges: if applicable, check internal IP addresses using VPC Peering, Cloud VPN, or Cloud Interconnect, or Cloud NAT IP addresses.
  * Review database credentials or connectivity strings. Check connection details, usernames, and passwords.



## What's next

  * Learn about [Managed Service for Apache Spark networking](https://docs.cloud.google.com/managed-spark/docs/concepts/network).
  * Review [Managed Service for Apache Spark service accounts](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account).
  * Refer to general network troubleshooting guides: 
    * [Troubleshoot Managed Service for Apache Spark cluster creation issues](https://docs.cloud.google.com/managed-spark/docs/support/troubleshoot-cluster-creation)
    * [Troubleshoot Dataproc Metastore connectivity](https://docs.cloud.google.com/dataproc-metastore/docs/troubleshooting-connectivity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
