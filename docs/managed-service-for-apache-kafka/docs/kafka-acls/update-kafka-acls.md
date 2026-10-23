---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/update-kafka-acls/
title: Replace the ACL entries in a Managed Kafka ACL \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:55.389838+00:00
---

# Replace the ACL entries in a Managed Kafka ACL  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/update-kafka-acls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Replace the ACL entries in a Managed Kafka ACL Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to update a Managed Kafka ACL resource with a new list of ACL entries.

You can't update an ACL with an empty list of entries. To remove all ACL entries for an ACL, delete the Managed Kafka ACL resource. For more information, see [Delete a Managed Kafka ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/delete-kafka-acl).

You can also add or remove individual ACL entries. For more information, see the following documents:

  * [Add an ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry)
  * [Remove an ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/remove-acl-entry)



## Required roles and permissions

To get the permissions that you need to update a Managed Kafka ACL, ask your administrator to grant you the [Managed Kafka ACL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to update a Managed Kafka ACL. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to update a Managed Kafka ACL:

  * All: `managedkafka.acls.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Retrieve the ETag for the ACL

When you perform an update operation on a Managed Kafka ACL, you must provide an [ETag](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#etag). The ETag ensures that changes are applied to the same version of the ACL entries that exists in the Kafka cluster.

To get the current ETag for an ACL, see [View a Managed Kafka ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/view-kafka-acl).

If the ETag contains a terminal `'T'` character, it indicates that the ACL entries are truncated. In that case, you can't use the Managed Kafka API to perform the update operation. Instead, use standard Apache Kafka tools such as `kafka-acls.sh` or `AdminClient` to manage the ACLs directly.

## Replace ACL entries

###  gcloud 

Run the [`gcloud managed-kafka acls update`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/update) command:
    
    
    gcloud managed-kafka acls update ACL_ID \
        --cluster=CLUSTER_ID \
        --location=LOCATION \
        --etag=ETAG_VALUE \
        --acl-entry=principal='PRINCIPAL',operation=OPERATION_TYPE,permission_type=PERMISSION_TYPE,host='*' \
        --acl-entry= ...
    

Replace the following:

  * `ACL_ID`: The ID of the Managed Kafka ACL resource to update. For more information, see [ACL ID](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-id).

  * `CLUSTER_ID`: The ID of your Kafka cluster.

  * `LOCATION`: The region of your Kafka cluster.

  * `ETAG_VALUE`: The ETag for the ACL.




For each ACL entry that you want to include in the updated ACL, specify a separate `--acl-entry` flag and replace the following:

  * `PRINCIPAL`: The [principal](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-principal) for the ACL entry.

  * `OPERATION`: The [operation type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-operation), such as `READ` or `CREATE`.

  * `PERMISSION_TYPE`: The permission that the principal has for the operation. Specify either `ALLOW` or `DENY`.


**Important:** This command replaces the entire list of ACL entries, so make sure to include any existing entries that you want to keep.

### Example for replacing ACL entries

This command replaces all existing ACL entries for the `topic/orders` resource pattern in the `test-kafka-cluster` located in `us-central1` with a single new entry. This new entry grants `WRITE` permission to the service account `producer-app@test-project.iam.gserviceaccount.com`. The command requires the current `etag` of the ACL resource which is `"AYk=Ags="` in this example.
    
    
    gcloud managed-kafka acls update topic/orders \
        --cluster=test-kafka-cluster \
        --location=us-central1 \
        --project=test-project \
        --etag='"AYk=Ags="' \
        --acl-entry=principal='User:producer-app@test-project.iam.gserviceaccount.com',operation=WRITE,permission_type=ALLOW,host='*'
    

If the command is successful, the output shows the updated ACL resource configuration, including the new `aclEntries` list and a new `etag`. Any previously existing entries for this ACL resource are removed.
    
    
    aclEntries:
    -   host: '*'
      operation: WRITE
      permissionType: ALLOW
      principal: User:producer-app@test-project.iam.gserviceaccount.com
    etag: '"Bcn=Def="'  # Note: The etag value changes after a successful update.
    name: projects/test-project/locations/us-central1/clusters/my-kafka-cluster/acls/topic/orders
    resourcePatternType: TOPIC
    

## What's next

  * [Add an ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry)
  * [Remove an ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/remove-acl-entry)
  * [View a Managed Kafka ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/view-kafka-acl)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
