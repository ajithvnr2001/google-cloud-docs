---
url: https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine/
title: Connect from Compute Engine \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:30.293486+00:00
---

# Connect from Compute Engine  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/connect-from-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Connect from Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This guide gives instructions on creating a single Compute Engine client and connecting it to your Google Cloud Managed Lustre instance. Managed Lustre supports connections from up to 20,000 clients.

For better performance, client Compute Engine VMs should be created in the same zone as the Managed Lustre instance.

## Required permissions

You must have the following IAM roles:

  * Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`) to create a Compute Engine VM.

  * Compute Admin (`roles/compute.admin`) or Compute Security Admin (`roles/compute.securityAdmin`) to create a firewall rule.

  * IAP-Secured Tunnel User (`roles/iap.tunnelResourceAccessor`) to SSH to a Compute Engine VM using Identity-Aware Proxy.




For a full list of the permissions granted by each role, see the [IAM roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1).

## Limitations

Managed Lustre can't be mounted on [Shielded VMs](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm).

## Create a Compute Engine VM

Follow the instructions to create a Compute Engine VM using one of the following Google Cloud [image families](https://docs.cloud.google.com/compute/docs/images#os-compute-support):

  * Rocky Linux 8
  * Rocky Linux 9
  * Red Hat Enterprise Linux (RHEL) 9
  * Ubuntu 20.04 LTS, v20250213 or later. Note that Ubuntu 20.04 has reached [end of support (EOS)](https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol) and cannot be selected from the Google Cloud console.
  * Ubuntu 22.04 LTS, v20250128 or later
  * Ubuntu 24.04 LTS, for [Arm VMs only](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute).



If you're running a custom Ubuntu 22.04 or 24.04 kernel, support for DKMS [is available](https://docs.cloud.google.com/managed-lustre/docs/dkms).

### Machine types, storage, and networking

You can choose any machine type and boot disk supported by your OS image. We recommend at least a `c2-standard-4` machine type.

When selecting storage options:

  * Ensure you select a disk type supported by your machine series. 4th-generation machine families such as `c4`, `c4a`, or `n4`, require `hyperdisk-balanced` or another [Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#when-to-use). Standard machine families such as `c2d`, `c2`, or `n2`, use `pd-balanced` or another [Persistent Disk type](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types).



To obtain the best network throughput, consider your machine type and vCPU count. In general:

  * Increase the number of vCPUs. Per-instance maximum egress bandwidth is generally 2 Gbps per vCPU, up to the machine type maximum.
  * Select a machine series that supports higher ingress and egress limits. For example, C2 instances with Tier_1 networking support up to 100Gbps egress bandwidth, while C3 instances support up to 200Gbps.
  * Enable [per VM Tier_1 networking performance](https://cloud.google.com/blog/products/compute/increasing-bandwidth-to-compute-engine-vms-with-tier_1-networking) with larger machine types. Not all machine types support Tier_1 networking. If your selected machine type doesn't support it, omit the Tier_1 configuration option.
  * Select a machine series with multiple physical network interface cards (NICs) to aggregate network bandwidth. Physical NICs must be attached to regular VPCs, not VPCs with RDMA network profiles, in order to increase bandwidth. See [Networking and GPU machines](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth) for additional details.



For detailed information, refer to [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).

### Create the VM

###  Google Cloud console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. Click **Create instance**.

  4. Enter a name for your VM in **Name**. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  5. Select the **Region** and **Zone** from the drop-down menus for this VM. Your VM should be in the same zone as your Managed Lustre instance.

  6. Select a **Machine configuration** for your VM from the list.

  7. Click **OS and storage** in the left nav.

  8. Under **Operating system and storage** , click **Change**.

  9. From the **Operating system** drop-down, select one of:

     * **HPC VM image** for Rocky 8
     * **Rocky Linux** for Rocky 9
     * **Red Hat Enterprise Linux** for RHEL 9
     * **Ubuntu** for Ubuntu 22.04 LTS or 24.04 LTS
  10. From the **Version** drop-down, select one of:

     * **HPC Rocky Linux 8**
     * **Rocky Linux 9**
     * **Red Hat Enterprise Linux 9**
     * **Ubuntu 22.04 LTS**
     * **Ubuntu 24.04 LTS**

Select either the x86/64 version or the Arm64 version to match your machine type. Ubuntu 24.04 LTS is only supported on [Arm VMs](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute).

  11. Select a **Disk type** compatible with your machine series, such as `Hyperdisk Balanced` for 4th-generation machine families like `c4a` or `Balanced Persistent Disk` for standard families like `c2d`, then click **Select**.

  12. From the left nav, click **Networking**.

  13. Select the VPC network you created in [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc) and the primary subnet (`SUBNET_NAME`) as the primary interface.

  14. (Optional) For Multi-NIC, click **Add network interface** and select the same VPC network and a different subnet (e.g., `SUBNET_NAME_2`).

  15. (Optional) To enable Tier_1 networking, under **Network performance configurations** , set **Network bandwidth tier** to **Tier 1**. If Tier_1 networking is not supported for your chosen machine type, leave this at the default setting.

  16. From the left nav, click **Security**.

  17. Under **Access scopes** , select **Allow full access to all Cloud APIs**.

  18. From the left nav, click **Advanced**.

  19. Under **Automation** , enter the following in the **Startup script** field:
         
         #!/bin/bash
         sudo apt-get update
         sudo apt-get install -y lustre-client-modules-$(uname -r)
         

This script ensures that the Lustre client packages are updated if the Ubuntu kernel is upgraded. 

  20. To create and start the VM, click **Create**.




###  gcloud 

Use the `gcloud` command line tool to create a VM. When customizing the commands:

  * If your machine type doesn't support Tier_1 networking, omit `--network-performance-configs=total-egress-bandwidth-tier=TIER_1` from the command.
  * Set `type=hyperdisk-balanced` for 4th-generation machine types such as `c4a` or `n4`, or `type=pd-balanced` for standard machine types such as `c2d` or `c2`.




### HPC Rocky Linux 8

Create a VM using the `gcloud compute instances create` command. You can update the machine type and any disk specifications before running the command.
    
    
    gcloud compute instances create VM_NAME \
      --project=PROJECT_ID \
      --zone=LOCATION \
      --machine-type=c2d-standard-112 \
      --scopes="https://www.googleapis.com/auth/cloud-platform" \
      --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
      --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
      --create-disk=auto-delete=yes,boot=yes,device-name=VM_NAME,\
    image-project=cloud-hpc-image-public,image-family=hpc-rocky-linux-8,\
    mode=rw,size=100,type=pd-balanced
    

If your Compute Engine machine type has multiple physical network interface cards (NICs), assign each NIC to a subnet. This lets you aggregate bandwidth across multiple network interfaces.

To do so, add an additional `--network-interface` flag for each additional NIC, and specify a different subnet. See [Create additional subnets for multi-NIC](https://docs.cloud.google.com/managed-lustre/docs/vpc#multi-nic-vpc) for details.
    
    
    ...
    --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
    --network-interface=subnet=SUBNET_NAME_2,no-address,nic-type=GVNIC \
    ...

### Rocky Linux 9

Create a VM using the `gcloud compute instances create` command. You can update the machine type and any disk specifications before running the command.
    
    
    gcloud compute instances create VM_NAME \
      --project=PROJECT_ID \
      --zone=LOCATION \
      --machine-type=c2d-standard-112 \
      --scopes="https://www.googleapis.com/auth/cloud-platform" \
      --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
      --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
      --create-disk=auto-delete=yes,boot=yes,device-name=VM_NAME,\
    image-project=rocky-linux-cloud,image-family=rocky-linux-9,\
    mode=rw,size=100,type=pd-balanced
    

If your Compute Engine machine type has multiple physical network interface cards (NICs), assign each NIC to a subnet. This lets you aggregate bandwidth across multiple network interfaces.

To do so, add an additional `--network-interface` flag for each additional NIC, and specify a different subnet. See [Create additional subnets for multi-NIC](https://docs.cloud.google.com/managed-lustre/docs/vpc#multi-nic-vpc) for details.
    
    
    ...
    --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
    --network-interface=subnet=SUBNET_NAME_2,no-address,nic-type=GVNIC \
    ...

### RHEL 9

Create a VM using the `gcloud compute instances create` command. You can update the machine type and any disk specifications before running the command.
    
    
    gcloud compute instances create VM_NAME \
      --project=PROJECT_ID \
      --zone=LOCATION \
      --machine-type=c2d-standard-112 \
      --scopes="https://www.googleapis.com/auth/cloud-platform" \
      --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
      --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
      --create-disk=auto-delete=yes,boot=yes,device-name=VM_NAME,\
    image-project=rhel-cloud,image-family=rhel-9,\
    mode=rw,size=100,type=pd-balanced
    

If your Compute Engine machine type has multiple physical network interface cards (NICs), assign each NIC to a subnet. This lets you aggregate bandwidth across multiple network interfaces.

To do so, add an additional `--network-interface` flag for each additional NIC, and specify a different subnet. See [Create additional subnets for multi-NIC](https://docs.cloud.google.com/managed-lustre/docs/vpc#multi-nic-vpc) for details.
    
    
    ...
    --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
    --network-interface=subnet=SUBNET_NAME_2,no-address,nic-type=GVNIC \
    ...

### Ubuntu 20.04 LTS

**Note:** Ubuntu 20.04 has reached [end of support (EOS)](https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol).

Create a VM using the `gcloud compute instances create` command. You can update the machine type and any disk specifications before running the command.
    
    
    gcloud compute instances create VM_NAME \
      --project=PROJECT_ID \
      --zone=LOCATION \
      --machine-type=c2d-standard-112 \
      --scopes="https://www.googleapis.com/auth/cloud-platform" \
      --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
      --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
      --create-disk=auto-delete=yes,boot=yes,device-name=VM_NAME,\
    image=projects/ubuntu-os-cloud/global/images/ubuntu-2004-focal-v20250606,\
    mode=rw,size=100,type=pd-balanced \
      --metadata=startup-script='#!/bin/bash
        sudo apt-get update
        sudo apt-get install -y lustre-client-modules-$(uname -r)'
    

If your Compute Engine machine type has multiple physical network interface cards (NICs), assign each NIC to a subnet. This lets you aggregate bandwidth across multiple network interfaces.

To do so, add an additional `--network-interface` flag for each additional NIC, and specify a different subnet. See [Create additional subnets for multi-NIC](https://docs.cloud.google.com/managed-lustre/docs/vpc#multi-nic-vpc) for details.
    
    
    ...
    --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
    --network-interface=subnet=SUBNET_NAME_2,no-address,nic-type=GVNIC \
    ...

### Ubuntu 22.04 LTS

Create a VM using the `gcloud compute instances create` command. You can update the machine type and any disk specifications before running the command.
    
    
    gcloud compute instances create VM_NAME \
      --project=PROJECT_ID \
      --zone=LOCATION \
      --machine-type=c2d-standard-112 \
      --scopes="https://www.googleapis.com/auth/cloud-platform" \
      --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
      --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
      --create-disk=auto-delete=yes,boot=yes,device-name=VM_NAME,\
    image-project=ubuntu-os-cloud,image-family=ubuntu-2204-lts,\
    mode=rw,size=100,type=pd-balanced \
      --metadata=startup-script='#!/bin/bash
        sudo apt-get update
        sudo apt-get install -y lustre-client-modules-$(uname -r)'
    

If your Compute Engine machine type has multiple physical network interface cards (NICs), assign each NIC to a subnet. This lets you aggregate bandwidth across multiple network interfaces.

To do so, add an additional `--network-interface` flag for each additional NIC, and specify a different subnet. See [Create additional subnets for multi-NIC](https://docs.cloud.google.com/managed-lustre/docs/vpc#multi-nic-vpc) for details.
    
    
    ...
    --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
    --network-interface=subnet=SUBNET_NAME_2,no-address,nic-type=GVNIC \
    ...

### Ubuntu 24.04 LTS

Create a VM using the `gcloud compute instances create` command.

Managed Lustre only supports Ubuntu 24.04 LTS on [Arm VMs](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute).

You can update the machine type and any disk specifications before running the command.
    
    
    gcloud compute instances create VM_NAME \
      --project=PROJECT_ID \
      --zone=LOCATION \
      --machine-type=c4a-standard-32 \
      --scopes="https://www.googleapis.com/auth/cloud-platform" \
      --network-interface=network-tier=PREMIUM,nic-type=GVNIC,stack-type=IPV4_ONLY,subnet=SUBNET_NAME \
      --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
      --create-disk=auto-delete=yes,boot=yes,device-name=VM_NAME,\
    image-project=ubuntu-os-cloud,image-family=ubuntu-2404-lts-arm64,mode=rw,size=100,type=hyperdisk-balanced
    

If your Compute Engine machine type has multiple physical network interface cards (NICs), assign each NIC to a subnet. This lets you aggregate bandwidth across multiple network interfaces.

To do so, add an additional `--network-interface` flag for each additional NIC, and specify a different subnet. See [Create additional subnets for multi-NIC](https://docs.cloud.google.com/managed-lustre/docs/vpc#multi-nic-vpc) for details.
    
    
    ...
    --network-interface=stack-type=IPV4_ONLY,subnet=SUBNET_NAME,nic-type=GVNIC \
    --network-interface=subnet=SUBNET_NAME_2,no-address,nic-type=GVNIC \
    ...

For more information about available options, see the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#startinstancegcloud).

## Create a firewall rule allowing SSH

To SSH to your Compute Engine VM, you must first create a firewall rule allowing access to TCP port 22 on your VM.

### VMs without public IPs

When SSHing to VMs without external IPs, both the Google Cloud console SSH button and `gcloud compute ssh` use [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) to connect.

For these connections, follow the instructions in Create the firewall rule to create a firewall rule allowing ingress from the IAP source range only, which is always `35.235.240.0/20`. This enhances security by not exposing port 22 to the broader internet.

### VMs with public IPs

If you've assigned a public IP to your Compute Engine VM, the Google Cloud console SSH button might attempt a direct connection, bypassing IAP.

The source IP for this direct connection is not the IAP range, but one of a large pool of Google IP addresses. Allowing this connection requires a broader source address range, for example `0.0.0.0/0` (any source).

If your VM has a public IP, we recommend that you configure your firewall rule to allow SSH from the IAP range (`35.235.240.0/20`) only. Then use `gcloud compute ssh` to connect, specifying the `--tunnel-through-iap` flag.

If you must assign a public IP **and** connect from the Google Cloud console, specify `0.0.0.0/0` as the value of the source IPv4 range.

### Create the firewall rule

###  Google Cloud console 

Create a firewall rule allowing SSH.

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies)

  2. Click **Create firewall rule**.

  3. Enter a **Name** for the rule.

  4. For **Network** , select the VPC network you created earlier.

  5. Select **Ingress** as the **Direction of traffic** , and **Allow** as the **Action on match**.

  6. From the **Targets** drop-down, select **All instances in the network**.

  7. In the **Source IPv4 ranges** field, enter `35.235.240.0/20`.

  8. From **Protocols and ports** , select **Specified protocols and ports**.

  9. Select **TCP** and enter `22` in the **Ports** field.

  10. Click **Create**.




###  gcloud 

Create a firewall rule allowing SSH.
    
    
    gcloud compute firewall-rules create FIREWALL_RULE_NAME \
      --allow=tcp:22 \
      --network=NETWORK_NAME \
      --source-ranges=35.235.240.0/20 \
      --project=PROJECT_ID
    

## SSH to your Compute Engine VM

Once the firewall rule is created, you can SSH to your VM:

###  Google Cloud console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the instances table, find your instance's row, and click **SSH** in the column titled **Connect**.

  3. If prompted to do so, click **Authorize** to allow the connection.




###  gcloud 
    
    
    gcloud compute ssh VM_NAME \
      --zone=LOCATION \
      --project=PROJECT_ID \
      --tunnel-through-iap
    

## Install the Lustre client packages

The Lustre client packages are hosted in the `lustre-client-binaries` project in Artifact Registry.

### Configure access to the repository

To configure your VM to install from Artifact Registry, follow these instructions.

### HPC Rocky Linux 8

Run `gcloud beta artifacts print-settings` and pipe the output to bash to run the required commands:
    
    
    gcloud beta artifacts print-settings yum \
      --repository=lustre-client-rocky-8 \
      --location=us --project=lustre-client-binaries | sudo bash
    

### Rocky Linux 9

Run `gcloud beta artifacts print-settings` and pipe the output to bash to run the required commands:
    
    
    gcloud beta artifacts print-settings yum \
      --repository=lustre-client-rocky-9 \
      --location=us --project=lustre-client-binaries | sudo bash
    

### RHEL 9

Run `gcloud beta artifacts print-settings` and pipe the output to bash to run the required commands:
    
    
    gcloud beta artifacts print-settings yum \
      --repository=lustre-client-rocky-9 \
      --location=us --project=lustre-client-binaries | sudo bash
    

RHEL 9 uses the same `lustre-client-rocky-9` repository as Rocky Linux 9.

### Ubuntu 20.04 LTS

  1. Install the Apt repository signing keys:
         
         curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/google-cloud.gpg
         curl -fsSL https://us-apt.pkg.dev/doc/repo-signing-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/lustre-client.gpg
         

  2. Configure your VM to access Artifact Registry packages:
         
         echo 'deb [signed-by=/usr/share/keyrings/google-cloud.gpg] http://packages.cloud.google.com/apt apt-transport-artifact-registry-stable main' \
           | sudo tee /etc/apt/sources.list.d/artifact-registry.list
         

  3. Update Apt and install the `apt-transport-artifact-registry` package:
         
         sudo apt update && sudo apt install apt-transport-artifact-registry
         

  4. Configure Apt to fetch packages from the repository:
         
         echo "deb [signed-by=/usr/share/keyrings/lustre-client.gpg] ar+https://us-apt.pkg.dev/projects/lustre-client-binaries lustre-client-ubuntu-focal main" \
           | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
         

  5. Update your repository sources:
         
         sudo apt update
         

If the command returns an error, ensure that your Compute Engine VM was created with the access scope allowing full access to all Cloud APIs. See [Granting access to Compute Engine instances](https://docs.cloud.google.com/artifact-registry/docs/access-control#compute) for more details.




More information about these commands is available in the Artifact Registry documentation: [Configure VMs to install Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure).

### Ubuntu 22.04 LTS

  1. Install the Apt repository signing keys:
         
         curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/google-cloud.gpg
         curl -fsSL https://us-apt.pkg.dev/doc/repo-signing-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/lustre-client.gpg
         

  2. Configure your VM to access Artifact Registry packages:
         
         echo 'deb [signed-by=/usr/share/keyrings/google-cloud.gpg] http://packages.cloud.google.com/apt apt-transport-artifact-registry-stable main' \
           | sudo tee /etc/apt/sources.list.d/artifact-registry.list
         

  3. Update Apt and install the `apt-transport-artifact-registry` package:
         
         sudo apt update && sudo apt install apt-transport-artifact-registry
         

  4. Configure Apt to fetch packages from the repository:
         
         echo "deb [signed-by=/usr/share/keyrings/lustre-client.gpg] ar+https://us-apt.pkg.dev/projects/lustre-client-binaries lustre-client-ubuntu-jammy main" \
           | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
         

  5. Update your repository sources:
         
         sudo apt update
         

If the command returns an error, ensure that your Compute Engine VM was created with the access scope allowing full access to all Cloud APIs. See [Granting access to Compute Engine instances](https://docs.cloud.google.com/artifact-registry/docs/access-control#compute) for more details.




More information about these commands is available in the Artifact Registry documentation: [Configure VMs to install Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure).

### Ubuntu 24.04 LTS

  1. Install the Apt repository signing keys:
         
         curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/google-cloud.gpg
         curl -fsSL https://us-apt.pkg.dev/doc/repo-signing-key.gpg \
           | sudo gpg --dearmor -o /usr/share/keyrings/lustre-client.gpg
         

  2. Configure your VM to access Artifact Registry packages:
         
         echo 'deb [signed-by=/usr/share/keyrings/google-cloud.gpg] http://packages.cloud.google.com/apt apt-transport-artifact-registry-stable main' \
           | sudo tee /etc/apt/sources.list.d/artifact-registry.list
         

  3. Update Apt and install the `apt-transport-artifact-registry` package:
         
         sudo apt update && sudo apt install apt-transport-artifact-registry
         

  4. Configure Apt to fetch packages from the repository:
         
         echo "deb [signed-by=/usr/share/keyrings/lustre-client.gpg] ar+https://us-apt.pkg.dev/projects/lustre-client-binaries lustre-client-ubuntu-noble main" \
           | sudo tee -a /etc/apt/sources.list.d/artifact-registry.list
         

  5. Update your repository sources:
         
         sudo apt update
         

If the command returns an error, ensure that your Compute Engine VM was created with the access scope allowing full access to all Cloud APIs. See [Granting access to Compute Engine instances](https://docs.cloud.google.com/artifact-registry/docs/access-control#compute) for more details.




More information about these commands is available in the Artifact Registry documentation: [Configure VMs to install Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure).

### Install the Lustre client packages

Follow the instructions to install the Lustre client packages.

### HPC Rocky Linux 8
    
    
    sudo yum -y --enablerepo=lustre-client-rocky-8 install kmod-lustre-client
    sudo yum -y --enablerepo=lustre-client-rocky-8 install lustre-client
    

### Rocky Linux 9
    
    
    sudo yum -y --enablerepo=lustre-client-rocky-9 install kmod-lustre-client
    sudo yum -y --enablerepo=lustre-client-rocky-9 install lustre-client
    

### RHEL 9
    
    
    sudo yum -y --enablerepo=lustre-client-rocky-9 install kmod-lustre-client
    sudo yum -y --enablerepo=lustre-client-rocky-9 install lustre-client
    

### Ubuntu 20.04 LTS

Run the following commands.
    
    
    sudo apt install lustre-client-modules-$(uname -r)/lustre-client-ubuntu-focal
    
    
    
    sudo apt install lustre-client-utils/lustre-client-ubuntu-focal
    

The Lustre client packages are kernel version-specific. If you didn't include the startup script when creating your Compute Engine instance, and your Ubuntu kernel version changes due to an automatic kernel update, you must re-run these commands to download the appropriate Lustre client packages.

### Ubuntu 22.04 LTS

Run the following commands.
    
    
    sudo apt install lustre-client-modules-$(uname -r)/lustre-client-ubuntu-jammy
    
    
    
    sudo apt install lustre-client-utils/lustre-client-ubuntu-jammy
    

The Lustre client packages are kernel version-specific. If your Ubuntu kernel version changes due to an automatic kernel update, you must re-run these commands to download the appropriate Lustre client packages.

### Ubuntu 24.04 LTS

Run the following commands.
    
    
    sudo apt install lustre-client-modules-$(uname -r)/lustre-client-ubuntu-noble
    
    
    
    sudo apt install lustre-client-utils/lustre-client-ubuntu-noble
    

The Lustre client packages are kernel version-specific. If you didn't include the startup script when creating your Compute Engine instance, and your Ubuntu kernel version changes due to an automatic kernel update, you must re-run these commands to download the appropriate Lustre client packages.

### Load the Lustre kernel module

After the client packages are installed, follow these instructions to load the Lustre kernel module.

###  Standard configuration 

Run the following command:
    
    
    sudo modprobe lustre
    

###  Multi-NIC configuration 

If your VM has multiple NICs, each connected to a different subnet, you must configure LNet to use them before loading the module.

  1. Create or modify the `/etc/modprobe.d/lustre.conf` file:
         
         options lnet networks="tcp0(eth0, eth1)"
         

This example assumes that the interfaces on the VM are named `eth0` and `eth1`. Replace these with the correct corresponding interface names. You can see the interface names by running the `ip address` command.

  2. Load the module:
         
         sudo modprobe lustre
         

  3. (Optional) Verify TCP tuning. Run the following command:
         
         sudo lctl list_nids
         

The output shows both NICs.




### (Optional) Configure LNet for `gke-support-enabled` instances

This section applies only to Compute Engine clients connecting to Managed Lustre instances with the deprecated `--gke-support-enabled` flag specified.

If your Managed Lustre instance wasn't created with the **GKE support** option, skip this section.

#### Configure LNet to use `accept_port` 6988

If your Managed Lustre instance has the deprecated `--gke-support-enabled` set to true and you're connecting from a Compute Engine VM:

  1. Create or edit `/etc/modprobe.d/lnet.conf`.
  2. Add the following line: 
         
         options lnet accept_port=6988
         

  3. Reboot the VM: 
         
         sudo reboot
         




## Mount a Managed Lustre instance

Mount the Managed Lustre instance.

  * For a quick mount that doesn't need to persist across reboots, use the `mount` command.

  * To automatically mount each time your VM boots, use the `/etc/fstab` option.




In both cases, the directory to use as the mount point must exist before you run the command.

To retrieve the IP address and file system name for your instance, use the `gcloud lustre instances describe` command, or visit the [Instances](https://console.cloud.google.com/managed-lustre/) page in the Google Cloud console.
    
    
    gcloud lustre instances describe INSTANCE_NAME \
      --location=ZONE
    

###  `mount`

From your Compute Engine VM's command line, use the `mount` command to manually mount the Managed Lustre instance:
    
    
    sudo mkdir -p ~/MOUNT_DIR
    sudo mount -t lustre IP_ADDRESS:/FILESYSTEM_NAME ~/MOUNT_DIR
    

Where:

  * IP_ADDRESS is the IP address of your Managed Lustre instance.

  * FILESYSTEM_NAME is the file system name of your instance.

  * ~/MOUNT_DIR is the local mount point directory you created.




###  `/etc/fstab`

From your Compute Engine VM's command line:

  1. Create a local directory for the mount point:
         
         sudo mkdir -p ~/MOUNT_DIR
         

  2. Open the `/etc/fstab` file for editing and add the following line:
         
         IP_ADDRESS@tcp:/FILESYSTEM_NAME ~/MOUNT_DIR lustre defaults,_netdev 0 0
         

Where:

     * IP_ADDRESS is the IP address of your Managed Lustre instance.

     * FILESYSTEM_NAME is the file system name of your instance.

     * ~/MOUNT_DIR is the local mount point directory you created.

     * `lustre defaults,_netdev 0 0` are the recommended mount options:

       * `lustre` specifies the file system type as Lustre.
       * `defaults` uses the default set of mount options.
       * `_netdev` directs the system to wait for network connectivity before attempting to mount the file system.
       * `0 0` controls dumping and file system check order.
  3. Save and exit the `/etc/fstab` file.

  4. Run the following command to mount all file systems listed in `/etc/fstab`:
         
         sudo mount -a
         




Your Managed Lustre instance is now mounted. It will be automatically mounted each time your Compute Engine VM boots up.

If the mount command fails, see the [Troubleshooting](https://docs.cloud.google.com/managed-lustre/docs/troubleshooting-client-connections) instructions to diagnose the problem.

## Advanced networking configurations

The following sections describe advanced networking configurations.

### Using a secondary NIC

If you are mounting the Managed Lustre instance using a secondary NIC of a Compute Engine instance which has [multiple NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts), use the following instructions.

Note that this is not the same as multi-NIC.

  1. Configure LNET to use the correct NIC.

Copy the contents of `/etc/lnet.conf` to a file named `/etc/modprobe.d/lustre.conf` on the VM. Append the following line to the file, replacing `eth1` with the name of the secondary NIC:
         
         options lnet networks="tcp0(eth1)"
         

Reload the Lustre kernel module:
         
         lustre_rmmod
         modprobe lustre
         

Verify that LNET is configured to use the second NIC. The output of the following command should be the second NIC:
         
         lctl list_nids
         

  2. Add a static route to the Managed Lustre instance's CIDR block via the secondary NIC's gateway.

     * To find the gateway for the secondary NIC, run the `route` command.

     * To find the Managed Lustre instance's CIDR block:

       * Get the instance details by running the `gcloud lustre instances describe` command.
       * Get the address provided in the `mountPoint` field.
       * Convert the IP address to a CIDR block containing it, with a size of 23.

For example, if the Managed Lustre instance's CIDR block is `172.16.0.0/24`, the secondary NIC is `eth1`, and its gateway is `10.130.0.1`, then run the following command:
    
    ip route add 172.16.0.0/24 via 10.130.0.1 dev eth1
    

Note that the added route will not persist if the Compute Engine instance reboots. How to make that persistent will be specific to the specific OS family you are using.




### Multi-NIC routing

Manual routing configuration is required for multi-NIC Compute Engine instances to ensure traffic uses the additional interfaces correctly.

The following steps show how to configure the `eth1` interface. Repeat these steps for every additional NIC on the VM (e.g., `eth2`, `eth3`, etc.).

  1. Set the network interface name, then get its internal IP address and calculate the corresponding gateway IP. The gateway is the `.1` address of the interface's subnet.
         
         IFACE="eth1"
         IFACE_IP=$(ip -4 addr show ${IFACE} | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
         GATEWAY_IP=$(echo ${IFACE_IP} | awk -F. '{print $1"."$2"."$3".1"}')
         

  2. Get the mount point of your Managed Lustre instance, and convert it into a /23 CIDR block:
         
         LUSTRE_MOUNT_IP=$(gcloud lustre instances describe INSTANCE_NAME \
           --location=ZONE --format="value(mountPoint)")
         IFS=. read -r i1 i2 i3 i4 <<< "${LUSTRE_MOUNT_IP}"
         LUSTRE_CIDR="${i1}.${i2}.$((i3 & 254)).0/23"
         

  3. Create a unique routing table for the interface and apply the traffic rules. The value of `TABLE_ID` must be a unique number for each interface. When repeating these steps for additional interfaces, increment `TABLE_ID` by 1. For example, use `102` for eth2, `103` for eth3.
         
         TABLE_ID=101
         sudo ip route add ${LUSTRE_CIDR} via ${GATEWAY_IP} dev ${IFACE} table ${TABLE_ID}
         sudo ip rule add from ${IFACE_IP} table ${TABLE_ID}
         




These routing settings don't persist across reboots. To make them persistent, add them to a startup script or network configuration files.

## Access your Managed Lustre instance

Your Managed Lustre instance is now mounted to your Compute Engine VM and readable/writable using standard POSIX syntax, with [some exceptions](https://docs.cloud.google.com/managed-lustre/docs/posix-compliance).

Run the following command to check your mounted directory:
    
    
    sudo lfs df -h ~/MOUNT_DIR
    

You can test file copy and write with the following commands:
    
    
    # sample file copy/file write
    sudo dd if=/dev/zero of=~/MOUNT_DIR/bigfile1 bs=1M count=8000
    sudo dd if=/dev/urandom of=~/MOUNT_DIR/bigfile1 bs=1M count=1000
    

To confirm disk space usage:
    
    
    sudo lfs df -h ~/MOUNT_DIR
    

## Unmount the instance

The Managed Lustre instance can be unmounted using the following command:
    
    
    sudo umount ~/MOUNT_DIR
    

## What's next

  * [Transfer data to Managed Lustre from Cloud Storage](https://docs.cloud.google.com/managed-lustre/docs/transfer-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
