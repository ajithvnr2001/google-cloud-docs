---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/general-tips/
title: General tips for using Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:42.944552+00:00
---

# General tips for using Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/general-tips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  General tips for using Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

This page describes tips that you might find helpful if you run into problems using Compute Engine.

For help troubleshooting specific issues, see one of the following sections:

  * For steps to troubleshoot general issues with instances, such as if your instance doesn't start up, see [Troubleshoot creating, updating and deleting VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation).
  * For steps to troubleshoot issues with Windows instances, see [Troubleshooting Windows instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows).



## Viewing different response formats

The Google Cloud CLI performs most of its actions by making REST API calls. The pretty-printed results show only the most important information returned by any specific command. To see the different response formats, use the `--format` flag which displays the response in different output formats, including `json`, `yaml`, and `text`. For example, to see a list of instances in JSON, use `--format json`:
    
    
    gcloud compute instances list --format json
    

## Viewing gcloud compute logs

The gcloud CLI creates and stores logs in a log file that you can query, located at `$HOME/.config/gcloud/logs`. To see the latest log file on a Linux-based operating system, run:
    
    
    $ less $(find ~/.config/gcloud/logs | sort | tail -n 1)
    

The log file includes information about all requests and responses made using the `gcloud CLI` tool.

To automatically purge the log files created by the gcloud CLI, use the [`max_log_days`](https://docs.cloud.google.com/sdk/gcloud/reference/config#max_log_days) property, which sets the maximum number of days to retain log files before deleting. The default setting is 30 days. If you set this property value to 0, it turns off log garbage collection and does not delete log files.
    
    
     gcloud config set core/max_log_days DAYS_TO_RETAIN_LOGS
    

**Disable gcloud CLI file logging:**

The file `$HOME/.config/gcloud/logs` consumes space on the local file system. The amount of logs generated might overwhelm the amount of space on the local file system, which can cause issues like:

  * Space utilization reaching 100% on the instance.
  * Failure to execute gcloud CLI logging commands because there is no space left to create a new file on the local file system.



To change the gcloud CLI behavior and disable the file logging, use the [`disable_file_logging`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#disable_file_logging) property:
    
    
     gcloud config set core/disable_file_logging True
    

**Note:** The gcloud version must be higher than 250.0.0 to be able to use the `disable_file_logging` property. To check the gcloud version, use the command `gcloud -v`.

## Selecting resource names

When selecting names for your resources, keep in mind that these friendly-names may be visible on support and operational dashboards within Compute Engine. For this reason, it is recommended that resource names that do not expose any sensitive information.

## Communicating to the internet

An instance has _direct_ internet access only if both of the following conditions are true:

  * The instance has an [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address).
  * The instance's VPC network uses a [default route whose next hop is the default internet gateway](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet).



Instances can also access the internet indirectly, by connecting through [Cloud NAT](https://docs.cloud.google.com/nat/docs) or an instance-based proxy. For additional considerations, including firewall rule configuration, see [Internet access requirements](https://docs.cloud.google.com/vpc/docs/vpc#internet_access_reqs).

## Idle connections

Google Cloud network components don't keep idle connections open indefinitely. To prevent dropped connections, consider how the following components handle idle connections:

  * Cloud Next Generation Firewall connection tracking table entries are removed after a flow has been idle for 10 minutes.

  * Cloud NAT has [timeout settings that apply to idle connections](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts) for TCP, UDP, and ICMP. The TCP timeouts include TCP Established Connection Idle Timeout, TCP Transitory Connection Idle Timeout, and TCP `TIME_WAIT` Timeout.

  * Passthrough Network Load Balancers track connections using their own rules. For more information, see [Traffic distribution for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution) and [Traffic distribution for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution).




To prevent idle TCP connections from being dropped, you can configure [TCP keepalive](https://en.wikipedia.org/wiki/Keepalive), which keeps connections active by sending periodic packets (probes) to reset the idle timeouts:

  * Make sure that client or server applications create sockets with the `SO_KEEPALIVE` socket option. Consult your application or software library's documentation to determine how to open sockets with the `SO_KEEPALIVE` option.

  * Configure the following TCP keepalive parameters:

    * The _inactivity period_ , representing the time that must elapse between the last non-keepalive packet and the first keepalive probe in a sequence.

    * The _keepalive interval_ , representing the time between each TCP keepalive probe.

    * The _keepalive probes_ , representing the total number of unacknowledged TCP keepalive probes that are sent in a sequence before the connection is considered dropped.




Client or server applications can set the TCP keepalive parameters by using socket options such as `TCP_KEEPIDLE`, `TCP_KEEPINTVL`, and `TCP_KEEPCNT`, or you can set the TCP keepalive parameters for your operating system.

The following examples show how to set an inactivity period of 60 seconds for your operating system:

#### Linux

  


Run the following command:
    
    
    $ sudo /sbin/sysctl -w net.ipv4.tcp_keepalive_time=60 net.ipv4.tcp_keepalive_intvl=60 net.ipv4.tcp_keepalive_probes=5

To ensure that the settings survive a reboot, add the settings to your `/etc/sysctl.conf` file. These kernel parameters apply to both IPv4 and IPv6, even though they have `ipv4` in their names.

See [Linux TCP Keepalive HOWTO](http://www.tldp.org/HOWTO/html_single/TCP-Keepalive-HOWTO) for additional information. 

#### macOS

  


Run the following command:
    
    
    $ sudo sysctl -w net.inet.tcp.always_keepalive=1 net.inet.tcp.keepidle=60000 net.inet.tcp.keepinit=60000 net.inet.tcp.keepintvl=60000
    

#### Windows

  


Under the registry path `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\`, add the following settings, using the [DWORD](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dtyp/262627d8-3418-4627-9218-4ffe110850b2) data type, or edit the values if the settings already exist:
    
    
    KeepAliveInterval: 1000
    KeepAliveTime: 60000
    TcpMaxDataRetransmissions: 10
    

## Accessing Compute Engine as a different SSH user

By default, the `gcloud compute` command-line tool uses the `$USER` variable to add users to the `/etc/passwd` file for connecting to instances using SSH. You can specify a different user using the `--ssh-key-file PRIVATE_KEY_FILE` flag when running the `gcloud compute ssh` command. For example:
    
    
    gcloud compute ssh example-instance --ssh-key-file my-private-key-file
    

For more information, see the [`gcloud` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh).

## Interacting with the serial console

You can enable interactive access to an instance's serial console so you can connect and troubleshoot instances through the serial console.

For more information, see [Troubleshooting using the serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console).

## Avoiding packet fragmentation to instances built from custom images

The VPC network has a default maximum transmission unit (MTU) of `1460` bytes for Linux images and Windows Server images. However, the network MTU can be changed. For details, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu) in the VPC documentation.

When creating client applications that communicate with Compute Engine instances over UDP sockets, you can avoid fragmentation if you set the maximum size of the UDP datagram's data to 28 bytes less than the network MTU. For example, if the network's MTU is 1460 bytes, you can send up to 1432 bytes of UDP data per packet without fragmentation. If the network's MTU is 1500 bytes, you can send up to 1472 bytes of UDP data without fragmentation. The 28 bytes are used for an IPv4 packet header (20 bytes) and a UDP datagram header (8 bytes). You can set the network's MTU to a maximum of 8896 bytes.

## Performance and CPU diagnostics

Unexpected latency spikes or crashes in your application on modern CPU platforms might indicate CPU bus locks. These issues occur when atomic operations are performed on unaligned memory.

To identify the issue, review your serial port output for the following log entry: `x86/split lock detection: #DB: <process_name>/<pid> took a bus_lock trap at address: 0x<address>`.

Serial console output enables the detection of hardware-level events, such as CPU bus lock traps, which indicate unaligned memory operations that can degrade system performance.

For more information, see [Troubleshoot CPU bus locks](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-cpu-bus-locks).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
