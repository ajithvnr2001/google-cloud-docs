---
url: https://docs.cloud.google.com/spanner/docs/instances/
title: Instances overview \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:20.535018+00:00
---

# Instances overview  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Instances overview Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces Spanner instances and their two primary characteristics, instance configurations and compute capacity.

## Overview of instances

To use Spanner, you must first create a Spanner _instance_ within your Google Cloud project. This instance is an allocation of resources that is used by Spanner databases created in that instance.

Instance creation includes the following important choices:

  * The [_edition_](https://docs.cloud.google.com/spanner/docs/editions-overview): Spanner's tier-based pricing model that provides different capabilities at different price points.
  * The [_instance configuration_](https://docs.cloud.google.com/spanner/docs/instance-configurations): defines the geographic placement and replication topology of the instance.
  * The [_compute capacity_](https://docs.cloud.google.com/spanner/docs/compute-capacity): the amount of server and storage resources that are available to the databases in an instance.



Once an instance is created, you can list, edit, or delete it. Spanner is a fully managed database service which oversees its own underlying tasks and resources, including monitoring and restarting processes when necessary with zero downtime. As there is no need to manually stop or restart a given instance, Spanner does not offer a way to do so.

Spanner offers a 90-day free trial instance that lets you learn and explore Spanner features and capabilities at no cost for 90 days. To learn more, see [Spanner free trial instances overview](https://docs.cloud.google.com/spanner/docs/free-trial-instance).

## Spanner editions

Spanner offers different editions to support your various business and application needs. To learn more, see the [ Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview).

## Instance configurations

An instance configuration defines the geographic placement and replication of the databases in that instance. When you create an instance, you must configure it as one of the following:

  * _Regional_ : All resources are contained within a single Google Cloud [region](https://docs.cloud.google.com/docs/geography-and-regions).
  * _Dual-region_ : Resources span two regions in a single country.
  * _Multi-region_ : Resources span across multiple regions



You make this choice by selecting an instance configuration, which determines where your data is stored for that instance.

To learn more about instance configurations, see [Regional, dual-region, and multi-region configurations](https://docs.cloud.google.com/spanner/docs/instance-configurations).

## Compute capacity

Compute capacity defines amount of server and storage resources that are available to the databases in an instance. When you create an instance, you specify its compute capacity as a number of _processing units_ or as a number of _nodes_ , with 1000 processing units being equal to 1 node.

Which measurement unit you use does not matter unless you are creating an instance whose compute capacity is smaller than 1000 processing units (1 node); in this case, you must use processing units to specify the compute capacity of the instance.

To learn more about compute capacity, see [Compute capacity, nodes and processing units](https://docs.cloud.google.com/spanner/docs/compute-capacity).

## What's next

  * Learn more about [Spanner editions](https://docs.cloud.google.com/spanner/docs/editions-overview).
  * Learn more about [regional, dual-region, and multi-region instance configurations](https://docs.cloud.google.com/spanner/docs/instance-configurations).
  * Learn more about [compute capacity, processing units, and nodes](https://docs.cloud.google.com/spanner/docs/compute-capacity).
  * Learn how to [Create a Spanner instance](https://docs.cloud.google.com/spanner/docs/create-manage-instances#create-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
