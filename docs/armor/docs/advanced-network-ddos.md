---
url: https://docs.cloud.google.com/armor/docs/advanced-network-ddos/
title: Configure advanced network DDoS protection \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:58.682662+00:00
---

# Configure advanced network DDoS protection  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/advanced-network-ddos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Configure advanced network DDoS protection Stay organized with collections  Save and categorize content based on your preferences. 

A distributed denial-of-service (DDoS) attack is a deliberate attempt by a hostile actor to disrupt operations of publicly exposed sites, systems, and APIs, with the goal of degrading the experience of legitimate users. For workloads using [regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network), [protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding), or VMs with public IP addresses, Google Cloud Armor offers the following options to help protect systems against DDoS attacks:

  * **Standard network DDoS protection:** basic always-on protection for regional external passthrough Network Load Balancer, protocol forwarding, or VMs with public IP addresses. This protection helps to ensure infrastructure stability by continuously monitoring and throttling traffic that exceeds quota. Standard network DDoS protection does not look for attack signatures or provide other advanced mitigations to minimize collateral damage. For targeted protection, you must enable your own security policy with Advanced DDoS protection. The cost of Standard network DDoS protection is covered under Cloud Armor Standard and does not require any additional subscriptions.
  * **Advanced network DDoS protection:** additional protections for Google Cloud Armor Enterprise subscribers who use regional external passthrough Network Load Balancer, protocol forwarding, or VMs with public IP addresses. For more information about Cloud Armor Enterprise, see the [Cloud Armor Enterprise overview](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview).



This document explains the difference between standard and advanced network DDoS protection, how advanced network DDoS protection works, and how to enable advanced network DDoS protection.

## Compare standard and advanced network DDoS protection

Use the following table to compare standard and advanced network DDoS protection features.

Feature | Standard network DDoS protection | Advanced network DDoS protection  
---|---|---  
Protected endpoint type | 

  * Regional external passthrough Network Load Balancer
  * Protocol forwarding 
  * VMs with public IP addresses

| 

  * Regional external passthrough Network Load Balancer
  * Protocol forwarding
  * VMs with public IP addresses

  
Forwarding rule enforcement |  |   
Always-on attack monitoring and alerting |  |   
Targeted attack mitigations |  |   
Mitigation telemetry |  |   
**Important:** Advanced network DDoS protection isn't supported for VM instances using [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types).

## How network DDoS protection works

Standard network DDoS protection is always enabled. You don't need to take any action to enable it. Standard protection ensures that Google Cloud infrastructure remains stable by continuously monitoring and throttling traffic that exceeds quota. It does not look for attack signatures or provide other advanced mitigations to minimize collateral damage. For targeted protection, you must enable your own security policy with Advanced DDoS protection.

You configure advanced network DDoS protection on a per-region basis. Instead of associating the network edge security policy with one or more target pools, target instances, backend services, or instances with external IP addresses, you associate it with a network edge security service in a particular region. When you enable it for that region, Cloud Armor provides always-on targeted volumetric attack detection and mitigation for regional external passthrough Network Load Balancer, protocol forwarding, and VMs with public IP addresses in that region. You can only apply advanced network DDoS protection to projects that are enrolled in Cloud Armor Enterprise.

When you configure advanced network DDoS protection, you first create a security policy of the type `CLOUD_ARMOR_NETWORK` in a region that you choose. Next, you update the security policy to enable advanced network DDoS protection. Finally, you create a network edge security service, a resource to which you can attach security policies of type `CLOUD_ARMOR_NETWORK`. Attaching the security policy to the network edge security service enables advanced network DDoS protection for all applicable endpoints in the region that you chose.

Advanced network DDoS protection measures your baseline traffic to improve its mitigation performance. When you enable advanced network DDoS protection, there is a training period of 24 hours before advanced network DDoS protection develops a reliable baseline and can use its training to enhance its mitigations. When the training period is over, advanced network DDoS protection applies additional mitigation techniques based on historical traffic.

## Activate advanced network DDoS protection

Use the following steps to activate advanced network DDoS protection.

### Enroll in Cloud Armor Enterprise

Your project must be enrolled in Cloud Armor Enterprise to enable advanced network DDoS protection on a per-region basis. After they are activated, all regional endpoints in the activated region receive always-on advanced network DDoS protection.

Ensure that there is an active Cloud Armor Enterprise subscription in your billing account, and that the current project is enrolled in Cloud Armor Enterprise. For more information about enrolling in Cloud Armor Enterprise, see [Subscribing to Cloud Armor Enterprise and enrolling projects](https://docs.cloud.google.com/armor/docs/armor-enterprise-using#enrolling).

### Configure Identity and Access Management (IAM) permissions

To configure, update, or delete a Cloud Armor edge security service, you need the following IAM permissions:

  * `compute.networkEdgeSecurityServices.create`
  * `compute.networkEdgeSecurityServices.update`
  * `compute.networkEdgeSecurityServices.get`
  * `compute.networkEdgeSecurityServices.delete`



The following table lists the IAM roles' base permissions and their associated API methods.

IAM permission | API methods  
---|---  
`compute.networkEdgeSecurityServices.create` | `networkEdgeSecurityServices insert`  
`compute.networkEdgeSecurityServices.update` | `networkEdgeSecurityServices patch`  
`compute.networkEdgeSecurityServices.get` | `networkEdgeSecurityServices get`  
`compute.networkEdgeSecurityServices.delete` | `networkEdgeSecurityServices delete`  
`compute.networkEdgeSecurityServices.list` | `networkEdgeSecurityServices aggregatedList`  
  
For more information about the IAM permissions that you need when you use Cloud Armor, see [Set up IAM permissions for Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies#iam-perms).

### Configure advanced network DDoS protection

**Caution:** After you create the security policy described in this section, you can't add custom rules to the policy. To add custom rules, you must [create a new network edge security policy](https://docs.cloud.google.com/armor/docs/network-edge-policies#configure_custom_rules_for_network_edge_security_policies).

Use the following steps to enable advanced network DDoS protection.

  1. Create a security policy of type `CLOUD_ARMOR_NETWORK`, or use an existing security policy with type `CLOUD_ARMOR_NETWORK`.
         
         gcloud compute security-policies create SECURITY_POLICY_NAME \
              --type CLOUD_ARMOR_NETWORK \
              --region REGION
         

Replace the following:

     * `SECURITY_POLICY_NAME`: the name that you want your security policy to have
     * `REGION`: the region in which you want your security policy to be provisioned
  2. Update the newly created or existing security policy by setting the `--network-ddos-protection` flag to `ADVANCED`.
         
         gcloud compute security-policies update SECURITY_POLICY_NAME \
              --network-ddos-protection ADVANCED \
              --region REGION
         

Alternatively, you can set the `--network-ddos-protection` flag to `ADVANCED_PREVIEW` to enable the security policy in preview mode.
         
         gcloud beta compute security-policies update SECURITY_POLICY_NAME \
              --network-ddos-protection ADVANCED_PREVIEW \
              --region REGION
         

  3. Create a network edge security service that references your security policy.
         
         gcloud compute network-edge-security-services create SERVICE_NAME \
              --security-policy SECURITY_POLICY_NAME \
              --region REGION
         




## Disable advanced network DDoS protection

To disable advanced network DDoS protection, you can either update or delete the security policy.

### Update the security policy

Use the following command to update your security policy to set the `--network-ddos-protection` flag to `STANDARD`. Replace variables with information that is relevant to your deployment.
    
    
    gcloud compute security-policies update SECURITY_POLICY_NAME \
        --network-ddos-protection STANDARD \
        --region REGION
    

### Delete the security policy

Before you can delete a network edge security policy, you must first remove it from the network edge security service because you cannot delete in-use security policies. Use the following steps to delete your security policy:

  1. Remove your policy from the network edge security service or delete the network edge security service.

     * To remove your policy from the network edge security service, use the following command:
           
           gcloud compute network-edge-security-services update SERVICE_NAME \
                --security-policy="" \
                --region=REGION_NAME
           

     * To delete the network edge security service, use the following command:
           
           gcloud compute network-edge-security-services delete SERVICE_NAME \
                --region=REGION_NAME
           

  2. Delete the security policy using the following command:
         
         gcloud compute security-policies delete SECURITY_POLICY_NAME
         




## Use preview mode

Preview mode lets you monitor the effects of advanced network DDoS protection without enforcing the mitigation.

Cloud Armor Enterprise subscribers can also enable preview mode for advanced network DDoS protection policies. In preview mode, you receive all of the logging and telemetry about the detected attack and the proposed mitigation. However, the proposed mitigation is not enforced. This lets you test the effectiveness of the mitigation before enabling it. Because each policy is configured per region, you can enable or disable preview mode per region.

To enable preview mode, you set the `--ddos-protection` flag to `ADVANCED_PREVIEW`. You can use the following example to update an existing policy.
    
    
    gcloud beta compute security-policies update POLICY_NAME \
        --network-ddos-protection ADVANCED_PREVIEW \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of your policy
  * `REGION`: the region in which your policy is located.



If your security policy is in preview mode during an active attack and you want to enforce the mitigations, you can update your security policy to set the `--network-ddos-protection` flag to `ADVANCED`. The policy is enforced almost immediately, and the next `MITIGATION_ONGOING` logging event reflects the change. `MITIGATION_ONGOING` logging events occur every five minutes.

## Network DDoS mitigation telemetry

Cloud Armor generates three types of event logs when mitigating DDoS attacks: `MITIGATION_STARTED`, `MITIGATION_ONGOING`, and `MITIGATION_ENDED`. You can use the following log filters to view your logs by mitigation type:

Mitigation type | Log filter  
---|---  
Mitigation start | resource.type="network_security_policy"jsonPayload.mitigationType="MITIGATION_STARTED"  
Mitigation ongoing | resource.type="network_security_policy"jsonPayload.mitigationType="MITIGATION_ONGOING"  
Mitigation end | resource.type="network_security_policy"jsonPayload.mitigationType="MITIGATION_ENDED"  
  
### Cloud Logging attack mitigation event logs

The following sections provide examples of the log format for each type of event log:

#### Mitigation started
    
    
      @type: "type.googleapis.com/google.cloud.networksecurity.cloudarmor.logging.v1.CloudArmorMitigationAlert"
      alertId: "11275630857957031521"
      mitigation_type: "MITIGATION_STARTED"
      target_vip: "XXX.XXX.XXX.XXX"
      total_volume: {
       pps: 1400000
       bps: 140000000
      }
      started: {
       total_attack_volume: {
        pps: 1100000
        bps: 110000000
       }
       classified_attack: {
        attack_type: "NTP-udp"
        attack_volume: {
           pps: 500000
           bps: 50000000
        }
       }
       classified_attack: {
        attack_type: "CHARGEN-udp"
        attack_volume: {
           pps: 600000
           bps: 60000000
        }
       }
       attack_sources: {
        top_source_asns: {
          asn: "ABCDEF"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_asns: {
          asn: "UVWXYZ"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_geos: {
          region_code: "XX"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_geos: {
          region_code: "XY"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_ips: {
          region_code: "xx.xx.xx.xx"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_ips: {
          region_code: "yy.yy.yy.yy"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
       }
      }
      

#### Mitigation ongoing
    
    
      @type: "type.googleapis.com/google.cloud.networksecurity.cloudarmor.logging.v1.CloudArmorMitigationAlert"
      alertId: "11275630857957031521"
      mitigation_type: "MITIGATION_ONGOING"
      target_vip: "XXX.XXX.XXX.XXX"
      total_volume: {
       pps: 1500000
       bps: 150000000
      }
      ongoing: {
       total_attack_volume: {
        pps: 1100000
        bps: 110000000
       }
       classified_attack: {
        attack_type: "NTP-udp"
        attack_volume: {
           pps: 500000
           bps: 50000000
        }
       }
       classified_attack: {
        attack_type: "CHARGEN-udp"
        attack_volume: {
           pps: 600000
           bps: 60000000
        }
       }
       attack_sources: {
        top_source_asns: {
          asn: "ABCDEF"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_asns: {
          asn: "UVWXYZ"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_geos: {
          region_code: "XX"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_geos: {
          region_code: "XY"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_ips: {
          region_code: "xx.xx.xx.xx"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
        top_source_ips: {
          region_code: "yy.yy.yy.yy"
          volume: {
            pps: 20000
            bps: 2000000
          }
        }
       }
      }
      

#### Mitigation completed
    
    
      @type: "type.googleapis.com/google.cloud.networksecurity.cloudarmor.logging.v1.CloudArmorMitigationAlert"
      alertId: "11275630857957031521"
      mitigation_type: "MITIGATION_ENDED"
      target_vip: "XXX.XXX.XXX.XXX"
      ended: {
          attack_duration_seconds: 600
          attack_type: "NTP-udp"
      }
      

In preview mode, each of the preceding `mitigation_type`s are preceded by `PREVIEWED_`. For example, in preview mode, `MITIGATION_STARTED` is instead `PREVIEWED_MITIGATION_STARTED`.

To view these logs, go to the Logs Explorer and view the `network_security_policy` resource.

[Go to Logs Explorer](https://console.cloud.google.com/logs/viewer)

For more information about viewing logs, see [Viewing logs](https://docs.cloud.google.com/armor/docs/request-logging#view-logs).

### Security Command Center findings

The Security Command Center dashboard helps you monitor and respond to volumetric DDoS attacks targeting your passthrough Network Load Balancer and virtual machines. When Cloud Armor detects an attack, a dedicated finding labeled "Volumetric DDoS Attack Attempt - Network LB/VMs" appears on the dashboard and the Cloud Armor card.

The finding includes direct links to relevant logs, and provides the following information to help you understand the attack:

  * The specific resource under attack
  * The volume of traffic affecting the resource
  * The classification of the attack (like UDP, TCP, or SYN flood)



The finding dynamically reflects the attack status. Attack status is based on the following log events:

  * Mitigation started: the finding appears when mitigation measures begin
  * Mitigation ongoing: as the mitigation progresses, the finding updates automatically, keeping you informed of the ongoing situation. The following screenshot shows an example active finding:

[ ![An active Security Command Center finding.](https://docs.cloud.google.com/static/armor/images/scc-active.png)](https://docs.cloud.google.com/static/armor/images/scc-active.png) An active Security Command Center finding (click to enlarge).
  * Mitigation ended: when the attack subsides and mitigation ends, the finding becomes inactive, providing a record of the event. The following screenshot shows an example inactive finding:

[ ![An inactive Security Command Center finding.](https://docs.cloud.google.com/static/armor/images/scc-inactive.png)](https://docs.cloud.google.com/static/armor/images/scc-inactive.png) An inactive Security Command Center finding (click to enlarge).



## What's next

  * Learn to [Configure network edge security policies](https://docs.cloud.google.com/armor/docs/network-edge-policies)
  * Learn about [Cloud Armor Enterprise](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
