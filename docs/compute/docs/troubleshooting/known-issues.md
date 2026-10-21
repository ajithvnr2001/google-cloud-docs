---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues/
title: Known issues \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:22:37.854858+00:00
---

# Known issues  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page describes known issues that you might run into while using Compute Engine instances. For issues that specifically affect Confidential VMs, see [Confidential VM limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#limitations).

## General issues

The following issues provide troubleshooting guidance or general information.

### Guest agent ignores the `ip_forwarding` option in the `NetworkInterfaces` configuration

The guest agent [`NetworkInterfaces`](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#networkinterfaces) configuration section includes an `ip_forwarding` option. You can use this option to prevent the agent from installing alias IP addresses and IP forwarding routes from the metadata server (MDS). However, for guest agent versions that use the [plugin-based architecture](https://docs.cloud.google.com/compute/docs/images/guest-agent#plugin-architecture), which includes the core plugin, the agent ignores the `ip_forwarding` configuration option. The guest agent installs alias IP addresses and IP forwarding routes regardless of the configuration. For more information, see [guest agent documentation](https://docs.cloud.google.com/compute/docs/images/guest-agent). This issue affects you if you are using [SAP Netweaver pacemaker](https://docs.cloud.google.com/sap/docs/netweaver-ha-config-rhel#enable-back-end-comms) in a setup with an internal load balancer (ILB).

To mitigate this issue, set the metadata attribute `enable-guest-agent-core-plugin` to `false` as described in the [backward compatibility](https://docs.cloud.google.com/compute/docs/images/guest-agent#backward-compatibility) documentation.

### Compute instances with Secure Boot enabled might fail to boot

In rare cases, Shielded VM instances created prior to November 7, 2025 with Secure Boot enabled, or those using full disk encryption software or secret sealing to vTPM PCRs, might fail to boot. This might be caused by an incorrect sequence of updates (for example, updating shim without having proper certificates in place) after Microsoft Secure Boot certificates expire in the second half of 2026.

**Resolution**

To resolve this issue, update your compute instances with the new certificates. For more information, see [Microsoft Secure Boot certificates expiration guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-expiration).

### Local SSD disks attached to C4, C4A, C4D, C4N, and H4D instances might not capture all writes in case of power loss

Following a loss of power to a host server, if Compute Engine can recover the data on the Local SSD disks, then a compute instance running on that host server restarts with all disks attached, and the data includes all writes that were completed prior to the host error.

For C4, C4A, C4D, C4N, and H4D instances, the restored Local SSD disks might not include writes that were completed immediately prior to the power loss event. When the compute instance restarts, reading from an affected logical block address (LBA) returns an error indicating the LBA is unreadable. If your compute instance experiences an unexpected reboot, check the OS error logs for read or write failures after the compute instance restarts.

### Hyperdisk Throughput and Hyperdisk Extreme capacity consumes Persistent Disk quotas simultaneously

When you create Hyperdisk Throughput or Hyperdisk Extreme disks, the disk capacity counts against two separate quotas at the same time: the specific Hyperdisk quota and a corresponding Persistent Disk quota.

  * `Hyperdisk Throughput Capacity (GB)` (`HDT-TOTAL-GB`) also counts against your `Persistent disk standard (GB)` (`DISKS-TOTAL-GB`) quota.
  * `Hyperdisk Extreme Capacity (GB)` (`HDX-TOTAL-GB`) also counts against your `Persistent disk SSD (GB)` (`SSD-TOTAL-GB`) quota.



If your Persistent Disk quota limit is lower than your Hyperdisk quota limit, you'll encounter `QUOTA_EXCEEDED` errors. You can't create additional disks once the Persistent Disk limit is reached, even if you have remaining Hyperdisk quota available.

To mitigate this issue, you must adjust both quotas whenever you request an increase. When you adjust your `HDT-TOTAL-GB` or `HDX-TOTAL-GB` quota, you must also adjust your `DISKS-TOTAL-GB` or `SSD-TOTAL-GB` quota respectively.

### Workload interruptions on A4 instances due to firmware issues for NVIDIA B200 GPUs

NVIDIA has identified two firmware issues for B200 GPUs, which A4 instances use. These issues can cause workload interruptions, such as the `nvidia-smi` command not responding. If you notice workload interruptions on A4 VMs, then confirm that one of the following conditions are true:

  * The VM's uptime (`lastStartTimestamp`) exceeds 65 days.
  * Logs show an [`Xid 149` message that mentions `0x02a`](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#xid-149-0x02a).



If one of these conditions is true, then you must reset the GPUs that are attached to your A4 VMs. To prevent future interruptions to your workload due to firmware issues, we recommend that you reset your GPUs at least once every 60 days. For more information, see [Reset GPUs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#reset-gpus).

**Note:** If your A4 VMs are part of a GKE cluster, then you can use the [GKE GPU node reset tool](https://github.com/ai-on-gke/tutorials-and-examples/tree/main/gpu-reset-tool) to resolve minor GPU issues, such as unresponsive `nvidia-smi` commands, without rebooting your VMs.

### Possible host errors during C4 instance creation on sole tenant nodes

C4 machine type instances running on sole tenant nodes might encounter unexpected instance terminations due to host errors or instance creation failures.

To address this issue, Google has limited the maximum number of C4 instances allowed per sole tenant node to 26.

### Serial-console is read-only for C4 and C4D bare metal instances

You can't enable interactive access to the serial console for C4 or C4D bare metal instances; the serial console is read-only.

**Workaround**

To execute commands interactively, you can connect to the instance using SSH after the instance starts. For information about using SSH with Compute Engine instances, see [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh).

### Canceling jobs on 32-node or larger HPC clusters exceeds the timeout

For large jobs on 32-node or larger clusters, the time it takes to cancel a job can exceed the default `UnkillableStepTimeout` value of 300 seconds. Exceeding this value causes the affected nodes to become unusable for future jobs.

To resolve this issue, use one of the following methods:

  * Update Cluster Toolkit to release 1.65.0 or later. Then redeploy the cluster using the following command:
        
        gcluster deploy -w --force BLUEPRINT_NAME.yaml
        

  * If you can't update Cluster Toolkit or redeploy the cluster, then you can manually modify the `UnkillableStepTimeout` parameter by completing the following steps:

**Warning:** If you complete these steps but don't update Cluster Toolkit to release 1.65.0 or later, then these manual changes will get overwritten if the cluster is redeployed with the `gcluster deploy` command.
    1. Use SSH to connect to the main controller node of your cluster.
           
           gcloud compute ssh --project PROJECT_ID --zone ZONE DEPLOYMENT_NAME-controller
           

You can find the exact name and IP address for the main controller node by using the Google Cloud console and navigating to the [**VM instances** page](https://console.cloud.google.com/compute/instances).

    2. Create a backup of the current `cloud.conf` file. This file is usually located in `/etc/slurm/`.
           
           sudo cp /etc/slurm/cloud.conf /etc/slurm/cloud.conf.backup-$(date +%Y%m%d)
           

    3. Using `sudo` privileges, use a text editor to open the file `/etc/slurm/cloud.conf`.

    4. Add or modify the line that contains `UnkillableStepTimeout`. For example, set the timeout to 900 seconds (15 minutes) as follows:
           
           UnkillableStepTimeout=900
           

    5. Save the file.

**Note:** Cluster Toolkit deployments typically configure an NFS share from the controller node for directories like `/etc/slurm` and `/home`. This configuration means that any changes made to `cloud.conf` on the controller node are automatically visible to all compute nodes.
    6. Use the command `sudo scontrol reconfigure` to apply the new setting across the cluster without needing a full restart.




#### Verify the fix

You can verify the setting has changed by running the following command:
    
    
       scontrol show config | grep UnkillableStepTimeout
    

The output should reflect the new value you set, for example: `UnkillableStepTimeout = 900`.

### **Resolved** : Modifying the IOPS or throughput on an Asynchronous Replication primary disk using the `gcloud compute disks update` command causes a false error

**The following issue was resolved on June 1, 2025.**

When you use the [`gcloud compute disks update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update) command to modify the IOPS and throughput on an Asynchronous Replication primary disk, the gcloud CLI shows an error message even if the update was successful.

To accurately verify that an update was successful, check the disk properties using the gcloud CLI or the Google Cloud console to see the new IOPS and throughput values. For more information, see [View the provisioned performance settings for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk#view_provisioned).

### The metadata server might display old `physicalHost` compute instance metadata

After experiencing a [host error](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#hosterror) which moves a compute instance to a new host, when you [query the metadata server](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#programmatically-query-metadata), it might display the `physicalHost` metadata of the instance's previous host.

To work around this issue, do one of the following:

  * Use the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) or the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) to retrieve the correct `physicalHost` information.
  * [Stop and then start](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) your instance. This process updates the `physicalHost` information in the metadata server.
  * Wait 24 hours for the impacted instance's `physicalHost` information to be updated.



### Long `baseInstanceName` values in managed instance groups (MIGs) can cause disk name conflicts

In a MIG, disk name conflicts can occur if the instance template specifies disks to be created upon compute instance creation and the `baseInstanceName` value exceeds 54 characters. This happens because Compute Engine generates disk names using the instance name as a prefix.

When generating disk names, if the resulting name exceeds the resource name limit of 63 characters, then Compute Engine truncates the excess characters from the end of the instance name. This truncation can lead to the creation of identical disk names for instances that have similar naming patterns. In such a case, the new instance will attempt to attach the existing disk. If the disk is already attached to another compute instance, then the new instance creation fails. If the disk is not attached or is in [multi-writer mode](https://docs.cloud.google.com/compute/docs/disks#pdspecs_rw), then the new instance attaches the disk, potentially leading to data corruption.

To avoid disk name conflicts, keep the `baseInstanceName` value to a maximum length of 54 characters.

### Creating reservations or future reservation requests using an instance template that specifies an A2, C3, or G2 machine type causes issues

If you use an instance template that specifies an A2, C3, or G2 machine type to create a reservation, or to create and submit a future reservation request for review, then you encounter issues. Specifically, one of the following might happen:

  * Creating the reservation might fail. If it succeeds, then one of the following applies:

    * If you created an automatically consumed reservation (default), then the creation of compute instances with matching properties doesn't consume the reservation.

    * If you created a specific reservation, then the creation of compute instances to specifically target the reservation fails.

  * Creation of the future reservation request succeeds. However, if you submit it for review, then Google Cloud declines your request.




You can't replace the instance template used to create a reservation or future reservation request, or override the template's instance properties. If you want to reserve resources for A2, C3, or G2 machine types, then do one of the following instead:

  * Create a new [single-project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project#specify-vm-properties) or [shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared#specify-vm-properties) by specifying properties directly.

  * Create a new future reservation request by doing the following:

    1. If you want to stop an existing future reservation request from restricting the properties of the future reservation requests you can create in your current project—or in the projects the future reservation request is shared with—[delete the future reservation request](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations).

    2. Create a [single-project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations#specify-vm-properties) or [shared future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations#specify-vm-properties) by specifying properties directly and submit it for review.




### Limitations when using `-lssd` machine types with Google Kubernetes Engine

When using the Google Kubernetes Engine API, the node pool that you provision with Local SSD disks **must** have the same number of Local SSD disks as the selected C4, C3, or C3D machine type. For example, if you plan to create a compute instance that uses the `c3-standard-8-lssd` machine type, then there must be two Local SSD disks; if you use the `c3d-standard-8-lssd` machine type, then just one disk is required. If the disk number doesn't match, then you get a Local SSD misconfiguration error from the Compute Engine control plane. See [Machine types that automatically attach Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed) to select the correct number of Local SSD disks based on the `lssd` machine type.

If you use the Google Kubernetes Engine Google Cloud console to create a cluster or node pool, then either node creation fails or Local SSD disks are not detected as ephemeral storage when using any of the following machine types:

  * `c4-standard-*-lssd`
  * `c4-highmem-*-lssd`
  * `c3-standard-*-lssd`
  * `c3d-standard-*-lssd`



### Single flow TCP throughput variability on C3D instances

C3D instances that have more than 30 vCPUs might experience single flow TCP throughput variability and occasionally be limited to 20 to 25 Gbps. To achieve higher rates, use multiple tcp flows.

### The CPU utilization observability metric is incorrect for compute instances that use one thread per core

If your compute instance's CPU uses one thread per core, then the CPU utilization Cloud Monitoring metric in the _Observability_ * tab of the **VM instances** page in the Compute Engine Google Cloud console only scales to 50%. Two threads per core is the default for most machine types. For more information, see [Set number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

To view your compute instance's CPU utilization normalized to 100%, view CPU utilization in Metrics Explorer instead. For more information, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

### Google Cloud console SSH-in-browser connections might fail if you use custom firewall rules

If you use custom firewall rules to control SSH access to your compute instances, then you might not be able to use the [SSH-in-browser](https://docs.cloud.google.com/compute/docs/connect/ssh-in-browser) feature.

To work around this issue, do one of the following:

  * Enable [Identity-Aware Proxy for TCP](https://docs.cloud.google.com/compute/docs/connect/ssh-using-iap) to continue connecting to compute instances using the SSH-in-browser Google Cloud console feature.

  * [Recreate](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules) the [`default-allow-ssh` firewall rule](https://docs.cloud.google.com/firewall/docs/firewalls#more_rules_default_vpc) to continue connecting to compute instances using SSH-in-browser.

  * [Connect to compute instances using the Google Cloud CLI](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#gcloud) instead of SSH-in-browser.




### Temporary names for disks

During compute instance updates that were initiated using the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update) or the [`instances.update` API method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update), Compute Engine might temporarily change the name of your compute instance's disks, by adding any of the following suffixes to the original name:

  * `-temp`
  * `-old`
  * `-new`



Compute Engine removes the suffix and restores the original disk names as the update completes.

### Increased latency for some Persistent Disks caused by disk resizing

In some cases, resizing large Persistent Disks (~3 TB or larger) might be disruptive to the I/O performance of the disk. If you are impacted by this issue, your Persistent Disks might experience increased latency during the resize operation. This issue can impact Persistent Disks of any [type](https://docs.cloud.google.com/compute/docs/disks#disk-types).

### Your automated processes might fail if they use API response data about your resource-based commitment quotas

Your automated processes that consume and use API response data about your Compute Engine resource-based commitment quotas might fail if each of the following things happens. Your automated processes can include any snippets of code, business logic, or database fields that use or store the API responses.

  1. The response data is from any of the following Compute Engine API methods:

     * [`compute.regions.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regions/list)
     * [`compute.regions.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regions/get)
     * [`compute.projects.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/get)
  2. You use an `int` instead of a `number` to define the field for your resource quota limit in your API response bodies. You can find the field in the following ways for each method:

     * `items[].quotas[].limit` for the [`compute.regions.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regions/list#response-body).
     * `quotas[].limit` for the [`compute.regions.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regions/get#response-body).
     * `quotas[].limit` for the [`compute.projects.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects/get#response-body).
  3. You have unlimited default quota available for any of your Compute Engine committed SKUs.

For more information about quotas for commitments and committed SKUs, see [Quotas for commitments and committed resources](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#quota).




#### Root cause

When you have limited quota, if you define the `items[].quotas[].limit` or `quotas[].limit` field as an `int` type, the API response data for your quota limits might still fall within the range for `int` type and your automated process might not get disrupted. But when the default quota limit is unlimited, Compute Engine API returns a value for the `limit` field that falls outside of the range defined by `int` type. Your automated process can't consume the value returned by the API method and fails as a result.

#### How to work around this issue

You can work around this issue and continue generating your automated reports in the following ways:

  * **Recommended:** Follow the [Compute Engine API reference documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1) and use the correct data types for the API method definitions. Specifically, use the `number` type to define the `items[].quotas[].limit` and `quotas[].limit` fields for your API methods.

  * Decrease your quota limit to a value under 9,223,372,036,854,775,807. You must set quota caps for all projects that have resource-based commitments, across all regions. You can do this in one of the following ways:

    * Follow the same steps that you would to [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota), and request for a lower quota limit.
    * [Create a quota override](https://docs.cloud.google.com/docs/quotas/view-manage#create_override).

**Note:** Setting a quota limit cap is only a temporary workaround until you correct the definition of the `items[].quotas[].limit` field for `compute.regions.list` method and change it to `number` type. To return the default quota limits for your committed SKUs back to their unlimited value, you must remove the quota limit caps.

## Known issues for GPU instances

The following section describes the known issues for Compute Engine GPU instances.

### Accelerator-optimized machine types that have Local SSD disks automatically attached might take hours to terminate and restart

[Accelerator-optimized machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) have GPUs automatically attached. Most A-series accelerator-optimized machine types, with the exception of A2 Standard, have [Local SSD disks automatically attached](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disks_fixed).

Accelerator-optimized machine types don't support live migration, and you must [set their host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) to `TERMINATE`. These machine types can take up to one hour to terminate after failures or [host errors](https://docs.cloud.google.com/compute/docs/faq#hosterror). For the accelerator-optimized machine types that have Local SSD disks automatically attached, the termination process might take several hours.

### Creation errors and decreased performance when using Dynamic NICs with GPU instances

[Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nics) aren't supported for use with GPU instances. If you create a GPU instance with Dynamic NICs, or add Dynamic NICs to an existing GPU instance, the following issues might occur:

  * The operation fails with an error such as the following:

`Internal error. Please try again or contact Google Support. (Code: 'CODE')`

  * The operation succeeds, but the instance experiences decreased performance, such as significantly lower [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).




These issues occur because the Dynamic NIC configuration leads to errors when Compute Engine attempts to distribute the instance's vNICs across physical NICs on the host server.

## Known issues for bare metal instances

These are the known issues for Compute Engine bare metal instances.

### Manually starting host maintenance doesn't work for X4 instances

For X4 instances, the procedure described in [manually start a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) doesn't work.

**Workaround**

  1. Stop the X4 instance.
  2. Ater the instance state changes to `TERMINATED`, start the X4 instance.



For information about how to stop or restart an X4 instance, see [Stop or restart a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).

### C4D bare metal machine types don't support SUSE Linux 15 SP6 images

C4D bare metal instances can't run the SUSE Linux Enterprise Server (SLES) version 15 SP6 OS.

**Workaround**

Use SLES 15 SP5 instead.

### Simulating host maintenance doesn't work for C4 bare metal instances

The `c4-standard-288-metal` and `c4-highmem-288-metal` machine types don't support [simulating host maintenance events](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance).

#### Workaround

Use virtual machine (VM) instances that were created using other C4 machine types to simulate maintenance events.

  1. Create a VM instance using a C4 machine type that doesn't end in `-metal`.

When creating the VM, [configure the C4 instance to `Terminate`](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#setnewoption) instead of using Live Migration during host maintenance events.

  2. Simulate a host maintenance event for this VM.




During a simulated host maintenance event, the behavior for VMs configured to `Terminate` is the same behavior as for C4 bare metal instances.

### Lower than expected performance with Z3 bare metal instances on RHEL 8

When using Red Hat Enterprise Linux (RHEL) version 8 with a Z3 bare metal instance, the network performance is lower than expected.

#### Root cause

There is a missing Page Pool feature in the Linux kernel version (4.18) that is used by RHEL 8.

#### Workaround

Use a more recent version of RHEL or a different operating system when you are working with Z3 bare metal instances.

## Issues related to using Dynamic Network Interfaces

This section describes known issues related to using multiple network interfaces and Dynamic Network Interfaces.

### Dropped packets when using Dynamic NICs with alias IP ranges, protocol forwarding, or Passthrough Network Load Balancers

The guest agent automatically add local routes in the following scenarios for vNICs, but not for Dynamic NICs:

  * When you [configure an alias IP range](https://docs.cloud.google.com/vpc/docs/configure-alias-ip-ranges), the guest agent creates a local route for the alias IP range.
  * When you create a [target instance](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding#target-instances) that references a compute instance for protocol forwarding, the guest agent creates a local route for the associated forwarding rule IP address.
  * When you add a backend to a [Passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer), the guest agent creates a local route for the associated forwarding rule IP address.



Because the local routes aren't added for Dynamic NICs, the Dynamic NIC might experience dropped packets.

To resolve this issue, add the IP addresses manually as follows:

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

  2. If you are configuring an alias IP range, do the following. Otherwise, you can skip this step.

     1. In `/etc/default/instance_configs.cfg`, ensure that the `ip_aliases` setting is set to `true`.
     2. If the ip_aliases setting is set to `false`, modify the file to change it to `true` and then restart the guest agent:
            
            systemctl restart google-guest-agent
            

  3. Configure a local route for the alias IP range or the forwarding rule IP address by using the following command:
         
         ip route add to local IP_ADDRESS dev DYNAMIC_NIC_DEVICE_NAME proto 66
         

Replace the following:

     * `IP_ADDRESS`: the alias IP range or forwarding rule IP address that you want to add a local route for.
     * `DYNAMIC_NIC_DEVICE_NAME`: the device name of the Dynamic NIC that you want to add a local route for. For example, `a-gcp.ens4.3`.



### Issues with installation and management of Dynamic NICs in guest agent versions 20250901.00 to 20251120.01

If you [configure automatic management of Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics#configure-guest-os-automatic) and your instance is running the guest agent at a version from 20250901.00 to 20251120.01, you might encounter the following issues:

  * The guest agent fails to install and manage Dynamic NICs in the guest OS of your instance.

You might receive an error that includes `Cannot find device` when running commands in the guest OS that reference Dynamic NICs.

  * Deleting multiple Dynamic NICs causes the [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) to become inaccessible.




#### Root cause

Starting with version [20250901.00](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#September_03_2025), the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) migrated to a new plugin-based architecture to improve modularity. The new architecture didn't initially support the automatic installation and management of Dynamic NICs.

#### Resolution

To resolve these issues, update your instance to use guest agent version 20251205.00 or later:

  1. To update the guest agent to the latest version, see [Update the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest).
  2. To confirm the guest agent version that your instance is running, see [View installed packages by operating system version](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_packages).



If necessary, you can temporarily work around these issues for instances that are running guest agent versions 20250901.00 to 20251120.01 by following the instructions in [Backward compatibility](https://docs.cloud.google.com/compute/docs/images/guest-agent#backward-compatibility) to revert to the previous guest agent architecture.

### Packet interception can result in dropped packets due to missing VLAN tags in the Ethernet headers

Packet interception when using Dynamic NIC can result in dropped packets. Dropped packets can happen when the pipeline is terminated early. The issue affects both session-based and non-session-based modes.

#### Root cause

Dropped packets occur during packet interception when the pipeline is terminated early (ingress intercept and egress reinject). The early termination causes the VLAN ID to be missing from the ingress packet's Ethernet header. Because the egress packet is derived from the modified ingress packet, the egress packet also lacks the VLAN ID. This leads to incorrect endpoint index selection and subsequent packet drops.

#### Workaround

Don't use Google Cloud features that rely on packet intercept, such as [firewall endpoints](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#specifications).

### Dynamic NIC operations fail when a compute instance is in multiple instance groups

If you add or delete a Dynamic NIC, and the operation gets stuck in a `RUNNING` state at 0% progress and eventually fails with an `INTERNAL_ERROR`, this might be because the compute instance is in multiple instance groups (managed or unmanaged).

To let the operation complete, remove the instance from all but one instance group. You can [remove an instance from a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances) or [remove an instance from an unmanaged instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances#removing_vms).

## Known issues for Linux compute instances

These are the known issues for Linux compute instances.

### Package upgrade error on Rocky Linux 9.7

`dnf update` fails on Rocky Linux Accelerator Optimized images version `v20251113` or earlier (for example, `rocky-linux-9-optimized-gcp-nvidia-latest-v20251113`) due to a package dependency conflict. You might see an error similar to the following:
    
    
    [root@rockylinux9 ~]# dnf update
    CIQ SIG/Cloud Next for Rocky Linux 9 37 MB/s | 49 MB 00:01
    CIQ SIG/Cloud Next Nonfree for Rocky Linux 9 4.4 MB/s | 1.5 MB 00:00
    NVIDIA DOCA 2.10.0 packages for EL 9.5 239 kB/s | 160 kB 00:00
    Google Compute Engine 38 kB/s | 8.2 kB 00:00
    Google Cloud SDK 59 MB/s | 154 MB 00:02
    Rocky Linux 9 - BaseOS 24 MB/s | 6.3 MB 00:00
    Rocky Linux 9 - AppStream 36 MB/s | 11 MB 00:00
    Rocky Linux 9 - Extras 124 kB/s | 16 kB 00:00
    Error:
     Problem 1: package perftest-25.04.0.0.84-1.el9.x86_64 from baseos requires libhns.so.1(HNS_1.0)(64bit), but none of the providers can be installed
      - package perftest-25.04.0.0.84-1.el9.x86_64 from baseos requires libhns.so.1()(64bit), but none of the providers can be installed
      - cannot install both libibverbs-51.0-3.el9_5.cld_next.x86_64 from ciq-sigcloud-next and libibverbs-2501mlnx56-1.2501060.x86_64 from @System
      - cannot install both libibverbs-51.0-5.el9_5.cld_next.x86_64 from ciq-sigcloud-next and libibverbs-2501mlnx56-1.2501060.x86_64 from @System
      - cannot install both libibverbs-54.0-2.el9_6.cld_next.x86_64 from ciq-sigcloud-next and libibverbs-2501mlnx56-1.2501060.x86_64 from @System
      - cannot install both libibverbs-54.0-3.el9_6.cld_next.x86_64 from ciq-sigcloud-next and libibverbs-2501mlnx56-1.2501060.x86_64 from @System
      - cannot install both libibverbs-54.0-4.el9_6.cld_next.x86_64 from ciq-sigcloud-next and libibverbs-2501mlnx56-1.2501060.x86_64 from @System
      - cannot install both libibverbs-54.0-5.el9_6.cld_next.x86_64 from ciq-sigcloud-next and libibverbs-2501mlnx56-1.2501060.x86_64 from @System
      - cannot install both libibverbs-57.0-3.el9_7_ciq.x86_64 from ciq-sigcloud-next and libibverbs-2501mlnx56-1.2501060.x86_64 from @System
      - cannot install both libibverbs-57.0-2.el9.x86_64 from baseos and libibverbs-2501mlnx56-1.2501060.x86_64 from @System
      - cannot install the best update candidate for package perftest-25.01.0-0.70.g759a5c5.2501060.x86_64
      - cannot install the best update candidate for package libibverbs-2501mlnx56-1.2501060.x86_64
     Problem 2: package ucx-ib-mlx5-1.18.0-1.2501060.x86_64 from @System requires ucx(x86-64) = 1.18.0-1.2501060, but none of the providers can be installed
      - cannot install both ucx-1.18.1-1.el9.x86_64 from appstream and ucx-1.18.0-1.2501060.x86_64 from @System
      - cannot install both ucx-1.18.1-1.el9.x86_64 from appstream and ucx-1.18.0-1.2501060.x86_64 from doca
      - cannot install the best update candidate for package ucx-ib-mlx5-1.18.0-1.2501060.x86_64
      - cannot install the best update candidate for package ucx-1.18.0-1.2501060.x86_64
    ...
    (try to add '--allowerasing' to command line to replace conflicting packages or '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)

#### Root cause

A userspace package version conflict exists between DOCA OFED versions prior to 3.20 and Rocky Linux 9.7. Specifically, Rocky Linux 9.7 includes `ucx` and `perftest` packages that are a later version than the corresponding packages in the DOCA OFED repository. This version mismatch causes `dnf update` to fail with dependency resolution errors.

#### Resolution

Before you perform a full system upgrade, update the DOCA repository package:
    
    
    sudo dnf update doca-repo
    sudo dnf update
    

Rocky Linux Accelerator Optimized images built in December 2025 (for example, `rocky-linux-9-optimized-gcp-nvidia-latest-v20251215`) already include the updated `doca-repo` package, so this upgrade issue is not present on those builds or later.

### OS Login isn't supported on SLES 16

An SSH configuration issue in SUSE Linux Enterprise Server (SLES) 16 prevents the use of the Google Cloud feature [OSLogin](https://docs.cloud.google.com/compute/docs/oslogin). However [Metadata-managed SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh#metadata) are unaffected and continue to function.

### Supported URL formats for startup script

If your compute instance uses guest agent version `20251115.00`, fetching a startup script using the `startup-script-url` metadata key fails if the URL uses the `https://storage.googleapis.com/` format that is documented in the [Use startup scripts on Linux VMs](https://docs.cloud.google.com/compute/docs/instances/startup-scripts/linux#gcloud_3) page.

To work around this issue, use one of the following supported URL formats:

  * **Authenticated URL** : `https://storage.cloud.google.com/BUCKET/FILE`
  * **gcloud CLI storage URI** : `gs://BUCKET/FILE`



### VM instances that use Debian 11 images prior to version v20250728 fail to run `apt update`

On July 22, 2025, the Debian community [removed](https://lists.debian.org/debian-devel-announce/2025/06/msg00003.html) Debian 11 (Bullseye) backports from the main Debian upstream. This update causes `sudo apt update` to fail with the following error:
    
    
    The repository 'https://deb.debian.org/debian bullseye-backports Release' does
    not have a Release file.
    

#### Root cause

Because the Debian community removed the backports repositories from the main upstream, there is no longer any reference to `bullseye-backports Release`.

#### Resolution

Use image version `debian-11-bullseye-v20250728` or newer. These versions don't contain the backports repositories. Alternatively, you can update current instances by modifying `/etc/apt/sources.list`:

  * To update the repository URL and use the archive for `bullseye-backports`:
        
        sudo sed -i 's/^deb https:\/\/deb.debian.org\/debian bullseye-backports main$/deb https:\/\/archive.debian.org\/debian bullseye-backports main/g; s/^deb-src https:\/\/deb.debian.org\/debian bullseye-backports main$/deb-src https:\/\/archive.debian.org\/debian bullseye-backports main/g' /etc/apt/sources.list
        

  * To delete the repository URL and discard `bullseye-backports`:
        
        sudo sed -i '/^deb https:\/\/deb.debian.org\/debian bullseye-backports main$/d; /^deb-src https:\/\/deb.debian.org\/debian bullseye-backports main$/d' /etc/apt/sources.list
        




### `ubuntu-desktop` package installation breaks network connectivity when the instance restarts

When you restart a Ubuntu compute instance after installing the `ubuntu-desktop` package, network interfaces might not be correctly configured.

#### Root cause

The `ubuntu-deskop` package pulls `ubuntu-settings` as a dependency, which [sets NetworkManager as the default "renderer" for netplan](https://canonical-netplan.readthedocs-hosted.com/en/latest/nm-all/). More specifically, it inserts a new YAML configuration for `netplan` at `/usr/lib/netplan/00-network-manager-all.yaml` containing the following:
    
    
    network:
      version: 2
      renderer: NetworkManager
    

This configuration conflicts with our `networkd`-based early provisioning using `cloud-init`.

#### Recovery

If the compute instance has been restarted and is inaccessible, then do the following:

  1. Follow the [instructions on rescuing a compute instance](https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm#rescue).
  2. After mounting the inaccessible compute instance's Linux file system partition, run the following command (replacing `/rescue` with your mount point):
         
         echo -e 'network:\n  version: 2\n  renderer: networkd' | sudo tee /rescue/etc/netplan/99-gce-renderer.yaml
         

  3. [Continue to reboot the inaccessible compute instance](https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm#un-rescue).




### Compute instances that use Ubuntu OS version v20250530 show incorrect FQDN

You might see an incorrect Fully Qualified Domain Name (FQDN) with the addition of `.local` suffix when you do one of the following:

  * Update to version `20250328.00` of the `google-compute-engine` package.
  * Launch compute instances from any Canonical offered Ubuntu image with the version suffix `v20250530`.



For example, `projects/ubuntu-os-cloud/global/images/ubuntu-2204-jammy-v20250530`.

If you experience this issue, then you might see a FQDN similar to the following:
    
    
       [root@ubuntu2204 ~]# apt list --installed | grep google
       ...
       google-compute-engine/noble-updates,now 20250328.00-0ubuntu2~24.04.0 all [installed]
       ...
    
       [root@ubuntu2204 ~]# curl "http://metadata.google.internal/computeMetadata/v1/instance/image" -H "Metadata-Flavor: Google"
       projects/ubuntu-os-cloud/global/images/ubuntu-2204-jammy-v20250530
    
       [root@ubuntu2204 ~]# hostname -f
       ubuntu2204.local
    

#### Root cause

On all Ubuntu images with version `v20250530`, the `guest-config` package version `20250328.00` adds `local` to the search path due to the introduction of a new configuration file: <https://github.com/GoogleCloudPlatform/guest-configs/blob/20250328.00/src/etc/systemd/resolved.conf.d/gce-resolved.conf>
    
    
       [root@ubuntu2204 ~]# cat /etc/resolv.conf
       # This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8).
       # Do not edit.
       ...
    
       nameserver 127.0.0.53
       options edns0 trust-ad
       search local ... google.internal
    

The presence of this `local` entry within the search path in the `/etc/resolv.conf` file results in a `.local` element being appended to the hostname when a FQDN is requested.

Note that [version 20250501 of `guest-configs`](https://github.com/GoogleCloudPlatform/guest-configs/blob/20250501.00/src/etc/systemd/resolved.conf.d/gce-resolved.conf) already fixes the issue but Canonical hasn't incorporated the fix into their images yet.

#### Workaround

  1. Modify the Network Name Resolution configuration file `/etc/systemd/resolved.conf.d/gce-resolved.conf` by changing `Domains=local` to `Domains=~local`
  2. Run the following command to restart the systemd-resolved service: `systemctl restart systemd-resolved`
  3. Check that `local` is removed from the search path in `/etc/resolv.conf`
  4. Confirm the FQDN by using the command `hostname -f`
         
         [root@ubuntu2204 ~]# hostname -f
         ubuntu2204.us-central1-a.c.my-project.internal
         




### Missing mkfs.ext4 on openSUSE Images

Recent `v20250724` release of openSUSE images (starting with `opensuse-leap-15-6-v20250724-x86-64`) from August 2025 is missing the `e2fsprogs` package, which provides utilities for managing file systems. A common symptom of this issue is that you see an error message such as `command not found` when you attempt to use the `mkfs.ext4` command.

#### Workaround

If you encounter this issue, install the missing package manually by using the openSUSE package manager, `zypper`.
    
    
    # Update the package index
    user@opensuse:~> sudo zypper refresh
    
    # Install the e2fsprogs package
    user@opensuse:~> sudo zypper install e2fsprogs
    
    # Verify the installation
    user@opensuse:~> which mkfs.ext4
    

### SUSE Enterprise compute instances fail to boot after changing machine types

After you change the machine type for a compute instance that runs SUSE Enterprise Linux, the instance can fail to boot with the following error in the serial console:
    
    
                Starting [0;1;39mdracut initqueue hook[0m...
       [  136.146065] dracut-initqueue[377]: Warning: dracut-initqueue: timeout, still waiting for following initqueue hooks:
       [  136.164820] dracut-initqueue[377]: Warning: /lib/dracut/hooks/initqueue/finished/devexists-\x2fdev\x2fdisk\x2fby-uuid\x2fD3E2-0CEB.sh: "[ -e "/dev/disk/by-uuid/D3E2-0CEB" ]"
       [  136.188732] dracut-initqueue[377]: Warning: /lib/dracut/hooks/initqueue/finished/devexists-\x2fdev\x2fdisk\x2fby-uuid\x2fe7b218a9-449d-4477-8200-a7bb61a9ff4d.sh: "if ! grep -q After=remote-fs-pre.target /run/systemd/generator/systemd-cryptsetup@*.service 2>/dev/null; then
       [  136.220738] dracut-initqueue[377]:     [ -e "/dev/disk/by-uuid/e7b218a9-449d-4477-8200-a7bb61a9ff4d" ]
       [  136.240713] dracut-initqueue[377]: fi"
    

#### Root cause

SUSE creates its cloud images with a versatile `initramfs` (initial RAM filesystem) that supports various instance types. This is achieved by using the `--no-hostonly --no-hostonly-cmdline -o multipath` flags during the initial image creation. However, when a new kernel is installed or the `initramfs` is regenerated, which happens during system updates, these flags are omitted by default. This results in a smaller `initramfs` tailored specifically for the current system's hardware, potentially excluding drivers needed for other instance types.

For example, C3 instances use NVMe drives, which require specific modules to be included in the `initramfs`. If a system with an `initramfs` lacking these NVMe modules is migrated to a C3 instance, the boot process fails. This issue can also affect other instance types with unique hardware requirements.

#### Workaround

Before changing the machine type, regenerate the `initramfs` with all drivers:
    
    
    dracut --force --no-hostonly
    

If the system is already impacted by the issue, then create a [temporary rescue compute instance](https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm). Use the [`chroot`](https://www.unix.com/man-page/suse/1/CHROOT/) command to access the impacted instance's boot disk and then regenerate the `initramfs` using the following command:
    
    
    dracut -f --no-hostonly
    

### Lower IOPS performance for Local SSD on Z3 with SUSE 12 images

Z3 compute instances that use SUSE Linux Enterprise Server (SLES) 12 images have significantly lower than expected performance for IOPS on Local SSD disks.

#### Root cause

This is an issue within the SLES 12 codebase.

#### Workaround

A patch from SUSE to fix this issue is not available or planned. Instead, you should use the SLES 15 operating system.

### RHEL 7 and CentOS compute instances lose network access after reboot

If your CentOS or RHEL 7 compute instances have multiple network interface cards (NICs) and one of these NICs doesn't use the VirtIO interface, then network access might be lost on reboot. This happens because RHEL doesn't support disabling predictable network interface names if at least one NIC doesn't use the VirtIO interface.

**Resolution**

Network connectivity can be restored by [stopping and starting](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) the compute instance until the issue is resolved. Network connectivity loss can be prevented from reoccurring by doing the following:

  1. Edit the `/etc/default/grub` file and remove the kernel parameters `net.ifnames=0` and `biosdevname=0`.

  2. Regenerate the grub configuration.

  3. Reboot the compute instance.




### repomd.xml signature couldn't be verified

On Red Hat Enterprise Linux (RHEL) or CentOS 7 based systems, you might see the following error when trying to install or update software using yum. This error shows that you have an expired or incorrect repository GPG key.

Sample log: 
    
    
    [root@centos7 ~]# yum update
    
    
    
    
    ...
    
    
    
    
    
    google-cloud-sdk/signature                                                                  | 1.4 kB  00:00:01 !!!
    https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64/repodata/repomd.xml: [Errno -1] repomd.xml signature could not be verified for google-cloud-sdk
    Trying other mirror.
    
    
    
    
    
    ...
    
    
    
    
    
    failure: repodata/repomd.xml from google-cloud-sdk: [Errno 256] No more mirrors to try.
    https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64/repodata/repomd.xml: [Errno -1] repomd.xml signature could not be verified for google-cloud-sdk
    
    

**Resolution**

To fix this, disable repository GPG key checking in the yum repository configuration by setting `repo_gpgcheck=0`. In supported Compute Engine base images this setting might be found in `/etc/yum.repos.d/google-cloud.repo` file. However, your compute instance can have this set in different repository configuration files or automation tools.

Yum repositories don't usually use GPG keys for repository validation. Instead, the `https` endpoint is trusted.

To locate and update this setting, complete the following steps:

  1. Look for the setting in your `/etc/yum.repos.d/google-cloud.repo` file.
         
         cat /etc/yum.repos.d/google-cloud.repo
         
         
         [google-compute-engine]
         name=Google Compute Engine
         baseurl=https://packages.cloud.google.com/yum/repos/google-compute-engine-el7-x86_64-stable
         enabled=1
         gpgcheck=1
         repo_gpgcheck=1
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
            https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         [google-cloud-sdk]
         name=Google Cloud SDK
         baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
         enabled=1
         gpgcheck=1
         repo_gpgcheck=1
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
            https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         
         

  2. Change all lines that say `repo_gpgcheck=1` to `repo_gpgcheck=0`.
         
         sudo sed -i 's/repo_gpgcheck=1/repo_gpgcheck=0/g' /etc/yum.repos.d/google-cloud.repo

  3. Check that the setting is updated.
         
         cat /etc/yum.repos.d/google-cloud.repo
         
         [google-compute-engine]
         name=Google Compute Engine
         baseurl=https://packages.cloud.google.com/yum/repos/google-compute-engine-el7-x86_64-stable
         enabled=1
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
            https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         [google-cloud-sdk]
         name=Google Cloud SDK
         baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
         enabled=1
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
            https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         




### Instances using OS Login return a login message after connection

On some instances that [use OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access), you might receive the following error message after the connection is established:
    
    
    /usr/bin/id: cannot find name for group ID 123456789
    

**Resolution**

Ignore the error message.

## Known issues for Windows instances

  * Support for NVMe on Windows using the Community NVMe driver is in [**Beta**](https://cloud.google.com/products#product-launch-stages), and the performance might not match that of Linux instances. The Community NVMe driver has been replaced with the Microsoft StorNVMe driver in Google Cloud public images. We recommend that you replace the NVME driver on compute instances created before May 2022 and use the Microsoft StorNVMe driver instead.
  * After you create an instance, you cannot connect to it instantly. All new Windows instances use the [System preparation (sysprep)](http://technet.microsoft.com/en-us/library/cc721940\(v=ws.10\).aspx) tool to set up your instance, which can take 5–10 mins to complete.
  * Windows Server images cannot activate without a network connection to `kms.windows.googlecloud.com` and stop functioning if they don't initially authenticate within 30 days. Software activated by the KMS must reactivate every 180 days, but the KMS attempts to reactivate every 7 days. Make sure to [configure your Windows compute instances](https://docs.cloud.google.com/compute/docs/instances/windows#licensing_for_windows_server_images) so that they remain activated.
  * Kernel software that accesses non-emulated [model specific registers](https://en.wikipedia.org/wiki/Model-specific_register) will generate general protection faults, which can cause a system crash depending on the guest operating system.
  * The `vioscsi` driver, used for SCSI disks, sets the `removable` flag, causing the disks to be treated as removable storage. This causes unexpected access restrictions in Windows to disks that are subject to Group Policy Objects (GPOs) that target removable storage.



### Guest agent fails to start on Windows Server 2012 R2 and earlier

After updating the guest agent packages on instances running legacy Windows operating systems (such as Windows Server 2012 R2, Windows Server 2012, or Windows Server 2008 R2). If you run the binary manually, then you receive an error stating that the binary isn't recognized.

Upstream Go (Golang) dropped support for Windows Server 2012 R2 and earlier versions starting in [Go 1.21](https://tip.golang.org/doc/go1.21#windows). Guest agent releases built with Go 1.21 or later can't run on these operating systems.

**Workaround**

To resolve this issue, use one of the following methods:

  * Upgrade the operating system: upgrade your VM instance to a supported version, such as Windows Server 2016 or later. For more information, see [Windows end of support](https://docs.cloud.google.com/compute/docs/images/os-details#windows_end_of_support).

  * Revert to an earlier guest agent version: if you must continue running Windows Server 2012 R2 or earlier, then reinstall compatible guest agent packages from another running compute instance or a snapshot:

    1. On the working compute instance, check the version of `google-compute-engine-windows` and `google-compute-engine-metadata-scripts` packages.
    2. Go to the `Googet` cache directory `C:\ProgramData\Googet\cache\` and copy the`.goo` files for the above packages to the broken VM.
    3. On the broken VM, install the copied over packages one-by-one with `googet install -reinstall PACKAGE_NAME.goo`.
  * To prevent the guest agent from updating to an incompatible version, disable the auto-update for the guest agent.




### Guest agent fails to start

The Windows guest agent version `20251011.00` fails to start under certain load conditions.

**Root cause** The Windows guest agent packaging for version `20251011.00` incorrectly sets the start mode of the Windows guest agent to `auto` on Windows Service Manager.

**Resolution** To resolve this issue, update your instance to use guest agent version `20251120.01` or later.

**Manual workaround** If installing version `20251120.01` is not an option, run the following command:

  * `sc.exe config GCEAgent start=delayed-auto`



### Credential management features might fail for Windows instances using non-English language names

The Windows guest agent identifies administrator accounts and groups using string matching. Therefore, credential management features only function correctly when you use English language names for user accounts and groups, for example, `Administrators`. If you use non-English language names, credential management features such as generating or resetting passwords might not function as expected.

### Windows Server 2016 won't boot on C3D machine types with 180 or more vCPUs

Windows Server 2016 won't boot on [C3D machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types) that have 180 or 360 vCPUs. To work around this issue, choose one of the following options:

  * If you need to use Windows Server 2016, then use a machine type that has less than 180 vCPUs.
  * If you need to use a C3D machine type that has 180 or 360 vCPUs, then use a later version of Windows Server.



### Windows Server 2025 and Windows 11 24h2/25h2 - Suspend and resume support

Windows Server 2025, Windows 11 24h2, and Windows 11 25h2 are unable to resume when suspended. Until this issue is resolved, the suspend and resume feature won't be supported for Windows Server 2025, Windows 11 24h2 and Windows 11 25h2.

### Errors when measuring NTP time drift using w32tm on Windows instances

For Windows instances on Compute Engine that use a VirtIO network interface, there is a known bug where measuring NTP drift produces errors when using the following command:
    
    
    w32tm /stripchart /computer:metadata.google.internal
    

The errors appear similar to the following:
    
    
    Tracking metadata.google.internal [169.254.169.254:123].
    The current time is 11/6/2023 6:52:20 PM.
    18:52:20, d:+00.0007693s o:+00.0000285s  [                  *                  ]
    18:52:22, error: 0x80072733
    18:52:24, d:+00.0003550s o:-00.0000754s  [                  *                  ]
    18:52:26, error: 0x80072733
    18:52:28, d:+00.0003728s o:-00.0000696s  [                  *                  ]
    18:52:30, error: 0x80072733
    18:52:32, error: 0x80072733
    

This bug only impacts Compute Engine instances with VirtIO NICs. Compute instances that use gVNIC network interfaces don't encounter this issue.

To avoid this issue, Google recommends using other NTP drift measuring tools, such as the [Meinberg Time Server Monitor](https://www.meinbergglobal.com/english/sw/ntp-server-monitor.htm).

### Inaccessible boot device after updating a compute instance from Gen 1 or 2 to a Gen 3 or later instance

Windows Server binds the boot drive to its initial disk interface type upon first startup. To change an existing compute instance from an older machine series ([Generation 1 or 2](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology)) that uses a SCSI disk interface to a newer machine series (Generation 3 or later) that uses an NVMe disk interface, perform a Windows PnP driver sysprep before shutting down the compute instance. This sysprep only prepares device drivers and verifies that all disk interface types are scanned for the boot drive on the next start.

From a Powershell prompt, as `Administrator`, run:
    
    
    PS C:\> start rundll32.exe sppnp.dll,Sysprep_Generalize_Pnp -wait
    

To change the machine series of a compute instance, do the following:

  1. Stop the compute instance.
  2. Edit the compute instance to use the new machine type.
  3. Start the compute instance.



If the new compute instance doesn't start correctly, then edit the compute instance to use the original machine type and then restart the instance. This sequence of steps should get your compute instance running successfully. Review the [migration requirements](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm#prepare-vm-migrate) to verify that you meet them. Then retry the instructions.

### Limited disk count attachment for machine series that use NVMe disks

Compute instances that use the NVMe disk interface and a Microsoft Windows OS image have a disk attachment limit of 16 disks for specific machine series. This limit applies to N4, C3, C3D, and M3 machine series.

Machine series such as C4, C4D, N4D, and M4 support more than 16 disks when you use a compatible NVMe driver, such as the Microsoft StorNVMe driver.

This limit does not apply to Local SSD storage. To avoid errors, consolidate your Persistent Disk and Hyperdisk storage to a maximum of 16 disks per compute instance for affected machine series.

### Replace the NVME driver on compute instances created before May 2022

If you want to use NVMe on a compute instance that uses Microsoft Windows, and the instance was created prior to May 1, 2022, you must update the existing NVMe driver in the Guest OS to use the [Microsoft StorNVMe driver](https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/nvme-features-supported-by-stornvme).

You must update the NVMe driver on your compute instance before you change the machine type to a third generation or later machine series, or before creating a boot disk snapshot that will be used to create new compute instances that use a third generation or later machine series.

Use the following commands to install the StorNVME driver package and remove the community driver, if it's present in the guest OS.
    
    
    googet update
    googet install google-compute-engine-driver-nvme
    

### Lower performance for Local SSD disks on C3 and C3D instances that run Microsoft Windows

Local SSD performance is limited for C3 and C3D instances running Microsoft Windows.

Performance improvements are in progress.

### Lower performance for Hyperdisk Extreme volumes attached to `n2-standard-80` instances running Microsoft Windows

Compute instances based on the `n2-standard-80` machine type that run Microsoft Windows can reach at most 80,000 IOPS across all Hyperdisk Extreme volumes that are attached to the instance.

**Resolution**

To reach up to 160,000 IOPS with N2 instances running Windows, choose one of the following machine types:

  * `n2-highmem-80`
  * `n2-highcpu-80`
  * `n2-standard-96`
  * `n2-highmem-96`
  * `n2-highcpu-96`
  * `n2-highmem-128`
  * `n2-standard-128`



### Poor networking throughput when using gVNIC

Windows Server 2022 and Windows 11 compute instances that use gVNIC driver GooGet package version `1.0.0@44` or earlier might experience poor networking throughput when using [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic).

To resolve this issue, update the gVNIC driver GooGet package to version `1.0.0@45` or later by doing the following:

  1. Check which driver version is installed on your compute instance by running the following command from an administrator Command Prompt or Powershell session:
         
         googet installed
         

The output looks similar to the following:
         
         Installed packages:
           ...
           google-compute-engine-driver-gvnic.x86_64 VERSION_NUMBER
           ...
         

  2. If the `google-compute-engine-driver-gvnic.x86_64` driver version is `1.0.0@44` or earlier, update the [GooGet package repository](https://github.com/google/googet) by running the following command from an administrator Command Prompt or Powershell session:
         
         googet update
         




### Large C4, C4D, and C3D vCPU machine types don't support Windows OS images

C4 machine types that have more than 144 vCPUS and C4D and C3D machine types that have more than 180 vCPUs don't support Windows Server 2012 and 2016 OS images. Larger C4, C4D, and C3D machine types that use Windows Server 2012 and 2016 OS images will fail to boot. To work around this issue, select a smaller machine type or use another OS image.

C3D instances that were created with 360 vCPUs and Windows OS images will fail to boot. To work around this issue, select a smaller machine type or use another OS image.

C4D instances that were created with more than 255 vCPUs and Windows 2025 images will fail to boot. To work around this issue, select a smaller machine type or use another OS image.

### Generic disk error on Windows Server 2016 and 2012 R2 for M3, C3, C3D, and C4D instances

**Warning:** Windows Server 2012 R2 is no longer supported and is not recommended for use. Upgrade to a [supported version of Windows Server](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server).

The ability to add or resize a Hyperdisk or Persistent Disk for a running M3, C3, C3D, or C4D instance doesn't work as expected on specific Windows guests at this time. Windows Server 2012 R2 and Windows Server 2016, and their corresponding Windows client images, don't respond correctly to the disk attach and disk resize commands.

For example, if you remove a disk from a running M3 instance, then the disk detaches, but the Windows operating system doesn't recognize that the disk is no longer available. Subsequent writes to the disk return a generic error.

**Resolution**

If you use M3, C3, C3D, or C4D instances that run on the Windows operating system and you modify a Hyperdisk or Persistent Disk volume, then for the disk modifications to be recognized, you must restart the compute instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
