---
url: https://docs.cloud.google.com/cloud-ftp/connect-to-internal-server/
title: Connect to an internal SFTP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:22.923815+00:00
---

# Connect to an internal SFTP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/connect-to-internal-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Guides ](https://docs.cloud.google.com/cloud-ftp/overview)



Send feedback 

#  Connect to an internal SFTP server Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to connect to an internal SFTP server in Cloud FTP. An SFTP server lets you securely transfer files to and from Cloud Storage. You can upload or download data in Cloud Storage buckets by using [standard SFTP commands](https://docs.cloud.google.com/cloud-ftp/sftp-commands) and SFTP clients.

Internal servers can be accessed only within your Virtual Private Cloud (VPC) network by using Private Service Connect. For background information, see [VPC overview](https://docs.cloud.google.com/vpc/docs/overview) and [Private Service Connect overview](https://docs.cloud.google.com/vpc/docs/private-service-connect).

## Before you begin

Complete the prerequisites in the following sections.

### Configure a VPC network

The steps in this document assume that you have a VPC network. For steps to create a VPC network, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

You can connect to the Private Service Connect endpoint's private IP address from a Compute Engine instance or service in the same network as the endpoint. You might need to configure the network to allow these connections. For example, if you connect to the endpoint by using a Compute Engine client VM, then add a firewall rule that allows ingress SSH connections to VM instances.

### Configure a Private Service Connect endpoint

Before you connect to an internal SFTP server for the first time, complete the following steps:

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

     * The URI of the service attachment for the server.
     * Your SFTP username.
     * (Optional) The key fingerprint of the server.
  3. Follow the steps to [create a Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint). Provide the following information:

     * **Target** : select **Published service**.
     * **Target service** : the URI of the service attachment. The service attachment URI is in the format `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`.
     * **Name** : a name for the endpoint. Use the same value as the `SERVICE_PROJECT` from the service attachment URI.
     * **Network** : the VPC network for the endpoint.
     * **Subnetwork** : the subnetwork for the endpoint.
     * **IP address** : create an IP address for the endpoint.
     * If you're creating the client VM in a different region from the service attachment, then select **Enable global access**.

Note the IP address of the endpoint.

  4. In the same network as the endpoint, configure a client such as a Compute Engine instance or service so that the instance or service can connect to the endpoint's private IP address.

For example, to use a Compute Engine instance as a client VM, do the following:

     1. Follow the steps to [create a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), if it doesn't already exist. Provide the following information:

        * **Region** : if you didn't enable global access when you created the endpoint, then select the same region as the SFTP server's service attachment.
        * **Network interface** : select the same VPC network and subnetwork as the endpoint.

Note the name and zone of the client VM.

     2. Transfer your private key to the client VM:
            
            gcloud compute scp ~/.ssh/KEY_PAIR_NAME CLIENT_VM_NAME:~/.ssh/KEY_PAIR_NAME \
            --zone=CLIENT_VM_ZONE --project=PROJECT_ID

Replace the following:

        * `CLIENT_VM_NAME`: the name of the client VM.
        * `CLIENT_VM_ZONE`: the zone of the client VM.
        * `PROJECT_ID`: the project ID or number of your Google Cloud project.



## Connect to an internal SFTP server

###  OpenSSH

  1. Connect to the client Compute Engine instance or service in the same VPC network as the Private Service Connect endpoint.

For example, if you're using a Compute Engine instance as a client VM, then connect to the client VM by using SSH:
         
         gcloud compute ssh CLIENT_VM_NAME --zone=CLIENT_VM_ZONE --project=PROJECT_ID

Replace the following:

     * `CLIENT_VM_NAME`: the name of the client VM
     * `CLIENT_VM_ZONE`: the zone of the client VM
     * `PROJECT_ID`: the project ID or number of your Google Cloud project
  2. Use OpenSSH to connect to the SFTP server:
         
         sftp -i ~/.ssh/KEY_PAIR_NAME USERNAME@IP_ADDRESS

Replace the following:

     * `KEY_PAIR_NAME`: the name of your SSH key pair, such as `sftp_user_key`
     * `USERNAME`: your SFTP username
     * `IP_ADDRESS`: the IP address of the Private Service Connect endpoint

If this is your first time connecting to the server, you might see a message like `The authenticity of host 'HOSTNAME (IP_ADDRESS)' can't be established`, and the key fingerprint of the server. To verify the server, enter the key fingerprint that your administrator gave you. Or, if you trust the server, type `yes` to add the server to your list of trusted servers.




When you're done transferring files, disconnect from the client VM by entering `exit`.

###  PuTTY 

**Note:** For detailed steps to install and use this client, see the relevant third-party documentation. 

  1. Connect to the client Compute Engine instance or service in the same VPC network as the Private Service Connect endpoint.

For example, if you're using a Compute Engine instance as a client VM, then connect to the client VM by using SSH:
         
         gcloud compute ssh CLIENT_VM_NAME --zone=CLIENT_VM_ZONE --project=PROJECT_ID

Replace the following:

     * `CLIENT_VM_NAME`: the name of the client VM
     * `CLIENT_VM_ZONE`: the zone of the client VM
     * `PROJECT_ID`: the project ID or number of your Google Cloud project
  2. Use PuTTY to connect to the SFTP server:
         
         psftp -i ~/.ssh/KEY_PAIR_NAME.ppk USERNAME@IP_ADDRESS

Replace the following:

     * `KEY_PAIR_NAME`: the name of your SSH key pair, such as `sftp_user_key`
     * `USERNAME`: your SFTP username
     * `IP_ADDRESS`: the IP address of the Private Service Connect endpoint

If this is your first time connecting to the server, you might see a message that the host key isn't cached. Verify the key fingerprint that your administrator gave you, and optionally add the key to the cache. Then, proceed with the connection.




## What's next

  * [Transfer data by using SFTP commands](https://docs.cloud.google.com/cloud-ftp/sftp-commands)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
