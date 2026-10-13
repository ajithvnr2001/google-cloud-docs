---
url: https://docs.cloud.google.com/looker/docs/reference/param-field/
title: Field parameters \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:32.465604+00:00
---

# Field parameters  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  Field parameters Stay organized with collections  Save and categorize content based on your preferences. 

This page links to all of the LookML parameters that define fields.

There are several types of fields:

  * **Dimensions** represent a column in a table, or a computed value based on some sort of column manipulation or combination
  * **Dimension Groups** are only used with time-based data, and enable you to create many time-based dimensions at one time
  * **Measures** are similar to aggregate functions in SQL (for example, `COUNT`, `SUM`, `AVG`) and represent information about multiple rows
  * **Filters** create a filter-only field users can use to provide input to a [templated filter](https://docs.cloud.google.com/looker/docs/templated-filters) or a [conditional join](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-on#conditional_joins)
  * **Parameters** create a filter-only field users can use to provide input to a [Liquid `{% parameter %}` tag](https://docs.cloud.google.com/looker/docs/liquid-variable-reference)



## Example usage

Hold the pointer over a parameter name to see a quick description. Click a parameter name to jump to its reference page.

When a parameter can be set to one of several specific options, the default value is listed first.
    
    
    ## STRUCTURAL PARAMETERS
    [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view "Creates a view"): view_name {
      ([dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension "Creates a dimension field") |[dimension_group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group "Creates several time-based dimensions at the same time") |[measure](https://docs.cloud.google.com/looker/docs/reference/param-field-measure "Creates a measure field") |[filter](https://docs.cloud.google.com/looker/docs/reference/param-field-filter "Creates a filter-only field for use in a templated filter or conditional join") | [parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter "Creates a filter-only field for use in a Liquid parameter tag")):field_name{
        [intervals](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#intervals "Defines the set of duration dimensions you want a duration type dimension_group to produce"): [interval, interval, …]
        [timeframes](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes "Defines the set of timeframe dimensions you want a time type dimension_group to produce"): [timeframe, timeframe, …]
    
        # ACTION AND LINKING PARAMETERS
        [action](https://docs.cloud.google.com/looker/docs/reference/param-field-action "Creates a data action on a field that lets users perform tasks in other tools, directly from Looker"): {
          [label](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"): "Label to Appear in Action Menu"
          [url](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"): "url"
          [icon_url](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"): "url"
          [form_url](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"): "url"
          [param](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"): {
            [name](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"):  "name string"
            [value](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"):  "value string"
          }
          # Possibly more param definitions
          [form_param](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"): {
            [name](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"):  "title"
            [type](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"): select | string | textarea
            [label](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"):  "desired label name"
            [required](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"):  yes | no
            [default](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"):  "value string"
            [option](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"): {
              [name](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"):  "name string"
              [value](https://docs.cloud.google.com/looker/docs/reference/param-field-action "See action page for more detail"):  "value string"
            }
            # Possibly more option definitions
          }
          # Possibly more form_param definitions
        }
        [drill_fields](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields "Declares the list of fields that will be displayed when the measure or dimension is drilled into"): [field_or_set, field_or_set, ...]
        [tags](https://docs.cloud.google.com/looker/docs/reference/param-field-tags "Specifies text that can be passed to other applications"): ["string1", "string2", ...]
        [link](https://docs.cloud.google.com/looker/docs/reference/param-field-link "Specifies a valid URL to redirect upon clicking, possibly inserting the dimension value into the URL"): {
          [label](https://docs.cloud.google.com/looker/docs/reference/param-field-link "See link page for more detail"): "desired label name;"
          [url](https://docs.cloud.google.com/looker/docs/reference/param-field-link "See link page for more detail"): "desired_url"
          [icon_url](https://docs.cloud.google.com/looker/docs/reference/param-field-link "See link page for more detail"): "url_of_an_image_file"
        }
        # Possibly more link definitions
        # DISPLAY PARAMETERS
        [alias](https://docs.cloud.google.com/looker/docs/reference/param-field-alias "Allows saved URLs with old field names to remain functional after a field is renamed"): [old_field_name, old_field_name, ...]
        [alpha_sort](https://docs.cloud.google.com/looker/docs/reference/param-field-case#alpha_sort "Makes a case parameter sort its conditions alphabetically"): yes | no
        [description](https://docs.cloud.google.com/looker/docs/reference/param-field-description "Adds a description that users can see when holding the pointer over a field in the field picker"): "description string"
        [group_label](https://docs.cloud.google.com/looker/docs/reference/param-field-group-label "Groups fields together within a view in the field picker"):  "desired group label name"
        [group_item_label](https://docs.cloud.google.com/looker/docs/reference/param-field-group-item-label "Specifies a label to use for the field under its group label in the field picker"):  "label to use under the group label in the field picker"
        [hidden](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden "Hides a field from the Explore UI"): yes | no
        [label](https://docs.cloud.google.com/looker/docs/reference/param-field-label "Changes the way the field name appears in the field picker"): "desired label name"
        [label_from_parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-label-from-parameter "Changes the way a field name appears in a visualization based on the input to a parameter field"): parameter_name
        [order_by_field](https://docs.cloud.google.com/looker/docs/reference/param-field-order-by-field "Sorts a dimension or dimension group by the values of another dimension"): dimension_name | dimension_group_name | measure_name 
        [style](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#style "Changes the way that tiers appear in the Looker UI for a dimension of type: tier"): classic | interval | integer | relational
        [view_label](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label "Changes the way a view name appears, or the fields that appear within a view, in the field picker"): "desired label name"
    
        # FILTER PARAMETERS
        [can_filter](https://docs.cloud.google.com/looker/docs/reference/param-field-can-filter "Specifies whether a dimension or measure can be used as a filter"): yes | no
        [case_sensitive](https://docs.cloud.google.com/looker/docs/reference/param-field-case-sensitive "Specifies whether filters are case-sensitive for a dimension"): yes | no
        [filters](https://docs.cloud.google.com/looker/docs/reference/param-field-filters "Restricts a measure's calculation based on dimension limitations"): [dimension: "filter expression", dimension: "filter expression", ...]
        [skip_drill_filter](https://docs.cloud.google.com/looker/docs/reference/param-field-skip-drill-filter "Stops a dimension from being added to the filters when a measure is drilled into"): yes | no
    
        # FILTER SUGGESTION PARAMETERS
        [allowed_value](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#specifying_allowed_values "Specifies the choices for a parameter field"): {
          [label](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#specifying_allowed_values "See allowed_value for more detail"): "desired label name"
          [value](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#specifying_allowed_values "See allowed_value for more detail"): "looker filter expression"
        }
        # Possibly more allowed_value definitions
        [bypass_suggest_restrictions](https://docs.cloud.google.com/looker/docs/reference/param-field-bypass-suggest-restrictions "Shows suggestions to users when sql_always_where or access_filter_fields is in use, but don't apply those limits to the suggestions"): yes | no
        [full_suggestions](https://docs.cloud.google.com/looker/docs/reference/param-field-full-suggestions "Controls how Looker queries your database to provide suggestions for a field's values in the filter of an Explore."): yes | no
        [suggest_dimension](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-dimension "Bases the suggestions for a dimension on the values of a different dimension"): dimension_name
        [suggest_explore](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-explore "Bases the suggestions for a dimension on the values of a different explore"): explore_name
        [suggest_persist_for](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-persist-for "Changes the cache settings for Looker filter suggestions"): "N (seconds | minutes | hours)"
        [suggestable](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestable "Enables or disables suggestions for a dimension"): yes | no
        [suggestions](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions "Declares a list of values that will be used for a dimension's suggestions"): ["suggestion string", "suggestion string", "…"]<
    
        # QUERY PARAMETERS
        [allow_approximate_optimization](https://docs.cloud.google.com/looker/docs/reference/param-field-allow-approximate-optimization "Allows distinct count approximations for aggregate tables"): yes | no
        [approximate](https://docs.cloud.google.com/looker/docs/reference/param-field-approximate "Performs an approximate count for type: count_distinct measures"): yes | no
        [approximate_threshold](https://docs.cloud.google.com/looker/docs/reference/param-field-approximate-threshold "Sets the count at which BigQuery switches from an exact count distinct to an approximate count distinct"): N
        [convert_tz](https://docs.cloud.google.com/looker/docs/reference/param-field-convert-tz "Disables automatic time zone conversion for a field"): yes | no
        [datatype](https://docs.cloud.google.com/looker/docs/reference/param-field-datatype "Specifies the type of time data you are providing to a dimension_group"): epoch | timestamp | datetime | date | yyyymmdd
        [fanout_on](https://docs.cloud.google.com/looker/docs/reference/param-field-fanout-on "Enables access to Google BigQuery repeated fields"): repeated_record_name
        [precision](https://docs.cloud.google.com/looker/docs/reference/param-field-precision "Specifies the number of decimal places to use when making calculations for Looker symmetric aggregates"): N
        [primary_key](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key "Declares a dimension as the primary key of a view"): yes | no
        [required_access_grants](https://docs.cloud.google.com/looker/docs/reference/param-field-required-access-grants "Specifies which access grants are required for a user to access this field"): [access_grant_name, access_grant_name, ...]
        [required_fields](https://docs.cloud.google.com/looker/docs/reference/param-field-required-fields "Requires that additional fields are added to a query when a field is chosen"): [field_name, field_name, ...]
        [sql_distinct_key](https://docs.cloud.google.com/looker/docs/reference/param-field-sql-distinct-key "Defines the unique entities over which a distinct measure, such as type: sum_distinct or  type: average_distinct, will be calculated"): SQL expression to define repeated entities ;;
    
        # VALUE AND FORMATTING PARAMETERS
        [case](https://docs.cloud.google.com/looker/docs/reference/param-field-case "Creates a discrete set of values a dimension can have, determined by SQL conditions"): {
          [when](https://docs.cloud.google.com/looker/docs/reference/param-field-case "See case page for more detail"): {
            [sql](https://docs.cloud.google.com/looker/docs/reference/param-field-case "See case page for more detail"): SQL condition ;;
            [label](https://docs.cloud.google.com/looker/docs/reference/param-field-case "See case page for more detail"): "value"
          }
          # Possibly more when statements
        }
        [default_value](https://docs.cloud.google.com/looker/docs/reference/param-field-default-value "Specifies a default value for a filter field"): "desired default value"
        [direction](https://docs.cloud.google.com/looker/docs/reference/param-field-direction "Determines the direction that a measure of type: percent_of_total or type: running_total is calculated when pivots are used"): "row | column"
        [end_location_field](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance "Defines the field that contains the end location for a field of type: distance"): dimension_name
        [html](https://docs.cloud.google.com/looker/docs/reference/param-field-html "Modifies the HTML output of a field using liquid templating"): HTML expression using Liquid template elements ;;
        [list_field](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list "Declares the dimension from which a  type: list measure will be calculated"): dimension_name
    
        [percentile](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile "Specifies fractional value for a measure of type: percentile or type: percentile_distinct"): Nth percentile
        [sql](https://docs.cloud.google.com/looker/docs/reference/param-field-sql "Determines how the field will be calculated"): SQL expression to generate the field value ;;
        [sql_end](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration "Defines the end time for a duration type dimension or dimension group"): SQL expression indicating the end time of a duration ;;
        [sql_latitude](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location "Defines the latitude of a dimension of type: location"): SQL expression to generate a latitude ;;
        [sql_longitude](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location "Defines the longitude of a dimension of type: location"): SQL expression to generate a longitude ;;
        [sql_start](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration "Defines the start time for a duration type dimension or dimension group"): SQL expression indicating the start time of a duration ;;
        [start_location_field](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance "Defines the field that contains the start location for a field of type: distance"): dimension_name
        [synonyms](https://docs.cloud.google.com/looker/docs/reference/param-field-synonyms "Specifies a list of string synonyms \(words or phrases\) that can be used to help large language models and app developers understand other ways that users may refer to a field"): [synonym1, synonym2, ...]
        [tiers](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier "Defines the tiers for a dimension of type: tier"): [N, N, ...]
        [type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types "Specifies the type of dimension"): dimension_field_type # For a dimension field
        [type](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group "Specifies the type of dimension_group"): dimension_group_type # For a dimension_group field
        [type](https://docs.cloud.google.com/looker/docs/reference/param-measure-types "Specifies the type of measure"): measure_field_type   # For a measure field
        [type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types "Specifies the type of filter"): filter_field_type    # For a filter field
        [type](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types "Specifies the type of parameter"): parameter_field_type # For a parameter field
        [string_datatype](https://docs.cloud.google.com/looker/docs/reference/param-field-string-datatype "Specifies the unicode datatype for a string field for SQL Server or MySQL"): unicode # For a dimension field
        [units](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance "Specifies the units to use for a field of type: distance"): feet | kilometers | meters | miles | nautical_miles | yards
        [value_format](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format "Formats the output of a field using Excel style options"): "excel-style formatting string"
        [value_format_name](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name "Formats the output of a field using a built-in or custom format"): format_name
    
        # VISUALIZATION PARAMETERS
        [allow_fill](https://docs.cloud.google.com/looker/docs/reference/param-field-allow-fill "Specifies whether dimension filling is allowed for a dimension"): yes | no
        [map_layer_name](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name "Specifies a mapping from a data value to a geographic region that you've defined on a built-in or custom map"): name_of_map_layer
      }
    }
    

## Parameter definitions

  * D = Dimension
  * DG = Dimension Group
  * M = Measure
  * F = Filter
  * P = Parameter

Parameter Name | Valid Field Types | Description  
---|---|---  
Structural Parameters  
[`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) | D | Creates a dimension field  
[`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) | DG | Creates several time-based dimensions at the same time  
[`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) | F | Creates a filter-only field for use in a templated filter or conditional join  
[`measure`](https://docs.cloud.google.com/looker/docs/reference/param-field-measure) | M | Creates a measure field  
[`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) | P | Creates a filter-only field users can use to provide input to a Liquid `{% parameter %}` tag  
[`intervals`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#intervals) | DG |  Defines the set of duration dimensions you want in a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) of [`type: duration`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#duration_type)  
[`timeframes`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframes) | DG | Defines the set of timeframe dimensions you want in a [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) of [`type: time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#time_type)  
Action and Linking Parameters  
[`action`](https://docs.cloud.google.com/looker/docs/reference/param-field-action) | D M | Creates a data action on a field that lets users perform tasks in other tools, directly from Looker  
[`drill_fields`](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) | D DG M | Declares the list of fields that will be displayed when the measure or dimension is drilled into  
[`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link) | D M | Creates links to other Looker and external content  
[`tags`](https://docs.cloud.google.com/looker/docs/reference/param-field-tags) | D DG M F P | Adds text that can be passed to other applications to provide data about a field  
Display Parameters  
[`alias`](https://docs.cloud.google.com/looker/docs/reference/param-field-alias) | D DG M F P | Allows saved URLs with old field names to remain functional after a field is renamed  
[`alpha_sort`](https://docs.cloud.google.com/looker/docs/reference/param-field-case#alpha_sort) | D | Makes a [`case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) parameter sort its conditions alphabetically   
[`description`](https://docs.cloud.google.com/looker/docs/reference/param-field-description) | D DG M F P | Adds a description to the field users can see when hovering the cursor over the field.  
[`group_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-group-label) | D DG M F | Groups fields together within a view in the field picker  
[`group_item_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-group-item-label) | D DG M F |  Specifies a label to use for the field under its group label in the field picker  
[`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) | D DG M F P | Hides a field from the Explore UI  
[`label`](https://docs.cloud.google.com/looker/docs/reference/param-field-label) | D DG M F P | Changes the way a field name appears in the field picker  
[`label_from_parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-label-from-parameter) | D M | Changes the way a field name appears in a visualization based on the input to a [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter)  
[`order_by_field`](https://docs.cloud.google.com/looker/docs/reference/param-field-order-by-field) | D DG M | Sorts a field by the values of another field Supported for dimensions, dimension groups  Supported for measures   
[`style`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#style) | D | Changes the way that tiers appear in the Looker UI for a dimension of [`type: tier`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier)  
[`view_label`](https://docs.cloud.google.com/looker/docs/reference/param-field-view-label) | D DG M F P | Changes the fields that appear within a view in the field picker  
Filter Parameters  
[`can_filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-can-filter) | D DG M | Determines if a dimension or measure can be used as a filter  
[`case_sensitive`](https://docs.cloud.google.com/looker/docs/reference/param-field-case-sensitive) | D F | Determines if filters are case-sensitive for a dimension  
[`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) | F | Creates a filter-only field for use in a templated filter  
[`filters`](https://docs.cloud.google.com/looker/docs/reference/param-field-filters) | M | Restricts a measure's calculation based on dimension limitations  
[`skip_drill_filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-skip-drill-filter) | D | Stops a dimension from being added to the filters when a measure is drilled into  
Filter Suggestion Parameters  
[`allowed_value`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#specifying_allowed_values) | P | Specifies the choices for a [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter)  
[`bypass_suggest_restrictions`](https://docs.cloud.google.com/looker/docs/reference/param-field-bypass-suggest-restrictions) | D DG F P | Shows suggestions to users when [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where) is in use, but don't apply those limits to the suggestions  
[`full_suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-full-suggestions) | D DG F P | Controls how Looker queries your database to provide suggestions for a field's values in the filter of an Explore. Looker can use a basic `SELECT DISTINCT` query, or Looker can use the full logic of the Explore, including joins and `sql_always_where` and `access_filter` parameters.  
[`suggest_dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-dimension) | D DG M F P | Bases the suggestions for a field on the values of a different dimension  
[`suggest_explore`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-explore) | D DG M F P | Bases the suggestions for a field on the values of a different Explore  
[`suggest_persist_for`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-persist-for) | D F P | Changes the cache settings for Looker filter suggestions  
[`suggestable`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestable) | D DG M F P | Enables or disables suggestions for a field  
[`suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions) | D F P | Declares a list of values that will be used for a field's suggestions  
Query Parameters  
[`allow_approximate_optimization`](https://docs.cloud.google.com/looker/docs/reference/param-field-allow-approximate-optimization) | M | Allows distinct count approximations for measures of [`type: count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count) or [`type: count_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count_distinct), so that the measure can be used for [aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness)  
[`approximate`](https://docs.cloud.google.com/looker/docs/reference/param-field-approximate) | M | Performs an approximate count for a measure of [`type: count_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count_distinct). See the [`approximate`](https://docs.cloud.google.com/looker/docs/reference/param-field-approximate#dialect_support_for_approximate) documentation page for a list of dialects that support this parameter.  
[`approximate_threshold`](https://docs.cloud.google.com/looker/docs/reference/param-field-approximate-threshold) | M | Sets the count at which BigQuery switches from an exact count distinct to an approximate count distinct  
[`convert_tz`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#convert_tz) | D DG M F P | Disables automatic time zone conversion for a field  
[`datatype`](https://docs.cloud.google.com/looker/docs/reference/param-field-datatype) | D DG F M | Specifies the type of time data you are providing to a field  
[`fanout_on`](https://docs.cloud.google.com/looker/docs/reference/param-field-fanout-on) | D DG M | Enables access to Google BigQuery repeated fields  
[`precision`](https://docs.cloud.google.com/looker/docs/reference/param-field-precision) | M | Specifies the number of decimal places to use when making calculations for Looker symmetric aggregates  
[`primary_key`](https://docs.cloud.google.com/looker/docs/reference/param-field-primary-key) | D | Declares a dimension as the primary key of a view  
[`required_access_grants`](https://docs.cloud.google.com/looker/docs/reference/param-field-required-access-grants) | D DG F M P |  Limits access to the field to only users whose user attribute values match the access grants  
[`required_fields`](https://docs.cloud.google.com/looker/docs/reference/param-field-required-fields) | D M | Requires that additional fields are added to a query when a field is chosen |  [`sql_distinct_key`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql-distinct-key) | M | Defines the unique entities over which a measure of [`type: sum_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum_distinct) or [`type: average_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average_distinct_or_avg_distinct) will be calculated  
Value and Formatting Parameters  
[`case`](https://docs.cloud.google.com/looker/docs/reference/param-field-case) | D | Creates a discrete set of values a dimension can have determined by SQL conditions  
[`default_value`](https://docs.cloud.google.com/looker/docs/reference/param-field-default-value) | F P | Specifies a default value for [filter fields](https://docs.cloud.google.com/looker/docs/reference/param-field-filter)  
[`direction`](https://docs.cloud.google.com/looker/docs/reference/param-field-direction) | M | Determines the direction that a measure of [`type: percent_of_total`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percent_of_total) or [`type: running_total`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#running_total) is calculated when pivots are used  
[`end_location_field`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance) | D | Defines the field that contains the end location for a field of [`type: distance`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance)  
[`html`](https://docs.cloud.google.com/looker/docs/reference/param-field-html) | D DG M | Modifies the HTML output of a field using Liquid templating  
[`list_field`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list) | M | Declares the dimension from which a measure of [`type: list`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list) will be calculated  
[`percentile`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile) | M | Specifies the fractional value (the Nth percentile) for a measure of [`type: percentile`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile) or [`type: percentile_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile_distinct)  
[`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) | D DG M F | Determines how a field will be calculated  
[`sql_end`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration) | D DG |  Defines the end time of a duration for a [duration type dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration) or a [duration type dimension](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#individual_duration_types)  
[`sql_latitude`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location) | D | Defines the latitude of a dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location)  
[`sql_longitude`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location) | D | Defines the longitude of a dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location)  
[`sql_start`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration) | D DG |  Defines the begin time of a duration for a [duration type dimension group](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration) or a [duration type dimension](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#individual_duration_types)  
[`start_location_field`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance) | D | Defines the field that contains the start location for a field of [`type: distance`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance)  
[`synonyms`](https://docs.cloud.google.com/looker/docs/reference/param-field-synonyms) | D DG F M P | Specifies a list of string synonyms (words or phrases) that can be used to help large language models and app developers understand other ways that users may refer to a field  
[`tiers`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier) | D | Defines the tiers for a dimension of [`type: tier`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#tier)  
[`type` (for dimension, filter, or parameter)](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) | D F P | Specifies the type of dimension, filter, or parameter  
[`type` (for dimension group)](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#types) | DG | Specifies the type of dimension group  
[`type` (for measure)](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) | M | Specifies the type of measure  
[`string_datatype`](https://docs.cloud.google.com/looker/docs/reference/param-field-string-datatype) | D | Specifies the unicode data type for a field of [`type: string`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#string) for SQL Server or MySQL  
[`units`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance) | D | Specifies the units to use for a field of [`type: distance`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#distance)  
[`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) | D M | Formats the output of a field using Excel style options  
[`value_format_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name) | D M | Formats the output of a field using a built-in or custom format  
Visualization Parameters  
[`allow_fill`](https://docs.cloud.google.com/looker/docs/reference/param-field-allow-fill) | D DG | Determines if dimension filling is allowed for a dimension  
[`map_layer_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) | D | Specifies a mapping from a data value to a geographic region that you've defined on a built-in or custom map  
Parameters to Avoid  
[`decimals`](https://docs.cloud.google.com/looker/docs/reference/param-field-decimals) | D M |  Removed 5.4  Replaced by [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format)  
[`format`](https://docs.cloud.google.com/looker/docs/reference/param-field-format) | D M |  Removed 3.16  Replaced by [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
