---
url: https://docs.cloud.google.com/pubsub/docs/amazon-msk-import-topic-troubleshooting/
title: Troubleshooting an Amazon Managed Streaming for Apache Kafka import topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:26.900726+00:00
---

# Troubleshooting an Amazon Managed Streaming for Apache Kafka import topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/amazon-msk-import-topic-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshooting an Amazon Managed Streaming for Apache Kafka import topic Stay organized with collections  Save and categorize content based on your preferences. 

This document provides some common troubleshooting tips for Amazon Managed Streaming for Apache Kafka (Amazon MSK) import topics.

After you configure the import topic and start ingesting messages, you can check the relevant Cloud Monitoring metrics to see if data is ingested. Perform the following steps:

  1. In the console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the Amazon MSK import topic that you want to troubleshoot.

  3. In the topic details page, click the **Metrics** tab.

  4. Check the chart for the metric **Ingestion byte count**.

  5. If no data is being ingested, in the topic details page, check to see if there is an error for the **Topic state** field.

  6. You can also check the metric **Ingestion data source state**. To do so, in the topic details page, click the **Metrics** tab.

  7. Here is a list of errors that you might encounter:

Error Code | Description | Fix  
---|---|---  
`MSK_PERMISSION_DENIED ` | Error consuming Amazon MSK data due to permission issues. | Verify the AWS role ARN for accuracy and check that the AWS role has the required read permissions. For more information, see [Create a policy in AWS.](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#create-AWS-policy)  
Ensure that a service account exists and that it is correctly configured as described in the procedure [Create a role in AWS using a custom trust policy.](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#create_id) For more information about how to create a service account, see [Create a service account in Google Cloud.](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#create-service-account)  
Verify that the Pub/Sub service account has the `iam.serviceAccounts.getOpenIdToken` permission. For more information, see [Add the Service Account Token Creator role to the Pub/Sub service account.](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#add-service-account-token-creator)  
Verify that you have added the service account user role to the service account. For more information, see [Add the service account user role to the service account.](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#add-service-account-role)  
`PUBLISH_PERMISSION_DENIED` | Error publishing to the Pub/Sub topic due to permission issues. |  Grant the Pub/Sub service account the [necessary publish permissions](https://docs.cloud.google.com/pubsub/docs/access-control#pubsub.publisher). For more information, see [Add the Pub/Sub publisher role to the Pub/Sub service account.](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic#add-publisher-role)  
`CLUSTER_NOT_FOUND` | The provided cluster wasn't found. | Verify the cluster ARN for accuracy. Ensure that the cluster exists and is accessible.  
`Cluster is not public` | The provided cluster can't be accessed  | Non-public clusters behind VPCs aren't supported. You must use a public cluster.  
`TOPIC_NOT_FOUND` | The provided Kafka topic wasn't found. | Verify the topic name for accuracy. Ensure that the topic exists within the specified cluster.  



If there are no errors until this point, check the best practices in [Maintain a healthy publisher](https://docs.cloud.google.com/pubsub/docs/monitoring#keeping_publishers_healthy).

You can also enable [platform logs](https://docs.cloud.google.com/pubsub/docs/platform-logs-pubsub) for an import topic. These logs help you troubleshoot issues when you have issues ingesting objects into Pub/Sub import topics.

_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
