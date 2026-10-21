---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/net-ip_in_range_cidr/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:52:12.046612+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/net-ip_in_range_cidr/




Stay organized with collections  Save and categorize content based on your preferences. 

### net.ip_in_range_cidr

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search)
    
    
    net.ip_in_range_cidr(ipAddress, subnetworkRange)
    

#### Description

Returns `true` when the given IP address is within the specified subnetwork.

You can use YARA-L to search for UDM events across all of the IP addresses within a subnetwork using the `net.ip_in_range_cidr()` statement. Both IPv4 and IPv6 are supported.

To search across a range of IP addresses, specify an IP UDM field and a CIDR range. YARA-L can handle both singular and repeating IP address fields.

To search across a range of IP addresses, specify an `ip` UDM field and a Classless Inter-Domain Routing (CIDR) range. YARA-L can handle both singular and repeating IP address fields.

#### Param data types

`STRING`, `STRING`

#### Return type

`BOOL`

#### Code samples

##### Example 1

IPv4 example:
    
    
    net.ip_in_range_cidr($e.principal.ip, "192.0.2.0/24")
    

##### Example 2

IPv6 example:
    
    
    net.ip_in_range_cidr($e.network.dhcp.yiaddr, "2001:db8::/32")
    

For an example rule using the `net.ip_in_range_cidr()`statement, see the example rule in [Single Event within Range of IP Addresses](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-overview#single_event_within_range_of_ip_addresses).)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
