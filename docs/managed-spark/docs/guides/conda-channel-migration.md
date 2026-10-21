---
url: https://docs.cloud.google.com/managed-spark/docs/guides/conda-channel-migration/
title: Migrate and set up Conda channels \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:48.290251+00:00
---

# Migrate and set up Conda channels  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/conda-channel-migration/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Migrate and set up Conda channels Stay organized with collections  Save and categorize content based on your preferences. 

Preconfigured Conda package channels are being removed from Managed Service for Apache Spark cluster images and serverless runtimes. This document describes how you can migrate and configure Conda channels for your workloads.

## Removal of preconfigured Conda channels

Previously, Managed Service for Apache Spark images bundled preconfigured Conda channels, such as Anaconda's `defaults` repository. Due to licensing changes, Managed Service for Apache Spark is removing all preconfigured channel pointers from all past and future Managed Service for Apache Spark images and serverless runtimes.

  * **What changes:** Commands that run `conda install PACKAGE` without an explicitly supplied channel no longer resolve packages against default repositories, and fail.
  * **What doesn't change:** Standard Python package installations from PyPI (`pip install PACKAGE` or the `dataproc:pip.packages` cluster property) are completely unaffected.



### Availability of channels-free lateral images

To help developers adapt to this update, Managed Service for Apache Spark has released channels-free subminor versions as listed in the following table. These images maintain 100% binary and component compatibility with existing images, differing only in the removal of the preconfigured Conda channels.

Image track | Legacy or affected versions | Published Conda-free lateral version | Status and compatibility  
---|---|---|---  
1.3 | `<= 1.3.95` | `1.3.96` | 100% compatible with `1.3.95`; Conda channels removed  
1.4 | `<= 1.4.80` | `1.4.81` | 100% compatible with `1.4.80`; Conda channels removed  
1.5 | `<= 1.5.90` | `1.5.92` | 100% compatible with `1.5.90`; Conda channels removed  
2.0 | `<= 2.0.160` | `2.0.161` | 100% compatible with `2.0.160`; Conda channels removed  
2.1 | `<= 2.1.116` | `2.1.117`, and `2.1.119` and later | Supported release; Conda channels removed  
2.2 | `<= 2.2.84` | `2.2.85`, and `2.2.87` and later | Supported release; Conda channels removed  
2.3 | `<= 2.3.31` | `2.3.32`, and `2.3.36` and later | Supported release; Conda channels removed  
  
### How the removal affects workloads

  * **Unpinned clusters:** Any cluster creation script that specifies an image version alias (such as `--image-version=2.2-debian12`) automatically receives the new channels-free image.
  * **Pinned or custom images:** Clusters pinned to earlier subminor releases or that use custom images continue to reference old channel configurations unless updated. If you use pinned images, you must request an extension to secure additional time and migrate to supported, channels-free versions.
  * **Execution failure:** Any initialization action, pipeline script, or job that submits `conda install PACKAGE` without specifying a channel fails with channel resolution errors.



## How to configure Conda channels

If your workloads depend on Conda to install binary packages, you must explicitly declare your channel by using one of the following options. To specify channels in Conda-related cluster properties instead, see [Use conda-related cluster properties](https://docs.cloud.google.com/managed-spark/docs/tutorials/python-configuration#use-conda-properties).

**Note:** Google Cloud doesn't provide a commercial Anaconda license for repository access. If you choose to download packages from `repo.anaconda.com`, you must ensure compliance with Anaconda's terms of service and license agreements.

### Option 1: Explicit command-line flag

This option is recommended for ad hoc installs. Pass the `--channel` flag when you run `conda install`:
    
    
    conda install --channel conda-forge PACKAGE
    

Or use the short `-c` flag:
    
    
    conda install -c conda-forge PACKAGE
    

Replace PACKAGE with the name of the package to install.

### Option 2: Cluster initialization actions

This option is recommended for automated environments. Add a custom [initialization action](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions) that preconfigures the channel that you want to use in the `.condarc` configuration file:
    
    
    #!/bin/bash
    # Preconfigure the community conda-forge channel or a private enterprise repository.
    conda config --add channels conda-forge
    conda config --set channel_priority strict
    

## Migrate from legacy images (1.x and 2.0)

Managed Service for Apache Spark versions 1.3, 1.4, 1.5, and 2.0 have been unsupported for an extended period. Running earlier images introduces significant operational and security risks, including known Common Vulnerabilities and Exposures (CVEs) in underlying operating systems and open source software (OSS) dependencies.

  * Google Cloud is permanently turning down image creation for the 1.x and 2.0 tracks.
  * All initialization actions available in the [GoogleCloudDataproc/initialization-actions](https://github.com/GoogleCloudDataproc/initialization-actions) GitHub repository that support only these deprecated images (1.x and 2.0) will also be removed.
  * **All workloads must migrate to the Conda channels-free lateral images by October 15, 2026**.
  * **All workloads must ultimately migrate to active, supported versions (2.1, 2.2, 2.3, or 3.0 and later)**.



For more information, see [Unsupported Managed Service for Apache Spark image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-version-lists#unsupported-image-versions).

## Available extensions

Managed Service for Apache Spark provides two extension pathways through an opt-in allowlist, which requires approval by the service team.

### Extension types

The following extension types are available.

#### Temporary Conda workaround extension

  * **Validity:** Up to October 31, 2026 maximum.
  * **Purpose:** Provides an immediate operational buffer for customers whose automated deployments or initialization actions break due to the default image alias switch on August 25, 2026 and September 1, 2026.
  * **Benefit:** Lets projects temporarily retain previous behavior while modifying scripts to include `--channel` or transitioning to channels-free images.

**Note:** This extension applies only if image versions are pinned during cluster creation. If image aliases are used, the new default images without Conda channels are used automatically, even if the extension is approved.

#### Legacy image deprecation extension

  * **Validity:** Up to December 31, 2026.
  * **Purpose:** For mission-critical workloads running on 1.x or 2.0 that can't immediately refactor code for Spark 3.x or newer OS environments.
  * **Benefit:** Lets you continue to create clusters on legacy tracks through the end of 2026, preventing immediate production halts.
  * **Prerequisite:** You can obtain this extension only if your current 1.x and 2.0 workloads use Conda-compliant lateral images.



### Extension requirements

Extensions are governed by compliance and infrastructure constraints. To be approved, you must meet all of the following requirements:

  * **Existing projects only:** Extensions apply strictly to Google Cloud project IDs that have an active history of running these versions before August 2026. New projects won't be added to the allowlist.
  * **Mandatory lateral image swap by October 31, 2026:** If you're granted an extension on 1.x or 2.0, you must transition your cluster creation configurations to the lateral Conda-compliant subminor versions (`1.3.96`, `1.4.81`, `1.5.92`, and `2.0.161`) no later than October 31, 2026.
  * **No`global` region usage:** For image versions 1.5 and earlier, clusters must not be deployed to the legacy `global` region. Workloads must use specific regional endpoints (for example, `us-central1` or `europe-west1`).
  * **Committed migration roadmap:** You must have an active modernization plan to move workloads to Conda-compliant supported versions (2.2 and later, or 3.0) before the December 31, 2026 deadline.



### How to request an extension

To request placement on the extension allowlist, submit a request through any of the following channels:

  * **Email:** Send your request directly to [dataproc-msa-support@google.com](mailto:dataproc-msa-support@google.com).
  * **Support case:** File a case with [Cloud Customer Care](https://docs.cloud.google.com/support) that references the **Dataproc Conda Deprecation MSA**.
  * **Account team:** Contact your dedicated Google Cloud Technical Account Manager (TAM) or Customer Engineer (CE).



Include the following information in your request:

  * Google Cloud organization name
  * Target Google Cloud project IDs and project numbers
  * Affected cluster names or UUIDs
  * Current image versions in use
  * Reason for the extension request and the targeted migration completion date



## Checklist for compliant Conda channels

Complete the following priorities in order.

### Priority 1: Workload discovery and inventory

  * **Identify deprecated images:** Audit your organization's projects for any clusters running on 1.3, 1.4, 1.5, or 2.0.

The following command lists the image version of active clusters in a region:
        
        gcloud dataproc clusters list --region=REGION \
            --format="table(clusterName, status.state, config.softwareConfig.imageVersion)"
        

Replace REGION with the region where your clusters are located.

  * **Audit Conda usage:** Review your initialization actions (`--initialization-actions`), startup scripts, and job submission scripts for any invocations of `conda install`.




### Priority 2: Immediate failure triage

If you're experiencing outages, do the following:

  * If automated pipelines fail due to missing Conda packages, immediately patch the initialization action or script by adding `--channel conda-forge` (or `-c conda-forge`):
        
        conda install -c conda-forge PACKAGE
        

  * If cluster creation fails due to deprecated image blocks, immediately contact [dataproc-msa-support@google.com](mailto:dataproc-msa-support@google.com) or your TAM to request temporary allowlist enrollment.




### Priority 3: Execute a lateral subminor swap

This step requires zero code changes.

  * For pipelines that can't immediately upgrade to image version 2.2 or later, update your cluster creation templates (for example, Terraform, Apache Airflow `DataprocCreateClusterOperator`, Managed Service for Apache Airflow, and CI/CD scripts) to use the channels-free lateral version:

    * Replace `1.3.*` with `1.3.96`.
    * Replace `1.4.*` with `1.4.81`.
    * Replace `1.5.*` with `1.5.92`.
    * Replace `2.0.*` with `2.0.161`.
  * **Why this works:** These images contain the same versions of Apache Spark, Apache Hadoop, Apache Hive, and Java as earlier subminor versions. They guarantee 100% application compatibility without requiring any code changes.




### Priority 4: Recreate long-running clusters

If you have static, long-running clusters deployed on earlier images, schedule a maintenance window to [recreate them](https://docs.cloud.google.com/managed-spark/docs/guides/recreate-cluster) using the latest lateral subminor versions (or Conda-compliant supported 2.x or 3.x versions). Recreating the clusters ensures that they pick up all critical security and configuration updates.

### Priority 5: Plan a full upgrade to supported versions

Target completion for this priority is Q4 2026.

  * Establish testing environments on image version [2.2](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-2.2) (Debian 12, Spark 3.5) or image version [3.0](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/image-release-3.0), which is generally available (GA).
  * Validate PySpark, Scala, and Java jobs against Spark 3.x API specifications.
  * If you need dedicated modernization support, use Google Cloud Professional Services Organization (PSO) or certified migration partners, such as Wipro and HCL.



## Frequently asked questions

The following sections answer frequently asked questions about the Conda channel removal.

### General and background

The following questions explain why these changes are happening and how they differ from each other.

#### Why is Managed Service for Apache Spark removing preconfigured Conda channels?

Due to changes in the licensing requirements, Managed Service for Apache Spark is decoupling its services from proprietary Anaconda channels and moving to standard open source packaging mechanisms.

#### What's the difference between Conda channel removal and image deprecation?

  * **Conda channel removal** affects all Managed Service for Apache Spark versions, including actively supported versions 2.1, 2.2, and 2.3, and serverless runtimes. It removes default pointers to Anaconda repositories.
  * **Image deprecation** specifically affects legacy 1.x and 2.0 images. These images have reached end of life, no longer receive security patches, and will be blocked from cluster creation.



### Technical and compatibility issues

The following questions cover how the changes affect Python package installation, Conda usage, and image compatibility.

#### Does this change affect `pip install` or `dataproc:pip.packages`?

No. Standard Python package installations using `pip` or the Managed Service for Apache Spark cluster property `dataproc:pip.packages` pull directly from the Python Package Index (PyPI). PyPI is completely independent of Conda and isn't affected in any way.

#### Can my organization continue using Anaconda or Conda packages?

Yes. You're free to continue using Conda to manage your environments. However, you must explicitly supply the repository channel. You can point to the community-supported `conda-forge` channel (by adding `-c conda-forge`) or point to your organization's private, licensed Anaconda repository mirror by using initialization actions.

#### What exact error occurs if my script isn't updated?

When you run `conda install PACKAGE` on a channels-free image, Conda returns an error indicating that no channels are configured or that the requested package can't be found in the default search paths. For example: `PackagesNotFoundError: The following packages are not available from current channels`.

#### What is a lateral subminor image, and why should I use it?

A lateral subminor image (such as `1.5.92` for the 1.5 track or `2.0.161` for the 2.0 track) is an image release where the core big data ecosystem components (Hadoop, Spark, Hive, Presto, and Java runtimes) remain identical to earlier releases in that track, but the underlying Conda channels have been removed. Upgrading to a lateral subminor version requires zero code changes for your Spark jobs.

### Deployments and ecosystem

The following questions cover how the changes affect serverless workloads, Google Kubernetes Engine (GKE) deployments, and managed orchestration services.

#### How does this affect Managed Service for Apache Spark serverless?

Starting August 25, 2026, newly submitted serverless batch workloads run on base runtime images that don't contain preconfigured Conda channels. If you package dependencies using custom container images or Conda environment tarballs, ensure that your build definitions specify `--channel conda-forge` or your private channel.

#### How does this affect Managed Service for Apache Spark on Google Kubernetes Engine?

Managed Service for Apache Spark on GKE images have been updated to remove preconfigured Conda channels (for example, runtime image `3.5-dataproc-28` and subsequent releases). Custom container Dockerfiles that run `conda install` must be updated to pass an explicit `--channel`.

#### Are managed orchestrators such as Managed Service for Apache Airflow or Cloud Data Fusion affected?

Default, standard pipelines managed by Managed Airflow or Cloud Data Fusion that invoke built-in Managed Service for Apache Spark cluster creation tasks are unaffected, unless your workflow relies on custom initialization actions that run unflagged `conda install` commands or pins deprecated 1.x or 2.0 images.

### Support and assistance

The following question describes where to get help with your migration.

#### Where can I get technical assistance for my migration?

  * For technical troubleshooting and allowlist requests, contact [dataproc-msa-support@google.com](mailto:dataproc-msa-support@google.com) or open a case with [Cloud Customer Care](https://docs.cloud.google.com/support).
  * For enterprise migration assistance, the Google Cloud PSO offers structured modernization packages, and certified systems integrator (SI) partners, including Wipro and HCL, provide dedicated migration services that are eligible for Partner Service Funds (PSF).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
