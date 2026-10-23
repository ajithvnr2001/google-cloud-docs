---
url: https://docs.cloud.google.com/migrate/containers/docs/windows-assessment-tool/
title: Using the Windows discovery tool \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:44.080243+00:00
---

# Using the Windows discovery tool  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/windows-assessment-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Using the Windows discovery tool

This release of Migrate to Containers includes a new tool, called the _fit assessment_ tool, that replaces the existing Windows discovery tool. See [Using the fit assessment tool](https://docs.cloud.google.com/migrate/containers/docs/fit-assessment) for more information. 

Migrate to Containers provides a self-service tool that you run on a Windows VM workload to determine the workload's fit for migration to a container.

The tool outputs a zip file that indicates whether or not the Windows VM is a potential fit for migration. The name of the file indicates the results:

  * `info-hostname-timestamp.zip` indicates that the VM is a potential fit to be migrated.
  * `info-hostname-timestamp-**NOFIT**.zip` indicates that the VM is not fit to be migrated. Typically a NOFIT results from a missing or incorrect version of IIS.



## How the tool works

Because Migrate to Containers requires Windows VMs to run Microsoft IIS 7 or higher, the discovery tool collects IIS and general system information.

## Prerequisites

To run the Windows discovery tool:

  * You must have a 64-bit version of Windows.
  * You must be an administrator on the Windows VM. 



## Downloading and running the tool

The tool is packaged as a single .exe file. You must download the tool before you can execute it.

**To evaluate a VM** :

  1. Log in to your VM. 

  2. Create a directory for the tool: 
         
         > mkdir m4a 
         > cd m4a

  3. Download the tool to the VM from <https://storage.googleapis.com/anthos-migrate-release/v1.9.0/windows/amd64/collect_info.exe>.

  4. Run the tool on the VM as an administrator: 

You can either right click on the tool in the File Manager and select **Run as Administrator** , or open a PowerShell command window as an administrator:
         
         > collect_info.exe

The tool outputs a zip file named `info-hostname-timestamp.zip` or `info-hostname-timestamp-NOFIT.zip` to the current directory.

The timestamp is in the format `YYYMMDDhhmmss`. See Output zip file format for a description of the zip file. 

You can optionally use the `-o` option to specify the path to the output directory. For example: 
         
         > collect_info.exe -o /home/mydir

To see help information, use: 
         
         > collect_info.exe -h




## Output zip file format

The output zip file contains:

  * A log file named `log.log`.
  * A file named `collect_info_version.txt` containing the version of the tool.
  * Directories containing information about the system: 
    * `computer_info`
    * `iis`
    * `gac`
    * `odbc`



The contents of each directory are described below. 

### The computer_info directory

The `computer_info` directory contains:

File | Description  
---|---  
`hosts.txt` | Copy of machine `hosts` file  
`installed_programs.json` | Information of installed programs  
`ipconfig_out.txt` | Output of `ipconfig /all`.  
`msinfo32_out.txt` | Report from `msinfo32` utility.  
`netstat_out.txt` | Information of all connections and listening ports with executables involved in creating each connection or listening port.  
`routing_tables.txt` | The machine's routing tables.  
`schedtasks.csv` | Information of scheduled tasks  
`systeminfo_out.csv` | Output of `systeminfo` utility in CSV format.  
`win32_product_installed_programs.json` | Information of installed programs provided by `Win32_Product` WMI class.  
`windows_features.json` | Information on Windows features.  
  
### The iis directory

The `iis` directory contains information about IIS, sites and .NET configurations, and additional selected information that might help us to understand the applications.

**Note:** If IIS is not installed on the VM then this directory is empty.

The directory contains following files:

File | Description  
---|---  
`Framework[64]_v<version>_config` | Copy of all .NET global config directories, for each framework and version.  Includes global.configs and machine.configs, for example `Framework_v2.0.50727_config`, `Framework64_v4.0.30319_config`. The source for this information is `%windir%\Microsoft.NET\Framework[64]\version\config`.  
`iis_config` | A copy of the IIS config directory including configs and schemes.   
`sites_files` | A directory contains exported files from IIS sites, meaning copies of all `web.config` files in sites.  
`sites.json` | Information on all sites configured in IIS, including recursive directory listing for each site with ACL information of files.  
`version.txt` | The IIS version.  
  
#### Handling secrets in the iis directory

Copies of config files and directories (IIS, global .NET, and sites) might contain secrets. These files include `applicationHost.config` and `web.config`. 

The `collect_info.exe` tool filters passwords from [connection strings](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/connection-strings) in those files ([ .NET 3.5+ format](https://www.connectionstrings.com/store-connection-string-in-webconfig/)). Every password is replaced with `***`. You can remove and filter any additional sensitive information manually from the output zip file.

### The gac directory

The `gac` directory contains information of the .NET [Global Assembly Cache](https://docs.microsoft.com/en-us/dotnet/framework/app-domains/gac):

File | Description  
---|---  
`clr2.txt` | A list of assemblies in CLR2.0 GAC.  
`clr4.txt` | A list of assemblies in CLR4.0 GAC.  
  
### The odbc directory

The `odbc` directory contains information of the ODBC [DSNs](https://support.microsoft.com/en-us/help/966849/what-is-a-dsn-data-source-name) and installed drivers:

File | Description  
---|---  
`system_dsn_32.reg` | Exported registries with all information of system DSNs and drivers for 32-bit.  
`system_dsn_64.reg` | Exported registries with all information of system DSNs and drivers for 64-bit.  
`user_dsn.reg` | Exported registries with all information of user DSNs and drivers for 32- and 64-bit.  
  
#### Handling secrets in the odbc directory

ODBC DSNs might contain secrets. The `collect_info.exe` tool filters out passwords from the exported .reg files. You can remove and filter any additional sensitive information manually from the output zip file.

## What's next

  * [Setting up Migrate to Containers](https://docs.cloud.google.com/migrate/containers/docs/setting-up-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
