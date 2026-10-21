---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/managed-traffic-classification/
title: Configure managed traffic classification \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:38:45.937928+00:00
---

# Configure managed traffic classification  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/managed-traffic-classification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)



Send feedback 

#  Configure managed traffic classification Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how you can configure managed traffic classification to automate the assignment of differentiated services field codepoint (DSCP) bits in your outgoing packets.

To configure managed traffic classification, you create a network policy resource which acts as a container for traffic classification rules. These rules tell Cloud Interconnect how to mark your outgoing packets. The following sections explain how network policies and traffic classification rules work together.

## Network policies

A network policy is a container which can hold a collection of traffic classification rules. When you create a new network policy, you specify a region in which you want to apply the policy. Then, after you add rules to the policy, you associate it with one or more of your VPC networks. Cloud Interconnect then applies your rules to all virtual machine instances within each associated network in the specified region. Alternatively, you can use secure tags to apply rules to only a subset of instances in each network.

You can only associate one network policy with each VPC network per region. This means that you can associate multiple network policies in different regions with one VPC network, or you can have multiple network policies in the same region that are associated with different VPC networks.

## Traffic classification rules

Traffic classification rules have three components:

  * Priority: a number which determines the order in which the rules in a network policy are evaluated
  * Match condition: a value that determines which packets a rule applies to
  * Rule action: an action that performed on packets that match the match condition. Traffic classification rules can only have the `APPLY_TRAFFIC_CLASSIFICATION` action.



The following sections describe each of the rule components in detail.

### Rule evaluation order

The order in which your rules are evaluated against a packet is determined by rule priority, from the lowest number to the highest number. The rule with the lowest numeric value assigned has the highest logical priority, and is evaluated prior to rules with lower logical priorities. This means that a rule with the minimum numeric priority, 0, is always evaluated first.

You cannot configure two or more rules with the same priority. The priority for each rule must be set to a number from 0 to 2147483646 inclusive. The priority value 2147483647, also known as `INT-MAX`, is reserved for the default rule in the network policy. You can't delete the default rule, but you can modify it.

Priority numbers can have gaps. These gaps let you add or remove rules in the future without affecting the rest of the rules. For example, 1, 2, 3, 4, 5, 9, 12, 16 is a valid series of priority numbers to which you can add rules numbered from 6 to 8, 10 to 11, and 13 to 15 in the future. Adding rule with the priority values 7, 10, and 14 changes the order of execution even though you don't modify any of the original rules.

### Match conditions

The match condition is an expression that describes the criteria that a packet must match in order for the rule's action to be applied. You can use the following categories of match conditions with traffic classification rules, based on what attribute you want to look for:

  * **IP address ranges** : match against a packet's source or destination IP address range. Each rule can contain a maximum of 5000 Classless Inter-Domain Routing (CIDR) IP address ranges, all of which must be either IPv4 or all of which must be IPv6. If you need to match on both IPv4 and IPv6 address ranges, you must create more than one rule.
  * **Ports and protocols** : match against a packet's destination port or ports, Internet Protocol (IP) number, or one of the following protocol strings:

    * `tcp`
    * `udp`
    * `icmp`
    * `esp`
    * `ah`
    * `ipip`
    * `sctp`

You can only match upon destination ports when using the UDP, TCP, or SCTP protocols.

  * **Target tags** : match against incoming packets whose target has a specified secure tag. For more information about secure tags, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).




You can combine some or all of these match conditions to achieve more granular matching.

### Rule actions

The rule action is the action that's taken when a packet matches a rule's match condition. Only one action is applied on each packet, and when an action has been applied more rules are not evaluated. Traffic classification rules can only have the `APPLY_TRAFFIC_CLASSIFICATION` action.

The `APPLY_TRAFFIC_CLASSIFICATION` action applies the specified traffic class to the IP packet. You choose whether the DSCP value is assigned automatically based on the traffic class, or if it is assigned a custom value. The automatic assignments based on traffic class are as follows:

Traffic class | DSCP value  
---|---  
TC1 | 7 (000111)  
TC2 | 15 (001111)  
TC3 | 23 (010111)  
TC4 | 31 (011111)  
TC5 | 47 (101111)  
TC6 | 63 (111111)  
  
Custom DSCP values can have a value of 0-63 inclusive.

## Configure a network policy

The following procedure describes how to create a network policy and assign it to a region:

###  Console 

  1. In the Google Cloud console, go to the **Traffic Classification** tab.

[Go to Traffic Classification](https://console.cloud.google.com/net-services/traffic-classification/)

  2. Click **Create policy**.

  3. In the **Name** field, enter a name for the network policy.

  4. In the **Region** list box, select the region in which you want to apply your network policy.

  5. Click **Create**.




###  gcloud 
    
    
    gcloud compute network-policies create NETWORK_POLICY_NAME \
      --region REGION
    

Replace the following:

  * `NETWORK_POLICY_NAME`: the name that you want to give to your network policy
  * `REGION`: the region in which you want to apply your network policy



## Configure traffic classification rules

The following sections describe how to create traffic classification rules and attach them to an existing network policy.

### Match packets using destination IP address ranges

Use the following procedure to create a rule that matches on packets based on their destination IP address range:

###  Console 

  1. In the Google Cloud console, go to the **Traffic Classification** tab.

[Go to Traffic Classification](https://console.cloud.google.com/net-services/traffic-classification/)

  2. Click the name of the network policy to which you want to add a rule.

  3. Click **Create rule**.

  4. In the **Name** field, enter a name for the rule.

  5. In the **Priority** field, enter the numeric priority to be used in the rule evaluation order.

  6. In the **Class** list box, choose a traffic class to which you want to assign this packet.

  7. In the **DSCP value** field, choose **Automatic** or **Specified**. If you choose **Specified** , enter a DSCP value.

  8. In the **Destination Filters** field, specify the IP address protocol and range:

     * In the **IP type** list box choose an IP address protocol
     * In the **IP ranges** field, enter at least one destination IP address range.
  9. Click **Create**.




###  gcloud 

To create a traffic classification rule that automatically assigns DSCP, use the following command:
    
    
    gcloud compute network-policies traffic-classification-rules create PRIORITY \
      --action APPLY_TRAFFIC_CLASSIFICATION \
      --traffic-class TRAFFIC_CLASS \
      --dscp-mode AUTO \
      --network-policy NETWORK_POLICY_NAME \
      --dest-ip-ranges DESTINATION_RANGES
    

Replace the following:

  * `PRIORITY`: the numeric priority to be used in the rule evaluation order
  * `TRAFFIC_CLASS`: the traffic class to which you want to assign this packet
  * `NETWORK_POLICY_NAME`: the name of the network policy to which you want to add this rule
  * `DESTINATION_RANGES`: a comma-delimited list of destination IP address ranges on which you want to match



To create a traffic classification rule that assigns a custom DSCP value, use the following command:
    
    
    gcloud compute network-policies traffic-classification-rules create PRIORITY \
      --action APPLY_TRAFFIC_CLASSIFICATION \
      --traffic-class TRAFFIC_CLASS \
      --dscp-mode CUSTOM \
      --dscp-value DSCP_VALUE \
      --network-policy NETWORK_POLICY_NAME \
      --dest-ip-ranges DESTINATION_RANGES
    

Replace the following:

  * `PRIORITY`: the numeric priority to be used in the rule evaluation order
  * `TRAFFIC_CLASS`: the traffic class to which you want to assign the matching packet
  * `DSCP_VALUE`: the custom DSCP value that you want to give the matching packet
  * `NETWORK_POLICY_NAME`: the name of the network policy to which you want to add this rule
  * `DESTINATION_RANGES`: a comma-delimited list of destination IP address ranges on which you want to match



### Match packets using port or protocol

Use the following procedure to create a rule that matches on packets based on their ports or protocols:

###  Console 

  1. In the Google Cloud console, go to the **Traffic Classification** tab.

[Go to Traffic Classification](https://console.cloud.google.com/net-services/traffic-classification/)

  2. Click the name of the network policy to which you want to add a rule.

  3. Click **Create rule**.

  4. In the **Name** field, enter a name for the rule.

  5. In the **Priority** field, enter the numeric priority to be used in the rule evaluation order.

  6. In the **Class** list box, choose a traffic class to which you want to assign this packet.

  7. In the **DSCP value** field, choose **Automatic** or **Specified**. If you choose **Specified** , enter a DSCP value.

  8. In the **Destination Filters** field, specify the IP address protocol and range:

     * In the **IP type** list box choose an IP address protocol
     * In the **IP ranges** field, enter at least one destination IP address range.
  9. In the **Protocols and ports** field, select **Specified protocols and ports**.

  10. For each listed protocol that you want to match on, select its checkbox and enter ports into its **Ports** field.

  11. Optional: To match on protocols that aren't listed, select the **Other protocols** checkbox, then enter a comma-delimited list of protocols.

  12. Click **Create**.




###  gcloud 

To create a traffic classification rule that automatically assigns DSCP, use the following command:
    
    
    gcloud compute network-policies traffic-classification-rules create PRIORITY \
      --action APPLY_TRAFFIC_CLASSIFICATION \
      --traffic-class TRAFFIC_CLASS \
      --dscp-mode AUTO \
      --network-policy NETWORK_POLICY_NAME \
      --layer4-configs PROTOCOLS
    

Replace the following:

  * `PRIORITY`: the numeric priority to be used in the rule evaluation order
  * `TRAFFIC_CLASS`: the traffic class to which you want to assign this packet
  * `NETWORK_POLICY_NAME`: the name of the network policy to which you want to add this rule
  * `PROTOCOLS`: a comma-delimited list of protocols on which you want to match. To specify a port or port range with each protocol, use the following format: 
    * One port: `protocol:port`. For example, `tcp:80`
    * Port range: `protocol:port1-port2`. For example, `tcp:20000-25000`



To create a traffic classification rule that assigns a custom DSCP value, use the following command:
    
    
    gcloud compute network-policies traffic-classification-rules create PRIORITY \
      --action APPLY_TRAFFIC_CLASSIFICATION \
      --traffic-class TRAFFIC_CLASS \
      --dscp-mode CUSTOM \
      --dscp-value DSCP_VALUE \
      --network-policy NETWORK_POLICY_NAME \
      --layer4-configs PROTOCOLS
    

Replace the following:

  * `PRIORITY`: the numeric priority to be used in the rule evaluation order
  * `TRAFFIC_CLASS`: the traffic class to which you want to assign the matching packet
  * `DSCP_VALUE`: the custom DSCP value that you want to give the matching packet
  * `NETWORK_POLICY_NAME`: the name of the network policy to which you want to add this rule
  * `PROTOCOLS`: a comma-delimited list of protocols on which you want to match. To specify a port or port range with each protocol, use the following format: 
    * One port: `protocol:port`. For example, `tcp:80`
    * Port range: `protocol:port1-port2`. For example, `tcp:20000-25000`



### Match packets using tags

Use the following procedure to create a rule that matches on packets based on target secure tags. To configure secure tags, see [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

###  Console 

  1. In the Google Cloud console, go to the **Traffic Classification** tab.

[Go to Traffic Classification](https://console.cloud.google.com/net-services/traffic-classification/)

  2. Click the name of the network policy to which you want to add a rule.

  3. Click **Create rule**.

  4. In the **Name** field, enter a name for the rule.

  5. In the **Priority** field, enter the numeric priority to be used in the rule evaluation order.

  6. In the **Class** list box, choose a traffic class to which you want to assign this packet.

  7. In the **DSCP value** field, choose **Automatic** or **Specified**. If you choose **Specified** , enter a DSCP value.

  8. In the **Target** field, select **Secure tags**.

  9. Click **Select scope for tags**. In the new window, choose a scope, which can be a project, folder, or organization. Specify your secure tags:

     1. In the **Key 1** field, select a key from the listbox.
     2. In the **Value 1** field, select a value from the listbox.
     3. Optional: To add more secure tags, click **Add tag** and then repeat the previous two steps.
  10. In the **Destination Filters** field, specify the IP address protocol and range:

     * In the **IP type** list box choose an IP address protocol
     * In the **IP ranges** field, enter at least one destination IP address range.
  11. Click **Create**.




###  gcloud 

To create a traffic classification rule that automatically assigns DSCP, use the following command:
    
    
    gcloud compute network-policies traffic-classification-rules create PRIORITY \
      --action APPLY_TRAFFIC_CLASSIFICATION \
      --traffic-class TRAFFIC_CLASS \
      --dscp-mode AUTO \
      --network-policy NETWORK_POLICY_NAME \
      --target-secure-tags TAG_KEY/TAG_VALUE
    

Replace the following:

  * `PRIORITY`: the numeric priority to be used in the rule evaluation order
  * `TRAFFIC_CLASS`: the traffic class to which you want to assign this packet
  * `NETWORK_POLICY_NAME`: the name of the network policy to which you want to add this rule
  * `TAG_KEY`: the secure tag key
  * `TAG_VALUE`: the value to assign to the secure tag key



To create a traffic classification rule that assigns a custom DSCP value, use the following command:
    
    
    gcloud compute network-policies traffic-classification-rules create PRIORITY \
      --action APPLY_TRAFFIC_CLASSIFICATION \
      --traffic-class TRAFFIC_CLASS \
      --dscp-mode CUSTOM \
      --dscp-value DSCP_VALUE \
      --network-policy NETWORK_POLICY_NAME \
      --target-secure-tags TAG_KEY/TAG_VALUE
    

Replace the following:

  * `PRIORITY`: the numeric priority to be used in the rule evaluation order
  * `TRAFFIC_CLASS`: the traffic class to which you want to assign the matching packet
  * `DSCP_VALUE`: the custom DSCP value that you want to give the matching packet
  * `NETWORK_POLICY_NAME`: the name of the network policy to which you want to add this rule
  * `TAG_KEY`: the secure tag key
  * `TAG_VALUE`: the value to assign to the secure tag key



## Associate a network policy with networks

After you have attached your traffic classification rules to a network policy, use the following procedure to associate the network policy with one or more networks.

###  Console 

  1. In the Google Cloud console, go to the **Traffic Classification** tab.

[Go to Traffic Classification](https://console.cloud.google.com/net-services/traffic-classification/)

  2. Click the name of the network policy that you want to associate with a network.

  3. Select the **Associations** tab.

  4. Click **Add association**.

  5. Select the checkbox for each network that you want to associate the network policy with.

  6. Click **Associate**.




###  gcloud 

Use the following command to associate the network policy with each network.
    
    
    gcloud compute network-policies associations create \
      --network-policy NETWORK_POLICY_NAME \
      --network NETWORK_NAME
    

Replace the following:

  * `NETWORK_POLICY_NAME`: the name of the network policy that you want to associate
  * `NETWORK_NAME`: the name of the network with which you want to associate the network policy



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
