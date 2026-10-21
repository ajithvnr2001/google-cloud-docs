---
url: https://docs.cloud.google.com/vpc/docs/add-remove-network-tags/
title: Add network tags \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:10.378880+00:00
---

# Add network tags  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/add-remove-network-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add network tags

A tag is simply a character string added to a _tags_ field in a resource, such as [Compute Engine ](https://docs.cloud.google.com/compute/docs) virtual machine (VM) instances or [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates). A tag is not a separate resource, so you cannot create it separately. All resources with that string are considered to have that tag. Tags enable you to make [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) and [routes](https://docs.cloud.google.com/vpc/docs/routes) applicable to specific VM instances.

**Note:** Network tags are different from [Resource Manager tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). A Resource Manager tag is a key-value pair that can be attached to a Google Cloud resource. For more information about the differences between Resource Manager tags and network tags, see [Comparison of Tags and network tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#differences).

You can assign network tags to new VMs at creation time, or you can edit the set of assigned tags at any time later. You can edit network tags without stopping a VM.

## Specifications

The network tags that you assign to an instance apply to all of the instance's network interfaces. A network tag only applies to the [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc) that are directly attached to the instance's network interfaces. This is true even for [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), because peered networks remain distinct networks. Thus, the network tags are still only meaningful in the network to which the instance's network interface is attached.

Network tags must start with a lowercase letter and can contain lowercase letters, numbers, and hyphens. Tags must end with a lowercase letter or number.

**Note:** Networks tags don't need to be unique across multiple VPC networks. The same tags can be used in different networks for unique purposes in each.

### Permissions

The following IAM roles are required for tasks discussed on this page. For more details, see [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam).

Task | Required Role  
---|---  
Assign a network tag to a new instance when it is created | Project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) _or_ [Instance Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1)  
Add or remove network tags for existing instances  
Add, remove, or edit firewall rules | Project [owner or editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) _or_ [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin)  
  
### Limits

The following limits apply to network tags:

Limit | Value | Description  
---|---|---  
Maximum number of tags per VM | 64 | All tags for a VM must be unique. You can assign up to 64 different tags per VM.  
Maximum number of characters for each tag | 63 |   
Acceptable characters for a tag | lowercase letters, numbers, dashes | Additionally:  
• Tags must start with a lowercase letter.  
• Tags must end with either a number or a lowercase letter.  
  
## Firewall rules and routes

Network tags allow you to apply firewall rules and routes to a specific instance or set of instances:

  * You make a firewall rule applicable to specific instances by using target tags and source tags.

  * You make a route applicable to specific instances by using a tag.




### Targets for firewall rules

Every firewall rule in Google Cloud must have a [target](https://docs.cloud.google.com/vpc/docs/firewalls#rule_assignment) which defines the instances to which it applies. The default target is _all instances in the network_ , but you can specify instances as targets using either target tags or target service accounts.

The _target tag_ defines the Google Cloud VMs to which the rule applies. The rule is applied to a specific VPC network. It is made applicable to the primary internal IP address associated with the network interface of any instance attached to that VPC network that has a matching network tag.

Both ingress and egress firewall rules have targets:

  * Ingress rules apply to traffic entering your VPC network. For ingress rules, the targets are _destination_ VMs in Google Cloud.

  * Egress rules apply to traffic leaving your VPC network. For egress rules, the targets are _source_ VMs in Google Cloud.




Consider an ingress firewall rule that allows traffic on TCP port `80` from any source. The rule has a target tag of `http-server`. This rule would apply only to instances that have the `http-server` network tag, which means that incoming traffic on port `80` would be allowed to those instances.

### Source filters for ingress firewall rules

When you create _ingress_ firewall rules, you must specify a [source](https://docs.cloud.google.com/vpc/docs/firewalls#sources_or_destinations_for_the_rule). You can define it using ranges of either internal or external IP addresses or by referring to specific instances. You specify instances using either source tags or source service accounts.

The _source tag_ for an ingress firewall rule applied on a VPC network defines a source of traffic as coming from the primary internal IP address associated with the network interface attached to that VPC network for any instance having a matching network tag.

You can use a combination of IP ranges and source tags or a combination of IP ranges and source [service accounts](https://docs.cloud.google.com/compute/docs/access/service-accounts). You **cannot** use both network tags and service accounts in the same rule. For more information about source tags and service accounts, see [filtering by service account vs. network tag](https://docs.cloud.google.com/vpc/docs/firewalls#service-accounts-vs-tags).

#### Considerations

When you use an ingress firewall rule with source tags, you might observe a propagation delay. This delay is typically a few seconds, but it can be, in rare cases, a few minutes. When you make the following changes, the ingress firewall rule can take time to apply to or be removed from an associated instance:

  * Starting or stopping an instance that has a tag that is associated with a rule's source tag
  * Starting an instance that has a tag that is associated with a rule's target tag
  * Adding or removing tags from an instance if the tags are used in the source or target fields of a rule
  * Adding or removing source or target tags from a rule



This propagation delay applies only to ingress rules that use source tags. All other firewall rules take effect immediately on an instance. For example, an ingress rule that uses a source IP address range and target tags has no propagation delay.

### Interaction with static routes

When you create a static route, you specify a VPC network. You can then specify _tags_ so that the route only applies to traffic sent from VMs with matching network tags in the specified VPC network.

## Add, view, and remove tags

You can specify network tags when you create a VM instance. You can also add tags to, and remove tags from, an existing VM.

### Add tags when creating a VM

###  Console 

  1. Go to the VM instances page.   
[Go to the VM instances page](https://console.cloud.google.com/compute/instances)
  2. Click **Create instance**.
  3. Click **Management, security, disks, networking, sole tenancy** to open that section.
  4. Click the **Networking** tab.
  5. In the **Network tags** field, specify one or more tags, separated by commas.
  6. Populate other fields for the VM.
  7. Click **Create**.



###  gcloud 

To assign new tags to an instance, use the following `gcloud` command.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone ZONE \
        --tags TAGS \
        ...other parameters as needed.
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `ZONE`: the instance's zone.
  * `TAGS`: a comma-delimited list of tags.



See the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) for more information.

### Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) to create a VM instance that has network tags.
    
    
    resource "google_compute_instance" "default" {
      project      = var.project_id # Replace this with your project ID in quotes
      zone         = "southamerica-east1-b"
      name         = "backend-instance"
      machine_type = "e2-medium"
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-9"
        }
      }
      network_interface {
        network = "default"
      }
      tags = ["health-check", "ssh"]
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Add tags to an existing VM

###  Console 

  1. Go to the VM instances page.   
[Go to the VM instances page](https://console.cloud.google.com/compute/instances)
  2. Click an instance name.
  3. On the _VM instance details_ page, click **Edit**.
  4. In the **Network tags** section, specify one or more tags, separated by commas.
  5. Click **Save**.



###  gcloud 

To assign new tags to an instance, use the following `gcloud` command.
    
    
    gcloud compute instances add-tags INSTANCE_NAME \
        --zone ZONE \
        --tags TAGS
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `ZONE`: the instance's zone.
  * `TAGS`: a comma-delimited list of tags.



See the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-tags) for more information.

**Important:** The `gcloud compute instances add-tags` command **preserves** any existing tags associated with the instance.

### View tags

###  Console 

  1. Go to the VM instances page.   
[Go to the VM instances page](https://console.cloud.google.com/compute/instances)
  2. View tags in the **Network tags** column.

If needed, click **Column display options** to add the **Network tags** column.

  3. To view instances that are tagged with a specific tag, in the filter, select the property **Network tags** and enter the tags you want to filter on.




###  gcloud 

To list instances with their tags, run this command:
    
    
    gcloud compute instances list --format='table(name,status,tags.list())'
    

To list instances that are tagged with a specific tag, run this command:
    
    
    gcloud compute instances list --filter='tags:TAG_EXPRESSION'
    

Replace the following:

  * `TAG_EXPRESSION`: the expression you want to filter. For example, `tag1`, `tag1 OR tag2`, `tag1 AND tag2`. See [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters) for more information on filtering output.



### Remove tags

###  Console 

  1. Go to the VM instances page.   
[Go to the VM instances page](https://console.cloud.google.com/compute/instances)
  2. Click an instance name.
  3. On the _VM instance details_ page, click **Edit**.
  4. In the **Network tags** section, remove tags by clicking remove (`X`).
  5. Click **Save**.



###  gcloud 

To remove tags from an instance, use the following `gcloud` command.
    
    
    gcloud compute instances remove-tags INSTANCE_NAME \
        --zone ZONE \
        --tags TAGS
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `ZONE`: the instance's zone.
  * `TAGS`: a comma-delimited list of tags.



See the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/remove-tags) for more information.

**Important:** The `gcloud compute instances remove-tags` command **preserves** any tags that you do not explicitly choose to remove.

### Direct API requests

You can set the network tags associated with an instance by making a direct API request. Unlike using the Google Cloud console or `gcloud` commands, updating tags by direct API request **does not preserve** any existing tags. Ensure that you specify **the complete set** of tags that should be associated with an instance whenever you update tags in this way.

To update tags using a direct API request:

  1. Determine the latest fingerprint associated with the tags. The fingerprint is used to prevent any collisions from simultaneous API requests. The process of updating network tags for an instance is similar to [updating instance metadata](https://docs.cloud.google.com/compute/docs/metadata#update_metadata_on_a_running_instance).   
  
Perform a `GET` request to the instance; for example:
         
         GET https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances/example-instance
         

Look for the `tags.fingerprint` property in the response:
         
         200 OK
         {
         ...
         "tags": {
          "items": [
          "http-server",
          "db-client"
          ],
          "fingerprint": "MW8EqhxILtc="
         },
         ...
         }
         

You can also use a `gcloud` command to get the `fingerprint`, as shown in the following example:
         
         gcloud compute instances describe INSTANCE_NAME \
            --zone ZONE \
            --format="get(tags.fingerprint)"

  2. Make a `POST` request to the `instance().setTags` method. The request body must contain **all** of the tags that should be associated with the instance along with the `fingerprint` value.   
  
Example request:
         
         POST https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances/example-instance/setTags
         {
          "items": [
           "http-server",
           "db-client",
           "allow-internet-access"
           ],
          "fingerprint": "MW8EqhxILtc="
         }
         

Example response:
         
         200 OK
         {
               "kind": "compute#operation",
               "id": "9251830049681941507",
               "name": "operation-1442414898862-51fde63aa57b1-422323e0-c439fb04",
               "zone": "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f",
               "operationType": "setTags",
               "targetLink": "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instances/example-instance",
               "targetId": "4392196237934605253",
               "status": "PENDING",
               "user": "user@example.com",
               "progress": 0,
         ...
         }
         




## What's next

  * For more information about how to work with firewall rules, see [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) and [Use VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls).
  * For more information about how to work with routes, see [Routes](https://docs.cloud.google.com/vpc/docs/routes) and [Use routes](https://docs.cloud.google.com/vpc/docs/using-routes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
