---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-bloom-filters/
title: About Bloom filters \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:17.356465+00:00
---

# About Bloom filters  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-bloom-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  About Bloom filters Stay organized with collections  Save and categorize content based on your preferences. 

A [Bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) is a space-efficient, probabilistic data structure that you can use to test whether an element is a member of a set. With this type of structure, you can have false positives. For example, the filter can indicate that an element is in the set, even though it isn't. However, you can't have false negatives. So, if you add an element to the set, then the filter must indicate that the element is in the set.

The filter achieves this by using multiple hash functions to map an element to several bits in a fixed-size bit array. To control the probability of false positives, you can adjust the number of bits in the array and the number of hash functions used.

## Use cases

This section describes the following use cases for using Bloom filters:

  * **Deduplicate advertisements and events** : If you have an ecommerce site, streaming service, advertising network, or marketing platform, then Bloom filters can help you determine whether a user saw an advertisement, received a promotional email or notification, or purchased a product.

You can use a Bloom filter to store all of the products that a user purchases.

    * If a product isn't in the filter, then show the ad to the user and add the product to the filter.
    * If the product is in the filter, then the user probably saw the associated advertisement and purchased the product. Therefore, find a different ad to show to the user.
  * **Detect fraud** : You can use Bloom filters to detect whether a credit card is flagged as stolen. To do this, use a filter that contains cards reported as stolen. When a card is used, check whether it appears in the filter.

    * If the card isn't in the filter, then it isn't marked as stolen.
    * If the card is in the filter, then you can check the card against the main database or deny the purchase.
  * **Filter spam and harmful content** : You can use Bloom filters to screen content for potential threats, harmful materials, and spam. To do this, create a filter that contains malicious URLs, spam email addresses, and spam phone numbers. When the user inputs a URL, or receives an email or text, check whether this information appears in the filter.

    * If the URL, email, or text isn't in the filter, then allow the user to access the site represented by the URL, or receive the email or text.
    * If the URL, email, or text is in the filter, then deny the user access to the associated site or prevent the user from receiving the email or text.
  * **Detect duplicate usernames** : You can use Bloom filters to determine whether a username is new or if it already exists. To do this, use a filter to track every username that signs up for your ecommerce site or streaming service. When a new user attempts to sign up with their username, check whether the username appears in the filter.

    * If the username isn't in the filter, then create the account and add the username to the filter.
    * If the username is in the filter, then reject the username.



For more information about these use cases, see [Common use cases for Bloom filters](https://valkey.io/topics/bloomfilters/#common-use-cases-for-bloom-filters).

## Availability

If you create a Memorystore for Valkey instance, version 8.0 and later, then version 1.0 of the [Bloom data type and associated commands](https://github.com/valkey-io/valkey-bloom) is available automatically. This data type is API-compatible with the Bloom filter command syntax of the following Valkey client libraries:

  * [valkey-py](https://github.com/valkey-io/valkey-py)
  * [valkey-java](https://github.com/valkey-io/valkey-java)
  * [valkey-go](https://github.com/valkey-io/valkey-go)

**Note:** The Bloom data type isn't RDB-compatible with other non-Valkey-based Bloom offerings.

## Bloom filter types

You can have the following types of Bloom filters:

  * **Scaling** : This type of filter doesn't have a fixed capacity so the filter can grow. If the filter reaches its capacity and you add a new, unique item to the filter, then the filter scales out and a new subfilter is created. This subfilter has a larger capacity than the filter.
  * **Non-scaling** : This type of filter has a fixed capacity so there's a limit to how many items you can add to the filter. If the filter reaches its capacity and you attempt to add a new, unique item to the filter, then you receive an error.



For more information about the differences between these types of Bloom filters, see [Scaling and non-scaling Bloom filters](https://valkey.io/topics/bloomfilters/#scaling-and-non-scaling-bloom-filters).

## Bloom filter properties

A Bloom filter has the following properties:

  * **Capacity** : The number of items that a Bloom filter can hold before either the filter scales out (for a scaling filter) or it rejects adding additional items (for a non-scaling filter).
  * **False positive rate** : The rate that controls the probability of operations for Bloom filters resulting in false positives. For example, an operation that you use to check whether an element is in the filter indicates that the element is in the filter, even though it isn't.
  * **Expansion** : This property is associated with scaling Bloom filters. It controls the growth in overall capacity when the filter scales out because the filter reaches its capacity.
  * **Scaling or non-scaling** : Whether a Bloom filter is a scaling or non-scaling filter.



For more information about the properties of Bloom filters, see [Bloom properties](https://valkey.io/topics/bloomfilters/#bloom-properties).

## Bloom filter objects

A Bloom filter object can consume a maximum of 128 MB of memory. To check how much memory a Bloom filter consumes, use the [`BF.INFO key SIZE`](https://valkey.io/commands/bf.info/) command, where `key` is the key name for the filter and SIZE is the number of bytes that the filter consumes.

## Bloom categories

To manage access to Bloom commands and data, use the `@bloom` category. In addition to this category, the following categories use Bloom commands: `@read`, `@write`, and `@fast`.

The following table indicates whether you can map Bloom commands to the `@read`, `@write`, `@fast`, and `@bloom` categories.

Bloom command | `@bloom` | `@read` | `@write` | `@fast`  
---|---|---|---|---  
`BF.ADD` | Y | N | Y | Y  
`BF.CARD` | Y | Y | N | Y  
`BF.EXISTS` | Y | Y | N | Y  
`BF.INFO` | Y | Y | N | Y  
`BF.INSERT` | Y | N | Y | Y  
`BF.MADD` | Y | N | Y | Y  
`BF.MEXISTS` | Y | Y | N | Y  
`BF.RESERVE` | Y | Y | N | Y  
  
## Bloom metrics

To monitor the usage of the Bloom data type, the following Cloud Monitoring metrics are available in Memorystore for Valkey:

  * `objects_count`
  * `used_memory`



For more information about these metrics, see [Bloom filter and JSON metrics](https://docs.cloud.google.com/memorystore/docs/valkey/supported-monitoring-metrics#bloom-filter-json-metrics).

## Bloom commands

This section lists and describes the Bloom commands that you can use to perform Bloom operations on the Bloom data type.

Command | Description  
---|---  
`[BF.ADD](https://valkey.io/commands/bf.add/)` | Add a single item to a Bloom filter. If the filter doesn't exist, then the command creates it.  
`[BF.CARD](https://valkey.io/commands/bf.card/)` | Return the cardinality of a Bloom filter.  
`[BF.EXISTS](https://valkey.io/commands/bf.exists/)` | Determine if a Bloom filter contains the item that you specify.  
`[BF.INFO](https://valkey.io/commands/bf.info/)` | Return usage information and properties of a Bloom filter.  
`[BF.INSERT](https://valkey.io/commands/bf.insert/)` | Create a Bloom filter with 0 or more items or add items to an existing filter.  
`[BF.MADD](https://valkey.io/commands/bf.madd/)` | Add one or more items to a Bloom filter. If the filter doesn't exist, then the command creates it.  
`[BF.MEXISTS](https://valkey.io/commands/bf.mexists/)` | Determine if the bloom filter contains one or more items.  
`[BF.RESERVE](https://valkey.io/commands/bf.reserve/)` | Create an empty bloom filter with the properties that you specify.  
  
**Note** : For more information about using these commands, see the [Valkey command reference](https://valkey.io/commands/#bloom) page. Memorystore for Valkey doesn't support the [`BF.LOAD`](https://valkey.io/commands/bf.load/) command.

You can check the performance of using these commands. For more information, see [Performance](https://valkey.io/topics/bloomfilters/#performance). 

## Check Bloom filters

You can check the following information about Bloom filters:

  * **Memory usage** : check if a filter reaches its memory usage limit. To check the amount of memory that a filter uses, use the [`BF.INFO`](https://valkey.io/commands/bf.info/) command.
  * **Capacity** : check if a filter is a scaling filter. If it is, scale the filter so that it reaches its capacity, and then scale out.



For more information about checking the memory usage and capacity for Bloom filters, see [Handle large Bloom filters](https://valkey.io/topics/bloomfilters/#handling-large-bloom-filters).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
