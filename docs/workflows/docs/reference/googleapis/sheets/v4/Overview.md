---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview/
title: Types overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:30.432636+00:00
---

# Types overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Types overview Stay organized with collections  Save and categorize content based on your preferences. 

## AddBandingRequest

Adds a new banded range to the spreadsheet. Fields  
---  
`bandedRange` |  `object ([BandedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BandedRange))` The banded range to add. The bandedRangeId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a range that already exists.)  
  
## AddBandingResponse

The result of adding a banded range. Fields  
---  
`bandedRange` |  `object ([BandedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BandedRange))` The banded range that was added.  
  
## AddChartRequest

Adds a chart to a sheet in the spreadsheet. Fields  
---  
`chart` |  `object ([EmbeddedChart](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedChart))` The chart that should be added to the spreadsheet, including the position where it should be placed. The chartId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of an embedded object that already exists.)  
  
## AddChartResponse

The result of adding a chart to a spreadsheet. Fields  
---  
`chart` |  `object ([EmbeddedChart](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedChart))` The newly added chart.  
  
## AddConditionalFormatRuleRequest

Adds a new conditional format rule at the given index. All subsequent rules' indexes are incremented. Fields  
---  
`index` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The zero-based index where the rule should be inserted.  
`rule` |  `object ([ConditionalFormatRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ConditionalFormatRule))` The rule to add.  
  
## AddDataSourceRequest

Adds a data source. After the data source is added successfully, an associated DATA_SOURCE sheet is created and an execution is triggered to refresh the sheet to read data from the data source. The request requires an additional `bigquery.readonly` OAuth scope. Fields  
---  
`dataSource` |  `object ([DataSource](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSource))` The data source to add.  
  
## AddDataSourceResponse

The result of adding a data source. Fields  
---  
`dataExecutionStatus` |  `object ([DataExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataExecutionStatus))` The data execution status.  
`dataSource` |  `object ([DataSource](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSource))` The data source that was created.  
  
## AddDimensionGroupRequest

Creates a group over the specified range. If the requested range is a superset of the range of an existing group G, then the depth of G is incremented and this new group G' has the depth of that group. For example, a group [C:D, depth 1] + [B:E] results in groups [B:E, depth 1] and [C:D, depth 2]. If the requested range is a subset of the range of an existing group G, then the depth of the new group G' becomes one greater than the depth of G. For example, a group [B:E, depth 1] + [C:D] results in groups [B:E, depth 1] and [C:D, depth 2]. If the requested range starts before and ends within, or starts within and ends after, the range of an existing group G, then the range of the existing group G becomes the union of the ranges, and the new group G' has depth one greater than the depth of G and range as the intersection of the ranges. For example, a group [B:D, depth 1] + [C:E] results in groups [B:E, depth 1] and [C:D, depth 2]. Fields  
---  
`range` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The range over which to create a group.  
  
## AddDimensionGroupResponse

The result of adding a group. Fields  
---  
`dimensionGroups[]` |  `object ([DimensionGroup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionGroup))` All groups of a dimension after adding a group to that dimension.  
  
## AddFilterViewRequest

Adds a filter view. Fields  
---  
`filter` |  `object ([FilterView](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterView))` The filter to add. The filterViewId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a filter that already exists.)  
  
## AddFilterViewResponse

The result of adding a filter view. Fields  
---  
`filter` |  `object ([FilterView](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterView))` The newly added filter view.  
  
## AddNamedRangeRequest

Adds a named range to the spreadsheet. Fields  
---  
`namedRange` |  `object ([NamedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#NamedRange))` The named range to add. The namedRangeId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a range that already exists.)  
  
## AddNamedRangeResponse

The result of adding a named range. Fields  
---  
`namedRange` |  `object ([NamedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#NamedRange))` The named range to add.  
  
## AddProtectedRangeRequest

Adds a new protected range. Fields  
---  
`protectedRange` |  `object ([ProtectedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ProtectedRange))` The protected range to be added. The protectedRangeId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a range that already exists.)  
  
## AddProtectedRangeResponse

The result of adding a new protected range. Fields  
---  
`protectedRange` |  `object ([ProtectedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ProtectedRange))` The newly added protected range.  
  
## AddSheetRequest

Adds a new sheet. When a sheet is added at a given index, all subsequent sheets' indexes are incremented. To add an object sheet, use AddChartRequest instead and specify EmbeddedObjectPosition.sheetId or EmbeddedObjectPosition.newSheet. Fields  
---  
`properties` |  `object ([SheetProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SheetProperties))` The properties the new sheet should have. All properties are optional. The sheetId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a sheet that already exists.)  
  
## AddSheetResponse

The result of adding a sheet. Fields  
---  
`properties` |  `object ([SheetProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SheetProperties))` The properties of the newly added sheet.  
  
## AddSlicerRequest

Adds a slicer to a sheet in the spreadsheet. Fields  
---  
`slicer` |  `object ([Slicer](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Slicer))` The slicer that should be added to the spreadsheet, including the position where it should be placed. The slicerId field is optional; if one is not set, an id will be randomly generated. (It is an error to specify the ID of a slicer that already exists.)  
  
## AddSlicerResponse

The result of adding a slicer to a spreadsheet. Fields  
---  
`slicer` |  `object ([Slicer](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Slicer))` The newly added slicer.  
  
## AppendCellsRequest

Adds new cells after the last row with data in a sheet, inserting new rows into the sheet if necessary. Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields of CellData that should be updated. At least one field must be specified. The root is the CellData; 'row.values.' should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`rows[]` |  `object ([RowData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#RowData))` The data to append.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet ID to append the data to.  
  
## AppendDimensionRequest

Appends rows or columns to the end of a sheet. Fields  
---  
`dimension` |  `enum` Whether rows or columns should be appended.  
Enum type. Can be one of the following:  
`DIMENSION_UNSPECIFIED` | The default value, do not use.  
`ROWS` | Operates on the rows of a sheet.  
`COLUMNS` | Operates on the columns of a sheet.  
`length` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of rows or columns to append.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet to append rows or columns to.  
  
## AppendValuesResponse

The response when updating a range of values in a spreadsheet. Fields  
---  
`spreadsheetId` |  `string` The spreadsheet the updates were applied to.  
`tableRange` |  `string` The range (in A1 notation) of the table that values are being appended to (before the values were appended). Empty if no table was found.  
`updates` |  `object ([UpdateValuesResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateValuesResponse))` Information about the updates that were applied.  
  
## AutoFillRequest

Fills in more data based on existing data. Fields  
---  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range to autofill. This will examine the range and detect the location that has data and automatically fill that data in to the rest of the range.  
`sourceAndDestination` |  `object ([SourceAndDestination](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SourceAndDestination))` The source and destination areas to autofill. This explicitly lists the source of the autofill and where to extend that data.  
`useAlternateSeries` |  `boolean` True if we should generate data with the "alternate" series. This differs based on the type and amount of source data.  
  
## AutoResizeDimensionsRequest

Automatically resizes one or more dimensions based on the contents of the cells in that dimension. Fields  
---  
`dataSourceSheetDimensions` |  `object ([DataSourceSheetDimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceSheetDimensionRange))` The dimensions on a data source sheet to automatically resize.  
`dimensions` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The dimensions to automatically resize.  
  
## BandedRange

A banded (alternating colors) range in a sheet. Fields  
---  
`bandedRangeId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The id of the banded range.  
`columnProperties` |  `object ([BandingProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BandingProperties))` Properties for column bands. These properties are applied on a column- by-column basis throughout all the columns in the range. At least one of row_properties or column_properties must be specified.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range over which these properties are applied.  
`rowProperties` |  `object ([BandingProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BandingProperties))` Properties for row bands. These properties are applied on a row-by-row basis throughout all the rows in the range. At least one of row_properties or column_properties must be specified.  
  
## BandingProperties

Properties referring a single dimension (either row or column). If both BandedRange.row_properties and BandedRange.column_properties are set, the fill colors are applied to cells according to the following rules: * header_color and footer_color take priority over band colors. * first_band_color takes priority over second_band_color. * row_properties takes priority over column_properties. For example, the first row color takes priority over the first column color, but the first column color takes priority over the second row color. Similarly, the row header takes priority over the column header in the top left cell, but the column header takes priority over the first row color if the row header is not set. Fields  
---  
`firstBandColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The first color that is alternating. (Required) Deprecated: Use first_band_color_style.  
`firstBandColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The first color that is alternating. (Required) If first_band_color is also set, this field takes precedence.  
`footerColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the last row or column. If this field is not set, the last row or column is filled with either first_band_color or second_band_color, depending on the color of the previous row or column. Deprecated: Use footer_color_style.  
`footerColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the last row or column. If this field is not set, the last row or column is filled with either first_band_color or second_band_color, depending on the color of the previous row or column. If footer_color is also set, this field takes precedence.  
`headerColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the first row or column. If this field is set, the first row or column is filled with this color and the colors alternate between first_band_color and second_band_color starting from the second row or column. Otherwise, the first row or column is filled with first_band_color and the colors proceed to alternate as they normally would. Deprecated: Use header_color_style.  
`headerColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the first row or column. If this field is set, the first row or column is filled with this color and the colors alternate between first_band_color and second_band_color starting from the second row or column. Otherwise, the first row or column is filled with first_band_color and the colors proceed to alternate as they normally would. If header_color is also set, this field takes precedence.  
`secondBandColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The second color that is alternating. (Required) Deprecated: Use second_band_color_style.  
`secondBandColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The second color that is alternating. (Required) If second_band_color is also set, this field takes precedence.  
  
## BaselineValueFormat

Formatting options for baseline value. Fields  
---  
`comparisonType` |  `enum` The comparison type of key value with baseline value.  
Enum type. Can be one of the following:  
`COMPARISON_TYPE_UNDEFINED` | Default value, do not use.  
`ABSOLUTE_DIFFERENCE` | Use absolute difference between key and baseline value.  
`PERCENTAGE_DIFFERENCE` | Use percentage difference between key and baseline value.  
`description` |  `string` Description which is appended after the baseline value. This field is optional.  
`negativeColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` Color to be used, in case baseline value represents a negative change for key value. This field is optional. Deprecated: Use negative_color_style.  
`negativeColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` Color to be used, in case baseline value represents a negative change for key value. This field is optional. If negative_color is also set, this field takes precedence.  
`position` |  `object ([TextPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextPosition))` Specifies the horizontal text positioning of baseline value. This field is optional. If not specified, default positioning is used.  
`positiveColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` Color to be used, in case baseline value represents a positive change for key value. This field is optional. Deprecated: Use positive_color_style.  
`positiveColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` Color to be used, in case baseline value represents a positive change for key value. This field is optional. If positive_color is also set, this field takes precedence.  
`textFormat` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` Text formatting options for baseline value. The link field is not supported.  
  
## BasicChartAxis

An axis of the chart. A chart may not have more than one axis per axis position. Fields  
---  
`format` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The format of the title. Only valid if the axis is not associated with the domain. The link field is not supported.  
`position` |  `enum` The position of this axis.  
Enum type. Can be one of the following:  
`BASIC_CHART_AXIS_POSITION_UNSPECIFIED` | Default value, do not use.  
`BOTTOM_AXIS` | The axis rendered at the bottom of a chart. For most charts, this is the standard major axis. For bar charts, this is a minor axis.  
`LEFT_AXIS` | The axis rendered at the left of a chart. For most charts, this is a minor axis. For bar charts, this is the standard major axis.  
`RIGHT_AXIS` | The axis rendered at the right of a chart. For most charts, this is a minor axis. For bar charts, this is an unusual major axis.  
`title` |  `string` The title of this axis. If set, this overrides any title inferred from headers of the data.  
`titleTextPosition` |  `object ([TextPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextPosition))` The axis title text position.  
`viewWindowOptions` |  `object ([ChartAxisViewWindowOptions](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartAxisViewWindowOptions))` The view window options for this axis.  
  
## BasicChartDomain

The domain of a chart. For example, if charting stock prices over time, this would be the date. Fields  
---  
`domain` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data of the domain. For example, if charting stock prices over time, this is the data representing the dates.  
`reversed` |  `boolean` True to reverse the order of the domain values (horizontal axis).  
  
## BasicChartSeries

A single series of data in a chart. For example, if charting stock prices over time, multiple series may exist, one for the "Open Price", "High Price", "Low Price" and "Close Price". Fields  
---  
`color` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color for elements (such as bars, lines, and points) associated with this series. If empty, a default color is used. Deprecated: Use color_style.  
`colorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color for elements (such as bars, lines, and points) associated with this series. If empty, a default color is used. If color is also set, this field takes precedence.  
`dataLabel` |  `object ([DataLabel](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataLabel))` Information about the data labels for this series.  
`lineStyle` |  `object ([LineStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#LineStyle))` The line style of this series. Valid only if the chartType is AREA, LINE, or SCATTER. COMBO charts are also supported if the series chart type is AREA or LINE.  
`pointStyle` |  `object ([PointStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PointStyle))` The style for points associated with this series. Valid only if the chartType is AREA, LINE, or SCATTER. COMBO charts are also supported if the series chart type is AREA, LINE, or SCATTER. If empty, a default point style is used.  
`series` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data being visualized in this chart series.  
`styleOverrides[]` |  `object ([BasicSeriesDataPointStyleOverride](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BasicSeriesDataPointStyleOverride))` Style override settings for series data points.  
`targetAxis` |  `enum` The minor axis that will specify the range of values for this series. For example, if charting stocks over time, the "Volume" series may want to be pinned to the right with the prices pinned to the left, because the scale of trading volume is different than the scale of prices. It is an error to specify an axis that isn't a valid minor axis for the chart's type.  
Enum type. Can be one of the following:  
`BASIC_CHART_AXIS_POSITION_UNSPECIFIED` | Default value, do not use.  
`BOTTOM_AXIS` | The axis rendered at the bottom of a chart. For most charts, this is the standard major axis. For bar charts, this is a minor axis.  
`LEFT_AXIS` | The axis rendered at the left of a chart. For most charts, this is a minor axis. For bar charts, this is the standard major axis.  
`RIGHT_AXIS` | The axis rendered at the right of a chart. For most charts, this is a minor axis. For bar charts, this is an unusual major axis.  
`type` |  `enum` The type of this series. Valid only if the chartType is COMBO. Different types will change the way the series is visualized. Only LINE, AREA, and COLUMN are supported.  
Enum type. Can be one of the following:  
`BASIC_CHART_TYPE_UNSPECIFIED` | Default value, do not use.  
`BAR` | A bar chart.  
`LINE` | A line chart.  
`AREA` | An area chart.  
`COLUMN` | A column chart.  
`SCATTER` | A scatter chart.  
`COMBO` | A combo chart.  
`STEPPED_AREA` | A stepped area chart.  
  
## BasicChartSpec

The specification for a basic chart. See BasicChartType for the list of charts this supports. Fields  
---  
`axis[]` |  `object ([BasicChartAxis](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BasicChartAxis))` The axis on the chart.  
`chartType` |  `enum` The type of the chart.  
Enum type. Can be one of the following:  
`BASIC_CHART_TYPE_UNSPECIFIED` | Default value, do not use.  
`BAR` | A bar chart.  
`LINE` | A line chart.  
`AREA` | An area chart.  
`COLUMN` | A column chart.  
`SCATTER` | A scatter chart.  
`COMBO` | A combo chart.  
`STEPPED_AREA` | A stepped area chart.  
`compareMode` |  `enum` The behavior of tooltips and data highlighting when hovering on data and chart area.  
Enum type. Can be one of the following:  
`BASIC_CHART_COMPARE_MODE_UNSPECIFIED` | Default value, do not use.  
`DATUM` | Only the focused data element is highlighted and shown in the tooltip.  
`CATEGORY` | All data elements with the same category (e.g., domain value) are highlighted and shown in the tooltip.  
`domains[]` |  `object ([BasicChartDomain](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BasicChartDomain))` The domain of data this is charting. Only a single domain is supported.  
`headerCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of rows or columns in the data that are "headers". If not set, Google Sheets will guess how many rows are headers based on the data. (Note that BasicChartAxis.title may override the axis title inferred from the header values.)  
`interpolateNulls` |  `boolean` If some values in a series are missing, gaps may appear in the chart (e.g, segments of lines in a line chart will be missing). To eliminate these gaps set this to true. Applies to Line, Area, and Combo charts.  
`legendPosition` |  `enum` The position of the chart legend.  
Enum type. Can be one of the following:  
`BASIC_CHART_LEGEND_POSITION_UNSPECIFIED` | Default value, do not use.  
`BOTTOM_LEGEND` | The legend is rendered on the bottom of the chart.  
`LEFT_LEGEND` | The legend is rendered on the left of the chart.  
`RIGHT_LEGEND` | The legend is rendered on the right of the chart.  
`TOP_LEGEND` | The legend is rendered on the top of the chart.  
`NO_LEGEND` | No legend is rendered.  
`lineSmoothing` |  `boolean` Gets whether all lines should be rendered smooth or straight by default. Applies to Line charts.  
`series[]` |  `object ([BasicChartSeries](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BasicChartSeries))` The data this chart is visualizing.  
`stackedType` |  `enum` The stacked type for charts that support vertical stacking. Applies to Area, Bar, Column, Combo, and Stepped Area charts.  
Enum type. Can be one of the following:  
`BASIC_CHART_STACKED_TYPE_UNSPECIFIED` | Default value, do not use.  
`NOT_STACKED` | Series are not stacked.  
`STACKED` | Series values are stacked, each value is rendered vertically beginning from the top of the value below it.  
`PERCENT_STACKED` | Vertical stacks are stretched to reach the top of the chart, with values laid out as percentages of each other.  
`threeDimensional` |  `boolean` True to make the chart 3D. Applies to Bar and Column charts.  
`totalDataLabel` |  `object ([DataLabel](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataLabel))` Controls whether to display additional data labels on stacked charts which sum the total value of all stacked values at each value along the domain axis. These data labels can only be set when chart_type is one of AREA, BAR, COLUMN, COMBO or STEPPED_AREA and stacked_type is either STACKED or PERCENT_STACKED. In addition, for COMBO, this will only be supported if there is only one type of stackable series type or one type has more series than the others and each of the other types have no more than one series. For example, if a chart has two stacked bar series and one area series, the total data labels will be supported. If it has three bar series and two area series, total data labels are not allowed. Neither CUSTOM nor placement can be set on the total_data_label.  
  
## BasicFilter

The default filter associated with a sheet. Fields  
---  
`criteria` |  `map (key: string, value: object ([FilterCriteria](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterCriteria)))` The criteria for showing/hiding values per column. The map's key is the column index, and the value is the criteria for that column. This field is deprecated in favor of filter_specs.  
`filterSpecs[]` |  `object ([FilterSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterSpec))` The filter criteria per column. Both criteria and filter_specs are populated in responses. If both fields are specified in an update request, this field takes precedence.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range the filter covers.  
`sortSpecs[]` |  `object ([SortSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SortSpec))` The sort order per column. Later specifications are used when values are equal in the earlier specifications.  
  
## BasicSeriesDataPointStyleOverride

Style override settings for a single series data point. Fields  
---  
`color` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` Color of the series data point. If empty, the series default is used. Deprecated: Use color_style.  
`colorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` Color of the series data point. If empty, the series default is used. If color is also set, this field takes precedence.  
`index` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Zero based index of the series data point.  
`pointStyle` |  `object ([PointStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PointStyle))` Point style of the series data point. Valid only if the chartType is AREA, LINE, or SCATTER. COMBO charts are also supported if the series chart type is AREA, LINE, or SCATTER. If empty, the series default is used.  
  
## BatchClearValuesByDataFilterRequest

The request for clearing more than one range selected by a DataFilter in a spreadsheet. Fields  
---  
`dataFilters[]` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The DataFilters used to determine which ranges to clear.  
  
## BatchClearValuesByDataFilterResponse

The response when clearing a range of values selected with DataFilters in a spreadsheet. Fields  
---  
`clearedRanges[]` |  `string` The ranges that were cleared, in [A1 notation](https://developers.google.com/sheets/api/guides/concepts#cell). If the requests are for an unbounded range or a ranger larger than the bounds of the sheet, this is the actual ranges that were cleared, bounded to the sheet's limits.  
`spreadsheetId` |  `string` The spreadsheet the updates were applied to.  
  
## BatchClearValuesRequest

The request for clearing more than one range of values in a spreadsheet. Fields  
---  
`ranges[]` |  `string` The ranges to clear, in [A1 notation or R1C1 notation](https://developers.google.com/sheets/api/guides/concepts#cell).  
  
## BatchClearValuesResponse

The response when clearing a range of values in a spreadsheet. Fields  
---  
`clearedRanges[]` |  `string` The ranges that were cleared, in A1 notation. If the requests are for an unbounded range or a ranger larger than the bounds of the sheet, this is the actual ranges that were cleared, bounded to the sheet's limits.  
`spreadsheetId` |  `string` The spreadsheet the updates were applied to.  
  
## BatchGetValuesByDataFilterRequest

The request for retrieving a range of values in a spreadsheet selected by a set of DataFilters. Fields  
---  
`dataFilters[]` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The data filters used to match the ranges of values to retrieve. Ranges that match any of the specified data filters are included in the response.  
`dateTimeRenderOption` |  `enum` How dates, times, and durations should be represented in the output. This is ignored if value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.  
Enum type. Can be one of the following:  
`SERIAL_NUMBER` | Instructs date, time, datetime, and duration fields to be output as doubles in "serial number" format, as popularized by Lotus 1-2-3. The whole number portion of the value (left of the decimal) counts the days since December 30th 1899. The fractional portion (right of the decimal) counts the time as a fraction of the day. For example, January 1st 1900 at noon would be 2.5, 2 because it's 2 days after December 30th 1899, and .5 because noon is half a day. February 1st 1900 at 3pm would be 33.625. This correctly treats the year 1900 as not a leap year.  
`FORMATTED_STRING` | Instructs date, time, datetime, and duration fields to be output as strings in their given number format (which depends on the spreadsheet locale).  
`majorDimension` |  `enum` The major dimension that results should use. For example, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`, then a request that selects that range and sets `majorDimension=ROWS` returns `[[1,2],[3,4]]`, whereas a request that sets `majorDimension=COLUMNS` returns `[[1,3],[2,4]]`.  
Enum type. Can be one of the following:  
`DIMENSION_UNSPECIFIED` | The default value, do not use.  
`ROWS` | Operates on the rows of a sheet.  
`COLUMNS` | Operates on the columns of a sheet.  
`valueRenderOption` |  `enum` How values should be represented in the output. The default render option is FORMATTED_VALUE.  
Enum type. Can be one of the following:  
`FORMATTED_VALUE` | Values will be calculated & formatted in the reply according to the cell's formatting. Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` would return `"$1.23"`.  
`UNFORMATTED_VALUE` | Values will be calculated, but not formatted in the reply. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` would return the number `1.23`.  
`FORMULA` | Values will not be calculated. The reply will include the formulas. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then A2 would return `"=A1"`.  
  
## BatchGetValuesByDataFilterResponse

The response when retrieving more than one range of values in a spreadsheet selected by DataFilters. Fields  
---  
`spreadsheetId` |  `string` The ID of the spreadsheet the data was retrieved from.  
`valueRanges[]` |  `object ([MatchedValueRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#MatchedValueRange))` The requested values with the list of data filters that matched them.  
  
## BatchGetValuesResponse

The response when retrieving more than one range of values in a spreadsheet. Fields  
---  
`spreadsheetId` |  `string` The ID of the spreadsheet the data was retrieved from.  
`valueRanges[]` |  `object ([ValueRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ValueRange))` The requested values. The order of the ValueRanges is the same as the order of the requested ranges.  
  
## BatchUpdateSpreadsheetRequest

The request for updating any aspect of a spreadsheet. Fields  
---  
`includeSpreadsheetInResponse` |  `boolean` Determines if the update response should include the spreadsheet resource.  
`requests[]` |  `object ([Request](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Request))` A list of updates to apply to the spreadsheet. Requests will be applied in the order they are specified. If any request is not valid, no requests will be applied.  
`responseIncludeGridData` |  `boolean` True if grid data should be returned. Meaningful only if include_spreadsheet_in_response is 'true'. This parameter is ignored if a field mask was set in the request.  
`responseRanges[]` |  `string` Limits the ranges included in the response spreadsheet. Meaningful only if include_spreadsheet_in_response is 'true'.  
  
## BatchUpdateSpreadsheetResponse

The reply for batch updating a spreadsheet. Fields  
---  
`replies[]` |  `object ([Response](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Response))` The reply of the updates. This maps 1:1 with the updates, although replies to some requests may be empty.  
`spreadsheetId` |  `string` The spreadsheet the updates were applied to.  
`updatedSpreadsheet` |  `object ([Spreadsheet](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Spreadsheet))` The spreadsheet after updates were applied. This is only set if BatchUpdateSpreadsheetRequest.include_spreadsheet_in_response is `true`.  
  
## BatchUpdateValuesByDataFilterRequest

The request for updating more than one range of values in a spreadsheet. Fields  
---  
`data[]` |  `object ([DataFilterValueRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilterValueRange))` The new values to apply to the spreadsheet. If more than one range is matched by the specified DataFilter the specified values are applied to all of those ranges.  
`includeValuesInResponse` |  `boolean` Determines if the update response should include the values of the cells that were updated. By default, responses do not include the updated values. The `updatedData` field within each of the BatchUpdateValuesResponse.responses contains the updated values. If the range to write was larger than the range actually written, the response includes all values in the requested range (excluding trailing empty rows and columns).  
`responseDateTimeRenderOption` |  `enum` Determines how dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.  
Enum type. Can be one of the following:  
`SERIAL_NUMBER` | Instructs date, time, datetime, and duration fields to be output as doubles in "serial number" format, as popularized by Lotus 1-2-3. The whole number portion of the value (left of the decimal) counts the days since December 30th 1899. The fractional portion (right of the decimal) counts the time as a fraction of the day. For example, January 1st 1900 at noon would be 2.5, 2 because it's 2 days after December 30th 1899, and .5 because noon is half a day. February 1st 1900 at 3pm would be 33.625. This correctly treats the year 1900 as not a leap year.  
`FORMATTED_STRING` | Instructs date, time, datetime, and duration fields to be output as strings in their given number format (which depends on the spreadsheet locale).  
`responseValueRenderOption` |  `enum` Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE.  
Enum type. Can be one of the following:  
`FORMATTED_VALUE` | Values will be calculated & formatted in the reply according to the cell's formatting. Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` would return `"$1.23"`.  
`UNFORMATTED_VALUE` | Values will be calculated, but not formatted in the reply. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` would return the number `1.23`.  
`FORMULA` | Values will not be calculated. The reply will include the formulas. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then A2 would return `"=A1"`.  
`valueInputOption` |  `enum` How the input data should be interpreted.  
Enum type. Can be one of the following:  
`INPUT_VALUE_OPTION_UNSPECIFIED` | Default input value. This value must not be used.  
`RAW` | The values the user has entered will not be parsed and will be stored as-is.  
`USER_ENTERED` | The values will be parsed as if the user typed them into the UI. Numbers will stay as numbers, but strings may be converted to numbers, dates, etc. following the same rules that are applied when entering text into a cell via the Google Sheets UI.  
  
## BatchUpdateValuesByDataFilterResponse

The response when updating a range of values in a spreadsheet. Fields  
---  
`responses[]` |  `object ([UpdateValuesByDataFilterResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateValuesByDataFilterResponse))` The response for each range updated.  
`spreadsheetId` |  `string` The spreadsheet the updates were applied to.  
`totalUpdatedCells` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total number of cells updated.  
`totalUpdatedColumns` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total number of columns where at least one cell in the column was updated.  
`totalUpdatedRows` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total number of rows where at least one cell in the row was updated.  
`totalUpdatedSheets` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total number of sheets where at least one cell in the sheet was updated.  
  
## BatchUpdateValuesRequest

The request for updating more than one range of values in a spreadsheet. Fields  
---  
`data[]` |  `object ([ValueRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ValueRange))` The new values to apply to the spreadsheet.  
`includeValuesInResponse` |  `boolean` Determines if the update response should include the values of the cells that were updated. By default, responses do not include the updated values. The `updatedData` field within each of the BatchUpdateValuesResponse.responses contains the updated values. If the range to write was larger than the range actually written, the response includes all values in the requested range (excluding trailing empty rows and columns).  
`responseDateTimeRenderOption` |  `enum` Determines how dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER.  
Enum type. Can be one of the following:  
`SERIAL_NUMBER` | Instructs date, time, datetime, and duration fields to be output as doubles in "serial number" format, as popularized by Lotus 1-2-3. The whole number portion of the value (left of the decimal) counts the days since December 30th 1899. The fractional portion (right of the decimal) counts the time as a fraction of the day. For example, January 1st 1900 at noon would be 2.5, 2 because it's 2 days after December 30th 1899, and .5 because noon is half a day. February 1st 1900 at 3pm would be 33.625. This correctly treats the year 1900 as not a leap year.  
`FORMATTED_STRING` | Instructs date, time, datetime, and duration fields to be output as strings in their given number format (which depends on the spreadsheet locale).  
`responseValueRenderOption` |  `enum` Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE.  
Enum type. Can be one of the following:  
`FORMATTED_VALUE` | Values will be calculated & formatted in the reply according to the cell's formatting. Formatting is based on the spreadsheet's locale, not the requesting user's locale. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` would return `"$1.23"`.  
`UNFORMATTED_VALUE` | Values will be calculated, but not formatted in the reply. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then `A2` would return the number `1.23`.  
`FORMULA` | Values will not be calculated. The reply will include the formulas. For example, if `A1` is `1.23` and `A2` is `=A1` and formatted as currency, then A2 would return `"=A1"`.  
`valueInputOption` |  `enum` How the input data should be interpreted.  
Enum type. Can be one of the following:  
`INPUT_VALUE_OPTION_UNSPECIFIED` | Default input value. This value must not be used.  
`RAW` | The values the user has entered will not be parsed and will be stored as-is.  
`USER_ENTERED` | The values will be parsed as if the user typed them into the UI. Numbers will stay as numbers, but strings may be converted to numbers, dates, etc. following the same rules that are applied when entering text into a cell via the Google Sheets UI.  
  
## BatchUpdateValuesResponse

The response when updating a range of values in a spreadsheet. Fields  
---  
`responses[]` |  `object ([UpdateValuesResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateValuesResponse))` One UpdateValuesResponse per requested range, in the same order as the requests appeared.  
`spreadsheetId` |  `string` The spreadsheet the updates were applied to.  
`totalUpdatedCells` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total number of cells updated.  
`totalUpdatedColumns` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total number of columns where at least one cell in the column was updated.  
`totalUpdatedRows` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total number of rows where at least one cell in the row was updated.  
`totalUpdatedSheets` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total number of sheets where at least one cell in the sheet was updated.  
  
## BigQueryDataSourceSpec

The specification of a BigQuery data source that's connected to a sheet. Fields  
---  
`projectId` |  `string` The ID of a BigQuery enabled GCP project with a billing account attached. For any queries executed against the data source, the project is charged.  
`querySpec` |  `object ([BigQueryQuerySpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BigQueryQuerySpec))` A BigQueryQuerySpec.  
`tableSpec` |  `object ([BigQueryTableSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BigQueryTableSpec))` A BigQueryTableSpec.  
  
## BigQueryQuerySpec

Specifies a custom BigQuery query. Fields  
---  
`rawQuery` |  `string` The raw query string.  
  
## BigQueryTableSpec

Specifies a BigQuery table definition. Only [native tables](https://cloud.google.com/bigquery/docs/tables-intro) is allowed. Fields  
---  
`datasetId` |  `string` The BigQuery dataset id.  
`tableId` |  `string` The BigQuery table id.  
`tableProjectId` |  `string` The ID of a BigQuery project the table belongs to. If not specified, the project_id is assumed.  
  
## BooleanCondition

A condition that can evaluate to true or false. BooleanConditions are used by conditional formatting, data validation, and the criteria in filters. Fields  
---  
`type` |  `enum` The type of condition.  
Enum type. Can be one of the following:  
`CONDITION_TYPE_UNSPECIFIED` | The default value, do not use.  
`NUMBER_GREATER` | The cell's value must be greater than the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue.  
`NUMBER_GREATER_THAN_EQ` | The cell's value must be greater than or equal to the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue.  
`NUMBER_LESS` | The cell's value must be less than the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue.  
`NUMBER_LESS_THAN_EQ` | The cell's value must be less than or equal to the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue.  
`NUMBER_EQ` | The cell's value must be equal to the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue for data validation, conditional formatting, and filters on non-data source objects and at least one ConditionValue for filters on data source objects.  
`NUMBER_NOT_EQ` | The cell's value must be not equal to the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue for data validation, conditional formatting, and filters on non-data source objects and at least one ConditionValue for filters on data source objects.  
`NUMBER_BETWEEN` | The cell's value must be between the two condition values. Supported by data validation, conditional formatting and filters. Requires exactly two ConditionValues.  
`NUMBER_NOT_BETWEEN` | The cell's value must not be between the two condition values. Supported by data validation, conditional formatting and filters. Requires exactly two ConditionValues.  
`TEXT_CONTAINS` | The cell's value must contain the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue.  
`TEXT_NOT_CONTAINS` | The cell's value must not contain the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue.  
`TEXT_STARTS_WITH` | The cell's value must start with the condition's value. Supported by conditional formatting and filters. Requires a single ConditionValue.  
`TEXT_ENDS_WITH` | The cell's value must end with the condition's value. Supported by conditional formatting and filters. Requires a single ConditionValue.  
`TEXT_EQ` | The cell's value must be exactly the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue for data validation, conditional formatting, and filters on non-data source objects and at least one ConditionValue for filters on data source objects.  
`TEXT_IS_EMAIL` | The cell's value must be a valid email address. Supported by data validation. Requires no ConditionValues.  
`TEXT_IS_URL` | The cell's value must be a valid URL. Supported by data validation. Requires no ConditionValues.  
`DATE_EQ` | The cell's value must be the same date as the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue for data validation, conditional formatting, and filters on non-data source objects and at least one ConditionValue for filters on data source objects.  
`DATE_BEFORE` | The cell's value must be before the date of the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue that may be a relative date.  
`DATE_AFTER` | The cell's value must be after the date of the condition's value. Supported by data validation, conditional formatting and filters. Requires a single ConditionValue that may be a relative date.  
`DATE_ON_OR_BEFORE` | The cell's value must be on or before the date of the condition's value. Supported by data validation. Requires a single ConditionValue that may be a relative date.  
`DATE_ON_OR_AFTER` | The cell's value must be on or after the date of the condition's value. Supported by data validation. Requires a single ConditionValue that may be a relative date.  
`DATE_BETWEEN` | The cell's value must be between the dates of the two condition values. Supported by data validation. Requires exactly two ConditionValues.  
`DATE_NOT_BETWEEN` | The cell's value must be outside the dates of the two condition values. Supported by data validation. Requires exactly two ConditionValues.  
`DATE_IS_VALID` | The cell's value must be a date. Supported by data validation. Requires no ConditionValues.  
`ONE_OF_RANGE` | The cell's value must be listed in the grid in condition value's range. Supported by data validation. Requires a single ConditionValue, and the value must be a valid range in A1 notation.  
`ONE_OF_LIST` | The cell's value must be in the list of condition values. Supported by data validation. Supports any number of condition values, one per item in the list. Formulas are not supported in the values.  
`BLANK` | The cell's value must be empty. Supported by conditional formatting and filters. Requires no ConditionValues.  
`NOT_BLANK` | The cell's value must not be empty. Supported by conditional formatting and filters. Requires no ConditionValues.  
`CUSTOM_FORMULA` | The condition's formula must evaluate to true. Supported by data validation, conditional formatting and filters. Not supported by data source sheet filters. Requires a single ConditionValue.  
`BOOLEAN` | The cell's value must be TRUE/FALSE or in the list of condition values. Supported by data validation. Renders as a cell checkbox. Supports zero, one or two ConditionValues. No values indicates the cell must be TRUE or FALSE, where TRUE renders as checked and FALSE renders as unchecked. One value indicates the cell will render as checked when it contains that value and unchecked when it is blank. Two values indicate that the cell will render as checked when it contains the first value and unchecked when it contains the second value. For example, ["Yes","No"] indicates that the cell will render a checked box when it has the value "Yes" and an unchecked box when it has the value "No".  
`TEXT_NOT_EQ` | The cell's value must be exactly not the condition's value. Supported by filters on data source objects. Requires at least one ConditionValue.  
`DATE_NOT_EQ` | The cell's value must be exactly not the condition's value. Supported by filters on data source objects. Requires at least one ConditionValue.  
`values[]` |  `object ([ConditionValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ConditionValue))` The values of the condition. The number of supported values depends on the condition type. Some support zero values, others one or two values, and ConditionType.ONE_OF_LIST supports an arbitrary number of values.  
  
## BooleanRule

A rule that may or may not match, depending on the condition. Fields  
---  
`condition` |  `object ([BooleanCondition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BooleanCondition))` The condition of the rule. If the condition evaluates to true, the format is applied.  
`format` |  `object ([CellFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CellFormat))` The format to apply. Conditional formatting can only apply a subset of formatting: bold, italic, strikethrough, foreground color & background color.  
  
## Border

A border along a cell. Fields  
---  
`color` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the border. Deprecated: Use color_style.  
`colorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the border. If color is also set, this field takes precedence.  
`style` |  `enum` The style of the border.  
Enum type. Can be one of the following:  
`STYLE_UNSPECIFIED` | The style is not specified. Do not use this.  
`DOTTED` | The border is dotted.  
`DASHED` | The border is dashed.  
`SOLID` | The border is a thin solid line.  
`SOLID_MEDIUM` | The border is a medium solid line.  
`SOLID_THICK` | The border is a thick solid line.  
`NONE` | No border. Used only when updating a border in order to erase it.  
`DOUBLE` | The border is two solid lines.  
`width` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The width of the border, in pixels. Deprecated; the width is determined by the "style" field.  
  
## Borders

The borders of the cell. Fields  
---  
`bottom` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The bottom border of the cell.  
`left` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The left border of the cell.  
`right` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The right border of the cell.  
`top` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The top border of the cell.  
  
## BubbleChartSpec

A bubble chart. Fields  
---  
`bubbleBorderColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The bubble border color. Deprecated: Use bubble_border_color_style.  
`bubbleBorderColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The bubble border color. If bubble_border_color is also set, this field takes precedence.  
`bubbleLabels` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data containing the bubble labels. These do not need to be unique.  
`bubbleMaxRadiusSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The max radius size of the bubbles, in pixels. If specified, the field must be a positive value.  
`bubbleMinRadiusSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The minimum radius size of the bubbles, in pixels. If specific, the field must be a positive value.  
`bubbleOpacity` |  `number ([float](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The opacity of the bubbles between 0 and 1.0. 0 is fully transparent and 1 is fully opaque.  
`bubbleSizes` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data containing the bubble sizes. Bubble sizes are used to draw the bubbles at different sizes relative to each other. If specified, group_ids must also be specified. This field is optional.  
`bubbleTextStyle` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The format of the text inside the bubbles. Strikethrough, underline, and link are not supported.  
`domain` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data containing the bubble x-values. These values locate the bubbles in the chart horizontally.  
`groupIds` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data containing the bubble group IDs. All bubbles with the same group ID are drawn in the same color. If bubble_sizes is specified then this field must also be specified but may contain blank values. This field is optional.  
`legendPosition` |  `enum` Where the legend of the chart should be drawn.  
Enum type. Can be one of the following:  
`BUBBLE_CHART_LEGEND_POSITION_UNSPECIFIED` | Default value, do not use.  
`BOTTOM_LEGEND` | The legend is rendered on the bottom of the chart.  
`LEFT_LEGEND` | The legend is rendered on the left of the chart.  
`RIGHT_LEGEND` | The legend is rendered on the right of the chart.  
`TOP_LEGEND` | The legend is rendered on the top of the chart.  
`NO_LEGEND` | No legend is rendered.  
`INSIDE_LEGEND` | The legend is rendered inside the chart area.  
`series` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data containing the bubble y-values. These values locate the bubbles in the chart vertically.  
  
## CandlestickChartSpec

A candlestick chart. Fields  
---  
`data[]` |  `object ([CandlestickData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CandlestickData))` The Candlestick chart data. Only one CandlestickData is supported.  
`domain` |  `object ([CandlestickDomain](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CandlestickDomain))` The domain data (horizontal axis) for the candlestick chart. String data will be treated as discrete labels, other data will be treated as continuous values.  
  
## CandlestickData

The Candlestick chart data, each containing the low, open, close, and high values for a series. Fields  
---  
`closeSeries` |  `object ([CandlestickSeries](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CandlestickSeries))` The range data (vertical axis) for the close/final value for each candle. This is the top of the candle body. If greater than the open value the candle will be filled. Otherwise the candle will be hollow.  
`highSeries` |  `object ([CandlestickSeries](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CandlestickSeries))` The range data (vertical axis) for the high/maximum value for each candle. This is the top of the candle's center line.  
`lowSeries` |  `object ([CandlestickSeries](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CandlestickSeries))` The range data (vertical axis) for the low/minimum value for each candle. This is the bottom of the candle's center line.  
`openSeries` |  `object ([CandlestickSeries](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CandlestickSeries))` The range data (vertical axis) for the open/initial value for each candle. This is the bottom of the candle body. If less than the close value the candle will be filled. Otherwise the candle will be hollow.  
  
## CandlestickDomain

The domain of a CandlestickChart. Fields  
---  
`data` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data of the CandlestickDomain.  
`reversed` |  `boolean` True to reverse the order of the domain values (horizontal axis).  
  
## CandlestickSeries

The series of a CandlestickData. Fields  
---  
`data` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data of the CandlestickSeries.  
  
## CellData

Data about a specific cell. Fields  
---  
`dataSourceFormula` |  `object ([DataSourceFormula](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceFormula))` Output only. Information about a data source formula on the cell. The field is set if user_entered_value is a formula referencing some DATA_SOURCE sheet, e.g. `=SUM(DataSheet!Column)`.  
`dataSourceTable` |  `object ([DataSourceTable](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceTable))` A data source table anchored at this cell. The size of data source table itself is computed dynamically based on its configuration. Only the first cell of the data source table contains the data source table definition. The other cells will contain the display values of the data source table result in their effective_value fields.  
`dataValidation` |  `object ([DataValidationRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataValidationRule))` A data validation rule on the cell, if any. When writing, the new data validation rule will overwrite any prior rule.  
`effectiveFormat` |  `object ([CellFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CellFormat))` The effective format being used by the cell. This includes the results of applying any conditional formatting and, if the cell contains a formula, the computed number format. If the effective format is the default format, effective format will not be written. This field is read-only.  
`effectiveValue` |  `object ([ExtendedValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ExtendedValue))` The effective value of the cell. For cells with formulas, this is the calculated value. For cells with literals, this is the same as the user_entered_value. This field is read-only.  
`formattedValue` |  `string` The formatted value of the cell. This is the value as it's shown to the user. This field is read-only.  
`hyperlink` |  `string` A hyperlink this cell points to, if any. If the cell contains multiple hyperlinks, this field will be empty. This field is read-only. To set it, use a `=HYPERLINK` formula in the userEnteredValue.formulaValue field. A cell-level link can also be set from the userEnteredFormat.textFormat field. Alternatively, set a hyperlink in the textFormatRun.format.link field that spans the entire cell.  
`note` |  `string` Any note on the cell.  
`pivotTable` |  `object ([PivotTable](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotTable))` A pivot table anchored at this cell. The size of pivot table itself is computed dynamically based on its data, grouping, filters, values, etc. Only the top-left cell of the pivot table contains the pivot table definition. The other cells will contain the calculated values of the results of the pivot in their effective_value fields.  
`textFormatRuns[]` |  `object ([TextFormatRun](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormatRun))` Runs of rich text applied to subsections of the cell. Runs are only valid on user entered strings, not formulas, bools, or numbers. Properties of a run start at a specific index in the text and continue until the next run. Runs will inherit the properties of the cell unless explicitly changed. When writing, the new runs will overwrite any prior runs. When writing a new user_entered_value, previous runs are erased.  
`userEnteredFormat` |  `object ([CellFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CellFormat))` The format the user entered for the cell. When writing, the new format will be merged with the existing format.  
`userEnteredValue` |  `object ([ExtendedValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ExtendedValue))` The value the user entered in the cell. e.g, `1234`, `'Hello'`, or `=NOW()` Note: Dates, Times and DateTimes are represented as doubles in serial number format.  
  
## CellFormat

The format of a cell. Fields  
---  
`backgroundColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background color of the cell. Deprecated: Use background_color_style.  
`backgroundColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background color of the cell. If background_color is also set, this field takes precedence.  
`borders` |  `object ([Borders](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Borders))` The borders of the cell.  
`horizontalAlignment` |  `enum` The horizontal alignment of the value in the cell.  
Enum type. Can be one of the following:  
`HORIZONTAL_ALIGN_UNSPECIFIED` | The horizontal alignment is not specified. Do not use this.  
`LEFT` | The text is explicitly aligned to the left of the cell.  
`CENTER` | The text is explicitly aligned to the center of the cell.  
`RIGHT` | The text is explicitly aligned to the right of the cell.  
`hyperlinkDisplayType` |  `enum` If one exists, how a hyperlink should be displayed in the cell.  
Enum type. Can be one of the following:  
`HYPERLINK_DISPLAY_TYPE_UNSPECIFIED` | The default value: the hyperlink is rendered. Do not use this.  
`LINKED` | A hyperlink should be explicitly rendered.  
`PLAIN_TEXT` | A hyperlink should not be rendered.  
`numberFormat` |  `object ([NumberFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#NumberFormat))` A format describing how number values should be represented to the user.  
`padding` |  `object ([Padding](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Padding))` The padding of the cell.  
`textDirection` |  `enum` The direction of the text in the cell.  
Enum type. Can be one of the following:  
`TEXT_DIRECTION_UNSPECIFIED` | The text direction is not specified. Do not use this.  
`LEFT_TO_RIGHT` | The text direction of left-to-right was set by the user.  
`RIGHT_TO_LEFT` | The text direction of right-to-left was set by the user.  
`textFormat` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The format of the text in the cell (unless overridden by a format run). Setting a cell-level link here clears the cell's existing links. Setting the link field in a TextFormatRun takes precedence over the cell-level link.  
`textRotation` |  `object ([TextRotation](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextRotation))` The rotation applied to text in the cell.  
`verticalAlignment` |  `enum` The vertical alignment of the value in the cell.  
Enum type. Can be one of the following:  
`VERTICAL_ALIGN_UNSPECIFIED` | The vertical alignment is not specified. Do not use this.  
`TOP` | The text is explicitly aligned to the top of the cell.  
`MIDDLE` | The text is explicitly aligned to the middle of the cell.  
`BOTTOM` | The text is explicitly aligned to the bottom of the cell.  
`wrapStrategy` |  `enum` The wrap strategy for the value in the cell.  
Enum type. Can be one of the following:  
`WRAP_STRATEGY_UNSPECIFIED` | The default value, do not use.  
`OVERFLOW_CELL` | Lines that are longer than the cell width will be written in the next cell over, so long as that cell is empty. If the next cell over is non-empty, this behaves the same as `CLIP`. The text will never wrap to the next line unless the user manually inserts a new line. Example: | First sentence. | | Manual newline that is very long. <\- Text continues into next cell | Next newline. |  
`LEGACY_WRAP` | This wrap strategy represents the old Google Sheets wrap strategy where words that are longer than a line are clipped rather than broken. This strategy is not supported on all platforms and is being phased out. Example: | Cell has a | | loooooooooo| <\- Word is clipped. | word. |  
`CLIP` | Lines that are longer than the cell width will be clipped. The text will never wrap to the next line unless the user manually inserts a new line. Example: | First sentence. | | Manual newline t| <\- Text is clipped | Next newline. |  
`WRAP` | Words that are longer than a line are wrapped at the character level rather than clipped. Example: | Cell has a | | loooooooooo| <\- Word is broken. | ong word. |  
  
## ChartAxisViewWindowOptions

The options that define a "view window" for a chart (such as the visible values in an axis). Fields  
---  
`viewWindowMax` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum numeric value to be shown in this view window. If unset, will automatically determine a maximum value that looks good for the data.  
`viewWindowMin` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The minimum numeric value to be shown in this view window. If unset, will automatically determine a minimum value that looks good for the data.  
`viewWindowMode` |  `enum` The view window's mode.  
Enum type. Can be one of the following:  
`DEFAULT_VIEW_WINDOW_MODE` | The default view window mode used in the Sheets editor for this chart type. In most cases, if set, the default mode is equivalent to `PRETTY`.  
`VIEW_WINDOW_MODE_UNSUPPORTED` | Do not use. Represents that the currently set mode is not supported by the API.  
`EXPLICIT` | Follows the min and max exactly if specified. If a value is unspecified, it will fall back to the `PRETTY` value.  
`PRETTY` | Chooses a min and max that make the chart look good. Both min and max are ignored in this mode.  
  
## ChartCustomNumberFormatOptions

Custom number formatting options for chart attributes. Fields  
---  
`prefix` |  `string` Custom prefix to be prepended to the chart attribute. This field is optional.  
`suffix` |  `string` Custom suffix to be appended to the chart attribute. This field is optional.  
  
## ChartData

The data included in a domain or series. Fields  
---  
`aggregateType` |  `enum` The aggregation type for the series of a data source chart. Only supported for data source charts.  
Enum type. Can be one of the following:  
`CHART_AGGREGATE_TYPE_UNSPECIFIED` | Default value, do not use.  
`AVERAGE` | Average aggregate function.  
`COUNT` | Count aggregate function.  
`MAX` | Maximum aggregate function.  
`MEDIAN` | Median aggregate function.  
`MIN` | Minimum aggregate function.  
`SUM` | Sum aggregate function.  
`columnReference` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` The reference to the data source column that the data reads from.  
`groupRule` |  `object ([ChartGroupRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartGroupRule))` The rule to group the data by if the ChartData backs the domain of a data source chart. Only supported for data source charts.  
`sourceRange` |  `object ([ChartSourceRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartSourceRange))` The source ranges of the data.  
  
## ChartDateTimeRule

Allows you to organize the date-time values in a source data column into buckets based on selected parts of their date or time values. Fields  
---  
`type` |  `enum` The type of date-time grouping to apply.  
Enum type. Can be one of the following:  
`CHART_DATE_TIME_RULE_TYPE_UNSPECIFIED` | The default type, do not use.  
`SECOND` | Group dates by second, from 0 to 59.  
`MINUTE` | Group dates by minute, from 0 to 59.  
`HOUR` | Group dates by hour using a 24-hour system, from 0 to 23.  
`HOUR_MINUTE` | Group dates by hour and minute using a 24-hour system, for example 19:45.  
`HOUR_MINUTE_AMPM` | Group dates by hour and minute using a 12-hour system, for example 7:45 PM. The AM/PM designation is translated based on the spreadsheet locale.  
`DAY_OF_WEEK` | Group dates by day of week, for example Sunday. The days of the week will be translated based on the spreadsheet locale.  
`DAY_OF_YEAR` | Group dates by day of year, from 1 to 366. Note that dates after Feb. 29 fall in different buckets in leap years than in non-leap years.  
`DAY_OF_MONTH` | Group dates by day of month, from 1 to 31.  
`DAY_MONTH` | Group dates by day and month, for example 22-Nov. The month is translated based on the spreadsheet locale.  
`MONTH` | Group dates by month, for example Nov. The month is translated based on the spreadsheet locale.  
`QUARTER` | Group dates by quarter, for example Q1 (which represents Jan-Mar).  
`YEAR` | Group dates by year, for example 2008.  
`YEAR_MONTH` | Group dates by year and month, for example 2008-Nov. The month is translated based on the spreadsheet locale.  
`YEAR_QUARTER` | Group dates by year and quarter, for example 2008 Q4.  
`YEAR_MONTH_DAY` | Group dates by year, month, and day, for example 2008-11-22.  
  
## ChartGroupRule

An optional setting on the ChartData of the domain of a data source chart that defines buckets for the values in the domain rather than breaking out each individual value. For example, when plotting a data source chart, you can specify a histogram rule on the domain (it should only contain numeric values), grouping its values into buckets. Any values of a chart series that fall into the same bucket are aggregated based on the aggregate_type. Fields  
---  
`dateTimeRule` |  `object ([ChartDateTimeRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartDateTimeRule))` A ChartDateTimeRule.  
`histogramRule` |  `object ([ChartHistogramRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartHistogramRule))` A ChartHistogramRule  
  
## ChartHistogramRule

Allows you to organize numeric values in a source data column into buckets of constant size. Fields  
---  
`intervalSize` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The size of the buckets that are created. Must be positive.  
`maxValue` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum value at which items are placed into buckets. Values greater than the maximum are grouped into a single bucket. If omitted, it is determined by the maximum item value.  
`minValue` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The minimum value at which items are placed into buckets. Values that are less than the minimum are grouped into a single bucket. If omitted, it is determined by the minimum item value.  
  
## ChartSourceRange

Source ranges for a chart. Fields  
---  
`sources[]` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The ranges of data for a series or domain. Exactly one dimension must have a length of 1, and all sources in the list must have the same dimension with length 1. The domain (if it exists) & all series must have the same number of source ranges. If using more than one source range, then the source range at a given offset must be in order and contiguous across the domain and series. For example, these are valid configurations: domain sources: A1:A5 series1 sources: B1:B5 series2 sources: D6:D10 domain sources: A1:A5, C10:C12 series1 sources: B1:B5, D10:D12 series2 sources: C1:C5, E10:E12  
  
## ChartSpec

The specifications of a chart. Fields  
---  
`altText` |  `string` The alternative text that describes the chart. This is often used for accessibility.  
`backgroundColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background color of the entire chart. Not applicable to Org charts. Deprecated: Use background_color_style.  
`backgroundColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background color of the entire chart. Not applicable to Org charts. If background_color is also set, this field takes precedence.  
`basicChart` |  `object ([BasicChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BasicChartSpec))` A basic chart specification, can be one of many kinds of charts. See BasicChartType for the list of all charts this supports.  
`bubbleChart` |  `object ([BubbleChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BubbleChartSpec))` A bubble chart specification.  
`candlestickChart` |  `object ([CandlestickChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CandlestickChartSpec))` A candlestick chart specification.  
`dataSourceChartProperties` |  `object ([DataSourceChartProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceChartProperties))` If present, the field contains data source chart specific properties.  
`filterSpecs[]` |  `object ([FilterSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterSpec))` The filters applied to the source data of the chart. Only supported for data source charts.  
`fontName` |  `string` The name of the font to use by default for all chart text (e.g. title, axis labels, legend). If a font is specified for a specific part of the chart it will override this font name.  
`hiddenDimensionStrategy` |  `enum` Determines how the charts will use hidden rows or columns.  
Enum type. Can be one of the following:  
`CHART_HIDDEN_DIMENSION_STRATEGY_UNSPECIFIED` | Default value, do not use.  
`SKIP_HIDDEN_ROWS_AND_COLUMNS` | Charts will skip hidden rows and columns.  
`SKIP_HIDDEN_ROWS` | Charts will skip hidden rows only.  
`SKIP_HIDDEN_COLUMNS` | Charts will skip hidden columns only.  
`SHOW_ALL` | Charts will not skip any hidden rows or columns.  
`histogramChart` |  `object ([HistogramChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#HistogramChartSpec))` A histogram chart specification.  
`maximized` |  `boolean` True to make a chart fill the entire space in which it's rendered with minimum padding. False to use the default padding. (Not applicable to Geo and Org charts.)  
`orgChart` |  `object ([OrgChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#OrgChartSpec))` An org chart specification.  
`pieChart` |  `object ([PieChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PieChartSpec))` A pie chart specification.  
`scorecardChart` |  `object ([ScorecardChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ScorecardChartSpec))` A scorecard chart specification.  
`sortSpecs[]` |  `object ([SortSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SortSpec))` The order to sort the chart data by. Only a single sort spec is supported. Only supported for data source charts.  
`subtitle` |  `string` The subtitle of the chart.  
`subtitleTextFormat` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The subtitle text format. Strikethrough, underline, and link are not supported.  
`subtitleTextPosition` |  `object ([TextPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextPosition))` The subtitle text position. This field is optional.  
`title` |  `string` The title of the chart.  
`titleTextFormat` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The title text format. Strikethrough, underline, and link are not supported.  
`titleTextPosition` |  `object ([TextPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextPosition))` The title text position. This field is optional.  
`treemapChart` |  `object ([TreemapChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TreemapChartSpec))` A treemap chart specification.  
`waterfallChart` |  `object ([WaterfallChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#WaterfallChartSpec))` A waterfall chart specification.  
  
## ClearBasicFilterRequest

Clears the basic filter, if any exists on the sheet. Fields  
---  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet ID on which the basic filter should be cleared.  
  
## ClearValuesResponse

The response when clearing a range of values in a spreadsheet. Fields  
---  
`clearedRange` |  `string` The range (in A1 notation) that was cleared. (If the request was for an unbounded range or a ranger larger than the bounds of the sheet, this will be the actual range that was cleared, bounded to the sheet's limits.)  
`spreadsheetId` |  `string` The spreadsheet the updates were applied to.  
  
## Color

Represents a color in the RGBA color space. This representation is designed for simplicity of conversion to/from color representations in various languages over compactness. For example, the fields of this representation can be trivially provided to the constructor of `java.awt.Color` in Java; it can also be trivially provided to UIColor's `+colorWithRed:green:blue:alpha` method in iOS; and, with just a little work, it can be easily formatted into a CSS `rgba()` string in JavaScript. This reference page doesn't carry information about the absolute color space that should be used to interpret the RGB value (e.g. sRGB, Adobe RGB, DCI-P3, BT.2020, etc.). By default, applications should assume the sRGB color space. When color equality needs to be decided, implementations, unless documented otherwise, treat two colors as equal if all their red, green, blue, and alpha values each differ by at most 1e-5. Example (Java): import com.google.type.Color; // ... public static java.awt.Color fromProto(Color protocolor) { float alpha = protocolor.hasAlpha() ? protocolor.getAlpha().getValue() : 1.0; return new java.awt.Color( protocolor.getRed(), protocolor.getGreen(), protocolor.getBlue(), alpha); } public static Color toProto(java.awt.Color color) { float red = (float) color.getRed(); float green = (float) color.getGreen(); float blue = (float) color.getBlue(); float denominator = 255.0; Color.Builder resultBuilder = Color .newBuilder() .setRed(red / denominator) .setGreen(green / denominator) .setBlue(blue / denominator); int alpha = color.getAlpha(); if (alpha != 255) { result.setAlpha( FloatValue .newBuilder() .setValue(((float) alpha) / denominator) .build()); } return resultBuilder.build(); } // ... Example (iOS / Obj-C): // ... static UIColor _fromProto(Color_ protocolor) { float red = [protocolor red]; float green = [protocolor green]; float blue = [protocolor blue]; FloatValue _alpha_wrapper = [protocolor alpha]; float alpha = 1.0; if (alpha_wrapper != nil) { alpha = [alpha_wrapper value]; } return [UIColor colorWithRed:red green:green blue:blue alpha:alpha]; } static Color_ toProto(UIColor _color) { CGFloat red, green, blue, alpha; if (![color getRed: &red green:&green blue:&blue alpha:&alpha]) { return nil; } Color_ result = [[Color alloc] init]; [result setRed:red]; [result setGreen:green]; [result setBlue:blue]; if (alpha <= 0.9999) { [result setAlpha:floatWrapperWithValue(alpha)]; } [result autorelease]; return result; } // ... Example (JavaScript): // ... var protoToCssColor = function(rgb_color) { var redFrac = rgb_color.red || 0.0; var greenFrac = rgb_color.green || 0.0; var blueFrac = rgb_color.blue || 0.0; var red = Math.floor(redFrac * 255); var green = Math.floor(greenFrac * 255); var blue = Math.floor(blueFrac * 255); if (!('alpha' in rgb_color)) { return rgbToCssColor(red, green, blue); } var alphaFrac = rgb_color.alpha.value || 0.0; var rgbParams = [red, green, blue].join(','); return ['rgba(', rgbParams, ',', alphaFrac, ')'].join(''); }; var rgbToCssColor = function(red, green, blue) { var rgbNumber = new Number((red << 16) | (green << 8) | blue); var hexString = rgbNumber.toString(16); var missingZeros = 6 - hexString.length; var resultBuilder = ['#']; for (var i = 0; i < missingZeros; i++) { resultBuilder.push('0'); } resultBuilder.push(hexString); return resultBuilder.join(''); }; // ... Fields  
---  
`alpha` |  `number ([float](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The fraction of this color that should be applied to the pixel. That is, the final pixel color is defined by the equation: `pixel color = alpha * (this color) + (1.0 - alpha) * (background color)` This means that a value of 1.0 corresponds to a solid color, whereas a value of 0.0 corresponds to a completely transparent color. This uses a wrapper message rather than a simple float scalar so that it is possible to distinguish between a default value and the value being unset. If omitted, this color object is rendered as a solid color (as if the alpha value had been explicitly given a value of 1.0).  
`blue` |  `number ([float](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The amount of blue in the color as a value in the interval [0, 1].  
`green` |  `number ([float](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The amount of green in the color as a value in the interval [0, 1].  
`red` |  `number ([float](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The amount of red in the color as a value in the interval [0, 1].  
  
## ColorStyle

A color value. Fields  
---  
`rgbColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` RGB color. The [`alpha`](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#Color.FIELDS.alpha) value in the [`Color`](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/other#color) object isn't generally supported.  
`themeColor` |  `enum` Theme color.  
Enum type. Can be one of the following:  
`THEME_COLOR_TYPE_UNSPECIFIED` | Unspecified theme color  
`TEXT` | Represents the primary text color  
`BACKGROUND` | Represents the primary background color  
`ACCENT1` | Represents the first accent color  
`ACCENT2` | Represents the second accent color  
`ACCENT3` | Represents the third accent color  
`ACCENT4` | Represents the fourth accent color  
`ACCENT5` | Represents the fifth accent color  
`ACCENT6` | Represents the sixth accent color  
`LINK` | Represents the color to use for hyperlinks  
  
## ConditionValue

The value of the condition. Fields  
---  
`relativeDate` |  `enum` A relative date (based on the current date). Valid only if the type is DATE_BEFORE, DATE_AFTER, DATE_ON_OR_BEFORE or DATE_ON_OR_AFTER. Relative dates are not supported in data validation. They are supported only in conditional formatting and conditional filters.  
Enum type. Can be one of the following:  
`RELATIVE_DATE_UNSPECIFIED` | Default value, do not use.  
`PAST_YEAR` | The value is one year before today.  
`PAST_MONTH` | The value is one month before today.  
`PAST_WEEK` | The value is one week before today.  
`YESTERDAY` | The value is yesterday.  
`TODAY` | The value is today.  
`TOMORROW` | The value is tomorrow.  
`userEnteredValue` |  `string` A value the condition is based on. The value is parsed as if the user typed into a cell. Formulas are supported (and must begin with an `=` or a '+').  
  
## ConditionalFormatRule

A rule describing a conditional format. Fields  
---  
`booleanRule` |  `object ([BooleanRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BooleanRule))` The formatting is either "on" or "off" according to the rule.  
`gradientRule` |  `object ([GradientRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GradientRule))` The formatting will vary based on the gradients in the rule.  
`ranges[]` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The ranges that are formatted if the condition is true. All the ranges must be on the same grid.  
  
## CopyPasteRequest

Copies data from the source to the destination. Fields  
---  
`destination` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The location to paste to. If the range covers a span that's a multiple of the source's height or width, then the data will be repeated to fill in the destination range. If the range is smaller than the source range, the entire source data will still be copied (beyond the end of the destination range).  
`pasteOrientation` |  `enum` How that data should be oriented when pasting.  
Enum type. Can be one of the following:  
`NORMAL` | Paste normally.  
`TRANSPOSE` | Paste transposed, where all rows become columns and vice versa.  
`pasteType` |  `enum` What kind of data to paste.  
Enum type. Can be one of the following:  
`PASTE_NORMAL` | Paste values, formulas, formats, and merges.  
`PASTE_VALUES` | Paste the values ONLY without formats, formulas, or merges.  
`PASTE_FORMAT` | Paste the format and data validation only.  
`PASTE_NO_BORDERS` | Like `PASTE_NORMAL` but without borders.  
`PASTE_FORMULA` | Paste the formulas only.  
`PASTE_DATA_VALIDATION` | Paste the data validation only.  
`PASTE_CONDITIONAL_FORMATTING` | Paste the conditional formatting rules only.  
`source` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The source range to copy.  
  
## CopySheetToAnotherSpreadsheetRequest

The request to copy a sheet across spreadsheets. Fields  
---  
`destinationSpreadsheetId` |  `string` The ID of the spreadsheet to copy the sheet to.  
  
## CreateDeveloperMetadataRequest

A request to create developer metadata. Fields  
---  
`developerMetadata` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The developer metadata to create.  
  
## CreateDeveloperMetadataResponse

The response from creating developer metadata. Fields  
---  
`developerMetadata` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The developer metadata that was created.  
  
## CutPasteRequest

Moves data from the source to the destination. Fields  
---  
`destination` |  `object ([GridCoordinate](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridCoordinate))` The top-left coordinate where the data should be pasted.  
`pasteType` |  `enum` What kind of data to paste. All the source data will be cut, regardless of what is pasted.  
Enum type. Can be one of the following:  
`PASTE_NORMAL` | Paste values, formulas, formats, and merges.  
`PASTE_VALUES` | Paste the values ONLY without formats, formulas, or merges.  
`PASTE_FORMAT` | Paste the format and data validation only.  
`PASTE_NO_BORDERS` | Like `PASTE_NORMAL` but without borders.  
`PASTE_FORMULA` | Paste the formulas only.  
`PASTE_DATA_VALIDATION` | Paste the data validation only.  
`PASTE_CONDITIONAL_FORMATTING` | Paste the conditional formatting rules only.  
`source` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The source data to cut.  
  
## DataExecutionStatus

The data execution status. A data execution is created to sync a data source object with the latest data from a DataSource. It is usually scheduled to run at background, you can check its state to tell if an execution completes There are several scenarios where a data execution is triggered to run: * Adding a data source creates an associated data source sheet as well as a data execution to sync the data from the data source to the sheet. * Updating a data source creates a data execution to refresh the associated data source sheet similarly. * You can send refresh request to explicitly refresh one or multiple data source objects. Fields  
---  
`errorCode` |  `enum` The error code.  
Enum type. Can be one of the following:  
`DATA_EXECUTION_ERROR_CODE_UNSPECIFIED` | Default value, do not use.  
`TIMED_OUT` | The data execution timed out.  
`TOO_MANY_ROWS` | The data execution returns more rows than the limit.  
`TOO_MANY_COLUMNS` | The data execution returns more columns than the limit.  
`TOO_MANY_CELLS` | The data execution returns more cells than the limit.  
`ENGINE` | Error is received from the backend data execution engine (e.g. BigQuery). Check error_message for details.  
`PARAMETER_INVALID` | One or some of the provided data source parameters are invalid.  
`UNSUPPORTED_DATA_TYPE` | The data execution returns an unsupported data type.  
`DUPLICATE_COLUMN_NAMES` | The data execution returns duplicate column names or aliases.  
`INTERRUPTED` | The data execution is interrupted. Please refresh later.  
`CONCURRENT_QUERY` | The data execution is currently in progress, can not be refreshed until it completes.  
`OTHER` | Other errors.  
`TOO_MANY_CHARS_PER_CELL` | The data execution returns values that exceed the maximum characters allowed in a single cell.  
`DATA_NOT_FOUND` | The database referenced by the data source is not found. */  
`PERMISSION_DENIED` | The user does not have access to the database referenced by the data source.  
`MISSING_COLUMN_ALIAS` | The data execution returns columns with missing aliases.  
`OBJECT_NOT_FOUND` | The data source object does not exist.  
`OBJECT_IN_ERROR_STATE` | The data source object is currently in error state. To force refresh, set force in RefreshDataSourceRequest.  
`OBJECT_SPEC_INVALID` | The data source object specification is invalid.  
`errorMessage` |  `string` The error message, which may be empty.  
`lastRefreshTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Gets the time the data last successfully refreshed.  
`state` |  `enum` The state of the data execution.  
Enum type. Can be one of the following:  
`DATA_EXECUTION_STATE_UNSPECIFIED` | Default value, do not use.  
`NOT_STARTED` | The data execution has not started.  
`RUNNING` | The data execution has started and is running.  
`SUCCEEDED` | The data execution has completed successfully.  
`FAILED` | The data execution has completed with errors.  
  
## DataFilter

Filter that describes what data should be selected or returned from a request. Fields  
---  
`a1Range` |  `string` Selects data that matches the specified A1 range.  
`developerMetadataLookup` |  `object ([DeveloperMetadataLookup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadataLookup))` Selects data associated with the developer metadata matching the criteria described by this DeveloperMetadataLookup.  
`gridRange` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` Selects data that matches the range described by the GridRange.  
  
## DataFilterValueRange

A range of values whose location is specified by a DataFilter. Fields  
---  
`dataFilter` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The data filter describing the location of the values in the spreadsheet.  
`majorDimension` |  `enum` The major dimension of the values.  
Enum type. Can be one of the following:  
`DIMENSION_UNSPECIFIED` | The default value, do not use.  
`ROWS` | Operates on the rows of a sheet.  
`COLUMNS` | Operates on the columns of a sheet.  
`values[]` |  `array` The data to be written. If the provided values exceed any of the ranges matched by the data filter then the request fails. If the provided values are less than the matched ranges only the specified values are written, existing values in the matched ranges remain unaffected.  
  
## DataLabel

Settings for one set of data labels. Data labels are annotations that appear next to a set of data, such as the points on a line chart, and provide additional information about what the data represents, such as a text representation of the value behind that point on the graph. Fields  
---  
`customLabelData` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` Data to use for custom labels. Only used if type is set to CUSTOM. This data must be the same length as the series or other element this data label is applied to. In addition, if the series is split into multiple source ranges, this source data must come from the next column in the source data. For example, if the series is B2:B4,E6:E8 then this data must come from C2:C4,F6:F8.  
`placement` |  `enum` The placement of the data label relative to the labeled data.  
Enum type. Can be one of the following:  
`DATA_LABEL_PLACEMENT_UNSPECIFIED` | The positioning is determined automatically by the renderer.  
`CENTER` | Center within a bar or column, both horizontally and vertically.  
`LEFT` | To the left of a data point.  
`RIGHT` | To the right of a data point.  
`ABOVE` | Above a data point.  
`BELOW` | Below a data point.  
`INSIDE_END` | Inside a bar or column at the end (top if positive, bottom if negative).  
`INSIDE_BASE` | Inside a bar or column at the base.  
`OUTSIDE_END` | Outside a bar or column at the end.  
`textFormat` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The text format used for the data label. The link field is not supported.  
`type` |  `enum` The type of the data label.  
Enum type. Can be one of the following:  
`DATA_LABEL_TYPE_UNSPECIFIED` | The data label type is not specified and will be interpreted depending on the context of the data label within the chart.  
`NONE` | The data label is not displayed.  
`DATA` | The data label is displayed using values from the series data.  
`CUSTOM` | The data label is displayed using values from a custom data source indicated by customLabelData.  
  
## DataSource

Information about an external data source in the spreadsheet. Fields  
---  
`calculatedColumns[]` |  `object ([DataSourceColumn](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumn))` All calculated columns in the data source.  
`dataSourceId` |  `string` The spreadsheet-scoped unique ID that identifies the data source. Example: 1080547365.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the Sheet connected with the data source. The field cannot be changed once set. When creating a data source, an associated DATA_SOURCE sheet is also created, if the field is not specified, the ID of the created sheet will be randomly generated.  
`spec` |  `object ([DataSourceSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceSpec))` The DataSourceSpec for the data source connected with this spreadsheet.  
  
## DataSourceChartProperties

Properties of a data source chart. Fields  
---  
`dataExecutionStatus` |  `object ([DataExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataExecutionStatus))` Output only. The data execution status.  
`dataSourceId` |  `string` ID of the data source that the chart is associated with.  
  
## DataSourceColumn

A column in a data source. Fields  
---  
`formula` |  `string` The formula of the calculated column.  
`reference` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` The column reference.  
  
## DataSourceColumnReference

An unique identifier that references a data source column. Fields  
---  
`name` |  `string` The display name of the column. It should be unique within a data source.  
  
## DataSourceFormula

A data source formula. Fields  
---  
`dataExecutionStatus` |  `object ([DataExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataExecutionStatus))` Output only. The data execution status.  
`dataSourceId` |  `string` The ID of the data source the formula is associated with.  
  
## DataSourceObjectReference

Reference to a data source object. Fields  
---  
`chartId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` References to a data source chart.  
`dataSourceFormulaCell` |  `object ([GridCoordinate](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridCoordinate))` References to a cell containing DataSourceFormula.  
`dataSourcePivotTableAnchorCell` |  `object ([GridCoordinate](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridCoordinate))` References to a data source PivotTable anchored at the cell.  
`dataSourceTableAnchorCell` |  `object ([GridCoordinate](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridCoordinate))` References to a DataSourceTable anchored at the cell.  
`sheetId` |  `string` References to a DATA_SOURCE sheet.  
  
## DataSourceObjectReferences

A list of references to data source objects. Fields  
---  
`references[]` |  `object ([DataSourceObjectReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceObjectReference))` The references.  
  
## DataSourceParameter

A parameter in a data source's query. The parameter allows the user to pass in values from the spreadsheet into a query. Fields  
---  
`name` |  `string` Named parameter. Must be a legitimate identifier for the DataSource that supports it. For example, [BigQuery identifier](https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#identifiers).  
`namedRangeId` |  `string` ID of a NamedRange. Its size must be 1x1.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` A range that contains the value of the parameter. Its size must be 1x1.  
  
## DataSourceRefreshDailySchedule

A schedule for data to refresh every day in a given time interval. Fields  
---  
`startTime` |  `object ([TimeOfDay](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TimeOfDay))` The start time of a time interval in which a data source refresh is scheduled. Only `hours` part is used. The time interval size defaults to that in the Sheets editor.  
  
## DataSourceRefreshMonthlySchedule

A monthly schedule for data to refresh on specific days in the month in a given time interval. Fields  
---  
`daysOfMonth[]` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Days of the month to refresh. Only 1-28 are supported, mapping to the 1st to the 28th day. At lesat one day must be specified.  
`startTime` |  `object ([TimeOfDay](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TimeOfDay))` The start time of a time interval in which a data source refresh is scheduled. Only `hours` part is used. The time interval size defaults to that in the Sheets editor.  
  
## DataSourceRefreshSchedule

Schedule for refreshing the data source. Data sources in the spreadsheet are refreshed within a time interval. You can specify the start time by clicking the Scheduled Refresh button in the Sheets editor, but the interval is fixed at 4 hours. For example, if you specify a start time of 8am , the refresh will take place between 8am and 12pm every day. Fields  
---  
`dailySchedule` |  `object ([DataSourceRefreshDailySchedule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceRefreshDailySchedule))` Daily refresh schedule.  
`enabled` |  `boolean` True if the refresh schedule is enabled, or false otherwise.  
`monthlySchedule` |  `object ([DataSourceRefreshMonthlySchedule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceRefreshMonthlySchedule))` Monthly refresh schedule.  
`nextRun` |  `object ([Interval](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Interval))` Output only. The time interval of the next run.  
`refreshScope` |  `enum` The scope of the refresh. Must be ALL_DATA_SOURCES.  
Enum type. Can be one of the following:  
`DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED` | Default value, do not use.  
`ALL_DATA_SOURCES` | Refreshes all data sources and their associated data source objects in the spreadsheet.  
`weeklySchedule` |  `object ([DataSourceRefreshWeeklySchedule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceRefreshWeeklySchedule))` Weekly refresh schedule.  
  
## DataSourceRefreshWeeklySchedule

A weekly schedule for data to refresh on specific days in a given time interval. Fields  
---  
`daysOfWeek[]` |  `string` Days of the week to refresh. At least one day must be specified.  
`startTime` |  `object ([TimeOfDay](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TimeOfDay))` The start time of a time interval in which a data source refresh is scheduled. Only `hours` part is used. The time interval size defaults to that in the Sheets editor.  
  
## DataSourceSheetDimensionRange

A range along a single dimension on a DATA_SOURCE sheet. Fields  
---  
`columnReferences[]` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` The columns on the data source sheet.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the data source sheet the range is on.  
  
## DataSourceSheetProperties

Additional properties of a DATA_SOURCE sheet. Fields  
---  
`columns[]` |  `object ([DataSourceColumn](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumn))` The columns displayed on the sheet, corresponding to the values in RowData.  
`dataExecutionStatus` |  `object ([DataExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataExecutionStatus))` The data execution status.  
`dataSourceId` |  `string` ID of the DataSource the sheet is connected to.  
  
## DataSourceSpec

This specifies the details of the data source. For example, for BigQuery, this specifies information about the BigQuery source. Fields  
---  
`bigQuery` |  `object ([BigQueryDataSourceSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BigQueryDataSourceSpec))` A BigQueryDataSourceSpec.  
`parameters[]` |  `object ([DataSourceParameter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceParameter))` The parameters of the data source, used when querying the data source.  
  
## DataSourceTable

A data source table, which allows the user to import a static table of data from the DataSource into Sheets. This is also known as "Extract" in the Sheets editor. Fields  
---  
`columnSelectionType` |  `enum` The type to select columns for the data source table. Defaults to SELECTED.  
Enum type. Can be one of the following:  
`DATA_SOURCE_TABLE_COLUMN_SELECTION_TYPE_UNSPECIFIED` | The default column selection type, do not use.  
`SELECTED` | Select columns specified by columns field.  
`SYNC_ALL` | Sync all current and future columns in the data source. If set, the data source table fetches all the columns in the data source at the time of refresh.  
`columns[]` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` Columns selected for the data source table. The column_selection_type must be SELECTED.  
`dataExecutionStatus` |  `object ([DataExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataExecutionStatus))` Output only. The data execution status.  
`dataSourceId` |  `string` The ID of the data source the data source table is associated with.  
`filterSpecs[]` |  `object ([FilterSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterSpec))` Filter specifications in the data source table.  
`rowLimit` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The limit of rows to return. If not set, a default limit is applied. Please refer to the Sheets editor for the default and max limit.  
`sortSpecs[]` |  `object ([SortSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SortSpec))` Sort specifications in the data source table. The result of the data source table is sorted based on the sort specifications in order.  
  
## DataValidationRule

A data validation rule. Fields  
---  
`condition` |  `object ([BooleanCondition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BooleanCondition))` The condition that data in the cell must match.  
`inputMessage` |  `string` A message to show the user when adding data to the cell.  
`showCustomUi` |  `boolean` True if the UI should be customized based on the kind of condition. If true, "List" conditions will show a dropdown.  
`strict` |  `boolean` True if invalid data should be rejected.  
  
## DateTimeRule

Allows you to organize the date-time values in a source data column into buckets based on selected parts of their date or time values. For example, consider a pivot table showing sales transactions by date: +----------+--------------+ | Date | SUM of Sales | +----------+--------------+ | 1/1/2017 | $621.14 | | 2/3/2017 | $708.84 | | 5/8/2017 | $326.84 | ... +----------+--------------+ Applying a date-time group rule with a DateTimeRuleType of YEAR_MONTH results in the following pivot table. +--------------+--------------+ | Grouped Date | SUM of Sales | +--------------+--------------+ | 2017-Jan | $53,731.78 | | 2017-Feb | $83,475.32 | | 2017-Mar | $94,385.05 | ... +--------------+--------------+ Fields  
---  
`type` |  `enum` The type of date-time grouping to apply.  
Enum type. Can be one of the following:  
`DATE_TIME_RULE_TYPE_UNSPECIFIED` | The default type, do not use.  
`SECOND` | Group dates by second, from 0 to 59.  
`MINUTE` | Group dates by minute, from 0 to 59.  
`HOUR` | Group dates by hour using a 24-hour system, from 0 to 23.  
`HOUR_MINUTE` | Group dates by hour and minute using a 24-hour system, for example 19:45.  
`HOUR_MINUTE_AMPM` | Group dates by hour and minute using a 12-hour system, for example 7:45 PM. The AM/PM designation is translated based on the spreadsheet locale.  
`DAY_OF_WEEK` | Group dates by day of week, for example Sunday. The days of the week will be translated based on the spreadsheet locale.  
`DAY_OF_YEAR` | Group dates by day of year, from 1 to 366. Note that dates after Feb. 29 fall in different buckets in leap years than in non-leap years.  
`DAY_OF_MONTH` | Group dates by day of month, from 1 to 31.  
`DAY_MONTH` | Group dates by day and month, for example 22-Nov. The month is translated based on the spreadsheet locale.  
`MONTH` | Group dates by month, for example Nov. The month is translated based on the spreadsheet locale.  
`QUARTER` | Group dates by quarter, for example Q1 (which represents Jan-Mar).  
`YEAR` | Group dates by year, for example 2008.  
`YEAR_MONTH` | Group dates by year and month, for example 2008-Nov. The month is translated based on the spreadsheet locale.  
`YEAR_QUARTER` | Group dates by year and quarter, for example 2008 Q4.  
`YEAR_MONTH_DAY` | Group dates by year, month, and day, for example 2008-11-22.  
  
## DeleteBandingRequest

Removes the banded range with the given ID from the spreadsheet. Fields  
---  
`bandedRangeId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the banded range to delete.  
  
## DeleteConditionalFormatRuleRequest

Deletes a conditional format rule at the given index. All subsequent rules' indexes are decremented. Fields  
---  
`index` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The zero-based index of the rule to be deleted.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet the rule is being deleted from.  
  
## DeleteConditionalFormatRuleResponse

The result of deleting a conditional format rule. Fields  
---  
`rule` |  `object ([ConditionalFormatRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ConditionalFormatRule))` The rule that was deleted.  
  
## DeleteDataSourceRequest

Deletes a data source. The request also deletes the associated data source sheet, and unlinks all associated data source objects. Fields  
---  
`dataSourceId` |  `string` The ID of the data source to delete.  
  
## DeleteDeveloperMetadataRequest

A request to delete developer metadata. Fields  
---  
`dataFilter` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The data filter describing the criteria used to select which developer metadata entry to delete.  
  
## DeleteDeveloperMetadataResponse

The response from deleting developer metadata. Fields  
---  
`deletedDeveloperMetadata[]` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The metadata that was deleted.  
  
## DeleteDimensionGroupRequest

Deletes a group over the specified range by decrementing the depth of the dimensions in the range. For example, assume the sheet has a depth-1 group over B:E and a depth-2 group over C:D. Deleting a group over D:E leaves the sheet with a depth-1 group over B:D and a depth-2 group over C:C. Fields  
---  
`range` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The range of the group to be deleted.  
  
## DeleteDimensionGroupResponse

The result of deleting a group. Fields  
---  
`dimensionGroups[]` |  `object ([DimensionGroup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionGroup))` All groups of a dimension after deleting a group from that dimension.  
  
## DeleteDimensionRequest

Deletes the dimensions from the sheet. Fields  
---  
`range` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The dimensions to delete from the sheet.  
  
## DeleteDuplicatesRequest

Removes rows within this range that contain values in the specified columns that are duplicates of values in any previous row. Rows with identical values but different letter cases, formatting, or formulas are considered to be duplicates. This request also removes duplicate rows hidden from view (for example, due to a filter). When removing duplicates, the first instance of each duplicate row scanning from the top downwards is kept in the resulting range. Content outside of the specified range isn't removed, and rows considered duplicates do not have to be adjacent to each other in the range. Fields  
---  
`comparisonColumns[]` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The columns in the range to analyze for duplicate values. If no columns are selected then all columns are analyzed for duplicates.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range to remove duplicates rows from.  
  
## DeleteDuplicatesResponse

The result of removing duplicates in a range. Fields  
---  
`duplicatesRemovedCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of duplicate rows removed.  
  
## DeleteEmbeddedObjectRequest

Deletes the embedded object with the given ID. Fields  
---  
`objectId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the embedded object to delete.  
  
## DeleteFilterViewRequest

Deletes a particular filter view. Fields  
---  
`filterId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the filter to delete.  
  
## DeleteNamedRangeRequest

Removes the named range with the given ID from the spreadsheet. Fields  
---  
`namedRangeId` |  `string` The ID of the named range to delete.  
  
## DeleteProtectedRangeRequest

Deletes the protected range with the given ID. Fields  
---  
`protectedRangeId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the protected range to delete.  
  
## DeleteRangeRequest

Deletes a range of cells, shifting other cells into the deleted area. Fields  
---  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range of cells to delete.  
`shiftDimension` |  `enum` The dimension from which deleted cells will be replaced with. If ROWS, existing cells will be shifted upward to replace the deleted cells. If COLUMNS, existing cells will be shifted left to replace the deleted cells.  
Enum type. Can be one of the following:  
`DIMENSION_UNSPECIFIED` | The default value, do not use.  
`ROWS` | Operates on the rows of a sheet.  
`COLUMNS` | Operates on the columns of a sheet.  
  
## DeleteSheetRequest

Deletes the requested sheet. Fields  
---  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the sheet to delete. If the sheet is of DATA_SOURCE type, the associated DataSource is also deleted.  
  
## DeveloperMetadata

Developer metadata associated with a location or object in a spreadsheet. Developer metadata may be used to associate arbitrary data with various parts of a spreadsheet and will remain associated at those locations as they move around and the spreadsheet is edited. For example, if developer metadata is associated with row 5 and another row is then subsequently inserted above row 5, that original metadata will still be associated with the row it was first associated with (what is now row 6). If the associated object is deleted its metadata is deleted too. Fields  
---  
`location` |  `object ([DeveloperMetadataLocation](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadataLocation))` The location where the metadata is associated.  
`metadataId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The spreadsheet-scoped unique ID that identifies the metadata. IDs may be specified when metadata is created, otherwise one will be randomly generated and assigned. Must be positive.  
`metadataKey` |  `string` The metadata key. There may be multiple metadata in a spreadsheet with the same key. Developer metadata must always have a key specified.  
`metadataValue` |  `string` Data associated with the metadata's key.  
`visibility` |  `enum` The metadata visibility. Developer metadata must always have a visibility specified.  
Enum type. Can be one of the following:  
`DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED` | Default value.  
`DOCUMENT` | Document-visible metadata is accessible from any developer project with access to the document.  
`PROJECT` | Project-visible metadata is only visible to and accessible by the developer project that created the metadata.  
  
## DeveloperMetadataLocation

A location where metadata may be associated in a spreadsheet. Fields  
---  
`dimensionRange` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` Represents the row or column when metadata is associated with a dimension. The specified DimensionRange must represent a single row or column; it cannot be unbounded or span multiple rows or columns.  
`locationType` |  `enum` The type of location this object represents. This field is read-only.  
Enum type. Can be one of the following:  
`DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED` | Default value.  
`ROW` | Developer metadata associated on an entire row dimension.  
`COLUMN` | Developer metadata associated on an entire column dimension.  
`SHEET` | Developer metadata associated on an entire sheet.  
`SPREADSHEET` | Developer metadata associated on the entire spreadsheet.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the sheet when metadata is associated with an entire sheet.  
`spreadsheet` |  `boolean` True when metadata is associated with an entire spreadsheet.  
  
## DeveloperMetadataLookup

Selects DeveloperMetadata that matches all of the specified fields. For example, if only a metadata ID is specified this considers the DeveloperMetadata with that particular unique ID. If a metadata key is specified, this considers all developer metadata with that key. If a key, visibility, and location type are all specified, this considers all developer metadata with that key and visibility that are associated with a location of that type. In general, this selects all DeveloperMetadata that matches the intersection of all the specified fields; any field or combination of fields may be specified. Fields  
---  
`locationMatchingStrategy` |  `enum` Determines how this lookup matches the location. If this field is specified as EXACT, only developer metadata associated on the exact location specified is matched. If this field is specified to INTERSECTING, developer metadata associated on intersecting locations is also matched. If left unspecified, this field assumes a default value of INTERSECTING. If this field is specified, a metadataLocation must also be specified.  
Enum type. Can be one of the following:  
`DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED` | Default value. This value must not be used.  
`EXACT_LOCATION` | Indicates that a specified location should be matched exactly. For example, if row three were specified as a location this matching strategy would only match developer metadata also associated on row three. Metadata associated on other locations would not be considered.  
`INTERSECTING_LOCATION` | Indicates that a specified location should match that exact location as well as any intersecting locations. For example, if row three were specified as a location this matching strategy would match developer metadata associated on row three as well as metadata associated on locations that intersect row three. If, for instance, there was developer metadata associated on column B, this matching strategy would also match that location because column B intersects row three.  
`locationType` |  `enum` Limits the selected developer metadata to those entries which are associated with locations of the specified type. For example, when this field is specified as ROW this lookup only considers developer metadata associated on rows. If the field is left unspecified, all location types are considered. This field cannot be specified as SPREADSHEET when the locationMatchingStrategy is specified as INTERSECTING or when the metadataLocation is specified as a non-spreadsheet location: spreadsheet metadata cannot intersect any other developer metadata location. This field also must be left unspecified when the locationMatchingStrategy is specified as EXACT.  
Enum type. Can be one of the following:  
`DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED` | Default value.  
`ROW` | Developer metadata associated on an entire row dimension.  
`COLUMN` | Developer metadata associated on an entire column dimension.  
`SHEET` | Developer metadata associated on an entire sheet.  
`SPREADSHEET` | Developer metadata associated on the entire spreadsheet.  
`metadataId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_id.  
`metadataKey` |  `string` Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_key.  
`metadataLocation` |  `object ([DeveloperMetadataLocation](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadataLocation))` Limits the selected developer metadata to those entries associated with the specified location. This field either matches exact locations or all intersecting locations according the specified locationMatchingStrategy.  
`metadataValue` |  `string` Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_value.  
`visibility` |  `enum` Limits the selected developer metadata to that which has a matching DeveloperMetadata.visibility. If left unspecified, all developer metadata visibile to the requesting project is considered.  
Enum type. Can be one of the following:  
`DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED` | Default value.  
`DOCUMENT` | Document-visible metadata is accessible from any developer project with access to the document.  
`PROJECT` | Project-visible metadata is only visible to and accessible by the developer project that created the metadata.  
  
## DimensionGroup

A group over an interval of rows or columns on a sheet, which can contain or be contained within other groups. A group can be collapsed or expanded as a unit on the sheet. Fields  
---  
`collapsed` |  `boolean` This field is true if this group is collapsed. A collapsed group remains collapsed if an overlapping group at a shallower depth is expanded. A true value does not imply that all dimensions within the group are hidden, since a dimension's visibility can change independently from this group property. However, when this property is updated, all dimensions within it are set to hidden if this field is true, or set to visible if this field is false.  
`depth` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The depth of the group, representing how many groups have a range that wholly contains the range of this group.  
`range` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The range over which this group exists.  
  
## DimensionProperties

Properties about a dimension. Fields  
---  
`dataSourceColumnReference` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` Output only. If set, this is a column in a data source sheet.  
`developerMetadata[]` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The developer metadata associated with a single row or column.  
`hiddenByFilter` |  `boolean` True if this dimension is being filtered. This field is read-only.  
`hiddenByUser` |  `boolean` True if this dimension is explicitly hidden.  
`pixelSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The height (if a row) or width (if a column) of the dimension in pixels.  
  
## DimensionRange

A range along a single dimension on a sheet. All indexes are zero-based. Indexes are half open: the start index is inclusive and the end index is exclusive. Missing indexes indicate the range is unbounded on that side. Fields  
---  
`dimension` |  `enum` The dimension of the span.  
Enum type. Can be one of the following:  
`DIMENSION_UNSPECIFIED` | The default value, do not use.  
`ROWS` | Operates on the rows of a sheet.  
`COLUMNS` | Operates on the columns of a sheet.  
`endIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The end (exclusive) of the span, or not set if unbounded.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet this span is on.  
`startIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The start (inclusive) of the span, or not set if unbounded.  
  
## DuplicateFilterViewRequest

Duplicates a particular filter view. Fields  
---  
`filterId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the filter being duplicated.  
  
## DuplicateFilterViewResponse

The result of a filter view being duplicated. Fields  
---  
`filter` |  `object ([FilterView](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterView))` The newly created filter.  
  
## DuplicateSheetRequest

Duplicates the contents of a sheet. Fields  
---  
`insertSheetIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The zero-based index where the new sheet should be inserted. The index of all sheets after this are incremented.  
`newSheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` If set, the ID of the new sheet. If not set, an ID is chosen. If set, the ID must not conflict with any existing sheet ID. If set, it must be non-negative.  
`newSheetName` |  `string` The name of the new sheet. If empty, a new name is chosen for you.  
`sourceSheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet to duplicate. If the source sheet is of DATA_SOURCE type, its backing DataSource is also duplicated and associated with the new copy of the sheet. No data execution is triggered, the grid data of this sheet is also copied over but only available after the batch request completes.  
  
## DuplicateSheetResponse

The result of duplicating a sheet. Fields  
---  
`properties` |  `object ([SheetProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SheetProperties))` The properties of the duplicate sheet.  
  
## Editors

The editors of a protected range. Fields  
---  
`domainUsersCanEdit` |  `boolean` True if anyone in the document's domain has edit access to the protected range. Domain protection is only supported on documents within a domain.  
`groups[]` |  `string` The email addresses of groups with edit access to the protected range.  
`users[]` |  `string` The email addresses of users with edit access to the protected range.  
  
## EmbeddedChart

A chart embedded in a sheet. Fields  
---  
`border` |  `object ([EmbeddedObjectBorder](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedObjectBorder))` The border of the chart.  
`chartId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the chart.  
`position` |  `object ([EmbeddedObjectPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedObjectPosition))` The position of the chart.  
`spec` |  `object ([ChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartSpec))` The specification of the chart.  
  
## EmbeddedObjectBorder

A border along an embedded object. Fields  
---  
`color` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the border. Deprecated: Use color_style.  
`colorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the border. If color is also set, this field takes precedence.  
  
## EmbeddedObjectPosition

The position of an embedded object such as a chart. Fields  
---  
`newSheet` |  `boolean` If true, the embedded object is put on a new sheet whose ID is chosen for you. Used only when writing.  
`overlayPosition` |  `object ([OverlayPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#OverlayPosition))` The position at which the object is overlaid on top of a grid.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet this is on. Set only if the embedded object is on its own sheet. Must be non-negative.  
  
## ErrorValue

An error in a cell. Fields  
---  
`message` |  `string` A message with more information about the error (in the spreadsheet's locale).  
`type` |  `enum` The type of error.  
Enum type. Can be one of the following:  
`ERROR_TYPE_UNSPECIFIED` | The default error type, do not use this.  
`ERROR` | Corresponds to the `#ERROR!` error.  
`NULL_VALUE` | Corresponds to the `#NULL!` error.  
`DIVIDE_BY_ZERO` | Corresponds to the `#DIV/0` error.  
`VALUE` | Corresponds to the `#VALUE!` error.  
`REF` | Corresponds to the `#REF!` error.  
`NAME` | Corresponds to the `#NAME?` error.  
`NUM` | Corresponds to the `#NUM!` error.  
`N_A` | Corresponds to the `#N/A` error.  
`LOADING` | Corresponds to the `Loading...` state.  
  
## ExtendedValue

The kinds of value that a cell in a spreadsheet can have. Fields  
---  
`boolValue` |  `boolean` Represents a boolean value.  
`errorValue` |  `object ([ErrorValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ErrorValue))` Represents an error. This field is read-only.  
`formulaValue` |  `string` Represents a formula.  
`numberValue` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Represents a double value. Note: Dates, Times and DateTimes are represented as doubles in SERIAL_NUMBER format.  
`stringValue` |  `string` Represents a string value. Leading single quotes are not included. For example, if the user typed `'123` into the UI, this would be represented as a `stringValue` of `"123"`.  
  
## FilterCriteria

Criteria for showing/hiding rows in a filter or filter view. Fields  
---  
`condition` |  `object ([BooleanCondition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BooleanCondition))` A condition that must be true for values to be shown. (This does not override hidden_values -- if a value is listed there, it will still be hidden.)  
`hiddenValues[]` |  `string` Values that should be hidden.  
`visibleBackgroundColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background fill color to filter by; only cells with this fill color are shown. Mutually exclusive with visible_foreground_color. Deprecated: Use visible_background_color_style.  
`visibleBackgroundColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background fill color to filter by; only cells with this fill color are shown. This field is mutually exclusive with visible_foreground_color, and must be set to an RGB-type color. If visible_background_color is also set, this field takes precedence.  
`visibleForegroundColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The foreground color to filter by; only cells with this foreground color are shown. Mutually exclusive with visible_background_color. Deprecated: Use visible_foreground_color_style.  
`visibleForegroundColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The foreground color to filter by; only cells with this foreground color are shown. This field is mutually exclusive with visible_background_color, and must be set to an RGB-type color. If visible_foreground_color is also set, this field takes precedence.  
  
## FilterSpec

The filter criteria associated with a specific column. Fields  
---  
`columnIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The column index.  
`dataSourceColumnReference` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` Reference to a data source column.  
`filterCriteria` |  `object ([FilterCriteria](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterCriteria))` The criteria for the column.  
  
## FilterView

A filter view. Fields  
---  
`criteria` |  `map (key: string, value: object ([FilterCriteria](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterCriteria)))` The criteria for showing/hiding values per column. The map's key is the column index, and the value is the criteria for that column. This field is deprecated in favor of filter_specs.  
`filterSpecs[]` |  `object ([FilterSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterSpec))` The filter criteria for showing/hiding values per column. Both criteria and filter_specs are populated in responses. If both fields are specified in an update request, this field takes precedence.  
`filterViewId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the filter view.  
`namedRangeId` |  `string` The named range this filter view is backed by, if any. When writing, only one of range or named_range_id may be set.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range this filter view covers. When writing, only one of range or named_range_id may be set.  
`sortSpecs[]` |  `object ([SortSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SortSpec))` The sort order per column. Later specifications are used when values are equal in the earlier specifications.  
`title` |  `string` The name of the filter view.  
  
## FindReplaceRequest

Finds and replaces data in cells over a range, sheet, or all sheets. Fields  
---  
`allSheets` |  `boolean` True to find/replace over all sheets.  
`find` |  `string` The value to search.  
`includeFormulas` |  `boolean` True if the search should include cells with formulas. False to skip cells with formulas.  
`matchCase` |  `boolean` True if the search is case sensitive.  
`matchEntireCell` |  `boolean` True if the find value should match the entire cell.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range to find/replace over.  
`replacement` |  `string` The value to use as the replacement.  
`searchByRegex` |  `boolean` True if the find value is a regex. The regular expression and replacement should follow Java regex rules at https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html. The replacement string is allowed to refer to capturing groups. For example, if one cell has the contents `"Google Sheets"` and another has `"Google Docs"`, then searching for `"o.* (.*)"` with a replacement of `"$1 Rocks"` would change the contents of the cells to `"GSheets Rocks"` and `"GDocs Rocks"` respectively.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet to find/replace over.  
  
## FindReplaceResponse

The result of the find/replace. Fields  
---  
`formulasChanged` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of formula cells changed.  
`occurrencesChanged` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of occurrences (possibly multiple within a cell) changed. For example, if replacing `"e"` with `"o"` in `"Google Sheets"`, this would be `"3"` because `"Google Sheets"` -> `"Googlo Shoots"`.  
`rowsChanged` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of rows changed.  
`sheetsChanged` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of sheets changed.  
`valuesChanged` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of non-formula cells changed.  
  
## GetSpreadsheetByDataFilterRequest

The request for retrieving a Spreadsheet. Fields  
---  
`dataFilters[]` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The DataFilters used to select which ranges to retrieve from the spreadsheet.  
`includeGridData` |  `boolean` True if grid data should be returned. This parameter is ignored if a field mask was set in the request.  
  
## GradientRule

A rule that applies a gradient color scale format, based on the interpolation points listed. The format of a cell will vary based on its contents as compared to the values of the interpolation points. Fields  
---  
`maxpoint` |  `object ([InterpolationPoint](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#InterpolationPoint))` The final interpolation point.  
`midpoint` |  `object ([InterpolationPoint](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#InterpolationPoint))` An optional midway interpolation point.  
`minpoint` |  `object ([InterpolationPoint](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#InterpolationPoint))` The starting interpolation point.  
  
## GridCoordinate

A coordinate in a sheet. All indexes are zero-based. Fields  
---  
`columnIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The column index of the coordinate.  
`rowIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The row index of the coordinate.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet this coordinate is on.  
  
## GridData

Data in the grid, as well as metadata about the dimensions. Fields  
---  
`columnMetadata[]` |  `object ([DimensionProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionProperties))` Metadata about the requested columns in the grid, starting with the column in start_column.  
`rowData[]` |  `object ([RowData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#RowData))` The data in the grid, one entry per row, starting with the row in startRow. The values in RowData will correspond to columns starting at start_column.  
`rowMetadata[]` |  `object ([DimensionProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionProperties))` Metadata about the requested rows in the grid, starting with the row in start_row.  
`startColumn` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The first column this GridData refers to, zero-based.  
`startRow` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The first row this GridData refers to, zero-based.  
  
## GridProperties

Properties of a grid. Fields  
---  
`columnCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of columns in the grid.  
`columnGroupControlAfter` |  `boolean` True if the column grouping control toggle is shown after the group.  
`frozenColumnCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of columns that are frozen in the grid.  
`frozenRowCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of rows that are frozen in the grid.  
`hideGridlines` |  `boolean` True if the grid isn't showing gridlines in the UI.  
`rowCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of rows in the grid.  
`rowGroupControlAfter` |  `boolean` True if the row grouping control toggle is shown after the group.  
  
## GridRange

A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 == sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1` `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id: 123456` The start index must always be less than or equal to the end index. If the start index equals the end index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as `#REF!`. Fields  
---  
`endColumnIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The end column (exclusive) of the range, or not set if unbounded.  
`endRowIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The end row (exclusive) of the range, or not set if unbounded.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet this range is on.  
`startColumnIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The start column (inclusive) of the range, or not set if unbounded.  
`startRowIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The start row (inclusive) of the range, or not set if unbounded.  
  
## HistogramChartSpec

A histogram chart. A histogram chart groups data items into bins, displaying each bin as a column of stacked items. Histograms are used to display the distribution of a dataset. Each column of items represents a range into which those items fall. The number of bins can be chosen automatically or specified explicitly. Fields  
---  
`bucketSize` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` By default the bucket size (the range of values stacked in a single column) is chosen automatically, but it may be overridden here. E.g., A bucket size of 1.5 results in buckets from 0 - 1.5, 1.5 - 3.0, etc. Cannot be negative. This field is optional.  
`legendPosition` |  `enum` The position of the chart legend.  
Enum type. Can be one of the following:  
`HISTOGRAM_CHART_LEGEND_POSITION_UNSPECIFIED` | Default value, do not use.  
`BOTTOM_LEGEND` | The legend is rendered on the bottom of the chart.  
`LEFT_LEGEND` | The legend is rendered on the left of the chart.  
`RIGHT_LEGEND` | The legend is rendered on the right of the chart.  
`TOP_LEGEND` | The legend is rendered on the top of the chart.  
`NO_LEGEND` | No legend is rendered.  
`INSIDE_LEGEND` | The legend is rendered inside the chart area.  
`outlierPercentile` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The outlier percentile is used to ensure that outliers do not adversely affect the calculation of bucket sizes. For example, setting an outlier percentile of 0.05 indicates that the top and bottom 5% of values when calculating buckets. The values are still included in the chart, they will be added to the first or last buckets instead of their own buckets. Must be between 0.0 and 0.5.  
`series[]` |  `object ([HistogramSeries](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#HistogramSeries))` The series for a histogram may be either a single series of values to be bucketed or multiple series, each of the same length, containing the name of the series followed by the values to be bucketed for that series.  
`showItemDividers` |  `boolean` Whether horizontal divider lines should be displayed between items in each column.  
  
## HistogramRule

Allows you to organize the numeric values in a source data column into buckets of a constant size. All values from HistogramRule.start to HistogramRule.end are placed into groups of size HistogramRule.interval. In addition, all values below HistogramRule.start are placed in one group, and all values above HistogramRule.end are placed in another. Only HistogramRule.interval is required, though if HistogramRule.start and HistogramRule.end are both provided, HistogramRule.start must be less than HistogramRule.end. For example, a pivot table showing average purchase amount by age that has 50+ rows: +-----+-------------------+ | Age | AVERAGE of Amount | +-----+-------------------+ | 16 | $27.13 | | 17 | $5.24 | | 18 | $20.15 | ... +-----+-------------------+ could be turned into a pivot table that looks like the one below by applying a histogram group rule with a HistogramRule.start of 25, an HistogramRule.interval of 20, and an HistogramRule.end of 65. +-------------+-------------------+ | Grouped Age | AVERAGE of Amount | +-------------+-------------------+ | < 25 | $19.34 | | 25-45 | $31.43 | | 45-65 | $35.87 | | > 65 | $27.55 | +-------------+-------------------+ | Grand Total | $29.12 | +-------------+-------------------+ Fields  
---  
`end` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum value at which items are placed into buckets of constant size. Values above end are lumped into a single bucket. This field is optional.  
`interval` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The size of the buckets that are created. Must be positive.  
`start` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The minimum value at which items are placed into buckets of constant size. Values below start are lumped into a single bucket. This field is optional.  
  
## HistogramSeries

A histogram series containing the series color and data. Fields  
---  
`barColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the column representing this series in each bucket. This field is optional. Deprecated: Use bar_color_style.  
`barColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the column representing this series in each bucket. This field is optional. If bar_color is also set, this field takes precedence.  
`data` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data for this histogram series.  
  
## InsertDimensionRequest

Inserts rows or columns in a sheet at a particular index. Fields  
---  
`inheritFromBefore` |  `boolean` Whether dimension properties should be extended from the dimensions before or after the newly inserted dimensions. True to inherit from the dimensions before (in which case the start index must be greater than 0), and false to inherit from the dimensions after. For example, if row index 0 has red background and row index 1 has a green background, then inserting 2 rows at index 1 can inherit either the green or red background. If `inheritFromBefore` is true, the two new rows will be red (because the row before the insertion point was red), whereas if `inheritFromBefore` is false, the two new rows will be green (because the row after the insertion point was green).  
`range` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The dimensions to insert. Both the start and end indexes must be bounded.  
  
## InsertRangeRequest

Inserts cells into a range, shifting the existing cells over or down. Fields  
---  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range to insert new cells into.  
`shiftDimension` |  `enum` The dimension which will be shifted when inserting cells. If ROWS, existing cells will be shifted down. If COLUMNS, existing cells will be shifted right.  
Enum type. Can be one of the following:  
`DIMENSION_UNSPECIFIED` | The default value, do not use.  
`ROWS` | Operates on the rows of a sheet.  
`COLUMNS` | Operates on the columns of a sheet.  
  
## InterpolationPoint

A single interpolation point on a gradient conditional format. These pin the gradient color scale according to the color, type and value chosen. Fields  
---  
`color` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color this interpolation point should use. Deprecated: Use color_style.  
`colorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color this interpolation point should use. If color is also set, this field takes precedence.  
`type` |  `enum` How the value should be interpreted.  
Enum type. Can be one of the following:  
`INTERPOLATION_POINT_TYPE_UNSPECIFIED` | The default value, do not use.  
`MIN` | The interpolation point uses the minimum value in the cells over the range of the conditional format.  
`MAX` | The interpolation point uses the maximum value in the cells over the range of the conditional format.  
`NUMBER` | The interpolation point uses exactly the value in InterpolationPoint.value.  
`PERCENT` | The interpolation point is the given percentage over all the cells in the range of the conditional format. This is equivalent to `NUMBER` if the value was: `=(MAX(FLATTEN(range)) * (value / 100)) + (MIN(FLATTEN(range)) * (1 - (value / 100)))` (where errors in the range are ignored when flattening).  
`PERCENTILE` | The interpolation point is the given percentile over all the cells in the range of the conditional format. This is equivalent to `NUMBER` if the value was: `=PERCENTILE(FLATTEN(range), value / 100)` (where errors in the range are ignored when flattening).  
`value` |  `string` The value this interpolation point uses. May be a formula. Unused if type is MIN or MAX.  
  
## Interval

Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive). The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time. Fields  
---  
`endTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Optional. Exclusive end of the interval. If specified, a Timestamp matching this interval will have to be before the end.  
`startTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Optional. Inclusive start of the interval. If specified, a Timestamp matching this interval will have to be the same or after the start.  
  
## IterativeCalculationSettings

Settings to control how circular dependencies are resolved with iterative calculation. Fields  
---  
`convergenceThreshold` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` When iterative calculation is enabled and successive results differ by less than this threshold value, the calculation rounds stop.  
`maxIterations` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` When iterative calculation is enabled, the maximum number of calculation rounds to perform.  
  
## KeyValueFormat

Formatting options for key value. Fields  
---  
`position` |  `object ([TextPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextPosition))` Specifies the horizontal text positioning of key value. This field is optional. If not specified, default positioning is used.  
`textFormat` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` Text formatting options for key value. The link field is not supported.  
  
## LineStyle

Properties that describe the style of a line. Fields  
---  
`type` |  `enum` The dash type of the line.  
Enum type. Can be one of the following:  
`LINE_DASH_TYPE_UNSPECIFIED` | Default value, do not use.  
`INVISIBLE` | No dash type, which is equivalent to a non-visible line.  
`CUSTOM` | A custom dash for a line. Modifying the exact custom dash style is currently unsupported.  
`SOLID` | A solid line.  
`DOTTED` | A dotted line.  
`MEDIUM_DASHED` | A dashed line where the dashes have "medium" length.  
`MEDIUM_DASHED_DOTTED` | A line that alternates between a "medium" dash and a dot.  
`LONG_DASHED` | A dashed line where the dashes have "long" length.  
`LONG_DASHED_DOTTED` | A line that alternates between a "long" dash and a dot.  
`width` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The thickness of the line, in px.  
  
## Link

An external or local reference. Fields  
---  
`uri` |  `string` The link identifier.  
  
## ManualRule

Allows you to manually organize the values in a source data column into buckets with names of your choosing. For example, a pivot table that aggregates population by state: +-------+-------------------+ | State | SUM of Population | +-------+-------------------+ | AK | 0.7 | | AL | 4.8 | | AR | 2.9 | ... +-------+-------------------+ could be turned into a pivot table that aggregates population by time zone by providing a list of groups (for example, groupName = 'Central', items = ['AL', 'AR', 'IA', ...]) to a manual group rule. Note that a similar effect could be achieved by adding a time zone column to the source data and adjusting the pivot table. +-----------+-------------------+ | Time Zone | SUM of Population | +-----------+-------------------+ | Central | 106.3 | | Eastern | 151.9 | | Mountain | 17.4 | ... +-----------+-------------------+ Fields  
---  
`groups[]` |  `object ([ManualRuleGroup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ManualRuleGroup))` The list of group names and the corresponding items from the source data that map to each group name.  
  
## ManualRuleGroup

A group name and a list of items from the source data that should be placed in the group with this name. Fields  
---  
`groupName` |  `object ([ExtendedValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ExtendedValue))` The group name, which must be a string. Each group in a given ManualRule must have a unique group name.  
`items[]` |  `object ([ExtendedValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ExtendedValue))` The items in the source data that should be placed into this group. Each item may be a string, number, or boolean. Items may appear in at most one group within a given ManualRule. Items that do not appear in any group will appear on their own.  
  
## MatchedDeveloperMetadata

A developer metadata entry and the data filters specified in the original request that matched it. Fields  
---  
`dataFilters[]` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` All filters matching the returned developer metadata.  
`developerMetadata` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The developer metadata matching the specified filters.  
  
## MatchedValueRange

A value range that was matched by one or more data filers. Fields  
---  
`dataFilters[]` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The DataFilters from the request that matched the range of values.  
`valueRange` |  `object ([ValueRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ValueRange))` The values matched by the DataFilter.  
  
## MergeCellsRequest

Merges all cells in the range. Fields  
---  
`mergeType` |  `enum` How the cells should be merged.  
Enum type. Can be one of the following:  
`MERGE_ALL` | Create a single merge from the range  
`MERGE_COLUMNS` | Create a merge for each column in the range  
`MERGE_ROWS` | Create a merge for each row in the range  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range of cells to merge.  
  
## MoveDimensionRequest

Moves one or more rows or columns. Fields  
---  
`destinationIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The zero-based start index of where to move the source data to, based on the coordinates _before_ the source data is removed from the grid. Existing data will be shifted down or right (depending on the dimension) to make room for the moved dimensions. The source dimensions are removed from the grid, so the the data may end up in a different index than specified. For example, given `A1..A5` of `0, 1, 2, 3, 4` and wanting to move `"1"` and `"2"` to between `"3"` and `"4"`, the source would be `ROWS [1..3)`,and the destination index would be `"4"` (the zero-based index of row 5). The end result would be `A1..A5` of `0, 3, 1, 2, 4`.  
`source` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The source dimensions to move.  
  
## NamedRange

A named range. Fields  
---  
`name` |  `string` The name of the named range.  
`namedRangeId` |  `string` The ID of the named range.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range this represents.  
  
## NumberFormat

The number format of a cell. Fields  
---  
`pattern` |  `string` Pattern string used for formatting. If not set, a default pattern based on the user's locale will be used if necessary for the given type. See the [Date and Number Formats guide](https://developers.google.com/sheets/api/guides/formats) for more information about the supported patterns.  
`type` |  `enum` The type of the number format. When writing, this field must be set.  
Enum type. Can be one of the following:  
`NUMBER_FORMAT_TYPE_UNSPECIFIED` | The number format is not specified and is based on the contents of the cell. Do not explicitly use this.  
`TEXT` | Text formatting, e.g `1000.12`  
`NUMBER` | Number formatting, e.g, `1,000.12`  
`PERCENT` | Percent formatting, e.g `10.12%`  
`CURRENCY` | Currency formatting, e.g `$1,000.12`  
`DATE` | Date formatting, e.g `9/26/2008`  
`TIME` | Time formatting, e.g `3:59:00 PM`  
`DATE_TIME` | Date+Time formatting, e.g `9/26/08 15:59:00`  
`SCIENTIFIC` | Scientific number formatting, e.g `1.01E+03`  
  
## OrgChartSpec

An org chart. Org charts require a unique set of labels in labels and may optionally include parent_labels and tooltips. parent_labels contain, for each node, the label identifying the parent node. tooltips contain, for each node, an optional tooltip. For example, to describe an OrgChart with Alice as the CEO, Bob as the President (reporting to Alice) and Cathy as VP of Sales (also reporting to Alice), have labels contain "Alice", "Bob", "Cathy", parent_labels contain "", "Alice", "Alice" and tooltips contain "CEO", "President", "VP Sales". Fields  
---  
`labels` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data containing the labels for all the nodes in the chart. Labels must be unique.  
`nodeColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the org chart nodes. Deprecated: Use node_color_style.  
`nodeColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the org chart nodes. If node_color is also set, this field takes precedence.  
`nodeSize` |  `enum` The size of the org chart nodes.  
Enum type. Can be one of the following:  
`ORG_CHART_LABEL_SIZE_UNSPECIFIED` | Default value, do not use.  
`SMALL` | The small org chart node size.  
`MEDIUM` | The medium org chart node size.  
`LARGE` | The large org chart node size.  
`parentLabels` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data containing the label of the parent for the corresponding node. A blank value indicates that the node has no parent and is a top-level node. This field is optional.  
`selectedNodeColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the selected org chart nodes. Deprecated: Use selected_node_color_style.  
`selectedNodeColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the selected org chart nodes. If selected_node_color is also set, this field takes precedence.  
`tooltips` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data containing the tooltip for the corresponding node. A blank value results in no tooltip being displayed for the node. This field is optional.  
  
## OverlayPosition

The location an object is overlaid on top of a grid. Fields  
---  
`anchorCell` |  `object ([GridCoordinate](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridCoordinate))` The cell the object is anchored to.  
`heightPixels` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The height of the object, in pixels. Defaults to 371.  
`offsetXPixels` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The horizontal offset, in pixels, that the object is offset from the anchor cell.  
`offsetYPixels` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The vertical offset, in pixels, that the object is offset from the anchor cell.  
`widthPixels` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The width of the object, in pixels. Defaults to 600.  
  
## Padding

The amount of padding around the cell, in pixels. When updating padding, every field must be specified. Fields  
---  
`bottom` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The bottom padding of the cell.  
`left` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The left padding of the cell.  
`right` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The right padding of the cell.  
`top` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The top padding of the cell.  
  
## PasteDataRequest

Inserts data into the spreadsheet starting at the specified coordinate. Fields  
---  
`coordinate` |  `object ([GridCoordinate](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridCoordinate))` The coordinate at which the data should start being inserted.  
`data` |  `string` The data to insert.  
`delimiter` |  `string` The delimiter in the data.  
`html` |  `boolean` True if the data is HTML.  
`type` |  `enum` How the data should be pasted.  
Enum type. Can be one of the following:  
`PASTE_NORMAL` | Paste values, formulas, formats, and merges.  
`PASTE_VALUES` | Paste the values ONLY without formats, formulas, or merges.  
`PASTE_FORMAT` | Paste the format and data validation only.  
`PASTE_NO_BORDERS` | Like `PASTE_NORMAL` but without borders.  
`PASTE_FORMULA` | Paste the formulas only.  
`PASTE_DATA_VALIDATION` | Paste the data validation only.  
`PASTE_CONDITIONAL_FORMATTING` | Paste the conditional formatting rules only.  
  
## PieChartSpec

A pie chart. Fields  
---  
`domain` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data that covers the domain of the pie chart.  
`legendPosition` |  `enum` Where the legend of the pie chart should be drawn.  
Enum type. Can be one of the following:  
`PIE_CHART_LEGEND_POSITION_UNSPECIFIED` | Default value, do not use.  
`BOTTOM_LEGEND` | The legend is rendered on the bottom of the chart.  
`LEFT_LEGEND` | The legend is rendered on the left of the chart.  
`RIGHT_LEGEND` | The legend is rendered on the right of the chart.  
`TOP_LEGEND` | The legend is rendered on the top of the chart.  
`NO_LEGEND` | No legend is rendered.  
`LABELED_LEGEND` | Each pie slice has a label attached to it.  
`pieHole` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The size of the hole in the pie chart.  
`series` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data that covers the one and only series of the pie chart.  
`threeDimensional` |  `boolean` True if the pie is three dimensional.  
  
## PivotFilterCriteria

Criteria for showing/hiding rows in a pivot table. Fields  
---  
`condition` |  `object ([BooleanCondition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BooleanCondition))` A condition that must be true for values to be shown. (`visibleValues` does not override this -- even if a value is listed there, it is still hidden if it does not meet the condition.) Condition values that refer to ranges in A1-notation are evaluated relative to the pivot table sheet. References are treated absolutely, so are not filled down the pivot table. For example, a condition value of `=A1` on "Pivot Table 1" is treated as `'Pivot Table 1'!$A$1`. The source data of the pivot table can be referenced by column header name. For example, if the source data has columns named "Revenue" and "Cost" and a condition is applied to the "Revenue" column with type `NUMBER_GREATER` and value `=Cost`, then only columns where "Revenue" > "Cost" are included.  
`visibleByDefault` |  `boolean` Whether values are visible by default. If true, the visible_values are ignored, all values that meet condition (if specified) are shown. If false, values that are both in visible_values and meet condition are shown.  
`visibleValues[]` |  `string` Values that should be included. Values not listed here are excluded.  
  
## PivotFilterSpec

The pivot table filter criteria associated with a specific source column offset. Fields  
---  
`columnOffsetIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The column offset of the source range.  
`dataSourceColumnReference` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` The reference to the data source column.  
`filterCriteria` |  `object ([PivotFilterCriteria](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotFilterCriteria))` The criteria for the column.  
  
## PivotGroup

A single grouping (either row or column) in a pivot table. Fields  
---  
`dataSourceColumnReference` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` The reference to the data source column this grouping is based on.  
`groupLimit` |  `object ([PivotGroupLimit](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotGroupLimit))` The count limit on rows or columns to apply to this pivot group.  
`groupRule` |  `object ([PivotGroupRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotGroupRule))` The group rule to apply to this row/column group.  
`label` |  `string` The labels to use for the row/column groups which can be customized. For example, in the following pivot table, the row label is `Region` (which could be renamed to `State`) and the column label is `Product` (which could be renamed `Item`). Pivot tables created before December 2017 do not have header labels. If you'd like to add header labels to an existing pivot table, please delete the existing pivot table and then create a new pivot table with same parameters. +--------------+---------+-------+ | SUM of Units | Product | | | Region | Pen | Paper | +--------------+---------+-------+ | New York | 345 | 98 | | Oregon | 234 | 123 | | Tennessee | 531 | 415 | +--------------+---------+-------+ | Grand Total | 1110 | 636 | +--------------+---------+-------+  
`repeatHeadings` |  `boolean` True if the headings in this pivot group should be repeated. This is only valid for row groupings and is ignored by columns. By default, we minimize repetition of headings by not showing higher level headings where they are the same. For example, even though the third row below corresponds to "Q1 Mar", "Q1" is not shown because it is redundant with previous rows. Setting repeat_headings to true would cause "Q1" to be repeated for "Feb" and "Mar". +--------------+ | Q1 | Jan | | | Feb | | | Mar | +--------+-----+ | Q1 Total | +--------------+  
`showTotals` |  `boolean` True if the pivot table should include the totals for this grouping.  
`sortOrder` |  `enum` The order the values in this group should be sorted.  
Enum type. Can be one of the following:  
`SORT_ORDER_UNSPECIFIED` | Default value, do not use this.  
`ASCENDING` | Sort ascending.  
`DESCENDING` | Sort descending.  
`sourceColumnOffset` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The column offset of the source range that this grouping is based on. For example, if the source was `C10:E15`, a `sourceColumnOffset` of `0` means this group refers to column `C`, whereas the offset `1` would refer to column `D`.  
`valueBucket` |  `object ([PivotGroupSortValueBucket](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotGroupSortValueBucket))` The bucket of the opposite pivot group to sort by. If not specified, sorting is alphabetical by this group's values.  
`valueMetadata[]` |  `object ([PivotGroupValueMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotGroupValueMetadata))` Metadata about values in the grouping.  
  
## PivotGroupLimit

The count limit on rows or columns in the pivot group. Fields  
---  
`applyOrder` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The order in which the group limit is applied to the pivot table. Pivot group limits are applied from lower to higher order number. Order numbers are normalized to consecutive integers from 0. For write request, to fully customize the applying orders, all pivot group limits should have this field set with an unique number. Otherwise, the order is determined by the index in the PivotTable.rows list and then the PivotTable.columns list.  
`countLimit` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The count limit.  
  
## PivotGroupRule

An optional setting on a PivotGroup that defines buckets for the values in the source data column rather than breaking out each individual value. Only one PivotGroup with a group rule may be added for each column in the source data, though on any given column you may add both a PivotGroup that has a rule and a PivotGroup that does not. Fields  
---  
`dateTimeRule` |  `object ([DateTimeRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DateTimeRule))` A DateTimeRule.  
`histogramRule` |  `object ([HistogramRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#HistogramRule))` A HistogramRule.  
`manualRule` |  `object ([ManualRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ManualRule))` A ManualRule.  
  
## PivotGroupSortValueBucket

Information about which values in a pivot group should be used for sorting. Fields  
---  
`buckets[]` |  `object ([ExtendedValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ExtendedValue))` Determines the bucket from which values are chosen to sort. For example, in a pivot table with one row group & two column groups, the row group can list up to two values. The first value corresponds to a value within the first column group, and the second value corresponds to a value in the second column group. If no values are listed, this would indicate that the row should be sorted according to the "Grand Total" over the column groups. If a single value is listed, this would correspond to using the "Total" of that bucket.  
`valuesIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The offset in the PivotTable.values list which the values in this grouping should be sorted by.  
  
## PivotGroupValueMetadata

Metadata about a value in a pivot grouping. Fields  
---  
`collapsed` |  `boolean` True if the data corresponding to the value is collapsed.  
`value` |  `object ([ExtendedValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ExtendedValue))` The calculated value the metadata corresponds to. (Note that formulaValue is not valid, because the values will be calculated.)  
  
## PivotTable

A pivot table. Fields  
---  
`columns[]` |  `object ([PivotGroup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotGroup))` Each column grouping in the pivot table.  
`criteria` |  `map (key: string, value: object ([PivotFilterCriteria](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotFilterCriteria)))` An optional mapping of filters per source column offset. The filters are applied before aggregating data into the pivot table. The map's key is the column offset of the source range that you want to filter, and the value is the criteria for that column. For example, if the source was `C10:E15`, a key of `0` will have the filter for column `C`, whereas the key `1` is for column `D`. This field is deprecated in favor of filter_specs.  
`dataExecutionStatus` |  `object ([DataExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataExecutionStatus))` Output only. The data execution status for data source pivot tables.  
`dataSourceId` |  `string` The ID of the data source the pivot table is reading data from.  
`filterSpecs[]` |  `object ([PivotFilterSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotFilterSpec))` The filters applied to the source columns before aggregating data for the pivot table. Both criteria and filter_specs are populated in responses. If both fields are specified in an update request, this field takes precedence.  
`rows[]` |  `object ([PivotGroup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotGroup))` Each row grouping in the pivot table.  
`source` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range the pivot table is reading data from.  
`valueLayout` |  `enum` Whether values should be listed horizontally (as columns) or vertically (as rows).  
Enum type. Can be one of the following:  
`HORIZONTAL` | Values are laid out horizontally (as columns).  
`VERTICAL` | Values are laid out vertically (as rows).  
`values[]` |  `object ([PivotValue](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PivotValue))` A list of values to include in the pivot table.  
  
## PivotValue

The definition of how a value in a pivot table should be calculated. Fields  
---  
`calculatedDisplayType` |  `enum` If specified, indicates that pivot values should be displayed as the result of a calculation with another pivot value. For example, if calculated_display_type is specified as PERCENT_OF_GRAND_TOTAL, all the pivot values are displayed as the percentage of the grand total. In the Sheets editor, this is referred to as "Show As" in the value section of a pivot table.  
Enum type. Can be one of the following:  
`PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED` | Default value, do not use.  
`PERCENT_OF_ROW_TOTAL` | Shows the pivot values as percentage of the row total values.  
`PERCENT_OF_COLUMN_TOTAL` | Shows the pivot values as percentage of the column total values.  
`PERCENT_OF_GRAND_TOTAL` | Shows the pivot values as percentage of the grand total values.  
`dataSourceColumnReference` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` The reference to the data source column that this value reads from.  
`formula` |  `string` A custom formula to calculate the value. The formula must start with an `=` character.  
`name` |  `string` A name to use for the value.  
`sourceColumnOffset` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The column offset of the source range that this value reads from. For example, if the source was `C10:E15`, a `sourceColumnOffset` of `0` means this value refers to column `C`, whereas the offset `1` would refer to column `D`.  
`summarizeFunction` |  `enum` A function to summarize the value. If formula is set, the only supported values are SUM and CUSTOM. If sourceColumnOffset is set, then `CUSTOM` is not supported.  
Enum type. Can be one of the following:  
`PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED` | The default, do not use.  
`SUM` | Corresponds to the `SUM` function.  
`COUNTA` | Corresponds to the `COUNTA` function.  
`COUNT` | Corresponds to the `COUNT` function.  
`COUNTUNIQUE` | Corresponds to the `COUNTUNIQUE` function.  
`AVERAGE` | Corresponds to the `AVERAGE` function.  
`MAX` | Corresponds to the `MAX` function.  
`MIN` | Corresponds to the `MIN` function.  
`MEDIAN` | Corresponds to the `MEDIAN` function.  
`PRODUCT` | Corresponds to the `PRODUCT` function.  
`STDEV` | Corresponds to the `STDEV` function.  
`STDEVP` | Corresponds to the `STDEVP` function.  
`VAR` | Corresponds to the `VAR` function.  
`VARP` | Corresponds to the `VARP` function.  
`CUSTOM` | Indicates the formula should be used as-is. Only valid if PivotValue.formula was set.  
  
## PointStyle

The style of a point on the chart. Fields  
---  
`shape` |  `enum` The point shape. If empty or unspecified, a default shape is used.  
Enum type. Can be one of the following:  
`POINT_SHAPE_UNSPECIFIED` | Default value.  
`CIRCLE` | A circle shape.  
`DIAMOND` | A diamond shape.  
`HEXAGON` | A hexagon shape.  
`PENTAGON` | A pentagon shape.  
`SQUARE` | A square shape.  
`STAR` | A star shape.  
`TRIANGLE` | A triangle shape.  
`X_MARK` | An x-mark shape.  
`size` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The point size. If empty, a default size is used.  
  
## ProtectedRange

A protected range. Fields  
---  
`description` |  `string` The description of this protected range.  
`editors` |  `object ([Editors](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Editors))` The users and groups with edit access to the protected range. This field is only visible to users with edit access to the protected range and the document. Editors are not supported with warning_only protection.  
`namedRangeId` |  `string` The named range this protected range is backed by, if any. When writing, only one of range or named_range_id may be set.  
`protectedRangeId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the protected range. This field is read-only.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range that is being protected. The range may be fully unbounded, in which case this is considered a protected sheet. When writing, only one of range or named_range_id may be set.  
`requestingUserCanEdit` |  `boolean` True if the user who requested this protected range can edit the protected area. This field is read-only.  
`unprotectedRanges[]` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The list of unprotected ranges within a protected sheet. Unprotected ranges are only supported on protected sheets.  
`warningOnly` |  `boolean` True if this protected range will show a warning when editing. Warning-based protection means that every user can edit data in the protected range, except editing will prompt a warning asking the user to confirm the edit. When writing: if this field is true, then editors is ignored. Additionally, if this field is changed from true to false and the `editors` field is not set (nor included in the field mask), then the editors will be set to all the editors in the document.  
  
## RandomizeRangeRequest

Randomizes the order of the rows in a range. Fields  
---  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range to randomize.  
  
## RefreshDataSourceObjectExecutionStatus

The execution status of refreshing one data source object. Fields  
---  
`dataExecutionStatus` |  `object ([DataExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataExecutionStatus))` The data execution status.  
`reference` |  `object ([DataSourceObjectReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceObjectReference))` Reference to a data source object being refreshed.  
  
## RefreshDataSourceRequest

Refreshes one or multiple data source objects in the spreadsheet by the specified references. The request requires an additional `bigquery.readonly` OAuth scope. If there are multiple refresh requests referencing the same data source objects in one batch, only the last refresh request is processed, and all those requests will have the same response accordingly. Fields  
---  
`dataSourceId` |  `string` Reference to a DataSource. If specified, refreshes all associated data source objects for the data source.  
`force` |  `boolean` Refreshes the data source objects regardless of the current state. If not set and a referenced data source object was in error state, the refresh will fail immediately.  
`isAll` |  `boolean` Refreshes all existing data source objects in the spreadsheet.  
`references` |  `object ([DataSourceObjectReferences](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceObjectReferences))` References to data source objects to refresh.  
  
## RefreshDataSourceResponse

The response from refreshing one or multiple data source objects. Fields  
---  
`statuses[]` |  `object ([RefreshDataSourceObjectExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#RefreshDataSourceObjectExecutionStatus))` All the refresh status for the data source object references specified in the request. If is_all is specified, the field contains only those in failure status.  
  
## RepeatCellRequest

Updates all cells in the range to the values in the given Cell object. Only the fields listed in the fields field are updated; others are unchanged. If writing a cell with a formula, the formula's ranges will automatically increment for each field in the range. For example, if writing a cell with formula `=A1` into range B2:C4, B2 would be `=A1`, B3 would be `=A2`, B4 would be `=A3`, C2 would be `=B1`, C3 would be `=B2`, C4 would be `=B3`. To keep the formula's ranges static, use the `$` indicator. For example, use the formula `=$A$1` to prevent both the row and the column from incrementing. Fields  
---  
`cell` |  `object ([CellData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CellData))` The data to write.  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `cell` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range to repeat the cell in.  
  
## Request

A single kind of update to apply to a spreadsheet. Fields  
---  
`addBanding` |  `object ([AddBandingRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddBandingRequest))` Adds a new banded range  
`addChart` |  `object ([AddChartRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddChartRequest))` Adds a chart.  
`addConditionalFormatRule` |  `object ([AddConditionalFormatRuleRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddConditionalFormatRuleRequest))` Adds a new conditional format rule.  
`addDataSource` |  `object ([AddDataSourceRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddDataSourceRequest))` Adds a data source.  
`addDimensionGroup` |  `object ([AddDimensionGroupRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddDimensionGroupRequest))` Creates a group over the specified range.  
`addFilterView` |  `object ([AddFilterViewRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddFilterViewRequest))` Adds a filter view.  
`addNamedRange` |  `object ([AddNamedRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddNamedRangeRequest))` Adds a named range.  
`addProtectedRange` |  `object ([AddProtectedRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddProtectedRangeRequest))` Adds a protected range.  
`addSheet` |  `object ([AddSheetRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddSheetRequest))` Adds a sheet.  
`addSlicer` |  `object ([AddSlicerRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddSlicerRequest))` Adds a slicer.  
`appendCells` |  `object ([AppendCellsRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AppendCellsRequest))` Appends cells after the last row with data in a sheet.  
`appendDimension` |  `object ([AppendDimensionRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AppendDimensionRequest))` Appends dimensions to the end of a sheet.  
`autoFill` |  `object ([AutoFillRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AutoFillRequest))` Automatically fills in more data based on existing data.  
`autoResizeDimensions` |  `object ([AutoResizeDimensionsRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AutoResizeDimensionsRequest))` Automatically resizes one or more dimensions based on the contents of the cells in that dimension.  
`clearBasicFilter` |  `object ([ClearBasicFilterRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ClearBasicFilterRequest))` Clears the basic filter on a sheet.  
`copyPaste` |  `object ([CopyPasteRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CopyPasteRequest))` Copies data from one area and pastes it to another.  
`createDeveloperMetadata` |  `object ([CreateDeveloperMetadataRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CreateDeveloperMetadataRequest))` Creates new developer metadata  
`cutPaste` |  `object ([CutPasteRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CutPasteRequest))` Cuts data from one area and pastes it to another.  
`deleteBanding` |  `object ([DeleteBandingRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteBandingRequest))` Removes a banded range  
`deleteConditionalFormatRule` |  `object ([DeleteConditionalFormatRuleRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteConditionalFormatRuleRequest))` Deletes an existing conditional format rule.  
`deleteDataSource` |  `object ([DeleteDataSourceRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteDataSourceRequest))` Deletes a data source.  
`deleteDeveloperMetadata` |  `object ([DeleteDeveloperMetadataRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteDeveloperMetadataRequest))` Deletes developer metadata  
`deleteDimension` |  `object ([DeleteDimensionRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteDimensionRequest))` Deletes rows or columns in a sheet.  
`deleteDimensionGroup` |  `object ([DeleteDimensionGroupRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteDimensionGroupRequest))` Deletes a group over the specified range.  
`deleteDuplicates` |  `object ([DeleteDuplicatesRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteDuplicatesRequest))` Removes rows containing duplicate values in specified columns of a cell range.  
`deleteEmbeddedObject` |  `object ([DeleteEmbeddedObjectRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteEmbeddedObjectRequest))` Deletes an embedded object (e.g, chart, image) in a sheet.  
`deleteFilterView` |  `object ([DeleteFilterViewRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteFilterViewRequest))` Deletes a filter view from a sheet.  
`deleteNamedRange` |  `object ([DeleteNamedRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteNamedRangeRequest))` Deletes a named range.  
`deleteProtectedRange` |  `object ([DeleteProtectedRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteProtectedRangeRequest))` Deletes a protected range.  
`deleteRange` |  `object ([DeleteRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteRangeRequest))` Deletes a range of cells from a sheet, shifting the remaining cells.  
`deleteSheet` |  `object ([DeleteSheetRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteSheetRequest))` Deletes a sheet.  
`duplicateFilterView` |  `object ([DuplicateFilterViewRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DuplicateFilterViewRequest))` Duplicates a filter view.  
`duplicateSheet` |  `object ([DuplicateSheetRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DuplicateSheetRequest))` Duplicates a sheet.  
`findReplace` |  `object ([FindReplaceRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FindReplaceRequest))` Finds and replaces occurrences of some text with other text.  
`insertDimension` |  `object ([InsertDimensionRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#InsertDimensionRequest))` Inserts new rows or columns in a sheet.  
`insertRange` |  `object ([InsertRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#InsertRangeRequest))` Inserts new cells in a sheet, shifting the existing cells.  
`mergeCells` |  `object ([MergeCellsRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#MergeCellsRequest))` Merges cells together.  
`moveDimension` |  `object ([MoveDimensionRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#MoveDimensionRequest))` Moves rows or columns to another location in a sheet.  
`pasteData` |  `object ([PasteDataRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#PasteDataRequest))` Pastes data (HTML or delimited) into a sheet.  
`randomizeRange` |  `object ([RandomizeRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#RandomizeRangeRequest))` Randomizes the order of the rows in a range.  
`refreshDataSource` |  `object ([RefreshDataSourceRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#RefreshDataSourceRequest))` Refreshs one or multiple data sources and associated dbobjects.  
`repeatCell` |  `object ([RepeatCellRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#RepeatCellRequest))` Repeats a single cell across a range.  
`setBasicFilter` |  `object ([SetBasicFilterRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SetBasicFilterRequest))` Sets the basic filter on a sheet.  
`setDataValidation` |  `object ([SetDataValidationRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SetDataValidationRequest))` Sets data validation for one or more cells.  
`sortRange` |  `object ([SortRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SortRangeRequest))` Sorts data in a range.  
`textToColumns` |  `object ([TextToColumnsRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextToColumnsRequest))` Converts a column of text into many columns of text.  
`trimWhitespace` |  `object ([TrimWhitespaceRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TrimWhitespaceRequest))` Trims cells of whitespace (such as spaces, tabs, or new lines).  
`unmergeCells` |  `object ([UnmergeCellsRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UnmergeCellsRequest))` Unmerges merged cells.  
`updateBanding` |  `object ([UpdateBandingRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateBandingRequest))` Updates a banded range  
`updateBorders` |  `object ([UpdateBordersRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateBordersRequest))` Updates the borders in a range of cells.  
`updateCells` |  `object ([UpdateCellsRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateCellsRequest))` Updates many cells at once.  
`updateChartSpec` |  `object ([UpdateChartSpecRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateChartSpecRequest))` Updates a chart's specifications.  
`updateConditionalFormatRule` |  `object ([UpdateConditionalFormatRuleRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateConditionalFormatRuleRequest))` Updates an existing conditional format rule.  
`updateDataSource` |  `object ([UpdateDataSourceRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateDataSourceRequest))` Updates a data source.  
`updateDeveloperMetadata` |  `object ([UpdateDeveloperMetadataRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateDeveloperMetadataRequest))` Updates an existing developer metadata entry  
`updateDimensionGroup` |  `object ([UpdateDimensionGroupRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateDimensionGroupRequest))` Updates the state of the specified group.  
`updateDimensionProperties` |  `object ([UpdateDimensionPropertiesRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateDimensionPropertiesRequest))` Updates dimensions' properties.  
`updateEmbeddedObjectBorder` |  `object ([UpdateEmbeddedObjectBorderRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateEmbeddedObjectBorderRequest))` Updates an embedded object's border.  
`updateEmbeddedObjectPosition` |  `object ([UpdateEmbeddedObjectPositionRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateEmbeddedObjectPositionRequest))` Updates an embedded object's (e.g. chart, image) position.  
`updateFilterView` |  `object ([UpdateFilterViewRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateFilterViewRequest))` Updates the properties of a filter view.  
`updateNamedRange` |  `object ([UpdateNamedRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateNamedRangeRequest))` Updates a named range.  
`updateProtectedRange` |  `object ([UpdateProtectedRangeRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateProtectedRangeRequest))` Updates a protected range.  
`updateSheetProperties` |  `object ([UpdateSheetPropertiesRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateSheetPropertiesRequest))` Updates a sheet's properties.  
`updateSlicerSpec` |  `object ([UpdateSlicerSpecRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateSlicerSpecRequest))` Updates a slicer's specifications.  
`updateSpreadsheetProperties` |  `object ([UpdateSpreadsheetPropertiesRequest](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateSpreadsheetPropertiesRequest))` Updates the spreadsheet's properties.  
  
## Response

A single response from an update. Fields  
---  
`addBanding` |  `object ([AddBandingResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddBandingResponse))` A reply from adding a banded range.  
`addChart` |  `object ([AddChartResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddChartResponse))` A reply from adding a chart.  
`addDataSource` |  `object ([AddDataSourceResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddDataSourceResponse))` A reply from adding a data source.  
`addDimensionGroup` |  `object ([AddDimensionGroupResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddDimensionGroupResponse))` A reply from adding a dimension group.  
`addFilterView` |  `object ([AddFilterViewResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddFilterViewResponse))` A reply from adding a filter view.  
`addNamedRange` |  `object ([AddNamedRangeResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddNamedRangeResponse))` A reply from adding a named range.  
`addProtectedRange` |  `object ([AddProtectedRangeResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddProtectedRangeResponse))` A reply from adding a protected range.  
`addSheet` |  `object ([AddSheetResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddSheetResponse))` A reply from adding a sheet.  
`addSlicer` |  `object ([AddSlicerResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#AddSlicerResponse))` A reply from adding a slicer.  
`createDeveloperMetadata` |  `object ([CreateDeveloperMetadataResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CreateDeveloperMetadataResponse))` A reply from creating a developer metadata entry.  
`deleteConditionalFormatRule` |  `object ([DeleteConditionalFormatRuleResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteConditionalFormatRuleResponse))` A reply from deleting a conditional format rule.  
`deleteDeveloperMetadata` |  `object ([DeleteDeveloperMetadataResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteDeveloperMetadataResponse))` A reply from deleting a developer metadata entry.  
`deleteDimensionGroup` |  `object ([DeleteDimensionGroupResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteDimensionGroupResponse))` A reply from deleting a dimension group.  
`deleteDuplicates` |  `object ([DeleteDuplicatesResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeleteDuplicatesResponse))` A reply from removing rows containing duplicate values.  
`duplicateFilterView` |  `object ([DuplicateFilterViewResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DuplicateFilterViewResponse))` A reply from duplicating a filter view.  
`duplicateSheet` |  `object ([DuplicateSheetResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DuplicateSheetResponse))` A reply from duplicating a sheet.  
`findReplace` |  `object ([FindReplaceResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FindReplaceResponse))` A reply from doing a find/replace.  
`refreshDataSource` |  `object ([RefreshDataSourceResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#RefreshDataSourceResponse))` A reply from refreshing data source objects.  
`trimWhitespace` |  `object ([TrimWhitespaceResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TrimWhitespaceResponse))` A reply from trimming whitespace.  
`updateConditionalFormatRule` |  `object ([UpdateConditionalFormatRuleResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateConditionalFormatRuleResponse))` A reply from updating a conditional format rule.  
`updateDataSource` |  `object ([UpdateDataSourceResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateDataSourceResponse))` A reply from updating a data source.  
`updateDeveloperMetadata` |  `object ([UpdateDeveloperMetadataResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateDeveloperMetadataResponse))` A reply from updating a developer metadata entry.  
`updateEmbeddedObjectPosition` |  `object ([UpdateEmbeddedObjectPositionResponse](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#UpdateEmbeddedObjectPositionResponse))` A reply from updating an embedded object's position.  
  
## RowData

Data about each cell in a row. Fields  
---  
`values[]` |  `object ([CellData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CellData))` The values in the row, one per column.  
  
## ScorecardChartSpec

A scorecard chart. Scorecard charts are used to highlight key performance indicators, known as KPIs, on the spreadsheet. A scorecard chart can represent things like total sales, average cost, or a top selling item. You can specify a single data value, or aggregate over a range of data. Percentage or absolute difference from a baseline value can be highlighted, like changes over time. Fields  
---  
`aggregateType` |  `enum` The aggregation type for key and baseline chart data in scorecard chart. This field is not supported for data source charts. Use the ChartData.aggregateType field of the key_value_data or baseline_value_data instead for data source charts. This field is optional.  
Enum type. Can be one of the following:  
`CHART_AGGREGATE_TYPE_UNSPECIFIED` | Default value, do not use.  
`AVERAGE` | Average aggregate function.  
`COUNT` | Count aggregate function.  
`MAX` | Maximum aggregate function.  
`MEDIAN` | Median aggregate function.  
`MIN` | Minimum aggregate function.  
`SUM` | Sum aggregate function.  
`baselineValueData` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data for scorecard baseline value. This field is optional.  
`baselineValueFormat` |  `object ([BaselineValueFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BaselineValueFormat))` Formatting options for baseline value. This field is needed only if baseline_value_data is specified.  
`customFormatOptions` |  `object ([ChartCustomNumberFormatOptions](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartCustomNumberFormatOptions))` Custom formatting options for numeric key/baseline values in scorecard chart. This field is used only when number_format_source is set to CUSTOM. This field is optional.  
`keyValueData` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data for scorecard key value.  
`keyValueFormat` |  `object ([KeyValueFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#KeyValueFormat))` Formatting options for key value.  
`numberFormatSource` |  `enum` The number format source used in the scorecard chart. This field is optional.  
Enum type. Can be one of the following:  
`CHART_NUMBER_FORMAT_SOURCE_UNDEFINED` | Default value, do not use.  
`FROM_DATA` | Inherit number formatting from data.  
`CUSTOM` | Apply custom formatting as specified by ChartCustomNumberFormatOptions.  
`scaleFactor` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Value to scale scorecard key and baseline value. For example, a factor of 10 can be used to divide all values in the chart by 10. This field is optional.  
  
## SearchDeveloperMetadataRequest

A request to retrieve all developer metadata matching the set of specified criteria. Fields  
---  
`dataFilters[]` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The data filters describing the criteria used to determine which DeveloperMetadata entries to return. DeveloperMetadata matching any of the specified filters are included in the response.  
  
## SearchDeveloperMetadataResponse

A reply to a developer metadata search request. Fields  
---  
`matchedDeveloperMetadata[]` |  `object ([MatchedDeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#MatchedDeveloperMetadata))` The metadata matching the criteria of the search request.  
  
## SetBasicFilterRequest

Sets the basic filter associated with a sheet. Fields  
---  
`filter` |  `object ([BasicFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BasicFilter))` The filter to set.  
  
## SetDataValidationRequest

Sets a data validation rule to every cell in the range. To clear validation in a range, call this with no rule specified. Fields  
---  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range the data validation rule should apply to.  
`rule` |  `object ([DataValidationRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataValidationRule))` The data validation rule to set on each cell in the range, or empty to clear the data validation in the range.  
  
## Sheet

A sheet in a spreadsheet. Fields  
---  
`bandedRanges[]` |  `object ([BandedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BandedRange))` The banded (alternating colors) ranges on this sheet.  
`basicFilter` |  `object ([BasicFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BasicFilter))` The filter on this sheet, if any.  
`charts[]` |  `object ([EmbeddedChart](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedChart))` The specifications of every chart on this sheet.  
`columnGroups[]` |  `object ([DimensionGroup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionGroup))` All column groups on this sheet, ordered by increasing range start index, then by group depth.  
`conditionalFormats[]` |  `object ([ConditionalFormatRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ConditionalFormatRule))` The conditional format rules in this sheet.  
`data[]` |  `object ([GridData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridData))` Data in the grid, if this is a grid sheet. The number of GridData objects returned is dependent on the number of ranges requested on this sheet. For example, if this is representing `Sheet1`, and the spreadsheet was requested with ranges `Sheet1!A1:C10` and `Sheet1!D15:E20`, then the first GridData will have a startRow/startColumn of `0`, while the second one will have `startRow 14` (zero-based row 15), and `startColumn 3` (zero-based column D). For a DATA_SOURCE sheet, you can not request a specific range, the GridData contains all the values.  
`developerMetadata[]` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The developer metadata associated with a sheet.  
`filterViews[]` |  `object ([FilterView](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterView))` The filter views in this sheet.  
`merges[]` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The ranges that are merged together.  
`properties` |  `object ([SheetProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SheetProperties))` The properties of the sheet.  
`protectedRanges[]` |  `object ([ProtectedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ProtectedRange))` The protected ranges in this sheet.  
`rowGroups[]` |  `object ([DimensionGroup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionGroup))` All row groups on this sheet, ordered by increasing range start index, then by group depth.  
`slicers[]` |  `object ([Slicer](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Slicer))` The slicers on this sheet.  
  
## SheetProperties

Properties of a sheet. Fields  
---  
`dataSourceSheetProperties` |  `object ([DataSourceSheetProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceSheetProperties))` Output only. If present, the field contains DATA_SOURCE sheet specific properties.  
`gridProperties` |  `object ([GridProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridProperties))` Additional properties of the sheet if this sheet is a grid. (If the sheet is an object sheet, containing a chart or image, then this field will be absent.) When writing it is an error to set any grid properties on non-grid sheets. If this sheet is a DATA_SOURCE sheet, this field is output only but contains the properties that reflect how a data source sheet is rendered in the UI, e.g. row_count.  
`hidden` |  `boolean` True if the sheet is hidden in the UI, false if it's visible.  
`index` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The index of the sheet within the spreadsheet. When adding or updating sheet properties, if this field is excluded then the sheet is added or moved to the end of the sheet list. When updating sheet indices or inserting sheets, movement is considered in "before the move" indexes. For example, if there were 3 sheets (S1, S2, S3) in order to move S1 ahead of S2 the index would have to be set to 2. A sheet index update request is ignored if the requested index is identical to the sheets current index or if the requested new index is equal to the current sheet index + 1.  
`rightToLeft` |  `boolean` True if the sheet is an RTL sheet instead of an LTR sheet.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the sheet. Must be non-negative. This field cannot be changed once set.  
`sheetType` |  `enum` The type of sheet. Defaults to GRID. This field cannot be changed once set.  
Enum type. Can be one of the following:  
`SHEET_TYPE_UNSPECIFIED` | Default value, do not use.  
`GRID` | The sheet is a grid.  
`OBJECT` | The sheet has no grid and instead has an object like a chart or image.  
`DATA_SOURCE` | The sheet connects with an external DataSource and shows the preview of data.  
`tabColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the tab in the UI. Deprecated: Use tab_color_style.  
`tabColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the tab in the UI. If tab_color is also set, this field takes precedence.  
`title` |  `string` The name of the sheet.  
  
## Slicer

A slicer in a sheet. Fields  
---  
`position` |  `object ([EmbeddedObjectPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedObjectPosition))` The position of the slicer. Note that slicer can be positioned only on existing sheet. Also, width and height of slicer can be automatically adjusted to keep it within permitted limits.  
`slicerId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the slicer.  
`spec` |  `object ([SlicerSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SlicerSpec))` The specification of the slicer.  
  
## SlicerSpec

The specifications of a slicer. Fields  
---  
`applyToPivotTables` |  `boolean` True if the filter should apply to pivot tables. If not set, default to `True`.  
`backgroundColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background color of the slicer. Deprecated: Use background_color_style.  
`backgroundColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background color of the slicer. If background_color is also set, this field takes precedence.  
`columnIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The column index in the data table on which the filter is applied to.  
`dataRange` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The data range of the slicer.  
`filterCriteria` |  `object ([FilterCriteria](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterCriteria))` The filtering criteria of the slicer.  
`horizontalAlignment` |  `enum` The horizontal alignment of title in the slicer. If unspecified, defaults to `LEFT`  
Enum type. Can be one of the following:  
`HORIZONTAL_ALIGN_UNSPECIFIED` | The horizontal alignment is not specified. Do not use this.  
`LEFT` | The text is explicitly aligned to the left of the cell.  
`CENTER` | The text is explicitly aligned to the center of the cell.  
`RIGHT` | The text is explicitly aligned to the right of the cell.  
`textFormat` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The text format of title in the slicer. The link field is not supported.  
`title` |  `string` The title of the slicer.  
  
## SortRangeRequest

Sorts data in rows based on a sort order per column. Fields  
---  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range to sort.  
`sortSpecs[]` |  `object ([SortSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SortSpec))` The sort order per column. Later specifications are used when values are equal in the earlier specifications.  
  
## SortSpec

A sort order associated with a specific column or row. Fields  
---  
`backgroundColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background fill color to sort by; cells with this fill color are sorted to the top. Mutually exclusive with foreground_color. Deprecated: Use background_color_style.  
`backgroundColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background fill color to sort by; cells with this fill color are sorted to the top. Mutually exclusive with foreground_color, and must be an RGB-type color. If background_color is also set, this field takes precedence.  
`dataSourceColumnReference` |  `object ([DataSourceColumnReference](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceColumnReference))` Reference to a data source column.  
`dimensionIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The dimension the sort should be applied to.  
`foregroundColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The foreground color to sort by; cells with this foreground color are sorted to the top. Mutually exclusive with background_color. Deprecated: Use foreground_color_style.  
`foregroundColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The foreground color to sort by; cells with this foreground color are sorted to the top. Mutually exclusive with background_color, and must be an RGB-type color. If foreground_color is also set, this field takes precedence.  
`sortOrder` |  `enum` The order data should be sorted.  
Enum type. Can be one of the following:  
`SORT_ORDER_UNSPECIFIED` | Default value, do not use this.  
`ASCENDING` | Sort ascending.  
`DESCENDING` | Sort descending.  
  
## SourceAndDestination

A combination of a source range and how to extend that source. Fields  
---  
`dimension` |  `enum` The dimension that data should be filled into.  
Enum type. Can be one of the following:  
`DIMENSION_UNSPECIFIED` | The default value, do not use.  
`ROWS` | Operates on the rows of a sheet.  
`COLUMNS` | Operates on the columns of a sheet.  
`fillLength` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of rows or columns that data should be filled into. Positive numbers expand beyond the last row or last column of the source. Negative numbers expand before the first row or first column of the source.  
`source` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The location of the data to use as the source of the autofill.  
  
## Spreadsheet

Resource that represents a spreadsheet. Fields  
---  
`dataSourceSchedules[]` |  `object ([DataSourceRefreshSchedule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceRefreshSchedule))` Output only. A list of data source refresh schedules.  
`dataSources[]` |  `object ([DataSource](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSource))` A list of external data sources connected with the spreadsheet.  
`developerMetadata[]` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The developer metadata associated with a spreadsheet.  
`namedRanges[]` |  `object ([NamedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#NamedRange))` The named ranges defined in a spreadsheet.  
`properties` |  `object ([SpreadsheetProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SpreadsheetProperties))` Overall properties of a spreadsheet.  
`sheets[]` |  `object ([Sheet](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Sheet))` The sheets that are part of a spreadsheet.  
`spreadsheetId` |  `string` The ID of the spreadsheet. This field is read-only.  
`spreadsheetUrl` |  `string` The url of the spreadsheet. This field is read-only.  
  
## SpreadsheetProperties

Properties of a spreadsheet. Fields  
---  
`autoRecalc` |  `enum` The amount of time to wait before volatile functions are recalculated.  
Enum type. Can be one of the following:  
`RECALCULATION_INTERVAL_UNSPECIFIED` | Default value. This value must not be used.  
`ON_CHANGE` | Volatile functions are updated on every change.  
`MINUTE` | Volatile functions are updated on every change and every minute.  
`HOUR` | Volatile functions are updated on every change and hourly.  
`defaultFormat` |  `object ([CellFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#CellFormat))` The default format of all cells in the spreadsheet. CellData.effectiveFormat will not be set if the cell's format is equal to this default format. This field is read-only.  
`iterativeCalculationSettings` |  `object ([IterativeCalculationSettings](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#IterativeCalculationSettings))` Determines whether and how circular references are resolved with iterative calculation. Absence of this field means that circular references result in calculation errors.  
`locale` |  `string` The locale of the spreadsheet in one of the following formats: * an ISO 639-1 language code such as `en` * an ISO 639-2 language code such as `fil`, if no 639-1 code exists * a combination of the ISO language code and country code, such as `en_US` Note: when updating this field, not all locales/languages are supported.  
`spreadsheetTheme` |  `object ([SpreadsheetTheme](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SpreadsheetTheme))` Theme applied to the spreadsheet.  
`timeZone` |  `string` The time zone of the spreadsheet, in CLDR format such as `America/New_York`. If the time zone isn't recognized, this may be a custom time zone such as `GMT-07:00`.  
`title` |  `string` The title of the spreadsheet.  
  
## SpreadsheetTheme

Represents spreadsheet theme Fields  
---  
`primaryFontFamily` |  `string` Name of the primary font family.  
`themeColors[]` |  `object ([ThemeColorPair](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ThemeColorPair))` The spreadsheet theme color pairs. To update you must provide all theme color pairs.  
  
## TextFormat

The format of a run of text in a cell. Absent values indicate that the field isn't specified. Fields  
---  
`bold` |  `boolean` True if the text is bold.  
`fontFamily` |  `string` The font family.  
`fontSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The size of the font.  
`foregroundColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The foreground color of the text. Deprecated: Use foreground_color_style.  
`foregroundColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The foreground color of the text. If foreground_color is also set, this field takes precedence.  
`italic` |  `boolean` True if the text is italicized.  
`link` |  `object ([Link](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Link))` The link destination of the text, if any. Setting the link field in a TextFormatRun will clear the cell's existing links or a cell-level link set in the same request. When a link is set, the text foreground color will be set to the default link color and the text will be underlined. If these fields are modified in the same request, those values will be used instead of the link defaults.  
`strikethrough` |  `boolean` True if the text has a strikethrough.  
`underline` |  `boolean` True if the text is underlined.  
  
## TextFormatRun

A run of a text format. The format of this run continues until the start index of the next run. When updating, all fields must be set. Fields  
---  
`format` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The format of this run. Absent values inherit the cell's format.  
`startIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The character index where this run starts.  
  
## TextPosition

Position settings for text. Fields  
---  
`horizontalAlignment` |  `enum` Horizontal alignment setting for the piece of text.  
Enum type. Can be one of the following:  
`HORIZONTAL_ALIGN_UNSPECIFIED` | The horizontal alignment is not specified. Do not use this.  
`LEFT` | The text is explicitly aligned to the left of the cell.  
`CENTER` | The text is explicitly aligned to the center of the cell.  
`RIGHT` | The text is explicitly aligned to the right of the cell.  
  
## TextRotation

The rotation applied to text in a cell. Fields  
---  
`angle` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The angle between the standard orientation and the desired orientation. Measured in degrees. Valid values are between -90 and 90. Positive angles are angled upwards, negative are angled downwards. Note: For LTR text direction positive angles are in the counterclockwise direction, whereas for RTL they are in the clockwise direction  
`vertical` |  `boolean` If true, text reads top to bottom, but the orientation of individual characters is unchanged. For example: | V | | e | | r | | t | | i | | c | | a | | l |  
  
## TextToColumnsRequest

Splits a column of text into multiple columns, based on a delimiter in each cell. Fields  
---  
`delimiter` |  `string` The delimiter to use. Used only if delimiterType is CUSTOM.  
`delimiterType` |  `enum` The delimiter type to use.  
Enum type. Can be one of the following:  
`DELIMITER_TYPE_UNSPECIFIED` | Default value. This value must not be used.  
`COMMA` | ","  
`SEMICOLON` | ";"  
`PERIOD` | "."  
`SPACE` | " "  
`CUSTOM` | A custom value as defined in delimiter.  
`AUTODETECT` | Automatically detect columns.  
`source` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The source data range. This must span exactly one column.  
  
## ThemeColorPair

A pair mapping a spreadsheet theme color type to the concrete color it represents. Fields  
---  
`color` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The concrete color corresponding to the theme color type.  
`colorType` |  `enum` The type of the spreadsheet theme color.  
Enum type. Can be one of the following:  
`THEME_COLOR_TYPE_UNSPECIFIED` | Unspecified theme color  
`TEXT` | Represents the primary text color  
`BACKGROUND` | Represents the primary background color  
`ACCENT1` | Represents the first accent color  
`ACCENT2` | Represents the second accent color  
`ACCENT3` | Represents the third accent color  
`ACCENT4` | Represents the fourth accent color  
`ACCENT5` | Represents the fifth accent color  
`ACCENT6` | Represents the sixth accent color  
`LINK` | Represents the color to use for hyperlinks  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are google.type.Date and `google.protobuf.Timestamp`. Fields  
---  
`hours` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Hours of day in 24 hour format. Should be from 0 to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Minutes of hour of day. Must be from 0 to 59.  
`nanos` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.  
`seconds` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Seconds of minutes of the time. Must normally be from 0 to 59. An API may allow the value 60 if it allows leap-seconds.  
  
## TreemapChartColorScale

A color scale for a treemap chart. Fields  
---  
`maxValueColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background color for cells with a color value greater than or equal to maxValue. Defaults to #109618 if not specified. Deprecated: Use max_value_color_style.  
`maxValueColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background color for cells with a color value greater than or equal to maxValue. Defaults to #109618 if not specified. If max_value_color is also set, this field takes precedence.  
`midValueColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background color for cells with a color value at the midpoint between minValue and maxValue. Defaults to #efe6dc if not specified. Deprecated: Use mid_value_color_style.  
`midValueColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background color for cells with a color value at the midpoint between minValue and maxValue. Defaults to #efe6dc if not specified. If mid_value_color is also set, this field takes precedence.  
`minValueColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background color for cells with a color value less than or equal to minValue. Defaults to #dc3912 if not specified. Deprecated: Use min_value_color_style.  
`minValueColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background color for cells with a color value less than or equal to minValue. Defaults to #dc3912 if not specified. If min_value_color is also set, this field takes precedence.  
`noDataColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background color for cells that have no color data associated with them. Defaults to #000000 if not specified. Deprecated: Use no_data_color_style.  
`noDataColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background color for cells that have no color data associated with them. Defaults to #000000 if not specified. If no_data_color is also set, this field takes precedence.  
  
## TreemapChartSpec

A Treemap chart. Fields  
---  
`colorData` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data that determines the background color of each treemap data cell. This field is optional. If not specified, size_data is used to determine background colors. If specified, the data is expected to be numeric. color_scale will determine how the values in this data map to data cell background colors.  
`colorScale` |  `object ([TreemapChartColorScale](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TreemapChartColorScale))` The color scale for data cells in the treemap chart. Data cells are assigned colors based on their color values. These color values come from color_data, or from size_data if color_data is not specified. Cells with color values less than or equal to min_value will have minValueColor as their background color. Cells with color values greater than or equal to max_value will have maxValueColor as their background color. Cells with color values between min_value and max_value will have background colors on a gradient between minValueColor and maxValueColor, the midpoint of the gradient being midValueColor. Cells with missing or non-numeric color values will have noDataColor as their background color.  
`headerColor` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The background color for header cells. Deprecated: Use header_color_style.  
`headerColorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The background color for header cells. If header_color is also set, this field takes precedence.  
`hideTooltips` |  `boolean` True to hide tooltips.  
`hintedLevels` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of additional data levels beyond the labeled levels to be shown on the treemap chart. These levels are not interactive and are shown without their labels. Defaults to 0 if not specified.  
`labels` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data that contains the treemap cell labels.  
`levels` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of data levels to show on the treemap chart. These levels are interactive and are shown with their labels. Defaults to 2 if not specified.  
`maxValue` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum possible data value. Cells with values greater than this will have the same color as cells with this value. If not specified, defaults to the actual maximum value from color_data, or the maximum value from size_data if color_data is not specified.  
`minValue` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The minimum possible data value. Cells with values less than this will have the same color as cells with this value. If not specified, defaults to the actual minimum value from color_data, or the minimum value from size_data if color_data is not specified.  
`parentLabels` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data the contains the treemap cells' parent labels.  
`sizeData` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data that determines the size of each treemap data cell. This data is expected to be numeric. The cells corresponding to non-numeric or missing data will not be rendered. If color_data is not specified, this data is used to determine data cell background colors as well.  
`textFormat` |  `object ([TextFormat](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#TextFormat))` The text format for all labels on the chart. The link field is not supported.  
  
## TrimWhitespaceRequest

Trims the whitespace (such as spaces, tabs, or new lines) in every cell in the specified range. This request removes all whitespace from the start and end of each cell's text, and reduces any subsequence of remaining whitespace characters to a single space. If the resulting trimmed text starts with a '+' or '=' character, the text remains as a string value and isn't interpreted as a formula. Fields  
---  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range whose cells to trim.  
  
## TrimWhitespaceResponse

The result of trimming whitespace in cells. Fields  
---  
`cellsChangedCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of cells that were trimmed of whitespace.  
  
## UnmergeCellsRequest

Unmerges cells in the given range. Fields  
---  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range within which all cells should be unmerged. If the range spans multiple merges, all will be unmerged. The range must not partially span any merge.  
  
## UpdateBandingRequest

Updates properties of the supplied banded range. Fields  
---  
`bandedRange` |  `object ([BandedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#BandedRange))` The banded range to update with the new properties.  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `bandedRange` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
  
## UpdateBordersRequest

Updates the borders of a range. If a field is not set in the request, that means the border remains as-is. For example, with two subsequent UpdateBordersRequest: 1. range: A1:A5 `{ top: RED, bottom: WHITE }` 2\. range: A1:A5 `{ left: BLUE }` That would result in A1:A5 having a borders of `{ top: RED, bottom: WHITE, left: BLUE }`. If you want to clear a border, explicitly set the style to NONE. Fields  
---  
`bottom` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The border to put at the bottom of the range.  
`innerHorizontal` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The horizontal border to put within the range.  
`innerVertical` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The vertical border to put within the range.  
`left` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The border to put at the left of the range.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range whose borders should be updated.  
`right` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The border to put at the right of the range.  
`top` |  `object ([Border](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Border))` The border to put at the top of the range.  
  
## UpdateCellsRequest

Updates all cells in a range with new data. Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields of CellData that should be updated. At least one field must be specified. The root is the CellData; 'row.values.' should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`range` |  `object ([GridRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridRange))` The range to write data to. If the data in rows does not cover the entire requested range, the fields matching those set in fields will be cleared.  
`rows[]` |  `object ([RowData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#RowData))` The data to write.  
`start` |  `object ([GridCoordinate](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#GridCoordinate))` The coordinate to start writing data at. Any number of rows and columns (including a different number of columns per row) may be written.  
  
## UpdateChartSpecRequest

Updates a chart's specifications. (This does not move or resize a chart. To move or resize a chart, use UpdateEmbeddedObjectPositionRequest.) Fields  
---  
`chartId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the chart to update.  
`spec` |  `object ([ChartSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartSpec))` The specification to apply to the chart.  
  
## UpdateConditionalFormatRuleRequest

Updates a conditional format rule at the given index, or moves a conditional format rule to another index. Fields  
---  
`index` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The zero-based index of the rule that should be replaced or moved.  
`newIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The zero-based new index the rule should end up at.  
`rule` |  `object ([ConditionalFormatRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ConditionalFormatRule))` The rule that should replace the rule at the given index.  
`sheetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The sheet of the rule to move. Required if new_index is set, unused otherwise.  
  
## UpdateConditionalFormatRuleResponse

The result of updating a conditional format rule. Fields  
---  
`newIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The index of the new rule.  
`newRule` |  `object ([ConditionalFormatRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ConditionalFormatRule))` The new rule that replaced the old rule (if replacing), or the rule that was moved (if moved)  
`oldIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The old index of the rule. Not set if a rule was replaced (because it is the same as new_index).  
`oldRule` |  `object ([ConditionalFormatRule](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ConditionalFormatRule))` The old (deleted) rule. Not set if a rule was moved (because it is the same as new_rule).  
  
## UpdateDataSourceRequest

Updates a data source. After the data source is updated successfully, an execution is triggered to refresh the associated DATA_SOURCE sheet to read data from the updated data source. The request requires an additional `bigquery.readonly` OAuth scope. Fields  
---  
`dataSource` |  `object ([DataSource](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSource))` The data source to update.  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `dataSource` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
  
## UpdateDataSourceResponse

The response from updating data source. Fields  
---  
`dataExecutionStatus` |  `object ([DataExecutionStatus](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataExecutionStatus))` The data execution status.  
`dataSource` |  `object ([DataSource](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSource))` The updated data source.  
  
## UpdateDeveloperMetadataRequest

A request to update properties of developer metadata. Updates the properties of the developer metadata selected by the filters to the values provided in the DeveloperMetadata resource. Callers must specify the properties they wish to update in the fields parameter, as well as specify at least one DataFilter matching the metadata they wish to update. Fields  
---  
`dataFilters[]` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The filters matching the developer metadata entries to update.  
`developerMetadata` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The value that all metadata matched by the data filters will be updated to.  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `developerMetadata` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
  
## UpdateDeveloperMetadataResponse

The response from updating developer metadata. Fields  
---  
`developerMetadata[]` |  `object ([DeveloperMetadata](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DeveloperMetadata))` The updated developer metadata.  
  
## UpdateDimensionGroupRequest

Updates the state of the specified group. Fields  
---  
`dimensionGroup` |  `object ([DimensionGroup](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionGroup))` The group whose state should be updated. The range and depth of the group should specify a valid group on the sheet, and all other fields updated.  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `dimensionGroup` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
  
## UpdateDimensionPropertiesRequest

Updates properties of dimensions within the specified range. Fields  
---  
`dataSourceSheetRange` |  `object ([DataSourceSheetDimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataSourceSheetDimensionRange))` The columns on a data source sheet to update.  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `properties` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`properties` |  `object ([DimensionProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionProperties))` Properties to update.  
`range` |  `object ([DimensionRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DimensionRange))` The rows or columns to update.  
  
## UpdateEmbeddedObjectBorderRequest

Updates an embedded object's border property. Fields  
---  
`border` |  `object ([EmbeddedObjectBorder](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedObjectBorder))` The border that applies to the embedded object.  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `border` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`objectId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the embedded object to update.  
  
## UpdateEmbeddedObjectPositionRequest

Update an embedded object's position (such as a moving or resizing a chart or image). Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields of OverlayPosition that should be updated when setting a new position. Used only if newPosition.overlayPosition is set, in which case at least one field must be specified. The root `newPosition.overlayPosition` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`newPosition` |  `object ([EmbeddedObjectPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedObjectPosition))` An explicit position to move the embedded object to. If newPosition.sheetId is set, a new sheet with that ID will be created. If newPosition.newSheet is set to true, a new sheet will be created with an ID that will be chosen for you.  
`objectId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of the object to moved.  
  
## UpdateEmbeddedObjectPositionResponse

The result of updating an embedded object's position. Fields  
---  
`position` |  `object ([EmbeddedObjectPosition](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#EmbeddedObjectPosition))` The new position of the embedded object.  
  
## UpdateFilterViewRequest

Updates properties of the filter view. Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `filter` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`filter` |  `object ([FilterView](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#FilterView))` The new properties of the filter view.  
  
## UpdateNamedRangeRequest

Updates properties of the named range with the specified namedRangeId. Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `namedRange` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`namedRange` |  `object ([NamedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#NamedRange))` The named range to update with the new properties.  
  
## UpdateProtectedRangeRequest

Updates an existing protected range with the specified protectedRangeId. Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `protectedRange` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`protectedRange` |  `object ([ProtectedRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ProtectedRange))` The protected range to update with the new properties.  
  
## UpdateSheetPropertiesRequest

Updates properties of the sheet with the specified sheetId. Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `properties` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`properties` |  `object ([SheetProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SheetProperties))` The properties to update.  
  
## UpdateSlicerSpecRequest

Updates a slicer's specifications. (This does not move or resize a slicer. To move or resize a slicer use UpdateEmbeddedObjectPositionRequest. Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root `SlicerSpec` is implied and should not be specified. A single "*"` can be used as short-hand for listing every field.  
`slicerId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The id of the slicer to update.  
`spec` |  `object ([SlicerSpec](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SlicerSpec))` The specification to apply to the slicer.  
  
## UpdateSpreadsheetPropertiesRequest

Updates properties of a spreadsheet. Fields  
---  
`fields` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` The fields that should be updated. At least one field must be specified. The root 'properties' is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.  
`properties` |  `object ([SpreadsheetProperties](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#SpreadsheetProperties))` The properties to update.  
  
## UpdateValuesByDataFilterResponse

The response when updating a range of values by a data filter in a spreadsheet. Fields  
---  
`dataFilter` |  `object ([DataFilter](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataFilter))` The data filter that selected the range that was updated.  
`updatedCells` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of cells updated.  
`updatedColumns` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of columns where at least one cell in the column was updated.  
`updatedData` |  `object ([ValueRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ValueRange))` The values of the cells in the range matched by the dataFilter after all updates were applied. This is only included if the request's `includeValuesInResponse` field was `true`.  
`updatedRange` |  `string` The range (in [A1 notation](https://developers.google.com/sheets/api/guides/concepts#cell)) that updates were applied to.  
`updatedRows` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of rows where at least one cell in the row was updated.  
  
## UpdateValuesResponse

The response when updating a range of values in a spreadsheet. Fields  
---  
`spreadsheetId` |  `string` The spreadsheet the updates were applied to.  
`updatedCells` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of cells updated.  
`updatedColumns` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of columns where at least one cell in the column was updated.  
`updatedData` |  `object ([ValueRange](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ValueRange))` The values of the cells after updates were applied. This is only included if the request's `includeValuesInResponse` field was `true`.  
`updatedRange` |  `string` The range (in A1 notation) that updates were applied to.  
`updatedRows` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of rows where at least one cell in the row was updated.  
  
## ValueRange

Data within a range of the spreadsheet. Fields  
---  
`majorDimension` |  `enum` The major dimension of the values. For output, if the spreadsheet data is: `A1=1,B1=2,A2=3,B2=4`, then requesting `range=A1:B2,majorDimension=ROWS` will return `[[1,2],[3,4]]`, whereas requesting `range=A1:B2,majorDimension=COLUMNS` will return `[[1,3],[2,4]]`. For input, with `range=A1:B2,majorDimension=ROWS` then `[[1,2],[3,4]]` will set `A1=1,B1=2,A2=3,B2=4`. With `range=A1:B2,majorDimension=COLUMNS` then `[[1,2],[3,4]]` will set `A1=1,B1=3,A2=2,B2=4`. When writing, if this field is not set, it defaults to ROWS.  
Enum type. Can be one of the following:  
`DIMENSION_UNSPECIFIED` | The default value, do not use.  
`ROWS` | Operates on the rows of a sheet.  
`COLUMNS` | Operates on the columns of a sheet.  
`range` |  `string` The range the values cover, in [A1 notation](https://developers.google.com/sheets/api/guides/concepts#cell). For output, this range indicates the entire requested range, even though the values will exclude trailing rows and columns. When appending values, this field represents the range to search for a table, after which values will be appended.  
`values[]` |  `array` The data that was read or to be written. This is an array of arrays, the outer array representing all the data and each inner array representing a major dimension. Each item in the inner array corresponds with one cell. For output, empty trailing rows and columns will not be included. For input, supported value types are: bool, string, and double. Null values will be skipped. To set a cell to an empty value, set the string value to an empty string.  
  
## WaterfallChartColumnStyle

Styles for a waterfall chart column. Fields  
---  
`color` |  `object ([Color](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#Color))` The color of the column. Deprecated: Use color_style.  
`colorStyle` |  `object ([ColorStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ColorStyle))` The color of the column. If color is also set, this field takes precedence.  
`label` |  `string` The label of the column's legend.  
  
## WaterfallChartCustomSubtotal

A custom subtotal column for a waterfall chart series. Fields  
---  
`dataIsSubtotal` |  `boolean` True if the data point at subtotal_index is the subtotal. If false, the subtotal will be computed and appear after the data point.  
`label` |  `string` A label for the subtotal column.  
`subtotalIndex` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The 0-based index of a data point within the series. If data_is_subtotal is true, the data point at this index is the subtotal. Otherwise, the subtotal appears after the data point with this index. A series can have multiple subtotals at arbitrary indices, but subtotals do not affect the indices of the data points. For example, if a series has three data points, their indices will always be 0, 1, and 2, regardless of how many subtotals exist on the series or what data points they are associated with.  
  
## WaterfallChartDomain

The domain of a waterfall chart. Fields  
---  
`data` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data of the WaterfallChartDomain.  
`reversed` |  `boolean` True to reverse the order of the domain values (horizontal axis).  
  
## WaterfallChartSeries

A single series of data for a waterfall chart. Fields  
---  
`customSubtotals[]` |  `object ([WaterfallChartCustomSubtotal](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#WaterfallChartCustomSubtotal))` Custom subtotal columns appearing in this series. The order in which subtotals are defined is not significant. Only one subtotal may be defined for each data point.  
`data` |  `object ([ChartData](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#ChartData))` The data being visualized in this series.  
`dataLabel` |  `object ([DataLabel](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataLabel))` Information about the data labels for this series.  
`hideTrailingSubtotal` |  `boolean` True to hide the subtotal column from the end of the series. By default, a subtotal column will appear at the end of each series. Setting this field to true will hide that subtotal column for this series.  
`negativeColumnsStyle` |  `object ([WaterfallChartColumnStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#WaterfallChartColumnStyle))` Styles for all columns in this series with negative values.  
`positiveColumnsStyle` |  `object ([WaterfallChartColumnStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#WaterfallChartColumnStyle))` Styles for all columns in this series with positive values.  
`subtotalColumnsStyle` |  `object ([WaterfallChartColumnStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#WaterfallChartColumnStyle))` Styles for all subtotal columns in this series.  
  
## WaterfallChartSpec

A waterfall chart. Fields  
---  
`connectorLineStyle` |  `object ([LineStyle](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#LineStyle))` The line style for the connector lines.  
`domain` |  `object ([WaterfallChartDomain](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#WaterfallChartDomain))` The domain data (horizontal axis) for the waterfall chart.  
`firstValueIsTotal` |  `boolean` True to interpret the first value as a total.  
`hideConnectorLines` |  `boolean` True to hide connector lines between columns.  
`series[]` |  `object ([WaterfallChartSeries](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#WaterfallChartSeries))` The data this waterfall chart is visualizing.  
`stackedType` |  `enum` The stacked type.  
Enum type. Can be one of the following:  
`WATERFALL_STACKED_TYPE_UNSPECIFIED` | Default value, do not use.  
`STACKED` | Values corresponding to the same domain (horizontal axis) value will be stacked vertically.  
`SEQUENTIAL` | Series will spread out along the horizontal axis.  
`totalDataLabel` |  `object ([DataLabel](https://cloud.google.com/workflows/docs/reference/googleapis/sheets/v4/Overview#DataLabel))` Controls whether to display additional data labels on stacked charts which sum the total value of all stacked values at each value along the domain axis. stacked_type must be STACKED and neither CUSTOM nor placement can be set on the total_data_label.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
