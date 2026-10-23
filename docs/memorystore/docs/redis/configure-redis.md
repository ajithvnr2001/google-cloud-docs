---
url: https://docs.cloud.google.com/memorystore/docs/redis/configure-redis/
title: Configure a Redis instance \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:32.826078+00:00
---

# Configure a Redis instance  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/configure-redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Configure a Redis instance Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Redis supports a subset of the [native Redis configuration parameters](https://redis.io/topics/config) that you can modify to customize the behavior of your Redis instance. Other Redis configuration parameters are set to default values and [cannot be modified.](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs#unmodifiable_configuration_parameters) Configuration changes take place immediately, don't require a restart of the instance, and are saved if the instance restarts. You can update modifiable configuration parameters after instance creation.

For tables showing acceptable values for modifiable parameters and default values for unmodifiable parameters, see the [Redis configurations](https://docs.cloud.google.com/memorystore/docs/redis/redis-configs) reference page.

### Viewing and updating configurations in the Google Cloud console

**Note:** You can only modify the `maxmemory-gb` configuration using the gcloud CLI. The configuration is not available in the Google Cloud console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.   
[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)
  2. Click the Instance ID of the instance.
  3. Click **Edit**.
  4. The **Configurations** section is now visible. Click the trash bin to the right of a configuration to delete it, or click **Add Configuration** to add a new configuration.



### Setting and updating configuration parameters with the Google Cloud CLI

**Note:** Make sure that you have installed the latest version of the Google Cloud CLI by running `gcloud components update`.

You can set modifiable configuration parameters when creating or updating an instance. To set a configuration parameter during creation, enter the following command, replacing the highlighted-variables with the appropriate values:
    
    
    gcloud redis instances create instance-id --size=size --region=region-id --zone=zone --redis-config maxmemory-policy=policy

To change a configuration parameter for an existing instance, enter the following command:
    
    
    gcloud redis instances update instance-id --update-redis-config maxmemory-policy=policy

### Viewing current configuration parameters with the Google Cloud CLI

To view configuration parameters that you set when creating or updating an instance, enter the `describe` command for the instance:
    
    
    gcloud redis instances describe instance-id --region=region-id

You won't see configuration parameters when running `describe` unless you have changed a configuration from its default value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
