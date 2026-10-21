---
url: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-synchronizing-user-accounts/
title: Active Directory user account provisioning \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:18:21.574909+00:00
---

# Active Directory user account provisioning  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-synchronizing-user-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Active Directory user account provisioning Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-26 UTC

This document shows you how to set up user and group provisioning between Active Directory and your Cloud Identity or Google Workspace account by using [Google Cloud Directory Sync (GCDS)](https://tools.google.com/dlpage/dirsync/).

To follow this guide, you must have an Active Directory user that is allowed to manage users and groups in Active Directory. Also, if you don't yet have a Cloud Identity or Google Workspace account, you'll need administrative access to your DNS zone in order to [verify domains](https://support.google.com/cloudidentity/answer/7331243). If you already have a Cloud Identity or Google Workspace account, make sure that your user has [super admin](https://support.google.com/cloudidentity/answer/2405986) privileges.

## Objectives

  * Install GCDS and connect it to Active Directory and Cloud Identity or Google Workspace.
  * Configure GCDS to provision users and, optionally, groups to Google Cloud.
  * Set up a scheduled task for continuous provisioning.



## Costs

If you're using the [free edition of Cloud Identity](https://support.google.com/cloudidentity/answer/7431902), following this guide won't use any billable Google Cloud components.

## Before you begin

  * Make sure you understand [how Active Directory identity management can be extended to Google Cloud](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).
  * Decide how you want to map identities, groups, and domains. Specifically, make sure that you've answered the following questions:

    * Which DNS domain do you plan to use as the primary domain for Cloud Identity or Google Workspace? Which additional DNS domains do you plan to use as secondary domains?
    * Do you need to use domain substitution?
    * Do you plan to use the email address (`mail`) or User Principal Name (`userPrincipalName`) as common identifiers for users?
    * Do you plan to provision groups, and if so, do you intend to use the common name (`cn`) or email address (`mail`) as common identifiers for groups?

For guidance on making these decisions, refer to the [overview document on extending Active Directory identity and access management to Google Cloud](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).

  * Before connecting your production Active Directory to Google Cloud, consider using an Active Directory test environment for setting up and testing user provisioning.

  * [Sign up for Cloud Identity](https://gsuite.google.com/signup/gcpidentity/welcome) if you don't have an account already, and [add additional DNS domains](https://support.google.com/a/answer/7502379) if necessary.

  * If you're using the [free edition of Cloud Identity](https://support.google.com/cloudidentity/answer/7431902) and intend to provision more than 50 users, [request an increase](https://support.google.com/cloudidentity/answer/7295541) of the total number of free Cloud Identity users through your support contact.

  * If you suspect that any of the domains you plan to use for Cloud Identity could have been used by employees to register consumer accounts, consider migrating these user accounts first. For more details, see [Assessing existing user accounts](https://docs.cloud.google.com/architecture/identity/assessing-existing-user-accounts).




## Plan the GCDS deployment

The following sections describe how to plan your GCDS deployment.

### Decide where to deploy GCDS

GCDS can provision users and groups from an LDAP directory to Cloud Identity or Google Workspace. Acting as a go-between for the LDAP server and Cloud Identity or Google Workspace, GCDS queries the LDAP directory to retrieve the necessary information from the directory and uses the [Directory API](https://developers.google.com/admin-sdk/directory/) to add, modify, or delete users in your Cloud Identity or Google Workspace account.

Because Active Directory Domain Services is based on LDAP, GCDS is well suited to implement user provisioning between Active Directory and Cloud Identity or Google Workspace.

When connecting an on-premises Active Directory infrastructure to Google Cloud, you can run GCDS either on-premises or on a Compute Engine virtual machine in Google Cloud. In most cases, it's best to run GCDS on-premises:

  * Because the information that Active Directory manages includes personally identifiable information and is usually considered sensitive, you might not want Active Directory to be accessed from outside the local network.
  * By default, Active Directory uses unencrypted LDAP. If you access Active Directory remotely from within Google Cloud, you should use encrypted communication. Although you can encrypt the connection by using LDAPS (LDAP+SSL) or [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn).
  * Communication from GCDS to Cloud Identity or Google Workspace is conducted through HTTPS and requires little or no change to your firewall configuration.



You can run GCDS on either Windows or Linux. Although it's possible to deploy GCDS on the domain controller, it's best to run GCDS on a separate machine. This machine must satisfy the [system requirements](https://support.google.com/a/answer/6123896) and have LDAP access to Active Directory. Although it's not a prerequisite for the machine to be domain joined or to run Windows, this guide assumes that Cloud Directory Sync runs on a domain-joined Windows machine.

To aid with setting up provisioning, GCDS includes a graphical user interface (GUI) called [Configuration Manager](https://support.google.com/a/answer/6126578). If the server on which you intend to run GCDS has a desktop experience, you can run Configuration Manager on the server itself. Otherwise, you must run Configuration Manager locally and then copy the resulting configuration file to the server, where you can use it to run GCDS. This guide assumes that you run Configuration Manager on a server with a GUI.

### Decide where to retrieve data

GCDS uses LDAP to interact with Active Directory and to retrieve information about users and groups. To make this interaction possible, GCDS requires you to provide a hostname and port in the configuration. In a small Active Directory environment that runs only a single global catalog (GC) server, providing a hostname and port is not a problem because you can point GCDS directly to the global catalog server.

In a more complex environment that runs redundant GC servers, pointing GCDS to a single server does not make use of the redundancy and is therefore not ideal. Although it's possible to set up a load balancer that distributes LDAP queries across multiple GC servers and keeps track of servers that might be temporarily unavailable, it's preferable to use the [DC Locator](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/enabling-clients-to-locate-the-next-closest-domain-controller) mechanism to locate servers dynamically.

By default, GCDS requires you to explicitly [specify the endpoint of an LDAP server](https://support.google.com/a/answer/6258071#ldap_connection) and does not support using the DC Locator mechanism. In this guide, you complement GCDS with a small PowerShell script that engages the DC Locator mechanism so that you don't have to statically configure endpoints of global catalog servers.

## Prepare your Cloud Identity or Google Workspace account

This section describes how to create a user for GCDS. To enable GCDS to interact with the [Directory API](https://developers.google.com/admin-sdk/directory) and [Domain Shared Contacts API](https://developers.google.com/admin-sdk/domain-shared-contacts/) of Cloud Identity and Google Workspace, the application needs a user account that has administrative privileges.

When signing up for Cloud Identity or Google Workspace, you already created one super admin user. Although you could use this user for GCDS, it's preferable to create a separate user that is exclusively used by Cloud Directory Sync:

  1. Open the [Admin console](https://admin.google.com) and sign in by using the super admin user that you created when signing up for Cloud Identity or Google Workspace.
  2. Create a user. For detailed instructions, see [Add an account for a new user](https://support.google.com/a/answer/33310) or [Add an account for multiple users (Beta)](https://support.google.com/a/answer/16499021).

  3. When you create the user account, provide an appropriate name and email address, such as the following:

     * **First Name** : `Google Cloud`
     * **Last Name** : `Directory Sync`
     * **Primary email** : `cloud-directory-sync`

Retain the primary domain in the email address, even if the domain does not correspond to the forest that you're provisioning from.

  4. Configure a password:

     * If the password option is available on the page, ensure that **Automatically generate a new password** isn't selected, and then enter a password. Make sure that **Ask for a password change at the next sign-in** isn't selected.
     * If the password option isn't available on the page, save the new user account, and then [reset the user's password](https://support.google.com/a/answer/33319).



To enable GCDS to create, list, and delete user accounts and groups, the user needs additional privileges. Additionally, it's a good idea to exempt the user from single sign-on—otherwise, you might not be able to re-authorize GCDS when experiencing single sign-on problems. Both can be accomplished by making the user a super admin:

  1. In the menu, go to **Directory > Users**.
  2. Locate the newly created user in the list and open it.
  3. Under **Admin roles and privileges** , click **Assign Roles**.
  4. Enable the **Super Admin** role.
  5. Click **Save**.

**Warning:** The super admin role grants the user full access to Cloud Identity, Google Workspace, and Google Cloud resources. To protect the user against credential theft and malicious use, we recommend that you enable [2-step verification](https://support.google.com/a/answer/175197) for the user. For more details on how to protect super admin users, see [Security best practices for administrator accounts](https://support.google.com/a/answer/9011373).

## Configure user provisioning

The following sections describe how to configure user provisioning.

### Create an Active Directory user for GCDS

To enable GCDS to retrieve information about users and groups from Active Directory, GCDS also requires a domain user with sufficient access. Rather than reusing an existing Windows user for this purpose, create a dedicated user for GCDS:

### Graphical Interface

  1. Open the **Active Directory Users and Computers** MMC snap-in from the Start menu.
  2. Navigate to the domain and organizational unit where you want to create the user. If there are multiple domains in your forest, create the user in the same domain as the GCDS machine.
  3. Right-click on the right window pane and choose **New** > **User**.
  4. Provide an appropriate name and email address, such as: 
     1. **First Name** : `Google Cloud`
     2. **Last Name** : `Directory Sync`
     3. **User logon name** : `gcds`
     4. **User logon name (pre-Windows 2000)** : `gcds`
  5. Click **Next**.
  6. Provide a password that satisfies your password policy.
  7. Clear **User must change password at next logon**.
  8. Select **Password never expires**.
  9. Click **Next** , and then click **Finish**.



### PowerShell

  1. Open a PowerShell console as Administrator.
  2. Create a user by running the following command:
         
         New-ADUser -Name "Google Cloud Directory Sync" `
             -GivenName "Google Cloud" `
             -Surname "Directory Sync" `
             -SamAccountName "gcds" `
             -UserPrincipalName (-Join("gcds@",(Get-ADDomain).DNSRoot)) `
             -AccountPassword(Read-Host -AsSecureString "Type password for User") `
             -Enabled $True
          

**Note:** You can use the "Path" argument to create a user under a specific organizational unit (OU). For example: `-Path "OU=dest,OU=root,DC=domain,DC=com"`.



You now have the prerequisites in place for installing GCDS.

### Install GCDS

On the machine on which you will run GCDS, download and run the [GCDS installer](https://tools.google.com/dlpage/dirsync). Rather than using a browser to perform the download, you can use the following PowerShell command to download the installer:
    
    
    (New-Object net.webclient).DownloadFile("https://dl.google.com/dirsync/dirsync-win64.exe", "$(pwd)\dirsync-win64.exe")
    

After the download has completed, you can launch the installation wizard by running the following command:
    
    
    .\dirsync-win64.exe

If you have already had GCDS installed, you can [update GCDS](https://support.google.com/a/answer/9346614) to ensure that you are using the [latest version](https://support.google.com/a/answer/1263028).

### Create a folder for the GCDS configuration

GCDS stores its configuration in an XML file. Because this configuration includes an OAuth refresh token that GCDS uses to authenticate with Google, make sure that you properly secure the folder used for configuration.

In addition, because GCDS doesn't require access to local resources other than this folder, you can configure GCDS to run as a limited user, [LocalService](https://docs.microsoft.com/en-us/windows/desktop/services/localservice-account):

  1. On the machine where you installed GCDS, log on as a local administrator.
  2. Open a PowerShell console that has administrative privileges.
  3. Run the following commands to create a folder that is named `$Env:ProgramData\gcds` to store the configuration, and to apply an access control list (ACL) so that only GCDS and administrators have access:
         
         $gcdsDataFolder = "$Env:ProgramData\gcds"
         New-Item -ItemType directory -Path  $gcdsDataFolder
         &icacls "$gcdsDataFolder" /inheritance:r
         &icacls "$gcdsDataFolder" /grant:r "CREATOR OWNER:(OI)(CI)F" /T
         &icacls "$gcdsDataFolder" /grant   "BUILTIN\Administrators:(OI)(CI)F" /T
         &icacls "$gcdsDataFolder" /grant   "Domain Admins:(OI)(CI)F" /T
         &icacls "$gcdsDataFolder" /grant   "LOCAL SERVICE:(OI)(CI)F" /T
         

  4. To determine the location of the ProgramData folder, run the command `Write-Host $Env:ProgramData`. On English versions of Windows, this path will usually be `c:\ProgramData`. You need this path later.




### Connect to Google

You will now use Configuration Manager to prepare the GCDS configuration. These steps assume that you run Configuration Manager on the same server where you plan to run GCDS.

If you use a different machine to run Configuration Manager, make sure to copy the configuration file to the GCDS server afterward. Also, be aware that testing the configuration on a different machine might not be possible.

  1. Launch Configuration Manager. You can find Configuration Manager in the Windows Start menu under **Google Cloud Directory Sync** > **Configuration Manager**.
  2. Click **Google Domain Configuration > Connection Settings**.

![Google Domain Configuration > Connection Settings](https://docs.cloud.google.com/static/solutions/images/federating-gcp-with-ad-gcds-config-settings-v4.7.6.png)

  3. [Authorize GCDS and configure domain settings](https://support.google.com/a/answer/6162412#googleapps).

  4. In the menu, click **File > Save as**.

  5. In the file dialog, enter `PROGRAM_DATA\gcds\config.xml` as the filename. Replace `PROGRAM_DATA` with the path to the `ProgramData` folder that the PowerShell command returned when you ran it earlier.

  6. Click **Save** , and then click **OK**.




### Connect to Active Directory

The next step is to configure GCDS to connect to Active Directory:

  1. In Configuration Manager, click **LDAP Configuration > Connection Settings**.
  2. Configure the [LDAP connection settings](https://support.google.com/a/answer/6258071#ldap_connection): 
     1. **Server Type** : Select **MS Active Directory**.
     2. **Connection Type** : Select either **Standard LDAP** or **LDAP+SSL**.
     3. **Host Name** : Enter the name of a GC server. This setting is used only for testing. Later, you will automate the discovery of the GC server.
     4. **Port** : **3268** (GC) or **3269** (GC over SSL). Using a GC server instead of a domain controller helps ensure that you can provision users from all domains of your Active Directory forest. Also, [ensure authentication after Microsoft ADV190023 update](https://support.google.com/a/answer/9747365).
     5. **Authentication Type** : **Simple**.
     6. **Authorized User** : Enter the User Principal Name (UPN) of the domain user that you created earlier: `gcds@UPN_SUFFIX_DOMAIN`. Replace `UPN_SUFFIX_DOMAIN` with the appropriate UPN suffix domain for the user. Alternatively, you can also specify the user by using the `NETBIOS_DOMAIN_NAME\gcds` syntax.
     7. **Base DN** : Leave this field empty to ensure that searches are performed across all domains in the forest.
  3. To verify the settings, click **Test connection**. If the connection fails, double-check that you've specified the hostname of a GC server and that the username and password are correct.
  4. Click **Close**.



### Decide what to provision

Now that you've successfully connected GCDS, you can decide which items to provision:

  1. In Configuration Manager, click **General Settings**.
  2. Ensure that **User Accounts** is selected.
  3. If you intend to provision groups, ensure that **Groups** is selected; otherwise, clear the checkbox.
  4. Synchronizing organizational units is beyond the scope of this guide, so leave **Organizational Units** unselected.
  5. Leave **User Profiles** and **Custom Schemas** unselected.



For more details, see [Decide what to provision](https://support.google.com/a/answer/6162412).

### Provision users

To provision users, you configure how to map users between Active Directory:

  1. In Configuration Manager, click **User Accounts** > **Additional User Attributes**.
  2. Click **Use defaults** to automatically populate the attributes for **Given Name** and **Family Name** with `givenName` and `sn`, respectively.



The remaining settings depend on whether you intend to use the UPN or email address to map Active Directory to users in Cloud Identity or Google Workspace, and whether you need to apply domain name substitutions. If you're unsure which option is best for you, see the article on [how Active Directory identity management can be extended to Google Cloud](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction).

### UPN

  1. In Configuration Manager, click **User Accounts > User Attributes**.
  2. Click **Use defaults**.
  3. Change **Email Address Attribute** to `userPrincipalName`.
  4. Click `proxyAddresses` > `Remove` if you don't want to sync alias addresses.
  5. Click the **Search Rules** tab, and then click **Add Search Rule**.
  6. Enter the following settings:

     1. **Scope** : **Sub-tree**
     2. **Rule** :
            
            (&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(!(userPrincipalName=gcds@*)))

This rule matches all non-disabled users but ignores computer and managed service accounts, as well as the `gcds` user account.

     3. **Base DN** : Leave blank to search all domains in the forest.

  7. Click **OK** to create the rule.




### UPN: domain substitution

  1. In Configuration Manager, click the **User Accounts** > **User Attributes** tab.
  2. Click **Use defaults**.
  3. Change **Email Address Attribute** to `userPrincipalName`
  4. Click `proxyAddresses` > `Remove` if you don't want to sync alias addresses.
  5. Click the **Search Rules** tab, and then click **Add Search Rule**.
  6. Enter the following settings:

     1. **Scope** : **Sub-tree**
     2. **Rule** :
            
            (&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2))(!(userPrincipalName=gcds@*)))

This rule matches all non-disabled users but ignores computer and managed service accounts, as well as the `gcds` user account.

     3. **Base DN** : Leave blank to search all domains within the forest.

  7. Click **OK** to create the rule.

  8. Click **Google Domain Configuration > Connection Settings**, and choose **Replace domain names in LDAP email addresses with this domain name**.




### Email

  1. In Configuration Manager, click **User Accounts** > **User Attributes**.
  2. Click **Use defaults**.
  3. Click the **Search Rules** tab, and then click **Add Search Rule**.
  4. Enter the following settings:

     1. **Scope** : **Sub-tree**
     2. **Rule** :
            
            (&(objectCategory=person)(objectClass=user)(mail=*)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))

This rule matches all non-disabled users with a non-empty email address but ignores computer and managed service accounts.

     3. **Base DN** : Leave blank to search all domains in the forest.

  5. Click **OK** to create the rule.




### Email: domain substitution

  1. In Configuration Manager, click **User Accounts** > **User Attributes**.
  2. Click **Use defaults**.
  3. Click `proxyAddresses` > `Remove` if you don't want to sync alias addresses.
  4. Click the **Search Rules** tab, and then click **Use defaults**.
  5. Click **Google Domain Configuration** > **Connection Settings** , and choose **Replace domain names in LDAP email addresses with this domain name**.



For further details on mapping user attributes, see [Set up your sync with Configuration Manager](https://support.google.com/a/answer/6162412#useraccounts).

#### Deletion policy

So far, the configuration has focused on adding and updating users in Cloud Identity or Google Workspace. However, it's also important that users that are disabled or deleted in Active Directory be suspended or deleted in Cloud Identity or Google Workspace.

As part of the provisioning process, GCDS generates a list of users in Cloud Identity or Google Workspace that don't have corresponding matches in the Active Directory LDAP query results. Because the LDAP query incorporates the clause `(!(userAccountControl:1.2.840.113556.1.4.803:=2))`, any users that have been disabled or deleted in Active Directory since the last provisioning was performed will be included in this list. The default behavior of GCDS is to delete these users in Cloud Identity or Google Workspace, but you can customize this behavior:

  1. In Configuration Manager, click **User Accounts > User Attributes**.
  2. Under **Google Domain Users Deletion/Suspension Policy** , ensure that **Don't suspend or delete Google domain admins not found in LDAP** is checked. This setting ensures that GCDS won't suspend or delete the super admin user that you used to configure your Cloud Identity or Google Workspace account.
  3. Optionally, change the deletion policy for non-administrator users.



If you use multiple separate instances of GCDS to provision different domains or forests to a single Cloud Identity or Google Workspace account, make sure that the different GCDS instances don't interfere with one another. By default, users in Cloud Identity or Google Workspace that have been provisioned from a different source will wrongly be identified in Active Directory as having been deleted. To avoid this situation, you can move all users that are beyond the scope of the domain or forest that you're provisioning from to a single OU and then exclude that OU.

  1. In Configuration Manager, click **Google Domain Configuration** > **Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **Organization Complete Path**
     2. **Match Type** : **Exact Match**
     3. **Exclusion Rule** : Enter the OU path and its name. For example:
            
            ROOT OU/EXCLUDED OU

Replace `ROOT OU/EXCLUDED OU` with your OU path and the excluded OU's name.

  4. Click **OK** to create the rule.




Alternatively, if excluding a single OU doesn't fit your business, you can exclude domain or forest base on users' email addresses.

### UPN

  1. In Configuration Manager, click **Google Domain Configuration > Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **User Email Address**
     2. **Match Type** : **Regular Expression**
     3. **Exclusion Rule** : If you use a single UPN suffix domain, enter the following regular expression:
            
            .*@((?!UPN_SUFFIX_DOMAIN).*)$

Replace `UPN_SUFFIX_DOMAIN` with your UPN suffix domain, as in this example: 
            
            .*@((?!corp.example.com).*)$

If you use more than one UPN suffix domain, extend the expression as shown:
            
            .*@((?!corp.example.com|branch.example.com).*)$

  4. Click **OK** to create the rule.




### UPN: domain substitution

  1. In Configuration Manager, click **Google Domain Configuration** > **Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **User Email Address**
     2. **Match Type** : **Regular Expression**
     3. **Exclusion Rule** : If you use a single UPN suffix domain, enter the following regular expression:
            
            .*@((?!SUBSTITUTION_DOMAIN).*)$

Replace `SUBSTITUTION_DOMAIN` with the domain that you use to replace the UPN suffix domain, as in this example:
            
            .*@((?!corp.example.com).*)$

  4. Click **OK** to create the rule.




### Email

  1. In Configuration Manager, click **Google Domain Configuration** > **Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **User Email Address**
     2. **Match Type** : **Regular Expression**
     3. **Exclusion Rule** : If you use a single UPN suffix domain, enter the following regular expression:
            
            .*@((?!MX_DOMAIN).*)$

Replace `MX_DOMAIN` with the domain name that you use in email addresses, as in this example:
            
            .*@((?!corp.example.com).*)$

If you use more than one UPN suffix domain, extend the expression as shown:
            
            .*@((?!corp.example.com|branch.example.com).*)$

  4. Click **OK** to create the rule.




### Email: domain substitution

  1. In Configuration Manager, click **Google Domain Configuration > Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **User Email Address**
     2. **Match Type** : **Regular Expression**
     3. **Exclusion Rule** : If you use a single UPN suffix domain, enter the following regular expression:
            
            .*@((?!SUBSTITUTION_DOMAIN).*)$

Replace `SUBSTITUTION_DOMAIN` with the domain that you use to replace the email domain, as in this example:
            
            .*@((?!corp.example.com).*)$

  4. Click **OK** to create the rule.




For further details on deletion and suspension settings, see [Learn more about Configuration Manager options](https://support.google.com/a/answer/6258071#user).

### Provision groups

The next step is to configure how to map groups between Active Directory and Cloud Identity or Google Workspace. This process differs based on whether you plan to map groups by [common name or by email address](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-introduction#mapping_groups).

#### Configure group mappings by common name

First, you need to identify the types of security groups that you intend to provision, and then formulate an appropriate LDAP query. The following table contains common queries that you can use.

Type | LDAP query  
---|---  
Domain local groups | `(&(objectCategory=group)(groupType:1.2.840.113556.1.4.803:=2147483652))`  
Global groups | `(&(objectCategory=group)(groupType:1.2.840.113556.1.4.803:=2147483650))`  
Universal groups | `(&(objectCategory=group)(groupType:1.2.840.113556.1.4.803:=2147483656))`  
Global and universal groups | `(&(objectCategory=group)(|(groupType:1.2.840.113556.1.4.803:=2147483650)(groupType:1.2.840.113556.1.4.803:=2147483656)))`  
All groups | `(objectCategory=group)`  
  
The query for global groups also covers Active Directory–defined groups such as domain controllers. You can filter these groups by restricting the search by organizational unit (`ou`).

The remaining settings depend on whether you intend to use UPN or email address to map Active Directory to users in Cloud Identity or Google Workspace.

### UPN

  1. In Configuration Manager, click **Groups** > **Search Rules**.
  2. Click **Use Defaults** to add two default rules.
  3. Click the first rule edit icon.
  4. Edit **Rule** to replace the LDAP query.
  5. In the **Groups** box, enter the following settings: 
     1. **Group Email Address Attribute** : `cn`
     2. **User Email Address Attribute** : `userPrincipalName`
  6. Click the **Prefix-Suffix** tab.
  7. In the **Group Email Address** box, enter the following settings:

     1. **Suffix** : `@PRIMARY_DOMAIN`, where you replace `@PRIMARY_DOMAIN` with the primary domain of your Cloud Identity or Google Workspace account. Although the setting seems redundant because GCDS appends the domain automatically, you must specify the setting explicitly to prevent multiple GCDS instances from erasing group members that they had not added.

**Example:** `@example.com`

     2. Click **OK**.

  8. Click the second rule cross icon to delete that rule.




### Email

  1. In Configuration Manager, click **Groups** > **Search Rules**.
  2. Click **Use Defaults** to add a couple of default rules.
  3. Click the first rule edit icon.
  4. Edit **Rule** to replace the LDAP query.
  5. In the **Groups** box, edit **Group Email Address Attribute** to enter the setting `cn`.
  6. Click **OK**.



The same settings also apply if you used domain substitution when mapping users.

#### Configure group mappings by email address

First, you need to identify the types of security groups that you intend to provision, and then formulate an appropriate LDAP query. The following table contains common queries that you can use.

Type | LDAP query  
---|---  
Domain local groups with email address | `(&(objectCategory=group)(groupType:1.2.840.113556.1.4.803:=2147483652)(mail=*))`  
Global groups with email address | `(&(objectCategory=group)(groupType:1.2.840.113556.1.4.803:=2147483650)(mail=*))`  
Universal groups with email address | `(&(objectCategory=group)(groupType:1.2.840.113556.1.4.803:=2147483656)(mail=*))`  
Global and universal groups with email address | `(&(objectCategory=group)(|(groupType:1.2.840.113556.1.4.803:=2147483650)(groupType:1.2.840.113556.1.4.803:=2147483656))(mail=*))`  
All groups with email address | `(&(objectCategory=group)(mail=*))`  
  
The remaining settings depend on whether you intend to use UPN or email address to map Active Directory to users in Cloud Identity or Google Workspace.

### UPN

  1. In Configuration Manager, click **Groups** > **Search Rules**.
  2. Click **Use Defaults** to add two default rules.
  3. Click the first rule edit icon.
  4. Edit **Rule** to replace the LDAP query.
  5. In the **Groups** box, edit **User Email Name Attribute** to enter the setting `userPrincipalName`.
  6. Click **OK**.
  7. Click the second rule cross icon to delete that rule.



### Email

  1. In Configuration Manager, click **Groups** > **Search Rules**.
  2. Click **Use Defaults** to add a couple of default rules.
  3. Click the first rule edit icon.
  4. Edit **Rule** to replace the LDAP query.
  5. Click **OK**.
  6. Click the second rule cross icon to remove this rule.



If you have enabled **Replace domain names in LDAP email addresses with this domain name** , it also applies to email addresses of groups and members.

#### Deletion policy

GCDS handles the deletion of groups similarly to the deletion of users. If you use multiple separate instances of GCDS to provision different domains or forests to a single Cloud Identity or Google Workspace account, make sure that the different GCDS instances don't interfere with one another.

By default, a group member in Cloud Identity or Google Workspace that has been provisioned from a different source will wrongly be identified in Active Directory as having been deleted. To avoid this situation, configure GCDS to ignore all group members that are beyond the scope of the domain or forest that you're provisioning from.

### UPN

  1. Click **Google Domain Configuration > Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **Group Member Email Address**
     2. **Match Type** : **Regular Expression**
     3. **Exclusion Rule** : If you use a single UPN suffix domain, enter the following regular expression:
            
            .*@((?!UPN_SUFFIX_DOMAIN).*)$

Replace `UPN_SUFFIX_DOMAIN` with your UPN suffix domain, as in the following example:
            
            .*@((?!corp.example.com).*)$

If you use more than one UPN suffix domain, extend the expression as shown:
            
            .*@((?!corp.example.com|branch.example.com).*)$

  4. Click **OK** to create the rule.




### UPN: domain substitution

  1. Click **Google Domain Configuration > Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **Group Member Email Address**
     2. **Match Type** : **Regular Expression**
     3. **Exclusion Rule** : If you use a single UPN suffix domain, enter the following regular expression:
            
            .*@((?!SUBSTITUTION_DOMAIN).*)$

Replace `SUBSTITUTION_DOMAIN` with the domain that you use to replace the UPN suffix domain, as in this example:
            
            .*@((?!corp.example.com).*)$

  4. Click **OK** to create the rule.




### Email

  1. Click **Google Domain Configuration > Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **Group Member Email Address**
     2. **Match Type** : **Regular Expression**
     3. **Exclusion Rule** : If you use a single UPN suffix domain, enter the following regular expression:
            
            .*@((?!MX_DOMAIN).*)$

Replace `MX_DOMAIN` with the domain name that you use in email addresses, as in the following example:
            
            .*@((?!corp.example.com).*)$

If you use more than one UPN suffix domain, extend the expression as shown:
            
            .*@((?!corp.example.com|branch.example.com).*)$

  4. Click **OK** to create the rule.




### Email: domain substitution

  1. Click **Google Domain Configuration > Exclusion Rules**.
  2. Click **Add Exclusion Rule**.
  3. Configure the following settings:

     1. **Type** : **Group Member Email Address**
     2. **Match Type** : **Regular Expression**
     3. **Exclusion Rule** : If you use a single UPN suffix domain, enter the following regular expression:
            
            .*@((?!SUBSTITUTION_DOMAIN).*)$

Replace `SUBSTITUTION_DOMAIN` with the domain that you use to replace the email domain, as in the following example:
            
            .*@((?!corp.example.com).*)$

     4. Click **OK** to create the rule.




For more information about group settings, see [Learn more about Configuration Manager options](https://support.google.com/a/answer/6258071#group_search).

### Configure logging and notifications

Keeping users in sync requires that you run GCDS on a scheduled basis. To allow you to keep track of GCDS activity and potential problems, you can control how and when GCDS writes its log file:

  1. In Configuration Manager, click **Logging**.
  2. Set **File name** to `PROGRAM_DATA\gcds\gcds_sync.#{timestamp}.log`. Replace `PROGRAM_DATA` with the path to the `ProgramData` folder that the PowerShell command returned when you ran it earlier.
  3. Click **File > Save** to commit the configuration changes to disk, then click **OK**.

**Note:** You can click **File** > **Save** or **Save as** to commit the configuration changes to disk when you complete each of the preceding steps. If the configuration is ready to be tested, you can click **Go to the simulation tab**. Otherwise, you can click **Skip simulation**.



In addition to [logging](https://support.google.com/a/answer/6258071#logging), GCDS can send [notifications](https://support.google.com/a/answer/6258071#notification) by email. To activate this service, click **Notifications** and provide connection information for your mail server.

### Simulate user provisioning

You've completed the GCDS configuration. To verify that the configuration works as intended, you need to at first save the configuration to disk then simulate a user provisioning run. During simulation, GCDS won't perform any changes to your Cloud Identity or Google Workspace account, but will instead report which changes _it would perform_ during a regular provision run.

  1. In Configuration Manager, click **Sync**.
  2. At the bottom of the screen, select **Clear cache** , and then click **Simulate sync**.
  3. After the process completes, review the **Proposed changes** section of the log that is shown in the lower half of the dialog and verify that there are no unwanted changes such as deleting or suspending any users or groups.



### Initial user provisioning

You can now trigger the initial user provisioning:

**Warnings**

  * Triggering user provisioning will make permanent changes to users and groups in your Cloud Identity or Google Workspace account.
  * If you have a large number of users to provision, consider temporarily changing the LDAP query to match a subset of these users only. Using this subset of users, you can then test the process and adjust settings if necessary. After you've successfully validated results, change back the LDAP query and provision the remaining users.
  * Avoid repeatedly modifying or deleting a large number of users when testing because such actions might be flagged as abusive behavior.



Trigger a provision run as follows:

  1. In Configuration Manager, click **Sync**.
  2. At the bottom of the screen, select **Clear cache** , and then click **Sync & apply changes**.

A dialog appears showing the status.

  3. After the process completes, check the log that is shown in the lower half of the dialog:

     1. Under **Successful user changes** , verify that at least one user has been created.
     2. Under **Failures** , verify that no failures occurred.



## Schedule provisioning

To ensure that changes performed in Active Directory are propagated to your Cloud Identity or Google Workspace account, set up a scheduled task that triggers a provisioning run every hour:

  1. Open a PowerShell console as Administrator.
  2. Check if the [Active Directory PowerShell module](https://docs.microsoft.com/en-us/powershell/module/activedirectory/) is available on the system:
         
         import-module ActiveDirectory

If the command fails, download and install the [Remote Server Administration Tools](https://www.microsoft.com/en-us/download/details.aspx?id=45520) and try again.

  3. In Notepad, create a file, copy the following content into it, and save the file to `%ProgramData%\gcds\sync.ps1`. When you're done, close the file.
         
         [CmdletBinding()]
         Param(
             [Parameter(Mandatory=$True)]
             [string]$config,
         
             [Parameter(Mandatory=$True)]
             [string]$gcdsInstallationDir
         )
         
         import-module ActiveDirectory
         
         # Stop on error.
         $ErrorActionPreference ="stop"
         
         # Ensure it's an absolute path.
         $rawConfigPath = [System.IO.Path]::Combine((pwd).Path, $config)
         
         # Discover closest GC in current domain.
         $dc = Get-ADDomainController -discover -Service "GlobalCatalog" -NextClosestSite
         Write-Host ("Using GC server {0} of domain {1} as LDAP source" -f [string]$dc.HostName, $dc.Domain)
         
         # Load XML and replace the endpoint.
         $dom = [xml](Get-Content $rawConfigPath)
         $ldapConfigNode = $dom.SelectSingleNode("//plugin[@class='com.google.usersyncapp.plugin.ldap.LDAPPlugin']/config")
         
         # Tweak the endpoint.
         $ldapConfigNode.hostname = [string]$dc.HostName
         $ldapConfigNode.ldapCredMachineName = [string]$dc.HostName
         $ldapConfigNode.port = "3268"   # Always use GC port
         
         # Tweak the tsv files location
         $googleConfigNode = $dom.SelectSingleNode("//plugin[@class='com.google.usersyncapp.plugin.google.GooglePlugin']/config")
         $googleConfigNode.nonAddressPrimaryKeyMapFile = [System.IO.Path]::Combine((pwd).Path, "nonAddressPrimaryKeyFile.tsv")
         $googleConfigNode.passwordTimestampFile = [System.IO.Path]::Combine((pwd).Path, "passwordTimestampCache.tsv")
         
         # Save resulting config.
         $targetConfigPath = $rawConfigPath + ".autodiscover"
         
         $writer = New-Object System.IO.StreamWriter($targetConfigPath, $False, (New-Object System.Text.UTF8Encoding($False)))
         $dom.Save($writer)
         $writer.Close()
         
         # Start provisioning.
         Start-Process -FilePath "$gcdsInstallationDir\sync-cmd" `
             -Wait -ArgumentList "--apply --config ""$targetConfigPath"""
         

  4. Configuration Manager created a secret key to encrypt the credentials in the config file. To ensure that GCDS can still read the configuration when it's run as a scheduled task, run the following commands to copy that secret key from your own profile to the profile of `NT AUTHORITY\LOCAL SERVICE`:
         
         New-Item -Path Registry::HKEY_USERS\S-1-5-19\SOFTWARE\JavaSoft\Prefs\com\google\usersyncapp -Force;
         Copy-Item -Path Microsoft.PowerShell.Core\Registry::HKEY_CURRENT_USER\SOFTWARE\JavaSoft\Prefs\com\google\usersyncapp\util `
             -Destination Microsoft.PowerShell.Core\Registry::HKEY_USERS\S-1-5-19\SOFTWARE\JavaSoft\Prefs\com\google\usersyncapp\util
         

If the commands fail, ensure that you started the PowerShell console as Administrator.

  5. Create a scheduled task by running the following commands. The scheduled task will be triggered every hour and invokes the `sync.ps1` script as `NT AUTHORITY\LOCAL SERVICE`.

**Warning:** After it starts, the scheduled task will make permanent changes to your Cloud Identity or Google Workspace account.
         
         $taskName = "Synchronize to Cloud Identity"
         $gcdsDir = "$Env:ProgramData\gcds"
         
         $action = New-ScheduledTaskAction -Execute 'PowerShell.exe' `
           -Argument "-ExecutionPolicy Bypass -NoProfile $gcdsDir\sync.ps1 -config $gcdsDir\config.xml -gcdsInstallationDir '$Env:Programfiles\Google Cloud Directory Sync'" `
           -WorkingDirectory $gcdsDir
         $trigger = New-ScheduledTaskTrigger `
           -Once `
           -At (Get-Date) `
           -RepetitionInterval (New-TimeSpan -Minutes 60) `
           -RepetitionDuration (New-TimeSpan -Days (365 * 20))
         
         $principal = New-ScheduledTaskPrincipal -UserID "NT AUTHORITY\LOCAL SERVICE" -LogonType ServiceAccount
         Register-ScheduledTask -Action $action -Trigger $trigger -Principal $principal -TaskName $taskName
         
         $task = Get-ScheduledTask -TaskName "$taskName"
         $task.Settings.ExecutionTimeLimit = "PT12H"
         Set-ScheduledTask $task
         




For more information, see [Schedule automatic synchronizations](https://support.google.com/a/answer/6152426).

## Test user provisioning

You've completed the installation and configuration of GCDS, and the scheduled task will trigger a provision run every hour.

To trigger a provisioning run manually, switch to the PowerShell console and run the following command:
    
    
    Start-ScheduledTask "Synchronize to Cloud Identity"
    

## Clean up

To remove GCDS, perform the following steps:

  1. Open Windows Control Panel and click **Programs > Uninstall a program**.
  2. Select **Google Cloud Directory Sync** , and click **Uninstall/Change** to launch the uninstall wizard. Then follow the instructions in the wizard.
  3. Open a PowerShell console and run the following command to remove the scheduled task:
         
         $taskName = "Synchronize to Cloud Identity"
         Unregister-ScheduledTask -TaskName $taskName -Confirm:$False
         

  4. Run the following command to delete the configuration and log files:
         
         Remove-Item -Recurse -Force "$Env:ProgramData\gcds"
         Remove-Item -Recurse -Path Registry::HKEY_USERS\S-1-5-19\SOFTWARE\JavaSoft\Prefs\com\google\usersyncapp
         




## What's next

  * [Configure single sign-on between Active Directory and Google Cloud](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-active-directory-configuring-single-sign-on).
  * Review [GCDS best practices](https://support.google.com/a/answer/7177267) and [FAQ](https://support.google.com/a/answer/7177266).
  * Find out how to [troubleshoot common GCDS issues](https://support.google.com/a/answer/3075991).
  * Read about [best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and [best practices for federating Google Cloud with an external identity provider](https://docs.cloud.google.com/architecture/identity/best-practices-for-federating).
  * Acquaint yourself with [best practices for managing super admin users](https://docs.cloud.google.com/resource-manager/docs/super-admin-best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-26 UTC."],[],[]] 
