---
url: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape/
title: Set a target distribution shape for VMs in a regional MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:41.477446+00:00
---

# Set a target distribution shape for VMs in a regional MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set a target distribution shape for VMs in a regional MIG Stay organized with collections  Save and categorize content based on your preferences. 

If you use a [regional managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs), you can set that MIG's [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape) to one of the following options:

  * **EVEN** (default): the group creates and deletes VMs to achieve and maintain the same number of VMs across the selected zones. In an `EVEN` distribution, the number of VMs does not differ by more than 1 between any two zones. Recommended for highly available serving workloads. 
  * **BALANCED** : the group prioritizes creation of VMs in zones where resources are available, while distributing VMs as evenly as possible across selected zones to minimize the impact of zonal failure. Recommended for highly available serving or batch workloads. 
  * **ANY** : the group picks zones for creating VM instances to fulfill the requested number of VMs within present resource constraints and to maximize utilization of unused zonal reservations. Recommended for batch workloads that do not require high availability. 
  * **ANY SINGLE ZONE** : the group creates all VM instances within a single zone. The zone is chosen based on hardware support, current resource and quota availability, and matching reservations. Recommended in combination with a [ compact instance placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) for workloads that require extensive communication between VMs. 



To use reserved VMs in a regional managed instance group, create identical reservations with the same name in each applicable zone. Then, target those reservations by name in the group's instance template.

To help you choose a shape, see the [comparison table](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#comparison_of_shapes), [use cases](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#use_cases), and [how distribution shapes work](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#how_it_works).

Set a target distribution shape when creating your regional MIG or update the target shape of an existing regional MIG.

## Before you begin

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

  * You can only select zones for your MIG when you create the MIG.
  * If you specify resources in your MIG's instance template or stateful configuration that are not available in all selected zones, the following limitations apply:

    * You must set the [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#target_distribution_shape) to `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`.
    * You must ensure that any resources required by the MIG–for example, existing disks, machine types, or GPUs–are available in at least one of the selected zones.
    * If you want to update the [MIG's configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#configuration_components_for_vms_in_a_mig) (for example, instance template) to a configuration that cannot be instantiated in all selected zones, you must [remove managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from all unsupported zones before setting the new configuration.
  * To set the target distribution shape to `BALANCED` or `ANY_SINGLE_ZONE`, you must disable [proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution).

  * If you set the target distribution shape to `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`, the following limitations apply:

    * [Canary](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#canary_updates) updates with two [versions](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#relationship_between_versions_and_instancetemplate_fields) are not supported.
    * In case of limited availability of requested resources in the whole region, the group might schedule VM instance creation in a zone where the resources are already unavailable. You can try decreasing and increasing group size to get the requested resources in other zones.
    * Rolling updates that use the `SUBSTITUTE` [replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#replacement_method) will try to create the new updated instances in the same zone as the outdated machines, even if the zone doesn't have resources to accommodate the requirements of the new version. To mediate this behavior, you can delete the outdated VMs from the constrained zone, then increase the group size by the number of the deleted VMs. The group creates instances from the latest template in zones where capacity is available.
    * If you want to update the group's instance template to a template that specifies resources that are not available in all selected zones, you must [remove](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) managed instances from unsupported zones before setting the new template.
  * If you set the target distribution shape to `ANY_SINGLE_ZONE` and the group has existing VMs in a single zone, you can create additional VMs in that zone only. If you want to use a different zone, you must first scale in the group to zero VMs.

  * If you need to [provision a group of sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#provision_a_group_of_sole-tenant_vms), you must set the MIG's target distribution shape to `EVEN`. Create your node groups in the same zones as the MIG's zones and set the MIG's node affinities in the MIG's instance template.

**Warning:** If you set the target distribution shape to `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`, the MIG might create VMs outside of your sole-tenant nodes.



## Creating a group with a target distribution shape

To create your group, select its zones, and set its target distribution shape, use the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create), Terraform, or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers/insert).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups/)

  2. Click **Create instance group** to create a new instance group.
  3. Select one of the **New managed instance group options** : stateless (default) or [stateful](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).
  4. Assign a name and optionally a description to your instance group.
  5. Choose an instance template for the instance group or create a new one.
  6. Specify the number of VMs for this group. For highly available workloads, remember to [provision](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision) enough VMs to support your application if a zone failure happens.
  7. Under **Location** , select **Multiple zones**.
  8. Choose a region and select the zones you want to use.

     * If you want your MIG to be able to use all zones in the region, select all available zones.
     * Note that you cannot update a regional MIG to use different zones after it is created.
  9. Choose a target distribution shape.

If you select **Any single zone** or **Balanced** , then in the **Instance redistribution** section, don't select **Allow instance redistribution**.

  10. Continue with the rest of the MIG creation process.




###  gcloud 

Use the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) and include the `--target-distribution-shape` flag.
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --template TEMPLATE \
        --size SIZE \
        --region REGION \
        --zones ZONES \
        --target-distribution-shape SHAPE
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the instance group.
  * `TEMPLATE`: the name of the instance template to use for the group.
  * `SIZE`: the target size of the instance group.
  * `REGION`: the region where you want your group.
  * `ZONES` (optional): a list of zones in the region where you want to deploy VM instances. By default, Compute Engine selects three zones for you.

    * If you want your MIG to be able to use all zones in the region, specify all the available zones. You can get a list of zones in region with the following command:
          
          gcloud compute zones list --filter=region:REGION --format='list(NAME)'

    * Note that you cannot update a regional MIG to use different zones after it is created.

  * `SHAPE`: the target distribution shape. This can be one of the following values: 

    * `even` (default): the group creates and deletes VMs to achieve and maintain the same number of VMs across the selected zones. In an `EVEN` distribution, the number of VMs does not differ by more than 1 between any two zones. Recommended for highly available serving workloads. 
    * `balanced`: the group prioritizes creation of VMs in zones where resources are available, while distributing VMs as evenly as possible across selected zones to minimize the impact of zonal failure. Recommended for highly available serving or batch workloads. 
    * `any`: the group picks zones for creating VM instances to fulfill the requested number of VMs within present resource constraints and to maximize utilization of unused zonal reservations. Recommended for batch workloads that do not require high availability. 
    * `any-single-zone`: the group creates all VM instances within a single zone. The zone is chosen based on hardware support, current resource and quota availability, and matching reservations. Recommended in combination with a [ compact instance placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) for workloads that require extensive communication between VMs. 



For example, to create a regional MIG with a balanced target distribution shape, set the `--target-distribution-shape` flag to `balanced`.
    
    
    gcloud compute instance-groups managed create example-rmig \
        --template example-template \
        --size 30 \
        --zones us-east1-b,us-east1-c \
        --target-distribution-shape balanced \
        --instance-redistribution-type none
    

###  Terraform 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To create a regional MIG, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).

The following example creates a regional MIG with `BALANCED` target distribution shape.
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      name                             = "example-rmig"
      region                           = "us-east1"
      distribution_policy_zones        = ["us-east1-b", "us-east1-c"]
      distribution_policy_target_shape = "BALANCED"
      update_policy {
        type                         = "PROACTIVE"
        minimal_action               = "REFRESH"
        instance_redistribution_type = "NONE"
        max_unavailable_fixed        = 3
      }
      target_size        = 30
      base_instance_name = "instance"
      version {
        instance_template = google_compute_instance_template.default.id
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

Call the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert). In the request body, include the `distributionPolicy` property, and set its `targetShape` field.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
    
    {
        "name": INSTANCE_GROUP_NAME,
        "instanceTemplate": "global/instanceTemplates/TEMPLATE",
        "targetSize": SIZE,
        "distributionPolicy": {
            "zones": [
                {"zone": "zones/ZONE1"},
                {"zone": "zones/ZONE2"},
                {"zone": "zones/ZONE3"},
            ],
            "targetShape": "SHAPE"
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request.
  * `REGION`: the region for the instance group.
  * `INSTANCE_GROUP_NAME`: the name of the instance group.
  * `TEMPLATE`: the name of the instance template to use for the instance group.
  * `SIZE`: the target size of the instance group.
  * `ZONE`: the name of a zone in the region where you want to deploy VM instances. 
    * If you want your MIG to be able to use all zones in the region, specify all the available zones. You can get a list of zones in region by calling the [`regions.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regions/get).
    * Note that you cannot update a regional MIG to use different zones after it is created.
  * `SHAPE`: the target distribution shape. This can be one of the following values: 
    * `EVEN` (default): the group creates and deletes VMs to achieve and maintain the same number of VMs across the selected zones. In an `EVEN` distribution, the number of VMs does not differ by more than 1 between any two zones. Recommended for highly available serving workloads. 
    * `BALANCED`: the group prioritizes creation of VMs in zones where resources are available, while distributing VMs as evenly as possible across selected zones to minimize the impact of zonal failure. Recommended for highly available serving or batch workloads. 
    * `ANY`: the group picks zones for creating VM instances to fulfill the requested number of VMs within present resource constraints and to maximize utilization of unused zonal reservations. Recommended for batch workloads that do not require high availability. 
    * `ANY_SINGLE_ZONE`: the group creates all VM instances within a single zone. The zone is chosen based on hardware support, current resource and quota availability, and matching reservations. Recommended in combination with a [ compact instance placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) for workloads that require extensive communication between VMs. 



## Changing the target distribution shape of an existing group

You can change the [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#target_distribution_shape) in an existing regional MIG but with the following limitations:

  * If you want to change the target distribution shape to `BALANCED` or `ANY_SINGLE_ZONE`, you must first [disable proactive redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution).
  * If you want to change the target distribution shape to `EVEN` and if the current distribution of instances is uneven, you must first disable proactive redistribution.
  * If you change the shape to `EVEN` and you want to re-enable proactive redistribution, you must first [manually rebalance the group](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-rebalance-manually).
  * If you want to change the target distribution shape to `EVEN` but your instance template specifies resources that are not supported in all selected zones, you must first update the group's instance template to one that is supported in all selected zones.



#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups/)

  2. In the **Name** column of the list, click the name of the instance group where you want to change the target distribution shape.
  3. Click **Edit** to modify this managed instance group.
  4. Click **Location** to expand the section.
  5. In the **Target distribution shape** list, select the shape that you want.
  6. Click **Save** to apply the changes.



###  gcloud 

Use the [`gcloud compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) and include the `--target-distribution-shape` flag.
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        --target-distribution-shape SHAPE
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the instance group.
  * `SHAPE`: the target distribution shape. This can be one of the following values: 
    * `even` (default): the group creates and deletes VMs to achieve and maintain the same number of VMs across the selected zones. In an `EVEN` distribution, the number of VMs does not differ by more than 1 between any two zones. Recommended for highly available serving workloads. 
    * `balanced`: the group prioritizes creation of VMs in zones where resources are available, while distributing VMs as evenly as possible across selected zones to minimize the impact of zonal failure. Recommended for highly available serving or batch workloads. 
    * `any`: the group picks zones for creating VM instances to fulfill the requested number of VMs within present resource constraints and to maximize utilization of unused zonal reservations. Recommended for batch workloads that do not require high availability. 
    * `any-single-zone`: the group creates all VM instances within a single zone. The zone is chosen based on hardware support, current resource and quota availability, and matching reservations. Recommended in combination with a [ compact instance placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) for workloads that require extensive communication between VMs. 



###  REST 

Call the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch). In the request body, include the `distributionPolicy` property, and set its `targetShape` field.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
        "distributionPolicy": {
            "targetShape": "SHAPE"
        }
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request.
  * `REGION`: the region for the instance group.
  * `INSTANCE_GROUP_NAME`: the name of the instance group.
  * `SHAPE`: the target distribution shape. This can be one of the following values: 
    * `EVEN` (default): the group creates and deletes VMs to achieve and maintain the same number of VMs across the selected zones. In an `EVEN` distribution, the number of VMs does not differ by more than 1 between any two zones. Recommended for highly available serving workloads. 
    * `BALANCED`: the group prioritizes creation of VMs in zones where resources are available, while distributing VMs as evenly as possible across selected zones to minimize the impact of zonal failure. Recommended for highly available serving or batch workloads. 
    * `ANY`: the group picks zones for creating VM instances to fulfill the requested number of VMs within present resource constraints and to maximize utilization of unused zonal reservations. Recommended for batch workloads that do not require high availability. 
    * `ANY_SINGLE_ZONE`: the group creates all VM instances within a single zone. The zone is chosen based on hardware support, current resource and quota availability, and matching reservations. Recommended in combination with a [ compact instance placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) for workloads that require extensive communication between VMs. 



## Viewing the configured instance distribution policy

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.get` on the instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups/)

If you have existing instance groups, the page lists those groups.
  2. Click the name of the instance group that you want to examine. A page opens with the instance group properties and a list of instances that are included in the group.
  3. Click **Details**.
  4. In the **Location** section, look for **Target distribution shape**.



###  gcloud 

Run the [`gcloud compute instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe).
    
    
    gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME \
        --region REGION
    

The command returns the group's details, including the `distributionPolicy.targetShape` field:
    
    
    ...
    distributionPolicy:
      targetShape: BALANCED
      zones:
      - zone: https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f
      ...
    name: my-group
    region: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1
    ...
    

###  REST 

Construct a `GET` request to the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request
  * `REGION`: the region for the instance group
  * `INSTANCE_GROUP_NAME`: the name of the instance group



The target distribution shape is returned in the `distributionPolicy.targetShape` field. For example:
    
    
    {
      "name": "my-instance-group",
      "distributionPolicy": {
        "targetShape": "BALANCED",
      },
      "targetSize": 50,
      ...
    }
    

While the distribution policy shows your configured target shape, you can also view the runtime instance distribution across zones for a specific MIG or aggregated data across multiple MIGs. For instructions on how to view the instance distribution, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).

## What's next

  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).
  * Learn more about [Viewing info about MIGs and their VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs).
  * Learn about [Working with VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances), including adding, recreating, and removing VMs, and updating VM configuration.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
