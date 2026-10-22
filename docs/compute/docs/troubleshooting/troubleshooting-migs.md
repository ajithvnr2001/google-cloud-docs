---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-migs/
title: Troubleshooting managed instance groups \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:41.759992+00:00
---

# Troubleshooting managed instance groups  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting managed instance groups Stay organized with collections  Save and categorize content based on your preferences. 

There are several issues that can prevent a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) from successfully creating or recreating a VM instance.

## If logs are generated for a deleted MIG

The problem might be related to the following situations.

### Attached autoscaler still exists

If you [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig#delete_a_mig) a MIG using the Compute Engine API and you did not issue a separate request to delete the attached autoscaler, the Logs Explorer might show logs with the following message.
    
    
    The resource 'projects/PROJECT/zones/ZONE/instanceGroupManagers/DELETED_INSTANCE_GROUP_NAME' was not found.
    

**Resolution** :

To resolve this issue, delete the attached autoscaler using the Compute Engine API methods:

  * For an autoscaler of a zonal MIG, use the [`autoscalers.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/delete).
  * For an autoscaler of a regional MIG, use the [`regionAutoscalers.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/delete).



## If your MIG cannot create or recreate instances

The problem might be related to the following situations.

### The boot disk already exists

By default, a new boot persistent disk is created when you create an instance. The name of the boot disk matches the name of the VM. If you name a VM `my-instance`, the disk is also named `my-instance`. If a persistent disk already exists with that name, the request fails. To resolve this issue, you can optionally [take a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots), and then delete the existing persistent disk.

### The instance template is not valid

If you updated your instance template recently, there could be an invalid property that causes the MIG to fail VM creation. Examine the properties for these common errors:

  * You specified a resource that doesn't exist, such as a source image.
  * You misspelled a resource name.
  * You tried to attach an existing non-boot persistent disk in read/write mode but your group contains more than one VM. For groups with more than one VM, any additional disks you want to share between all of the VMs in the group can be attached only in read-only mode.



### Limit exceeded for resource type

The following error occurs when you try to create more than 2,000 VMs in a regional MIG or more than 1,000 VMs in a zonal MIG. You have reached the size limit for your instance group.

**Error message** :
    
    
    ERROR: (gcloud.compute.<INSTANCE_GROUP_TYPE>.<METHOD>) Could not
    fetch resource:
    
     - Exceeded limit 'MAX_INSTANCES_IN_INSTANCE_GROUP' on resource 'PROJECT_ID'.
     Limit: NUMBER

**Resolution** :

To resolve this issue, try one of the following:

  * If you are using a zonal MIG, use a [regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups#types_of_managed_instance_groups) instead.
  * Create multiple MIGs and split your workload across them—for example by adjusting your [load balancing](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer) configuration.
  * If you still need a bigger group, you can [increase the size limit of your MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_size_limit) or [contact support](https://cloud.google.com/support-hub) to make a request.



## If you cannot delete your MIG or its instances

The problem might be related to the following situation.

### Resource not found in zone or region

The following error occurs when you try to delete a regional MIG and you specify the `--zone` flag, specify no region, or specify the wrong region. A similar error can occur if you try to delete a zonal MIG and you specify the `--region` flag.

**Error message** :

  * ERROR: (gcloud.compute.instance-groups.managed.delete) Some requests did not succeed:
        ‐ The resource 'projects/PROJECT/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME' was not found
        

  * ERROR: (gcloud.compute.instance-groups.managed.delete) Some requests did not succeed:
        ‐ The resource 'projects/PROJECT/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME' was not found
        




**Resolution** :

To resolve this issue, try one of the following:

  * Append the appropriate `--region` or `--zone` flag to your command
  * [Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-region-zone)



### Resource is used by a backend service

You cannot remove an instance group when it is used by a load balancer's backend service. You must remove the instance from the backend service before you can delete the instance group.

**Error message** :

  * ERROR: (gcloud.compute.instance-groups.managed.delete) Some requests did not succeed:
        ‐ The instance_group_manager resource 'projects/PROJECT/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME is already being used by 'projects/PROJECT/global/backendServices/BACKEND_SERVICE

  * ERROR: (gcloud.compute.instance-groups.managed.delete) Some requests did not succeed:
        ‐ The instance_group_manager resource 'projects/PROJECT/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME is already being used by 'projects/PROJECT/global/backendServices/BACKEND_SERVICE




**Resolution** :

  1. Optional: Drain the backend instance group.

     * For [proxy load balancers only](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#lb-summary), you can set the [capacity scaler](https://docs.cloud.google.com/load-balancing/docs/backend-service#capacity_scaler) to `0.0` before removing the instance group from a backend service. You can set the capacity scaler to zero by using the [`gcloud compute backend-services edit` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit).

     * For both proxy and pass-through load balancers, if you [enable connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining) on the backend service, Google Cloud attempts to allow existing connections to persist, complete, and drain whenever an instance group is removed from a backend service.

  2. Remove the MIG from the regional or global backend service.

     * For a zonal MIG, run the following command:
           
           gcloud compute backend-services remove-backend BACKEND_SERVICE \
               --instance-group=INSTANCE_GROUP_NAME \
               --instance-group-zone=ZONE \
               [--region=REGION | --global]
           

     * For a regional MIG, run the following command:
           
           gcloud compute backend-services remove-backend BACKEND_SERVICE  \
               --instance-group=INSTANCE_GROUP_NAME \
               --instance-group-region=REGION \
               [--region=REGION | --global]
           

  3. Delete the MIG:
         
         gcloud compute instance-groups managed delete INSTANCE_GROUP_NAME
         




## If your MIG continually tries to recreate instances

The problem might be related to the following situation.

### Health check probes cannot reach the instance

If you configured an autohealing policy but you did not configure—or misconfigured—the firewall rule that lets the health check probes reach your application, then your VMs [appear unhealthy](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#checking_the_status), and the MIG continuously tries to recreate them. For information about how to configure a health check firewall rule, see [Example health check set up](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#example_health_check_set_up).

## If your MIG has uneven zonal distribution or uses unexpected machine types

If your [regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs) or [MIG with instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility) is operational but you suspect that instances are not distributed across zones as expected, or that the group is relying on fallback machine types, then you can monitor the actual distribution of your successfully provisioned instances.

You can view the runtime instance distribution for a specific MIG or aggregated data across multiple MIGs. Note that monitoring instance distribution provides observability into provisioned instances; it doesn't identify the underlying causes of creation failures or capacity constraints. For instructions on how to view the instance distribution, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).

## If stockout logs are missing or appear unexpectedly for a MIG with instance flexibility

If you don't see expected stockout logs in Cloud Logging, or if they appear unexpectedly for a MIG with instance flexibility, review the following behaviors:

  * **Skipped ranks don't log stockout errors** : Before a MIG creates VMs, it checks capacity across all instance selections. If higher-preference machine types are unavailable, then the MIG skips them and provisions instances by using available lower-preference options. Because Compute Engine logs `ZONE_RESOURCE_POOL_EXHAUSTED` errors only when a VM creation fails, you won't see stockout errors in Logging for higher-preference machine types that were skipped during capacity checks.

  * **VM repairs might log stockout errors for the original machine type** : If [update on repair](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair) is enabled, then a MIG attempts to recreate a failed VM by using its original machine type while checking availability for alternative machine types. As a result, you might see stockout errors for the original machine type even though the MIG is checking or using alternative machine types.




For more information, see [Capacity evaluation and error logging](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility#capacity_evaluation_and_error_logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
