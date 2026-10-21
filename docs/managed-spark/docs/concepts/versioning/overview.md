---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/overview/
title: Managed Service for Apache Spark cluster image versions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:29.000733+00:00
---

# Managed Service for Apache Spark cluster image versions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/overview/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark cluster image versions Stay organized with collections  Save and categorize content based on your preferences. 

Managed Service for Apache Spark on clusters uses images to tie together useful Google Cloud connectors and Apache Spark & Apache Hadoop components into one package that can be deployed on a Managed Service for Apache Spark cluster. These images contain the base operating system (Debian or Ubuntu) for the cluster, along with [core and optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview) needed to run jobs, such as Spark, Hadoop, and Hive. These images are periodically upgraded to include new improvements and features. Managed Service for Apache Spark versioning lets you select sets of software versions when you create clusters.

## How versioning works

When an image is created, it is given an [image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions) number in the following format:

`version_major.version_minor.version_sub_minor-os_distribution`

The following OS distributions are maintained:

OS Distribution Code | OS Distribution  
---|---  
debian12 | Debian 12  
debian10 | Debian 10  
debian11 | Debian 11  
rocky8 | Rocky Linux 8  
rocky9 | Rocky Linux 9  
ubuntu18 | Ubuntu 18.04 LTS  
ubuntu20 | Ubuntu 20.04 LTS  
ubuntu22 | Ubuntu 22.04 LTS  
  
See old image versions for previously supported OS distributions.

The recommended practice is to specify the `major.minor` image version for production environments or when compatibility with specific component versions is important. The subminor and OS distributions are automatically set to the latest weekly release.

## Select versions

When you create a new Managed Service for Apache Spark cluster, the latest available **Debian** image version are used by default. You can select a Debian, Rocky Linux or Ubuntu image version when creating a cluster (see the [Managed Service for Apache Spark image version list](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions)). When specifying Debian-based images, you can omit the OS Distribution Code suffix, for example by specifying `2.0` to select the `2.0-debian10` image. The OS suffix **must** be used to select a Rocky Linux or Ubuntu-based image, for example by specifying `2.0-ubuntu18`.

### Google Cloud console

Open the[**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. In the **Define your cluster** section, the **Image type and version** drop-down field shows the image that will be used when creating the cluster. Initially, the default image, the latest available Debian version, is selected. Click the field to select from a list of available standard images or to select a custom image.

### gcloud CLI command

When using the `gcloud dataproc clusters create` command, you can use the `--image-version` argument to specify an image version for the new cluster.

**Debian image example:**
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --image-version=2.0 \
        --region=REGION
    

**Ubuntu image example:**
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --image-version=2.0-ubuntu18 \
        --region=REGION
    

Best practice is to omit the subminor version so that the latest subminor version is used. However, if necessary, the subminor version can be specified, for example, `2.0.20`.

You can check your current version with the Google Cloud CLI.
    
    
    gcloud dataproc clusters describe CLUSTER_NAME \
        --region=REGION
    

### REST API

You can specify the `SoftwareConfig` [imageVersion](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#SoftwareConfig) field as part of a [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) API request.

**Example**
    
    
    POST /v1/projects/project-id/regions/us-central1/clusters/
    {
      "projectId": "project-id",
      "clusterName": "example-cluster",
      "config": {
        "configBucket": "",
        "gceClusterConfig": {
          "subnetworkUri": "default",
          "zoneUri": "us-central1-b"
        },
        "masterConfig": {
          ...
          }
        },
        "workerConfig": {
          ...
          }
        },
        **"softwareConfig":** {
          **"imageVersion":** "2.0"
        }
      }
    }
      

## When new versions are created

New **major** versions are periodically created to incorporate one or more of the following:

  * Major releases for: 
    * Spark, Hadoop, and other Big Data components
    * Google Cloud connectors
  * Major changes or updates to Managed Service for Apache Spark functionality



New **preview** versions (with a `-RC` suffix) are released prior to the release of a new major version:

  * Preview images are not intended for use in production workloads.
  * Preview image component versions might be upgraded to the latest available component version in the post-preview GA image version.



New **minor** versions are periodically created to incorporate one or more of the following:

  * Minor releases and updates for: 
    * Spark, Hadoop, and other Big Data components
    * Google Cloud connectors
  * Minor changes or updates to Managed Service for Apache Spark functionality



When a new minor version is created, its Debian image becomes the default for the major version, and represents the latest release of the major version.

New **subminor** versions are periodically created to incorporate one or more of the following:

  * Patches or fixes for a component in the image
  * Component subminor version upgrades



## Image version and Managed Service for Apache Spark support

Minor image versions are supported for 24 months after initial GA (General Availability) release. During this period, clusters using these image versions are eligible for support (to receive fixes, recreate your cluster using the latest supported subminor image version). After the support window has closed, clusters using the image versions aren't eligible for support.

## Old image versions

### Previously supported OS distributions

The following OS distributions were previously supported:

OS Distribution Code | OS Distribution | Last Patched (End of support)  
---|---|---  
debian9 | Debian 9 | July 10, 2020  
deb8 | Debian 8 | October 26, 2018  
  
## Image versions without explicit OS distribution

Prior to August 16, 2018, image versions were built with Debian 8, and omitted the OS Distribution Code. They are specified in the following format:

`version_major.version_minor.version_sub_minor`

### Versions 0.1 and 0.2

Image versions released as alpha or beta releases prior to Managed Service for Apache Spark version `1.0` general availability aren't subject to the Managed Service for Apache Spark support policy.

## Important notes about versioning

  * Image versions contain the following components: 
    * [Core components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview) that are installed on all clusters, such as Spark, Hadoop, and Hive
    * [Optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components) that you specify when you create a cluster
  * Your Managed Service for Apache Spark clusters are not automatically updated when new image versions are released. 
    * **Recommendations:**
    * Run clusters with the latest [subminor image version](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#debian_images). Image metadata includes a `previous-subminor` label, which is set to `true` if the cluster is not using the latest subminor image version. 
      * To view image metadata: 
        1. Run the following [`gcloud compute images list --filter`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/list#--filter) command to list the resource name of a Managed Service for Apache Spark image. 
               
               gcloud compute images list --project=PROJECT_NAME --filter="labels.goog-dataproc-version ~ ^IMAGE_VERSION (such as 2.2.16-debian12)"
               

        2. Run the following [`gcloud compute images describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/describe) to view image metadata. 
               
               gcloud compute images describe --project=PROJECT_NAME IMAGE_NAME"
               

    * Test and validate that your applications run successfully on clusters created with new image versions, particularly when using new major image version releases.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
