---
url: https://docs.cloud.google.com/managed-spark/docs/guides/best-practices/
title: Managed Service for Apache Spark best practices for production \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:02.925595+00:00
---

# Managed Service for Apache Spark best practices for production  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/best-practices/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark best practices for production Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses Managed Service for Apache Spark best practices that can help you run reliable, efficient, and insightful data processing jobs on Managed Service for Apache Spark clusters in production environments.

## Specify cluster image versions

Managed Service for Apache Spark uses [image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions) to bundle operating system, big data [components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview), and Google Cloud connectors into a package that is deployed on a cluster. If you don't specify an image version when creating a cluster, Managed Service for Apache Spark defaults to the most recent stable image version.

For production environments, associate your cluster with a specific `major.minor` Managed Service for Apache Spark image version, as shown in the following gcloud CLI command.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=region \
        --image-version=2.0
    

Dataproc resolves the `major.minor` version to the latest sub-minor version version (`2.0` is resolved to `2.0.x`). Note: if you need to rely on a specific sub-minor version for your cluster, you can specify it: for example, `--image-version=2.0.x`. See [How versioning works](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/overview#how_versioning_works) for more information.

Each supported minor image version page, such as [2.0.x release versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.0), lists the component versions available with the current and previous four sub-minor image releases.

### Managed Service for Apache Spark preview image versions

New minor versions of Managed Service for Apache Spark images are available in a `preview` version prior to release in the standard minor image version track. Use a preview image to test and validate your jobs against a new minor image version prior to adopting the standard minor image version in production. See [Managed Service for Apache Spark versioning](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/overview) for more information.

## Use custom images when necessary

If you have dependencies to add to the cluster, such as native Python libraries, or security hardening or virus protection software, [create a custom image](https://docs.cloud.google.com/managed-spark/docs/guides/dataproc-images) from the **latest image** in your target minor image version track. This practice allows you to meet dependency requirements when you create clusters using your custom image. When you rebuild your custom image to update dependency requirements, use the latest available sub-minor image version within the minor image track.

## Submit jobs to Managed Service for Apache Spark

Submit jobs to Managed Service for Apache Spark with a [jobs.submit](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs/submit) call using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/jobs/submit) or the Google Cloud console. Set job and cluster permissions by granting [Managed Service for Apache Spark roles](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/iam#roles). Use custom roles to separate cluster access from job submit permissions.

Benefits of submitting jobs to Managed Service for Apache Spark:

  * No complicated networking settings required - the API is widely reachable
  * Easy to manage IAM permissions and roles
  * Track job status easily - no Managed Service for Apache Spark job metadata to complicate results.



In production, run jobs that only depend on cluster-level dependencies at a fixed minor image version, (for example, `--image-version=2.0`). Bundle dependencies with jobs when the jobs are submitted. Submitting an [uber jar](https://imagej.net/Uber-JAR) to Spark or MapReduce is a common way to do this.

  * Example: If a job jar depends on `args4j` and `spark-sql`, with `args4j` specific to the job and `spark-sql` a cluster-level dependency, bundle `args4j` in the job's uber jar.



## Control initialization action locations

[Initialization actions](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions) allow you to automatically run scripts or install components when you create a Managed Service for Apache Spark cluster (see the [dataproc-initialization-actions](https://github.com/GoogleCloudPlatform/dataproc-initialization-actions) GitHub repository for common Managed Service for Apache Spark initialization actions). When using cluster initialization actions in a production environment, copy initialization scripts to Cloud Storage rather than sourcing them from a public repository. This practice avoids running initialization scripts that are subject to modification by others.

## Monitor Managed Service for Apache Spark release notes

Managed Service for Apache Spark regularly releases new sub-minor image versions. View or subscribe to [Managed Service for Apache Spark release notes](https://docs.cloud.google.com/managed-spark/docs/release-notes) to be aware of the latest Managed Service for Apache Spark image version releases and other announcements, changes, and fixes.

## View the staging bucket to investigate failures

  1. Look at your cluster's [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/staging-bucket) to investigate cluster and job error messages. Typically, the staging bucket Cloud Storage location is shown in error messages, as shown in the **bold** text in the following sample error message:
         
         ERROR:
         (gcloud.dataproc.clusters.create) Operation ... failed:
         ...
         - Initialization action failed. Failed action ... see output in:
         **gs://dataproc- <BUCKETID>-us-central1/google-cloud-dataproc-metainfo/CLUSTERID/<CLUSTER_ID>\dataproc-initialization-script-0_output**
          

  2. Use the gcloud CLI to view staging bucket contents: 
         
         gcloud storage cat gs://STAGING_BUCKET
         

Sample output: 
         
         + readonly RANGER_VERSION=1.2.0
         ... Ranger admin password not set. Please use metadata flag - default-password
         




## Get support

Google Cloud supports your production OSS workloads and helps you meet your business SLAs through [tiers of support](https://docs.cloud.google.com/support). Also, Google Cloud [Consulting Services](https://docs.cloud.google.com/consulting) can provide guidance on best practices for your team's production deployments.

## For more information

  * Read the Google Cloud blog [Managed Service for Apache Spark best practices guide](https://cloud.google.com/blog/topics/developers-practitioners/dataproc-best-practices-guide).

  * View [Democratizing Managed Service for Apache Spark](https://www.youtube.com/watch?v=2ksD7udWFys) on YouTube.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
