---
url: https://docs.cloud.google.com/compute/docs/instances/time-synchronization/configure-ntp/
title: Configure NTP on a compute instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:59.385437+00:00
---

# Configure NTP on a compute instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/time-synchronization/configure-ntp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure NTP on a compute instance Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Many software systems that depend on careful sequencing of events rely on a stable, consistent system clock. These systems often use system logs with timestamps to ensure time synchronization and debug issues as they occur. To help keep system clocks in sync, Compute Engine instances are preconfigured to use _network time protocol (NTP)_ , a bundled solution of time synchronization hardware and software.

NTP is also helpful in the rare case of a _leap second_ , a one-second adjustment made to UTC time to account for changes in the Earth's rotation. Leap seconds don't happen at routine intervals, because the Earth's rotation speed varies irregularly in response to climatic and geological events. Previous leap seconds have noticeably impacted a variety of services and applications on the web. NTP servers help ensure that all servers report the same time during the event of a leap second.

This document describes how to configure NTP servers on your compute instances, including proper handling of leap seconds.

## Overview of Google NTP servers and leap smearing

Leap seconds for a Unix operating system are commonly implemented by repeating the last second of the day. This can cause problems with software that expects timestamps to only ever increase. To get around this problem, the time servers at Google Cloud "[smear](https://googleblog.blogspot.ca/2011/09/time-technology-and-leaping-seconds.html)" the extra second over 24 hours—12 before and 12 after the leap second event—so that computers don't see the extra second all at once as a repeated timestamp. This reduces risk in systems that depend on a consistent timestamp. We recommend that you configure all of your compute instances to use the internal Google NTP services.

## Recommendation against using external NTP services

Google Cloud can't predict how external NTP services, such as `pool.ntp.org`, handle leap seconds. We strongly recommend that you don't use external NTP sources with your compute instances. If you use both Google's NTP service and an external service, you can cause unpredictable changes in the system time. Using only a single external NTP source is preferable to using a mix, but external NTP services, such as `pool.ntp.org`, often use stepping to handle leap seconds. As a result, your instances might see repeated timestamps.

The safest approach is to configure your compute instances to use a single NTP server—the internal NTP server provided by Google. For more information about the internal NTP server provided by Google, see the [Google Public NTP FAQ](https://developers.google.com/time/faq).

### Use leap smearing with systems external to Google Cloud

The [leap smearing](https://developers.google.com/time/smear) feature of Google's NTP servers is a convenient way to manage the risk involved with replaying a second on time-sensitive systems. Other NTP services might provide an acceptable workaround for most software systems. However, it's important that you don't mix Google leap smearing NTP services with public NTP stepping services.

To synchronize devices outside Google Cloud to smeared time, you can use [Google Public NTP](https://developers.google.com/time/) for those devices. The Google Public NTP uses the same leap second smearing that's provided to Compute Engine instances.

## Configure NTP for your instances

To ensure your compute instances are correctly configured, follow these instructions:

###  Linux (chrony) 

By default, the majority of Linux releases use [`chrony`](https://chrony.tuxfamily.org/) to manage their NTP settings and time synchronization. To make sure that `chrony` uses only the internal NTP service, check the `chrony` configuration and remove external NTP servers.

  1. Use `ssh` to connect to your compute instance.

###  Console 

To use the console to connect to the compute instance using SSH, follow these steps:

     1. Go to the **VM instances** page in the Google Cloud console.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the **SSH** button for the instance that you want to configure.

![SSH button.](https://docs.cloud.google.com/static/compute/images/ssh-console-screenshot.png)

###  gcloud 

To use the Google Cloud CLI to connect to the compute instance using SSH, run the following command:
    
    gcloud compute instances ssh INSTANCE_NAME
    

Replace `INSTANCE_NAME` with the name of the instance that you're connecting to.

  2. On your instance, run `chronyc sources` to check the current state of your NTP configuration:
         
         $ chronyc sources
         

The output looks similar to the following:
         
         210 Number of sources = 2
          MS Name/IP address         Stratum Poll Reach LastRx Last sample
          ===============================================================================
          ^* metadata.google.internal      2   6   377     4    -14us[  -28us] +/-  257us
          ^- 38.229.53.9                   2   6    37     4   -283us[ -297us] +/-   28ms
         

If you see a single record pointing at `metadata.google` or `metadata.google.internal`, you don't need to make any changes. If you see multiple sources, mixed between `metadata.google` and a public source such as `pool.ntp.org`, update your sources to remove any external NTP servers.

In the example output, there are two records, one pointing at `metadata.google.internal` and another pointing to an external address. Because there are multiple sources, you would update your NTP servers to remove the `38.229.53.9` address, as described in the next step.

  3. Configure your NTP servers to remove external NTP servers.

To remove the additional NTP server from the list, edit the `/etc/chrony/chrony.conf` file using your favorite text editor. Find all the lines that start with `server external_source_ip_or_name` and remove them.

After editing your `/etc/chrony/chrony.conf` file, restart the `chrony` service. The command to restart might vary depending on the Linux distribution, as shown in the following examples:
         
         sudo service chrony restart
         
         
         sudo systemctl restart chrony
         

  4. Verify your configuration by running the `chronyc sources` command again:
         
         $ chronyc sources
         

The output should look similar to the following: 
         
         210 Number of sources = 1
          MS Name/IP address         Stratum Poll Reach LastRx Last sample
          ===============================================================================
          ^* metadata.google.internal      2   7   377    98  -1343ns[-1588ns] +/-  396us
         




###  Linux (ntpd) 

Older Linux distributions that don't support `chrony` instead use [`ntpd`](https://en.wikipedia.org/wiki/Ntpd) to manage their NTP settings and time synchronization. To make sure that `ntpd` uses only the internal NTP service, check the `ntpd` configuration and remove external NTP servers.

  1. Use `ssh` to connect to your compute instance.

###  Console 

To use the console to connect to the compute instance using SSH, follow these steps:

     1. Go to the **VM instances** page in the Google Cloud console.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the **SSH** button for the instance that you want to configure.

![SSH button.](https://docs.cloud.google.com/static/compute/images/ssh-console-screenshot.png)

###  gcloud 

To use the Google Cloud CLI to connect to the compute instance using SSH, run the following command:
    
    gcloud compute instances ssh INSTANCE_NAME
    

Replace `INSTANCE_NAME` with the name of the instance that you're connecting to.

  2. On your instance, run `ntpq -p` to check the current state of your NTP configuration:
         
         $ ntpq -p
         

The output looks similar to following:
         
         remote           refid           st t when poll reach   delay   offset  jitter
         
         ==============================================================================
         *metadata.google 255.28.23.83     2 u   27   64    1    0.634   -2.537   2.285
         *217.162.232.173 130.149.17.8     2 u  191 1024  176   79.245    3.589  27.454
         

If you see a single record pointing at `metadata.google` or `metadata.google.internal`, you don't need to make any changes. If you see multiple sources, mixed between `metadata.google` and a public source such as `pool.ntp.org`, you must update your sources to remove any external NTP servers.

In the example output, there are two records, one pointing at `metadata.google` and another pointing to an external address. Because there are multiple sources, you would need to update your NTP servers to remove the `*217.162.232.173` address, as described in the next step.

  3. Configure your NTP servers to remove external sources.

To configure your NTP servers, edit the `/etc/ntp.conf` file using your preferred text editor. Find the `servers` section of the configuration, and remove all non-Google NTP sources, for example:
         
         vim /etc/ntp.conf
         
         
         # You do need to talk to an NTP server or two (or three).
         #server ntp.your-provider.example
         ...
         server metadata.google.internal iburst
         

After editing your `/etc/ntp.conf` file, restart the NTP service. The command to restart might vary from the following example, based on your Linux distribution:
         
         sudo service ntp reload
         

**Note:** By default, the DHCP client adds a list of NTP servers to the `ntp.conf` file. If you're using an enterprise Linux distribution and if you want to ignore the NTP configuration provided by the DHCP client, add `PEERNTP=no` in the `/etc/sysconfig/network` file.
  4. Verify your configuration by running the `ntpq -p` command again:
         
         ntpq -p
         
         
         remote           refid           st t when poll reach   delay   offset  jitter
         ==============================================================================
         *metadata.google 255.28.23.83     2 u   27   64    1    0.634   -2.537   2.285
         




###  Windows 

  1. Go to the **VM instances** page in the Google Cloud console.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **RDP** button next to the Windows instance that you want to connect to.

![SSH button.](https://docs.cloud.google.com/static/compute/images/rdp-console.png)

  3. After you're logged in, right-click on the PowerShell icon and select **Run as administrator**.

![The PowerShell icon.](https://docs.cloud.google.com/static/compute/images/powershellicon.png)

  4. When the command-prompt loads, run the following command to see the current NTP configuration:
         
         w32tm /query /configuration
         
         
         [Configuration]
         ...
         Type: NTP (Local)
         NtpServer: metadata.google.internal,
         ...
         

If you see a single record pointing at `metadata.google` or `metadata.google.internal`, you don't need to make any changes. If you see multiple sources, mixed between `metadata.google` and a public source, you need to remove the external server. Follow the [Windows' guide](https://support.microsoft.com/kb/816042) for configuring your NTP server.

  5. To ensure the most widespread software compatibility on Windows VMs, Google recommends that you use the [gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) to ensure sub-millisecond NTP accuracy with `metadata.google`.

If you must use VirtIO with your Windows VM, to get sub-millisecond accuracy with NTP servers, Google recommends that you don't use the Windows Time Service (stop and unregister `w32tm`).

     1. Stop the Windows Time Service:
            
            net stop w32time
            

     2. Remove the Windows Time Service from the registry:
            
            w32tm /unregister
            

     3. After the Windows Time Service has been stopped and removed from the registry, install the [Meinberg NTP client](https://www.meinbergglobal.com/english/sw/ntp.htm).

Follow the configuration instructions as provided in the Meinberg documentation.

     4. Configure the NTP server for the Meinberg NTP client as `metadata.google.internal`.

After you finish configuring NTP, wait between five and 15 minutes for the system clock in the compute instance to stabilize with the NTP server.

For information about why we don't recommend using `w32tm`, see the [Known Issues documentation](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#ntp-drift).




## What's next

  * Learn more about [PCI Data Security Standard compliance](https://docs.cloud.google.com/architecture/pci-dss-compliance-in-gcp).
  * Review the [Google Public NTP FAQ](https://developers.google.com/time/faq).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
