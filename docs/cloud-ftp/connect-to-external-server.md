---
url: https://docs.cloud.google.com/cloud-ftp/connect-to-external-server/
title: Connect to an external SFTP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:17:50.420600+00:00
---

# Connect to an external SFTP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/connect-to-external-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Connect to an external SFTP server Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to connect to an external SFTP server in Cloud FTP. An SFTP server lets you securely transfer files to and from Cloud Storage. You can upload or download data in Cloud Storage buckets by using [standard SFTP commands](https://docs.cloud.google.com/cloud-ftp/sftp-commands) and SFTP clients like Cyberduck, FileZilla, or WinSCP.

## Before you begin

Before you connect to an external SFTP server for the first time, complete the following steps:

  1. Generate an SSH key pair that you will use to authenticate to the server.

#### Which key format do you need?

The key format that you need depends on which client you use to connect to the SFTP server. For more information, see [Supported SFTP clients](https://docs.cloud.google.com/cloud-ftp/third-party-clients).

### PEM format

     1. To create an OpenSSH key pair (PEM format), use the [`ssh-keygen` utility](https://man.openbsd.org/ssh-keygen).

On the client machine that will connect to the SFTP server, run the following command:
            
            ssh-keygen -t rsa -b 4096 -f ~/.ssh/KEY_PAIR_NAME

Replace `KEY_PAIR_NAME` with a name for the key pair, such as `sftp_user_key`.

     2. Extract the public key:
            
            cat ~/.ssh/KEY_PAIR_NAME.pub

### PPK format

     1. To create a PuTTY key pair (PPK format), use the [`PuTTYgen`](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) tool.

On the client machine that will connect to the SFTP server, run the following command:
            
            puttygen -t rsa -b 4096 -o KEY_PAIR_NAME.ppk

Replace `KEY_PAIR_NAME` with a name for the key pair, such as `sftp_user_key`.

     2. Extract the public key:
            
            puttygen -L KEY_PAIR_NAME.ppk

Provide the public key to your Cloud FTP administrator. Your administrator will create an SFTP user account for you, and add you to a server.

  2. Ask your Cloud FTP administrator to give you the following information, which you need to connect to the server:

     * The IP address or hostname of the server.
     * Your SFTP username.
     * (Optional) The key fingerprint of the server.



## Connect to an external SFTP server

###  Cyberduck 

**Note:** For detailed steps to install and use this client, see the relevant third-party documentation. 

  1. In Cyberduck, create a new connection with the following settings:

     * **Connection type** : SFTP (SSH File Transfer Protocol)
     * **Server** : the IP address of the SFTP server
     * **Port** : `22`
     * **User** : your SFTP username
     * Leave the **Password** field empty, because you use SSH keys for authentication.
     * Expand the **More options** section. For **SSH private key** , provide your SSH private key file.
  2. Connect to the SFTP server.

If this is your first time connecting to the server, you might see a message about an unknown fingerprint. Optionally, select the option to always trust this host. Then, proceed with the connection.




###  FileZilla 

**Note:** For detailed steps to install and use this client, see the relevant third-party documentation. 

  1. In FileZilla, create a new site with the following settings:

     * **Protocol** : SFTP - SSH File Transfer Protocol
     * **Host** : the IP address of the SFTP server
     * **Port** : `22`
     * **Logon type** : select **Key file**.
     * **User** : your SFTP username
     * **Key file** : provide your SSH private key file.
  2. Connect to the SFTP server.

If prompted, convert your key file to PPK format.

If this is your first time connecting to the server, you might see a message about an unknown host key. Optionally, select the option to always trust this host. Then, proceed with the connection.




###  OpenSSH 

  1. Use OpenSSH to connect to the SFTP server:
         
         sftp -i ~/.ssh/KEY_PAIR_NAME USERNAME@IP_ADDRESS

Replace the following:

     * `KEY_PAIR_NAME`: the name of your SSH key pair, such as `sftp_user_key`
     * `USERNAME`: your SFTP username
     * `IP_ADDRESS`: the IP address of the SFTP server

If this is your first time connecting to the server, you might see a message like `The authenticity of host 'HOSTNAME (IP_ADDRESS)' can't be established`, and the key fingerprint of the server. To verify the server, enter the key fingerprint that your administrator gave you. Or, if you trust the server, type `yes` to add the server to your list of trusted servers.




###  PuTTY 

**Note:** For detailed steps to install and use this client, see the relevant third-party documentation. 

  1. Use PuTTY to connect to the SFTP server:
         
         psftp -i ~/.ssh/KEY_PAIR_NAME.ppk USERNAME@IP_ADDRESS

Replace the following:

     * `KEY_PAIR_NAME`: the name of your SSH key pair, such as `sftp_user_key`
     * `USERNAME`: your SFTP username
     * `IP_ADDRESS`: the IP address of the SFTP server

If this is your first time connecting to the server, you might see a message that the host key isn't cached. Verify the key fingerprint that your administrator gave you, and optionally add the key to the cache. Then, proceed with the connection.




###  WinSCP 

**Note:** For detailed steps to install and use this client, see the relevant third-party documentation. 

  1. In WinSCP, create a new site with the following settings:

     * **File protocol** : SFTP
     * **Hostname** : the IP address of the SFTP server
     * **Port number** : `22`
     * **Username** : your SFTP username
     * Leave the **Password** field empty, because you use SSH keys for authentication.
     * Click **Advanced** , and then open the **SSH > Authentication** page. For **Private key file** , provide your SSH private key file.

       * If prompted, convert your key file to PPK format.
  2. Log in to the SFTP server.

If this is your first time connecting to the server, you might see a message about an unknown server and host key. Verify the key fingerprint that your administrator gave you, and optionally add the key to the cache. Then, proceed with the connection.




## What's next

  * [Transfer data by using SFTP commands](https://docs.cloud.google.com/cloud-ftp/sftp-commands)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
