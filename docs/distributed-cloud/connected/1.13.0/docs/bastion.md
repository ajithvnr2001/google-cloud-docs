---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/bastion/
title: Configure a bastion host \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:08.208955+00:00
---

# Configure a bastion host  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/bastion/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)



Send feedback 

#  Configure a bastion host Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure a bastion host on your Google Distributed Cloud connected deployment to allow Google engineers to access and troubleshoot the nodes in your Distributed Cloud connected zone over Secure Shell (SSH).

Google provides the full source code from which you can build a customized bastion host virtual machine based on your business requirements.

## Prerequisites

This section lists the prerequisites for deploying the Distributed Cloud connected bastion host solution.

### Enable Access Approval

The bastion host feature uses the Access Approval feature of Access Transparency to let Google request access to your data. You must enable Access Transparency and Access Approval on your Google Cloud project before deploying bastion host virtual machines. For more information, see the following pages:

  * [Enabling Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable)
  * [Overview of Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



### Virtual machine specifications

The Distributed Cloud connected bastion host solution requires the equivalent of a `small` size OpenStack deployment with the following specifications:

  * CPU: 1 vCPU
  * RAM: 2GB
  * Disk: 20GB



Google recommends deploying N+1 bastion host virtual machines per Google Cloud region for increased reliability.

### Networking requirements

The Distributed Cloud connected bastion host solution requires that you configure the following network peering sessions for each bastion host virtual machine:

  * **Northbound.** Connects the bastion host virtual machine to the Internet. Requires Internet access and must allow connections on port 22 from specific IP addresses that Google provides as part of the bastion host solution disk image and source code package.
  * **Southbound.** Connects the bastion host virtual machine over port 22 to the corresponding Distributed Cloud connected zones in a single Google Cloud region.
  * **Management.** Connects the bastion host virtual machine to your local network for operation and maintenance purposes. Configure this peering session according to your organization's security policy.



### Security best practices

Google highly recommends that you follow the security best practices described in this section when configuring a bastion host solution on your Distributed Cloud connected deployment in addition to your organization's security policies:

  * Follow the least-privilege rule and maintain a clear separation of duties for users.
  * For all user accounts other than the Administrator use only certificate-based authentication; disable password-based authentication and root access to the bastion host virtual machines.
  * Reject access from all IPs on the northbound peering session that are not part of the Google-provided support IP address list.
  * Close all ports on the southbound peering session except port 22 (SSH) and allow it only for IP addresses on the Google-provided support IP address list.
  * Keep all bastion host virtual machines up to date. Google provides a new source code package with each security patch and version update.
  * Configure an alerting and an auditing solution that both satisfy your organization's security policies.



## Enable bastion host support

To enable bastion host support on your Distributed Cloud connected deployment, [submit a request](https://docs.google.com/forms/d/e/1FAIpQLSdDh4yHBxwxz04tkYNiTT3QSGpDSAZGMFAu6CqCqXGGrQP0Vw/viewform?usp=header_link).

You must individually enable and configure bastion host support for each of your Distributed Cloud connected zones. This lets you deploy different access and network configurations that best fit your organization's business needs for each Distributed Cloud connected zone.

## Obtain the bastion host software

The bastion host software package is sent to you after Google Support activates the bastion host feature for your Distributed Cloud connected deployment. The package contains the following:

  * **Source code.** You can customize and build your own bastion host virtual machine images based on your business requirements.
  * **Documentation.** Additional documentation for tasks such as configuring certificates.



## Build a bastion host virtual machine image

This section provides an overview of the steps required to build a bastion host virtual machine image from the source code provided by Google. Complete instructions are provided in the `README` file that ships with the source code.

### Prerequisites

You need the following items to build a bastion host virtual machine image:

  * A machine running Debian 11.
  * The latest Debian cloud server image.
  * The `qemu-img`, `qemu-system-x86_x64`, and GNU `mtools` software installed on the machine.
  * A file named `host-user-key.pub` containing a public SSH key for logging on to the bastion host instance and initiating a `host-user` session. This key can be used for direct authentication or as a certificate authority signing key. The bastion host instance must trust this CA.
  * A file named `admin-user-key.pub` containing a public SSH key for performing administrative tasks on the target bastion host instance. This key can be used for direct authentication or as a certificate authority signing key. The bastion host instance must trust this CA. 
  * A file named `guest-user-key.pub` containing a public SSH certificate authority signing key provided by Google that allows Google Support to authenticate as `guest-user` when connecting to the bastion host instance.



### Build the virtual machine image

Follow the instructions provided in the `README` file that ships with the source code to build the bastion host virtual machine image from source code provided by Google. The examples in this guide refer to the resulting image file as `bastion-host.img`.

### Build the HIBA package

Build the Debian installation package for the Host Identity-Based Authorization for SSH (HIBA) authentication software layer as follows:

  1. Install the required dependencies using the following command:
         
         sudo apt-get install autoconf autogen build-essential git libssl-dev libtool zlib1g-dev

  2. Build the installation package using the following command:
         
         ./build-hiba.sh -j $(nproc) /tmp/hiba-build-workdir




The installation package is deposited in the `/tmp/hiba-build-workdir` directory and is named `hiba_x.y-z_amd64.deb` where `x`, `y` and `z` denote the HIBA version number.

### Generate the `cloud-init` configs

Use the `generate-cloud-init.py` script to generate the required `cloud-init` configs. You can also generate these configs using your own tools. These configs do the following:

  * Create the required user accounts within the bastion host virtual machine image and configure those accounts with the SSH keys described earlier.
  * Add a script that limits the privileges of the `guest-user` account to only joining an established terminal multiplexer session.
  * Add scripts that create and manage a terminal multiplexer session.
  * Prepare the HIBA configuration files.



The `generate-cloud-init.py` script requires the HIBA package you built earlier, and the three files containing the required SSH keys. Run the script as follows:
    
    
    ./generate-cloud-init.py \
        --hiba-package="${WORK_DIR}/hiba_1.0-1_amd64.deb" \
        --host-user-key="HOST_USER_KEY_FILE" \
        --manager-user-key="ADMIN_USER_KEY_FILE" \
        --guest-user-ca="GUEST_USER_KEY_FILE" \
        "${WORK_DIR}/cloud-init/"

Replace the following:

  * `HOST_USER_KEY_FILE`: the full path and name of the `host-user-key.pub` file.
  * `ADMIN_USER_KEY_FILE`: the full path and name of the `admin-user-key.pub` file.
  * `GUEST_USER_KEY_FILE`: the full path and name of the `guest-user-key.pub` file.



The script deposits the `cloud-init.img` file into the `cloud-init` directory inside your local working directory.

### Apply the `cloud-init` configs to the bastion host virtual machine image

Use the `qemu-system-x86_64` tool to apply the `cloud-init` configs you generated earlier to your bastion host virtual machine image file as follows:
    
    
    qemu-system-x86_64 \
          -nographic \
          -enable-kvm \
          -smp 1 \
          -m 1g \
          -drive format=qcow2,index=0,file=${WORK_DIR}/bastion-host.img \
          -drive format=raw,index=1,file=${WORK_DIR}/cloud-init/cloud-init.img \
          -nic user,hostfwd=tcp::10022-:22

If this command returns an error, you might need to resize the disk size in your bastion host virtual machine image.

You can verify that the configs have been applied successfully once you boot the virtual machine. You will see output similar to the following in the `auditd` logs:
    
    
    [   52.659013] cloud-init[615]: Cloud-init v. 20.4.1 finished at Fri, 28 Apr 2023 18:53:55 +0000.
    

You can also manually examine its user accounts and `sshd` configuration to verify them.

### Import the bastion host virtual machine image

Before you import the fully configured bastion host virtual machine image into your deployment infrastructure, you must snapshot it using the `qemu-img` tool as follows:
    
    
    qemu-img snapshot -c installed bastion-image.img

Follow the processes established by your organization to import the bastion host virtual machine image into your deployment infrastructure.

## Configure the bastion host virtual machine

Follow the steps in this section to configure a bastion host virtual machine.

### Configure the required user accounts

The bastion host feature of Distributed Cloud connected requires one or more user accounts in each of the following categories:

  * **Management**. This is the administrator account for the bastion host virtual machine. It has root access.
  * **Host user**. This is the operations engineer account. It can start and manage terminal multiplexer sessions for Google Support, but cannot enter any commands into those sessions.
  * **Guest user**. This is the Google Support engineer account. It can establish an SSH connection within a terminal multiplexer session shared with your operations engineer on a bastion host virtual machine. It has no other privileges.
  * **Joint user**. This account establishes the terminal multiplexer session on the bastion host virtual machine. Your operations engineer and a Google support engineer jointly connect to this session.



### Configure certificates

You must configure certificates that allow the accounts described in the previous section to access the bastion host virtual machine. The bastion host software package includes a script named `generate-cloud-init.py` that generates the required `cloud-init` configuration with the required accounts, SSH keys, and certificates for each account. 

For instructions, see Generate the `cloud-init` configs.

### Configure logging

Bastion host logs are available in real-time and on-demand from the `audit` daemon. You can manage your logging configuration through the `auditd.conf` file. You are responsible for rotating and exporting logs from bastion host virtual machines based on your business requirements. You must also maintain adequate disk space to store them on the virtual machine.

## Test your configuration

Complete the steps in this section to test your bastion host virtual machine deployment, including connectivity from both ends, and proper access control for the required user accounts. We also recommend that you work then work with Google Support to perform live testing.

### Test your deployment locally

  1. Verify that you can establish an SSH session as `host-user` with your bastion host virtual machine. If this fails, check your SSH keys and certificates.

  2. Verify that you can start a terminal multiplexer session using the following command:
         
         ./opt/create-shared-tmux-session

  3. Verify that your Distributed Cloud connected deployment is reachable from the bastion host virtual machine using the following command:
         
         ssh -vv bastion-user@TARGET_ADDRESS

Replace `TARGET_ADDRESS` with the IP address of the target Distributed Cloud machine or ToR switch.

The request will be rejected by SSH authentication, but the SSH transport and authentication requests must still reach your Distributed Cloud connected deployment. If this fails, check your firewall configuration.

  4. Verify that both Access Transparency and Access Approval have been enabled on your Google Cloud organization and target project as described earlier in this guide.




### Test your deployment live with Google Support

After you have successfully tested your bastion host deployment locally, contact Google Support to schedule a live testing session. Prior to the session, Google Support will send you an Access Approval request. During the live testing session, you and Google will cover the following:

  * Access Approval request generation and approval.
  * End-to-end access workflow for your bastion host deployment.
  * Access Approval and Access Transparency logs.
  * How to troubleshoot the following scenarios: 
    * Google attempting to connect to a bastion host instance not specified in an Access Approval request.
    * Google attempting to connect to a bastion host instance when you haven't started a terminal multiplexer session.
    * Google attempting to connect to a bastion host instance after the corresponding Access Approval request has been denied or revoked.
    * You disconnecting from or terminating the terminal multiplexer session.



## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/deploy)
  * [Manage machines](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/machines)
  * [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/clusters)
  * [Create and manage networks](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/networks)
  * [Create and manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/nodepools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
