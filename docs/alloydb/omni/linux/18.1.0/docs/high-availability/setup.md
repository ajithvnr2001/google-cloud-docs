---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/high-availability/setup/
title: Create a high availability setup \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:40:27.520751+00:00
---

# Create a high availability setup  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/high-availability/setup/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Create a high availability setup Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/high-availability/setup)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/high-availability/setup)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/high-availability/setup)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/high-availability/setup)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/high-availability/setup)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This page describes how to set up a high availability configuration for AlloyDB Omni. This page only covers creating a new AlloyDB Omni instance in a high availability configuration. It doesn't cover converting existing instances to high availability.

## Before you begin

  1. Read the [High availability and data resilience](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/high-availability/overview).

  2. If you don't already have one, create a Google Cloud project.

  3. Ensure that billing is enabled for your project.

  4. Open Cloud Shell in the Google Cloud console.

  5. In the Google Cloud console, clone the following source repository.
         
         git clone https://github.com/GoogleCloudPlatform/cloud-solutions.git
         




## Installation

In this guide, we deploy a three node [Patroni](https://patroni.readthedocs.io/en/latest/) cluster with AlloyDB Omni and a three node cluster [etcd](https://etcd.io/) as the configuration store. In the front of the cluster, we use [HAProxy](https://www.haproxy.org/) in a managed instance group for the floating IP address so that the failover is transparent to clients.

The initial configuration for this setup is shown in the following diagram:

![Configuration where HAProxy manages the connection between clients and the primary node](https://docs.cloud.google.com/static/alloydb/omni/linux/18.1.0/docs/images/ha-install-01.svg)

**Figure 1.** Configuration where HAProxy manages the connection between clients and the primary node.

If an outage occurs, the configuration changes to the following diagram:

![Updated configuration where the failed primary node is replaced by the standby node](https://docs.cloud.google.com/static/alloydb/omni/linux/18.1.0/docs/images/ha-install-02.svg)

**Figure 2.** Updated configuration where the failed primary node is replaced by the standby node.

If the number of clients that connect to the database becomes an issue and you have performance issues due to the high number of simultaneous database connections, we recommend that you add application-side connection pooling. If you can't do that, then you can add database-side connection pooling using a tool like PgBouncer.

## Deployment

  1. In Cloud Shell and after cloning the Cloud Solutions repository, navigate to the terraform directory.
         
         cd cloud-solutions/projects/alloydbomni-ha-patroni-etcd/terraform
         

  2. Create and edit a `terraform.tfvars` file. In the file, set values for the following variables.
         
         project_id                   = "PROJECT_ID"
         region                       = "REGION"
         zones                        = "ZONES"
         node_count                   = 3
         cluster_name                 = "CLUSTER_NAME"
         replication_user_password    = "REPLICATION_USER_PASSWORD"
         postgres_super_user_password = "PG_SUPER_USER_PASSWORD"
         

Descriptions for each variable can be found on GitHub in the [variables configuration file](https://github.com/GoogleCloudPlatform/cloud-solutions/blob/79ceca9b9ff498d2af6101f264b1c731c8911aee/projects/alloydbomni-ha-patroni-etcd/terraform/variables.tf).

  3. Run the Terraform script to create all the resources.
         
         terraform init && terraform apply
         

This script creates and configures the following:

     * Three nodes for your etcd cluster

     * Three nodes for your Patroni cluster

     * One node for HAProxy




### Configuring Patroni to be synchronous

To make Patroni use only synchronous replication in your three nodes cluster, add configuration items like `synchronous_mode`, `synchronous_node_count`, `synchronous_commit`, and `synchronous_standby_names` in the bootstrap section in your Patroni configuration files. The Patroni configuration is defined in the [startup script template](https://github.com/GoogleCloudPlatform/cloud-solutions/blob/79ceca9b9ff498d2af6101f264b1c731c8911aee/projects/alloydbomni-ha-patroni-etcd/terraform/scripts/patroni_startup.tftpl) and in the `/alloydb/config/patroni.yml` file on the Patroni nodes. To use synchronous replication, your Patroni bootstrap configuration should look as follows:
    
    
    bootstrap:
      dcs:
        ttl: 30
        loop_wait: 10
        retry_timeout: 10
        maximum_lag_on_failover: 1048576
        synchronous_mode: true
        synchronous_node_count: 2
        postgresql:
          use_pg_rewind: true
          use_slots: true
          parameters:
            hot_standby: "on"
            wal_keep_segments: 20
            max_wal_senders: 8
            max_replication_slots: 8
            synchronous_commit: remote_apply
            synchronous_standby_names: '*'
    

When `synchronous_mode` is turned on, Patroni uses synchronous replication between its primary and the other replicas. The parameter `synchronous_node_count` is used by Patroni to manage the number of synchronous standby replicas. Patroni manages precise number of synchronous standby replicas based on parameter `synchronous_node_count` and adjusts the state in the configuration store and in the `synchronous_standby_names` as members join and leave. For more information about synchronous replication, see the [Replication modes](https://patroni.readthedocs.io/en/latest/replication_modes.html) section in Patroni's documentation.

## What's next

  * [Test your high availability setup](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/high-availability/test)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
