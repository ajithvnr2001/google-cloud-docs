---
url: https://docs.cloud.google.com/monitoring/dashboards/filter-permanent/
title: Create and manage variables and pinned filters \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:10.385771+00:00
---

# Create and manage variables and pinned filters  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/dashboards/filter-permanent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create and manage variables and pinned filters Stay organized with collections  Save and categorize content based on your preferences. 

Pinned filters and variables on a custom dashboard in Cloud Monitoring let you dynamically change the data displayed across your dashboard from the toolbar without editing individual widgets. Pinned filters apply to all widgets that support the filter's label, whereas variables apply to specific widgets to modify their queries or control their visibility.

This document describes how to configure pinned filters and variables in the Google Cloud console. To configure them by using the Cloud Monitoring API, see [Create and manage dashboards by API: Dashboard filters](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard#define_filters). To apply filters or groupings for only your current session, see [Add temporary filters to a custom dashboard](https://docs.cloud.google.com/monitoring/charts/filter-dashboard).

## About pinned filters

A pinned filter contains a label, one or more default values, and a list of all possible values. The list of all possible values is derived dynamically from the time-series data displayed on your dashboard.

**You don't apply a pinned filter to individual widgets.** Instead, the following rules are used to determine whether the pinned filter can change the data displayed by the widget:

  * If the widget displays data that includes the label key specified by a pinned filter and if the widget doesn't specify a value for that label key, then the pinned filter can change the data that is displayed.

For example, suppose you add the pinned filter **cluster_name: mycluster**. Then charts automatically display only those time series that have a **cluster_name** label with a value of **mycluster**. Similarly, the queries on your logs panel widgets are modified to **resource.labels."cluster_name"="mycluster"** , and your charts automatically display only those time series that include the label in the pinned filter.

  * A pinned filter is ignored by a widget when the widget includes a filter for the same label key, or when the data displayed by the widget doesn't contain the label key specified in the pinned filter.




In the API, pinned filters are defined by the [`DashboardFilter`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DashboardFilter) structure. For example, the following structure defines a pinned filter. Time series that have a `zone` label whose value is `us-central1-c` match the pinned filter.
    
    
    {
       "labelKey": "zone",
       "stringValue": "us-central1-c",
       "valueType": "STRING",
       "filterType": "RESOURCE_LABEL"
    },
    

## About variables

Similar to pinned filters, a variable has a name and type, and one or more default values. However, unlike pinned filters which are always label-based, variables don't have to depend on labels.

**A variable is applied to a particular widget by modifying the query that the widget contains.**

In the dashboard toolbar, variable names are prepended with a dollar sign `$`. If you also see a _visibility_ **Visible** icon, then the variable controls the visibility of at least one widget.

User-defined variables can either be label-based or only have a value:

  * Label-based variables are like pinned filters. These variables contain a label key, one or more default label values, and a list of all possible label values. The list of all possible values is derived dynamically from the time-series data displayed on your dashboard.

  * Value-only variables contain one or more default values, and they might list all possible values. If you don't specify a default value, then the wildcard operator, `(*)`, is selected for the default value. To define the set of all possible values, you either provide an array of values or you write a SQL query.

There are three types of value-only variables: **Custom** , **Text Input** , and **SQL Query**.

    * **Custom** : Use when you want to enumerate both the list of all possible values and also set one or more default values. For example, you might set the list of all possible values to `prod, staging, dev`, and set the default value to `prod`.

    * **Text Input** : Use when you don't know all possible values. When you create this variable, you can specify one or more values. However, the menu option lets you add new values that apply to your current session.

    * **SQL Query** : Use when you want to generate the list of possible values by using a SQL query. These variables are intended to be applied to charts created by using Observability Analytics.

For these variables, ensure that the query result is a table with one column, that the data type of that column is string, and that each row in the table contains a unique string value:
          
          SELECT log_name
          FROM `VIEW`
          GROUP BY log_name
          

The SQL query can't depend on a variable.




There is one system-defined variable, `@__project_id`. You can use this variable only in the `FROM` clause for SQL queries. To learn how to apply this variable to a query, see [Charts with SQL queries](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#sql).

To apply a variable to a widget, you either update the query issued by the widget or you update the visibility of the widget. You can always edit the widget to update its query. However, for label-based variables and some widget types, you can update the query by making menu selections. To control the visibility, you must edit the widget. For more information, see the following sections of this document:

  * Update the query of a widget
  * Set the visibility of a widget



In the API, variables are defined by the [`DashboardFilter`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DashboardFilter) structure. For example, the following structure defines the variable `my_zone_variable` that operates on the `zone` resource label. Time series that have a `zone` label whose value is `us-central1-c` match the variable.
    
    
    {
       "labelKey": "zone",
       "stringValue": "us-central1-c",
       "templateVariable": "my_zone_variable",
       "valueType": "STRING",
       "filterType": "RESOURCE_LABEL",
    },
    

## Before you begin

Complete the following for the Google Cloud project where you want to configure pinned filters and variables:

  * To get the permissions that you need to add or modify variables or pinned filters by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).




## Create and pin a filter

To create and pin a filter that applies to all dashboard widgets that support filters, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard, go to the dashboard toolbar, and then click _settings_ **Settings**.
  4. In the **Filters** section, click **Add a filter**.
  5. Click _arrow_drop_down_ **Label** and then select a label. For example, you might select `zone`.
  6. To let users select multiple values from the filter's value menu, select **Multi-select**. When **Multi-select** isn't enabled, users can only select one option from the value menu.
  7. Click _arrow_drop_down_ **Default value** and then select the default value, or values, for the label. To match all values, select `*`.

**Note:** When dashboards contain PromQL-defined charts, the menu of values for a filter might not load or the menu might not contain the correct values. However, you can enter the filter value manually.

After the filter is created, it is added to your dashboard toolbar. To temporarily change the filter value, select the filter, and then make a selection from the menu.

  8. Click **Done** and then **Apply**.

  9. To save your modified dashboard, in the toolbar, click **Save**.




## Create a variable

To create a variable that applies to specific dashboard widgets, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select a dashboard, go to the dashboard toolbar, and then click _settings_ **Settings**.
  4. In the **Variables** section, click **Add a variable**.
  5. Select the type of variable and then complete the dialog.

**Note:** To let a user select multiple values from the variable's value menu, select **Multi-select**. When **Multi-select** isn't enabled, users can only select one option from the value menu.

To create a label-based variable, select **Label**. Use this option when you want a variable that has a label key and label value, and that can be used like a pinned filter. The list of all possible values is derived dynamically from the time-series data displayed on your dashboard. The **Apply to charts** menu lets you select widgets whose query is to be modified by the variable. You can also update the query by editing the widget.

For value-only variables, you have the following options:

     * **SQL** : Use this option when you want the results of a SQL query to generate the list of all possible values.

Enter one or more default values, and enter a SQL query that generates the list of all possible values. Ensure that the query result is a table with one column, that the data type of that column is string, and that each row in the table contains a unique string value.

     * **Custom** : Use this option when you want to specify both the list of possible values and also a default value. For example, you might set the **Values** field to `prod, staging, dev`, and set the **Default value** to `prod`.

     * **Text Input** : Use this option when you want to specify a list of values that are applied as defaults.

  6. Click **Done** and then **Apply**.

  7. To save your modified dashboard, in the toolbar, click **Save**.

Monitoring adds the variable to the dashboard toolbar. The name on the toolbar is a dollar sign `$` followed by the name of the variable. The toolbar contains a menu that lets you change the value of the variable.

  8. Optional: Move your variable from the dashboard toolbar to a dashboard widget.

You can add a widget to your dashboard that lets you modify the value of your variable. If you make this change, then the toolbar variable is removed. However, you can place the widget that controls the variable adjacent to the widgets it affects. To learn how to make this change, see Add widget to manage the value of a variable.

  9. Apply the variable to widgets. If you update the query of a widget, then when you change the value of the variable, the query is modified and the data the widget displays is modified. You can also use a variable to control whether a widget is visible. For more information, see the following sections of this document:

     * Set the visibility of a widget
     * Update the query of a widget



## Add widget to manage the value of a variable

Because variables apply to a subset of dashboard widgets, you might want to group the control of the variable and the widgets to which it applies. For example, you might create a collapsible group or create a section in the dashboard for the variable menu and associated widgets. This strategy also simplifies the toolbar, by removing variables that don't apply to all widgets.

To manage the value of a variable by using a dashboard widget, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the **Add widget** dialog, go to the **Layout** section, and then select **Variable**.
  4. Complete the dialog and then select **Save**.

The dashboard displays a widget that lets you select the value for your variable. You can move this widget into a collapsible group or otherwise reposition the widget.

  5. To save your modified dashboard, in the toolbar, click **Save**.




## Set the visibility of a widget

When a widget queries data, you can use a variable to control whether the widget is visible on a dashboard. For example, suppose that a dashboard contains widgets that display data for your production systems and another set of widgets that display data for your staging systems. When debugging during development, you might only want to view the staging data. By configuring the visibility of the dashboard widgets with a variable, you can switch between only production data, only staging data, and all data.

Any type of variable can control whether a widget is visible or hidden.

To configure the visibility of a widget, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select a dashboard.
  3. Go to the toolbar of the widget whose visibility you want to configure, and then click _edit_ **Edit**.
  4. In the **Display** pane, expand **Widget visibility**.
  5. Select a variable and complete the dialog.

**Note:** The value of the **Comparator** must be set to regular expression.
  6. Click **Done** and then **Apply**.

  7. To save your modified dashboard, in the toolbar, click **Save**.

The dashboard is refreshed. When at least one widget on the dashboard is hidden due to visibility controls, the dashboard displays a banner. To view all widgets, click **Show all widgets**.




When you use a variable to control the visibility of at least one widget on your dashboard, in the toolbar, the variable name is annotated with a _visibility_ **Visible** icon.

### Limitations

The following limitations apply when configuring the visibility of a widget:

  * Organizational widgets, such as collapsible group, section-header, and single-view widgets, are always visible.

  * You can delete a variable that is referenced by the visibility controls of a widget. The variable-delete action also removes any reference to the variable.

  * Not all dashboards support creation of variables. However, if a dashboard contains variables, then you can use those variables to manage the visibility of widgets on the dashboard.




## Update the query of a widget

This section describes how to include variables in the query that the widget issues. As a result, when you change the value of the variable, the query is modified and the data the widget displays is modified:

  * For charts that use SQL or PromQL queries, and for logs panel widgets, you must edit the widget and modify the query. This section describes how to make those edits.

  * For charts that you configured by using menus or by using direct-filter mode, Monitoring edits the query when you select the widget by using the **Apply to charts** menu. As an alternative, you can edit the widget, go to the **Filter** field, and then select the variable.




To learn how to update the query of a widget with a label-based variable or value-only variable, see the following sections:

  * General syntax to dereference a variable
  * Logs panel widgets
  * Charts with PromQL queries
  * Charts with SQL queries
  * Charts with Monitoring filter queries

When you use the menu-driven interface to create a chart that displays time-series data, your selections are converted into a [Monitoring filter](https://docs.cloud.google.com/monitoring/api/v3/filters).




### Create filters and variables

###  Console 

For information about how to use the Google Cloud console to create pinned filters and variables, see the following documents:

  * [Create and pin a filter](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#create-permanent-filter)
  * [Create a variable](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent#create-variable)



###  REST 

To define pinned filters and variables, use the [`dashboardFilters`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DashboardFilter) data structure.

  * To create a variable, set the value of the `templateVariable` field to the name of the variable. Omit this field or set the value to an empty string when you want to create a pinned filter.
  * To create a pinned filter or a label-based variable, you must specify the `labelKey` field. Omit this field when you want a value-only variable.
  * Set the default value for the filter or variable. The configuration of this field determines whether a user can select exactly one option from the menu of value, or whether they can select multiple values.

  * To set a single default value and to restrict users to selecting exactly one option in the values menu, set the `valueType` field as `STRING` and also set the `stringValue` field:
        
        "valueType": "STRING",
        "stringValue": "my-default-value",
        

  * To set at least one default value and to let users select multiple options in the values menu, set the `valueType` field as `STRING_ARRAY` and also set the `stringArrayValue` field. In the following example, there are three default values.
        
        "valueType": "STRING_ARRAY",
        "stringArrayValue": {
          "values": [ "a", "b", "c" ]
        },
        

**Note:** If you don't specify a default value, then the wildcard operator, `(*)`, is selected automatically. If you plan to use the variable in a logs panel, then you must use the regular expression as a comparator. For SQL queries, you must use an `IF` statement. For more information, see Charts with SQL queries.
  * Optional: To specify the list of all possible values for a value-only variable, set either the `stringArray` field or the `timeSeriesQuery` field. If you specify a query, it must be an analytics query.

**Note:** Don't set the `timeSeriesQuery` or `stringArray` fields when you create a pinned filter or a label-based variable. The set of all possible values is dynamically determined.



For example, consider the following `dashboardFilters` object:
    
    
    {
      "dashboardFilters": [
          {
            "labelKey": "zone"
            "stringValue": "us-central1-c",
            "valueType": "STRING",
            "filterType": "RESOURCE_LABEL"
          },
          {
            "labelKey": "instance_id",
            "stringValue": "3133577226154888113",
            "valueType": "STRING",
            "filterType": "RESOURCE_LABEL",
            **"templateVariable": "my_label_based_variable"**
          },
          {
            "filterType": "VALUE_ONLY",
            **"templateVariable": "my_value_only_variable"** ,
            timeSeriesQuery: {
              opsAnalyticsQuery: {
                **sql: "
                  SELECT log_name
                  FROM `MY_TABLE`
                  GROUP BY log_name**
                ",
              }
            }
          }
        ],
      "displayName": "Illustrate Variables",
      ...
    }
    

The previous JSON defines one pinned filter and two variables:

  * The pinned filter has the label key of `zone`, which is is displayed on the toolbar. The `valueType` and `stringValue` fields specify the single default value. For more information, see the API references page for the [`dashboardFilters`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.dashboards#DashboardFilter) data structure.

  * The label-based variable has the name `my_label_based_variable`, and its label key is `instance_id`. The default value for this variable is set to a specific instance ID. You can also configure the default value by using an array. On the toolbar, the filter is displayed with the name `my_label_based_variable`.

  * The value-only variable is named `my_value_only_variable`. This entry doesn't specify a default value, so the wildcard operator, `(*)`, is automatically applied. Additionally, this variable uses a SQL query to generate the list of possible values for the variable.




Note that the `dashboardFilters` object doesn't list the widgets to which the variable applies. Instead, you update the query of a widget to depend on a variable.

### General syntax to dereference a variable

For all widgets, except those that are defined by SQL, use the following syntax to apply a variable to a query:

  * To apply a label-based variable and have the label key and the label value resolved into a valid filter expression for the query language, use `${my_label_based_variable}`.

  * To apply only the value of a label-based variable, use `${my_label_based_variable.value}`. The comparison must use a regular expression.

  * To apply only the value of a value-only variable, use `${my_value_only_variable}`. For value-only variables, don't include a `.value` clause. The comparison must use a regular expression.




### Logs panel widgets

To apply a variable to a logs panel widget, update the queries pane. The syntax for these widgets follows that specified under General syntax.

###  Console 

For example, the following query uses a regular expression to compare the value of the `jsonPayload.message` field with a string value that includes the value of a label-based variable:
    
    
    jsonPayload.message=~"Connected to instance: **${my_label_based_variable.value}** "
    

As another example, consider a value-only variable, `value_only_severity_variable`, and assume that in the menu of values, three values are selected: `ERROR`, `INFO`, and `NOTICE`. Next, you add the following to the query pane of your logs panel widget:
    
    
    severity =~ "${value_only_severity_variable}"
    

The following illustrates the rendered form:
    
    
    severity =~ "^(ERROR|INFO|NOTICE)$"
    

###  REST 

For example, the following JSON illustrates how to update the query of a logs panel widget with a label-based variable:
    
    
    "logsPanel": {
      "filter": "**${my_label_based_variable}** ",
      "resourceNames": [
        "projects/1234512345"
      ]
    },
    

For example, the following query uses a regular expression to compare the value of the `jsonPayload.message` field with a string value that includes the value of a label-based variable:
    
    
    "logsPanel": {
      "filter": "resource.type=\"gce_instance\"\n
                resource.labels.project_id**=~\"${my_label_based_variable.value}\"** \n",
      "resourceNames": [
        "projects/012345"
      ]
    }
    

As another example, consider a value-only variable, `value_only_severity_variable`, and assume that three values are selected in the menu: `ERROR`, `INFO`, and `NOTICE`. Next, you add the following to the query pane of your logs panel widget:
    
    
    "logsPanel": {
      "filter": "severity =~ \"${value_only_severity_variable}\"\n",
      ...
    }
    

The following illustrates the query as executed by the logs panel widget:
    
    
    severity =~ "^(ERROR|INFO|NOTICE)$"
    

If you've configured a query for the logs panel and then select the button to open the Logs Explorer, the variables are resolved before the Logs Explorer is opened.

The following table illustrates how the example variables are are resolved by the logs panel. As previously mentioned, when only the value of a variable is used, you must use a regular expression as the comparison operator:

Syntax | Selected  
Value | Resolved logs panel expression  
---|---|---  
`${my_label_based_variable}` | `12345` | `resource.labels."instance_id"="12345"` The example variable is based on the resource label `instance_id`.  
`${my_label_based_variable}` | `*` | `""`  
`${my_label_based_variable.value}`  
`${my_value_based_variable}` | `12345` | `12345`  
`${my_label_based_variable.value}`  
`${my_value_based_variable}` | `*` | `.*`  
  
### Charts with PromQL queries

To update a chart that has a PromQL query to depend on a label-based variable, follow the guidance listed in General syntax.

###  Console 

For example, the following query relies on the label-based variable, `my_label_based_variable`, being resolved into a filter expression:
    
    
    compute_googleapis_com:instance_cpu_utilization{
        monitored_resource="gce_instance", **${my_label_based_variable}** }
    

You can also modify query to resolve only the value of a variable. The following example uses a regular expression to compare the value of a label-based query to the `instance_id`:
    
    
    compute_googleapis_com:instance_cpu_utilization{
        instance_id**=~"${my_label_based_variable.value}"**
    }
    

If you have a value-only variable, then omit the `.value` clause. For example, to filter by zone using a value-only variable, the query would include something like the following:
    
    
    zone**=~"${my_value_only_variable}"**
    

###  REST 

For example, the following JSON illustrates a query that relies on the label-based variable, `my_label_based_variable`, being resolved into a filter expression:
    
    
    "timeSeriesQuery": {
      "prometheusQuery": "avg_over_time(
        compute_googleapis_com:instance_cpu_utilization{
          monitored_resource=\"gce_instance\",
          **${my_label_based_variable}**
          }[${__interval}])",
      "unitOverride": "",
      "outputFullDuration": false
    },
    

You can also modify query to resolve only the value of a variable. The following example uses a regular expression to compare the value of a label-based query to the `instance_id`:
    
    
    "timeSeriesQuery": {
      "prometheusQuery": "avg_over_time(
        compute_googleapis_com:instance_cpu_utilization{
        monitored_resource=\"gce_instance\",
        instance_id**=~\"${my_label_based_variable.value}\"**
        }[${__interval}])",
      "unitOverride": "",
      "outputFullDuration": false
    },
    

If you have a value-only variable, then omit the `.value` clause. For example, to filter by zone using a value-only variable, the query would include something like the following:
    
    
    zone**=~\"${my_value_only_variable}\"**
    

The following table illustrates how the example variables are are resolved by the PromQL. As previously mentioned, when only the value of a variable is used, you must use a regular expression as the comparison operator:

Syntax | Selected  
Value | Resolved PromQL expression  
---|---|---  
`${my_label_based_variable}` | `12345` | `instance_id == '12345'` The example variable is based on the resource label `instance_id`.  
`${my_label_based_variable}` | `*` | `noop_filter=~".*"`  
`${my_label_based_variable.value}`  
`${my_value_based_variable}` | `12345` | `12345`  
`${my_label_based_variable.value}`  
`${my_value_based_variable}` | `*` | `.+`  
  
### Charts with SQL queries

There are two places where you can use variables in your SQL queries:

  * The `FROM` clause can depend on the system-defined variable named `@__project_id`, which resolves to the value of your selected project.

  * The `WHERE` clause can depend on user-defined variables.




**Update the`FROM` clause to depend on a system-defined variable**

If you create dashboard templates and these templates chart the results of SQL queries, then replace the project ID in your query with the variable `@__project_id`. When you install the template in a project, the variable automatically resolves to the project ID. You don't need to manually edit the widget and update the `FROM` clause.

The following illustrates a `FROM` clause that depends on the system-defined variable:
    
    
    FROM `@__project_id.global._Default._Default`
    

The `FROM` clause can't depend on user-defined variables.

**Update the`WHERE` clause to depend on a user-defined variable**

This section describes how you can update the `WHERE` clause of a SQL-defined widget to depend on a user-defined variable. For all variables, prefix the variable name with the "at" sign, for example: `@variable_name`. For label-based variables, append `.value` to the variable name, `@my_label_based_variabe.value`.

For SQL queries, the variable substitution relies on BigQuery, and is SQL-injection safe. For more information, see [Running parameterized queries](https://docs.cloud.google.com/bigquery/docs/parameterized-queries).

###  Console 

Because SQL doesn't interpret the wildcard operator to mean "any value", we recommend that you always use an `IF` statement when using variables in a SQL query. The following example illustrates usage for a value-only variable whose data type is a string:
    
    
    WHERE **IF(@my_value_only_variable = "*", TRUE, log_name = @my_value_only_variable)**
    

When the menu option for the variable lets users select multiple values, you must cast the value of the variable to a GoogleSQL data type by using the [`CAST` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#cast). The following query illustrates this syntax:
    
    
    IF(ARRAY_LENGTH(CAST(@my_value_only_variable)) = 0, TRUE,
       severity IN UNNEST(@my_value_only_variable))
    

The `IF` statement shown in the previous examples is recommended because SQL doesn't interpret the wildcard operator to mean "any value". Therefore, if you omit the `IF` statement and if you select the wildcard operator, then the result of the query is an empty table. In the second example, the [`UNNEST` function](https://docs.cloud.google.com/bigquery/docs/arrays#flattening_arrays) converts the array to a table.

To add a properly-formatted `WHERE` clause, do the following:

  1. Edit the widget.
  2. In the toolbar, select **Insert variable filter** , and then select the variable whose `WHERE` clause you want to update.
  3. In the dialog that opens, review the generated code and then click **Copy and close**.
  4. Paste the copied code into the **Query** pane and make any necessary edits.

For example, suppose you create a variable named `LogName` that generates a list of log names and outputs the result in a table with a single column named `log_name`. Next, you create a chart, select **Insert variable filter** , and then select the variable `LogName`. The following code is generated:
         
         WHERE IF(@LogName = '*', TRUE, LogName = @LogName)
         

In this example, you need to edit the generated code and replace `LogName =` with `log_name =`, so that the table join can occur:
         
         WHERE IF(@LogName = '*', TRUE, log_name = @LogName)
         

  5. Click **Run** and then **Apply**.

  6. To save your modified dashboard, in the toolbar, click **Save**.




###  REST 

Because SQL doesn't interpret the wildcard operator to mean "any value", we recommend that you always use an `IF` statement when using variables in a SQL query. The following example illustrates usage for a value-only variable whose data type is a string:
    
    
    WHERE **IF(@my_value_only_variable = "*", TRUE, log_name = @my_value_only_variable)**
    

For example, the following shows a partial JSON representation of a chart that displays the results of a SQL query. To support filtering the results by the name of a log, a `WHERE` clause was added that references the variable named `LogName`:
    
    
    "plotType": "STACKED_BAR",
    "targetAxis": "Y1",
    "timeSeriesQuery": {
      "opsAnalyticsQuery": {
        "queryExecutionRules": {},
        "queryHandle": "",
        "sql": "SELECT\n timestamp, severity, resource.type, log_name, text_payload, proto_payload, json_payload\n
                FROM\n `my-project.global._Default._Default`\n
                WHERE \n **IF (@LogName = \"*\", TRUE, log_name=@LogName)** \nLIMIT 10000"
      }
    }
    

The variable `LogName` also issues a query to determine the list of possible log names:
    
    
    "dashboardFilters": [
      {
        "filterType": "VALUE_ONLY",
        "templateVariable": "LogName",
        "valueType": "STRING",
        "timeSeriesQuery": {
          "opsAnalyticsQuery": {
            "savedQueryId": "",
            "sql": "SELECT log_name FROM `my-project.global._Default._Default` GROUP BY log_name LIMIT 1000",
            "queryHandle": ""
          },
          "unitOverride": "",
          "outputFullDuration": false
        }
      }
    ],
    

When the menu option for the variable lets users select multiple values, you must cast the value of the variable to a GoogleSQL data type by using the [`CAST` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#cast). The following query illustrates this syntax:
    
    
    IF(ARRAY_LENGTH(CAST(@my_value_only_variable)) = 0, TRUE,
       severity IN UNNEST(@my_value_only_variable))
    

The `IF` statement shown in the previous examples is recommended because SQL doesn't interpret the wildcard operator to mean "any value". Therefore, if you omit the `IF` statement and if you select the wildcard operator, then the result of the query is an empty table. In the second example, the [`UNNEST` function](https://docs.cloud.google.com/bigquery/docs/arrays#flattening_arrays) converts the array to a table.

### Charts with Monitoring filter queries

To update a chart that has a query in the form of a Monitoring filter to depend on a label-based variable, follow the guidance listed in General syntax.

###  Console 

If you use the Google Cloud console to create your charts, and if you use the menu-driven interface, then you can update the chart's query by using the variable's **Apply to charts** field or by editing the widget and selecting label-based variable from the **Filter** menu. The **Filter** menu lists all label-based variables and all label keys.

To update the query of a chart to depend on a value-based variable, do the following:

  1. Edit the chart.
  2. In the query pane, click **Add filter** and select a label key. For example, you might select **zone**.
  3. In the **Value** menu, select your value-only variable.
  4. Click **Apply**.
  5. To save your modified dashboard, in the toolbar, click **Save**.



For example, the following JSON illustrates a query that relies on a label-based variable, `my_label_based_variable`, being resolved into a filter expression:
    
    
    metric.type="compute.googleapis.com/instance/cpu/utilization"
    resource.type="gce_instance" **${my_label_based_variable}** "
    

Widgets that use a query in the form of a Monitoring filter can't filter the time series by the value in a label-based variables; however, you can filter by value-only variables. For example, the following query shows the value of the **Filters** field of a query that filters by `zone`, based on the value of a value-only variable:
    
    
    metric.type="compute.googleapis.com/instance/cpu/utilization"
    resource.type="gce_instance"
    resource.label."zone"=**monitoring.regex.full_match(${my_value_only_variable})**
    

###  REST 

For example, the following JSON illustrates a query that relies on a label-based variable, `my_label_based_variable`, being resolved into a filter expression:
    
    
    "timeSeriesQuery": {
      "timeSeriesFilter": {
        "filter": "metric.type=\"compute.googleapis.com/instance/cpu/utilization\"
                  resource.type=\"gce_instance\"
                  **${my_label_based_variable}** ",
        "aggregation": {
          "alignmentPeriod": "60s",
          "perSeriesAligner": "ALIGN_MEAN",
          "groupByFields": []
        }
      },
      "unitOverride": "",
      "outputFullDuration": false
    },
    

Widgets that use a query in the form of a Monitoring filter can't filter the time series by the value in a label-based variables; however, you can filter by value-only variables. For example, the following query shows the `"filter"` field of a query that filters by `zone`, based on the value of a value-only variable:
    
    
    "filter": "metric.type=\"compute.googleapis.com/instance/cpu/utilization\"
              resource.type=\"gce_instance\"
              resource.labels.\"zone\"**=monitoring.regex.full_match(${my_value_only_variable})** "
    

The following table illustrates how the example variables are are resolved by the Monitoring filter. As previously mentioned, when only the value of a variable is used, you must use a regular expression as the comparison operator:

Syntax | Selected  
Value | Resolved filter expression  
---|---|---  
`${my_label_based_variable}` | `12345` | `resource.instance_id == "12345"` The example variable is based on the resource label `instance_id`.  
`${my_label_based_variable}` | `*` | Omitted  
`${my_label_based_variable.value}` | `12345` | Not supported  
`${my_label_based_variable.value}` | `*` | Not supported  
`${my_value_based_variable}` | `12345` | `"12345"`  
`${my_value_based_variable}` | `*` | `".*"`  
  
## Modify a pinned filter or variable

**Note:** If you modify the value of a variable, then only those widgets to which you've applied the variable can be modified. However, if you modify the value of a pinned filter, then all widgets on a dashboard can be modified.

To temporarily change the value of any pinned filter or variable displayed on the dashboard toolbar, click the name of the filter or variable, and either enter a value or make a selection from the menu.

If your dashboard contains a table that displays time-series data, then you can add temporary filters or modify permanent filters and variables by using a cell's _filter_list_ **Filter dashboard to this value** button. This button, when selected, either applies a new temporary filter or it updates the value for an existing filter or variable. Existing filters and variables are updated when the label key for the table column matches the label key for a filter or variable.

**Note:** When dashboards contain PromQL-defined charts, the menu of values for a filter might not load or the menu might not contain the correct values. However, you can enter the filter value manually.

To change the configuration of a pinned filter or a variable, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the dashboard toolbar, click _settings_ **Settings**.
  4. Find the filter or variable that you want to modify and expand its definition.
  5. After you complete your modifications, click **Apply**.
  6. To save your modified dashboard, in the toolbar, click **Save**.



## Delete a pinned filter or variable

To delete a pinned filter or a variable, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the dashboard toolbar, click _settings_ **Settings**.
  4. Find the filter or variable that you want to remove, and then click delete **Delete**.
  5. Click **Apply**.
  6. To save your modified dashboard, in the toolbar, click **Save**.



## Limitations

  * Dashboard-level filters rely on filtering data by key-value pairs. These filters don't apply when the data doesn't support key-value pairs or when it doesn't support the specific key. For example, you can't use a dashboard-level filter to modify the data that a trace widget displays.

  * To apply a variable to a widget you must modify the widget's query. Not all widgets support modification.




## What's next

  * [Explore charted data](https://docs.cloud.google.com/monitoring/charts/working-with-charts)
  * [Access resource-specific dashboards](https://docs.cloud.google.com/monitoring/charts/working-with-legends#resource-dashboards)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
