---
url: https://docs.cloud.google.com/armor/docs/network-edge-policies/
title: Configure network edge security policies \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:28.534353+00:00
---

# Configure network edge security policies  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/network-edge-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Configure network edge security policies Stay organized with collections  Save and categorize content based on your preferences. 

Network edge security policies let you configure rules to allow or block traffic at the edge of Google's network. You can configure network edge security policies for the following frontend types:

  * Regional external passthrough Network Load Balancers
  * Protocol forwarding
  * VMs with public IP addresses



You can use network edge security policies to filter by source and destination IP address ranges similarly to Cloud Next Generation Firewall but without consuming your resources. In addition, a network edge security policy is the only security policy type with support for byte offset filtering.

**Note:** Network edge security policies aren't supported for VM instances using [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types).

## Configure custom rules for network edge security policies

**Note:** When you add a network edge security service to a network edge security policy, you can't remove the network edge security service using the Google Cloud console. You can only remove the network edge security service by using the Google Cloud CLI or the API.

Like backend and edge security policies, you can configure custom rules for network edge security policies. In the following example, you create a network edge security policy, configure a custom rule to allow traffic from only a given source IP address range, and attach the policy to your backend service.

Network edge security policies support several Google Cloud Armor filters, including unique filters like byte-offset filtering. For more information about what features network edge security policies support, see the [security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types). In addition, you can deploy network edge security policies in [preview mode](https://docs.cloud.google.com/armor/docs/security-policy-overview#preview_mode).

Before you proceed, you must [enroll in Google Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-using#enrolling) and [configure advanced network DDoS protection](https://docs.cloud.google.com/armor/docs/advanced-network-ddos#activate-advanced-ddos-protection). You cannot use custom rules for network edge security policies without an active Cloud Armor Enterprise subscription and advanced network DDoS protection.

To configure custom rules, follow these steps:

  1. Create a new network edge security policy with the name `POLICY_NAME` in the region `REGION`. Don't use the same security policy that you used when you enabled advanced network DDoS protection.
         
         gcloud compute security-policies create POLICY_NAME \
            --type=CLOUD_ARMOR_NETWORK \
            --region=REGION
         

  2. Change your policy's [default rule](https://docs.cloud.google.com/armor/docs/security-policy-overview#default-rule) from `allow` to `deny` to block traffic that is not explicitly allowed by other rules.
         
         gcloud compute security-policies rules update 2147483647 \
            --security-policy=POLICY_NAME \
            --action=deny \
            --region=REGION
         

  3. In the same security policy, add a rule at priority `RULE_PRIORITY` that allows requests in the source IP address range `RANGE`.
         
         gcloud compute security-policies rules create RULE_PRIORITY \
            --security-policy=POLICY_NAME \
            --network-src-ip-ranges=RANGE \
            --action=allow \
            --region=REGION
         

  4. Associate the security policy with your backend service `BACKEND_SERVICE_NAME`.
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
            --security-policy=POLICY_NAME \
            --region=REGION
         

Alternatively, you can associate the security policy with a single VM instance by using the following command:
         
         gcloud beta compute instances network-interfaces update VM_NAME \
            --security-policy=POLICY_NAME \
            --security-policy-region=REGION \
            --network-interface=NETWORK_INTERFACE \
            --zone=ZONE_NAME
         

  5. Optional: You can verify that the security policy is attached by using the following command. If successful, the `securityPolicy` field in the output has a link to your security policy resource.
         
         gcloud compute instances describe VM_NAME --zone=ZONE_NAME
         




After you create the preceding example, you can continue to add rules to your network edge security policy by using the `security-policies rules update` command. The supported fields for network edge security policies are as follows:

Field | Flag | Description  
---|---|---  
**Source IP address** | `--network-src-ip-ranges` | Source IPv4/6 addresses or CIDR prefixes, in standard text format.  
**Source ports** | `--network-src-ports` | Source port numbers for TCP/UDP/SCTP. Each element can be a (16-bit) number (like "80") or range (like "0-1023").  
**Source region codes** | `--network-src-region-codes` | Two-letter country code ([ISO 3166-1 alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)).  
**Source ASNs** | `--network-src-asns` | BGP Autonomous System Number of the source IP address.  
**Destination IP address ranges** | `--network-dest-ip-ranges` | Destination IPv4/6 addresses or CIDR prefixes, in standard text format.  
**Destination ports** | `--network-dest-ports` | Destination port numbers for TCP/UDP/SCTP. Each element can be a (16-bit) number (like "80") or range (like "0-1023").  
**IP address protocols** | `--network-ip-protocols` | IPv4 protocol / IPv6 next header (after extension headers). Each element can be an 8-bit number (like "6"), range (like "253-254"), or one of the following protocol names: 

  * `tcp`
  * `udp`
  * `icmp`
  * `esp`
  * `ah`
  * `ipip`
  * `sctp`

  
**Byte-offset filtering** | N/A | See the following section.  
  
When you use the `--network-src-region-codes` flag with a network edge security policy, you can use region codes for the following territories subject to comprehensive US sanctions:

**Territories** | **Assigned code**  
---|---  
Crimea | XC  
The so-called Donetsk People's Republic (DNR), and  
the so-called Luhansk People's Republic (LNR) | XD  
  
## Configure byte-offset filtering

If you use regional external passthrough Network Load Balancers, protocol forwarding, or VMs with public IP addresses, Cloud Armor can perform deep packet inspection on ingressed traffic. You can configure a security policy rule that matches on a specific TCP/UDP byte offset value. You can configure the rule to apply the rule action when the configured value is present, or alternatively when it is absent.

The following example allows traffic when the value is present, and denies all other traffic:

  1. Create a new network edge security policy. You can skip this step if you have an existing network edge security policy.
         
         gcloud compute security-policies create POLICY_NAME \
            --type=CLOUD_ARMOR_NETWORK \
            --region=REGION_NAME
         

  2. Update your network edge security policy to add user-defined fields by using the following parameters:

     * **Base** : value can be `IPv4`, `IPv6`, `TCP`, or `UDP`
     * **Offset** : offset of the field from the base in bytes
     * **Size** : size of the field in bytes (maximum value is `4`)
     * **Mask** : the mask for the bits in the field to be matched

You can use up to eight user-defined fields per policy. In the following example, you create two user defined fields.
    
    gcloud compute security-policies add-user-defined-field POLICY_NAME \
       --user-defined-field-name=USER_DEFINED_FIELD_NAME_TCP \
       --base=TCP \
       --offset=OFFSET \
       --size=SIZE \
       --mask=MASK \
       --region=REGION_NAME
    
    
    gcloud compute security-policies add-user-defined-field POLICY_NAME \
       --user-defined-field-name=USER_DEFINED_FIELD_NAME_UDP \
       --base=UDP \
       --offset=OFFSET \
       --size=SIZE \
       --mask=MASK \
       --region=REGION_NAME
    

  3. In your network edge security policy, add a rule with the same custom field name that you used in the previous example. Replace `VALUE1` and `VALUE2` with values that match traffic that you want to allow.
         
         gcloud compute security-policies rules create RULE_PRIORITY \
            --security-policy=POLICY_NAME \
            --network-user-defined-fields="USER_DEFINED_FIELD_NAME_TCP;VALUE1:VALUE2,USER_DEFINED_FIELD_NAME_UDP;VALUE1:VALUE2,USER_DEFINED_FIELD_NAME_UDP;VALUE1,VALUE2" \
            --action=allow \
            --region=REGION_NAME
         

  4. Set the default rule in your network edge security policy to be a deny rule. You can skip this step if the default rule in your security policy is already a deny rule.
         
         gcloud compute security-policies rules update 2147483647 \
            --security-policy=POLICY_NAME \
            --action=deny \
            --region=REGION_NAME
         

  5. Associate your network edge security policy with your regional external passthrough Network Load Balancer's backend service.
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
            --security-policy=POLICY_NAME \
            --region=REGION_NAME
         




## Monitoring

Cloud Armor exports the following metrics to Cloud Monitoring for each of your network edge security policy rules:

  * `packet_count`
    * `Blocked`: a boolean value representing the result of an `allow` or `deny`  
rule action
    * `Count`: the value of `packet_count` incremented once for each 10,000 packets—for example, a `packet_count` value of `5` means that at least 50,000 packets have matched your rule
  * `preview_packet_count`: the same as `packet_count`, used for rules in preview mode



To view metrics for network edge security policies, you must first enable the [Network Security API](https://docs.cloud.google.com/service-mesh/docs/reference/network-security/rest) (`networksecurity.googleapis.com`). This permission is included in the [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`). After you enable the Network Security API, you can view the metrics in Monitoring in the Google Cloud console.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
