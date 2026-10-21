---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-expression/
title: Use an expression to assign a variable value \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:20.904213+00:00
---

# Use an expression to assign a variable value  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-expression/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Use an expression to assign a variable value Stay organized with collections  Save and categorize content based on your preferences. 

Uses an expression to assign the value of a variable previously defined.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables)



## Code sample

### YAML
    
    
    - get_message:
        assign:
          - name: "Harsha"
          - last_name: "Kapoor"
          - full_name: ${name+" "+last_name}
          - temperature_C: 27
          - temperature_F: ${temperature_C * 9/5 + 32}
          - temperature_msg: ${"Current temperature is "+string(temperature_F)+" F"}
    - return_value:
        return: ${temperature_msg}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
