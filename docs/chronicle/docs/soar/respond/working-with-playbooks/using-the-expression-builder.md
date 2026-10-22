---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder/
title: Build logic with the Expression Builder \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:15.231088+00:00
---

# Build logic with the Expression Builder  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-the-expression-builder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build logic with the Expression Builder

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

The Expression Builder lets you parse and modify JSON results, for use in subsequent actions. The Expression Builder generates various dynamic transformation functions that you can chain together, preview, and test, providing an interactive experience for transforming and parsing raw action results. 

After selecting a placeholder for the parameter in the playbook action, you can use the JSON results. These results give you comprehensive information returned by the action, which you can use in subsequent playbook actions and flow. For details, see [Use Cases for Expression Builder](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/use-cases-for-expression-builder). 

**Note:** Some characters in the Expression Builder, like slash (/), backslash (\\) or quotation marks ("), require an escape character, like a backslash (\\) before them to return results. For example: `replace("\/","y") `

##  View the Expression Builder 

This example demonstrates potential data and doesn't reflect real-time results. The actual data may differ and might contain more or fewer fields. If an analyst knows of additional fields that will be returned at runtime, they can enter the corresponding key path in the **syntax** field.

### Functions

The following pipe functions are supported:

  * **First (x)** : Returns the first X elements of an array.  
Example: `alerts | First(2)` (If `alerts` is `[{"id": "A"}, {"id": "B"}, {"id": "C"}]`, returns `[{"id": "A"}, {"id": "B"}]`)
  * **Last (x)** : Returns the last X elements of an array.  
Example: `alerts | Last(1)` (If `alerts` is `[{"id": "A"}, {"id": "B"}, {"id": "C"}]`, returns `[{"id": "C"}]`)
  * **Min (KeyPath)** : Returns the item with the minimum value from an array. If a keyPath parameter is provided, it returns the object with the minimum value at the specified path.  
Example: `alerts | Min("score")` (If `alerts` contains list of objects with a `score` field, returns the object with the lowest score)
  * **Max (KeyPath)** : Returns the item with the maximum value from an array. If a keyPath parameter is provided, it returns the object with the maximum value at the specified path.  
Example: `alerts | Max("score")` (If `alerts` contains list of objects with a `score` field, returns the object with the highest score)
  * **Filter (ConditionKey, Operator, Value)** : Filters an array of objects, returning only the objects that match a condition on a specified field.
    * **ConditionKey** : The field in each object to evaluate against the condition.
    * **Operator** : Operator to use for the condition.
      * For string input: `=`, `!=`, `in`, `not in`.
      * For number/date input: `=`, `!=`, `>`, `>=`, ` < `, `<=`.
  * **Value** : Value to check in condition.  
Example: `alerts | Filter("severity", "=", "HIGH")` (Returns all alerts where the `severity` field is "HIGH")
  * **dateFormat ("pattern")** \- Formats a date string. Use the pattern parameter to describe the format of your input date string. The function standardizes the date to the following format: `YYYY-MM-DD hh:mm:ss`.  
Example: `timestamp_field | dateFormat("yyyy/MM/ddTHH:mm:ss")` (If `timestamp_field` is "2024/07/20T10:00:00Z", returns "2024-07-20 10:00:00") 

**Supported pattern tokens:**

    * **Year:** `yyyy` (4 digits), `yy` (2 digits), `y` (1 or 2 digits).
    * **Month:** `MM` (01-12), `M` (1-12), `MMMM` (full name), `MMM` (abbreviated).
    * **Day:** `dd` (01-31), `d` (1-31), `dddd` (full day name), `ddd` (abbreviated).
    * **Hour:** `HH` (24-hour, 00-23), `H` (24-hour, 0-23), `hh` (12-hour, 01-12), `h` (12-hour, 1-12).
    * **Minute:** `mm` (00-59), `m` (0-59).
    * **Second:** `ss` (00-59), `s` (0-59).
    * **Fractional seconds:** `fff` or `FFF`.
    * **Time Zone:** `zzz` (for example, `-08:00`), `zz`, `z`.
    * **AM/PM:** `tt` (AM/PM), `t` (A/P).
  * **Count ()** : Returns the number of items in the input array.  
Example: `alerts | Count()` (If `alerts` is an array with 4 elements, returns 4) 
  * **OrderBy ("keyPath", "direction")** : Orders an array of objects based on the values of a specified key path.  
Example: `alerts | OrderBy("score", "DESC")` (Orders the `alerts` array by `score` in descending order) 
  * **toLower ()** : Convert an input to lowercase characters.  
Example: `status_field | toLower()` (If `status_field` is "OPEN", returns "open") 
  * **toUpper ()** : Convert an input to uppercase characters.  
Example: `severity_field | toUpper()` (If `severity_field` is "high", returns "HIGH") 
  * **Replace ("x", "y")** : Replaces a substring within a string with another string.  
Example: `message_field | Replace("World", "Universe")` (If `message_field` is "Hello World", returns "Hello Universe") 
  * **Distinct ()** : Removes duplicate values from an array. For arrays of objects, performs a deep comparison to identify duplicated objects.  
Example: `[10, 20, 30, 20, 40] | Distinct()` (Returns `[10, 20, 30, 40]`) 
  * **getByIndex ("index")** : Get items of an array by a specified index or a list of indexes.  
Example: `alerts | getByIndex("0")` (Returns the first element of the `alerts` array)  
Example: `alerts | getByIndex("0,2")` (Returns the first and third elements of the `alerts` array) 
  * **split ("delimiter")** : Divides a string into an array of substrings, using a specified delimiter.  
Example: `"tag1,tag2,tag3" | split(",")` (Returns `["tag1", "tag2", "tag3"]`) 
  * **join ("delimiter")** : Concatenates an array of strings into a single string, using a specified delimiter.  
Example: `["malware", "critical"] | join(" & ")` (Returns "malware & critical") 
  * **trim ()** : Removes leading and trailing whitespaces from a string.  
Example: `" hello world " | trim()` (Returns "hello world") 
  * **trimChars ("characters")** : Removes specified characters from the beginning and end of a string. Leading and trailing whitespaces are always removed, even if not explicitly specified.  
Example: `"--TEST--ABC--" | trimChars("-")` (Returns "TEST--ABC") 
  * **substring (start, end)** : Extracts a substring from a string, using a specified start index and an optional end index.  
Example: `"Hello World" | substring(0, 5)` (Returns "Hello")  
Example: `"Hello World" | substring(6)` (Returns "World") 
  * **incrementValue (value)** : Increases a numeric value by a specified amount. If no amount is specified, the value is incremented by 1.  
Example: `score_field | incrementValue(5)` (If `score_field` is 90, returns 95)  
Example: `counter_field | incrementValue()` (If `counter_field` is 10, returns 11) 
  * **setIfEmpty ("defaultValue")** : Returns the provided default value if the input value is empty.  
Example: `optional_field | setIfEmpty("N/A")` (If `optional_field` is empty, returns "N/A"; otherwise, returns the value of `optional_field`) 
  * **toUnixtime ()** : Converts a human-readable date and time string (e.g. "2014/03/12T13:37:27Z" or "2014-03-12T13:37:27+01:00") to a Unix timestamp, expressed in UTC.  
Example: `"2024-07-20T10:00:00Z" | toUnixtime()` (Returns 1721469600) 
  * **ifThenElse ("operator", "comparedValue", "trueResult", "falseResult")** \- Evaluates a condition and returns the first expression if true, otherwise returns the second expression.  
Example: `severity_field | ifThenElse("=", "HIGH", "High Priority", "Normal Priority")` (If `severity_field` is "HIGH", returns "High Priority"; otherwise, returns "Normal Priority")  
Example: `score_field | ifThenElse(">", "70", "Above Threshold", "Below Threshold")` (If `score_field` is 90, returns "Above Threshold"; if `score_field` is 60, returns "Below Threshold") 

**Note:** For more advanced use cases, such as parsing entity lists, use the [Template Engine](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-and-integrations/power-ups/templateengine) power-up. 

### Expression

The Expression field is where you insert the JSON results together with the functions and pipes to add several functions together and build the expression. 

### Run / Results

After filling in the Expression Builder, click **Run** to display the Results based on the JSON Sample Data displayed in the Expression Builder. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
