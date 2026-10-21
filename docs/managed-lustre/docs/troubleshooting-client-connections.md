---
url: https://docs.cloud.google.com/managed-lustre/docs/troubleshooting-client-connections/
title: Troubleshoot client connections \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:49:56.653237+00:00
---

# Troubleshoot client connections  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/troubleshooting-client-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Troubleshoot client connections Stay organized with collections  Save and categorize content based on your preferences. 

When encountering issues mounting or connecting to a Managed Lustre file system on a client VM or instance, follow these steps to diagnose the problem.

## Verify that the Managed Lustre instance is reachable

First, ensure that your Managed Lustre instance is reachable from your client instance:
    
    
    sudo lctl ping IP_ADDRESS@tcp
    

To obtain the value of IP_ADDRESS, see [Get an instance](https://docs.cloud.google.com/managed-lustre/docs/instances#get_an_instance).

A successful ping returns a response similar to the following:
    
    
    12345-0@lo
    12345-10.115.0.3@tcp
    

A failed ping returns the following:
    
    
    failed to ping 10.115.0.3@tcp: Input/output error
    

If your ping fails:

  * Make sure your Managed Lustre instance and your client instance are in the same VPC network. Compare the output of the following commands:
        
        gcloud compute instances describe VM_NAME \
          --zone=VM_ZONE \
          --format='get(networkInterfaces[0].network)'
        
        gcloud lustre instances describe INSTANCE_NAME \
          --location=ZONE --format='get(network)'
        

The output looks like:
        
        https://www.googleapis.com/compute/v1/projects/my-project/global/networks/my-network
        projects/my-project/global/networks/my-network
        

The output of the `gcloud compute instances describe` command is prefixed with `https://www.googleapis.com/compute/v1/`; everything following that string must match the output of the `gcloud lustre instances describe` command.

  * Review your VPC network's firewall rules and routing configurations to ensure they allow traffic between your client instance and the Managed Lustre instance.




## Check the LNet accept port (legacy instances)

Although the `--gke-support-enabled` flag is deprecated and no longer required when creating new Managed Lustre instances, you might have existing older instances that were created with this flag.

If you are connecting to a legacy instance where GKE support was enabled, you must configure LNet on all client Compute Engine instances to use `accept_port` 6988\. See [Configure LNet for `gke-support-enabled` instances](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine#lnet-gke-support-enabled).

To determine whether an existing instance was configured with this legacy flag, run the following command:
    
    
    gcloud lustre instances describe INSTANCE_NAME \
      --location=LOCATION | grep gkeSupportEnabled
    

If the command returns `gkeSupportEnabled: true`, you must configure LNet on your client VMs.

## Ubuntu kernel version mismatch with Lustre client

For Compute Engine instances running Ubuntu, the Ubuntu kernel version must match the specific version of the Lustre client packages. If your Lustre client tools are failing, check whether your Compute Engine instance has auto-upgraded to a newer kernel.

To check your kernel version:
    
    
    uname -r
    

The response looks like:
    
    
    6.8.0-1029-gcp
    

To check your Lustre client package version:
    
    
    dpkg -l | grep -i lustre
    

The response looks like:
    
    
    ii  lustre-client-modules-6.8.0-1029-gcp 2.14.0-ddn198-1  amd64  Lustre Linux kernel module (kernel 6.8.0-1029-gcp)
    ii  lustre-client-utils                  2.14.0-ddn198-1  amd64  Userspace utilities for the Lustre filesystem (client)
    

If there is a mismatch between the kernel version listed from both commands, you must [re-install the Lustre client packages](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine#install_the_lustre_client_packages).

## Check dmesg for Lustre errors

Many Lustre warnings and errors are logged to the Linux kernel ring buffer. The `dmesg` command prints the kernel ring buffer.

To search for Lustre-specific messages, use `grep` in conjunction with `dmesg`:
    
    
    dmesg | grep -i lustre
    

Or, to look for more general errors that might be related:
    
    
    dmesg | grep -i error
    

## Mounting Lustre on a multi-NIC VM fails

When a VM has multiple network interface controllers (NICs), and the Managed Lustre instance is on a VPC connected to a secondary NIC (for example, `eth1`), mounting the instance may fail. To resolve this issue, follow the instructions to [mount using a secondary NIC](https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine#secondary-nic).

## Cannot connect from the 172.17.0.0/16 subnet range

Compute Engine and GKE clients with an IP address in the 172.17.0.0/16 subnet range cannot mount Managed Lustre instances.

## Can't access Managed Lustre from a peered project

If your client VMs or GKE clusters reside in a peered VPC network and cannot connect to your Managed Lustre instance, verify the following:

  * **Network Connectivity Center (NCC) routing:** VPC peering alone does not route traffic to the private services access connection used by Managed Lustre. To connect across peered VPC networks, you must connect both networks through [Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes) (NCC).
  * **Firewall rules:** Ensure that firewall rules in both the host VPC network and the peered VPC network allow TCP traffic on ports `988` and `6988` between client subnets and the allocated IP range (`$CIDR_BLOCK`) of the instance.



For step-by-step setup instructions and `gcloud` commands, see [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).

## Mounting fails on Shielded VMs (Secure Boot)

Managed Lustre can't be mounted on [Shielded VMs](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm). Attempting to load the Lustre kernel module in a Secure Boot environment fails with the error: `ERROR: could not insert 'lustre': Required key not available.`

## Information to include with a support request

If you're unable to resolve the mount failure, gather diagnostic information before creating a support case. You must have SSH access to your client machine to run the commands in this section.

The `sosreport` utility collects system logs and configuration information and generates a compressed tar file.

To generate an sosreport, SSH to your client machine. Then, run:
    
    
    sudo sos report --all-logs --batch --tmp-dir=/var
    

If the command is not found:

###  Rocky Linux & RHEL 

Use the `dnf` package manager to install the `sos` package:
    
    
    sudo dnf install -y sos
    

###  Ubuntu 

Use the `apt` package manager to install the `sosreport` package:
    
    
    sudo apt update
    sudo apt install -y sosreport
    

###  Container-Optimized OS 

Use the `apt` package manager from inside [toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox) to install the `sosreport` package:
    
    
    sudo toolbox
    sudo apt install sosreport -y
    

Attach the `sosreport` archive to your support case.

For more information about the `sosreport` utility, see [Collecting debugging information using sosreport](https://docs.cloud.google.com/container-optimized-os/docs/how-to/sosreport).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
