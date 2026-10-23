---
url: https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone/
title: Set up Cloud Monitoring with a standalone agent \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:56.465561+00:00
---

# Set up Cloud Monitoring with a standalone agent  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Cloud Monitoring with a standalone agent

[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) helps you gain visibility into the performance, availability, and health of your applications and infrastructure. You can use Cloud Monitoring and other parts of Google Cloud Observability to monitor, troubleshoot, and operate VMware Engine services at scale.

You define configuration of metrics forwarding separately for each private cloud using a standalone agent. Each private cloud requires a separate agent, hosted in either a Compute Engine VM or a VMware VM.

Once you successfully enable metrics forwarding, you can see metrics in the Cloud Monitoring Metrics Explorer. Resource types and metrics from VMware Engine begin with `external.googleapis.com/vmware/vcenter`, and the vCenter FQDN is tagged as part of the namespace.

**Note:** Use of the standalone agent itself comes at no additional cost to VMware Engine customers, but metrics collected through the agent are charged at standard [custom metric rates](https://docs.cloud.google.com/stackdriver/pricing). These rates include free data usage allotments to get started with no upfront fees or commitments.

## Before you begin

The steps in this document assume that you first do the following:

  1. [Enable the Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/enable-api)
  2. Identify a [solution user account](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-solution-user-accounts) to use with the standalone agent, and set a strong password for the solution user account.
  3. Create a Compute Engine VM or a VMware VM to use as a host for the standalone agent. Compute Engine VMs must be in a Virtual Private Cloud (VPC) network that's peered to the private cloud VPC network containing the resources you want to monitor.

For an example of creating a _Compute Engine VM_ , see the Compute Engine [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance). For an example of creating a _VMware VM_ , see [Creating a VMware VM](https://docs.cloud.google.com/vmware-engine/docs/create-vmware-vm).




If you use a Compute Engine VM to host the standalone agent, then Google manages key rotation for the service account that you connect. However, it can be cost efficient to create a VMware VM if you have unused capacity in your private cloud and you don't mind managing key rotation by yourself.

Regardless of where you create your agent host VM, it must meet the following requirements:

#### Requirements

Your agent host VM must meet the following system requirements:

  * Supported Linux operating systems:
    * Red Hat Enterprise Linux 9
    * SLES 15
    * Ubuntu 20.04 LTS, 22.04 LTS, or 24.04 LTS
  * At least 4 GB of RAM
  * 300 MB installation space available
  * Installation directory set to `/opt/bpagent`
  * `curl` CLI utility installed



Your agent host VM also needs access to the following addresses to collect and push metrics and logs:

  * Port 443 (TCP) for the HTTPS connection to your vCenter Server (default)
  * `monitoring.googleapis.com:443 (external access)`
  * `logging.googleapis.com:443 (external access)`



## Enabling metrics forwarding

To obtain agent binaries and installation steps, contact Cloud Customer Care.

The process of setting up your agent host VM and enabling metrics forwarding consists of the following steps:

  1. Specify a service account
  2. Configure the agent to access your private cloud for metrics
  3. Configure the agent to access the service account for reporting
  4. Collect metrics and logs
  5. Configure a private cloud for syslog forwarding



### Specify a service account

Forwarding data from the agent to Cloud Monitoring requires a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) from your Google Cloud project. That service account must have the **Monitoring Admin** role for metrics and the **Logs Writer** role for logs.

If you don't have a service account for monitoring and logging applications, create one:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Select a project** and then select the organization, folder, or project where you want to create the service account.

  3. Click **Create service account**.

  4. Enter a name, ID, and description for the service account. We recommend noting that the account is used for the agent integration.

  5. Click **Create and continue**.

  6. For **Role** , select **Monitoring Admin**.

  7. For **Role** , select **Logs Writer**.

  8. Click **Continue**.

  9. Click **Done**.




If you created a VMware VM as your agent host VM, retrieve the service account private key so you can use it to set up the agent:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **Select a project** and then select the organization, folder, or project where your service account is located.

  3. Find your service account in the list of service accounts.

  4. In the **Actions** column, click the more_vertservice account actions menu and select **Manage keys**.

  5. Click **Add key** and select **Create new key**.

  6. Select the **JSON** key type, and click **Create**.

  7. Open the generated JSON file and copy the entire file contents. Metrics and logging collection both use the same JSON key file.

  8. On your agent host VM, copy the JSON key file to the `/opt/bpagent/config/destinations/google_cloud` directory.




### Configure the agent to access your private cloud for metrics

The standalone agent needs access to your private cloud to collect metrics. On your agent host VM, set up access by copying and configuring the `vmware_vcenter.yaml` file:

  1. Copy `vmware_vcenter.yaml` to the `config/metrics/sources` directory:
         
         cp /opt/bpagent/config/metrics/examples/vmware_vcenter.yaml /opt/bpagent/config/metrics/sources
         

  2. Edit the `vmware_vcenter.yaml` to match the information in your VMware Engine environment:
         
         collection_interval: 1m0s
         connection_info:
         connection_timeout: "30"
         enable_performance_counters: "true"
         **host : VCSA_FQDN**
         **password : SOLUTION_USER_PASSWORD**
         performance_counter_end_time: ""
         performance_counter_query_timeout: "15"
         performance_counter_start_time: ""
         port: "443"
         sdk_path: ""
         ssl_config: "No Verify"
         **username : SOLUTION_USER_ACCOUNT**

Replace the following:

     * `VCSA_FQDN`: the fully qualified domain name (FQDN) of the vCenter Server Appliance in your private cloud
     * `SOLUTION_USER_PASSWORD`: the password that corresponds to the solution user account being used
     * `SOLUTION_USER_ACCOUNT`: the solution user account that the agent uses to report information



### Configure the agent to access the service account for reporting

The standalone agent needs access to Google Cloud Observability to send metrics and logs. Configure the agent to access the project used for reporting through the service account that has monitoring and logging permissions.

On your agent host VM, copy and configure the `log_agent.yaml` file:

  1. Copy `log_agent.example.yaml` to `log_agent.yaml` before editing:
         
         cp /opt/bpagent/config/log_agent.example.yaml /opt/bpagent/config/log_agent.yaml
         

  2. At the bottom of `log_agent.yaml`, enter your project name and the full path to the JSON key file. For agent host VMs created in Compute Engine, remove or comment out the `credentials_file` line.
         
         ...
         - id: my_project_destination
           **project_id : PROJECT_ID**
           type: google_cloud_output
           **credentials_file : /opt/bpagent/config/destinations/google_cloud/JSON_KEY_FILE**

Replace the following:

     * `PROJECT_ID`: ID of the project where you want to output logs
     * `JSON_KEY_FILE`: name of your service account private key file. Remove or comment out this line for agent host VMs created in Compute Engine.

If you want to export syslog messages from ESXi Hosts to Google Cloud Logging, update the file `/opt/bpagent/config/log_agent.yaml` within the standalone agent VM with the following details:
    
    - id: vmware-esxi-logs
    # A syslog address of the form `:`
    listen_address: 0.0.0.0:514
    # Enable TLS for the TCP listener
    enable_tls: false
    # File path for the X509 TLS certificate chain, only relevant if enable_tls is true
    certificate_file: /opt/cert
    # File path for the X509 TLS private key, only relevant if enable_tls is true
    private_key_file: /opt/key
    # whether or not to start parsing logs from `end` of file or `beginning`
    start_at: end
    type: vmware_vcenter
    output: my_project_destination

**Note:** If you use port `514` for ESXi syslog, ensure that the target port on the standalone agent is always set to `TCP/514` in your ESXi configuration.

**Caution:** Be aware of your service account key refresh intervals. If your private key expires, you must generate a new private key and update `log_agent.yaml` with any filename changes.

### Collect metrics and logs

To collect metrics or logs, the standalone agent must be running on your agent host VM. Connect to your agent host VM and use the following commands to start or stop the agent:

  * To start the agent on your host VM, run the following:
        
        systemctl start bpagent
        

  * To stop the agent on your host VM, run the following:
        
        systemctl stop bpagent
        




### Configure a private cloud for syslog forwarding

VMware Engine integrates with Cloud Logging by forwarding syslog messages from vCenter and NSX to the standalone agent. The standalone agent is configured to parse both vCenter and NSX logs for Cloud Logging to read.

To forward syslog messages from VMware Engine, do the following:

  * For vCenter syslog forwarding, follow the steps in [Forward vCenter syslog messages](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-forward-syslog#forward-vcenter). In the **Server** field, enter the IP address or hostname of your agent host VM. The standalone agent uses the **TCP** communication protocol and listens on port `5142`. The standalone agent must be running for the syslog configuration to connect successfully.
  * For NSX syslog forwarding, follow the steps in [Forward NSX syslog messages](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-forward-syslog#forward-nsxt). In the **FQDN or IP Address** field, enter the IP address or hostname of your agent host VM. The standalone agent uses the **TCP** communication protocol and listens on port `5142`.



If you plan to forward syslog from ESXi Hosts, change the default port on which the log agent listens from `5142` to `514`. In that case, use the same port (`514`) for forwarding syslog from vCenter as well as NSX.

## Cloud Monitoring dashboards

After you enable metrics forwarding, you can install predefined dashboards for VMware Engine. The following dashboards provide you with aggregated information across all sources that you specify:

  * **Overview dashboard:** High-level view that lists key resources like data centers, clusters, and VMs.
  * **Contention dashboard:** Resource utilization for storage, CPU, memory, and networking to help you locate top VMs and hosts by resource demand.
  * **Virtual machine performance dashboard:** Virtual machine (VM) instance performance indicators that can be filtered by instance name and used to compare the performance of multiple VMs with each other.



To access a VMware Engine dashboard, do the following:

  1. In the Google Cloud console, go to **Monitoring > Dashboards**.

[Go to Dashboards](https://console.cloud.google.com/monitoring/dashboards)

  2. In the **Sample Library** tab, select the **VMware** category.

  3. Select the dashboard of interest and click _file_download_**Import**.




The definitions for these dashboards are also [stored on GitHub](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/dashboards/vmware). For steps to install or view the definitions as custom dashboards, see [Install sample dashboards](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates).

## Cloud Monitoring alerts

You can use metrics from your integration to trigger alerts and notifications based on custom thresholds and incidents. For example, you can have Cloud Monitoring send you an SMS notification when someone creates a new VM in your private cloud.

For details, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

## List of collected metrics

Once you successfully enable metrics forwarding, you can see metrics in the Cloud Monitoring Metrics Explorer. Resource types and metric types from VMware Engine begin with the prefix `external.googleapis.com/vmware/vcenter.` in the Metrics Explorer.

Here's the full list of metrics collected for VMware Engine, with the prefix omitted:

Resource and metric type | Description  
---|---  
`cluster.cpu.available` | CPU available in a cluster, in megahertz  
`cluster.memory.available` | Memory available in a cluster, in bytes  
`cluster.cpu.threads` | Number of CPU threads in a cluster  
`cluster.cpu.effective` | Effective CPU in a cluster from all running hosts. Hosts that are unresponsive or in maintenance mode are not counted.  
`cluster.effective_hosts` | Number of effective hosts in a cluster. Hosts that are unresponsive or in maintenance mode are not counted.  
`cluster.memory.effective` | Effective memory in a cluster from all running hosts. Hosts that are unresponsive or in maintenance mode are not counted.  
`cluster.hosts` | Number of hosts in a cluster  
`cluster.vsan.latency` | vSAN latency of a cluster, in microseconds  
`cluster.vsan.throughput` | vSAN read-write throughput of a cluster, in bytes  
`cluster.vsan.iops` | vSAN IOPS of a cluster  
`cluster.vsan.congestions` | vSAN congestion value of a cluster  
`cluster.vsan.oio` | vSAN outstanding I/O (oio) in a cluster  
`datacenter.cpu.average_host_utilization` | Average host utilization of a data center, as a percentage  
`datacenter.clusters` | Number of clusters in a data center  
`datacenter.datastores` | Number of datastores in a data center  
`datacenter.hosts` | Number of hosts in a data center  
`datacenter.host_systems` | Number of host systems in a data center  
`datacenter.hosts/powered_on` | Number of powered on hosts in a data center  
`datacenter.hosts/powered_off` | Number of powered off hosts in a data center  
`datacenter.disk/space` | Total disk space in a data center, in terabytes  
`datastore.capacity_bytes` | Capacity of a datastore, in bytes  
`datastore.capacity_utilization` | Capacity utilization of a datastore, as a percentage  
`host_system.network.transmitted_packets` | Number of network packets transmitted by the host system  
`host_system.network.received_packets` | Number of network packets received by the host system  
`host_system.dropped_packets` | Number of network packets dropped by the host system  
`host_system.network.adapters` | Number of host system network adapters  
`host_system.memory.utilization` | Memory utilization of the host system, as a percentage  
`host_system.memory.utilization_ratio` | Memory utilization ratio of the host system  
`host_system.memory.used` | Memory used by the host system, in megabytes  
`host_system.disk.read` | Disk read of the host system, in kilobytes per second  
`host_system.disk_latency` | Disk latency of the host system, in milliseconds  
`host_system.cpu.usage` | CPU usage of the host system, as a percentage  
`host_system.cpu.utilization_ratio` | CPU utilization ratio of the host system  
`host_system.cpu.capacity` | CPU capacity of the host system, in megahertz  
`host_system.cpu.reserved_capacity` | Reserved CPU capacity of the host system, in megahertz  
`host_system.cpu.average_speed` | Average CPU speed of the host system, in megahertz  
`host_system.cpu.used` | CPU used by the host system, in megahertz  
`host_system.vsan.throughput` | vSAN read-write throughput of the host system, in bytes  
`host_system.vsan.iops` | vSAN IOPS of the host system  
`host_system.vsan.latency` | vSAN latency of the host system, in microseconds  
`host_system.vsan.client_cache_hits` | vSAN client cache hits of the host system  
`host_system.vsan.client_cache_hit_rate` | vSAN client cache hit rate of the host system, as a percentage  
`host_system.vsan.congestions` | vSAN congestion value of the host system  
`resource_pool.memory.swapped_bytes` | vCenter swapped memory, in megabytes  
`resource_pool.memory.shared_bytes` | vCenter shared memory, in megabytes  
`resource_pool.memory.private_bytes` | vCenter private memory, in megabytes  
`resource_pool.memory.shares` | Number of vCenter memory shares  
`resource_pool.memory.overhead_usage_bytes` | vCenter memory overhead usage, in megabytes  
`resource_pool.memory.host_usage_bytes` | vCenter memory host usage, in megabytes  
`resource_pool.memory.active_guest_usage_bytes` | vCenter memory active guest usage, in megabytes  
`resource_pool.memory.balloon_size` | Size of the vCenter balloon memory, in megabytes  
`resource_pool.cpu.usage` | CPU used by vCenter, in megahertz  
`resource_pool.cpu.shares` | Number of CPU shares in the resource pool, in megabytes  
`vm.memory.ballooned` | Size of the VM balloon memory, in megabytes  
`vm.network.throughput_bytes` | Network throughput of the VM, in kilobytes per second  
`vm.memory.used_percent` | Memory used by the VM, as a percentage of available memory  
`vm.memory.usage_bytes` | Memory used by the VM, in megabytes  
`vm.disk.throughput_bytes` | Disk read-write throughput of the VM, in kilobytes per second  
`vm.disk.used_percent` | Disk usage of the VM, as a percentage of available storage  
`vm.disk.usage_bytes` | Disk usage of the VM, in bytes  
`vm.disk.free_bytes` | Available disk space of the VM, in bytes  
`vm.cpu.used_percent` | CPU usage of the VM, as a percentage of available CPU  
`vm.cpu.usage` | CPU usage of the VM, in megahertz  
`vm.cpu.ready_percent` | CPU of the VM that's ready but unable to run, as a percentage  
`vm.vsan.throughput` | vSAN read-write throughput of the VM, in bytes  
`vm.vsan.iops` | vSAN IOPS of the VM  
`vm.vsan.latency` | vSAN latency of the VM, in microseconds  
`vm.vsan.readCount` | vSAN read count of the VM  
`vm.vsan.writeCount` | vSAN write count of the VM  
`vsphere.cpu.available` | CPU available across clusters managed by vSphere, in gigahertz  
`vsphere.memory.available` | Memory available across clusters managed by vSphere, in gigabytes  
`vsphere.clusters.total` | Number of clusters managed by vSphere  
`vsphere.clusters` | Count of clusters managed by vSphere with the cluster status color code (like green, grey, red, or yellow)  
`vsphere.cpu.cpus` | Total number of host system CPU cores managed by vSphere  
`vsphere.datacenters` | Number of data centers managed by vSphere  
`vsphere.datastores.total` | Number of datastores in vSphere  
`vsphere.datastores` | Count of datastores managed by vSphere with the datastore status color code (like green, grey, red, or yellow)  
`vsphere.disk.space` | Total attached disk space in vSphere, in terabytes  
`vsphere.host_systems` | Number of host systems in vSphere  
`vsphere.hosts` | Count of host systems managed by vSphere with the host system status color code (like green, grey, red, or yellow)  
`vsphere.network.adapters` | Number of network adapters in vSphere  
`vsphere.hosts.powered_off` | Number of powered off hosts in vSphere  
`vsphere.hosts.powered_on` | Number of powered on hosts in vSphere  
`vsphere.virtual_machines.total` | Number of VMs across all vSphere clusters  
`vsphere.virtual_machines` | Count of VMs managed by vSphere with the VM status color code (like green, grey, red, or yellow)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
