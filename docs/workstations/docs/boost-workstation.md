---
url: https://docs.cloud.google.com/workstations/docs/boost-workstation/
title: Boost your workstation \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:13:05.579660+00:00
---

# Boost your workstation  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/boost-workstation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Boost your workstation Stay organized with collections  Save and categorize content based on your preferences. 

Boost configurations in Cloud Workstations let you temporarily allocate additional compute resources to a workstation on demand, including larger machine types, GPUs, larger boot disks, and nested virtualization. When you specify a boost configuration in a workstation configuration, you can start workstations created from that configuration with those boosted resources whenever your workloads require them—for example, when running applications that require attached GPUs. In the Cloud Workstations API, these parameters are collectively referred to as the [`BoostConfig`](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs#boostconfig).

## Creating a boost configuration

To create a workstation config that includes a boost configuration, run the following `gcloud` CLI command:
    
    
        gcloud beta workstations configs create WORKSTATION_CONFIG_ID \
            --cluster=WORKSTATION_CLUSTER_ID \
            --region=LOCATION \
            --project=PROJECT_ID \
            --boost-config=id=BOOST_CONFIG_ID,machine-type=MACHINE_TYPE,accelerator-type=ACCELERATOR_TYPE,accelerator-count=ACCELERATOR_COUNT,enable-nested-virtualization=ENABLE_NESTED_VIRTUALIZATION,boot-disk-size=BOOT_DISK_SIZE,pool-size=POOL_SIZE,enable-automatic-failover=ENABLE_AUTOMATIC_FAILOVER
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the workstation configuration.
  * `LOCATION`: the location of the workstation cluster.
  * `WORKSTATION_CLUSTER_ID`: the name of the workstation cluster that contains the workstation configuration.
  * `WORKSTATION_CONFIG_ID`: the name of the workstation configuration to be created.
  * `BOOST_CONFIG_ID`: the ID to be used for the boost configuration.
  * `MACHINE_TYPE`: the type of machine that boosted VM instances use (for example, `e2-standard-4`).
  * `ENABLE_NESTED_VIRTUALIZATION`: whether to enable nested virtualization.
  * `ACCELERATOR_TYPE`: the type of accelerator card attached to the boost instance (for example, `nvidia-tesla-t4`).
  * `ACCELERATOR_COUNT`: the number of accelerator cards attached to the boost instance.
  * `BOOT_DISK_SIZE`: the size of the boot disk for the VM in gigabytes (GB).
  * `POOL_SIZE`: the number of boost VMs that the system keeps idle.
  * `ENABLE_AUTOMATIC_FAILOVER`: whether to automatically fail over to this boost configuration if Compute Engine lacks capacity for the default machine type during workstation startup. Defaults to `false`.



See [Boost Config API reference](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs#boostconfig) for more information about each parameter and their defaults.

## Starting a boosted workstation

If the workstation config includes a boost configuration, when starting a workstation, users can choose to use a VM provisioned under the `BoostConfig` by passing the `boost config id` in the start request. If no `boost config id` is provided in the start request, the system will choose a VM from the pool provisioned under the default config.

To boost a specific workstation, run the following `gcloud` CLI command:
    
    
        gcloud beta workstations start WORKSTATION_ID \
            --boost=BOOST_CONFIG_ID
    

Replace the following:

  * `WORKSTATION_ID`: the name of the workstation to start.
  * `BOOST_CONFIG_ID`: the ID matching the boost configuration to boost up to.



## Automatic failover to a boost configuration

To prevent workstation startup failures caused by regional or zonal resource exhaustion, you can configure automatic failover ([Preview](https://cloud.google.com/products#product-launch-stages)) on one or more boost configurations.

To enable automatic failover on a boost configuration, set `enable-automatic-failover=true` in the `--boost-config` flag in the `gcloud` CLI, or set `enableAutomaticFailover` to `true` in the [`BoostConfig`](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#boostconfig) API resource. A boost configuration with automatic failover enabled must specify a machine type from a different machine series than the workstation configuration's default machine type. For example, if your default machine type is `e2-standard-4`, your failover boost configuration must use a machine series other than E2, such as `n2-standard-4`.

When you start a workstation without specifying a boost configuration and Compute Engine can't provision the default machine type due to resource exhaustion, Cloud Workstations automatically attempts to provision the workstation using an eligible boost configuration. If multiple boost configurations have automatic failover enabled, Cloud Workstations evaluates them in the order that they appear in the workstation configuration until provisioning succeeds. Automatic failover applies only to the active workstation session; subsequent starts attempt to provision the default machine type first. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
