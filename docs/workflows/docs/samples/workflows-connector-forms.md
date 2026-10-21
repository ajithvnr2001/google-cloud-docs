---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-forms/
title: Connector for Google Forms \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:12:24.245932+00:00
---

# Connector for Google Forms  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-forms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Google Forms Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Google Forms within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Google Forms API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/forms/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Google Forms connector:
    # Create, update, get, and delete a Google Form
    # Expected output: "SUCCESS"
    - init:
        assign:
          - form_title: "sample-form"
    - create_form:
        call: googleapis.forms.v1.forms.create
        args:
          body:
            info:
              title: ${form_title}
        result: create_form_resp
    - update_form:
        call: googleapis.forms.v1.forms.batchUpdate
        args:
          formId: ${create_form_resp.formId}
          body:
            requests:
              - updateFormInfo:
                  info:
                    title: "new-title"
                  updateMask: title
    - get_form:
        call: googleapis.forms.v1.forms.get
        args:
          formId: ${create_form_resp.formId}
    - list_responses:
        call: googleapis.forms.v1.forms.responses.list
        args:
          formId: ${create_form_resp.formId}
          pageSize: 10
    - delete_form:
        call: http.delete
        args:
          url: ${"https://www.googleapis.com/drive/v3/files/" + create_form_resp.formId}
          auth:
            type: OAuth2
            scope: https://www.googleapis.com/auth/drive
    - the_end:
        return: "SUCCESS"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
