---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/delete-kafka-acl/
title: Delete a Managed Kafka ACL \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:28:13.547114+00:00
---

# Delete a Managed Kafka ACL  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/delete-kafka-acl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Delete a Managed Kafka ACL Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to delete a Managed Kafka ACL resource. Deleting an ACL removes all of the individual permission rules that are specified in the list of ACL entries.

**Caution:** If you delete the only Managed Kafka ACL that is associated with a particular resource pattern, you might unintentionally grant access for that pattern to all authenticated principals. For more information, see [Default access](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls#default-access).

## Required roles and permissions

To get the permission that you need to delete a Managed Kafka ACL, ask your administrator to grant you the [Managed Kafka ACL Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclEditor) (`roles/managedkafka.aclEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `managedkafka.acls.delete` permission, which is required to delete a Managed Kafka ACL. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete an ACL

###  gcloud 

Run the [`gcloud managed-kafka acls delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/delete) command:
    
    
    gcloud managed-kafka acls delete ACL_ID \
      --cluster=CLUSTER_ID \
      --location=LOCATION
    

Replace the following:

  * `ACL_ID`. The ID of the Managed Kafka ACL resource to delete. For more information, see [ACL ID](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-id).

  * `CLUSTER_ID` The ID of your Kafka cluster.

  * `LOCATION`: The region of your Kafka cluster.




This command permanently deletes the specified ACL resource and all the underlying Apache Kafka ACL bindings associated with its resource pattern. You are prompted to confirm the deletion.

## Sample command

Run the following command to delete an ACL called `topic/test-topic`:
    
    
    gcloud managed-kafka acls delete topic/test-topic  \
      --project=test-project \
      --location=us-central1 \
      --cluster=test-cluster
    

The following is the sample output of the command:
    
    
    You are about to delete acl [topic/test-topic].
    Do you want to continue (Y/n)?  y
    Deleted acl [topic/test-topic].
    

The output of the `delete` command includes a confirmation prompt before proceeding with the deletion. Upon successful deletion, a message confirms that the ACL resource is removed.

## What's next

  * [List ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/list-kafka-acls)

  * [Create an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls)

  * [Add an ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
