---
url: https://docs.cloud.google.com/firewall/docs/secure-tag-best-practices/
title: Best practices for secure tags in Cloud NGFW \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:29.308568+00:00
---

# Best practices for secure tags in Cloud NGFW  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/secure-tag-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Best practices for secure tags in Cloud NGFW Stay organized with collections  Save and categorize content based on your preferences. 

This document provides architectural best practices to design, manage, and enforce secure tags in Cloud Next Generation Firewall (Cloud NGFW). Secure tags provide an identity-aware approach to network security by binding firewall rule evaluation to virtual machine (VM) workload identities rather than dynamic IP addresses. Secure tags are a foundational feature included in the Cloud Next Generation Firewall Essentials tier and are supported across all [Cloud NGFW tiers](https://docs.cloud.google.com/firewall/docs/ngfw_tiers). This guide is intended for network architects, security administrators, and DevOps engineers who design and maintain cloud network security policies.

This document organizes best practices into four key stages of the secure tag lifecycle:

  1. **Design your tag schema** : align tags with workload identities, configure micro-segmentation, and keep tags coarse-grained to avoid exceeding secure tag quota limits.
  2. **Configure access control and governance** : establish Identity and Access Management (IAM) separation of duties, choose appropriate scopes, and enforce tags during VM provisioning.
  3. **Design firewall policies and rule logic** : optimize rule evaluation, configure hierarchical policies, and implement safe default-deny rules.
  4. **Protect, monitor, and audit** : prevent accidental deletion with tag holds, enable firewall logging, and perform regular access audits.



Before using this guide, make sure that you are familiar with [Secure tags for firewalls overview](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview) and [Cloud NGFW overview](https://docs.cloud.google.com/firewall/docs/about-firewalls).

## Summary of best practices

The following table summarizes core best practices across the secure tag lifecycle:

Lifecycle stage | Key recommendation | Description  
---|---|---  
**Tag schema design** | Align tags with workload identity | Define tag keys by workload role (such as `env/prod` or `tier/database`), enforce mutually exclusive values, and keep tags coarse-grained to stay within quota limits.  
**Access control and governance** | Enforce separation of duties | Grant the `roles/resourcemanager.tagAdmin` role exclusively to security teams, restrict the `roles/resourcemanager.tagUser` role to deployment pipelines, and choose the right scope (`organization=auto` versus `network`).  
**VM provisioning** | Enforce tags at creation | Bind secure tags to VM network interfaces during provisioning and use organization policies to require tags on all new instances.  
**Policy architecture** | Specify target secure tags | Use target secure tags in firewall rules for static evaluation performance. Configure default-deny rules in hierarchical policies to protect untagged resources.  
**Cross-network security** | Secure cross-Virtual Private Cloud (VPC) connectivity | Maintain identity boundaries across peered VPC networks and Network Connectivity Center (NCC) spokes without managing static CIDR blocks.  
**Protection and monitoring** | Protect and monitor tags | Apply tag holds to prevent accidental deletion, enable firewall rule logging for troubleshooting, and audit IAM assignments regularly.  
  
## Design your tag schema

A well-structured tag schema simplifies firewall rules, streamlines security audits, and prevents conflicting policies.

### Align tags with workload identity

Design secure tag keys around distinct workload roles, application tiers, or regulatory classifications:

  * **Environment tier** : `env/prod`, `env/staging`, `env/dev`
  * **Application tier** : `tier/frontend`, `tier/backend`, `tier/database`
  * **Compliance status** : `scope/pci-dss`, `scope/hipaa`



#### Example: Three-tier application micro-segmentation

A typical three-tier web application consists of a **web frontend** , an **application backend** , and a **database**. To protect your database from unauthorized access, you can use secure tags to enforce network micro-segmentation so that each tier can communicate only with its adjacent tier:
    
    
    [ Web Tier (tag: tier/frontend) ]
                  |
                  |  Allow port 8080 (Web can communicate with App)
                  v
    [ App Tier (tag: tier/backend) ]
                  |
                  |  Allow port 5432 (App can communicate with DB)
                  v
    [ Database Tier (tag: tier/database) ]
    

To enforce this flow, configure two firewall policy rules:

  1. **Rule 1 (Web to App)** : allow ingress on port `8080` where the source tag is `tier/frontend` and the target tag is `tier/backend`.
  2. **Rule 2 (App to DB)** : allow ingress on port `5432` where the source tag is `tier/backend` and the target tag is `tier/database`.



**Result:** The web frontend cannot communicate directly with the database tier because no firewall rule allows traffic between `tier/frontend` and `tier/database`. Cloud NGFW enforces this boundary automatically, even if the VM instances share the same IP subnet.

#### Migration from network tags to secure tags

When upgrading from VPC network tags to firewall secure tags, note the following architectural differences:

Capability | Network tags (VPC rules) | Secure tags (Firewall policies)  
---|---|---  
**Target specification** | `targetTags = ["web-tier"]` | `targetSecureTags = ["tagValues/1234567890"]`  
**Source specification** | `sourceTags = ["db-client"]` | `sourceSecureTags = ["tagValues/0987654321"]`  
**Enforcement scope** | Single VPC network only | Across peered VPC networks, NCC spokes, and hierarchical policies  
**Routing support** | You can use network tags as next hops for static routes (also known as route tags) | You cannot use secure tags for routing. Use them only for firewall traffic filtering.  
**Access control** | No IAM permissions on individual tags | Resource Manager and IAM roles strictly govern tag access and binding  
  
### Enforce mutually exclusive tag values

Ensure resources receive exactly one value per tag key. For example, a VM instance must be assigned either `env/prod` or `env/dev`, but never both:

  * **Do** : assign a single environment tag (`env/prod`) and allow access to shared services through explicit firewall rules referencing destination tags (such as `env/shared-logging`).

  * **Don't** : stack multiple environment tags (`env/prod` and `env/dev`) on the same VM. Doing so allows the VM to match development firewall rules, exposing production resources to developer traffic.




### Keep tags coarse-grained to stay within quotas

Group similar VM instances under shared tag values rather than creating unique, instance-specific tags. Coarse-grained tagging keeps your security posture manageable and prevents your organization from exceeding secure tag quota limits.

When planning your tag schema, review the following limits:

  * [Maximum secure tag keys per organization](https://docs.cloud.google.com/firewall/docs/quotas#per-organization-limits)
  * [Maximum secure tag values per tag key](https://docs.cloud.google.com/firewall/docs/quotas#per-secure-tag)
  * [Maximum secure tag values per network interface](https://docs.cloud.google.com/firewall/docs/quotas#per-vm-nic)



### Use tags instead of service accounts for multi-NIC VMs

We recommend secure tags over service accounts as sources or destinations in firewall policies. Unlike service accounts, you can bind secure tags directly to individual network interfaces (vNICs) of a multi-homed VM. This approach lets you enforce different network policies on each network interface.

## Configure access control and governance

IAM governs secure tags to provide strict access control and clear separation of duties.

### Separate duties with IAM roles

Establish an operational boundary between the administrators who create tags and the teams that provision workloads:

  * **Tag Administrator (`roles/resourcemanager.tagAdmin`)**: grant exclusively to central network and security administrators to create, edit, and delete tag keys and values.
  * **Tag User (`roles/resourcemanager.tagUser`)**: grant to automated CI/CD deployment pipelines or provisioning service accounts at specific project or resource scopes to bind tags to VM network interfaces.
  * **Tag Viewer (`roles/resourcemanager.tagViewer`)**: grant to operations and audit teams who need read-only visibility into tag configurations.



#### Prevent self-tagging and privilege escalation

  * **Do** : grant `roles/resourcemanager.tagUser` exclusively to audited Infrastructure as Code (IaC) deployment pipelines (such as Terraform [`google_tags_tag_binding`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/tags_tag_binding) workflows) at the project or network interface level.
  * **Don't** : grant `roles/resourcemanager.tagUser` broadly to developer groups at the organization level. This prevents developers from self-attaching production tags (such as `env/prod`) to unauthorized development workloads.



### Scope tag keys appropriately

Define secure tag keys at the level of the resource hierarchy that matches your operational governance:

  * **Organization-scoped tags (`purpose-data=organization=auto`)**: define keys at the organization or folder level for centralized security governance across multiple VPC networks, peered networks, and hierarchical firewall policies.
  * **Network-scoped tags (`purpose-data=network`)**: use only for project-level isolation where tags must be permanently confined to a single VPC network.

**Note:** You cannot modify the parent resource, purpose (`GCE_FIREWALL`), and `purpose-data` parameters after tag creation. Plan your schema and scope before deployment.

### Enforce tag assignment during VM creation

Binding secure tags to VM network interfaces at creation time ensures that workloads are protected immediately when they launch.

To ensure that users and automated pipelines cannot provision instances without required secure tags, configure an organization policy to [enforce tags on resource creation](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview#enforce_tags). This policy blocks the creation of untagged, unprotected VM instances.

## Design firewall policies and rule logic

Integrate secure tags into your firewall policies to optimize rule evaluation and maintain consistent protection.

### Use hierarchical firewall policies for central enforcement

Define firewall rules that reference secure tags within hierarchical firewall policies at the organization or folder level. Hierarchical policies enforce organization-wide governance that local project owners cannot override.

**Note:** Hierarchical firewall policies support only organization-scoped tags (`organization=auto`). They don't support network-scoped tags.

### Specify target secure tags for efficiency

When creating firewall policy rules, specify target secure tags (`targetSecureTags`) whenever possible. Cloud NGFW evaluates target tags and source tags differently:

  * **Target secure tags (matched statically)** : rules with target tags apply statically to only the VM instances that carry those tags. This reduces the number of rules evaluated on each VM and improves performance.

  * **Source secure tags (matched dynamically per connection)** : rules that specify only source tags (`sourceSecureTags`) without target tags are evaluated dynamically for every connection across all VM instances in the network, which increases processing overhead.




### Implement safe defaults with hierarchical default-deny

Because VM instances don't inherit `GCE_FIREWALL` secure tags from parent folders or organizations, protect untagged resources by defining safe fallback rules in hierarchical policies:

  1. **Default-deny rule** : create a low-priority rule (for example, priority `65000`) at the organization or folder level that denies all traffic by default.

  2. **Conditional allow rules** : create higher-priority rules that allow traffic only between specific secure tags (such as `tier/frontend` to `tier/backend`).




If a VM instance is created without tags or its tags are detached, then the hierarchical default-deny rule automatically blocks traffic to and from the instance.

### Use secure tags across peered networks and NCC

Use secure tags to control traffic across VPC networks connected with VPC Network Peering or NCC [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). Secure tags maintain identity-aware boundaries across connected networks without requiring you to manage changing CIDR blocks.

## Protect, monitor, and audit

Continuous operational controls ensure that your secure tag configurations remain secure and resilient.

### Protect critical tag values with tag holds

Prevent accidental outages that occur when you delete in-use tags:

  * Apply tag holds to critical secure tag values to prevent deletion.
  * Verify that no active firewall rules rely on the Secure tag before you detach it from VM network interfaces. Removing all resource bindings (and any tag holds) is required before Google Cloud lets you delete a secure tag value.



### Enable firewall rule logging

Enable [firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging) on all rules that use secure tags. These logs capture matching traffic hits to help you audit access patterns, verify segmentation, and troubleshoot connectivity issues.

### Regularly audit IAM role assignments

Periodically audit principal assignments for `roles/resourcemanager.tagAdmin` and `roles/resourcemanager.tagUser`. This audit ensures that only authorized pipelines have tag binding permissions, which prevents privilege escalation and preserves environment isolation.

## What's next

  * [Secure tags for firewalls overview](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview)
  * [Create and manage secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls)
  * [Global network firewall policies overview](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies)
  * [Use secure tags across peered networks](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#use-tags-in-peering)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
