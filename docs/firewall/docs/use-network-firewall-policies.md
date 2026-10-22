---
url: https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies/
title: Create global network firewall policies and rules \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:23.738875+00:00
---

# Create global network firewall policies and rules  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create global network firewall policies and rules Stay organized with collections  Save and categorize content based on your preferences. 

To control network traffic and enhance security across your global network, use global network firewall policies and rules. Global network firewall policies centralize the management of ingress and egress traffic across multiple Virtual Private Cloud (VPC) networks. You define a policy once and attach it to one or more networks or subnets, ensuring consistent security posture and simplified administration.

This page describes how to configure global network firewall policies by defining rules that specify actions for various traffic types. You learn how to allow or deny connections based on source, destination, protocol, and port. Before you read this page, ensure you are familiar with the concepts described in the [Global network firewall policies overview](https://docs.cloud.google.com/firewall/docs/network-firewall-policies).

## Create a global network firewall policy

When you create a global network firewall policy using the Google Cloud console, you can associate the policy with a VPC network during creation. If you create the policy using the Google Cloud CLI, you must associate the policy with a network after you create the policy.

The VPC network with which the global network firewall policy is associated must be in the same project as the global network firewall policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.create`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the project where you want to create the policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your project within your organization.

  3. Click **Create firewall policy**.

  4. In the **Policy name** field, enter a name for the policy.

  5. For **Policy type** , select **VPC policy**.

**Note:** The RDMA RoCE is only supported for regional network firewall policy. When you select the RoCE policy type, the deployment scope is automatically set to regional and can't be modified.
  6. For **Deployment scope** , select **Global.**

  7. To create rules for your policy, click **Continue**.

  8. In the **Add rules** section, click **Create firewall rule**. For more information about creating firewall rules, see the following:

     * Create an ingress rule for VM targets
     * Create an egress rule for VM targets
  9. To create packet mirroring rules for your policy, click **Continue**.

  10. In the **Add mirroring rules** section, click **Create mirroring rule**.

For more information, see [Create a firewall policy with a mirroring rule](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/create-manage-mirroring-rules#create-mirroring-rule).

  11. If you want to associate the policy with a network, click **Continue**.

  12. In the **Associate policy with networks** section, click **Associate**.

For more information, see Associate a policy with a network.

  13. Click **Create**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies create NETWORK_FIREWALL_POLICY_NAME \
        --description DESCRIPTION \
        --policy-type POLICY_TYPE \
        --global
    

Replace the following:

  * `NETWORK_FIREWALL_POLICY_NAME`: a name for the policy
  * `DESCRIPTION`: a description for the policy
  * `POLICY_TYPE`: type of network firewall policy. For more information, see [Specifications](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies#specifications).



## Associate a policy with a network

When you associate a firewall policy with a VPC network, all rules in the firewall policy, except the disabled rules, apply to the VPC network.

**Note:** You can only associate a network firewall policy with a network, not with individual VM instances.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.use`
  * `compute.networks.setFirewallPolicy`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the firewall policy or project containing the firewall policy _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains your policy.

  3. Click your policy.

  4. Click the **Associations** tab.

  5. Click **Add association**.

  6. Select the networks within the project.

  7. Click **Associate**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies associations create \
        --firewall-policy POLICY_NAME \
        --network NETWORK_NAME \
        [ --name ASSOCIATION_NAME ] \
        --global-firewall-policy
    

Replace the following:

  * `POLICY_NAME`: either the short name or the system-generated name of the policy.
  * `NETWORK_NAME`: the name of your network.
  * `ASSOCIATION_NAME`: an optional name for the association; if unspecified, the name is set to `network-NETWORK_NAME`.



## Add firewall policy rule

This section describes how to add rules in a global network firewall policy.

### Create an ingress rule for VM targets

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



This section describes how to create an [ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#ingress_rules) that applies to network interfaces of Compute Engine instances.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select a project that contains a global network firewall policy. 

  3. In the **Network firewall policies** section, click the name of a global network firewall policy in which you want to create a rule. 

  4. In the **Firewall rules** section, click **Create firewall rule** and specify the following configuration parameters:

     1. **Priority** : the numeric evaluation order of the rule.

The rules are evaluated from highest to lowest priority where `0` is the highest priority. Priorities must be unique for each rule. We recommend that you separate rule priority values by more than just a difference of one (for example, `100`, `200`, `300`) so that you can create new rules between the existing rules later.

     2. **Description** : provide an optional description.

     3. **Target type** : select **Instances**.

When you select this option, Cloud NGFW uses VM instances as the target. 

     4. **Target** : select one of the following:

        * **Apply to all** : Cloud NGFW uses the [broadest instance targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-vm-broadest).
        * **Service accounts** : narrows the broadest instance targets to the network interfaces of VM instances that use the service account you specify: 
          * In the **Service account scope** section, select **In this project > Target service account**. This is to specify a service account in the same project as the global network firewall policy.
          * In the **Service account scope** section, select **In another project > Target service account**. This is to specify a service account in a Shared VPC service project.
        * **Secure tags** : narrows the broadest instance targets to the network interfaces of VM instances that are bound to at least one of the [secure tag](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) values that you specify. Click **Select scope for tags** and select the organization or project that contains the tag values to match. To add more tag values, click **Add tag**.
     5. **Direction of traffic** : select **Ingress**. 

     6. **Action on match** : select one of the following:

        * **Allow** : to permit connections that match the rule parameters.
        * **Deny** : to block connections that match the rule parameters.
        * **Go to next** : to continue the [firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation).
        * **Apply security profile group** : sends the packets to a [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) or [intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview) based on the **Purpose** you select. 
          * To send packets to a Cloud NGFW firewall endpoint, select **Cloud NGFW Enterprise** , then select a **Security profile group**. To enable TLS inspection of the packets, select **Enable TLS inspection**.
          * To send packets to a Network Security Integration intercept endpoint group for in-band integration, select **NSI In-Band** , then select a **Security profile group**.
     7. **Logs** : select **On** to enable firewall rules logging or **Off** to disable firewall rules logging for this rule. 

     8. **Source network context** : specify a [network context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts):

        * To skip filtering inbound traffic by network context, select **All network contexts**.
        * To filter inbound traffic to a specific network context, select **Specific network context** , and then select a network context: 
          * **Internet** : inbound traffic must match the [Internet network context for ingress packets](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#internet-context-ingress).
          * **Non-internet** : inbound traffic must match the [Non-internet network context for ingress packets](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#non-internet-ingress). 
          * **Intra VPC** : inbound traffic must match the [Criteria for intra-VPC network context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#intra-vpc-network-context-criteria).
          * **VPC networks** : inbound traffic must match the [Criteria for VPC networks context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#vpc-networks-context-criteria). You must select at least one VPC network: 
            * **Select current project** : lets you add one or more VPC network from the project that contains the firewall policy.
            * **Manually enter network** : lets you manually enter a project and VPC network.
            * **Select project** : lets you select a project from which you can select a VPC network.
     9. **Source filters** : specify additional source parameters. Some source parameters can't be used together, and your choice of source network context limits which source parameters you can use. For more information, see [Sources for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src) and [Ingress rule source combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src-combinations).

        * To filter inbound traffic by source IPv4 ranges, select **IPv4** , and then enter the CIDR blocks in the **IP ranges** field. Use `0.0.0.0/0` for any IPv4 source.
        * To filter inbound traffic by source IPv6 ranges, select **IPv6** , and then enter the CIDR blocks into the **IPv6 ranges** field. Use `::/0` for any IPv6 source. 
        * To filter inbound traffic by source secure tag values, select **Select scope for tags** in the **Secure tags** section. Then, provide tag keys and tag values. To add more tag values, click **Add tag**. 
        * To filter inbound traffic by source FQDN, enter FQDNs in the **FQDNs** field. For more information, see [FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview). 
        * To filter inbound traffic by source geolocation, select one or more locations from the **Geolocations** field. For more information, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview). 
        * To filter inbound traffic by source address group, select one or more address groups from the **Address groups** field. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies). 
        * To filter inbound traffic by source Google Threat Intelligence lists, select one or more Google Threat Intelligence lists from the **Google Cloud Threat Intelligence** field. For more information, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview). 
     10. **Destination** : specify optional destination parameters. For more information, see [Destinations for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-dest).

        * To skip filtering inbound traffic by destination IP address, select **None**.
        * To filter inbound traffic to by destination IP address, select **IPv4** or **IPv6** and then enter one or more CIDRs using the same format used for source IPv4 ranges or source IPv6 ranges.
     11. **Protocols and ports** : specify the protocols and destination ports for traffic to match the rule. For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).

     12. **Enforcement** : specify whether the firewall rule is enforced or not:

        * **Enabled** : creates the rule and begins enforcing the rule on new connections.
        * **Disabled** : creates the rule but doesn't enforce the rule on new connections.
  5. Click **Create**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies rules create PRIORITY \
        --firewall-policy=POLICY_NAME \
        --project=PROJECT_ID \  
        --global-firewall-policy \
        --description=DESCRIPTION \
        --direction=INGRESS \
        --action=ACTION \
        [--enable-logging | --no-enable-logging] \
        [--disabled | --no-disabled] \
        [--target-secure-tags=TARGET_SECURE_TAGS] \  
        [--target-service-accounts=TARGET_SERVICE_ACCOUNTS] \
        [--layer4-configs=LAYER_4_CONFIGS] \
        [--src-network-context=SRC_NETWORK_CONTEXT] \  
        [--src-networks=SRC_VPC_NETWORKS] \
        [--src-ip-ranges=SRC_IP_RANGES] \  
        [--src-address-groups=SRC_ADDRESS_GROUPS] \  
        [--src-fqdns=SRC_DOMAIN_NAMES] \  
        [--src-secure-tags=SRC_SECURE_TAGS] \  
        [--src-region-codes=SRC_COUNTRY_CODES] \  
        [--src-threat-intelligence=SRC_THREAT_LIST_NAMES] \
        [--dest-ip-ranges=DEST_IP_RANGES]
    

Replace the following:

  * `PRIORITY`: the numeric evaluation order of the rule within the policy. The rules are evaluated from highest to lowest priority, where `0` is the highest priority. Priorities must be unique for each rule. We recommend that you separate rule priority values by more than just a difference of one (for example, `100`, `200`, `300`) so that you can create new rules between the existing rules later.
  * `POLICY_NAME`: the name of the global network firewall policy in which you want to create the rule. 
  * `PROJECT_ID`: the project ID that contains the global network firewall policy. 
  * `DESCRIPTION`: an optional description for the new rule.
  * `ACTION`: specify one of the following actions: 
    * `allow`: allows connections that match the rule.
    * `deny`: denies connections that match the rule.
    * `goto_next`: continues the [firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation).
    * `apply_security_profile_group`: sends the packets to a [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) or [intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview). 
      * When the action is `apply_security_profile_group`, you must include `--security-profile-group SECURITY_PROFILE_GROUP`, where `SECURITY_PROFILE_GROUP` is the name of a [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profiles).
      * The security profile group's security profile can reference either a Cloud NGFW firewall endpoint or a Network Security Integration intercept endpoint group for in-band integration.
      * If the security profile group's security profile references a Cloud NGFW firewall endpoint, include either `--tls-inspect` or `--no-tls-inspect` to enable or disable TLS inspection.
  * The `--enable-logging` and `--no-enable-logging` flags enable or disable VPC firewall rules logging.
  * The `--disabled` and `--no-disabled` flags control whether the rule is disabled (not enforced) or enabled (enforced).
  * Specify a [target](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets): 
    * If you omit both the `--target-secure-tags` and `--target-service-accounts` flags, Cloud NGFW uses the [broadest instance targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-vm-broadest). 
    * `TARGET_SECURE_TAGS`: a comma-separated list of [secure tag](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) values that narrows the broadest instance targets to the network interfaces of VM instances that are bound to at least one of the secure tag values.
    * `TARGET_SERVICE_ACCOUNTS`: a comma-separated list of service accounts that narrows the broadest instance targets to the network interfaces of VM instances that use one of the service accounts.
  * `LAYER_4_CONFIGS`: a comma-separated list of Layer 4 configs. Each Layer 4 config can be one of the following: 
    * An IP protocol name (`tcp`) or IANA IP protocol number (`17`) without any destination port.
    * An IP protocol name and destination port separated by a colon (`tcp:80`).
    * An IP protocol name and destination port range separated by a colon using a dash to separate the beginning and ending destination ports (`tcp:5000-6000`). For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).
  * Specify a [source for the ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src). For more information, [Ingress rule source combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src-combinations): 
    * `SRC_NETWORK_CONTEXT`: defines a source network contexts to be used in conjunction with another supported source parameter to produce a source combination. Valid values when `--target-type=INSTANCES` are: `INTERNET`, `NON_INTERNET`, `VPC_NETWORKS`, or `INTRA_VPC`. For more information, see [Network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts).
    * `SRC_VPC_NETWORKS`: a comma-separated list of VPC networks specified by their URL identifiers. Specify this flag only when the `--src-network-context` is `VPC_NETWORKS`.
    * `SRC_IP_RANGES`: a comma-separated list of IP address ranges in CIDR format. Ranges in the list must all be either IPv4 CIDRs or IPv6 CIDRs, not a combination of both.
    * `SRC_ADDRESS_GROUPS`: a comma-separated list of address groups specified by their [unique URL identifiers](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification). Address groups in the list must contain all IPv4 addresses or all IPv6 addresses, not a combination of both.
    * `SRC_DOMAIN_NAMES`: a comma-separated list of FQDN objects specified in the [domain name format](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview#domain-name-format). 
    * `SRC_SECURE_TAGS`: a comma-separated list of [Tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview). You cannot use the `--src-secure-tags` flag if the `--src-network-context` is `INTERNET`.
    * `SRC_COUNTRY_CODES`: a comma-separated list of two-letter country codes. For more information, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview). You cannot use the `--src-region-codes` flag if the `--src-network-context` is `NON_INTERNET`, `VPC_NETWORKS`, or `INTRA_VPC`. 
    * `SRC_THREAT_LIST_NAMES`: a comma-separated list of names of Google Threat Intelligence lists. For more information, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview). You cannot use the `--src-threat-intelligence` flag if the `--src-network-context` is `NON_INTERNET`, `VPC_NETWORKS`, or `INTRA_VPC`. 
  * Optionally, specify a [destination for the ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-dest): 
    * `DEST_IP_RANGES`: a comma-separated list of IP address ranges in CIDR format. Ranges in the list must all be either IPv4 CIDRs or IPv6 CIDRs, not a combination of both.



### Create an ingress rule for internal load balancer targets

To restrict access to one or more internal Application Load Balancer or internal proxy Network Load Balancer forwarding rules, create at least two ingress rules that use internal load balancers as targets. Because the [implied action](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation) for internal Application Load Balancer and internal proxy Network Load Balancer targets is to allow ingress traffic, you must create the following rules to restrict access:

  * A lower-priority deny-ingress firewall rule with the `--src-ip-ranges=0.0.0.0/0` flag.
  * A higher-priority allow-ingress firewall rule with the source parameters you specify.



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



This section describes how to create an [ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#ingress_rules) for internal Application Load Balancers and internal proxy Network Load Balancer targets.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select a project that contains a global network firewall policy. 

  3. In the **Network firewall policies** section, click the name of a global network firewall policy in which you want to create a rule. 

  4. In the **Firewall rules** section, click **Create firewall rule** and specify the following configuration parameters:

     1. **Priority** : the numeric evaluation order of the rule.

The rules are evaluated from highest to lowest priority where `0` is the highest priority. Priorities must be unique for each rule. We recommend that you separate rule priority values by more than just a difference of one (for example, `100`, `200`, `300`) so that you can create new rules between the existing rules later.

     2. **Description** : provide an optional description.

     3. **Target type** : select **Internal load balancers**.

When you select this option, Cloud NGFW uses internal Application Load Balancers and internal proxy Network Load Balancers as the target.

     4. **Target** : select one of the following:

        * **Apply to all** : Cloud NGFW uses the [broadest load balancer targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-lb-broadest).
        * **Forwarding rule** : To select the forwarding rule, do the following: 
          1. Click **Select project** and select a project.
          2. For **Load balancer type** , select the load balancer type.
          3. For **Load balancer** , select the load balancer.
          4. For **Forwarding rule** , select the forwarding rule.
     5. **Action on match** : select one of the following:

        * **Allow** : to permit connections that match the rule parameters.
        * **Deny** : to block connections that match the rule parameters.
        * **Go to next** : to continue the [firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation).
     6. **Logs** : select **On** to enable firewall rules logging or **Off** to disable firewall rules logging for this rule. 

     7. **Source network context** : specify a [network context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts):

        * To skip filtering inbound traffic by network context, select **All network contexts**.
        * To filter inbound traffic to a specific network context, select **Specific network context** , and then select a network context: 
        * **Intra VPC** : inbound traffic must match the [Criteria for intra-VPC network context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#intra-vpc-network-context-criteria).
        * **VPC networks** : inbound traffic must match the [Criteria for VPC networks context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#vpc-networks-context-criteria). You must select at least one VPC network: 
          * **Select current project** : lets you add one or more VPC network from the project that contains the firewall policy.
          * **Manually enter network** : lets you manually enter a project and VPC network.
          * **Select project** : lets you select a project from which you can select a VPC network.
  5. **Source filters** : specify additional source parameters. Some source parameters can't be used together, and your choice of source network context limits which source parameters you can use. For more information, see [Sources for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src) and [Ingress rule source combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src-combinations).

     * To filter inbound traffic by source IPv4 ranges, select **IPv4** , and then enter the CIDR blocks in the **IP ranges** field. Use `0.0.0.0/0` for any IPv4 source.
     * To filter inbound traffic by source IPv6 ranges, select **IPv6** , and then enter the CIDR blocks into the **IPv6 ranges** field. Use `::/0` for any IPv6 source. 
     * To filter inbound traffic by source FQDN, enter FQDNs in the **FQDNs** field. For more information, see [FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview). 
     * To filter inbound traffic by source address group, select one or more address groups from the **Address groups** field. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies). 
  6. **Destination** : specify optional destination parameters. For more information, see [Destinations for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-dest).

     * To skip filtering inbound traffic by destination IP address, select **None**.
     * To filter inbound traffic to by destination IP address, select **IPv4** or **IPv6** and then enter one or more CIDRs using the same format used for source IPv4 ranges or source IPv6 ranges.
  7. **Protocols and ports** : specify the protocols and destination ports for traffic to match the rule. For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).

  8. **Enforcement** : specify whether the firewall rule is enforced or not:

     * **Enabled** : creates the rule and begins enforcing the rule on new connections.
     * **Disabled** : creates the rule but doesn't enforce the rule on new connections.


* Click **Create**.

###  gcloud 
    
    
    gcloud compute network-firewall-policies rules create PRIORITY \
        --firewall-policy=POLICY_NAME \
        --project=PROJECT_ID \  
        --global-firewall-policy \
        --description=DESCRIPTION \
        --direction=INGRESS \
        --action=ACTION \
        [--enable-logging | --no-enable-logging] \
        [--disabled | --no-disabled] \
        --target-type=INTERNAL_MANAGED_LB \  
        [--target-forwarding-rules=TARGET_FORWARDING_RULES] \
        [--layer4-configs=LAYER_4_CONFIGS] \
        [--src-network-context=SRC_NETWORK_CONTEXT] \  
        [--src-networks=SRC_VPC_NETWORKS] \
        [--src-ip-ranges=SRC_IP_RANGES] \  
        [--src-address-groups=SRC_ADDRESS_GROUPS] \  
        [--src-fqdns=SRC_DOMAIN_NAMES] \
        [--dest-ip-ranges=DEST_IP_RANGES]
    

Replace the following:

  * `PRIORITY`: the numeric evaluation order of the rule within the policy. The rules are evaluated from highest to lowest priority, where `0` is the highest priority. Priorities must be unique for each rule. We recommend that you separate rule priority values by more than just a difference of one (for example, `100`, `200`, `300`) so that you can create new rules between the existing rules later.
  * `POLICY_NAME`: the name of the global network firewall policy in which you want to create the rule. 
  * `PROJECT_ID`: the project ID that contains the global network firewall policy. 
  * `DESCRIPTION`: an optional description for the new rule.
  * `ACTION`: specify one of the following actions: 
    * `allow`: allows connections that match the rule.
    * `deny`: denies connections that match the rule.
    * `goto_next`: continues the [firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation).
  * The `--enable-logging` and `--no-enable-logging` flags enable or disable VPC firewall rules logging.
  * The `--disabled` and `--no-disabled` flags control whether the rule is disabled (not enforced) or enabled (enforced).
  * Specify a [target](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets): 
    * If you omit the `--target-forwarding-rules` flag, Cloud NGFW uses the [broadest load balancer targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-lb-broadest).
    * `TARGET_FORWARDING_RULES`: a single forwarding rule for an internal Application Load Balancer or internal proxy Network Load Balancer specified in the [target forwarding rules format](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-lb-specific-format). This parameter narrows the broadest load balancer targets to a specific internal Application Load Balancer or internal proxy Network Load Balancer.
  * `LAYER_4_CONFIGS`: a comma-separated list of Layer 4 configs. Each Layer 4 config can be one of the following: 
    * An IP protocol name (`tcp`) or IANA IP protocol number (`17`) without any destination port.
    * An IP protocol name and destination port separated by a colon (`tcp:80`).
    * An IP protocol name and destination port range separated by a colon using a dash to separate the beginning and ending destination ports (`tcp:5000-6000`). For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).
  * Specify a [source for the ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src). For more information, [Ingress rule source combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src-combinations): 
    * `SRC_NETWORK_CONTEXT`: defines a source network contexts to be used in conjunction with another supported source parameter to produce a source combination. Valid values when `--target-type=INTERNAL_MANAGED_LB` are `VPC_NETWORKS` or `INTRA_VPC`. For more information, see [Network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts).
    * `SRC_VPC_NETWORKS`: a comma-separated list of VPC networks specified by their URL identifiers. Specify this flag only when the `--src-network-context` is `VPC_NETWORKS`.
    * `SRC_IP_RANGES`: a comma-separated list of IP address ranges in CIDR format. Ranges in the list must all be either IPv4 CIDRs or IPv6 CIDRs, not a combination of both.
    * `SRC_ADDRESS_GROUPS`: a comma-separated list of address groups specified by their [unique URL identifiers](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification). Address groups in the list must contain all IPv4 addresses or all IPv6 addresses, not a combination of both.
    * `SRC_DOMAIN_NAMES`: a comma-separated list of FQDN objects specified in the [domain name format](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview#domain-name-format). 
  * Optionally, specify a [destination for the ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-dest): 
    * `DEST_IP_RANGES`: a comma-separated list of IP address ranges in CIDR format. Ranges in the list must all be either IPv4 CIDRs or IPv6 CIDRs, not a combination of both.



### Create an ingress rule to apply a security profile group to a load balancer

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To apply application layer inspection services to load balancer traffic, you can create a rule with the `apply_security_profile_group` action. This rule must target a specific forwarding rule belonging to a cross-region internal Application Load Balancer.

**Note:** To apply application layer inspection to load balancer traffic, you must also attach a Service Extension (`LBTCPExtension` resource) to the VPC network. The Service Extension applies to all cross-region internal Application Load Balancers in the VPC network. For more information, see [Configure application layer inspection](https://docs.cloud.google.com/firewall/docs/global-network-app-lb#configure-ngfw-enterprise).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

To perform this task, you need the following permissions or one of the following IAM roles: 

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy.



###  gcloud 

To create a firewall rule that applies application layer inspection to a specific cross-region internal Application Load Balancer, use the [`gcloud compute network-firewall-policies rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/create):
    
    
    gcloud compute network-firewall-policies rules create PRIORITY \
       --action=apply_security_profile_group \
       --security-profile-group=SECURITY_PROFILE_GROUP_NAME \
       --firewall-policy=NETWORK_FIREWALL_POLICY_NAME \
       --global-firewall-policy \
       --direction=INGRESS \
       --target-type=INTERNAL_MANAGED_LB \
       --target-forwarding-rules=CROSS_REGION_ALB_FORWARDING_RULE
    

Replace the following:

  * `PRIORITY`: the unique priority of the rule.
  * `SECURITY_PROFILE_GROUP_NAME`: the full or partial URI of the security profile group resource.
  * `NETWORK_FIREWALL_POLICY_NAME`: the name of the global network firewall policy.
  * `CROSS_REGION_ALB_FORWARDING_RULE`: the relative resource name of the forwarding rule in the format `projects/` PROJECT_ID`/global/forwardingRules/` FORWARDING_RULE_NAME`.



### Create an egress rule for VM targets

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



The following directions show how to create an [egress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#egress_rules). Egress rules only apply to targets that are network interfaces of Compute Engine instances. 

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select a project that contains a global network firewall policy. 

  3. In the **Network firewall policies** section, click the name of a global network firewall policy in which you want to create a rule. 

  4. In the **Firewall rules** section, click **Create firewall rule** and specify the following configuration parameters:

     1. **Priority** : the numeric evaluation order of the rule.

The rules are evaluated from highest to lowest priority where `0` is the highest priority. Priorities must be unique for each rule. We recommend that you separate rule priority values by more than just a difference of one (for example, `100`, `200`, `300`) so that you can create new rules between the existing rules later.

     2. **Description** : provide an optional description.

     3. **Target type** : select **Instances**.

When you select this option, Cloud NGFW uses VM instances as the target. 

     4. **Target** : select one of the following:

        * **Apply to all** : Cloud NGFW uses the [broadest instance targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-vm-broadest).
        * **Service accounts** : narrows the broadest instance targets to the network interfaces of VM instances that use the service account you specify: 
          * In the **Service account scope** section, select **In this project > Target service account**. This is to specify a service account in the same project as the global network firewall policy.
          * In the **Service account scope** section, select **In another project > Target service account**. This is to specify a service account in a Shared VPC service project.
        * **Secure tags** : narrows the broadest instance targets to the network interfaces of VM instances that are bound to at least one of the [secure tag](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) values that you specify. Click **Select scope for tags** and select the organization or project that contains the tag values to match. To add more tag values, click **Add tag**.
     5. **Direction of traffic** : select **Egress**. 

     6. **Action on match** : select one of the following:

        * **Allow** : to permit connections that match the rule parameters.
        * **Deny** : to block connections that match the rule parameters.
        * **Go to next** : to continue the [firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation).
        * **Apply security profile group** : sends the packets to a [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) or [intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview) based on the **Purpose** you select. 
          * To send packets to a Cloud NGFW firewall endpoint, select **Cloud NGFW Enterprise** , then select a **Security profile group**. To enable TLS inspection of the packets, select **Enable TLS inspection**.
          * To send packets to a Network Security Integration intercept endpoint group for in-band integration, select **NSI In-Band** , then select a **Security profile group**.
     7. **Logs** : select **On** to enable firewall rules logging or **Off** to disable firewall rules logging for this rule. 

     8. **Destination network context** : specify a [network context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts):

        * To skip filtering outgoing traffic by network context, select **All network contexts**.
        * To filter outgoing traffic to a specific network context, select **Specific network context** , and then select a network context: 
          * **Internet** : outgoing traffic must match the [Internet network context for egress packets](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#internet-context-egress).
          * **Non-internet** : outgoing traffic must match the [Non-internet network context for egress packets](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#non-internet-egress).
     9. **Destination filters** : specify additional destination parameters. Some destination parameters can't be used together, and your choice of destination network context limits which destination filters you can use. For more information, see [Destinations for egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest) and [Egress rule destination combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest-combinations).

        * To filter outgoing traffic by destination IPv4 ranges, select **IPv4** , and then enter the CIDR blocks in the **IP ranges** field. Use `0.0.0.0/0` for any IPv4 destination.
        * To filter outgoing traffic by destination IPv6 ranges, select **IPv6** , and then enter the CIDR blocks into the **IPv6 ranges** field. Use `::/0` for any IPv6 destination.
        * To filter outgoing traffic by destination FQDN, enter FQDNs in the **FQDNs** field. For more information, see [FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview).
        * To filter outgoing traffic by destination geolocation, select one or more locations from the **Geolocations** field. For more information, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview).
        * To filter outgoing traffic by destination address group, select one or more address groups from the **Address groups** field. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies). 
        * To filter outgoing traffic by destination Google Threat Intelligence lists, select one or more Google Threat Intelligence lists from the **Google Cloud Threat Intelligence** field. For more information, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview). 
     10. **Source** : specify optional source parameters. For more information, see [Sources for egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-src).

        * To skip filtering outgoing traffic by source IP address, select **None**.
        * To filter outgoing traffic to by source IP address, select **IPv4** or **IPv6** and then enter one or more CIDRs using the same format used for destination IPv4 ranges or destination IPv6 ranges.
     11. **Protocols and ports** : specify the protocols and destination ports for traffic to match the rule. For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).

     12. **Enforcement** : specify whether the firewall rule is enforced or not:

        * **Enabled** : creates the rule and begins enforcing the rule on new connections.
        * **Disabled** : creates the rule but doesn't enforce the rule on new connections.
  5. Click **Create**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies rules create PRIORITY \
        --firewall-policy=POLICY_NAME \
        --project=PROJECT_ID \  
        --global-firewall-policy \
        --description=DESCRIPTION \
        --direction=EGRESS \
        --action=ACTION \
        [--enable-logging | --no-enable-logging] \
        [--disabled | --no-disabled] \
        [--target-secure-tags=TARGET_SECURE_TAGS] \  
        [--target-service-accounts=TARGET_SERVICE_ACCOUNTS] \
        [--layer4-configs=LAYER_4_CONFIGS] \
        [--dest-network-context=DEST_NETWORK_CONTEXT] \
        [--dest-ip-ranges=DEST_IP_RANGES] \  
        [--dest-address-groups=DEST_ADDRESS_GROUPS] \  
        [--dest-fqdns=DEST_DOMAIN_NAMES] \  
        [--dest-region-codes=DEST_COUNTRY_CODES] \  
        [--dest-threat-intelligence=DEST_THREAT_LIST_NAMES] \
        [--src-ip-ranges=SRC_IP_RANGES]
    

Replace the following:

  * `PRIORITY`: the numeric evaluation order of the rule within the policy. The rules are evaluated from highest to lowest priority, where `0` is the highest priority. Priorities must be unique for each rule. We recommend that you separate rule priority values by more than just a difference of one (for example, `100`, `200`, `300`) so that you can create new rules between the existing rules later.
  * `POLICY_NAME`: the name of the global network firewall policy in which you want to create the rule. 
  * `PROJECT_ID`: the project ID that contains the global network firewall policy. 
  * `DESCRIPTION`: an optional description for the new rule.
  * `ACTION`: specify one of the following actions: 
    * `allow`: allows connections that match the rule.
    * `deny`: denies connections that match the rule.
    * `goto_next`: continues the [firewall rule evaluation process](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order#default-rule-evaluation).
    * `apply_security_profile_group`: sends the packets to a [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) or [intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview). 
      * When the action is `apply_security_profile_group`, you must include `--security-profile-group SECURITY_PROFILE_GROUP`, where `SECURITY_PROFILE_GROUP` is the name of a [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profiles).
      * The security profile group's security profile can reference either a Cloud NGFW firewall endpoint or a Network Security Integration intercept endpoint group for in-band integration.
      * If the security profile group's security profile references a Cloud NGFW firewall endpoint, include either `--tls-inspect` or `--no-tls-inspect` to enable or disable TLS inspection.
  * The `--enable-logging` and `--no-enable-logging` flags enable or disable VPC firewall rules logging.
  * The `--disabled` and `--no-disabled` flags control whether the rule is disabled (not enforced) or enabled (enforced).
  * Specify a [target](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets): 
    * If you omit both the `--target-secure-tags` and `--target-service-accounts` flags, Cloud NGFW uses the [broadest instance targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-vm-broadest). 
    * `TARGET_SECURE_TAGS`: a comma-separated list of [secure tag](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) values that narrows the broadest instance targets to the network interfaces of VM instances that are bound to at least one of the secure tag values.
    * `TARGET_SERVICE_ACCOUNTS`: a comma-separated list of service accounts that narrows the broadest instance targets to the network interfaces of VM instances that use one of the service accounts.
  * `LAYER_4_CONFIGS`: a comma-separated list of Layer 4 configs. Each Layer 4 config can be one of the following: 
    * An IP protocol name (`tcp`) or IANA IP protocol number (`17`) without any destination port.
    * An IP protocol name and destination port separated by a colon (`tcp:80`).
    * An IP protocol name and destination port range separated by a colon using a dash to separate the beginning and ending destination ports (`tcp:5000-6000`). For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).
  * Specify a [destination for the egress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest). For more information, [Egress rule destination combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest-combinations): 
    * `DEST_NETWORK_CONTEXT`: defines a destination network contexts to be used in conjunction with another supported destination parameter to produce a destination combination. Valid values are `INTERNET` and `NON_INTERNET`. For more information, see [Network contexts](https://docs.cloud.google.com/firewall/docs/understand-network-contexts).
    * `DEST_IP_RANGES`: a comma-separated list of IP address ranges in CIDR format. Ranges in the list must all be either IPv4 CIDRs or IPv6 CIDRs, not a combination of both.
    * `DEST_ADDRESS_GROUPS`: a comma-separated list of address groups specified by their [unique URL identifiers](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies#address-group-specification).
    * `DEST_DOMAIN_NAMES`: a comma-separated list of FQDN objects specified in the [domain name format](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview#domain-name-format).
    * `DEST_COUNTRY_CODES`: a comma-separated list of two-letter country codes. For more information, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview). 
    * `DEST_THREAT_LIST_NAMES`: a comma-separated list of names of Google Threat Intelligence lists. For more information, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview). 
  * Optionally, specify a [source for the egress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-src): 
    * `SRC_IP_RANGES`: a comma-separated list of IP address ranges in CIDR format. Ranges in the list must all be either IPv4 CIDRs or IPv6 CIDRs, not a combination of both.



## What's next

  * [Manage global network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies)
  * [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies)
  * [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
