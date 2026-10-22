---
url: https://docs.cloud.google.com/dns/docs/monitoring/
title: Use logging and monitoring \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:31.586547+00:00
---

# Use logging and monitoring  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Use logging and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about logging and monitoring metrics for Cloud DNS including [public zones](https://docs.cloud.google.com/dns/docs/dns-overview#public_zone), [private zones](https://docs.cloud.google.com/dns/docs/overview#private_zone), and [forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones). This page also provides instructions for monitoring the propagation of your public DNS changes.

## Use Cloud DNS logging

Cloud DNS logging tracks queries that name servers resolve for your Virtual Private Cloud (VPC) networks, as well as queries from an external entity directly to a public zone.

Logged queries can come from Compute Engine virtual machine (VM) instances, Google Kubernetes Engine containers in the same VPC network, [peering zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#peering_zones), or on-premises clients that use [inbound DNS forwarding](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns-server-policy-in). Private DNS zones, forwarding DNS zones, alternative name servers, internal Google Cloud DNS zones, or external DNS zones might eventually resolve the queries.

Log records belong to the project that owns the network or public zone that carried the request. In the case of [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), the log records belong to the host project because the host project owns the network.

**Note:** Cloud DNS might respond to queries using cached responses. By default, cached responses are not logged. However, if logging is enabled, at least one prior response is logged before any subsequent cached response is served without logging.

### Enable logging for private managed zones

Use DNS policies to enable or disable logging for your networks. When you enable query logging, every DNS query to a Cloud DNS private managed zone is logged.

To enable logging for a network that does not have a DNS policy, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS policy** page.

[Go to Create a DNS policy](https://console.cloud.google.com/net-services/dns/policies/create)

  2. For **Name** , enter a name for your policy.

  3. Optionally, enter a description for **Description**.

  4. For **Logs** , select **On**.

  5. In the **Networks** section, click **Add networks** and choose the networks you need.

  6. Click **Create**.




###  gcloud 

Run the [`dns policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create) command.
    
    
    gcloud dns policies create POLICY_NAME \
        --networks=NETWORK \
        --enable-logging \
        --description=DESCRIPTION

Replace the following:

  * `POLICY_NAME`: the name of the DNS policy
  * `NETWORK`: one or more networks in a comma-separated list
  * `DESCRIPTION`: a description of the policy



To enable logging for a network that has an existing DNS policy, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS policies** page.

[Go to Cloud DNS policies](https://console.cloud.google.com/net-services/dns/policies/list)

  2. Click the DNS server policy you want to update.

  3. Click **Edit policy**

  4. In the **Logs** section, select **On**.

  5. Click **Save**.




###  gcloud 

Run the [`dns policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/update) command.
    
    
    gcloud dns policies update POLICY_NAME \
        --networks=NETWORK \
        --enable-logging
    

Replace the following:

  * `POLICY_NAME`: the name of the DNS policy
  * `NETWORK`: one or more networks in a comma-separated list



### Disable logging for private managed zones

To turn off logging while leaving the policy in place, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS policies** page.

[Go to Cloud DNS policies](https://console.cloud.google.com/net-services/dns/policies/list)

  2. Click the DNS server policy you want to update.

  3. Click **Edit policy**

  4. In the **Logs** section, select **Off**.

  5. Click **Save**.




###  gcloud 

Run the [`dns policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/update) command.
    
    
    gcloud dns policies update POLICY_NAME \
        --networks=NETWORK \
        --no-enable-logging

Replace the following:

  * `POLICY_NAME`: the name of the DNS policy
  * `NETWORK`: one or more networks in a comma-separated list



### Enable logging for managed public zones

To turn on logging for an existing managed public zone, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/zones/)

  2. Click the managed public zone you want to enable logging.

  3. Click **Edit**.

  4. In the **Cloud Logging** section, click **On**.

  5. Click **Save**.




###  gcloud 

Run the [`dns managed-zones update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update) command.
    
    
    gcloud dns managed-zones update ZONE_NAME --log-dns-queries \
    

Replace `ZONE_NAME` with the name of the DNS managed zone that you want to enable logging for.

### Disable logging for managed public zones

To turn off logging for an existing public managed zone.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/zones/)

  2. Click the managed public zone you want to enable logging.

  3. Click **Edit**.

  4. In the **Cloud Logging** section, click **Off**.

  5. Click **Save**.




###  gcloud 

Run the [`dns managed-zones update`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update) command.
    
    
    gcloud dns managed-zones update ZONE_NAME --no-log-dns-queries \
    

Replace `ZONE_NAME` with the name of the DNS managed zone that you want to disable logging for. 

### View logs

You can view logs in the Google Cloud console.

###  Console 

In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer?resource=dns_query)

#### View record format fields

Every log entry has the following fields, if applicable. Some of the fields are also shared with monitoring metrics.

Field | Field type | Description | Used in metrics  
---|---|---|---  
`alias_query_response_code` | String | The response code returned from the query to resolve the ALIAS record's canonical name | Yes  
`authAnswer` | Boolean / DNS | Authoritative answer, [IANA DNS Parameters: DNS Header Flags](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-12) | No  
`destinationIP` | String / Target | Target IP address, only applicable for forwarding cases | No  
`egressError` | String | Egress proxy error, the actual error reported by the egress proxy as received from the on-premises DNS server This field can be used to differentiate an actual SERVFAIL returned by the on-premises DNS versus a network error encountered by the egress proxy | No  
`egressPath` | String | If `none` or omitted, the query used the default standard Cloud DNS path, or `OUTBOUND_ENDPOINT` if the query was forwarded with an Outbound Endpoint | No  
`healthyIps` | String | Set of IP addresses in the ResourceRecordSet that are known to be `HEALTHY` to Cloud DNS at the time of the query | No  
`location` | String | Google Cloud region, for example `us-east1`, from which the response was served | Yes  
`outboundEndpoint.name` | String | User-provided name of the Outbound Endpoint (this string is only present if `egress_path` is `OUTBOUND_ENDPOINT`) | No  
`outboundEndpoint.projectId` | String | The Google Cloud project ID where the Outbound Endpoint is located (this string is only present if `egress_path` is `OUTBOUND_ENDPOINT`) | No  
`outboundEndpoint.location` | String | The Google Cloud region where the Outbound Endpoint is located (this string is only present if `egress_path` is `OUTBOUND_ENDPOINT`) | No  
`project_id` | String | Google Cloud project ID of the network from which the query was received | Yes  
`protocol` | String / DNS | `TCP` | `UDP` | No  
`queryName` | String / DNS | DNS query name, [RFC 1035 4.1.2](https://datatracker.ietf.org/doc/html/rfc1035#section-4.1.2) | No  
`queryType` | String / DNS | DNS query type, [IANA DNS Parameters: Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4) | No  
`responseCode` | Number / DNS | Response code, [IANA DNS Parameters: DNS RCODEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6) | No  
`rdata` | String / DNS | DNS answer in presentation format, [IANA DNS Parameters: Resource Record (RR) TYPEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4), truncated to 260 bytes | No  
`sourceIP` | String / Source | IP originating the query | No  
`sourceNetwork` | String / Source | Network from which the query reached our system | No  
`source_type` | String | Source of the query: `inbound-forwarding`, `gce-vm`, `internet`, `peering-zone`, `fqdn-forwarding-target` | No  
`target_name` | String | The target name, for example zone name, policy name, internal zone name, external domain name | Yes  
`target_type` | String | Type of target resolving the DNS query: `private-zone`, `forwarding-zone`, `forwarding-policy`, `peering-zone`, `internal`, `external`, `response-policy`, `service-directory-zone`, `reverse-lookup-zone`, `zonal-private-zone` | Yes  
`unHealthyIps` | String | Set of IP addresses in the ResourceRecordSet known to be `UNHEALTHY` to Cloud DNS at the time of the query | No  
`vmInstanceId` | Number / Source | Compute Engine VM instance ID, only applicable to queries initiated by Compute Engine VMs | No  
`vmInstanceName` | String / Source | Compute Engine VM instance name, only applicable to queries initiated by Compute Engine VMs | No  
`vmProjectId` | String / Source | Google Cloud project ID of the network from which the query was sent, only applicable to queries initiated by Compute Engine VMs | No  
`vmZoneName` | String / Source | Name of the VM zone from which the query was sent, only applicable to queries initiated by Compute Engine VMs | No  
  
## Pricing

All Cloud DNS logs are written to Cloud Logging. There is no separate charge from Cloud DNS for this service. However, these logs can result in additional storage costs depending on the size of the logs that are written and stored.

For calculation purposes, Cloud DNS writes approximately 5 MB of log data for processing 10,000 DNS queries.

For information about Cloud Logging pricing, see [Pricing for Google Cloud Observability: Cloud Logging](https://cloud.google.com/stackdriver/pricing).

## Troubleshoot outbound forwarding

If you receive logs containing `SERVFAIL` that are missing certain fields such as `destinationIP`, `egressIP`, and `egressError`, see the [related section in the Troubleshooting documentation](https://docs.cloud.google.com/dns/docs/troubleshooting#outbound-forwarded-queries-receive-servfail-errors).

## Monitor metrics

Cloud DNS exports monitoring metrics to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

You can monitor the rate of DNS queries and responses that point to private zones, forwarding zones, policy forwarding, internal Google Cloud zones, and the internet. Monitoring is available on the Google Cloud console [Monitoring page](https://console.cloud.google.com/monitoring) and in the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3).

Private DNS exports the `dns.googleapis.com/query/response_count` delta metric that contains the `response_code` label to count the number of queries per response code.

The `response_code` label is of type `string` with the possible values of `NOERROR`, `FORMERR`, `SERVFAIL`, `NXDOMAIN`, `NOTIMP`, and `UNKNOWN`. For definitions of these codes, see the [IANA DNS RCODEs](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-6).

The metric is exported under the `dns_query` resource type by using the applicable fields of the log record format.

## Monitor DNS propagation

When you use the Google Cloud CLI or the REST API to make changes, the changes are initially marked as pending until the operation is completed. You can use the gcloud CLI or the REST API to check on the status of changes or get a history of changes.

An operation is completed (status: `done`) when Cloud DNS has successfully updated the system that controls the servers. There might still be delays before all name servers are updated.

### List changes for a managed zone

To list changes for a managed zone, run the [`dns record-sets changes list`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/record-sets/changes/list) command.

###  gcloud 
    
    
    gcloud dns record-sets changes list --zone=ZONE
    

Replace `ZONE` with the name of the managed zone whose record sets you want to manage.

### Verify DNS propagation

To monitor and verify that the DNS name server has picked up your changes, you can use the `watch` and `dig` commands. The following example demonstrates how to look up your name server and check to see when one of your managed zone's name servers has picked up a change to an `MX` record.

**Note:** The commands `watch` and `dig` are provided by the Linux operating system and are not `gcloud` commands. As such, they don't require the `gcloud` prefix to run. For other operating systems, you might have to install the commands.

To look up your zone's name servers, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to Cloud DNS zones](https://console.cloud.google.com/net-services/dns/zones/)

  2. Click the name of the managed zone you want to check.

  3. On the **Zone details** page, click **Registrar setup** at the top right corner.




###  gcloud 

Run the [`dns managed-zones describe`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/describe) command.
    
    
    gcloud dns managed-zones describe ZONE_NAME
    

Replace `ZONE_NAME` with the name of your Cloud DNS zone.

To check if the records are available yet on your authoritative name server, run the following `dig` command:

###  gcloud 
    
    
    watch dig example.com in MX @ZONE_NAME_SERVER
    

Replace `ZONE_NAME_SERVER` with one of the name servers from the managed zone.

The `watch` command runs the `dig` command every 2 seconds by default. You can use this command to determine when your authoritative name server picks up your change, which should happen within 120 seconds. After your authoritative name server has the change, DNS resolvers can start to pick up the new record. Resolvers that already have the previous record cached wait for the previous TTL value of the record to expire.

To run `dig` against your system's name server, you can remove the `@<address>` from the `dig` command. If you would like to monitor propagation to other name servers, you can change the `address` to point to other name servers.

## What's next

  * To add, delete, and update records, see [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records).
  * To create, update, list, and delete managed zones, see [Managing zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To reference the API, see [Cloud DNS REST API](https://docs.cloud.google.com/dns/docs/reference/v1).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
