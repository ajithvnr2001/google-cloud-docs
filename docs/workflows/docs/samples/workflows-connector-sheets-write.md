---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-sheets-write/
title: Write to Google Sheets from a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:10.253671+00:00
---

# Write to Google Sheets from a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-sheets-write/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Write to Google Sheets from a workflow Stay organized with collections  Save and categorize content based on your preferences. 

Uses the Google Sheets API connector to create a spreadsheet.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write to Google Sheets from a workflow](https://docs.cloud.google.com/workflows/docs/write-to-google-sheets)



## Code sample

### YAML
    
    
    main:
      steps:
        - init:
            assign:
              - folder_id: 'FOLDER_ID'
              - drive_url: 'https://www.googleapis.com/drive/v3/files/'
              - drive_auth_scope: 'https://www.googleapis.com/auth/drive'
        - create_sheet:
            call: googleapis.sheets.v4.spreadsheets.create
            args:
              body: null
              connector_params:
                scopes: 'https://www.googleapis.com/auth/drive'
            result: resp
        - get_sheet_info:
            call: http.get
            args:
              url: '${drive_url + resp.spreadsheetId}'
              query:
                fields: parents
              auth:
                type: OAuth2
                scopes: '${drive_auth_scope}'
            result: sheet_info
        - move_sheet:
            call: http.patch
            args:
              url: '${drive_url + resp.spreadsheetId}'
              query:
                addParents: '${folder_id}'
                removeParents: '${sheet_info["body"]["parents"][0]}'
              auth:
                type: OAuth2
                scopes: '${drive_auth_scope}'
            result: resp
        - return:
            return: '${resp}'

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
