---
url: https://docs.cloud.google.com/compute/docs/networking/monitor-dns-failures/
title: Use Cloud DNS logs to monitor DNS failure rates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:29.921664+00:00
---

# Use Cloud DNS logs to monitor DNS failure rates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/monitor-dns-failures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Use Cloud DNS logs to monitor DNS failure rates Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

You can enable Cloud DNS query logs in your Compute Engine project and use those logs to monitor and compare internal DNS failure rates before and after migration to zonal internal DNS. Log entries record successful DNS resolution and when internal DNS fails to resolve a given domain name.

## Overview

To use Cloud DNS query logs to monitor internal DNS failure rates, complete the following steps:

  1. Get the Virtual Private Cloud (VPC) network name for the VPC that contains the VMs to monitor.
  2. Using the VPC network names, run a Google Cloud CLI command to enable DNS query logging.
  3. Run queries in Logs Explorer to visualize and investigate success and failure rates.



## Pricing information for Cloud DNS query logging

When you enable Cloud DNS query logging, it generates a significant amount of logs, many of which are not related to internal DNS. As a result, you might incur a cost for using this feature. In general, the first 50 GiB of log storage per project per month is free. Each additional 50 GiB costs $0.50 USD.

For more information about the pricing, see [Cloud Logging pricing summary](https://cloud.google.com/stackdriver/pricing).

## Get the Virtual Private Cloud (VPC) network names

To capture DNS query data, you must enable logging for the VPC network that is used by your compute instance. Often, a Google Cloud project has multiple VPC networks. You can use a gcloud CLI command to list the VPC networks used by the compute instances that you want to monitor.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Optional: Use the filter_list **Filter** box to restrict the number of instances shown.

  3. Click the name of the instance that you want to inspect.

  4. In the **Networking** section, under **Network interfaces** , you can see the network interfaces (NICs) created for the instance, the network and subnet associated with each NIC, and their assigned IP addresses.




###  gcloud 

  * To view the VPC networks used by all compute instances in a project, use the [`gcloud compute instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list). You can append a `--format` option to the command to restrict the information returned to specific fields and change how it is displayed, for example:
        
        gcloud compute instances list \
          --format="flattened(name,networkInterfaces[].name, \
            networkInterfaces[].network.basename(), \
            networkInterfaces[].stackType, networkInterfaces[].nicType)"
        

The output is similar to the following:
        
        name:                           test-gvnic
        networkInterfaces[0].name:      nic0
        **networkInterfaces[0].network:   default**
        networkInterfaces[0].nicType:   GVNIC
        networkInterfaces[0].stackType: IPV4_ONLY
        ---
        name:                           test-multinic
        networkInterfaces[0].name:      nic0
        **networkInterfaces[0].network:   default**
        networkInterfaces[0].nicType:   GVNIC
        networkInterfaces[0].stackType: IPV4_ONLY
        networkInterfaces[1].name:      nic0.14
        **networkInterfaces[1].network:   net0**
        networkInterfaces[1].stackType: IPV4_ONLY
        networkInterfaces[2].name:      nic1
        **networkInterfaces[2].network:   prod-ipv6**
        networkInterfaces[2].nicType:   GVNIC
        networkInterfaces[2].stackType: IPV4_IPV6
        

  * To view the network interfaces (NICs) for a specific compute instance and its assigned VPC networks, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe). You can append a `--format` option to the command to restrict the information returned to specific fields and change how it is displayed, for example:
        
        gcloud compute instances describe INSTANCE_NAME --zone=ZONE \
          --format="flattened(name,networkInterfaces[].name, \
          networkInterfaces[].network.basename(), \
          networkInterfaces[].stackType, networkInterfaces[].nicType)"
        

Replace the following:

    * `INSTANCE_NAME`: the name of the instance to view
    * `ZONE`: the zone for the instance that you want to view

The output is similar to the following:
    
    name:                           test-instance
    networkInterfaces[0].name:      nic0
    **networkInterfaces[0].network:   default**
    networkInterfaces[0].nicType:   GVNIC
    networkInterfaces[0].stackType: IPV4_ONLY
    networkInterfaces[1].name:      nic1
    **networkInterfaces[1].network:   prod-ipv6**
    networkInterfaces[1].nicType:   GVNIC
    networkInterfaces[1].stackType: IPV4_IPV6
    networkInterfaces[1].name:      nic1.2
    **networkInterfaces[1].network:   alt-ipv6-net**
    networkInterfaces[1].nicType:   GVNIC
    networkInterfaces[1].stackType: IPV4_IPV6
    networkInterfaces[1].parentNicName: nic1
    




## Enable Cloud DNS query logging

Cloud DNS logging tracks queries that name servers resolve for your VPC networks, as well as queries from an external entity directly to a public zone.

Logged queries can come from Compute Engine instances, Google Kubernetes Engine containers in the same VPC network, peering zones, or on-premises clients that use inbound DNS forwarding. Private DNS zones, forwarding DNS zones, alternative name servers, internal Google Cloud DNS zones, or external DNS zones might eventually resolve the queries.

Log records belong to the project that owns the network or public zone that carried the request. In the case of Shared VPC, the log records belong to the host project because the host project owns the network.

To enable DNS logging, do one of the following:

  * Create a new DNS policy with logging enabled by running the [`gcloud dns policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create).
        
        gcloud dns policies create POLICY_NAME \
            --networks=NETWORK_NAMES \
            --enable-logging \
            --description="Enable DNS query logging for NETWORK_NAMES"
        

  * If the network already has DNS policy, update the existing logging policy by running the [`gcloud dns policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/update).
        
        gcloud dns policies update POLICY_NAME \
           --networks=NETWORK_NAMES \
           --enable-logging
        




Replace the following:

  * POLICY_NAME: the name of the DNS policy
  * NETWORK_NAMES: a comma-separated list of network names



For detailed instructions on how to create and enable DNS policies for logging, see [Use Cloud DNS logging](https://docs.cloud.google.com/dns/docs/monitoring).

## Use Logs Explorer to view the logs and visualize DNS failure rates

After you enable DNS logging, the project starts to accumulate logs in Logs Explorer. To view these logs, use the Google Cloud console and go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer?resource=dns_query)

### Monitor DNS name resolution failures

Use the `NXDOMAIN` response code to isolate non-existent domain failures. These failures occur when internal DNS fails to resolve a given domain name.

  1. In the query box on the **Logs Explorer** console page, enter the following text:
         
         resource.type="dns_query"
         jsonPayload.queryType="A"
         jsonPayload.queryName=~"\.internal\.$"
         jsonPayload.responseCode = "NXDOMAIN"
         

  2. Click **Run query**.


**Note:** Some failures are normal when using non-fully qualified domain names (FQDN) for compute instances because of how the DNS resolver uses search paths to facilitate communication.

### Monitor successful name resolution queries

Use the `NOERROR` response code to isolate successful DNS resolution.

  1. In the query box on the **Logs Explorer** console page, enter the following text:
         
         resource.type="dns_query"
         jsonPayload.queryType="A"
         jsonPayload.queryName=~"\.internal\.$"
         jsonPayload.responseCode = "NOERROR"
         

  2. Click **Run query**.




### Establish an analysis timeframe

You can use the logs time range selector to change the timeframe for the analyzed logs. This selector is found in the top right corner of the **Logs Explorer** window.

For an effective comparison of error and success rates you must enable DNS query logs prior to migrating to using zonal DNS. Google recommends that you enable DNS query logging at least 24 hours before the migration to establish a pre-migration baseline.

After you have collected enough data in the DNS query logs, you can perform the zonal DNS migration. You can monitor DNS resolution rates during the migration to ensure that the migration doesn't cause an increase in DNS query failures.

### Analyze and compare DNS name resolution rates

Use the following to analyze and compare the error and success rates.

  * **Log Counts** : For each query and time period, Logs Explorer shows the number of log entries found. A significant increase in `NXDOMAIN` counts post-migration for DNS names that previously resolved (had `NOERROR`) could indicate a problem.

  * **Histogram** : The Logs Explorer interface includes a histogram. When your queries are run, the histogram shows the frequency of matching log entries over the selected time range. This is useful for visualizing:

    * A baseline rate of `NXDOMAIN` log entries before migration.
    * Any spikes in `NXDOMAIN` log entries immediately after migration.
    * Changes in the rate of `NOERROR` log entries.

To see the histogram, click **Preferences** , and then click **View** , and then click **Show timeline**.




## What's next

  * Learn more about [internal DNS for Compute Engine](https://docs.cloud.google.com/compute/docs/internal-dns).
  * [View the network configuration](https://docs.cloud.google.com/compute/docs/instances/view-network-properties) for your compute instances.
  * Learn more about how to [view logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
