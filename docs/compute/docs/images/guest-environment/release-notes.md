---
url: https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes/
title: Guest environment release notes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:15.080218+00:00
---

# Guest environment release notes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Guest environment release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents updates to the guest environment, which is a set of scripts, daemons, and binaries that read metadata server content to ensure instances function correctly on Compute Engine. The central component of the guest environment is the guest agent, which handles tasks like account management, OS Login integration, and network interface management. For more information about the guest environment, see [Guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment). 

Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/guestenvironment-release-notes.xml) directly. 

## October 05, 2026

Feature

Version `20260921.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for all supported operating systems. This version introduces the following features:

  * The managed workload identity certificate refresher is now a locally bundled extension. For more information, see [Managed workload identities overview](https://docs.cloud.google.com/iam/docs/managed-workload-identity).
  * The guest telemetry extension is updated to version 1.1 and polls every 15 minutes instead of every 24 hours. However, it will only send data to the API every 24 hours, unless it detects a change in the system since the previous poll. The extension supports the following capabilities: 
    * Running a command as the user associated with a discovered process.
    * Configuring regular expressions to match against the version command output.



Fixed

Version `20260921.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for all supported operating systems. This version introduces the following fixes:

  * The `NetworkManager` setup now no longer reloads the primary NIC when it applies changes to the network configuration of secondary NICs, unless necessary.
  * If the core plugin successfully rolls back any configurations, then it force-reloads the configurations to make sure that the instance re-obtains DHCP leases for secondary NICs.
  * The core plugin now respects the `address-manager` configuration flag and the corresponding metadata attribute.
  * The extensions manager now ignores install and remove requests from ACS for the core plugin and locally bundled extensions.
  * The extensions manager no longer logs that there are no local plugins to install when it's installing local plugins.
  * The metadata script runner now respects the `sysprep_specialize` configuration flag.



## August 03, 2026

Fixed

Version `20260717.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for Windows only. This version introduces the following fix:

  * Fixed a race condition in the extensions manager during Windows shutdown that could cause an incorrect state on the next boot. This occurred when the Service Control Manager (SCM) attempted to restart the extensions manager after it received an early termination signal.



## July 27, 2026

Fixed

Version `20260716.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for all supported operating systems. This version introduces the following fixes:

  * The `systemctl start` operations performed by the OS Login module no longer leave behind zombie processes.
  * The extensions monitor, which monitors the health of extensions that the guest agent manages, no longer logs an error when it reads an empty log file from an extension.
  * Dependency updates address multiple high-severity CVEs, such as [CVE-2026-39830](https://www.cve.org/CVERecord?id=CVE-2026-39830) and [CVE-2026-39832](https://www.cve.org/CVERecord?id=CVE-2026-39832).



## May 20, 2026

Fixed

Version `20260511.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for all supported operating systems. This is a rebuild of version `20260423.01` announced in the [April 27, 2026 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#April_27_2026). It includes no additional changes and is released specifically to trigger a guest agent restart.

Between May 4, 2026, and May 11, 2026, the control plane accidentally sent an erroneous request to remove the core plugin. This caused the agent to stop functioning, which disrupted features that rely on it, such as SSH and Windows password resets. This package update automatically restarts the agent on instances where auto-update is enabled to resolve the issue.

## April 27, 2026

Fixed

Version `20260423.01` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for all supported operating systems. This version includes the following fixes:

  * Updates the guest agent Go dependencies to address security vulnerabilities.
  * Ensures that the internal initialization is complete before signaling readiness to systemd. This fix resolves an issue in version `20260329.00` where dependent services like SSH failed to start due to missing host keys.



## March 30, 2026

Feature

Version `20260329.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for all supported operating systems. This version introduces the following features:

  * A new local extension, guest telemetry, is introduced, which collects important telemetry data about Independent Software Vendors (ISVs) running on a compute instance. For more information about the telemetry the guest agent collects, see [System telemetry collection](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#system-telemetry-collection).
  * The `enable_local_plugins` configuration now defaults to `true`.
  * A new configuration flag `connection_type` is introduced to the `PluginConfig` section of the guest agent configuration file. This option forces a specific connection type when the guest agent connects to the extensions it is managing. Supported connection types are UDS and TCP.



Fixed

Version `20260329.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for all supported operating systems. This version introduces the following fixes:

  * The guest agent no longer terminates abruptly when an extension's gRPC client is null. Instead, it logs an error.
  * The credentials setup for HTTPS access to the metadata server was moved to prevent it from blocking the guest agent's readiness signal. This mitigates an issue on machines without vTPM, where the guest agent can take an extra 10 seconds to signal that it's ready.
  * The core plugin now logs during the startup phase to provide a better signal on when it's started.
  * Locally bundled extensions are now direct child processes of the agent manager process. This helps resolve an issue where plugins remain as running processes but fail to start correctly.



## March 05, 2026

Feature

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for Debian 12, AlmaLinux 9, CentOS Stream 9, Oracle Linux 9, Red Hat Enterprise Linux 9, and Rock Linux 9. To review the features and fixes included in version `20260228.00` of the guest agent, see the [March 2, 2026 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#March_02_2026).

## March 04, 2026

Feature

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for Windows. To review the features and fixes included in version `20260228.00` of the guest agent, see the [March 2, 2026 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#March_02_2026).

## March 03, 2026

Feature

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for Debian 11, AlmaLinux 8, CentOS Stream 8, Oracle Linux 8, Red Hat Enterprise Linux 8, and Rock Linux 8. To review the features and fixes included in version `20260228.00` of the guest agent, see the [March 2, 2026 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#March_02_2026).

## March 02, 2026

Fixed

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) includes the following fixes:

  * The guest agent is now able to add users to the Administrator group on different locales on Windows.
  * The guest agent now signals itself ready only after the network setup has fully completed. This should prevent the guest agent from hitting race conditions with custom routing solutions that depend on the guest agent service.
  * The guest agent no longer spams metadata SSH key errors when a key is incorrectly formatted.
  * The guest agent now ensures proper reconnection of the primary NIC after a configuration rollback, specifically when `NetworkManager` is active. This resolves an issue where the NIC might not come back online in such scenarios.
  * The guest agent now applies the value of the following configuration flags correctly: `Daemons.network_daemon` and `NetworkInterfaces.vlan_setup_enabled`.



Feature

Version `20260228.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for Debian 13, AlmaLinux 10, CentOS Stream 10, Oracle Linux 10, Red Hat Enterprise Linux 10, and Rock Linux 10. This version introduces the following features:

  * Supports bootstrapping credentials for the HTTPS endpoint for the metadata server by default. For more information about the HTTPS metadata server endpoint, see [HTTPS metadata server endpoints](https://docs.cloud.google.com/compute/docs/metadata/overview#https-mds).
  * Includes a cleanup job that runs once a day and each time the guest agent manager service initializes. This cleanup job ensures that leftover plugin files and states are properly cleaned up.
  * Supports dynamically starting locally installed extensions. This feature is disabled by default, but it can be toggled by setting the `enable_local_plugins` flag to `true` in the guest agent configuration file.



## December 18, 2025

Fixed

Version `20251218.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for Windows only. This version includes the following fixes:

  * Fixes a crash loop in VM extensions due to a race condition where the guest agent manager service can sometimes try to connect to the extension before it is able to create and bind to its unix socket.
  * Fixes an issue where the core plugin is not creating required registry keys before attempting to write to them.



## December 11, 2025

Feature

Version `20251209.00` of the guest agent, which re-introduces the plugin-based architecture to Windows, is now available.

For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

The plugin-based architecture for Windows was previously rolled back due to a bug that prevented the correct setup of IP alias routes when used with the WSFC module, see [October 21, 2025 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#October_21_2025).

## December 08, 2025

Feature

Version `20251205.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is available for Linux only. This version includes the following feature:

  * Snapshot module now supports using NGUIDs to identify disks supporting a wider range of VM families.



Fixed

Version `20251205.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is available for Linux only. This version includes the following fixes:

  * Fixes an issue where the metadata server would become inaccessible during the dynamic removal of multiple vLAN NICs.
  * Fixes an issue where the metadata script runner failed to parse all supported URL patterns and formats.
  * Rolls back multi-universe support for the Agent Communication Service (ACS) client due to issues in the default universe.



## November 20, 2025

Feature

Version `20251120.01` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available for Windows only. This version includes the following fix:

  * Changes the start mode guest agent from `auto` to `delayed-auto` on Windows Service Manager.



## November 17, 2025

Feature

Version `20251115.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available.

Fixed

Version `20251115.00` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available and includes the following fixes:

  * Fixes an issue in the dynamic vLAN subsystem where the `dhclient` backend attempted to remove `netplan`'s vLAN NICs.
  * Fixes a crash loop in the plugin manager caused by its handling of plugin logs.



## November 13, 2025

Feature

Version `20251107.01` of the [guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) is now available.

Fixed

Version `20251107.01` includes a fix for the [Startup script runner](https://docs.cloud.google.com/compute/docs/instances/startup-scripts) component that prevented it from writing status logs and script output to Cloud Logging.

## October 31, 2025

Fixed

Version `20251030.02` includes fixes for the plugin-based architecture that is used by guest agent. For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

  * The Clock Skew module no longer causes time inconsistencies on VMs. The agent no longer attempts to synchronize the hardware clock (`hwclock`) when the VM's Real-time Clock (RTC) isn't set to Coordinated Universal Time 0(UTC). For more information about how the guest agent handles clock synchronization, see [Clock Synchronization](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#clock-synchronization).
  * The `vlan_setup_enabled` option now correctly sets up Dynamic Network Interfaces (NICs). [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics) now initialize reliably.
  * The agent now prevents a race condition in network interface and route setup. Previously, routes were temporarily flushed if they were added before a DHCP lease was acquired. The agent now ensures routes persist correctly, preventing a brief period of missing routes. These routes were previously auto-corrected after approximately one minute.



## October 21, 2025

Fixed

Version `20251009.01` of the guest agent, announced in the [October 20, 2025 release notes](https://docs.cloud.google.com/compute/docs/images/guest-environment/release-notes#October_20_2025), has been rolled back. This version introduced the plugin-based architecture to Windows but contained a bug in the [WSFC module](https://docs.cloud.google.com/compute/docs/images/guest-agent-functions#windows-failover). To resolve this issue, guest agent version `20251011.00` is now available for Windows, which excludes the new plugin-based architecture.

## October 20, 2025

Feature

Version `20251009.01` of the guest agent, which introduces the plugin-based architecture to Windows, is now available.

For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

## October 02, 2025

Feature

Version `20250930.01` of the guest agent, which introduces the plugin-based architecture to Debian 11, is now available.

For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

## September 30, 2025

Fixed

Version `20250930.01` includes the following fixes for issues found in the plugin-based architecture. For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

  * Fixes an issue where the networking module incorrectly added routes when `ip_forwarding` and `target_instance_ips` settings were disabled in `/etc/default/instance_configs.cfg`.
  * Prevents unnecessary error logs in the OS Login module caused by attempts to read a non-existent file.



## September 26, 2025

Feature

Version `20250926.00` of the guest agent is now available. This guest agent version introduces the plugin-based architecture to Debian 12.

For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

## September 18, 2025

Feature

Version `20250918.01` of the guest agent is now available. This guest agent version introduces the plugin-based architecture to the following Debian and Enterprise Linux 10 operating systems:

  * Red Hat Enterprise Linux (RHEL) 10
  * Rocky Linux 10
  * CentOS Stream 10
  * Debian 13



For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

Fixed

Version `20250918.01` includes the following fixes for issues found in plugin-based architecture. For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

  * Corrects an issue in the OS Login module that was incorrectly writing `perm_denied=die` [PAM](https://en.wikipedia.org/wiki/Pluggable_Authentication_Module) module configuration when two-factor authentication isn't enabled.
  * Fixes an issue in the metadata-based SSH module where re-adding a user didn't add the user to the sudoers group.



## September 09, 2025

Fixed

Version `20250907.00` includes the following fixes for issues found in guest agent version `20250901.00`:

  * Corrects an issue in the OS Login module that was incorrectly handling optional runtime systemd dependencies and causing an error log.
  * Fixes a bug that could cause the metadata SSH key module to enter an infinite loop when setting up SSH keys. This occurred if an initial setup attempt failed and the metadata server returned the SSH keys in a different order on a subsequent retry.



Feature

Version `20250907.00` of the guest agent, which introduces the plugin-based architecture to Enterprise Linux 8 operating systems, is now available. For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

With this version, the plugin-based guest agent is now also available for the following operating systems:

  * Red Hat Enterprise Linux (RHEL) 8
  * Rocky Linux 8
  * CentOS Stream 8
  * Oracle Linux 8
  * AlmaLinux 8



## September 03, 2025

Feature

With the introduction of the plugin-based architecture, the guest agent includes the following updates:

  * A new command-line tool, `ggactl_plugin`, is available to manage and restart the guest agent core plugin. To restart the agent, run:
        
        ggactl_plugin coreplugin restart
        

For more information, see [Restarting the guest agent](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#restart-guest-agent).

  * All guest agent components now use a new logging framework. This framework lets you set the logging level in the [guest agent configuration file](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#update-guest-agent-config). For more information about the logging options, see [core settings](https://docs.cloud.google.com/compute/docs/images/manage-guest-agent#core) in the configuration options table.

  * The workload refresh service `gce-workload-cert-refresher` is now part of the guest agent's core plugin. It is no longer a separate systemd service.

  * The guest agent updates the metadata script runner and the Authorized Keys binary (Windows only) to use the new, configurable logging framework. Compatibility managers are included to facilitate the migration.




Announcement

Starting with version `20250901.00`, the guest agent is migrated to a new plugin-based architecture to improve modularity. You can revert to the previous version by setting the metadata attribute `enable-guest-agent-core-plugin` to `FALSE`. For more information about the plugin-based architecture, see [Guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent).

This plugin-based guest agent is available for the following operating systems:

  * Red Hat Enterprise Linux (RHEL) 9
  * Rocky Linux 9
  * CentOS Stream 9
  * Oracle Linux 9
  * AlmaLinux 9



Fixed

An issue is fixed where network routes were not consistently applied ([GitHub Issue #516](https://github.com/GoogleCloudPlatform/guest-agent/issues/516)). The system now consistently applies network routes by monitoring the route table and re-adding routes when they disappear.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
