---
url: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/re-capture_all/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:38:47.553889+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-functions/re-capture_all/




Stay organized with collections  Save and categorize content based on your preferences. 

### re.capture_all

Supported in:

[ Rules ](https://docs.cloud.google.com/chronicle/docs/detection/default-rules) [ Search ](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search) [ Dashboards ](https://docs.cloud.google.com/chronicle/docs/reports/dashboards-overview)
    
    
    re.capture_all(stringText, regex)
    

#### Description

Use the `re.capture_all()` function to extract every non-overlapping match of a regular expression from a string. While the standard `re.capture()` function stops after the first match it finds, `re.capture_all()` continues through the entire string to identify every instance that matches your pattern.

This function takes two arguments:

  * `string_to_search`: The input string or UDM field you want to search.
  * `regex_pattern`: The regular expression you apply. Note: This regular expression must not contain more than one capturing group.



#### Common use cases

You use `re.capture_all()` to solve scenarios where a single log field contains multiple valuable data points.

  * **Extract multiple indicators:** Pull all IP addresses, URLs, or hostnames from a single log message or description field.
  * **Parse delimited data:** Isolate specific values from fields where multiple pieces of information are separated by commas, semicolons, or mixed with other text.
  * **Analyze free-form text:** Scan unstructured fields (like **Notes** or **Comments**) to identify every pattern match, such as file paths or registry keys.
  * **Audit command lines:** Extract all arguments or specific flags from a process command line to better understand the scope of a command.



#### Param data types

`STRING`, `STRING`

#### Return type

`ARRAY_STRINGS`

#### Examples

This section shows examples that demonstrate how you apply `re.capture_all()` to different types of telemetry. You use these patterns in the `events` section to filter data or the `outcome` section to enrich your final detection alerts.

##### Example: Extract the fifth .conf path from a command line

This search example first confirms the presence of `.conf` in a command line.

It then saves the full command line and extracts the fifth occurrence of a specific pattern related to `.conf` file paths. You can combine the `re.capture_all()` function with `arrays.index_to_str()` to extract a specific occurrence, such as the fifth `.conf` path from a command line.
    
    
    re.regex(principal.process.command_line, `\.conf`)
    $command_line = principal.process.command_line
    $path_component_5 = arrays.index_to_str(re.capture_all(principal.process.command_line, `[s='"]([^'"=s]*.conf)`), 4)
    

**Note:** If the `re.capture_all()` function finds fewer than five matches, index 4 is out of bounds. In this case, `arrays.index_to_str()` returns an empty string `""` for `$path_component_5`.

##### Example: Extract all words that start with `error`

In this rule example, you capture every word starting with `error` from a security result description and store them in an array called `$all_errors`.
    
    
    rule ExtractErrors {
      meta:
        author = "user@example.com"
      events:
        $e.principal.hostname = "server1"
        $log_message = $e.security_result[0].description
      outcome:
        $all_errors = re.capture_all($log_message, `error\w+`)
      condition:
        $e
    }
    

##### Example: Join all captured IP-like patterns from a User-Agent string

In this rule example, you extract all IPv4 addresses from the `network.http.user_agent` field of security events.

Since `re.capture_all()` returns an array, you can use `arrays.join_string()` to merge these matches into a single, readable list.
    
    
    rule CaptureAllIPs {
      meta:
        author = "user@example.com"
      events:
        $e.network.http.user_agent != ""
        $captured_ips = arrays.join_string(re.capture_all($e.network.http.user_agent, `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`), ", ")
      condition:
        $e
    }
    

#### Known limitations

  * **Single capturing group:** The regular expression used with `re.capture_all()` must not contain more than one capturing group.
  * **Array return type:** The function returns an array of strings. To assign the result to an event variable or to use it in functions expecting a single string, you typically need to wrap it with `arrays.join_string()`.



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
