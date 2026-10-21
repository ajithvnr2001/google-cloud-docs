---
url: https://docs.cloud.google.com/sql/docs/sqlserver/ad-diagnosis-tool/
title: Active Directory Diagnosis tool for Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:57.158404+00:00
---

# Active Directory Diagnosis tool for Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/ad-diagnosis-tool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Active Directory Diagnosis tool for Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

The Active Directory (AD) Diagnosis tool is a utility PowerShell script that helps you to troubleshoot AD setup issues with your on-premises domain and Cloud SQL for SQL Server instances in Google Cloud.

The tool performs various checks for issues, such as closed ports, FQDN lookups, and DNS issues. It runs on an on-premises Windows VM that is one of the domain controllers for your on-premises domain.

This page describes how to use the Active Directory Diagnosis tool for Cloud SQL and explains the checks that the tool performs.

## Prerequisites

Ensure that you have the following components set up before proceeding to use the AD Diagnosis tool:

  * An AD enabled on-premises domain.
  * A Managed AD domain in Google Cloud console.
  * A Cloud SQL for SQL Server instance joined to the Managed AD domain.



## How to use the AD Diagnosis tool

To use the AD Diagnosis tool, perform the following steps:

  1. Log on to any one of the on-premises domain controllers or a VM joined to the on-premises domain.
  2. [Download the `diagnose_ad.ps1` script](https://github.com/GoogleCloudPlatform/cloud-sql-active-directory-diagnosis-tool/blob/main/diagnose_ad.ps1) on the VM.
  3. Launch Powershell as Administrator.
  4. Run the `diagnose_ad.ps1` script in the Powershell window using the following command:
         
         powershell -command "& { . C:\\<var>SCRIPT_PATH</var>\\diagnose_ad.ps1; Run-Tool }"
         

  5. Enter the following information when prompted:

**Note:** Some checks require administrator privileges. If you didn't launch Powershell as Administrator earlier, you are prompted to choose to run it as Administrator.
     * On-premises domain name, such as `my-onprem-domain.com`
     * Managed AD domain name, such as `my-ad-domain.com`
     * List of SQL Server Active Directory FQDNs and private IP addresses. This list is available in the Google Cloud console on the instance's **Overview** page.



The tool then performs a number of checks, as described in [Checks performed by the AD Diagnosis tool](https://docs.cloud.google.com/sql/docs/sqlserver/ad-diagnosis-tool#checks).

## Checks performed by the AD Diagnosis tool

Check| Description | Notes and recommendation  
---|---|---  
Available domain controllers  |  Issues a ping to the IP address of each domain controller on the on-premises domain to ensure they are reachable.  |  The remaining checks proceed on the IP addresses that were reachable. In case of failure of this check, ensure network connectivity to the remaining on-premises domain controllers. To learn more, see [ Creating the network infrastructure](https://cloud.google.com/architecture/deploy-fault-tolerant-active-directory-environment#creating_the_network_infrastructure.).   
Ports  |  Verifies that all the required TCP and UDP ports for AD are open on all the on-premises domain controllers.  |  This check returns a warning status for the RPC port range (49152-65535) because it does not have a consistent list of open ports. We recommend that you verify that there is a firewall rule set for allowing this range. To learn more, see [ Opening firewall ports](https://cloud.google.com/managed-microsoft-ad/docs/create-trust?hl=en#opening-firewall)  
DNS server  |  Checks for a healthy and fault-tolerant AD setup.  |  This check returns a warning if the script is not run on an on-premises domain controller. We recommend that you [ deploy fault-tolerant AD setup by setting primary and secondary DNS servers.](https://cloud.google.com/architecture/deploy-fault-tolerant-active-directory-environment)  
FQDN (Managed AD domain)  |  Performs an nslookup for the Managed AD domain name that you provide.  |  This check validates if the Managed AD domain is reachable from the on-premises domain controller. In case of failure, try establishing network connectivity between your on-premises network and your Google Cloud Virtual Private Cloud (VPC). To learn more, see [ Establishing network connectivity](https://cloud.google.com/managed-microsoft-ad/docs/create-trust?hl=en#establishing-network).   
FQDN (SQL Server)  |  Performs an nslookup for the SQL Server FQDNs that you provide.  |  This check validates if your instance is reachable from the on-premises domain controller. In case of failure, try establishing network connectivity between your on-premises network and your Google Cloud Virtual Private Cloud (VPC). To learn more, see [ Establishing network connectivity](https://cloud.google.com/managed-microsoft-ad/docs/create-trust?hl=en#establishing-network).   
DC Replication  |  Looks for any AD replication failures between the on-premises domain controllers.  |  If the script is run on an on-premises domain joined VM, expect a failed status if Powershell is not run as an Active Directory domain user. In case of failure of this check, follow the steps given in [ Testing the installation](https://cloud.google.com/architecture/deploy-fault-tolerant-active-directory-environment#testing_the_installation).   
DNS Forwarding  |  Looks for conditional DNS forwarding setup on the on-premises domain controllers, which is required to route requests from on-premises domain controllers to Managed AD domain controllers.  |  This check can fail if the script is not run on an on-premises domain controller. We recommend that you [ configure DNS conditional forwarders](https://cloud.google.com/managed-microsoft-ad/docs/create-trust?hl=en#configuring-dns-forwarder).   
Trust setup  |  Verifies that AD trust is set up between the on-premises domain and the Managed AD domain.  |  This check verifies that AD trust is set up between the on-premises and Managed AD domain. We recommend that you create a trust between your on-premises domain and your Managed Microsoft AD domain. To learn more, see [ Setting up the trust](https://cloud.google.com/managed-microsoft-ad/docs/create-trust?hl=en#setting-up-trust) **Note:** The external trust type is not supported.  
Local security policy  |  Checks that the local security policy configuration `Network access: Named pipes that can be accessed anonymously` has been set. You need this check for creating an AD trust.  |  This check is expected to fail if the script is not run on an on-premises domain controller. This check requires you to run Powershell as Administrator to check local security policy settings. In case of failure, we recommend that you [ verify the local security policy for your on-premises domain](https://cloud.google.com/managed-microsoft-ad/docs/create-trust?hl=en#verifying-local-security-policy).   
Name suffix routing  |  Checks if name suffix routing to Managed AD domain is enabled on the on-premises domain controller. You need this check to route requests from an on-premises forest to Managed AD forest.  |  This check requires you to run Powershell as Administrator to check Name Suffix Routing settings. In case of failure, we recommend that you [ refresh name suffix routing for on-premises trust](https://cloud.google.com/managed-microsoft-ad/docs/manage-trusts#name-suffix-routing).   
Kerberos ticket for on-premises domain  |  Validates that Kerberos authentication is enabled on the on-premises domain. It looks for an existing Kerberos ticket for the on-premises domain. If not found, it attempts to generate a new ticket.  |  This check attempts to find an existing Kerberos ticket for the on-premises DC. If that fails, it tries to generate a new ticket as a form of validation. Errors in other checks can cause an error on this check. If you resolve failures for the other checks, it should resolve a failure for this check.   
Kerberos ticket for SQL Server  |  Validates that Kerberos authentication is enabled on the on-premises domain. It looks for an existing Kerberos ticket for each SQL Server Service Principal Name (SPN) that you provide. The SPN for SQL Server is `MSSQLSvc/{SQL Server FQDN}:1433`. If getting a ticket for the SPN fails, Cloud SQL checks if the Windows registry value for allowing IP in hostnames is set. If it is set, try to get a ticket with SPN `MSSQLSvc/{SQL Server IP}:1433`.  
To learn more, see the [ Microsoft documentation](https://learn.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip).  |  This check attempts to find an existing Kerberos ticket for SQL Server. If that fails, it tries to generate a new ticket as a form of validation. Errors in other checks can cause an error on this check. Resolving failures for the other checks should resolve a failure for this check.   
Cloud SQL connectivity  |  Tests network connectivity from the on-premises domain to the provided Cloud SQL instance IP addresses through TCP port `1433`.  |  This check validates that the network path to the database is open. If it fails, verify that your on-premises firewalls and Google Cloud VPC firewall rules allow outbound and inbound traffic, respectively, on TCP port `1433`.   
Kerberos Service (SRV) records  |  Queries the local DNS for `_kerberos._tcp` and `_kerberos._udp` SRV records and verifies that the target hosts correctly match the provided domain name.   
  
To learn more, see the [Microsoft documentation for SRV records](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created).  |  If this check fails, verify that your Active Directory domain's DNS SRV records exist and are configured correctly.   
  
## What's Next

  * To share your feedback, you can use [GitHub Issues](https://github.com/GoogleCloudPlatform/cloud-sql-active-directory-diagnosis-tool/issues).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
