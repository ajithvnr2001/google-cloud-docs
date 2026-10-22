---
url: https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/verify-setup/
title: Verifying VM Manager setup \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:05.844244+00:00
---

# Verifying VM Manager setup  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/verify-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Verifying VM Manager setup Stay organized with collections  Save and categorize content based on your preferences. 

Use this document to verify that VM Manager is set up properly. For information about setting up VM Manager, see [Set up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup).

To verify the setup, you can either use the troubleshoot command or perform manual checks on the virtual machine (VM) instance.

## Before you begin

  * For Windows VMs, use [PowerShell 3.0 or later](https://docs.microsoft.com/powershell/).
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




## Use the troubleshoot command

Use the [`os-config troubleshoot` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/troubleshoot) to verify the setup. If any of the checks fail, you are provided with feedback on how to fix the issue.
    
    
    gcloud compute os-config troubleshoot VM_NAME \
       --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM instance that you want to troubleshoot
  * `ZONE`: the zone where the instance is located



### Examples

  * Example 1: shows the output for the `os-config troubleshoot` command when the VM instance has issues with the setup
  * Example 2: shows the output for the `os-config troubleshoot` command when the VM instance is properly set up




###  Example 1 

To troubleshoot a VM instance called `my-instance-1` in zone `asia-east2-b`, run the following:
    
    
    gcloud compute os-config troubleshoot my-instance-1 \
        --zone=asia-east2-b
    

The output resembles the following:
    
    
    OS Config troubleshooter tool is checking if there are issues with the
    VM Manager setup for this VM instance.
    
    > Is the OS Config API enabled? Yes
    > Is the OS Config agent enabled? Yes
    > Is the OS Config agent up to date? No
    
    The version of OS Config agent running on this VM instance is not the
    latest version.
    See https://cloud.google.com/compute/docs/manage-os/upgrade-vm-manager#update-agent
    on how to update the agent.
    

###  Example 2 

To troubleshoot a VM instance called `my-instance-2` in zone `us-west1-b`, run the following:
    
    
    gcloud compute os-config troubleshoot my-instance-2 \
        --zone=us-west1-b
    

The output resembles the following:
    
    
    OS Config troubleshooter tool is checking if there are issues with the
    VM Manager setup for this VM instance.
    
    > Is the OS Config API enabled? Yes
    > Is the OS Config agent enabled? Yes
    > Is the OS Config agent up to date? Yes
    > Is a service account present on the instance? Yes
    > Is the OS Config Service account present for this instance? Yes
    > Does this instance have a public IP or Private Google Access? Yes
    This instance has a public IP.
    

## Manual verification

To manually verify that VM Manager is properly set up, complete the following checks:

  * OS Config API enabled
  * OS Config metadata is enabled
  * OS Config agent installed and running
  * Service account enabled
  * VM can communicate with the OS Config API



If VM Manager is properly setup but you still have issues, see [Troubleshooting VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager).

### Check if OS Config API is enabled

In your Google Cloud project, check if the API is enabled.

###  Console 

In the Google Cloud console, go to the **OS Config API** page.

[Go to OS Config API](https://console.cloud.google.com/apis/api/osconfig.googleapis.com/overview)

###  gcloud 
    
    
    gcloud services list --enabled
    

If the API is enabled, the output resembles the following: 
    
    
    osconfig.googleapis.com              OS Config API
    

If the API is not enabled, enable the [OS Config API](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-service-api).

### Check if metadata is enabled

###  Linux 

For project metadata, on the VM, complete the following steps:

  1. Query the project attributes endpoint:
         
         curl "http://metadata.google.internal/computeMetadata/v1/project/attributes/" \
         -H "Metadata-Flavor: Google"
         

If the agent metadata value is set, the output resembles the following:
         
         enable-osconfig
         

  2. If the `enable-osconfig` value displays, query the endpoint:
         
         curl "http://metadata.google.internal/computeMetadata/v1/project/attributes/enable-osconfig" \
         -H "Metadata-Flavor: Google"

If enabled, the endpoint returns `TRUE`.


**Note:** To check the instance metadata setting, replace `/project/attributes/` with `/instance/attributes/` in the request URL.

If the metadata is not enabled, enable the [OS Config metadata](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-metadata).

###  Windows 

For project metadata, on a VM, open a PowerShell terminal as an administrator and run the following command:

  1. Query the project attributes endpoint:
         
         $value = (Invoke-RestMethod `
                  -Headers @{'Metadata-Flavor' = 'Google'} `
                  -Uri "http://metadata.google.internal/computeMetadata/v1/project/attributes/")
         $value
         

If the agent metadata value is set, the output resembles the following:
         
         enable-osconfig
         

  2. If the `enable-osconfig` value displays, query the endpoint:
         
         $value = (Invoke-RestMethod `
                  -Headers @{'Metadata-Flavor' = 'Google'} `
                  -Uri "http://metadata.google.internal/computeMetadata/v1/project/attributes/enable-osconfig")
         $value
         

If enabled, the endpoint returns `TRUE`.

**Note:** To check the instance metadata setting, replace `/project/attributes/` with `/instance/attributes/` in the request URL.



If the metadata is not enabled, enable the [OS Config metadata](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-metadata).

### Check if the OS Config agent is installed and running

###  Linux 

To check whether your Linux VM has the agent installed, run the following command:
    
    
    sudo systemctl status google-osconfig-agent
    

If the agent is installed and running, the output resembles the following:
    
    
    google-osconfig-agent.service - Google OSConfig Agent
    Loaded: loaded (/lib/systemd/system/google-osconfig-agent.service; enabled; vendor preset:
    Active: active (running) since Wed 2020-01-15 00:14:22 UTC; 6min ago
    Main PID: 369 (google_osconfig)
     Tasks: 8 (limit: 4374)
    Memory: 102.7M
    CGroup: /system.slice/google-osconfig-agent.service
            └─369 /usr/bin/google_osconfig_agent
    

If the agent is not installed, install the [OS Config agent](https://docs.cloud.google.com/compute/vm-manager/docs/setup#agent-install).

###  Windows 

To check whether your Windows VM has the agent installed, run the following command:
    
    
    PowerShell Get-Service google_osconfig_agent

If the agent is installed and running, the output resembles the following:
    
    
    Status   Name               DisplayName
    ------   ----               -----------
    Running  google_osconfig... Google OSConfig Agent
    

If the agent is not installed, install the [OS Config agent](https://docs.cloud.google.com/compute/vm-manager/docs/setup#agent-install).

### Check if the service account is enabled

For information about service account requirements, see [Setup overview](https://docs.cloud.google.com/compute/vm-manager/docs/setup#overview).

###  Linux 

On the VM, run the following:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/" \
    -H "Metadata-Flavor: Google"
    

The output should at least include the default service account.
    
    
    default/
    

###  Windows 

On the VM, open a PowerShell terminal as an administrator and run the following command:
    
    
    $value = (Invoke-RestMethod `
             -Headers @{'Metadata-Flavor' = 'Google'} `
             -Uri "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/")
    $value
    

The output should at least include the default service account.
    
    
    default/
    

### Check if the VM can communicate with the OS Config API

To check if the VM can communicate with the OS Config API, run the following command on your Linux or Windows VM:
    
    
    ping osconfig.googleapis.com

To stop pinging the OS Config API, press **Control + C**.

If your VM is running within a private VPC network and does not have public internet access, check that you have enabled [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

After you enable Private Google Access, check that the VM can communicate with the OS Config API.

###  Linux 

On the VM, run the following:
    
    
     curl --ssl 'https://osconfig.googleapis.com/$discovery/rest' | head
    

If the VM can communicate with the OS Config API, the command output is similar to the following:
    
    
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
    0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{
    "discoveryVersion": "v1",
    "baseUrl": "https://osconfig.googleapis.com/",
    "ownerName": "Google",
    "version": "v1beta",
    "schemas": {
      "GooSettings": {
        "description": "Googet patching is performed by running `googet update`.",
        "properties": {},
        "id": "GooSettings",
    100  9569    0  9569    0     0   198k      0 --:--:-- --:--:-- --:--:--  198k
    

###  Windows 

On the VM, open a PowerShell terminal as an administrator and run the following:
    
    
     Invoke-RestMethod  -Headers @{'Metadata-Flavor' = 'Google'}
     -Uri 'https://osconfig.googleapis.com/$discovery/rest'
    

## What's next?

  * [View operating system details](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/view-os-details).
  * [Create an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment).
  * [Create patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).
  * [Troubleshooting VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
