---
url: https://docs.cloud.google.com/filestore/docs/unresponsive/
title: Troubleshoot Filestore instance response errors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:49.458942+00:00
---

# Troubleshoot Filestore instance response errors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/unresponsive/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Troubleshoot Filestore instance response errors Stay organized with collections  Save and categorize content based on your preferences. 

The following sections describe scenarios where an instance might be unresponsive and provides steps to help address the issue.

## Filestore instance not responding to `ping` or `traceroute` requests

Filestore instances do not respond to `ping` or `traceroute` requests because Filestore doesn't allow ICMP.

To test for connectivity to a Filestore instance, you can run `showmount` from the client:
    
    
    sudo showmount -e filestore-ip
    

The Filestore instance responds with its exported file system, for example:
    
    
    Export list for 10.139.19.98:
    /vol1 192.168.0.0/16,172.16.0.0/12,10.0.0.0/8
    

You can also check whether the client can reach Filestore's RPC information by running:
    
    
    sudo rpcinfo -p <filestore-ip>
    

The response looks like:
    
    
    program vers proto   port  service
     100000    4   tcp    111  portmapper
     100000    3   tcp    111  portmapper
     100000    2   tcp    111  portmapper
     100000    4   udp    111  portmapper
     100000    3   udp    111  portmapper
     100000    2   udp    111  portmapper
     100024    1   udp   2046  status
     100024    1   tcp   2046  status
     100003    3   tcp   2049  nfs
     100227    3   tcp   2049
     100021    1   udp   4045  nlockmgr
     100021    3   udp   4045  nlockmgr
     100021    4   udp   4045  nlockmgr
     100021    1   tcp   4045  nlockmgr
     100021    3   tcp   4045  nlockmgr
     100021    4   tcp   4045  nlockmgr
     100005    3   udp   2050  mountd
     100005    3   tcp   2050  mountd
    

## Scheduled maintenance

Once in a while, Filestore becomes unresponsive for a few minutes and then becomes responsive again because of a scheduled maintenance event. For Filestore's SLA, see the [SLA](https://cloud.google.com/filestore/sla) page.

Filestore does not support customer-defined maintenance windows. The schedule for maintenance windows for Filestore is also unavailable to customers.

## Instance was deleted while still mounted to the client

If a file operation or unix command like `df`, `ls`, or any read/write operation stops responding, then the Filestore instance was likely deleted while still mounted to the client.

Check to see if the instance still exists:
    
    
        gcloud filestore instances list
    

If the instance is no longer listed, you can recover control by creating a new instance with the same IP address and file share name as the instance that was deleted. Once the instance is created, the unresponsive operation exits with an error. If you don't need the Filestore instance, you can unmount the file share and delete it.

To prevent something like this from happening in the future, make sure you unmount the Filestore instance first before deleting it.

## Instance shows status `REPAIRING`

The Filestore instance is in an unhealthy state from internal causes beyond the user's control and is automatically repairing itself. The instance is unavailable during this time and you don't need to take any further actions.

## Instance shows status `UNAVAILABLE`

If a change in Cloud KMS key state is detected, the instance automatically stops serving data. Some examples include the following:

  * [Disabling](https://docs.cloud.google.com/kms/docs/enable-disable#disable) a key or key version.
  * [Destroying](https://docs.cloud.google.com/kms/docs/destroy-restore#destroy) a key or key version.
  * Modifying a key's permissions.



For more information, see [Encrypt data with CMEKs](https://docs.cloud.google.com/filestore/docs/cmek#disable_or_destroy_a_key_thats_used_by_an_instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
