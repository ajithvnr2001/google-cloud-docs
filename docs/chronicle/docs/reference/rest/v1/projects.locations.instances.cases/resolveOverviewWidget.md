---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/resolveOverviewWidget/
title: Method: cases.resolveOverviewWidget \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:05.919169+00:00
---

# Method: cases.resolveOverviewWidget  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.cases/resolveOverviewWidget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: cases.resolveOverviewWidget Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



**Full name** : projects.locations.instances.cases.resolveOverviewWidget

Resolves updated data for a specific case overview widget. Use this method to refresh content for UI elements like graphs or activity feeds associated with a case.

### HTTP request

`GET https://{endpoint}/v1/{name}:resolveOverviewWidget`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The case to resolve overview widget for. Format: projects/{project}/locations/{location}/instances/{instance}/cases/{case}:resolveOverviewWidget  
  
### Query parameters

Parameters  
---  
`widgetIdentifier` |  `string` Required. Widget identifier to resolve.  
`caseId` |  `integer` Required. Case id to resolve overview widget for.  
`forceRefresh` |  `boolean` Optional. Force refresh the widget.  
`firstRequest` |  `boolean` Optional. Is first request to resolve overview widget.  
  
### Request body

The request body must be empty.

### Response body

Response message for cases.resolveOverviewWidget.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "alertOverviewWidget": {
        object ([AlertOverviewWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/AlertOverviewWidget))
      },
      "caseApsGraphWidget": {
        object ([CaseApsGrapthWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseApsGrapthWidget))
      },
      "caseAssistantWidget": {
        object ([CaseAssistantWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseAssistantWidget))
      },
      "caseDescriptionWidget": {
        object ([CaseDescriptionWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseDescriptionWidget))
      },
      "caseImpactedResourcesWidget": {
        object ([CaseImpactedResourcesWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseImpactedResourcesWidget))
      },
      "caseRecommendationsWidget": {
        object ([CaseRecommendationsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseRecommendationsWidget))
      },
      "caseRelatedFindingsWidget": {
        object ([CaseRelatedFindingsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseRelatedFindingsWidget))
      },
      "entitiesHighlightWidget": {
        object ([EntitiesHighlightWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EntitiesHighlightWidget))
      },
      "eventsWidget": {
        object ([EventsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EventsWidget))
      },
      "formWidget": {
        object ([FormWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FormWidget))
      },
      "graphWidget": {
        object ([GraphWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/GraphWidget))
      },
      "htmlWidget": {
        object ([HtmlWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/HtmlWidget))
      },
      "insightsWidget": {
        object ([InsightsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/InsightsWidget))
      },
      "jsonResultsWidget": {
        object ([JsonResultsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/JsonResultsWidget))
      },
      "keyValueWidget": {
        object ([KeyValueWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/KeyValueWidget))
      },
      "pendingStepsWidget": {
        object ([WorkflowPendingStepsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WorkflowPendingStepsWidget))
      },
      "potentiallyGroupedAlertsWidget": {
        object ([PotentiallyGroupedAlertsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/PotentiallyGroupedAlertsWidget))
      },
      "quickActionsWidget": {
        object ([QuickActionsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/QuickActionsWidget))
      },
      "siemAlertsWidget": {
        object ([SiemAlertsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/SiemAlertsWidget))
      },
      "statisticsWidget": {
        object ([StatisticsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/StatisticsWidget))
      },
      "textWidget": {
        object ([TextWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/TextWidget))
      },
      "timelineWidget": {
        object ([TimelineWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/TimelineWidget))
      },
      "wallActivitiesWidget": {
        object ([WallActivitiesWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WallActivitiesWidget))
      },
      "ruleOverviewWidget": {
        object ([RuleOverviewWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/RuleOverviewWidget))
      },
      "thirdPartyWidget": {
        object ([ThirdPartyWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/ThirdPartyWidget))
      },
      "eventHighlightsWidget": {
        object ([EventHighlightsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EventHighlightsWidget))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The overview widget to resolve. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`alertOverviewWidget` |  `object (`[AlertOverviewWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/AlertOverviewWidget)`)` Output only. The alert overview widget to resolve.  
`caseApsGraphWidget` |  `object (`[CaseApsGrapthWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseApsGrapthWidget)`)` Output only. The case aps graph widget to resolve.  
`caseAssistantWidget` |  `object (`[CaseAssistantWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseAssistantWidget)`)` Output only. The AI case assistant widget to resolve.  
`caseDescriptionWidget` |  `object (`[CaseDescriptionWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseDescriptionWidget)`)` Output only. The case description widget to resolve.  
`caseImpactedResourcesWidget` |  `object (`[CaseImpactedResourcesWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseImpactedResourcesWidget)`)` Output only. The case impacted resources widget to resolve.  
`caseRecommendationsWidget` |  `object (`[CaseRecommendationsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseRecommendationsWidget)`)` Output only. The case recommendations widget to resolve.  
`caseRelatedFindingsWidget` |  `object (`[CaseRelatedFindingsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/CaseRelatedFindingsWidget)`)` Output only. The case related findings widget to resolve.  
`entitiesHighlightWidget` |  `object (`[EntitiesHighlightWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EntitiesHighlightWidget)`)` Output only. The entities highlight widget to resolve.  
`eventsWidget` |  `object (`[EventsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EventsWidget)`)` Output only. The events widget to resolve.  
`formWidget` |  `object (`[FormWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/FormWidget)`)` Output only. The form widget to resolve.  
`graphWidget` |  `object (`[GraphWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/GraphWidget)`)` Output only. The graph widget to resolve.  
`htmlWidget` |  `object (`[HtmlWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/HtmlWidget)`)` Output only. The html widget to resolve.  
`insightsWidget` |  `object (`[InsightsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/InsightsWidget)`)` Output only. The insights widget to resolve.  
`jsonResultsWidget` |  `object (`[JsonResultsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/JsonResultsWidget)`)` Output only. The json result widget to resolve.  
`keyValueWidget` |  `object (`[KeyValueWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/KeyValueWidget)`)` Output only. The key value widget to resolve.  
`pendingStepsWidget` |  `object (`[WorkflowPendingStepsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WorkflowPendingStepsWidget)`)` Output only. The workflow pending steps widget to resolve.  
`potentiallyGroupedAlertsWidget` |  `object (`[PotentiallyGroupedAlertsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/PotentiallyGroupedAlertsWidget)`)` Output only. The potentially grouped alerts widget to resolve.  
`quickActionsWidget` |  `object (`[QuickActionsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/QuickActionsWidget)`)` Output only. The quick actions widget to resolve.  
`siemAlertsWidget` |  `object (`[SiemAlertsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/SiemAlertsWidget)`)` Output only. The siem alerts widget to resolve.  
`statisticsWidget` |  `object (`[StatisticsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/StatisticsWidget)`)` Output only. The statistics widget to resolve.  
`textWidget` |  `object (`[TextWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/TextWidget)`)` Output only. The text widget to resolve.  
`timelineWidget` |  `object (`[TimelineWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/TimelineWidget)`)` Output only. The timeline widget to resolve.  
`wallActivitiesWidget` |  `object (`[WallActivitiesWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/WallActivitiesWidget)`)` Output only. The case wall activities widget to resolve.  
`ruleOverviewWidget` |  `object (`[RuleOverviewWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/RuleOverviewWidget)`)` Output only. The rule overview widget to resolve.  
`thirdPartyWidget` |  `object (`[ThirdPartyWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/ThirdPartyWidget)`)` Output only. The third party widget to resolve.  
`eventHighlightsWidget` |  `object (`[EventHighlightsWidget](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/EventHighlightsWidget)`)` Output only. The event highlights widget to resolve.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `chronicle.cases.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
