---
url: https://docs.cloud.google.com/data-studio/parameters/
title: Parameters \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:46.840979+00:00
---

# Parameters  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/parameters/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Parameters Stay organized with collections  Save and categorize content based on your preferences. 

Parameters let you interact with user-provided data. For example, you can create calculated fields that include input from people who are using your report, or you can pass values back to the SQL query that is used by your data source. Using parameters makes your reports more interactive. You can also use parameters to create report templates.

## How parameters work

Parameters act like variables in a programming language. Parameters serve three primary uses:

  * You can use parameters in calculated fields to display results that are based on user input.
  * You can pass parameters back to the custom SQL query in a BigQuery data source.
  * You can pass parameters back to a community connector.



Parameters can get their data from the following places:

  * From a default value that is defined for the parameter
  * From the component properties panel
  * From a control placed on the report
  * From the link to the report



You'll find parameters at the bottom of the field lists in the report and data source editors. Parameters appear as purple fields.

### How parameters share your data in reports

Editors of your reports and data sources can access any data that is controlled by parameters. Parameters let report editors request data that differs from the default.

Before you enable parameters for your data source, be sure that you understand how changes to parameter values could affect the data in your reports. Some parameters may return only relatively "safe" data, like weather in a new locale. Other parameters, however, might allow someone to request entirely new datasets.

For example, an account number parameter or the name of a database table would potentially return data that you didn't intend to share Either of these might return a different schema, which might be incompatible with existing charts in the report.

## Create a parameter

You can create parameters in the following places:

  * A data source
  * The BigQuery Connector



### Create a parameter in a data source

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. In the upper right, click **ADD A PARAMETER**. You can also create a parameter while editing a report by selecting a component, then in the bottom right, clicking **ADD A PARAMETER**. Be sure to select a component based on the desired data source.
  3. Configure the parameter's options and default value.



> While editing a report, you can use the **+Add a parameter** link in the data panel to create a parameter in the selected data source. Parameters that are added at the report level are also added into the data source automatically and can be used by multiple reports with the same data source connection.

### Create a parameter in the BigQuery connector

You can pass parameters to a custom SQL query in the BigQuery connector. The BigQuery connector defines several standard parameters that pass the report's start and end date, and the user's email address, if available. You can also pass custom parameters. [Learn more about connecting to BigQuery](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery).

## Parameters and Community connectors

Community connector can include [overridable parameters](https://developers.google.com/looker-studio/connector/data-source-parameters), which let report editors modify their default values in a data source. If you can edit the connection for a data source built with a Community connector, you can specify which parameters report editors can change:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. In the top left, click **EDIT CONNECTION**.
  3. If the connector provides editable parameters, they appear at the bottom of the page. Connectors that allow you to define custom parameters will include instructions on the page.
  4. Use the **Allow <parameter name> to be modified in reports** checkboxes to allow or disallow editing the parameter in reports.
  5. In the top right, click **RECONNECT**.



Once you've created a data source from a community connector, changes to the parameters in that connector won't appear in the data source automatically. You'll need to reconnect the data source to see any new, removed, or changed parameters.

## Edit an existing parameter

To change the configuration of an existing parameter:

  1. Edit the data source that contains the parameter.
  2. Locate the parameter in the field list.
  3. Click the @ sign to the right of the parameter name.
  4. Make any changes, then in the bottom right, click **SAVE**.



## Configure a parameter

Use these options to configure a parameter in the data source. See the respective pages if you're using the [BigQuery connector](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery) or a [community connector](https://developers.google.com/looker-studio/connector/data-source-parameters).

**Parameter name** : you'll see this name in the lists of fields in your reports and data sources. This is also the name you'll use to refer to the parameter in a calculated field.

**Parameter ID** : set by default. The parameter ID is used internally by Data Studio to identify the parameter. Report viewers don't see it.

**Important:** Changing the Parameter ID will break components and calculated fields that include the parameter.

**Data type** : parameters can store text, numbers, or Boolean (true/false) values.

**Permitted values** : specifies the values that can be input by the user.

To specify a list of values, choose that option, then enter the acceptable value, along with an optional display name. Click **Add option** to add more items to the list.

To specify a range of permitted values, enter the minimum and maximum values for the range.

**Default value** : specify a starting value for the parameter.

## Set parameter values

You can set the value of a parameter in the following ways:

  * Set a default value for the parameter
  * Use a control to get input from users
  * Override default parameter values in a component
  * Modify parameters via the report link



### Set a default value for the parameter

You can set default values for a parameter when you create a parameter or edit a parameter.

### Use a control to get input from users

Controls are components that let people interact with a report. To store user input in a parameter, add that parameter to a control's **Control field** property:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. At the top, click ![Control icon.](https://docs.cloud.google.com/static/data-studio/images/filterlistgrey6002x48dp-2020-09-09.png)**Add a control**.
  3. Choose the type of control to add.
  4. In the **Properties** panel, select the **SETUP** tab.
  5. Add the parameter to the **Control field**.



Learn more [about controls](https://docs.cloud.google.com/data-studio/about-controls).

### Override default parameter values in a component

You can override the default values for parameters by editing individual components in the report:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a component based on a data source that includes parameters.
  3. At the bottom of the component's DATA tab, edit the default parameter values.



You can also edit parameters at the report and page level:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select **File > Report Settings** or **Page > Current Page Settings**.
  3. Edit the parameter values.



#### Parameter inheritance

Parameters follow the same rules for inheritance as filter properties. Specifically, parameters on higher precedence components override the parameters on lower precedence components. The order of precedence (from lowest to highest) is:

  1. Data source (default)
  2. Report
  3. Page
  4. Group
  5. Individual chart or control



### Modify parameters via the report link

Setting parameters via the report's URL lets developers and advanced users to construct reports that can be configured programmatically.

Data Studio report parameters and their corresponding values are passed in as URL encoded JSON strings appended to report URL using the "params" query parameter.

Learn more in the [Developer Guide](https://developers.google.com/looker-studio/connector/data-source-parameters#set_url_parameters).

#### Manage report parameters

Parameters in your reports are **not editable** via the report URL by default.

To select which parameters report users are allowed to modify:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select **Resource > Manage variables (parameters)**.
  3. In the **Allow to be modified in report URL** column check the parameters you want to allow.



This page also displays the URL parameter for each parameter. This is the name you'll use, not the Parameter name, when you construct the encoded parameter object. You can edit this name by clicking the edit pencil. Every URL parameter in a report must be unique.

Editing the URL parameter name has no effect on how the parameter is used in the report.

## Use parameters

Once created, you can use parameters in calculated fields and report components much as you would dimensions and metrics.

### Use a parameter in a calculated field

You can use a parameter just as you'd use a dimension or metric in a calculated field.

####  Calculated field with a parameter. Click to expand.

For example, say you want to visualize forecasted sales by letting someone enter a multiplier to your sales from last quarter. 

First, create the parameter to hold the forecast multiplier: 

  1. Sign in to Data Studio. 
  2. Edit your data source. 
  3. At the top right, click **ADD A PARAMETER**. 
  4. Name the parameter (for example, "Forecast multiplier"). 
  5. Set the **Data type** to **Number**. 
  6. For simplicity, leave the **Permitted values** option set to **Any value**. 

You can use the other options to let the user pick from a list of values, or you can restrict their entry to a range of values. 
  7. Set the **Default value** to 1. 
  8. Click **Save**. 
  9. To return to the data source fields list, on the left, click **ALL FIELDS**. 



Next, create the calculated field: 

  1. At the top right, click **ADD A FIELD**. 
  2. Name the field (for example, "Sales forecast with parameter"). 
  3. In the formula, multiply the "Sales" field from your data source by the `Forecast multiplier` parameter. For example, if your data source has a field called **Revenue** , enter the following: 

`Revenue * Forecast multiplier`
  4. Click **Save**. 



Next, add a control to gather the user's input: 

  1. Edit or create a report. 
  2. If necessary, add your data source to the report. 
  3. At the top, click ![Control icon.](https://docs.cloud.google.com/static/data-studio/images/filterlistgrey6002x48dp-2020-09-09.png) />**Add a control**. 
  4. Select the **Input box** control. 

The Input box control lets you type in parameter values directly. Other types of controls let you select from a list, use a slider, or toggle Boolean values with a checkbox. 
  5. On the right, in **DATA properties** , add the `Forecast multiplier` parameter that you created previously. 



Finally, visualize the parameterized calculated field in a chart. 

  1. At the top, click ![Add a chart icon.](https://docs.cloud.google.com/static/data-studio/images/addchartgrey6002x48dp-2020-08-18-icon-rge.png)**Add a chart**. 
  2. For simplicity, select a **Scorecard**. 
  3. On the right, in **DATA properties** , add the `Sales forecast with parameter` calculated field as the metric. 



Now, try it out: 

  1. At the top right, click **View**. 
  2. Enter a number in the **Forecast multiplier** control, and then press **Enter**. 
  3. You'll see the value in the scorecard change as it is multiplied by the value that you enter. 



### Use a parameter in a visualization

You can add a parameter to a chart, just as you would a dimension or metric. If you use a numeric parameter as a metric, its value is aggregated.

## Show or hide parameters in reports

You can show or hide parameters that you've created in a data source:

  1. Edit your data source.
  2. Locate the parameter.
  3. To the right of the parameter, click ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) Options.
  4. Click **Show** (if the parameter is currently hidden) or **Hide** (if the parameter is currently shown).



> Hiding a parameter removes it from the list of fields in the **Data** panel, and will break any components that use it. If the parameter is used in a calculated field, the formula uses the parameter's default value.

## Copy a component with parameters

Copying a component copies its parameter values as set in the property panel. You can override the copy's parameters by editing the component.

## Fix invalid parameters

If the parameter configuration changes in the connector, any charts using those parameters may break. For example, the connector's developer may remove the ability to override a parameter value, and the value you've provided in the report no longer returns valid data. In this case, you'll see an error message in any charts impacted by that change.

To fix this, locate the component containing the now-invalid parameter. Then, in the _Parameters_ section of that component's DATA properties, click **Fix Invalid Values**.

Remember that parameters can be set at the report, page, and group level, as well as on individual charts, so you may need to look in several places to find and fix the error.

## Related resource

[About controls](https://docs.cloud.google.com/data-studio/about-controls)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
