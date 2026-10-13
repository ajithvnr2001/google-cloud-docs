---
url: https://docs.cloud.google.com/firewall/docs/manage-vpc-firewall-rules-logging/
title: Manage VPC firewall rules logging \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:14.402410+00:00
---

# Manage VPC firewall rules logging  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-vpc-firewall-rules-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage VPC firewall rules logging Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to enable and disable logging for VPC firewall rules. For instructions about logging for Virtual Private Cloud (VPC) firewall rules, see [Enable and disable VPC firewall rules logging](https://docs.cloud.google.com/firewall/docs/manage-vpc-firewall-rules-logging#enabling_and_disabling_vpc_firewall_rules_logging). You can also learn how to view generated logs for VPC firewall rules. To understand VPC firewall rules logging, see [ VPC firewall rules logging overview](https://docs.cloud.google.com/firewall/docs/vpc-firewall-rules-logging-overview). 

If you enable logging on a VPC firewall rule, you can view insights and recommendations for it from Firewall Insights. For more information, see [Firewall Insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/overview) in the Network Intelligence Center documentation.

## Permissions

To modify VPC firewall rules or access logs, Identity and Access Management (IAM) principals need one of the following roles.

Task | Required role  
---|---  
Create, delete, or update firewall rules | Project [owner or editor](https://docs.cloud.google.com/iam/docs/understanding-roles#basic) or [Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)   
View logs | Project [owner, editor or viewer](https://docs.cloud.google.com/iam/docs/understanding-roles#basic) or [Logs Viewer role](https://docs.cloud.google.com/iam/docs/understanding-roles#logging-roles) (`roles/logging.viewer`)   
For details about Logging IAM roles and permissions, see [ Predefined roles](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles).   
  
## Enable and disable VPC firewall rules logging

When you create a VPC firewall rule, you can enable VPC firewall rules logging. For more information, see [Create VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules).

When you enable logging, you can specify whether to include metadata fields. If you omit them, you can save on storage costs. To enable or disable VPC firewall rules logging for an existing firewall policy rule, see the following sections.

### Enable VPC firewall rules logging

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select the name of the project.

  3. In the **VPC firewall rules** section, you can view the list of the VPC firewall rules.

  4. In the **Logs** column, determine if **Logs** is **On** or **Off** for each firewall rule.

  5. To enable logging for one or more rules, select the checkbox next to each rule that you want to update.

  6. In the **VPC firewall rules** action bar, click **Configure logs**.

  7. In the **Configure logs** dialog, select **On**.

  8. To omit the metadata fields, expand **Show logs details** , and then clear the **Include metadata** checkbox.

  9. Click **Save configuration**.




###  gcloud 
    
    
    gcloud compute firewall-rules update RULE_NAME \
        --enable-logging \
        --logging-metadata=LOGGING_METADATA
    

Replace the following:

  * `RULE_NAME`: the name of the VPC firewall rule.
  * `LOGGING_METADATA`: whether VPC firewall rules logging includes metadata fields in [VPC firewall rules logging format](https://docs.cloud.google.com/firewall/docs/vpc-log-format). You can configure this field only if logging is enabled. The value must be `exclude-all` or `include-all`. By default, metadata fields are included.



For more information, see the [SDK reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update).

### Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall) to create a VPC firewall rule with logging enabled.
    
    
    resource "google_compute_firewall" "rules" {
      project     = var.project_id # Replace this with your project ID in quotes
      name        = "my-firewall-rule"
      network     = "default"
      description = "Creates firewall rule targeting tagged instances"
    
      log_config {
        metadata = "INCLUDE_ALL_METADATA"
      }
    
      allow {
        protocol = "tcp"
        ports    = ["80", "8080", "1000-2000"]
      }
      target_tags = ["web"]
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Enable VPC firewall rules logging for an existing VPC firewall rule.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls/RULE_NAME
    {
      "name": "RULE_NAME",
      "logConfig": {
        "enable": true,
        "metadata": "LOGGING_METADATA"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC firewall rule is located.
  * `RULE_NAME`: the name of the VPC firewall rule.
  * `LOGGING_METADATA`: whether VPC firewall rules logging includes metadata fields in [VPC firewall rules logging format](https://docs.cloud.google.com/firewall/docs/vpc-log-format). You can configure this field only if logging is enabled. The value must be `exclude-all` or `include-all`. By default, metadata fields are included.



For more information, refer to the [`firewalls.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/patch) method.

### Disable VPC firewall rules logging

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select the name of the project.

  3. In the **VPC firewall rules** section, you can view the list of the VPC firewall rules.

  4. In the **Logs** column, determine if **Logs** is **On** or **Off** for each firewall rule.

  5. To disable logging for one or more rules, select the checkbox next to each rule that you want to update.

  6. In the **VPC firewall rules** action bar, click **Configure logs**.

  7. In the **Configure logs** dialog, select **Off** , and then click **Save configuration**.




###  gcloud 
    
    
    gcloud compute firewall-rules update RULE_NAME \
        --no-enable-logging
    

Replace `RULE_NAME` with the name of the VPC firewall rule.

###  API 

Disable VPC firewall rules logging for an existing VPC firewall rule.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls/RULE_NAME
    {
      "name": "RULE_NAME",
      "logConfig": {
        "enable": false
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC firewall rule is located.
  * `RULE_NAME`: the name of the VPC firewall rule.



For more information, refer to the [`firewalls.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/patch) method.

## View logs

Firewall policy rule logs are created in the project that hosts the network containing the VM instances and firewall rules. With [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you create VM instances in service projects, but these instances use a Shared VPC network located in the host project. In such scenarios, the host project stores the firewall policy rule logs.

VPC firewall rule logs are created in the project that hosts the network containing the VM instances and VPC firewall rules. With [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you create VM instances in service projects, but these instances use a Shared VPC network located in the host project. In such scenarios, the host project stores the firewall policy rule logs.

To view VPC firewall rule logs, use the Logs Explorer section of the Google Cloud console. For more information, see [View and analyze logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

The following queries demonstrate how you can search for specific VPC firewall events.

### View all firewall logs

To view the VPC firewall rule logs, use one of the following options.

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

To view the VPC firewall rule logs for specific subnets, use one of the following options.

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

To view the VPC firewall rule logs for specific VMs, use one of the following options.

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

To view the VPC firewall rule logs for a specific country, do the following:

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

To export VPC firewall rule logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2). You can use the [example queries](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging#viewing_logs) to narrow the logs that you export.

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

  * [Manage firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/manage-firewall-policy-rules-logging)
  * [Cloud Logging overview](https://docs.cloud.google.com/logging/docs)
  * [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
