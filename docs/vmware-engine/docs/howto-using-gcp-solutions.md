---
url: https://docs.cloud.google.com/vmware-engine/docs/howto-using-gcp-solutions/
title: Access Google Cloud resources from VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:36.743103+00:00
---

# Access Google Cloud resources from VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/howto-using-gcp-solutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access Google Cloud resources from VMware Engine

You can use Google Cloud services with VMware Engine to do the following:

  * Access Cloud Storage from VMware VMs to export data or as an extended storage target.
  * Monitor all your public, private, and hybrid applications by using Cloud Monitoring.
  * Import data from databases into BigQuery for analytics.
  * Deploy GKE Enterprise for high performance and private, containerized application deployments.



## Authenticating to Google Cloud services

Workloads running on VMware Engine VMs can access Google Cloud services using service account credentials. When applications running in VMware Engine VMs use [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc), they first look for credentials in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

To authenticate to Google Cloud services from a VMware Engine VM, do the following:

  1. Create a service account and grant it IAM roles that are required by your application. For more information, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).
  2. Create a service account key for the service account you created.
  3. Download the service account key, and then upload the key file to your VMware Engine VM. For more information, see [Create and manage service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).
  4. In the VM, set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the absolute path of the service account key file.



After you set the environment variable, your application can use ADC to authenticate with Google Cloud services when it runs in the VM.

## Access Cloud Storage from VMware VMs

Cloud Storage is a globally unified, scalable, and highly durable object storage for developers. Use Cloud Storage to do the following:

  * Optimize price and performance across storage classes by using Object Lifecycle Management.
  * Get secure and durable storage for resilience against errors or outages.
  * Deliver content and centralize data lakes and backups.



In VMware Engine, you can access Cloud Storage from VMware VMs, vCenter, or directly through private addressing. Private addressing enhances security by avoiding external internet traffic and improves performance due to fewer hops. For applications, access Cloud Storage from VMware VMs. To add vCenter management tools such as backup, access Cloud Storage from vCenter.

To learn more about Cloud Storage access from VMware VMs, see [Discover object storage with the Google Cloud CLI tool](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud) and [Mounting Cloud Storage buckets as file systems](https://docs.cloud.google.com/storage/docs/gcs-fuse).

## Monitor applications using Cloud Logging and Cloud Monitoring

Cloud Logging is a fully managed service that performs at scale and that can use application and system log data and custom log data from Google Kubernetes Engine environments and VMs. Cloud Logging lets you analyze and export selected logs to long-term storage in real time.

Cloud Monitoring provides visibility into the performance, uptime, and overall health of cloud-powered applications. You can collect metrics, events, and metadata from Google Cloud services, hosted uptime probes, application instrumentation, and a variety of common application components.

In VMware Engine, you can do the following:

  * Access Cloud Logging and Cloud Monitoring from VMware VMs.
  * Enable Cloud Logging and Cloud Monitoring from the VMware vSphere platforms using a standalone agent.
  * Access Cloud Storage directly through private addressing. This avoids external internet traffic, improves performance due to fewer hops, and enhances security by keeping traffic private.



To enable Cloud Logging and Cloud Monitoring from the VMware vSphere platform using a standalone agent, see [Setting up Cloud Monitoring with a standalone agent](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone).

## Import data from databases into BigQuery

Using VMware Engine and BigQuery, you can do the following:

  * Connect databases running inside VMware Engine to BigQuery for data warehousing analysis.
  * Export data directly to services in Google Cloud private addressing.



For more information, see [Use Alooma to perform real-time, incremental data transfer from a variety of sources (which might be running on VMware) to BigQuery](https://www.alooma.com/docs/connect-your-data).

## Deploy Google Distributed Cloud

Google Distributed Cloud is hybrid cloud software that brings Google Kubernetes Engine to VMware-based environments. With GKE in an on-premises environment, you can create, manage, and upgrade Kubernetes clusters in your VMware environments, whether they are deployed on-premises or on VMware Engine.

Your VMware infrastructure has production workloads, databases, and line-of-business applications. Use containers and Kubernetes to modernize your infrastructure.

Google Distributed Cloud uses VMware's vCenter Server to manage your clusters. With Anthos Connect, you can view and sign in to your VMware-based and cloud Kubernetes clusters from the Google Cloud console.

Use Google Distributed Cloud with VMware Engine for a dedicated, private environment with the latest hardware and 100 Gbps of networking. Your containerized workloads can be next to your databases for low latency. This environment is a single tenant, so you get the privacy and security of dedicated infrastructure.

For more information, see the following overviews:

  * [GKE Enterprise overview](https://docs.cloud.google.com/anthos/docs/concepts/overview)
  * [Google Distributed Cloud overview](https://docs.cloud.google.com/anthos/gke/docs/on-prem/overview)
  * [Connect overview](https://docs.cloud.google.com/anthos/multicluster-management/connect)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
