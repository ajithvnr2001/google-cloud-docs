---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/cloud-storage-bucket/
title: Create a Cloud Storage bucket \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:53.838505+00:00
---

# Create a Cloud Storage bucket  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/cloud-storage-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Cloud Storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

Use the `cloud-storage-bucket` module to create a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets).

This module lets your Compute Engine instances, including bare metal instances, store and retrieve data globally. You can mount these buckets directly to your file system by using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview).

For a complete list of all available input fields and output values, see the [`cloud-storage-bucket` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/cloud-storage-bucket#inputs) on GitHub.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. To view a working example of a blueprint configured for the `cloud-storage-bucket` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select storage type** menu and then select **Cloud Storage**. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).



### Required roles

To get the permissions that you need to create and mount Cloud Storage buckets, ask your administrator to grant you the following IAM roles on your project: 

  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud Storage bucket

To create a Cloud Storage bucket, add the `cloud-storage-bucket` module to your blueprint.

The following example creates a bucket with a name similar to `simulation-results-RANDOM_SUFFIX`, where the `RANDOM_SUFFIX` value is a randomly generated ID.
    
    
      - id: bucket
        source: modules/file-system/cloud-storage-bucket
        settings:
          name_prefix: simulation-results
          random_suffix: true
    

### Configure the bucket name

Cloud Storage buckets share a global namespace across all users, which increases the likelihood of naming conflicts. To help you create unique names, the module divides the bucket name into three configurable parts. You can configure these parts as follows:

  * **Custom prefix:** Use the `name_prefix` setting to define a custom string at the beginning of the name.
  * **Deployment name:** The module includes the deployment name by default. To exclude it, set the field value `use_deployment_name_in_bucket_name: false`.
  * **Random suffix:** The module excludes a random suffix by default. To append a random ID, set the field value `random_suffix: true`.



If you don't provide a custom prefix, exclude the deployment name, and disable the random suffix, the module assigns a default name. In this case, the bucket name is `no-bucket-name-provided`.

**Warning:** If you create a bucket with a value `random_suffix: true` and attempt to use the bucket in a startup script within the same deployment group, then Terraform returns a `not known at apply time` error. To resolve this error, either create the bucket in a separate deployment group or set the field `random_suffix` to `false`.

### Enable hierarchical namespace

To organize your data with a logical file system structure and improve directory performance for Cloud Storage FUSE workloads, set the `enable_hierarchical_namespace` field to `true`. You must configure this setting when you first create the bucket.

For more information, see the [Cloud Storage hierarchical namespace documentation](https://docs.cloud.google.com/storage/docs/hns-overview).

The following example creates a bucket with a hierarchical namespace enabled:
    
    
      - id: bucket
        source: modules/file-system/cloud-storage-bucket
        settings:
          enable_hierarchical_namespace: true
    

### Configure soft delete

To protect your data from accidental deletion, you can specify how long deleted objects are retained by using the `soft_delete_retention_duration` setting. You can provide a value from `604800` seconds (7 days) to `7776000`seconds (90 days), or set the field to `0` to disable the feature entirely.

For more information, see the [Cloud Storage soft delete documentation](https://docs.cloud.google.com/storage/docs/soft-delete).

The following example creates a bucket with a retention duration of 7 days:
    
    
      - id: bucket
        source: modules/file-system/cloud-storage-bucket
        settings:
          soft_delete_retention_duration: 604800
    

## Mount the bucket

To mount the Cloud Storage bucket, you must install the Cloud Storage FUSE client and execute the proper mount command. Cluster Toolkit offers two methods for mounting the bucket: automatic mounting or manual mounting.

### Automatic mounting

When you connect the `cloud-storage-bucket` module to a compatible compute module by using the `use` keyword, Cluster Toolkit automatically handles client installation and mounting.

For a complete list of supported modules, see the [compatibility matrix](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/network_storage.md#compatibility-matrix) on GitHub.

### Manual mounting

If you need to mount the storage manually, such as in a custom startup script, then you can use the `client_install_runner` and `mount_runner` outputs from the module.

The following example uses the `startup-script` module to install the client and mount the file system to the `/data` directory.
    
    
      - id: bucket
        source: modules/file-system/cloud-storage-bucket
        settings: {local_mount: /data}
    
      - id: mount-at-startup
        source: modules/scripts/startup-script
        settings:
          runners:
          - $(bucket.client_install_runner)
          - $(bucket.mount_runner)
    

## Configure Rapid Cache

You can configure the `cloud-storage-bucket` module to use Rapid Cache. Rapid Cache is a fully managed service that caches Cloud Storage data within Google Cloud.

To enable this feature, configure the `anywhere_cache` block in your module settings. You can define the following properties:

  * **Zones:** Provide a list of zones by using the `zones` field. The zones must be within the location of your bucket. For example, if your bucket is located in the `us-east1` region, you can create a cache in the `us-east1-b` zone, but not in the `us-central1-c` zone. If your bucket is located in the `ASIA` dual-region, then you can create a cache in any zones that make up the `asia-east1` region and the `asia-southeast1` region.
  * **Time to live (TTL):** Set the time to live by using the `ttl` field. The value must be between 1 day (the `86400s` value) and 7 days (the `604800s` value). The module defaults to the `86400s` value.
  * **Admission policy:** Choose an admission policy by using the `admission_policy` field. Use the possible values of `admit-on-first-miss` or `admit-on-second-miss`. The module defaults to the `admit-on-first-miss` policy.



The following example creates a bucket with Rapid Cache enabled in two zones:
    
    
      - id: bucket
        source: modules/file-system/cloud-storage-bucket
        settings:
          region: us-east1
          anywhere_cache:
            zones: ["us-east1-b", "us-east1-c"]
            ttl: "86400s"
            admission_policy: "admit-on-first-miss"
    
    

### Configure the creation timeout

Cache creation operations take time to complete. You can adjust the timeout duration by using the `anywhere_cache_create_timeout` setting. You can provide a duration string, such as `1h` or `30m`. The module defaults to the `240m` duration (4 hours). The maximum creation time is 48 hours.

For more information about this service, see the [Rapid Cache documentation](https://docs.cloud.google.com/storage/docs/anywhere-cache).

## What's next

  * For a complete list of all available input fields and output values, see the [`cloud-storage-bucket` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/cloud-storage-bucket#inputs) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
