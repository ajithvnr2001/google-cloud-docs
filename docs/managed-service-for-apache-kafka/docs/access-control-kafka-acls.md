---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls/
title: Access control with Kafka ACLs \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:53.431499+00:00
---

# Access control with Kafka ACLs  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Access control with Kafka ACLs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use Apache Kafka access control lists (ACLs) for access control in Google Cloud Managed Service for Apache Kafka.

Apache Kafka ACLs provide fine-grained access control within the Kafka cluster. Managed Service for Apache Kafka enables the out-of-the-box `StandardAuthorizer`, which stores ACLs in the KRaft-based Kafka cluster metadata.

  * These ACLs control which authenticated users can perform specific operations on specific Kafka resources, like producing or consuming messages on a topic.

  * These ACLs are useful to control interactions with the cluster using standard Apache Kafka clients, which are only subject to a cluster-level IAM check for the initial connection. For more information, see [Access control with IAM](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control).




## How Kafka ACL access control works

The client interacts with Kafka's standard ACL authorizer within the cluster. The authorizer evaluates the relevant Apache Kafka ACLs to authorize specific operations requested by the principal, such as producing to a topic or consuming from a group. The principal used for the ACL check is derived from one of the following authentication methods:

  * **SASL:** the IAM principal such as a service account email.

  * **mTLS:** the Distinguished Name (DN) from the client certificate, potentially transformed by [principal mapping rules](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls#principal-mapping).




For comprehensive security, you must configure the following:

  * IAM permissions for management access. For more information, see [Access control with IAM](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-iam).

  * Kafka ACLs for in-cluster data access and operations from open-source Apache Kafka clients, independent of the authentication method.




## Usage of Apache Kafka ACLs

Apache Kafka ACL bindings have the following format:
    
    
    Principal P is [Allowed/Denied] Operation O From Host H on any resource matching Resource Pattern RP.
    
    

The following is a list of important information about the format:

  * Principal(P): The user identity being authorized. This is prefixed with `User:`.

    * For SASL authentication, this is the IAM principal, such as `User:my-service-account@my-project.iam.gserviceaccount.com`.

    * For mTLS authentication, this is the Distinguished Name (DN) from the client certificate, such as `User:CN=my-client,OU=my-org-unit`. The exact format depends on the certificate's Subject. [Principal mapping rules](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls#principal-mapping) can transform this value.

  * Permission type(Allowed/Denied): whether the ACL binding allows or denies access. Deny bindings take precedence.

  * Operation(O): the action performed such as Read, Write, or Create. For information about which operations apply to which resources for various Kafka protocols, see [Operations and Resources on Protocols](https://kafka.apache.org/37/security/authorization-and-acls/#operations-and-resources-on-protocols) in the Apache Kafka documentation.

  * Host(H): the machine from which the request originates. Since Managed Service for Apache Kafka translates client network addresses, use of hosts other than `'*'` is not supported.

  * Resource Pattern(RP): a pattern used to match specific resources. A resource pattern consists of a resource type, a resource name, and a pattern type (`LITERAL` or `PREFIXED`).




### Default access

Managed Service for Apache Kafka clusters operate with the Apache Kafka property `allow.everyone.if.no.acl.found` set to `true`. The presence or absence of Kafka ACLs directly dictates the level of access to resources:

  * If no Kafka ACLs are defined for a specific resource like a topic, all authenticated principals are granted access to it. This configuration lets Managed Service for Apache Kafka clusters be immediately operable, without the requirement to configure ACLs.

  * As soon as you define any Kafka ACL for that resource, access becomes restricted. Only principals explicitly granted permission using an `ALLOW` entry in a Kafka ACL can access matching resources (unless specifically blocked by a `DENY` entry).




Managed Service for Apache Kafka gives its [service agent](https://docs.cloud.google.com/iam/docs/service-agents) administrative access to your cluster. This access allows the service agent to perform operations requested by the Managed Service for Apache Kafka API, regardless of other ACLs configured in the cluster. Managed Service for Apache Kafka accomplishes this by modifying the `StandardAuthorizer` implementation. The modification grants the service agent permissions similar to super users, except for read and write operations. You cannot change this configuration.

### Kafka principals

Kafka principals for Managed Service for Apache Kafka clusters are specified with the Kafka StandardAuthorizer prefix `"User:"`.

  * **For SASL/IAM:** the principal is the Google Cloud account. For example, to grant access to the service account `test-kafka-client@test-project.iam.gserviceaccount.com`, use the Kafka principal `"User:test-kafka-client@test-project.iam.gserviceaccount.com"`. Kafka ACL principals must specify a user, a service account, or an individual IAM principal, but not a group or principal set. Kafka ACLs don't support resolving group memberships for Google Cloud principals.

  * **For mTLS:** the principal is derived from the client certificate's Subject Distinguished Name (DN). For example, `User:CN=client1,OU=dev,O=MyOrg,L=City,ST=State,C=US`. You can use [mTLS principal mapping rules](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka-mtls#principal-mapping) to transform the DN into a more user-friendly principal string for ACLs.




To create an ACL that applies to all members of a Google Group or principal set, you can use a proxy service account principal and service account impersonation:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) to use as a proxy for the group.

  2. Grant the Google Group or principal set the [Service Account Token Creator role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) on the service account. See [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#single-role)

  3. Add Kafka ACLs for the proxy service account. An example principal would be: `User:group-proxy@test-project.iam.gserviceaccount.com`.

  4. Use [service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation) in Kafka clients to authenticate to Kafka as the service account. Google Cloud IAM authorizes an individual principal as a member of the group that's allowed to impersonate the proxy service account. And Kafka authorizes the proxy service account against existing ACLs in the cluster.




### Kafka operations for producers and consumers

An operation is an action performed on a resource. For each resource, an operation is mapped to one or more Kafka protocol requests for that resource. For example, a `READ` operation for the `topic` resource type is mapped to `Fetch`, `OffsetCommit`, and `TxnOffsetCommit` Apache Kafka protocols.

To grant a principal producer access on a topic, perform the following steps:

  1. On the topic resource, allow the `WRITE` and `CREATE` operations.

  2. If using transactional IDs, on the transactional ID resource, allow the `WRITE` operation.




To grant a principal consumer access on a topic, perform the following steps:

  1. On the topic resource, allow the `READ` operation.

  2. On the consumer group resource, allow the `READ` operation.




For more information about the valid operations on resources that the Kafka API supports, see [Operations and Resources on Protocols](https://kafka.apache.org/37/security/authorization-and-acls/#operations-and-resources-on-protocols) in the Apache Kafka documentation.

### Configure ACLS for default-deny behavior

Managed Kafka clusters are configured with `allow.everyone.if.no.acl.found = true`. So by default, if no ACLs are set on a resource, all principals can access the resource.

To configure a `default-deny` behavior similar to that in IAM, you can first configure access for an administrator user on all resources in the cluster. As a result, every resource gets an ACL defined on it, and the `allow.everyone.if.no.acl.found` behavior is suppressed. By default, any principal not explicitly allowed by an `ALLOW` ACL is denied access.

For example, to set ACLs on all resources in the cluster for the service account `clusterAdmin@test-project.iam.gserviceaccount.com`, create the following ACL entries.

The following gcloud CLI command grants a service account named `clusterAdmin@test-project.iam.gserviceaccount.com` full administrative access (`--operation=ALL`) to a specific Kafka cluster located in a particular region. This permission allows the service account to perform any operation on the cluster from any host.
    
    
    gcloud managed-kafka acls add-acl-entry cluster \
        --principal=`User:clusterAdmin@test-project.iam.gserviceaccount.com` \
        --operation=ALL \
        --permission-type=ALLOW \
        --host=* \
        --cluster=CLUSTER_ID \
        --location=LOCATION
    

The following gcloud CLI command grants a service account named `clusterAdmin@test-project.iam.gserviceaccount.com` full administrative access (`--operation=ALL`) to all topics within a specific Kafka cluster located in a particular region. This permission allows the service account to perform any operation on all topics from any host.
    
    
    gcloud managed-kafka acls add-acl-entry allTopics \
        --principal=`User:clusterAdmin@test-project.iam.gserviceaccount.com` \
        --operation=ALL \
        --permission-type=ALLOW \
        --host=* \
        --cluster=CLUSTER_ID \
        --location=LOCATION
    

The following gcloud CLI command grants a service account named `clusterAdmin@test-project.iam.gserviceaccount.com` full administrative access (`--operation=ALL`) to all consumer groups within a specific Kafka cluster located in a particular region. This permission allows the service account to perform any operation on all consumer groups from any host.
    
    
    gcloud managed-kafka acls add-acl-entry allConsumerGroups \
        --principal=`User:clusterAdmin@test-project.iam.gserviceaccount.com` \
        --operation=ALL \
        --permission-type=ALLOW \
        --host=* \
        --cluster=CLUSTER_ID \
        --location=LOCATION
    

The following gcloud CLI command grants a service account named `clusterAdmin@test-project.iam.gserviceaccount.com` full administrative access (`--operation=ALL`) to all transactional IDs within a specific Kafka cluster located in a particular region. This permission allows the service account to perform any operation on all transactional IDs from any host.
    
    
    gcloud managed-kafka acls add-acl-entry allTransactionalIds \
        --principal=`User:clusterAdmin@test-project.iam.gserviceaccount.com` \
        --operation=ALL \
        --permission-type=ALLOW \
        --host=* \
        --cluster=CLUSTER_ID \
        --location=LOCATION
    

The following is a list of important information about the commands:

  * `--principal='User:test-kafka-client@test-project.iam.gserviceaccount.com'`: the principal to whom the ACL applies. The principal is a Google Cloud account, with the Kafka StandardAuthorizer prefix `User:`.

  * `--operation=all`: the Kafka operation being granted, which is full access in this case.

  * `--permission-type=ALLOW`: this ACL entry grants access.

  * `--host='*'`: the host from which the principal can access the resource. `'*'` grants access from any host. Managed Service for Apache Kafka only supports ACLs with host `'*'`.

  * CLUSTER_ID: the name of your Managed Service for Apache Kafka cluster.

  * LOCATION: the Google Cloud region where your Managed Service for Apache Kafka cluster is located such as `us-central1`.




### Configure ACLs

You can configure Apache Kafka ACLs with the Managed Service for Apache Kafka ACL APIs, or with open-source Apache Kafka tools such as Apache Kafka authorizer cli [`kafka-acls.sh`](https://kafka.apache.org/37/security/authorization-and-acls/#command-line-interface), or `Admin Client`.

Managed Service for Apache Kafka organizes ACLs by Kafka resource patterns. The resource pattern is defined by the following:

  * Resource type: cluster, topic, consumer group, or transactional ID

  * Pattern type: literal, or prefixed (all resources whose name start with the provided string)

  * Resource name: the resource name or prefix to which the ACL entries apply.




A Managed Service for Apache Kafka ACL resource represents all access control configured for a single Kafka resource pattern, as a repeated list of ACL entries. The name of the ACL resource uniquely identifies the resource pattern of the ACL binding. For more information, see [ACL ID](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/guidelines-resource#acl-id).

You can manage Managed Service for Apache Kafka ACLs at the ACL resource level (all ACL entries for a resource pattern), or incrementally by adding and removing individual ACL entries for an ACL resource pattern.

For more information, see [Create a Managed Kafka ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls) and [Add a Managed Kafka ACL entry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry).

### Allow reading from a topic

To allow open-source Apache Kafka clients running as the service account `test-kafka-client@test-project.iam.gserviceaccount.com` to read from the topic `topic-name`, create a Managed Service for Apache Kafka ACL entry using the [`managed-kafka acls add-acl-entry` command](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry):
    
    
    gcloud managed-kafka acls add-acl-entry topic/topic-name \
        --cluster=CLUSTER_ID \
        --location=LOCATION
        --principal='User:test-kafka-client@test-project.iam.gserviceaccount.com' \
        --operation=READ \
        --permission-type=ALLOW \
        --host='*'
    

The following is a list of important information about the command:

  * `topic/topic-name`: specifies the Managed Service for Apache Kafka topic to which you want to grant access. Replace `topic-name` with the actual name of your topic. The `topic/` prefix indicates that this ACL entry applies to a specific (literal) topic resource pattern.

  * `LOCATION`: the Google Cloud region where your Managed Service for Apache Kafka cluster is located, such as `us-central1`.

  * `CLUSTER_ID`: the name of your Managed Service for Apache Kafka cluster.

  * `--principal='User:test-kafka-client@test-project.iam.gserviceaccount.com'`: the principal to whom the ACL applies. The principal is a Google Cloud account, with the Kafka StandardAuthorizer prefix `User:`.

  * `--operation=READ`: the Kafka operation being granted, which is `READ` in this case.

  * `--permission-type=ALLOW`: indicates that this ACL entry grants access.

  * `--host='*'`: specifies the host from which the principal can access the resource. `'*'` grants access from any host. Managed Service for Apache Kafka only supports ACLs with host `'*'`.




To remove read access, you can use the [`remove-acl-entry` command](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/remove-acl-entry) with the same parameters.
    
    
    gcloud managed-kafka acls remove-acl-entry topic/topic-name \
        --cluster=CLUSTER_ID \
        --location=LOCATION
        --principal='User:test-kafka-client@test-project.iam.gserviceaccount.com' \
        --operation=READ \
        --permission-type=ALLOW \
        --host='*'
    

### Allow writing to all topics with a common prefix

To allow open-source Apache Kafka clients running as the service account `test-kafka-client@test-project.iam.gserviceaccount.com` to write to all topics whose name starts with the prefix `topic-prefix`, add a Managed Kafka ACL entry as follows:
    
    
    gcloud managed-kafka acls add-acl-entry topicPrefixed/topic-prefix \
        --cluster=CLUSTER_ID \
        --location=LOCATION
        --principal='User:test-kafka-client@test-project.iam.gserviceaccount.com' \
        --operation=WRITE \
        --permission-type=ALLOW \
        --host='*'
    

The following is a list of important information about the command:

  * `topicPrefixed/topic-prefix`: specifies the Managed Service for Apache Kafka resource pattern to which you want to grant access. Replace `topic-prefix` with the actual prefix of your topics. The `topicPrefixed/` prefix indicates that this ACL entry applies to a prefixed resource pattern: all topics matching the given prefix.

  * `PROJECT`: the ID of your Google Cloud project where your Managed Service for Apache Kafka cluster is located.

  * `LOCATION`: the Google Cloud region where your Managed Service for Apache Kafka cluster is located such as `us-central1`.

  * `CLUSTER_ID`: the name of your Managed Service for Apache Kafka cluster.

  * `--principal='User:test-kafka-client@test-project.iam.gserviceaccount.com'`: the principal to whom the ACL applies. The principal is a Google Cloud account, with the Kafka StandardAuthorizer prefix `User:`.

  * `--operation=WRITE`: the Kafka operation being granted, which is `WRITE` in this case.

  * `--permission-type=ALLOW`: this ACL entry grants access.

  * `--host='*'`: the host from which the principal can access the resource. `'*'` grants access from any host. Managed Service for Apache Kafka only supports ACLs with host `'*'`.




To remove write access for this service account, remove the ACL entry:
    
    
    gcloud managed-kafka acls remove-acl-entry topicPrefixed/topic-prefix \
        --cluster=CLUSTER_ID \
        --location=LOCATION
        --principal='User:test-kafka-client@test-project.iam.gserviceaccount.com' \
        --operation=WRITE \
        --permission-type=ALLOW \
        --host='*'
    

### Deny modifying all topics

To prevent open-source Apache Kafka clients running as the service account `test-kafka-client@test-project.iam.gserviceaccount.com` from modifying all topics in a cluster, you can create a Managed Service for Apache Kafka ACL resource with a list of `AclEntry` resources to deny the `ALTER`, `ALTER_CONFIGS`, and `DELETE` operations on all topics. This approach defines the required state in a single configuration.

Alternatively, you can achieve the same result by imperatively adding three separate ACL entries using the `gcloud managed-kafka acls add-acl-entry` command. This method involves running the command to deny access to each of the operations `ALTER`, `ALTER_CONFIGS`, and `DELETE`, as follows:
    
    
    gcloud managed-kafka acls add-acl-entry allTopics \
        --cluster=CLUSTER_ID \
        --location=LOCATION
        --principal='User:test-kafka-client@test-project.iam.gserviceaccount.com' \
        --operation=ALTER \
        --permission-type=DENY \
        --host='*'
    
    
    
    gcloud managed-kafka acls add-acl-entry allTopics \
        --cluster=CLUSTER_ID \
        --location=LOCATION
        --principal='User:test-kafka-client@test-project.iam.gserviceaccount.com' \
        --operation=ALTER_CONFIGS \
        --permission-type=DENY \
        --host='*'
    
    
    
    gcloud managed-kafka acls add-acl-entry allTopics \
        --cluster=CLUSTER_ID \
        --location=LOCATION
        --principal='User:test-kafka-client@test-project.iam.gserviceaccount.com' \
        --operation=DELETE \
        --permission-type=DENY \
        --host='*'
    

The following information applies to each of the `add-acl-entry` commands:

  * `allTopics`: specifies that this ACL applies to all topics within the Managed Service for Apache Kafka cluster.

  * `LOCATION`: the Google Cloud region where your Managed Service for Apache Kafka cluster is located such as `us-central1`.

  * `CLUSTER_ID`: the name of your Managed Service for Apache Kafka cluster.

  * `--principal='User:test-kafka-client@test-project.iam.gserviceaccount.com'`: specifies the principal to whom the ACL applies. The principal is a Google Cloud account, with the Kafka `StandardAuthorizer` prefix `User:`.

  * `--operation`: specifies the Kafka operation being denied:

    * `ALTER`: includes actions like changing the number of partitions or replication factor.

    * `ALTER_CONFIGS`: includes modifying topic-level configurations.

    * `DELETE`: includes deleting topics.

  * `--permission-type=DENY`: indicates that these ACL entries block access for the specified operations.

  * `--host='*'`: specifies that this denial applies regardless of the host from which the request originates. Managed Service for Apache Kafka only supports ACLs with host `'*'`.




To remove these restrictions, use the `remove-acl-entry` command for each of the added entries, using the same parameters. For example, to re-allow topic deletion:
    
    
    gcloud managed-kafka acls remove-acl-entry allTopics \
        --cluster=CLUSTER_ID \
        --location=LOCATION
        --principal='User:test-kafka-client@test-project.iam.gserviceaccount.com' \
        --operation=DELETE \
        --permission-type=DENY \
        --host='*'
    

### Troubleshooting ACLs

The Apache Kafka Standard Authorizer writes audit logs by default on authorization denials. If you receive a Kafka Authorization error, you can confirm the principal, resource, and operation that was denied by searching the cluster logs for `StandardAuthorizerData logAuditMessage`.

For example, here is a sample cluster log.
    
    
    org.apache.kafka.metadata.authorizer.StandardAuthorizerData logAuditMessage\n
    INFO: Principal = User:556291496362-compute@developer.iam.gserviceaccount.com is
    Denied operation = DESCRIBE from host = 172.16.0.20 on resource = Topic:LITERAL:t1
    for request = Metadata with resourceRefCount = 1 based on rule DefaultDeny
    

## What's next

  * [Access control with IAM](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control).

  * [Managed Service for Apache Kafka roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka).

  * [Apache Kafka documentation on ACLs](https://kafka.apache.org/37/security/authorization-and-acls/).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
