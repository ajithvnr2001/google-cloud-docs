---
url: https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials/
title: Manage accounts and credentials on Windows VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:21.184927+00:00
---

# Manage accounts and credentials on Windows VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage accounts and credentials on Windows VMs Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

By default, Windows virtual machine (VM) instances authenticate by using a username and a password instead of by using SSH. If you don't [enable SSH for Windows](https://docs.cloud.google.com/compute/docs/connect/windows-ssh), you must generate new credentials before connecting to the VM. This document describes how to generate credentials and manage accounts on Windows VMs.

You can also use this process to generate new credentials if you no longer have the original credentials. If you use this process to generate new credentials for existing users, any data that is encrypted with the current credentials, such as encrypted files or stored passwords, might not be retained.

**Caution:** If the VM is running an Active Directory domain controller, generating new credentials can cause the password of an existing domain user to be reset or a new domain user to be created. To prevent credential generation, [disable the account manager](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#disable_the_account_manager).

## Accounts disabled by default

The following accounts are built-in to Windows Server and are disabled by default:

  * `Administrator`
  * `Guest`
  * `DefaultAccount`
  * `WDAGUtilityAccount`



For these accounts, the Windows guest agent can reset the credentials. Resetting the credentials won't do the following:

  * Enable a disabled built-in account
  * Set additional policies so that the user can sign in to the VM



The built-in accounts are not guaranteed to have the default names because the local security policy, which is used by many organizations, can rename the accounts. If the accounts were renamed, you can use the original names.

**Caution:** For credential management features to work correctly, you must use English for key account and group names, such as `Administrator` and `Administrators`. The system relies on these specific English names to identify and manage credentials. Using non-English names for these accounts or groups can cause actions such as generating or resetting passwords to fail.

## Before you begin

  * [ Create a Windows Server VM. ](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances)
  * [ Ensure that the instance is online and ready. ](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp#instance_ready)
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




### Required roles

To get the permissions that you need to generate credentials for Windows Server VMs, ask your administrator to grant you the following IAM roles: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on the VM or project
  * If your VM uses a service account: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account or project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Generate credentials

Generate credentials for Windows Server VMs by using the Google Cloud console or the Google Cloud CLI.

**Note:** Before you can generate credentials for VMs that you imported to Compute Engine, you must [enable the COM4 port in the Windows Device Manager](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/using-device-manager).

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the Windows Server VM to change the password on.

  3. On the **VM instance details** page, in **Remote access** , click **Set Windows password**.

  4. In the **Username** field, enter the username to change the password for, or enter a new username to create a new user.

  5. Click **Set**.




###  gcloud 

  1. Run the following [`gcloud compute reset-windows-password` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reset-windows-password):
         
         gcloud compute reset-windows-password VM_NAME
         

Replace `VM_NAME` with the name of the VM to change the password for.

  2. Review the information in the confirmation prompt:
         
         This command creates an account and sets an initial password for the
         user [username] if the account does not already exist.
         If the account already exists, resetting the password can cause the
         LOSS OF ENCRYPTED DATA secured with the current password, including
         files and stored passwords.
         
         For more information, see:
         https://docs.cloud.google.com/compute/docs/instances/windows#reset
         
         Would you like to set or reset the password for [username] (Y/n)?
         

  3. After confirming the previous prompt, review the confirmation of new credentials, which appears as follows:
         
         Resetting and retrieving password for [username] on [instance-name]
         Updated [https://www.googleapis.com/compute/v1/projects/project-name/zones/zone/instances/instance-name].
         ip_address: ip-address
         password:   password
         username:   username
         

  4. You can now [connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) by using the new credentials.




## Change your password

After you [connect to your Windows Server VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows), you can use the Windows Command Prompt or the Windows user interface to change your password.

###  Command Prompt 

Use the [`net user`](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771865\(v=ws.11\)) command to change the password.

###  Windows Server 2016 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Control Panel**.

  3. Under the **User Accounts** icon, click either **Change Account Type** or **Add or remove user accounts**.

  4. Select the account that you want to modify.

  5. Click **Change the password**.

  6. Enter your current password and your new password.

  7. Click **Change password** to save your changes.




###  Windows Server 2019 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Settings**.

  3. Click **Accounts**.

  4. Click **Sign-in options**.

  5. Under **Password** , click **Change**.

  6. Enter your current password and click **Next**.

  7. Enter your new password in the **New password** field and enter it again in the **Re-enter password** field.

  8. Enter a **Password hint** , and click **Next**.

  9. Click **Finish**.




###  Windows Server 2022 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Settings**.

  3. Click **Accounts**.

  4. Click **Sign-in options**.

  5. Click **Password** and click **Change**.

  6. Enter your current password and click **Next**.

  7. Enter your new password in the **New password** field and enter it again in the **Confirm password** field.

  8. Enter a **Password hint** , and click **Next**.

  9. Click **Finish**.




## Create a local user account

### Command Prompt

Use the [`net user`](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771865\(v=ws.11\)) to create a new user.

Example: 
    
    
       net user USERNAME PASSWORD /add
       

Replace `USERNAME` with your username and `PASSWORD` with your password of choice.

###  Windows Server 2016 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Control Panel**.

  3. Under the **User Accounts** icon, click either **Change Account Type** or **Add or remove user accounts**.

  4. Click **Add a user account**.

  5. Set the username, password and password hint, then click **Next**.

  6. After an account is created click **Finish**.




###  Windows Server 2019 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Settings**.

  3. Click **Accounts**.

  4. Click **Other users** , then **Add someone else on this PC**.

  5. Skip all the Microsoft account related steps and click **Add a user without a Microsoft account**.

  6. Set the username, password and password hint, then click **Next**.




###  Windows Server 2022 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Settings**.

  3. Click **Accounts**.

  4. Click **Other users** , then **Add someone else on this PC**.

  5. Skip all the Microsoft account related steps and click **Add a user without a Microsoft account**.

  6. Set the username, password and password hint, then click **Next**.




## Grant local users Administrator privileges

Adding a local account to the Administrator group will give you administrative privileges on your Windows VM. See more information on [`Local Accounts`](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts).

**Caution:** For credential management features to work correctly, you must use English for key account and group names, such as `Administrator` and `Administrators`. The system relies on these specific English names to identify and manage credentials. Using non-English names for these accounts or groups can cause actions such as generating or resetting passwords to fail.

### Command Prompt

Use the [`net localgroup`](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc725622\(v=ws.11\)) to add a user to the Administrator group.

Example: 
    
    
       net localgroup administrators USERNAME /add
       

Replace `USERNAME` with the username of choice.

**Note:** Replace `/add` with `/delete` if you want to remove a user from the local administrator group.

###  Windows Server 2016 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Control Panel**.

  3. Under the **User Accounts** icon, click either **Change Account Type** or **Add or remove user accounts**.

  4. Select the account that you want to change.

  5. Click **Change the account type**.

  6. Select **Administrator** and confirm by clicking **Change Account Type**.




###  Windows Server 2019 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Settings**.

  3. Click **Accounts**.

  4. Click **Other users** then click the account that you want to change.

  5. Click **Change account type**.

  6. From the drop-down, select the **Administrator** account type and click **OK**.




###  Windows Server 2022 

  1. After the desktop finishes loading, click the **Start** menu icon.

  2. Click **Settings**.

  3. Click **Accounts**.

  4. Click **Other users** then click the account that you want to change.

  5. Click **Change account type**.

  6. From the drop-down, select the **Administrator** account type and click **OK**.




## What's next

  * [Troubleshoot Windows VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows)
  * [Connect to a Windows instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)
  * [Automate Windows password generation](https://docs.cloud.google.com/compute/docs/instances/windows/automate-pw-generation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
