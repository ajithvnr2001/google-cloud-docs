---
url: https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud/deployment/
title: Deploy RIOT Live Migration to migrate to Redis Enterprise Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:47.620109+00:00
---

# Deploy RIOT Live Migration to migrate to Redis Enterprise Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud/deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy RIOT Live Migration to migrate to Redis Enterprise Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-01-29 UTC

By: Gilbert Lau, Principal Cloud Architect, [Redis](https://redis.io/)

This document describes how you deploy [RIOT Live Migration to migrate to Redis Enterprise Cloud](https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud). Database architects, DevOps and SRE teams, or Network administrators can use this architecture to offer near-zero downtime migrations to their teams. This document assumes that you're familiar with using the Google Cloud CLI and Compute Engine.

## Architecture

The following diagram shows the reference architecture that uses RIOT Live Migration Service to migrate Redis-compatible sources to Redis Enterprise Cloud.

![Redis-compatible sources are migrated through RIOT to Redis Enterprise Cloud.](https://docs.cloud.google.com/static/architecture/images/riot-live-migration-redis-enterprise-cloud-architecture.svg)

For details about the architecture, see [RIOT Live Migration to migrate to Redis Enterprise Cloud](https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud).

The sample deployment in this document uses the following architecture in which the source is a Redis OSS on a Compute Engine VM:

![Redis OSS is migrated through RIOT and VPC peering to Redis Enterprise Cloud.](https://docs.cloud.google.com/static/architecture/images/riot-live-migration-redis-enterprise-cloud-deployment.svg)

In the diagram, a Redis OSS instance and RIOT are consolidated into a single Compute Engine VM for simplicity. In a production environment, we recommend that RIOT always runs on its own VM to help ensure better performance.

The sample deployment architecture contains the following components:

  * **Source** : Redis OSS instance running on Compute Engine VM.
  * **Target** : Redis Enterprise Cloud running in the Redis managed VPC.
  * **Migration Service** : RIOT running on the same Compute Engine VM as Redis OSS.
  * **Network Setup** : VPC Peering between a managed VPC and the Redis managed VPC.



The RIOT migration tool has near-zero downtime. During migration from Redis OSS (source) to Redis Enterprise Cloud (target), your applications can still access Redis OSS without impact or service disruption. During the migration process, after the initial load of data from Redis OSS, RIOT Live Migration continues to migrate changes from Redis OSS as they occur.

## Objectives

  * Set up your Redis OSS source by creating and loading data.
  * Set up a migration target cluster in Redis Enterprise Cloud.
  * Use RIOT Live Migration to migrate data from Redis OSS to Redis Enterprise Cloud.
  * Understand testing, cutover, and fallback strategies.



## Costs

Deployment of this architecture uses the following billable components of Google Cloud:

  * [Compute Engine](https://cloud.google.com/compute/vm-instance-pricing) costs for running Redis OSS and RIOT instances.
  * [Redis Enterprise Cloud](https://console.cloud.google.com/marketplace/product/redis-marketplace-isaas/redis-enterprise-cloud-flexible-plan) cost procured through Google Cloud Marketplace.
  * [Network charges](https://cloud.google.com/vpc/network-pricing) incurred from data migration traffic between zones and [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).



## Before you begin

Complete the following steps to set up an environment for your migration.

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the BigQuery, Pub/Sub, Dataflow, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,pubsub.googleapis.com,dataflow.googleapis.com,compute.googleapis.com)

  4. To get the permissions that you need to complete this deployment, ask your administrator to grant you the Billing Administrator (`roles/billing.admin`) IAM role on your organization. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).




## Set up a Redis OSS instance

To start the deployment, you install the Redis OSS instance on a Compute Engine VM. The instance serves as your source instance.

### Install the Redis OSS instance

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In Cloud Shell, create an Ubuntu VM:
         
         gcloud compute instances create redis-oss-riot-vm \
           --image-family=ubuntu-2004-lts \
             --image-project=ubuntu-os-cloud \
             --zone=us-central1-a \
             --machine-type=e2-medium \
             --network=VPC_NETWORK_NAME \
             --subnet=VPC_SUBNETWORK_NAME \
           --metadata=startup-script='#! /bin/bash
             apt-get update -y
             apt-get install redis-tools -y
             snap install redis'
         

Replace the following:

     * **`VPC_NETWORK_NAME`** : the name of your VPC network.
     * **`VPC_SUBNETWORK_NAME`** : the name of your VPC subnetwork.
  3. Use an SSH connection to sign in to the Compute Engine instance that runs the Redis OSS instance:
         
         PROJECT_ID=$(gcloud info --format='value(config.project)')
         
         gcloud compute ssh redis-oss-riot-vm --project $PROJECT_ID --zone us-central1-a
         

  4. Enable [keyspace notification](https://redis.io/docs/manual/keyspace-notifications/) for live migration, which is required by RIOT:
         
         redis-cli config set notify-keyspace-events KEA
         




### Verify that the Redis OSS instance is operational

  1. In Cloud Shell, launch the [Redis CLI](https://redis.io/docs/connect/cli/):
         
         redis-cli
         

  2. Set and get a simple key-value pair:
         
         set my_key my_value
         get my_key
         unlink my_key
         

The output is the following:
         
         OK
         "my_value"
         (integer) 1
         

You have now created and accessed your Redis OSS instance and confirmed that it's operational.




## Insert sample data

In this section, you insert sample data into the Redis OSS instance and verify that the data is successfully inserted.

  1. In Cloud Shell, launch the Redis CLI:
         
         redis-cli
         

  2. Add the following six key-value pairs as the initial dataset. Enter each command individually and wait for the output `OK` before you enter the next key-value pair.
         
         set tennis federer
         
         
         set soccer ronaldo
         
         
         set basketball curry
         
         
         set football montana
         
         
         set golf woods
         
         
         set swimmer phelps
         

  3. Verify that you added six key-value pairs successfully:
         
         SCAN 0
         

The output is the following:
         
         "swimmer"
         "soccer"
         "football"
         "golf"
         "tennis"
         "basketball"
         




After you set up and start the RIOT migration, the data is migrated to the target Redis Enterprise Cloud instance.

## Install RIOT on the Redis OSS instance VM

In order to run RIOT, you need to make sure that your Compute Engine VM is appropriately sized. In general, we recommend that you size your VM to 8 VCPUs or larger, depending on the amount of data to be transported and the update frequency. For more information, see [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).

  1. In Cloud Shell, use an SSH connection to sign in to the Compute Engine instance that runs the Redis OSS instance:
         
         PROJECT_ID=$(gcloud info --format='value(config.project)')
         
         gcloud compute ssh redis-oss-riot-vm --project $PROJECT_ID --zone us-central1-a
         

  2. Install JDK for RIOT:
         
         sudo apt install default-jre -y
         

  3. Download and install RIOT:
         
         sudo apt-get install unzip
         
         wget https://github.com/redis-developer/riot/releases/download/v2.19.0/riot-redis-2.19.0.zip
         
         unzip riot-redis-2.19.0.zip
         

  4. Verify that RIOT is installed correctly:
         
         ./riot-redis-2.19.0/bin/riot-redis -V
         

The output is similar to the following, which shows a RIOT logo and a version number:

![A RIOT logo and version number.](https://docs.cloud.google.com/static/architecture/images/riot-live-migration-redis-enterprise-cloud-output.png)




You have now installed the RIOT migration tool on the Redis OSS instance and confirmed that it's operational.

## Create a Redis Enterprise Cloud instance

[Redis Enterprise Cloud](https://docs.redis.com/latest/rc/) is available through Cloud Marketplace. If you _don't_ have a Redis Enterprise cluster set up as your target Redis Enterprise instance, follow the steps in this section. If you already have a Redis Enterprise cluster set up as your target database, you can skip this section and proceed to Start the RIOT live migration.

  1. In Cloud Marketplace, go to **Redis Enterprise Cloud Flexible - Pay as You Go**.

[Go to Redis Enterprise in Marketplace](https://console.cloud.google.com/marketplace/product/redis-marketplace-isaas/redis-enterprise-cloud-flexible-plan)

For more information, see the instructions in the Redis document [Flexible subscriptions with Cloud Marketplace](https://docs.redis.com/latest/rc/cloud-integrations/gcp-marketplace/).

  2. Sign in to the [Redis console](https://app.redislabs.com/) using the Redis account information that you provided when you subscribed to Redis Enterprise Cloud Flexible.

  3. Create a Flexible subscription by following the instructions in the Redis document [Create a Flexible subscription](https://docs.redis.com/latest/rc/subscriptions/create-flexible-subscription/). Choose Google Cloud as your cloud vendor, and create a database with all the default settings.

  4. Create a VPC peering between your Google Virtual Private Cloud and the Redis managed VPC by following the instructions in the Redis document [Enable VPC peering](https://docs.redis.com/latest/rc/security/vpc-peering/#gcp-vpc-peering).

  5. In the [Redis console](https://app.redislabs.com/), go to **Subscription** , and then locate your **Redis Enterprise database connection string** :

     1. Make a note of the **Private endpoint IP and Port** , in the format of:
            
            ENDPOINT_IP:ENDPOINT_PORT
            

Where the values represent the following:

        * **`ENDPOINT_IP`** : the private endpoint IP address for the Redis Enterprise database.
        * **`ENDPOINT_PORT`** : the private endpoint port number for the Redis Enterprise database.
     2. Make a note of the database password.




## Start the RIOT live migration

To migrate the data from the Redis OSS (source) to Redis Enterprise Cloud (target) instance, do the following:

  1. In Cloud Shell, use an SSH connection to sign in to the Compute Engine instance that runs the Redis OSS instance:
         
         PROJECT_ID=$(gcloud info --format='value(config.project)')
         
         gcloud compute ssh redis-oss-riot-vm --project $PROJECT_ID --zone us-central1-a
         

  2. Initiate a live migration between the source and target. If your Redis OSS instance is on Redis 7.2, you need to use type-based replication. For information about using the `--type` option, see the Redis documentation [Type-based replication](https://developer.redis.com/riot/#_replicate_type_based).
         
         ./riot-redis-2.19.0/bin/riot-redis -u redis://localhost:6379 replicate  \
         -u redis://ENDPOINT_IP:ENDPOINT_PORT \
           -a REDIS_ENTERPRISE_DB_PASSWORD \
           --mode live
         

Replace the following with the values that you noted in the previous section:

     * **`ENDPOINT_IP`** : the private endpoint IP address for the Redis Enterprise cluster database.
     * **`ENDPOINT_PORT`** : the private endpoint port number for the Redis Enterprise cluster database.
     * **`REDIS_ENTERPRISE_DB_PASSWORD`** : the password for the Redis Enterprise cluster database.

The output is similar to the following:
    
    Listening  ? % ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━0/? (0:00:00 / ?) ?/s\
    Scanning 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6/6 (0:00:00 / 0:00:00) ?/s
    




## Verify the database migration

It's important to design and implement a database migration verification strategy to confirm that the database migration is successful. Although the verification strategy that you use depends on your specific use case, we recommend that you perform these checks for all migrations:

  * **Completeness check** : Verify that the initial key-value pairs successfully migrated from the Redis OSS to Redis Enterprise (initial load).
  * **Dynamic check** : Verify that changes in the source are being transferred to the target instance (ongoing migration).



### Initial load

  1. In Cloud Shell, use an SSH connection to sign in to the Compute Engine instance that runs the Redis OSS instance:
         
         PROJECT_ID=$(gcloud info --format='value(config.project)')
         $ gcloud compute ssh redis-oss-riot-vm --project $PROJECT_ID --zone us-central1-a
         

  2. Launch the [Redis CLI](https://redis.io/docs/connect/cli/):
         
         redis-cli -u redis://ENDPOINT_IP:ENDPOINT_PORT \
         -a REDIS_ENTERPRISE_DB_PASSWORD
         

  3. Verify that the six key-value pairs successfully migrated from Redis OSS to Redis Enterprise instance:
         
         SCAN 0
         

The output is the following:
         
         "swimmer"
         "soccer"
         "football"
         "golf"
         "tennis"
         "basketball"
         

  4. Get the value of the tennis key:
         
         get tennis
         

The output is the following:
         
         [return federer]
         

  5. Exit the Redis CLI:
         
         exit
         




### Ongoing migration

Verify that ongoing changes to the source Redis OSS are reflected in the target Redis Enterprise instance:

  1. In Cloud Shell, use an SSH connection to sign in to the Redis OSS VM.
  2. Launch the Redis CLI:
         
         redis-cli
         

  3. Add new key-value pairs:

     1. Add a new `runner bolt` pair:
            
            set runner bolt
            

     2. Upsert a new `tennis alcaraz` pair:
            
            set tennis alcaraz
            

The output for each of these commands is the following:
    
    OK
    

  4. In the Redis Enterprise instance, observe that new key-value pairs are added:
         
         get runner
         

The output is the following:
         
         [return bolt]
         

  5. To verify that all key-value pairs are present, check key counts:
         
         redis-cli info keyspace and redis-cli -u <REMOTE> info keyspace
         

The output is the following:
         
         # Keyspace
         db0:keys=7,expires=0,avg_ttl=0
         




You have now verified that RIOT Live Migration has automatically migrated all the key-value pairs from the source Redis OSS instance and any ongoing changes to the source.

## Cut over from the source to the target

After you verify the database migration, you can perform a cutover from the source Redis OSS instance to the target Redis Enterprise instance:

  1. Suspend client write access to the source Redis OSS instance by using [Redis Access Control List](https://redis.io/docs/management/security/acl/).
  2. Unless you need to preserve the source database for your fallback strategy, decommission the source Redis OSS by removing the VM instance.
  3. Migrate the client to the same region as the Redis Enterprise database instance. For information, see the documentation for your client host.
  4. In the [Redis console](https://app.redislabs.com/), locate the private endpoint of the Redis Enterprise database instance and update your client's Redis connection to the private endpoint. For more information, see [View and edit databases](https://docs.redis.com/latest/rc/databases/view-edit-database/) in the Redis documentation.
  5. In Cloud Shell, stop the RIOT process by pressing **Ctrl+C**.



## Prepare a fallback strategy

After the cutover is finished, the target Redis Enterprise instance is the system of record; the source Redis OSS instance is out of date and eventually removed. However, you might want to fall back to the source Redis OSS instance in case of severe failures in the new target Redis Enterprise instance.

To fall back from such failures, you might want to keep the original source Redis OSS instance up to date with the target database changes. When you're confident that the new target instance is reliable, you can shut down the source instance.

## Clean up

The following sections explain how you can avoid future charges for your Google Cloud project and the Redis resources that you used in this deployment.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the Redis Enterprise database

To delete the Redis Enterprise database, see [Delete Database](https://docs.redis.com/latest/rc/databases/delete-database/) in the Redis documentation

## What's next

  * Learn how to [Define the scope of your migration to Redis Enterprise Cloud](https://docs.cloud.google.com/architecture/partners/riot-live-migration-redis-enterprise-cloud/assessment).
  * Read [Google Cloud data migration content](https://docs.cloud.google.com/solutions/database-migration).
  * For more in-depth documentation and best practices, review [RIOT documentation](https://developer.redis.com/riot/).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Saurabh Kumar](https://www.linkedin.com/in/saurabh-kumar-48556a19) | ISV Partner Engineer
  * [Gilbert Lau](https://www.linkedin.com/in/gilau) | Principal Cloud Architect, Redis



Other contributors: 

  * [Chris Mague](https://www.linkedin.com/in/chris-mague-35b1624) | Customer Engineer, Data Management
  * [Gabe Weiss](https://www.linkedin.com/in/weissgabriel) | Developer Advocacy Manager
  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-01-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-01-29 UTC."],[],[]] 
