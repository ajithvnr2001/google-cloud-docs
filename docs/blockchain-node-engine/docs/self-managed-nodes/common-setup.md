---
url: https://docs.cloud.google.com/blockchain-node-engine/docs/self-managed-nodes/common-setup/
title: Common self-managed node setup \u00a0|\u00a0 Blockchain Node Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:12.093356+00:00
---

# Common self-managed node setup  |  Blockchain Node Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/blockchain-node-engine/docs/self-managed-nodes/common-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Blockchain Node Engine ](https://docs.cloud.google.com/blockchain-node-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/blockchain-node-engine/docs/overview)



Send feedback 

#  Common self-managed node setup Stay organized with collections  Save and categorize content based on your preferences. 

This page contains best practices for running RPC nodes across multiple blockchain networks.

Specifically, this tutorial will walk you through:

  * Creating a new VPC for your node.
  * Spinning up a VM for your node.
  * Setting up a new profile for your node manager.
  * Mounting an external disk to the VM for the chain data.



**This guide assumes you already have a Google Cloud project with billing enabled.** For instructions on how to do this, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

## Create a new VPC

For detailed instructions on VPC creation, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  1. Create a VPC for your node following these recommendations:

     * Create a custom VPC
     * Regional routing mode
     * MTU 1460
     * Enable the default `BLOCKCHAIN_VPC_NETWORK-allow-ssh` firewall rule for your network. See [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-ssh) for more. 

Replace `BLOCKCHAIN_VPC_NETWORK` with the name of the VPC that will hold your node resources, for example `ethereum-vpc`.

  2. [Add an IPv4 subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) for your network. **Make sure the region chosen for your subnet is the same region where you want to deploy your node.**


**Note:** Refer to VPC and networking requirements in each blockchain-specific node page to see the required ports you need to enable for the VMs in the VPC.

To learn how to create firewall rules VMs in a VPC, see [Create VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules).

## Spin up a VM with an external SSD

For detailed instructions on VM creation and external disk attachment, [see the Compute Engine documentation](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#create_a_vm_instance_with_additional_non-boot_disks).

Specific instructions for the VM shape that matches the specific requirements for the blockchain network can be found under the `Hardware Requirements and Recommended Machine Type` section in the blockchain-specific node page. Refer to the blockchain-specific documentation to see the CPU and memory requirements, recommended VM shape for your node, and creation commands for your node.

## Connect to the VM using SSH and create a new user

### Connect to the VM using SSH

  1. When the VM is provisioned, connect to the VM using SSH by either navigating to the compute engine page, or by running the following command in [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell):
         
         gcloud compute ssh NODE_NAME
         

Replace NODE_NAME with the name of your node. Use lowercase letters, numbers, and hyphens. For example: `my-node`.

  2. If connecting from your own machine, install the Google Cloud CLI as described in [Install the gcloud CLI](https://cloud.google.com/sdk/docs/install).

  3. When the Google Cloud CLI installation is complete, login to your project and connect to the VM:
         
         gcloud init
         gcloud compute ssh USER@NODE_NAME
         

Replace USER with your Google Cloud user login name.




### Create a new user

Once you have connected to the VM via SSH, create a non-SSH sudo user to own and administrate all the resources for the node. Since this user does not have SSH keys in the VM metadata, it can only be accessed by connecting to the machine first via one of the authenticated Google Cloud users.

  1. Create a new sudo user, run:
         
         sudo useradd -m NODE_ADMIN
         

Replace NODE_ADMIN with the user ID of the new user. For example, `node-admin`.

  2. Add the user to the sudo group:
         
         sudo usermod -aG sudo NODE_ADMIN
         

  3. Switch to this user to finish mounting the external disk:
         
         sudo su - NODE_ADMIN
         




## Mount the external disks

The external disk you created in step 2 will house all the chain data for your node. This is a best practice since it allows you to port the data across nodes once the VM is shutdown, as well as [easily configure snapshot schedules](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots) for your chain data.

  1. Mount your disk, first list all the available disks in the VM:
         
         sudo lsblk
         

Most likely, the external disk will be found under `/dev/sdb`. You can tell the external disk by the size of the disk you create in step 2.

  2. Format the disk:
         
         sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb
         

  3. Create a directory for the disk and mount it:
         
         sudo mkdir -p /mnt/disks/CHAIN_DATA_NAME
         sudo mount -o discard,defaults /dev/sdb /mnt/disks/CHAIN_DATA_NAME
         

Replace the following:

     * CHAIN_DATA_NAME: the name of the data directory for your chain. For example, `my-eth-data`.
     * /dev/sdb: the location of the disk if different than `/dev/sdb`.
  4. Assign write privileges to `NODE_ADMIN`:
         
         sudo chmod a+w /mnt/disks/CHAIN_DATA_NAME
         

  5. Get the UUID of the disk and add it to `fstab` for automatic remounting on restart:
         
         sudo blkid /dev/sdb
         export DISK_UUID=$(findmnt -n -o UUID /dev/sdb)
         echo "UUID=$DISK_UUID /mnt/disks/CHAIN_DATA_NAME ext4 discard,defaults,nofail 0 2" | sudo tee -a /etc/fstab
         

  6. Your disk is now mounted and ready. To check your mounted disk, run:
         
         df -h
         




## What's next?

The skeleton of your node is ready to go. By this point, you should have:

  * A VPC for your node with SSH access enabled.
  * A VM fitted to the requirements of your node.
  * A new node admin user to own and manage node resources.
  * A mounted external SSD disk fitted to the storage requirements of your node.



Make sure to go back to the blockchain-specific documentation to finish running the deployment commands for your node. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
