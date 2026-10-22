---
url: https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task/
title: Data Transformer task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:42.082296+00:00
---

# Data Transformer task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data Transformer task

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Data Transformer** task provides two modes– _Diagram and Script_ –to transform your data. In the _Diagram_ mode, you use a visual mapping canvas, called the Data Transformer editor, to perform data assignments and mappings in your integration. In addition, you can also use the supported transformations to transform your data into meaningful variables and formats to make them accessible to other tasks or triggers in your integration. In the _Script_ mode, you can write, edit, and evaluate custom [Jsonnet](https://jsonnet.org/) templates to perform data mapping in your integration. 

For information about data mapping in Application Integration, see [Data mapping overview](https://docs.cloud.google.com/application-integration/docs/data-mapping-overview). 

## Configure the Data Transformer task

To add a **Data Transformer** task to your integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**. The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Tasks** to view the list of available tasks and connectors. 
  5. Click and place the **Data Transformer** element in the integration editor.
  6. Click the **Data Transformer** element to view the task configuration pane.
  7. Click **Open Data Transformer editor**. In the **Data Transformer (preview) Task Editor** page, select one of the following options:
     * By default, the **Diagram** mode opens. The **Diagram** mode provides a console-based experience to select the input and output variables and perform transformations in the data transformation editor. 

In the **Diagram** mode, you can visually perform data mapping between input and output variables.

     * To perform data transformations in your integration by writing, editing, and evaluating custom [Jsonnet](https://jsonnet.org/) templates, go to the script mode by clicking **Script**. You can use the **Script** mode if you have complex data transformation requirements and if you want to leverage Jsonnet functions. 

The **Data Transformer editor** appears displaying a default commented Jsonnet template example. Write your Jsonnet code and close the editor once complete. Any changes will be autosaved.

For detailed steps about adding a mapping, see Add a mapping.




## Add a mapping

To add a mapping, you can either use the _Diagram_ mode or the _Script_ mode.

### Use the Diagram mode

The **Diagram** mode provides a console-based experience to select the input and output variables and perform transformations in the data transformation editor. To add mapping using the **Diagram** mode, follow these steps:

  1. In the Data Transformer task configuration pane, click **Open Data Transformer Editor**. 

By default, the **Diagram** mode is open. 

![image showing the diagram mode](https://docs.cloud.google.com/static/application-integration/images/data-transformer-diagram-mode.png)![image showing the diagram mode](https://docs.cloud.google.com/static/application-integration/images/data-transformer-diagram-mode.png)

  2. To add the input variable for mapping, click **\+ Add input**. The **Choose Input Variable or Value** dialog appears. The **Variable** tab is selected by default. **_Input_** : Source of the data transformation input. Source can be a literal value, a base function, or an input variable, with mapping functions. 

![image showing the add input dialog](https://docs.cloud.google.com/static/application-integration/images/data-transformer-input-variable.png)![image showing the add input dialog](https://docs.cloud.google.com/static/application-integration/images/data-transformer-input-variable.png)

Then, do the following:

     1. From the **Select Variable(s)** list, select the input variable(s). If you want to [create a new variable](https://docs.cloud.google.com/application-integration/docs/variables#create-a-variable), click **\+ Add New Variable**.
     2. Click **Submit**.

Optionally, if you want to add a constant, click the **Constant** tab.

Unlike variables, constants are not accessible to other tasks or triggers in your integration and are only limited to be used in the **Data Transformation** task where these are created. For example, you can use constants to add delimiters or to map a constant value to a variable.

![image showing the add constant dialog](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-constant.png)![image showing the add constant dialog](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-constant.png)

Then, do the following:

     1. In the **Constant identifier** field, enter the name of the constant.
     2. From the **Data Type** list, select from one of the following data types: 
        * **String**
        * **Boolean**
        * **Number**
     3. In the **Enter the constant value** field, enter the value.
     4. Click **Submit**.
  3. To add the output variable for mapping, click **\+ Add Output** and select the output variable or [create a new variable](https://docs.cloud.google.com/application-integration/docs/variables#create-a-variable). 

![image showing the add output dialog](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-output.png)![image showing the add output dialog](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-output.png)

  4. Configure the mapping: 
     1. Add a mapping from a variable or its subfield from the **Variables** list in the **Input** section to the variable or its subfield from the **Variables** list in the **Output** section. 

![image showing data-transformer diagram mode](https://docs.cloud.google.com/static/application-integration/images/data-transformer-diagram-mapping.png)![image showing data-transformer diagram mode](https://docs.cloud.google.com/static/application-integration/images/data-diagram-script.png)

     2. To add a transformation function, hover over the mapping line and click settings to add the data transformation function. The **Transformation** button appears on the canvas. 

Alternatively, you can click settings **Add transformation** to add the transformation function.

Then, do the following:

        1. To add the transformation, click the **Transformation** button. The **Transformation** panel appears. 

![image showing data transformation](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-transformation.png)![image showing data transformation](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-transformation.png)

Then, do the following:

           1. Click **\+ Add Operation**. The **Add Operation** dialog appears. 

![image showing data transformation operations](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-operation.png)![image showing data transformation operations](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-operation.png)

           2. In the **Search operations** field, enter the operation that you want to add. Alternatively, you can select the operation from the list of operations. 

If you want to add a custom operation, select **Function expression** and enter the function expression. To copy the variables, click content_copy from the **Variables** list and paste it in the expression editor.

![image showing function expression](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-function-expression.png)![image showing function expression ](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-function-expression.png)

           3. Click **Done**.
        2. Based on the operation, fill the required details. Optionally, you can add multiple operations in a transformation. If you want to choose the result of the previous operation in the succeeding operation, select the **Previous Operation Result** variable as shown in the following image: 

![image showing multiple transformation operations](https://docs.cloud.google.com/static/application-integration/images/data-transformer-multiple-operations.png)![image showing multiple transformation operations](https://docs.cloud.google.com/static/application-integration/images/data-transformer-multiple-operations.png)

        3. To remove the operation, click  delete  **Delete** next to the operation.
     3. Optionally, you can add mapping from multiple input variables to a transformation function. However, only one mapping can be added for each output variable from a transformation function.
     4. To remove the input and output variables, click  more_vert > **Delete**.
     5. Optionally, to delete a mapping row or a transformation, select the mapping and press **Delete**.
     6. Close the **Data Mapping Editor** once your mapping is complete. Any changes will be autosaved.

#### Example: Mapping an old bug ticketing system to a new ticket system

Suppose you have a legacy bug ticketing system that you want to migrate to a new ticket system. You can use the **Diagram** option to map the fields from the old to the new system as shown in the following image:

![image showing data-transformer diagram mode](https://docs.cloud.google.com/static/application-integration/images/data-transformer-diagram-mapping.png)![image showing data-transformer diagram mode](https://docs.cloud.google.com/static/application-integration/images/data-diagram-script.png)

To add a constant value for one of the fields, click **Add input** and add a new constant. You can map the newly added constant from the _Input_ section to the field in the _Output_ section.

![image showing data-transformer adding constant](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-input.png)![image showing data-transformer adding constant](https://docs.cloud.google.com/static/application-integration/images/data-add-input.png)

To add the transformation for fields that cannot be mapped directly, click settings **Transformation** and add the transformation operation by clicking **\+ Add operation** :

![image showing data-transformer adding transformation](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-transformation.png)![image showing data-transformer adding transformation](https://docs.cloud.google.com/static/application-integration/images/data-transformer-add-transformation.png)

After the transformation is complete, you can execute the integration to map the old ticketing system to the new system.

### Use the Script mode

You can use the **Data Transformer Script editor** to access the integration variables, perform variable assignments, and add or modify variables in your integration. The **Data Transformer Script editor** provides the following features to enrich your scripting experience: 

     * Syntax/code highlighting, indentation, and line numbering for easier code readability and structure recognition. 
     * A minimap that displays a high-level overview of the script code and helps with quick navigation. 
     * Click-to-copy option to copy the script code to the clipboard. 

To open the editor, go to the **Data Transformer Script** task configuration pane and click **Open Data Transformer Script Editor**. 

The **Data Transformer Script editor** by default imports `[functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference)`, a predefined custom library containing a set of Jsonnet functions for data mapping in Application Integration. For details of the available custom functions, see [Data Transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference). 

The following image shows the sample layout of the **Data Transformer Script editor** :

![image showing data-transformer script editor](https://docs.cloud.google.com/static/application-integration/images/data-transformer-script.png)![image showing data-transformer script editor](https://docs.cloud.google.com/static/application-integration/images/data-transformer-script.png)

#### Access integration variables

To read an existing integration variable from the **Data Transformer Script editor** use the `**extVar**` function from the predefined `[functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference)` library. 

**Caution:** Jsonnet doesn't allow using hyphens (-) as part of an identifier name. For example, a variable name or a function name. If you want to use a hyphen (-) as part of a variable name, the variable must be declared within double quotes as shown in the following example.

#### Example: Read and update existing integration variables using the Data Transformer Script editor.

### Jsonnet script
    
    local f = import "functions"; // Import predefined Data Transformer function library
    
    local str1 = f.extVar("inputVar1"); // Access integration input variable "Inputstr1" with value "Hello"
    local str2 = f.extVar("inputVar2"); // Access integration input variable "Inputstr2" with value "World"
    {
      OutputVar: str1 + " " + str2 + "!", // Write to Jsonnet output variable "OutputVar"
      "output-str-var": str1 + " Integration " + str2 + "!", // Write to Jsonnet output variable "output-str-var"
    }

### Output

![image showing data-transformer script example](https://docs.cloud.google.com/static/application-integration/images/data-transformer-script-example.png)![image showing data-transformer script example](https://docs.cloud.google.com/static/application-integration/images/data-transformer-script-example.png)

## Jsonnet usage reference

Jsonnet is a purely functional language and its programs are composed of expressions. For information about how to form these expressions, see [Jsonnet Expressions](https://jsonnet.org/ref/language.html#expressions).

## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## Quotas and limits

For information about the usage limits that apply to the **Data Transformer** task, see [ Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits). 

## What's next

     * Learn about the following: 
       * [All tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
       * [Data Transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference) ([Preview](https://cloud.google.com/terms/service-terms#1))
       * [Testing and publishing integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
       * [Error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
     * [Integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
