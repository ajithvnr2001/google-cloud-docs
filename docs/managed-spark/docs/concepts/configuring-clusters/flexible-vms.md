---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms/
title: Prioritize VM types with flexible VMs \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:33.300234+00:00
---

# Prioritize VM types with flexible VMs  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/flexible-vms/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Prioritize VM types with flexible VMs Stay organized with collections  Save and categorize content based on your preferences. 

Flexible VMs is a Managed Service for Apache Spark feature that lets you specify prioritized lists of VM types for Managed Service for Apache Spark master, primary, and secondary worker nodes when you [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster).

## Why use flexible VMs?

The problem: If a VM type is unavailable when you submit a cluster creation request, the request fails, and you need to update your request, script, or code to specify a "next-best" VM type. This re-request process can involve multiple iterations until you specify a VM type that is available.

The solution: The Managed Service for Apache Spark flexible VM feature helps your cluster creation request succeed by selecting master, primary, and secondary worker VM types from your ranked VM lists, and then searching for zones within your specified cluster region with availability of the listed VM types.

## Limitations

  * Clusters that use flexible VMs cannot be [stopped](https://docs.cloud.google.com/managed-spark/docs/guides/start-stop).
  * Master nodes in [High availability clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability) cannot use flexible VMs, but HA cluster worker nodes can use flexible VMs.



## Terminology

  * **VM type:** The family, memory capacity, and number of CPU cores of a VM instance. Managed Service for Apache Spark supports the use of [predefined and custom VM types](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types). In this document the terms "VM type" and "instance-selection" refer to a [supported machine type](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/supported-machine-types) used to provision VMs in a cluster master or worker node.
  * **Master and primary worker nodes:** By default, a Managed Service for Apache Spark cluster has one master node and two primary worker nodes. 
    * A [High availability (HA) cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/high-availability) has three master nodes.
    * A [single node cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) has one node that acts as a master and worker node.
    * A [zero-scale cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-zero-scale-cluster) has a master node and secondary workers only (no primary workers).
  * **Secondary worker nodes:** [Secondary workers](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/secondary-vms) don't store data and function only as processing nodes. You can use secondary workers to scale compute without scaling storage. The default flexible VM secondary worker type is a Spot VM, which is a preemptible type.



## Usage

  * Flexible VMs are available in Managed Service for Apache Spark on Managed Service for Apache Spark `2.0.74+`, `2.1.76+`, `2.2.42+`, and later [imageversions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions). 
    * Starting with image version `3.0`, when you create a cluster without specifying a machine type for a cluster node, Managed Service for Apache Spark specifies the node with a ranked list of flexible VM machine types, such as a ranked list of N4, N2, and E2 series machine types, with the list optimized for resource availability.
  * You can specify up to five ranked VM type lists, with up to 10 VM types in a list.

**Note:** To improve the likelihood of obtaining suitable VMs, specify at least three machine families in the highest priority (rank 0) flexible VM list. For recommended rankings, see [Use flexible VMs](https://docs.cloud.google.com/managed-spark/docs/guides/maximize-cluster-job-flexibility#use-flexible-vms).
  * You can include Flexible VMs in [workflow templates](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/use-workflows) to provide resiliency against resource unavailability when clusters are created from the template.

**Recommendation:** Enable [Managed Service for Apache Spark autozone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone), which allows Managed Service for Apache Spark to choose a zone with the capacity to provision requested VMs.

  * By default, a cluster node must use one disk type. You can use disk overrides to specify different disk types for different machine types specified for a Flex VM cluster node.

  * Although you can specify different CPU-to-memory ratios for primary and secondary worker VM types in a cluster, this can lead to performance degradation because the smallest CPU-to-memory ratio is used as the smallest container unit.  Use a uniform CPU-to-memory ratio for primary and secondary workers, including flexible VMs.

  * If your cluster creation request includes an [autoscaling policy](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/autoscaling#create_an_autoscaling_cluster), flexible VMs can be from different VM families, but they must have the same amount of memory and core count.

  * Machine types that match reservations are first selected within a rank, followed by VM types with the largest number of CPUs.

  * Managed Service for Apache Spark applies Google Cloud [quotas](https://docs.cloud.google.com/managed-spark/quotas) to flexible VM provisioning.

  * If you update a cluster that was created using flexible VMs, Managed Service for Apache Spark selects and adds workers from the flexible VM lists that you provided when you created your cluster.




## How to request flexible VMs

You can specify up to five ranked VM type lists, with up to 10 VM types in a list. Lowest ranked lists have the highest priority. By default, flexible VM lists have a rank of 0. Within a list, Managed Service for Apache Spark prioritizes VM types with unused reservations, followed by the largest VM sizes. VM types within a list with the same CPU count are treated equally.

You can request flexible VMs when you create a Managed Service for Apache Spark cluster using the Google Cloud console, Google Cloud CLI, Dataproc API, Managed Service for Apache Airflow, or Terraform.

### Console

To create a cluster with flexible VMs, do the following:

**Note:** Console support for manager (master) node Flex VMs is not available.

  1. Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Primary workers** or **Secondary workers**. Under **Add worker types** , specify additional ranked VMs.



### gcloud

Use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with `master-instance-selection`, `worker-instance-selection` and `secondary-worker-instance-selection` flags to specify ranked flexible VM lists for master, primary, and secondary workers.

**Deprecated:** The previous `--master-machine-types`, `--worker-machine-types`, and `--secondary-worker-machine-types` flags are deprecated.

The following example requests master, primary, and secondary VM types with the following priorities:

  * Provision `e2-standard-8` VMs if available (rank 0); if `e2-standard-8` machines are not available, provision `n2-standard-8` VMs (rank 1).



Since the [secondary worker type](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--secondary-worker-type) isn't specified, preemptible Spot secondary VMs will be provisioned.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --zone="" \
        --master-instance-selection='{"machineTypes":["e2-standard-8"],"rank":0}' \
        --master-instance-selection='{"machineTypes":["n2-standard-8"],"rank":1}' \
        --num-workers=10 \
        --worker-instance-selection='{"machineTypes":["e2-standard-8"],"rank":0}' \
        --worker-instance-selection='{"machineTypes":["n2-standard-8"],"rank":1}' \
        --num-secondary-workers=4 \
        --secondary-worker-instance-selection='{"machineTypes":["e2-standard-8"],"rank":0}' \
        --secondary-worker-instance-selection='{"machineTypes":["n2-standard-8"],"rank":1}'
    

Notes:

  * `--zone=""`: Setting this flag to an empty value enables [autozone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone), which allows Managed Service for Apache Spark to choose a zone that has the requested VM types available for use. This flag value overrides any zone selection specified in your default `gcloud config list`.



### API

Use the [`instanceFlexibilityPolicy.instanceSelectionList`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#InstanceFlexibilityPolicy.FIELDS.instance_selection_list) as part of a Dataproc API [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request to specify a ranked list of [machineTypes](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#InstanceSelection.FIELDS.machine_types) for master, primary, and secondary workers.

Example: The following JSON snippet from a `clusters.create` [request body](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create#request-body) specifies master (`masterConfig`), primary worker (`workerConfig`), and secondary worker (`secondaryWorkerConfig`) machine types with ranks 0 and rank 1.
    
    
    {
      "projectId": "PROJECT_ID",
      "clusterName": "CLUSTER_NAME",
      "config": {
        "gceClusterConfig": {
          "zoneUri": ""
        },
        "masterConfig": {
          "numInstances": 1,
          "instanceFlexibilityPolicy": {
            "instanceSelectionList": [
              {
                "machineTypes": ["e2-standard-8"],
                "rank": 0
              },
              {
                "machineTypes": ["n2-standard-8"],
                "rank": 1
              }
            ]
          }
        },
        "workerConfig": {
          "numInstances": 10,
          "instanceFlexibilityPolicy": {
            "instanceSelectionList": [
              {
                "machineTypes": ["e2-standard-8"],
                "rank": 0
              },
              {
                "machineTypes": ["n2-standard-8"],
                "rank": 1
              }
            ]
          }
        },
        "secondaryWorkerConfig": {
          "numInstances": 4,
          "instanceFlexibilityPolicy": {
            "instanceSelectionList": [
              {
                "machineTypes": ["e2-standard-8"],
                "rank": 0
              },
              {
                "machineTypes": ["n2-standard-8"],
                "rank": 1
              }
            ]
          }
        }
      }
    }
    

### Cloud Composer

Use the [`DataprocCreateClusterOperator`](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocCreateClusterOperator) operator in an Apache Airflow DAG to specify `instance_flexibility_policy` for master, primary, and secondary workers:
    
    
    from airflow import DAG
    from airflow.models import Variable
    from airflow.providers.google.cloud.operators.dataproc import (
        DataprocCreateClusterOperator,
    )
    from airflow.utils.dates import days_ago
    
    PROJECT_ID = Variable.get("DATAPROC_PROJECT_ID")
    REGION = Variable.get("DATAPROC_REGION")
    CLUSTER_NAME = Variable.get("DATAPROC_CLUSTER_NAME")
    NUM_WORKERS = int(Variable.get("DATAPROC_NUM_WORKERS"))
    MIN_NUM_WORKERS = int(Variable.get("DATAPROC_MIN_NUM_WORKERS"))
    
    FLEX_SELECTION_LIST = [
        {
            "machine_types": ["e2-standard-8"],
            "rank": 0,
        },
        {
            "machine_types": ["n2-standard-8"],
            "rank": 1,
        },
    ]
    
    CLUSTER_CONFIG = {
        "gce_cluster_config": {
            "zone_uri": "",
        },
        "master_config": {
            "num_instances": 1,
            "instance_flexibility_policy": {
                "instance_selection_list": FLEX_SELECTION_LIST,
            },
        },
        "worker_config": {
            "num_instances": NUM_WORKERS,
            "min_num_instances": MIN_NUM_WORKERS,
            "instance_flexibility_policy": {
                "instance_selection_list": FLEX_SELECTION_LIST,
            },
        },
        "secondary_worker_config": {
            "num_instances": 4,
            "instance_flexibility_policy": {
                "instance_selection_list": FLEX_SELECTION_LIST,
            },
        },
    }
    
    with DAG(
        "dataproc_flexvm_dag",
        start_date=days_ago(1),
        schedule_interval=None,
        catchup=False,
    ) as dag:
        create_dataproc_cluster = DataprocCreateClusterOperator(
            task_id="create_dataproc_flexvm_cluster",
            project_id=PROJECT_ID,
            region=REGION,
            cluster_name=CLUSTER_NAME,
            cluster_config=CLUSTER_CONFIG,
        )
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

Use the [`google_dataproc_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataproc_cluster) resource with `instance_flexibility_policy` blocks to specify ranked flexible VM lists:
    
    
    variable "project_id" {
      type        = string
      description = "The Google Cloud project ID"
    }
    
    variable "region" {
      type        = string
      description = "The Google Cloud region for Dataproc deployment"
    }
    
    variable "cluster_name" {
      type        = string
      description = "Name of the Dataproc cluster"
    }
    
    variable "num_workers" {
      type        = number
      description = "Target number of primary workers"
    }
    
    variable "min_num_workers" {
      type        = number
      description = "Minimum primary workers for partial cluster creation"
    }
    
    resource "google_dataproc_cluster" "flex_cluster" {
      name    = var.cluster_name
      project = var.project_id
      region  = var.region
    
      cluster_config {
        gce_cluster_config {
          zone = ""
        }
    
        master_config {
          num_instances = 1
          instance_flexibility_policy {
            instance_selection_list {
              machine_types = ["e2-standard-8"]
              rank          = 0
            }
            instance_selection_list {
              machine_types = ["n2-standard-8"]
              rank          = 1
            }
          }
        }
    
        worker_config {
          num_instances     = var.num_workers
          min_num_instances = var.min_num_workers
          instance_flexibility_policy {
            instance_selection_list {
              machine_types = ["e2-standard-8"]
              rank          = 0
            }
            instance_selection_list {
              machine_types = ["n2-standard-8"]
              rank          = 1
            }
          }
        }
    
        secondary_worker_config {
          num_instances = 4
          instance_flexibility_policy {
            instance_selection_list {
              machine_types = ["e2-standard-8"]
              rank          = 0
            }
            instance_selection_list {
              machine_types = ["n2-standard-8"]
              rank          = 1
            }
          }
        }
      }
    }
    

## Disk overrides

You can specify disk overrides for each machine type (instance selection) in your flexible VM specification. This lets you customize boot disks, override local ssds and attach additional disks for specific machine types.

**Note:** The `diskType` field in `attachedDiskConfigs` is deprecated. Use `type` instead.

### Disk override options and rules

Disk override configuration options:

  * **Base disk configuration:** A disk configuration specified for a cluster node, for example, specifying a boot disk size for primary workers using the gcloud CLI [`--worker-boot-disk-size`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create#--worker-boot-disk-size) flag or the [`workerConfig.diskConfig.bootDiskSizeGb`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/InstanceGroupConfig#diskconfig) Dataproc API field.
  * **Instance selection disk overrides:** Disk configurations for machine types specified for a cluster node.



Disk override configuration rules:

  * **Base disk configuration:** If no instance selection for a cluster node includes a `diskConfig` override, you can define a base disk configuration for the node. This base disk configuration is applied to all instance selections for the node.

  * **Instance selection disk configurations:** If an instance selection for a cluster node includes a `diskConfig` override, **all** instance selections in the node group must include a `diskConfig` (if you also define a base disk configuration for the node, a validation error occurs).

  * **Machine type compatibility:** All machine types within a single `InstanceSelection` must be compatible with the specified `diskConfig`. For example, you can't group an `e2-standard-4` machine type, which does not support a hyperdisk, with an `n4-standard-4` machine type, which requires a hyperdisk, in the same instance selection since the `diskConfig` can't satisfy both machine types.

  * **Local SSD support:** If you configure local SSDs (`numLocalSsds` > 0) in a disk override configuration, **all** machine types in the instance selection must support local SSDs.

  * **Mandatory disk override configuration fields:**

    * If you define `diskConfig` for an instance selection, `bootDiskType` is mandatory.
    * If you define `attachedDiskConfigs`, both `type` and `diskSizeGb` are mandatory for each attached disk.



### Disk override configuration examples

The following example specifies the following disk override configuration options for the following cluster nodes:

  * **Master nodes:** Use default boot disks.
  * **Primary workers:** Use customized disks per instance selection: for example `n4-standard-4` uses `hyperdisk-balanced`, while `n2-standard-4` uses `pd-standard`.
  * **Secondary workers:** Use a custom base disk configuration: `pd-ssd` with `200 GB`, which is applied to all instance selections.



### gcloud YAML

Define the flexible VM policies in YAML files for master, primary worker, and secondary worker nodes:

  1. `master-flex-policy.yaml`: 
         
         instanceFlexibilityPolicy:
           instanceSelectionList:
           -   machineTypes:
             -   e2-standard-8
             rank: 0
           -   machineTypes:
             -   n2-standard-8
             rank: 1

  2. `worker-flex-policy.yaml`: 
         
         instanceFlexibilityPolicy:
           instanceSelectionList:
           -   machineTypes:
             -   n4-standard-4
             rank: 0
             diskConfig:
               bootDiskType: hyperdisk-balanced
               bootDiskSizeGb: 100
               bootDiskProvisionedIops: 6000
               bootDiskProvisionedThroughput: 400
               attachedDiskConfigs:
               -   type: hyperdisk-throughput
                 diskSizeGb: 300
           -   machineTypes:
             -   n2-standard-4
             rank: 0
             diskConfig:
               bootDiskType: pd-standard
               bootDiskSizeGb: 400

  3. `secondary-worker-flex-policy.yaml`: 
         
         instanceFlexibilityPolicy:
           instanceSelectionList:
           -   machineTypes:
             -   e2-standard-8
             rank: 0
           -   machineTypes:
             -   n2-standard-8
             rank: 1




Use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command to pass the policy files:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --zone="" \
        --num-masters=1 \
        --master-instance-flexibility-policy-file=master-flex-policy.yaml \
        --num-workers=10 \
        --worker-instance-flexibility-policy-file=worker-flex-policy.yaml \
        --num-secondary-workers=4 \
        --secondary-worker-boot-disk-type=pd-ssd \
        --secondary-worker-boot-disk-size=200 \
        --secondary-worker-instance-flexibility-policy-file=secondary-worker-flex-policy.yaml
    

### gcloud JSON

Use the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with inline JSON `diskConfig` specifications in `--worker-instance-selection`:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --zone="" \
        --num-masters=1 \
        --master-instance-selection='{"machineTypes":["e2-standard-8"],"rank":0}' \
        --master-instance-selection='{"machineTypes":["n2-standard-8"],"rank":1}' \
        --num-workers=10 \
        --worker-instance-selection='{"machineTypes":["n4-standard-4"],"rank":0,"diskConfig":{"bootDiskType":"hyperdisk-balanced","bootDiskSizeGb":100,"bootDiskProvisionedIops":6000,"bootDiskProvisionedThroughput":400,"attachedDiskConfigs":[{"type":"hyperdisk-throughput","diskSizeGb":300}]}}' \
        --worker-instance-selection='{"machineTypes":["n2-standard-4"],"rank":0,"diskConfig":{"bootDiskType":"pd-standard","bootDiskSizeGb":400}}' \
        --num-secondary-workers=4 \
        --secondary-worker-boot-disk-type=pd-ssd \
        --secondary-worker-boot-disk-size=200 \
        --secondary-worker-instance-selection='{"machineTypes":["e2-standard-8"],"rank":0}' \
        --secondary-worker-instance-selection='{"machineTypes":["n2-standard-8"],"rank":1}'
    

### API

Use the `diskConfig` field within an `instanceFlexibilityPolicy.instanceSelectionList` in a Dataproc API `clusters.create` request.

Example JSON request body:
    
    
    {
      "projectId": "PROJECT_ID",
      "clusterName": "CLUSTER_NAME",
      "config": {
        "gceClusterConfig": {
          "zoneUri": ""
        },
        "masterConfig": {
          "numInstances": 1,
          "instanceFlexibilityPolicy": {
            "instanceSelectionList": [
              {
                "machineTypes": ["e2-standard-8"],
                "rank": 0
              },
              {
                "machineTypes": ["n2-standard-8"],
                "rank": 1
              }
            ]
          }
        },
        "workerConfig": {
          "numInstances": 10,
          "instanceFlexibilityPolicy": {
            "instanceSelectionList": [
              {
                "machineTypes": ["n4-standard-4"],
                "rank": 0,
                "diskConfig": {
                  "bootDiskType": "hyperdisk-balanced",
                  "bootDiskSizeGb": 100,
                  "bootDiskProvisionedIops": 6000,
                  "bootDiskProvisionedThroughput": 400,
                  "attachedDiskConfigs": [
                    {
                      "type": "hyperdisk-throughput",
                      "diskSizeGb": 2048
                    }
                  ]
                }
              },
              {
                "machineTypes": ["n2-standard-4"],
                "rank": 0,
                "diskConfig": {
                  "bootDiskType": "pd-standard",
                  "bootDiskSizeGb": 400
                }
              }
            ]
          }
        },
        "secondaryWorkerConfig": {
          "numInstances": 4,
          "diskConfig": {
            "bootDiskType": "pd-ssd",
            "bootDiskSizeGb": 200
          },
          "instanceFlexibilityPolicy": {
            "instanceSelectionList": [
              {
                "machineTypes": ["e2-standard-8"],
                "rank": 0
              },
              {
                "machineTypes": ["n2-standard-8"],
                "rank": 1
              }
            ]
          }
        }
      }
    }
    

## Override Flex VM properties

Managed Service for Apache Spark sets properties at the cluster level. When you create a cluster that uses flexible VMs, you can override system-generated properties for primary and secondary worker Flex VM types.

### gcloud

To override properties when you create a cluster, use the `--properties` flag with the following syntax:
    
    
    --properties="$ROLE:$MACHINE_TYPE:$COMPONENT_PREFIX:$COMPONENT_PROPERTY=$VALUE"
    

  * ROLE can be either `primary_worker` or `secondary_worker`. 
  * Separate multiple properties with a comma.



The following `gcloud dataproc clusters create` command overrides the number of vCPUs that YARN allocates for NodeManager on secondary workers. This example sets the `yarn.nodemanager.resource.cpu-vcores` value in `yarn-site.xml` to `6` for all `e2-standard-8` and `n2-standard-8` secondary worker VMs.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --zone="" \
        --master-instance-selection='{"machineTypes":["e2-standard-8"],"rank":0}' \
        --master-instance-selection='{"machineTypes":["n2-standard-8"],"rank":1}' \
        --num-workers=10 \
        --worker-instance-selection='{"machineTypes":["e2-standard-8"],"rank":0}' \
        --worker-instance-selection='{"machineTypes":["n2-standard-8"],"rank":1}' \
        --num-secondary-workers=4 \
        --secondary-worker-instance-selection='{"machineTypes":["e2-standard-8"],"rank":0}' \
        --secondary-worker-instance-selection='{"machineTypes":["n2-standard-8"],"rank":1}' \
        --properties="secondary_worker:e2-standard-8:yarn:yarn.nodemanager.resource.cpu-vcores=6,secondary_worker:n2-standard-8:yarn:yarn.nodemanager.resource.cpu-vcores=6"
    

### API

To override properties, define them in the `properties` field of the [`SoftwareConfig`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#softwareconfig) object in your cluster creation request.

Use the following syntax for the property key:
    
    
    ROLE:MACHINE_TYPE:COMPONENT_PREFIX:COMPONENT_PROPERTY
    

  * ROLE can be either `primary_worker` or `secondary_worker`.



The following `SoftwareConfig` object overrides the number of vCPUs that YARN allocates for NodeManager on secondary workers. This example sets the `yarn.nodemanager.resource.cpu-vcores` value to `6` for all `e2-standard-8` and `n2-standard-8` secondary worker VMs.
    
    
    {
      "imageVersion":"2.2.42",
      "properties": {
        "secondary_worker:e2-standard-8:yarn:yarn.nodemanager.resource.cpu-vcores" : "6",
        "secondary_worker:n2-standard-8:yarn:yarn.nodemanager.resource.cpu-vcores" : "6"
      }
    }
    

## What's next

  * Learn more about [Managed Service for Apache Spark cluster properties](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties). 
    * Learn how to [create a Managed Service for Apache Spark cluster](https://docs.cloud.google.com/managed-spark/docs/guides/create-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
