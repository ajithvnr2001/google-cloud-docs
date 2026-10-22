---
url: https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/test-connectivity-netapp-volumes/
title: Test connectivity to Google Cloud NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:16.226628+00:00
---

# Test connectivity to Google Cloud NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/test-connectivity-netapp-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Test connectivity to Google Cloud NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to test connectivity to NetApp Volumes.

Using the `ping` command to test connectivity through routers and firewalls is a standard industry practice. The `ping` command and other network tools, such as `traceroute`, use the ICMP protocol.

The service responds to ICMP on the following interfaces or IP addresses:

  * All NFS or SMB IP addresses of Standard, Premium, and Extreme service levels.

  * All intercluster IP addresses of Standard, Premium, and Extreme service levels. Intercluster IPs are used for SnapMirror-based features, such as volume migration and external replication.

  * Flex Unified iSCSI and intercluster IP addresses.




The service doesn't respond to ICMP on the following interfaces or IP addresses:

  * All Flex File pools IP addresses

  * Flex Unified NFS or SMB IP addresses




To test connectivity to a service IP that doesn't respond to ICMP, connect to a service TCP port instead to verify that it's open. You can use this method as an alternative to `ping`.

On Linux clients, run the following CLI command:
    
    
    timeout 2 bash -c '/dev/tcp/VOLUME_IP/PORT && echo Port is open || echo Port is closed' || echo Connection timeout
    

On Windows clients, run the following PowerShell command:
    
    
    Test-NetConnection -ComputerName VOLUME_IP -Port PORT
    

Replace the following information:

  * `VOLUME_IP`: the NetApp Volumes IP address you want to connect to.

  * `PORT`: specify a service port number. For example, common ports include `2049/TCP` for NFS and `445/TCP` for SMB.




## What's next

[Known issues and limitations](https://docs.cloud.google.com/netapp/volumes/docs/troubleshoot/known-limitations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
