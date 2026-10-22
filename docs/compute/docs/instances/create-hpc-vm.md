---
url: https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm/
title: Create an HPC-ready VM instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:26.825062+00:00
---

# Create an HPC-ready VM instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an HPC-ready VM instance Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

You can create an HPC-ready VM instance by using the following interfaces:

  * [ **Google Cloud CLI** ](https://docs.cloud.google.com/compute/docs/gcloud-compute)
  * **Google Cloud console**
  * [**SchedMD's Slurm workload manager**](https://cloud.google.com/blog/topics/hpc/introducing-the-latest-slurm-on-gcp-scripts)



To learn about the HPC VM image and Advanced Compute Images, see [Overview of HPC-ready VM images](https://docs.cloud.google.com/compute/docs/images/workload/hpc-vm-images) and [Overview of Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images). 

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).




## Quickstarts

These tutorials describe the steps to set up an HPC-optimized VM instance. The procedures describe how to:

  * Create an HPC VM instance (without configuring Cloud RDMA)
  * Specify a compact placement policy when creating HPC VM instances
  * Create an HPC VM instance that uses Cloud RDMA



You can't add Cloud RDMA to an existing HPC VM instance, so follow the appropriate steps when creating your instance.

### Before you begin

  1. To use the Google Cloud CLI for this quickstart, you must first install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs): 
     * [Download and install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
     * [Initialize the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/initialize).
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.



### Create an HPC VM instance

We strongly recommend using the HPC VM image or [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images) ([Preview](https://cloud.google.com/products#product-launch-stages)) with your HPC workloads using the following machine series:

  * [H4D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series)
  * [H3](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_series)
  * [C2D](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_series)
  * [C2](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2_series)



The machine types in these series have fixed virtual-to-physical core mappings and expose NUMA cell architecture to the guest OS, both of which are critical for performance of tightly-coupled HPC applications.

If you are creating multiple, interconnected HPC VM instances, then follow the instructions at create HPC VM instances with compact placement policies to achieve low network latency.

###  Console 

Use the Google Cloud console to create HPC-ready instances that run an HPC VM image for the guest OS. To use one of the Advanced Compute Images, you must use either gcloud CLI or REST.

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your compute instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     2. Optional: Select a **Region** and **Zone** for the instance.

The default selection for **Zone** is **Any**. If you don't change this default selection, then Google automatically chooses a zone for you based on machine type and availability.

     3. Click the **Compute-optimized** tab. The Google Cloud console then displays the machine series that are available for your selected machine family.

     4. In the **Series** column, select the machine series for your VM, for example **C2**.

     5. In the **Machine type** section, select the machine type for your VM, for example, **c2-standard-60**.

  3. In the navigation menu (on the left side), click **OS and storage**.

  4. In the **Operating system and storage** pane, configure your boot disk by doing the following: 

     1. Click **Change**. The **Boot disk** pane appears and displays the **Public images** tab.
     2. In the **Operating system** list, select **HPC VM Image**.
     3. In the **Version** list, select the OS version.
     4. Optional: In the **Boot disk type** list, select the type of the boot disk.
     5. Optional: In the **Size (GB)** field, specify the size of the boot disk.
     6. Optional: For Hyperdisk Balanced boot disks, specify values for the **Provisioned IOPS** and **Provisioned throughput** fields.
     7. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section.
     8. To confirm your boot disk options and return to the **Operating system and storage** pane, click **Select**.
**Note:** Unless you explicitly choose a different boot disk, if the name you specified for the instance matches the name of an existing disk, then the existing disk automatically attaches to the new instance as the boot disk.
  5. In the navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. Go to the **Firewall** section.
     2. To permit HTTP or HTTPS traffic to the VM, select **Allow HTTP traffic** or **Allow HTTPS traffic**.

The Compute Engine adds a network tag to your VM and creates the corresponding ingress firewall rule that allows all incoming traffic on `tcp:80` (HTTP) or `tcp:443` (HTTPS). The network tag associates the firewall rule with the VM. For more information, see [Firewall rules overview](https://docs.cloud.google.com/firewall/docs/firewalls) in the Cloud Next Generation Firewall documentation.

  6. Optional: If you chose an OS image that supports [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) features, you can modify the Shielded VM settings.

To do so, in the navigation menu, Click **Security**. In the **Security** pane that appears, you can configure the following:

     * To turn on [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot), select the **Turn on Secure Boot** checkbox. Secure Boot is [disabled by default](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).

     * To turn off [vTPM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm), clear the **Turn on vTPM** checkbox. vTPM is [enabled by default](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm). Disabling vTPM also disables [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring) because integrity monitoring relies on data gathered by [Measured Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#measured-boot).

     * To turn off [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring), clear the **Turn on Integrity Monitoring** checkbox. Integrity monitoring is [enabled by default](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).

  7. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  8. Optional: To create the compute instance using reserved resources, in the navigation menu, click **Advanced**. In the **Reservations** section, select **Use automatic selection**. To [consume the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation), make sure the compute instance properties match the properties specified in the reservation.

  9. To create and start the HPC VM instance, click **Create**.




###  gcloud 

Create an HPC VM instance by using the [`instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

To create an HPC VM instance without a placement policy, use a command similar to the following:
    
    
    gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --image-family=IMAGE_FAMILY \
            --image-project=IMAGE_PROJECT \
            --maintenance-policy=TERMINATE \
            --machine-type=MACHINE_TYPE
    

Replace the following:

  * `INSTANCE_NAME`: a name for the HPC VM instance.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) to create the instance in.
  * `IMAGE_FAMILY`: The [image family](https://docs.cloud.google.com/compute/docs/images/workload/hpc-vm-images) of the image to use when creating the VM instances. 
    * For HPC VM images, use either `hpc-rocky-linux-8` or `hpc-rocky-linux-9`
    * For Advanced Compute Images, use one of the image families listed in [Supported hardware and image families](https://docs.cloud.google.com/compute/docs/images/workload/aci-images#aci-families).
  * `IMAGE_PROJECT`: The image project to use when creating VM instances. For HPC VM images, the project is `cloud-hpc-image-public`. For Advanced Compute Images, the project is `advanced-compute-images`.
  * `MACHINE_TYPE`: the machine type to use when creating the VM instance.



After some time, the VM instance creation completes. To verify the instance configuration and to see its status, run the following command:
    
    
    gcloud compute instances describe INSTANCE_NAME
    

###  REST 

Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create a compute instance that uses an HPC VM OS image:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
       "machineType":"zones/ZONE/machineTypes/MACHINE_TYPE",
       "name":"VM_NAME",
       "disks":[
          {
             "initializeParams":{
                "sourceImage":"projects/cloud-hpc-image-public/global/images/IMAGE"
             },
             "boot":true
          }
       ],
       "networkInterfaces":[
          {
             "network":"global/networks/NETWORK_NAME"
          }
       ]
    }
    

Replace the following:

  * `PROJECT_ID`: ID of the project to create the compute instance in
  * `ZONE`: zone to create the compute instance in
  * `MACHINE_TYPE`: machine type, predefined or custom, for the new compute instance
  * `INSTANCE_NAME`: name of the new compute instance
  * `IMAGE_FAMILY`: The image family of the image to use when creating the VM instances. 
    * For HPC VM images, use either `hpc-rocky-linux-8` or `hpc-rocky-linux-9`
    * For Advanced Compute Images, use one of the image families listed in [Supported hardware and image families](https://docs.cloud.google.com/compute/docs/images/workload/aci-images#aci-families).
  * `IMAGE_PROJECT`: The image project to use when creating VM instances. 
    * For HPC VM images, use the project `cloud-hpc-image-public`.
    * For Advanced Compute Images, use the project `advanced-compute-images`.
  * `NETWORK_NAME`: the VPC network that you want to use for the compute instance. You can specify `default` to use your default network.



### Create HPC VM instances with compact placement policies

You can reduce the latency between compute instances by creating a compact placement policy. A compact placement policy ensures that instances in the same availability zone are located close to each other.

If you need more compute instances than can fit in a single compact placement policy, then divide your instances into multiple placement policies. Use the minimum number of placement policies that can fit all your instances.

To create HPC VM instances that specify a compact placement policy, follow these steps:

  1. [Create a compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy).

  2. Do one of the following:

     * [Apply the compact placement policy to an existing HPC VM instance](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#apply-to-vm).

     * [Create an instance that specifies the compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-vm).

To create an instance that specifies a compact placement policy, use the `--maintenance-policy` and `--resource-policies` flags with the `gcloud compute instances create` command.




### Create an HPC VM instance that uses Cloud RDMA

To create an HPC VM instance that uses Cloud RDMA, you must first create at least one regular Virtual Private Cloud (VPC) network and one [Falcon VPC network](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles). The Falcon VPC network uses an RDMA network profile that enables RDMA traffic between compute instances. This network is separate from the regular VPC network that carries non-RDMA traffic to other Google Cloud services or the internet.

To create an HPC VM instance that uses Cloud RDMA, the tasks to complete are as follows:

  1. Identify or create at least two VPC networks:

     * A regular VPC network for the traffic that goes through the gVNIC network interface
     * A Falcon VPC network for the RDMA network traffic
  2. Create an HPC VM instance.

     1. For the source image, use an HPC VM image or a Rocky Linux-based Advanced Compute Images. These images include the drivers needed for Cloud RDMA.
     2. During the instance creation, configure at least two network interfaces—one that uses the gVNIC driver and one that uses the [IRDMA driver](https://docs.cloud.google.com/compute/docs/networking/using-irdma).

For a more complete explanation, see [Create an instance that uses Cloud RDMA](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma).

  3. If you plan to run MPI applications on the HPC VM instances that use Cloud RDMA, then following the MPI configuration steps in [Set up and scale MPI applications on H4D VMs with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application).




### Access the HPC VM instance

After you create the HPC VM instance, it starts automatically. To access the instance, do one of the following:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of your compute instance.

  3. In the **Remote Access** section, click the first drop-down list and choose how you want to access the instance.




Compute Engine propagates your SSH keys and creates your user. For more information, see [Connecting to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

###  gcloud 

To access the instance using SSH, use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh):
    
    
    gcloud compute ssh INSTANCE_NAME --zone ZONE
    

Compute Engine propagates your SSH keys and creates your user. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

### Clean up

To avoid incurring charges to your Google Cloud account for the resources used in these quickstarts, delete any HPC VM instances and all attached resources that you created.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instances that you want to delete.

  3. Click delete **Delete**.

  4. In the dialog, do the following:

     1. Optional: To delete the instances without gracefully shutting them down, or to end an ongoing graceful shutdown, select the **Skip graceful shutdown (if applicable)** checkbox.

     2. To confirm, click **Delete**.

  5. To delete the disks used by the deleted instances, go to the **Disks** page, then perform the following steps:

[Go to Disks](https://console.cloud.google.com/compute/disks)

     1. Select the disks that you want to delete. The disks you select can't have a value in the **In use by** column.

     2. Click delete **Delete**.

     3. To confirm, click **Delete**.




###  gcloud 

To delete one or more instances in the same zone, use the [`gcloud compute instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete). To force the deletion of the disks attached to one or more instances, include the `--delete-disks` flag:
    
    
    gcloud compute instances delete INSTANCE_NAMES \
            --delete-disks=DELETE_DISK_TYPE \
            --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a list of instance names separated by spaces—for example, `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the instances are located.

  * `DELETE_DISK_TYPE`: specify one of the following values:

    * To delete attached boot and non-boot persistent storage: `all`
    * To delete only attached boot persistent storage: `boot`
    * To delete only non-boot persistent storage: `data`



###  REST 

  1. To delete an instance, make a `DELETE` request to the [`instances.delete` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/delete):
         
         DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the instance is located.
     * `ZONE`: the zone of the instance.
     * `INSTANCE_NAME`: the instance name.
  2. To delete a disk used by the instance, make a `DELETE` request to the [`disks.delete` method](https://docs.cloud.google.com/compute/docs/reference/latest/disks/delete):
         
         DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the disk is located.
     * `ZONE`: the zone where the disk is located.
     * `DISK_NAME`: the disk name.
  3. Repeat the previous steps for additional instances or disks.




## Configure your HPC VM instance according to best practices

To get better and more predictable performance for your HPC VM instance, we recommend that you use the following best practices.

### Disable simultaneous multithreading

The HPC VM image and Rocky Linux-based Advanced Compute Images enable simultaneous multithreading (SMT), also known as [Hyper-Threading on Intel processors](https://en.wikipedia.org/wiki/Hyper-threading), by default. Disabling SMT can make your performance more predictable and can decrease job times.

**Note:** For H4D and H3 instances, SMT is disabled by default.

You can use the following methods to disable SMT:

  * To disable SMT while creating a new HPC VM instance, follow the steps to create an HPC VM instance and include the flag  
`--threads-per-core=1`.

  * To disable SMT on an existing HPC VM instance, [connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) and run the following command from the guest OS:
        
        sudo google_mpi_tuning --nosmt
        




For more information, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

### Configure gVNIC as the network interface type for C2 and C2D instances

If you create a new C2 or C2D instance, then, by default, Virtio-net is used for the virtual network interface. Using gVNIC instead of Virtio-net can improve the scalability of MPI applications by providing better communication performance and higher throughput. Additionally, gVNIC is a prerequisite for [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#creating_a_vm_with_high-bandwidth_configuration), which provides higher bandwidth and allows for higher throughput.

**Note:** H4D and H3 instances use only the gVNIC network interface for standard network traffic; VirtIO is not supported. H4D or H3 instances don't use Tier_1 networking.

To use gVNIC, follow the steps to create an HPC VM instance or [create a compute instance with Advanced Compute Images](https://docs.cloud.google.com/compute/docs/instances/use-aci-images#create) and do one of the following:

###  Console 

To set gVNIC as the network interface, when creating the instance, in the navigation menu, click **Networking**. In the Networking pane that appears, do the following:

  1. Go to the **Network interfaces** section
  2. For **Network interface card** , select `gVNIC`.



###  gcloud 

Include the `--network-interface=nic-type=GVNIC` flag in the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

###  REST 

In the `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert), include `"nicType": "GVNIC"` in the `networkInterfaces` property.

The HPC VM image and Rocky Linux-based Advanced Compute Images include the gVNIC driver as a [Dynamic Kernel Module Support (DKMS)](https://en.wikipedia.org/wiki/Dynamic_Kernel_Module_Support). For more information, see [Using Google Virtual NIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

### Turn off Meltdown and Spectre mitigations

The HPC VM image and Rocky Linux-based Advanced Compute Images enable the Meltdown and Spectre mitigations by default. In some cases, these mitigations might result in workload-specific performance degradation. To disable these mitigations and incur the associated security risks, do the following:

  1. Run the following command on your instance:
         
         sudo google_mpi_tuning --nomitigation
         

  2. Reboot the instance.




### Improve network performance

To improve the network performance of your instance, set up one or more of the following configurations:

  * **Configure a higher bandwidth**. To configure Tier_1 networking for C2 or C2D compute instances, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create the instance. Specify the `--network-performance-configs` flag when creating the instance. For more information, see [Create instances and containers that use Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#create-high-bandwidth-vms-containers).

**Note:** Don't configure Tier_1 networking for H4D or H3 instances.
  * **Use jumbo frames**. To help minimize the processing overhead for network packets, we recommend using a larger packet size. You need to validate larger packet sizes for the specifics of your application. For information about the use of jumbo frames and packet sizes, see [Maximum transmission unit guide](https://docs.cloud.google.com/vpc/docs/mtu).

  * **Increase the TCP memory limits**. Higher bandwidth requires larger TCP memory. Follow the steps to [increase `tcp_*mem` settings](https://docs.cloud.google.com/compute/docs/networking/tcp-optimization-for-network-performance-in-gcp-and-hybrid#increase-socket-memory).

  * **Use the network-latency profile**. Evaluate your application's latency and enable busy polling that reduces latency in the network receive path. Adjust the `net.core.busy_poll` and `net.core.busy_read` settings in `/etc/sysctl.conf`, or [use `tuned-adm`](https://www.linux.org/threads/optimizing-linux.38680/).




## Use Intel MPI 2021

Google recommends to use the Intel MPI 2021 library for running MPI jobs on Google Cloud.

MPI implementations have many internal configuration parameters that can affect communication performance. These parameters are especially relevant for MPI Collective communication, which lets you specify algorithms and configuration parameters that can perform very differently in the Google Cloud environment.

The HPC VM image and Rocky Linux-based Advanced Compute Images include a utility, `google-hpc-compute`, that installs the recommended MPI libraries and uses Google Cloud tailored libfabric providers over the TCP transport.

### Limitations

The benefits of tuning vary from application to application. In some cases, a particular tuning might have a negative effect on performance. Consider benchmarking your applications to find the most efficient or cost-effective configuration.

### Use `google-hpc-compute` utility for Intel MPI 2021 support

The `google_install_intelmpi` script is the MPI related tool in the `google-hpc-compute` utility. It helps to install and configure Intel MPI.

To install the Intel MPI library while creating a new HPC VM instance or an Advanced Compute Images instance, follow the steps to create an HPC VM instance or [create a compute instance with Advanced Compute Images](https://docs.cloud.google.com/compute/docs/instances/use-aci-images#create) and include the following when creating the compute instance:
    
    
    --metadata=google_install_intelmpi="--impi_2021"
    

To install the library on an existing HPC VM instance or an Advanced Compute Images instance, run the following command on that compute instance:
    
    
    sudo google_install_intelmpi --impi_2021 --install_dir=PATH_INSTALL_MPI
    

The default location for `install_dir` is set to `/opt/intel`.

## Intel MPI library and MPI collective tunings

The HPC VM image and Rocky Linux-based Advanced Compute Images include generic tunings which disable hyperthreading, optimize memory, modify system resource limits and apply custom tuned profiles. The `google_hpc_firstrun` script is designed to run automatically on the first boot of the instance.

As a part of `google-hpc-firstrun` utility, the `mpi-tuning` script is run to improve the performance and latency of the HPC VM instance. You can run the `mpi-tuning.sh` script to apply tunings on individual compute instances.
    
    
    Usage:
      Verify tuning steps: $ mpi_tuning OPTIONS --dryrun
      Apply tunings: $ mpi_tuning OPTIONS
    
    Options:
      --hpcprofile       Install and apply google-hpc-compute tuned profile
                         Also applies: --tcpmem, --limits
      --hpcthroughput    Install and apply google-hpc-compute-throughput profile
                         Also applies: --tcpmem, --limits
      --tcpmem           Increase memory for TCP
      --limits           Change the system ulimits
      --nosmt            Disable simultaneous multi threading
      --nofirewalld      Disable firewalld
      --noselinux        Disable SE Linux (reboot required)
      --nomitigation     Disable CPU vulnerabilities mitigations (reboot required)
      --reboot           Reboot system after tunings if required
      --dryrun           Do not execute commands
      --verbose          Print verbose messages
      --help             Show help message
    

## Create a custom image using the HPC VM image

To implement the best practices at scale, create a custom OS image to use with your HPC VM instances. Complete the following tasks to create a custom image to use when creating HPC VM instances:

  1. Create a compute instance that uses the HPC VM image.

  2. Customize the compute instance with MPI tunings.

  3. Create a custom image using the boot disk of your HPC VM image as the source disk. You can do so using the [Google Cloud console](https://console.cloud.google.com/) or the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).




###  Console 

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. Click **Create image**.

  3. Specify a **Name** for your image.

  4. Under **Source disk** , select the name of the boot disk on your HPC VM instance.

  5. Choose other remaining properties for your image.

  6. Click **Create**.




###  gcloud 

Create the custom image by using the [`images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create).
    
    
    gcloud compute images create IMAGE_NAME \
             --source-disk=INSTANCE_NAME \
             --source-disk-zone=ZONE \
             --family=IMAGE_FAMILY \
             --storage-location=LOCATION
    

Replace the following:

  * `IMAGE_NAME`: name for the custom image.
  * `INSTANCE_NAME`: name of your HPC VM instance.
  * `ZONE`: zone where your HPC VM instance is located.
  * `IMAGE_FAMILY`: optional. The [image family](https://docs.cloud.google.com/compute/docs/images#image_families) this image belongs to.
  * `LOCATION`: optional. Region in which to store the custom image. The default location is the multi-region closest to the location of the source disk.



## Pricing

The HPC VM image and Advanced Compute Images are available at no additional cost. Because these images run on Compute Engine, you might incur charges for Compute Engine resources such as vCPUs, disks, and memory.

To learn more, see [Compute Engine pricing](https://cloud.google.com/compute/vm-instance-pricing).

## What's next

  * Review the [best practices for running HPC workloads](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices).
  * Learn about [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images) for HPC workloads.
  * Learn how to [set up and scale MPI applications on H4D VMs with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application) on Google Cloud.
  * Learn more about the [Compute-optimized machine family](https://docs.cloud.google.com/compute/docs/compute-optimized-machines).
  * Learn how to [create H4D HPC clusters with enhanced cluster management capabilities](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters).
  * If you have feedback or require support, then send an email at [hpc-image-feedback@google.com](mailto:hpc-image-feedback@google.com).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
