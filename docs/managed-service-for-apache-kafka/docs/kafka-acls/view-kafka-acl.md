---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/view-kafka-acl/
title: View a Managed Kafka ACL \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:08:16.621555+00:00
---

# View a Managed Kafka ACL  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/view-kafka-acl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  View a Managed Kafka ACL Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view the details of a Managed Kafka ACL resource, including:

  * The [ACL entries](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-entries), which define the permissions that are in effect for the ACL's resource pattern.

  * The [ETag](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#etag) used for concurrency control.




## Required roles and permissions

To get the permission that you need to view a Managed Kafka ACL, ask your administrator to grant you the [Managed Kafka ACL Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.aclViewer) (`roles/managedkafka.aclViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `managedkafka.acls.get` permission, which is required to view a Managed Kafka ACL. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View an ACL

###  gcloud 

Run the [`gcloud managed-kafka acls describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/acls/describe) command:
    
    
    gcloud managed-kafka acls describe ACL_ID \
      --cluster=CLUSTER_ID \
      --location=LOCATION
    

Replace the following:

  * `ACL_ID` The ID of the Managed Kafka ACL resource to view. For more information, see [ACL ID](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-id).

  * `CLUSTER_ID` The ID of your Kafka cluster.

  * `LOCATION`: The region of your Kafka cluster.




## Sample command

Run the following command to display the properties of the specified Managed Service for Apache Kafka ACL resource called `test_ACL`.
    
    
    gcloud managed-kafka acls describe test_ACL \
      --cluster=default-cluster \
      --location=us-central1 \

Here is a sample output of the command. The output displays the ACL ID, the resource pattern it applies to, its current eTag to be used for updates, and the list of individual ACL entries
    
    
    aclEntries:
    - host: '*'
      operation: ALL
      permissionType: ALLOW
      principal: User:admin@test-project.iam.gserviceaccount.com
    etag: W/da909178
    name: projects/test-project/locations/us-central1/clusters/default-cluster/acls/test_ACL
    patternType: LITERAL
    resourceName: default-cluster
    resourceType: CLUSTER
    

The output of the `describe` command provides information about the Managed Service for Apache Kafka ACL resource:

  * `aclEntries`: this is a list containing all the access control entries (permission rules) defined for this ACL. Each entry has the following fields:

    * `host`: the client host for the ACL entry.
    * `operation`: the Kafka operation to which this entry applies.
    * `permissionType`: whether the access is `ALLOW` or `DENY`.
    * `principal`: the user or service account this entry is for.
  * `etag`: this is the entity tag for the ACL resource. It's used for optimistic concurrency control during subsequent updates.

  * `name`: the unique identifier for the ACL resource. It follows the format `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`.

  * `patternType`: the type of resource pattern for this ACL, such as `LITERAL`.

  * `resourceName`: the name of the Kafka resource to which this ACL applies.

  * `resourceType`: the type of Kafka resource.




## What's next

  * [List ACLs](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/list-kafka-acls)

  * [Create an ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls)

  * [Add an ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
