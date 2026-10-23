---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-hytrust-kms/
title: Configuring vSAN encryption using HyTrust KeyControl \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:03.418261+00:00
---

# Configuring vSAN encryption using HyTrust KeyControl  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-hytrust-kms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configuring vSAN encryption using HyTrust KeyControl

One option to encrypt data at rest using [vSAN encryption](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption) is to use HyTrust KeyControl as an external key management service (KMS). To deploy HyTrust KeyControl in Google Cloud, use the steps in this document.

## Prerequisites

  * One of the following vSphere versions supported by HyTrust KeyControl: 
    * vSphere 6.5, 6.6, 6.7, or 7.0
    * vSphere Trust Authority 7.0
    * Universal key management for KMIP-compatible encryption agents
  * **Manage KMS** permission for vCenter in your private cloud. The default **CloudOwner** role in VMware Engine has sufficient privileges.
  * A valid license for HyTrust KeyControl. The deployed KeyControl has a 30-day trial license.



## Establish private connection between your private cloud and your VPC network

Identify a project and a Virtual Private Cloud (VPC) network in Google Cloud where you plan to deploy HyTrust KeyControl nodes. [Configure a private connection](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access) between that VPC network and your private cloud.

## Create a VM instance that will become the initial KeyControl node in your cluster

  1. If you do not already have an existing VPC network that you want to use for the KeyControl node, create a new VPC network.
  2. In the Google Cloud console, go to the **Images** page.

[Go to the Images page](https://console.cloud.google.com/compute/images)

  3. Click on the HyTrust KeyControl image.

  4. Click **Create instance**.

  5. Configure the instance:

     * Under **Machine type** , select **n1-standard-2(2 vCPU, 7.5 GB)**.
     * Check **Allow HTTPS traffic**.
     * Under **Network interface** , choose the VPC network you want to use. You can't change this later.
     * The external IP address may be static or ephemeral. To use a static IP address, choose any previously created public IP or choose **Create IP address** under **External IP**.
     * Under **Create public IP address** , enter a name and description for the IP address.
  6. Click **OK**.

  7. Click **Create**.




To create additional KeyControl nodes, you can use metadata from the instance you just created. To see instance metadata, go to the **VM instances** page.

[Go to the VM Instances page](https://console.cloud.google.com/compute/instances)

## Configure firewall rules for the KeyControl instance

Before you start configuring KeyControl, make sure that the following ports are open for KeyControl from your VPC network or from any other network from which you plan to access KeyControl.

#### Required ports

Type | Protocol | Port range  
---|---|---  
SSH (22) | TCP | 22  
HTTPS (443) | TCP | 443  
Custom TCP Rule | TCP | 8443  
Custom UDP Rule | UDP | 123  
  
#### Additional ports

The following ports are required if you plan to use KeyControl as a KMIP server or if you want to use the SNMP polling feature for KeyControl.

Type | Protocol | Default port | KMIP | TCP | 5696  
---|---|---  
SNMP | UDP | 161  
  
To learn how to set up the firewall, see [Firewall tables](https://docs.cloud.google.com/vmware-engine/docs/concepts-firewall-tables).

## Configure the first KeyControl node and initialize the KeyControl web interface

You need to configure the KeyControl instance using SSH before you can use the KeyControl web interface to configure and maintain your KeyControl cluster.

The following procedure describes how to configure the first KeyControl node in the cluster. Make sure you have the KeyControl VM instance ID and external IP address.

  1. Sign in to the **htadmin** account on your KeyControl VM instance.
         
         ssh htadmin@external-ip-address
         

  2. When prompted for the htadmin password, enter the instance ID for your KeyControl instance.

  3. Enter a new password for the KeyControl system administration account htadmin and click **Enter**. The password must contain at least 6 characters and cannot contain spaces or any non-ASCII characters. This password controls access to the HyTrust KeyControl System Console that lets users perform some KeyControl administration tasks. It doesn't permit a KeyControl user to access the full operating system.

**Important:** Keep this password in a secure place. If you lose the password, you must contact HyTrust Support. For security reasons, KeyControl doesn't provide a user-accessible password recovery mechanism.
  4. Under **System configuration** screen, select **Install Initial KeyControl Node** and click **Enter**.

  5. Review the confirmation dialog. This dialog provides the public URL that you can use with the KeyControl web interface and the private IP address that you can use if you want to add other KeyControl nodes to this cluster.

  6. Click **Enter**.

  7. To initialize the KeyControl web interface for this cluster:

     1. In a web browser, navigate to `https://external-ip-address`, where `external-ip-address` is the external IP address associated with the KeyControl instance.
     2. If prompted, add a security exception for the KeyControl IP address and proceed to the KeyControl web interface.
     3. On the HyTrust KeyControl login page, enter **secroot** for the username and enter the instance ID for the password.
     4. Review the EULA (end user license agreement). Click **I Agree** to accept the license terms.
     5. On the **Change Password** page, enter a new password for the secroot account and click **Update Password**.
     6. On the **Configure E-Mail and Mail Server Settings** page, enter your email settings. If you enter an email address, KeyControl sends an email with the admin key for the new node. It also sends system alerts to this email address.

**Note:** To disable alerts by email, check **Disable email notifications**. You download the admin key from the **Settings** tab in the KeyControl web interface. You must download and save the admin key to complete several administrative operations.
     7. Click **Continue**.

     8. On the **Automatic Vitals Reporting** page, specify whether you want to enable or disable automatic vitals reporting. Automatic vitals reporting lets you automatically share information about the health of your KeyControl cluster with HyTrust Support.

If you enable this service, KeyControl periodically sends an encrypted bundle containing system status and diagnostic information to a secure HyTrust server. HyTrust support might proactively contact you if the Vitals Service identifies issues with the health of your cluster.

KeyControl Security Admins can enable or disable this service at any time by selecting **Settings > Vitals** in the KeyControl web interface. For details, see [Configuring Automatic Vitals Reporting](https://docs.hytrust.com/DataControl/5.1.2/Online/Content/Books/aaCommon/Configuring-Automatic-Vitals-Reporting.html).

     9. Click **Save & continue**.

     10. If you are using Internet Explorer, import the certificate and add the KeyControl IP address to your trusted sites list. Verify that the **Downloads > File download** option is enabled under **Internet Options > Security > Custom Level**.




## Configure additional nodes and add them to the existing cluster (optional)

After the first KeyControl node is configured, you can then add additional nodes from other zones or regions. All configuration information from the first node in your cluster is copied to any nodes that you add to your cluster.

Make sure you have the instance ID for your KeyControl VM instance, the external IP address associated with that VM instance, and the private IP address of one of the existing KeyControl nodes in your cluster.

  1. Log into the **htadmin** account on your KeyControl VM instance.
         
         ssh htadmin@external-ip-address
           

  2. When prompted for the htadmin password, enter the instance ID for the KeyControl instance that you are configuring.

  3. Enter a new password for the KeyControl system administration account **htadmin** and click **Enter**. The password must contain at least 6 characters and cannot contain spaces or any non-ASCII characters.

  4. This password controls access to the HyTrust KeyControl System Console that lets users perform some KeyControl administration tasks. It does not permit a KeyControl user to access the full operating system.

**Important:** Keep this password in a secure place. If you lose the password, you must contact HyTrust Support. For security reasons, KeyControl doesn't provide a user-accessible password recovery mechanism.
  5. Under **System configuration** screen, select **Add KeyControl node to existing cluster** and click **Enter**.

  6. Type the internal IP address of any KeyControl node already in the cluster and click **Enter**. KeyControl begins the initial configuration process for the node.

  7. To find the internal IP address for the existing node, log into the KeyControl web interface and click **Cluster** in the top menu bar. Go to the **Servers** tab and look at the IP address in the table.

  8. If this node was previously a part of the selected cluster, KeyControl displays a prompt asking if you want to clear the existing data and rejoin the cluster. Select **Yes** and click **Enter**.

  9. If this node was a member of a different cluster, or was originally configured as the only node in the cluster, KeyControl prompts you that all data will be destroyed on the current node if you continue. Select **Yes** and click **Enter** , then click **Enter** again to confirm the action at the next prompt.

  10. If prompted, enter a one-time password for this KeyControl node and click **Enter**. The password must contain at least 16 alphanumeric characters. It cannot contain spaces or special characters. This password is a temporary string used to encrypt the initial communication between this node and the existing KeyControl cluster. When you authenticate the new node with the existing cluster, you enter this passphrase in the KeyControl web interface so that the existing node can decrypt the communication and verify that the join request is valid.

  11. If the wizard can connect to the designated KeyControl node, it displays the **Authentication** screen informing you that the node is now part of the cluster but must be authenticated in the KeyControl web interface before it can be used by the system.

  12. Authenticate the node in the KeyControl web interface. When the **Joining KeyControl Cluster** screen displays a message that a domain administrator needs to authenticate the new node, log into the KeyControl web interface on that node and authenticate the new server. After the node has been authenticated, KeyControl continues the setup process.

  13. Click **Enter**.




## Authenticate your new KeyControl nodes

When you add a new KeyControl node to an existing cluster, you must authenticate the new node from the KeyControl web interface of the node that was specified in the system console of the joining node. For example, if you have three nodes, and you join a fourth node by specifying node two, you must authenticate the new node from the web interface for node two. If you attempt to authenticate from a different node, the process fails.

  1. Sign in to the KeyControl web interface using an account with Domain Admin privileges.
  2. In the menu bar, click **Cluster**.
  3. Click the **Servers** tab.
  4. Select the node that you want to authenticate. The **Status** column shows **Join Pending** for all nodes that have not yet been authenticated.
  5. Click **Actions > Authenticate**.
  6. Enter the one-time password and click **Authenticate**. This passphrase must exactly match the passphrase that you specified when you installed the KeyControl node. The passphrase is case-sensitive.
  7. Click **Refresh** and make sure that the status is **Online**.
  8. If you want to track the progress of the authentication process, sign in to the KeyControl VM console on the node that you are authenticating as htadmin.



## Configure firewall rules between your private cloud and KeyControl VPC

The vCenter communicates with HyTrust KeyControl over the KMIP protocol on the KMIP Port. The default is TCP 5696. THe port is configurable from the KeyControl web interface.

  1. In the Google Cloud console, click **VPC network > Firewall**.
  2. Click **Create firewall rule**.
  3. Enter the firewall rule details. Allow the vCenter's IP address to communicate with KeyControl on the KMIP port.



## Configure vCenter to use HyTrust KeyControl as an external KMS

  1. [Configure the KMIP server](https://docs.hytrust.com/DataControl/5.1.2/Online/Content/Books/VMware-vSphere-VSAN-Encryption/configuring-kmip-server.html)
  2. [Create a KMS cluster in vCenter](https://docs.hytrust.com/DataControl/5.1.2/Online/Content/Books/VMware-vSphere-VSAN-Encryption/creating-KMS-Cluster.html)
  3. [Establish a trusted connection between vCenter and KeyControl by using a vCenter generated CSR](https://docs.hytrust.com/DataControl/5.1.2/Online/Content/Books/VMware-vSphere-VSAN-Encryption/Establish-Trust-with-vSphere-CSR.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
