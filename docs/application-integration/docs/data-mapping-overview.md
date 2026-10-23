---
url: https://docs.cloud.google.com/application-integration/docs/data-mapping-overview/
title: Data mapping \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:14.739364+00:00
---

# Data mapping  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/data-mapping-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data mapping

Enterprise data might reside in various sources and formats, making it difficult to integrate them into a unified data model or data pipeline. Data mapping is the process of extracting and standardizing data from multiple sources in order to establish a relationship between them and the related target data fields in the destination. Some examples of using data mapping in an integration include the following: 

  * Extracting fields from a complex data structure such as a JSON.
  * Mapping data source to the target schema.
  * Transforming data by appling transform functions.
  * Generating output values and storing/using them as integration variables.



Application Integration lets you perform data mapping using the following [tasks](https://docs.cloud.google.com/application-integration/docs/task-overview):

  * Data Transformer task ([Preview](https://cloud.google.com/terms/service-terms#1))
  * Data Mapping task



## Data Transformer task

**Preview — Data Transformer task**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [Data Transformer](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task) task is a template engine-based data mapping feature available in Application Integration. It uses Google's [Jsonnet](https://jsonnet.org/) configuration language to create and edit Jsonnet templates that define the mapping relationships for specified source and target integration variables in your integration. The **Data Transformer** task also provides a visual mapping canvas (Diagram mode) to perform data assignments and mappings in your integrations.

### Diagram mode

The _Diagram mode_ provides a visual canvas containing the following integration elements: 

  * **Input**. Displays the input variables of the data transformation. The source can be variables or constants. To assign an input variable, you can either select an existing variable or create a new variable. These variables are mapped with the related output variables by clicking the input element and dragging the line to map with the related output variable. 
  * **Output**. Displays the output variables of the data transformation. Target variables can be used for mapping in subsequent input rows. To assign an output variable, you can either select an existing variable or create a new variable.
  * **Canvas**. The canvas is used to visually map the input and output variables.



For more information about variables in Application Integration, see [Using variables in Application Integration](https://docs.cloud.google.com/application-integration/docs/variables). 

The following image shows the sample layout of the _Data Transformer diagram mode_ : 

![image showing data transformer diagram mode](https://docs.cloud.google.com/static/application-integration/images/data-transformer-diagram-mapping.png)![image showing data transformer diagram mode](https://docs.cloud.google.com/static/application-integration/images/data-transformer-diagram-mapping.png)

#### Transformation operations

You can use the predefined [transformation operations](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference) to transform and standardize mapping data in your integration. Transformation operations can have one or more input parameters, where each parameter can hold a literal value or a variable. You can use multiple mapping functions for a single input source, forming a mapping transform expression.

The end data type of an input source is based on the return type of the transform expression defined in the respective data mapping input row.

### Script mode

Using the **Data Transformer Script editor** and the supported [Data Transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference) you can write custom data mapping logic, perform variable assignments, and add or modify integration variables. 

The following image shows the sample layout of the **Data Transformer Script editor** : 

![image showing data-transformer script editor](https://docs.cloud.google.com/static/application-integration/images/data-transformer-script.png)![image showing data-transformer script editor](https://docs.cloud.google.com/static/application-integration/images/data-transformer-script.png)

For information about how to add and configure the **Data Transformer** task, see [Data Transformer task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task). 

## Data Mapping task

The **Data Mapping** task is a no-code low-code feature in Application Integration that provides a visual mapping canvas–Data Mapping editor–to perform data assignments and mappings in your integrations. In addition, you can also use the supported mapping functions to further transform your data into meaningful variables/formats to make them accessible to the other tasks or triggers in your integration. 

With the **Data Mapping** task, you can: 

  * Use the Data Mapping editor to visualize and define variable mapping for single or nested variables. 
  * Transform variables from one data type to another data type. The **Data Mapping** task lets you apply multiple mapping functions (including nested functions) to transform the variable data. 

For information about how to add and configure the **Data Mapping** task, see [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task). 

### Data Mapping editor and layout

The **Data Mapping editor** provides a visual canvas containing the following integration elements: 

  * **Variables** pane: Displays the different types of variables that are available to the integration: 
    * **Inputs**. Input variables of the integration.
    * **Outputs**. Output variables of the integration.
    * **Local Variables**. Variables that exist within the scope of the integration.

If no variables are listed, click **Add +** to configure a new variable. 

Click chevron_right **(Expand)** to expand each variable and view the available subfields of that variable. To search for any variable or its subfield from the available variable list, click search **(Search variables)**. 

For more information about variables in Application Integration, see [Variables](https://docs.cloud.google.com/application-integration/docs/variables). 

  * **Input** column: Displays input mapping rows containing the source of the data mapping input. Source can be a literal value, a base function, or an input variable, with mapping functions. Click **Variable or Value** in an input mapping row to add a source. **Tip:** To add an input variable,you can directly drag and drop a variable from the **Variables** column to the **Input** column. 
  * **Output** column: Displays the output mapping rows containing the related target variables for the respective input mapping row. Target variables can be used for mapping in subsequent input rows. To assign an output variable, you can either create a new variable or directly drag and drop an existing output variable from the **Variables** column. 

The following image shows the sample layout of the **Data Mapping editor** : 

![image showing data mapping editor](https://docs.cloud.google.com/static/application-integration/images/example-data-transform.png)![image showing data mapping editor](https://docs.cloud.google.com/static/application-integration/images/example-data-transform.png)

### Mapping functions

The **Data Mapping** task provides various predefined [mapping functions](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference) to transform and standardize the mapping data in your integration. A mapping function can have one or more input parameters, wherein each parameter can further hold a literal value, a variable, or a base function with mapping functions applied. You can use multiple mapping functions for a single input source, forming a mapping transform expression.

The end data type of an input source is based on the return type of the transform expression defined in the respective data mapping input row. The **Data Mapping editor** displays a validation error  error  under the respective data mapping input row if the return type of the input source doesn't match the return type of the corresponding output mapping target variable.

### Transform expression

A transform expression is a combination of several [mapping functions](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference) that are either chained together in-series or in a nested structure. Using the **Data Mapping editor** , you can easily insert, modify, or remove a function or a function parameter in a defined transform expression. If the defined transform expression is invalid, the **Data Mapping editor** displays a validation error  error  next to the respective function or function parameter that is causing the error in the expression. To view the complete error message, hold the pointer over the validation error  error  icon.

The following image shows a sample mapping with validation errors in the **Data Mapping editor** : 

![image showing data mapping validation error](https://docs.cloud.google.com/static/application-integration/images/data_mapping_error.png)![image showing data mapping validation error](https://docs.cloud.google.com/static/application-integration/images/data_mapping_error.png)

For more information about how to configure a mapping in a **Data Mapping** task, see [Add a mapping](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task#add-map).

For information about the supported pre-defined mapping functions in Application Integration, see [Supported data types and mapping functions](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference). 

### Mapping order

Mappings specified in the **Data Mapping editor** are run in sequence from top to bottom. For example, in the preceding image, `Num1` is mapped to `Num1ToInt` in the first row, making `Num1ToInt` available for mapping in the subsequent rows. 

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Add and configure a [Data Transformer task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task) ([Preview](https://cloud.google.com/terms/service-terms#1))
  * Learn about [Data Transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference) ([Preview](https://cloud.google.com/terms/service-terms#1))
  * Add and configure a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/data-mapping-task)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
