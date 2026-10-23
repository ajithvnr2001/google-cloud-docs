---
url: https://docs.cloud.google.com/alloydb/quotas/
title: Quotas and limits \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:45.957250+00:00
---

# Quotas and limits  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Resources ](https://docs.cloud.google.com/alloydb/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to AlloyDB for PostgreSQL.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



## Quotas

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

Google Cloud also offers free trial quotas that provide limited access for projects to help you explore Google Cloud at no charge.

Not all projects have the same quotas. If your Google Cloud usage increases, your quotas might increase. **Important** : 

  * If you're using the [Google Cloud free trial](https://docs.cloud.google.com/free/docs/gcp-free-tier#free-trial), you cannot request a change to your quota.
  * If your project's billing service is disrupted or if you change your project's billing account, your quotas reset to their default values.



For more information about quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

For information specific to quotas imposed by AlloyDB, see Rate quotas and Resource quotas.

There are also _limits_ on AlloyDB resources. Unlike quotas, system limits can't be changed.

### Permissions for checking and editing quotas

To view your quotas, you must have the [`serviceusage.quotas.get`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.get) permission.

To change your quotas, you must have the [`serviceusage.quotas.update`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.update) permission.

These permissions are included by default in the [basic IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) of Owner and Editor and in the predefined [Quota Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement).

### Check your quotas

By default, the quotas table in the Google Cloud console lists quotas for all services. You can check the current quotas for AlloyDB resources in your project by using the **Filter** list in the table.

To check the current quotas for AlloyDB resources in your project, complete the following steps:

  1. In the Google Cloud console, go to the **Quotas** page.

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the quotas table, click **Filter**.

  3. Select **Service** from the **Properties** list, and then select **AlloyDB API** from the **Values** list.




### Increase your quotas

As your use of Google Cloud expands over time, your quotas can increase accordingly. If you expect a notable upcoming increase in usage, make your request a few days in advance to ensure your quotas are adequately sized.

**Note:** To request additional quotas, your user account must have the `serviceusage.quotas.update` permission. This permission is included by default for the following [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles): Owner, Editor, and Quota Administrator.

  1. In the [Quotas](https://console.cloud.google.com/iam-admin/quotas) page, click **Filter**.
  2. Select **Service** from the **Properties** list, and then select **AlloyDB API** from the **Values** list.

If you do not see **AlloyDB API** , it means that the AlloyDB Admin API is not enabled.

  3. Select the quotas you want to change.

  4. Click **Edit quotas**.

  5. Enter your name, email, phone number, and click **Next**.

  6. Enter your quota request and click **Submit request**.




### Rate quotas

AlloyDB supports _rate quotas_ , also known as rate limits or API quotas. Rate quotas define the number of requests that you can make to the [AlloyDB API](https://docs.cloud.google.com/alloydb/docs/reference/rest).

Each rate quota corresponds to all the requests for a group of one or more AlloyDB API methods. Rate quotas reset after a time interval that's specific to the service—for example, the number of API requests per day.

When you use the Google Cloud CLI or the Google Cloud console, you're making requests to the API and these requests count toward your rate limits. If you use service accounts to access the API, those requests also count toward your rate limit.

The rate quotas are enforced and automatically refilled over 60-second (1-minute) intervals. That means that if your project reaches a rate quota's maximum any time within 60 seconds, you must wait for that quota to refill before making more requests in that group. If your project exceeds a rate limit, you receive an HTTP `429` status code with the reason `rateLimitExceeded`.

The AlloyDB APIs are divided into six groups based on the operation type. The rate quotas are imposed per minute, per API group, per project, per region, and per user. For each unique combination of these attributes, AlloyDB imposes a separate quota. For example, if 100 users are accessing the Mutate APIs in a single minute for a given project and region, each user is given a default quota in the range of 180—250 requests per minute for each project and region combination.

The default quota range for each group is as follows:

Group name | Description | Default quota range in queries per minute | API methods  
---|---|---|---  
Connect APIs | Establish new connections. | 180-2000 | 

  * `projects.locations.clusters.generateClientCertificate`
  * `projects.locations.clusters.instances.getConnectionInfo`

  
Get APIs | Read a single resource. | 180-1000 | 

  * `projects.locations.clusters.get`
  * `projects.locations.clusters.instances.get`
  * `projects.locations.backups.get`
  * `projects.locations.get`

  
Get operation API | Get the latest state of a long-running operation. | 950-2000 | 

  * `projects.locations.operations.get`

  
List APIs | Read a group of resources of the same type. | 180-1000 | 

  * `projects.locations.clusters.list`
  * `projects.locations.clusters.instances.list`
  * `projects.locations.backups.list`
  * `projects.locations.supportedDatabaseFlags.list`
  * `projects.locations.list`

  
List operations API | List operations that match a specific filter in the request. | 2200-3000 | 

  * `projects.locations.operations.list`

  
Mutate APIs | Modify resource state. | 180-250 | 

  * `projects.locations.clusters.create`
  * `projects.locations.clusters.patch`
  * `projects.locations.clusters.delete`
  * `projects.locations.clusters.restore`
  * `projects.locations.clusters.instances.create`
  * `projects.locations.clusters.instances.patch`
  * `projects.locations.clusters.instances.delete`
  * `projects.locations.clusters.instances.failover`
  * `projects.locations.clusters.instances.restart`
  * `projects.locations.backups.create`
  * `projects.locations.backups.patch`
  * `projects.locations.backups.delete`
  * `projects.locations.operations.delete`
  * `projects.locations.operations.cancel`

  
  
### Resource quotas

AlloyDB supports _resource quotas_ , also known as allocation quotas. Resource quotas are the maximum amount of resources that you can create for a resource type if those resources are available. Resource quotas restrict the use of resources that don't have a rate of usage, such as the number of virtual machine (VM) instances used by your project at a given time.

Resource quotas don't reset over time. Instead, you must take action to release the unused resources, such as deleting an unneeded cluster.

Resource quotas are imposed on the number of clusters and vCPUs used, as detailed in the following sections.

#### Resource quotas on clusters

This quota applies to the number of clusters per project per region. The default value for this quota ranges from 3 to 10 clusters per project per region depending upon the project's usage history. The maximum supported value for this quota is 20 clusters per project per region.

If you make a create or restore cluster request using the Google Cloud console, gcloud CLI, or AlloyDB API, and if that results in quota violation, then the request fails with an error message similar to the following:
    
    
    Quota limit 'ClustersUsedPerProjectPerRegion' has been exceeded. Limit: 5 in region us-central1.
    

#### Resource quotas on vCPUs

This quota applies to the number of vCPUs per project per region. Each instance consumes some amount of this quota depending on how many VMs it uses. Each primary instance uses two VMs. Each read pool instance uses one VM for every node it contains. The number of vCPUs used by each VM is provided by you while creating or updating the instance.

The default value of the quota for all customer projects is 10,000 vCPUs.

If you make a create or update instance request using the Google Cloud console, gcloud CLI, or AlloyDB API, and if that results in quota violation, then the request fails with an error message similar to the following:
    
    
    Quota limit 'VCPUsUsedPerProjectPerRegion' has been exceeded. Limit: 128 in region us-central1.
    

#### Resource quotas on storage

This quota applies to the amount of data that can be stored in each cluster. The default value for this quota is 16 TiB per cluster. The maximum supported value is 128 TiB per cluster.

If you make a database write request, such as an `INSERT` statement that results in quota violation, then the request fails with the following error message:
    
    
    AlloyDB instance exceeds available storage quota.
    

#### Resource availability

Resource quotas do not guarantee that resources are available at all times. If a resource is not physically available for your region, you cannot create new resources of that type, even if you have remaining quota in your project.

## Limits

To request a limit increase, [file a support case](https://support.google.com/googlecloud/answer/1041916).

Item | Limit  
---|---  
Read pool nodes per cluster (across all read pool instances) | 20  
Maximum concurrent connections per instance | Default limit varies by instance size; adjustable up to the maximum limit supported by that size  
  
### Maximum concurrent connections

By default, AlloyDB sets the maximum number of concurrent connections for an instance based on its size. To change this limit, set the `max_connections` flag.

Use the following table to choose the `max_connections` value based on your instance size:

VCPU | Memory (GB) | Default `max_connections` value | Maximum recommended `max_connections` value  
---|---|---|---  
1 | 8 | `100` | `200`  
2 | 16 | `100` | `570`  
4 | 32 | `200` | `980`  
8 | 64 | `400` | `2300`  
14 | 112 | `700` | `4000`  
16 | 128 | `800` | `4600`  
22 | 176 | `1000` | `6300`  
32 | 256 | `1000` | `9175`  
44 | 352 | `1000` | `12600`  
48 | 384 | `1000` | `13760`  
64 | 512 | `1000` | `18350`  
72 | 576 | `1000` | `20640`  
88 | 704 | `1000` | `25230`  
96 | 768 | `1000` | `27525`  
128 | 864 | `1000` | `30960`  
144 | 1152 | `1000` | `41290`  
  
Note the following considerations before setting the value:

  * When you set the `max_connections` flag on a read pool instance, the new value must match or exceed the `max_connections` value of its cluster's primary instance.
  * Before you downsize an existing instance, update the `max_connections` flag value accordingly. Otherwise, you might encounter issues.
  * We recommend that you run a maximum of four concurrent queries per instance vCPU.
  * For workloads that involve short-term connections, consider using a connection pooler such as [pgbouncer](https://www.pgbouncer.org/) or [pgpool-II](https://www.pgpool.net/mediawiki/index.php/Main_Page).
  * We recommend adding an application-side connection pooler such as [HikariCP](https://github.com/brettwooldridge/HikariCP) or [c3p0](https://www.mchange.com/projects/c3p0/).
  * If you decide to set the value to a value higher than the recommendations (up to 240,000), then consider the additional memory consumption for each active connection that would reduce the memory for the shared buffer.

This memory consumption can be calculated by multiplying the number of concurrent queries with the value set for the `work_mem` flag. The default value for this flag is `4MB` or the number of vCPUs in the instance, whichever is higher.




### Saved queries limits

**Preview —[Saved queries](https://docs.cloud.google.com/alloydb/docs/saved-queries) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Value | Limit  
---|---  
Maximum number of saved queries per project (including saved queries for other Google Cloud products) | 10,000  
Maximum size for each query | 1 MiB  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
