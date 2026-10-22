---
url: https://docs.cloud.google.com/memorystore/docs/memcached/verify-connection/
title: Verify a private services access connection \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:42.997539+00:00
---

# Verify a private services access connection  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/verify-connection/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Verify a private services access connection Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for checking to see if a [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) connection is set up for your network. Any network on which you provision a Memorystore for Memcached instance must have a private services access connection. Otherwise, you cannot select that network when creating a Memorystore for Memcached instance. See [Networking](https://docs.cloud.google.com/memorystore/docs/memcached/networking) for more details.

For instructions on setting up a private services access connection, see [Establishing a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).

### Console

  1. Go to the **VPC Networks** page in the Google Cloud console.   
[VPC Networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network that you want to verify.

  3. Click the **Private service connection** tab.

  4. Click the **Private connections to services** tab.

If you see a connection listed called `servicenetworking-googleapis-com`, then a connection has been established for this network.

If the connection has not been established, follow the instructions at [Establishing a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).




### gcloud

Verify if private services access is already set up for your project by running the following command, replacing the highlighted-variables with the appropriate values:
    
    
       gcloud services vpc-peerings list --network=network --project=project-id
       

To select your default network use `--network=default`.

If a connection is enabled, the command returns the text below with the `[bracketed-variables]` replaced by your project's variables. If a connection is not enabled for private services access, the previous command returns nothing.
    
    
       network: projects/[project-number]/global/networks/[network]
       peering: servicenetworking-googleapis-com
       reservedPeeringRanges: [Range description]
       

If the connection has not been established, follow the instructions at [Establishing a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).

## What's next

  * [Establish a private services access connection](https://docs.cloud.google.com/memorystore/docs/memcached/establishing-connection).
  * [Create a Memcached instance](https://docs.cloud.google.com/memorystore/docs/memcached/creating-managing-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
