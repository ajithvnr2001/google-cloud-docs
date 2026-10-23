---
url: https://docs.cloud.google.com/looker/docs/powerbi-connector/
title: Looker\u2013Power BI Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:36.605980+00:00
---

# Looker–Power BI Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/powerbi-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker–Power BI Connector Stay organized with collections  Save and categorize content based on your preferences. 

The Looker–Power BI Connector lets you use Microsoft Power BI Desktop to connect to data from a Looker [Explore](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#explore).

The Looker–Power BI Connector is designed to be used with Power BI's [DirectQuery Mode](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand#directquery-mode).

When you use the Looker–Power BI Connector in DirectQuery mode, Power BI doesn't import or copy your data. Instead, Power BI generates a [Power Query M](https://learn.microsoft.com/en-us/powerquery-m/) expression for every visualization, filter, and DAX calculation. The Looker–Power BI Connector translates these expressions into live queries by using the Looker API.

This process relies on [Power BI query folding](https://learn.microsoft.com/en-us/power-query/query-folding-basics). If your query uses a function that the Looker–Power BI Connector doesn't support, query folding stops. When query folding stops, Power BI downloads all your data to calculate the results locally, which slows down report loading and increases network usage.

**Note:** If you instead use the Power BI [Import Mode](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand#import-mode), Power BI will run a query that includes all fields from all the views that are referenced in the Looker Explore, which could be a very large query. In addition, with the **Import** option, Looker cannot correctly evaluate the [measures](https://docs.cloud.google.com/looker/docs/glossary#measure) that are used in the Explore. See the Data modeling and modes known limitations for additional information.

## Setting up Power BI Desktop to connect to Looker

The general steps to use the Looker–Power BI Connector are as follows:

  1. Verify the requirements.
  2. Enable the connector on your Looker instance.
  3. Download and save the connector file: Each user who wants to access the Looker–Power BI Connector must download the `looker_1.4.3.mez` file and save it in a specific directory on their computer.
  4. Set up Power BI Desktop for a custom connector: Each Power BI user must configure their Power BI Desktop security settings to use a non-certified custom connector.



The sections on this page describe these steps in detail.

After you complete the steps to connect Looker with Power BI Desktop, you can [connect to Looker data from Power BI](https://docs.cloud.google.com/looker/docs/powerbi-connector#connecting_to_looker_data_from_power_bi_desktop) and publish reports in Power BI. You can optionally use Power BI service (Power BI online) to interact with your Looker reports in a web browser. You can also publish reports with Power BI service using row-level security.

**Note:** The `looker_1.4.3.mez` is a Looker product. If you have any questions or need assistance, contact [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

### Requirements

To set up the Looker–Power BI Connector, you need the following:

  * Microsoft Power BI Desktop installed on your computer.
  * A Looker user account on the Looker instance with the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission, which is required to access Explores in Looker. If you want to work with queries with more than 5,000 rows, you also need the [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permission (see Query row limits for information on downloading limits).



In addition, your Looker instance must meet the following requirements:

  * Your instance must be enabled for the **Microsoft Power BI** connector. A Looker admin must enable the [**Microsoft Power BI**](https://docs.cloud.google.com/looker/docs/bi-connectors#microsoft_power_bi) toggle on the Looker [**BI Connectors**](https://docs.cloud.google.com/looker/docs/bi-connectors) page.
  * [Looker (Google Cloud core) instances that are configured for private connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) and [customer-hosted Looker instances](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps) must meet the following requirements: 
    * The instance must be running Looker 25.16 or later.
    * Your network administrator must configure your network so that traffic from Looker–Power BI Connector can reach your Looker instance.



### Enable the connector on your Looker instance

The Looker instance you want to use with the Looker–Power BI Connector must be enabled for the **Microsoft Power BI** connector:

  * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances, BI connectors are enabled by default.
  * For Looker (original) instances, BI connectors are disabled by default.



Your Looker admin can enable BI connectors on the [BI Connectors panel](https://docs.cloud.google.com/looker/docs/bi-connectors) in the **Platform** section of the Looker **Admin** menu.

### Download and save the connector file

To download the connector file, follow these steps on the computer with Microsoft Power BI Desktop installed:

  1. To download the connector file, click the following link: [`looker_1.4.3.mez`](https://docs.cloud.google.com/looker/docs/file-downloads/looker_1.4.3.mez)
  2. When the download is completed, move the `looker_1.4.3.mez` file to the directory **[Documents]\Microsoft Power BI Desktop\Custom Connectors**. (Create the folders on your computer if they don't already exist.)

**Note:** If you were participating in the Looker–Power BI Connector Private Preview, once your instance is updated to Looker 23.10 or later, you need to download the `looker_1.4.3.mez` file and replace the earlier version of the `.mez` file that was supported for the Private Preview. The `looker_1.4.3.mez` file has improvements and bug fixes that the Private Preview version does not have.

### Setting up Power BI Desktop for a custom connector

To set up the Looker–Power BI Connector on the Power BI Desktop side, follow the [Custom connectors](https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-connector-extensibility#custom-connectors) instructions on the Microsoft Power BI website.

As it says in the instructions, under **Data Extensions** , you will select the option **(Not Recommended) Allow any extension to load without validation or warning**. Select **OK** , and then restart the Power BI Desktop.

## Connecting to Looker data from Power BI Desktop

Once you have downloaded the `looker_1.4.3.mez` connector file and set up your Power BI Desktop application for a custom connector, you can use Power BI Desktop to connect to data from your Looker instance:

  1. From the Power BI Desktop toolbar, select **Get Data > More...**
  2. In the **Get Data** dialog, enter **Looker** in the search field.
  3. In the search results, click the **Looker** entry, and then click **Connect**.
  4. In the **Connecting to a third-party service** dialog, click **Continue**.
  5. Power BI Desktop will display a Looker sign-in dialog. In the **Host** field, type in the URL of your instance. For example: `example.cloud.looker.com`.
  6. Optionally, click **Advanced Options** to expand the section and configure the following additional options:

     * Use the **Show Hidden Explores and Fields** drop-down to include Explores and fields that are configured as hidden in LookML (for more information, see the documentation for [hidden (for Explores)](https://docs.cloud.google.com/looker/docs/reference/param-explore-hidden) and [hidden (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden)): 
       * **FALSE** (default): Hidden fields are suppressed.
       * **TRUE** : Hidden fields are shown.
     * Use the **Enable Logging** drop-down to enable or disable diagnostic logs within the connector for troubleshooting purposes. See the Enabling debug logging for Power BI Desktop section for information.
  7. Select the **DirectQuery** option to create a live connection to your data on Looker.

  8. Click **OK**.

  9. In the **Looker** dialog, click **Sign in**.

  10. In the Looker login screen, sign in to your Looker instance.

  11. Power BI Desktop will return to the Looker sign-in dialog, with a message that says that you are signed in. Click **Connect**.

  12. Power BI Desktop will display a list of the Looker models that you have access to, each represented as a folder. Click the Looker model that you want to access, and then select the checkbox next to the Looker Explore that you want to load in Power BI Desktop. To see a model, you must have Looker user access or group access to a [model set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model-sets) that contains the model. To access Explores, you must have the Looker [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission.

  13. Click **Load**.




Power BI Desktop will populate its **Data** pane with the fields from your selected Explore. You can then use the Looker data from the Explore to create reports in Power BI Desktop. See Viewing Looker elements in Power BI Desktop for information on how Looker elements are displayed by the Looker–Power BI Connector.

Field names will appear in a single list in the format `ViewName.FieldName`.

## Viewing Looker elements in Power BI Desktop

After you connect to Looker data from Power BI Desktop, Power BI Desktop will populate its **Data** pane with the fields from your selected Explore.

The Looker–Power BI Connector uses the following format to display Looker fields in Power BI Desktop:

`ViewName.FieldType.FieldName`

  * The `ViewName` value is the LookML [view](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#view) where the field is defined.
  * The `FieldType` value can be one of the following types that are supported by the Looker–Power BI Connector: 
    * `dim`: Dimension, a field that represents an attribute, a fact, or a value, such as dates, names, and IDs. Dimensions often correspond to columns in your underlying data table. In LookML, dimensions are defined with the [`dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension) parameter.
    * `mea`: Measure, a field that represents measurable information about your data, such as sums, counts, averages, minimums, and maximums. In LookML, measures are defined with the [`measure`](https://docs.cloud.google.com/looker/docs/reference/param-field-measure) parameter.
    * `fil`: Filter, a filter-only field that's used only to create a filter in an Explore query; filter fields aren't included in a query's result set. In LookML, filters are defined with the [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) parameter.
    * `par`: Parameter, a field that's used only to create a filter in an Explore query; parameter fields aren't included in a query's result set. A parameter can create interactive query results, labels, URLs, and more when it's defined with the `{% parameter parameter_name %}` and `parameter_name._parameter_value` Liquid variables. In LookML, parameters are defined with the [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) parameter.
  * The `FieldName` value is the name of the field as it's displayed in the Looker Explore.



Power BI Desktop displays Looker elements just as they are displayed in the Looker Explore, with the same capitalization and word spacing. For example, if a Looker Explore displays a LookML dimension as `Created Date` from a view displayed as `Order Items`, Power BI Desktop will display this field as `Order Items.dim.Created Date`.

## Creating queries with Looker dimensions and measures

The Looker–Power BI Connector lets you use Looker [dimensions and measures](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#dimension_and_measure_fields) to create queries in Power BI Desktop.

**Note:** In the **Data** pane, Looker dimension names include `dim`, and Looker measure names include `mea` (see Viewing Looker elements in Power BI Desktop for details about how Power BI displays Looker elements).

To create a query in Power BI Desktop using Looker dimensions and measures, follow these steps:

  1. Connect to Looker data from Power BI Desktop, and wait for Power BI to populate its **Data** pane with the fields from your selected Looker Explore.
  2. In the Power BI **Data** pane, select the checkbox for each Looker dimension or measure that you want to include in the query.



As you select each dimension or measure, Power BI will update the query that is displayed in the report canvas.

## Filtering queries with Looker filters and parameters

The Looker–Power BI Connector lets you use LookML [parameters](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) and [filter-only fields](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) from a Looker Explore to add filters to your Power BI report.

**Note:** In the **Data** pane, Looker filter-only field names include `fil`, and Looker parameter names include `par` (see Viewing Looker elements in Power BI Desktop for details about how Power BI displays Looker elements).

To filter a report in Power BI Desktop using Looker parameters and filter-only fields, follow these steps:

  1. If you haven't already, connect to Looker data from Power BI Desktop and wait for Power BI to populate its **Data** pane with the fields from your selected Looker Explore.

  2. In the Power BI **Data** pane, drag the name of a parameter or a filter-only field into one of the **Add data fields here** boxes in **Filters** pane, either for **Filters on this page** or for **Filters on all pages**. See the [Power BI documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-report-add-filter?tabs=powerbi-desktop) for details on adding filters to a report in Power BI.




Note the following about using Looker parameters and filter-only fields in Power BI:

  * For filter-only fields that are configured in LookML with the [`suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions) parameter or the [`suggest_dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-dimension) parameter, Power BI will fetch the suggestion values and display them in the **Basic filtering** options in the **Filters** pane.
  * For parameters that are configured in LookML with the [`allowed_value`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter#specifying_allowed_values) attribute, Power BI will fetch all of the allowed values that are configured in LookML for the parameter and display them in the **Basic filtering** options in the **Filters** pane.

**Note:** LookML parameters support only one allowed value, so be sure to select only one of the allowed values that Power BI displays in the **Basic filtering** options.



## Using DAX with the Looker–Power BI Connector

[DAX](https://learn.microsoft.com/en-us/dax/dax-overview) (Data Analysis Expressions) is a formula language that's used in Power BI to create custom calculations.

Power BI translates DAX queries into Power Query M expressions and sends them to the Looker–Power BI Connector. The Looker–Power BI Connector then translates these M expressions into Looker API calls.

If a DAX or Power Query M function isn't supported, [query folding](https://learn.microsoft.com/en-us/power-query/query-folding-basics) stops. When this happens, Power BI retrieves the entire raw table from Looker in order to process the operation locally, which can cause significant performance degradation. See the Supported Power Query M functions section for a list of supported functions.

### Measures versus columns

Power BI provides two primary ways to create new data by using DAX: **New Measure** and **New Column**.

  * **New Measure:** Power BI calculates this dynamic value on the fly when you use it in a visualization. This model doesn't store this value. Use measures primarily for aggregating data. 
    * Example: `Total Sales = SUM('Sales'[Revenue])`
  * **New Column:** Power BI calculates this static value row by row. It updates only when the data refreshes. The model stores this value. Use columns primarily for categorizing data. 
    * Example: `Profit = 'Sales'[Revenue] - 'Sales'[Cost]`

**Note:** DAX measures and columns don't appear in the Power Query **Transform Data** window. To create a column that's visible in the **Transform Data** window, create it within the Power Query editor (for example, select **Add Column > Custom Column**).

#### Create a new measure

To create a new measure in Power BI, follow these steps:

  1. In the **Data** pane, right-click the table where you want to add the measure.
  2. Select **New measure**.
  3. In the formula bar, enter your DAX formula. Replace `Measure` with your selected measure name.



#### Create a new column

To create a new column in Power BI, follow these steps:

  1. In the **Data** pane, right-click the table where you want to add the column.
  2. Select **New column**.
  3. In the formula bar, enter your DAX formula. Replace `Column` with your selected column name.



### DAX query examples

The following tables provide examples of DAX queries for common aggregations. For more information, see the [DAX documentation](https://learn.microsoft.com/en-us/dax/).

The following table provides some examples of how to create measures for common aggregations.

**Note:** The examples in this section use the **theLook eCommerce** dataset, which is available in the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/bigquery-public-data/thelook-ecommerce).Aggregation type | Example  
---|---  
SUM | `Total Sales = SUM('The Look E-Commerce'[Order Items Ecomm.dim.Sale Price])`  
AVERAGE | `Average Sale Price = AVERAGE('The Look E-Commerce'[Order Items Ecomm.dim.Sale Price])`  
MIN | `Minimum Sale Price = MIN('The Look E-Commerce'[Order Items Ecomm.dim.Sale Price])`  
MAX | `Maximum Sale Price = MAX('The Look E-Commerce'[Order Items Ecomm.dim.Sale Price])`  
COUNT | `Order Count = COUNT('The Look E-Commerce'[Order Items Ecomm.dim.Order ID])`  
DISTINCTCOUNT | `Distinct Order Count = DISTINCTCOUNT('The Look E-Commerce'[Order Items Ecomm.dim.Order ID])`  
  
The following table shows how to perform basic arithmetic operations.

Aggregation type | Example  
---|---  
Addition | `Total Orders = [Shipped Orders] + [Pending Orders]`  
Subtraction | `Total Profit = [Total Sales] - [Total Cost]`  
Multiplication | `Total Sales with Tax = [Total Sales] * 1.05`  
Division | `Profit Margin = DIVIDE([Total Profit], [Total Sales])`  
Power | `Sales Squared = POWER([Total Sales], 2)`  
or  
`Sales Squared = [Total Sales] ^ 2`  
Square root | `Square Root of Sales = SQRT([Total Sales])`  
Modulus | `Order ID Type =`   
`IF(`  
`MOD('The Look E-Commerce'[Order Items Ecomm.dim.Order ID], 2) = 0,`  
`"Even",`  
`"Odd"`  
`)`  
Absolute value | `Absolute Profit = ABS([Total Profit])`  
  
### Supported Power Query M functions

When you use the Looker–Power BI Connector in DirectQuery mode, Power BI generates a [Power Query M](https://learn.microsoft.com/en-us/powerquery-m/) expression for every visualization, filter, and DAX calculation. The Looker–Power BI Connector translates these expressions into live queries by using the Looker API.

### Text

  * `Text.From`
  * `Text.At`
  * `Text.Combine`
  * `Text.Contains` (`Text.Contains` is case-sensitive)
  * `Text.End`
  * `Text.EndsWith`
  * `Text.Length`
  * `Text.Lower`
  * `Text.Upper`
  * `Text.Middle`
  * `Text.PositionOf`
  * `Text.Range`
  * `Text.RemoveRange`
  * `Text.Replace`
  * `Text.Start`
  * `Text.StartsWith`
  * `Text.Insert`
  * `Text.Split`
  * `Text.FromBinary`



### List and table

  * `Value.Equals` / `Value.NullableEquals`
  * `Table.RowCount`
  * `Table.First`
  * `Table.FirstN`
  * `Table.SelectRows`
  * `Table.Sort`
  * `List.Sum`
  * `List.Average`
  * `List.Max`
  * `List.Min`
  * `List.Count`
  * `List.Distinct`
  * `List.Select`
  * `List.Contains`
  * `List.AnyTrue`



### Numeric

##### Basic arithmetic

  * `Value.Add`
  * `Value.Subtract`
  * `Value.Multiply`
  * `Value.Divide`



##### Scientific and advanced math

  * `Number.Power`
  * `Number.Sqrt`
  * `Number.Exp`
  * `Number.Ln`
  * `Number.Log10`
  * `Number.Log`
  * `Number.PI`



##### Number properties

  * `Number.Sign`
  * `Number.IsEven`
  * `Number.IsOdd`
  * `Number.Abs`



##### Division and remainder

  * `Number.Mod`
  * `Number.IntegerDivide`



##### Random number generation

  * `Number.Random`
  * `Number.RandomBetween`



##### Type conversions

The connector **doesn't support** using the following numeric conversion functions within visualizations:

  * `Byte.From`
  * `Currency.From`
  * `Decimal.From`
  * `Int8.From`, `Int16.From`, `Int32.From`, `Int64.From`
  * `Number.From`, `Number.FromText`
  * `Single.From`, `Double.From`



### Numeric rounding

  * `Number.Round`
  * `Number.RoundDown`
  * `Number.RoundUp`
  * `Number.RoundTowardZero`
  * `Number.RoundAwayFromZero`

**Note:** When you use DirectQuery mode with the Looker–Power BI Connector, `Number.Round` defaults to **Round Half Up** (tie-breaking away from zero), whereas standard Power Query defaults to _Round to Even_. 

The following table shows examples for each rounding operation:

Input | `Number.Round` | `Number.RoundDown` | `Number.RoundUp` | `Number.RoundTowardZero` | `Number.RoundAwayFromZero`  
---|---|---|---|---|---  
**2.7** | 3 | 2 | 3 | 2 | 3  
**2.5** | 3 | 2 | 3 | 2 | 3  
**2.2** | 2 | 2 | 3 | 2 | 3  
**0** | 0 | 0 | 0 | 0 | 0  
**-2.2** | -2 | -3 | -2 | -2 | -3  
**-2.5** | -3 | -3 | -2 | -2 | -3  
**-2.7** | -3 | -3 | -2 | -2 | -3  
  
### Date and time

##### Getting current date and time

  * `DateTime.LocalNow`
  * `DateTime.FixedLocalNow`
  * `DateTimeZone.UtcNow`
  * `DateTimeZone.FixedUtcNow`
  * `DateTimeZone.LocalNow`
  * `DateTimeZone.FixedLocalNow`



##### Datetime type conversion

  * `DateTime.FromText`
  * `DateTimeZone.FromText`
  * `DateTime.From`
  * `DateTimeZone.From`
  * `Date.FromText`
  * `Time.ToText`



##### Date arithmetic

  * `Date.AddDays`
  * `Date.AddMonths`
  * `Date.AddYears`



##### Extracting date and time parts

  * `Date.Day`
  * `Date.Month`
  * `Date.Year`
  * `Time.Hour`
  * `Time.Minute`
  * `Time.Second`
  * `DateTime.Time`



##### Date and time period boundaries

  * `Date.StartOfDay`
  * `Date.StartOfYear`
  * `Date.EndOfDay`
  * `Date.EndOfYear`
  * `Time.StartOfHour`
  * `Time.EndOfHour`



### Higher-order functions

The Looker–Power BI Connector supports the following higher-order functions, provided that the Looker–Power BI Connector also supports the nested operations.

  * `Table.AddColumn`

    * **Constraint:** The Looker–Power BI Connector must support the function that's defined in the `columnGenerator` parameter.
    * **Example:** The following query works because the Looker–Power BI Connector supports the nested function `Text.Length`: `powerquery Table.AddColumn(LookerTable, "NewColumnName", each Text.Length([lookerTextDimensionColumn]))`
  * `Table.Group`

    * **Constraint:** The Looker–Power BI Connector must support any aggregation functions that are used in the `aggregatedColumns` list.
    * **Example:** The following query works because the Looker–Power BI Connector supports the nested function `List.Sum`: `powerquery Table.Group(LookerTable, "CustomerID", {"total", each List.Sum([price])})`



## Using Looker measures in Power BI in DirectQuery mode

Many Power BI visualizations that use column, bar, and line charts require an aggregated value on the Y-axis. Power BI needs a single value to determine where to plot the data point, such as the height of a column or the position of a line. Without an aggregation, the visualization won't render.

For example, here is the visualization of a Looker measure of [`type: sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) that shows the total cost per item:

![Looker visualization of total cost per item](https://docs.cloud.google.com/static/looker/docs/images/powerbi_sumsample_looker.png)

Power BI won't display a [`type: sum`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum) measure in most visualizations unless you apply an aggregation. To display the sum, you can set the Power BI aggregation to **Sum**. Here is the resulting visualization in Power BI using a sum aggregation:

![Power BI's Sum visualization](https://docs.cloud.google.com/static/looker/docs/images/powerbi_sumsample_powerbi.png)

Similarly, you can use Power BI's sum aggregation to visualize Looker measures that use the following types of aggregation:

  * [`average`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#average)
  * [`count`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count)
  * [`count_distinct`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#count_distinct)
  * [`min`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#min)
  * [`max`](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#max)



## Using Power BI features with the Looker–Power BI Connector

The following sections describe the Looker–Power BI Connector support for various Power BI features:

### Sparkline

Add sparklines to table or matrix visualizations. For more information, see the [Power BI sparklines documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-sparklines-tables).

### Conditional formatting

Conditional formatting can be applied to table or matrix visualizations. The Looker–Power BI Connector supports conditional formatting for numerical columns, but not for text fields. For general setup instructions, see the [Power BI documentation](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-conditional-table-formatting).

### Type conversion

The Looker–Power BI Connector doesn't support converting a column to a number or a date within a visualization. However, the connector supports converting a column to text and using that field within a visualization.

### Connect with Excel

You can load data from Looker directly into Excel for Desktop or Excel for web. For setup instructions, see the [Connect Excel to Power BI datasets](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-connect-excel-power-bi-datasets) Power BI documentation.

When using the Looker–Power BI Connector in Excel, it functions similarly to DirectQuery mode in Power BI. When the data is filtered, the connector applies the filter at the source before loading the data into Excel.

**Note:** Refreshing data in Excel updates only the data values, not the structure. Excel won't reflect changes to columns, such as additions or removals. To update the schema, refresh the Power BI semantic model, republish the report, and then reopen the Excel file.

You can connect to your data using one of the following methods in Excel:

  * Insert a PivotTable
  * Get data



#### Insert a PivotTable

To insert a PivotTable that is directly connected to the dataset, follow these steps:

  1. Select the **Insert** tab.
  2. Select **PivotTable > From Power BI**.



#### Get data

To import the data using the **Data** ribbon, follow these steps:

  1. Select the **Data** tab.
  2. Select **Get Data > From Fabric & Power Platform > From Power BI**.



## Monitoring the Looker–Power BI Connector

A Looker admin can view Looker–Power BI Connector usage using the **Query API Client Properties** group of fields in the [System Activity History Explore](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#history). An entry is created in the **History** Explore every time a new query is run.

In the **Query API Client Properties** group of fields, the **API Client Name** shows a `Power BI` value to identify Looker–Power BI Connector entries.

The following is an example of a System Activity URL that shows Power BI usage. Replace `<instance_name.looker.com>` with your instance URL.
    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=query_api_client_context.name,user.name,history.created_date,history.created_time_of_day&f[query_api_client_context.name]=Power+BI&sorts=history.created_time_of_day+desc&limit=5000
    

## Power BI service

After you [connect to Looker data from Power BI](https://docs.cloud.google.com/looker/docs/powerbi-connector#connecting_to_looker_data_from_power_bi_desktop) and publish reports in Power BI, you can optionally use [Power BI service](https://learn.microsoft.com/en-us/power-bi/fundamentals/power-bi-service-overview) (Power BI online) to interact with your Looker reports in a web browser.

You can also publish reports with Power BI service using row-level security.

**Note:** The Looker–Power BI Connector is a Looker product. If you have any questions or need assistance, contact [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

### Authentication considerations

When you publish a report to the Power BI service, the credentials that you used to create the report are embedded in the report. These credentials are reused for all users who view the report in the Power BI service.

This re-use of credentials occurs because the Microsoft Power BI connector framework doesn't support end-user single sign-on (SSO) authentication for custom connectors. To restrict data access based on the user viewing the report, use row-level security (RLS) within Power BI.

### Publishing a report with Power BI service using row-level security

After you have published reports in Power BI Desktop using the Looker–Power BI Connector, you can optionally use Power BI service to interact with the reports from a web browser.

Power BI Desktop lets you use [row-level security (RLS)](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls) to restrict data access for certain users. See the Power BI documentation for the procedures for [defining roles and rules](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls#define-roles-and-rules-in-power-bi-desktop) and [validating the roles](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls#validating-the-role-within-the-power-bi-service) within Power BI Desktop.

Once you define the roles in Power BI Desktop, you can use the roles and rules online with Power BI service.

To publish a report with Power BI service using row-level security, follow these steps:

  1. In Power BI Desktop, open your report and select the **Home** menu from the top of the window.
  2. Select the **Publish** option from the **Home** menu.
  3. Select a workspace from the drop-down menu, and then click **Select**. Power BI Desktop shows a success message that includes a link to open the report in Power BI.
  4. Click the link to open Power BI.
  5. In Power BI service, go to **Workspaces** and select the workspace where you published the report.
  6. Find the listing for your report's dataset (not the report itself).
  7. In the dataset's listing, click the three-dot **More options** menu, and then select **Security**.



Power BI will show the **Row-Level Security** window. From here, you can select the role that you created in Power BI Desktop and [add people or groups who belong to the role](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls#working-with-members) and [validate your roles in Power BI service](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-rls#validating-the-role-within-the-power-bi-service).

Now you can share the report with anyone you want, and they will see only the data that they are allowed to see, based on the roles that you created.

### Enabling debug logging for Power BI Desktop

To troubleshoot or diagnose an issue, you can enable logging for the connection between Power BI and Looker.

**Note:** Because logging may impact the performance of the connection, you should enable logging on the connection only if you are troubleshooting or diagnosing an issue.

You must enable logging for the connection and also for Power BI itself, as described in the following sections:

  * Enabling connector-level logging
  * Enabling Power BI level tracing



#### Enabling connector-level logging

To troubleshoot issues, you can enable diagnostic logging within the Looker–Power BI Connector.

When you're creating a new connection to Looker data from Power BI Desktop, enable logging by following these steps:

  1. In the Looker connection dialog, expand **Advanced Options**.
  2. Select **TRUE** from the **Enable Logging** drop-down menu.



If you have already created a connection to Looker data from Power BI Desktop, you must edit the query manually within the Power Query editor by following these steps:

  1. In Power BI Desktop, select **Transform Data**.
  2. In the **Home** ribbon, select **Advanced Editor**.
  3. Locate the line starting with `Source = Looker.DataSource`.
  4. Update the second argument of the function to include `EnableLogging=true`.
         
         Looker.DataSource("instance.looker.com", [EnableLogging=true])
         

  5. Click **Done**.




#### Enabling Power BI level tracing

In addition to enabling logging on the connection to Looker data from Power BI Desktop, you must also enable tracing from Power BI Desktop by following these steps:

  1. Select **File > Options and settings > Options**.
  2. In the **Options** dialog, select **Diagnostics**.
  3. Under **Diagnostic Options** , select **Enable tracing**.
  4. To view the log files, select **Open crash dump/traces folder**.

**Note:** You must enable tracing manually for each Power BI session.

## Things to consider

### Query row limits

Queries from the Looker–Power BI Connector will automatically include a `LIMIT 5000` statement unless the Looker user account has the [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permission. If the Looker user account has `download_without_limit`, queries from the Looker–Power BI Connector have no imposed query row limit.

### Explore filters

If the Looker Explore is defined with [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) or [`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter) LookML parameters, the filters will be applied to queries in the Looker–Power BI Connector, even though the filters won't be visible in Power BI.

### Supported dimension group timeframes

For the [`dimension_group`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group) of [`type: time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_time), only the [`date`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#date) and [`time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#time_table) timeframes are supported with the Looker–Power BI Connector. Other timeframes will be hidden.

### System Activity Explores aren't surfaced with the Looker–Power BI Connector

[System Activity Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) aren't surfaced in the Looker–Power BI Connector. Looker admins can view the System Activity Explores directly in the Looker UI.

### Type conversion limitations

When possible, it's best to set column types inside of your LookML view.

## Known limitations

Be aware of the following limitations when using the Looker–Power BI Connector:

### Data modeling and modes

  * **Numeric dimensions:** Both numeric dimensions and measures appear as measures in Power BI. To use a numeric dimension as a dimension, you must change its default summarization to [**Do not summarize**](https://learn.microsoft.com/en-us/power-bi/create-reports/service-aggregates#ways-to-aggregate-your-data) in Power BI Desktop.
  * **Import mode:** For optimal performance, use [DirectQuery Mode](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand#directquery-mode). If you are using Power BI [Import Mode](https://learn.microsoft.com/en-us/power-bi/connect-data/service-dataset-modes-understand#import-mode), note the following constraints: 
    * **Performance:** Reports that access large models might load slowly.
    * **Timeouts:** If the "Get Data" process hangs or times out, switch to DirectQuery Mode.
    * **Field restrictions:** Import Mode disables filter-only fields and parameter fields.
    * **Measure evaluation:** Import mode restricts Looker from evaluating measures within the Explore, which can impact report accuracy.



### Aggregations

Power BI applies its own aggregations to Looker measures. This can cause errors or inconsistent results, particularly in matrix visuals.

  * **Supported types:** Only use `average`, `count`, `count_distinct`, `max`, `min`, and `sum`.
  * **Unsupported types:** The connector doesn't support queries for standard deviation, variance, or alphabetical first or last string aggregations.
  * **Median performance:** Power BI calculates median locally by retrieving all values. This is slow on large datasets and may time out.



### Filtering and sorting

  * **Sorting by hidden fields:** You can't sort by a field that isn't included in the visualization. To sort by a field, add it to the visualization.
  * **Advanced filter limitations:** Due to differences between [Power Query](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query) and [Looker filter expressions](https://docs.cloud.google.com/looker/docs/filter-expressions), the following limitations apply: 
    * **Text:** Multiple text filters aren't supported.
    * **Dates:** For date and datetime fields, only `is`, `is not`, `is on or after`, and `is before` are supported.
    * Multiple number filters are supported only in the following cases: 
      * INEQUALITY AND INEQUALITY (for example, is less than AND is greater than).
      * INEQUALITY OR INEQUALITY (for example, is less than OR is greater than).
      * is OR is.
    * Multiple date and datetime filters are supported only in the following cases: 
      * `is on or after AND is before`
      * `is or is`



### Power Query functions

The following table functions aren't foldable:

  * `Table.Distinct`
  * `Table.Join`
  * `Table.NestedJoin`
  * `Table.Skip`



## Troubleshooting

The following sections describe common issues and their solutions.

### The Looker–Power BI Connector doesn't appear in Power BI's **Get Data** list

Verify that the `[Documents]\Microsoft Power BI Desktop\Custom Connectors` directory contains the `looker_1.4.3.mez` file.

  1. In Power BI Desktop, verify the security settings:
  2. Select **File > Options and settings > Options**.
  3. Select **Security**.
  4. Under **Data Extensions** , select **(Not Recommended) Allow any extension to load without validation or warning**.
  5. Click **OK**.
  6. Restart Power BI Desktop.



### Error: Field names may only include letters, numbers and underscores

In some cases, you may receive the following error message when refreshing data or applying changes:
    
    
    DataSource.Error
    Message: A LookML model issue has occurred.
    Details: Invalid field name "...". Field names may only include letters, numbers and underscores and must start with a letter or underscore for Google BigQuery Standard SQL
    

This error occurs when a column name contains spaces or special characters that aren't supported by the underlying database (such as BigQuery).

To resolve this, follow these steps:

  1. Identify the column causing the error (usually referenced in the `Details` section of the error message).
  2. Rename the column to use only letters, numbers, and underscores. 
     * Incorrect: `Custom Column Name`
     * Correct: `Custom_Column_Name`



### Error: Error fetching data for this visual

In some cases, you may receive an authentication error in Power BI that indicates an OAuth failure or a credential issue, such as `Looker database authentication required`.

If you see this error, your Looker account is missing the required OAuth credentials for the database connection. To resolve this, follow these steps:

  1. Log in to your Looker instance.
  2. Select your user profile icon, and then select **Account**.
  3. Go to the **OAuth Connection Credentials** section.
  4. Find the connection you are trying to access and select **Log In**.
  5. Return to Power BI Desktop and refresh the data.



## Looker–Power BI Connector changelog

The following sections show the updates in each version of the Looker–Power BI Connector:

  * Version 1.4.3
  * Version 1.4.2
  * Version 1.4.0
  * Version 1.3.1
  * Version 1.3.0
  * Version 1.2.0



### Version 1.4.3

Version 1.4.3 of the Looker–Power BI Connector has the following updates:

  * The connector label now includes the connector version number.
  * Added a new **Enable Logging** option to dynamically enable diagnostic logs within the connector for troubleshooting purposes.
  * Added a new **Show Hidden Explores and Fields** option. When enabled, hidden explores and fields are shown. This replaces the previous **Show Hidden Fields** option.



Version 1.4.3 of the Looker–Power BI Connector has the following bug fixes:

  * Fixed an issue where string concatenation DAX operator (`&`) was failing.
  * Fixed the issue where applying a Power BI measure onto a Looker measure would cause an error.
  * The Credential Configuration menu now shows the Looker icon again.



### Version 1.4.2

Version 1.4.2 of the Looker–Power BI Connector has the following updates:

  * The **Disable Preview Optimization** connection setting has been removed.
  * The **Show Hidden Fields** connection option has moved under the **Advanced Options** section.
  * The Beta flag has been removed; the connector no longer appears as beta in Power BI.



Version 1.4.2 of the Looker–Power BI Connector has the following bug fixes:

  * Fixed the regression error where Boolean slicers and date slicers failed in Power BI.
  * Fixed `is-not` filter not working for `dates` filter.



### Version 1.4.0

Version 1.4.0 of the Looker–Power BI Connector has the following updates:

  * Added support for Import Mode
  * Enabled data preview
  * Improved behavior when performing `SELECT *` queries
  * Improved Looker cache hit rate
  * Improved performance of filter suggestions retrieval



Version 1.4.0 of the Looker–Power BI Connector has the following bug fixes:

  * Fixed bug where Looker wouldn't detect that values had been passed for filter and parameter fields
  * Fixed bug where parameter suggested values would sometimes be missing from slicers
  * Fixed bug where Liquid variables would be ignored by LookML statements
  * Fixed bug where count distinct measure values would be inconsistent in Power BI matrix views



### Version 1.3.1

Version 1.3.1 of the Looker–Power BI Connector has the following updates:

  * Added option to show hidden fields



Version 1.3.1 of the Looker–Power BI Connector has the following bug fix:

  * Fixed bug where a visual would fail if a filter exists on both the visual and report



### Version 1.3.0

Version 1.3.0 of the Looker–Power BI Connector has the following updates:

  * Simplified datetime formatting
  * Improved detection on unsupported text expressions
  * Improved error message reporting



Version 1.3.0 of the Looker–Power BI Connector has the following bug fix:

  * Improved support for escape characters in filter values



### Version 1.2.0

Version 1.2.0 of the Looker–Power BI Connector has the following updates:

  * Parameter and filter-only fields are now supported
  * Advanced filters support for filter-only fields of type text, number, date and datetime
  * Basic filter support for filter-only field utilizing Looker suggested values



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
