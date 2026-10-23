---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-sheets/
title: Connector for Google Sheets \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:27.681253+00:00
---

# Connector for Google Sheets  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-connector-sheets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Connector for Google Sheets Stay organized with collections  Save and categorize content based on your preferences. 

Workflows connector that defines the built-in function used to access Google Sheets from within a workflow.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Google Sheets API Connector Overview](https://docs.cloud.google.com/workflows/docs/reference/googleapis/sheets/Overview)



## Code sample

### YAML
    
    
    # This workflow demonstrates how to use the Google Sheets connector:
    # Create, update, get, and delete a Google Sheets spreadsheet
    # Expected output: "SUCCESS"
    - init:
        assign:
          - createRange: "A20"  # example range
          - getRange: "A1:B4"  # example range
          - row:
              values:
                - {"userEnteredFormat": {"backgroundColor": {"red": 0, "green":1, "blue":0, "alpha":1}}}
          - start1:
              sheetId: 0
              rowIndex: 2
              columnIndex: 0
          - request1:
              rows:
                - ${row}
              fields: userEnteredFormat.backgroundColor
              start: ${start1}
          - driveScope: https://www.googleapis.com/auth/drive
    - create_spreadsheet:
        call: googleapis.sheets.v4.spreadsheets.create
        args:
          body:
          connector_params:
            scopes: ${driveScope}
        result: resp
    - assign_sheet_id:
        assign:
          - sheetId: ${resp.spreadsheetId}
    - update_spreadsheet:
        call: googleapis.sheets.v4.spreadsheets.values.update
        args:
          spreadsheetId: ${sheetId}
          range: ${createRange}
          valueInputOption: RAW
          includeValuesInResponse:
          body:
            values:
              - ["text to update"]
    - batch_update:
        call: googleapis.sheets.v4.spreadsheets.batchUpdate
        args:
          spreadsheetId: ${sheetId}
          body:
            requests:
              - updateCells: ${request1}
            includeSpreadsheetInResponse: true
          connector_params:
            scopes: ${driveScope}
    - get_from_sheet:
        call: googleapis.sheets.v4.spreadsheets.get
        args:
          spreadsheetId: ${sheetId}
          ranges:
            - ${getRange}
          includeGridData: false
          connector_params:
            scopes: ${driveScope}
    - delete_sheet:
        call: http.delete
        args:
          url: ${"https://www.googleapis.com/drive/v2/files/" + sheetId}
          auth:
            type: OAuth2
            scopes: ${driveScope}
    - return_step:
        return: SUCCESS

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
