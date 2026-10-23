---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/manage-insights/
title: Manage and export insights \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:35.616377+00:00
---

# Manage and export insights  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/manage-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  Manage and export insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to list, describe, dismiss, restore, and export insights.

## Required roles and permissions

To get the permissions that you need to manage and export insights, ask your administrator to grant you the following IAM roles on your project: 

  * [Firewall Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.firewallAdmin) (`roles/recommender.firewallAdmin`)
  * [Firewall Recommender Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.firewallViewer) (`roles/recommender.firewallViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage and export insights. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage and export insights:

  * `recommender.computeFirewallInsights.list`
  * `recommender.computeFirewallInsights.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List insights for a project

To list the insights for a project, do the following: 

###  gcloud 

Use the [`gcloud recommender insights list` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list):
    
    
    gcloud recommender insights list \
        --project=PROJECT_ID \
        --location=global \
        --insight-type=google.compute.firewall.Insight \
        --filter=EXPRESSION \
        --limit=LIMIT \
        --page-size=PAGE_SIZE \
        --sort-by=SORT_BY \
        --format=json
    

Replace `PROJECT_ID` with the project ID that you want to list insights for.

The `location` flag always uses the location named `global`. The `insight-type` flag always uses the insight type named `google.compute.firewall.Insight`. Unless you format the output in JSON, the command output is tabular.

The following fields are optional:

  * `EXPRESSION`: apply this Boolean filter to each resource that you want to list

If the expression evaluates as `True`, that item is listed. For more details and examples of filter expressions, run `$ gcloud topic filters` or see the [`gcloud topic filters` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

  * `LIMIT`: the maximum number of resources to list; the default number of resources listed is unlimited

  * `PAGE_SIZE`: the maximum number of resources to list per page

The default page size is determined by the service; otherwise, there's no paging. Paging might be applied before or after `FILTER` and `LIMIT`.

  * `SORT_BY`: a list of comma-separated field key names to sort by for a resource

The default order is ascending. To specify a descending order, prefix a field with `~` (a tilde).




###  API 

Make a `GET` request to the [`projects.locations.insightTypes.insights` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/get):
    
    
    GET https://recommender.googleapis.com/v1/{parent=projects/*/locations/global/insightTypes/*}/insights
    

The following example shows a sample response for this command:
    
    
    insights {
    "name": "projects/{project_number}/locations/global/insightTypes/google.compute.firewall.Insight/insights/{insight-id}"
    "description": "Firewall projects/{project_id}/global/firewalls/{shadowed_firewall_name} is shadowed by projects/{project_id}/global/firewalls/{shadowing_firewall_name}."
    "content": {
      "shadowingFirewalls": [
        "//compute.googleapis.com/projects/{project_id}/global/firewalls/{shadowing_firewall_name1}"
      ]
    },
    "lastRefreshTime": "2020-04-01T19:16:43Z",
    "observationPeriod": "0s",
    "stateInfo" {
     "state": "ACTIVE"
    }
    "category": "SECURITY"
    "targetResources":[
     "//compute.googleapis.com/projects/{project_id}/global/firewalls/{shadowed_firewall_name}"
     ],
    "insightSubtype": "SHADOWED_RULE"
    }
    

## Describe insights

To describe details about a particular firewall rule in a project, do the following: 

###  gcloud 

Use the [`gcloud recommender insights describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/describe):
    
    
    gcloud recommender insights describe INSIGHT_ID \
        --project=PROJECT_NAME \
        --location=global \
        --insight-type=google.compute.firewall.Insight
    

Replace the following:

  * `INSIGHT_ID`: the ID of the insight to describe
  * `PROJECT_NAME`: the name of the project that you want to list insights for



The `location` flag always uses the location named `global`. The `insight-type` flag always uses the insight type named `google.compute.firewall.Insight`.

###  API 

Make a `GET` request to the [`projects.locations.insightTypes.insights` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/get):
    
    
    GET
    https://recommender.googleapis.com/v1/{name=projects/*/locations/global/insightTypes/*/insights/*}
    {
     "name": projects/PROJECT_ID/locations/LOCATION/insightTypes/INSIGHT_TYPE_ID/insights/INSIGHT_ID,
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `LOCATION`: always use the location named `global`
  * `INSIGHT_TYPE_ID`: always use the value `google.compute.firewall.Insight`
  * `INSIGHT_ID`: the ID for the insight



## Mark an insight as dismissed

If any insight isn't meaningful, or if you want to hide it for any other reason, you can dismiss it. After you dismiss an insight, the Google Cloud console no longer displays the insight to you or other users unless you restore it.

To mark an insight as dismissed, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Firewall Insights** page.

[Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)

  2. Find the appropriate card and click **View full list**.

  3. Select the rules that you want to dismiss, and then click **Dismiss**.




## Restore a dismissed insight

If you dismissed an insight that you later think is relevant, you or another user can restore it and make it visible in the Google Cloud console.

To restore a dismissed insight, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Firewall Insights** page.

[Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)

  2. Click **Dismiss History**. In response, the Google Cloud console displays the **Dismissed insights** page.

  3. Select the insights that you want to restore, and then click **Restore**.




## Export insights

You can export shadowed and overly permissive rule insights to a Cloud Storage [bucket](https://docs.cloud.google.com/storage/docs/buckets) in CSV or JSON format. `Deny rules with hits` information can't be exported because it is based on firewall stackdriver metrics and not on insights.

To export insights, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Firewall Insights** page.

[Go to Firewall Insights](https://console.cloud.google.com/net-intelligence/firewalls)

  2. Click **Save as**.

  3. Enter the Cloud Storage bucket name.

  4. For **Save as...** , select CSV or JSON.

  5. Click **Save**.




You can also export insights to BigQuery. When you export insights to BigQuery, you can view daily snapshots of insights for your organization. For more information, see [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

## What's next

  * [Review and optimize firewall rules](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/review-optimize)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
