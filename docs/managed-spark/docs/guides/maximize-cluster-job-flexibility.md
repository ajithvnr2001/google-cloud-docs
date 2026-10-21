---
url: https://docs.cloud.google.com/managed-spark/docs/guides/maximize-cluster-job-flexibility/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:33.457365+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/maximize-cluster-job-flexibility/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Maximize cluster and job flexibility and efficiency

This page provides best practices and scheduling strategies to help you design resilient Managed Service for Apache Spark clusters that maximize resource obtainability across Google Cloud regions, reduce provisioning delays, and take advantage of performance and cost optimizations.

## Overview of resource obtainability

Running jobs on rigid Managed Service for Apache Spark clusters creates single points of failure that can lead to job interruptions and cluster and job failures due to localized unavailability or provisioning delays.

The risk of resource unavailability is high for clusters configured with any of the following rigid anti-patterns:

  * **Fixed zone placement:** Hardcoding a single zone using the `zone` flag or field instead of allowing [Managed Service for Apache Spark AutoZone](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone) to dynamically place the cluster in the optimal zone. This anti-pattern prevents cluster creation from using compute resources available in adjacent zones. 
  * **Single machine type or generation per node role:** Restricting node roles to a single [machine generation or type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). This anti-pattern prevents the cluster from falling back to alternatives.
  * **Too few machine families at the highest priority rank:** Listing only one or two machine families at rank 0 of a flexible VM policy, even when fallback ranks are defined. This anti-pattern narrows the pool of resources that Managed Service for Apache Spark can first draw from, which increases the likelihood of falling back to lower ranks or of provisioning delays.
  * **Vertical scaling with fewer large VMs:** Scaling clusters vertically to rely on a small number of large VM shapes. This anti-pattern restricts scheduling flexibility.
  * **All-or-nothing cluster creation:** Requiring all worker nodes to provision simultaneously rather than using [partial cluster creation](https://docs.cloud.google.com/managed-spark/docs/guides/create-partial-cluster) paired with autoscaling. This anti-pattern causes cluster creation to fail if a worker node can't be allocated due to temporary resource unavailability.
  * **Peak scheduling spikes:** Triggering large batch pipelines during peak-use hours, which increases regional contention.



Resource obtainability is the practice of designing jobs to be hardware-flexible, multi-zonal, and scalable. By decoupling clusters from rigid configurations and enabling multi-machine family fallbacks, you can increase creation success rates, minimize startup latency, and consistently achieve SLAs.

## Resource obtainability recommendations

Adopt the following optimizations to improve resource availability and job stability:

### Use flexible VMs

The [Flexible VM](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms) feature lets you specify a ranked list of VM types for master, primary, and secondary worker nodes. This increases creation success rates by evaluating listed VM types and automatically selecting zones with available capacity.

**Recommendations:** Use flexible VMs with disk overrides, which lets you specify different disk types, such as hyperdisk and persistent disk, for different candidate machine families in the same cluster policy. You can also blend Gen2 and Gen4 machine families within a single policy to scale jobs across a broader pool and bypass capacity limits.

**Specify at least three distinct machine families at rank 0.** Managed Service for Apache Spark draws from the highest priority (rank 0) list first, so a wide rank 0 gives cluster creation the largest pool of candidate resources before it falls back to lower ranks. Combining Gen4 and Gen2 families at rank 0 is the most effective way to widen this pool.

For general-purpose workloads, for example, jobs currently running on N2 or N2D machines, use the following rankings:

  * **Rank 0:** N4, N4D (with hyperdisk balanced), N2, N2D
  * **Rank 1:** C4, C4D (with hyperdisk balanced), C2D. Local SSDs can be used with C4 and C4D, but typically 8 or 16 cores support only 1–2 local SSDs.
  * **Rank 2:** E2 (lower performance; use only if needed)



For example, for jobs using `n2d-standard-16`, the rankings are:

  * **Rank 0:** `n4-standard-16`, `n4d-standard-16`, `n2-standard-16`, `n2d-standard-16`
  * **Rank 1:** `c4-standard-16`, `c4d-standard-16`, `c2d-standard-16`
  * **Rank 2:** `e2-standard-16`



Because N4 and N4D require Hyperdisk and N2 and N2D use persistent disk, define rank 0 as two instance selections that share the same rank but use different `diskConfig` values. For example, the following [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) flags define the primary worker policy for the preceding example:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --zone="" \
        --num-workers=NUM_WORKERS \
        --worker-instance-selection='{"machineTypes":["n4-standard-16","n4d-standard-16"],"rank":0,"diskConfig":{"bootDiskType":"hyperdisk-balanced","bootDiskSizeGb":BOOT_DISK_SIZE_GB}}' \
        --worker-instance-selection='{"machineTypes":["n2-standard-16","n2d-standard-16"],"rank":0,"diskConfig":{"bootDiskType":"pd-balanced","bootDiskSizeGb":BOOT_DISK_SIZE_GB}}' \
        --worker-instance-selection='{"machineTypes":["c4-standard-16","c4d-standard-16"],"rank":1,"diskConfig":{"bootDiskType":"hyperdisk-balanced","bootDiskSizeGb":BOOT_DISK_SIZE_GB}}' \
        --worker-instance-selection='{"machineTypes":["c2d-standard-16"],"rank":1,"diskConfig":{"bootDiskType":"pd-balanced","bootDiskSizeGb":BOOT_DISK_SIZE_GB}}' \
        --worker-instance-selection='{"machineTypes":["e2-standard-16"],"rank":2,"diskConfig":{"bootDiskType":"pd-balanced","bootDiskSizeGb":BOOT_DISK_SIZE_GB}}'
    

**Note:** The number of VMs to provision depends on your specific job requirements.

When using Flexible VMs, consider the following factors:

  * **Mixed disk type support:** Gen3 and Gen4 machine types only support [Hyperdisk disk types](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) and don't support [Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#pd-machine-series). When blending Gen2 and Gen4, specify a `diskConfig` for each instance selection in the `instanceFlexibilityPolicy`. For more information, see [Disk overrides](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms#disk-overrides).

    * Use hyperdisk balanced with the baseline values for IOPS and throughput specified in [hyperdisk balanced default performance](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#default-perf).
  * **Resource quotas:** When you define a Flexible VM policy with fallback types, Compute Engine checks quotas for all candidate types and disks in the region. Ensure that your project has sufficient compute and disk quotas allocated for all configured items.

  * **Compute Engine discounts:** Take advantage of [flexible committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) to apply spend-based savings across multiple VM families and regions.

  * **Pricing:** Use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator) to compare costs for each rank in your policy.




For configuration templates and deployment examples, see:

  * [Flexible VMs with Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataproc_cluster#instance_flexibility_policy-1)
  * [Apache Airflow Managed Service for Apache Spark operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.InstanceSelection)



### Use autozone placement

Use [AutoZone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone) to let Managed Service for Apache Spark select the best zone to provision resources. If you use custom Virtual Private Cloud (VPC) networks, ensure that the subnet has sufficient IP addresses across all regional zones.

### Use smaller machine shapes

Design jobs to scale horizontally across smaller machine types (4, 8, or 16 cores) instead of scaling vertically with larger VMs. Smaller VM sizes have higher availability across zones, helping prevent creation delays.

  * Review and re-architect jobs that use large machine types for driver nodes.
  * Review jobs that run only driver nodes without worker nodes (single-node clusters). Jobs running on single-node clusters can't scale up dynamically and bind execution to a single physical host.



### Use cluster autoscaling

Use [cluster autoscaling](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling) with a sufficient maximum number of instances to manage capacity for jobs with resource variability (spikes).

#### Use partial cluster creation with autoscaling

Use [partial cluster creation](https://docs.cloud.google.com/managed-spark/docs/guides/create-partial-cluster), which lets you specify a minimum number of primary workers, with autoscaling. If the cluster starts with fewer workers than requested, autoscaling can add more workers dynamically once resources become available.

### Schedule jobs during off-peak hours

Schedule jobs during off-peak hours, such as midday and weekends. Schedule at non-standard times, for example, at `10:07` instead of `10:00`, to avoid scheduling spikes.

**Tip:** **Serverless workloads** If instead of running jobs on clusters, you [submit serverless jobs](https://docs.cloud.google.com/managed-spark/docs/serverless-overview) to Managed Service for Apache Spark, use runtime version `3.0` and later to run jobs across multiple availability zones in your selected region, and include automated Gen4 hardware fallbacks.

## What's next

  * Learn how to [prioritize VM types with flexible VMs](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms).
  * Learn how to [configure AutoZone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone).
  * Learn how to [create a partial cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-partial-cluster).
  * Learn how to [configure autoscaling policies](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling).
  * Learn more about [committed use discounts](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based). 
    * Learn more about [Managed Service for Apache Spark serverless](https://docs.cloud.google.com/managed-spark/docs/serverless-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
