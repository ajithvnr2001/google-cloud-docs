---
url: https://docs.cloud.google.com/sql/docs/mysql/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:06.165320+00:00
---

# Quotas and limits  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Resources ](https://docs.cloud.google.com/sql/docs/mysql/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/quotas "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/quotas "View this page for the SQL Server database engine")

This page provides information about the Cloud SQL quotas and limits. Quotas are applied per-project; limits are applied to the instance or to the project, depending on the limit.

**Note:** Creating or increasing storage capacity to 64 TB might increase latency of common operations, such as backups, dependent on your workload.

The Cloud SQL Admin API uses standard and custom HTTP headers such as `x-goog-user-project`. This request header specifies a user project to be used for quota accounting on the request. 

A valid value for this request is the [project ID](https://docs.cloud.google.com/docs/overview#projects) of an existing Google Cloud project (for example,  
`x-goog-user-project: my-project`). The user making the request must have the `**[serviceusage.services.use](https://docs.cloud.google.com/iam/docs/roles-permissions)**` permission for this project ID.

## Quotas

A _quota_ restricts how much of a Google Cloud resource your Google Cloud project can use. Cloud SQL is an example of this type of resource.

For Cloud SQL, quotas are part of a system that do the following:

  * Monitor your use or consumption of Cloud SQL instances
  * Restrict your consumption of these instances for reasons including ensuring fairness and reducing spikes in usage
  * Maintain configurations that enforce prescribed restrictions automatically
  * Provide a means to make or request changes to the quota



When a quota is exceeded, in most cases, the system blocks access to the relevant instance immediately, and the task that you're trying to perform fails. Quotas apply to each Google Cloud project and are shared across all instances that use that project.

### Permissions to check and increase your quotas

To check and increase your quotas, you need the following permissions:

  * `[serviceusage.quotas.get](https://docs.cloud.google.com/iam/docs/roles-permissions):` check your quotas
  * `[serviceusage.quotas.update](https://docs.cloud.google.com/iam/docs/roles-permissions):` increase your quotas



By default, these permissions are included in the [basic IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) of Editor and Owner and in the predefined [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) role. If you need additional permissions, then contact your quota administrator.

### Check your quotas

To check the current quotas for resources in your project, go to the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console and filter for **Cloud SQL Admin API**. These quotas apply only to API calls; they don't include database queries.

### Increase your quotas

As your use of Google Cloud expands over time, your quotas can increase accordingly. If you expect a notable upcoming increase in usage, then make your request a few days in advance to ensure your quotas are adequately sized.

There's no charge for requesting a quota increase. Your costs increase only if you use more resources.

To increase your quotas, follow these steps:

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to the Quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. Filter for the **Cloud SQL Admin API** service.

If you don't see this service, then [enable the Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/mysql/admin-api#enable_the_api).

  3. Select the checkboxes next to the quotas that you want to change, and then click **Edit quotas**.

  4. For each quota that you selected, in the **New limit** field, enter the value for the desired limit.

  5. In the **Reason description** field, enter a reason for your request of a quota increase, and then click **Done**.

  6. Click **Next**.

  7. Fill out your name, email, and phone number, and then click **Submit request**.

If you have trouble increasing your quotas, then [file a support case](https://support.google.com/googlecloud/answer/1041916). 




### How resource quotas are replenished

Daily quotas are replenished daily at midnight Pacific Time.

### Quotas and resource availability

Resource quotas are the maximum amount of resources you can create for that resource type if those resources are available. Quotas do not guarantee that resources are available at all times. If a resource isn't physically available for your region, then you can't create new resources of that type, even if you still have remaining quota in your project.

### Rate quotas

Cloud SQL supports rate quotas, which are also known as rate limits or API quotas. Rate quotas define how many requests you can make to the [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs/mysql/apis).

Each rate quota corresponds to all requests for a category of one or more Cloud SQL Admin API methods. Rate quotas reset after a time interval that's specific to Cloud SQL (for example, the number of API requests per minute).

When you use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Google Cloud console, you're making requests to the Cloud SQL Admin API and these requests count toward your rate quotas. If you use service accounts to access the API, then these requests also count toward your rate quotas.

Cloud SQL enforces and refills rate quotas automatically over 60-second intervals. If your project reaches a rate quota's limit any time within 60 seconds, then you must wait for that quota to refill before making more requests in that category. If your project exceeds this limit, then you receive an HTTP `429` status code with the reason of `rateLimitExceeded`.

The Cloud SQL Admin API is divided into the following categories:

  * **Connect:** look up values that are required to connect to a Cloud SQL database.
  * **Get:** retrieve information about a resource (for example, an instance, an operation, or a backup).
  * **List:** list resources.
  * **Mutate:** create, modify, and delete resources.
  * **Default per region:** interact with a Cloud SQL instance without connecting to, retrieving, listing, or mutating it.
  * **Default:** list database flags and machine types (tiers) for Cloud SQL instances. The APIs in this category are global.



Cloud SQL imposes rate quotas for each category per minute, per user, and per region. For each unique combination of these attributes, Cloud SQL imposes a separate rate limit.

The Cloud SQL Admin API produces detailed metrics that can help you track your usage of the API, monitor performance of your Cloud SQL instance and the API, and discover problems between your instance and the API. For more information, see [Monitoring API usage](https://docs.cloud.google.com/apis/docs/monitoring).

The following table provides information about the metric, APIs, and default limit for each category:

Category | Metric | APIs | Default limit  
---|---|---|---  
Connect | `sqladmin.googleapis.com/connect` The number of requests that are made per minute per user per region to use the APIs in this category. | 

  * `[SqlConnectService.  
GetConnectSettings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/connect/get)`
  * `[SqlConnectService.  
GenerateEphermalCertificates](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/connect/generateEphemeralCert)`

| 1000  
Get | `sqladmin.googleapis.com/get` The number of requests that are made per minute per user per region to use the APIs in this category. | 

  * `[SqlBackupRunsService.Get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/get)`
  * `[SqlDatabasesService.Get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/get)`
  * `[SqlInstancesService.Get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get)`
  * `[SqlOperationsService.Get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/get)`
  * `[SqlSslCertsService.Get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/get)`
  * `[SqlUsersService.Get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/get)`

| 500  
List | `sqladmin.googleapis.com/list` The number of requests that are made per minute per user per region to use the APIs in this category. | 

  * `[SqlBackupRunsService.List](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/list)`
  * `[SqlDatabasesService.List](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/list)`
  * `[SqlInstancesService.List](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/list)`
  * `[SqlInstancesService.  
ListServerCas](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/listServerCas)`
  * `[SqlOperationsService.List](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/list)`
  * `[SqlSslCertsService.List](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/list)`
  * `[SqlUsersService.List](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/list)`

| 500  
Mutate | `sqladmin.googleapis.com/mutate` The number of requests that are made per minute per user per region to use the APIs in this category. | 

  * `[SqlBackupRunsService.Delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/delete)`
  * `[SqlBackupRunsService.Insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/insert)`
  * `[SqlDatabasesService.Delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/delete)`
  * `[SqlDatabasesService.Insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/insert)`
  * `[SqlDatabasesService.Patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/patch)`
  * `[SqlDatabasesService.Update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/update)`
  * `[SqlInstancesService.  
AddServerCa](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/addServerCa)`
  * `[SqlInstancesService.Clone](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/clone)`
  * `[SqlInstancesService.Delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/delete)`
  * `[SqlInstancesService.  
DemoteMaster](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/demoteMaster)`
  * `[SqlInstancesService.Import](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/import)`
  * `[SqlInstancesService.Insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert)`
  * `[SqlInstancesService.Patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch)`
  * `[SqlInstancesService.  
PromoteReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/promoteReplica)`
  * `[SqlInstancesService.  
ResetSslConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/resetSslConfig)`
  * `[SqlInstancesService.  
RestoreBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restoreBackup)`
  * `[SqlInstancesService.  
RotateServerCa](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/rotateServerCa)`
  * `[SqlInstancesService.  
TruncateLog](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/truncateLog)`
  * `[SqlInstancesService.Update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/update)`
  * `[SqlSslCertsService.  
CreateEphemeral](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/createEphemeral)`
  * `[SqlSslCertsService.Delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/delete)`
  * `[SqlSslCertsService.Insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/insert)`
  * `[SqlUsersService.Delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/delete)`
  * `[SqlUsersService.Insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/insert)`
  * `[SqlUsersService.Update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/update)`

| 180  
Default per region | `sqladmin.googleapis.com/  
default_per_region` The number of default regional requests that are made per minute per user per region to use the APIs in this category. | 

  * `[SqlInstancesService.Export](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/export)`
  * `[SqlInstancesService.Failover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/failover)`
  * `[SqlInstancesService.Restart](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restart)`
  * `[SqlInstancesService.  
StartReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/startReplica)`
  * `[SqlInstancesService.  
StopReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/stopReplica)`

| 180  
Default | `sqladmin.googleapis.com/default` The number of default requests that are made per minute per user to use the APIs in this category. | 

  * `[SqlFlagsService.List](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/flags/list)`
  * `[SqlTiersService.List](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/tiers/list)`

| 180  
  
### Troubleshoot rate limit errors

Because Cloud SQL enforces rate quotas per minute, per user, and per region, the Cloud Quotas page in the Google Cloud console doesn't display per-user quota usage. If a single user or service account exhausts its per-user rate quota, then the Cloud SQL Admin API returns an HTTP `429 Too Many Requests` status code with the reason `rateLimitExceeded`. In this scenario, the aggregate project-level quota metrics on the Cloud Quotas page might show that quota is still available.

To diagnose which user or service account is exhausting a per-user rate limit, complete the following steps:

  1. In the Google Cloud console, select the consumer project that initiates the Cloud SQL requests, and then go to the [**Metrics Explorer**](https://console.cloud.google.com/monitoring/metrics-explorer) page.
  2. Click **Select a metric** , and then enter `serviceruntime.googleapis.com/api/request_count` in the filter bar. In the submenus, select **Consumed API > Api > Request count**, and then click **Apply**.
  3. In the **Filter** element, add the following filters to isolate the throttled requests: 
     1. Click **Add filter** , and then select `response_code`. In the filter dialog, leave **Comparator** set to **= (equals)** , enter `429` in the **Value** field, and then click **Apply**.
     2. Click **Add filter** again, and then select `service`. Leave **Comparator** set to **= (equals)** , enter `sqladmin.googleapis.com` in the **Value** field, and then click **Apply**.
     3. Optional: To filter by a specific API method, click **Add filter** , and then select `method`. Leave **Comparator** set to **= (equals)** , enter the method name in the **Value** field (such as `google.cloud.sql.v1.SqlInstancesService.Get`), and then click **Apply**.
  4. In the **Aggregation** element, verify that the first menu is set to **Sum** , and then in the second menu (next to **by**), select `credential_id` to group request counts by individual credential.
  5. In the results, find the credential ID (`credential_id`) with the highest volume of `429` response codes. This value is the OAuth 2.0 client ID of the service account or user credential that is exhausting the per-user rate limit.
  6. To find which service account corresponds to that client ID, go to the [**Service accounts**](https://console.cloud.google.com/iam-admin/serviceaccounts) page in the Google Cloud console and enter the OAuth 2.0 client ID in the filter box. The matching entry is the service account that is exhausting the per-user rate limit.



To resolve the error after you identify the service account, apply one or more of the following mitigations:

  * Implement client-side caching: if your application frequently polls instance metadata—such as during container restarts or health checks—cache the instance metadata to avoid repeated calls to `SqlInstancesService.Get`.
  * Apply exponential backoff: ensure that client retry logic uses exponential backoff with jitter to avoid sending bursts of requests that exceed the rate limit.
  * Distribute workloads across service accounts: if multiple workloads share a single service account or consumer project, create dedicated service accounts for each workload to prevent one workload from consuming the shared quota.
  * Request a quota adjustment: if your application requires higher throughput, [request a quota increase](https://docs.cloud.google.com/docs/quotas/help/request_increase) for Cloud SQL Admin API rate quotas.



## Limits

There are restrictions on some Cloud SQL resources that are not replenished periodically and not shown on the Quotas page in the Google Cloud console. Some limits can be increased while others cannot.

### Configurable limits

#### Instances per project

The maximum number of instances you can have in a single project depends on the [network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture#overview) of those instances:

  * New SQL network architecture: You can have up to 1,000 instances per project.
  * Old SQL network architecture: You can have up to 100 instances per project.
  * Using both architectures: Your limit will be somewhere between 100 and 1,000, depending on the distribution of your instances across the two architectures.



[File a support case](https://support.google.com/googlecloud/answer/1041916) to request an increase. Read replicas are counted as instances.

We recommend that you distribute your instance count across multiple projects to reduce the reliance on quota increase requests. This helps you avoid any potential blockages.

#### Maximum concurrent connections

You can use the [ `max_connections`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-m) flag to configure a connections limit. When you create a Cloud SQL for MySQL instance, you choose a machine type, which determines the amount of memory. The amount of available memory determines the connection limits for the instance.

**Note:** To support a maximum number of connections, an instance requires sufficient resources, specifically memory. For stable operations and performance make sure that your instance is adequately sized.

You can find the connections limit for your instance by connecting to your database and running this command: `SHOW VARIABLES LIKE "max_connections";`

### Caveats

#### Quota usage for Cloud SQL Connectors

The Cloud SQL Auth Proxy and [other Cloud SQL Connectors](https://docs.cloud.google.com/sql/docs/mysql/connect-connectors) use Cloud SQL Admin API's quota. The Cloud SQL Connectors work by running a refresh operation approximately every hour. This refresh operation makes two API calls. One call retrieves the instance metadata and the other call retrieves an ephemeral certificate.

The quota usage is calculated as:

`Quota usage = connector processes running * instances * 2 API calls per hour`

For example, if you have three processes running a connector, the connector is configured to connect to two Cloud SQL instances, and two API calls are made for one hour, then your quota consumption is 12 (3 processes * 2 instances * 2 API calls).

If you're getting started with Cloud SQL, then keeping note of the above formula, you should be mindful of:

  * How quickly you scale up new DB clients

  * How quickly you add more instances

  * Using different service accounts for each application




#### Cloud SQL IAM database authentication

There's a per-minute login quota for each instance, which includes both successful and unsuccessful logins. When the quota is exceeded, logins are unavailable temporarily. We recommend that you avoid frequent logins and restrict logins using [authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks). The quota for authorization of logins is 12,000 per minute, per instance. 

#### Forwarding rule quota

Each Cloud SQL instance consists of a forwarding rule and a load balancer. There's quota limit on the forwarding rule, based on the kind of load balancer to which it's pointing. There are multiple quotas on each kind of forwarding rules, per project, [per network](https://cloud.google.com/vpc/docs/quota#per_network) and per [peering group](https://cloud.google.com/vpc/docs/quota#vpc-peering). There's also an override rule for per network quota and per peering group quotas, for Cloud SQL. This means when we bump up the [per network](https://cloud.google.com/vpc/docs/quota#per_network) quota for producer networks, the per [peering group](https://cloud.google.com/vpc/docs/quota#vpc-peering) quota gets bumped to the same value as well.

Cloud SQL producer VPC is peered with customer's VPC, so we often hit per network quota for Cloud SQL producer network, and per peering group quota for customer's VPC.

When we hit the quota, certain operations can fail, which include:

  * Create Operation: We need new forwarding rules when we create new instances.

  * Update Operation: We allow customers to switch the network of instances, so we need new forwarding rules in the new network.

  * Maintenance Operation: Forwarding rules get recreated.




To avoid any issues, consider limiting the total number of instances per network to below 500.

If you experience an issue, then [file a support case](https://support.google.com/googlecloud/answer/1041916), and we'll bump the relevant quota(s) for you.

### Fixed limits

#### IOPS

IOPS are the number of input/output operations (or read/write) operations that your disk can process per second.

Cloud SQL uses Compute Engine virtual machines (VMs) with persistent storage disks. For details on specific VM performance characteristics, see the **maximum sustained IOPS** table on the [persistent disk performance](https://docs.cloud.google.com/compute/docs/disks/performance) page.

#### Table limit

Cloud SQL for MySQL has a limit of 50,000 tables by default, or 500,000 tables for an instance if you meet the minimum hardware requirements of at least 32 cores and a minimum of 200G of memory. For optimal performance, we recommend that the number of tables in a single database not exceed 50,000.

Instances that exceed these limits are not covered by the SLA. If the `innodb_file_per_table` database flag is enabled, and a table size reaches 16 TB, the maximum size for Linux partitions, no additional data can be added.

The memory needed by your instance depends on various factors. To learn more about how Cloud SQL for MySQL uses memory, see [How MySQL uses memory](https://cloud.google.com/mysql/memory-usage).

If your active table count is larger than the Cloud SQL defaults, or if the overall cache size is significantly large, then you need to make adjustments to your instance. To maintain optimal performance, you can: 

  * Upgrade to the [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/mysql/editions-intro) for higher memory options.
  * Upgrade your Cloud SQL machine to add memory to your instance.
  * Reduce the value of the `innodb_buffer_pool_size` database flag.



The [`table_open_cache`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-t) and [`table_definition_cache`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-t) flags can be used to modify the Cloud SQL for MySQL table cache. You can use the [performance schema](https://docs.cloud.google.com/sql/docs/mysql/diagnose-issues#performance-schema) to get an estimate of the table cache size for your instance. See the [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/performance-schema.html) for more information.

If the number of active tables is significantly larger than both the Cloud SQL table defaults and the open tables recommendation by MySQL, then Cloud SQL recommends configuring the `table_open_cache` and `table_definition_cache` database flags with your instance's active table count. For more information, see [How MySQL Opens and Closes Tables](https://dev.mysql.com/doc/refman/8.4/en/table-cache.html).

#### Operations limit

Micro and small tier machine types limit the number of concurrent operations. Exceeding these limits causes a `Too many operations` error.

The db-custom-1-3840 (single CPU) machine type limit is 50 concurrent operations.

The f1-micro (shared-core CPU) machine type limit is 20 concurrent operations. 

#### Cloud SQL storage limits

  * **Dedicated core:** Up to 64 TB. 

See [CPU and memory pricing](https://docs.cloud.google.com/sql/pricing#cpu-mem-pricing) for more information. 

  * **Shared core:** Up to 3 TB. 

See [Instance pricing](https://docs.cloud.google.com/sql/pricing#instance-pricing) for more information. 




#### Cloud SQL storage options

To configure a storage option for best performance, it's important to understand your workload and choose [the appropriate disk type and size](https://docs.cloud.google.com/compute/docs/disks/performance). For more information on the available choices for Cloud SQL, see [instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-capacity-2ndgen). 

#### App Engine limits

Each App Engine instance running in a standard environment cannot have more than **100 concurrent connections** to an instance. For PHP 5.5 apps, the limit is **60 concurrent connections**. 

App Engine applications are subject to request time limits depending on usage and environment. For more information, see how instances are managed in App Engine standard environment [ standard](https://docs.cloud.google.com/appengine/docs/standard/python/how-instances-are-managed#timeout) and[ flexible](https://docs.cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed) environments. 

App Engine applications are also subject to additional App Engine quotas and limits as discussed on the [ App Engine Quotas](https://docs.cloud.google.com/appengine/docs/quotas) page. 

#### Cloud Run limits

If you use the built-in Cloud SQL connection on Cloud Run, then Cloud Run container instances are limited to 100 connections per Cloud SQL database.

Each instance of a Cloud Run service or job can have 100 connections to the database, and as this service or job scales, the total number of connections per deployment can grow.

This limit _doesn't_ apply when using other connection methods such as the Cloud SQL Auth Proxy in a sidecar, the Cloud SQL Language Connectors, or when connecting directly to the IP address of the Cloud SQL instance. 

#### Cloud Run functions limits

Cloud Run functions (1st gen) limits concurrent executions to one per instance. You never have a situation where a single 1st gen function instance is processing two requests at the same time. In most situations, only a single database connection is needed.

Cloud Run functions (2nd gen) is based on Cloud Run and has a limit of 100 database connections per instance. 

### Saved queries limits

**Preview —[Saved queries](https://docs.cloud.google.com/sql/docs/mysql/saved-queries) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Value | Limit  
---|---  
Maximum number of saved queries per project (including saved queries for other Google Cloud products) | 10,000  
Maximum size for each query | 1 MiB  
  
#### Cloud SQL storage limits

  * **Dedicated core:** Up to 64 TB. 

See [CPU and memory pricing](https://docs.cloud.google.com/sql/pricing#cpu-mem-pricing) for more information. 

  * **Shared core:** Up to 3 TB. 

See [Instance pricing](https://docs.cloud.google.com/sql/pricing#instance-pricing) for more information. 




#### Cloud SQL storage options

To configure a storage option for best performance, it's important to understand your workload and choose [the appropriate disk type and size](https://docs.cloud.google.com/compute/docs/disks/performance). For more information on the available choices for Cloud SQL, see [instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-capacity-2ndgen). 

#### App Engine limits

Each App Engine instance running in a standard environment cannot have more than **100 concurrent connections** to an instance. For PHP 5.5 apps, the limit is **60 concurrent connections**. 

App Engine applications are subject to request time limits depending on usage and environment. For more information, see how instances are managed in App Engine standard environment [ standard](https://docs.cloud.google.com/appengine/docs/standard/python/how-instances-are-managed#timeout) and[ flexible](https://docs.cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed) environments. 

App Engine applications are also subject to additional App Engine quotas and limits as discussed on the [ App Engine Quotas](https://docs.cloud.google.com/appengine/docs/quotas) page. 

#### Cloud Run limits

If you use the built-in Cloud SQL connection on Cloud Run, then Cloud Run container instances are limited to 100 connections per Cloud SQL database.

Each instance of a Cloud Run service or job can have 100 connections to the database, and as this service or job scales, the total number of connections per deployment can grow.

This limit _doesn't_ apply when using other connection methods such as the Cloud SQL Auth Proxy in a sidecar, the Cloud SQL Language Connectors, or when connecting directly to the IP address of the Cloud SQL instance. 

#### Cloud Run functions limits

Cloud Run functions (1st gen) limits concurrent executions to one per instance. You never have a situation where a single 1st gen function instance is processing two requests at the same time. In most situations, only a single database connection is needed.

Cloud Run functions (2nd gen) is based on Cloud Run and has a limit of 100 database connections per instance. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
