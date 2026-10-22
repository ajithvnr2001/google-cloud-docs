---
url: https://docs.cloud.google.com/firewall/docs/using-firewall-policies/
title: Create hierarchical firewall policies and rules \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:12.497132+00:00
---

# Create hierarchical firewall policies and rules  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/using-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create hierarchical firewall policies and rules Stay organized with collections  Save and categorize content based on your preferences. 

To enforce consistent security and control network traffic across your Google Cloud organization and folders, you can create and manage hierarchical firewall policies and rules.

In this document, you learn how to create hierarchical policies, add ingress and egress policy rules, and associate the policies with the organization or folders within the organization. To create hierarchical firewall policies, you must have folder-level or organization-level Identity and Access Management (IAM) permissions, such as the Compute Security Admin role (`roles/compute.securityAdmin`). Before you read this page, make sure that you are familiar with the concepts described in the [Hierarchical firewall policies overview](https://docs.cloud.google.com/firewall/docs/firewall-policies).

## Limitations

  * Hierarchical firewall policy rules don't support using network tags to define targets. You must use a target Virtual Private Cloud (VPC) network or target service account instead.
  * Firewall policies can be applied at the folder and the organization level, but not at the VPC network level. Regular VPC firewall rules are supported for VPC networks.
  * Only one firewall policy can be associated to a resource (folder or organization), although the virtual machine (VM) instances in a folder can inherit rules from the entire hierarchy of resources above the VM.
  * [Firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview) is supported for `allow` and `deny` rules but not for `goto_next` rules.
  * IPv6 Hop-by-Hop protocol isn't supported in firewall rules.

**Note:** When you create a policy, you can give it a _short name_ that you can remember. The short name field was previously called _display name_ , and it might appear as display name in certain cases for a while.

## Firewall policy tasks

This section describes how to create and associate hierarchical firewall policies.

### Create a firewall policy

When you create a hierarchical firewall policy, you can set its parent to either the organization or a folder within the organization. After creating the policy, you can associate the policy with the organization or a folder in the organization.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.create`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the organization or folder where you want to create the policy
  * Compute Security Admin (`roles/compute.securityAdmin`) on the organization or folder where you want to create the policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or a folder within your organization.

  3. Click **Create firewall policy**.

  4. In the **Policy name** field, enter a name for the policy.

  5. Optional: If you want to create rules for your policy, click **Continue**.

  6. In the **Add rules** section, click **Create firewall rule**. For more information about creating firewall rules, see the following:

     * Create an ingress rule for VM targets
     * Create an egress rule for VM targets
  7. Optional: If you want to associate the policy with a resource, click **Continue**.

  8. In the **Associate policy with resources** section, click **Add**.

For more information, see Associate a policy with the organization or folder.

  9. Click **Create**.




###  gcloud 

Run these commands to create a hierarchical firewall policy whose parent is an organization:
    
    
    gcloud compute firewall-policies create \
        --organization ORG_ID \
        --short-name SHORT_NAME
    

Run these commands to create a hierarchical firewall policy whose parent is a folder within an organization:
    
    
    gcloud compute firewall-policies create \
        --folder FOLDER_ID \
        --short-name SHORT_NAME
    

Replace the following:

  * `ORG_ID`: your organization's ID

Specify an organization ID to create a policy whose parent is an organization. The policy can be associated with the organization or a folder within the organization.

  * `SHORT_NAME`: a name for the policy

A policy created by using the Google Cloud CLI has two names: a system-generated name and a short name provided by you. When using the gcloud CLI to update an existing policy, you can provide either the system-generated name or the short name and the organization ID. When using the API to update the policy, you must provide the system-generated name.

  * `FOLDER_ID`: the ID of a folder

Specify a folder ID to create a policy whose parent is a folder. The policy can be associated with the organization that contains the folder or any folder within that organization.




### Associate a policy with the organization or folder

When you associate a hierarchical firewall policy with an organization or folder in an organization, the firewall policy's rules—except for disabled rules and subject to each rule's target—apply to resources in VPC networks in projects of the associated organization or folder.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.use`
  * `compute.organizations.setFirewallPolicy`



**Roles**

  * Compute Organization Resource Admin (`roles/compute.orgSecurityResourceAdmin`) on the organization or folder to which the firewall policy should apply
  * And one of the following roles: 
    * Compute Network Admin (`roles/compute.networkAdmin`) on the firewall policy or organization or folder that contains the firewall policy
    * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the firewall policy or organization or folder that contains the firewall policy
    * Compute Organization Firewall Policy User (`roles/compute.orgFirewallPolicyUser `) on the firewall policy or organization or folder that contains the firewall policy
    * Compute Organization Security Policy Admin (`roles/compute.orgSecurityPolicyAdmin`) on the firewall policy or organization or folder that contains the firewall policy
    * Compute Organization Security Policy User (`roles/compute.orgSecurityPolicyUser`) on the firewall policy or organization or folder that contains the firewall policy
    * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or organization or folder that contains the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains your policy.

  3. Click your policy.

  4. Click the **Associations** tab.

  5. Click **Add Association**.

  6. Select the organization root or select folders within the organization.

  7. Click **Add**.




###  gcloud 

By default, if you attempt to insert an association to an organization or folder that already has an association, the method fails. If you specify the `--replace-association-on-target` flag, the existing association is deleted at the same time that the new association is created. This prevents the resource from being without a policy during the transition.
    
    
    gcloud compute firewall-policies associations create \
        --firewall-policy POLICY_NAME \
        --organization ORG_ID \
        [ --folder FOLDER_ID ] \
        [ --name ASSOCIATION_NAME ] \
        [ --replace-association-on-target ]
    

Replace the following:

  * `POLICY_NAME`: either the short name or the system-generated name of the policy
  * `ORG_ID`: your organization's ID
  * `FOLDER_ID`: if you are associating the policy with a folder, specify it here; omit if you are associating the policy to the organization level
  * `ASSOCIATION_NAME`: an optional name for the association; if unspecified, the name is set to "organization `ORG_ID`" or "folder `FOLDER_ID`"



## Firewall policy rule tasks

This section describes how to create hierarchical firewall policy rules.

### Create an ingress rule for VM targets

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the firewall policy or organization or folder that contains the policy
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or organization or folder that contains the policy



This section describes how to create an [ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#ingress_rules) that applies to network interfaces of Compute Engine instances.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select a organization or folder that contains a hierarchical firewall policy. 

  3. If necessary, in the **Hierarchy index** section, select a child folder.

  4. In the **Firewall policies** section, click the name of a hierarchical firewall policy in which you want to create a rule. 

  5. In the **Firewall rules** section, click **Create firewall rule** and specify the following configuration parameters:

     1. **Priority** : the numeric evaluation order of the rule.

The rules are evaluated from highest to lowest priority where `0` is the highest priority. Priorities must be unique for each rule. We recommend that you separate rule priority values by more than just a difference of one (for example, `100`, `200`, `300`) so that you can create new rules between the existing rules later.

     2. **Description** : provide an optional description.

     3. **Target type** : select **Instances**.

When you select this option, Cloud NGFW uses VM instances as the target. 

     4. **Target** : select one of the following:

        * **Apply to all** : Cloud NGFW uses the [broadest instance targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-vm-broadest).
        * **Service accounts** : narrows the broadest instance targets to the network interfaces of VM instances that use the service account that you specify in **Target service account**. 
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

     8. **Target networks** : optionally, to make the firewall policy apply to targets in specific VPC networks, click **Add network** , and then select the **Project** and the **Network**. 

     9. **Source network context** : specify a [network context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts):

        * To skip filtering inbound traffic by network context, select **All network contexts**.
        * To filter inbound traffic to a specific network context, select **Specific network context** , and then select a network context: 
          * **Internet** : inbound traffic must match the [Internet network context for ingress packets](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#internet-context-ingress).
          * **Non-internet** : inbound traffic must match the [Non-internet network context for ingress packets](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#non-internet-ingress). 
          * **Intra VPC** : inbound traffic must match the [Criteria for intra-VPC network context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#intra-vpc-network-context-criteria).
          * **VPC networks** : inbound traffic must match the [Criteria for VPC networks context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#vpc-networks-context-criteria). You must select at least one VPC network: 
            * **Select current project** : lets you add one or more VPC network from the project that contains the firewall policy.
            * **Manually enter network** : lets you manually enter a project and VPC network.
            * **Select project** : lets you select a project from which you can select a VPC network.
     10. **Source filters** : specify additional source parameters. Some source parameters can't be used together, and your choice of source network context limits which source parameters you can use. For more information, see [Sources for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src) and [Ingress rule source combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src-combinations).

        * To filter inbound traffic by source IPv4 ranges, select **IPv4** , and then enter the CIDR blocks in the **IP ranges** field. Use `0.0.0.0/0` for any IPv4 source.
        * To filter inbound traffic by source IPv6 ranges, select **IPv6** , and then enter the CIDR blocks into the **IPv6 ranges** field. Use `::/0` for any IPv6 source. 
        * To filter inbound traffic by source secure tag values, select **Select scope for tags** in the **Secure tags** section. Then, provide tag keys and tag values. To add more tag values, click **Add tag**. 
        * To filter inbound traffic by source FQDN, enter FQDNs in the **FQDNs** field. For more information, see [FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview). 
        * To filter inbound traffic by source geolocation, select one or more locations from the **Geolocations** field. For more information, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview). 
        * To filter inbound traffic by source address group, select one or more address groups from the **Address groups** field. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies). 
        * To filter inbound traffic by source Google Threat Intelligence lists, select one or more Google Threat Intelligence lists from the **Google Cloud Threat Intelligence** field. For more information, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview). 
     11. **Destination** : specify optional destination parameters. For more information, see [Destinations for ingress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-dest).

        * To skip filtering inbound traffic by destination IP address, select **None**.
        * To filter inbound traffic to by destination IP address, select **IPv4** or **IPv6** and then enter one or more CIDRs using the same format used for source IPv4 ranges or source IPv6 ranges.
     12. **Protocols and ports** : specify the protocols and destination ports for traffic to match the rule. For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).

     13. **Enforcement** : specify whether the firewall rule is enforced or not:

        * **Enabled** : creates the rule and begins enforcing the rule on new connections.
        * **Disabled** : creates the rule but doesn't enforce the rule on new connections.
  6. Click **Create**.




###  gcloud 
    
    
    gcloud compute firewall-policies rules create PRIORITY \
        --firewall-policy=POLICY_NAME \
        --organization=ORG_ID | --folder=FOLDER_ID \
        --description=DESCRIPTION \
        --direction=INGRESS \
        --action=ACTION \
        [--enable-logging | --no-enable-logging] \
        [--disabled | --no-disabled] \
        [--target-resources=TARGET_NETWORKS] \  
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
  * `POLICY_NAME`: the name of the hierarchical firewall policy in which you want to create the rule. 
  * `ORG_ID`: the organization ID that contains the hierarchical firewall policy, if its parent is an organization.
  * `FOLDER_ID`: the folder ID that contains the hierarchical firewall policy, if its parent is a folder. 
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
    * If you omit the `--target-resources`, `--target-secure-tags`, and `--target-service-accounts` flags, Cloud NGFW uses the [broadest instance targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-vm-broadest). 
    * `TARGET_NETWORKS`: a comma-separated list of VPC networks specified by their network resource URLs in the form `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME`. The `--target-resources` flag can be used by itself or in combination with one other target flag. For more information, see [Specific target combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-specific-combinations). 
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



### Create an egress rule for VM targets

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the firewall policy or organization or folder that contains the policy
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or organization or folder that contains the policy



The following directions show how to create an [egress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview#egress_rules). Egress rules only apply to targets that are network interfaces of Compute Engine instances. 

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select a organization or folder that contains a hierarchical firewall policy. 

  3. If necessary, in the **Hierarchy index** section, select a child folder.

  4. In the **Firewall policies** section, click the name of a hierarchical firewall policy in which you want to create a rule. 

  5. In the **Firewall rules** section, click **Create firewall rule** and specify the following configuration parameters:

     1. **Priority** : the numeric evaluation order of the rule.

The rules are evaluated from highest to lowest priority where `0` is the highest priority. Priorities must be unique for each rule. We recommend that you separate rule priority values by more than just a difference of one (for example, `100`, `200`, `300`) so that you can create new rules between the existing rules later.

     2. **Description** : provide an optional description.

     3. **Target type** : select **Instances**.

When you select this option, Cloud NGFW uses VM instances as the target. 

     4. **Target** : select one of the following:

        * **Apply to all** : Cloud NGFW uses the [broadest instance targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-vm-broadest).
        * **Service accounts** : narrows the broadest instance targets to the network interfaces of VM instances that use the service account that you specify in **Target service account**. 
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

     8. **Target networks** : optionally, to make the firewall policy apply to targets in specific VPC networks, click **Add network** , and then select the **Project** and the **Network**. 

     9. **Destination network context** : specify a [network context](https://docs.cloud.google.com/firewall/docs/understand-network-contexts):

        * To skip filtering outgoing traffic by network context, select **All network contexts**.
        * To filter outgoing traffic to a specific network context, select **Specific network context** , and then select a network context: 
          * **Internet** : outgoing traffic must match the [Internet network context for egress packets](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#internet-context-egress).
          * **Non-internet** : outgoing traffic must match the [Non-internet network context for egress packets](https://docs.cloud.google.com/firewall/docs/understand-network-contexts#non-internet-egress).
     10. **Destination filters** : specify additional destination parameters. Some destination parameters can't be used together, and your choice of destination network context limits which destination filters you can use. For more information, see [Destinations for egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest) and [Egress rule destination combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-dest-combinations).

        * To filter outgoing traffic by destination IPv4 ranges, select **IPv4** , and then enter the CIDR blocks in the **IP ranges** field. Use `0.0.0.0/0` for any IPv4 destination.
        * To filter outgoing traffic by destination IPv6 ranges, select **IPv6** , and then enter the CIDR blocks into the **IPv6 ranges** field. Use `::/0` for any IPv6 destination.
        * To filter outgoing traffic by destination FQDN, enter FQDNs in the **FQDNs** field. For more information, see [FQDN objects](https://docs.cloud.google.com/firewall/docs/fqdn-objects-overview).
        * To filter outgoing traffic by destination geolocation, select one or more locations from the **Geolocations** field. For more information, see [Geolocation objects](https://docs.cloud.google.com/firewall/docs/geolocation-objects-overview).
        * To filter outgoing traffic by destination address group, select one or more address groups from the **Address groups** field. For more information, see [Address groups for firewall policies](https://docs.cloud.google.com/firewall/docs/address-groups-firewall-policies). 
        * To filter outgoing traffic by destination Google Threat Intelligence lists, select one or more Google Threat Intelligence lists from the **Google Cloud Threat Intelligence** field. For more information, see [Google Threat Intelligence for firewall policy rules](https://docs.cloud.google.com/firewall/docs/threat-intelligence-overview). 
     11. **Source** : specify optional source parameters. For more information, see [Sources for egress rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-egress-src).

        * To skip filtering outgoing traffic by source IP address, select **None**.
        * To filter outgoing traffic to by source IP address, select **IPv4** or **IPv6** and then enter one or more CIDRs using the same format used for destination IPv4 ranges or destination IPv6 ranges.
     12. **Protocols and ports** : specify the protocols and destination ports for traffic to match the rule. For more information, see [Protocols and ports](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#protocols_and_ports).

     13. **Enforcement** : specify whether the firewall rule is enforced or not:

        * **Enabled** : creates the rule and begins enforcing the rule on new connections.
        * **Disabled** : creates the rule but doesn't enforce the rule on new connections.
  6. Click **Create**.




###  gcloud 
    
    
    gcloud compute firewall-policies rules create PRIORITY \
        --firewall-policy=POLICY_NAME \
        --organization=ORG_ID | --folder=FOLDER_ID \
        --description=DESCRIPTION \
        --direction=EGRESS \
        --action=ACTION \
        [--enable-logging | --no-enable-logging] \
        [--disabled | --no-disabled] \
        [--target-resources=TARGET_NETWORKS] \  
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
  * `POLICY_NAME`: the name of the hierarchical firewall policy in which you want to create the rule. 
  * `ORG_ID`: the organization ID that contains the hierarchical firewall policy, if its parent is an organization.
  * `FOLDER_ID`: the folder ID that contains the hierarchical firewall policy, if its parent is a folder. 
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
    * If you omit the `--target-resources`, `--target-secure-tags`, and `--target-service-accounts` flags, Cloud NGFW uses the [broadest instance targets](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-vm-broadest). 
    * `TARGET_NETWORKS`: a comma-separated list of VPC networks specified by their network resource URLs in the form `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME`. The `--target-resources` flag can be used by itself or in combination with one other target flag. For more information, see [Specific target combinations](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#target-specific-combinations). 
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

  * [Manage hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/manage-hierarchical-firewall-policies)
  * [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls)
  * [Hierarchical firewall policy examples](https://docs.cloud.google.com/firewall/docs/firewall-policies-examples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
