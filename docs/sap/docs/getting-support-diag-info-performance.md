---
url: https://docs.cloud.google.com/sap/docs/getting-support-diag-info-performance/
title: Gather diagnostic information about SAP workload performance \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:00:33.594639+00:00
---

# Gather diagnostic information about SAP workload performance  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/getting-support-diag-info-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  Gather diagnostic information about SAP workload performance Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to gather performance diagnostic information for your SAP workloads by using Google Cloud's Agent for SAP, version 3.4 or later. 

When you contact Cloud Customer Care for assistance in troubleshooting a performance issue with your SAP workload, you need to share pertinent diagnostic information about your workload. By using the agent's built-in performance diagnostic tool, you can automate the gathering of the necessary diagnostic information, which in turn can help accelerate troubleshooting and resolution.

For information about the performance diagnostics that the agent can run for your SAP workloads, see [Workload performance diagnostics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#workload-performance-diagnostics).

## Before you begin

  * Make sure that you're using version 3.4 or later of Google Cloud's Agent for SAP.

For information about how to check and update the agent, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).




## Gather performance diagnostics information

To gather performance diagnostics information for your SAP workload, invoke the agent's tool by using the `performancediagnostics` command:
    
    
    sudo /usr/bin/google_cloud_sap_agent performancediagnostics \
        --type="COMMA_SEPARATED_DIAGNOSTIC_TYPES" \
        --test-bucket=STORAGE_BUCKET_NAME \
        --backint-config-file=BACKINT_CONFIG_FILE_PATH \
        --output-file-name=OUTPUT_FILE_NAME \
        --output-file-path=OUTPUT_FILE_PATH
    

Replace the following:

  * `COMMA_SEPARATED_DIAGNOSTIC_TYPES`: the diagnostic types that you want to run.
  * `STORAGE_BUCKET_NAME`: the name of the Cloud Storage that the tool must use to run the `backup` diagnostics.
  * `BACKINT_CONFIG_FILE_PATH`: the path to the required [Backint configuration file](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#backint_configuration_file).
  * `OUTPUT_FILE_NAME`: the name of the output ZIP file, which contains the diagnostic information about your SAP workload
  * `OUTPUT_FILE_PATH`: the path to the directory where you want the performance diagnostic tool to save the output ZIP file. The specified path is created if it doesn't exist.



For information about the parameters supported by this command, see Supported parameters.

### Supported parameters

The following table describes the parameters that you can use with the `performancediagnostics` command:

Parameter | Description  
---|---  
`type` |  `STRING` Specify a comma-separated list of diagnostic types that you want to run. The following are the supported diagnostic types:

  * `backup`: Runs the Backint feature's [self diagnostic](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#self_diagnostics) and [`gsutil perfdiag` diagnostics](https://docs.cloud.google.com/storage/docs/gsutil/commands/perfdiag) for SAP HANA workloads. 
  * `IO`: Runs the input/output diagnostics, which is done by using the [Flexible I/O tester (FIO)](https://fio.readthedocs.io/en/latest/fio_doc.html). This performs stress tests on the I/O capabilities of your workload's storage systems. It also runs workload simulations to assess the performance of your workload's infrastructure such as disks and network file system.
  * `all`: Runs all on-demand and default diagnostics supported by the tool.
If you're running the `IO` or `all` diagnostics, then you need to ensure that the FIO tool is installed on your compute instance. You can install this tool by running `sudo yum install fio` on RHEL, and `sudo zypper install fio` on SLES. 
For more information about the supported diagnostics, see [Workload performance diagnostics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#workload-performance-diagnostics).  
`backint-config-file` |  `String` If you want to run the `backup` diagnostics, then specify the path to your Backint configuration file. For example: `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/PARAMETERS.json`. To run the `backup` diagnostics, you need to specify at least one of the following parameters: `backint-config-file` or `test-bucket`. If you're using separate configuration files for data, log, or catalog backups, then specify the path that corresponds to the backup type for which you want to collect diagnostic information.  
`test-bucket` |  `String` If you want to run the `backup` diagnostics, then specify the name of the Cloud Storage bucket that the tool must use to test uploading and downloading files to and from Cloud Storage. For example: `mybucket`. Ensure that the bucket used for testing does not have a retention policy set. To run the `backup` diagnostics, you need to specify at least one of the following parameters: `backint-config-file` or `test-bucket`. If you specify values for both parameters, then the tool uses the bucket specified for `test-bucket`.  
`output-bucket` |  `String` Optional. Specify the name of the Cloud Storage bucket where you want to upload the output of the performance diagnostics tool. For example: `mytestbucket`. The tool creates a folder named `performancediagnostics` in this bucket to store the output files. If you don't specify this parameter, then the tool saves the output in the directory determined by whether or not you specify the `output-file-path` parameter. To let the tool upload the output to Cloud Storage, the service account used by the agent must be assigned the **Storage Object User (`roles/storage.objectUser`)** IAM role. If you're using the agent's Backint feature, then the service account has the underlying permissions.  
`output-file-name` |  `String` Optional. Specify the name of the output ZIP file that the performance diagnostics tool creates. By default, the ZIP file is named `performance-diagnostics-TIMESTAMP`, where `TIMESTAMP` is the date and time when the tool creates the ZIP file.  
`output-file-path` |  `String` Optional. Specify the path to the directory where you want the performance diagnostic tool to save the output ZIP file. The specified path is created if it doesn't exist. By default, the ZIP file is saved in the `/tmp` directory.  
`hyper-threading` |  `String` Optional. Specify to set the hyperthreading settings for Compute Engine bare metal machine types, such as X4. The default value is `on`. Supported values are `on` and `off`.  
`log-level` |  `String` Optional. Sets the agent's logging level for the duration it runs the performance diagnostics. The default value is `info`. The supported values are: `debug`, `info`, `warn`, and `error`. Operations performed by the tool to collect diagnostic information are captured in the following file: `/var/log/google-cloud-sap-agent/performancediagnostics.log`.  
  
## View logs

When you run the `performancediagnostics` command, the operations performed are logged in the following file: `/var/log/google-cloud-sap-agent/performancediagnostics.log`.

## What's next

Once you generate the output of performance diagnostic tool, you need to send it to Customer Care. This can help Customer Care accelerate troubleshooting the performance issue with your SAP workload.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
