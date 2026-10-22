---
url: https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys/
title: Predefined metadata keys \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:45.237367+00:00
---

# Predefined metadata keys  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/metadata/predefined-metadata-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Predefined metadata keys Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Predefined metadata keys and their values provide instance and project information. You can use these keys to control various instance behaviors.

When you create a new compute instance, Compute Engine automatically creates these keys for your instance on the metadata server. Compute Engine also automatically populates values for some predefined keys, such as the instance ID or project ID. For other keys, you set values to enable or disable features. For example, to activate OS login for an instance, set the `enable-oslogin` key to `TRUE`.

You can update the values of these predefined keys; key values are case-sensitive. However, you cannot modify the keys themselves. When you understand the metadata keys that are in your `instance/` and `project/` metadata directories, you can optimize instance performance, troubleshoot configurations, and maintain a reliable compute environment.

For information about how VM metadata for Compute Engine is defined, categorized, and arranged, see [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

## Predefined project metadata keys

Predefined metadata keys for project metadata are stored under the following directory:

  * `http://metadata.google.internal/computeMetadata/v1/project/`



The following table provides a list of metadata keys and directories that Compute Engine automatically creates in the `project/` metadata directory:

Metadata entry | Description  
---|---  
`attributes/` |  A directory of custom metadata values passed to the VMs in your project during startup or shutdown. These custom values can either be Google Cloud attributes or user-created metadata values. For a list of project-level Google Cloud attributes that you can set, see Project attributes. For more information about setting custom metadata, see [Set custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).  
`numeric-project-id` |  The [numeric project ID (project number)](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the instance, which is not the same as the project name that is visible in the [Google Cloud console](https://console.cloud.google.com/). This value is different from the `project-id` metadata entry value.   
`project-id` | The [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).  
  
### Predefined project attribute metadata keys

Predefined metadata keys for project attributes are stored under the following directory:

  * `http://metadata.google.internal/computeMetadata/v1/project/attributes/`



The following table provides a list of metadata keys that, if set for your project, Compute Engine creates in the `project/attributes/` metadata directory, along with its associated effect:

Metadata entry | Description  
---|---  
`disable-legacy-endpoints` |  Disables legacy metadata server endpoints for all VMs in your project. Legacy endpoints are deprecated, always set `disable-legacy-endpoints=TRUE`.   
`enable-guest-attributes` |  Sets guest attributes for the project. Guest attributes are custom VM instance metadata values that you can use to publish infrequent status notifications, low volume data, or low frequency data. These values are useful for indicating when startup scripts have finished or for providing other infrequent status notifications to other applications.  **Note:** Any user or process on your VM instance can read and write to the namespaces and keys in `guest-attributes` metadata.  For more information about guest attributes, see [Set and query guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes).   
`enable-os-inventory` |  Enables or disables OS inventory for the project. Collects and stores OS information. This includes information such as hostname, kernel version, architecture, and installed packages.  For more information about OS inventory, see [View operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).   
`enable-osconfig` |  Enables or disables VM Manager for the project. Setting `enable-osconfig` to `TRUE` enables Patch, OS policies, and OS inventory management.  For more information about enabling VM Manager, see [Set the metadata values](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-metadata).   
`osconfig-poll-interval` |  Configures the OS inventory scan interval, in minutes, for the project. By default, the OS Config agent runs an inventory scan on each VM every 10 minutes.  For more information about configuring the scan interval, see [Configure the OS inventory scan interval](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/view-os-details#configure-scan-interval).   
`enable-oslogin` |  Enables or disables SSH key management on your project. For more information about OS Login, see [Set up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).   
`enable-windows-ssh` |  **Preview** This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages).  Enables or disables SSH for Windows VMs. For more information, see [Connect to Windows VMs using SSH](https://docs.cloud.google.com/compute/docs/connect/windows-ssh).   
`google-compute-default-data-protection` | If set, stores the default option that is used to back up new instances created in the project. For more information, see [Configure the default backup setting for the console](https://docs.cloud.google.com/compute/docs/disks/default-backup).  
`google-compute-default-region` | If set, stores the default region that is used by the project.  For more information about setting default regions, see [Default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-region-zone).   
`google-compute-default-zone` | If set, stores the default zone that is used by the project.  For more information about setting default zones, see [Default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-region-zone).   
`ssh-keys` |  If you are [managing SSH keys using metadata](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys), this attribute lets you configure public SSH keys that can connect to VMs in this project. If there are multiple SSH keys, each key is separated by a newline character (`\n`). The value of the `ssh-keys` attribute is a string. **Example:** `"user1:ssh-rsa mypublickey user1@host.com\nuser2:ssh-rsa mypublickey user2@host.com"` SSH keys managed by [OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) aren't visible in metadata.   
`sshKeys` | **Deprecated:** Use `ssh-keys`.   
`vmdnssetting` |  Enable zonal DNS and global DNS for the VMs in your project. For more information about using zonal DNS names for your VMs, see [Use Zonal DNS for your internal DNS type](https://docs.cloud.google.com/compute/docs/networking/zonal-dns).   
  
## Predefined instance metadata keys

Predefined metadata keys for instance metadata are stored under the following directory:

  * `http://metadata.google.internal/computeMetadata/v1/instance/`



The following table provides a list of metadata keys and directories that Compute Engine automatically creates in the `instance/` metadata directory:

Metadata entry | Description  
---|---  
`attributes/` |  A directory of custom metadata values passed to the VM during startup or shutdown. These custom values can either be Google Cloud attributes or user-created metadata values. For a list of instance-level Google Cloud attributes that you can set, see Instance attributes For more information about setting custom metadata, see [Set custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).  
`cpu-platform` |  CPU platform of the VM. For information about CPU platforms, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
`description` |  The free-text description of an instance that is assigned using the `--description` flag by using the Google Cloud CLI or the API.   
`disks/` | A directory of disks that are attached to the VM. For each disk, the following information is available:

  * `device-name`
  * `index`
  * `interface`
  * `mode`
  * `type`

For more information about disks, see [Storage options](https://docs.cloud.google.com/compute/docs/disks).   
`gce-workload-certificates/` (**Deprecated**) | Stores the following endpoints for the managed workload identities feature used by applications running in the VM.

  * `config-status`: Contains any errors in the configuration values provided through the VM metadata.
  * `workload-identities`: Contains the identities managed by the Compute Engine control plane. This endpoint contains the X.509 certificate and the private key for the VM's trust domain.
  * `trust-anchors`: Contains a set of trusted certificates for peer X.509 certificate chain validation.

For more information, see [Authenticate workloads to other workloads over mTLS](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls).   
`guest-attributes/` | Sets guest attributes for the VM. These custom values can either be Google Cloud attributes or user-created metadata values. For a list of instance-level Google Cloud attributes that you can set, see Instance guest attributes **Note:** Any user or process on your VM instance can read and write to the namespaces and keys in `guest-attributes` metadata.  For more information about guest attributes, see [Set and query guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes).   
`hostname` | The hostname of the VM.  
`id` |  The ID of the VM. This is a unique, numerical ID generated by Compute Engine for your project and the zone of the VM. You can use this ID to identify your VM, especially if you haven't assigned a custom name to the VM.   
`image` | The operating system image used by the VM. This value has the following format: `projects/IMAGE_PROJECT/global/images/IMAGE_NAME`.  
`legacy-endpoint-access/` |  Stores the list of legacy endpoints. Values are `0.1` and `v1beta1`.   
`licenses/` |  A list of license code IDs that are used to attach the licenses to images, snapshots, and disks.   
`machine-type` |  The machine type for this VM. This value has the following format: `projects/PROJECT_NUM/machineTypes/MACHINE_TYPE`  
`maintenance-event` |  Indicates whether a maintenance event is affecting this VM. For more information, see [Live migrate](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#live_migrate).   
`name` |  The name of the VM.   
`network-interfaces/` | A directory of network interfaces. For each network interface the following information is available:

  * `access-configs/`: Directory containing access configurations for this interface. Only `0/` is supported, which contains details for a one-to-one NAT access config. Under `access-configs/0/`: 
    * `external-ip`: The external IP address of this interface.
    * `type`: The type of access configuration. `ONE_TO_ONE_NAT` is the only value provided at this time.
  * `dns-servers`: A list of DNS name servers for this interface.
  * `forwarded-ips/`: Directory containing IPs forwarded to this instance by using load balancing or protocol forwarding. Each entry is an IP address.
  * `forwarded-ipv6s/`: Directory containing IPv6 CIDR ranges forwarded to this instance by using load balancing or protocol forwarding. Each entry is an IPv6 CIDR range.
  * `gateway`: The gateway address for this network interface.
  * `gateway-ipv6`: The IPv6 gateway address for this network interface.
  * `ip`: The assigned internal IP address for this network interface.
  * `ip-aliases/`: Directory containing IP alias ranges assigned to this network interface. Each entry is an IP alias range.
  * `ipv6`: A list of IPv6 CIDR ranges assigned to the network interface.
  * `ipv6s`: A list of IPv6 addresses or prefixes assigned to the network interface.
  * `mac`: The MAC address for this network interface.
  * `mtu`: The MTU for this network interface.
  * `network`: The network for this interface, in `projects/PROJECT_ID/networks/NETWORK_NAME` format.
  * `subnetmask`: The subnet mask for this network interface.
  * `target-instance-ips`: The list of internal IP addresses of forwarding rules that are targeting this instance.

For more information about network interfaces, see [Multiple network interfaces overview](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).   
`partner-attributes/` (**Deprecated**) |  A directory containing namespaces within which metadata entries are stored. The namespaces are created by Google Cloud services, which use partner-attributes to store their configurations. When there are no services using the partner-attributes, the directory is empty.  For example, [managed workload identities](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#configure_identities) use partner-attributes for its configurations.   
`preempted` | A boolean value that indicates whether a VM is about to be preempted.  
`scheduling/` |  Sets the scheduling options for the VM. Scheduling metadata values include the following:

  * `on-host-maintenance`: indicates whether the VM terminates or live migrates during host maintenance.
  * `automatic-restart`: If this value is `TRUE`, the VM automatically restarts after a maintenance event or crash.
  * `preemptible`: If this value is `TRUE`, the VM is preemptible. This value is set when you create a VM, and it can't be changed.

For more information about scheduling options, see [Set instance availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).   
`service-accounts/` |  A directory of service accounts associated with the VM. For each service account, the following information is available:

  * `aliases`
  * `email`: The email address for the service account.
  * `identity`: A JSON Web Token that is unique to the VM. You must include the `audience` parameter in your request for this VM metadata value. For example, `?audience=http://www.example.com`.  For information about how to request and verify instance identity tokens, see [Verify VM identity](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity).
  * `scopes`: The access scopes assigned to the service account.
  * `token`: The `OAuth2` access token that can be used to authenticate applications.  For information about access tokens, see [ Authenticating applications directly with access tokens](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#applications).

For more information about how Compute Engine uses service accounts, see [Service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts).   
`tags` |  Lists any network tags associated with the VM. For more information about network tags, see [Add network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).  
`virtual-clock/drift-token` | The accumulated drift of the VM clock. Initialized to zero during instance creation and increased by the accumulated clock skew as the VM [live migrates](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).  
`zone` | The zone where this VM is located. This value has the following format: `projects/PROJECT_NUM/zones/ZONE`  
  
### Predefined instance attribute metadata keys

Predefined metadata keys for instance attributes are stored under the following directory:

  * `http://metadata.google.internal/computeMetadata/v1/instance/attributes/`



The following table provides a list of metadata keys that, if set for your instance, Compute Engine creates in the `instance/attributes/` metadata directory, along with its associated effect:

Metadata entry | Description  
---|---  
`physical_host_topology` |  A hash string that represents the physical location of a VM within a zone. For more information about this attribute, see [Verify the physical location of a VM](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology).   
`enable-osconfig` |  Enables or disables VM Manager for the VM. Setting `enable-osconfig` to `TRUE` enables Patch, OS policies, and OS inventory management.  For more information about enabling VM Manager, see [Set the metadata values](https://docs.cloud.google.com/compute/vm-manager/docs/setup#enable-metadata).   
`osconfig-poll-interval` |  Configures the OS inventory scan interval, in minutes, for the VM. By default, the OS Config agent runs an inventory scan on each VM every 10 minutes.  For more information about configuring the scan interval, see [Configure the OS inventory scan interval](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/view-os-details#configure-scan-interval).   
`enable-oslogin` |  Enables or disables SSH key management on your VM. For more information about OS Login, see [Set up OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access).   
`enable-windows-ssh` ([Preview](https://cloud.google.com/products/#product-launch-stages)) |  Enables or disables SSH for Windows VMs. For more information, see [Connect to Windows VMs using SSH](https://docs.cloud.google.com/compute/docs/connect/windows-ssh).   
`enable-workload-certificate` (**Deprecated**) |  Enables or disables managed workload identities on a VM. For more information, see [Enable managed workload identities for individual VMs](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#enable-workload-id-vms).  
`vmdnssetting` |  Enable zonal DNS and global DNS for the VM. For more information about using zonal DNS names for your VMs DNS, see [Use Zonal DNS for your internal DNS type](https://docs.cloud.google.com/compute/docs/networking/zonal-dns).   
`ssh-keys` |  If you are [managing SSH keys using metadata](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys), this attribute lets you configure public SSH keys that can connect to VMs in this project. If there are multiple SSH keys, each key is separated by a newline character (`\n`). The value of the `ssh-keys` attribute is a string. **Example:** `"user1:ssh-rsa mypublickey user1@host.com\nuser2:ssh-rsa mypublickey user2@host.com"` SSH keys managed by [OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) aren't visible in metadata.   
`block-project-ssh-keys` |  Block project SSH keys from VMs that use metadata-based SSH keys. For more information, see [ Restrict SSH keys from VMs](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys#block-keys).  
`disable-https-mds-setup` |  Disables automatic HTTPS Metadata Server certificate provisioning by Compute Engine. For more information, see [ Enable automatic certificate setup](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds-disabling-certificate-setup).  
`enable-https-mds-native-cert-store` |  Enables Compute Engine to add the root certificate to the OS trust store during automatic HTTPS Metadata Server certificate provisioning. For more information, see [ Enabling root certificate storage in OS trust store](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds-trust-store).  
  
### Predefined guest attribute metadata keys

Predefined metadata keys for instance guest attributes are stored under the following directory:

  * `http://metadata.google.internal/computeMetadata/v1/instance/guest-attributes/`



The following table provides a list of metadata keys and directories that Compute Engine automatically creates in the `instance/guest-attributes/` metadata directory:

Metadata entry | Description  
---|---  
`guestInventory/` |  Stores OS inventory for the VM. Collects and stores OS details information. This includes information such as hostname, kernel version, architecture, and installed packages details.  For more information about OS inventory, see [View operating system details](https://docs.cloud.google.com/compute/docs/instances/view-os-details).   
`hostkeys/` |  Stores SSH host keys. Host keys can be used to identify a particular host or machine.  For information host keys, see [Storing host keys by enabling guest attributes](https://cloud.google.com/solutions/connecting-securely#storing_host_keys_by_enabling_guest_attributes).   
  
## What's next?

  * Learn more about [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).
  * Learn how to [set custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).
  * Learn how to [set and query guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes).
  * Learn how to [view and query VM metadata](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
