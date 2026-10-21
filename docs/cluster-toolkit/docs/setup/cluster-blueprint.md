---
url: https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint/
title: Cluster blueprint overview \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:39.118253+00:00
---

# Cluster blueprint overview  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Cluster blueprint overview Stay organized with collections  Save and categorize content based on your preferences. 

Cluster blueprints are YAML files that define reusable configurations for deploying high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads with Cluster Toolkit. Blueprints help you quickly deploy clusters, standardize configurations, and help ensure that your environments are in accordance with Google Cloud best practices. A blueprint defines your cluster's architecture by specifying which modules to use and how to configure them.

## Design a cluster blueprint

A cluster blueprint is comprised of the following three main components:

  * **Blueprint name**. The name of the blueprint. When naming your cluster blueprint, use the following conventions:

    * If you are updating or modifying an existing configuration, then don't change the blueprint name.
    * If you are creating a new configuration, then specify a new unique blueprint name.

The blueprint name is added as a label to your cloud resources and is used for tracking usage and monitoring costs.

The blueprint name is set using the `blueprint_name` field.

  * **Deployment variables**. A set of parameters that are used by all modules in the blueprint. Use these variables to set values that are specific to a deployment.

Deployment variables are set using the `vars` field in the blueprint, but you can override or set deployment variables at deployment time by specifying the `--vars` flag with the [`gcluster` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster).

The most common deployment variables are as follows:

    * `deployment_name`: the name of the deployment. The `deployment_name` is a required variable for a deployment.

This variable must be set to a unique value any time you deploy a new copy of an existing blueprint. The deployment name is added as a label to cloud resources and is used for tracking usage and monitoring costs.

Because a single cluster blueprint can be used for multiple deployments, you can use the `blueprint_name` to identify the type of environment, for example `slurm-high-performance-cluster`. While the `deployment_name` can be used to identify the targeted use of that cluster, for example `research-dept-prod`.

    * `project_id`: the [ID for the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to deploy the cluster. The `project_id` is a required variable for a deployment.

    * `zone`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to deploy the cluster.

    * `region`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to deploy the cluster.

Other variables that you might want to specify here include a custom image family, a Shared VPC network, or subnetwork that you want all modules to use.

  * **Deployment groups**. Defines a distinct set of modules that are to be deployed together. A deployment group can only contain modules of a single type, for example a deployment group can't mix Packer and Terraform modules.

Deployment groups are set using the `deployment_groups` field. Each deployment group requires the following parameters:

    * `group`: the name of the group.
    * `modules`: the descriptors for each module, these include the following:

      * `id`: a unique identifier for the module.
      * `source`: the directory path or URL where the module is located. For more information, see [Module fields](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules#module-fields).
      * `kind`: the type of module. Valid values are `packer` or `terraform`. This is an optional parameter that defaults to `terraform` if omitted.
      * `use`: a list of module IDs whose outputs can be linked to the module's settings. This is an optional parameter.
      * `outputs`: If you are using Terraform modules, use this parameter to specify a list of [Terraform output values](https://www.terraform.io/language/values/outputs) that you want to make available at the deployment group level.

During deployment, these output values are printed to the screen after you run the `terraform apply` command.

After deployment, you can access these outputs by running the [`terraform output` command](https://www.terraform.io/cli/commands/output).

This is an optional parameter.

      * `settings`: any module variable that you want to add. This is an optional parameter.

For a list of supported modules, see [Modules](https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview).

  * **Terraform Remote State configuration (optional)**. Most blueprints use Terraform modules to provision Cloud infrastructure. It is recommended to use Terraform [remote state](https://developer.hashicorp.com/terraform/language/state/remote) backed by a Cloud Storage bucket configured with [object versioning](https://docs.cloud.google.com/storage/docs/object-versioning). All configuration settings of the [Cloud Storage backend](https://developer.hashicorp.com/terraform/language/settings/backends/gcs) are supported. The `prefix` setting determines the path within a bucket where state is stored. If `prefix` is left unset, the Cluster Toolkit automatically generates a unique value based upon the `blueprint_name`, `deployment_name`, and deployment group name. The following configuration enables remote state for all deployment groups in a blueprint:
        
        terraform_backend_defaults:
        type: gcs
        configuration:
          bucket: BUCKET_NAME
        

For more information about advanced Terraform remote state configuration, see the [Cluster Toolkit GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/README.md#optional-setting-up-a-remote-terraform-state).

  * **Blueprint Versioning (optional)**. Defines the GitHub repository URL and the specific version to use for any modules that use an embedded module path. Embedded module paths include the following:

    * `source: modules/`
    * `source: community/modules/`

Providing the GitHub repository URL and the module version ensures that the module is pulled from a specific GitHub repository and uses a specific version. This provides more control and flexibility over the modules used in your deployments. To version a blueprint you must set both of the following parameters:

    * `toolkit_modules_url`: specifies the base URL of the GitHub repository containing the modules.
    * `toolkit_modules_version`: specifies the version of the modules to use.

When these parameters are specified, the blueprint processing logic modifies the source field of any module that references an embedded module path. In the deployment folder, any reference to an embedded module path is replaced with a GitHub URL that includes the specified repository, version, and module path.

For example if you set the following:
    
    toolkit_modules_url: github.com/GoogleCloudPlatform/cluster-toolkit
    toolkit_modules_version: v1.38.0
    

A module that is specified as `source: modules/compute/vm-instance` is updated to the following in the deployment folder: `source: github.com/GoogleCloudPlatform/cluster-toolkit//modules/compute/vm-instance?ref=v1.38.0&depth=1`




## Cluster blueprint examples

To get started, you can use one of the following cluster blueprint examples.

  * Example 1: Deploys a basic HPC cluster with Slurm
  * Example 2: Deploys an HPC cluster with Slurm and a tiered file system



For a full list of example cluster blueprints, see the [Cluster Toolkit GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples).

### Example 1

Deploys a basic autoscaling cluster with Slurm that uses default settings. The blueprint also creates a new VPC network, and a filestore instance mounted to `/home`.
    
    
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    ---
    
    blueprint_name: hpc-slurm
    
    vars:
      project_id:  ## Set GCP Project ID Here ##
      deployment_name: hpc-slurm
      region: us-central1
      zone: us-central1-a
    
    # Documentation for each of the modules used below can be found at
    # https://github.com/GoogleCloudPlatform/hpc-toolkit/blob/main/modules/README.md
    
    deployment_groups:
    - group: primary
      modules:
      # Source is an embedded module, denoted by "modules/*" without ./, ../, /
      # as a prefix. To refer to a local module, prefix with ./, ../ or /
      - id: network
        source: modules/network/vpc
    
      # Private Service Access (PSA) requires the compute.networkAdmin role which is
      # included in the Owner role, but not Editor.
      # PSA is a best practice for Filestore instances, but can be optionally
      # removed by deleting the private_service_access module and any references to
      # the module by Filestore modules.
      # https://cloud.google.com/vpc/docs/configure-private-services-access#permissions
      - id: private_service_access
        source: modules/network/private-service-access
        use: [network]
    
      - id: homefs
        source: modules/file-system/filestore
        use: [network, private_service_access]
        settings:
          local_mount: /home
    
      - id: debug_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network]
        settings:
          node_count_dynamic_max: 4
          machine_type: n2-standard-2
          allow_automatic_updates: false
    
      - id: debug_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use:
        - debug_nodeset
        settings:
          partition_name: debug
          exclusive: false # allows nodes to stay up after jobs are done
          is_default: true
    
      - id: compute_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network]
        settings:
          node_count_dynamic_max: 20
          bandwidth_tier: gvnic_enabled
          allow_automatic_updates: false
    
      - id: compute_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use:
        - compute_nodeset
        settings:
          partition_name: compute
    
      - id: h3_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network]
        settings:
          node_count_dynamic_max: 20
          # Note that H3 is available in only specific zones. https://cloud.google.com/compute/docs/regions-zones
          machine_type: h3-standard-88
          # H3 does not support pd-ssd and pd-standard
          # https://cloud.google.com/compute/docs/compute-optimized-machines#h3_disks
          disk_type: pd-balanced
          bandwidth_tier: gvnic_enabled
          allow_automatic_updates: false
    
      - id: h3_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use:
        - h3_nodeset
        settings:
          partition_name: h3
    
      - id: slurm_login
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-login
        use: [network]
        settings:
          machine_type: n2-standard-4
          enable_login_public_ips: true
    
      - id: slurm_controller
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
        use:
        - network
        - debug_partition
        - compute_partition
        - h3_partition
        - homefs
        - slurm_login
        settings:
          enable_controller_public_ips: true
    

### Example 2

Deploys a cluster with Slurm that has a tiered file systems for higher performance. It connects to the default Virtual Private Cloud of the project and creates seven partitions and a login node.
    
    
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    ---
    
    blueprint_name: hpc-enterprise-slurm-v6
    
    vars:
      project_id:  ## Set GCP Project ID Here ##
      deployment_name: hpc01
      region: us-central1
      zone: us-central1-a
      gpu_zones: [us-central1-a, us-central1-b, us-central1-c, us-central1-f]
      lustre_instance_id: lustre-hpc
      slurm_image:
        # Visit https://github.com/GoogleCloudPlatform/slurm-gcp/blob/master/docs/images.md#published-image-family
        # for a list of valid family options with Slurm
        # Rocky 8: slurm-gcp-6-12-hpc-rocky-linux-8
        # Rocky 9: slurm-gcp-6-12-hpc-rocky-linux-9
        family: slurm-gcp-6-12-hpc-rocky-linux-9
        project: schedmd-slurm-public
      # If image above is changed to use custom image, then setting below must be set to true
      instance_image_custom: false
      metadata: # Workaround for https://github.com/GoogleCloudPlatform/cluster-toolkit/discussions/3243
        VmDnsSetting: GlobalOnly
    
    # Recommended to use GCS backend for Terraform state
    # See https://github.com/GoogleCloudPlatform/hpc-toolkit/tree/main/examples#optional-setting-up-a-remote-terraform-state
    #
    # terraform_backend_defaults:
    #  type: gcs
    #  configuration:
    #    bucket: <<BUCKET_NAME>>
    
    # Documentation for each of the modules used below can be found at
    # https://github.com/GoogleCloudPlatform/hpc-toolkit/blob/main/modules/README.md
    
    deployment_groups:
    - group: primary
      modules:
      # Source is an embedded module, denoted by "modules/*" without ./, ../, /
      # as a prefix. To refer to a local or community module, prefix with ./, ../ or /
      - id: network
        source: modules/network/vpc
    
      # Private Service Access (PSA) requires the compute.networkAdmin role which is
      # included in the Owner role, but not Editor.
      # PSA is a best practice for Filestore instances, but can be optionally
      # removed by deleting the private_service_access module and any references to
      # the module by Filestore modules.
      # https://cloud.google.com/vpc/docs/configure-private-services-access#permissions
      - id: private_service_access
        source: modules/network/private-service-access
        use: [network]
    
      - id: controller_sa
        source: modules/project/service-account
        settings:
          name: controller
          project_roles:
          - bigquery.dataOwner # needed if enable_bigquery_load is enabled
          - compute.instanceAdmin.v1
          - iam.serviceAccountUser
          - logging.logWriter
          - monitoring.metricWriter
          - storage.objectViewer
    
      - id: login_sa
        source: modules/project/service-account
        settings:
          name: login
          project_roles:
          - logging.logWriter
          - monitoring.metricWriter
          - storage.objectViewer
    
      - id: compute_sa
        source: modules/project/service-account
        settings:
          name: compute
          project_roles:
          - logging.logWriter
          - monitoring.metricWriter
          - storage.objectUser
    
      - id: homefs
        source: modules/file-system/filestore
        use: [network, private_service_access]
        settings:
          local_mount: /home
    
      - id: projectsfs
        source: modules/file-system/filestore
        use: [network, private_service_access]
        settings:
          local_mount: /projects
    
      - id: lustre-gcp
        source: modules/file-system/managed-lustre
        use: [network, private_service_access]
        settings:
          name: $(vars.lustre_instance_id)
          local_mount: /lustre
          remote_mount: lustrefs
          size_gib: 36000
    
      - id: n2_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network, compute_sa]
        settings:
          node_count_dynamic_max: 4
          machine_type: n2-standard-2
          instance_image: $(vars.slurm_image)
          allow_automatic_updates: false
    
      - id: n2_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use: [n2_nodeset]
        settings:
          partition_name: n2
          exclusive: false  # allows nodes to stay up after jobs are done
          is_default: true
          partition_conf:
            SuspendTime: 300 # time (in secs) the nodes in this partition stay active after their tasks have completed
    
      - id: c2_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network, compute_sa]
        settings:
          node_count_dynamic_max: 20
          machine_type: c2-standard-60  # this is the default
          bandwidth_tier: tier_1_enabled
          instance_image: $(vars.slurm_image)
          disk_type: pd-ssd
          disk_size_gb: 100
          allow_automatic_updates: false
    
      # use `-p c2` to submit jobs to this partition:
      # ex: `srun -p c2 -N 1 hostname`
      - id: c2_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use: [c2_nodeset]
        settings:
          partition_name: c2
          # the following two are true by default
          exclusive: true
    
      - id: c2d_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network, compute_sa]
        settings:
          node_count_dynamic_max: 20
          machine_type: c2d-standard-112
          instance_image: $(vars.slurm_image)
          bandwidth_tier: tier_1_enabled
          disk_type: pd-ssd
          disk_size_gb: 100
          allow_automatic_updates: false
    
      - id: c2d_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use: [c2d_nodeset]
        settings:
          partition_name: c2d
    
      - id: c3_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network, compute_sa]
        settings:
          node_count_dynamic_max: 20
          machine_type: c3-highcpu-176
          instance_image: $(vars.slurm_image)
          bandwidth_tier: tier_1_enabled
          disk_type: pd-ssd
          disk_size_gb: 100
          allow_automatic_updates: false
    
      - id: c3_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use: [c3_nodeset]
        settings:
          partition_name: c3
    
      - id: a2_8_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network, compute_sa]
        settings:
          node_count_dynamic_max: 16
          machine_type: a2-ultragpu-8g
          # This makes this nodeset look for machines in any of the following zones
          # https://github.com/GoogleCloudPlatform/hpc-toolkit/tree/develop/community/modules/compute/schedmd-slurm-gcp-v6-nodeset#compute-vm-zone-policies
          zones: $(vars.gpu_zones)
          bandwidth_tier: gvnic_enabled
          instance_image: $(vars.slurm_image)
          disk_type: pd-ssd
          disk_size_gb: 100
          node_conf:
            SocketsPerBoard: 2
            CoresPerSocket: 24
          allow_automatic_updates: false
    
      # use `-p a208` to submit jobs to this partition:
      # ex: `srun -p a208 --gpus-per-node=8 -N 1 nvidia-smi`
      - id: a2_8_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use: [a2_8_nodeset]
        settings:
          partition_name: a208
          # The following allows users to use more host memory without specifying cpus on a job
          partition_conf:
            DefMemPerGPU: 160000
            DefMemPerCPU: null
    
      - id: a2_16_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network, compute_sa]
        settings:
          node_count_dynamic_max: 16
          machine_type: a2-megagpu-16g
          # This makes this nodeset look for machines in any of the following zones
          # https://github.com/GoogleCloudPlatform/hpc-toolkit/tree/develop/community/modules/compute/schedmd-slurm-gcp-v6-nodeset#compute-vm-zone-policies // !!!
          zones: $(vars.gpu_zones)
          bandwidth_tier: gvnic_enabled
          instance_image: $(vars.slurm_image)
          disk_type: pd-ssd
          disk_size_gb: 100
          node_conf:
            SocketsPerBoard: 2
            CoresPerSocket: 24
          allow_automatic_updates: false
    
      # use `-p a216` to submit jobs to this partition:
      # ex: `srun -p a216 --gpus-per-node=16 -N 1 nvidia-smi`
      - id: a2_16_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use: [a2_16_nodeset]
        settings:
          partition_name: a216
          # The following allows users to use more host memory without specifying cpus on a job
          partition_conf:
            DefMemPerGPU: 160000
            DefMemPerCPU: null
    
      - id: h3_nodeset
        source: community/modules/compute/schedmd-slurm-gcp-v6-nodeset
        use: [network, compute_sa]
        settings:
          node_count_dynamic_max: 16
          # Note that H3 is available in only specific zones. https://cloud.google.com/compute/docs/regions-zones
          machine_type: h3-standard-88
          bandwidth_tier: gvnic_enabled  # https://cloud.google.com/compute/docs/compute-optimized-machines#h3_network
          instance_image: $(vars.slurm_image)
          # H3 does not support pd-ssd and pd-standard
          # https://cloud.google.com/compute/docs/compute-optimized-machines#h3_disks
          disk_type: pd-balanced
          disk_size_gb: 100
          allow_automatic_updates: false
    
      # use `-p h3` to submit jobs to this partition:
      # ex: `srun -p h3  -N 1 hostname`
      - id: h3_partition
        source: community/modules/compute/schedmd-slurm-gcp-v6-partition
        use: [h3_nodeset]
        settings:
          partition_name: h3
    
      - id: slurm_login
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-login
        use: [network, login_sa]
        settings:
          instance_image: $(vars.slurm_image)
          machine_type: n2-standard-4
          # we recommend disabling public IPs if possible
          # but that requires your network to have a NAT or
          # private access configured
          enable_login_public_ips: false
    
      - id: slurm_controller
        source: community/modules/scheduler/schedmd-slurm-gcp-v6-controller
        use: [network, controller_sa, homefs, projectsfs, lustre-gcp, slurm_login,
              n2_partition, c2_partition, c2d_partition, c3_partition, a2_8_partition, a2_16_partition, h3_partition]
        settings:
          instance_image: $(vars.slurm_image)
          # the following allow for longer boot time
          # which is useful for large GPU nodes
          cloud_parameters:
            no_comma_params: false
            resume_rate: 0
            resume_timeout: 600
            suspend_rate: 0
            suspend_timeout: 600
          # we recommend disabling public IPs if possible
          # but that requires your network to have a NAT or
          # private access configured
          enable_controller_public_ips: false
    
      - id: hpc_dashboard
        source: modules/monitoring/dashboard
        outputs: [instructions]
    

## Request additional quotas

You might need to request additional quota to be able to deploy and use your cluster.

For example, by default, the [`schedmd-slurm-gcp-v6-nodeset` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/community/modules/compute/schedmd-slurm-gcp-v6-nodeset) uses `c2-standard-30` Compute Engine instances for compute nodes. The default quota for C2 instances might be as low as 8, which might prevent even a single node from being started.

The required quotas are based on your custom configuration. Minimum quotas are [documented on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples#readme) for the provided example blueprints.

To view and adjust quotas, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

## What's next

  * To view the available blueprints in Cluster Toolkit, see [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog).
  * To set up your environment, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * To learn about the deployment process, see [Cluster deployment overview](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview).
  * To change the functionality of your blueprints using modules, see [Modules](https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
