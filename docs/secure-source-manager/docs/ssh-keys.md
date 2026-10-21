---
url: https://docs.cloud.google.com/secure-source-manager/docs/ssh-keys/
title: Authenticate using SSH public keys \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:20.531977+00:00
---

# Authenticate using SSH public keys  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/ssh-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Authenticate using SSH public keys Stay organized with collections  Save and categorize content based on your preferences. 

Users and service accounts can use SSH public keys to authenticate to Secure Source Manager repositories. This page describes how to generate an SSH key pair, and then add it as an authentication method in the Secure Source Manager web interface.

Secure Source Manager supports RSA, ECDSA, and Ed25519 SSH key types.

## Required roles

To get the permissions that you need to authenticate using SSH public keys, ask your administrator to grant you the following IAM roles: 

  * To add an SSH key for a user: [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance 
  * To add an SSH key for a service account: 
    * [Secure Source Manager Instance Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceManager) (`roles/securesourcemanager.instanceManager`) on the Secure Source Manager instance
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to authenticate using SSH public keys. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to authenticate using SSH public keys:

  * `securesourcemanager.sshkeys.createAny` on the Secure Source Manager instance
  * To assign an SSH key to a service account: `iam.serviceAccounts.actAs` on the service account 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Generate a key pair

An SSH key pair consists of a private key that resides on your local system and a public key that you register with Google Cloud.

###  Linux or macOS 

  1. Install [OpenSSH](https://www.openssh.com/) on your local system.

  2. At a command prompt, enter the following command:
         
         ssh-keygen -t KEY_TYPE -C "USER_EMAIL"
         

Where:

     * USER_EMAIL is your email address.
     * KEY_TYPE is one of `rsa`, `ecdsa`, or `ed25519`.

For example:
    
    ssh-keygen -t rsa -C "user@example.com"
    

     1. When prompted, enter a location and filename for the public key file. To accept the default location and filename, press **Enter**.

     2. When prompted, leave the passphrase empty and press **Enter**.




###  Windows 

  1. If you don't have it, install the [OpenSSH client](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui) (included in Windows 10 and later) and [Git for Windows](https://git-scm.com/download/win) on your local system. The following instructions use OpenSSH and Git for Windows.

  2. In a PowerShell or Command Prompt, run the following command:
         
         ssh-keygen -t KEY_TYPE -C "USER_EMAIL"
         

Where:

     * USER_EMAIL is your email address.
     * KEY_TYPE is one of `rsa`, `ecdsa`, or `ed25519`.

For example:
    
    ssh-keygen -t rsa -C "user@example.com"
    

     1. When prompted, enter a location and filename for the public key file. To accept the default location and filename (`%USERPROFILE%.ssh`), press **Enter**.

     2. When prompted, leave the passphrase empty and press **Enter**.




## Add SSH key to SSH agent

To use the SSH key pair you generated, add your key to the SSH agent. If you didn't save your key in the default location, adding it to the SSH agent helps SSH locate your key.

###  Linux or macOS 

  1. Start `ssh-agent` in the background:
         
         eval "$(ssh-agent -s)"
         

The command returns the agent process ID (PID), for example:
         
         Agent pid 3245
         

Depending on your environment, you might need to use a different command, for example:

     * To use root access, run `sudo -s -H` before starting `ssh-agent`.
     * To run `ssh-agent` directly, use `exec ssh-agent bash` or `exec ssh-agent zsh`.
  2. Add your SSH private key to `ssh-agent`.
         
         ssh-add ~/.ssh/FILENAME
         

Where `FILENAME` is the name of your private key file, for example `id_rsa` or `id_ed25519`.




###  Windows 

  1. Start `ssh-agent`.

     * If you are using Git Bash, start `ssh-agent`:
           
           eval "$(ssh-agent -s)"
           

     * If you are using PowerShell or Command Prompt, start `ssh-agent` service. In PowerShell, run:
           
           Set-Service ssh-agent -StartupType Automatic; Start-Service ssh-agent
           

  2. Add your SSH private key to `ssh-agent`.

     * If you are using Git Bash:
           
           ssh-add ~/.ssh/FILENAME
           

     * If you are using PowerShell or Command Prompt:
           
           ssh-add $env:USERPROFILE\.ssh\FILENAME
           

Where `FILENAME` is the name of your private key file, for example `id_rsa` or `id_ed25519`.




## Add SSH keys for users

  1. In the Secure Source Manager web interface, from the instance or repository page, click the more_vert **more options** menu.
  2. Click **User SSH keys**.

The **User SSH keys** page opens, and a list of any existing keys you've created is displayed.

  3. In the **User SSH keys** page, click **Add key**.

  4. In the **Add SSH Key** page, enter the following values for your key:

     1. **Title** : add a descriptive title for the key.
     2. **SSH public key** : paste your public key string. To get your public key string, open the public key file (`FILENAME.pub`) in a text editor, or run one of the following commands:

###  Linux or macOS 
            
            cat ~/.ssh/FILENAME.pub
            

###  Windows 
            
            cat $env:USERPROFILE\.ssh\FILENAME.pub
            

Replace `FILENAME` with the name of your key file.




You can use SSH keys to authenticate to any Secure Source Manager repository provided you have the needed permissions on that repository.

## Add SSH keys for service accounts

To allow programmatic access to your repository, you can add an SSH key for a service account.

  1. If you don't already have a service account that you want to use, [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating).
  2. From the Secure Source Manager web interface, click the more_vert **more options** menu.
  3. Click **Service account SSH keys**. The **Service account SSH keys** page opens, and a list of any existing keys you've added is displayed.
  4. In the **Service account SSH keys** page, click **Add key**.
  5. In the **Add service account SSH key** page, enter the following values for your key:

     1. **Title** : a descriptive title for the key
     2. **Service account** : the service account email for the service account you want to use the SSH key in the format `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`

Where

        * `SA_NAME` is the service account name.
        * `PROJECT_ID` is the project ID of the project the service account was created in.
     3. **SSH Public Key** : Your public SSH key. See Generate a key pair for information on how to generate an SSH key pair.

  6. If the service account is not in the same project as your Secure Source Manager instance, give Secure Source Manager's [service agent](https://docs.cloud.google.com/iam/docs/service-agents) one of the following roles or permissions on the service account you want to use:

     * `iam.serviceAccounts.signJwt` permission
     * Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) role

Run the following command to add an IAM policy to your Secure Source Manager service account to grant it the Service Account Token Creator role.
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT \
        --member="serviceAccount:service-INSTANCE_PROJECT_NUMBER@gcp-sa-sourcemanager.iam.gserviceaccount.com" \
        --role="roles/iam.serviceAccountTokenCreator"
    

Where SERVICE_ACCOUNT is the service account you want to use and INSTANCE_PROJECT_NUMBER is the project number of your Secure Source Manager instance.

The SERVICE_ACCOUNT should be formatted either as a numeric service account ID or as an email, like this: 123456789876543212345 or my-iam-account@somedomain.com.




## What's next

  * [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build).
  * [Connect to Jenkins](https://docs.cloud.google.com/secure-source-manager/docs/connect-jenkins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
