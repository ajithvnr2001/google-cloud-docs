---
url: https://docs.cloud.google.com/sql/docs/sqlserver/cmad-diagnosis-tool/
title: Customer-managed Active Directory Diagnosis tool for Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:33.316924+00:00
---

# Customer-managed Active Directory Diagnosis tool for Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/cmad-diagnosis-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Customer-managed Active Directory Diagnosis tool for Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

The customer-managed Active Directory (CMAD) Diagnosis tool is a utility PowerShell script that helps you to troubleshoot Active Directory setup issues with your domain before or during integration with Cloud SQL in Google Cloud.

The tool performs various checks for issues, such as closed ports, domain controller (DC) reachability, account status, and organizational unit (OU) existence and permissions. It runs on a Windows VM that is one of the domain controllers or a domain-joined machine for your Active Directory domain.

This page describes how to use the CMAD Diagnosis tool for Cloud SQL and explains the checks that the tool performs.

## Prerequisites

Ensure that you have the following components set up before proceeding to use the CMAD Diagnosis tool:

  * An Active Directory domain.
  * An Active Directory administrator account with permissions to join computers to the target OU.
  * An Organizational Unit (OU) in Active Directory where Cloud SQL computer accounts will be created.
  * If running the script on a domain-joined VM (instead of a domain controller), the [Active Directory module for PowerShell](https://learn.microsoft.com/en-us/windows-server/administration/install-remote-server-administration-tools) (`RSAT-AD-PowerShell`) must be installed.



## How to use the CMAD Diagnosis tool

To use the CMAD Diagnosis tool, perform the following steps:

  1. Log on to any one of the domain controllers or a VM joined to the Active Directory domain.
  2. [Download the `diagnose_cmad.ps1` script](https://github.com/GoogleCloudPlatform/cloud-sql-active-directory-diagnosis-tool/blob/main/diagnose_cmad.ps1) on the VM.
  3. Launch PowerShell as Administrator.
  4. Run the `diagnose_cmad.ps1` script in the PowerShell window using the following command:
         
         C:\SCRIPT_PATH\diagnose_cmad.ps1

Replace SCRIPT_PATH with the path to the directory where you downloaded the script.

  5. Enter the following information when prompted:

**Note:** Some checks require administrator privileges. If you didn't launch Powershell as Administrator earlier, you are prompted to choose to run it as Administrator.
     * On-premises domain name, such as `my-domain.com`
     * AD administrator account, such as `myadmin`
     * Target OU, such as `OU=cloud,DC=my-domain,DC=com`



The tool then performs a number of checks, as described in [Checks performed by the CMAD Diagnosis tool](https://docs.cloud.google.com/sql/docs/sqlserver/cmad-diagnosis-tool#checks).

## Checks performed by the CMAD Diagnosis tool

Check| Description | Notes and recommendation  
---|---|---  
Available domain controllers  |  Issues a ping to the IP address of each domain controller on the on-premises domain to ensure they are reachable.  |  The remaining checks proceed on the IP addresses that were reachable. In case of failure of this check, ensure network connectivity to the remaining on-premises domain controllers. To learn more, see [ Creating the network infrastructure](https://docs.cloud.google.com/architecture/deploy-an-active-directory-forest-on-compute-engine#creating_the_network_infrastructure.).   
Ports  |  Verifies that all the required TCP and UDP ports for AD are open on all the on-premises domain controllers.  |  This check returns a warning status for the RPC port range (49152-65535) because it does not have a consistent list of open ports. We recommend that you verify that there is a firewall rule set for allowing this range. To learn more, see [ Customer-managed Active Directory firewall rules](https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmad#customer-managed-firewall-rules).   
DC Replication  |  Looks for any AD replication failures between the on-premises domain controllers.  |  If the script is run on an on-premises domain joined VM, expect a failed status if Powershell is not run as an Active Directory domain user. In case of failure of this check, follow the steps given in [ Testing the installation](https://docs.cloud.google.com/architecture/deploy-an-active-directory-forest-on-compute-engine#testing_the_installation).   
Kerberos Service (SRV) records  |  Queries the local DNS for `_kerberos._tcp` and `_kerberos._udp` SRV records and verifies that the target hosts correctly match the provided domain name.   
  
To learn more, see the [Microsoft documentation for SRV records](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created).  |  If this check fails, then verify that your Active Directory domain's DNS SRV records exist and are configured correctly.   
AD administrator account status  |  Validates that the administrator account specified for CMAD integration exists, is enabled, is not locked out, and has not expired.  |  If this check fails, then unlock the user account, enable the account in Active Directory Users and Computers (ADUC), or update the credentials in Secret Manager if the password has expired.   
Organizational Unit (OU)  |  Verifies that the target Organizational Unit (OU) Distinguished Name (DN) exists in Active Directory.  |  If this check fails, then verify that the target OU exists in Active Directory and that the DN provided (for example, `OU=cloud,DC=my-domain,DC=com`) is formatted correctly.   
OU permissions  |  Verifies that the Active Directory administrator account has the permissions that Cloud SQL requires on the target OU, including permissions that the account gets through its group memberships.  |  If this check fails, then delegate the missing permissions to the administrator account, as described in [Before you begin](https://docs.cloud.google.com/sql/docs/sqlserver/cmad#before-you-begin) in the CMAD overview, and remove any **Deny** permission entries on the OU that apply to the account or its groups.  If this check returns a warning, then the tool couldn't read the account's group memberships. Verify whether the account gets the missing permissions through a group.   
  
## What's Next

  * To share your feedback, you can use [GitHub Issues](https://github.com/GoogleCloudPlatform/cloud-sql-active-directory-diagnosis-tool/issues).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
