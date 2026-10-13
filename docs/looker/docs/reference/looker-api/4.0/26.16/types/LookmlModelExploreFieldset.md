---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldset/
title: LookmlModelExploreFieldset \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:03:13.544568+00:00
---

# LookmlModelExploreFieldset  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  LookmlModelExploreFieldset Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

dimensions

[LookmlModelExploreField](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreField)[] 

Expand LookmlModelExploreField definition... 

align

_lock_

string 

The appropriate horizontal text alignment the values of this field should be displayed in. Valid values are: "left", "right".

available_custom_timeframes

string[] 

timeframe_labels

_lock_

object 

A map of timeframe keys to their localized labels.

can_filter

_lock_

boolean 

Whether it's possible to filter on this field.

category

_lock_

string 

Field category Valid values are: "parameter", "filter", "measure", "dimension".

default_filter_value

_lock_

string 

The default value that this field uses when filtering. Null if there is no default value.

description

_lock_

string 

Description

dimension_group

_lock_

string 

Dimension group if this field is part of a dimension group. If not, this will be null.

drill_fields

string[] 

enumerations

[LookmlModelExploreFieldEnumeration](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldEnumeration)[] 

Expand LookmlModelExploreFieldEnumeration definition... 

label

_lock_

string 

Label

value

_lock_

any 

Value

error

_lock_

string 

An error message indicating a problem with the definition of this field. If there are no errors, this will be null.

field_group_label

_lock_

string 

A label creating a grouping of fields. All fields with this label should be presented together when displayed in a UI.

field_group_variant

_lock_

string 

When presented in a field group via field_group_label, a shorter name of the field to be displayed in that context.

fill_style

_lock_

string 

The style of dimension fill that is possible for this field. Null if no dimension fill is possible. Valid values are: "enumeration", "range".

fiscal_month_offset

_lock_

integer 

An offset (in months) from the calendar start month to the fiscal start month defined in the LookML model this field belongs to.

has_allowed_values

_lock_

boolean 

Whether this field has a set of allowed_values specified in LookML.

has_drills_metadata

_lock_

boolean 

Whether this field has links or drill fields defined.

hidden

_lock_

boolean 

Whether this field should be hidden from the user interface.

is_filter

_lock_

boolean 

Whether this field is a filter.

is_fiscal

_lock_

boolean 

Whether this field represents a fiscal time value.

is_numeric

_lock_

boolean 

Whether this field is of a type that represents a numeric value.

is_timeframe

_lock_

boolean 

Whether this field is of a type that represents a time value.

can_time_filter

_lock_

boolean 

Whether this field can be time filtered.

time_interval

_lock_

[LookmlModelExploreFieldTimeInterval](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldTimeInterval)

Details on the time interval this field represents, if it is_timeframe.

Expand LookmlModelExploreFieldTimeInterval definition... 

name

_lock_

string 

The type of time interval this field represents a grouping of. Valid values are: "day", "hour", "minute", "second", "millisecond", "microsecond", "week", "month", "quarter", "year".

count

_lock_

integer 

The number of intervals this field represents a grouping of.

label

_lock_

string 

Fully-qualified human-readable label of the field.

label_from_parameter

_lock_

string 

The name of the parameter that will provide a parameterized label for this field, if available in the current context.

label_short

_lock_

string 

The human-readable label of the field, without the view label.

lookml_link

_lock_

string 

A URL linking to the definition of this field in the LookML IDE.

links

[LookmlFieldLink](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlFieldLink)[] 

Expand LookmlFieldLink definition... 

label

_lock_

string 

The name of the link as it would appear to users.

url

_lock_

string 

URL the link will go to.

icon_url

_lock_

string 

A URL containing an image file to display with a link.

map_layer

_lock_

[LookmlModelExploreFieldMapLayer](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldMapLayer)

If applicable, a map layer this field is associated with.

Expand LookmlModelExploreFieldMapLayer definition... 

url

_lock_

string 

URL to the map layer resource.

name

_lock_

string 

Name of the map layer, as defined in LookML.

feature_key

_lock_

string 

Specifies the name of the TopoJSON object that the map layer references. If not specified, use the first object..

property_key

_lock_

string 

Selects which property from the TopoJSON data to plot against. TopoJSON supports arbitrary metadata for each region. When null, the first matching property should be used.

property_label_key

_lock_

string 

Which property from the TopoJSON data to use to label the region. When null, property_key should be used.

projection

_lock_

string 

The preferred geographic projection of the map layer when displayed in a visualization that supports multiple geographic projections.

format

_lock_

string 

Specifies the data format of the region information. Valid values are: "topojson", "vector_tile_region".

extents_json_url

_lock_

string 

Specifies the URL to a JSON file that defines the geographic extents of each region available in the map layer. This data is used to automatically center the map on the available data for visualization purposes. The JSON file must be a JSON object where the keys are the mapping value of the feature (as specified by property_key) and the values are arrays of four numbers representing the west longitude, south latitude, east longitude, and north latitude extents of the region. The object must include a key for every possible value of property_key.

max_zoom_level

_lock_

integer 

The minimum zoom level that the map layer may be displayed at, for visualizations that support zooming.

min_zoom_level

_lock_

integer 

The maximum zoom level that the map layer may be displayed at, for visualizations that support zooming.

measure

_lock_

boolean 

Whether this field is a measure.

name

_lock_

string 

Fully-qualified name of the field.

strict_value_format

_lock_

boolean 

If yes, the field will not be localized with the user attribute number_format. Defaults to no

parameter

_lock_

boolean 

Whether this field is a parameter.

period_over_period_params

_lock_

[LookmlModelExploreFieldPeriodOverPeriodParams](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldPeriodOverPeriodParams)

For measures of type period_over_period, this will return the individual metadata parameters.

Expand LookmlModelExploreFieldPeriodOverPeriodParams definition... 

based_on

_lock_

string 

Specifies the measure that will be calculated over the different periods.

based_on_time

_lock_

string 

Specifies the time dimension that this measure will operate over.

period

_lock_

string 

Specifies the time frame for the comparison. Valid values are: "year", "fiscal_year", "quarter", "fiscal_quarter", "month", "week", "date".

kind

_lock_

string 

The type of calculation for the period_over_period measure. Valid values are: "previous", "difference", "relative_change".

value_to_date

_lock_

boolean 

specifies whether to compare the current partially completed period to an equivalent part of the previous period, or to use the entire previous period.

permanent

_lock_

boolean 

Whether this field can be removed from a query.

primary_key

_lock_

boolean 

Whether or not the field represents a primary key.

project_name

_lock_

string 

The name of the project this field is defined in.

requires_refresh_on_sort

_lock_

boolean 

When true, it's not possible to re-sort this field's values without re-running the SQL query, due to database logic that affects the sort.

scope

_lock_

string 

The LookML scope this field belongs to. The scope is typically the field's view.

sortable

_lock_

boolean 

Whether this field can be sorted.

source_file

_lock_

string 

The path portion of source_file_path.

source_file_path

_lock_

string 

The fully-qualified path of the project file this field is defined in.

sql

_lock_

string 

SQL expression as defined in the LookML model. The SQL syntax shown here is a representation intended for auditability, and is not neccessarily an exact match for what will ultimately be run in the database. It may contain special LookML syntax or annotations that are not valid SQL. This will be null if the current user does not have the see_lookml permission for the field's model.

sql_case

[LookmlModelExploreFieldSqlCase](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldSqlCase)[] 

Expand LookmlModelExploreFieldSqlCase definition... 

value

_lock_

string 

SQL Case label value

condition

_lock_

string 

SQL Case condition expression

filters

[LookmlModelExploreFieldMeasureFilters](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldMeasureFilters)[] 

Expand LookmlModelExploreFieldMeasureFilters definition... 

field

_lock_

string 

Filter field name

condition

_lock_

string 

Filter condition value

suggest_dimension

_lock_

string 

The name of the dimension to base suggest queries from.

suggest_explore

_lock_

string 

The name of the explore to base suggest queries from.

suggestable

_lock_

boolean 

Whether or not suggestions are possible for this field.

suggestions

string[] 

synonyms

string[] 

tags

string[] 

type

_lock_

string 

The LookML type of the field.

user_attribute_filter_types

string[] 

value_format

_lock_

string 

If specified, the LookML value format string for formatting values of this field.

value_format_name

_lock_

string 

If specified, the name of the value format, as defined in the LookML model.

view

_lock_

string 

The name of the view this field belongs to.

view_label

_lock_

string 

The human-readable label of the view the field belongs to.

dynamic

_lock_

boolean 

Whether this field was specified in "dynamic_fields" and is not part of the model.

week_start_day

_lock_

string 

The name of the starting day of the week. Valid values are: "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday".

times_used

_lock_

integer 

The number of times this field has been used in queries

original_view

_lock_

string 

The name of the view this field is defined in. This will be different than "view" when the view has been joined via a different name using the "from" parameter.

datatype

_lock_

string 

The data_type for a date in lookml

convert_tz

_lock_

boolean 

Whether time zones should be converted for datetime fields

measures

[LookmlModelExploreField](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreField)[] 

Expand LookmlModelExploreField definition... 

align

_lock_

string 

The appropriate horizontal text alignment the values of this field should be displayed in. Valid values are: "left", "right".

available_custom_timeframes

string[] 

timeframe_labels

_lock_

object 

A map of timeframe keys to their localized labels.

can_filter

_lock_

boolean 

Whether it's possible to filter on this field.

category

_lock_

string 

Field category Valid values are: "parameter", "filter", "measure", "dimension".

default_filter_value

_lock_

string 

The default value that this field uses when filtering. Null if there is no default value.

description

_lock_

string 

Description

dimension_group

_lock_

string 

Dimension group if this field is part of a dimension group. If not, this will be null.

drill_fields

string[] 

enumerations

[LookmlModelExploreFieldEnumeration](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldEnumeration)[] 

Expand LookmlModelExploreFieldEnumeration definition... 

label

_lock_

string 

Label

value

_lock_

any 

Value

error

_lock_

string 

An error message indicating a problem with the definition of this field. If there are no errors, this will be null.

field_group_label

_lock_

string 

A label creating a grouping of fields. All fields with this label should be presented together when displayed in a UI.

field_group_variant

_lock_

string 

When presented in a field group via field_group_label, a shorter name of the field to be displayed in that context.

fill_style

_lock_

string 

The style of dimension fill that is possible for this field. Null if no dimension fill is possible. Valid values are: "enumeration", "range".

fiscal_month_offset

_lock_

integer 

An offset (in months) from the calendar start month to the fiscal start month defined in the LookML model this field belongs to.

has_allowed_values

_lock_

boolean 

Whether this field has a set of allowed_values specified in LookML.

has_drills_metadata

_lock_

boolean 

Whether this field has links or drill fields defined.

hidden

_lock_

boolean 

Whether this field should be hidden from the user interface.

is_filter

_lock_

boolean 

Whether this field is a filter.

is_fiscal

_lock_

boolean 

Whether this field represents a fiscal time value.

is_numeric

_lock_

boolean 

Whether this field is of a type that represents a numeric value.

is_timeframe

_lock_

boolean 

Whether this field is of a type that represents a time value.

can_time_filter

_lock_

boolean 

Whether this field can be time filtered.

time_interval

_lock_

[LookmlModelExploreFieldTimeInterval](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldTimeInterval)

Details on the time interval this field represents, if it is_timeframe.

Expand LookmlModelExploreFieldTimeInterval definition... 

name

_lock_

string 

The type of time interval this field represents a grouping of. Valid values are: "day", "hour", "minute", "second", "millisecond", "microsecond", "week", "month", "quarter", "year".

count

_lock_

integer 

The number of intervals this field represents a grouping of.

label

_lock_

string 

Fully-qualified human-readable label of the field.

label_from_parameter

_lock_

string 

The name of the parameter that will provide a parameterized label for this field, if available in the current context.

label_short

_lock_

string 

The human-readable label of the field, without the view label.

lookml_link

_lock_

string 

A URL linking to the definition of this field in the LookML IDE.

links

[LookmlFieldLink](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlFieldLink)[] 

Expand LookmlFieldLink definition... 

label

_lock_

string 

The name of the link as it would appear to users.

url

_lock_

string 

URL the link will go to.

icon_url

_lock_

string 

A URL containing an image file to display with a link.

map_layer

_lock_

[LookmlModelExploreFieldMapLayer](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldMapLayer)

If applicable, a map layer this field is associated with.

Expand LookmlModelExploreFieldMapLayer definition... 

url

_lock_

string 

URL to the map layer resource.

name

_lock_

string 

Name of the map layer, as defined in LookML.

feature_key

_lock_

string 

Specifies the name of the TopoJSON object that the map layer references. If not specified, use the first object..

property_key

_lock_

string 

Selects which property from the TopoJSON data to plot against. TopoJSON supports arbitrary metadata for each region. When null, the first matching property should be used.

property_label_key

_lock_

string 

Which property from the TopoJSON data to use to label the region. When null, property_key should be used.

projection

_lock_

string 

The preferred geographic projection of the map layer when displayed in a visualization that supports multiple geographic projections.

format

_lock_

string 

Specifies the data format of the region information. Valid values are: "topojson", "vector_tile_region".

extents_json_url

_lock_

string 

Specifies the URL to a JSON file that defines the geographic extents of each region available in the map layer. This data is used to automatically center the map on the available data for visualization purposes. The JSON file must be a JSON object where the keys are the mapping value of the feature (as specified by property_key) and the values are arrays of four numbers representing the west longitude, south latitude, east longitude, and north latitude extents of the region. The object must include a key for every possible value of property_key.

max_zoom_level

_lock_

integer 

The minimum zoom level that the map layer may be displayed at, for visualizations that support zooming.

min_zoom_level

_lock_

integer 

The maximum zoom level that the map layer may be displayed at, for visualizations that support zooming.

measure

_lock_

boolean 

Whether this field is a measure.

name

_lock_

string 

Fully-qualified name of the field.

strict_value_format

_lock_

boolean 

If yes, the field will not be localized with the user attribute number_format. Defaults to no

parameter

_lock_

boolean 

Whether this field is a parameter.

period_over_period_params

_lock_

[LookmlModelExploreFieldPeriodOverPeriodParams](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldPeriodOverPeriodParams)

For measures of type period_over_period, this will return the individual metadata parameters.

Expand LookmlModelExploreFieldPeriodOverPeriodParams definition... 

based_on

_lock_

string 

Specifies the measure that will be calculated over the different periods.

based_on_time

_lock_

string 

Specifies the time dimension that this measure will operate over.

period

_lock_

string 

Specifies the time frame for the comparison. Valid values are: "year", "fiscal_year", "quarter", "fiscal_quarter", "month", "week", "date".

kind

_lock_

string 

The type of calculation for the period_over_period measure. Valid values are: "previous", "difference", "relative_change".

value_to_date

_lock_

boolean 

specifies whether to compare the current partially completed period to an equivalent part of the previous period, or to use the entire previous period.

permanent

_lock_

boolean 

Whether this field can be removed from a query.

primary_key

_lock_

boolean 

Whether or not the field represents a primary key.

project_name

_lock_

string 

The name of the project this field is defined in.

requires_refresh_on_sort

_lock_

boolean 

When true, it's not possible to re-sort this field's values without re-running the SQL query, due to database logic that affects the sort.

scope

_lock_

string 

The LookML scope this field belongs to. The scope is typically the field's view.

sortable

_lock_

boolean 

Whether this field can be sorted.

source_file

_lock_

string 

The path portion of source_file_path.

source_file_path

_lock_

string 

The fully-qualified path of the project file this field is defined in.

sql

_lock_

string 

SQL expression as defined in the LookML model. The SQL syntax shown here is a representation intended for auditability, and is not neccessarily an exact match for what will ultimately be run in the database. It may contain special LookML syntax or annotations that are not valid SQL. This will be null if the current user does not have the see_lookml permission for the field's model.

sql_case

[LookmlModelExploreFieldSqlCase](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldSqlCase)[] 

Expand LookmlModelExploreFieldSqlCase definition... 

value

_lock_

string 

SQL Case label value

condition

_lock_

string 

SQL Case condition expression

filters

[LookmlModelExploreFieldMeasureFilters](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldMeasureFilters)[] 

Expand LookmlModelExploreFieldMeasureFilters definition... 

field

_lock_

string 

Filter field name

condition

_lock_

string 

Filter condition value

suggest_dimension

_lock_

string 

The name of the dimension to base suggest queries from.

suggest_explore

_lock_

string 

The name of the explore to base suggest queries from.

suggestable

_lock_

boolean 

Whether or not suggestions are possible for this field.

suggestions

string[] 

synonyms

string[] 

tags

string[] 

type

_lock_

string 

The LookML type of the field.

user_attribute_filter_types

string[] 

value_format

_lock_

string 

If specified, the LookML value format string for formatting values of this field.

value_format_name

_lock_

string 

If specified, the name of the value format, as defined in the LookML model.

view

_lock_

string 

The name of the view this field belongs to.

view_label

_lock_

string 

The human-readable label of the view the field belongs to.

dynamic

_lock_

boolean 

Whether this field was specified in "dynamic_fields" and is not part of the model.

week_start_day

_lock_

string 

The name of the starting day of the week. Valid values are: "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday".

times_used

_lock_

integer 

The number of times this field has been used in queries

original_view

_lock_

string 

The name of the view this field is defined in. This will be different than "view" when the view has been joined via a different name using the "from" parameter.

datatype

_lock_

string 

The data_type for a date in lookml

convert_tz

_lock_

boolean 

Whether time zones should be converted for datetime fields

filters

[LookmlModelExploreField](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreField)[] 

Expand LookmlModelExploreField definition... 

align

_lock_

string 

The appropriate horizontal text alignment the values of this field should be displayed in. Valid values are: "left", "right".

available_custom_timeframes

string[] 

timeframe_labels

_lock_

object 

A map of timeframe keys to their localized labels.

can_filter

_lock_

boolean 

Whether it's possible to filter on this field.

category

_lock_

string 

Field category Valid values are: "parameter", "filter", "measure", "dimension".

default_filter_value

_lock_

string 

The default value that this field uses when filtering. Null if there is no default value.

description

_lock_

string 

Description

dimension_group

_lock_

string 

Dimension group if this field is part of a dimension group. If not, this will be null.

drill_fields

string[] 

enumerations

[LookmlModelExploreFieldEnumeration](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldEnumeration)[] 

Expand LookmlModelExploreFieldEnumeration definition... 

label

_lock_

string 

Label

value

_lock_

any 

Value

error

_lock_

string 

An error message indicating a problem with the definition of this field. If there are no errors, this will be null.

field_group_label

_lock_

string 

A label creating a grouping of fields. All fields with this label should be presented together when displayed in a UI.

field_group_variant

_lock_

string 

When presented in a field group via field_group_label, a shorter name of the field to be displayed in that context.

fill_style

_lock_

string 

The style of dimension fill that is possible for this field. Null if no dimension fill is possible. Valid values are: "enumeration", "range".

fiscal_month_offset

_lock_

integer 

An offset (in months) from the calendar start month to the fiscal start month defined in the LookML model this field belongs to.

has_allowed_values

_lock_

boolean 

Whether this field has a set of allowed_values specified in LookML.

has_drills_metadata

_lock_

boolean 

Whether this field has links or drill fields defined.

hidden

_lock_

boolean 

Whether this field should be hidden from the user interface.

is_filter

_lock_

boolean 

Whether this field is a filter.

is_fiscal

_lock_

boolean 

Whether this field represents a fiscal time value.

is_numeric

_lock_

boolean 

Whether this field is of a type that represents a numeric value.

is_timeframe

_lock_

boolean 

Whether this field is of a type that represents a time value.

can_time_filter

_lock_

boolean 

Whether this field can be time filtered.

time_interval

_lock_

[LookmlModelExploreFieldTimeInterval](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldTimeInterval)

Details on the time interval this field represents, if it is_timeframe.

Expand LookmlModelExploreFieldTimeInterval definition... 

name

_lock_

string 

The type of time interval this field represents a grouping of. Valid values are: "day", "hour", "minute", "second", "millisecond", "microsecond", "week", "month", "quarter", "year".

count

_lock_

integer 

The number of intervals this field represents a grouping of.

label

_lock_

string 

Fully-qualified human-readable label of the field.

label_from_parameter

_lock_

string 

The name of the parameter that will provide a parameterized label for this field, if available in the current context.

label_short

_lock_

string 

The human-readable label of the field, without the view label.

lookml_link

_lock_

string 

A URL linking to the definition of this field in the LookML IDE.

links

[LookmlFieldLink](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlFieldLink)[] 

Expand LookmlFieldLink definition... 

label

_lock_

string 

The name of the link as it would appear to users.

url

_lock_

string 

URL the link will go to.

icon_url

_lock_

string 

A URL containing an image file to display with a link.

map_layer

_lock_

[LookmlModelExploreFieldMapLayer](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldMapLayer)

If applicable, a map layer this field is associated with.

Expand LookmlModelExploreFieldMapLayer definition... 

url

_lock_

string 

URL to the map layer resource.

name

_lock_

string 

Name of the map layer, as defined in LookML.

feature_key

_lock_

string 

Specifies the name of the TopoJSON object that the map layer references. If not specified, use the first object..

property_key

_lock_

string 

Selects which property from the TopoJSON data to plot against. TopoJSON supports arbitrary metadata for each region. When null, the first matching property should be used.

property_label_key

_lock_

string 

Which property from the TopoJSON data to use to label the region. When null, property_key should be used.

projection

_lock_

string 

The preferred geographic projection of the map layer when displayed in a visualization that supports multiple geographic projections.

format

_lock_

string 

Specifies the data format of the region information. Valid values are: "topojson", "vector_tile_region".

extents_json_url

_lock_

string 

Specifies the URL to a JSON file that defines the geographic extents of each region available in the map layer. This data is used to automatically center the map on the available data for visualization purposes. The JSON file must be a JSON object where the keys are the mapping value of the feature (as specified by property_key) and the values are arrays of four numbers representing the west longitude, south latitude, east longitude, and north latitude extents of the region. The object must include a key for every possible value of property_key.

max_zoom_level

_lock_

integer 

The minimum zoom level that the map layer may be displayed at, for visualizations that support zooming.

min_zoom_level

_lock_

integer 

The maximum zoom level that the map layer may be displayed at, for visualizations that support zooming.

measure

_lock_

boolean 

Whether this field is a measure.

name

_lock_

string 

Fully-qualified name of the field.

strict_value_format

_lock_

boolean 

If yes, the field will not be localized with the user attribute number_format. Defaults to no

parameter

_lock_

boolean 

Whether this field is a parameter.

period_over_period_params

_lock_

[LookmlModelExploreFieldPeriodOverPeriodParams](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldPeriodOverPeriodParams)

For measures of type period_over_period, this will return the individual metadata parameters.

Expand LookmlModelExploreFieldPeriodOverPeriodParams definition... 

based_on

_lock_

string 

Specifies the measure that will be calculated over the different periods.

based_on_time

_lock_

string 

Specifies the time dimension that this measure will operate over.

period

_lock_

string 

Specifies the time frame for the comparison. Valid values are: "year", "fiscal_year", "quarter", "fiscal_quarter", "month", "week", "date".

kind

_lock_

string 

The type of calculation for the period_over_period measure. Valid values are: "previous", "difference", "relative_change".

value_to_date

_lock_

boolean 

specifies whether to compare the current partially completed period to an equivalent part of the previous period, or to use the entire previous period.

permanent

_lock_

boolean 

Whether this field can be removed from a query.

primary_key

_lock_

boolean 

Whether or not the field represents a primary key.

project_name

_lock_

string 

The name of the project this field is defined in.

requires_refresh_on_sort

_lock_

boolean 

When true, it's not possible to re-sort this field's values without re-running the SQL query, due to database logic that affects the sort.

scope

_lock_

string 

The LookML scope this field belongs to. The scope is typically the field's view.

sortable

_lock_

boolean 

Whether this field can be sorted.

source_file

_lock_

string 

The path portion of source_file_path.

source_file_path

_lock_

string 

The fully-qualified path of the project file this field is defined in.

sql

_lock_

string 

SQL expression as defined in the LookML model. The SQL syntax shown here is a representation intended for auditability, and is not neccessarily an exact match for what will ultimately be run in the database. It may contain special LookML syntax or annotations that are not valid SQL. This will be null if the current user does not have the see_lookml permission for the field's model.

sql_case

[LookmlModelExploreFieldSqlCase](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldSqlCase)[] 

Expand LookmlModelExploreFieldSqlCase definition... 

value

_lock_

string 

SQL Case label value

condition

_lock_

string 

SQL Case condition expression

filters

[LookmlModelExploreFieldMeasureFilters](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldMeasureFilters)[] 

Expand LookmlModelExploreFieldMeasureFilters definition... 

field

_lock_

string 

Filter field name

condition

_lock_

string 

Filter condition value

suggest_dimension

_lock_

string 

The name of the dimension to base suggest queries from.

suggest_explore

_lock_

string 

The name of the explore to base suggest queries from.

suggestable

_lock_

boolean 

Whether or not suggestions are possible for this field.

suggestions

string[] 

synonyms

string[] 

tags

string[] 

type

_lock_

string 

The LookML type of the field.

user_attribute_filter_types

string[] 

value_format

_lock_

string 

If specified, the LookML value format string for formatting values of this field.

value_format_name

_lock_

string 

If specified, the name of the value format, as defined in the LookML model.

view

_lock_

string 

The name of the view this field belongs to.

view_label

_lock_

string 

The human-readable label of the view the field belongs to.

dynamic

_lock_

boolean 

Whether this field was specified in "dynamic_fields" and is not part of the model.

week_start_day

_lock_

string 

The name of the starting day of the week. Valid values are: "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday".

times_used

_lock_

integer 

The number of times this field has been used in queries

original_view

_lock_

string 

The name of the view this field is defined in. This will be different than "view" when the view has been joined via a different name using the "from" parameter.

datatype

_lock_

string 

The data_type for a date in lookml

convert_tz

_lock_

boolean 

Whether time zones should be converted for datetime fields

parameters

[LookmlModelExploreField](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreField)[] 

Expand LookmlModelExploreField definition... 

align

_lock_

string 

The appropriate horizontal text alignment the values of this field should be displayed in. Valid values are: "left", "right".

available_custom_timeframes

string[] 

timeframe_labels

_lock_

object 

A map of timeframe keys to their localized labels.

can_filter

_lock_

boolean 

Whether it's possible to filter on this field.

category

_lock_

string 

Field category Valid values are: "parameter", "filter", "measure", "dimension".

default_filter_value

_lock_

string 

The default value that this field uses when filtering. Null if there is no default value.

description

_lock_

string 

Description

dimension_group

_lock_

string 

Dimension group if this field is part of a dimension group. If not, this will be null.

drill_fields

string[] 

enumerations

[LookmlModelExploreFieldEnumeration](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldEnumeration)[] 

Expand LookmlModelExploreFieldEnumeration definition... 

label

_lock_

string 

Label

value

_lock_

any 

Value

error

_lock_

string 

An error message indicating a problem with the definition of this field. If there are no errors, this will be null.

field_group_label

_lock_

string 

A label creating a grouping of fields. All fields with this label should be presented together when displayed in a UI.

field_group_variant

_lock_

string 

When presented in a field group via field_group_label, a shorter name of the field to be displayed in that context.

fill_style

_lock_

string 

The style of dimension fill that is possible for this field. Null if no dimension fill is possible. Valid values are: "enumeration", "range".

fiscal_month_offset

_lock_

integer 

An offset (in months) from the calendar start month to the fiscal start month defined in the LookML model this field belongs to.

has_allowed_values

_lock_

boolean 

Whether this field has a set of allowed_values specified in LookML.

has_drills_metadata

_lock_

boolean 

Whether this field has links or drill fields defined.

hidden

_lock_

boolean 

Whether this field should be hidden from the user interface.

is_filter

_lock_

boolean 

Whether this field is a filter.

is_fiscal

_lock_

boolean 

Whether this field represents a fiscal time value.

is_numeric

_lock_

boolean 

Whether this field is of a type that represents a numeric value.

is_timeframe

_lock_

boolean 

Whether this field is of a type that represents a time value.

can_time_filter

_lock_

boolean 

Whether this field can be time filtered.

time_interval

_lock_

[LookmlModelExploreFieldTimeInterval](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldTimeInterval)

Details on the time interval this field represents, if it is_timeframe.

Expand LookmlModelExploreFieldTimeInterval definition... 

name

_lock_

string 

The type of time interval this field represents a grouping of. Valid values are: "day", "hour", "minute", "second", "millisecond", "microsecond", "week", "month", "quarter", "year".

count

_lock_

integer 

The number of intervals this field represents a grouping of.

label

_lock_

string 

Fully-qualified human-readable label of the field.

label_from_parameter

_lock_

string 

The name of the parameter that will provide a parameterized label for this field, if available in the current context.

label_short

_lock_

string 

The human-readable label of the field, without the view label.

lookml_link

_lock_

string 

A URL linking to the definition of this field in the LookML IDE.

links

[LookmlFieldLink](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlFieldLink)[] 

Expand LookmlFieldLink definition... 

label

_lock_

string 

The name of the link as it would appear to users.

url

_lock_

string 

URL the link will go to.

icon_url

_lock_

string 

A URL containing an image file to display with a link.

map_layer

_lock_

[LookmlModelExploreFieldMapLayer](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldMapLayer)

If applicable, a map layer this field is associated with.

Expand LookmlModelExploreFieldMapLayer definition... 

url

_lock_

string 

URL to the map layer resource.

name

_lock_

string 

Name of the map layer, as defined in LookML.

feature_key

_lock_

string 

Specifies the name of the TopoJSON object that the map layer references. If not specified, use the first object..

property_key

_lock_

string 

Selects which property from the TopoJSON data to plot against. TopoJSON supports arbitrary metadata for each region. When null, the first matching property should be used.

property_label_key

_lock_

string 

Which property from the TopoJSON data to use to label the region. When null, property_key should be used.

projection

_lock_

string 

The preferred geographic projection of the map layer when displayed in a visualization that supports multiple geographic projections.

format

_lock_

string 

Specifies the data format of the region information. Valid values are: "topojson", "vector_tile_region".

extents_json_url

_lock_

string 

Specifies the URL to a JSON file that defines the geographic extents of each region available in the map layer. This data is used to automatically center the map on the available data for visualization purposes. The JSON file must be a JSON object where the keys are the mapping value of the feature (as specified by property_key) and the values are arrays of four numbers representing the west longitude, south latitude, east longitude, and north latitude extents of the region. The object must include a key for every possible value of property_key.

max_zoom_level

_lock_

integer 

The minimum zoom level that the map layer may be displayed at, for visualizations that support zooming.

min_zoom_level

_lock_

integer 

The maximum zoom level that the map layer may be displayed at, for visualizations that support zooming.

measure

_lock_

boolean 

Whether this field is a measure.

name

_lock_

string 

Fully-qualified name of the field.

strict_value_format

_lock_

boolean 

If yes, the field will not be localized with the user attribute number_format. Defaults to no

parameter

_lock_

boolean 

Whether this field is a parameter.

period_over_period_params

_lock_

[LookmlModelExploreFieldPeriodOverPeriodParams](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldPeriodOverPeriodParams)

For measures of type period_over_period, this will return the individual metadata parameters.

Expand LookmlModelExploreFieldPeriodOverPeriodParams definition... 

based_on

_lock_

string 

Specifies the measure that will be calculated over the different periods.

based_on_time

_lock_

string 

Specifies the time dimension that this measure will operate over.

period

_lock_

string 

Specifies the time frame for the comparison. Valid values are: "year", "fiscal_year", "quarter", "fiscal_quarter", "month", "week", "date".

kind

_lock_

string 

The type of calculation for the period_over_period measure. Valid values are: "previous", "difference", "relative_change".

value_to_date

_lock_

boolean 

specifies whether to compare the current partially completed period to an equivalent part of the previous period, or to use the entire previous period.

permanent

_lock_

boolean 

Whether this field can be removed from a query.

primary_key

_lock_

boolean 

Whether or not the field represents a primary key.

project_name

_lock_

string 

The name of the project this field is defined in.

requires_refresh_on_sort

_lock_

boolean 

When true, it's not possible to re-sort this field's values without re-running the SQL query, due to database logic that affects the sort.

scope

_lock_

string 

The LookML scope this field belongs to. The scope is typically the field's view.

sortable

_lock_

boolean 

Whether this field can be sorted.

source_file

_lock_

string 

The path portion of source_file_path.

source_file_path

_lock_

string 

The fully-qualified path of the project file this field is defined in.

sql

_lock_

string 

SQL expression as defined in the LookML model. The SQL syntax shown here is a representation intended for auditability, and is not neccessarily an exact match for what will ultimately be run in the database. It may contain special LookML syntax or annotations that are not valid SQL. This will be null if the current user does not have the see_lookml permission for the field's model.

sql_case

[LookmlModelExploreFieldSqlCase](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldSqlCase)[] 

Expand LookmlModelExploreFieldSqlCase definition... 

value

_lock_

string 

SQL Case label value

condition

_lock_

string 

SQL Case condition expression

filters

[LookmlModelExploreFieldMeasureFilters](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreFieldMeasureFilters)[] 

Expand LookmlModelExploreFieldMeasureFilters definition... 

field

_lock_

string 

Filter field name

condition

_lock_

string 

Filter condition value

suggest_dimension

_lock_

string 

The name of the dimension to base suggest queries from.

suggest_explore

_lock_

string 

The name of the explore to base suggest queries from.

suggestable

_lock_

boolean 

Whether or not suggestions are possible for this field.

suggestions

string[] 

synonyms

string[] 

tags

string[] 

type

_lock_

string 

The LookML type of the field.

user_attribute_filter_types

string[] 

value_format

_lock_

string 

If specified, the LookML value format string for formatting values of this field.

value_format_name

_lock_

string 

If specified, the name of the value format, as defined in the LookML model.

view

_lock_

string 

The name of the view this field belongs to.

view_label

_lock_

string 

The human-readable label of the view the field belongs to.

dynamic

_lock_

boolean 

Whether this field was specified in "dynamic_fields" and is not part of the model.

week_start_day

_lock_

string 

The name of the starting day of the week. Valid values are: "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday".

times_used

_lock_

integer 

The number of times this field has been used in queries

original_view

_lock_

string 

The name of the view this field is defined in. This will be different than "view" when the view has been joined via a different name using the "from" parameter.

datatype

_lock_

string 

The data_type for a date in lookml

convert_tz

_lock_

boolean 

Whether time zones should be converted for datetime fields

## Related Types

  * [LookmlModelExplore](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExplore "LookmlModelExplore")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
