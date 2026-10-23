---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-sql-server/
title: Connect Microsoft SQL Server \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:35.830179+00:00
---

# Connect Microsoft SQL Server  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-sql-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Connect Microsoft SQL Server Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to add accounts so you can use Microsoft SQL Server with Managed Service for Microsoft Active Directory. You can use the following procedure for a Compute Engine instance running SQL Server or a self-managed instance.

## Create local administrator account

To set up the SQL Server integration, create a local administrator account and temporarily grant it the `sysadmin` role. Learn [how to configure Windows Service Accounts and Permissions](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/configure-windows-service-accounts-and-permissions?view=sql-server-ver15).

By default, SQL Server grants the `sysadmin` role to all members of `Users`. Initially, the `Authenticated Users` group is the only member of `Users`. However, when a computer joins the domain, the `Domain Users` group is automatically added to the `Users` group on the computer.

To improve security, you should consider restricting the `sysadmin` role to a smaller set of users. Learn about [Roles in SQL Server](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/server-and-database-roles-in-sql-server).

## Joining the SQL Server instance to the domain

Next, join the instance that is running SQL Server to the Managed Microsoft AD domain. If the instance is already joined, you can skip to adding logins.

To join the instance to the domain, complete the following steps:

  1. Use the local administrator account to connect to the instance with Remote Desktop Protocol (RDP).
  2. [Join the instance to the domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/quickstart-domain-join-windows).
  3. Restart the instance.



Note that after you complete joining the instance to the domain, the local administrator account will no longer work for Windows Authentication to SQL unless you explicitly allow it.

## Adding logins

  1. Use the local administrator account to connect to the SQL Server instance using RDP.
  2. Open **Microsoft SQL Server Management Studio (SSMS)**.
  3. For **Authentication** , select **Windows Authentication** to log in with the built-in local administrator account.
  4. Select **Connect**.
  5. In **Object Explorer** , select **Security**.
  6. Right-click **Logins** , and then select **New Login** from the menu.
  7. For **Login name** , select **Windows authentication** , and then enter domain-name\username. username can be an Active Directory username, group name or built-in security principal.
  8. On the **Server Roles** page, select the server roles to grant to the Active Directory user.
  9. Select the **General** page, and then click **Ok**.



These new logins now work when you use Windows Authentication with SSMS.

## Adding RDP permissions

Add the new logins to the local `Remote Desktop Users` group to grant them permission to RDP into the SQL Server instance. Learn how to [allow log on through Remote Desktop Services](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/allow-log-on-through-remote-desktop-services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
