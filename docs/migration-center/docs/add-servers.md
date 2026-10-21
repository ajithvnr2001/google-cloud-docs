---
url: https://docs.cloud.google.com/migration-center/docs/add-servers/
title: Add server assets \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:22.189347+00:00
---

# Add server assets  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/add-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Add server assets Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can add servers to the discovery client, and how you can use it to collect data from those servers.

You can automatically identify the server assets in your infrastructure using the discovery client IP scan feature, or you can manually add your servers' IP addresses.

## Overview

After you create the credentials, you can start adding servers to your inventory of machines that the discovery client scans.

If you provide a range of IP addresses, the discovery client can automatically ping each IP address in the range to identify the responsive IP addresses. Then, it uses the credentials already added in the application to access the discovered servers, and adds them to the inventory. This approach is useful when you have a large number of servers to add, or you're not sure about the exact IP addresses of your infrastructure.

Alternatively, you can manually add your servers one by one from the application, or by providing a CSV file with a list of IP addresses. This approach is useful when you have a limited number of servers to scan and you know exactly their IP addresses.

## Before you begin

  * Add the credentials that the discovery client uses to access your servers.



## Limitations

  * The discovery client application supports the discovery of up to 10,000 servers.
  * You can create up to 100 IP ranges. Each IP range can contain at most 65,536 IPs.
  * The discovery client supports IP addresses using the IPv4 protocol.



## Automatically add servers to scan

The discovery client can automatically identify servers to add to your inventory with the IP range scan feature. When performing an IP range scan, the discovery client sends Internet Control Message Protocol (ICMP) requests with the `ping` command. To be able to use IP range scan, make sure that your firewall rules allow ICMP requests from the discovery client.

You can manually add each IP range from the application UI, or upload a CSV file with a list of ranges.

### Add IP ranges from the application UI

To add a new range of IP addresses to scan from the application UI, do the following:

  1. In the discovery client application, go to the **Discovery** tab.
  2. In the **IP addresses/ranges** page, click **Add IP addresses > Add ranges manually**, then agree to the terms and conditions for the scan.
  3. Enter the initial and final IP addresses of the range. To add another range to the same scan, click **Add IP range** , then enter the new pair of IP addresses.

**Tip:** Include all the IP ranges that share the same credentials for authentication in the same list.

  4. To finish, click **Save**.




### Import IP ranges from CSV

To add multiple IP ranges at the same time, follow these steps:

  1. In the discovery client application, go to the **Discovery** tab.
  2. In the **IP addresses/ranges** page, click **Add IP addresses > Add ranges via CSV**, then agree to the terms and conditions for the scan.
  3. In the new dialog that appears, download the template and fill in the IP address ranges that you want to scan. The template has the following format:
         
         "StartIpAddress","EndIpAddress"
         10.10.10.1,10.10.10.255
         10.10.11.1,10.10.11.255
         

  4. Browse to upload the template that you modified with your ranges, then click **Upload**.




After you upload the file, the discovery client scans all the IP addresses in the ranges and pings each server.

To verify which servers are discovered, follow these steps:

  1. In the **Discovery** tab, click **IP addresses**.
  2. From the list of IP ranges, click the range that you want to view.
  3. In the **Scan details** section, review the list of IP addresses of the discovered servers and their status.



### Import IP addresses from CSV

To add multiple IP addresses at the same time, follow these steps:

  1. In the discovery client application, go to the **Discovery** tab.
  2. In the **IP addresses/ranges** page, click **Add IP addresses > Add address list via CSV**, then agree to the terms and conditions for the scan.
  3. In the new dialog that appears, download the template and fill in the IP addresses that you want to scan. The template has the following format:
         
         ipAddress
         10.10.10.10
         10.10.10.11
         

  4. Browse to upload the file that you modified with your addresses, then click **Upload**.




### Scan statuses

When you perform a server scan, the servers that you discover appear in one of the following statuses:

  * **Success:** The discovery client pinged and authenticated to the server correctly.
  * **Already listed:** The server was already added to your inventory during a previous scan.
  * **Authentication failed:** The discovery client was able to ping the server, but couldn't authenticate using the credentials provided.
  * **Pending validation:** In case of an IP addresses list, this is the server status before the discovery client completed the attempts to find a credentials match.



## Manually add servers to scan

If you have individual servers in your infrastructure that you want to scan, you can manually specify the connection details and credentials. Follow these steps:

  1. In the discovery client application, go to the **Servers** tab.
  2. Click **Add information manually**.
  3. In the **Add information manually** page that opens, enter the following information: 
     1. The credentials needed to connect to the server
     2. The name of the server
     3. The IP address of the server
     4. The OS type of the server
  4. To verify that the information you entered is correct, click **Test connection**.
  5. Optional: to customize the scanning schedule, do the following: 
     1. Click the **Schedules for opting out of scanning** to the on position.
     2. Click **Create new opt-out schedule**.
     3. Enter a name for your opt-out schedule. You can later use the same schedule for other assets.
     4. Select the days when the collection shouldn't run.
     5. For each day, select the two-hour time slots when the collection shouldn't run.
     6. To create your opt-out schedule, click **Save and continue**.
  6. To confirm the server details, click **Save**.



## Add vCenter for discovery

To discover your vCenter VMs, follow these steps:

  1. In the discovery client application, go to the **Discovery** tab.
  2. Click **vCenter**.
  3. In the **vCenter** page, click **Add vCenter.**
  4. In the **Add vCenter** page that opens, enter the following information: 
     1. The credentials needed to connect to the vCenter.
     2. The URL of the vCenter. For example: `https://172.0.0.1` or `http://172.0.0.1`.
     3. Optional: to reduce the scope of the collection, add the inventory path. For example: `MyDataCenter/vm`.
     4. Optional: to run a guest discovery of your servers, provide the guest credentials for Linux and Windows machines.
     5. Select if you want to allow HTTPS access using self-signed, less secure certificates.
     6. Select if you want to turn on performance data collection on vCenter.
  5. To verify that the information you entered is correct, click **Test connection**.
  6. To confirm the server details, click **Save**.



## Configure the scan schedule

The discovery client lets you configure when to scan your infrastructure. By default, the discovery client performs a full collection every 24 hours, and collects performance data every 10 minutes, but you can choose to pause the collection during specific days and hours of the week. This is useful, for example, to avoid additional load on your machines during peak times, or to stop the collection when you're not using your machines, to avoid skewing the performance data.

To configure a scan schedule for servers that are already present in the discovery client, follow these steps:

  1. In the discovery client application, go to the **Servers** tab.
  2. From the list of available servers, select those for which you want to customize the schedule, then click **Configure schedule**.
  3. If you have already created a scan schedule, click **Select existing opt-out schedule** , then select the schedule from the list. Otherwise, click **Create new opt-out schedule** and do the following: 
     1. Enter a name for your opt-out schedule. You can later use the same schedule for other assets.
     2. Select the days when the collection shouldn't run.
     3. For each day, select the two-hour time slots when the collection shouldn't run.
  4. To confirm your opt-out schedule, click **Save**.



## What's next

  * Learn how to [manage discovery client](https://docs.cloud.google.com/migration-center/docs/manage-discovery-client).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
