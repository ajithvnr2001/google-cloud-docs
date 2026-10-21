---
url: https://docs.cloud.google.com/monitoring/uptime-checks/response-validation/
title: Validate response data \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:21.288119+00:00
---

# Validate response data  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/uptime-checks/response-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Validate response data Stay organized with collections  Save and categorize content based on your preferences. 

Response validation lets you verify that a monitored resource returns both an expected HTTP status code and specific payload content during an uptime check. By default, HTTP and HTTPS uptime checks only verify that the status code is in the `2xx` range and don't inspect the body. You can customize these settings to accept additional status codes, such as `3xx`, or to check whether the payload matches specific strings, regular expressions, or JSON paths.

## How to validate the response data

You can configure Cloud Monitoring to validate the response data from a checked resource when you create or edit an uptime check.

###  Console 

To [create an uptime check](https://docs.cloud.google.com/monitoring/uptime-checks) that validates the response data, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Click **Create uptime check**.
  4. Enter a **Title** and click **Next**.
  5. Enter the **Target** and click **Next**.
  6. Configure the **Response validation** :

     * To validate the response data, ensure **Content matching is enabled** is shown, and then complete the fields related to response validation. For information about these options, see the next section of this document.
     * For the HTTP uptime checks, configure the acceptable response codes. By default, HTTP uptime checks mark any `2xx` response as a successful response.
  7. Click **Next** and complete the uptime check configuration.




###  REST 

To configure an uptime check to validate the response data, populate the `contentMatchers` array of the [`UptimeCheckConfig`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig) object.

[`ContentMatcher`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentMatcher) objects contain the following fields:

  * `matcher`: Describes how the comparison is performed. For a list of values, see [`ContentMatcherOption`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#ContentMatcherOption).

Don't use the `CONTENT_MATCHER_OPTION_UNSPECIFIED` value.

  * `content`: Stores the value to search for in the response data. The value is a string literal or a regular expression.

  * `jsonPathMatcher`: Stores a [`JsonPathMatcher`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#JsonPathMatcher) object that describes which JSONpath to search and how to perform the comparison.

Omit this field unless the uptime check is validating a specific JSONpath.




The remainder of this document describes how to use the content-matching options.

## Options to validate the response data

This section describes the string-matching strategies that you can use to validate the response sent by a checked resource. For each strategy, you specify a value and whether finding that value in the response data results in the uptime check passing or failing.

The entire response from a checked resource might not be searched:

  * HTTP and HTTPS uptime checks: The first 4 MB is searched.
  * TCP uptime checks: The first 1 MB is searched.



### Search for a literal substring

###  Console 

To configure the uptime check to pass when the response data contains a literal substring, use the following settings:

  1. Select **Contains** in the **Response content match type** menu.
  2. Enter the literal substring in the **Response content** field.
  3. To verify the configuration, click **Test**.



To configure the uptime check to fail when the response data contains a literal substring, use the following settings:

  1. Select **Does not contain** in the **Response content match type** menu.
  2. Enter the literal substring in the **Response content** field.
  3. To verify the configuration, click **Test**.



###  REST 

To configure the uptime check to pass when the response data contains a literal substring, use the following values:
    
    
    ...
    "contentMatchers": [
        {
          "content": "Set to the string to be matched.",
          "matcher": "CONTAINS_STRING"
        }
    ],
    ...
    

To configure the uptime check to fail when the response data contains a literal substring, use the following values:
    
    
    ...
    "contentMatchers": [
        {
          "content": "Set to the string to be matched.",
          "matcher": "NOT_CONTAINS_STRING"
        }
    ],
    ...
    

The following table displays the uptime check status for different response data, test strings, and test types:

|  | Uptime check status   
---|---|---  
Response data | Test string | Contains | Doesn't contain  
`abcd` | `abcd` | pass | fail  
`abc` | `abcd` | fail | pass  
`abc` | `a` | pass | fail  
`Uptime Checks` | `Uptime` | pass | fail  
`Uptime Checks` | `uptime` | fail | pass  
  
In the previous table, the **Response data** column describes the data returned by the checked resource while the **Test string** column lists the string literal. The next two columns specify the type of test and the result of the uptime check.

### Search by using a regular expression

###  Console 

To configure the uptime check to pass when the response data matches a regular expression, use the following settings:

  1. Select **Matches regex** in the **Response content match type** menu.
  2. Enter a regular expression in the **Response content** field.
  3. To verify the configuration, click **Test**.



To configure the uptime check to fail when the response data matches a regular expression, use the following settings:

  1. Select **Does not match regex** in the **Response content match type** menu.
  2. Enter a regular expression in the **Response content** field.
  3. To verify the configuration, click **Test**.



###  REST 

To configure the uptime check to pass when the response data matches a regular expression, use the following values:
    
    
    ...
    "contentMatchers": [
        {
          "content": "Set to the regular expression to be matched.",
          "matcher": "MATCHES_REGEX"
        }
    ],
    ...
    

To configure the uptime check to fail when the response data matches a regular expression, use the following values:
    
    
    ...
    "contentMatchers": [
        {
          "content": "Set to the regular expression to be matched.",
          "matcher": "NOT_MATCHES_REGEX"
        }
    ],
    ...
    

The following table displays the uptime check status for different response data, regular expressions, and test types:

|  | Uptime check status   
---|---|---  
Response data | Regex | Matches regex | Doesn't match regex  
`abcd` | `abcd` | pass | fail  
`Uptime Checks` | `[uU]ptime` | pass | fail  
`Uptime Checks` | `[a-z]{6}` | fail | pass  
`Uptime Checks` | `[a-zA-Z]{6}` | pass | fail  
  
In the previous table, the **Response data** column describes the data returned by the checked resource while the **Regex** column lists the regular expression. The next two columns specify the type of test and the result of the uptime check.

### Search a specific field in a JSON response

You can configure an uptime check to validate a JSONpath. When you select a JSONpath test, the test compares a path value to a number, a string literal, or to a regular expression:

  * Compare JSONpath to a number or string literal
  * Compare JSONpath to a regular expression



When you specify a JSONpath, you must specify the root object with `$.` and then follow that with a specific field identifier. When the JSON response contains an array of elements, use brackets, `[]`, to identify the specific array element to match. The following examples illustrate the path syntax:

  * `$.type` matches the `type` field of a root object.
  * `$.[0].address.city` matches the `city` field in the `address` object stored in the first array element of the JSON response.
  * `$.content[0].phone` matches the `phone` field of the first array element of the `content` field. The `content` field is a child of the root object.



You can configure an uptime test to match multiple fields. Consider the following JSON:
    
    
    [
      {
        ...
        "address": {
          ...
          "city": "Gwenborough",
          "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
          }
        },
      },
      ...
    ]
    

To match the entire path of the `geo` field in the first array element, set the JSONpath to `$.[0].address.geo`, and enter the complete value in the content field:
    
    
    {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
    

If you are interested in experimenting with these options, then find a public website that returns a JSON response.

#### Compare JSONpath to a number or string literal

###  Console 

**Note:** In the **Response content** field, you can enter numbers, boolean values of `true` and `false`, and strings. For a match to occur, the value you enter must match the response the uptime check receives. For example, you can enter the boolean `true`, the number `5`, or a string like `"true"`, `"5"`, or `"hello"`.

To configure the uptime check to pass when a specific JSONpath in the response data matches a string literal, use the following settings:

  1. Select **Matches at JSONPath** in the **Response content match type** menu.
  2. Enter the path in the **JSONPath** field.
  3. Enter the number or the string literal in the **Response content** field.
  4. To verify the configuration, click **Test**.



To configure the uptime check to fail when a specific JSONpath in the response data matches a string literal, use the following settings:

  1. Select **Does not match at JSONPath** in the **Response content match type** menu.
  2. Enter the path in the **JSONPath** field.
  3. Enter the number or the string literal in the **Response content** field.
  4. To verify the configuration, click **Test**.



###  REST 

**Note:** Because the value of the `"content"` field must be a string, you must wrap the value in quotes. When the value is a string, you must escape the inner quotes. For example, to match the boolean `true`, set the value to `"true"`. Similarly, to match the number `5`, set the value to `"5"`. Lastly, to match the string `"5"`, enter `"\"5\""`.

To configure the uptime check to pass when a specific field in the JSON-formatted response matches a number or a string literal, use the following values for the `ContentMatcher` object:
    
    
    ...
    "contentMatchers": [
        {
           "content" : "Set to a number, a boolean, or the string to be matched.",
           "matcher" : "MATCHES_JSON_PATH",
           "jsonPathMatcher" : {
               "jsonPath" : "Set to the JSONpath.",
               "jsonMatcher" : "EXACT_MATCH"
           }
        }
    ],
    ...
    

To configure the uptime check to fail when a specific field in the JSON-formatted response matches a number or a string literal, use the following values for the `ContentMatcher` object:
    
    
    ...
    "contentMatchers": [
        {
           "content" : "Set to a number, a boolean, or the string to be matched.",
           "matcher" : "NOT_MATCHES_JSON_PATH",
           "jsonPathMatcher" : {
               "jsonPath" : "Set to the JSONpath.",
               "jsonMatcher" : "EXACT_MATCH"
           }
        }
    ],
    ...
    

To illustrate how the JSONpath string-match tests operate, consider the following JSON response data:
    
    
    {
        "name": "Sample Uptime Check",
        "type": "JSONpath",
        "content": [
            {
                "id": 1,
                "phone": "1234567890",
                "alias": "Exact",
                "enabled": true,
            },
            {
                "id": 2,
                "phone": "1234512345",
                "alias": "Regex",
                "enabled": false,
            }
        ]
    }
    

The following table displays the uptime check status for the previous response, but for different paths, test values, and test types:

|  | Uptime check status   
---|---|---  
JSONpath | Test value | JSONpath matches | JSONpath doesn't match  
`$.type` | `"JSONpath"` | pass | fail  
`$.name` | `"Sample"` | fail | pass  
`$.name` | `"Sample Uptime Check"` | pass | fail  
`$.content[0].id` | `1` | pass | fail  
`$.content[0].alias` | `"Exact"` | pass | fail  
`$.content[0].enabled` | `true` | pass | fail  
  
In the previous table, the **JSONpath** column identifies which element to test and the **Test value** column lists the value. The next two columns specify the type of test and the result of the uptime check.

#### Compare JSONpath to a regular expression

Regular expression matches support matching a string, a number, a boolean, and null JSON values.

**Note:** The expression that you enter must match the entire value of the JSONpath. For example, if the value of a field is `"North Pole"`, then `.*North.*` and `^North.*` match the field while `North` and `"North"` don't match.

###  Console 

To configure the uptime check to pass when a specific JSONpath in the response data matches a regular expression, use the following settings:

  1. Select **Matches at JSONPath** in the **Response content match type** menu.
  2. Enter the path in the **JSONPath** field.
  3. Enter the regular expression in the **Response content** field.
  4. To verify the configuration, click **Test**.



To configure the uptime check to fail when a specific JSONpath in the response data matches a regular expression, use the following settings:

  1. Select **Does not match at JSONPath** in the **Response content match type** menu.
  2. Enter the path in the **JSONPath** field.
  3. Enter the regular expression in the **Response content** field.
  4. To verify the configuration, click **Test**.



###  REST 

To configure the uptime check to pass when a specific field in the JSON-formatted response matches a regular expression, use the following values for the `ContentMatcher` object:
    
    
    ...
    "contentMatchers": [
        {
           "content" : "Set to the regular expression to be matched.",
           "matcher" : "MATCHES_JSON_PATH",
           "jsonPathMatcher" : {
               "jsonPath" : "Set to the JSONpath.",
               "jsonMatcher" : "REGEX_MATCH"
           }
        }
    ],
    ...
    

To configure the uptime check to fail when a specific field in the JSON-formatted response matches a regular expression, use the following values for the `ContentMatcher` object:
    
    
    ...
    "contentMatchers": [
        {
           "content" : "Set to the regular expression to be matched.",
           "matcher" : "NOT_MATCHES_JSON_PATH",
           "jsonPathMatcher" : {
               "jsonPath" : "Set to the JSONpath.",
               "jsonMatcher" : "REGEX_MATCH"
           }
        }
    ],
    ...
    

To illustrate how the JSONpath regular-expression tests operate, consider the following JSON response data:
    
    
    {
        "name": "Sample Uptime Check",
        "type": "JSONpath",
        "content": [
            {
                "id": 1,
                "phone": "1234567890",
                "alias": "Exact",
                "enabled": true,
            },
            {
                "id": 2,
                "phone": "1234512345",
                "alias": "Regex",
                "enabled": false,
            }
        ]
    }
    

The following table displays the uptime check status for the previous response, but for different paths, regular expressions, and test types:

|  | Uptime check status   
---|---|---  
JSONpath | Regex | JSONpath matches regex | JSONpath doesn't match regex  
`$.type` | `[A-Z]{4}Path` | pass | fail  
`$.name` | `Sample` | fail | pass  
`$.name` | `.*Sample.*` | pass | fail  
`$.content[1].id` | `2` | pass | fail  
`$.content[1].phone` | `"[12345]{2}"` | pass | fail  
`$.content[1].enabled` | `f.*` | pass | fail  
  
In the previous table, the **JSONpath** column identifies which element to test and the **Regex** column lists the regular expression. The next two columns specify the type of test and the result of the uptime check.

## What's next

  * [Create an uptime check](https://docs.cloud.google.com/monitoring/uptime-checks)
  * [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage)
  * [Create alerting policies for uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/uptime-alerting-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
