---
url: https://docs.cloud.google.com/oracle/database/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:57.946622+00:00
---

# Quotas and limits  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Resources ](https://docs.cloud.google.com/oracle/database/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about the Oracle Database@Google Cloud quotas and limits. Quotas are applied at a project level, and limits are applied to the instance or to the project, depending on the limit.

**Note:** For quotas and limits enforced by Oracle Cloud Infrastructure (OCI), see [OCI quotas and service limits](https://docs.oracle.com/en-us/iaas/Content/database-at-gcp/service-limits.htm).

## Required IAM roles

To check and edit your quotas, make sure that you've the following Identity and Access Management (IAM) roles and permissions:

  * [`serviceusage.quotas.get`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.get): to view your quotas.

  * [`serviceusage.quotas.update`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.update): to change your quotas.




Both these permissions are included by default in the [basic IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) Owner and Editor, and in the predefined [Quota Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement).

## Check your quotas

You can check the current quotas for resources in your project using the Google Cloud console. To check your quotas, do the following:

  1. [Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the filter section, in the **Enter property name or value** field, enter the product name: _Oracle AI Database_ , then press enter to filter.

The quotas are shown in the **Results** pane. These quotas only apply to API calls.




## Increase your quotas

As your use of Oracle Database@Google Cloud resources expands over time, your quotas can increase accordingly. If you expect a notable upcoming increase in usage, then make your request a few days in advance to ensure that your quotas are adequately sized.

There's no charge for requesting a quota increase. Your costs increase only if you use more resources.

To increase your quotas, follow these steps:

  1. Go to the **Quotas** page.

[Go to the Quotas page](https://console.cloud.google.com/iam-admin/quotas)

  2. Select the checkboxes next to the quotas that you want to change, and then click **Edit quotas**.

  3. In the **Quota changes** window, for each quota that you selected, in the **New limit** field, enter the value for the new limit.

  4. Click **Done** , then **Submit Request**.




## Rate quotas

Rate quotas define the number of requests that you can make to the [Oracle Database@Google Cloud API](https://docs.cloud.google.com/oracle/database/docs/reference/rest).

When you use the Google Cloud CLI or the Google Cloud console, you're making requests to the API and these requests count toward your rate limits. If you use service accounts to access the API, those requests also count toward your rate limit.

The rate quotas are enforced and automatically refilled over 60-second (1-minute) intervals. That means that if your project reaches a rate quota's maximum any time within 60 seconds, you must wait for that quota to refill before making more requests in that group. If your project exceeds a rate limit, you receive an HTTP `429` status code with the reason `rateLimitExceeded`.

The default quota range for each group is as follows:

Quota  
Quota description | Metric name | Default quota range in queries per minute  
---|---|---  
Read requests per minute (`ReadRequestsPerMinutePerProjectPerRegion`)  
Quota for `get` and `list` methods.  | `oracledatabase.googleapis.com/read_requests` | 300  
Mutation requests (`MutateRequestsPerMinutePerProjectPerRegion`)  
Quota for mutation methods.  | `oracledatabase.googleapis.com/mutate_requests` | 120  
  
## Resource quotas

Oracle Database@Google Cloud supports resource quotas, also known as allocation quotas. Resource quotas are the maximum amount of resources that you can create for a resource type if those resources are available.

Resource quotas don't reset over time. Instead, you must take action to release the unused resources, such as deleting an unneeded cluster.

Oracle Database@Google Cloud has the following resource quotas:

### ODB Subnet

The following table shows the minimum requirements for an ODB Subnet:

Value | Minimum requirement  
---|---  
Internal CIDR range | 1 per ODB Subnet per region  
  
### Exadata Database Service

The following table shows the minimum requirements for an Exadata VM Cluster:

Value | Minimum requirement  
---|---  
Interconnect attachments | 4 per ODB Network per region  
Cloud Router | 1 per ODB Network per region  
  
### Autonomous AI Database Service

The following table shows the minimum requirements for an Autonomous AI Database:

Value | Minimum requirement  
---|---  
Interconnect attachments | 4 per ODB Network per region  
Cloud Router | 1 per ODB Network per region  
DNS zone | 2 per Autonomous AI Database  
  
### Exadata Database Service on Exascale Infrastructure

The following table shows the minimum requirements for an Exascale VM Cluster:

Value | Minimum requirement  
---|---  
Interconnect attachments | 4 per ODB Network per region  
Cloud Router | 1 per ODB Network per region  
  
### Base Database Service

The following table shows the minimum requirements for a DB system:

Value | Minimum requirement  
---|---  
Interconnect attachments | 4 per ODB Network per region  
Cloud Router | 1 per ODB Network per region  
  
### Goldengate

The following table shows the minimum requirements for a Goldengate deployment:

Value | Minimum requirement  
---|---  
Interconnect attachments | 4 per ODB Network per region  
Cloud Router | 1 per ODB Network per region  
  
### Default quotas for provisioning resources

The following table shows the default resource quotas required for provisioning resources in Oracle Database@Google Cloud:

Value | Default limit  
---|---  
`interconnect_attachments_per_region`   
  
The number of Interconnect attachments required per project, per VPC, per region. | 16   
`routers-per-project`   
  
The number of Cloud Routers required per project, per VPC, per region. | 10   
`PerProjectInternalRanges`   
  
The internal CIDR range required per project, per VPC, per region. | 1500   
`managed-zones-per-project`   
  
The number of DNS zones required per project. | 10000   
`managed-zones-per-network`   
  
The number of DNS zones required per VPC. | 10000   
`target-nameservers-per-managed-zones`   
  
The number of servers required per project, per VPC, per region. | 50   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
