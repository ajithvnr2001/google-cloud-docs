---
url: https://docs.cloud.google.com/recommender/docs/unattended-project-recommender/
title: Unattended project recommender \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:11:15.085169+00:00
---

# Unattended project recommender  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/unattended-project-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Unattended project recommender

The unattended project recommender analyzes usage activity on projects in your organization and provides recommendations that help you discover, reclaim or remove unattended projects.

## Overview

In fast-moving organizations, it's not uncommon for cloud resources, including entire projects, to occasionally be forgotten about. Such unattended resources can be difficult to identify and tend to result in unnecessary waste and security risks.

Unattended project recommender analyzes usage activity across all projects in your organization and provides you with the following features to help you discover, reclaim, and shut down unattended projects:

  * Usage insights for every project (networking, API, project owner, service activity, and more).
  * Recommendations to turn down projects having low usage activity.
  * Recommendations to assign a new owner to projects that have high usage activity but no active owner.



Shutting down or reclaiming unattended projects can provide the following [impact and benefits](https://docs.cloud.google.com/recommender/docs/key-concepts#impact) to your organization:

  * Reduction in security risks (`SECURITY`)
  * Reduction in unnecessary spending (`COST`)
  * Reduction in carbon footprint associated with your workloads (`SUSTAINABILITY`)

**Note:** The unattended project recommender can be used only for projects assigned to Google Cloud organizations.

## How it works

The unattended project recommender analyzes project usage over the last 30 days. The following table lists the recommendations and insights that the unattended project recommender can generate based on whether the usage activity is low or high .

Project usage/type | Insight subtype | Recommendation | Recommendation subtype  
---|---|---|---  
Projects with: 

  * Low usage for the last 30 days

| `PROJECT_ACTIVITY` | Review or delete the project. | `CLEANUP_PROJECT`  
Projects with: 

  * High usage for the last 30 days
  * User owners assigned but none of whom are active on the project.

| `PROJECT_ACTIVITY` | Reclaim the project by assigning a new owner. | `RECLAIM_PROJECT`  
All other non-Apps Script projects.  | `PROJECT_ACTIVITY` | - | -  
**Note:** The unattended project recommender does not generate any insights or recommendations for [Apps Scripts](https://docs.cloud.google.com/apps-script/guides/cloud-platform-projects) projects since these projects are auto-deleted upon deletion of the associated scripts.

Recommendations and Insights are available at different levels of your Cloud Organization Hierarchy. Accessing those recommendations and insights requires an IAM role binding at the corresponding level:

  * At a Project level: Project Owners can discover and act on insights and recommendations for the projects they have access to.
  * At an Organizational level: Organization Administrators can discover and act on insights and recommendations for projects within a cloud organization.
  * At a Billing Account level: Billing Administrators can discover and act on insights and recommendations for projects associated with a particular billing account.

**Note:** The number of Insights and Recommendations per Organization or Billing Account is currently limited to 10,000. If your Organization or Billing Account includes more than 10,000 projects and you would like to review the full set of recommendations and insights, we recommend that you either rely on the Project-level insights and recommendations or [use BigQuery export of insights and recommendations](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

### Ranking the usage activity of a project

A project can be ranked to have a low or high usage activity, based on which recommendations are provided. The ranking of a project's usage activity is computed based on the content included in the project's utilization insight.

For projects that are identified to have low usage activity, the following conditions apply: 

Usage classification | Condition  
---|---  
Organizations that have more than 50 projects | 

  * A project is ranked based on the level of usage activity across all content included in the project's utilization insight.
  * A project is classified as unattended if it falls within 10% of usage activity in comparison to all other projects in that organization.

  
Organizations that have less than 50 projects | 

  * Daily average of API calls consumed by a project (`consumedApiDailyCount`) is less than 100.
  * [Cloud logging](https://docs.cloud.google.com/logging/docs) is the only service used by a project. 
  * All other project utilization insights have a value equal to zero.

  
**Note:** Recommendations are provided only for projects that are older than 30 days.

## Recommendation priority and impacts

Unattended project recommendations contain the following fields that help prioritize and estimate the benefits of applying them:

  * `priority` \- A priority value between P1-P4, with P1 being the highest priority.
  * `primaryImpact` \- `SECURITY`. The count of high-priority security recommendations in an unattended project.
  * `additionalImpact(s)` \- `COST` and `SUSTAINABILITY`. The cost ($) and sustainability emission (kgCO2e) reduction that would be realized if the project was removed.



### Recommendation priority

The priority of the unattended project recommendation ranges from P1 to P4, with P1 being the highest priority.

The recommender begins by reviewing security recommendations in each unattended project. From there, it sets the priority of the unattended project recommendation equal to that of the highest priority recommendation found within the project. For example, if an unattended project has 10 security recommendations, eight P2 recommendations and two P1 recommendations, the unattended project recommendation would be assigned a priority value of P1.

The most frequently occurring security recommendations found in unattended projects are from the [IAM Recommender](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview). An unattended project recommendation with a priority of P1 likely means there is a publicly accessible cloud storage bucket in the unattended project (learn more about [how IAM Recommender sets priorities](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#priority)).

### Security impact

The `primaryImpact` \- `SECURITY` field offers a `securityProjection` equal to the count of high-priority (P2 and higher) security recommendations in the unattended project. For example, when a project has a recommendation to replace the broad Editor role with a more granular role, that recommendation has a [priority of P2](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#priority) and gets counted in the `priorityRecommendationCount`.

### Cost Impact

The `additionalImpact` \- `COST` field offers a `costProjection` that is an estimate of the cost savings if the unattended project was removed. This is based on the costs incurred from resources running in the unattended project over the last 30 days.

**Note:** To view custom pricing in cost projections, the associated cloud billing account must not have changed in the last 30 days, and the user must have billing permissions.

### Sustainability impact

The `additionalImpact` \- `SUSTAINABILITY` field offers a `sustainabilityProjection` that is an estimate of [carbon emissions](https://docs.cloud.google.com/carbon-footprint/docs/methodology) contributed by the resources running in the unattended project over the last 30 days. The estimate is measured in kilograms of carbon dioxide equivalent (kgCO2e).

## Contents of a project utilization insight

The contents of a project's utilization insight are field values that are used to rank the usage activity of the project and generate `CLEANUP_PROJECT` and/or `RECLAIM_PROJECT` recommendations.

**Warning:** Project utilization insights are generated for all projects, regardless of whether the project is unattended or not. These insights are generated on a daily basis. A single insight is not a reliable indicator for a project to be considered as unattended. Please refrain from removing projects based on a single day's insight.

The following table lists the various fields that the recommender surfaces as part of the `PROJECT_ACTIVITY` insight:

Field | Description  
---|---  
**Level of usage**  
`usagePercentile` | Percentile of the usage level of this project compared with other projects within the same organization.  If the percentile is -1, this means that the value is not computed. The value is not computed when organizations have less than 50 projects.   
**API activity**  
`activeServiceAccountDailyCount` | Daily average of service accounts with [authentication activity](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-iam) under this project.   
`apiClientDailyCount` | Daily average of [distinct clients](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime) of API calls produced by this project.   
`consumedApiDailyCount` | Daily average of [API calls](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-serviceruntime) consumed by this project.  
`datastoreApiDailyCount` | Daily average of [Datastore API](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-datastore) calls consumed by this project  
**Networking activity**  
`vpcEgressDailyBytes` | Daily average of [ VPC egress bytes](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) out of this project.  
`vpcIngressDailyBytes` | Daily average of [ VPC ingress bytes](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) into this project  
**Billing usage**  
`hasBillingAccount` | Checks if the project has a billing account at the end of the observation  
`serviceWithBillableUsage` | Names of the billable services used in the trailing 30 days.  
**Cloud services usage**  
`activeAppengineInstanceDailyCount`: system/instance_count | Daily average of the number of active [App Engine instances](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-appengine) under this project  
`activeCloudsqlInstanceDailyCount` | Daily average of the number of active [Cloud SQL instances](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudsql) under this project.  
`activeGceInstanceDailyCount` | Daily average of the number of active [Compute Engine instances](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) under this project.  
`bigqueryInflightJobDailyCount` | Daily average of inflight [BigQuery jobs](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquery) under this project.  
`bigqueryInflightQueryDailyCount` | Daily average of inflight [BigQuery query count](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquery) under this project.  
`bigqueryStorageDailyBytes` | Daily average of inflight [BigQuery storage](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquery) under this project.  
`bigqueryTableDailyCount` | Daily average of [BigQuery table count](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender/) under this project.  
`gcsObjectDailyCount` | Daily average of [number of Cloud Storage objects](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage) under this project.  
`gcsRequestDailyCount` | Daily average of [number of Cloud Storage API](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage) under this project.  
`gcsStorageDailyBytes` | Daily average of [storage bytes used by Cloud Storage](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage) under this project.  
**User activity**  
`numActiveUserOwners` | The number of active user type project owners at the end of the observation period. Active means that the user account is not disabled and there was some activity identified under this project during the observation period.   
`owners` | List of project owners and their activities  
**Other fields**  
`hasActiveOauthTokens` | Checks if the project has any active OAuth tokens used in the last 180 days.  
`carbonFootprintDailyKgCO2` | Daily average of [carbon emissions](https://docs.cloud.google.com/carbon-footprint/docs/methodology) contributed by this project based on the last 30 days of data available.  
`costProjection` | Projected [cost](https://github.com/googleapis/googleapis/blob/master/google/type/money.proto) savings for the specified duration if the project was to be removed. A custom or list price is shown based on the billing account permissions. It is an estimate based on the last 30 days of available data and does not constitute a bill.  
`severity` | The `severity` is set to the corresponding value of the highest severity security insight found in the project. For example, based on how [IAM Recommender sets severities](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#severity) for their insights, a `CRITICAL` severity on the unattended project insight likely means there is a publicly accessible cloud storage bucket in the unattended project.   
  
### Recommendations to delete a project

A project is recommended for deletion when it has a low usage in the last 30 days **and** no OAuth tokens used in the last 180 days.

**Warning:** Carefully examine the utilization insights associated with a project. Deleting a project might lead to irreversible data loss. For more information, refer to [Shutting down (deleting) projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).**Caution:** Recommendations are provided for [tenant projects](https://docs.cloud.google.com/service-infrastructure/docs/manage-tenant-projects). Deleting this project might lead to data loss owing to additional project utilization fields that aren't captured for these projects.

### Recommendations to assign a new owner to a project

It is recommended to assign a new owner to a project when it meets all conditions as listed below:

  * All assigned owners are either inactive on the project for the last 90 days or no longer with the company.
  * The project has a high usage activity.

**Note:** If a project has no user owner assigned, it is considered as an intended behavior where the `RECLAIM_PROJECT` recommendation is not provided.

## Pricing

For more details on Active Assist pricing, refer to the recommender [pricing](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view the insights and recommendations, you must do the following:

  * You must [enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling). You only need to enable the API on a single billing project. You can then use this same billing project to examine recommendations and insights for other projects, the entire organization or the billing account, using the `--billing-project` functionality of gcloud/API.
  * Make sure that you have one of these required roles assigned:

Description | Roles  
---|---  
View recommendations |  `recommender.projectUtilViewer`  
  
View and update recommendations |  `recommender.projectUtilAdmin`  
  
Opting-out of insights and recommendations in Transparency and Control Center |  `dataprocessing.admin`  
  
  
These roles provide a set of [permissions](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender#required_iam_permissions) that enable you to access the insights and recommendations. For more information about roles, refer to [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Granting these roles at the Organization level lets you access the recommendations and insights for the projects in the organization individually, or collectively (all unattended projects in the organization) using the Organization level API.

Granting these roles at the Billing Account level lets you access the recommendations and insights for projects that use the specified billing account.

For more information about opting out, refer to [opting out of insights and recommendations](https://docs.cloud.google.com/recommender/docs/opting-out).

### Recommender ID

Here are the unattended project recommender ID and insight type:

  * `google.resourcemanager.projectUtilization.Recommender`
  * `google.resourcemanager.projectUtilization.Insight`



### Required IAM permissions

To access the list of recommendations and insights, the following permissions are required:

  * `recommender.resourcemanagerProjectUtilizationRecommendations.get`
  * `recommender.resourcemanagerProjectUtilizationRecommendations.list`
  * `recommender.resourcemanagerProjectUtilizationInsights.get`
  * `recommender.resourcemanagerProjectUtilizationInsights.list`



To update recommendations and insights (for example, to dismiss a recommendation), the following permissions are required:

  * `recommender.resourcemanagerProjectUtilizationRecommendations.update`
  * `recommender.resourcemanagerProjectUtilizationInsights.update`



### Viewing unattended project recommendations

This section describes how to check for unattended insights and recommendations using `gcloud`, and using `curl` to send requests to the recommender API.

###  gcloud 

To view recommendations and insights using `gcloud`, follow the steps below. For more information, see [Using the API - Insights](https://docs.cloud.google.com/recommender/docs/insights/using-api) and [Using the API - Recommendations](https://docs.cloud.google.com/recommender/docs/using-api).

#### Recommendations

  1. To list unattended project recommendations for the project where you've enabled the Recommender API, run the following command:
         
         gcloud recommender recommendations list \
           --project=PROJECT_ID \
           --location=global \
           --recommender=google.resourcemanager.projectUtilization.Recommender
         

Replace the following:

     * `PROJECT_ID`: The project ID.
  2. To list unattended project recommendations in a different project while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         gcloud recommender recommendations list \
           --billing-project=BILLING_PROJECT_ID \
           --project=PROJECT_ID \
           --location=global \
           --recommender=google.resourcemanager.projectUtilization.Recommender
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `PROJECT_ID`: The ID of a different project for which you'd like to view the unattended project recommendations.
**Note:** If the command does not return any recommendations, the project is either not unattended or hasn't been around for 30 days or more.
  3. To list unattended project recommendations for the entire organization, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         gcloud recommender recommendations list \
           --billing-project=BILLING_PROJECT_ID \
           --organization=ORGANIZATION_ID \
           --location=global \
           --recommender=google.resourcemanager.projectUtilization.Recommender
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `ORGANIZATION_ID`: The ID of the Organization for which you'd like to view the unattended project recommendations.
  4. To list unattended project recommendations that are using a specific Billing Account, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         gcloud recommender recommendations list \
           --billing-project=BILLING_PROJECT_ID \
           --billing-account=BILLING_ACCOUNT_ID \
           --location=global \
           --recommender=google.resourcemanager.projectUtilization.Recommender
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `BILLING_ACCOUNT_ID`: The ID of your Google Cloud Billing Account.

**Note:** You can expand the details of the Recommendations from the list command by appending a --format=yaml flag towards the end.

#### Insights

  1. To list usage insights for a given project, run the following command:
         
         gcloud recommender insights list \
           --project=PROJECT_ID \
           --location=global \
           --insight-type=google.resourcemanager.projectUtilization.Insight
         

Replace the following:

     * `PROJECT_ID`: The project ID.
  2. To list usage insights for a different project, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         gcloud recommender insights list \
           --billing-project=BILLING_PROJECT_ID \
           --project=PROJECT_ID \
           --location=global \
           --insight-type=google.resourcemanager.projectUtilization.Insight
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `PROJECT_ID`: The ID of a different project for which you'd like to view the unattended recommender insights.
  3. To list usage insights for the entire organization, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         gcloud recommender insights list \
           --billing-project=BILLING_PROJECT_ID \
           --organization=ORGANIZATION_ID \
           --location=global \
           --insight-type=google.resourcemanager.projectUtilization.Insight
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `ORGANIZATION_ID`: The ID of the Organization for which you'd like to view the usage insights.
  4. To list usage insights that are using a specific Billing Account, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         gcloud recommender insights list \
           --billing-project=BILLING_PROJECT_ID \
           --billing-account=BILLING_ACCOUNT_ID \
           --location=global \
           --insight-type=google.resourcemanager.projectUtilization.Insight
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `BILLING_ACCOUNT_ID`: The ID of your Google Cloud Billing Account.

**Note:** You can expand the details of the Insights from the list command by appending a --format=yaml flag towards the end.

###  API 

To view recommendations and insights, you can use `curl` to send a request to the recommender APIs. To authorize requests from the command line, you use OAuth access tokens. An OAuth access token is a string that grants temporary access to an API.

**Note:** If you aren't already familiar with the authentication prerequisites for calling Google Cloud APIs, see the [Authentication overview](https://docs.cloud.google.com/docs/authentication#service-account-keys).

#### Recommendations

  1. To list unattended project recommendations for the project where you've enabled the Recommender API, run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/\
         recommenders/google.resourcemanager.projectUtilization.Recommender/recommendations"
         

Replace the following:

     * PROJECT_ID`: The project ID.
**Note:** If the API call does not return any recommendations, the project is either not unattended or hasn't been around for 30 days or more.
  2. To list unattended project recommendations in a different project while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
         -H "x-goog-user-project: BILLING_PROJECT_ID" \
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global/\
         recommenders/google.resourcemanager.projectUtilization.Recommender/recommendations"
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `PROJECT_ID`: The ID of a different project for which you'd like to view the unattended project recommendations.
  3. To list unattended project recommendations for the entire organization, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
         -H "x-goog-user-project: BILLING_PROJECT_ID" \
         "https://recommender.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/\
         recommenders/google.resourcemanager.projectUtilization.Recommender/recommendations"
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `ORGANIZATION_ID`: The ID of the Organization for which you'd like to view the unattended project recommendations.
  4. To list unattended project recommendations that are using a specific Billing Account, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
         -H "x-goog-user-project: BILLING_PROJECT_ID" \
         "https://recommender.googleapis.com/v1/billingAccounts/BILLING_ACCOUNT_ID/locations/global/\
         recommenders/google.resourcemanager.projectUtilization.Recommender/recommendations"
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `BILLING_ACCOUNT_ID`: The ID of your Google Cloud Billing Account.



#### Insights

  1. To list usage insights for a given project, run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/global\
         /insightTypes/google.resourcemanager.projectUtilization.Insight/insights"
         

Replace the following:

     * PROJECT_ID`: The project ID.
  2. To list usage insights for a different project, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "x-goog-user-project: BILLING_PROJECT_ID/" \
         "https://recommender.googleapis.com/v1/projects/PROJECT_ID//locations/global\
         /insightTypes/google.resourcemanager.projectUtilization.Insight/insights"
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `PROJECT_ID`: The ID of a different project for which you'd like to view the unattended recommender insights.
  3. To list usage insights for the entire organization, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
         -H "x-goog-user-project: PROJECT_ID/" \
         "https://recommender.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/\
         insightTypes/google.resourcemanager.projectUtilization.Insight/insights"
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `ORGANIZATION_ID`: The ID of the Organization for which you'd like to view the unattended project recommendations.
  4. To list usage insights that are using a specific Billing Account, while using a project where you've enabled the Recommender API (as in the previous step), run the following command:
         
         curl \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
         -H "x-goog-user-project: PROJECT_ID/" \
         "https://recommender.googleapis.com/v1/billingAccounts/BILLING_ACCOUNT_ID/locations/global/\
         insightTypes/google.resourcemanager.projectUtilization.Insight/insights"
         

Replace the following:

     * `BILLING_PROJECT_ID`: The ID of the project that you've enabled with the Recommender API (this would be the same PROJECT_ID as given in the previous step).
     * `BILLING_ACCOUNT_ID`: The ID of your Google Cloud Billing Account.



### Configuring recommendation parameters

This section describes how to view and [configure](https://docs.cloud.google.com/recommender/docs/key-concepts#configuration) this recommender using `gcloud` and `curl`.

The following table lists various parameters that can be configured:

Parameter | Description | Expected Values  
---|---|---  
`minimum_observation_period` | Minimum observation period defines the number of days of Project activity to be analyzed, before a Recommendation is generated.  Setting this value is currently only supported at the Organization level.  | "P30D"[DEFAULT], "P60D", "P90D", "P180D", "P270D", "P365D"   
  
###  gcloud 

To view and update recommender configurations using `gcloud`, follow the steps below.

#### Viewing configurations

  1. To view Unattended Project Recommender configurations for a given organization, run the following command from a project belonging to that organization which has the Recommender API enabled:
         
         gcloud beta recommender recommender-config describe \
         google.resourcemanager.projectUtilization.Recommender \
         --organization=ORGANIZATION_ID \
         --location=global
         

Replace the following:

     * `ORGANIZATION_ID`: The organization ID.
  2. Example Output: 
         
         etag: ETAG
         name: organizations/ORGANIZATION_ID/locations/global/recommenders/google.resourcemanager.projectUtilization.Recommender/config
         recommenderGenerationConfig:
           params:
             minimum_observation_period: P30D
         revisionId: DEFAULT
         updateTime: '2022-04-19T00:57:55Z'
         

Note the ETAG value:

     * `ETAG`: This value will be used in `recommender-config update`.



#### Updating configurations

  1. To update Unattended Project Recommender configurations for a given organization, pick a project belonging to that organization where you have enabled the Recommender API, create a `config.gcloud` file:
         
         
         {
          "params": {
             "minimum_observation_period": DURATION
           }
         }
         

Replace the following:

     * `DURATION`: One value from "P30D", "P60D", "P90D", "P180D", "P270D", "P365D"
  2. Run the following command:
         
         gcloud beta recommender recommender-config update \
         google.resourcemanager.projectUtilization.Recommender \
         --organization=ORGANIZATION_ID \
         --location=global \
         --config-file=config.gcloud \
         --etag=ETAG
         

Replace the following:

     * `ORGANIZATION_ID`: The organization ID.
     * `ETAG`: The etag value that was returned from `recommender-config describe`.



###  API 

To view and update recommender configurations, you can use `curl` to send a request to the Recommender APIs. To authorize requests from the command line, you use OAuth access tokens. An OAuth access token is a string that grants temporary access to an API.

**Note:** If you aren't already familiar with the authentication prerequisites for calling Google Cloud APIs, see the [Authentication overview](https://docs.cloud.google.com/docs/authentication#service-account-keys).

#### Viewing configurations

  1. To view Unattended Project Recommender configurations for a given organization, run the following command from a project belonging to that organization which has the Recommender API enabled:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "x-goog-user-project: PROJECT_ID" \
         https://recommender.googleapis.com/v1beta1/organizations/ORGANIZATION_ID/locations/global/recommenders/google.resourcemanager.projectUtilization.Recommender/config
         

Replace the following:

     * `PROJECT_ID`: The project ID.
     * `ORGANIZATION_ID`: The organization ID.
  2. Example Output:
         
         {
           "name": "organizations/ORGANIZATION_ID/locations/global/recommenders/google.resourcemanager.projectUtilization.Recommender/config",
           "recommenderGenerationConfig": {
             "params": {
               "minimum_observation_period": "P60D"
             }
           },
           "etag": ETAG,
           "updateTime": "2022-04-21T18:51:17.407255Z",
           "revisionId": "75c3b0d7"
         }
         
         

Note the ETAG value:

     * `ETAG`: This value will be used in `curl PATCH`.



#### Updating configurations

  1. To update Unattended Project Recommender configurations for a given organization, pick a project belonging to that organization where you have enabled the Recommender API, create a `request.json` file:
         
         
         {
           "name": "organizations/ORGANIZATION_ID/locations/global/recommenders/google.resourcemanager.projectUtilization.Recommender/config",
           "recommenderGenerationConfig": {
             "params": {
               "minimum_observation_period": DURATION
             }
           },
         "etag": ETAG,
         }
         

Replace the following:

     * `DURATION`: One value from "P30D", "P60D", "P90D", "P180D", "P270D", "P365D"
     * `ETAG`: The etag value that was returned from `CURL get`.
  2. Run the following command line:
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "x-goog-user-project: PROJECT_ID" \
         -H "Content-Type: application/json; charset=utf-8" -d @request.json \
         https://recommender.googleapis.com/v1beta1/organizations/ORGANIZATION_ID/locations/global/recommenders/google.resourcemanager.projectUtilization.Recommender/config
         

Replace the following:

     * `PROJECT_ID`: The project ID.
     * `ORGANIZATION_ID`: The organization ID.



## What's next

  * [Shutting down (deleting) projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects)
  * [Deleting projects in an organization](https://docs.cloud.google.com/resource-manager/docs/organization-resource-management#delete-projects)
  * [Carbon Footprint reporting methodology](https://docs.cloud.google.com/carbon-footprint/docs/methodology)
  * [Interactive tutorial](https://github.com/GoogleCloudPlatform/cloud-shell-tutorials/blob/master/cloud-console-tutorials/active_assist_recommenders/unattended_project_recommender.md) ([open in Cloud Shell](https://console.cloud.google.com/?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fcloud-shell-tutorials&cloudshell_tutorial=cloud-console-tutorials%2Factive_assist_recommenders%2Funattended_project_recommender.md&page=shell))



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
