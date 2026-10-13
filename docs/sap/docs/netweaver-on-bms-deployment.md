---
url: https://docs.cloud.google.com/sap/docs/netweaver-on-bms-deployment/
title: SAP NetWeaver on Bare Metal Solution deployment guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:16.698907+00:00
---

# SAP NetWeaver on Bare Metal Solution deployment guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-on-bms-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP NetWeaver on Bare Metal Solution deployment guide Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** For new SAP NetWeaver deployments, instead of using Bare Metal Solution servers, we recommend that you use Compute Engine C3 or C4 machine types. 

For information about C3 and C4 machine types, see [General-purpose machine family for Compute Engine](https://docs.cloud.google.com/compute/docs/general-purpose-machines).

This guide covers the aspects of setting up a Bare Metal Solution environment that are unique or relevant to SAP NetWeaver and SAP applications.

In a Bare Metal Solution environment, you install SAP NetWeaver and other SAP software yourself by following the SAP documentation.

**Note:** Installing SAP software is not documented in this guide.

This guide also covers the installation and configuration of the Google Cloud foundational services for SAP that are required or optional for SAP NetWeaver in a Bare Metal Solution environment.

For an overview of SAP NetWeaver on Bare Metal Solution to help you plan for your deployment, see [SAP NetWeaver on Bare Metal Solution planning guide](https://docs.cloud.google.com/sap/docs/netweaver-on-bms-planning).

## High-level steps

The following list shows the high-level steps you need to complete to deploy SAP NetWeaver on Bare Metal Solution after Google Cloud notifies you that your servers are ready.

  1. Complete the connection to your new servers by following the Bare Metal Solution documentation. For the set up procedures, see [Setting up the Bare Metal Solution environment](https://docs.cloud.google.com/bare-metal/docs/bms-setup) in the Bare Metal Solution documentation.
  2. Validate the server configuration for SAP NetWeaver.
  3. Establish a connection to the internet for software updates. See [Accessing the internet](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-access-internet) in the Bare Metal Solution documentation.
  4. Establish a connection to Google Cloud APIs. See [Setting up access to Google Cloud APIs and services](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-to-gc-apis) in the Bare Metal Solution documentation.
  5. Set up access to a Network Time Protocol (NTP) server, which is not covered in this guide.
  6. Set up a Domain Name System (DNS) server, which is not covered in this guide.
  7. Install Google Cloud's Agent for SAP on a Bare Metal Solution server.



## Validating the server configuration for SAP NetWeaver

When you log into your servers for the first time, you need to confirm that your server configuration matches your order.

For information about Bare Metal Solution server validation, see [Logging in to a Bare Metal Solution server for the first time](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-first-logon).

## Set up application service accounts

Any application program, agent, or process that accesses Google Cloud resources from a Bare Metal Solution environment needs an IAM service account for authentication and authorization.

To create a service account:

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select your Google Cloud project.

  3. Click **Create Service Account**.

  4. Specify a name for the service account and, optionally, a description.

  5. Click **Create and Continue**.

  6. On the **Grant this service account access to project** panel, select the roles that contain the permissions that your application needs.

For example, the `fence_gce` agent that is used in high-availability clusters needs the `baremetalsolution.service.resetInstance` permission, which is included in the IAM roles `roles/baremetalsolution.editor` and `roles/baremetalsolution.admin`.

  7. Click **Continue**.

  8. As appropriate, grant other users access to the service account.

  9. Click **Done**.

  10. On the **Service accounts** page in the Google Cloud console, click the email address of the service account that you just created.

  11. Under the service account name, click the **Keys** tab.

  12. Click the **Add Key** drop-down menu, and then select **Create new key** to create [a service account key](https://docs.cloud.google.com/iam/docs/service-account-creds#key-types).

  13. Accept JSON as the key type and click **Create**. A private key is saved to your computer.

  14. Upload the JSON key file to a secure location on the Bare Metal Solution servers that is accessible to the applications that require it.

  15. Configure your applications to access the JSON key file.

For example, when you create the high-availability cluster resource that uses the `fence_gce` agent, you specify the path and filename of the JSON key file in the `fence_gce` configuration properties.




For more information about IAM service accounts, see:

  * [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts)
  * [Service account best practices](https://docs.cloud.google.com/iam/docs/understanding-service-accounts)



## Confirming connectivity to the application servers

Confirm that you have network connectivity between the database server and the application servers.

Make sure that your Google Cloud and guest operating system firewall rules allow traffic between the servers.

## Installing SAP NetWeaver

To install SAP NetWeaver on a Bare Metal Solution server, you need to follow the SAP installation documentation for your version of SAP NetWeaver.

To find the installation documentation for your version of SAP NetWeaver, see the [SAP Help Portal](https://help.sap.com/viewer/product/SAP_NETWEAVER/ALL).

## Install Google Cloud's Agent for SAP

Google Cloud's Agent for SAP is required for SAP support of SAP NetWeaver systems running on Bare Metal Solution servers. When you install Google Cloud's Agent for SAP on your Bare Metal Solution server, the agent gathers data from Cloud Monitoring and the Bare Metal Solution server, and then provides that data to the SAP Host Agent.

If you're using the following RHEL or SLES "for SAP" OS images that Google Cloud provides, then Google Cloud's Agent for SAP is packaged with the OS images:

  * RHEL: all "for SAP" images
  * SLES: SLES 15 SP4 for SAP and later versions



For information about the OS versions that you can use to run SAP NetWeaver systems on Bare Metal Solution servers, see [Certified operating systems](https://docs.cloud.google.com/sap/docs/netweaver-on-bms-planning#netweaver-cert-table-oss).

To install Google Cloud's Agent for SAP on a Bare Metal Solution server, follow these steps:

  1. Establish an SSH connection to your Bare Metal Solution server.

  2. In your terminal, install the agent by running the command that is specific to your operating system:

     * (Recommended) To install version 3.15 (latest) of the agent: 

### RHEL
           
           sudo tee /etc/yum.repos.d/google-cloud-sap-agent.repo << EOM
           [google-cloud-sap-agent]
           name=Google Cloud Agent for SAP
           baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-el$(cat /etc/redhat-release | cut -d . -f 1 | tr -d -c 0-9)-x86_64
           enabled=1
           gpgcheck=1
           repo_gpgcheck=0
           gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
           EOM
           sudo yum install google-cloud-sap-agent

### SLES15
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles15-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent

### SLES 12
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles12-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent

     * To install a specific version of the agent: 

### RHEL
           
           sudo tee /etc/yum.repos.d/google-cloud-sap-agent.repo << EOM
           [google-cloud-sap-agent]
           name=Google Cloud Agent for SAP
           baseurl=https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-el$(cat /etc/redhat-release | cut -d . -f 1 | tr -d -c 0-9)-x86_64
           enabled=1
           gpgcheck=1
           repo_gpgcheck=0
           gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
           EOM
           sudo yum install google-cloud-sap-agent-VERSION_NUMBER.x86_64

### SLES15
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles15-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

### SLES 12
           
           sudo zypper addrepo --refresh https://packages.cloud.google.com/yum/repos/google-cloud-sap-agent-sles12-x86_64 google-cloud-sap-agent
           sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

Replace `VERSION_NUMBER` with the agent's version number that you want to install, such as `3.1-606637668`. For information about the agent versions that you can install, see [List all available versions of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#list_all_available_versions_of_the_agent).

  3. Open the following configuration file:
         
         /etc/google-cloud-sap-agent/configuration.json

  4. Modify or add the following parameters to the configuration file:

     * In the first section: 
       * `bare_metal`: set to `true`.
     * Add the `cloud_properties` section and specify the following parameters: 
       * `project_id`: specify your Google Cloud project
       * `instance_name`: specify the name of your Bare Metal Solution server
       * `region`: specify the region of your Bare Metal Solution server
  5. Save the configuration file.

  6. Restart the agent:
         
         sudo systemctl restart google-cloud-sap-agent




For more information about the configuration parameters, see [Install Google Cloud's Agent for SAP on a Bare Metal Solution server](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms#configuration_parameters)

After you install Google Cloud's Agent for SAP and the SAP Host Agent, validate the installation of Google Cloud's Agent for SAP, as described in Validate your installation of the agent.

### Validate your installation of Google Cloud's Agent for SAP

  1. Establish an SSH connection with your Bare Metal Solution server. 

  2. Run the following command: 
         
         systemctl status google-cloud-sap-agent

If the agent is functioning properly, then the output contains `active (running)`. For example: 
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
         Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; enabled; vendor preset: disabled)
         Active: **active (running)** since Fri 2022-12-02 07:21:42 UTC; 4 days ago
         Main PID: 1337673 (google-cloud-sa)
         Tasks: 9 (limit: 100427)
         Memory: 22.4 M (max: 1.0G limit: 1.0G)
         CGroup: /system.slice/google-cloud-sap-agent.service
                └─1337673 /usr/bin/google-cloud-sap-agent
         




If the agent isn't running, then [restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).

### Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## Configure a high-availability cluster

Configure clustering or a suitable high availability solution for your business critical workloads. We recommend Pacemaker clustering.

With the exception of a few requirements and recommendations, configure high-availability clusters on Bare Metal Solution servers by following the clustering instructions that your operating system vendor provides.

For more information about the Google Cloud requirements and recommendations for configuring a highly available SAP NetWeaver system on Bare Metal Solution, see [High-availability clusters for SAP NetWeaver on Bare Metal Solution](https://docs.cloud.google.com/sap/docs/netweaver-on-bms-planning#nw-ha-clusters-on-bms).

### Floating IP addresses

A high-availability cluster for SAP NetWeaver uses two floating or virtual IP addresses (VIPs): one to direct network communication to the SAP Central Services component and another for Enqueue Replication Server communication between the nodes. When configuring your VIPs, use the standard `IPaddr2` Pacemaker resource, which uses gratuitous ARP requests to move the VIP between the hosts. For more information, see [Address Resolution Protocol](https://en.wikipedia.org/wiki/Address_Resolution_Protocol).

The following example shows an `IPaddr2` resource definition for SAP Central Services on SUSE:
    
    
    crm configure primitive scs-vip-rsc-name IPaddr2 \
        params ip=10.0.0.79 \
        op monitor interval=10 timeout=20

You add each `IPaddr2` resource to a resource group that contains the SAP Central Services resource or the Enqueue Replication Server resource that it is for, so that the resources move together during a failover. For example, the following command creates a group for SAP Central Services:
    
    
    crm configure group scs-rsc-group-name \
      scs-file-system-rsc-name \
      **scs-vip-rsc-name** \
      **scs-instance-sap-rsc-name** \
      meta resource-stickiness=3000

Similarly, the following command creates another group for the Enqueue Replication Server:
    
    
    crm configure group ers-rsc-group-name \
      ers-file-system-rsc-name \
      **ers-vip-rsc-name** \
      **ers-instance-rsc-name**

#### Configure SBD fencing with shared block storage

To configure SBD fencing, you need to follow the instructions that are provided by your software vendor.

This section shows you only how to identify and validate the storage devices that Google Cloud provisioned for SBD fencing.

To configure SBD fencing on SUSE, see:

  * [Storage Protection and SBD on SUSE Linux Enterprise HAE 12 SP5](https://documentation.suse.com/sle-ha/12-SP5/html/SLE-HA-all/cha-ha-storage-protect.html)
  * [Storage Protection and SBD on SUSE Linux Enterprise HAE 15 SP1](https://documentation.suse.com/sle-ha/15-SP1/html/SLE-HA-all/cha-ha-storage-protect.html)
  * [Storage Protection and SBD on SUSE Linux Enterprise HAE 15 SP2](https://documentation.suse.com/sle-ha/15-SP2/html/SLE-HA-all/cha-ha-storage-protect.html)



##### Validate the block storage devices for SBD fencing

Google Cloud creates three shared LUNs for SBD block storage when it provisions an order for a high-availability cluster that uses SBD fencing.

You can identify the shared storage devices for SBD by issuing the `multipath -ll` command to list the multipath devices on both servers:
    
    
    multipath -ll | grep "size=Size of your LUN" -B1

In each list, look for three devices of the same size and make a note of their names. The default size is 50 GB.

In the following example, the string `size=50G` is used to filter the list of multipath devices that is returned by the `multipath -ll` command:
    
    
    multipath -ll | grep "size=50G" -B1

The example output from the preceding command includes the three 50 GB multipath devices to be used for SBD fencing:
    
    
    3600a098038314566785d5150506a594b dm-16,LUN C-Mode
    size=50G features='3 queue_if_no_path pg_init_retries 50' hwhandler='1 alua' wp=rw
    --
    3600a098038314566785d5150506a594c dm-15,LUN C-Mode
    size=50G features='3 queue_if_no_path pg_init_retries 50' hwhandler='1 alua' wp=rw
    --
    3600a098038314566785d5150506a594d dm-11,LUN C-Mode
    size=50G features='3 queue_if_no_path pg_init_retries 50' hwhandler='1 alua' wp=rw

The names of the three devices must be exactly the same on both servers, which indicates that they are shared LUNs.

When you follow the SBD configuration instructions that are provided by your operating system vendor, you reference these three device names.

For example, when you initialize each device for SBD use and set the wait and timeout values, you specify the device names as shown in the following example:
    
    
    sbd -d /dev/mapper/3600a098038314566785d5150506a594b -1 60 -4 180 create

When you set the SBD configuration in `/etc/sysconfig/sbd`, you also need to reference the device names. For example:
    
    
    SBD_DEVICE="/dev/mapper/3600a098038314566785d5150506a594b;/dev/mapper/3600a098038314566785d5150506a594c;/dev/mapper/3600a098038314566785d5150506a594d"
    [..]
    SBD_PACEMAKER="yes"
    [...]
    SBD_STARTMODE="always"

#### Configure the `fence_gce` agent

The following high-level steps help you configure a fencing resource for your high availability cluster that uses the `fence_gce` agent that is included with your Linux operating system.

  1. In your Google Cloud project, assign an IAM role that includes the `baremetalsolution.service.resetInstance` permission to a new or existing IAM service account for which you have the JSON key file.

The predefined role `roles/baremetalsolution.editor` includes the required permission or you can create a custom role for more granular control over the permissions that the role includes.

For more information, see Set up application service accounts.

  2. Upload the service account JSON key file to all Bare Metal Solution servers in the high-availability cluster.

  3. Confirm that your version of the `fence_gce` agent supports Bare Metal Solution.

     1. Connect to your Bare Metal Solution server by using SSH.

     2. Display the `fence_gce` agent help:
            
            $ sudo fence_gce --help

     3. In the `fence_gce` help, look for the following properties:
            
            --baremetalsolution            Enable on bare metal
            ...
            --serviceaccount=[filename]    Service account json file location e.g.
                                               serviceaccount=/somedir/service_account.json
            

If you don't see both the `--baremetalsolution` and `--serviceaccount=[filename]` properties, then you need to update the agent. Contact Cloud Customer Care for patching instructions. The patching procedure differs depending on which Linux version you are using.

  4. Specify the `fence_gce` agent as your fencing device on each cluster node when you configure the cluster resources according to the clustering instructions that are provided by your operating system vendor.

When you define the resource, specify the following `fence_gce` parameters to enable the agent for the Bare Metal Solution environment:

     * `baremetalsolution="true"`
     * `serviceaccount="file_path/key_file.json"`

The following example shows a `fence_gce` fencing device resource that is defined on SUSE:
    
    crm configure primitive STONITH-"server_name" stonith:fence_gce \
     op monitor interval="300s" timeout="60s" on-fail="restart" \
     op start interval="0" timeout="60s" onfail="restart" \
     params port="server_name" zone="Google_Cloud_zone" project="Google_Cloud_project_ID" \
       baremetalsolution="true" method="cycle" \
       serviceaccount="file_path/key_file.json"

The fencing resource example uses the following definitions:

Definition | Explanation  
---|---  
`baremetalsolution=true` | Configures the fencing agent for operation in the Bare Metal Solution environment.  
`serviceaccount=file_path/key_file.json` | The path to the JSON key file that contains the key for the service account that the fencing agent uses to access the Google Cloud APIs.  
`port=server_name` | The original hostname of the Bare Metal Solution server that the fencing device can reset.  
`method=cycle` | Defines the method to use for resetting the failed server.  
  5. After you define each fencing resource, set the location of the fencing device to a server other than the server that you intend it to reset:
         
         crm configure location LOC_STONITH_server_name STONITH-server_name -inf: server_name




## Restarting your Bare Metal Solution server

You can restart your Bare Metal Solution server by using the Google Cloud console, Google Cloud CLI, or API.

Before restarting a server, make sure to stop all applications and databases that are running on the server.

For information about how to restart a Bare Metal Solution server, see [Operate your Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#operate_a_server).

## Getting support for SAP NetWeaver on Bare Metal Solution

If you need help resolving a problem with SAP NetWeaver and SAP application deployments on Bare Metal Solution, gather the required diagnostic information and contact Cloud Customer Care. For more information, see [SAP on Bare Metal Solution diagnostic information](https://docs.cloud.google.com/sap/docs/getting-support-diag-info-sap-bms).

## Support

For issues with Google Cloud infrastructure or services, contact Customer Care. You can find the contact information on the [Support Overview page](https://console.cloud.google.com/support) in the Google Cloud console. If Customer Care determines that a problem resides in your SAP systems, then you are referred to SAP Support.

For SAP product-related issues, log your support request with [SAP support](https://support.sap.com/support-programs-services/about/getting-started.html). SAP evaluates the support ticket and, if it appears to be a Google Cloud infrastructure issue, then SAP transfers that ticket to the appropriate Google Cloud component in its system: `BC-OP-LNX-GOOGLE` or `BC-OP-NT-GOOGLE`.

### Support requirements

Before you can receive support for SAP systems and the Bare Metal Solution infrastructure and services that they use, you must meet the minimum support plan requirements.

For more information about the minimum support requirements for SAP on Google Cloud, see:

  * [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support)
  * [ SAP Note 2456406 - SAP on Google Cloud Platform: Support Prerequisites](https://launchpad.support.sap.com/#/notes/2456406) (An SAP user account is required)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
