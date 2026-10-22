---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-mirrormaker-connector/
title: Troubleshoot a MirrorMaker 2.0 connector \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:55.397064+00:00
---

# Troubleshoot a MirrorMaker 2.0 connector  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-mirrormaker-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Troubleshoot a MirrorMaker 2.0 connector Stay organized with collections  Save and categorize content based on your preferences. 

This document provides troubleshooting guidance for common issues encountered when using a [MirrorMaker 2.0 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector).

## Common MirrorMaker 2.0 errors

This section lists common errors that you might see when using a MirrorMaker 2.0 connector.

### Timed out waiting for a node assignment

If the Connect cluster cannot access the Kafka cluster, you get the following error:
    
    
    Timed out waiting for a node assignment.
    

Causes for this error include the following:

  * The Connect cluster cannot authenticate with the Kafka cluster. Check the authentication parameters in the connector configuration. For more information, see [Create a MirrorMaker 2.0 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector#before-you-begin).

  * A networking issue prevents the Connect cluster from reaching the Kafka cluster. Follow the steps in Troubleshoot networking issues.




### DNS resolution failed

If the Connect cluster can't resolve the bootstrap address, you get the following error:
    
    
    No resolvable bootstrap urls given in bootstrap.servers
    

You might also get an error similar to the following:
    
    
    Couldn't resolve server BOOTSTRAP_ADDRESS from bootstrap.servers as DNS resolution failed for BOOTSTRAP_ADDRESS
    

To resolve this issue, first verify that the bootstrap address is correct. If it is, then follow the steps in Troubleshoot domain name resolution.

### Invalid credentials

If the Connect cluster can't authenticate with one of the Kafka clusters, you get an error similar to the following:
    
    
    org.apache.kafka.clients.NetworkClient processDisconnection
    SEVERE: [AdminClient clientId=source->target|mm2|offset-syncs-source-admin] Connection to
    node 11 (broker-1.BOOTSTRAP_ADDRESS/IP_ADDRESS:9092) failed authentication due to: Authentication
    failed during authentication due to invalid credentials with SASL mechanism OAUTHBEARER
    

Possible causes for this error include the following:

  * **The Managed Kafka Service Account for one or both clusters is missing the Managed Kafka Service Agent role.**

For each Managed Service for Apache Kafka cluster, grant the [Managed Kafka Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/managedkafka#managedkafka.serviceAgent) IAM role to the Managed Kafka Service Account for that cluster's project. For more information, see [Configure Managed Service for Apache Kafka networking](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).

  * **Authentication to a self-managed or external cluster failed.**

For self-managed or external Kafka clusters, make sure the authentication properties are correct for the cluster. The details depend on your cluster setup. For more information, see [Create a MirrorMaker 2 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector).

  * **The clusters are not inside the same VPC Service Controls perimeter.**

If you are using VPC Service Controls to isolate your Kafka clusters, make sure the clusters are inside the same perimeter. For more information, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).




### Principal is denied operation

If you create an Apache Kafka [access control list](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/access-control-kafka-acls) (ACL), and the ACL doesn't give read and write permissions to the Managed Kafka Service Account, you get an error similar to the following:
    
    
    Principal = User:SERVICE_ACCOUNT is Denied operation = OPERATION from host = HOST
    on resource = Topic:LITERAL:TOPIC for request = TOPIC with resourceRefCount = 1 based on rule DefaultDeny
    

By default, Managed Service for Apache Kafka clusters operate with `allow.everyone.if.no.acl.found` set to `true`, which gives the Managed Kafka Service Account read and write access to cluster resources.

However, if you set any ACLs, those ACLs must give read and write permissions to the service account. Otherwise, the Connect cluster loses read and write permissions on all topics, and loses read permission on all consumer groups.

To resolve this issue, add ACL entries that grant the necessary permissions to the Managed Kafka Service Account. To do so, follow the steps in [Add an ACL entry to a Managed Kafka ACL](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/add-acl-entry).

  * The principal is `User:service-PROJECT_NUMBER@gcp-sa-managedkafka.iam.gserviceaccount.com`. Replace PROJECT_NUMBER with your Google Cloud project number.

  * Grant read and write access to specific topics, and grant read access to specific consumer groups. For information about how to specify resources for an ACL, see [ACL ID](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-acls/create-kafka-acls#acl-id).




### Messages are not duplicated

To troubleshoot this issue, check the connector configuration. If you are using the primary Kafka cluster as the source cluster, set `producer.override.bootstrap.servers` to the bootstrap address of the target cluster.

## Troubleshoot networking issues

If you experience networking issues when using a MirrorMaker 2.0 connector, perform the following troubleshooting steps.

  * When connecting to a Managed Service for Apache Kafka cluster:

    1. Look up the Connect cluster's [worker subnet](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#worker-subnet) and find the subnet's VPC network.

    2. View the primary Kafka cluster's [configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster) and find the list of subnets. At least one subnet must be in the same VPC network as the Connect cluster's subnet.

    3. Repeat the previous step for the secondary Kafka cluster.

    4. Make sure that firewall rules allow the Private Service Connect interface to reach both the source and target Kafka clusters.

  * When connecting to an external or self-managed Kafka cluster:

    1. Look up the Connect cluster's [worker subnet](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#worker-subnet) and find the subnet's VPC network.

    2. Verify that the Kafka cluster can be accessed from the VPC network. For example, you can deploy the Kafka cluster in the same VPC network, or make the cluster reachable from the VPC network by using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) or [DNS zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview).

1 If either the source or target Kafka cluster is accessed over the internet, configure a [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to allow the Connect cluster workers to access the internet.




For more information about networking in Managed Service for Apache Kafka, see [Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/networking-kafka).

## Troubleshoot domain name resolution

If you experience problems with domain name resolution when using a MirrorMaker 2.0 connector, perform the following troubleshooting steps:

  1. Look up the Connect cluster's [worker subnet](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-connect-cluster#worker-subnet) and find the subnet's VPC network.

  2. In the Google Cloud console, go to the **Cloud DNS zones** page.

[Go to DNS Zones](https://console.cloud.google.com/net-services/dns/zones)

  3. Select the Google Cloud project that contains the VPC network.

  4. Click **Zones** and verify that the domain name appears in the list of DNS zones.

  5. View the Connect cluster's [configuration](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/view-connect-cluster) and find the list of resolvable DNS domains. If the domain name is not listed, update the Connect cluster to add the DNS domain. See [Update a Connect cluster](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/update-connect-cluster).




## What's next

  * [Troubleshoot Connect clusters and connectors](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/troubleshoot-kafka-connect)
  * [Create a MirrorMaker 2.0 connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector)



_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
