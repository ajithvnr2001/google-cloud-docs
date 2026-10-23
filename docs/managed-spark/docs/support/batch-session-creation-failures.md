---
url: https://docs.cloud.google.com/managed-spark/docs/support/batch-session-creation-failures/
title: Troubleshoot batch and session creation failures \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:40.584309+00:00
---

# Troubleshoot batch and session creation failures  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/support/batch-session-creation-failures/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Troubleshoot batch and session creation failures Stay organized with collections  Save and categorize content based on your preferences. 

This document provides guidance on troubleshooting common issues that prevent Managed Service for Apache Spark batch workloads and interactive sessions from starting.

## Overview

Typically, when a batch or session fails to start, it reports the following error message:
    
    
    Driver compute node failed to initialize for batch in 600 seconds
    

This error message indicates that the Spark driver couldn't start within the default timeout period of 600 seconds (10 minutes). Common causes are related to service account permissions, resource availability, network configuration, or Spark properties.

## Batch and session start failure causes and troubleshooting steps

The following sections list common causes of batch and session start failures with troubleshooting tips to help you resolve the issues.

### Insufficient service account permissions

The service account used by your Managed Service for Apache Spark batch or session requires specific IAM roles that include permissions for Managed Service for Apache Spark operation and access to Google Cloud resources. If the service account lacks the necessary roles, the Spark driver for the batch or session can fail to initialize.

  * Required Worker role: The batch or session service account must have the **Managed Service for Apache Spark Worker role** (`roles/dataproc.worker`). This role contains the minimum permissions needed for Managed Service for Apache Spark to provision and manage compute resources.
  * Data Access Permissions: If your Spark application reads from or writes to Cloud Storage or BigQuery, the service account needs roles related to those services: 
    * Cloud Storage: The **`Storage Object Viewer` role** (`roles/storage.objectViewer`) is needed for reading, and the **`Storage Object Creator` role** (`roles/storage.objectCreator`) or **`Storage Object Admin` role** (`roles/storage.admin`) is needed for writing.
    * BigQuery: The **`BigQuery Data Viewer` role** (`roles/bigquery.dataViewer`) is needed for reading and the **`BigQuery Data Editor` role** (`roles/bigquery.dataEditor`) is needed for writing.
  * Logging Permissions: The service account needs a role with permission to write logs to Cloud Logging. Typically, the **`Logging Writer` role** (`roles/logging.logWriter`) is sufficient.



Troubleshooting tips:

  * Identify the batch or session [service account](https://docs.cloud.google.com/managed-spark/docs/concepts/service-account). If not specified, it defaults to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).
  * Go to the [**IAM & Admin > IAM**](https://console.cloud.google.com/iam-admin/iam) page in the Google Cloud console, find the batch or session service account, and then verify that it has the necessary roles needed for operations. Grant any missing roles.



### Insufficient quota

Exceeding project or region-specific quotas for Managed Service for Apache Spark or other Google Cloud resources can prevent new batches or session from starting.

Troubleshooting tips:

  * Review the [Managed Service for Apache Spark quotas](https://docs.cloud.google.com/managed-spark/quotas) page to understand limits on concurrent batches, DCUs, and shuffle storage.

    * You can also use the `gcloud compute quotas list` command to view current usage and limits for your project and region: 
          
          gcloud compute quotas list --project=PROJECT_ID --filter="service:dataproc.googleapis.com"
          

  * If you repeatedly hit quota limits, consider requesting a quota increase through the Google Cloud console.




### Network configuration issues

Incorrect network settings, such as VPC configuration, Private Google Access, or firewall rules, can block the Spark driver from initializing or connecting to necessary services.

Troubleshooting tips:

  * Verify that the VPC network and subnet specified for your batch or session are correctly configured and have sufficient IP addresses available.

  * If your batch or session needs to access Google APIs and services without traversing the public internet, verify Private Google Access is enabled for the subnet. Managed Service for Apache Spark batch workloads and interactive sessions run on VMs with internal IP addresses only and on a regional subnet with Private Google Access automatically enabled on the session subnet.

  * Review your VPC firewall rules to verify they don't inadvertently block internal communication or egress to Google APIs or external services that are required by your Spark application.


**Tip:** To diagnose batch and network connectivity issues, also see [Troubleshoot batch and session connectivity](https://docs.cloud.google.com/managed-spark/docs/support/troubleshoot-connectivity#network-configuration-issues).

### Invalid spark properties or application code issues

Misconfigured Spark properties, particularly those related to driver resources, or issues within your Spark application code can lead to startup failures.

Troubleshooting tips:

  * Check [`spark.driver.memory` and `spark.driver.cores`](https://docs.cloud.google.com/managed-spark/docs/concepts/properties#resource_allocation_properties) values. Verify they are within reasonable limits and align with available DCUs. Excessively large values for these properties can lead to resource exhaustion and initialization failures. Remove any unnecessary or experimental Spark properties to simplify debugging.

  * Try running a "Hello World" Spark application to determine if the issue is with your environment setup or due to code complexity or errors.

  * Verify that all application JARs, Python files, or dependencies specified for your batch or session are correctly located in Cloud Storage and are accessible by the batch or session service account.




## Check logs

A critical step in diagnosing batch creation failures is to examine the detailed logs in Cloud Logging.

  1. Go to the [**Cloud Logging**](https://console.cloud.google.com/logs/viewer) page in the Google Cloud console.
  2. Filter for Managed Service for Apache Spark Batches or Sessions: 
     1. In the **Resource** drop-down, select `Cloud Managed Service for Apache Spark Batch` or `Cloud Managed Service for Apache Spark Session`.
     2. Filter by `batch_id` or `session_id` for the failed batch or session. You can also filter by `project_id` and `location` (region).
  3. Look for log entries with `jsonPayload.component="driver"`. These logs often contain specific error messages or stack traces that can pinpoint the reason for the driver initialization failure before the 600-second timeout occurs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
