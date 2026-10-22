---
url: https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus-windows/
title: Monitoring GPU performance on Windows VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:39.415383+00:00
---

# Monitoring GPU performance on Windows VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitoring GPU performance on Windows VMs Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

To help with better utilization of resources, you can track the GPU usage rates of your virtual machine (VM) instances.

When you know the GPU usage rates, you can perform tasks such as setting up [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that can be used to autoscale resources.

To review GPU metrics using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs), complete the following steps:

  1. On each VM, set up the GPU metrics reporting script. This script installs the GPU metrics reporting agent. This agent runs at intervals on the VM to collect GPU data, and sends this data to Cloud Monitoring.
  2. On each VM, run the script.
  3. On each VM, set GPU metrics reporting agent to automatically start on boot.
  4. View logs in Google Cloud Cloud Monitoring.



## Required roles

To monitor GPU performance on Windows VMs, you need to grant the required Identity and Access Management (IAM) roles to the following principles:

  * The [service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account#serviceaccountname) that is used by the VM instance
  * Your user account



To ensure that you and the VM's service account has the necessary permissions to monitor GPU performance on Windows VMs, ask your administrator to grant the following IAM roles to you and the VM's service account on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give you and the VM's service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up the GPU metrics reporting script

### Requirements

On each of your VMs, check that you meet the following requirements:

  * Each VM must have [GPUs attached](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).
  * Each VM must have a [GPU driver installed](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#verify-driver-install).



### Download the script

Open a PowerShell terminal as an administrator and use the [`Invoke-WebRequest` command](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.1) to download the script.

`Invoke-WebRequest` is available on PowerShell 3.0 or later. Google Cloud recommends that you use `ctrl+v` to paste the copied code blocks.
    
    
    mkdir c:\google-scripts
    cd c:\google-scripts
    Invoke-Webrequest -uri https://raw.githubusercontent.com/GoogleCloudPlatform/compute-gpu-monitoring/main/windows/gce-gpu-monitoring-cuda.ps1 -outfile gce-gpu-monitoring-cuda.ps1
    

## Run the script
    
    
    cd c:\google-scripts
    .\gce-gpu-monitoring-cuda.ps1
    

## Configure the agent to automatically start on boot

To ensure that the GPU metrics reporting agent is set up to run on system boot, use the following command to add the agent to the Windows Task Scheduler.
    
    
    $Trigger= New-ScheduledTaskTrigger -AtStartup
    $Trigger.ExecutionTimeLimit = "PT0S"
    $User= "NT AUTHORITY\SYSTEM"
    $Action= New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "C:\google-scripts\gce-gpu-monitoring-cuda.ps1"
    $settingsSet = New-ScheduledTaskSettingsSet
    # Set the Execution Time Limit to unlimited on all versions of Windows Server
    $settingsSet.ExecutionTimeLimit = 'PT0S'
    Register-ScheduledTask -TaskName "MonitoringGPUs" -Trigger $Trigger -User $User -Action $Action -Force -Settings $settingsSet
    

## Review metrics in Cloud Monitoring

  1. In the Google Cloud console, go to the **Metrics Explorer** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Expand the **Select a metric** menu.

  3. In the **Resource** menu, select **VM Instance**.

  4. In the **Metric category** menu, select **Custom**.

  5. In the **Metric** menu, select the metric to chart. For example `custom/instance/gpu/utilization`.

**Note:** Custom metrics might take some time to display.
  6. Click **Apply**.

Your GPU utilization should resemble the following output:

![Cloud Monitoring initiation.](https://docs.cloud.google.com/static/compute/images/gpus/gpu_monitoring.png)




## Available metrics

Metric name | Description  
---|---  
  
#### instance/gpu/utilization

| Percent of time over the past sample period during which one or more kernels was executing on the GPU.  
  
#### instance/gpu/memory_utilization

| Percent of time over the past sample period during which global (device) memory was being read or written.   
  
#### instance/gpu/memory_total

| Total installed GPU memory.  
  
#### instance/gpu/memory_used

| Total memory allocated by active contexts.  
  
#### instance/gpu/memory_used_percent

| Percentage of total memory allocated by active contexts. Ranges from 0 to 100.  
  
#### instance/gpu/memory_free

| Total free memory.  
  
#### instance/gpu/temperature

| Core GPU temperature in Celsius (°C).  
  
## What's next?

  * To handle GPU host maintenance, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).
  * To improve network performance, see [Use higher network bandwidth](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
