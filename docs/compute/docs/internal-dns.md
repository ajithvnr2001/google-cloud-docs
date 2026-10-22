---
url: https://docs.cloud.google.com/compute/docs/internal-dns/
title: Overview of internal DNS \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:00.342372+00:00
---

# Overview of internal DNS  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/internal-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Overview of internal DNS Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

When you create Compute Engine instances, internal DNS automatically creates a DNS name for the instance. This DNS name facilitates internal instance-to-instance communication by resolving internal IP addresses. Virtual Private Cloud networks on Google Cloud use the internal DNS service to let compute instances in the same network access each other by using internal DNS names.

Google Cloud automatically creates, updates, and removes the following DNS record types as you manage your instances:

  * DNS address records, or _A records_ , are created for instances in a DNS zone for `.internal`.
  * PTR records for instances, used for reverse DNS lookup, are created in corresponding reverse zones.



For example, when you delete an instance, Google Cloud automatically removes the associated A and PTR records for its internal DNS name. If you then create an instance with the same name, Google Cloud creates new records for the replacement.

## Limitations

  * Compute Engine creates internal DNS name A and PTR records only for the primary internal IPv4 address of the `nic0` network interface of an instance. Consequently, the stack type of the `nic0` network interface must be either IPv4-only or dual-stack. Internal DNS doesn't support IPv6-only network interfaces.

  * Compute Engine _doesn't_ create internal DNS records for the following:

    * The primary internal IPv4 address of a network interface different from `nic0`.
    * An external IPv4 address of any network interface.
    * An internal IPv4 address of an [alias IP range](https://docs.cloud.google.com/vpc/docs/alias-ip) of any network interface.
    * An internal or external IPv6 address range of any network interface.
  * Resolving internal DNS names requires that the client VM and VM associated with the internal DNS record are both:

    * In the same VPC network.
    * In the same project (except for certain Shared VPC scenarios).

For more information about Shared VPC scenarios, see Internal DNS names and Shared VPC.




## Zonal and global internal DNS names

Google Cloud has two types of internal DNS names:

  * **Zonal DNS** : instance names must be unique within each zone, but you can reuse instance names across zones. For example, you can have several instances named `instance-1` as long as the instances are in different zones.
  * **Global DNS** : instance names must be unique within each project. With global DNS, you can't reuse instance names within the project.



Google _strongly recommends_ using zonal DNS because it offers higher reliability by isolating failures in the DNS registration to individual zones. In the event of an outage, global DNS has the following issues:

  * The instance name must be unique across the entire project. As a result, you can't create new instances in any region experiencing control plane failures where you have or previously had project resources. Google Cloud can't verify the existing resource DNS names in the unavailable region.
  * Certain features of Compute Engine are not available, such as [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) of managed instance groups (MIGs). As a result, your applications that use autoscaling to gracefully handle workload increases aren't able to scale up.



The default internal DNS type is set when you enable the Compute Engine API.

  * The default internal DNS type is zonal DNS.
  * If your organization or standalone project enabled the Compute Engine API before September 6, 2018, then the default internal DNS type is set to global DNS.

**Note:** Migrating a project to a different organization doesn't change the instance's default internal DNS type.

The fully qualified domain names for internal DNS names are described in the following table.

Internal DNS type | Fully qualified domain name (FQDN)  
---|---  
[Zonal DNS](https://docs.cloud.google.com/compute/docs/networking/zonal-dns) | `INSTANCE_NAME.ZONE.c.PROJECT_ID.internal`  
Global (project wide) DNS | `INSTANCE_NAME.c.PROJECT_ID.internal`  
  
Replace the following:

  * `INSTANCE_NAME`: the name of the instance. For zonal DNS, this value must be unique within the zone but can be repeated across zones. For global DNS, the instance name must be unique across the project.
  * `ZONE`: the zone where your instance is located.
  * `PROJECT_ID`: the project to which the instance belongs.



For information about how to control which type of internal DNS name is used at the project or instance level, see [configure DNS names for your project or instances](https://docs.cloud.google.com/compute/docs/networking/zonal-dns#setting-zonal-dns).

## DNS name resolution

Instances receive internal DNS resolution information as part of their DHCP leases. The method of DNS resolution depends on the operating system platform:

  * Linux: By default, the instance's DNS server resolves internal DNS names.
  * Windows: By default, the subnet's default gateway resolves internal DNS names.

**Important:** If you change the name server configuration for your instance, you cannot resolve records in Compute Engine internal DNS (the `.internal` zone) or in Cloud DNS managed private zones, forwarding zones, and peering zones unless your replacement DNS server forwards these queries to the metadata server on Linux or the default gateway on Windows.

## Reverse zones for PTR records

Google Cloud's internal DNS service automatically creates PTR records for instances in the following [reverse zones](https://wikipedia.org/wiki/Reverse_DNS_lookup):

  * `10.in-addr.arpa.`
  * `168.192.in-addr.arpa.`
  * `16.172.in-addr.arpa.`, `17.172.in-addr.arpa.`, ... through `31.172.in-addr.arpa.`



## Internal DNS names and Shared VPC

The client VM and the VM associated with the internal DNS record can be located in separate projects, but they must use the same Shared VPC network. For example, the client can be located in one service project, and the VM associated with the internal DNS record can be located in a different service project or the host project.

Clients must issue fully qualified domain name (FQDN) queries for internal DNS records instead of relying on partial queries and DNS search domains. DNS search domains are different in each project for reasons such as the following:

  * The domain name portion of each internal DNS A record contains the project ID of the project that contains the VM. For a VM in a service project whose `nic0` network interface uses a Shared VPC network, the project of the VM is different from the project containing the network.

  * Whether zonal or global (project wide) internal DNS names are used depends on the configuration of the project that contains the VM.




For more information about Shared VPC, see:

  * [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc)
  * [Provision Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc)



## Customizing internal DNS names

Some organizations or applications might require custom internal DNS names instead of the default internal DNS names created by Google Cloud.

### Private zones and custom records with Cloud DNS

You can use a [Cloud DNS private zone](https://docs.cloud.google.com/dns/docs/overview#concepts) to create custom DNS entries for your instances. You can configure PTR records that let you override the default internal DNS name for your instance with the custom name that you provide.

To create custom PTR records that override the automatically created internal DNS PTR names, see [PTR records for RFC 1918 addresses in private zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#ptr_records_in_private_zones). For information about creating PTR records for instances, see [Create a PTR record for an instance](https://docs.cloud.google.com/compute/docs/instances/create-ptr-record).

**Note:** Internal DNS names are distinct from custom records created using Cloud DNS. Internal DNS records are automatically created and cannot be changed.

### Custom hostnames

You can specify a custom hostname for an instance when you create it. Custom hostnames assigned in this way are not resolved by internal DNS. With custom hostnames, you still need to create a corresponding DNS record in the appropriate zone (for example, using Cloud DNS). For more information, see [Create an instance with a custom hostname](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm).

## Internal DNS and DHCP

Compute Engine instances are configured to renew DHCP leases every 24 hours. For instances that are enabled for zonal DNS, the DHCP lease expires every hour. Instances using [zonal DNS](https://docs.cloud.google.com/compute/docs/networking/zonal-dns) have both zonal and global entries in the DHCP configuration file.

By default, most Linux distributions store DHCP information in [`resolv.conf`](http://man7.org/linux/man-pages/man5/resolv.conf.5.html). Manually editing `resolv.conf` results in it being reverted to the default DHCP every time the DHCP lease expires on your instance. To make static modifications in the `resolv.conf` file, several Linux distributions allow items to be prepended or appended to the [DHCP policy](https://www.isc.org/wp-content/uploads/2017/08/dhcp41clientconf.html).

**Note:** The `resolv.conf` file isn't related to the `gce-resolved.conf` file, which is used by Cloud DNS.

How you modify the DHCP policy or configuration file depends on what distribution of Linux you use. For example, Red Hat Enterprise Linux and Debian use the `/etc/dhcp/dhcpd.conf` configuration file. On CentOS, you use the [Network Manager command line utility](https://infotechys.com/change-dns-settings-using-the-nmcli-utility/), `nmcli`.

Refer to your operating system documentation for information about how to configure custom DHCP and DNS network settings. For example, for Red Hat Enterprise Linux for SAP with HA and Update Services 8.6, use the following link: [Manually configuring the /etc/resolv.conf file](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/manually-configuring-the-etc-resolv-conf-file_configuring-and-managing-networking)

### Example `resolv.conf` file

By default, most Linux distributions store DHCP information in [`resolv.conf`](http://man7.org/linux/man-pages/man5/resolv.conf.5.html). The `systemd-resolved` service also provides resolver services for DNS. You can configure this service by editing the `/etc/systemd/resolved.conf` file and other `*.conf` files in the `/etc/systemd/resolved.conf.d/` directory. On Linux distributions that store DHCP information in `resolved.conf`, you can view zonal and global DNS entries in the [`/etc/systemd/resolved.conf`](https://wiki.archlinux.org/title/Systemd-resolved#Configuration) file.

**Note:** When you view the `resolv.conf` file, make sure that the file is refreshed to the latest version. To do this, you might need to refresh the DHCP lease or restart the network stack, depending on the operating system that your instance uses.

These files have the following restrictions:

  * The search path can handle only 6 records, and 3 of those records are provided by Compute Engine. If you add entries to the search path such that the total number of entries is greater than 6, search rules after the 6th entry are not applied by your OS. This can cause Compute Engine features to stop working, such as accessing instances by using their instance names.
  * Manually editing `resolv.conf` results in it being reverted to the default DHCP every time the 24-hour DHCP lease expires on your instance. On instances using zonal DNS, the DHCP lease expires every hour. To make static modifications in the `resolv.conf` file, several Linux distributions allow items to be prepended or appended to the [DHCP policy](https://www.isc.org/wp-content/uploads/2017/08/dhcp41clientconf.html).




###  Zonal DNS config 

Sample zonal `resolv.conf` file:
    
    
    # Local domain name. Computed from your project name.
    domain ZONE.c.PROJECT_ID.internal
    # Search list for hostname lookup. Starting with entries that represent
    # your project and ending with google.internal to facilitate metadata server requests.
    search ZONE.c.PROJECT_ID.internal. c.PROJECT_ID.internal. google.internal.
    # Address of the DNS server to resolve project specific, and global domain names.
    nameserver MDS_IP_ADDRESS
    

Replace the following:

  * `ZONE`: the zone where your instance is located
  * `PROJECT_ID`: the project to which the instance belongs
  * `MDS_IP_ADDRESS`: the IP address of the instance's metadata server, which is one of the following: 
    * `169.254.169.254` for IPv4-only and dual-stack instances.
    * `fd20:ce::254` for IPv6-only instances.



Sample zonal `dhcp.lease` file:
    
    
    lease {
      # What interface we are using for the network
      interface "eth0";
      fixed-address 10.128.0.9;
      option subnet-mask 255.255.255.255;
      option routers 10.128.0.1;
      # Lease timeout, older instances will have this value set to infinite.
      option dhcp-lease-time 3600;
      option dhcp-message-type 5;
      option domain-name-servers MDS_IP_ADDRESS;
      option dhcp-server-identifier MDS_IP_ADDRESS;
      option interface-mtu 1460;
      # Search path options that are copied into the resolv.conf
      option domain-search "ZONE.c.PROJECT_ID.internal.", "c.PROJECT_ID.internal.", "google.internal.";
      option ntp-servers MDS_IP_ADDRESS;
      option rfc3442-classless-static-routes 32,10,128,0,1,0,0,0,0,0,10,128,0,1;
      option host-name "INSTANCE_NAME.ZONE.c.PROJECT_ID.internal";
      option domain-name "ZONE.c.PROJECT_ID.internal";
      renew 4 2017/11/16 02:15:52;
      rebind 4 2017/11/16 02:43:59;
      expire 4 2017/11/16 02:51:29;
    }
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance
  * `ZONE`: the zone where your instance is located
  * `PROJECT_ID`: the project to which the instance belongs
  * `MDS_IP_ADDRESS`: the IP address of the instance's metadata server, which is one of the following: 
    * `169.254.169.254` for IPv4-only and dual-stack instances.
    * `fd20:ce::254` for IPv6-only instances.



###  Global DNS config 

Sample global `resolv.conf` file:
    
    
    # Local domain name. Computed from your project name.
    domain c.PROJECT_ID.internal
    # Search list for hostname lookup. Starting with entries that represent
    # your project and ending with google.internal to facilitate metadata server requests.
    search c.PROJECT_ID.internal google.internal.
    # Address of the DNS server to resolve project specific, and global domain names.
    nameserver MDS_IP_ADDRESS
    

Replace the following:

  * `PROJECT_ID`: the project to which the instance belongs
  * `MDS_IP_ADDRESS`: the IP address of the instance's metadata server, which is one of the following: 
    * `169.254.169.254` for IPv4-only and dual-stack instances.
    * `fd20:ce::254` for IPv6-only instances.



Sample global `dhcp.lease` file:
    
    
    lease {
      # What interface we are using for the network
      interface "eth0";
      fixed-address 10.128.0.8;
      option subnet-mask 255.255.255.255;
      option routers 10.128.0.1;
      # Lease timeout, older instances will have this value set to infinite.
      option dhcp-lease-time 86400;
      option dhcp-message-type 5;
      option domain-name-servers MDS_IP_ADDRESS;
      option dhcp-server-identifier MDS_IP_ADDRESS;
      option interface-mtu 1460;
      # Search path options that are copied into the resolv.conf
      option domain-search "c.PROJECT_ID.internal.", "google.internal.";
      option ntp-servers MDS_IP_ADDRESS;
      option rfc3442-classless-static-routes 32,10,128,0,1,0,0,0,0,0,10,128,0,1;
      option host-name "INSTANCE_NAME.c.PROJECT_ID.internal";
      option domain-name "c.PROJECT_ID.internal";
      renew 4 2017/11/16 12:07:00;
      rebind 4 2017/11/16 22:44:53;
      expire 5 2017/11/17 01:44:53;
    }

Replace the following:

  * `INSTANCE_NAME`: the name of the instance
  * `PROJECT_ID`: the project to which the instance belongs
  * `MDS_IP_ADDRESS`: the IP address of the instance's metadata server, which is one of the following: 
    * `169.254.169.254` for IPv4-only and dual-stack instances.
    * `fd20:ce::254` for IPv6-only instances.



### Example `dhclient.conf` file

Some operating systems, such as Debian 9, use the `dhclient.conf` file instead of the `resolv.conf` file.

Sample `/etc/dhcp/dhclient.conf` file:
    
    
    # Configuration file for /sbin/dhclient.
    #
    ...
    append domain-search "mydomain.com";
    prepend domain-name-servers 172.16.1.1;
    

In this example, `mydomain.com` is the new search domain and `172.16.1.1` is the IP of your DNS server.

## What's next

  * For information about Google Cloud VPC networks, see the [VPC overview](https://docs.cloud.google.com/vpc/docs/vpc).
  * For information about creating and modifying VPC networks, see [Using VPC](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * Migrate your organization and projects to [use zonal DNS instead of global DNS](https://docs.cloud.google.com/compute/docs/networking/zonal-dns).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
