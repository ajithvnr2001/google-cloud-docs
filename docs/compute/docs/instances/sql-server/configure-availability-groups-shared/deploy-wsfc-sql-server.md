---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/deploy-wsfc-sql-server/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:49.376582+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/deploy-wsfc-sql-server/




Stay organized with collections  Save and categorize content based on your preferences. 

## Deploying the failover cluster

You now use the VM instances to deploy a Windows Server Failover Cluster and SQL Server.

### Preparing SQL Server

Create a new user account in Active Directory for SQL Server:

  1. Connect to `node-1` [by using Remote Desktop](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows). Sign in with your domain user account.
  2. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.
  3. Confirm the elevation prompt by clicking **Yes**.
  4. Create a domain user account for SQL server and the SQL agent and assign a password.
         
         $Credential = Get-Credential -UserName sql_server -Message 'Enter password'
         New-ADUser `
           -Name "sql_server" `
           -Description "SQL Admin account." `
           -AccountPassword $Credential.Password `
           -Enabled $true -PasswordNeverExpires $true
         

**Note:** If you use Managed AD, append `-Path "OU=Cloud,DC=example,DC=org"` to the command to create the user in the `Cloud` OU. Ensure that the value of the path is the output of the following command: `Get-ADOrganizationalUnit -Filter "Name -eq 'Cloud'" | Select-Object -ExpandProperty DistinguishedName`



To configure SQL Server, perform the following steps on both `node-1` and `node-2`:

  1. Right-click the **Start** button (or press **Win+X**) and click **Windows PowerShell (Admin)**.

Rename the SQL server instance so that its name matches the hostname.
         
         $OLD_NAME = Invoke-Sqlcmd -Query "
           select @@SERVERNAME;
           GO" | ConvertTo-Csv | SELECT -Skip 2
         $OLD_NAME = $OLD_NAME.Replace('"', '')
         Invoke-Sqlcmd -Query "
           sp_dropserver '$OLD_NAME';
           GO
           sp_addserver '$env:computername', local;
           GO"
         Restart-Service -Name MSSQLSERVER
         

  2. Open **SQL Server Configuration Manager**.

  3. In the navigation pane, select **SQL Server Services**

  4. In the list of services, right-click **SQL Server (MSSQLSERVER)** and select **Properties**.

  5. Under **Log on as** , change the account.

     * **Account name** : `DOMAIN\sql_server` where `DOMAIN` is the NetBIOS name of your Active Directory domain.
     * **Password** : Enter the password you chose previously.
  6. Click **OK**.

  7. When prompted to restart SQL Server, select **Yes**.




SQL Server now runs under a domain user account.

**Warning:** Make sure you've completed the previous configuration steps on both VM instances, otherwise setting up the Always On availability group will fail.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
