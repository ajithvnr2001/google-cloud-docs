---
url: https://docs.cloud.google.com/alloydb/docs/enforce-connectors/
title: Control connector enforcement \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:06.901024+00:00
---

# Control connector enforcement  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/enforce-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Control connector enforcement Stay organized with collections  Save and categorize content based on your preferences. 

To ensure that all database connections to an existing AlloyDB for PostgreSQL instance use mutual TLS (mTLS) encryption and Identity and Access Management (IAM) authorization, you can enforce connections through the AlloyDB Auth Proxy or AlloyDB Language Connectors. You can also disable connector enforcement on an instance at any time. For information about how to require connectors when you create an instance, see [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create).

**Note:** For the primary instance in a Private Service Connect cluster, connector enforcement is only supported when there are no secondary instances.

AlloyDB instances accept connections on two TCP ports:

  * Port `5432`, the default PostgreSQL port that applications use to connect to the instance. If you're using [managed connection pooling](https://docs.cloud.google.com/alloydb/docs/configure-managed-connection-pooling), the instance also listens on port `6432` for connections to the connection pool.

  * Port `5433`, which connectors, including the AlloyDB Auth Proxy and AlloyDB Language Connectors, use to connect to the instance.




Applications connect to a chosen connector on the local host and port that the connector listens on, and that connector communicates with your AlloyDB instance on port `5433`.

## Enforce connectors on an instance

### Console

  1. Go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource name** column.
  3. In the **Overview** page, go to the **Instances in your cluster** section, and click **Edit primary**.
  4. In the **Edit primary instance** pane, expand **Advanced configuration options**.
  5. Select **Enforce mTLS via AlloyDB connectors**.
  6. Click **Update instance**.



### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command with the `--require-connectors` flag to enforce connector connections on an AlloyDB instance:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --require-connectors

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you are updating.
  * `REGION_ID`: the region where the instance is placed.
  * `CLUSTER_ID`: the ID of the cluster where the instance is placed.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.



If the command returns an error message that includes the phrase `invalid cluster state MAINTENANCE`, then the cluster is undergoing routine maintenance. This state temporarily disallows instance reconfiguration. Run the command again after the cluster returns to a `READY` state. To check the cluster's status, see [View cluster details](https://docs.cloud.google.com/alloydb/docs/cluster-view).

## Disable connector enforcement on an instance

### Console

  1. Go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource name** column.
  3. In the **Overview** page, go to the **Instances in your cluster** section, and click **Edit primary**.
  4. In the **Edit primary instance** pane, expand **Advanced configuration options**.
  5. Clear **Enforce mTLS via AlloyDB connectors**.
  6. Click **Update instance**.



### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command with the `--no-require-connectors` flag to disable connector enforcement on an AlloyDB instance:
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --no-require-connectors

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you are updating.
  * `REGION_ID`: the region where the instance is placed.
  * `CLUSTER_ID`: the ID of the cluster where the instance is placed.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.



## What's next

  * [AlloyDB Auth Proxy overview](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview)
  * [AlloyDB Language Connectors overview](https://docs.cloud.google.com/alloydb/docs/language-connectors-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
