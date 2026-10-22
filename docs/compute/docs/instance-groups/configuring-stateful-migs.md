---
url: https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs/
title: Configuring stateful MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:46.462804+00:00
---

# Configuring stateful MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configuring stateful MIGs Stay organized with collections  Save and categorize content based on your preferences. 

You can improve the uptime and resiliency of your [stateful applications](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs) with [stateful managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) (stateful MIGs).

By creating a [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration), you can preserve the unique state of each of your MIG's Virtual Machine (VM) instances—including name, persistent disks, and metadata—on machine restart, recreation, auto-healing, or update events.

This page describes ways you can configure stateful MIGs, along with links to the guides for each task:

  * Setting and preserving instance names
  * Configuring and managing stateful persistent disks
  * Configuring and managing stateful metadata
  * Configuring and managing stateful IP addresses



After you create or update a stateful configuration, you can [apply](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_stateful_configuration_to_managed_instances) it to make it effective, [view](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#viewing_stateful_configuration_and_preserved_state) the configuration as well as the effective preserved state of each VM, or [remove](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#removing_stateful_configuration) it if you no longer need it.

If you have an existing stateful application on standalone (unmanaged) Compute Engine VMs, also see the guide to [Migrate an existing workload to a stateful MIG](https://docs.cloud.google.com/compute/docs/tutorials/migrate-workload-to-stateful-mig).

## Before you begin

  * Review [When to use stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs)
  * Review [What makes a MIG stateful](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#what_makes_a_mig_stateful)
  * For more information, see [How stateful MIGs work](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work)
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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Limitations

A MIG with [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#what_makes_a_mig_stateful)—a _stateful MIG_ —has the following limitations:

  * You cannot use autoscaling if your MIG has stateful configuration.
  * If you want to use automated rolling updates, you must set the [replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#replacement_method) to `RECREATE`.
  * For stateful regional MIGs, you must [disable proactive redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) (set the redistribution type to `NONE`) to prevent deletion of stateful instances by automatic cross-zone redistribution.
  * If you use an [all-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic) to override instance template properties, you cannot specify those properties in any per-instance configuration and at the same time in the group's all-instances configuration.

  * A stateful regional MIG does not automatically orchestrate cross-zone failover. When using a regional MIG, you can make your stateful application resilient to zonal failure by deploying redundant replicas to multiple zones and relying on your application's data replication functionality.

  * When you permanently [delete](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) an instance (either manually or by resizing), the MIG does not preserve the instance's stateful metadata.




## Setting and preserving instance names

A MIG always preserves the names of its VM instances, unless you permanently [delete](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) the instances by decreasing the group size or by performing a rolling update that substitutes existing instances with new ones.

If you want to preserve instance names during updates, set the [replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#preserving_instance_names) for the update to `RECREATE` in the group's update policy.

You can specify custom names by [creating instances manually](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs) or you can let the MIG autogenerate names for its VMs.

Setting custom VM names is useful for:

  * Migrating existing standalone VMs to a stateful MIG to benefit from autohealing and auto-updating, while preserving their names.
  * Deploying architectures where external dependencies rely on specific VM names, for example, a primary VM that keeps a registry of working nodes based on pre-configured names or using a special naming pattern.
  * Deploying legacy configurations that require specific VM names, for example, because the names are hardcoded.



In all other cases, you can let the MIG autogenerate VM names using the [base instance name](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--base-instance-name) plus a random suffix.

## Configuring and managing stateful persistent disks

Configuring persistent disks to be stateful lets you benefit from VM [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) and [controlled updates](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#selective_updates) while preserving the state of the disks. For more information, see the [use cases](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs) for stateful MIGs.

For instructions, see [Configuring stateful persistent disks](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs).

## Configuring stateful metadata

You can use instance [metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to set properties for and communicate with your applications through the metadata server. For example, you can use metadata to configure the identity of the VM, environment variables, information about cluster architecture, or data range this VM is responsible for.

By using stateful metadata you ensure that instance-specific metadata is preserved on instance autohealing, update, and recreate events.

For instructions, see [Configuring stateful metadata](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs).

## Configuring and managing stateful IP addresses

You can configure a managed instance group (MIG) to preserve [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses) on instance autohealing, update, and recreation events by declaring them stateful. Both internal and external IP addresses can be preserved. You can configure IP addresses to be assigned automatically or assign specific IP addresses to each VM instance in a MIG.

For instructions, see [Configuring stateful IP addresses](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs).

## Applying, viewing, and removing stateful configuration

After you configure a MIG to be stateful, you can:

  * Apply the stateful configuration for it to take effect.
  * View the stateful configuration as well as the effective [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) of your managed instances.
  * Remove the stateful configuration.



For instructions, see [Applying, viewing, and removing stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs).

## Feedback

We want to learn about your use cases, challenges, and feedback about stateful MIGs. Please share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

## What's next

  * [Create VMs with specific names](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#adding_instances_with_specific_names) in a MIG.
  * [Configure stateful persistent disks](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs) for all VMs or for specific VMs in a MIG.
  * [Configure stateful metadata](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs) for VMs in a MIG.
  * [Configuring stateful IP addresses](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs) for all VMs or for specific VMs in a MIG.
  * [Apply, view, or remove](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs) your stateful configuration.
  * Learn more about [MIGs](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) and [working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
