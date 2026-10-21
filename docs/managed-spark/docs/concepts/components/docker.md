---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/docker/
title: Managed Service for Apache Spark optional Docker component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:41.203339+00:00
---

# Managed Service for Apache Spark optional Docker component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/docker/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional Docker component Stay organized with collections  Save and categorize content based on your preferences. 

To run Docker containers on your Managed Service for Apache Spark cluster nodes, enable the Docker optional component during cluster creation. This document explains how to install and configure the Docker component on Managed Service for Apache Spark.

To learn more about other available optional components in Managed Service for Apache Spark, see [Available optional components](https://docs.cloud.google.com/managed-spark/docs/concepts/components/overview#available_optional_components).

## How the Docker component works

When you enable the Managed Service for Apache Spark Docker component, it installs a [Docker daemon](https://docs.docker.com/get-started/overview/#the-docker-daemon) on each cluster node. It also sets up a Linux user and group, both named "docker", on each node to run the Docker daemon. Additionally, the component creates "docker" [`systemd`](https://docs.docker.com/config/daemon/systemd/) service to run the [`dockerd`](https://docs.docker.com/engine/reference/commandline/dockerd/) service. You should use this `systemd` service to manage the lifecycle of the Docker service.

## Install the component

Install the component when you create a Managed Service for Apache Spark cluster. The Docker component can be installed on clusters created with Managed Service for Apache Spark **image version 1.5 or later**.

See [Supported Managed Service for Apache Spark versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-versions#supported_cloud_dataproc_versions) for the component version included in each Managed Service for Apache Spark image release.

### Google Cloud console

  1. In the Google Cloud console, open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Optional components**.
  4. In the panel that opens, select the checkbox for **Docker** , then click **Save**.



### gcloud CLI

To create a Managed Service for Apache Spark cluster that includes the Docker component, use the [gcloud dataproc clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) cluster-name command with the `--optional-components` flag.
    
    
    gcloud dataproc clusters create cluster-name \
        --optional-components=DOCKER \
        --region=region \
        --image-version=1.5 \
        ... other flags
    

### REST API

The Docker component can be specified through the Dataproc API using [SoftwareConfig.Component](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#Component) as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

## Enable Docker on YARN

See [Customize your Spark job runtime environment with Docker on YARN](https://docs.cloud.google.com/managed-spark/docs/guides/docker-yarn) to use a customized Docker image with YARN.

## Docker Logging

By default, the Managed Service for Apache Spark Docker component writes logs to Cloud Logging by [setting the `gcplogs driver`](https://github.com/GoogleCloudPlatform/community/blob/master/archived/docker-gcplogs-driver/index.md#setting_the_default_logging_driver)—see [Viewing your logs](https://github.com/GoogleCloudPlatform/community/blob/master/archived/docker-gcplogs-driver/index.md#viewing_your_logs).

## Docker Registry

The Managed Service for Apache Spark Docker component configures Docker to use Container Registry in addition to the default Docker registries. Docker will use the Docker credential helper to authenticate with Container Registry.

## Use the Docker component on a Kerberos cluster

You can install the Docker optional component on a cluster that is being created with [Kerberos security enabled](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/security#enabling_hadoop_secure_mode_via_kerberos).

Docker is not part of the Hadoop ecosystem, and isn't recognized by Hadoop services. If you run a container that communicates with Hadoop services directly, your container must have the required Kerberos keytab file and credential.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
