---
url: https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager/
title: Troubleshooting VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:14.049114+00:00
---

# Troubleshooting VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Troubleshooting VM Manager Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to troubleshoot issues with VM Manager.

For more information about VM Manager, see [VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Overview

To troubleshoot issues, first verify that VM Manager [is set up properly](https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/verify-setup). If the setup is correct and you have still have issues, you can then review logs. When you review logs, you can identify issues with your VM or in your VM Manager workflow, such as errors in commands or scripts, that you can isolate and resolve.

You can collect the following information from logs:

  * Any error message or warning logged by the VM. This is ideal for identifying VM-level errors, or errors from other services running on your VM. To review these logs, see Inspect Cloud Logging.
  * Verbose debug information logged by the OS Config agent. This is useful for identifying issues with any of the operations run by VM Manager. To inspect debug logs for the OS Config agent, see Inspect debug logs.



After identifying the issues or errors, you can also review the common errors section to see potential fixes.

## Inspect Cloud Logging

You can use the Google Cloud console quick links for each feature to view logs.

### OS patch

  1. In the Google Cloud console, go to the **Jobs run** tab on the **Patch** page. 

[ Go to Jobs run](https://console.cloud.google.com/compute/patch/jobs)

  2. Click the name of the patch job that you want to debug.
  3. Go to the **Updated VM instances** section.
  4. For a specific VM, under **Logs** , click **View**.



### OS policies

This procedure is supported for OS policies. For guest policies (beta), use the debug logs option, in the following section.

  1. In the Google Cloud console, go to the **VM instances** tab on the **OS policies** page. 

[ Go to VM instances](https://console.cloud.google.com/compute/config/instances)

  2. Click the name of the VM that you want to debug.
  3. Go to the **Policies** section.
  4. Under **Logs** , click **View**.



### OS policy orchestrators

  1. In the Google Cloud console, go to the **OS policy orchestrators** tab on the **OS policies** page. 

[ Go to OS policy orchestrators](https://console.cloud.google.com/compute/config/orchestrators)

  2. Click the name of the OS policy orchestrator that you want to debug.
  3. Go to the **Logs** section and verify the log entry.



## Inspect debug logs

You can identify issues with any VM Manager feature by enabling debugging for the OS Config agent and viewing debug log.

### Enable debug logging for the OS Config agent

You can enable debug logging by setting the `osconfig-log-level=debug` metadata on the VM instance or project.

To enable debug logging on your VM, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM for which you want to set the metadata value.

  3. On the **Instance details** page, click **Edit** to edit the settings.

  4. Under **Custom metadata** , add the following metadata entries:

Key: `osconfig-log-level`  
Value: `debug`

  5. Click **Save** to apply your changes to the VM.




###  gcloud 

Use the [`instances add-metadata` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata) with the `--metadata=osconfig-log-level=debug` flag.
    
    
    gcloud compute instances add-metadata VM_NAME \
        --metadata=osconfig-log-level=debug
    

Replace `VM_NAME` with the name of your VM.

###  REST 

For instructions on setting instance metadata, follow the API instructions for [setting instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#updatinginstancemetadata).

The following key-value pair is required as part of the metadata property:

Key: `osconfig-log-level`  
Value: `debug`

### View debug logs

When debug logging is enabled, the OS Config agent writes log entries to Cloud Logging and the serial port console.

After you enable debug logging on your VM, it takes the OS Config agent approximately ten minutes to start writing debug messages in Cloud Logging. You can reduce this wait time by restarting the agent or rebooting your VM. For more information about Cloud Logging, see [Viewing Cloud Logging logs](https://docs.cloud.google.com/logging/docs/write-query-log-entries-gcloud#explore).

To view debug logs you can use the following options:

  * Cloud Logging: use the Google Cloud console or Google Cloud CLI
  * Serial port console




###  Console 

  1. Go to the **Logging > Logs Explorer** (Logs Explorer) page in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. If needed, select an existing Google Cloud project at the top of the page, or create a new project.

  3. In the **Resource** drop-down list, select **VM Instance**. A list of available VMs (`instance_id`) displays.

  4. Click the VM that you want to view.

  5. Click **Add**.

  6. In the **Log name** drop-down list, select **OSConfigAgent**.

  7. Click **Add**.

  8. Your query should be similar to the following:
         
         resource.type="gce_instance" resource.labels.instance_id="INSTANCE_ID"
         logName="projects/PROJECT_ID/logs/OSConfigAgent"
         

  9. Click **Run query**.




###  gcloud 

Run the [`gcloud logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read).
    
    
     gcloud logging read "resource.type=gce_instance AND logName=projects/PROJECT_ID/logs/OSConfigAgent"
     

Replace `PROJECT_ID` with your project ID.

###  Serial port 

To view debug log information from the serial port console, see [Viewing serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output#viewing_serial_port_output).

## Common errors

### Authentication issues

For VM Manager to work, you must have the following:

  * An attached service account. VM Manager uses this service account to sign requests to the API service.
  * Make sure that the attached service account has the [`roles/logging.logWriter`](https://docs.cloud.google.com/iam/docs/understanding-roles?hl=en#logging-roles) role to write logs to the Logging API.
  * [Google Cloud OS Config Service Agent](https://docs.cloud.google.com/compute/vm-manager/docs/overview#service-agent). VM Manager creates this service agent when starting patch jobs and gives it the Cloud OS Config Service Agent role. To create OS policies, you need not configure this service agent.



If you use VM Manager and you don't have an attached service account, or a Google Cloud OS Config Service Agent, you might see the following errors while working with patch jobs:
    
    
    Service account permissions are missing. Verify that the service account has the correct permissions and try again.
    
    
    OSConfigAgent Error main.go:88: error getting token from metadata: metadata: GCE metadata "instance/service-accounts/default/identity?audience=osconfig.googleapis.com&format=full" not defined
    
    
    message: "Error running OPERATION_NAME: error calling OPERATION_NAME: code: "PermissionDenied", message: "The caller does not have permission", details: []"
    

Authentication issues might also prevent VM instances from showing up on the [Patch dashboard](https://docs.cloud.google.com/compute/vm-manager/docs/patch#dashboard).

To resolve these issues, try one or all of the following:

  * Verify that all VMs have an [attached service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-to-resources).
  * Ensure that the Cloud OS Config Service Agent role (`roles/osconfig.serviceAgent`) is set on the Google Cloud OS Config Service Agent.
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
          --member='serviceAccount:service-PROJECT_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com' \
          --role='roles/osconfig.serviceAgent'
        

Replace the following:

    * `PROJECT_ID`: your project ID
    * `PROJECT_NUMBER`: your [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)



### Error when excluding packages for patch updates

If you specify wildcards or special characters for the name of packages when excluding packages in a patch job, OS patch management might ignore the list and update all packages.

To resolve this issue, [update the OS Config agent](https://docs.cloud.google.com/compute/vm-manager/docs/upgrade-vm-manager#update-agent) to version `20220829.00` and use forward slashes (`/`) to wrap the package name.

In the following example, OS patch management excludes `yum` packages with prefix `google-` in the package name.
    
    
          gcloud compute os-config patch-jobs execute --instance-filter-all   
    
            --yum-excludes=/google-.*/
        

## What's next?

  * [Manage your patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs).
  * [Manage OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
