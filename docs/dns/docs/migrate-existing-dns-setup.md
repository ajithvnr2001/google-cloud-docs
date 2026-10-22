---
url: https://docs.cloud.google.com/dns/docs/migrate-existing-dns-setup/
title: Migrate an existing Cloud DNS forwarding setup to Outbound Endpoints \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:34.702856+00:00
---

# Migrate an existing Cloud DNS forwarding setup to Outbound Endpoints  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/migrate-existing-dns-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Migrate an existing Cloud DNS forwarding setup to Outbound Endpoints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides a high-level overview of what you need to do to migrate an existing Cloud DNS forwarding setup to use Outbound Endpoints.

## Migrate an existing Cloud DNS forwarding setup

There are four phases to migrating an existing Cloud DNS forwarding setup to use Outbound Endpoints, which are as follows:

  * Preparation
  * Verification
  * Production migration
  * Cleanup



### Preparation

In the preparation phase, before you can start the migration, you create the proxy-only subnets, regular subnets, and Outbound Endpoints. Also make sure your on-premises firewall rules permit inbound DNS traffic from the IP address range of your regional proxy-only subnet.

  1. **Create proxy-only subnets** : If not already present, in each region where you intend to deploy an Outbound Endpoint, create a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets) with a minimum size of `/26` (64 addresses).
  2. **Identify or create a regular subnet** : In each region where you plan to deploy an Outbound Endpoint, identify or create a regular subnet with an available internal IPv4 address in its primary IP range.
  3. **Create Outbound Endpoints** : [Create your Outbound Endpoints](https://docs.cloud.google.com/dns/docs/create-update-outbound-endpoints#create-outbound-endpoint) and associate them with your target VPC network, region, regular subnet (`--subnetwork=REGULAR_SUBNET`), and an available internal IPv4 address (`--endpoint-ip=IP_ADDRESS_STRING`). Cloud DNS automatically creates and manages the static IP reservation resource and binds the endpoint to the regional proxy-only subnet in the VPC network.
  4. **Update on-premises firewalls** : Add firewall rules in your on-premises and external environments to permit inbound DNS traffic (UDP and TCP port 53) originating from the IP address range of your regional proxy-only subnet.

**Note:** Don't remove the existing firewall rule for `35.199.192.0/19` at this time.



### Verification (optional)

Optionally, you can use the verification phase to verify your Outbound Endpoint configuration.

  1. **Create a test forwarding zone** : Create a new, temporary forwarding zone for a test domain (for example, `test.corp.example.com`).
  2. **Configure for the endpoints** : Configure the test zone to use the new Outbound Endpoints.
  3. **Launch a test VM** : In a relevant VPC network, launch a temporary test VM.
  4. **Verify resolution** : From the test VM, use `dig` or `nslookup` to query a host within your test zone (for example, `dig host.test.corp.example.com`). Confirm that you receive a successful DNS response in the test VM and that the server received the query. Also verify that the server received the query from a source IP address in the new proxy-only subnet.



### Production migration

During the production migration phase, you update your forwarding zones and server policies to use your Outbound Endpoints and review query logs to make sure queries are resolving successfully.

  1. **Update forwarding zones and server policies** : For each forwarding zone or server policy you want to migrate, edit the configuration and change the forwarding path from the default `35.199.192.0/19` range to your Outbound Endpoints.
  2. **Monitor resolution and health** : Review your Cloud DNS query logs and monitoring metrics for the migrated zones to confirm that queries are successfully resolving. 
     * Use `dns.googleapis.com/query/response_count` to track query volume and response status codes.
  3. **High-volume migration and pre-warming strategy** : 
     * **Auto scaling latency** : There is approximately a 10-minute autoscaling spin-up latency for underlying Google-managed proxy infrastructure.
     * **Incremental rollout** : Migrate zones incrementally (one zone at a time) if your aggregate query volume exceeds 10,000 queries per second (QPS) per region to avoid dropped queries during autoscaling ramp up.
     * **Support pre-warming** : For large single-zone migrations that immediately exceed 10,000 QPS per region, ramp up traffic gradually (for example, 10%, 25%, 50%, and then 100%) or contact your Google Cloud account team or Support before your planned migration to request infrastructure pre-warming during your scheduled maintenance window. In your request, specify: 
       * Project ID
       * Target region(s)
       * Estimated peak QPS



### Cleanup

After you have verified the production migration is successful, you need to clean up the previous forwarding mechanism.

  1. **Confirm full migration** : Verify all necessary forwarding zones and server policies in your project aren't using the default `35.199.192.0/19` range. 
     * Review your on-premises DNS logs and make sure there is no traffic sourcing from this range for a safe period (for example, 24 hours).
  2. **Remove the previous firewall rule** : After confirming all traffic has been moved to Outbound Endpoints, you can safely remove the on-premises firewall rule that allowed inbound DNS traffic from the default `35.199.192.0/19` range. Make sure no other Google Cloud services are using this rule before removing or adjusting it.



### Rollback

If you need to roll back your migration, do the following:

  1. **Revert forwarding zone or server policies** : Edit the affected zone or server policy and change its forwarding back to the default `35.199.192.0/19` range.
  2. **Restore firewall rules** : Ensure the rule which allows inbound DNS traffic from `35.199.192.0/19` is still active. Don't remove this rule before the cleanup phase of a successful migration.



## What's next

  * For general information about Outbound Endpoints, see [Outbound endpoints overview](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview).
  * For details about creating and updating Outbound Endpoints, see [Create and update Outbound Endpoints](https://docs.cloud.google.com/dns/docs/create-update-outbound-endpoints).
  * For solutions to common issues related to Outbound Endpoints, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting#outbound-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
