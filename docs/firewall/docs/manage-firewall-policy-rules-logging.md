---
url: https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging/
title: Manage firewall policy rules logging \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:04.945468+00:00
---

# Manage firewall policy rules logging  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage firewall policy rules logging Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to enable and disable logging for hierarchical and network firewall policy rules. For instructions about logging for firewall policy rules, see [Enable and disable firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging#enabling_and_disabling_firewall_policy_rules_logging). You can also learn how to view generated logs for firewall policy rules. To understand firewall policy rules logging, see [Firewall policy rules logging overview](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview). 

If you enable logging on a firewall policy rule, you can view insights and recommendations for it from Firewall Insights. For more information, see [Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview) in the Network Intelligence Center documentation.

## Permissions

To modify firewall policy rules or access logs, Identity and Access Management (IAM) principals need one of the following roles.

Task | Required role  
---|---  
Create, delete, or update firewall rules | Project [owner or editor](https://docs.cloud.google.com/iam/docs/understanding-roles#basic) or [Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)   
View logs | Project [owner, editor or viewer](https://docs.cloud.google.com/iam/docs/understanding-roles#basic) or [Logs Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#logging-roles) (`roles/logging.viewer`)   
For details about Logging IAM roles and permissions, see [ Predefined roles](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles).   
  
## Enable and disable firewall policy rules logging

When you create a firewall policy rule, you can enable firewall policy rules logging. For more information, see the following:

  * [Use hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks)
  * [Use global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules)
  * [Use regional network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#rule_tasks)



When you enable logging, you can specify whether to include metadata fields. If you omit them, you can save on storage costs. To enable or disable firewall policy rules logging for an existing firewall policy rule, see the following sections.

### Enable firewall policy rules logging for a hierarchical firewall policy

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select the name of the organization where you have created your hierarchical firewall policy.

  3. In the **Firewall policies located in this organization** section, click the name of your hierarchical firewall policy.

  4. In the **Logs** column, determine if firewall policy rules logging is **Disabled** or **Enabled** for each firewall policy rule.

  5. To enable logging for a firewall policy rule, click the rule priority, and then click **Edit**.

  6. In the **Logs** section, select **Enabled**.

  7. Click **Save**.




###  gcloud 

To update organization firewall policy rules, use the [`gcloud compute firewall-policies rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/update):
    
    
    gcloud compute firewall-policies rules update PRIORITY \
        --firewall-policy= FIREWALL_POLICY \
        --enable-logging
    

Replace the following:

  * `PRIORITY`: the priority of the firewall policy rule to update.
  * `FIREWALL_POLICY`: the name of the firewall policy into which the rule is updated.



For more information, see [SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/update).

### Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy_rule) to create a firewall policy rule with logging enabled.
    
    
    resource "google_compute_firewall_policy_rule" "primary" {
      firewall_policy = google_compute_firewall_policy.POLICY_ID
      description     = "Creates an ingress firewall policy rule with logging enabled"
      priority        = PRIORITY
      enable_logging  = true
      action          = "allow"
      direction       = "INGRESS"
      disabled        = false
      match {
        layer4_configs {
          ip_protocol = "tcp"
          ports = [8080]
        }
        layer4_configs {
          ip_protocol = "udp"
          ports = [22]
        }
        src_ip_ranges = ["SOURCE_IP_ADDRESS"]
      }
    }
    

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Enable firewall policy rules logging for an existing hierarchical firewall policy rule.
    
    
    POST https://compute.googleapis.com/compute/v1/locations/global/firewallPolicies/POLICY_ID/patchRule?priority=PRIORITY
    
    {
      "enableLogging": true,
    }
    
    

Replace the following:

  * `POLICY_ID`: the ID of the hierarchical firewall policy where the firewall policy rule is located.
  * `PRIORITY`: the priority of the firewall policy rule.



For more information, refer to the [`firewallPolicies.patchRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/patchRule) method.

### Disable firewall policy rules logging for a hierarchical firewall policy

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select the name of the organization where you have created your hierarchical firewall policy.

  3. In the **Firewall policies located in this organization** section, click the name of your hierarchical firewall policy.

  4. In the **Logs** column, determine if firewall policy rules logging is **Disabled** or **Enabled** for each firewall policy rule.

  5. To disable logging for a firewall policy rule, click the rule priority, and then click **Edit**.

  6. In the **Logs** section, select **Disabled**.

  7. Click **Save**.




###  gcloud 

To update organization firewall policy rules, use the [`gcloud compute firewall-policies rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/update):
    
    
    gcloud compute firewall-policies rules update PRIORITY \
        --firewall-policy= FIREWALL_POLICY \
        --no-enable-logging
    

Replace the following:

  * `PRIORITY`: the priority of the firewall policy rule to update.
  * `FIREWALL_POLICY`: the name of the firewall policy into which the rule is updated.



For more information, see [SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-policies/rules/update).

###  API 

Disable firewall policy rules logging for an existing hierarchical firewall policy rule
    
    
    POST https://compute.googleapis.com/compute/v1/locations/global/firewallPolicies/POLICY_ID/patchRule?priority=PRIORITY
    
    {
      "enableLogging": false,
    }
    

Replace the following:

  * `POLICY_ID`: the ID of the hierarchical firewall policy where the firewall policy rule is located.
  * `PRIORITY`: the priority of the firewall policy rule.



For more information, refer to the [`firewallPolicies.patchRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewallPolicies/patchRule) method.

### Enable firewall policy rules logging for a network firewall policy

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select the name of your project where you have created your network firewall policy.

  3. In the **Network firewall policies** section, click the name of the network firewall policy for which you want to enable logging.

  4. In the **Logs** column, determine if firewall policy rules logging is **Disabled** or **Enabled** for each firewall policy rule.

  5. To enable logging for a network firewall policy rule, click the rule priority, and then click **Edit**.

  6. In the **Logs** section, select **Enabled**.

  7. Click **Save**.




###  gcloud 

To update network firewall policy rules, use the [`gcloud compute network-firewall-policies rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/update):
    
    
    gcloud compute network-firewall-policies rules update PRIORITY \
        --firewall-policy= FIREWALL_POLICY \
        --enable-logging
    

Replace the following:

  * `PRIORITY`: the priority of the firewall policy rule to update.
  * `FIREWALL_POLICY`: the name of the network firewall policy where the firewall policy rule is located.



For more information, see the [SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/update).

### Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy_rule) to create a firewall policy rule with logging enabled.
    
    
    resource "google_compute_firewall_policy_rule" "primary" {
      firewall_policy = google_compute_firewall_policy.POLICY_ID
      description     = "Creates an ingress firewall policy rule with logging enabled"
      priority        = PRIORITY
      enable_logging  = true
      action          = "allow"
      direction       = "INGRESS"
      disabled        = false
      match {
        layer4_configs {
          ip_protocol = "tcp"
          ports = [8080]
        }
        layer4_configs {
          ip_protocol = "udp"
          ports = [22]
        }
        src_ip_ranges = ["SOURCE_IP_ADDRESS"]
      }
    }
    

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Enable firewall policy rules logging for an existing network firewall policy rule.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewallPolicies/POLICY_ID/patchRule?priority=PRIORITY
    
    {
      "enableLogging": true,
    }
    
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where your network policy is located.
  * `POLICY_ID`: the ID of the hierarchical firewall policy where the firewall policy rule is located.
  * `PRIORITY`: the priority of the firewall policy rule.



For more information, refer to the [`networkFirewallPolicies.patchRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies/patchRule) method.

### Disable firewall policy rules logging for a network firewall policy

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select the name of your project where you have created your network firewall policy.

  3. In the **Network firewall policies** section, click the name of the network firewall policy for which you want to enable logging.

  4. In the **Logs** column, determine if firewall policy rules logging is **Disabled** or **Enabled** for each firewall policy rule.

  5. To disable logging for a network firewall policy rule, click the rule priority, and then click **Edit**.

  6. In the **Logs** section, select **Disabled**.

  7. Click **Save**.




###  gcloud 

To update network firewall policy rules, use the [`gcloud compute network-firewall-policies rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/update):
    
    
    gcloud compute network-firewall-policies rules update PRIORITY \
        --firewall-policy= FIREWALL_POLICY \
        --no-enable-logging
    

Replace the following:

  * `PRIORITY`: the priority of the firewall policy rule to update.
  * `FIREWALL_POLICY`: the name of the network firewall policy where the firewall policy rule is located.



For more information, see the [SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/update).

###  API 

Disable firewall policy rules logging for an existing hierarchical firewall policy rule
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewallPolicies/POLICY_ID/patchRule?priority=PRIORITY
    
    {
      "enableLogging": false,
    }
    

Replace the following:

  * `POLICY_ID`: the ID of the hierarchical firewall policy where the firewall policy rule is located.
  * `PRIORITY`: the priority of the firewall policy rule.



For more information, refer to the [`networkFirewallPolicies.patchRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkFirewallPolicies/patchRule) method.

## View logs

Firewall policy rule logs are created in the project that hosts the network containing the VM instances and firewall rules. With [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you create VM instances in service projects, but these instances use a Shared VPC network located in the host project. In such scenarios, the host project stores the firewall policy rule logs.

To view firewall policy rule logs, use the Logs Explorer section of the Google Cloud console. For more information, see [View and analyze logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

The following queries demonstrate how you can search for specific firewall events.

### View all firewall logs

To view the firewall policy rule logs, use one of the following options.

###  Option 1 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **All resource**.

  3. In the **Select resource** list, click **Subnetwork** , and then click **Apply**.

  4. Click **All log names** , and then in the list, select **firewall**.

  5. Click **Apply**.




###  Option 2

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following into the query editor field.
         
         resource.type="gce_subnetwork"
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Ffirewall"
         

Replace `PROJECT_ID` with your project ID.

  3. If you don't see the query editor field, click the **Show query** toggle.

  4. Click **Run query**.




### View logs for specific subnets

To view the firewall policy rule logs for specific subnets, use one of the following options.

###  Option 1 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **All resource**.

  3. In the **Select resource** list, click **Subnetwork**.

  4. Select the subnetwork that you want to view logs for, and then click **Apply**.

  5. Click **All log names** , and then in the list, select **firewall**.

  6. Click **Apply**.




###  Option 2 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following into the query editor field.
         
         resource.type="gce_subnetwork"
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Ffirewall"
         resource.labels.subnetwork_name="SUBNET_NAME"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project
     * `SUBNET_NAME`: the name of your subnetwork
  3. If you don't see the query editor field, click the **Show query** toggle.

  4. Click **Run query**.




### View logs in specific VMs

To view the firewall policy rule logs for specific VMs, use one of the following options.

###  Option 1 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **All resource**.

  3. In the **Select resource** list, click **VM instance**.

  4. Select the instance that you want to view logs for, and then click **Apply**.

  5. Click **All log names** , and then in the list, select **firewall**.

  6. Click **Apply**.




###  Option 2 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following into the query editor field.
         
         resource.type="gce_subnetwork"
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Ffirewall"
         jsonPayload.instance.vm_name="INSTANCE_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your project
     * `INSTANCE_ID`: the ID of the VM that you want to view logs for
  3. If you don't see the query editor field, click the **Show query** toggle.

  4. Click **Run query**.




### View logs for connections from a specific country

To view the firewall policy rule logs for a specific country, do the following:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Paste the following into the query editor field.
         
         resource.type="gce_subnetwork"
         logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Ffirewall"
         jsonPayload.remote_location.country=COUNTRY
         

Replace the following:

     * `PROJECT_ID`: the ID of your project
     * `COUNTRY`: the [ISO 3166-1alpha-3](https://wikipedia.org/wiki/ISO_3166-1_alpha-3#Current_codes) code of the country that you want to view logs for
  3. If you don't see the query editor field, click the **Show query** toggle.

  4. Click **Run query**.




## Export logs

To export firewall policy rule logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2). You can use the [example queries](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging#viewing_logs) to narrow the logs that you export.

## Table of interactions

  * In the case of VM-to-VM communication, log records might be generated by both VMs, depending on their respective firewall rules.
  * The logged connection includes packets flowing both ways if the initial packet was allowed by the firewall.
  * For a given VM, incoming connections are matched against firewall rules configured on that VM's and outgoing connections are matched against egress firewall rule configured on that VM.
  * An allowed connection that matches a firewall rule with "allow and logging" is logged only once. The log entry is not repeated every 5 seconds even if the connection endures.
  * A denied connection matching a firewall rule with "denied and logging" does repeat the log entry every 5 seconds for as long as there are packets observed in that denied connection.
  * If you enable logging on a firewall rule that matches an already active TCP or UDP connection, a new log entry isn't generated. A log entry is created only if the connection remains idle for at least 10 minutes and a new packet is sent on the same connection. For continuous traffic with idle periods shorter than 10 minutes, only one log entry is generated for the connection.



This table shows the firewall logging behavior from the perspective of a single VM.

In a scenario in which a VM1 has an ingress rule R1 that matches packets and egress rule R2 that also matches packets, the behavior of firewall logging is as follows:

**VM1 has Ingress Rule R1 (matching packets)** | **VM1 has Egress Rule R2 (matching packets)** | **Connection Direction** | **Action** | **Log**  
---|---|---|---|---  
Allow + Log | Allow | Ingress | Allow | One log entry:  
disposition=allow, rule=R1   
Deny  
Allow + Log  
Deny + Log  
Allow | Allow | Ingress | Allow | No logging  
Deny  
Allow + Log  
Deny + Log  
Deny + Log | N/A | Ingress | Deny | One log entry every 5 seconds:  
disposition=deny, rule=R1  
Deny | N/A | Ingress | Deny | No logging  
Allow | Allow + Log | Egress | Allow | One log entry:  
disposition=allow, rule=R2  
Deny  
Allow + Log  
Deny + Log  
Allow | Allow | Egress | Allow | No Logging  
Deny  
Allow + Log  
Deny + Log  
N/A | Deny + Log | Egress | Deny | One log entry every 5 seconds:  
disposition=deny, rule=R2  
N/A | Deny | Egress | Deny | No logging  
  
Note that ingress and egress are symmetric.

This is the detailed description of the firewall logs semantics:

  * Allow + Log (logging is supported for TCP and UDP only)

    * Connection initiated in the direction to which the rule applies causes a single log record to be created.
    * Reply traffic is allowed due to connection tracking. Reply traffic does not cause any logging to occur, regardless of VPC firewall rules in that direction.
    * If the connection expires from the firewall (inactive for 10 minutes or TCP RST received), then another packet in either direction may trigger logging.
    * Logging is based on 5-tuples. TCP flags don't affect logging behavior.
  * Deny + Log (logging is supported for TCP and UDP only)

    * Packets are dropped (no connection is initiated).
    * Each packet that corresponds to a unique 5-tuple is logged as a failed connection attempt.
    * The same 5-tuple is logged again every 5 seconds if it continues to receive packets.



## What's next

  * [Manage VPC firewall rules logging](https://docs.cloud.google.com/firewall/docs/manage-vpc-firewall-rules-logging)
  * [Cloud Logging overview](https://docs.cloud.google.com/logging/docs)
  * [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
