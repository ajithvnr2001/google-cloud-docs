---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes/
title: Connect large capacity volumes with multiple storage endpoints \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:27.050528+00:00
---

# Connect large capacity volumes with multiple storage endpoints  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Connect large capacity volumes with multiple storage endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about connecting large capacity volumes with multiple storage endpoints.

Large capacity volumes provide access to the same volume through six endpoints or IP addresses. While you can mount all of your clients to just one of these IP addresses, it is recommended to spread your clients over all six IP addresses to distribute the load they generate and achieve higher aggregated throughput. The six IP addresses are provided within the volume export path or mount instructions.

One approach is to set up round-robin DNS, where the same DNS name maps to all of the six IP addresses. Clients then use the DNS name to mount the volume. While the clients will be distributed across the six IP addresses, you can't control which client connects to the same IP address.

  * For SMB access, NetApp Volumes automatically registers all six IP addresses under the volume's computer name in Active Directory DNS. SMB clients then look for the name when mapping the volume.

  * For NFS access, you have to manually create a DNS entry and add the six IP addresses to it. For more information about how to add a DNS record, see [Cloud DNS](https://docs.cloud.google.com/dns/docs/records#add_a_record). Note that NFS clients resolve the DNS name to an IP address during the mounting of the volume. To ensure that an NFS client picks up new settings from DNS, you need to remount the volume.




Another approach for NFS clients is to manually group the clients into six groups, and mount each group of clients to one of the six IP addresses. This approach lets you control the exact group of clients that connect to a single IP address, which can be useful if you want to fine-tune the load-balancing.

For more information about large capacity volumes, see [About volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview).

## What's next

[Protect your data](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/protect-your-data).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
