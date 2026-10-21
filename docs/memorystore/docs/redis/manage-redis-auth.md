---
url: https://docs.cloud.google.com/memorystore/docs/redis/manage-redis-auth/
title: Manage Redis AUTH \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:53.248496+00:00
---

# Manage Redis AUTH  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/manage-redis-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Manage Redis AUTH Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are looking for the Memorystore for Redis Cluster documentation, see [Manage IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/manage-iam-auth).

This page gives instructions on common tasks for the [Redis AUTH](https://redis.io/commands/auth) feature on Memorystore for Redis. For details on what the AUTH feature provides, see [AUTH feature overview](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview).

For a list of permissions a user needs in order to perform the AUTH tasks on this page, see [Redis AUTH permissions](https://docs.cloud.google.com/memorystore/docs/redis/access-control#redis_authentication_permissions).

## Create a Redis instance with AUTH enabled

### Console

When you [create a Redis instance](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#create_a_redis_instance_on_a_vpc_network), select **Enable AUTH**.

### gcloud

Enter the following command, replacing variables with appropriate values:
    
    
    gcloud redis instances create instance-id --enable-auth --size=size --region=region --zone=zone --redis-version=version
    

## Enable and disable AUTH on an existing Redis instance

**Note:** AUTH string credentials are not confidential when transmitted. See [AUTH feature overview](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview) for more details.

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. View your instance's _Instance details_ page by clicking on your _Instance ID_.

  3. Click the **Edit** button.

  4. Find the AUTH section.

     * If you want to enable AUTH, select checkbox labeled **Enable AUTH**.

     * If you want to disable AUTH, deselect the checkbox labeled **Enable AUTH**.

  5. Click the **Save** button.




### gcloud

  1. Enable AUTH for your instance by running the following command, replacing variables with appropriate values:
         
         gcloud redis instances update instance-id --enable-auth --region=region
         

  2. Disable AUTH for your instance by running the following command, replacing variables with appropriate values:
         
         gcloud redis instances update instance-id --no-enable-auth --region=region
         




## Get the AUTH string

### Console

  1. Go to the **Memorystore for Redis** page in the Google Cloud console.

[Memorystore for Redis](https://console.cloud.google.com/memorystore/redis/instances)

  2. View your instance's _Instance details_ page by clicking on your _Instance ID_.

  3. Find the **AUTH string** value in the **Security** section.




### gcloud

  1. Get the AUTH string by copying it from the response body returned by the following command:
         
         gcloud redis instances get-auth-string instance-id --region=region
         




## Change the AUTH string

Follow the steps below to change the AUTH string to a new value:

  1. Disable AUTH:
         
         gcloud redis instances update instance-id --no-enable-auth --region=region
         

  2. Enable AUTH:
         
         gcloud redis instances update instance-id --enable-auth --region=region
         

**Note:** This step interrupts your client's authenticated connection because a new AUTH string is generated, invalidating the previous AUTH string.
  3. Get the new AUTH string:
         
         gcloud redis instances get-auth-string instance-id --region=region
         

  4. In your application, replace the old AUTH string with the new AUTH string and reconnect your client.




## Connect to a Redis instance with AUTH

To connect to your instance using AUTH and `redis-cli`, see [Connect to a Redis instance that uses AUTH](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance#connect_to_a_redis_instance_that_uses_auth). If you enable in-transit encryption, then you must use a proxy like Stunnel to connect securely. For more information, see [Connect to a Redis instance securely by using Stunnel and telnet](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance#connect_to_a_redis_instance_securely_by_using_stunnel_and_telnet).

## What's next

  * View the [AUTH feature overview](https://docs.cloud.google.com/memorystore/docs/redis/auth-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
