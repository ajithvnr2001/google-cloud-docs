---
url: https://docs.cloud.google.com/migration-center/docs/download-collector-cli/
title: Download Migration Center discovery client CLI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:22:21.080551+00:00
---

# Download Migration Center discovery client CLI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/download-collector-cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Download Migration Center discovery client CLI Stay organized with collections  Save and categorize content based on your preferences. 

To discover your assets, you need to download the Migration Center discovery client CLI to a machine that has access to all your target assets. The machine can be a physical server or a virtual machine (VM) instance. The `mcdc` CLI executable is available in two versions, Linux and Windows, depending on the OS of the machine where you want to install it.

The `mcdc` CLI performs the guest discovery by running collection scripts remotely on your target machines from the machine where it is installed. It can also find and collect data from multiple machines using the IP range scan. You can run a guest discovery on VMs running on VMware, and on machines with a connection to the machine hosting the `mcdc` CLI.

Alternatively, to perform a discovery on VMs hosted on AWS and Azure, or on your on-premises machines without SSH access, you need to download the guest collection script and run it locally. Use `mcdc-linux-collect.sh` on Linux machines and `mcdc-windows-collect.ps1` on Windows machines.

**Note:** In environments where you have hundreds or thousands of VMs, you might already have tools to automate the process of downloading and running the guest collection script on each VM.

This document describes how to download the `mcdc` CLI and the collection scripts to discover and collect your infrastructure data.

## Before you begin

  * [Review the requirements for downloading the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements)



## Download `mcdc` CLI

Depending on the OS of the machine, download the Linux or Windows executable of the `mcdc` CLI.

###  Linux 

  * Download the latest version of the `mcdc` CLI on a Linux machine and make it executable:


    
    
    curl -O "https://mc-release.storage.googleapis.com/mcdc/$(curl -s https://mc-release.storage.googleapis.com/mcdc/latest)/mcdc"
    chmod +x mcdc
    

###  Windows 

  * To download the latest version of the `mcdc` CLI on a Windows machine with Powershell and `Invoke-WebRequest`:


    
    
    $ProgressPreference = 'SilentlyContinue'; $version = Invoke-RestMethod -Uri 'https://mc-release.storage.googleapis.com/mcdc/latest'; Invoke-WebRequest -Uri  "https://storage.googleapis.com/mc-release/mcdc/$($version.Trim())/windows/mcdc.exe" -OutFile mcdc.exe
    

  * To download the latest version of the `mcdc` CLI on a Windows machine with Command Prompt and `curl`:


    
    
    for /f usebackq %V in (`curl -s https://mc-release.storage.googleapis.com/mcdc/latest`) do curl -O https://mc-release.storage.googleapis.com/mcdc/%V/windows/mcdc.exe
    

  * To download the latest version of the `mcdc` CLI with a direct link:


    
    
    https://mc-release.storage.googleapis.com/mcdc/current/windows/mcdc.exe
    

## View help information for `mcdc` CLI

  * To view help information for the `mcdc` CLI, use the `--help` flag:

### Linux
        
        ./mcdc --help

### Windows
        
        mcdc.exe --help

  * To view help for a specific command, use the `--help` flag with the command. For example, to view help for the `import` command, run the following command:

### Linux
        
        ./mcdc discover import --help

### Windows
        
        mcdc.exe discover import --help




## Download guest collection scripts

To download the guest collection scripts on the target machine, perform the steps in the following sections.

### Download guest collection script on a Linux machine

On a Linux machine, to download `mcdc-linux-collect.sh`, follow these steps:

  1. Log in to the machine.

**Note:** To generate optimal assessment results, it is recommended that for running a guest discovery, you log in with a user that has administrator rights.
  2. Download the guest collection script to the machine and make it executable:
         
         curl -O "https://mc-release.storage.googleapis.com/mcdc/$(curl -s https://mc-release.storage.googleapis.com/mcdc/latest)/mcdc-linux-collect.sh"
         chmod +x mcdc-linux-collect.sh
         




### Download guest collection script on a Windows machine

On a Windows machine, to download `mcdc-windows-collect.ps1`, follow these steps:

  1. Log in to your machine and open PowerShell.

**Note:** To generate optimal assessment results, it is recommended that for running a guest discovery, you log in with a user that has administrator rights.
  2. Download the guest collection script to the machine:
         
         $version = Invoke-WebRequest -UseBasicParsing https://mc-release.storage.googleapis.com/mcdc/latest
         $WebClient = New-Object System.Net.WebClient
         $WebClient.DownloadFile("https://mc-release.storage.googleapis.com/mcdc/"+$version+"/mcdc-windows-collect.ps1", (Get-Location).Path + "\mcdc-windows-collect.ps1")
         




## What's next

  * Learn how to discover assets using the following methods:

    * [Inventory discovery](https://docs.cloud.google.com/migration-center/docs/run-inventory-discovery)
    * [Guest discovery](https://docs.cloud.google.com/migration-center/docs/run-guest-discovery)
    * [IP range scan](https://docs.cloud.google.com/migration-center/docs/run-ip-range-scan)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
