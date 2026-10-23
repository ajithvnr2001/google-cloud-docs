---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/br-appliance-network-settings/
title: Appliance network settings for backup/recovery appliances \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:42.822577+00:00
---

# Appliance network settings for backup/recovery appliances  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/br-appliance-network-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Appliance network settings for backup/recovery appliances Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to configure network settings for any backup/recovery appliance managed by your appliance management console.

From this page, you can:

  * Configure Self Service Network for backup/recovery appliances

  * Modify DNS and NTP

  * Perform Network Troubleshooting

  * Create and modify Host Resolution




## Configure self service network for backup/recovery appliances

  1. Click the **Manage** tab and select the **Appliances** option from the drop-down list.

  2. Right-click an appliance and select **Configure Appliance Networking** to open the System Management page.

  3. On the **DNS and NTP** tab, enter or modify the DNS or NTP settings or both. See DNS and NTP. Any field you leave empty will revert to DHCP provided values.

  4. Click the **IP & Interfaces** tab to view the a list of configured IP addresses. You cannot edit any information, it is view only.

  5. Click the **Troubleshooting** tab and troubleshoot problematic network connections. See Network Troubleshooting for additional information.

  6. Click the **Host Resolution tab** to override DNS resolution for specific hosts. See Host Resolution for additional information.




## DNS and NTP

Changes made on this page can have a significant impact on the operation of your backup/recovery appliance. Ensure IP addresses for DNS and NTP are valid and reachable, without firewalls blocking the traffic. This may be tested using the TCP connection test on the **Troubleshooting** tab.

  * **DNS Domain** : Enter the domain of the hosts connected to this appliance.

If you have additional hosts on other domains, you can set up a **DNS Suffix Search** to ensure the appliance can find them by their short names.

**Note:** If you set any entries in DNS Suffix Search, then the DNS Domain will NOT be searched. To search both the manual entries AND the DNS domain, include the DNS domain in the DNS Suffix Search.
  * **Primary DNS** : Enter the IP address of your primary DNS server.

  * **Secondary DNS** : Enter the IP address of your secondary DNS server (optional).

  * **NTP Server** : Enter the IP address or hostname of your NTP server. We recommend leaving this blank or set to metadata.google.internal which is provided by Google Cloud and is always reachable.




## Troubleshooting

Use this page to troubleshoot problematic network connections. Under **Utility** , select the troubleshooting tool to use, enter the necessary parameters, and then click **Run Test**. The results appear in the Test Results box.

**Ping** : Runs a ping to determine reachability of a target host, returning the output as a plain text stream. This command sends 4 ICMP echo packets. Enter:

  * **Source IP** : The default value of Auto Select is generally the best choice. If your appliance has multiple IP addresses, you may select which will be used for the outbound ICMP traffic by selecting it here.

  * **Destination IP** : A valid IPv4 address.

Example Ping result:
        
        PING 1.2.3.4 (1.2.3.4) 56(84) bytes of data.
        --- 1.2.3.4 ping statistics ---
        4 packets transmitted, 0 received, 100% packet loss, time 3001ms
        




**IP route get** : Queries the routing tables for the selected Destination IP address without sending any packets. Enter:

  * **Source IP** : The default value of Auto Select is generally the best choice. If your appliance has multiple IP addresses, you may select which will be used for the routing request by selecting it here.

  * **Destination IP** : The IP address of a target host.

Example IP route get result:
        
        test or routeget 1.2.3.4
        1.2.3.4 using 172.17.1.2 dev eth0 src 172.17.134.80
        cache mtu 1500 advmss 1460 hoplimit 64
        




**Traceroute** : Runs a traceroute to the given IP address by sending a series of UDP probes, returning the output as a plain text stream. This can take up to 2 minutes to run. Use Traceroute to identify intervening networks on the path. Traceroute cannot accept a source IP parameter, so it is not useful for testing the behavior of reply packets. Only outgoing connections can be diagnosed with this tool.

  * **Destination IP** : The IP address of a target host.

  * **UDP Port** : See Specifies the base port to use for the test. Leave blank to use the default 33434. Note: the number of ports used will be equal to the number of hops.

Example Traceroute result:
        
        test or traceroute 8.8.8.8
        1: dev134-86.dev.acme.com (172.17.134.86) 0.092ms
        pmtu 1500
        1: devgw-waln5k02.dev.acme.com (172.17.0.3) 4.287ms
        1: devgw-waln5k02.dev.acme.com (172.17.0.3) 1.287ms
        2: e-1-20-walpalo.core.acme.com (192.168.255.21) 2.805ms
        3: ge-0-0-1-walasr.edge.acme.com (192.43.242.209) 2.769ms
        4: 205.158.44.81.ptr.us.xo.net (205.158.44.81) 9.247ms asymm 14
        5: vb1020.rar3.nyc-ny.us.xo.net (216.156.0.25) 10.080ms asymm 12
        6: 207.88.12.104.ptr.us.xo.net (207.88.12.104) 8.537ms asymm 12
        7: 207.88.13.35.ptr.us.xo.net (207.88.13.35) 8.175ms asymm 11
        8: no reply
        9: no reply
        .
        .
        .
        31: no reply
        Too many hops: pmtu 1500
        Resume: pmtu 1500
        




**TCP Connection Test** : Attempts a TCP connection to the target IP and port. If successful, the connection is closed immediately without transferring any data. If not successful it returns a failure message. Most commonly used to verify if firewalls are blocking traffic, or if a destination host is listening on a specific TCP port.

  * **Source IP** : The default value of Auto Select is generally the best choice. If your appliance has multiple IP addresses, you can select which will be used for the TCP connection test by selecting it here.

  * **Destination IP** : The IP address of a target host.

  * **TCP Port** : Specify the TCP port on the destination to use when attempting to make a connection.

Example TCP Connection Test result:
        
        test/TCP ConnectionTest
        Connection to 10.138.200.3:443 succeeded!
        




To validate the connectivity from appliance to Backup and DR agent, see Validate backup/recovery appliance to Backup and DR agent connectivity.

**Test DNS** : Attempts to use the configured DNS server to resolve a name or IP address.

  * In **Resolve** , select Name to resolve a name to an IP address, or select IP to resolve IP address to name using PTR records (reverse DNS lookup).
  * In **Name to Resolve** , enter the name you want to attempt to resolve using the configured DNS server.
  * In **IP to Resolve** , enter the IP address you want to attempt to resolve to a name using PTR records (reverse DNS lookup).



## Host resolution

Sometimes, it is necessary to manually create static entries for name resolution. This may be required for hosts with multiple IP addresses, where you want to resolve to an IP that is different from what is registered in DNS. You can also resolve names that are not available in DNS at all with the static entries creation.

From this tab you can Add, Modify, or Delete IP/Name pairs. When added, these are resolved as if they were stored in /etc/hosts on a standard linux platform. One or more aliases may also be specified for each row in the table (multiple aliases are separated by a space).

**Note:** It is not allowed to specify multiple rows in the table with the same name, but different IP addresses. If it is necessary to resolve a name to multiple IP addresses, using a DNS server is the only way to achieve this.

## Validate backup/recovery appliance to Backup and DR agent connectivity

To validate that the backup/recovery appliance is connect to the Backup and DR agent running on a host, you can run the connectivity test. You need the IP address of the target host to perform the connectivity test.

  1. From the appliance management console, go to **Manage** > **Appliances**.
  2. Right select the relevant appliance and select **Configure Appliance Networking**. The **System Management** page opens in a new tab.
  3. Go to the **Troubleshooting** tab.
  4. Select **TCP Connection Test** from the **Utility** drop-down.
  5. Leave the **Source IP** to **Auto Select**.
  6. In the **Destination IP** box, enter the IP address of the target host.
  7. In the **TCP Port** box, enter the value 5106.
  8. Select **Run Test**.

The **Test Results** display three possible results (your IP will be different) as follows:

     * **Successful result** : `Connection to 10.0.0.5:5106 succeeded!`

This means that the agent is running on the host and that the firewall is not blocking connection. If the Certificate Status for the host in **Manage** > **Hosts** is shown as invalid, then you must create a new secret key using the Backup and DR agent on the host and then adding that key by editing the host entry in **Manage** > **Hosts**.

     * **Unsuccessful result (time out)** : `Connection to 10.0.0.5:5106 failed: Connection timed out.`

The reason for connection timed out can be any of the following:

       * The host is not powered on.
       * The Backup and DR agent is not installed.
       * The Backup and DR agent is installed but not running.
       * The firewall for the VPC is not allowing ingress traffic to port 5106 on that host.
       * There is no network connectivity between the appliance and host.
     * **Unsuccessful result (refused)** : `Connection to 10.0.0.5:5106 refused`

The reason for connection refused can be any of the following:

       * The Backup and DR agent is not installed.
       * The Backup and DR agent is installed but not running.
       * You are connecting to a wrong IP address.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
