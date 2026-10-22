---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api/
title: Use the Recommender CLI and API \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:14.029014+00:00
---

# Use the Recommender CLI and API  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  Use the Recommender CLI and API Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Recommender API or Google Cloud CLI to view Network Analyzer insights. This document shows how to view insights for a specific Network Analyzer insight type.

## Request insights

###  gcloud 

To list insights for a Google Cloud project, run the following command:
    
    
    gcloud recommender insights list \
        --project=PROJECT_ID \
        --location=LOCATION \
        --insight-type=INSIGHT_TYPE \
        --filter=EXPRESSION \
        --limit=LIMIT \
        --page-size=PAGE_SIZE \
        --sort-by=SORT_BY \
        --format=json
    

Replace the following:

  * `PROJECT_ID`: the project ID that you want to list insights for. You can also list all insights for a folder, organization, or a billing account.
  * `LOCATION`: the location to list insights for, such as `global`, `europe`, `asia-east1`, or `us-central1-a`.
  * `INSIGHT_TYPE`: the Network Analyzer insight type to request, such as `google.networkanalyzer.vpcnetwork.connectivityInsight`.

For a complete list of insight types, see Insight groups and types.




The following fields are optional:

  * `EXPRESSION`: apply this Boolean filter to each resource that you want to list.

If the expression evaluates as `True`, that item is listed. For more details and examples of filter expressions, run `$ gcloud topic filters` or see the [`gcloud topic filters` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

  * `LIMIT`: the maximum number of resources to list; the default number of resources listed is unlimited.

  * `PAGE_SIZE`: the maximum number of resources to list per page.

The default page size is determined by the service; otherwise, there is no paging. Paging might be applied before or after `FILTER` and `LIMIT`.

  * `SORT_BY`: a list of comma-separated field key names to sort by for a resource.

The default order is ascending. To specify a descending order, prefix a field with `~` (a tilde).




###  API 

To get insights for a Google Cloud project, make a `GET` request to the [`projects.locations.insightTypes.insights` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/get):
    
    
    https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/INSIGHT_TYPE/insights
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the location to list insights for, such as `global`, `europe`, `asia-east1`, or `us-central1-a`.
  * `INSIGHT_TYPE`: the Network Analyzer insight type to list, such as google.networkanalyzer.vpcnetwork.connectivityInsight.

For a complete list of insight types, see Insight groups and types.




The following example shows a sample response for this command:
    
    
    {
      "name": "projects/{project_number}/locations/{location}/insightTypes/google.networkanalyzer.hybridconnectivity.dynamicRouteInsight/insights/{insight_id}",
      "description": "Dynamic route is fully shadowed by a peering subnet route",
      "content": {
        "networkUri": "//compute.googleapis.com/projects/{project_id}/global/networks/{network_name}",
        "region": "{location}",
        "ipRange": "{ip_range}",
        "priority": 100,
        "nextHopUri": "//compute.googleapis.com/projects/{project_id}/regions/{location}/vpnTunnels/{tunnel_name}",
        "cloudRouterUri": "//compute.googleapis.com/projects/{project_id}/regions/{location}/routers/{router_name}",
        "shadowingRouteUris": [
          "//compute.googleapis.com/projects/{project_id}/global/routes/{route_name}"
        ],
        "shadowingRouteType": "PEERING_SUBNET"
      },
      "lastRefreshTime": "2022-09-15T21:10:57.187942979Z",
      "observationPeriod": "611870.625920374s",
      "stateInfo": {
        "state": "ACTIVE"
      },
      "category": "PERFORMANCE",
      "targetResources": [
        "//compute.googleapis.com/projects/{project_id}/regions/{location}/vpnTunnels/{tunnel_name}"
      ],
      "insightSubtype": "DYNAMIC_ROUTE_FULLY_SHADOWED",
      "severity": "MEDIUM"
    }
    

## Describe insight details

###  gcloud 

To list details of a particular insight, run the following command:
    
    
    gcloud recommender insights describe INSIGHT_ID \
        --project=PROJECT_ID \
        --location=LOCATION \
        --insight-type=INSIGHT_TYPE
    

Replace the following:

  * `INSIGHT_ID`: the ID of the insight to describe.
  * `PROJECT_ID`: the ID of the project containing the insight.
  * `LOCATION`: the location to list insights for.
  * `INSIGHT_TYPE`: the Network Analyzer insight type of the insight, such as `google.networkanalyzer.vpcnetwork.connectivityInsight`.

For a complete list of insight types, see Insight groups and types.




###  API 

To get details for an insight, make a `GET` request to the [`projects.locations.insightTypes.insights` method](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/get):
    
    
    https://recommender.googleapis.com/v1/projects/PROJECT/locations/LOCATION/insightTypes/INSIGHT_TYPE/insights/INSIGHT_ID
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `LOCATION`: the location of the insight.
  * `INSIGHT_TYPE`: the Network Analyzer insight type of the insight, such as `google.networkanalyzer.vpcnetwork.connectivityInsight`.

For a complete list of insight types, see Insight groups and types.

  * `INSIGHT_ID`: the insight ID for the insight.




## Insight groups and types

For more information about Network Analyzer insights, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
