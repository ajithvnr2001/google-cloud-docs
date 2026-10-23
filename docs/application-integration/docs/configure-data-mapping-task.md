---
url: https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task/
title: Data Mapping task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:03.473755+00:00
---

# Data Mapping task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data Mapping task

The **Data Mapping** task lets you perform variable assignments in your integration, get and set properties of json objects, and apply nested transform functions to values. The variables can be integration variables or task variables. 

For example, you can assign values from an integration variable `X` to a task variable `Y` or from a task variable `Y` to an integration variable `X`. For more information about variables in Application Integration, see [ Using variables in Application Integration](https://docs.cloud.google.com/application-integration/docs/variables-overview). 

## Configure the Data Mapping task

To configure a **Data Mapping** task, perform the following steps: 

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
  5. Click and place the **Data Mapping** element in the integration editor.
  6. Click the **Data Mapping** element on the designer to view the **Data Mapping** task configuration pane.
  7. Click **Open Data Mapping Editor** to view the default values of the task and to add a new mapping. For detailed steps about adding a mapping, see Add a mapping. 

For more information about the data mapping editor layout, see [ Data mapping overview](https://docs.cloud.google.com/application-integration/docs/data-mapping-overview). 




## Add a mapping 

To add a mapping, perform the following steps: 

  1. In the Data Mapping task configuration pane, click **Open Data Mapping Editor**. 
  2. Configure the mapping **_Input_** : **_Input_** : Source of the data mapping input. Source can be a literal value, a base function, or an input variable, with mapping functions. 
     1. Drag a variable or its subfield from the **Variables** list into the _Input_ row. To view the available subfields of a variable, click  expand_more **(Expand)** next to that variable in the **Variables** list. 
     2. Alternatively, In the _Input_ row, click **Variable or Value** and do the following: 
        * Select **Variable** to search and use an existing variable. To create a new variable, click **\+ Add new variable** , and enter the name and data type of the new variable.
        * Select **Value** to enter a literal value of type `string`, `integer`, `double`, or `Boolean`).
        * Select **Function** to search and use a base function. 

A base function is used to retrieve or generate values during the execution of an integration. For example, generating a random UUID or retrieving the current integration region. For information about the supported base functions, see  Supported base functions. 

        * Click **Save**.
     3. Click **\+ (Add a function)** on any input variable, value, or base function in the _Input_ row to add a mapping function from the list of available mapping functions. A mapping function can have one or more parameters. Each parameter can further have a value, a variable, or a base function followed by a chain of mapping functions. 
        * To add a nested function, click **\+ (Add a function)** next to the parameter of the function. Similarly, to remove or delete the most recently added function, click **\- (Delete previous function)**. 
        * To add, remove, or change a function in-between a mapping expression, click on a function and select **Add Function** , **Remove Function** , or **Change Function** respectively from the drop-down menu.

To know more about mapping functions, see [mapping functions](https://docs.cloud.google.com/application-integration/docs/data-mapping-overview#mapping-functions).

For information about the supported mapping functions, see  Supported data types and mapping functions. 

     4. To remove a variable inside a mapping expression, click  cancel  **(Remove)** next to the variable row.
     5. To remove the entire _Input_ row, click  clear **(Clear)** on the row.
  3. Configure the mapping **_Output_** : **_Output_** : Target variable for the data mapping output. Target variables can be used for mapping in subsequent input rows. 
     1. Drag a variable from the **Variables** list into the _Output_ row. If the variable is not available, then click **create a new one** to configure the name and data type of the new variable. Optionally, you can click the output variable and select whether to use that variable as an output of the integration, or as an input to another integration. 
     2. To remove the output variable, click  clear **(Clear)**.
  4. (Optional) To delete a mapping row, click delete **(Delete this mapping)**. 
  5. Close the **Data Mapping Editor** once your mapping is complete. Any changes will be autosaved.



The completed data mapping is available to view from the **Data Mapping** task configuration pane, as shown in the following image: 

![image showing data mapping editor](https://docs.cloud.google.com/static/application-integration/images/data-map-with-int.png)![image showing data mapping editor](https://docs.cloud.google.com/static/application-integration/images/data-map-with-int.png)

## Supported data types and mapping functions

Application Integration supports the following data types for variables in the **Data Mapping** task: 

  * String and String array 
  * Integer and Integer array 
  * Double and Double array 
  * Boolean and Boolean array 
  * JSON 

The following table lists the data mapping functions available for each of the data types. Data type | Supported mapping functions  
---|---  
Boolean |  [AND](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#and-function), [EQUALS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#equals-function), [NAND](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#nand-function), [NOR](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#nor-function), [NOT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#not-function), [OR](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#or-function), [TO_JSON](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_json-function), [TO_STRING](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_string-function), [XNOR](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#xnor-function), [XOR](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#xor-function)  
Boolean array | [APPEND](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append-function), [APPEND_ALL](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append_all-function), [CONTAINS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#contains-function), [FILTER](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#filter-function), [FOR_EACH](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#foreach-function), [GET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#get-function), [REMOVE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove-function), [REMOVE_AT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove_at-function), [SET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#set-function), [SIZE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#size-function), [TO_JSON](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_json-function), [TO_SET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_set-function)  
Double |  [ADD](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#add-function), [DIVIDE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#divide-function), [CEIL](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#ceil-function), [EQUALS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#equals-function), [EXPONENT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#exponent-function), [GREATER_THAN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#greater_than-function), [GREATER_THAN_EQUAL_TO](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#greater_than-equal-to-function), [FLOOR](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#floor-function), [LESS_THAN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#less_than-function), [LESS_THAN_EQUAL_TO](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#less_than_equal_to-function), [MOD](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#mod-function), [MULTIPLY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#multiply-function), [ROUND](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#round-function), [SUBTRACT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#subtract-function), [TO_JSON](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_json-function), [TO_STRING](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_string-function)  
Double array | [APPEND](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append-function), [APPEND_ALL](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append_all-function), [AVG](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#avg-function), [CONTAINS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#contains-function), [FILTER](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#filter-function), [FOR_EACH](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#foreach-function), [GET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#get-function), [MAX](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#max-function), [MIN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#min-function), [REMOVE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove-function), [REMOVE_AT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove_at-function), [SET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#set-function), [SIZE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#size-function), [SUM](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#sum-function), [TO_JSON](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_json-function), [TO_SET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_set-function)  
Integer | [ADD](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#add-function), [DIVIDE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#divide-function), [EPOCH_TO_HUMAN_READABLE_TIME](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#epoch_to_human_readable_time-function), [EQUALS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#equals-function), [EXPONENT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#exponent-function), [GREATER_THAN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#greater_than-function), [GREATER_THAN_EQUAL_TO](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#greater_than-equal-to-function), [LESS_THAN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#less_than-function), [LESS_THAN_EQUAL_TO](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#less_than_equal_to-function), [MOD](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#mod-function), [MULTIPLY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#multiply-function), [SUBTRACT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#subtract-function), [TO_DOUBLE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_double-function), [TO_JSON](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_json-function), [TO_STRING](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_string-function)  
Integer array | [APPEND](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append-function), [APPEND_ALL](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append_all-function), [AVG](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#avg-function), [CONTAINS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#contains-function), [FILTER](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#filter-function), [FOR_EACH](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#foreach-function), [GET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#get-function), [MAX](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#max-function), [MIN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#min-function), [REMOVE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove-function), [REMOVE_AT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove_at-function), [SET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#set-function), [SIZE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#size-function), [SUM](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#sum-function), [TO_JSON](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_json-function), [TO_SET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_set-function)  
JSON | [APPEND_ELEMENT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append-element-function), [FLATTEN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#flatten-function), [FILTER](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#filter-function), [FOR_EACH](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#foreach-function), [GET_ELEMENT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#get_element-function), [GET_PROPERTY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#get_property-function), [MERGE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#merge-function), [REMOVE_PROPERTY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove_property-function), [RESOLVE_TEMPLATE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#resolve_template-function), [SET_PROPERTY, ](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#set_property-function)[SIZE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#size-function), [TO_BOOLEAN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_boolean-function), [TO_BOOLEAN_ARRAY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_boolean_array-function), [TO_DOUBLE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_double-function), [TO_DOUBLE_ARRAY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_double_array-function), [TO_INT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_int-function), [TO_INT_ARRAY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_int_array-function), [TO_STRING](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_string-function), [TO_STRING_ARRAY](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_string_array-function)  
String | [CONCAT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#concat-function), [CONTAINS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#contains-function), [DECODE_BASE64_STRING](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#decode_base64_string-function), [EQUALS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#equals-function), [EQUALS_IGNORE_CASE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#equals_ignore_case-function), [LENGTH](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#length-function), [REPLACE_ALL](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#replace_all-function), [RESOLVE_TEMPLATE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#resolve_template-function), [SPLIT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#split-function), [SUBSTRING](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#substring-function), [TO_BASE_64](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_base-64-function), [TO_BOOLEAN](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_boolean-function), [TO_DOUBLE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_double-function), [TO_INT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_int-function), [TO_JSON](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_json-function), [TO_LOWERCASE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_lowercase-function), [TO_UPPERCASE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_uppercase-function)  
String array | [APPEND](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append-function), [APPEND_ALL](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#append_all-function), [CONTAINS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#contains-function), [FILTER](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#filter-function), [FOR_EACH](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#foreach-function), [GET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#get-function), [REMOVE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove-function), [REMOVE_AT](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#remove_at-function), [SET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#set-function), [SIZE](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#size-function), [TO_JSON](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_json-function), [TO_SET](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_set-function)  
For more information about each of the data mapping functions, see [Data Mapping Functions Reference](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#mapping-funcs). 

## Supported base functions

The following table lists the data mapping base functions available: Data type | Supported base functions  
---|---  
Integer | [NOW_IN_MILLIS](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#now-in-millis-function)  
Integer array | [INT_LIST](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#int-list-function)  
String |  [GENERATE_UUID](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#uuid-function), [GET_EXECUTION_ID](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#exec-id-function), [GET_INTEGRATION_NAME](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#ip-name-function), [GET_INTEGRATION_REGION](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#ip-region-function), [GET_PROJECT_ID](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#project-id-function)  
For more information about each of the data mapping base functions, see [Data Mapping Functions Reference](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#base-funcs). 

## Best practices 

Using the **Data Mapping** task can be a powerful way to transform and pass key variables to various tasks in your integration. Here are a few tips to keep in mind as you build your integration: 

  * Mappings are run in sequence from top to bottom. That is, if input variable `A` is mapped to an output variable `B` in the first row, the variable `B` is available for mapping in the subsequent rows. 
  * In each row, the data type of the _Input_ row must match the data type of the _Output_ row. To cast between types, use transformation functions such as `TO_STRING` and `TO_INT`. 
  * There are no limitations on the length of transformation chaining. However, debugging large chained transformations can be difficult. We recommend keeping input transformations readable and splitting complex transformations into multiple mappings. 
  * If a mapping requires a fallback value, set a fallback value for the mapping. If you do not provide a fallback value, the mapping returns an error when the input value or transformation returns `null`. 
  * When deleting a variable, make sure to delete any mapping that contains it. 



For information about the usage limits that apply to the **Data Mapping** task, see [ Usage limits](https://docs.cloud.google.com/application-integration/docs/quotas#usage-limits). 

## Considerations 

For JSON variables, based on a JSON schema, Application Integration interprets the child property of the variable as a JSON type in the following cases: 

  * If the child property's type specifies null. For example: 
        
        {
          "properties": {
            "PersonID": {
              "type": [
                "double",
                "null"
              ],
              "readOnly": false
            }
          }
        }

  * If the child property's type specifies multiple data types. For example: 
        
        {
          "properties": {
            "PersonID": {
              "type": [
                "integer",
                "string",
                "number"
              ],
              "readOnly": false
            }
          }
        }




In these cases, using the data mapping functions, you must explicitly convert the child variables to the desired type. 

The following examples illustrate the various types of property declarations and show how to use the data mapping functions to get the desired type: 

### Example 1
    
    
    {
      "type": "object",
      "properties": {
        "dbIntegers": {
          "type": "array",
          "items": {
            "type": [
              "integer",
              "null"
            ]
          }
        },
        "dbBooleans": {
          "type": [
            "array"
          ],
          "items": {
            "type": "boolean"
          }
        }
      }
    }

Application Integration interprets `dbIntegers` as a JSON type, and `dbBooleans` as a BOOLEAN_ARRAY type. 

To convert `dbIntegers` use: 
    
    
    dbIntegers.[TO_INT_ARRAY()](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_int_array-function)

### Example 2
    
    
    {
      "type": "object",
      "properties": {
        "dbId": {
          "type": [
            "number",
            "null"
          ],
          "readOnly": false
        },
        "dbStatus": {
          "type": [
            "boolean",
            "null"
          ],
          "readOnly": false
        }
      }
    }

Application Integration recognises both `dbId` and `dbStatus` as JSON types, but `dbId` is a parameter that can take a single double value or a null value, and `dbStatus` is a parameter that can take a single boolean value or a null value. 

To convert `dbId` and `dbStatus` use: 
    
    
    dbId.[TO_DOUBLE()](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_double-function)
    
    
    dbStatus.[TO_BOOLEAN()](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference#to_boolean-function)

### Example 3
    
    
    {
      "type": "object",
      "properties": {
        "dbString": {
          "type": [
            "string"
          ],
          "readOnly": false
        }
      }
    }

Application Integration recognises `dbString` as a string type. 

## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn about [Data Mapping task functions](https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference)
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
