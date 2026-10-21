---
url: https://docs.cloud.google.com/compute/docs/images/manage-guest-agent/
title: Configure the guest agent \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:44:42.882384+00:00
---

# Configure the guest agent  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/manage-guest-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure the guest agent Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to manage the guest agent service and configure its features by editing its configuration file.

The guest agent is a critical component of the guest environment. The guest environment contains scripts, daemons, and binaries that instances need to run on Compute Engine. For more information about the guest environment, see [Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment). While the guest agent works by default with default settings on [Google-provided OS images](https://docs.cloud.google.com/compute/docs/images/os-details), you might want to customize its behavior. For more information about guest agent core functions, see [Guest agent functionality](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions).

## Restart the guest agent

The guest agent runs as a daemon on both Linux and Windows operating systems. On Linux, the guest agent launches as a `systemd` service, and on Windows, it is a system service.

The restart steps vary between Linux and Windows operating systems as follows:

###  Linux 

To restart on Linux, choose one of the following options:

  * For guest agent version `20250901.00` or later, run the following command:
        
        ggactl_plugin coreplugin restart

  * For previous guest agent versions, run the following command:
        
        systemctl restart google-guest-agent




###  Windows 

To restart on Windows, choose one of the following options:

  * For guest agent version `20250901.00` or later, run the following command:
        
        ggactl_plugin coreplugin restart

  * For previous guest agent versions, use the following PowerShell commands:

    1. To stop the guest agent: 
           
           Stop-Service GCEAgent

    2. To start the guest agent: 
           
           Start-Service GCEAgent

Alternatively, to restart the guest agent: 
    
    Restart-Service GCEAgent




For all guest agent versions, you can also use the Task Manager: find the `GCEGuestAgent` service, and then restart it.

## Update the guest agent configuration file

You can customize the guest agent's behavior by editing its configuration file, `instance_configs.cfg`. This file lets you enable or disable features and set default values for operations.

To edit the `instance_configs.cfg` file on Linux and Windows operating systems, review the following sections.

###  Linux 

To edit the configuration file on a Linux VM, do the following:

  1. Create or edit the configuration file located at `/etc/default/instance_configs.cfg` and set the required option. For a list of options, see Configuration options.

For example, to customize how new users are created and specify which SSH host key types to generate, create or update the file with the following content:
         
         [Accounts]
         useradd_cmd = useradd -m -G google-sudoers
         [InstanceSetup]
         host_key_types = ecdsa,ed25519
         

  2. After you modify the configuration file, restart the guest agent for the changes to take effect.




### Configuration file precedence

The guest agent reads configuration settings from `/etc/default/instance_configs.cfg`, and its `.distro` and `.template` variants. These files are processed in a specific hierarchy to let users and Linux distributions set defaults. The order of precedence, from highest to lowest, is as follows:

  1. `/etc/default/instance_configs.cfg.template` (highest priority)
  2. `/etc/default/instance_configs.cfg.distro`
  3. `/etc/default/instance_configs.cfg` (lowest priority)



For example, you can define defaults in the `.template` file that overrides the base settings from both Linux distribution and guest agent package.

###  Windows 

On Windows VMs, the configuration file is located at `C:\Program Files\Google\Compute Engine\instance_configs.cfg`. For details about configuring the agent on Windows, see [Enabling and disabling Windows instance features](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#configure-windows-features).

## Configuration options

The following tables list the available configuration options for the `instance_configs.cfg` file.

### Accounts

Use the options in the `Accounts` section of the `instance_configs.cfg` file to control user and group management by the guest agent.

Option | Description | Operating system | Default value  
---|---|---|---  
`deprovision_remove` | If set to `true`, the guest agent removes the user account when you deprovision a user. By default (if set to `false`), the guest agent only removes the user from the `google-sudoers` group and deletes their SSH keys, but doesn't remove the user account. | Linux | `false`  
`groups` | A comma-separated list of groups for new users. | Linux | `adm,dip,docker,lxd,plugdev,video`  
`useradd_cmd` | Sets the command that the guest agent runs when creating a new user. For example, to create a user's home directory and add them to the `google-sudoers` group, set the value to `useradd -m -G google-sudoers`. | Linux | System default  
`userdel_cmd` | Specifies the command the guest agent runs to delete a user when `deprovision_remove` is `true`. For example, set this option to `userdel -r` to remove the user's home directory and files. | Linux | System default  
`usermod_cmd` | Sets the command that the guest agent runs when modifying a user's groups. | Linux | System default  
`gpasswd_add_cmd` | Sets the command that the guest agent runs when adding a user to a group. | Linux | System default  
`gpasswd_remove_cmd` | Sets the command that the guest agent runs when removing a user from a group. | Linux | System default  
`groupadd_cmd` | Sets the command that the guest agent runs when creating a new group. | Linux | System default  
  
### Core

Use the options in the `Core` section of the `instance_configs.cfg` file to control core functionalities of the guest agent.

Option | Description | Operating system | Default value  
---|---|---|---  
`acs_client` | If set to `false`, the guest agent's communication with the agent control plane is disabled. This disables features such as dynamic VM extensions and agent telemetry. | Linux and Windows | `true`  
`cloud_logging_enabled` | If set to `false`, the guest agent doesn't send activity logs to Cloud Logging. | Linux and Windows | `true`  
`log_file` | If you set this option, the guest agent logs to a local file. | Linux and Windows |   
`log_level` | Sets the logging level for guest agent logs. This setting applies to all logs generated by the guest agent, not just Cloud Logging. The settings and levels are as follows: 

  * `0 (FATAL)`: logs critical errors causing the agent to stop.
  * `1 (ERROR)`: logs errors that might prevent the agent from running.
  * `2 (WARN)`: logs potentially harmful conditions.
  * `3 (INFO)`: logs informational messages about agent activity. This is the default setting.
  * `4 (DEBUG)`: logs debugging information. This information can be verbose, but you can reduce the level of verbosity by using the `log_verbosity` option.

| Linux and Windows | `3`  
`log_verbosity` | Sets the logging verbosity level for `DEBUG` logs. Acceptable values are from `0` to `4`. The higher the value the more verbose the response.  | Linux and Windows | `0`  
`enable_local_plugins` | If set to `true`, the guest agent dynamically installs and starts local plugins stored in the configured local plugin directory. Available for guest agent `20260228.00` and later. | Linux and Windows | `true`  
  
### Daemons

Use the options in the `Daemons` section of the `instance_configs.cfg` file to enable or disable specific background daemons managed by the guest agent.

Option | Description | Operating system | Default value  
---|---|---|---  
`accounts_daemon` | If set to `false`, the guest agent disables [User account and SSH key management](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#user-account-ssh-key-management). | Linux | `true`  
`clock_skew_daemon` | If set to `false`, the guest agent disables [Clock synchronization](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#clock-synchronization). | Linux | `true`  
`network_daemon` | If set to `false`, the guest agent disables [Network management](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#network-management). | Linux | `true`  
  
### Instance setup

Use the options in the `InstanceSetup` section of the `instance_configs.cfg` file to control various tasks performed by the guest agent during the initial instance setup.

Option | Description | Operating system | Default value  
---|---|---|---  
`host_key_types` | A comma-separated list of host key types to generate. | Linux | `ecdsa,ed25519,rsa`  
`optimize_local_ssd` | If set to `false`, the guest doesn't optimize Local SSD on startup. | Linux | `true`  
`network_enabled` | If set to `false`, the guest agent skips instance setup functions that require metadata information. Setting this option to false also disables host key generation and prevents the guest agent from configuring the `boto` config file. | Linux and Windows | `true`  
`set_boto_config` | If set to `false`, the guest agent doesn't create or update the `boto` configuration file. Applications that use the Boto library and rely on the default guest agent configuration for Cloud Storage access might not function as expected without manual `boto` configuration. | Linux and Windows | `true`  
`set_host_keys` | If set to `false`, the guest agent skips generating host keys on firstboot. | Linux | `true`  
`set_multiqueue` | If set to `false`, the guest agent doesn't attempt to optimize network performance by enabling multiqueue features for the network drivers. When `true`, the agent configures the system to use multiple queues for network traffic, potentially improving throughput and reducing latency. | Linux | `true`  
  
### IP forwarding

Use the options in the `IpForwarding` section of the `instance_configs.cfg` file to configure how the guest agent manages IP forwarding and routing.

Option | Description | Operating system | Default value  
---|---|---|---  
`ethernet_proto_id` | The protocol ID string for daemon-added routes. | Linux | `66`  
`ip_aliases` | If set to `false`, the guest agent doesn't set up alias IP routes. | Linux | `true`  
`target_instance_ips` | If set to `false`, the guest agent doesn't enable internal IP address load balancing. | Linux | `true`  
  
### Managed Workload Identity

Use the options in the `MWLID` section of the `instance_configs.cfg` file to configure the bootstrapping of [workload identity credentials](https://docs.cloud.google.com/compute/docs/access/authenticate-workloads-over-mtls#enable-workload-id-vms).

Option | Description | Operating system | Default value  
---|---|---|---  
`enabled` |  If you set `enabled=true`, the guest agent bootstraps workload identity credentials to the following paths on the VM: 

  * Linux: `/run/secrets/workload-spiffe-credentials`
  * Windows: `C:\ProgramData\Google\ComputeEngine\secrets\workload-spiffe-credentials`

| Linux and Windows | `false`  
`credential_refresh_minutes` | The frequency, in minutes, at which workload identity credentials are refreshed. | Linux and Windows | `10` minutes  
  
### Metadata script execution

Use the options in the `MetadataScripts` section of the `instance_configs.cfg` file to control the execution of metadata scripts, such as startup and shutdown scripts.

Option | Description | Operating system | Default value  
---|---|---|---  
`default_shell` | The default shell to execute scripts. | Linux | `/bin/bash`  
`run_dir` | The base directory for metadata script execution. | Linux and Windows | Defaults to the operating system's temporary directory. For example, `/tmp` on Linux. To identify the temporary directory, you can use the `[os.TempDir()](https://pkg.go.dev/os#TempDir)` function.  
`startup` | If set to `false`, the guest agent doesn't run startup scripts from metadata. | Linux and Windows | `true`  
`shutdown` | If set to `false`, the guest agent doesn't run shutdown scripts from metadata. | Linux and Windows | `true`  
  
### Network interfaces

Use the options in the `NetworkInterfaces` section of the `instance_configs.cfg` file to control how the guest agent manages network interfaces on the VM.

Option | Description | Operating system | Default value  
---|---|---|---  
`setup` | If set to `false`, the guest agent skips network interface setup. | Linux | `true`  
`ip_forwarding` | If set to `false`, the guest agent skips IP forwarding. | Linux | `true`  
`manage_primary_nic` | If set to `true`, the guest agent manages the primary and secondary NICs. | Linux | `false`  
`dhcp_command` | The path to an alternate DHCP executable for enabling network interfaces. | Linux | Empty  
`restore_debian12_netplan_config` | If set to `true`, the guest agent recreates the Debian 12 default netplan configuration that is located at `/etc/netplan/90-default.yaml`. | Linux (Debian 12) | `true`  
`vlan_setup_enabled` | If set to `true`, the guest agent configures and manages [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics). | Linux | `false`

### OS Login

Use the options in the `OSLogin` section of the `instance_configs.cfg` file to configure the guest agent's integration with OS Login. | Option | Description | Operating system | Default value  
---|---|---|---  
`cert_authentication` | If set to `false`, the guest agent doesn't configure sshd's `TrustedUserCAKeys`, `AuthorizedPrincipalsCommand`, and `AuthorizedPrincipalsCommandUser` keys. | Linux | `true`  
  
### Plugin manager

Use the options in the `PluginConfig` section of the `instance_configs.cfg` file to configure the guest agent's plugin manager.

Option | Description | Operating system | Default value  
---|---|---|---  
`socket_connections_dir` | The directory where the plugin manager creates sockets to communicate with plugins. | Linux and Windows | 

  * Linux: `/run/google-guest-agent/plugin-connections`
  * Windows: `C:\ProgramData\Google\Compute Engine\google-guest-agent`

  
`state_dir` | The directory where the plugin manager saves plugin state and downloads its binaries. | Linux and Windows | 

  * Linux: `/var/lib/google-guest-agent`
  * Windows: `C:\ProgramData\Google\Compute Engine\google-guest-agent`

  
`local_plugin_dir` | The directory where the plugin manager looks for locally installed plugins. Available for versions `20260228.00` and later. | Linux and Windows | 

  * Linux: `/usr/lib/google/guest_agent/`
  * Windows: `C:\Program Files\Google\Compute Engine\agent`

  
`connection_type` | The type of connection that the guest agent uses to communicate with its extensions. Only the following values are supported: 

  * `uds`
  * `tcp`

This option is only available for guest agent versions `20260329.00` and later. | Linux and Windows |  `uds`  
  
## What's next

  * [View the serial port output](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output) to check the guest agent logs and troubleshoot issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
