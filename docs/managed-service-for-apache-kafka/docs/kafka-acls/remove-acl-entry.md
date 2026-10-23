---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/remove-acl-entry/
title: Remove an ACL entry from a Managed Kafka ACL \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:15.475336+00:00
---

# Remove an ACL entry from a Managed Kafka ACL  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/remove-acl-entry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Remove an ACL entry from a Managed Kafka ACL Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to remove an [ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-entries) from a Managed Kafka ACL resource.

Removing an ACL entry is analogous to deleting a single Apache Kafka ACL binding. Unlike the [update operation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/update-kafka-acls), this operation doesn't require an ETag for concurrency control.

## Required roles and permissions

To get the permission that you need to remove an ACL entry, ask your administrator to grant you the [Managed Kafka ACL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `managedkafka.acls.updateEntries` permission, which is required to remove an ACL entry. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Remove an ACL entry

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click the name of the cluster that contains the ACL entry.

  3. Click the **Access control** tab.

  4. In the **ACL entries** list, select one or more ACL entries to delete.

  5. Click **Delete**.




###  gcloud 

Run the [`gcloud managed-kafka acls remove-acl-entry`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/remove-acl-entry) command:
    
    
    gcloud managed-kafka acls remove-acl-entry ACL_ID \
      --cluster=CLUSTER_ID \
      --location=LOCATION \
      --principal=PRINCIPAL \
      --operation=OPERATION \
      --permission-type=PERMISSION-TYPE \
      --host=*
    

Replace the following:

  * `ACL_ID`. The ID of the Managed Kafka ACL resource to update. For more information, see [ACL ID](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-id).

  * `CLUSTER_ID` The ID of your Kafka cluster.

  * `LOCATION` The region of your Kafka cluster.

  * `PRINCIPAL`: The [principal](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-principal) of the ACL entry to remove.

  * `OPERATION`: The [operation type](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-operation), such as `READ` or `CREATE`, of the ACL entry to remove.

  * `PERMISSION_TYPE`: The permission type (`ALLOW` or `DENY`) of the ACL entry to remove.




Together, the `--principal`, `--operation`, and `--permission-type` flags specify which ACL entry to remove.

## Sample command

Run the following command to remove an ACL entry that allows a specific service account to read from a topic named `test-topic` in the cluster `test-cluster` in the `us-central1` region. If this ACL entry was the only one, the ACL is deleted and the response contains `deleted: True`. Otherwise, the updated ACL entry is returned.
    
    
    gcloud managed-kafka acls remove-acl-entry topic/test-topic \
      --cluster=test-cluster \
      --location=us-central1 \
      --principal='User:service-account@test-project.iam.gserviceaccount.com' \
      --operation=READ \
      --permission-type=ALLOW \
      --host='*' \
    

## What's next

  * [List ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/list-kafka-acls)

  * [View an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/view-kafka-acl)

  * [Create an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls)

  * [Add an ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
