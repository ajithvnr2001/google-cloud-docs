---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/collecting-diagnostic-information/
title: Collecting diagnostic information \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:44.457507+00:00
---

# Collecting diagnostic information  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/collecting-diagnostic-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Collecting diagnostic information Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

This document describes how to collect information about a virtual machine (VM) instance by using a diagnostic tool. Use the information that the tools collects to help with basic troubleshooting before contacting [Cloud Customer Care](https://docs.cloud.google.com/compute/docs/getting-support).

The tool does the following:

  * Collects information only from the VM that you specify.

  * Stores the information only in your project.

  * Stores the information for 10 days in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets), which, by default, only you can access.




Before sharing the collected information with Customer Care, do the following:

  1. Review the information for confidential or personally identifiable information (PII).

  2. Delete or mask the information as necessary.




## Before you begin

  * Compute Engine installs the diagnostic tool by default on public versions of Windows Server images later than `v20190714`. Otherwise, if your Windows Server image version is earlier than `v20190714`, or you are using a custom image, install the tool by using the `googet install google-compute-engine-diagnostics` command. 
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




## Diagnostic information collected from the VM

This diagnostic tool collects information about the following:

  * **Disks** :

    * [Windows Management Instrumentation (WMI)](https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page) object information about [disks](https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/msft-disk), [partitions](https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/msft-partition), and [volumes](https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/msft-volume)
  * **Events** :

    * [Windows Events](https://learn.microsoft.com/en-us/windows/win32/events/windows-events), including application events and system events
  * **Networks** :

    * WMI object information about [firewall rules](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/rules), and output from [ipconfig](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ipconfig), [netstat](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netstat), [nslookup](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/nslookup), [ping](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ping), [route](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/route_ws2008), and [tracert](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tracert)
  * **Programs** :

    * WMI object information about [processes](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-process), [scheduled tasks](https://learn.microsoft.com/en-us/powershell/module/scheduledtasks/get-scheduledtask?view=win10-ps), [services](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-service), and [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/windows-server-gke)
  * **System** :

    * WMI object information about [users](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-useraccount), Remote Desktop Protocol (RDP) settings by using [the rdp_status.ps1 script](https://github.com/GoogleCloudPlatform/compute-image-tools/blob/master/cli_tools/diagnostics/rdp_status.ps1), and output from [bcdedit](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit), [driverquery](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/driverquery), [msinfo32](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msinfo32), [pnputil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/pnputil), and [systeminfo](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/systeminfo), and [memory dump](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/memory-dump-file-options) logs



For detailed information about how Compute Engine collects this information, see the [public GitHub repository](https://github.com/GoogleCloudPlatform/compute-image-tools/tree/master/cli_tools/diagnostics).

## Limitations

  * You can only collect diagnostic information from VMs created based on Windows Server.



## Required roles

To get the permissions that you need to run the diagnostic tool by using Google Cloud CLI, ask your administrator to grant you the [Service Account Token Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Collecting diagnostic information from a VM

Run the diagnostic tool either directly from the VM, or remotely, by using the Google Cloud CLI.

###  gcloud 

  1. If you haven't already, grant the `iam.serviceAccountTokenCreator` role on the project to the user account or service account that will run the `gcloud compute diagnose export-logs` command:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member user:EMAIL \
             --role roles/iam.serviceAccountTokenCreator
         

Replace the following:

     * `PROJECT_ID`: the project ID
     * `EMAIL`: the email address to grant the `iam.serviceAccountTokenCreator` role
  2. Export the diagnostic information as an object to a Cloud Storage bucket using the [`diagnose export-logs` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/diagnose/export-logs).
         
         gcloud compute diagnose export-logs VM_NAME \
           [--collect-process-traces]
         

The optional `--collect-process-traces` flag specifies whether the diagnostic tool collects a 10 minute trace of the running system, which includes CPU, disk, file, and network activity. On Windows-based VMs, this uses the [Windows Performance Recorder](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder).

Replace `VM_NAME` with the name of the VM to collect diagnostic information from.

  3. The log exporting process might take a few minutes to complete. View the status by using the [`gcloud compute instances get-serial-port-output` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/get-serial-port-output).

  4. Compute Engine formats the name of the bucket containing the diagnostic information as `diagnostic_logs_project_PROJECT_NUMBER`. View or download the bucket by using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/storage), or, in the Google Cloud console, from the **Cloud Storage** page:

[Go to Storage](https://console.cloud.google.com/storage)




###  Locally (Windows only) 

To run the diagnostic tool from within a Windows VM, do the following:

  1. Connect to the Windows VM.

  2. Open a command prompt or PowerShell window with **Administrator** privileges.

  3. Navigate to the directory containing the diagnostic tool:
         
         cd "C:\Program Files\Google\Compute Engine\diagnostics"
         

  4. Run the diagnostic tool:
         
         .\diagnostics.exe
         

After the tool finishes running, it saves the collected diagnostic information to the compressed file `logs.zip` in your current working directory.




**Optional flags**

  * `-trace`: captures additional tracing information. The tool captures a 10-minute trace of the system using the [Windows Performance Recorder](https://docs.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder), which includes CPU, disk, file, and network activity.



## What's next

  * Learn how to [capture screenshots from VMs](https://docs.cloud.google.com/compute/docs/instances/capturing-vm-screenshots).

  * Learn how to [Troubleshoot Windows instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows).

  * Learn how to [Troubleshoot RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
