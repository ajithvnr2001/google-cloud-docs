---
url: https://docs.cloud.google.com/sap/docs/sap-lama-connector-deployment/
title: Connector for LaMa installation and operations guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:48.817283+00:00
---

# Connector for LaMa installation and operations guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/sap-lama-connector-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Connector for LaMa installation and operations guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide covers the installation and configuration of the Google Cloud Connector for SAP Landscape Management (Connector for LaMa), as well as operational tasks after the connector is installed.

To install and configure the Connector for LaMa, you perform the following high-level steps:

  * Configure authentication and authorization to the Google Cloud APIs.
  * Download the installation archive from Google Cloud.
  * Install the Connector for LaMa on the same host as SAP Landscape Management. The host can be either a Compute Engine virtual machine (VM) or a virtual or physical machine that is not on Google Cloud.
  * Configure the Cloud Manager for Google Cloud functionality in SAP Landscape Management.
  * Install storage library and operations files on each VM that hosts an SAP system to be managed by SAP Landscape Management.



## Prerequisites

Before you can install the Connector for LaMa, you need to install and configure a supported version of SAP Landscape Management. For the supported versions, see [Software requirements](https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning#software_requirements).

Install SAP Landscape Management according to the SAP Landscape Management installation guides and the SAP Landscape Management Adaptive Design principles.

For more information, see:

  * [SAP Landscape Management](https://help.sap.com/viewer/product/SAP_LANDSCAPE_MANAGEMENT_ENTERPRISE/LATEST?task=implement_task)
  * [Adaptive Design](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-US/737a99e86f8743bdb8d1f6cf4b862c79.html)



## Configure authentication and authorization to the Google Cloud APIs

You need to configure CA certificates and, if you need tighter access control, an IAM service account.

### Upload CA Certificates for Google API communication

The Connector for LaMa requires appropriate CA certificates to communicate with the Google Cloud APIs. Make sure the following certificates are available in the Trusted CAs view of the SAP NetWeaver Java KeyStore Storage view:

  * GTS CA 1C3
  * WR2


  1. Go to the Google Trust Services repository at <https://pki.goog/repository/>

  2. In the **Download CA certificates** section under **Subordinate CAs** , download CA certificates `GTS CA 1C3` and `WR2`. Note that the `WR2` certificate replaced `GTS CA 1C3` certificate in 2024 for certain APIs.

  3. Import the certificates by following the instructions in the SAP NetWeaver documentation: [Using the AS Java Key Storage](https://help.sap.com/viewer/1531c8a1792f45ab95a4c49ba16dc50b/7.5.20/en-US/e9a1dd44d2c83c43afb5ec8a4292f3e0.html). 




### Create an IAM service account

Unless you intend to use the service account of the hosting VM instance as the default service account, you need to create an IAM service account for the Connector for LaMa.

To create a service account for the Connector for LaMa:

  1. In the Google Cloud console, go to the **Service accounts** page:

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select your Google Cloud project.

  3. Click **Create Service Account**.

  4. Specify a name for the service account and, optionally, a description.

  5. Click **Create and Continue**.

  6. On the **Grant this service account access to project** step, grant the service account a role that contains all of the permissions that SAP Landscape Management requires. A role can be a predefined role, like `Compute Admin`, or a custom role that you create that contains the permissions that are listed in [Required IAM resource permissions for the Connector for LaMa](https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning#c4lm_minimum_iam_permissions).

  7. Click **Done**.

  8. On the **Service accounts** page in the Google Cloud console, click on the service account that you just created.

  9. Under the service account name, click the **Keys** tab.

  10. Click the **Add Key** menu, and then select **Create new key** to create [a service account key](https://docs.cloud.google.com/iam/docs/service-account-creds#key-types).

  11. Accept JSON as the key type and click **Create**. A private key is saved to your computer. Store the JSON key file in a safe place. Later, when you configure the Cloud Manager function SAP Landscape Management, you copy and paste the contents of the key file into SAP Landscape Management.




## Set the JVM to use Internet Protocol version 4

Use either [Java System Properties tool](https://help.sap.com/viewer/33292dc46b0e415ca41727cd5f215a24/LATEST/en-US/48bdba8f50dd35bce10000000a42189d.html) of SAP Netweaver Administrator or the [SAP NetWeaver Config tool](https://help.sap.com/viewer/0c333adb55cd4dbf8e92a5175703224c/LATEST/en-US/eab54b79ea7f419f85f328add7f0ab16.html) to specify `-Djava.net.preferIPv4Stack=true` in the JVM system parameters.

When `-Djava.net.preferIPv4Stack=true` is specified, SAP NetWeaver uses only Internet Protocol version 4 (IPv4).

For more information, see [Internet Protocol version 4 (IPv4) requirement](https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning#internet_protocol_version_4_ipv4_requirement).

## Download the Connector for LaMa

You download the Connector for LaMa from Google Cloud in a `tar` file, `gcp-connectorversion.tar`, that contains the following files:

  * The Connector for LaMa in a Java Enterprise Archive file, `lvm.cloud.gcp-version.ear`.
  * The Cloud Manager OS storage library: 
    * For Linux: `libsapacosprep_gcp-version.so`
    * For Windows: `libsapacosprep_gcp-version.dll`
  * Operation definitions that are customized for Google Cloud.
  * Operation scripts that correspond to the operation definitions.



To download the latest version of Connector for LaMa, contact Cloud Customer Care. To find the contact information for Customer Care, go to the [Support overview](https://console.cloud.google.com/support) page in the Google Cloud console. For more information, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).

With the compressed tar file, Google Cloud also provides an `asc` signature file, `gcp-connectorversion.tar.asc`, that you can use to confirm that the `gcp-connectorversion.tar` file downloaded correctly.

Store the `tar` file in a Cloud Storage bucket that is accessible to both the SAP Landscape Management server and the servers to be managed, or upload it via the Cloud Shell upload function as described in [Transferring files to instances](https://docs.cloud.google.com/compute/docs/instances/transfer-files).

## Install the Connector for LaMa on the SAP Landscape Management server

To install the Connector for LaMa, you deploy an EAR file to SAP NetWeaver and configure a Cloud Manager for Google Cloud in SAP Landscape Management.

### Deploying the Connector for LaMa on SAP NetWeaver

Install the EAR file that contains the Connector for LaMa by using any of the following SAP NetWeaver Java deployment methods (An SAP user account is required):

  * [SAP Note 1715441 - Deploy/Undeploy/Force Redeploy EAR/SDA/SCA files on SAP AS JAVA](https://launchpad.support.sap.com/#/notes/1715441)
  * [SAP Note 2462712 - Deploy/undeploy set of EAR/WAR/RAR/SDA files using SAP Shell Console Admin via telnet](https://launchpad.support.sap.com/#/notes/2462712)



### Configuring the Cloud Manager functionality in SAP Landscape Management

After you install the Connector for LaMa, in the SAP Landscape Management interface, you configure the Cloud Manager functionality for Google Cloud.

The general procedure for configuring Cloud Manager is documented by SAP in [Configuring Cloud Managers](https://help.sap.com/viewer/lama_help/af330fb5dd0b4636b3cb8df30494ff97.html).

The following steps are specific to configuring a Cloud Manager for Google Cloud.

To configure a new Cloud Manager for Google Cloud, perform the following configuration steps:

  1. In SAP Landscape Management, go to **SAP Landscape Management Infrastructure** > **Cloud Managers.**
  2. Create a new Cloud Manager by clicking **Add**.
  3. From the list of Installed Cloud Manager Types choose Google Cloud Adapter.
  4. In the **Basic properties** section: 
     * In the Label field, enter a name for the Cloud Manager for Google Cloud.
     * In the Monitoring Interval, accept the default of 300 seconds.
     * Leave all other fields blank.
  5. If you are using a dedicated service account for Connector for LaMa, paste the contents of the JSON key file of the service account into the **Service Account** field in the **Additional properties** section.
  6. If you are using the service account of the VM for Connector for LaMa, leave **Service Account** blank.
  7. Perform "Test Configuration" to validate the settings and to test the connection to the Google Cloud API urls.
  8. Choose **Next** and **Save to new Cloud Manager**.



Entries in the **Virtualization** and **Storage Manager** views are created automatically.

Only the Cloud Manager configuration can be changed; editing is deactivated in the other views.

### Configuring support for duplicate IP addresses

If the internal networks within your managed SAP landscape include duplicate IP addresses, configure SAP Landscape Management to use fully-qualified host names to map the managed SAP systems.

To use fully-qualified host names, in SAP Landscape Management monitoring settings, select the **Use FQDN Hostnames Only** checkbox. For more information, see [Configuring Monitoring Settings](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/3.0.21.0/en-US/ed12b6e8278b490bb0713fd80e7c887c.html).

**Software requirements:** Support for duplicate IP addresses requires Connector for LaMa version 2.3.0 or later and specific versions of SAP software. For more information, see [SAP software requirements](https://docs.cloud.google.com/sap/docs/sap-lama-connector-planning#c4lm_sap_software_requirements). 

## Install Google Cloud's Agent for SAP

For support and monitoring, Google Cloud provides the _Agent for SAP_ , for SAP workloads running on Compute Engine instances and Bare Metal Solution servers.

As mandated by SAP, to get support from SAP and to enable SAP to meet its service-level agreements (SLAs), you must install Google Cloud's Agent for SAP on all Compute Engine instances and Bare Metal Solution servers that run any SAP system. For more information on the support prerequisites, see [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406).

**Version 3.15 (latest)** of Google Cloud's Agent for SAP is the successor of Google Cloud's monitoring agent for SAP NetWeaver version 2, monitoring agent for SAP HANA version 2, and the Cloud Storage Backint agent for SAP HANA. Therefore, in addition to the collection of metrics, version 3.15 (latest) of Google Cloud's Agent for SAP includes the optional feature: _Backint based backup and recovery for SAP HANA_.

You can opt in to these features that enable products and services such as [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview) for your SAP workloads.

**Note:** SAP Host Agent, with the `saposcol program`, is required on any host that is running an SAP system. SAP Host Agent is installed automatically during the installation of new SAP system instances with SAP kernel 7.20 or higher. For more information, see [SAP Host Agent](https://help.sap.com/docs/SAP%20Host%20Agent/8661d17ee5c047a887f686b33e990ede/e817cfb89dbc4d799825c94da59c7867.html).

You install Google Cloud's Agent for SAP on the host alongside the SAP system. For instructions about how to install and configure the agent, validate your installation, and verify that the agent is running as expected, see [Install the agent on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm). 

If you use the following RHEL or SLES "for SAP" OS images that Google Cloud provides, then Google Cloud's Agent for SAP is packaged with the OS images:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



## Install the OS storage library and operation definitions on the managed VMs

The `gcp-connectorversion.tar` file includes an OS storage library and operation definitions with their corresponding scripts.

You need to install the OS storage library and operation files on each VM instance that is managed by SAP Landscape Management.

To install an OS storage library and operation definitions on a VM that is managed by SAP Landscape Management:

  1. Download or copy the `gcp-connectorversion.tar` file to the target VM.
  2. Extract the files in the `gcp-connectorversion.tar` file into a temporary directory.
  3. Run the installation script:

     * On Linux, enter: 
           
           sudo bash install.sh

     * On Windows, with administrative privileges enter: 
           
           install.cmd

The install script copies the OS storage library to the directory of the active SAP Host Agent, `/usr/sap/hostctrl/exe` and the operations files to a subdirectory, `/operations.d`. The script sets file ownership to `root:sapsys` and sets appropriate access rights for each file type.
    
    file ./storage/libsapacosprep_gcp-2.2.15.96.so copied to /usr/sap/hostctrl/exe/libsapacosprep_gcp.so
    file ./storage/Operations/AcActivateIP copied to /usr/sap/hostctrl/exe/operations.d/sapacosprep/AcActivateIP
    file ./storage/Operations/AcDeactivateIP copied to /usr/sap/hostctrl/exe/operations.d/sapacosprep/AcDeactivateIP
    file ./storage/Operations/ActivateIP.sh copied to /usr/sap/hostctrl/exe/operations.d/sapacosprep/ActivateIP.sh
    file ./storage/Operations/DeactivateIP.sh copied to /usr/sap/hostctrl/exe/operations.d/sapacosprep/DeactivateIP.sh




## Manage SAP systems on Google Cloud with SAP Landscape Management

After the Connector for LaMa is installed and the Cloud Manager function is configured in SAP Landscape Management, you can use SAP Landscape Management to manage SAP systems on Google Cloud. For information about how to use SAP Landscape Management, see the [SAP Landscape Management, enterprise edition](https://help.sap.com/viewer/product/SAP_LANDSCAPE_MANAGEMENT_ENTERPRISE/LATEST/en-US) documentation.

## Updating from an earlier release

To update the Connector for LaMa from a previous version, perform the following steps.

  1. In SAP Landscape Management, backup all existing Cloud Manager for Google Cloud configurations before updating the Connector for LaMa. For more information, see [Exporting configuration data](https://help.sap.com/viewer/e7dead4286c545808b3bd24feee7448c/LATEST/en-US/4e03e5957b3721e8e10000000a42189e.html).
  2. Reinstall the Connector for LaMa. For instructions, see Deploying the Connector for LaMa on SAP NetWeaver.
  3. Replace the existing OS storage libraries and operations files in the managed systems by following the instructions in Installing the OS storage library and operation definitions.
  4. After deployment, restart SAP Landscape Management.



## Troubleshooting

By default the SAP Landscape Management system operates on Google Cloud by using the identity of an IAM [service account](https://docs.cloud.google.com/iam/docs/service-accounts). If you experience authorization errors, first try using `gcloud` commands to perform the same action that is receiving the error from within the guest operating system. For example:

**SAP Landscape Management action** | **Equivalent`gcloud` command**  
---|---  
Stop/start | `gcloud compute instances stop/start`  
Clone | `gcloud compute disks snapshot`  
`gcloud compute disks create`  
Relocate | `gcloud compute instances attach-disk`  
`gcloud compute instances detach-disk`  
  
The `gcloud` command output provides you with an indication of whether you are missing authorizations to execute a particular action. If this is successful, but your error persists, contact Support as described in the following section.

## Support

If you come across issues with the operation of your SAP Landscape Management system that you need help to resolve, please log a support message via the SAP Support Portal under component BC-VCM-LVM.

If you determine that the root cause of the issue is in the Connector for LaMa, select sub-component BC-VCM-LVM-GOOGLE; however, if you are unsure of the cause of a problem, choose component BC-VCM-LVM, so that SAP support can analyse the issue first.

Information to include:

  * The SAP Landscape Management version
  * The Connector for LaMa version
  * The SAP NetWeaver kernel version
  * The version of the managed SAP system, including the version of the host agent
  * A description of the expected behavior



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
