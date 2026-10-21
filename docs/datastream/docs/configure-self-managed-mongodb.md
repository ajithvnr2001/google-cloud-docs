---
url: https://docs.cloud.google.com/datastream/docs/configure-self-managed-mongodb/
title: Configure a self-managed MongoDB database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:51.653104+00:00
---

# Configure a self-managed MongoDB database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-self-managed-mongodb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a self-managed MongoDB database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure a self-managed MongoDB instance to work with Datastream. You can configure Datastream for both replica sets and sharded clusters.

## Replica set

For information about deploying a MongoDB replica set, see [Deploy a self-managed replica set](https://www.mongodb.com/docs/manual/tutorial/deploy-replica-set/) in the MongoDB documentation.

To configure Datastream for use with a self-managed MongoDB replica set, follow these steps:

  1. Install the MongoDB Shell. For information about installing the MongoDB Shell, see [Install mongosh](https://www.mongodb.com/docs/mongodb-shell/install/).
  2. Open a terminal window, and run the `mongosh` command to connect to your replica set or primary node.
  3. Create a user for Datastream in the `admin` database:
         
         use admin
         db.createUser({
           user: "USERNAME",
           pwd: "PASSWORD",
           roles: [ "readAnyDatabase", {role: "read", db: "admin"} ]
         })
         

Replace USERNAME and PASSWORD with your preferred username and password.




## Sharded cluster

For information about deploying a sharded cluster, see [Deploy a sharded cluster](https://www.mongodb.com/docs/kubernetes-operator/current/tutorial/deploy-sharded-cluster/) in the MongoDB documentation.

To configure Datastream for use with a self-managed MongoDB sharded cluster, follow these steps:

  1. Install the MongoDB Shell. For information about installing the MongoDB Shell, see [Install mongosh](https://www.mongodb.com/docs/mongodb-shell/install/).
  2. Open a terminal window, and run the `mongosh` command to connect to your MongoDB sharded cluster.
  3. Create a Datastream user in every primary shard node and the `mongos` query router:
         
         use admin
         db.createUser({
            user: "USERNAME",
            pwd: "PASSWORD",
            roles: [ "readAnyDatabase" ]
         })
         

Replace USERNAME and PASSWORD with your username and password. You can choose any username and password, but they must be identical across all primary shard nodes and the `mongos` query router.

  4. To find out which shards are connected to the `mongos` query router, run the following command:

`db.adminCommand({ listShards: 1 })`




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
