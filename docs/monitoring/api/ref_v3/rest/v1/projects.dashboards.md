---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards
title: REST Resource: projects.dashboards \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:39.397803+00:00
---

# REST Resource: projects.dashboards  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.dashboards Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Dashboard
    * JSON representation
  * GridLayout
    * JSON representation
  * Widget
    * JSON representation
  * XyChart
    * JSON representation
  * DataSet
    * JSON representation
  * TimeSeriesQuery
    * JSON representation
  * TimeSeriesFilter
    * JSON representation
  * Aggregation
    * JSON representation
  * Aligner
  * Reducer
  * PickTimeSeriesFilter
    * JSON representation
  * Method
  * Direction
  * Interval
    * JSON representation
  * TimeSeriesFilterRatio
    * JSON representation
  * RatioPart
    * JSON representation
  * OpsAnalyticsQuery
    * JSON representation
  * TraceQuery
    * JSON representation
  * SpanDataValue
  * SpanFilters
    * JSON representation
  * SpanAttributeFilter
    * JSON representation
  * PlotType
  * TargetAxis
  * Dimension
    * JSON representation
  * SortOrder
  * Measure
    * JSON representation
  * AggregationFunction
    * JSON representation
  * Parameter
    * JSON representation
  * Breakdown
    * JSON representation
  * ColumnSortingOptions
    * JSON representation
  * Threshold
    * JSON representation
  * Color
  * Direction
  * TargetAxis
  * Axis
    * JSON representation
  * Scale
  * ChartOptions
    * JSON representation
  * Mode
  * Scorecard
    * JSON representation
  * GaugeView
    * JSON representation
  * SparkChartView
    * JSON representation
  * SparkChartType
  * Text
    * JSON representation
  * Format
  * TextStyle
    * JSON representation
  * HorizontalAlignment
  * VerticalAlignment
  * PaddingSize
  * FontSize
  * PointerLocation
  * AlertChart
    * JSON representation
  * TimeSeriesTable
    * JSON representation
  * TableDataSet
    * JSON representation
  * TableDisplayOptions
    * JSON representation
  * MetricVisualization
  * ColumnSettings
    * JSON representation
  * CellAlignment
  * CollapsibleGroup
    * JSON representation
  * LogsPanel
    * JSON representation
  * IncidentList
    * JSON representation
  * PieChart
    * JSON representation
  * PieChartDataSet
    * JSON representation
  * PieChartType
  * Treemap
    * JSON representation
  * TreemapDataSet
    * JSON representation
  * ErrorReportingPanel
    * JSON representation
  * SectionHeader
    * JSON representation
  * SingleViewGroup
    * JSON representation
  * DisplayType
  * FilterControl
    * JSON representation
  * VisibilityCondition
    * JSON representation
  * TemplateVariableCondition
    * JSON representation
  * Comparator
  * TimeRange
    * JSON representation
  * MosaicLayout
    * JSON representation
  * Tile
    * JSON representation
  * RowLayout
    * JSON representation
  * Row
    * JSON representation
  * ColumnLayout
    * JSON representation
  * Column
    * JSON representation
  * DashboardFilter
    * JSON representation
  * ValueType
  * StringArray
    * JSON representation
  * FilterType
  * DashboardAnnotations
    * JSON representation
  * EventAnnotation
    * JSON representation
  * EventType
  * Methods



## Resource: Dashboard

A Google Stackdriver dashboard. Dashboards define the content and layout of pages in the Stackdriver web application.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "etag": string,
      "dashboardFilters": [
        {
          object ([DashboardFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DashboardFilter))
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "annotations": {
        object ([DashboardAnnotations](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DashboardAnnotations))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gridLayout": {
        object ([GridLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#GridLayout))
      },
      "mosaicLayout": {
        object ([MosaicLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#MosaicLayout))
      },
      "rowLayout": {
        object ([RowLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#RowLayout))
      },
      "columnLayout": {
        object ([ColumnLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ColumnLayout))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the dashboard.  
`displayName` |  `string` Required. The mutable, human-readable name.  
`etag` |  `string` `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An `etag` is returned in the response to `dashboards.get`, and users are expected to put that etag in the request to `dashboards.patch` to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation.  
`dashboardFilters[]` |  `object (`[DashboardFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DashboardFilter)`)` Filters to reduce the amount of data charted based on the filter criteria.  
`labels` |  `map (key: string, value: string)` Labels applied to the dashboard  
`annotations` |  `object (`[DashboardAnnotations](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DashboardAnnotations)`)` Configuration for event annotations to display on this dashboard.  
A dashboard's root container element that defines the layout style. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gridLayout` |  `object (`[GridLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#GridLayout)`)` Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.  
`mosaicLayout` |  `object (`[MosaicLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#MosaicLayout)`)` The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.  
`rowLayout` |  `object (`[RowLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#RowLayout)`)` The content is divided into equally spaced rows and the widgets are arranged horizontally.  
`columnLayout` |  `object (`[ColumnLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ColumnLayout)`)` The content is divided into equally spaced columns and the widgets are arranged vertically.  
End of mutually exclusive fields.  
  
## GridLayout

A basic layout divides the available space into vertical columns of equal width and arranges a list of widgets using a row-first strategy.

JSON representation  
---  
      
    
    {
      "columns": string,
      "widgets": [
        {
          object ([Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget))
        }
      ]
    }  
  
Fields  
---  
`columns` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of columns into which the view's width is divided. If omitted or set to zero, a system default will be used while rendering.  
`widgets[]` |  `object (`[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget)`)` The informational elements that are arranged into the columns row-first.  
  
## Widget

Widget contains a single dashboard component and configuration of how to present the component in the dashboard.

JSON representation  
---  
      
    
    {
      "title": string,
      "id": string,
      "visibilityCondition": {
        object ([VisibilityCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#VisibilityCondition))
      },
      "timeRange": {
        object ([TimeRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeRange))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "xyChart": {
        object ([XyChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#XyChart))
      },
      "scorecard": {
        object ([Scorecard](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Scorecard))
      },
      "text": {
        object ([Text](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Text))
      },
      "blank": {
        object
      },
      "alertChart": {
        object ([AlertChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#AlertChart))
      },
      "timeSeriesTable": {
        object ([TimeSeriesTable](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesTable))
      },
      "collapsibleGroup": {
        object ([CollapsibleGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#CollapsibleGroup))
      },
      "logsPanel": {
        object ([LogsPanel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#LogsPanel))
      },
      "incidentList": {
        object ([IncidentList](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#IncidentList))
      },
      "pieChart": {
        object ([PieChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PieChart))
      },
      "treemap": {
        object ([Treemap](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Treemap))
      },
      "errorReportingPanel": {
        object ([ErrorReportingPanel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ErrorReportingPanel))
      },
      "sectionHeader": {
        object ([SectionHeader](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SectionHeader))
      },
      "singleViewGroup": {
        object ([SingleViewGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SingleViewGroup))
      },
      "filterControl": {
        object ([FilterControl](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#FilterControl))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`title` |  `string` Optional. The title of the widget.  
`id` |  `string` Optional. The widget id. Ids may be made up of alphanumerics, dashes and underscores. Widget ids are optional.  
`visibilityCondition` |  `object (`[VisibilityCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#VisibilityCondition)`)` Optional. If set, this widget is rendered only when the condition is evaluated to true.  
`timeRange` |  `object (`[TimeRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeRange)`)` Optional. Represents a time range for the widget. When set, this time range will override the dashboard time range. Supported for line, stacked area and stacked bar widgets only.  
Content defines the component used to populate the widget. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`xyChart` |  `object (`[XyChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#XyChart)`)` A chart of time series data.  
`scorecard` |  `object (`[Scorecard](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Scorecard)`)` A scorecard summarizing time series data.  
`text` |  `object (`[Text](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Text)`)` A raw string or markdown displaying textual content.  
`blank` |  `object` A blank space.  
`alertChart` |  `object (`[AlertChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#AlertChart)`)` A chart of alert policy data.  
`timeSeriesTable` |  `object (`[TimeSeriesTable](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesTable)`)` A widget that displays time series data in a tabular format.  
`collapsibleGroup` |  `object (`[CollapsibleGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#CollapsibleGroup)`)` A widget that groups the other widgets. All widgets that are within the area spanned by the grouping widget are considered member widgets.  
`logsPanel` |  `object (`[LogsPanel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#LogsPanel)`)` A widget that shows a stream of logs.  
`incidentList` |  `object (`[IncidentList](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#IncidentList)`)` A widget that shows list of incidents.  
`pieChart` |  `object (`[PieChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PieChart)`)` A widget that displays timeseries data as a pie chart.  
`treemap` |  `object (`[Treemap](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Treemap)`)` A widget that displays data as a treemap.  
`errorReportingPanel` |  `object (`[ErrorReportingPanel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ErrorReportingPanel)`)` A widget that displays a list of error groups.  
`sectionHeader` |  `object (`[SectionHeader](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SectionHeader)`)` A widget that defines a section header for easier navigation of the dashboard.  
`singleViewGroup` |  `object (`[SingleViewGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SingleViewGroup)`)` A widget that groups the other widgets by using a dropdown menu.  
`filterControl` |  `object (`[FilterControl](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#FilterControl)`)` A widget that displays an input field to change the value of a template variable.  
End of mutually exclusive fields.  
  
## XyChart

A chart that displays data on a 2D (X and Y axes) plane.

JSON representation  
---  
      
    
    {
      "dataSets": [
        {
          object ([DataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DataSet))
        }
      ],
      "timeshiftDuration": string,
      "thresholds": [
        {
          object ([Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Threshold))
        }
      ],
      "xAxis": {
        object ([Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Axis))
      },
      "yAxis": {
        object ([Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Axis))
      },
      "y2Axis": {
        object ([Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Axis))
      },
      "chartOptions": {
        object ([ChartOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ChartOptions))
      }
    }  
  
Fields  
---  
`dataSets[]` |  `object (`[DataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DataSet)`)` Required. The data displayed in this chart.  
`timeshiftDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration used to display a comparison chart. A comparison chart simultaneously shows values from two similar-length time periods (e.g., week-over-week metrics). The duration must be positive, and it can only be applied to charts with data sets of LINE plot type.  
`thresholds[]` |  `object (`[Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Threshold)`)` Threshold lines drawn horizontally across the chart.  
`xAxis` |  `object (`[Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Axis)`)` The properties applied to the x-axis.  
`yAxis` |  `object (`[Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Axis)`)` The properties applied to the y-axis.  
`y2Axis` |  `object (`[Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Axis)`)` The properties applied to the y2-axis.  
`chartOptions` |  `object (`[ChartOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ChartOptions)`)` Display options for the chart.  
  
## DataSet

Groups a time series query definition with charting options.

JSON representation  
---  
      
    
    {
      "timeSeriesQuery": {
        object ([TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery))
      },
      "plotType": enum ([PlotType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PlotType)),
      "legendTemplate": string,
      "minAlignmentPeriod": string,
      "targetAxis": enum ([TargetAxis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TargetAxis)),
      "dimensions": [
        {
          object ([Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dimension))
        }
      ],
      "measures": [
        {
          object ([Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Measure))
        }
      ],
      "breakdowns": [
        {
          object ([Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Breakdown))
        }
      ],
      "sort": [
        {
          object ([ColumnSortingOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ColumnSortingOptions))
        }
      ]
    }  
  
Fields  
---  
`timeSeriesQuery` |  `object (`[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery)`)` Required. Fields for querying time series data from the Stackdriver metrics API.  
`plotType` |  `enum (`[PlotType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PlotType)`)` How this data should be plotted on the chart.  
`legendTemplate` |  `string` A template string for naming `TimeSeries` in the resulting data set. This should be a string with interpolations of the form `${label_name}`, which will resolve to the label's value.  
`minAlignmentPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes, the `minAlignmentPeriod` should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.For PromQL queries, this field is used to set the minimum interval for the query `step`, controlling data granularity. Larger values can improve performance on long time ranges. See [Querying Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/) and [Range Queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries) for more details on the PromQL `step`.  
`targetAxis` |  `enum (`[TargetAxis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TargetAxis)`)` Optional. The target axis to use for plotting the metric.  
`dimensions[]` |  `object (`[Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dimension)`)` Optional. A collection of dimension columns.  
`measures[]` |  `object (`[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Measure)`)` Optional. A collection of measures.  
`breakdowns[]` |  `object (`[Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Breakdown)`)` Optional. The collection of breakdowns to be applied to the dataset.  
`sort[]` |  `object (`[ColumnSortingOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ColumnSortingOptions)`)` Optional. A collection of sort options, affects the order of the data and legend.  
  
## TimeSeriesQuery

TimeSeriesQuery collects the set of supported methods for querying time series data from the Stackdriver metrics API.

JSON representation  
---  
      
    
    {
      "unitOverride": string,
      "outputFullDuration": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "timeSeriesFilter": {
        object ([TimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesFilter))
      },
      "timeSeriesFilterRatio": {
        object ([TimeSeriesFilterRatio](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesFilterRatio))
      },
      "timeSeriesQueryLanguage": string,
      "prometheusQuery": string,
      "opsAnalyticsQuery": {
        object ([OpsAnalyticsQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#OpsAnalyticsQuery))
      },
      "traceQuery": {
        object ([TraceQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TraceQuery))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`unitOverride` |  `string` The unit of data contained in fetched time series. If non-empty, this unit will override any unit that accompanies fetched data. The format is the same as the [`unit`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors) field in `MetricDescriptor`.  
`outputFullDuration` |  `boolean` Optional. If set, Cloud Monitoring will treat the full query duration as the alignment period so that there will be only 1 output value.*Note: This could override the configured alignment period except for the cases where a series of data points are expected, like - XyChart - Scorecard's spark chart  
Parameters needed to obtain data for the chart. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`timeSeriesFilter` |  `object (`[TimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesFilter)`)` Filter parameters to fetch time series.  
`timeSeriesFilterRatio` |  `object (`[TimeSeriesFilterRatio](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesFilterRatio)`)` Parameters to fetch a ratio between two time series filters.  
`timeSeriesQueryLanguage` |  `string` A query used to fetch time series with MQL.  
`prometheusQuery` |  `string` A query used to fetch time series with PromQL.  
`opsAnalyticsQuery` |  `object (`[OpsAnalyticsQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#OpsAnalyticsQuery)`)` Preview: A query used to fetch a time series, category series, or numeric series with SQL. This is a preview feature and may be subject to change before final release.  
`traceQuery` |  `object (`[TraceQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TraceQuery)`)` Optional. Preview: Query for traces. This is a preview feature and may be subject to change before final release.  
End of mutually exclusive fields.  
  
## TimeSeriesFilter

A filter that defines a subset of time series data that is displayed in a widget. Time series data is fetched using the [`timeSeries.list`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.

JSON representation  
---  
      
    
    {
      "filter": string,
      "aggregation": {
        object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aggregation))
      },
      "secondaryAggregation": {
        object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aggregation))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "pickTimeSeriesFilter": {
        object ([PickTimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PickTimeSeriesFilter))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`filter` |  `string` Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.  
`aggregation` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aggregation)`)` By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.  
`secondaryAggregation` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aggregation)`)` Apply a second aggregation after `aggregation` is applied.  
Selects an optional time series filter. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`pickTimeSeriesFilter` |  `object (`[PickTimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PickTimeSeriesFilter)`)` Ranking based time series filter.  
End of mutually exclusive fields.  
  
## Aggregation

Describes how to combine multiple time series to provide a different view of the data. Aggregation of time series is done in two steps. First, each time series in the set is _aligned_ to the same time interval boundaries, then the set of time series is optionally _reduced_ in number.

Alignment consists of applying the `perSeriesAligner` operation to each time series after its data has been divided into regular `alignmentPeriod` time intervals. This process takes _all_ of the data points in an alignment period, applies a mathematical transformation such as averaging, minimum, maximum, delta, etc., and converts them into a single data point per period.

Reduction is when the aligned and transformed time series can optionally be combined, reducing the number of time series through similar mathematical transformations. Reduction involves applying a `crossSeriesReducer` to all the time series, optionally sorting the time series into subsets with `groupByFields`, and applying the reducer to each subset.

The raw time series data can contain a huge amount of information from multiple sources. Alignment and reduction transforms this mass of data into a more manageable and representative collection of data, for example "the 95% latency across the average of all tasks in a cluster". This representative data can be more easily graphed and comprehended, and the individual time series data is still available for later drilldown. For more details, see [Filtering and aggregation](https://cloud.google.com/monitoring/api/v3/aggregation).

JSON representation  
---  
      
    
    {
      "alignmentPeriod": string,
      "perSeriesAligner": enum ([Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aligner)),
      "crossSeriesReducer": enum ([Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Reducer)),
      "groupByFields": [
        string
      ]
    }  
  
Fields  
---  
`alignmentPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The `alignmentPeriod` specifies a time interval, in seconds, that is used to divide the data in all the `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries)` into consistent blocks of time. This will be done before the per-series aligner can be applied to the data.The value must be at least 60 seconds. If a per-series aligner other than `ALIGN_NONE` is specified, this field is required or an error is returned. If no per-series aligner is specified, or the aligner `ALIGN_NONE` is specified, then this field is ignored.The maximum value of the `alignmentPeriod` is 2 years, or 104 weeks.  
`perSeriesAligner` |  `enum (`[Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aligner)`)` An `Aligner` describes how to bring the data points in a single time series into temporal alignment. Except for `ALIGN_NONE`, all alignments cause all the data points in an `alignmentPeriod` to be mathematically grouped together, resulting in a single data point for each `alignmentPeriod` with end timestamp at the end of the period.Not all alignment operations may be applied to all time series. The valid choices depend on the `metricKind` and `valueType` of the original time series. Alignment can change the `metricKind` or the `valueType` of the time series.Time series data must be aligned in order to perform cross-time series reduction. If `crossSeriesReducer` is specified, then `perSeriesAligner` must be specified and not equal to `ALIGN_NONE` and `alignmentPeriod` must be specified; otherwise, an error is returned.  
`crossSeriesReducer` |  `enum (`[Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Reducer)`)` The reduction operation to be used to combine time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.Not all reducer operations can be applied to all time series. The valid choices depend on the `metricKind` and the `valueType` of the original time series. Reduction can yield a time series with a different `metricKind` or `valueType` than the input time series.Time series data must first be aligned (see `perSeriesAligner`) in order to perform cross-time series reduction. If `crossSeriesReducer` is specified, then `perSeriesAligner` must be specified, and must not be `ALIGN_NONE`. An `alignmentPeriod` must also be specified; otherwise, an error is returned.  
`groupByFields[]` |  `string` The set of fields to preserve when `crossSeriesReducer` is specified. The `groupByFields` determine how the time series are partitioned into subsets prior to applying the aggregation operation. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The `crossSeriesReducer` is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains `resource.type`. Fields not specified in `groupByFields` are aggregated away. If `groupByFields` is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If `crossSeriesReducer` is not defined, this field is ignored.  
  
## Aligner

The `Aligner` specifies the operation that will be applied to the data points in each alignment period in a time series. Except for `ALIGN_NONE`, which specifies that no operation be applied, each alignment operation replaces the set of data values in each alignment period with a single value: the result of applying the operation to the data values. An aligned time series has a single data value at the end of each `alignmentPeriod`.

An alignment operation can change the data type of the values, too. For example, if you apply a counting operation to boolean values, the data `valueType` in the original time series is `BOOLEAN`, but the `valueType` in the aligned result is `INT64`.

Enums  
---  
`ALIGN_NONE` | No alignment. Raw data is returned. Not valid if cross-series reduction is requested. The `valueType` of the result is the same as the `valueType` of the input.  
`ALIGN_DELTA` | Align and convert to `[DELTA](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind.ENUM_VALUES.DELTA)`. The output is `delta = y1 - y0`.This alignment is valid for `[CUMULATIVE](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind.ENUM_VALUES.CUMULATIVE)` and `DELTA` metrics. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_RATE` | Align and convert to a rate. The result is computed as `rate = (y1 - y0)/(t1 - t0)`, or "delta over time". Think of this aligner as providing the slope of the line that passes through the value at the start and at the end of the `alignmentPeriod`.This aligner is valid for `CUMULATIVE` and `DELTA` metrics with numeric values. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The output is a `GAUGE` metric with `valueType` `DOUBLE`.If, by "rate", you mean "percentage change", see the `ALIGN_PERCENT_CHANGE` aligner instead.  
`ALIGN_INTERPOLATE` | Align by interpolating between adjacent points around the alignment period boundary. This aligner is valid for `GAUGE` metrics with numeric values. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_NEXT_OLDER` | Align by moving the most recent data point before the end of the alignment period to the boundary at the end of the alignment period. This aligner is valid for `GAUGE` metrics. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_MIN` | Align the time series by returning the minimum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_MAX` | Align the time series by returning the maximum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_MEAN` | Align the time series by returning the mean value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `valueType` of the aligned result is `DOUBLE`.  
`ALIGN_COUNT` | Align the time series by returning the number of values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric or Boolean values. The `valueType` of the aligned result is `INT64`.  
`ALIGN_SUM` | Align the time series by returning the sum of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric and distribution values. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_STDDEV` | Align the time series by returning the standard deviation of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `valueType` of the output is `DOUBLE`.  
`ALIGN_COUNT_TRUE` | Align the time series by returning the number of `True` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `valueType` of the output is `INT64`.  
`ALIGN_COUNT_FALSE` | Align the time series by returning the number of `False` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `valueType` of the output is `INT64`.  
`ALIGN_FRACTION_TRUE` | Align the time series by returning the ratio of the number of `True` values to the total number of values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The output value is in the range [0.0, 1.0] and has `valueType` `DOUBLE`.  
`ALIGN_PERCENTILE_99` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 99th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
`ALIGN_PERCENTILE_95` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 95th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
`ALIGN_PERCENTILE_50` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 50th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
`ALIGN_PERCENTILE_05` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 5th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
`ALIGN_PERCENT_CHANGE` | Align and convert to a percentage change. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. This alignment returns `((current - previous)/previous) * 100`, where the value of `previous` is determined based on the `alignmentPeriod`.If the values of `current` and `previous` are both 0, then the returned value is 0. If only `previous` is 0, the returned value is infinity.A 10-minute moving mean is computed at each point of the alignment period prior to the above calculation to smooth the metric and prevent false positives from very short-lived spikes. The moving mean is only applicable for data whose values are `>= 0`. Any values `< 0` are treated as a missing datapoint, and are ignored. While `DELTA` metrics are accepted by this alignment, special care should be taken that the values for the metric will always be positive. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
  
## Reducer

A Reducer operation describes how to aggregate data points from multiple time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.

Enums  
---  
`REDUCE_NONE` | No cross-time series reduction. The output of the `Aligner` is returned.  
`REDUCE_MEAN` | Reduce by computing the mean value across time series for each alignment period. This reducer is valid for `[DELTA](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind.ENUM_VALUES.DELTA)` and `[GAUGE](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind.ENUM_VALUES.GAUGE)` metrics with numeric or distribution values. The `valueType` of the output is `[DOUBLE](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType.ENUM_VALUES.DOUBLE)`.  
`REDUCE_MIN` | Reduce by computing the minimum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `valueType` of the output is the same as the `valueType` of the input.  
`REDUCE_MAX` | Reduce by computing the maximum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `valueType` of the output is the same as the `valueType` of the input.  
`REDUCE_SUM` | Reduce by computing the sum across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric and distribution values. The `valueType` of the output is the same as the `valueType` of the input.  
`REDUCE_STDDEV` | Reduce by computing the standard deviation across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric or distribution values. The `valueType` of the output is `DOUBLE`.  
`REDUCE_COUNT` | Reduce by computing the number of data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of numeric, Boolean, distribution, and string `valueType`. The `valueType` of the output is `INT64`.  
`REDUCE_COUNT_TRUE` | Reduce by computing the number of `True`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `valueType`. The `valueType` of the output is `INT64`.  
`REDUCE_COUNT_FALSE` | Reduce by computing the number of `False`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `valueType`. The `valueType` of the output is `INT64`.  
`REDUCE_FRACTION_TRUE` | Reduce by computing the ratio of the number of `True`-valued data points to the total number of data points for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `valueType`. The output value is in the range [0.0, 1.0] and has `valueType` `DOUBLE`.  
`REDUCE_PERCENTILE_99` | Reduce by computing the [99th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_95` | Reduce by computing the [95th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_50` | Reduce by computing the [50th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_05` | Reduce by computing the [5th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
  
## PickTimeSeriesFilter

Describes a ranking-based time series filter. Each input time series is ranked with an aligner. The filter will allow up to `numTimeSeries` time series to pass through it, selecting them based on the relative ranking.

For example, if `rankingMethod` is `METHOD_MEAN`,`direction` is `BOTTOM`, and `numTimeSeries` is 3, then the 3 times series with the lowest mean values will pass through the filter.

JSON representation  
---  
      
    
    {
      "rankingMethod": enum ([Method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Method)),
      "numTimeSeries": integer,
      "direction": enum ([Direction](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Direction)),
      "interval": {
        object ([Interval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Interval))
      }
    }  
  
Fields  
---  
`rankingMethod` |  `enum (`[Method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Method)`)` `rankingMethod` is applied to each time series independently to produce the value which will be used to compare the time series to other time series.  
`numTimeSeries` |  `integer` How many time series to allow to pass through the filter.  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Direction)`)` How to use the ranking to select time series that pass through the filter.  
`interval` |  `object (`[Interval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Interval)`)` Select the top N streams/time series within this time interval  
  
## Method

The value reducers that can be applied to a `PickTimeSeriesFilter`.

Enums  
---  
`METHOD_UNSPECIFIED` | Not allowed. You must specify a different `Method` if you specify a `PickTimeSeriesFilter`.  
`METHOD_MEAN` | Select the mean of all values.  
`METHOD_MAX` | Select the maximum value.  
`METHOD_MIN` | Select the minimum value.  
`METHOD_SUM` | Compute the sum of all values.  
`METHOD_LATEST` | Select the most recent value.  
  
## Direction

Describes the ranking directions.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Not allowed. You must specify a different `Direction` if you specify a `PickTimeSeriesFilter`.  
`TOP` | Pass the highest `numTimeSeries` ranking inputs.  
`BOTTOM` | Pass the lowest `numTimeSeries` ranking inputs.  
  
## Interval

Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive).

The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Inclusive start of the interval.If specified, a Timestamp matching this interval will have to be the same or after the start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Exclusive end of the interval.If specified, a Timestamp matching this interval will have to be before the end.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## TimeSeriesFilterRatio

A pair of time series filters that define a ratio computation. The output time series is the pair-wise division of each aligned element from the numerator and denominator time series.

JSON representation  
---  
      
    
    {
      "numerator": {
        object ([RatioPart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#RatioPart))
      },
      "denominator": {
        object ([RatioPart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#RatioPart))
      },
      "secondaryAggregation": {
        object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aggregation))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "pickTimeSeriesFilter": {
        object ([PickTimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PickTimeSeriesFilter))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`numerator` |  `object (`[RatioPart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#RatioPart)`)` The numerator of the ratio.  
`denominator` |  `object (`[RatioPart](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#RatioPart)`)` The denominator of the ratio.  
`secondaryAggregation` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aggregation)`)` Apply a second aggregation after the ratio is computed.  
Selects an optional filter that is applied to the time series after computing the ratio. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`pickTimeSeriesFilter` |  `object (`[PickTimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PickTimeSeriesFilter)`)` Ranking based time series filter.  
End of mutually exclusive fields.  
  
## RatioPart

Describes a query to build the numerator or denominator of a TimeSeriesFilterRatio.

JSON representation  
---  
      
    
    {
      "filter": string,
      "aggregation": {
        object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aggregation))
      }
    }  
  
Fields  
---  
`filter` |  `string` Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.  
`aggregation` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Aggregation)`)` By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.  
  
## OpsAnalyticsQuery

Preview: A query that produces an aggregated response and supporting data. This is a preview feature and may be subject to change before final release.

JSON representation  
---  
      
    
    {
      "sql": string
    }  
  
Fields  
---  
`sql` |  `string` A SQL query to fetch time series, category series, or numeric series data.  
  
## TraceQuery

LINT.IfChange Preview: Query for traces. This is a preview feature and may be subject to change before final release.

JSON representation  
---  
      
    
    {
      "spanDataValue": enum ([SpanDataValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SpanDataValue)),
      "spanFilters": {
        object ([SpanFilters](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SpanFilters))
      },
      "resourceContainer": string
    }  
  
Fields  
---  
`spanDataValue` |  `enum (`[SpanDataValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SpanDataValue)`)` The type of span data value to be displayed on the chart. Required.  
`spanFilters` |  `object (`[SpanFilters](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SpanFilters)`)` First version of span filtering that we will support. Required.  
`resourceContainer` |  `string` Optional. The resource name of the project or Trace scope to fetch data from. If empty, the widget will default to the project's default Trace scope. If scope cannot be determined, then we fallback to the current project. Optional.  
  
## SpanDataValue

List of different span data values that is used to determine the data displayed on the chart

Enums  
---  
`SPAN_DATA_VALUE_UNSPECIFIED` | We are required to have an UNSPECIFIED value for enums. This should not be used in practice.  
`SPAN_COUNT` | Span count data value  
`SPAN_DURATION` | Span duration data value  
`SPAN_DURATION_PERCENTILES` | Span duration percentiles data value  
  
## SpanFilters

First version of span filtering that is supported by the Trace component.

JSON representation  
---  
      
    
    {
      "services": [
        string
      ],
      "displayNames": [
        string
      ],
      "status": [
        string
      ],
      "kinds": [
        string
      ],
      "minDuration": string,
      "maxDuration": string,
      "attributes": [
        {
          object ([SpanAttributeFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SpanAttributeFilter))
        }
      ],
      "isRootSpan": boolean,
      "applicationIds": [
        string
      ],
      "apphubServices": [
        string
      ],
      "apphubWorkloads": [
        string
      ]
    }  
  
Fields  
---  
`services[]` |  `string` Optional. Filtering for spans containing one of the services in the list. Multiple values will be OR'd together.  
`displayNames[]` |  `string` Optional. Filtering for spans containing one of the span display names in the list. Multiple values will be OR'd together.  
`status[]` |  `string` Optional. Filtering for spans containing one of the statuses in the list. Multiple values will be OR'd together.  
`kinds[]` |  `string` Optional. Filtering for spans containing one of the kinds in the list. Multiple values will be OR'd together.  
`minDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Filtering for spans with a minimum duration.  
`maxDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Filtering for spans with a maximum duration.  
`attributes[]` |  `object (`[SpanAttributeFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SpanAttributeFilter)`)` Optional. List of span attribute filters. Each SpanAttributeFilter key must be unique. Multiple attribute filters will be AND'd together.  
`isRootSpan` |  `boolean` Optional. Filters for root spans only if set to true. A root span is a span without a defined parent span ID.  
`applicationIds[]` |  `string` Optional. Filtering for spans containing one of the Apphub Application IDs in the list. Multiple values will be OR'd together.  
`apphubServices[]` |  `string` Optional. Filtering for spans containing one of the Apphub service IDs in the list. Multiple values will be OR'd together. Example: ["service-id1", "service-id2"]  
`apphubWorkloads[]` |  `string` Optional. Filtering for spans containing one of the Apphub workload IDs in the list. Multiple values will be OR'd together. Example: ["workload-id1", "workload-id2"]  
  
## SpanAttributeFilter

Span attribute key and list of values to be used for filtering.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": [
        string
      ]
    }  
  
Fields  
---  
`key` |  `string` Key of the attribute  
`value[]` |  `string` List of attribute values for given key. Multiple values will be OR'd together.  
  
## PlotType

The types of plotting strategies for data sets.

Enums  
---  
`PLOT_TYPE_UNSPECIFIED` | Plot type is unspecified. The view will default to `LINE`.  
`LINE` | The data is plotted as a set of lines (one line per series).  
`STACKED_AREA` | The data is plotted as a set of filled areas (one area per series), with the areas stacked vertically (the base of each area is the top of its predecessor, and the base of the first area is the x-axis). Since the areas do not overlap, each is filled with a different opaque color.  
`STACKED_BAR` | The data is plotted as a set of rectangular boxes (one box per series), with the boxes stacked vertically (the base of each box is the top of its predecessor, and the base of the first box is the x-axis). Since the boxes do not overlap, each is filled with a different opaque color.  
`HEATMAP` | The data is plotted as a heatmap. The series being plotted must have a `DISTRIBUTION` value type. The value of each bucket in the distribution is displayed as a color. This type is not currently available in the Stackdriver Monitoring application.  
  
## TargetAxis

An axis identifier.

Enums  
---  
`TARGET_AXIS_UNSPECIFIED` | The target axis was not specified. Defaults to Y1.  
`Y1` | The yAxis (the right axis of chart).  
`Y2` | The y2Axis (the left axis of chart).  
  
## Dimension

A chart dimension. Dimensions are a structured label, class, or category for a set of measurements in your data.

JSON representation  
---  
      
    
    {
      "column": string,
      "columnType": string,
      "maxBinCount": integer,
      "sortOrder": enum ([SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SortOrder)),
      "sortColumn": string,
      "xMin": number,
      "xMax": number,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "timeBinSize": string,
      "numericBinSize": integer,
      "floatBinSize": number
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`column` |  `string` Required. For widgets that use SQL queries, set the value to the name of the column in the results table whose data is charted. For a histogram that uses a time series query, set the value of this field to `metric_value`.  
`columnType` |  `string` Optional. The type of the dimension column. This is relevant only if one of the bin_size fields is set. If it is empty, the type TIMESTAMP or INT64 will be assumed based on which bin_size field is set. If populated, this should be set to one of the following types: DATE, TIME, DATETIME, TIMESTAMP, BIGNUMERIC, INT64, NUMERIC, FLOAT64.  
`maxBinCount` |  `integer` For widgets that use SQL queries, the limit to the number of bins to generate. When 0 is specified, the maximum count is not enforced. For a histogram that uses a time series query, the exact number of bins to generate. If not specified or the value is 0, then the histogram determines the number of bins to use.  
`sortOrder` |  `enum (`[SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SortOrder)`)` The sort order applied to the sort column.  
`sortColumn` |  `string` The column name to sort on for binning. This column can be the same column as this dimension or any other column used as a measure in the results. If `sortOrder` is set to `NONE`, then this value is not used.  
`xMin` |  `number` The minimum value for the x-axis.  
`xMax` |  `number` The maximum value for the x-axis.  
The values of `bin_size` are used to configure the grouping of points for the dimension specified by the `column` field. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`timeBinSize` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` `timeBinSize` is used when the data type of the specified dimension is a time type and the bin size is determined by a time duration. If `columnType` is `DATE`, this must be a whole value multiple of 1 day. If `columnType` is `TIME`, this must be less than or equal to 24 hours.  
`numericBinSize` |  `integer` `numericBinSize` is used when the column type used for a dimension is numeric or string. If the `column` field is set to `metric_value`, then `numericBinSize` overrides `maxBinCount`.  
`floatBinSize` |  `number` Optional. `floatBinSize` is used when the column type used for a dimension is a floating point numeric column.  
End of mutually exclusive fields.  
  
## SortOrder

Sort order options.

Enums  
---  
`SORT_ORDER_UNSPECIFIED` | An unspecified sort order. This option is invalid when sorting is required.  
`SORT_ORDER_NONE` | No sorting is applied.  
`SORT_ORDER_ASCENDING` | The lowest-valued entries are selected first.  
`SORT_ORDER_DESCENDING` | The highest-valued entries are selected first.  
  
## Measure

A chart measure. Measures represent a measured property in your chart data such as rainfall in inches, number of units sold, revenue gained, etc.

JSON representation  
---  
      
    
    {
      "column": string,
      "aggregationFunction": {
        object ([AggregationFunction](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#AggregationFunction))
      }
    }  
  
Fields  
---  
`column` |  `string` Required. The column name within in the dataset used for the measure.  
`aggregationFunction` |  `object (`[AggregationFunction](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#AggregationFunction)`)` Required. The aggregation function applied to the input column. This must not be set to `"none"` unless binning is disabled on the dimension. The aggregation function is used to group points on the dimension bins.  
  
## AggregationFunction

Preview: An identifier for an aggregation function. Aggregation functions are SQL functions that group or transform data from multiple points to a single point. This is a preview feature and may be subject to change before final release.

JSON representation  
---  
      
    
    {
      "type": string,
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Parameter))
        }
      ]
    }  
  
Fields  
---  
`type` |  `string` Required. The type of aggregation function, must be one of the following:

  * "none" - no function.
  * "percentile" - APPROX_QUANTILES() - 1 parameter numeric value
  * "average" - AVG()
  * "count" - COUNT()
  * "count-distinct" - COUNT(DISTINCT)
  * "count-distinct-approx" - APPROX_COUNT_DISTINCT()
  * "max" - MAX()
  * "min" - MIN()
  * "sum" - SUM()

  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Parameter)`)` Optional. Parameters applied to the aggregation function. Only used for functions that require them.  
  
## Parameter

Preview: Parameter value applied to the aggregation function. This is a preview feature and may be subject to change before final release.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "intValue": string,
      "doubleValue": number
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Parameter value. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`intValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` An integer parameter value.  
`doubleValue` |  `number` A floating-point parameter value.  
End of mutually exclusive fields.  
  
## Breakdown

Preview: A breakdown is an aggregation applied to the measures over a specified column. A breakdown can result in multiple series across a category for the provided measure. This is a preview feature and may be subject to change before final release.

JSON representation  
---  
      
    
    {
      "column": string,
      "limit": integer,
      "aggregationFunction": {
        object ([AggregationFunction](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#AggregationFunction))
      },
      "sortOrder": enum ([SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SortOrder))
    }  
  
Fields  
---  
`column` |  `string` Required. The name of the column in the dataset containing the breakdown values.  
`limit` |  `integer` Required. A limit to the number of breakdowns. If set to zero then all possible breakdowns are applied. The list of breakdowns is dependent on the value of the `sortOrder` field.  
`aggregationFunction` |  `object (`[AggregationFunction](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#AggregationFunction)`)` Required. The Aggregation function is applied across all data in each breakdown created.  
`sortOrder` |  `enum (`[SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SortOrder)`)` Required. The sort order is applied to the values of the breakdown column.  
  
## ColumnSortingOptions

Data structure to storing column's sort strategy

JSON representation  
---  
      
    
    {
      "column": string,
      "direction": enum ([SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SortOrder))
    }  
  
Fields  
---  
`column` |  `string` Optional. Column name to sort data by  
`direction` |  `enum (`[SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SortOrder)`)` Optional. A sorting direction that determines ascending or descending order. This is a legacy field kept for backwards compatibility with table.  
  
## Threshold

Defines a threshold for categorizing time series values.

JSON representation  
---  
      
    
    {
      "label": string,
      "value": number,
      "color": enum ([Color](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Color)),
      "direction": enum ([Direction](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Direction_1)),
      "targetAxis": enum ([TargetAxis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TargetAxis_1))
    }  
  
Fields  
---  
`label` |  `string` A label for the threshold.  
`value` |  `number` The value of the threshold. The value should be defined in the native scale of the metric.  
`color` |  `enum (`[Color](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Color)`)` The state color for this threshold. Color is not allowed in a XyChart.  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Direction_1)`)` The direction for the current threshold. Direction is not allowed in a XyChart.  
`targetAxis` |  `enum (`[TargetAxis](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TargetAxis_1)`)` The target axis to use for plotting the threshold. Target axis is not allowed in a Scorecard.  
  
## Color

The color suggests an interpretation to the viewer when actual values cross the threshold. Comments on each color provide UX guidance on how users can be expected to interpret a given state color.

Enums  
---  
`COLOR_UNSPECIFIED` | Color is unspecified. Not allowed in well-formed requests.  
`YELLOW` | Crossing the threshold is "concerning" behavior.  
`RED` | Crossing the threshold is "emergency" behavior.  
  
## Direction

Whether the threshold is considered crossed by an actual value above or below its threshold value.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Not allowed in well-formed requests.  
`ABOVE` | The threshold will be considered crossed if the actual value is above the threshold value.  
`BELOW` | The threshold will be considered crossed if the actual value is below the threshold value.  
  
## TargetAxis

An axis identifier.

Enums  
---  
`TARGET_AXIS_UNSPECIFIED` | The target axis was not specified. Defaults to Y1.  
`Y1` | The yAxis (the right axis of chart).  
`Y2` | The y2Axis (the left axis of chart).  
  
## Axis

A chart axis.

JSON representation  
---  
      
    
    {
      "label": string,
      "scale": enum ([Scale](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Scale))
    }  
  
Fields  
---  
`label` |  `string` The label of the axis.  
`scale` |  `enum (`[Scale](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Scale)`)` The axis scale. By default, a linear scale is used.  
  
## Scale

Types of scales used in axes.

Enums  
---  
`SCALE_UNSPECIFIED` | Scale is unspecified. The view will default to `LINEAR`.  
`LINEAR` | Linear scale.  
`LOG10` | Logarithmic scale (base 10).  
  
## ChartOptions

Options to control visual rendering of a chart.

JSON representation  
---  
      
    
    {
      "mode": enum ([Mode](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Mode)),
      "displayHorizontal": boolean
    }  
  
Fields  
---  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Mode)`)` The chart mode.  
`displayHorizontal` |  `boolean` Preview: Configures whether the charted values are shown on the horizontal or vertical axis. By default, values are represented the vertical axis. This is a preview feature and may be subject to change before final release.  
  
## Mode

Chart mode options.

Enums  
---  
`MODE_UNSPECIFIED` | Mode is unspecified. The view will default to `COLOR`.  
`COLOR` | The chart distinguishes data series using different color. Line colors may get reused when there are many lines in the chart.  
`X_RAY` | The chart uses the Stackdriver x-ray mode, in which each data set is plotted using the same semi-transparent color.  
`STATS` | The chart displays statistics such as average, median, 95th percentile, and more.  
  
## Scorecard

A widget showing the latest value of a metric, and how this value relates to one or more thresholds.

JSON representation  
---  
      
    
    {
      "timeSeriesQuery": {
        object ([TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery))
      },
      "thresholds": [
        {
          object ([Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Threshold))
        }
      ],
      "dimensions": [
        {
          object ([Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dimension))
        }
      ],
      "measures": [
        {
          object ([Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Measure))
        }
      ],
      "breakdowns": [
        {
          object ([Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Breakdown))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "gaugeView": {
        object ([GaugeView](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#GaugeView))
      },
      "sparkChartView": {
        object ([SparkChartView](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SparkChartView))
      },
      "blankView": {
        object
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`timeSeriesQuery` |  `object (`[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery)`)` Required. Fields for querying time series data from the Stackdriver metrics API.  
`thresholds[]` |  `object (`[Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Threshold)`)` The thresholds used to determine the state of the scorecard given the time series' current value. For an actual value x, the scorecard is in a danger state if x is less than or equal to a danger threshold that triggers below, or greater than or equal to a danger threshold that triggers above. Similarly, if x is above/below a warning threshold that triggers above/below, then the scorecard is in a warning state - unless x also puts it in a danger state. (Danger trumps warning.)As an example, consider a scorecard with the following four thresholds:
    
    
    {
      value: 90,
      category: 'DANGER',
      trigger: 'ABOVE',
    },
    {
      value: 70,
      category: 'WARNING',
      trigger: 'ABOVE',
    },
    {
      value: 10,
      category: 'DANGER',
      trigger: 'BELOW',
    },
    {
      value: 20,
      category: 'WARNING',
      trigger: 'BELOW',
    }
    

Then: values less than or equal to 10 would put the scorecard in a DANGER state, values greater than 10 but less than or equal to 20 a WARNING state, values strictly between 20 and 70 an OK state, values greater than or equal to 70 but less than 90 a WARNING state, and values greater than or equal to 90 a DANGER state.  
`dimensions[]` |  `object (`[Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dimension)`)` Optional. A dimension is a structured label, class, or category for a set of measurements in your data.  
`measures[]` |  `object (`[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Measure)`)` Optional. A measure is a measured value of a property in your data. For example, rainfall in inches, number of units sold, revenue gained, etc.  
`breakdowns[]` |  `object (`[Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Breakdown)`)` Optional. The collection of breakdowns to be applied to the dataset. A breakdown is a way to slice the data. For example, you can break down the data by region.  
Defines the optional additional chart shown on the scorecard. If neither is included - then a default scorecard is shown. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`gaugeView` |  `object (`[GaugeView](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#GaugeView)`)` Will cause the scorecard to show a gauge chart.  
`sparkChartView` |  `object (`[SparkChartView](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SparkChartView)`)` Will cause the scorecard to show a spark chart.  
`blankView` |  `object` Will cause the `Scorecard` to show only the value, with no indicator to its value relative to its thresholds.  
End of mutually exclusive fields.  
  
## GaugeView

A gauge chart shows where the current value sits within a pre-defined range. The upper and lower bounds should define the possible range of values for the scorecard's query (inclusive).

JSON representation  
---  
      
    
    {
      "lowerBound": number,
      "upperBound": number
    }  
  
Fields  
---  
`lowerBound` |  `number` The lower bound for this gauge chart. The value of the chart should always be greater than or equal to this.  
`upperBound` |  `number` The upper bound for this gauge chart. The value of the chart should always be less than or equal to this.  
  
## SparkChartView

A sparkChart is a small chart suitable for inclusion in a table-cell or inline in text. This message contains the configuration for a sparkChart to show up on a Scorecard, showing recent trends of the scorecard's timeseries.

JSON representation  
---  
      
    
    {
      "sparkChartType": enum ([SparkChartType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SparkChartType)),
      "minAlignmentPeriod": string
    }  
  
Fields  
---  
`sparkChartType` |  `enum (`[SparkChartType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#SparkChartType)`)` Required. The type of sparkchart to show in this chartView.  
`minAlignmentPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The lower bound on data point frequency in the chart implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes it would not make sense to fetch and align data at one minute intervals. This field is optional and exists only as a hint.For PromQL queries, this field is used to set the minimum interval for the query `step`, controlling data granularity. Larger values can improve performance on long time ranges. See [Querying Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/) and [Range Queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries) for more details on the PromQL `step`.  
  
## SparkChartType

Defines the possible types of spark chart supported by the `Scorecard`.

Enums  
---  
`SPARK_CHART_TYPE_UNSPECIFIED` | Not allowed in well-formed requests.  
`SPARK_LINE` | The sparkline will be rendered as a small line chart.  
`SPARK_BAR` | The sparkbar will be rendered as a small bar chart.  
  
## Text

A widget that displays textual content.

JSON representation  
---  
      
    
    {
      "content": string,
      "format": enum ([Format](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Format)),
      "style": {
        object ([TextStyle](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TextStyle))
      }
    }  
  
Fields  
---  
`content` |  `string` The text content to be displayed.  
`format` |  `enum (`[Format](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Format)`)` How the text content is formatted.  
`style` |  `object (`[TextStyle](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TextStyle)`)` How the text is styled  
  
## Format

The format type of the text content.

Enums  
---  
`FORMAT_UNSPECIFIED` | Format is unspecified. Defaults to MARKDOWN.  
`MARKDOWN` | The text contains Markdown formatting.  
`RAW` | The text contains no special formatting.  
  
## TextStyle

Properties that determine how the title and content are styled

JSON representation  
---  
      
    
    {
      "backgroundColor": string,
      "textColor": string,
      "horizontalAlignment": enum ([HorizontalAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#HorizontalAlignment)),
      "verticalAlignment": enum ([VerticalAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#VerticalAlignment)),
      "padding": enum ([PaddingSize](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PaddingSize)),
      "fontSize": enum ([FontSize](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#FontSize)),
      "pointerLocation": enum ([PointerLocation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PointerLocation))
    }  
  
Fields  
---  
`backgroundColor` |  `string` The background color as a hex string. "#RRGGBB" or "#RGB"  
`textColor` |  `string` The text color as a hex string. "#RRGGBB" or "#RGB"  
`horizontalAlignment` |  `enum (`[HorizontalAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#HorizontalAlignment)`)` The horizontal alignment of both the title and content  
`verticalAlignment` |  `enum (`[VerticalAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#VerticalAlignment)`)` The vertical alignment of both the title and content  
`padding` |  `enum (`[PaddingSize](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PaddingSize)`)` The amount of padding around the widget  
`fontSize` |  `enum (`[FontSize](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#FontSize)`)` Font sizes for both the title and content. The title will still be larger relative to the content.  
`pointerLocation` |  `enum (`[PointerLocation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PointerLocation)`)` The pointer location for this widget (also sometimes called a "tail")  
  
## HorizontalAlignment

The horizontal alignment of both the title and content on a text widget

Enums  
---  
`HORIZONTAL_ALIGNMENT_UNSPECIFIED` | No horizontal alignment specified, will default to H_LEFT  
`H_LEFT` | Left-align  
`H_CENTER` | Center-align  
`H_RIGHT` | Right-align  
  
## VerticalAlignment

The vertical alignment of both the title and content on a text widget

Enums  
---  
`VERTICAL_ALIGNMENT_UNSPECIFIED` | No vertical alignment specified, will default to V_TOP  
`V_TOP` | Top-align  
`V_CENTER` | Center-align  
`V_BOTTOM` | Bottom-align  
  
## PaddingSize

Specifies padding size around a text widget

Enums  
---  
`PADDING_SIZE_UNSPECIFIED` | No padding size specified, will default to P_EXTRA_SMALL  
`P_EXTRA_SMALL` | Extra small padding  
`P_SMALL` | Small padding  
`P_MEDIUM` | Medium padding  
`P_LARGE` | Large padding  
`P_EXTRA_LARGE` | Extra large padding  
  
## FontSize

Specifies a font size for the title and content of a text widget

Enums  
---  
`FONT_SIZE_UNSPECIFIED` | No font size specified, will default to FS_LARGE  
`FS_EXTRA_SMALL` | Extra small font size  
`FS_SMALL` | Small font size  
`FS_MEDIUM` | Medium font size  
`FS_LARGE` | Large font size  
`FS_EXTRA_LARGE` | Extra large font size  
  
## PointerLocation

Specifies where a visual pointer is placed on a text widget (also sometimes called a "tail")

Enums  
---  
`POINTER_LOCATION_UNSPECIFIED` | No visual pointer  
`PL_TOP` | Placed in the middle of the top of the widget  
`PL_RIGHT` | Placed in the middle of the right side of the widget  
`PL_BOTTOM` | Placed in the middle of the bottom of the widget  
`PL_LEFT` | Placed in the middle of the left side of the widget  
`PL_TOP_LEFT` | Placed on the left side of the top of the widget  
`PL_TOP_RIGHT` | Placed on the right side of the top of the widget  
`PL_RIGHT_TOP` | Placed on the top of the right side of the widget  
`PL_RIGHT_BOTTOM` | Placed on the bottom of the right side of the widget  
`PL_BOTTOM_RIGHT` | Placed on the right side of the bottom of the widget  
`PL_BOTTOM_LEFT` | Placed on the left side of the bottom of the widget  
`PL_LEFT_BOTTOM` | Placed on the bottom of the left side of the widget  
`PL_LEFT_TOP` | Placed on the top of the left side of the widget  
  
## AlertChart

A chart that displays alert policy data.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the alert policy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]
      
  
## TimeSeriesTable

A table that displays time series data.

JSON representation  
---  
      
    
    {
      "dataSets": [
        {
          object ([TableDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TableDataSet))
        }
      ],
      "metricVisualization": enum ([MetricVisualization](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#MetricVisualization)),
      "columnSettings": [
        {
          object ([ColumnSettings](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ColumnSettings))
        }
      ]
    }  
  
Fields  
---  
`dataSets[]` |  `object (`[TableDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TableDataSet)`)` Required. The data displayed in this table.  
`metricVisualization` |  `enum (`[MetricVisualization](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#MetricVisualization)`)` Optional. Store rendering strategy  
`columnSettings[]` |  `object (`[ColumnSettings](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ColumnSettings)`)` Optional. The list of the persistent column settings for the table.  
  
## TableDataSet

Groups a time series query definition with table options.

JSON representation  
---  
      
    
    {
      "timeSeriesQuery": {
        object ([TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery))
      },
      "tableTemplate": string,
      "minAlignmentPeriod": string,
      "tableDisplayOptions": {
        object ([TableDisplayOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TableDisplayOptions))
      }
    }  
  
Fields  
---  
`timeSeriesQuery` |  `object (`[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery)`)` Required. Fields for querying time series data from the Stackdriver metrics API.  
`tableTemplate` |  `string` Optional. A template string for naming `TimeSeries` in the resulting data set. This should be a string with interpolations of the form `${label_name}`, which will resolve to the label's value i.e. "${resource.labels.project_id}."  
`minAlignmentPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query For example, if the data is published once every 10 minutes, the `minAlignmentPeriod` should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.  
`tableDisplayOptions` |  `object (`[TableDisplayOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TableDisplayOptions)`)` Optional. Table display options for configuring how the table is rendered.  
  
## TableDisplayOptions

Table display options that can be reused.

JSON representation  
---  
      
    
    {
      "shownColumns": [
        string
      ]
    }  
  
Fields  
---  
`shownColumns[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. This field is unused and has been replaced by TimeSeriesTable.column_settings  
  
## MetricVisualization

Enum for metric metricVisualization

Enums  
---  
`METRIC_VISUALIZATION_UNSPECIFIED` | Unspecified state  
`NUMBER` | Default text rendering  
`BAR` | Horizontal bar rendering  
  
## ColumnSettings

The persistent settings for a table's columns.

JSON representation  
---  
      
    
    {
      "column": string,
      "visible": boolean,
      "alignment": enum ([CellAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#CellAlignment)),
      "displayName": string,
      "thresholds": [
        {
          object ([Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Threshold))
        }
      ]
    }  
  
Fields  
---  
`column` |  `string` Required. The id of the column.  
`visible` |  `boolean` Required. Whether the column should be visible on page load.  
`alignment` |  `enum (`[CellAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#CellAlignment)`)` Optional. Whether the column should be left / middle / right aligned  
`displayName` |  `string` Optional. Display name of the column  
`thresholds[]` |  `object (`[Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Threshold)`)` Optional. The thresholds used to determine how the table cell should be rendered given the time series' current value.  
  
## CellAlignment

The horizontal alignment of table cells in that column

Enums  
---  
`CELL_ALIGNMENT_UNSPECIFIED` | No horizontal alignment specified; fall back to the default behavior. Label values are left aligned. Numeric values are right aligned.  
`LEFT` | Left-align  
`CENTER` | Center-align  
`RIGHT` | Right-align  
  
## CollapsibleGroup

A widget that groups the other widgets. All widgets that are within the area spanned by the grouping widget are considered member widgets.

JSON representation  
---  
      
    
    {
      "collapsed": boolean
    }  
  
Fields  
---  
`collapsed` |  `boolean` The collapsed state of the widget on first page load.  
  
## LogsPanel

A widget that displays a stream of log.

JSON representation  
---  
      
    
    {
      "filter": string,
      "resourceNames": [
        string
      ]
    }  
  
Fields  
---  
`filter` |  `string` A filter that chooses which log entries to return. See [Advanced Logs Queries](https://cloud.google.com/logging/docs/view/advanced-queries). Only log entries that match the filter are returned. An empty filter matches all log entries.  
`resourceNames[]` |  `string` The names of logging resources to collect logs for. Currently projects and storage views are supported. If empty, the widget will default to the host project.  
  
## IncidentList

A widget that displays a list of incidents

JSON representation  
---  
      
    
    {
      "monitoredResources": [
        {
          object ([MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource))
        }
      ],
      "policyNames": [
        string
      ]
    }  
  
Fields  
---  
`monitoredResources[]` |  `object (`[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/MonitoredResource)`)` Optional. The monitored resource for which incidents are listed. The resource doesn't need to be fully specified. That is, you can specify the resource type but not the values of the resource labels. The resource type and labels are used for filtering.  
`policyNames[]` |  `string` Optional. A list of alert policy names to filter the incident list by. Don't include the project ID prefix in the policy name. For example, use `alertPolicies/utilization`.  
  
## PieChart

A widget that displays timeseries data as a pie or a donut.

JSON representation  
---  
      
    
    {
      "dataSets": [
        {
          object ([PieChartDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PieChartDataSet))
        }
      ],
      "chartType": enum ([PieChartType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PieChartType)),
      "showLabels": boolean
    }  
  
Fields  
---  
`dataSets[]` |  `object (`[PieChartDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PieChartDataSet)`)` Required. The queries for the chart's data.  
`chartType` |  `enum (`[PieChartType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#PieChartType)`)` Required. Indicates the visualization type for the PieChart.  
`showLabels` |  `boolean` Optional. Indicates whether or not the pie chart should show slices' labels  
  
## PieChartDataSet

Groups a time series query definition.

JSON representation  
---  
      
    
    {
      "timeSeriesQuery": {
        object ([TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery))
      },
      "sliceNameTemplate": string,
      "minAlignmentPeriod": string,
      "dimensions": [
        {
          object ([Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dimension))
        }
      ],
      "measures": [
        {
          object ([Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Measure))
        }
      ]
    }  
  
Fields  
---  
`timeSeriesQuery` |  `object (`[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery)`)` Required. The query for the PieChart. See, `google.monitoring.dashboard.v1.TimeSeriesQuery`.  
`sliceNameTemplate` |  `string` Optional. A template for the name of the slice. This name will be displayed in the legend and the tooltip of the pie chart. It replaces the auto-generated names for the slices. For example, if the template is set to `${resource.labels.zone}`, the zone's value will be used for the name instead of the default name.  
`minAlignmentPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes, the `minAlignmentPeriod` should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.  
`dimensions[]` |  `object (`[Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Dimension)`)` A dimension is a structured label, class, or category for a set of measurements in your data.  
`measures[]` |  `object (`[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Measure)`)` A measure is a measured value of a property in your data. For example, rainfall in inches, number of units sold, revenue gained, etc.  
  
## PieChartType

Types for the pie chart.

Enums  
---  
`PIE_CHART_TYPE_UNSPECIFIED` | The zero value. No type specified. Do not use.  
`PIE` | A Pie type PieChart.  
`DONUT` | Similar to PIE, but the DONUT type PieChart has a hole in the middle.  
  
## Treemap

A widget that displays hierarchical data as a treemap.

JSON representation  
---  
      
    
    {
      "dataSets": [
        {
          object ([TreemapDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TreemapDataSet))
        }
      ],
      "treemapHierarchy": [
        string
      ]
    }  
  
Fields  
---  
`dataSets[]` |  `object (`[TreemapDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TreemapDataSet)`)` Required. The collection of datasets used to construct and populate the treemap. For the rendered treemap rectangles:

  * Color is determined by the aggregated value for each grouping.
  * Size is proportional to the count of time series aggregated within that rectangle's segment.

  
`treemapHierarchy[]` |  `string` Required. Ordered labels representing the hierarchical treemap structure.  
  
## TreemapDataSet

The data represented by the treemap. Needs to include the data itself, plus rules on how to organize it hierarchically.

JSON representation  
---  
      
    
    {
      "timeSeriesQuery": {
        object ([TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery))
      },
      "measures": [
        {
          object ([Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Measure))
        }
      ],
      "breakdowns": [
        {
          object ([Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Breakdown))
        }
      ]
    }  
  
Fields  
---  
`timeSeriesQuery` |  `object (`[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery)`)` Required. The query that fetches the relevant data. See `google.monitoring.dashboard.v1.TimeSeriesQuery`  
`measures[]` |  `object (`[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Measure)`)` Optional. A collection of measures. A measure is a measured value of a property in your data. For example, rainfall in inches, number of units sold, revenue gained, etc.  
`breakdowns[]` |  `object (`[Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Breakdown)`)` Optional. The collection of breakdowns to be applied to the dataset. A breakdown is a way to slice the data. For example, you can break down the data by region.  
  
## ErrorReportingPanel

A widget that displays a list of error groups.

JSON representation  
---  
      
    
    {
      "projectNames": [
        string
      ],
      "services": [
        string
      ],
      "versions": [
        string
      ]
    }  
  
Fields  
---  
`projectNames[]` |  `string` The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectNumber}`, where `{projectID}` and `{projectNumber}` can be found in the [Google Cloud console](https://support.google.com/cloud/answer/6158840).Examples: `projects/my-project-123`, `projects/5551234`.  
`services[]` |  `string` An identifier of the service, such as the name of the executable, job, or Google App Engine service name. This field is expected to have a low number of values that are relatively stable over time, as opposed to `version`, which can be changed whenever new code is deployed.Contains the service name for error reports extracted from Google App Engine logs or `default` if the App Engine default service is used.  
`versions[]` |  `string` Represents the source code version that the developer provided, which could represent a version label or a Git SHA-1 hash, for example. For App Engine standard environment, the version is set to the version of the app.  
  
## SectionHeader

A widget that defines a new section header. Sections populate a table of contents and allow easier navigation of long-form content.

JSON representation  
---  
      
    
    {
      "subtitle": string,
      "dividerBelow": boolean
    }  
  
Fields  
---  
`subtitle` |  `string` The subtitle of the section  
`dividerBelow` |  `boolean` Whether to insert a divider below the section in the table of contents  
  
## SingleViewGroup

A widget that groups the other widgets by using a dropdown menu. All widgets that are within the area spanned by the grouping widget are considered member widgets.

JSON representation  
---  
      
    
    {
      "displayType": enum ([DisplayType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DisplayType))
    }  
  
Fields  
---  
`displayType` |  `enum (`[DisplayType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DisplayType)`)` Optional. Determines how the widget selector will be displayed.  
  
## DisplayType

A type indicating how the wiget selector will be displayed.

Enums  
---  
`DISPLAY_TYPE_UNSPECIFIED` | Display type is not specified, defaults to DROPDOWN.  
`DROPDOWN` | Renders the widget selector as a dropdown.  
`TAB` | Renders the widget selector as a tab list.  
  
## FilterControl

A widget that displays an input field to change the value of a template variable.

JSON representation  
---  
      
    
    {
      "templateVariable": string
    }  
  
Fields  
---  
`templateVariable` |  `string` Name of the template variable the widget affects.  
  
## VisibilityCondition

Condition that determines whether the widget should be displayed.

JSON representation  
---  
      
    
    {
      "templateVariableCondition": {
        object ([TemplateVariableCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TemplateVariableCondition))
      }
    }  
  
Fields  
---  
`templateVariableCondition` |  `object (`[TemplateVariableCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TemplateVariableCondition)`)` A condition whose evaluation is based on the value of a template variable.  
  
## TemplateVariableCondition

A condition whose evaluation is based on the value of a template variable.

JSON representation  
---  
      
    
    {
      "templateVariable": string,
      "templateVariableValue": string,
      "comparator": enum ([Comparator](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Comparator))
    }  
  
Fields  
---  
`templateVariable` |  `string` The template variable whose value is evaluated.  
`templateVariableValue` |  `string` The value to compare the template variable to. For example, if the comparator is REGEX_FULL_MATCH, this field should contain a regex.  
`comparator` |  `enum (`[Comparator](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Comparator)`)` Comparator to use to evaluate whether the value of the template variable matches the templateVariableValue. For example, if the comparator is REGEX_FULL_MATCH, templateVariableValue would contain a regex that is matched against the value of the template variable.  
  
## Comparator

Comparator options to evaluate when the template variable value matches.

Enums  
---  
`COMPARATOR_UNSPECIFIED` | No comparator specified. Behavior defaults to REGEX_FULL_MATCH.  
`REGEX_FULL_MATCH` | Condition with this comparator evaluates to true when the value of the template variables matches the specified regex.  
  
## TimeRange

Represents a time range.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "absoluteWindow": {
        object ([Interval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Interval))
      },
      "relativeDuration": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Specifies the type of time range interval. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`absoluteWindow` |  `object (`[Interval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Interval)`)` Optional. Represents a time range with absolute start and end times. The start time is inclusive, and the end time is exclusive.  
`relativeDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Specifies the duration used to shift the data relative to current time as the end time. The duration must be positive.  
End of mutually exclusive fields.  
  
## MosaicLayout

A mosaic layout divides the available space into a grid of blocks, and overlays the grid with tiles. Unlike `GridLayout`, tiles may span multiple grid blocks and can be placed at arbitrary locations in the grid.

JSON representation  
---  
      
    
    {
      "columns": integer,
      "tiles": [
        {
          object ([Tile](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Tile))
        }
      ]
    }  
  
Fields  
---  
`columns` |  `integer` The number of columns in the mosaic grid. The number of columns must be between 1 and 48, inclusive.  
`tiles[]` |  `object (`[Tile](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Tile)`)` The tiles to display.  
  
## Tile

A single tile in the mosaic. The placement and size of the tile are configurable.

JSON representation  
---  
      
    
    {
      "xPos": integer,
      "yPos": integer,
      "width": integer,
      "height": integer,
      "widget": {
        object ([Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget))
      }
    }  
  
Fields  
---  
`xPos` |  `integer` The zero-indexed position of the tile in grid blocks relative to the left edge of the grid. Tiles must be contained within the specified number of columns. `xPos` cannot be negative.  
`yPos` |  `integer` The zero-indexed position of the tile in grid blocks relative to the top edge of the grid. `yPos` cannot be negative.  
`width` |  `integer` The width of the tile, measured in grid blocks. Tiles must have a minimum width of 1.  
`height` |  `integer` The height of the tile, measured in grid blocks. Tiles must have a minimum height of 1.  
`widget` |  `object (`[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget)`)` The informational widget contained in the tile. For example an `XyChart`.  
  
## RowLayout

A simplified layout that divides the available space into rows and arranges a set of widgets horizontally in each row.

JSON representation  
---  
      
    
    {
      "rows": [
        {
          object ([Row](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Row))
        }
      ]
    }  
  
Fields  
---  
`rows[]` |  `object (`[Row](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Row)`)` The rows of content to display.  
  
## Row

Defines the layout properties and content for a row.

JSON representation  
---  
      
    
    {
      "weight": string,
      "widgets": [
        {
          object ([Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget))
        }
      ]
    }  
  
Fields  
---  
`weight` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The relative weight of this row. The row weight is used to adjust the height of rows on the screen (relative to peers). Greater the weight, greater the height of the row on the screen. If omitted, a value of 1 is used while rendering.  
`widgets[]` |  `object (`[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget)`)` The display widgets arranged horizontally in this row.  
  
## ColumnLayout

A simplified layout that divides the available space into vertical columns and arranges a set of widgets vertically in each column.

JSON representation  
---  
      
    
    {
      "columns": [
        {
          object ([Column](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Column))
        }
      ]
    }  
  
Fields  
---  
`columns[]` |  `object (`[Column](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Column)`)` The columns of content to display.  
  
## Column

Defines the layout properties and content for a column.

JSON representation  
---  
      
    
    {
      "weight": string,
      "widgets": [
        {
          object ([Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget))
        }
      ]
    }  
  
Fields  
---  
`weight` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The relative weight of this column. The column weight is used to adjust the width of columns on the screen (relative to peers). Greater the weight, greater the width of the column on the screen. If omitted, a value of 1 is used while rendering.  
`widgets[]` |  `object (`[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#Widget)`)` The display widgets arranged vertically in this column.  
  
## DashboardFilter

A filter to reduce the amount of data charted in relevant widgets.

JSON representation  
---  
      
    
    {
      "labelKey": string,
      "templateVariable": string,
      "valueType": enum ([ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ValueType)),
      "filterType": enum ([FilterType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#FilterType)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "stringValue": string,
      "stringArrayValue": {
        object ([StringArray](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#StringArray))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "timeSeriesQuery": {
        object ([TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery))
      },
      "stringArray": {
        object ([StringArray](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#StringArray))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`labelKey` |  `string` Optional. The key for the label. This must be omitted if the filterType is VALUE_ONLY but is required otherwise.  
`templateVariable` |  `string` The placeholder text that can be referenced in a filter string or MQL query. If omitted, the dashboard filter will be applied to all relevant widgets in the dashboard.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#ValueType)`)` The type of the filter value. If valueType is not provided, it will be inferred from the defaultValue. If neither valueType nor defaultValue is provided, valueType will be set to STRING by default.  
`filterType` |  `enum (`[FilterType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#FilterType)`)` The specified filter type  
The default value used in the filter comparison The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`stringValue` |  `string` A variable-length string value. If this field is set, valueType must be set to STRING or VALUE_TYPE_UNSPECIFIED  
`stringArrayValue` |  `object (`[StringArray](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#StringArray)`)` An array of variable-length string values. If this field is set, valueType must be set to STRING_ARRAY or VALUE_TYPE_UNSPECIFIED  
End of mutually exclusive fields.  
A definition of the set of valid values for the filter. This is optional but recommended for VALUE_ONLY filters. For other filter types, the set of valid values will be inferred from the charted data. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`timeSeriesQuery` |  `object (`[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#TimeSeriesQuery)`)` A query to run to fetch possible values for the filter. Only OpsAnalyticsQueries are supported  
`stringArray` |  `object (`[StringArray](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#StringArray)`)` A list of possible string values for the filter  
End of mutually exclusive fields.  
  
## ValueType

The type of the filter value

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | Value type is unspecified  
`STRING` | String type  
`STRING_ARRAY` | String array type  
  
## StringArray

An array of strings

JSON representation  
---  
      
    
    {
      "values": [
        string
      ]
    }  
  
Fields  
---  
`values[]` |  `string` The values of the array  
  
## FilterType

The type for the dashboard filter

Enums  
---  
`FILTER_TYPE_UNSPECIFIED` | Filter type is unspecified. This is not valid in a well-formed request.  
`RESOURCE_LABEL` | Filter on a resource label value  
`METRIC_LABEL` | Filter on a metrics label value  
`USER_METADATA_LABEL` | Filter on a user metadata label value  
`SYSTEM_METADATA_LABEL` | Filter on a system metadata label value  
`GROUP` | Filter on a group id  
`VALUE_ONLY` | Filter that only contains a value. The labelKey field must be unset for filters of this type.  
  
## DashboardAnnotations

Dashboard-level configuration for annotations

JSON representation  
---  
      
    
    {
      "defaultResourceNames": [
        string
      ],
      "eventAnnotations": [
        {
          object ([EventAnnotation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#EventAnnotation))
        }
      ]
    }  
  
Fields  
---  
`defaultResourceNames[]` |  `string` Dashboard level defaults for names of logging resources to search for events. Currently only projects are supported. Each individual `EventAnnotation` may have its own overrides. If both this field and the per annotation field is empty, then the scoping project is used. Limit: 50 projects. For example:
    
    
    “projects/some-project-id”
      
  
`eventAnnotations[]` |  `object (`[EventAnnotation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#EventAnnotation)`)` List of annotation configurations for this dashboard. Each entry specifies one event type.  
  
## EventAnnotation

Annotation configuration for one event type on a dashboard

JSON representation  
---  
      
    
    {
      "displayName": string,
      "eventType": enum ([EventType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#EventType)),
      "filter": string,
      "enabled": boolean,
      "resourceNames": [
        string
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Solely for UI display. Should not be used programmatically.  
`eventType` |  `enum (`[EventType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#EventType)`)` The type of event to display.  
`filter` |  `string` string filtering the events - event dependant. Example values:
    
    
    "resource.labels.pod_name = 'pod-1'"
    "protoPayload.authenticationInfo.principalEmail='user@example.com'"
      
  
`enabled` |  `boolean` Whether or not to show the events on the dashboard by default  
`resourceNames[]` |  `string` Per annotation level override for the names of logging resources to search for events. Currently only projects are supported. If both this field and the per annotation field is empty, it will default to the host project. Limit: 50 projects. For example:
    
    
    “projects/another-project-id”
      
  
## EventType

Predefined event types.

Enums  
---  
`EVENT_TYPE_UNSPECIFIED` | No event type specified.  
`GKE_WORKLOAD_DEPLOYMENT` | Patch/update of GKE workload.  
`GKE_POD_CRASH` | Crash events for a GKE Pod.  
`GKE_POD_UNSCHEDULABLE` | Scheduling failures for GKE Pods.  
`GKE_CONTAINER_CREATION_FAILED` | Failure to create a GKE container.  
`GKE_CLUSTER_CREATE_DELETE` | Create/delete of a GKE cluster.  
`GKE_CLUSTER_UPDATE` | Update of a GKE cluster.  
`GKE_NODE_POOL_UPDATE` | Update of a GKE node pool.  
`GKE_CLUSTER_AUTOSCALER` | GKE cluster autoscaler event.  
`GKE_POD_AUTOSCALER` | GKE pod autoscaler event.  
`VM_TERMINATION` | Termination of a virtual machine.  
`VM_GUEST_OS_ERROR` | Guest OS error on a virtual machine.  
`VM_START_FAILED` | Start failure on a virtual machine.  
`MIG_UPDATE` | Update of a managed instance group.  
`MIG_AUTOSCALER` | Autoscaler event for a managed instance group.  
`CLOUD_RUN_DEPLOYMENT` | New deployment of a Cloud Run service.  
`CLOUD_SQL_FAILOVER` | Failover of a Cloud SQL instance.  
`CLOUD_SQL_START_STOP` | Start/stop of a Cloud SQL instance.  
`CLOUD_SQL_STORAGE` | Storage event for a Cloud SQL instance.  
`UPTIME_CHECK_FAILURE` | Failure of a Cloud Monitoring uptime check.  
`CLOUD_ALERTING_ALERT` | Alerts from Cloud Alerting  
`SERVICE_HEALTH_INCIDENT` | Incidents from Service Health  
`SAP_BACKINT` | Agent for SAP Backint related events.  
`SAP_AVAILABILITY` | Agent for SAP availability related events.  
`SAP_OPERATIONS` | Agent for SAP operations related events.  
`INTERCONNECT_MAINTENANCE_STARTED` | Interconnect maintenance started event.  
`INTERCONNECT_MAINTENANCE_COMPLETED` | Interconnect maintenance completed event.  
`VPN_TRAFFIC_SELECTOR_NARROWING` | VPN traffic selector narrowing event.  
`VPN_MAINTENANCE` | VPN maintenance event.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/create)`

|  Creates a new custom dashboard.  
  
### `[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/delete)`

|  Deletes an existing custom dashboard.  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/get)`

|  Fetches a specific dashboard.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/list)`

|  Lists the existing dashboards.  
  
### `[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards/patch)`

|  Replaces an existing custom dashboard with a new definition.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
