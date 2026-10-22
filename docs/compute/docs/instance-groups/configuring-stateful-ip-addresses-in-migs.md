---
url: https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs/
title: Configuring stateful IP addresses in MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:35.562197+00:00
---

# Configuring stateful IP addresses in MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configuring stateful IP addresses in MIGs Stay organized with collections  Save and categorize content based on your preferences. 

By configuring stateful IP addresses in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups), you ensure that IP addresses are preserved when VM instances in the group are autohealed, updated, and recreated.

You can preserve internal and external IPv4 addresses. You can configure IP addresses to be assigned automatically or assign specific IP addresses to each VM instance in a MIG.

## Before you begin

  * Review [ when to use stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs) and [how stateful MIGs work.](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work)
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Limitations

A MIG with stateful IP addresses has the following limitations:

  * IPv6 addresses are not supported.

  * Internal IP addresses are not supported in networks that have no subnetworks–for example, legacy networks.




A MIG with [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#what_makes_a_mig_stateful)—a _stateful MIG_ —has the following limitations:

  * You cannot use autoscaling if your MIG has stateful configuration.
  * If you want to use automated rolling updates, you must set the [replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#replacement_method) to `RECREATE`.
  * For stateful regional MIGs, you must [disable proactive redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) (set the redistribution type to `NONE`) to prevent deletion of stateful instances by automatic cross-zone redistribution.
  * If you use an [all-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic) to override instance template properties, you cannot specify those properties in any per-instance configuration and at the same time in the group's all-instances configuration.



## Pricing

You are charged for external IP addresses according to networking [pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).

**Caution:** Unused reserved external static IP addresses incur charges, so make sure to delete them if you don't intend to keep them for future use. When configuring stateful IPs, you can use the auto-delete rule to automatically delete a static IP address when its instance is permanently deleted.

## When to use stateful IP addresses

Preserving instances' IP addresses is useful in the following scenarios:

  * Your application requires an IP address to remain static after it has been assigned—for example, Kafka.
  * Your application's configuration depends on specific IP addresses—for example, a DNS server.
  * Users, including other applications, access your server through a dedicated static IP address—for example, a file server.
  * You need to migrate existing workloads without changing network configuration.



## Configuring stateful IP addresses for all VMs in a group

Configuring stateful IP addresses for all VMs in a MIG is useful in the following scenarios:

  * Your application requires an IP address to remain static after it has been assigned. But your application doesn't require assigning specific IP addresses to specific instances. IP addresses can be auto-assigned on instance creation.
  * Your users, including other applications, access your servers through static IP addresses that you publish after deploying your application.
  * You would like to benefit from instance autohealing and automated updates while preserving the static IP address that is auto-assigned on instance creation.



To maintain static internal or external IP addresses for existing and future VM instances in the group, configure that in the stateful policy.

When you add stateful IP address configuration to the group's stateful policy, the MIG applies the configuration in the following way:

  * For new instances, the MIG automatically assigns and reserves static IP addresses.
  * For existing instances, the MIG promotes in-use ephemeral [internal](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#promote-in-use-internal-address) or [external](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#promote_ephemeral_ip) IP addresses to static addresses by reserving the corresponding static IP addresses.
  * For existing instances without external IP addresses, the MIG assigns and reserves static IP addresses, and adds [access configuration](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign) to the corresponding network interface with the following default values:
        
        "accessConfigs": [
          {
            "kind": "compute#accessConfig",
            "name": "External NAT",
            "natIP": "XX.XX.XX.XX",
            "networkTier": "PREMIUM",
            "type": "ONE_TO_ONE_NAT"
          }
        ]
        




To reserve a static IP address, the MIG creates an [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource.

**Note:** All VM instances have a network interface with the name `nic0` and this network interface is used by default when you configure a stateful IP.  
  
You have the option to create instances that have [multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces) by setting multiple network interfaces in your group's instance template. In this case, separately specify each internal or external IP that you want to make stateful for each network interface.

### Configuring stateful IP addresses on MIG creation

Use the Google Cloud console, gcloud CLI, Terraform, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the[`instanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) method
  * For regional MIGs, all permissions required to call the[`regionInstanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) method



A MIG uses the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) service account to manage its instances. This service account has [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role by default, which includes all necessary permissions for managing stateful IP addresses.

If you need to create a custom role, the following permissions are required for managing stateful network interfaces:

  * `compute.addresses.create` for creating static external IP addresses
  * `compute.addresses.createInternal` for creating static internal IP addresses
  * `compute.addresses.use` for assigning a static external IP address to an instance
  * `compute.addresses.useInternal` for assigning a static internal IP address to an instance
  * `compute.addresses.delete` for deleting static IP addresses on permanent instance deletion
  * `compute.subnetworks.use` for creating static external IP addresses
  * `compute.subnetworks.useInternal` for creating static internal IP addresses
  * [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role to either the whole host project or select subnets of its Shared VPC networks for creating VM instances with static IP addresses in Shared VPC networks or subnets that belong to the host project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select your project and click **Continue**.

  3. Click **Create instance group**.

  4. Select **New managed instance group (stateful)**.

  5. Specify a **Name** for the instance group.

  6. Select an **Instance template**.

  7. Under **Number of instances** , specify the number of instances that you want to include in the managed instance group.

  8. Under **Stateful configuration** , expand the External IP and the Internal IP sections to configure those IP address types as stateful.

     1. For **Stateful** , select **Yes**.
     2. In the **On permanent instance deletion** list, select the action to perform on the stateful IP address when the VM instance is deleted. The available options are: 
        * **Detach IP** : (Default.) Unassign the address on instance deletion and keep the address reserved.
        * **Delete IP** : Delete the static IP address reservation when an instance is permanently deleted from the instance group—for example, when you delete an instance manually or decrease the group's size.
     3. After you finish the stateful configuration, click **Done**.
  9. Click **Create**.




###  gcloud 

When creating a MIG, to specify which IP addresses in network interfaces from the instance template should be stateful, use one or multiple of the following flags with the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create):

  * `--stateful-internal-ip` to mark an internal IP address of a given network interface as stateful.
  * `--stateful-external-ip` to mark an external IP address of a given network interface as stateful.


    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --template INSTANCE_TEMPLATE \
        --size SIZE \
        --instance-redistribution-type NONE \
        --stateful-internal-ip [enabled | interface-name=NI_NAME][,auto-delete=DELETE_RULE] \
        --stateful-external-ip [enabled | interface-name=NI_NAME][,auto-delete=DELETE_RULE]
    

Replace the following:

  * INSTANCE_GROUP_NAME: The name of the MIG to create.
  * INSTANCE_TEMPLATE: The name of the instance template to use when creating new instances.
  * SIZE: The initial number of instances you need in this group.
  * NI_NAME: (Optional.) Network interface name. If not provided, then the `enabled` option is required and the primary network interface named `nic0` is assumed by default. If you have multiple network interfaces, you can specify this flag for each IP in each network interface.
  * DELETE_RULE: (Optional.) Prescribes what should happen to the associated static [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource when a VM instance is permanently deleted. The available options are as follows:

    * `never`: (Default.) Never delete the static IP address. Instead, unassign the address on instance deletion and keep the address reserved.
    * `on-permanent-instance-deletion`: Delete the static IP address reservation when an instance is permanently deleted from the instance group–for example, when you delete an instance manually or decrease the group's size.

Regardless of the value of the delete rule, the group always preserves stateful IP addresses on instance autohealing, update, and recreation operations.




**Example**

You need to create a regional group of VM instances with static internal IP addresses for the default and custom networks and static external IP addresses only for the default network. You want the addresses to be assigned automatically, but need them to be preserved through instance autohealing, updates, and recreation events. You store instance configuration in an instance template named `node-template`.

To create the group, run the following command:
    
    
    gcloud compute instance-groups managed create example-group \
        --region us-east1 \
        --template node-template \
        --base-instance-name node \
        --instance-redistribution-type NONE \
        --size 3 \
        --stateful-internal-ip interface-name=nic0,auto-delete=on-permanent-instance-deletion
        --stateful-internal-ip interface-name=nic1,auto-delete=on-permanent-instance-deletion
        --stateful-external-ip enabled,auto-delete=on-permanent-instance-deletion
    

The internal IPs within the `nic0` and `nic1` network interfaces and the external IP within the `nic0` network interface are configured as stateful for all instances in the group. The group automatically reserves static internal and external IP addresses for each instance. Because the `auto-delete` flag is set to `on-permanent-instance-deletion`, the group will automatically delete the static IP address reservations when you delete the associated instances or the whole group.

To verify that the internal IPs within the `nic0` and `nic1` network interfaces and the external IP within the `nic0` network interface are configured as stateful, run the following command:
    
    
    gcloud compute instance-groups managed describe example-group \
        --zone us-east1-c

The output resembles the following:
    
    
    baseInstanceName: node
    ...
    name: example-group
    ...
    statefulPolicy:
      preservedState:
        internalIPs:
          nic0:
            autoDelete: ON_PERMANENT_INSTANCE_DELETION
          nic1:
            autoDelete: ON_PERMANENT_INSTANCE_DELETION
        externalIPs:
          nic0:
            autoDelete: ON_PERMANENT_INSTANCE_DELETION
    ...
    

You can see that the group's stateful policy declares internal IPs within the `nic0` and `nic1` network interfaces and external IPs within the `nic0` network interface as stateful with the rule to delete static IP reservations on permanent instance deletion.

###  Terraform 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

When creating a MIG, to specify which IP addresses within network interfaces from the instance template should be stateful, use one or multiple of the following blocks:

  * `stateful_internal_ip` to mark an internal IP address of a given network interface as stateful.
  * `stateful_external_ip` to mark an external IP address of a given network interface as stateful.



The following sample configures stateful IP addresses when creating a regional MIG. For more information about the resource used in the sample, see [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      name               = "example-group"
      base_instance_name = "node"
      target_size        = 3
      region             = "us-east1"
    
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      update_policy {
        type                         = "OPPORTUNISTIC"
        minimal_action               = "REFRESH"
        instance_redistribution_type = "NONE"
        max_unavailable_fixed        = 3
      }
      stateful_internal_ip {
        interface_name = "nic0"
        delete_rule    = "ON_PERMANENT_INSTANCE_DELETION"
      }
      stateful_internal_ip {
        interface_name = "nic1"
        delete_rule    = "ON_PERMANENT_INSTANCE_DELETION"
      }
      stateful_external_ip {
        interface_name = "nic0"
        delete_rule    = "ON_PERMANENT_INSTANCE_DELETION"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

When creating a MIG, to specify which IP addresses within network interfaces from the instance template should be stateful, include them in the `statefulPolicy` field in the request body of the [`instanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) or [`regionInstanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/instanceGroupManagers
    
    {
      "name": "INSTANCE_GROUP_NAME",
      "versions": [
        {
          "instanceTemplate": "global/instanceTemplates/INSTANCE_TEMPLATE"
        }
      ],
      "targetSize": SIZE,
      "statefulPolicy": {
        "preservedState": {
          "internalIPs": {
            "NI_NAME": {"autoDelete": "DELETE_RULE" }
          },
          "externalIPs": {
            "NI_NAME": {"autoDelete": "DELETE_RULE" }
          }
        }
      },
      "updatePolicy": {
        "instanceRedistributionType": "NONE"
      }
    }
    

Replace the following:

  * PROJECT: The project ID for the request.
  * REGION: For regional MIGs, the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the group is located. For zonal MIGs, replace `regions/REGION` with `zones/ZONE` and specify the zone where the MIG is located.
  * NAME: The name of the MIG to create.
  * INSTANCE_TEMPLATE: The name of the instance template to use when creating new instances.
  * SIZE: The initial number of instances you need in this group.
  * NI_NAME: (Optional.) Network interface name. If not provided, then the `enabled` option is required and the primary network interface named `nic0` is assumed by default. If you have multiple network interfaces, you can specify multiple NI_NAMES.
  * DELETE_RULE: (Optional) Prescribes what should happen to an associated static [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource when a VM instance is permanently deleted. The available options are as follows:

    * `NEVER`: (Default) Never delete the static IP address. Instead, unassign the address on instance deletion and keep the address reserved.
    * `ON_PERMANENT_INSTANCE_DELETION`: Delete the static IP address reservation when an instance is permanently deleted from the instance group–for example, when you delete an instance manually or decrease the group's size.

Regardless of the value of the delete rule, the group always preserves stateful IP addresses on instance autohealing, update, and recreation operations.




**Example**

You need to create a regional group of VM instances with static internal IP addresses for the default and custom networks and static external IP addresses only for the default network. You want the addresses to be assigned automatically, but need them to be preserved through instance autohealing, updates, and recreation events. You store instance configuration in an instance template named `node-template`.

To create the group, use the `regionInstanceGroupManagers.insert` method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers
    
    {
      "name": "example-group",
      "baseInstanceName": "node",
      "versions": [
        {
          "instanceTemplate": "global/instanceTemplates/node-template"
        }
      ],
      "targetSize": 3,
      "statefulPolicy": {
        "preservedState": {
          "internalIPs": {
            "nic0": {"autoDelete": "ON_PERMANENT_INSTANCE_DELETION" },
            "nic1": {"autoDelete": "ON_PERMANENT_INSTANCE_DELETION" }
          }
          "externalIPs": {
            "nic0": {"autoDelete": "ON_PERMANENT_INSTANCE_DELETION" }
          }
        }
      },
      "updatePolicy": {
        "instanceRedistributionType": "NONE"
      }
    }
    

The internal IPs within the `nic0` and `nic1` network interfaces and the external IPs within the `nic0` network interface are configured as stateful for all instances in the group. The group automatically reserves static internal and external IP addresses for each instance. Because the `auto-delete` field is set to `ON_PERMANENT_INSTANCE_DELETION`, the group will automatically delete the static IP address reservations when you delete associated instances or the whole group.

Use the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get) to verify that the internal IPs within the `nic0` and `nic1` network interfaces and external IPs within the `nic0` network interface are configured in the stateful policy of the new `regionInstanceGroupManagers` resource:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers/example-group
    

The response contains the configured stateful policy:
    
    
    {
      "name": "example-group",
      "baseInstanceName": "node",
      ...
      "statefulPolicy": {
        "preservedState": {
          "internalIPs": {
            "nic0": {"autoDelete": "ON_PERMANENT_INSTANCE_DELETION" },
            "nic1": {"autoDelete": "ON_PERMANENT_INSTANCE_DELETION" }
          }
          "externalIPs": {
            "nic0": {"autoDelete": "ON_PERMANENT_INSTANCE_DELETION" }
          }
        }
      }
      ...
    }
    

You can see that the group's stateful policy declares internal IPs within the `nic0` and `nic1` network interfaces and external IPs within the `nic0` network interface as stateful with the rule to delete the associated static IP address reservations on permanent instance deletion.

### Setting and updating stateful configuration for IP addresses in existing MIG

If you run a workload on a stateless MIG (a MIG without any stateful configuration) and the workload requires static IP addresses, you can configure IP addresses already assigned to the managed VM instances to become stateful. This ensures that the IP addresses of your existing VMs are preserved on instance autohealing, updates, and recreation events. You can optionally keep the static IP address reservations after the instances have been deleted.

By configuring a stateful policy for IP addresses in an existing MIG, you can do the following:

  * Configure IP addresses as stateful for all existing and future instances in the group. This promotes the corresponding ephemeral IP addresses of all existing instances to static IP addresses.
  * Update the existing stateful configuration for IP addresses.



The MIG applies the updated configuration in the stateful policy automatically and asynchronously to all instances. Updates to IP address configurations in a stateful policy don't disrupt running VM instances. To learn more, read about [applying stateful policy updates](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#how_stateful_policy_updates_are_applied_to_instances).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the[`instanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) method
  * For regional MIGs, all permissions required to call the[`regionInstanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) method



A MIG uses the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) service account to manage its instances. This service account has [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role by default, which includes all necessary permissions for managing stateful IP addresses.

If you need to create a custom role, the following permissions are required for managing stateful network interfaces:

  * `compute.addresses.create` for creating static external IP addresses
  * `compute.addresses.createInternal` for creating static internal IP addresses
  * `compute.addresses.use` for assigning a static external IP address to an instance
  * `compute.addresses.useInternal` for assigning a static internal IP address to an instance
  * `compute.addresses.delete` for deleting static IP addresses on permanent instance deletion
  * `compute.subnetworks.use` for creating static external IP addresses
  * `compute.subnetworks.useInternal` for creating static internal IP addresses
  * [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role to either the whole host project or select subnets of its Shared VPC networks for creating VM instances with static IP addresses in Shared VPC networks or subnets that belong to the host project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group for which you want to specify stateful IP addresses.

  3. Click **Edit** to modify the managed instance group.

  4. Click **Stateful & per-instance configuration** to expand the section.

  5. In the **Group config** section, click the **External IP** and the **Internal IP** that you want to make stateful.

     1. For **Stateful** , select **Yes**.
     2. In the **On permanent instance deletion** list, select the action to perform on the stateful IP address when the VM instance is deleted. The available options are: 
        * **Detach IP** : (Default.) Unassign the address on instance deletion and keep the address reserved.
        * **Delete IP** : Delete the static IP address reservation when an instance is permanently deleted from the instance group— for example, when you delete an instance manually or decrease the group's size.
     3. After you update the stateful configuration, click **Done**.
     4. Click **Save** to complete the update.



###  gcloud 

To specify which IP addresses should be stateful or to update the stateful IP configuration for an existing MIG, use one or multiple `--stateful-internal-ip` or `--stateful-external-ip` flags with the [`gcloud compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update).
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        --stateful-internal-ip [enabled | interface-name=NI_NAME][,auto-delete=DELETE_RULE] \
        --stateful-external-ip [enabled | interface-name=NI_NAME][,auto-delete=DELETE_RULE]
    

Replace the following:

  * INSTANCE_GROUP_NAME: The name of the MIG to update.
  * NI_NAME: (Optional.) Network interface name. If not provided, then the `enabled` option is required and the primary network interface named `nic0` is assumed by default. If you have multiple network interfaces, you can specify this flag for each IP in each network interface.
  * DELETE_RULE: (Optional.) Prescribes what should happen to an associated static [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource when a VM instance is permanently deleted. The available options are as follows:

    * `never`: (Default.) Never delete the static IP address. Instead, unassign the address on instance deletion and keep the address reserved.
    * `on-permanent-instance-deletion`: Delete the static IP address reservation when an instance is permanently deleted from the instance group–for example, when you delete an instance manually or decrease the group's size.

Regardless of the value of the delete rule, the group always preserves stateful IP addresses on instance autohealing, update, and recreation operations.




If a specified IP address is already configured in the stateful policy for a given network interface, the command updates the configuration.

**Example**

You need to expose a file server, running on a stateful MIG named `example-fs-group`, to external users through static external IP addresses. The instances in the group have ephemeral external IP addresses. You must make sure that the IP addresses are preserved on instance autohealing and updates so that external users have continuous access to the servers through the published IP addresses. You also need to keep the IP addresses reserved for continuity in the event of unintended group deletion.

Update the MIG to define the external IP addresses as stateful by using the following command:
    
    
    gcloud compute instance-groups managed update example-fs-group \
        --stateful-external-ip enabled
    

As a result, the group promotes ephemeral external IP addresses within the `nic0` network interface to static IP addresses for all managed instances asynchronously.

The external IP addresses are now preserved on instance autohealing, update, and recreation events. The associated static IP address reservations are unassigned and preserved on instance deletion because the unspecified `auto-delete` rule is set to `never` by default.

You can verify that the stateful external IP is configured in the stateful policy by running the [`gcloud compute instance-groups managed describe example-fs-group` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe).

###  REST 

To specify which IP addresses should be stateful or to update the stateful IP configuration for an existing MIG, use the [`instanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [`regionInstanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) method:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "statefulPolicy": {
        "preservedState": {
          "internalIPs": {
            "NI_NAME": {"autoDelete": "DELETE_RULE" }
          },
          "externalIPs": {
            "NI_NAME": {"autoDelete": "DELETE_RULE" }
          }
        }
      }
    }
    

Replace the following:

  * PROJECT: The project ID for the request.
  * REGION: For regional MIGs, the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the group is located. For zonal MIGs, replace `regions/REGION` with `zones/ZONE` and specify the zone where the MIG is located.
  * NAME: The name of the MIG to create.
  * NI_NAME: (Required) Network interface name. The primary network interface is named `nic0`. If you have multiple network interfaces, you can specify multiple NI_NAMES.
  * DELETE_RULE: (Optional) Prescribes what should happen to an associated static [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource when a VM instance is permanently deleted. The available options are as follows:

    * `NEVER`: (Default) Never delete the static IP address. Instead, unassign the address on instance deletion and keep the address reserved.
    * `ON_PERMANENT_INSTANCE_DELETION`: Delete the static IP address reservation when an instance is permanently deleted from the instance group–for example, when you delete an instance manually or decrease the group's size.

Regardless of the value of the delete rule, the group always preserves stateful IP addresses on instance autohealing, update, and recreation operations.




If a specified IP address is already configured in the stateful policy, the method patches the configuration.

**Example**

You need to expose a file server, running on a stateful MIG named `example-fs-group`, to external users through static external IP addresses. The instances in the group have ephemeral external IP addresses. You must make sure that the IP addresses are preserved on instance autohealing and updates so that external users have continuous access to the servers through the published network interface. You also need to keep the IP addresses reserved for continuity in the event of unintended group deletion.

Patch the MIG to define the external IP addresses as stateful:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers/example-fs-group
    
    {
      "statefulPolicy": {
        "preservedState": {
          "externalIPs": {
            "nic0": {"autoDelete": "NEVER" }
          }
        }
      }
    }
    

As a result, the group promotes ephemeral external IP addresses within the `nic0` network interface to static IP addresses for all managed instances asynchronously.

The external IP addresses are now preserved on instance autohealing, update, and recreation events. The associated static IP address reservations will be unassigned and preserved on instance deletion because the `autoDelete` rule is set to `NEVER`.

Verify that the external IP address is configured in the stateful policy by viewing the `regionInstanceGroupManagers` resource, returned by the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get).

### Declaring previously stateful IP addresses as stateless

You might need to configure a stateful IP address to become ephemeral–for example, for the following reasons:

  * You rearchitect your app to no longer rely on static IP addresses.
  * You configured the IP to be stateful by mistake and would like to revert it.



You can remove stateful IP configuration from the group's stateful policy to declare an IP address within a given network interface as ephemeral for all managed instances.

**Note:** If stateful IP configuration for the same network interface is present in a per-instance configuration, the IP address remain stateful for an associated instance even if you remove its configuration from the stateful policy. In such case, to make the IP ephemeral, you must also remove the IP addresses configuration from the per-instance configuration.

When you remove stateful IP configuration from the stateful policy, the MIG removes the IP addresses automatically and asynchronously from the [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) of all instances in the group. This operation does not disrupt running VM instances. The IP addresses remain active on the instances, but are no longer stateful. When you recreate or update the instances, or when the instances are autohealed, the MIG [unassigns](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip) the associated static IP addresses and auto-assigns ephemeral addresses. If you no longer need to keep the static external IP address reservations, you can now [release](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) them.

**Note:** Static IP addresses remain reserved after you remove stateful IP configuration from a MIG's stateful policy. Because the stateful configuration has been removed, the group no longer manages the static IP addresses. If you don't need to keep the static IP addresses, make sure to [release](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) the reservations to avoid unnecessary [charges](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).

To learn more, read the following documents:

  * [How removing a resource from stateful policy affects preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#removing_resource_from_stateful_policy).
  * [Applying stateful policy updates](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#how_stateful_policy_updates_are_applied_to_instances).



#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the[`instanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) method
  * For regional MIGs, all permissions required to call the[`regionInstanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) method



A MIG uses the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) service account to manage its instances. This service account has [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role by default, which includes all necessary permissions for managing stateful IP addresses.

If you need to create a custom role, the following permissions are required for managing stateful network interfaces:

  * `compute.addresses.create` for creating static external IP addresses
  * `compute.addresses.createInternal` for creating static internal IP addresses
  * `compute.addresses.use` for assigning a static external IP address to an instance
  * `compute.addresses.useInternal` for assigning a static internal IP address to an instance
  * `compute.addresses.delete` for deleting static IP addresses on permanent instance deletion
  * `compute.subnetworks.use` for creating static external IP addresses
  * `compute.subnetworks.useInternal` for creating static internal IP addresses
  * [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role to either the whole host project or select subnets of its Shared VPC networks for creating VM instances with static IP addresses in Shared VPC networks or subnets that belong to the host project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group from which you want to remove the stateful configuration for IP addresses.

  3. Click **Edit** to modify the managed instance group.

  4. Click **Stateful & per-instance configuration** to expand the section.

  5. In the **Group config** section, expand the **External IP** and the **Internal** IP that you want to make stateless.

     1. Change the **Stateful** option to **No**.
     2. Click **Done**.
  6. After you make the changes, click **Save**.




###  gcloud 

To specify which IP addresses from a MIG's stateful policy to make ephemeral, use the `--remove-stateful-internal-ips` or `--remove-stateful-external-ips` flag with the [`gcloud compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        --remove-stateful-internal-ips NI_NAME[,NI_NAME,...] \
        --remove-stateful-external-ips NI_NAME[,NI_NAME,...]
    

Replace the following:

  * INSTANCE_GROUP_NAME: The name of the MIG to update.
  * NI_NAME: (Required.) Network interface name. The primary network interface is named `nic0`. If you've multiple network interfaces, you can specify multiple NI_NAMES.

**Note:** You can see the network interface names of IP addresses that are configured in a MIG's stateful policy by running the [`gcloud compute instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe).

If you need to turn a stateful IP address from the default primary network interface named `nic0` into an ephemeral IP address, you can also use the following command:
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        --stateful-internal-ip disabled \
        --stateful-external-ip disabled
    

**Example**

Your application has been exposed to users through published static external IP addresses of the VM instances in a MIG called `example-group`. You have rearchitected your service by [deploying a load balancer](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer) in front of the MIG and routing the traffic to the managed VMs through it. You no longer need to maintain the static external IP addresses and would like to make the external IP addresses of the VMs ephemeral.

To make the stateful external IP addresses of the VMs in a MIG ephemeral, run the following command:
    
    
    gcloud compute instance-groups managed update example-group \
        --remove-stateful-external-ips nic0
    

The MIG removes the static external IP addresses of the `nic0` network interface automatically and asynchronously from the [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) of all instances in the group. The external IP addresses remain active on the instances, but are no longer stateful. When you recreate or update the instances, or when the instances are autohealed, the MIG [unassigns](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip) the associated static IP addresses and auto-assigns ephemeral addresses. If you no longer need to keep the static external IP address reservations, you can now [release](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) them.

###  REST 

To specify which IP addresses from a MIG's stateful policy to make ephemeral, remove each IP's configuration from the MIG's stateful policy using the [`instanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [`regionInstanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) method:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "statefulPolicy": {
        "preservedState": {
          "internalIPs": {
            "NI_NAME": null
          },
          "externalIPs": {
            "NI_NAME": null
          }
        }
      }
    }
    

Replace the following:

  * PROJECT: The project ID for the request.
  * REGION: For regional MIGs, the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the group is located. For zonal MIGs, replace `regions/REGION` with `zones/ZONE` and specify the zone where the MIG is located.
  * INSTANCE_GROUP_NAME: The name of the MIG to create.
  * NI_NAME: (Required) Network interface name. The primary network interface is named `nic0`. If you have multiple network interfaces, you can specify multiple NI_NAMES.

**Note:** You can see the network interface names of IP addresses that are configured in a MIG's stateful policy by calling the [`instanceGroupManagers.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get) or [`regionInstanceGroupManagers.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get) method.

**Example**

Your application has been exposed to users through published static external IP addresses of the VM instances in a MIG called `example-group`. You have rearchitected your service by deploying a load balancer in front of the MIG and routing the traffic to the managed VMs through it. You no longer need to maintain the static external IP addresses and would like to make the external IP addresses of the VMs ephemeral.

To make the stateful external IP addresses of the VMs in a MIG ephemeral, patch the MIG:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers/example-group
    
    {
      "statefulPolicy": {
        "preservedState": {
          "externalIPs": {
            "nic0": null
          }
        }
      }
    }
    

The MIG removes the static external IP addresses of the `nic0` network interface automatically and asynchronously from the [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) of all instances in the group. The external IP addresses remain active on the instances, but are no longer stateful. When you recreate or update the instances, or when the instances are autohealed, the MIG [unassigns](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip) the associated static IP addresses and auto-assigns ephemeral addresses. If you no longer need to keep the static external IP address reservations, you can now [release](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) them.

## Configuring stateful IP addresses individually for VMs in a MIG

Configuring stateful IP addresses individually for VMs in a MIG is useful in the following scenarios:

  * Migrating existing workloads (bringing existing reserved static IP addresses) from standalone VM instances to stateful MIGs in order to benefit from autohealing and automated updates.
  * Assigning specific reserved static IP addresses required by the architecture or workload configuration.



**Pro Tip** : Where feasible, consider configuring and auto-assigning stateful IP addresses for all VM instances in a MIG, instead of assigning specific IP addresses individually to each instance. Maintaining a group's stateful policy is less work compared to maintaining a set of individual per-instance configurations.

**Note:** All VM instances have a network interface with the name `nic0` and this network interface is used by default when you configure a stateful IP.  
  
You have the option to create instances that have [multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces) by setting multiple network interfaces in your group's instance template. In this case, separately specify each network interface that you need to make stateful.

### Configuring static IP addresses on VM creation in a MIG

You can reserve and assign static IP addresses to specific instances when individually creating those instances in a MIG. This is useful for migrating a stateful application from existing standalone VMs to a stateful MIG in a situation when architecture, configuration, or users rely on specific static IP addresses.

When you manually create an instance in a MIG and supply a static IP address, the MIG performs the following actions:

  1. Creates a static [internal](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) or [external](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address) IP address reservation for the supplied IP addresses if they don't exist yet.
  2. Creates an instance from the instance template using the provided instance name and IP addresses.
  3. Creates a [per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) with the provided stateful configuration for the IP addresses.



#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the[`instanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/createInstances) method
  * For regional MIGs, all permissions required to call the[`regionInstanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/createInstances) method



A MIG uses the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) service account to manage its instances. This service account has [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role by default, which includes all necessary permissions for managing stateful IP addresses.

If you need to create a custom role, the following permissions are required for managing stateful network interfaces:

  * `compute.addresses.create` for creating static external IP addresses
  * `compute.addresses.createInternal` for creating static internal IP addresses
  * `compute.addresses.use` for assigning a static external IP address to an instance
  * `compute.addresses.useInternal` for assigning a static internal IP address to an instance
  * `compute.addresses.delete` for deleting static IP addresses on permanent instance deletion
  * `compute.subnetworks.use` for creating static external IP addresses
  * `compute.subnetworks.useInternal` for creating static internal IP addresses
  * [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role to either the whole host project or select subnets of its Shared VPC networks for creating VM instances with static IP addresses in Shared VPC networks or subnets that belong to the host project



###  gcloud 

To create an instance with a predefined static IP address, use the [`gcloud compute instance-groups managed create-instance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create-instance) with one or multiple of the following flags:

  * `--stateful-internal-ip` to set a static internal IP address of a given network interface.
  * `--stateful-external-ip` to set a static external IP address of a given network interface.


    
    
    gcloud compute instance-groups managed create-instance INSTANCE_GROUP_NAME \
        --instance INSTANCE_NAME \
        --stateful-internal-ip address=ADDRESS[,interface-name=NI_NAME][,auto-delete=DELETE_RULE] \
        --stateful-external-ip address=ADDRESS[,interface-name=NI_NAME][,auto-delete=DELETE_RULE]
    

Replace the following:

  * INSTANCE_GROUP_NAME: The name of the MIG.
  * INSTANCE_NAME: The name of the instance to create.
  * NI_NAME: (Optional.) Network interface name. If not provided, the primary network interface named `nic0` is assumed by default. If you've multiple network interfaces, you can specify this flag for each IP in each network interface.
  * ADDRESS: (Required.) Static IP address to assign to the instance in one of the following formats:

    * Address. URL of a static IP address reservation–for example: `"projects/example-project/regions/us-east1/addresses/example-ip-name"`.
    * Literal–for example: `"130.211.181.55"`. 
      * If the provided IP address is not yet reserved, the MIG automatically creates a corresponding IP address reservation.
      * If the provided IP address is reserved, the MIG assigns the reservation to the instance.
  * DELETE_RULE: (Optional.) Prescribes what should happen to an associated static [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource when a VM instance is permanently deleted. The available options are as follows:

    * `never`: (Default.) Never delete the static IP address. Instead, unassign the address on instance deletion and keep the address reserved.
    * `on-permanent-instance-deletion`: Delete the static IP address reservation when an instance is permanently deleted from the instance group–for example, when you delete an instance manually or decrease the group's size.

Regardless of the value of the delete rule, the group always preserves stateful IP addresses on instance autohealing, update, and recreation operations.




**Example**

You need to add one more VM instance to your proxy server cluster, running on a MIG named `proxy-cluster`. You have created a static internal IP address [reservation](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) named `proxy-node-03-ip` and need to assign it to the new node. You want to keep the IP address reservation even if you decide to delete the node in the future.

Run the following command to create the node:
    
    
    gcloud compute instance-groups managed create-instance proxy-cluster \
        --instance proxy-node-03 \
        --stateful-internal-ip address="projects/example-project/regions/us-east1/addresses/proxy-node-03-ip",auto-delete=never
    

The command creates an instance named `proxy-node-03`, assigns the provided static internal IP address named `proxy-node-03-ip` to the instance, and stores stateful configuration for the IP in the corresponding [per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs). Because the `auto-delete` flag is set to `never`, the IP remains reserved if you delete the instance later.

###  Terraform 

To create a VM with a predefined static IP address, use one or multiple of the following blocks:

  * `preserved_state.internal_ip` to mark an internal IP address of a given network interface as stateful.
  * `preserved_state.external_ip` to mark an external IP address of a given network interface as stateful.



The following sample configures static IP addresses on VM creation in a regional MIG. For more information about the resource used in the sample, see [`google_compute_region_per_instance_config` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_per_instance_config). For a zonal MIG, use the [`google_compute_per_instance_config` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_per_instance_config).
    
    
    resource "google_compute_region_per_instance_config" "default" {
      region_instance_group_manager = google_compute_region_instance_group_manager.default.name
      region                        = google_compute_region_instance_group_manager.default.region
      name                          = "proxy-node-03-ip"
      preserved_state {
        internal_ip {
          interface_name = "nic0"
          auto_delete    = "NEVER"
          ip_address {
            address = google_compute_address.default.id
          }
        }
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create one or multiple instances in a MIG, set custom instance names, and assign predefined static IP addresses to these instances, use the [`instanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/createInstances) or [`regionInstanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/createInstances) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/createInstances
    
    {
      "instances": [
        {
          "name": "INSTANCE_NAME",
          "preservedState" : {
            "internalIPs": {
              "NI_NAME" : {
                "ipAddress": {
                  "address": "ADDRESS",
                  "literal": "LITERAL"
                },
                "autoDelete": "DELETE_RULE"
              },
              ...
            },
            "externalIPs": {
              "NI_NAME" : {
                "ipAddress": {
                  "address": "ADDRESS",
                  "literal": "LITERAL"
                },
                "autoDelete": "DELETE_RULE"
              },
              ...
            },
            ...
          }
        },
        ...
      ]
    }
    

Replace the following:

  * PROJECT_ID: The project ID for the request.
  * NAME: The name of the MIG.
  * REGION: For regional MIGs, the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the group is located. For zonal MIGs, replace `regions/REGION` with `zones/ZONE` and specify the zone where the MIG is located.
  * INSTANCE_NAME: The name of the instance to create.
  * NI_NAME: (Required.) Network interface name. The primary network interface is named `nic0`. If you have multiple network interfaces, you can specify multiple NI_NAMES.
  * ADDRESS: (Optional.) Static IP address to assign to the instance in the format of a URL of a static IP address reservation–for example: `"projects/example-project/regions/us-east1/addresses/example-ip-name"`. You must and can only set one field at a time, either `address` or `literal`, when assigning a static IP address.
  * LITERAL: (Optional.) Static IP address to assign to the instance in the literal format–for example: `"130.211.181.55"`. You must and can only set one field at a time, either `address` or `literal`, when assigning a static IP address. 
    * If the provided literal IP address is not yet reserved, the MIG automatically creates a corresponding IP address reservation.
    * If the provided literal IP address is reserved, the MIG assigns the reservation to the instance.
  * DELETE_RULE: (Optional.) Prescribes what should happen to an associated static [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource when a VM instance is permanently deleted. The available options are as follows:

    * `NEVER`: (Default.) Never delete the static IP address. Instead, unassign the address on instance deletion and keep the address reserved.
    * `ON_PERMANENT_INSTANCE_DELETION`: Delete the static IP address reservation when an instance is permanently deleted from the instance group–for example, when you delete an instance manually or decrease the group's size.

Regardless of the value of the delete rule, the group always preserves stateful IP addresses on instance autohealing, update, and recreation operations.




**Example**

You need to add one more VM instance to your proxy server cluster, running on a MIG named `proxy-cluster`. You have created a static internal IP address [reservation](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) named `proxy-node-03-ip` and need to assign it to the new node. You want to keep the IP address reservation even if you decide to delete the node in the future.

Call the `regionInstanceGroupManagers.createInstances` method to create an additional instance:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers/proxy-cluster/createInstances
    
    {
      "instances": [
        {
          "name": "proxy-node-03",
          "preservedState" : {
            "internalIPs": {
              "nic0" : {
                "ipAddress": {
                  "address": "projects/example-project/regions/us-east1/addresses/proxy-node-03-ip"
                },
                "autoDelete": "NEVER"
              }
            }
          }
        }
      ]
    }
    

The method creates an instance named `proxy-node-03`, assigns the provided static internal IP address named `proxy-node-03-ip` to the instance, and stores stateful configuration for the IP in the corresponding [per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs). Because the `autoDelete` field is set to `NEVER`, the IP remains reserved if you delete the instance later.

### Configuring static IP addresses for an existing VM in a MIG

You can set a predefined static IP address or update the stateful IP configuration for a managed instance individually–for example:

  * Assign a static IP address to an existing instance in a MIG. For static external IPs, this operation requires instance refresh, and for static internal IPs, this requires instance recreation.
  * Update the deletion rule for an already assigned static IP address. This operation can be done without disrupting the running instance.



For an existing instance without an external IP address, for which you configure an external stateful IP, the MIG adds [access configuration](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign) to the corresponding network interface with the following default values:
    
    
    "accessConfigs": [
      {
        "kind": "compute#accessConfig",
        "name": "External Nat",
        "natIP": "XX.XX.XX.XX",
        "networkTier": "PREMIUM",
        "type": "ONE_TO_ONE_NAT"
      }
    ]
    

**Note:** If you need to promote ephemeral IP addresses to static IP addresses for all instances in an existing MIG, configure the corresponding IP addresses to be stateful for the entire MIG in a stateful policy. The group will then promote the ephemeral IP addresses to static for all instances.  
  
If you need to promote the ephemeral IP address of an individual instance in an existing MIG, specify the literal value of the ephemeral IP address (e.g. "130.211.181.55").

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the[`instanceGroupManagers.updatePerInstanceConfigs`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/updatePerInstanceConfigs) method
  * For regional MIGs, all permissions required to call the[`regionInstanceGroupManagers.updatePerInstanceConfigs`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/updatePerInstanceConfigs) method



A MIG uses the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) service account to manage its instances. This service account has [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role by default, which includes all necessary permissions for managing stateful IP addresses.

If you need to create a custom role, the following permissions are required for managing stateful network interfaces:

  * `compute.addresses.create` for creating static external IP addresses
  * `compute.addresses.createInternal` for creating static internal IP addresses
  * `compute.addresses.use` for assigning a static external IP address to an instance
  * `compute.addresses.useInternal` for assigning a static internal IP address to an instance
  * `compute.addresses.delete` for deleting static IP addresses on permanent instance deletion
  * `compute.subnetworks.use` for creating static external IP addresses
  * `compute.subnetworks.useInternal` for creating static internal IP addresses
  * [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role to either the whole host project or select subnets of its Shared VPC networks for creating VM instances with static IP addresses in Shared VPC networks or subnets that belong to the host project



###  gcloud 

To configure a stateful IP address individually for a VM instance in a MIG, add or update stateful IP configuration in the associated per-instance configuration.

If a per-instance configuration doesn't yet exist for the instance, use the [`gcloud compute instance-groups managed instance-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/create) with one or multiple of the following flags:

  * `--stateful-internal-ip` to set a static internal IP address of a given network interface.
  * `--stateful-external-ip` to set a static external IP address of a given network interface.


    
    
    gcloud compute instance-groups managed instance-configs create INSTANCE_GROUP_NAME \
        --instance INSTANCE_NAME \
        --stateful-internal-ip address=ADDRESS[,interface-name=NI_NAME][,auto-delete=DELETE_RULE] \
        --stateful-external-ip address=ADDRESS[,interface-name=NI_NAME][,auto-delete=DELETE_RULE] \
        [--no-update-instance | --update-instance]
        [--instance-update-minimal-action MINIMAL_ACTION]
    

If a per-instance configuration already exists for the instance, use the [`gcloud compute instance-groups managed instance-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/update) with one or multiple `--stateful-internal-ip` or `--stateful-external-ip` flags:
    
    
    gcloud compute instance-groups managed instance-configs update INSTANCE_GROUP_NAME \
        --instance INSTANCE_NAME \
        --stateful-internal-ip address=ADDRESS[,interface-name=NI_NAME][,auto-delete=DELETE_RULE] \
        --stateful-external-ip address=ADDRESS[,interface-name=NI_NAME][,auto-delete=DELETE_RULE] \
        [--no-update-instance | --update-instance]
        [--instance-update-minimal-action MINIMAL_ACTION]
    

Replace the following:

  * INSTANCE_GROUP_NAME: The name of the MIG.
  * INSTANCE_NAME: The name of the instance for which to configure stateful IP addresses.
  * NI_NAME: (Optional.) Network interface name. If not provided, the primary network interface named `nic0` is assumed by default. If you've multiple network interfaces, you can specify this flag for each IP in each network interface.
  * ADDRESS: Static IP address to assign to the instance in one of the following formats: 
    * Address. URL of a static IP address reservation–for example: `"projects/example-project/regions/us-east1/addresses/example-ip-name"`.
    * Literal. For example: `"130.211.181.55"`. 
      * If the provided IP address is not yet reserved, the MIG automatically creates a corresponding IP address reservation.
      * If the provided IP address is reserved, the MIG assigns the reservation to the instance.
    * This subflag is optional if the address is already defined in the instance's per-instance configuration. Otherwise it is required.
    * If omitted, the configured address remains unchanged.
  * DELETE_RULE: (Optional.) Prescribes what should happen to an associated static [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource when a VM instance is permanently deleted. The available options are as follows:

    * `never`: (Default.) Never delete the static IP address. Instead, unassign the address on instance deletion and keep the address reserved.
    * `on-permanent-instance-deletion`: Delete the static IP address reservation when an instance is permanently deleted from the instance group–for example, when you delete an instance manually or decrease the group's size.
    * If omitted, the default value is set for a new stateful IP configuration; the value remains unchanged in an existing configuration.

Regardless of the value of the delete rule, the group always preserves stateful IP addresses on instance autohealing, update, and recreation operations.

  * `--update-instance`: (Optional. Default.) Apply the changes immediately to the instance. If you use the `--no-update-instance` flag, the changes remain unapplied and will be [applied](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) when you recreate or apply the update to the instance later.

  * MINIMAL_ACTION: (Optional.) Perform at least the specified action when applying per-instance configuration update to the instance. Must be used together with `--update-instance` flag. The value must be one of the following:

    * `none`: No action.
    * `refresh`: Apply updates that are possible to apply without stopping the instance.
    * `restart`: Stop the instance and then start it again.
    * `replace`: Recreate the instance.



If omitted, the least disruptive action required by the update is used.

**Example**

You have a file server instance called `file-server`, which is a single instance in a stateful MIG called `fs-group`. The group has a corresponding per-instance configuration, where a stateful data disk is configured. The file server has only been accessible internally, but now you have users who need to access it externally through a static IP address. You have reserved the static external IP by creating `file-server-ip` address reservation. Now you need to assign this IP to the file server instance.

Run the following command to configure the stateful external IP for the file server instance:
    
    
    gcloud compute instance-groups managed instance-configs update fs-group \
        --instance file-server \
        --stateful-external-ip interface-name=nic0,address="projects/example-project/regions/us-east1/addresses/file-server-ip",auto-delete=never \
        --update-instance
    

The command does the following:

  1. Updates the per-instance configuration for the `file-server` instance: 
     1. Adds stateful external IP configuration, pointing to the `file-server-ip` address reservation.
     2. Keeps the existing stateful data disk configuration unchanged.
  2. Applies the per-instance configuration update to the `file-server` instance immediately because the `--update-instance` flag is included: refreshes the instance and assigns the static external IP address from `file-server-ip` reservation.



###  REST 

To configure stateful IPs individually for VM instances in a MIG, add or update the stateful IP configuration in the associated per-instance configurations.

If per-instance configurations don't yet exist for the given instances, use the [`instanceGroupManagers.updatePerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/updatePerInstanceConfigs) or [`regionInstanceGroupManagers.updatePerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/updatePerInstanceConfigs) with stateful configuration for one or multiple IP addresses:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/updatePerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "INSTANCE_NAME",
          "preservedState" : {
            "internalIPs": {
              "NI_NAME" : {
                "ipAddress": {
                  "address": "ADDRESS",
                  "literal": "LITERAL"
                },
                "autoDelete": "DELETE_RULE"
              },
              ...
            },
            "externalIPs": {
              "NI_NAME" : {
                "ipAddress": {
                  "address": "ADDRESS",
                  "literal": "LITERAL"
                },
                "autoDelete": "DELETE_RULE"
              },
              ...
            },
            ...
          },
          "fingerprint: "FINGERPRINT"
        },
        ...
      ]
    }
    

**Note:** While you can use the `updatePerInstanceConfigs` method for updating existing per-instance configurations, this method fully replaces the specified per-instance configurations with new values. We recommend you use the `patchPerInstanceConfigs` method to update existing per-instance configurations, as patching keeps the omitted configuration unchanged and prevents the risk of accidental deletion of stateful items or reset of any values to defaults.

If per-instance configurations already exist for the given instances, use the [`instanceGroupManagers.patchPerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patchPerInstanceConfigs) or [`regionInstanceGroupManagers.patchPerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patchPerInstanceConfigs) with stateful configuration for one or multiple IP addresses:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/patchPerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "INSTANCE_NAME",
          "preservedState" : {
            "internalIPs": {
              "NI_NAME" : {
                "ipAddress": {
                  "address": "ADDRESS",
                  "literal": "LITERAL"
                },
                "autoDelete": "DELETE_RULE"
              },
              ...
            },
            "externalIPs": {
              "NI_NAME" : {
                "ipAddress": {
                  "address": "ADDRESS",
                  "literal": "LITERAL"
                },
                "autoDelete": "DELETE_RULE"
              },
              ...
            },
            ...
          },
          "fingerprint: "FINGERPRINT"
        },
        ...
      ]
    }
    

Replace the following:

  * PROJECT_ID: The project ID for the request.
  * NAME: The name of the MIG.
  * REGION: For regional MIGs, the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the group is located. For zonal MIGs, replace `regions/REGION` with `zones/ZONE` and specify the zone where the MIG is located.
  * INSTANCE_NAME: (Required.) The name of the instance for which to configure stateful IPs.
  * NI_NAME: (Required.) Network interface name. The primary network interface is named `nic0`. If you have multiple network interfaces, you can specify multiple NI_NAMES.
  * ADDRESS: (Optional.) Static IP address to assign to the instance in the format of a URL of a static IP address reservation–for example: `"projects/example-project/regions/us-east1/addresses/example-ip-name"`. You must and can only set one field at a time, either address or literal, when assigning a static IP address.
  * LITERAL: (Optional.) Static IP address to assign to the instance in the literal format. For example: `"130.211.181.55"`. You must and can only set one field at a time, either address or literal, when assigning a static IP address. 
    * If the provided literal IP address is not yet reserved, the MIG automatically creates a corresponding IP address reservation.
    * If the provided literal IP address is reserved, the MIG assigns the reservation to the instance.
  * DELETE_RULE: (Optional.) Prescribes what should happen to an associated static [Address](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resource when a VM instance is permanently deleted. The available options are as follows:

    * `NEVER`: (Default.) Never delete the static IP address. Instead, unassign the address on instance deletion and keep the address reserved.
    * `ON_PERMANENT_INSTANCE_DELETION`: Delete the static IP address reservation when an instance is permanently deleted from the instance group–for example, when you delete an instance manually or decrease the group's size.
    * If omitted, the default value is set for a new stateful IP configuration; the value remains unchanged in an existing configuration.

Regardless of the value of the delete rule, the group always preserves stateful IP addresses on instance autohealing, update, and recreation operations.

  * FINGERPRINT: (Optional.) The fingerprint for the given configuration if it already exists. Used for optimistic locking. The operation fails if the fingerprint is different than provided, as it indicates that the per-instance configuration was changed since it was last read. To see the latest fingerprint, see the output of the `listPerInstanceConfigs` method for a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listPerInstanceConfigs) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listPerInstanceConfigs) MIG. If `fingerprint` is omitted, the operation proceeds without fingerprint comparison.




The `updatePerInstanceConfigs` and `patchPerInstanceConfigs` methods update the specified per-instance configurations but don't apply the configuration updates to the associated managed instances. The changes are applied to an instance when the MIG is instructed to recreate or update the instance. You can [apply the update manually](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig#updating_selected_instances) to apply the changes to an instance.

**Example**

You have a file server instance called `file-server`, which is a single instance in a stateful MIG called `fs-group`. The group has a corresponding per-instance configuration, where a stateful data disk is configured. The file server has only been accessible internally, but now you have users who need to access it externally through a static IP address. You have reserved the static external IP by creating `file-server-ip` address reservation. Now you need to assign this IP to the file server instance.

To update the per-instance configuration for `file-server` with the new stateful external IP, call the `patchPerInstanceConfigs` method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers/fs-group/patchPerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "file-server",
          "preservedState" : {
            "externalIPs": {
              "nic0" : {
                "ipAddress": {
                  "address": "projects/example-project/regions/us-east1/addresses/file-server-ip"
                },
                "autoDelete": "NEVER"
              }
            }
          }
        }
      ]
    }
    

The method patches the per-instance configuration for `file-server` instance:

  1. Adds stateful external IP configuration, pointing to the `file-server-ip` address reservation.
  2. Keeps the existing stateful data disk configuration unchanged.



The configuration update is not yet applied to the `file-server` VM instance. The MIG will apply the configuration update when you recreate or apply the update to the instance later.

To apply the per-instance configuration update to `file-server` VM instance, call the [`regionInstanceGroupManagers.applyUpdatesToInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/applyUpdatesToInstances) for the instance:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers/gs-group/applyUpdatesToInstances
    
    {
      "instances": ["/zones/us-east1-b/instances/file-server"]
    }
    

The method assigns the configured static external IP address from `file-server-ip` reservation to the managed instance. The method refreshes the `file-server` instance to assign an external IP address.

Because `autoDelete` is set to `NEVER` in the stateful IP configuration, the IP will remain reserved if you delete the instance later.

### Disassociating static IP addresses from an existing VM in a MIG

You might need to disassociate a static IP address from an existing VM, making the network interface ephemeral for the VM. This is useful in the following scenarios:

  * You rearchitect your app to no longer rely on static IP addresses.
  * You configured the IP to be stateful by mistake and would like to revert it.



You can disassociate a static IP address from an existing VM in MIG and make the IP address ephemeral for an individual VM by removing the IP's stateful configuration from the associated per-instance configuration or [deleting the entire per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#removing_stateful_configuration_for_a_specific_vm) if it doesn't contain any other state. [Applying](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) the change has the following effects:

  * The IP address remains active on the instance, but is no longer stateful.
  * When you recreate or update the instance, or when the instance is autohealed, the MIG [unassigns](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip) the associated static IP address reservation and auto-assigns an ephemeral address.
  * After having been unassigned, the static IP address remains reserved.

**Note:** If stateful IP configuration for the same network interface is present in the group's stateful policy, the IP address remains stateful for the instance even if you remove its configuration from the per-instance configuration. In such a case, you should also remove the IP addresses configuration from the stateful policy to make the IP ephemeral.

Removing a stateful IP configuration from a per-instance configuration does not disrupt running VM instances, unless you explicitly choose to do so.

To learn more, see the following documents:

  * [How removing stateful IP configuration from per-instance configurations affects preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#removing_ip_from_pic).
  * [Applying per-instance configurations updates](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs).



#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the[`instanceGroupManagers.patchPerInstanceConfigs`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patchPerInstanceConfigs) method
  * For regional MIGs, all permissions required to call the[`regionInstanceGroupManagers.patchPerInstanceConfigs`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patchPerInstanceConfigs) method



A MIG uses the [Google APIs Service Agent](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) service account to manage its instances. This service account has [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role by default, which includes all necessary permissions for managing stateful IP addresses.

If you need to create a custom role, the following permissions are required for managing stateful network interfaces:

  * `compute.addresses.create` for creating static external IP addresses
  * `compute.addresses.createInternal` for creating static internal IP addresses
  * `compute.addresses.use` for assigning a static external IP address to an instance
  * `compute.addresses.useInternal` for assigning a static internal IP address to an instance
  * `compute.addresses.delete` for deleting static IP addresses on permanent instance deletion
  * `compute.subnetworks.use` for creating static external IP addresses
  * `compute.subnetworks.useInternal` for creating static internal IP addresses
  * [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role to either the whole host project or select subnets of its Shared VPC networks for creating VM instances with static IP addresses in Shared VPC networks or subnets that belong to the host project



###  gcloud 

To remove a stateful IP configuration from the associated per-instance configuration, use the [`gcloud compute instance-groups managed instance-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/update) with the `--remove-stateful-internal-ips` or `--remove-stateful-external-ips` flags:
    
    
    gcloud compute instance-groups managed instance-configs update INSTANCE_GROUP_NAME \
        --instance INSTANCE_NAME \
        --remove-stateful-internal-ips NI_NAME[,NI_NAME,...] \
        --remove-stateful-external-ips NI_NAME[,NI_NAME,...]
        [--no-update-instance | --update-instance] \
        [--instance-update-minimal-action MINIMAL_ACTION]
    

Replace the following:

  * INSTANCE_GROUP_NAME: The name of the MIG.
  * INSTANCE_NAME: (Required.) The name of the instance for which to remove stateful IP configuration.
  * NI_NAME: (Required.) Network interface name. The primary network interface is named `nic0`. If you've multiple network interfaces, you can specify multiple NI_NAMES.
  * `--update-instance`: (Optional. Default.) Apply the changes immediately to the instance. If you use the `--no-update-instance` flag, the changes remain unapplied and will be [applied](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) when you recreate or apply the update to the instance later.
  * MINIMAL_ACTION: (Optional.) Perform at least the specified action when applying per-instance configuration update to the instance. This flag can only be used together with `--update-instance` flag. The value must be one of the following:

    * `none`: No action.
    * `refresh`: Apply updates that are possible to apply without stopping the instance.
    * `restart`: Stop the instance and then start it again.
    * `replace`: Recreate the instance.

If omitted, the least disruptive action required by the update is used.




**Example**

Your application has been exposed to users through specific published static external IP addresses of the VM instances in a MIG called `example-group`. You have rearchitected your service by deploying a load balancer in front of the MIG and routing the traffic to the managed VMs through it. You no longer need to maintain the static external IP addresses and would like to make the external IP addresses of the VMs ephemeral.

To make the stateful external IP addresses of the VMs in a MIG ephemeral, run the following command for each instance, for example, for `node-1`:
    
    
    gcloud compute instance-groups managed instance-configs update example-group \
        --instance node-1 \
        --remove-stateful-external-ips nic0 \
        --update-instance
    

The command does the following:

  1. Removes stateful configuration for the external IP address within the `nic0` network interface from the per-instance configuration for `node-1`.
  2. Applies the per-instance configuration update to `node-1` VM instance immediately because the `--update-instance` flag is included. The VM instance is not disrupted and keeps serving from the same IP, which is no longer stateful. The MIG removes the reference to static IP reservation from the managed instance's `preservedStateFromConfig` and treats the external IP address as ephemeral. The MIG will auto-assign an external IP on subsequent instance recreation, update, or autohealing events.
  3. After having been [unassigned](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip), the original static IP remains reserved. You can [release](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) the IP if you no longer need it.



###  REST 

To remove a stateful IP configuration from the associated per-instance configuration, use the [`instanceGroupManagers.patchPerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patchPerInstanceConfigs) or [`regionInstanceGroupManagers.patchPerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patchPerInstanceConfigs):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/patchPerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "INSTANCE_NAME",
          "preservedState" : {
            "internalIPs": {
              "NI_NAME" : null
            },
            "externalIPs": {
              "NI_NAME" : null
            }
          },
          "fingerprint: "FINGERPRINT"
        },
        ...
      ]
    }
    

Replace the following:

  * PROJECT_ID: The project ID for the request.
  * NAME: The name of the MIG.
  * REGION: For regional MIGs, the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the group is located. For zonal MIGs, replace `regions/REGION` with `zones/ZONE` and specify the zone where the MIG is located.
  * INSTANCE_NAME: (Required.) The name of the instance for which to remove stateful IP configuration.
  * NI_NAME: (Required.) Network interface name. The primary network interface is named `nic0`. If you have multiple network interfaces, you can specify multiple NI_NAMES.
  * FINGERPRINT: (Optional.) The fingerprint for the given configuration if it already exists. Used for optimistic locking. The operation fails if the fingerprint is different than provided, as it indicates that the per-instance configuration was changed since it was last read. To see the latest fingerprint, see the output of the `listPerInstanceConfigs` method for a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listPerInstanceConfigs) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listPerInstanceConfigs) MIG. If `fingerprint` is omitted, the operation proceeds without fingerprint comparison.



The `patchPerInstanceConfigs` method updates the specified per-instance configurations but does not apply the configuration updates to the associated managed instances. The changes are applied to an instance when the MIG is instructed to recreate or update the instance. You can [apply the update manually](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#updating_selected_instances) to apply the changes to an instance.

**Example**

Your application has been exposed to users through specific published static external IP addresses of the VM instances in a MIG called `example-group`. You have rearchitected your service by deploying a load balancer in front of the MIG and routing the traffic to the managed VMs through it. You no longer need to maintain the static external IP addresses and would like to make the external IP addresses of the VMs ephemeral.

To make the stateful external IP addresses of the VMs in a MIG ephemeral, run the following method for each instance, for example, for `node-1`, and provide `null` value to the network interface's stateful configuration:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers/example-group/patchPerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "node-1",
          "preservedState" : {
            "externalIPs": {
              "nic0" : null
            }
          }
        }
      ]
    }
    

The method removes configuration for the stateful IP address within `nic0` network interface from the per-instance configuration for `node-1`. The configuration update is not yet applied to the `node-1` VM instance. The MIG applies the configuration update on the next instance recreation or update.

To apply the per-instance configuration update to the `node-1` VM instance, run the [`regionInstanceGroupManagers.applyUpdatesToInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/applyUpdatesToInstances) for the instance:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-east1/instanceGroupManagers/example-group/applyUpdatesToInstances
    
    {
      "instances": ["/zones/us-east1-c/instances/node-1"]
    }
    

The MIG removes the reference to static IP reservation from the `preservedStateFromConfig` field for the `node-1` instance and treats the IP address as ephemeral. The MIG will auto-assign an external IP on subsequent instance recreation, update, or autohealing events.

After having been [unassigned](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#unassign_ip), the original static IP remains reserved. You can [release](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip) the IP if you no longer need it.

## Removing stateful configuration

To remove configuration from a stateful policy for all VMs in a MIG, see the following documents:

  * To only remove stateful IP addresses, see Declaring previously stateful IP addresses as stateless.
  * To remove all stateful configuration from a stateful policy, see [Removing a stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#removing_a_stateful_policy).



To remove configuration from a per-instance configuration for a specific VM in a MIG, see the following documents:

  * To only remove stateful IP addresses, see Disassociating a static IP address from an existing VM in a MIG.
  * To remove all stateful configuration from a per-instance configuration, see [Removing stateful configuration for a specific VM](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#removing_stateful_configuration_for_a_specific_vm).



### Cleaning up unused static IP addresses

When configuring stateful IP address for managed instances in a group, you can choose whether to release the associated static IP address reservations manually or automatically when an instance is [permanently deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group):

  * To release static IP address reservations automatically on permanent instance deletion, set the `autoDelete` parameter to `ON_PERMANENT_INSTANCE_DELETION`.
  * To release static IP address reservations manually, set the `autoDelete` parameter to `NEVER`. To clean up unused static IP address reservations, for example, in order to avoid unnecessary [charges](https://docs.cloud.google.com/vpc/network-pricing#ipaddress), see the following documents: 
    * [Delete a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#delete_a_static_internal_ip_address)
    * [Release a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip)



If you have instructed the MIG to never delete the associated IP reservations, the static IP addresses remain reserved after the corresponding instances or the MIG ceases to exist.

## Feedback

We want to learn about your use cases, challenges, and feedback about stateful MIGs. You can share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

## What's next

  * Learn about [applying, viewing, and removing](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs) stateful configuration.
  * [Get info](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about a specific MIG and its managed instances, including VM status and properties.
  * Learn more about [working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
