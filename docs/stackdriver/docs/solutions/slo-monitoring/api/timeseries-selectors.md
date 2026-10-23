---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/timeseries-selectors/
title: Retrieving SLO data \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:32.370668+00:00
---

# Retrieving SLO data  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/timeseries-selectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Retrieving SLO data Stay organized with collections  Save and categorize content based on your preferences. 

SLO data is stored in time series. You can retrieve SLO time series by specifying a _time-series selector_ in the `filter` parameter to the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method or by using the [direct filter mode](https://docs.cloud.google.com/monitoring/charts/metrics-selector#metric-filter) in Metrics Explorer.

**Note:** The use of the `timeSeries.list` method is described in [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics), and general filtering is described in [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters).

## SLO-based alerting policies

If you are creating an alerting policy by using the Cloud Monitoring API, you specify the filter using a time-series selector as a field in the policy's threshold condition. For information about how to create SLO-based alerting policies by using the Monitoring API, see [Create an alerting policy](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/create-policy-api#api-create-slo-policy).

Only a subset of the time-series selectors available for SLOs can be used in alerting policies. Also, SLO-based alerting policies created with the Google Cloud console always use the `select_slo_burn_rate` selector.

## Using a time-series selector in a filter

To retrieve time-series data for SLOs, your filter must specify a time-series selector. SLO data isn't stored with metric types and can't be retrieved with the filter that specifies a pair of metric and monitored-resource types.

### Names and arguments

Time-series selectors have one of the following forms:
    
    
    SELECTOR_NAME(SLO_NAME)
    SELECTOR_NAME(SLO_NAME, LOOKBACK_PERIOD)
    

The selectors have names that start with `select_slo_`, and they take one or two arguments:

  * The first argument to the selector is the resource name for an SLO, which looks like this: 
        
        projects/PROJECT_ID/services/SERVICE_ID/serviceLevelObjectives/SLO_ID
        

The previous expression contains three variables:

    * PROJECT_ID: Name or number of a Google Cloud project.
    * SERVICE_ID: Name of a service.
    * SLO_ID: Identifier for an SLO that is defined for the service.

For information about how to find the values for the SERVICE_ID and SLO_ID fields for your Google Cloud project, see [Working with the API](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/using-api).

  * The second argument, if supported, is a lookback period. See [Types of error-budget alerts](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/alerting-on-budget-burn-rate#burn-rates) for information about lookback periods. Valid time units are "ns", "us" "ms", "s", "m", "h".




For example, the `select_slo_budget` selector takes an SLO_NAME argument, so a filter using this selector looks like the following:
    
    
    select_slo_budget("projects/PROJECT_ID/services/SERVICE_ID/serviceLevelObjectives/SLO_ID")
    

In contrast, the `select_slo_burn_rate` selector requires the SLO_NAME and LOOKBACK_PERIOD arguments, so a filter using this selector looks like the following:
    
    
    select_slo_burn_rate("projects/PROJECT_ID/services/SERVICE_ID/serviceLevelObjectives/SLO_ID", "3600s")
    

For a list and description of all the selectors, see Time-series selectors.

### Retrieving data with a selector

One way you can query time-series data is to use the APIs Explorer tool on the [`timeSeries.list` method's reference page](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). For information about this tool, see [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer).

For example, to retrieve information about an SLO's budget, complete the following fields in the APIs Explorer tool:

  * **name** : `projects/PROJECT_ID`
  * **filter** : `select_slo_budget("projects/PROJECT_ID/services/SERVICE_ID/serviceLevelObjectives/SLO_ID")`
  * **interval.startTime** : `2021-10-07T13:00:20-04:00`
  * **interval.endTime** : `2021-10-08T13:00:20-04:00`



For one system, after variables such as PROJECT_ID are replaced with values and the method is executed, the following time series data is returned:

![An excerpt from the retrieved time series](https://docs.cloud.google.com/static/stackdriver/docs/solutions/slo-monitoring/images/tss-in-apiexplorer-resp.png)

## Time-series selectors

This section lists the available time-series selectors for SLOs and describes what they represent. All the selectors can be used in filters with the `timeSeries.list` method to retrieve time-series data. Not all of them are supported in alerting policies.

### `select_slo_burn_rate`

**Syntax** : `select_slo_burn_rate(SLO_NAME, LOOKBACK_PERIOD)`

The “burn-rate” time-series selector returns the ratio of the current failure rate (the rate of bad requests in the lookback interval) to the sustainable failure rate for the SLO. The sustainable failure rate is the rate at which the SLO is exactly met.

The values in this time series can range from 0 to infinity:

  * A value of one indicates that the service exhibits the ideal failure rate: not too risky, not too conservative.
  * A value greater than one means the failure rate exceeds the sustainable rate. The higher the value, the sooner the SLO falls out of compliance.
  * A value less than one means that the current failure rate is less than the sustainable rate.



We recommend that you use two alerting policies to monitor burn rate: a fast-burn policy to alert you to spikes in the burn rate, and a slow-burn policy to alert you to gradual increases.

You can create and edit alerting policies based on this time-series selector by using the API or the Google Cloud console.

All SLO-based alerting policies created by using the Google Cloud console use this selector to retrieve the SLO data.

### `select_slo_health`

**Syntax** : `select_slo_health(SLO_NAME)`

The “SLO health” time series answers the question, “During a given alignment period, what was the ratio of good requests to total requests?” The SLI for the service defines what counts as a good request. For more information about SLIs, see [Overview](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/sli-metrics/overview).

This time series measures service performance: if every request to the service is good, then the data points in this time series have the value 1. As the number of bad requests rise, the values of the data points drop.

### `select_slo_compliance`

**Syntax** : `select_slo_compliance(SLO_NAME)`

The “SLO compliance” time series answers the question, “What is the ratio of good units to total units since the beginning of the compliance period?” The SLO defines the compliance period as a rolling window or a range of calendar time. The unit can be a request or a window of time. For more information, see [Compliance in request- and windows-based SLOs](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#slo-types).

This time series gives you a general picture of how well the service is meeting the SLO. It doesn't produce an operationally urgent signal.

Don't use this time-series selector in alerting policies.

### `select_slo_budget`

**Syntax** : `select_slo_budget(SLO_NAME)`

The “SLO budget” time series answers the question, “How much of the error budget remained at the time of the measurement?” The error budget might be measured in requests or minutes, and the amount remaining is computed based on whether the compliance period is measured in calendar time or as a rolling window. For more information, see [Error budgets](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring#defn-error-budget).

This time series measures the risk in a service's reliability. If the error budget becomes less than zero, then it might not be possible to meet the SLO for the current period. A failure to meet the SLO might have real consequences for an organization's production environment, depending on how the organization governs reliability.

Don't use this time-series selector in alerting policies.

### `select_slo_budget_fraction`

**Syntax** : `select_slo_budget_fraction(SLO_NAME)`

The “SLO budget fraction” time series answers the question, “How much of the error budget, as a fraction from negative infinity to one, remains at this time?”

Don't use this time-series selector in alerting policies.

### `select_slo_budget_total`

**Syntax** : `select_slo_budget_total(SLO_NAME)`

The “SLO total budget” time series answers the question, “What is the total error budget (in requests or minutes) that is projected to be available at this time, based on the behavior of the service since the start of the compliance period?” The SLO defines the compliance period as a rolling window or a range of calendar time.

Don't use this time-series selector in alerting policies.

### `select_slo_counts`

**Syntax** : `select_slo_counts(SLO_NAME)`

The “SLO counts” time series answers the question, “During a given alignment period, what is the number of good and bad requests?” This selector provides a time series that records general health and is suitable for ingestion into long-term storage systems.

Don't use this time-series selector in alerting policies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
