---
url: https://docs.cloud.google.com/sap/docs/secops/troubleshooting/
title: Troubleshoot SAP log ingestion \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:29.532561+00:00
---

# Troubleshoot SAP log ingestion  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Troubleshoot SAP log ingestion Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide helps you resolve common configuration and connectivity issues that you might experience when ingesting SAP logs into Google SecOps.

## Troubleshooting overview

When you troubleshoot issues with Google SecOps for SAP, multiple areas might require your attention, depending on the scope of the issue you're investigating:

  * **Infrastructure** : Network connectivity, host availability, and Google Cloud resources, such as Cloud Storage and Secret Manager, or IAM permissions.
  * **SAP system** : SAP Basis configuration, service user authorizations, and the generation of logs within SAP.
  * **Application Telemetry Collector** : Collector configuration, SAP JCo library installation, and environment variables.
  * **Bindplane agent and Bindplane server** : Log forwarding pipeline configuration, OTLP source settings, and standardization processors.
  * **Google SecOps** : Feed status, Security Information and Event Management (SIEM) search for UDM logs, and ingestion labels.



### Involve the right teams

Determining which area the issue is occurring in is the first step. To resolve ingestion issues, you might need to coordinate with the following teams:

  * **SAP Basis team** : To manage SAP RFC connections, service user permissions, and verify that SAP logs are being created.
  * **Cloud or network infrastructure team** : To verify VPC peering, firewall rules, host instance health, and IAM role assignments.
  * **Security or SOC team** : To verify that the logs are appearing in Google SecOps and are being correctly normalized according to the threat detection requirements.



### Determine the root cause

Identify whether the issue is a connectivity failure, an authentication error, or a configuration mismatch. Because SAP systems and the log pipeline are tightly integrated, an error in one component, such as missing RFC authorizations, can appear as a failure in the collector. Always start by checking whether the collector is successfully extracting data from SAP before investigating the downstream pipeline. To do so, examine the collector's container logs for messages indicating that logs are being retrieved and sent, such as `Retrieved`, `Extracted`, or `Finished sending`. If you have heartbeat metrics enabled, you can also check Monitoring for collector activity.

## Logging

To identify the root cause of an issue, check the logs that are created by the ingestion components.

  * **Application Telemetry Collector** : You can view the collector logs by using the `docker logs` command or other methods appropriate for your container orchestration environment. If you enable heartbeat metrics, you can also verify the collector's health in Monitoring. For information about how to enable heartbeat metrics, see the configuration steps in [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#configure-the-collector) or [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#configure-the-collector).
  * **Bindplane agent** : You can find the Bindplane agent logs in the following files: 
    * **Linux** : `/var/log/bindplane-agent/bindplane-agent.log`
    * **Windows** : `C:\Program Files\BindPlane Agent\bindplane-agent.log`
  * **Google SecOps Feeds** : In the Google SecOps console, go to **SIEM Settings** > **Feeds** and check the **Last Run Status** for your feed.



## Common issues

The following sections provide information about common issues related to SAP log ingestion, their causes, and resolutions.

### Issue: SAP Java Connector (JCo) libraries missing

**Issue:** The Application Telemetry Collector fails to start, or logs indicate that JCo libraries are missing.

**Cause:** The collector requires the official SAP Java Connector (JCo) libraries to communicate with SAP systems. These libraries are not included in the collector image.

**Resolution:** To install the required libraries, do the following:

  1. Obtain the `sapjco3.jar` and `libsapjco3.so` files from the SAP Support Portal.
  2. Upload these files to your configuration bucket in a folder named `jco/`, for example, `gs://BUCKET_NAME/jco/`.
  3. Verify that the `COLLECTOR_GCS_BUCKET` environment variable is set to your bucket name.



For information about how to provide these libraries in your environment, see the setup instructions in [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#prepare-the-collector-host-and-dependencies) or [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#prepare-the-collector-host-and-dependencies).

### Issue: File not found in Cloud Storage

**Issue:** The collector fails to start with an error similar to `File not found in GCS: gs://BUCKET_NAME/jco/`.

**Cause:** The collector cannot find the JCo libraries or the configuration file in the specified bucket path.

**Resolution:** To fix this issue, do the following:

  1. Verify that `sapjco3.jar` and `libsapjco3.so` are located inside a directory named `jco/` in your bucket.
  2. Verify that the service account used by the collector has the `roles/storage.objectViewer` permission on the bucket.



For information about how to configure the required IAM roles, see [Prepare your environment for log ingestion](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-gcp-resources-app-logs).

### Issue: Another collector instance is already running

**Issue:** The collector fails to start with an error indicating that another instance is already running.

**Cause:** A file lock mechanism ensures only one instance runs at a time to prevent duplicate log ingestion.

**Resolution:** To resolve the lock issue, do the following:

  1. Verify that multiple instances of the collector are not running for the same configuration.
  2. If a previous collector instance crashed and left a stale lock, manually delete the `.lock` file from the temporary directory or the state location in Cloud Storage.



### Issue: `COLLECTOR_GCS_BUCKET` environment variable is not set

**Issue:** The collector fails to start because the collector cannot determine the configuration location.

**Cause:** The `COLLECTOR_GCS_BUCKET` variable is missing from the deployment environment.

**Resolution:** To resolve this issue, define the `COLLECTOR_GCS_BUCKET` variable in your deployment environment, for example, in your Docker run command, Kubernetes ConfigMap, or VM environment.

For information about how to define this variable during deployment, see [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#deploy-the-collector) or [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#deploy-the-collector).

### Issue: Invalid Cloud Storage bucket path format

**Issue:** The collector fails with an error indicating an invalid bucket path.

**Cause:** The bucket path provided in the environment variable is malformed.

**Resolution:** To fix the bucket path format, ensure the path follows the format `gs://BUCKET_NAME`. Don't include trailing slashes or internal directory paths in the `COLLECTOR_GCS_BUCKET` variable.

For information about how to verify the bucket path requirements for your environment, see [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#deploy-the-collector) or [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#deploy-the-collector).

### Issue: Failed to read configuration file from Cloud Storage

**Issue:** The collector cannot access the `collector_config.json` file.

**Cause:** The file is missing, incorrectly named, or the service account lacks permissions.

**Resolution:** To fix the configuration access error, do the following:

  1. Verify the file is named exactly `collector_config.json` and is placed in a folder named `config/` in your bucket.
  2. Check the JSON syntax of the file for errors.
  3. Verify that the service account has the `roles/storage.objectViewer` permission.



For information about how to name and upload the configuration file, see [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#configure-the-collector) or [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#configure-the-collector).

### Issue: Invalid secret version name format

**Issue:** The collector fails to retrieve SAP credentials from Secret Manager.

**Cause:** The resource name for the secret version is incorrect in the `collector_config.json` file.

**Resolution:** To resolve this issue, do the following:

  1. Use the fully qualified name for the secret version: `projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION`.
  2. Verify that the service account has the `roles/secretmanager.secretAccessor` permission.



For information about how to configure secrets and authentication, see [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#auth-basic) or [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#auth-basic).

### Issue: Failed to connect to SAP system

**Issue:** The collector logs show `Failed to get or ping JCoDestination for system SYSTEM_ID`.

**Cause:** Network connectivity issues or incorrect SAP connection parameters.

**Resolution:** To troubleshoot the SAP connection, do the following:

  1. **Check Configuration** : Verify the **Host** , **System Number** , and **Client** in the `collector_config.json` file.
  2. **Verify Network** : Verify that firewalls, Cloud VPN, or VPC peering allow traffic on RFC ports, which is usually `33INSTANCE_NUMBER`.
  3. **Check SAP Status** : Confirm the SAP Application Server is online. Check for SAP error codes like `WSAEWOULDBLOCK`, which indicates the network is blocked.



For information about how to configure connectivity and firewall requirements, see [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#before-you-begin) or [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#before-you-begin).

### Issue: SAP logon rejected or user locked

**Issue:** The collector cannot authenticate with the SAP system.

**Cause:** Invalid credentials or the SAP service user is locked.

**Resolution:** To resolve logon issues, do the following:

  1. Verify the credentials stored in Secret Manager.
  2. Check transaction `SU01` in the SAP system to verify that the user is not locked and is classified as a "System" or "Communications" user.



For information about how to create and classify an SAP service user, see [Create an SAP service user](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#create-an-sap-service-user).

### Issue: Failed to read or write state file

**Issue:** The collector fails to track ingestion progress and might restart extraction from the beginning, which can result in duplicate logs.

**Cause:** The collector cannot access the state file, also known as a high-watermark, in Cloud Storage. This file stores the timestamp or ID of the last successfully ingested log record, allowing the collector to resume extraction from the correct point after a restart.

**Resolution:** To fix state file access, verify that the service account has the `roles/storage.objectAdmin` or `roles/storage.objectUser` role on the configuration bucket.

For information about how to configure Cloud Storage and IAM, see [Prepare your environment for log ingestion](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-gcp-resources-app-logs).

### Issue: Invalid SAP timezone specified

**Issue:** Log timestamps are incorrect, or extraction fails.

**Cause:** The `timezone` parameter in the configuration uses an unsupported format.

**Resolution:** To resolve time zone errors, use a standard **IANA** time zone identifier, for example, `Europe/Berlin` or `UTC`.

### Issue: Skipping extraction

**Issue:** The collector logs indicate that extraction is being skipped.

**Cause:** A previous extraction process is still running. This skipping usually happens if the log volume is high or the polling interval is too short.

**Resolution:** To resolve skipping issues, do the following:

  1. Increase the polling interval in the `collector_config.json` file.
  2. Check the performance of the SAP system.



### Issue: Function module `RSAU_API_GET_LOG_DATA` not found

**Issue:** Security Audit Log extraction fails.

**Cause:** The required function module for extracting Security Audit Logs is missing in your SAP release.

**Resolution:** To fix the missing module error, contact your SAP Basis team to apply the SAP Notes that backport this module, such as SAP Note 2926298, or upgrade your SAP release.

For information about the required function modules, see [Set up remote function call (RFC) authorizations](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#set-up-remote-function-call-rfc-authorizations).

### Issue: Error extracting Security Audit Logs

**Issue:** The RFC connection succeeds, but the extraction of Security Audit Logs fails.

**Cause:** The SAP service user lacks the necessary authorizations to read audit logs.

**Resolution:** To resolve audit log extraction errors, do the following:

  1. In SAP, use transaction `SU53` to check for authorization failures for the service user.
  2. Verify that the user has the `S_RFC` authorization for the required function groups and the `S_SAL` (or `S_ADMI_FCD` for older releases) authorization.



For information about SAP authorization objects, see [Configure SAP authorizations](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-sap-authorizations).

### Issue: `RFC_READ_TABLE` not found or Change Document error

**Issue:** The collector fails to extract Change Documents from the SAP tables `CDHDR` and `CDPOS`.

**Cause:** Missing `RFC_READ_TABLE` module or insufficient permissions to read the `CDHDR` and `CDPOS` tables.

**Resolution:** To resolve change document extraction errors, do the following:

  1. Verify that the user has `S_RFC` authorization for the required function group.
  2. Verify that the user has `S_TABU_DIS`, specifically for the `&NC&` group, or `S_TABU_NAM` authorization for tables `CDHDR` and `CDPOS`.



For information about how to grant table-level access, see [Set up table access authorizations](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#set-up-table-access-authorizations).

### Issue: Logs are not appearing in Google SecOps

**Issue:** The collector reports successful extraction, but logs are not visible in the Google SecOps console.

**Cause:** Network egress issues or incorrect OTLP endpoint configuration.

**Resolution:** To fix missing logs in the console, do the following:

  1. Verify that the OTLP or Bindplane endpoint URL in the collector configuration.
  2. Verify that your network, such as VPC egress or Cloud NAT, allows outbound HTTPS traffic to the ingestion endpoint.
  3. Check the collector console output for `Error flushing OTel logs`.



For information about how to verify your log forwarding and destination settings, see [Set up log ingestion for SAP RISE](https://docs.cloud.google.com/sap/docs/secops/ingest-sap-rise-logs#secops-destination-bindplane-app-logs) or [Set up log ingestion for self-managed SAP systems](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#secops-destination-bindplane).

## Get support

For issues related to Google SecOps for SAP, [contact Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support). Our team provides assistance or guides you to the right resource to help ensure a timely resolution.

For issues involving SAP systems or the LogServ service, contact SAP support. For issues related to other third-party products, such as Bindplane, contact the appropriate third-party vendor for assistance.

Get technical answers and peer support in the [Google SecOps Community](https://security.googlecloudcommunity.com/google-security-operations-2).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
