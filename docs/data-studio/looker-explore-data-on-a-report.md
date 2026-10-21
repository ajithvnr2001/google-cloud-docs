---
url: https://docs.cloud.google.com/data-studio/looker-explore-data-on-a-report/
title: Understand Looker Explore data on a Data Studio report \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:19.979956+00:00
---

# Understand Looker Explore data on a Data Studio report  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/looker-explore-data-on-a-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Understand Looker Explore data on a Data Studio report Stay organized with collections  Save and categorize content based on your preferences. 

After Looker has been [established as a data source](https://docs.cloud.google.com/data-studio/connect-to-looker) for your report, you can add fields, charts, and filters that are based on data from a Looker Explore to your report.

Because they are defined by [LookML](https://docs.cloud.google.com/looker/docs/what-is-lookml) parameters, the fields and filters for a Looker data source may appear or behave differently than the fields and filters for other data sources in Data Studio or from how they appear in Looker. This page describes these nuances and how to interact with fields and filters from a Looker data source.

Learn more about how to [add data to a report](https://docs.cloud.google.com/data-studio/add-data-to-a-report) and how to [edit fields in your reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports).

## How Looker Explores appear in Data Studio reports

Looker data sources help you analyze Looker Explore data in a Data Studio report.

Explore data, including its [views](https://docs.cloud.google.com/looker/docs/reference/param-view-view), [dimensions](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension), [dimension groups](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group), [measures](https://docs.cloud.google.com/looker/docs/reference/param-field-measure) (known as _metrics_ in Data Studio), and [joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) are surfaced in various parts of the Data Studio report user interface, including the following areas:

  * Data source editor
  * Report editor: 
    * Data panel's list of fields
    * Properties panel: dimension section, metric section, blend section, filter section
    * Report canvas visualizations and tooltips
    * Report filters



Both the Looker Explore field picker and the Data Studio report field picker organize fields alphanumerically by type (dimensions, followed by measures or metrics) under the name or [label](https://docs.cloud.google.com/looker/docs/reference/param-explore-view-label) of the Explore. Both also further group fields by the [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view).

Hover over a field or view to see its metadata, which is defined in the Looker Explore's underlying LookML. Data Studio surfaces the following field or view metadata:

  * View name: the field's view name, as defined by its [view](https://docs.cloud.google.com/looker/docs/reference/param-view-view) LookML parameter
  * Dimension group: if applicable, the name of the group of time-based or duration-based dimensions, as defined by its [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) LookML parameter
  * Description: the field or view description, as defined by its [`description`](https://docs.cloud.google.com/looker/docs/reference/param-field-description) LookML parameter
  * Type: the field type, as defined by its `type` LookML parameter (see measure [`type`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) or dimension, filter, and parameter [`type`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types))
  * Default aggregation: the [aggregation method](https://docs.cloud.google.com/data-studio/aggregation-article#default-aggregation) that is used by the field
  * SQL: the field's SQL expression, as defined by its [`sql`](https://docs.cloud.google.com/looker/docs/reference/param-field-sql) LookML parameter



## How Looker Explores behave in Data Studio reports

A Looker data source in Data Studio is based on a Looker Explore, which is defined in a Looker [model's LookML](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#model). Looker developers use LookML to describe dimensions, aggregates, calculations, and data relationships in an organization's SQL database. Some LookML parameters are applied in the Looker data source but not surfaced in Data Studio. The following sections describe the LookML parameters that are applied in the Looker data source and that you can interact with in Data Studio.

### Drill fields and links

Drill fields and links that are defined with the [`drill_fields`](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) and [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link) LookML parameters are available to Data Studio report viewers in the **[Drill Actions](https://docs.cloud.google.com/data-studio/drill-into-your-data)** menu on Data Studio table charts.

See the [Drill into your data](https://docs.cloud.google.com/data-studio/drill-into-your-data) documentation page to learn more about using drill actions in Data Studio.

#### Things to know about drill actions in Data Studio

Keep the following information in mind when you're using drill actions (drill fields and links) with a Looker data source:

  * They are supported only on [table charts](https://docs.cloud.google.com/data-studio/table-reference).
  * They are supported only for Looker dimensions and dimension groups.
  * If they are imported from Looker, they are read-only. To make changes to imported drill actions, [edit the underlying LookML model](https://docs.cloud.google.com/looker/docs/lookml-validation) in Looker.



### Filters

Report editors can define [persistent filters](https://docs.cloud.google.com/data-studio/about-filter-properties) (at the chart, group, page, and report level), [quick filters](https://docs.cloud.google.com/data-studio/add-a-quick-filter), and [controls](https://docs.cloud.google.com/data-studio/about-controls) in Data Studio reports based on fields from the Looker data source.

Data Studio indicates which fields have been defined in the Looker data source's underlying LookML as filters or filter-only fields. Data Studio also displays suggestions for filter values based on the data source's LookML [`suggest_dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-dimension) and [`suggest_explore`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-explore) definitions when **Equal to (=)** and **In** conditions are used. To see filter value suggestions, enable **Show suggested values while typing** in the filter editor. Any predefined default values will be pre-selected.

Viewers can access and modify any of the report's editable filters by clicking the report's **More options** menu and selecting [**View applied filters**](https://docs.cloud.google.com/data-studio/about-filter-properties).

In reports that use a Looker data source, filters that have been defined with LookML parameters are referenced in Data Studio as described in the following table:

LookML definition | Data Studio location | Data Studio reference  
---|---|---  
[`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter) | [Report editor](https://docs.cloud.google.com/data-studio/edit-a-report): **Properties Setup Filter** section | **Conditionally required**  
[Filter manager](https://docs.cloud.google.com/data-studio/create-edit-and-manage-filter-properties): **Type** column | **Conditionally filter**  
Report editor: **Group Properties** | **Conditionally required**  
Report editor: **Current Page Settings** | Not distinguished from other filter types  
Report editor: **Report Settings** | **Conditionally required**  
[Data source editor](https://docs.cloud.google.com/data-studio/edit-a-data-source): **Datasource filters** section | **Conditionally filter**  
**Filter bar** (quick filters) | Not distinguished from other filter types  
[`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) | [Report editor](https://docs.cloud.google.com/data-studio/edit-a-report): **Properties Setup Filter** section | **Always required**  
[Filter manager](https://docs.cloud.google.com/data-studio/create-edit-and-manage-filter-properties): **Type** column | **Always filter**  
Report editor:**Group Properties** | **Always required**  
Report editor:**Current Page Settings** | Not distinguished from other filter types  
Report editor: **Report Settings** | **Always required**  
[Data source editor ](https://docs.cloud.google.com/data-studio/edit-a-data-source): **Datasource filters** section | **Always filter**  
**Filter bar** (quick filters) | Not distinguished from other filter types  
[`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter), [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) | [Report editor](https://docs.cloud.google.com/data-studio/edit-a-report): **Properties Setup Filter** | Not distinguished from other filter types  
[Report editor](https://docs.cloud.google.com/data-studio/edit-a-report): **Data** > Explore name > **Filter-only fields** field group | **Filter-only fields**  
[Filter manager](https://docs.cloud.google.com/data-studio/create-edit-and-manage-filter-properties): **Type** column | Not distinguished from other filter types  
Report editor: **Group Properties** | Not distinguished from other filter types  
Report editor: **CurrentPage Settings** | Not distinguished from other filter types  
Report editor: **Report Settings** | Not distinguished from other filter types  
[Data source editor](https://docs.cloud.google.com/data-studio/edit-a-data-source): **Filter-only fields** section | **Filter-only fields**  
**Filter bar** (quick filters) | Not distinguished from other filter types  
Report controls | N/A  
  
If [`sql_always_where`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where), [`sql_always_having`](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-having), or [`access_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter) parameters are included in the underlying LookML model, they will be applied to the data source but won't be visible in Data Studio.

#### More about filters that are always or conditionally required

Keep the following information in mind when using conditional LookML filters:

  * You can't remove filters that are either conditionally or always required from a chart.
  * Report editors can make changes to a filter clause's [condition or value](https://docs.cloud.google.com/data-studio/configure-filter-conditions) but can't change the filter field in Data Studio. To make changes to imported LookML filters, [edit the underlying LookML model](https://docs.cloud.google.com/looker/docs/lookml-validation) in Looker.
  * The numeric filter type supports the **Matches (advanced)** condition with the user-entered **not null** value only.
  * The **Matches (advanced)** condition behaves somewhat differently in Data Studio and in Looker. In a Looker Explore, Looker may convert the **matches (advanced)** condition to a more appropriate condition, based on the user's input. Data Studio uses the **Matches (advanced)** option as a catch-all condition when the user's input is inappropriate for the other filter conditions that Data Studio supports; however, Data Studio doesn't convert the condition. For more information about the filter values that you can use with the **Matches (advanced)** condition, see the [Looker filter expressions](https://docs.cloud.google.com/looker/docs/filter-expressions) documentation page.
  * Data Studio doesn't support all [Looker filter conditions](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#basic_filters). If a LookML model defines a `conditionally_filter` parameter or an `always_filter` parameter that uses an a filter condition that is not supported by Data Studio, Data Studio displays a filter condition of **Is Null**. Report editors must manually update the filter conditions and values. The Looker filter conditions that Data Studio supports are shown in the following table, with the Looker filter condition written as it would appear in a Looker Explore and the equivalent [Data Studio filter condition](https://docs.cloud.google.com/data-studio/configure-filter-conditions):

Filter expression type | Supported Looker filter condition | Equivalent Data Studio filter condition  
---|---|---  
String or text | **is** | **Equal to (=)**  
String or text | **is any value** | **Is Any**  
String or text | **is null** | **Is Null**  
String or text | **matches (advanced)** | **Matches (advanced)**  
Date and time | **is on the day** | **Equal to (=)**  
Date and time | **is any time** | **Is Any**  
Date and time | **matches (advanced)** | **Matches (advanced)**  
Boolean | **is** (with a value of **Yes** or **yes**) | **True**  
Boolean | **TRUE** or **is yes** | **True**  
Boolean | **is No** (with a value of **No** or **no**) | **False**  
Boolean | **FALSE** | **False**  
Boolean | **is any value** | **Is Any**  
Numeric | **is** | **Equal to (=)**  
Numeric | **is any value** | **Is Any**  
Numeric | **is null** | **Is Null**  
Numeric | **matches (advanced)** | **Matches (advanced)**  
  
#### More about filter-only fields

**Warning:** The LookML parameter that is called "[`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter)" differs from Data Studio [parameters](https://docs.cloud.google.com/data-studio/parameters). The LookML`parameter` creates a filter-only field that can be used to filter Explores, Looks, and dashboards but that can't be added to a result set. Data Studio parameters collect and pass user-supplied values to calculated fields and connectors.

  * To make changes to imported filter-only fields, such as [specifying the values](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#specifying_allowed_values) that a user can input, [edit the underlying LookML model](https://docs.cloud.google.com/looker/docs/lookml-validation) in Looker.
  * When a report editor edits a filter that uses a filter-only field, they must use an AND operator and can't include the same filter-only field. The available values are defined in the Looker data source's underlying LookML.
  * Advanced filter controls are unavailable for filter-only fields that have [allowed values](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#specifying_allowed_values) defined in the underlying LookML.
  * Data Studio doesn't support all types and values for filter-only fields. If a LookML model defines `parameter` or `filter` parameters that use an unsupported type, Data Studio displays a filter condition of **Is Null**. Report editors must manually update the filter conditions and values. The supported filter-only field types are shown in the following table:

LookML parameter | Field type | Data Studio filter condition | Supported input values  
---|---|---|---  
[`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) | [`string`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#parameters_of_type_string) | All | Any user input value or only predefined values  
[ ` unquoted `](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#parameters_of_type_unquoted) | All | Any user input value or only predefined values  
[`date_time`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#parameters_of_type_date_time) | Equal to (=) | Any user input date of the formats YYYY-MM-DD or YYYY/MM/DD  
[`yesno`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#parameters_of_type_yesno) | Equal to (=) | Predefined Boolean values  
[`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) | `string` | All | Any user input value  
`number` | All | Any user input value in a number format  
`yesno` | Equal to (=) | Predefined Boolean values  
` date_time ` | Equal to (=) | Any user input date of the formats YYYY-MM-DD or YYYY/MM/DD  
`date` | Equal to (=) | Any user input date of the formats YYYY-MM-DD or YYYY/MM/DD  
  
## Related resources

  * [Looker and Data Studio shared terms and concepts](https://docs.cloud.google.com/looker/docs/looker-and-studio-shared-terms-glossary)
  * [Add data to a report](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Edit fields in your reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
