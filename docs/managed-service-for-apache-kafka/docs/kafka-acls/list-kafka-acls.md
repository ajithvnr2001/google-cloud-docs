---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/list-kafka-acls/
title: List Managed Kafka ACLs \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:23.317270+00:00
---

# List Managed Kafka ACLs  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/list-kafka-acls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  List Managed Kafka ACLs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to list the Managed Kafka ACL resources that are defined for a specified Managed Service for Apache Kafka cluster.

## Required roles and permissions

To get the permission that you need to list Managed Kafka ACLs, ask your administrator to grant you the [Managed Kafka ACL Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclViewer) (`roles/managedkafka.aclViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `managedkafka.acls.list` permission, which is required to list Managed Kafka ACLs. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List ACLs

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster.

  3. Click the **Access control** tab.

  4. Under **ACL entries** , the ACL entries for this cluster are listed.




###  gcloud 

Run the [`gcloud managed-kafka acls list`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/list) command:
    
    
    gcloud managed-kafka acls list CLUSTER_ID \
      --location=LOCATION
    

Replace the following:

  * `CLUSTER_ID` The ID of your Kafka cluster.
  * `LOCATION`: The region of your Kafka cluster.



## Sample command

Run the following command to view the details of the ACL associated with a cluster called `kafka-cluster`
    
    
    gcloud managed-kafka acls list kafka-cluster \
      --location=us central1 \

The output is similar to the following:
    
    
    ---
    aclEntries:
    - host: '*'
      operation: ALL
      permissionType: ALLOW
      principal: User:admin@project.iam.gserviceaccount.com
    etag: W/da909178
    name: projects/gmk-consumer-smjo/locations/us-central1/clusters/default-cluster/acls/allTopics
    patternType: LITERAL
    resourceName: '*'
    resourceType: TOPIC
    ---
    aclEntries:
    - host: '*'
      operation: ALL
      permissionType: ALLOW
      principal: User:admin@project.iam.gserviceaccount.com
    etag: W/da909178
    name: projects/test-project/locations/us-central1/clusters/default-cluster/acls/cluster
    patternType: LITERAL
    resourceName: kafka-cluster
    resourceType: CLUSTER

The output includes the following information for each Managed Kafka ACL resource:

  * `aclEntries`: a list of access control entries for this ACL resource. Each entry defines a permission rule:

    * `host`: the host from which the principal can access the resource. `'*'` indicates any host.
    * `operation`: the Kafka operation type granted or denied. Examples—`ALL`, `READ`, `WRITE`.
    * `permissionType`: whether the operation is `ALLOW` or `DENY`.
    * `principal`: the user or service account to which the ACL entry applies. The format is typically `User:{google_service_account_email}` or the wildcard `User:*`.
  * `etag`: used for concurrency control during updates.

  * `name`: the unique identifier for the Managed Kafka ACL resource, including the project, location, cluster, and ACL ID.

  * `patternType`: the type of resource pattern defined by the ACL ID (`LITERAL` for a specific resource, `PREFIXED` for resources with a common prefix).

  * `resourceName`: the name of the Kafka resource to which the ACL applies. This can be a specific name like a topic name, a prefix, or a wildcard (`*`). For cluster-level ACLs, it is `kafka-cluster`.

  * `resourceType`: the type of Kafka resource to which the ACL applies such as `TOPIC`, `CLUSTER`, `GROUP`, `TRANSACTIONAL_ID`.




## What's next

  * [Create an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls)

  * [View an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/view-kafka-acl)

  * [Update an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/update-kafka-acls)

  * [Delete an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/delete-kafka-acl)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
