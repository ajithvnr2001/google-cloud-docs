---
url: https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/get_env/
title: Function: sys.get_env \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:21.953833+00:00
---

# Function: sys.get_env  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/stdlib/sys/get_env/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Function: sys.get_env Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves the value of the specified environment variable.

If the specified variable is not set, returns the default value instead.

The following built-in environment variables are supported:

Variable name | Description  
---|---  
`GOOGLE_CLOUD_LOCATION` | The workflow's location.  
`GOOGLE_CLOUD_PROJECT_ID` | The workflow project's identifier.  
`GOOGLE_CLOUD_PROJECT_NUMBER` | The workflow project's number.  
`GOOGLE_CLOUD_SERVICE_ACCOUNT_NAME` | The workflow execution's service  
| account name.  
`GOOGLE_CLOUD_WORKFLOW_EXECUTION_ID` | The workflow execution's identifier.  
`GOOGLE_CLOUD_WORKFLOW_ID` | The workflow's identifier.  
`GOOGLE_CLOUD_WORKFLOW_REVISION_ID` | The workflow's revision identifier.  
  
You can also retrieve user-defined environment variables. For more information, see [Use environment variables](https://cloud.google.com/workflows/docs/use-environment-variables).

## Arguments

Arguments  
---  
`name` |  `string` The requested environment variable name.  
`default` |  `string` The string value to return if the named variable is not set.  
  
## Returns

The value of the named environment variable, or the default if not set.

## Raised exceptions

Exceptions  
---  
`TypeError` | If either `name` or `default` is not a string.  
  
## Examples

For more information, see [Built-in environment variables](https://cloud.google.com/workflows/docs/reference/environment-variables)
    
    
    # Retrieve value of specified environment variable
    # For example, returns "us-central1"
    - returnStep:
        return: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
