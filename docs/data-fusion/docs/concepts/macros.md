---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/macros/
title: Macros and macro functions \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:06.312603+00:00
---

# Macros and macro functions  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/macros/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Macros and macro functions Stay organized with collections  Save and categorize content based on your preferences. 

Macros are placeholders within the Cloud Data Fusion plugin property configurations. They're represented by variables enclosed within `${ }`, such as `${input_file_path}`. To enable dynamic configuration for elements, such as file paths and table names, the placeholders are replaced with actual values at runtime.

When viewing a plugin's properties, you can add a macro to any property field that has an **M** next to it. To add the macro, click the **M**.

For more information, see [Manage macros, preferences, and runtime arguments](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-macros-prefs-and-runtime-args).

## Macro functions

In addition to macros, you can use the following predefined macro functions:

  * `logicalStartTime()`
  * `secure()`



### Logical Start Time function

The `logicalStartTime()` macro function returns the logical start time of a run of the pipeline as a string value.

If no parameters are supplied, it returns the start time in milliseconds. All parameters are optional. The function takes a time format, an offset, and a timezone as arguments and uses the logical start time of a pipeline to perform the substitution:
    
    
    ${logicalStartTime([timeFormat[,offset [,timezone])}
    

The following list shows the optional parameters for `logicalStartTime()`:

Parameter | Description  
---|---  
`timeFormat` | The time format pattern, in the format of a Java [ `SimpleDateFormat`](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html).  
`offset` |   
Time offset before the logical start time.  
`timezone` |   
Timezone to be used for the logical start time.  
  
**Example**

In this example, the logical start time of a pipeline run is `2020-01-01T00:00:00` and you provide the following macro:
    
    
    ${logicalStartTime(yyyy-MM-dd'T'HH-mm-ss,1d-4h+30m)}
    

The format is `yyyy-MM-dd'T'HH-mm-ss` and the offset is `1d-4h+30m` before the logical start time. At runtime, the macro value is replaced with `2019-12-31T03:30:00` because the offset translates to 20.5 hours. The entire macro evaluates to 20.5 hours before midnight of January 1, 2020.

**Note:** `logicalStartTime` is case sensitive. For example, if you enter `${logicalstarttime()}`, the pipeline fails. You must type `${logicalStartTime()}`.

### Using `logicalStartTime()` in file-based plugins

The most common way to use this function is in the **Path** field in file-based plugins.

#### Including the pipeline start time in milliseconds in a filename

To capture the actual start time in milliseconds in a filename, omit parameters in the macro function.

**Example**

In this example, you include the pipeline start time, in milliseconds, in an Amazon S3 filename:
    
    
    sales_012345671011.csv
    

In the Amazon S3 sink properties, enter the following value in the **Path** field:
    
    
    s3a://sales-data/sales_${logicalStartTime()}.csv
    

#### Including the today's date in a filename

You can use the `logicalStartTime()` macro function in a filename to capture the current date.

**Example**

In this example, you capture today's date in the following S3 filename:
    
    
    s3a://sales-data/sales_20210204.csv
    

In the Amazon S3 sink properties, enter the following value in the **Path** field:
    
    
    s3a://sales-data/sales_${logicalStartTime(yyyyMMdd)}.csv
    

### Using `logicalStartTime` to add a Timestamp field to structured records

You can add timestamp to a structured record using the **Add Field** transformation and `logicalStartTime()`.

  1. Get the **Field Adder Transform** plugin from Cloud Data Fusion Hub. After you deploy the plugin, it appears in the **Transform** list as **Add Field**.
  2. When you configure the plugin properties, add the timestamp to a structured record—for example, for the field name, enter the name of the new field and for the field value, enter the `logicalStartTime()` macro function.



### Secure function

The `secure()` macro function takes in a single key as an argument and looks up the key's associated string value from the [Secure Store](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/480347053). To perform the substitution, the [key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/801767425) provided as an argument must already exist in the Secure Store. This is useful for performing a substitution with sensitive data.

**Example**

In this example, for a plugin that connects to a MySQL database, you configure the password property field with the following value:
    
    
    ${secure(password)}
    

This macro pulls the password from the Secure Store at runtime.

## Recursive macros

Macros can recursively refer to other macros up to ten levels. Macro arguments are evaluated from the innermost to the outermost argument.

**Example**

In this example, you have a server that refers to a hostname and a port. You supply the following runtime arguments, the last of which is a macro that refers to other macros:

  * **hostname** : `examplepetstore.com`
  * **port** : `9991`
  * **server-address** : `${hostname}:${port}`



In a pipeline configuration, you use the following expression:
    
    
    server-address: ${server-address}
    

At runtime, it's replaced with the following value:
    
    
    examplepetstore.com:9991
    

## What's next

  * Learn more about [macros, preferences, and runtime arguments](https://docs.cloud.google.com/data-fusion/docs/how-to/manage-macros-prefs-and-runtime-args).

  * Learn how to use [plugin templates](https://docs.cloud.google.com/data-fusion/docs/how-to/create-plugin-templates).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
