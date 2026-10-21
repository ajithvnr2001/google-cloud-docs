---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry/
title: Add an ACL entry to a Managed Kafka ACL \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:13.023420+00:00
---

# Add an ACL entry to a Managed Kafka ACL  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Add an ACL entry to a Managed Kafka ACL Stay organized with collections  Save and categorize content based on your preferences. 

The document describes how to create an [ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-entries) and add it to a Managed Kafka ACL resource. If the Managed Kafka ACL resource doesn't exist, this operation also creates the ACL resource.

This operation is analogous to creating a single Apache Kafka ACL binding. Unlike the [update operation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/update-kafka-acls), it doesn't require an ETag for concurrency control.

## Required roles and permissions

To get the permission that you need to add an ACL entry, ask your administrator to grant you the [Managed Kafka ACL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `managedkafka.acls.updateEntries` permission, which is required to add an ACL entry. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Add an ACL entry

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster where you want to add an ACL entry.

  3. Click the **Access control** tab.

  4. Click **Create ACL entry**.

  5. In the **Create ACL entry** panel, enter the details of the ACL entry:

     1. In the **Resource type** list, select the type of cluster resource that this ACL applies to. For more information, see [ACL ID](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-id).

     2. If the resource type is `Topic`, `Consumer group`, or `Transactional ID`, select or enter the ID of the resource.

     3. If the resource type is `Topic prefix`, `Consumer group prefix`, or `Transactional ID prefix`, enter the prefix for the ACL to match against.

     4. In the **Principal** field, enter the [principal](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-principal) for the ACL entry.

     5. In the **Permission type** list, select `ALLOW` or `DENY`.

     6. In the **Operation** list, select the [operation type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-operation) for the ACL entry.

  6. Click **Create**.




###  gcloud 

Run the [`gcloud managed-kafka acls add-acl-entry`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/add-acl-entry) command:
    
    
    gcloud managed-kafka acls add-acl-entry ACL_ID \
      --cluster=CLUSTER_ID \
      --location=LOCATION \
      --principal=PRINCIPAL \
      --operation=OPERATION \
      --permission-type=PERMISSION_TYPE \
      --host=*
    

Replace the following:

  * `ACL_ID`. The ID of the Managed Kafka ACL resource to update. For more information, see [ACL ID](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-id). If a Managed Kafka ACL with this ID doesn't exist, one is automatically created.

  * `CLUSTER_ID`: The ID of your Kafka cluster.

  * `LOCATION`: The region of your Kafka cluster.

  * `PRINCIPAL`: The [principal](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-principal) for the new ACL entry.

  * `OPERATION`: The [operation type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-operation), such as `READ` or `CREATE`.

  * `PERMISSION_TYPE`: The permission that the principal has for the operation. Specify either `ALLOW` or `DENY`.




## Sample command

Run the following command to allow a specific service account to read from a topic named `test-topic` in the cluster `test-cluster` in the `us-central1` region.
    
    
    gcloud managed-kafka acls add-acl-entry topic/test-topic \
      --cluster=test-cluster \
      --location=us-central1 \
      --principal='User:service-account@test-project.iam.gserviceaccount.com' \
      --operation=READ \
      --permission-type=ALLOW \
      --host='*'
    

Here is a sample output:
    
    
    acl:
      aclEntries:
      - host: '*'
        operation: READ
        permissionType: ALLOW
        principal: 'User:service-account@test-project.iam.gserviceaccount.com'
      etag: W/another-new-etag
      name: projects/test-project/locations/us-central1/clusters/test-cluster/acls/topic/test-topic
      patternType: LITERAL
      resourceName: test-topic
      resourceType: TOPIC
    aclCreated: false
    

The output of the `add-acl-entry` command provides information about the resulting ACL state:

  * `acl`: this section describes the updated ACL resource after the new entry has been added.

    * `aclEntries`: this is a list containing all the access control entries for this ACL. In this example, it would now include the entry just added. Each entry has the following fields:

      * `host`: the host for the ACL entry.
      * `operation`: the Kafka operation this entry applies to.
      * `permissionType`: whether the access is `ALLOW` or `DENY`.
      * `principal`: the user or service account this entry is for.
    * `etag`: this is the entity tag for the updated ACL. It's used for optimistic concurrency control during subsequent updates. The value changes after an entry is added.

    * `name`: the unique identifier for the ACL resource. It follows the format `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`.

    * `patternType`: the type of resource pattern for this ACL.

    * `resourceName`: the name of the Kafka resource to which this ACL applies.

    * `resourceType`: the type of Kafka resource.

  * `aclCreated`: a boolean value indicating whether the ACL resource was created as a result of adding this entry.




## What's next

  * [Create an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls)

  * [View an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/view-kafka-acl)

  * [Update an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/update-kafka-acls)

  * [Delete an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/delete-kafka-acl)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
