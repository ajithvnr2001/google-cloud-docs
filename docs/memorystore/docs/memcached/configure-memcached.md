---
url: https://docs.cloud.google.com/memorystore/docs/memcached/configure-memcached/
title: Configure a Memcached instance \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:10.150332+00:00
---

# Configure a Memcached instance  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/configure-memcached/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Configure a Memcached instance Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Memcached supports a subset of [native Memcached configuration parameters](https://manpages.debian.org/unstable/memcached/memcached.1.en.html) that you can modify. You should use the same configurations for all nodes in your cluster. This page describes how to:

  * View instance configurations.
  * Modify instance configurations by: 
    * Staging instance configuration changes.
    * Updating node configuration changes.



Memorystore for Memcached requires you to update the configurations first, and then apply the changes to the nodes in your cluster. Applying a parameter update to a node causes a full cache flush on that node.

The advantage to being able to apply parameter updates to individual nodes is that you can roll out changes on a node-by-node basis. Doing so keeps your instance online and functional while you update configurations.

For a full list of the modifiable and unmodifiable parameters, see [Memcached configuration parameters](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).

## Viewing configurations

### Console

  1. Go to the **Memorystore for Memcached** page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)
  2. Click the ID of the instance to view the **Instance details** page.
  3. View your settings in the **Configuration** section.



### Gcloud

To view configuration parameters using the Google Cloud CLI, enter the `describe` command for the instance replacing variables with appropriate values:
    
    
    gcloud memcache instances describe instance-id --region=region
    

**Note:** You won't see configuration parameters when running `describe` unless you have changed a configuration from its default value.

For a list of modifiable configuration parameters and their default values, see [Memcached configuration parameters.](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs)

## Modifying configuration parameters

### Console

  1. Go to the **Memorystore for Memcached** page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)
  2. Click the ID of the instance.
  3. Click **Edit Configuration**.
  4. Adjust the value of any parameter that you want to change.
  5. Click the **Continue** button to stage the configuration updates.
  6. Select a node, and click **Update Selected Nodes** one at a time for each node, or in batches of nodes.

**Note:** Updating node configurations one at a time, or in batches, helps you avoid instance unavailability and reduces data loss.



### Gcloud

  1. Update the configuration parameters by running the following command:
         
         gcloud memcache instances update instance-id --region=region --parameters=parameter=value,parameter=value
         

  2. List and take note of all node IDs for your instance by running the following command:
         
         gcloud memcache instances describe instance-id --region=region --format="value(memcacheNodes.nodeId.list())"
         

  3. Apply the parameters one by one, or in batches, to nodes in your cluster by running the following command:

**Note:** Updating node configurations one at a time, or in batches, helps you avoid instance unavailability and reduces data loss.
         
         gcloud memcache instances apply-parameters instance-id --region=region --node-ids=node-1-id,node-2-id
         

Alternatively, you can apply the parameters for all nodes at once by using the following command, but we don't recommend it:
         
         gcloud memcache instances apply-parameters instance-id --region=region --apply-all
         




You cannot simultaneously run the`--parameters` flag with any other flags when using the Memorystore for Memcached `update` command.

## Configuring parameters using gcloud during instance creation

To set configuration parameters during creation, enter the following command replacing variables with appropriate values:
    
    
    gcloud memcache instances create instance-name --size=size --region=region --parameters=parameter=value,parameter=value
    

You can simultaneously run the `--parameters` flag with all other flags when using the Memorystore for Memcached `create` command.

## Clearing configuration parameters to default values using the Google Cloud console

  1. Go to the **Memorystore for Memcached** page in the Google Cloud console.   
[Memorystore for Memcached](https://console.cloud.google.com/memorystore/memcached/instances)
  2. Click the ID of the instance.
  3. Click **Edit Configuration**.
  4. Delete the value of any parameter that you want to reset to default, and leave the field blank.
  5. Click the **Continue** button to stage the configuration updates.
  6. Select a node, and click **Update Selected Nodes** one at a time for each node, or in batches of nodes.

**Note:** Updating node configurations one at a time, or in batches, helps you avoid instance unavailability and reduces data loss.



## What's next

  * Review the available [Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-configs).
  * Learn how to [scale your Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/scaling-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
