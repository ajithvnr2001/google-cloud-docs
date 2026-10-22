---
url: https://docs.cloud.google.com/compute/docs/images/guest-agent-functions/
title: Guest agent functionality \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:36.933474+00:00
---

# Guest agent functionality  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/guest-agent-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Guest agent functionality Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes the architecture and core functionality of the guest agent. Use this information to understand how the agent manages instance setup, network interfaces, metadata scripts, and user accounts to help maintain the health and performance of your Compute Engine instances. The guest agent is a core component of the [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment), which contains the scripts, daemons, and binaries that compute instances need to run on Compute Engine.

## How the guest agent works

Starting with version `20250901.00`, the guest agent uses a plugin-based architecture. This design improves reliability and flexibility by separating the agent's functions into distinct components.

The guest agent architecture consists of a few key components:

  * **Guest agent manager** : the central process on your instance that starts, stops, and monitors all plugins.
  * **Core plugin** : this plugin handles the essential services your instance needs to run on Google Cloud. Its functionality cannot be disabled.
  * **Extensions (Optional plugins)** : these are plugins that integrate your instance with other Google Cloud services, such as Cloud Monitoring. You can control which of these plugins run on your instance by using [VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).
  * **VM Extension Manager** : this is a managed Google Cloud service that runs on Google's backend infrastructure and manages the lifecycle of optional plugins, including their installation and updates.



For more information about the guest agent architecture, see [About guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

### Startup sequence and dependencies

The guest agent manager follows a specific startup sequence to ensure that the instance is correctly set up to run on Compute Engine. Immediately after the process starts, the agent manager launches the core plugin, a specialized component that handles foundational guest environment tasks.

###  Linux 

On Linux instances, the guest agent runs as a systemd service named `google-guest-agent-manager.service`. The startup sequence follows these steps:

  1. **Sets up network dependency** : the `google-guest-agent-manager.service` starts after the `network-online.target` systemd target. This ensures basic network connectivity before the agent communicates with the [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview) or perform other configuration steps. For implementation details, see the [google-guest-agent-manager.service unit configuration file](https://github.com/GoogleCloudPlatform/guest-agent/blob/main/google-guest-agent-manager.service).
  2. **Sends ready notification** : the guest agent runs its minimum required set up steps and then uses `systemd-notify --ready` to inform the system that it is fully operational and ready to serve other components. The agent performs the following minimum required setup steps: 
     * Network setup
     * MDS credentials bootstrapping
     * Initial host key setup



###  Windows 

On Windows instances, the guest agent runs as a Windows service named `GCEAgentManager`. The startup sequence follows these steps:

  1. **Enables delayed startup** : the service startup type is set to [Automatic (Delayed Start)](https://learn.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-service_delayed_auto_start_info). This allows the core operating system services to initialize first, reducing resource contention during the initial boot phase. For implementation details, see the [service installation script](https://github.com/GoogleCloudPlatform/guest-agent/blob/main/packaging/googet/agent_install.ps1).
  2. **Sets service status** : the agent runs its minimum required set up and then sets service status [`SERVICE_RUNNING`](https://learn.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-service_status) to inform the system that it is fully operational and ready to serve other components. The agent performs the following minimum required setup steps: 
     * Network setup
     * MDS credentials bootstrapping



#### Best practices for dependent processes

If you have custom services or scripts that depend on guest agent features, such as MDS credential bootstrapping, you must define an explicit startup dependency to ensure they execute only after the agent is active.

###  Linux 

Add a dependency on the guest agent systemd service in your unit file like:
    
    
    [Unit]
    After=google-guest-agent-manager.service
    

###  Windows 

Add a dependency on the guest agent windows service using [service control](https://learn.microsoft.com/en-us/windows/win32/services/controlling-a-service-using-sc) like:
    
    
    sc config "CustomService" depend= "GCEAgentManager"
    

## Core functionality

The core plugin is responsible for the fundamental services that your instance needs to function on Compute Engine. The following section details the functions that the core plugin provides. You can customize many of these features by using the [guest agent configuration file](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#update-guest-agent-config).

### Initial instance setup and optimizations

The guest agent performs several setup tasks to prepare the instance for running on Compute Engine. As shown in the following table, some tasks run only on the first boot, while others run on every startup.

Task | Default path | Frequency  
---|---|---  
Generate SSH host keys | `/etc/ssh/ssh_host_type_key` and `.pub`. Default types include `ecdsa`, `ed25519`, and `rsa`. | On first boot (Linux only)  
Create the `boto` config for using Cloud Storage | `/etc/boto.cfg` | On first boot (Linux only)  
Store unique instance ID |  Linux: `/etc/google_instance_id`  
Windows: `C:\ProgramData\Google\Compute Engine\google-guest-agent\google_instance_id` | On first boot  
Optimize for local SSD | Configured using system IO scheduler settings in `/sys/block/dev/queue/scheduler`, where dev is the device name (for example, `nvme0n1` or `sdb`). | On every startup (Linux only)  
Enable multi-queue on all `virtionet` devices | None | On every startup  
  
You can control these setup tasks by configuring the [`InstanceSetup` options](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#instancesetup) of the guest agent configuration file. For example, you can disable Local SSD optimization by setting `optimize_local_ssd = false`.

### System telemetry collection

The guest agent records some basic system telemetry information at boot time and then at regular intervals, at least every 24 hours. The information recorded includes the following:

  * Guest agent version and architecture
  * Operating system name and version
  * Operating system kernel release and version
  * Supported independent software vendor (ISV) application running on the compute instance and its recognized version

#### Supported ISV applications

    * Apache Cassandra
    * Apache Hadoop
    * Apache Spark
    * Apache Web Server
    * Citrix Cloud Connector
    * Citrix Delivery Controller
    * Citrix StoreFront
    * Citrix Virtual Delivery Agent
    * EDB Postgres
    * EDB Postgres Advanced Server (EPAS)
    * Kubernetes
    * MariaDB
    * Memcached
    * Microsoft Active Directory
    * Microsoft Message Queuing (MSMQ)
    * Microsoft SQL Server
    * MongoDB
    * MySQL
    * Oracle Data Guard
    * Oracle Database
    * Oracle E-Business Suite
    * Oracle GoldenGate
    * Oracle JD Edwards EnterpriseOne
    * Oracle PeopleSoft
    * Oracle WebLogic Server
    * PostgreSQL
    * Red Hat OpenShift
    * Redis
    * SAP Gateway
    * SAP HANA
    * SAP HANA Studio
    * SAP IQ
    * SAP NetWeaver ABAP
    * SAP NetWeaver ASCS
    * SAP NetWeaver Enqueue Replicator
    * SAP NetWeaver Java
    * SAP Web Dispatcher
    * SUSE Pacemaker




You can disable telemetry collection by setting the metadata key `disable-guest-telemetry` to `true`. To set metadata, see [Set and remove custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).

### Clock synchronization (Linux only)

To ensure accurate timekeeping, the guest agent uses the `clock_skew_daemon` component to periodically correct the clock on your instance to match the physical server it runs on. This process prevents a problem called _clock skew_ and generates a `system time has changed` message in your instance logs, which confirms the time was successfully synchronized.

If enabled, the agent normally synchronizes the clock after a stop or start event, or after a migration. However, if the real-time clock (RTC) on your instance is configured to use the local timezone instead of UTC, the agent automatically detects this configuration and disables clock synchronization to prevent potential inconsistencies.

The agent performs the re-synchronization by running the following command: `/sbin/hwclock --hctosys -u --noadjfile`.

You can disable the `clock_skew_daemon` component by setting [`clock_skew_daemon = false`](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#daemons) in the guest agent configuration file.

### Metadata script execution

You can use [startup scripts](https://docs.cloud.google.com/compute/docs/startupscript) and [shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript) to perform automated tasks each time your instance starts or stops.

The guest agent helps with the running of these scripts as follows:

  * Executes scripts in a shell.
  * If you specify multiple scripts (for example, if using both `startup-script` and `startup-script-url`), the agent runs both.
  * When multiple scripts are provided for the same event, the agent executes the script from the URL first.
  * After a script finishes, the agent logs its exit status.



You can configure the execution of metadata scripts by modifying the [`MetadataScripts` options](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#metadatascripts) in the guest agent configuration file.

### User account and SSH key management

The guest agent uses an [`accounts_daemon`](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#daemons) to manage local user accounts and SSH keys, which control access to the instance. The specific behavior varies between Linux and Windows operating systems.

You can modify accounts management options by configuring the [`Accounts` options](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#accounts) in the guest agent configuration file.

###  Linux 

OS Login is used to manage SSH access to your instances using IAM without having to create and manage individual SSH keys. For more information about OS Login, see [OS Login](https://docs.cloud.google.com/compute/docs/oslogin). On Linux instances if OS Login isn't enabled, the agent creates and manages local user accounts and their SSH keys by using metadata settings.

When you [add or remove SSH Keys](https://docs.cloud.google.com/compute/docs/instances/adding-removing-ssh-keys) from instance or project metadata, the guest agent creates or deletes a local user account. The guest agent also performs the following actions to manage these local user accounts:

  * Maintains the `authorized_keys` file (`~/.ssh/authorized_keys`) for each user account it manages as follows: 
    * When you add SSH keys to metadata, the agent creates an `authorized_keys` file for the user account.
    * When you remove all SSH keys for a user from metadata, the agent deletes that user account's `authorized_keys` file.
  * Manages administrator privileges by using the `google-sudoers` Linux group. Any members of this group receive sudo permissions on the instance. Sudo policies are configured in `/etc/sudoers.d/google_sudoers`.
  * Adds all the user accounts it provisions to the `google-sudoers` group.
  * Adds user accounts to any additional Linux groups that you specify in the [`groups`](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#accounts) option of the guest agent configuration file.



###  Windows 

On Windows instances, the agent automatically creates local user accounts for any SSH user account specified in the metadata SSH keys at the instance or project level. The guest agent also handles [creating user accounts and setting or resetting passwords](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances). These local user accounts are needed for [connecting to Windows instances using SSH](https://docs.cloud.google.com/compute/docs/connect/windows-ssh).

**Note:** Active Directory (AD) Domain Controller doesn't use the local user account database except when it is booted into the recovery console, so any account created on the system would become an administrator of the Active Directory Domain.

You can prevent unintended AD user provisioning by [disabling the account manager](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#disable_the_account_manager) on the AD controller instance. For more information on setting up AD on Compute Engine, see [deploy domain controllers](https://docs.cloud.google.com/architecture/deploy-an-active-directory-forest-on-compute-engine#deploy_domain_controllers).

### OS Login configuration (Linux only)

OS Login is used to manage SSH access to your instances using IAM without having to create and manage individual SSH keys. For more information about OS Login, see the [OS Login documentation](https://docs.cloud.google.com/compute/docs/oslogin).

When you [enable OS Login](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access), the guest agent is responsible for configuring the instance to use OS Login.

The guest agent configures [OS Login](https://docs.cloud.google.com/compute/docs/oslogin) by completing the following tasks:

  * Adds a Google config block to the [OpenSSH daemon configuration file](https://man7.org/linux/man-pages/man5/sshd_config.5.html) (`/etc/ssh/sshd_config`) and restarts `SSHD`.
  * Adds OS Login entries to the [Name Service Switch configuration file](https://man7.org/linux/man-pages/man5/nsswitch.conf.5.html) (`/etc/nsswitch.conf`).
  * Adds OS Login entries to the [PAM configuration file](https://man7.org/linux/man-pages/man5/pam.d.5.html) (`/etc/pam.d/sshd`) for `SSHD`.
  * Adds configuration for [PAM group management](https://man7.org/linux/man-pages/man5/group.conf.5.html) into `/etc/security/group.conf`.
  * Creates the SSH trusted CA [named pipe](https://man7.org/linux/man-pages/man3/mkfifo.3.html) `/etc/ssh/oslogin_trustedca.pub`.
  * Sets up the authorized [sudoers file](https://man7.org/linux/man-pages/man5/sudoers.5.html) at `/etc/sudoers.d/google-sudoers` and creates the `/var/google-sudoers.d` and `/var/google-users.d` directories.



If you disable OS Login, the configuration changes are removed. The options under the `Accounts` section of the `SSHD` configuration file don't apply to OS Login users.

### Network management

The guest agent automatically configures your instance's network interfaces on boot. It reads the network configuration from the metadata server to ensure your instance connects to the network correctly and can access other Google Cloud services.

You can control the agent's network management behavior by configuring the [`NetworkInterfaces` options](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#networkinterfaces) in the guest agent configuration file. For example, you can set the `manage_primary_nic = true` option to have the agent manage the primary network interface card (NIC) in addition to secondary NICs.

On every boot, the guest agent performs the following key tasks:

  * **Enables network interfaces** : the agent detects the active network manager on your OS and uses it to enable all secondary network NICs.
  * **Configures IP routes** : the agent sets up the necessary IP (IPv4 only) routes for features like IP forwarding and alias IP ranges as follows: 
    * Sets routes on the primary ethernet interface.
    * Configures Google routes by default, with the routing protocol ID `66`. This ID is a namespace for guest agent configured IP addresses. This ID can be changed by using the [`ethernet_proto_id`](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#ipforwarding) option in the guest agent configuration file.
  * **Creates a route to the metadata server** : the agent ensures that your primary NIC can always communicate with the metadata server to get instance information.
  * **VLAN configuration** : If your instance is configured to connect to a [Virtual Local Area Network (VLAN)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments), the guest agent automatically handles the setup. It reads the VLAN configuration from the metadata server and configures the network interface inside the instance to use the correct VLAN tag. This ensures the instance communicates on the intended logical network. Importantly, if the VLAN is attached to the primary NIC, the guest agent configures it even if `manage_primary_nic` is disabled.



#### Network manager selection

On Linux, the guest agent automatically detects which network manager is available on the system and uses it to configure the network interfaces. The agent checks for supported managers in order of priority, from `netplan` to `dhclient`.

The following table lists the supported network managers, organized by the operating system they are most commonly associated with by default. Your specific instance configuration can differ, but this table reflects the default network manager for the listed operating systems.

**Note:** Ubuntu 18.04 includes an outdated version of `networkctl` that is incompatible with the guest agent. To ensure reliable network configuration, the agent intentionally falls back to using `dhclient` on Ubuntu 18.04, even if `netplan` is present.Network manager | Operating system | Configuration location | Example path | Notes  
---|---|---|---|---  
`netplan` | 

  * Debian 12 or later
  * Ubuntu 20.04 or later

| `/run/netplan/` | `/run/netplan/20-google-guest-agent-eth0.yaml` | The agent may also use a drop-in location at `/etc/systemd/network/`  
`wicked` | 

  * SLES

| `/etc/sysconfig/network/` | `/etc/sysconfig/network/ifcfg-eth0` | Existing `ifcfg` files are not overwritten and are skipped instead.  
`NetworkManager` | 

  * CentOS
  * RHEL
  * Rocky Linux

| `/etc/NetworkManager/system-connections/` | `/etc/NetworkManager/system-connections/google-guest-agent-eth0.nmconnection` |   
`systemd-networkd` | 

  * Debian

| `/usr/lib/systemd/network/` | `/usr/lib/systemd/network/20-eth0-google-guest-agent.network` |   
`dhclient` | 

  * Debian 11 or earlier
  * Ubuntu 18.04 or earlier

| `/run/` | `/run/dhclient.google-guest-agent.eth0.ipv4.pid` | If none of the other network managers are detected, the guest agent defaults to using `dhclient`.  
**Important:** After writing the network configuration to disk in the locations described earlier, the agent executes a network reload to apply the changes. It automatically runs the appropriate command for the VM's active network manager (e.g., `nmcli conn reload` or `networkctl reload`). This reload operation may flush ephemeral routes. If you require custom routes, ensure they are configured to be persistent or implement automation to restore them if they are removed.

### Secure metadata server (MDS) credential management

[Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) now support secure communication with the metadata server by using the HTTPS endpoint `https://metadata.google.internal/computeMetadata/v1`. This enhancement provides a more secure channel for metadata access.

To enable this secure communication, the guest agent retrieves and stores necessary credentials on the instance's disk. These credentials are saved in a standard location, making them accessible to any client application running on the instance. To review these locations, see [Where are certificates stored](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds-certificates).

HTTPS MDS certificates are enabled by default starting with version `20260228.00` of the guest agent. On earlier versions of the guest agent, to automatically set up HTTPS MDS certificates on your Shielded VMs, set the `disable-https-mds-setup` metadata key to `false` on your instance or project. To set metadata, see [Set and remove custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).

Credential management by the guest agent includes:

  * **Initial update** : both the root certificate and client credentials are updated whenever the guest agent process starts.
  * **Automatic refresh** : for enhanced security, the guest agent automatically refreshes client credentials every 48 hours.
  * **Overlap period** : the agent generates and saves new credentials while the old ones remain valid. The overlap period ensures clients have sufficient time to transition to the new credentials before the old ones expire. This overlap period also allows the agent to retry credential acquisition in case of failure, ensuring valid credentials are in place before existing ones become invalid.
  * **Composition** : the guest agent ensures the client credentials consist of an EC (Elliptic Curve) private key concatenated with the client certificate.
  * **Uniqueness** : the guest agent ensures credentials are unique to an instance and can't be used elsewhere.



For more information on HTTPS metadata server endpoint, see [About the HTTPS metadata server endpoint](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds).

By default, the guest agent writes certificates directly to disk. However, you can configure the agent to integrate certificates into the operating system's built-in certificate stores. To enable this integration, set the `enable-https-mds-native-cert-store` metadata key to `true`. To set metadata, see [Set and remove custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).

The agent's behavior for adding certificates to OS trust stores varies by OS as follows:

###  Linux 

The guest agent performs the following steps:

  1. Adds the MDS root certificate to the system's trust store. The specific path depends on the OS distribution. To review these locations, see [Root certificate storage in OS trust store](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds-trust-store).
  2. Updates the local trust store by running the appropriate command for the OS, such as `update-ca-certificates` or `update-ca-trust`.



###  Windows 

The agent adds client credentials to `Cert:\LocalMachine\My` and the root certificate to `Cert:\LocalMachine\Root`.

**Note:** As documented by Microsoft in [Enable LDAP over SSL 3rd Certification Authority](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/enable-ldap-over-ssl-3rd-certification-authority#possible-issues), there could be issues with LDAPS process when multiple certificates are added in personal store. Avoid enabling OS built-in stores on Domain Controllers. Credentials can still be used from disk if required.

### Windows failover cluster support (Windows only)

The guest agent monitors the active node in the [Windows Server Failover Cluster](https://docs.cloud.google.com/compute/docs/tutorials/running-windows-server-failover-clustering) and coordinate with Google Cloud internal load balancer to forward all cluster traffic to the expected node.

You can control this behavior by using the following fields in instance metadata or in the [`instance_configs.cfg`](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#update-guest-agent-config) file:

  * `enable-wsfc`: when set to `true`, the agent ignores all IP forwarding information and starts responding to the health check port. The default setting is `false`.
  * `wsfc-agent-port`: specifies the port where the agent responds to health checks. The default setting is `59998`.
  * `wsfc-addrs`: a comma-separated list of IP addresses. This advanced setting lets you have both normal forwarding IPs and cluster IPs on the same instance. When you set this, the agent only skips auto-configuration for the IPs in this list. By default, this value is not set.



## What's next

  * To learn how to manage the guest agent, see [Configure guest agent](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
