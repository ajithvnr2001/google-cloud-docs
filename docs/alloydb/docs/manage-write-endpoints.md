---
url: https://docs.cloud.google.com/alloydb/docs/manage-write-endpoints/
title: Manage database connections with write endpoints \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:07.473446+00:00
---

# Manage database connections with write endpoints  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/manage-write-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Manage database connections with write endpoints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To decouple your applications from the specific IP address or Uniform Resource Identifier (URI) of your AlloyDB for PostgreSQL primary instance during switchovers, cross-region failovers, backup restores, or migrations, you can configure a _write endpoint_.

An _endpoint_ is an AlloyDB resource that provides a stable Domain Name System (DNS) name that your applications can use to connect to an AlloyDB instance. This abstraction simplifies connection management during operational events—for example, disaster recovery, backup restores, or migrations—because you can redirect the endpoint's DNS name to a different instance without changing your application's configuration.

AlloyDB endpoints support the `WRITE_ENDPOINT` type. A write endpoint directs traffic to a single AlloyDB primary instance and serves both read and write traffic.

While the DNS name functions as a global resource, the endpoint resource itself is regional. Even so, each endpoint can link to instances globally, and its DNS name resolves from any location.

## Benefits of using endpoints

Using a write endpoint provides the following benefits:

  * **Simplified disaster recovery:** If you perform a [switchover](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#switchover-secondary) or a [cross-region failover](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#promote-secondary-cluster) to a secondary cluster, AlloyDB automatically updates the endpoint to point to the new primary instance. Your applications can then reconnect using the same endpoint DNS name, reducing your recovery time objective (RTO).
  * **Streamlined backup recovery:** When you restore an instance from a backup, AlloyDB creates a new instance with a new IP address. You can update your endpoint to point to the newly restored instance. This capability lets applications resume operation without configuration changes.
  * **Easier migrations:** During migrations, you can switch an endpoint from a source database to an AlloyDB instance with minimal application disruption.



## Limitations

  * Endpoints only support instances that are configured to use [private services access (PSA)](https://docs.cloud.google.com/alloydb/docs/about-private-services-access). Endpoints don't support instances configured to use [Private Service Connect (PSC)](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect).
  * Support for AlloyDB Language Connectors and the AlloyDB Auth Proxy is unavailable for write endpoints.
  * Concurrent modification operations (such as simultaneous updates, or an update and a delete operation) on endpoints pointing to the same target instance aren't supported and might result in failure.



## Before you begin

  1. Install and initialize the Google Cloud CLI.
  2. Enable the Cloud DNS API.
  3. Make sure that you have an existing AlloyDB instance to serve as a target for the endpoint.
  4. To get the permissions that you need to manage endpoints, ask your administrator to grant you the [AlloyDB Admin (`roles/alloydb.admin`)](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles) Identity and Access Management (IAM) role on your project. This predefined role contains the permissions required to manage endpoints.

You might also be able to get these permissions with custom roles or other predefined roles. The specific permissions required are:

     * `alloydb.endpoints.create`
     * `alloydb.endpoints.update`
     * `alloydb.endpoints.get`
     * `alloydb.endpoints.list`
     * `alloydb.endpoints.delete`



For more information, see [AlloyDB IAM roles and permissions](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions).

You can create and manage write endpoints using the Google Cloud CLI.

### Create an endpoint

To create a write endpoint, use the Google Cloud CLI. The endpoint type must be `WRITE_ENDPOINT`, and it must target a single primary instance.

###  Console 

  1. In the Google Cloud console, go to the **Endpoints** page.

[Go to Endpoints](https://console.cloud.google.com/alloydb/endpoints)

  2. Click **Create endpoint**.

  3. In the **Endpoint name** field, enter an ID for your endpoint. Must consist of lowercase letters (a-z), numbers, and hyphens, start with a lowercase letter, and end with a lowercase letter or number.

  4. Select a **Region**.

  5. For **Endpoint type** , select **Write**.

  6. In the **Target instance** field, select the primary instance that this endpoint should point to.

  7. Click **Create**.




###  gcloud 
    
    
    gcloud beta alloydb endpoints create ENDPOINT_ID \
        --project=PROJECT_ID \
        --region=REGION_ID \
        --endpoint-type=ENDPOINT_TYPE \
        --target-instances=TARGET_INSTANCE_NAME
    

Replace the following:

  * `ENDPOINT_ID`: a unique identifier for the endpoint. This ID must be unique within the specified project and location.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION_ID`: the ID of the region where you want to create the endpoint—for example, `us-central1`.
  * `ENDPOINT_TYPE`: the type of the endpoint resource. Only `WRITE_ENDPOINT` is supported.
  * `TARGET_INSTANCE_NAME`: the full resource name of the AlloyDB for PostgreSQL instance that the endpoint points to. The full resource path for an instance has the following format: `projects/$PROJECT/locations/$LOCATION/clusters/$CLUSTER/instances/$INSTANCE`.

**Note:** `WRITE_ENDPOINT` can have only 1 target instance, which must be of type `PRIMARY`.



### Connect to an instance using an endpoint

To connect to your AlloyDB instance using an endpoint, you must first get the automatically generated DNS name associated with the endpoint.

#### Get the DNS name

You can view the DNS name of an endpoint using the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Endpoints** page.

[Go to Endpoints](https://console.cloud.google.com/alloydb/endpoints)

  2. Find the endpoint you want to connect to and copy the value in the **DNS name** column.




###  gcloud 

  1. Use the [`gcloud beta alloydb endpoints describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/endpoints/describe) command:
         
         gcloud beta alloydb endpoints describe ENDPOINT_ID \
             --project=PROJECT_ID \
             --region=REGION_ID
         

Replace the following:

     * `ENDPOINT_ID`: the ID of the endpoint
     * `PROJECT_ID`: your Google Cloud project ID
     * `REGION_ID`: the ID of the region where the endpoint resides
  2. In the command output, find the `dnsName` field and copy its value.




#### Connect using psql

After you have the DNS name, you can use it as the host in your connection string or client tool. For example, to connect using the `psql` client, run the following command:
    
    
    psql -h DNS_NAME -U USERNAME -d DATABASE_NAME
    

Replace the following:

  * `DNS_NAME`: the DNS name of the endpoint
  * `USERNAME`: the database user to connect as
  * `DATABASE_NAME`: the name of the database to connect to



For more information about using `psql`, see [Connect using the psql client](https://docs.cloud.google.com/alloydb/docs/connect-psql).

### Update an endpoint

To change the instance an endpoint points to, such as after a restore operation, use the following commands:

###  Console 

  1. In the Google Cloud console, go to the **Endpoints** page.

[Go to Endpoints](https://console.cloud.google.com/alloydb/endpoints)

  2. In the row of the endpoint you want to update, click more_vert **Actions** , and then select **Edit**.

  3. In the **Target instance** field, select the new primary instance that this endpoint should point to.

  4. Click **Update**.




###  gcloud 
    
    
    gcloud beta alloydb endpoints update ENDPOINT_ID \
        --project=PROJECT_ID \
        --region=REGION_ID \
        --target-instances=NEW_TARGET_INSTANCE_NAME
    

Replace the following:

  * `ENDPOINT_ID`: the ID of the endpoint to update
  * `PROJECT_ID`: your Google Cloud project ID
  * `REGION_ID`: the ID of the region where the endpoint resides
  * `NEW_TARGET_INSTANCE_NAME`: the full resource name of the new target instances



**Note:** When you update an endpoint to point to a new instance, there might be a brief DNS propagation delay before traffic is routed to the new target.

### List endpoints

To list all endpoints in a given project and region, use the following command:

###  Console 

  1. In the Google Cloud console, go to the **Endpoints** page.

[Go to Endpoints](https://console.cloud.google.com/alloydb/endpoints)

The page lists all endpoints in the current project.




###  gcloud 
    
    
    gcloud beta alloydb endpoints list --project=PROJECT_ID \
        --region=REGION_ID
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID
  * `REGION_ID`: the ID of the region where the endpoint resides



### View endpoint details

To view the details of a specific endpoint, use the following Google Cloud CLI command:

###  gcloud 
    
    
    gcloud beta alloydb endpoints describe ENDPOINT_ID \
        --project=PROJECT_ID \
        --region=REGION_ID
    

Replace the following:

  * `ENDPOINT_ID`: the ID of the endpoint to describe
  * `PROJECT_ID`: your Google Cloud project ID
  * `REGION_ID`: the ID of the region where the endpoint resides



In the Google Cloud console, you can view the endpoint details on the **Endpoints** page.

### Delete an endpoint

To delete an endpoint, use the following commands:

###  Console 

  1. In the Google Cloud console, go to the **Endpoints** page.

[Go to Endpoints](https://console.cloud.google.com/alloydb/endpoints)

  2. In the row of the endpoint you want to delete, click more_vert **Actions** , and then select **Delete**.

  3. To confirm, type the endpoint ID, and then click **Delete**.




###  gcloud 
    
    
    gcloud beta alloydb endpoints delete ENDPOINT_ID \
        --project=PROJECT_ID \
        --region=REGION_ID
    

Replace the following:

  * `ENDPOINT_ID`: the ID of the endpoint to delete
  * `PROJECT_ID`: your Google Cloud project ID
  * `REGION_ID`: the ID of the region where the endpoint resides



## Write endpoint behavior during switchover or cross-region failover

While an endpoint's DNS name resolves to the IP of a specific instance at creation, these endpoints are dynamic. In the event of [cross-region replication](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication) activities, such as a [switchover](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#switchover-secondary) or a [cross-region failover](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#promote-secondary-cluster) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)), AlloyDB write endpoints maintain continuous connectivity without manual intervention. When a secondary cluster is promoted to become the new primary cluster, the endpoint automatically updates its DNS record to point to the new primary instance. This behavior eliminates manual reconfiguration of application connection strings, significantly reducing operational complexity and minimizing downtime to meet a recovery time objective (RTO).

After the operation and DNS propagation complete, your application can reconnect to the new primary instance using the same endpoint DNS name.

### Prevent conflicting writes during failover

Using a write endpoint during a cross-region failover helps prevent conflicting writes by automatically directing new write traffic away from the original primary cluster and toward the new one. For more information about write endpoint behavior during failover, see [Use write endpoints to avoid split-brain](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#split-brain-prevention).

**Note:** During a cross-region failover, AlloyDB updates the endpoint's DNS record to point to the new primary instance. However, if the region of the original primary is unavailable, there might be a delay in updating the endpoint metadata. As a result, fields like `effective_target_instances` might temporarily show the old primary instance even though the DNS record has already been updated.

## What's next

  * Learn more about [connecting to an AlloyDB instance](https://docs.cloud.google.com/alloydb/docs/connection-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
