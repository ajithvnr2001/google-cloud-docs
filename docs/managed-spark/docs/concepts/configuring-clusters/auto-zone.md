---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone/
title: Auto Zone placement \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:40.484478+00:00
---

# Auto Zone placement  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Auto Zone placement Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Managed Service for Apache Spark cluster, you specify a Compute Engine [region](https://docs.cloud.google.com/managed-spark/docs/concepts/cluster-region) as the location of the cluster. You can also specify a zone within that region, or you can omit the zone to have the Managed Service for Apache Spark Auto Zone feature select a zone for you in the specified region. All nodes for the cluster are deployed to the selected zone.

You can exclude zones from Auto Zone selection criteria if the cluster region includes at least two non-excluded zones. For more information, see Use Auto Zone placement.

## Auto Zone and resource reservations

Auto Zone prioritizes creating a cluster in a zone with [resource reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type), as follows:

  * If requested cluster resources can be fully satisfied by reserved, plus, if necessary, on-demand resources in a zone, Auto Zone will consume the reserved and on-demand resources, and create the cluster in that zone.

  * Auto Zone prioritizes zones for selection according to total CPU core (`vCPU`) reservations in a zone.

**Example:** A cluster creation request specifies 20 `n2-standard-2` and 1 `n2-standard-64` (40 + 64 `vCPUs` requested). Auto Zone will prioritize the following zones for selection according to the total vCPU reservations available in the zone:

    1. `zone-c` available reservations: 3 `n2-standard-2` and 1 `n2-standard-64` (70 `vCPUs`)
    2. `zone-b` available reservations: 1 `n2-standard-64` (64 `vCPUs`)
    3. `zone-a` available reservations: 25 `n2-standard-2` (50 `vCPUs`)

Assuming each of these zones has additional on-demand `vCPU` and other resources sufficient to satisfy the cluster request, Auto Zone will select `zone-c` for cluster creation.

  * If requested cluster resources cannot be fully satisfied by reserved plus on-demand resources in a zone, Auto Zone will create the cluster in a zone that is most likely to satisfy the request using on-demand resources.




## Use Auto Zone placement

### Google Cloud console

To create a cluster that uses Auto Zone placement:

  1. In the Google Cloud console, Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. In the **Define your cluster** section, select a **Region**.
  3. In the **Zone** field, select **Any**.



**Exclude zones:** Specifying zones to exclude from Auto Zone placement is not supported through the Google Cloud console. This feature is available using the Google Cloud CLI and the REST API.

### gcloud CLI

To create a Managed Service for Apache Spark cluster that uses Auto Zone placement, use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command. Set the `--region` flag to a region. then either omit the `--zone` flag or set the `--zone` flag to an empty string (`--zone=""`).

As an alternative to using the `--zone` flag, you can use use the `--auto-zone-exclude-zones` flag to specify a comma-separated list of zones. Auto Zone selection will select a zone from the specified region, but exclude the listed zones from its selection criteria. Note that there must be at least two non-excluded zones available in the cluster region. **Note:** If you set a default zone with the `gcloud config set compute/zone` command, you must use the `--zone=""` or `--auto-zone-exclude-zones` flag to enable the Auto Zone feature. [Power Shell](https://docs.microsoft.com/en-us/powershell/) users must surround the empty quotes with single quotes: `--zone='""'`. 

**Examples:**

Basic Auto Zone usage:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        other args ...
    

Auto Zone with excluded zones:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --auto-zone-exclude-zones=ZONE_1,ZONE_2 \
        other args ...
    

### REST API

To create a Managed Service for Apache Spark cluster that uses Auto Zone placement, construct a JSON [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request, leaving the [gceClusterConfig.zoneUri](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig) field empty. In the REST endpoint, `https://dataproc.googleapis.com/v1/projects/projectId/regions/region/clusters`, insert a region name. Managed Service for Apache Spark Auto Zone will choose a zone for the cluster within the specified region.

To exclude specific zones, you can populate the [gceClusterConfig.autoZoneExcludeZoneUris](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig) field with a list of zone names to exclude. Note that there must be at least two non-excluded zones available in the cluster region.

**Use short resource names with Auto Zone placement** : When specifying a resource URI, such as [machineTypeUri](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#InstanceGroupConfig) or [acceleratorTypeUri](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#acceleratorconfig), in an Auto Zone placement REST API cluster creation request, use a short resource name without a zone specification, for example, "n1-standard-2" or "nvidia-tesla-t4".

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
