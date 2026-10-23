---
url: https://docs.cloud.google.com/migration-center/docs/run-guest-discovery/
title: Run a guest discovery \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:15.413411+00:00
---

# Run a guest discovery  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/run-guest-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Run a guest discovery Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to run the different guest discovery methods that the `mcdc` CLI provides.

Guest discovery lets you scan and collect data about the running applications on your machines, which includes both virtual machine (VM) instances and physical servers. It also collects data about the machine configuration, hardware, network, as well as open files, services, and processes.

For machines running on platforms for which the Migration Center discovery client CLI doesn't support [inventory discovery](https://docs.cloud.google.com/migration-center/docs/run-inventory-discovery), such as machines running on-premises, as well as for a full assessment of VMs running on VMware, AWS, and Azure, you can run a guest discovery. Guest discovery uses a guest collection script to collect data about the machine and writes that data to a guest collection tar file for Linux machines, or zip file for Windows machines.

The machine hosting the `mcdc` CLI uploads the script to the target machine, runs it, and then downloads the results. You can run the script locally on the target machine, or run it remotely. Depending on your infrastructure, you can choose to use the `mcdc` CLI in the following ways:

  * For Linux and Windows VMs deployed on VMware, the `mcdc` CLI supports remote execution with the `discover vsphere` command.
  * For Linux machines accessible by the `mcdc` CLI, you can perform a remote discovery using SSH with the `discover ssh` command.
  * For Windows machines accessible by the `mcdc` CLI, you can perform a remote discovery using Windows Management Instrumentation (WMI) with the `discover wmi` command.
  * For Linux and Windows machines without connection to the `mcdc` CLI, you can download and run the guest collection scripts locally, and then manually import the collected data to the machine that's hosting the `mcdc` CLI.



The guest collection script runs a series of commands to gather information about the source machine and might also collect potentially sensitive data such as command-line arguments, network information, or environment variables and arguments in running processes.

**Important:** Sensitive data such as personally identifiable information (PII) is never sent to Google or other third party. The data remains on the machine where it is collected during the `mcdc` CLI run.

## Before you begin

  1. Review the [requirements for downloading and running the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements).
  2. Review the [requirements for downloading and running the guest collection scripts](https://docs.cloud.google.com/migration-center/docs/review-collector-cli-requirements#requirements_for_downloading_and_running_guest_collection_scripts).
  3. Complete the steps to [download `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/download-collector-cli).



## Collect data remotely using VMware tools

For VMs hosted on vSphere, the `mcdc` CLI can use VMware tools to deploy and run the collection scripts remotely on both Linux and Windows VMs. When using VMware tools, the `mcdc` CLI tool does the following:

  * Uploads the collection script to the VM.
  * Runs the script on the VM.
  * Downloads and imports the results.



Two sets of credentials are required to collect data remotely:

  * The vCenter server username passed to the `mcdc` CLI to connect to vSphere, which must have the following privileges on the VM: 
    * Guest operation modifications
    * Guest operation program execution
    * Guest operation queries
  * User credentials for the VM: 
    * On Windows, you must have administrator privileges.
    * On Linux, you can use root or non-root credentials. For more information, see Guest discovery on Linux.



To collect data using VMware tools, follow these steps:

  1. Sign in to your Linux VM that's hosting the `mcdc` CLI.
  2. Change to the directory where you downloaded the `mcdc` CLI.
  3. Ensure that the VM is powered on.
  4. Run the guest discovery:

### Linux
         
         ./mcdc discover vsphere guest --url https://VSPHERE_URL -u VCENTER_USER --vm-user VM_USER VM_ID

### Windows
         
         mcdc.exe discover vsphere guest --url https://VSPHERE_URL -u VCENTER_USER --vm-user VM_USER VM_ID

Replace the following:

     * VCENTER_USER: the vCenter server user
     * VM_USER: the VM user
     * VM_ID: the name of the VM or MOREF
**Important:** If the vSphere cluster has multiple data centers, then you must use the `--dc` flag to specify the data center name.
  5. When prompted, enter the password for the VCENTER_USER and the VM_USER.




To collect data from multiple vSphere VMs in parallel using VMware tools, follow these steps:

**Important:** All the VMs you want to collect from must have the same username and password. If you have separate credentials for your Windows or Linux VMs, then you can select an operating system using the `--os-family` flag.

  1. Sign in to your Linux VM that's hosting the `mcdc` CLI.
  2. Change to the directory where you downloaded the `mcdc` CLI.
  3. Ensure that all VMs are powered on.
  4. Run the guest discovery:

### Linux
         
         ./mcdc discover vsphere guest all --url https://VSPHERE_URL -u VCENTER_USER --vm-user VM_USER --timeout TIMEOUT_IN_SECONDS

### Windows
         
         mcdc.exe discover vsphere guest all --url https://VSPHERE_URL -u VCENTER_USER --vm-user VM_USER --timeout TIMEOUT_IN_SECONDS

Replace TIMEOUT_IN_SECONDS with the timeout in seconds.

Optionally, limit the discovery to only Windows or Linux VMs using the `--os-family` flag, or change the level of parallelism using the `--max-parallelism` flag.

  5. When prompted, enter the password for the VCENTER_USER and VM_USER.

  6. You can also scope the discovery to specific VMs using the `--path` flag, as described for VMware in [Run an inventory discovery](https://docs.cloud.google.com/migration-center/docs/run-inventory-discovery).




You can export and assess this collected data online in Migration Center, or run an offline assessment.

## Guest discovery on Linux

If you run guest discovery with root access (for example, by using `sudo`), `mcdc` CLI collects more data from your machine than if you run it using non-root user credentials.

The following table compares the data collected by the guest discovery script based on privilege level.

**Click to see what data is collected**

Category | Data | Non-root access | Root access  
---|---|---|---  
Hardware | Product serial number | Skipped:  
requires root access. | Collected:  
from `/sys/class/dmi/id/product_serial`.  
Networking | Process-to-port mapping | Partial:  
connection information is collected, but PID/program names for other users' processes are not collected. | Full:  
all listening ports and connections are mapped to their respective PIDs and program names.  
Middleware | JBoss / Tomcat internals | Limited:  
only environment, descriptors, and limits for the current user's processes are accessible. | Full:  
reads process data (`environ`, `fd`, `limits`) for all middleware instances from `/proc/[PID]`.  
Storage | Block devices and mounts | Full:  
standard tools such as `lsblk` and `df` that are accessible to users. | Full:  
block device details and system mounts.  
Configuration | Restricted system files | Partial:  
doesn't collect information from files such as `/etc/exports` and some Apache configurations that might be unreadable depending on permissions. | Full:  
root bypasses all file permission restrictions to gather the required configuration files.  
Security | SELinux status | Restricted:  
detailed configuration details is not collected. | Full:  
complete output is collected from the `sestatus` tool.  
Inventory | Installed packages | Full:  
standard package managers (`dpkg`, `rpm`) are accessible to all users. | Full:  
a complete list of all installed system packages are collected.  
  
## Collect data remotely over SSH

If the machine that's hosting the `mcdc` CLI has SSH access to the target Linux machine (Windows machines are not supported), then the `mcdc` CLI can connect to the target machine over SSH to collect data.

When using SSH, the `mcdc` CLI does the following:

  1. Uploads the collection script to the machine.
  2. Runs the script on the machine with the machine user credentials passed to the `mcdc` CLI.

**Note:** While the machine user credentials don't require root access, having root access allows `mcdc` CLI to collect all assessment data.
  3. Downloads and imports the results.




### Supported SSH modes

If you're using the `mcdc` CLI on a Linux machine, you can use two modes to run SSH:

  * **Default:** uses the `ssh` binary and configurations on the `mcdc` CLI machine. Default mode can use the local SSH configuration files by default, such as `~/.ssh/config` and `~/.ssh/known_hosts`, of the workstation that's hosting it.

Enter the password when prompted, or use `sshpass` to pass the password or private key file passphrase on the command line. For example:
        
        sshpass -p password mcdc discover ssh IP_ADDRESS
        

Replace IP_ADDRESS with the IP address of the machine.

  * **Embedded:** uses the built-in SSH library. This mode lets you use the embedded SSH client if default mode malfunctions in your environment. However, it doesn't use the local SSH configuration files by default. You can use the `-i` flag to specify an SSH private key file.




If you're using the `mcdc` CLI on a Windows machine, only **embedded** mode is supported.

### Run the collection

To collect data over SSH, follow these steps:

  1. Sign in to the Linux machine that's hosting the `mcdc` CLI.
  2. Change to the directory where you downloaded the `mcdc` CLI.
  3. Collect data.

### Linux
         
         ./mcdc discover ssh IP_HOSTNAME

### Windows
         
         mcdc.exe discover ssh IP_HOSTNAME

To discover and collect database assets, use the `--db-engine` flag:

### Linux
         
         ./mcdc discover ssh IP_HOSTNAME --db-engine=DB_ENGINE

### Windows
         
         mcdc.exe discover ssh IP_HOSTNAME --db-engine=DB_ENGINE

Replace the following:

     * IP_HOSTNAME: the IP hostname of the machine.
     * DB_ENGINE: the database engine to collect. Supported values are `sqlserver`, `mysql`, `postgresql`.
  4. The SSH private key file of the user invoking the `mcdc` CLI is used for SSH authentication.

When prompted, enter the username of an account on the Linux machine. The collection script runs using these credentials. If the SSH private key of the user invoking the `mcdc` CLI fails to authenticate to the machine with the username, you're also prompted for a password.




### Additional scenarios when using SSH

See the following scenarios where you might need to modify the command:

  * To specify the machine user with default mode, use the `-u` flag:

### Linux
        
        ./mcdc discover ssh -u USER IP_HOSTNAME

### Windows
        
        mcdc.exe discover ssh -u USER IP_HOSTNAME

Replace USER with the machine user.

When prompted, enter the password for the user.

  * To specify verbose mode, use the `-v` flag:

### Linux
        
        ./mcdc discover ssh -u USER -v IP_HOSTNAME

### Windows
        
        mcdc.exe discover ssh -u USER -v IP_HOSTNAME

  * To specify the SSH private key file, use the `-i` flag. For example, to specify `.ssh/my_private_key`:

### Linux
        
        ./mcdc discover ssh -i ~/.ssh/my_private_key -u USER IP_HOSTNAME

### Windows
        
        mcdc.exe discover ssh -i ~/.ssh/my_private_key -u USER IP_HOSTNAME

  * To specify the password on the command line, use embedded mode:

### Linux
        
        ./mcdc discover ssh --ssh-client embedded -u USER --passphrase PASSWORD IP_HOSTNAME

### Windows
        
        mcdc.exe discover ssh --ssh-client embedded -u USER --passphrase PASSWORD IP_HOSTNAME

Because the embedded form of the command doesn't use the local SSH configuration files by default, ensure that the user you specify in the command is able to access the machine over SSH and has privileges on the machine to execute the collection script.

  * To specify the SSH private key file with embedded mode, use the `-i` flag:

### Linux
        
        ./mcdc discover ssh --ssh-client embedded -i ~/.ssh/id_rsa -u USER --password PASSWORD IP_HOSTNAME

### Windows
        
        mcdc.exe discover ssh --ssh-client embedded -i ~/.ssh/id_rsa -u USER --password PASSWORD IP_HOSTNAME

  * The `mcdc` CLI command lets you specify most SSH flags. It then passes these flags to the `ssh` command using the `-a` or `--ssh-args` flag. For example, to use a socks proxy:

### Linux
        
        ./mcdc discover ssh -u USER -a '-o' -a 'ProxyCommand=nc -X 5 -x 127.0.0.1:proxy port %h %p' IP_HOSTNAME

### Windows
        
        mcdc.exe discover ssh -u USER -a '-o' -a 'ProxyCommand=nc -X 5 -x 127.0.0.1:proxy port %h %p' IP_HOSTNAME




You can export and assess this collected data online in Migration Center, or run an offline assessment.

## Collect data on an individual Linux machine

To perform a guest collection locally on a Linux machine, you can run the `mcdc-linux-collect.sh` script. Then, you can copy the tar file generated by the script into the machine that hosts the `mcdc` CLI, and import it with the `discover import` command.

If you want to collect all the possible data from your Linux machine, run the script with root access using `sudo`. If you run it with user privileges, `mcdc` CLI collects a more limited set of data. For more information, see Guest discovery on Linux.

  1. Sign in to your machine.
  2. Change to the directory where you downloaded the guest collection script.
  3. Run the collection script on the machine:

     * To run with root access:
           
           sudo ./mcdc-linux-collect.sh
           

     * To run without root access:
           
           ./mcdc-linux-collect.sh
           

The script outputs a tar file named `mcdc-collect-MACHINE_NAME-TIMESTAMP.tar` to the current directory. The timestamp is in the format `YYYY-MM-DD-hh-mm`. 

#### Click to see the guest collection tar file format

The tar file has the following format:
    
    collect.log # Log output of the script
     files # Directory containing files with their full path from root. For example:
       |- etc/fstab
       |- etc/hostname
       |- etc/network/interfaces
       |- ...
     commands # Output of commands run by the script:
       |- dpkg
       |- netstat
       |- ps
       |- ...
     found_paths # Text file with the list of installation directories
     machinename # Text file with machine name
     ostype # Text file with operating system type (Linux)
     timestamp # Text file with collection timestamp
     version # Text file with the version of the script
     

Optionally, you can pass the argument `--output` and specify the path where you want to save the tar file.

  4. Copy the collected data from the target machine to the host machine.

  5. Import the collected data on the host machine:

### Linux
         
         ./mcdc discover import PATH_TO_TAR

### Windows
         
         mcdc.exe discover import PATH_TO_TAR

Replace PATH_TO_TAR with the path to the tar file.




You can export and assess this collected data online in Migration Center, or run an offline assessment.

## Collect data remotely over WMI

If you want to perform a guest discovery on a target Windows machine with WMI support, you can use the `mcdc discover wmi` command on the Windows machine that's hosting the `mcdc` CLI. WMI collection is supported only on the Windows version of the `mcdc` CLI.

By default, the `mcdc` CLI collects data by using remote WMI calls, which is faster than script-based collection. However, remote WMI calls aren't supported on Windows Server 2008 and earlier versions. If you need to collect data from earlier Windows versions, or if you encounter issues when using WMI remote calls, you can use script-based collection instead by adding the `--script` flag.

When using WMI, the `mcdc` CLI does the following:

  1. Uploads the collection script to the machine.
  2. Runs the script on the machine with the machine user credentials passed to the `mcdc` CLI.

**Note:** While the machine user credentials don't require administrator access, having administrator access lets the `mcdc` CLI collect all the assessment data. For information about configuring WMI for remote access by non-administrator accounts, see [Set up remote WMI connection](https://learn.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-remotely-starting-with-vista#setting-up-a-remote-wmi-connection) and [Securing a Remote WMI Connection](https://learn.microsoft.com/en-us/windows/win32/wmisdk/securing-a-remote-wmi-connection).
  3. Downloads and imports the results to Migration Center.




To collect data over WMI, follow these steps:

  1. Sign in to the Windows machine that's hosting the `mcdc` CLI.
  2. Change to the directory where you downloaded the `mcdc` CLI.
  3. Collect data using one of the following methods:

     * To collect data with remote WMI calls, run the following command:
           
           mcdc.exe discover wmi IP_HOSTNAME
           

Replace IP_HOSTNAME with the IP hostname of the machine.

     * To collect data by using script-based collection, use the `--script` flag:
           
           mcdc.exe discover wmi --script IP_HOSTNAME
           

  4. Enter your credentials when prompted.




You can export and assess this collected data online in Migration Center, or run an offline assessment.

## Collect data on an individual Windows machine

To perform a guest collection locally on a Windows machine, you can run the `mcdc-windows-collect.ps1` script. Then, you can copy the zip file generated by the script into the machine that hosts the `mcdc` CLI, and import it with the `discover import` command.

  1. Sign in to your machine.
  2. Open PowerShell using the **Run as Administrator** option.
  3. Change to the directory where you downloaded the `mcdc` CLI.
  4. Run the collection script on the machine:
         
         powershell -ExecutionPolicy ByPass -File .\mcdc-windows-collect.ps1
         

  5. The script outputs a zip file named `mcdc-collect-MACHINE_NAME-TIMESTAMP.zip` to the current directory.

Optionally, you can include an output path to specify a different location:
         
         .\mcdc-windows-collect.ps1 PATH_FOR_OUTPUT.zip
         

  6. Import the collected data on the host machine:

### Linux
         
         ./mcdc discover import PATH_TO_TAR

### Windows
         
         mcdc.exe discover import PATH_TO_TAR

Replace PATH_TO_TAR with the path to the tar file.




You can export the collected data and assess it online in Migration Center, or run an offline assessment.

## What's next

  * Learn how to [run an IP range scan](https://docs.cloud.google.com/migration-center/docs/run-ip-range-scan).
  * Learn how to [export collected data to Migration Center](https://docs.cloud.google.com/migration-center/docs/export-collected-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
