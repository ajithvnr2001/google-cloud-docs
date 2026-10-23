---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/sharding/
title: Config Controller sharding guidelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:49.441299+00:00
---

# Config Controller sharding guidelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/sharding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/overview)



Send feedback 

#  Config Controller sharding guidelines Stay organized with collections  Save and categorize content based on your preferences. 

This document provides recommendations on how to shard your Config Controller usage. Sharding is the process of splitting Config Controller-managed Google Cloud resources across multiple namespaces, clusters, or projects.

Sharding brings the following benefits:

  * **Reduces the impact of changes** : If a single shard stops functioning, the other shards are not impacted.
  * **Helps you manage security** : Each shard can have dedicated IAM and RBAC configurations. Malicious attackers who compromise one shard cannot access other shards. Misconfiguration in one shard cannot affect other shards.
  * **Better scalability** : A single shard can have scalability bottlenecks such as the number of managed objects, or API quotas. Having multiple shards increases the overall scalability of your Config Controller usage.



## Use sharding with Config Controller

There are a few different ways to implement sharding. The best approach for you will depend on your specific needs and requirements.

### Sharding models

There are two main sharding models:

  * **By business lines or application teams** : This model is typically used when Config Controller is used by different teams. In this model, each team has their own shard.
  * **By environment** : This model is typically used when Config Controller is used in different environments. For example, you might have a shard for your development environment, a shard for your QA environment, and a shard for your production environment.



### Minimize the need for cross-shard references

When you shard your Config Controller usage, you should minimize the need for cross-shard references. Cross-shard references can make your configuration more complex and difficult to manage. See Resource references across instances for more details.

### Sharding mechanisms

There are three main sharding mechanisms:

  * **By namespaces** : You can create additional namespaces and [configure Config Connector to manage resources in those namespaces](https://docs.cloud.google.com/config-connector/docs/how-to/advanced-install#project-namespace).
  * **By Config Controller instances** : You can create multiple Config Controller instances in one Google Cloud project.
  * **By projects** : You can create multiple Config Controller instances in multiple Google Cloud projects. This mechanism helps address API quota issues if you are hitting quota bottlenecks with one single project. See [Split your resources into multiple projects](https://docs.cloud.google.com/config-connector/docs/best-practices#quota-split) for more details.



## Caveats when implementing sharding

When implementing sharding for your Config Controller usage, there are some potential issues you should be aware of and plan to mitigate.

### Resource references across instances

One of the challenges of sharding Config Controller is dealing with resource references across instances. For example, a platform team might create Projects in one instance, and then app teams might create resources that refer to those Projects in other instances. This can create problems such as:

  * **Increased complexity** : Managing resource references across clusters can make your configuration more complex and difficult to manage.
  * **Increased risk** : If a resource is deleted in one shard, it can still be referenced by resources in other shards. This can lead to unexpected behavior and data loss.
  * **Performance degradation** : Resource references across clusters can increase the latency of your configuration changes.



There are a few ways to work around the cross-reference challenge:

  * Sharding in a way that no reference across shards is needed. This could be done by sharding by environments or by teams.
  * Using external references. This means that the object that is being referenced is not actually managed by Config Controller. This can be a good option if the object isn't changing frequently.
  * Having the same object available in all shards. This is a more complex option, but it can be the best option if the object changes frequently. The objects should share the same source of truth to avoid reconciliation fights between these objects in different shards. You need to set the [conflict prevention policy](https://docs.cloud.google.com/config-connector/docs/concepts/managing-conflicts#modifying_conflict_prevention) to `none` for these objects.



It is important to carefully consider the advantages and disadvantages of each approach before choosing one.

### API Quotas

Sharding could increase your API quotas. You should be aware of this and plan accordingly. See [Manage API quota limits](https://docs.cloud.google.com/config-connector/docs/best-practices#quota-limits) for best practices on managing API quota limits.

## What's next

  * Learn more about [Config Controller scalability](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/scalability)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
