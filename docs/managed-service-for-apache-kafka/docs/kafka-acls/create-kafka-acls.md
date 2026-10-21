---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls/
title: Create a Managed Kafka ACL \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:12.924459+00:00
---

# Create a Managed Kafka ACL  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Create a Managed Kafka ACL Stay organized with collections  Save and categorize content based on your preferences. 

Managed Kafka access control lists (ACLs) provide fine-grained authorization for operations within your Managed Service for Apache Kafka cluster. Creating a Managed Kafka ACL resource defines a set of permission rules for a specific Kafka resource pattern. For foundational concepts, see the [Access control with IAM and Kafka ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control).

## Before you begin

Ensure you have an existing [Managed Service for Apache Kafka cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster).

### Required roles and permissions

To get the permission that you need to create a Managed Kafka ACL, ask your administrator to grant you the [Managed Kafka ACL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `managedkafka.acls.create` permission, which is required to create a Managed Kafka ACL. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Properties of a Managed Kafka ACL

When you create a Managed Kafka ACL resource, you must define the following properties:

### ACL ID

The ACL ID is a unique identifier for the Managed Kafka ACL resource within the cluster. The ACL ID also defines which cluster resources the ACL applies to. Use the following naming pattern for ACL IDs:

  * **ACL that applies to the cluster:** `cluster`

  * **ACLs that apply to a specific resource in the cluster:**

    * Topic: `topic/RESOURCE_NAME`
    * Consumer group: `consumerGroup/RESOURCE_NAME`
    * Transaction ID: `transactionalId/RESOURCE_NAME`

Replace `RESOURCE_NAME` with the name of the resource.

For example, to grant permissions on a topic named `my-topic`, the ACL ID is `topic/my-topic`.

  * **ACLs that apply to resources matching a prefix:**

    * Topics: `topicPrefixed/PREFIX`
    * Consumer groups: `consumerGroupPrefixed/PREFIX`
    * Transaction ID: `transactionalIdPrefixed/PREFIX`

Replace `PREFIX` with the prefix to match.

For example, to grant permissions on all topics starting with `test-`, the ACL ID is `topicPrefixed/test-`.

  * **ACLs that apply to all resources of a given type:**

    * All topics: `allTopics`
    * All consumer groups: `allConsumerGroups`
    * All transaction IDs: `allTransactionalIds`



After you create a Managed Kafka ACL, you can't change the ACL ID.

### ACL entries

An ACL entry defines a specific permission that a principal has on the cluster resources that match the ACL. When you create a Managed Kafka ACL, you must specify at least one ACL entry. You can add or remove ACL entries on an existing ACL.

The maximum number of ACL entries per Managed Kafka ACL resource is 100. If you need more rules for a single resource pattern, you must manage ACLs directly using standard Apache Kafka tools.

Each ACL entry contains the following fields:

Principal
    The user or service account to which the permission applies. Use the following format: `User:PRINCIPAL_EMAIL`. Replace PRINCIPAL_EMAIL with the email address of the principal. You can also set this field to `User:*`, which matches every principal.
Operation type
    The Kafka operation that the permission applies to, such as `ALL`, `READ`, `WRITE`, `CREATE`, `DELETE`, `ALTER`, `DESCRIBE`, `CLUSTER_ACTION`, `DESCRIBE_CONFIGS`, `ALTER_CONFIGS`, or `IDEMPOTENT_WRITE`. The value is case-insensitive. For valid operation and resource type combinations, see [Operations and Resources on Protocols](https://kafka.apache.org/37/security/authorization-and-acls/#operations-and-resources-on-protocols) in the Apache Kafka documentation.
Permission type
    The type of permission. Supported values are `ALLOW` and `DENY` (case-insensitive).
Host
    This field must be set to the wildcard character (`*`) for Managed Service for Apache Kafka.

### Output-only ACL properties

When you create a Managed Kafka ACL, the service sets the following properties on it:

  * Resource type: The ACL resource type. One of: `CLUSTER`, `TOPIC`, `GROUP`, or `TRANSACTIONAL_ID`.

  * Resource name: The ACL resource name or matching prefix. For the `CLUSTER` resource type, the value is always `"kafka-cluster"`. Can be the wildcard literal `"*"`.

  * ACL pattern type: Either `LITERAL` or `PREFIXED`.




These fields are output-only. You can use them to map Managed Kafka ACL resources to Kafka ACL bindings.

### ETag

When you create, view, or update a Managed Kafka ACL, the response includes an ETag. The ETag is used for optimistic concurrency control. Update operations on a Managed Kafka ACL must include the ETag, to ensure that changes are applied to the same version that exists in the Kafka Cluster. For more information, see [Replace the ACL entries in a Managed Kafka ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/update-kafka-acls).

If the ETag contains a terminal `'T'` character, it indicates that the ACL entries are truncated. More entries for the ACL exist on the Kafka Cluster, but can't be returned in the ACL description, due to limits on repeated fields.

## Create an ACL

When you create a Managed Kafka ACL, you can specify the ACL entries directly in the command line or by creating a file that contains the ACL entries.

### Specify ACL entries in the command line

###  gcloud 

Run the [`gcloud managed-kafka acls create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create) command:
    
    
    gcloud managed-kafka acls create ACL_ID \
      --cluster=CLUSTER_ID \
      --location=LOCATION \
      --acl-entry=principal=PRINCIPAL,operation=OPERATION,permission-type=PERMISSION_TYPE,host=*
    

Replace the following:

  * `ACL_ID`. The ID for the new ACL resource. The ID defines which cluster resources the ACL applies to. For more information, see ACL ID.

  * `CLUSTER_ID` The ID of your Kafka cluster.

  * `LOCATION` The region of your Kafka cluster.




For each ACL entry, specify a separate `--acl-entry` flag and replace the following:

  * `PRINCIPAL`: The principal for the ACL entry.

  * `OPERATION`: The operation type, such as `READ` or `CREATE`.

  * `PERMISSION_TYPE`: The permission that the principal has for the operation. Specify either `ALLOW` or `DENY`.




### Specify ACL entries in a file

###  gcloud 

  1. Create a local file that defines the ACL entries in YAML format:
         
         ---
         aclEntries:
         - principal: PRINCIPAL
           operation: OPERATION
           permissionType: PERMISSION_TYPE
           host: "*"
         - principal: ...
           operation: ...
           permissionType: ...
           host: "*"
         

For each ACL entry in the `aclEntries` list, replace the following:

     * `PRINCIPAL`: The principal for the ACL entry.

     * `OPERATION`: The operation type, such as `READ` or `CREATE`.

     * `PERMISSION_TYPE`: The permission that the principal has for the operation. Specify either `ALLOW` or `DENY`.

  2. Run the [`gcloud managed-kafka acls create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/create) command:
         
         gcloud managed-kafka acls create ACL_ID \
           --cluster=CLUSTER_ID \
           --location=LOCATION \
           --acl-entries-from-file=FILE_PATH
         

Replace the following:

     * `ACL_ID`. The ID for the new ACL resource. The ID defines which cluster resources the ACL applies to. For more information, see ACL ID.

     * `CLUSTER_ID` The ID of your Kafka cluster.

     * `LOCATION` The region of your Kafka cluster.

     * `FILE_PATH`: The path to the local file containing the ACL entries list.




## What's next?

  * [View an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/view-kafka-acl)

  * [Update an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/update-kafka-acls)

  * [Delete an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/delete-kafka-acl)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
