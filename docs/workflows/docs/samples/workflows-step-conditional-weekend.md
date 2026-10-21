---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-step-conditional-weekend/
title: Conditional jump to a specific step \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:54:44.214095+00:00
---

# Conditional jump to a specific step  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-step-conditional-weekend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Conditional jump to a specific step Stay organized with collections  Save and categorize content based on your preferences. 

Jumps to a specific step depending on the day of the week returned by the first step of the workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Conditions](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions)



## Code sample

### YAML
    
    
    - getCurrentTime:
        call: http.get
        args:
          url: https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam
        result: currentTime
    - conditionalSwitch:
        switch:
          - condition: ${currentTime.body.dayOfWeek == "Friday"}
            next: friday
          - condition: ${currentTime.body.dayOfWeek == "Saturday" or currentTime.body.dayOfWeek == "Sunday"}
            next: weekend
        next: workWeek
    - friday:
        return: "It's Friday! Almost the weekend!"
    - weekend:
        return: "It's the weekend!"
    - workWeek:
        return: "It's the work week."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
