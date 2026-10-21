---
url: https://docs.cloud.google.com/workflows/docs/samples/workflows-sheets-bigquery/
title: Query a BigQuery dataset and write the results to a Sheet spreadsheet using connectors \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:02:11.300198+00:00
---

# Query a BigQuery dataset and write the results to a Sheet spreadsheet using connectors  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/samples/workflows-sheets-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Samples ](https://docs.cloud.google.com/workflows/docs/samples)



#  Query a BigQuery dataset and write the results to a Sheet spreadsheet using connectors Stay organized with collections  Save and categorize content based on your preferences. 

Queries a BigQuery dataset using the BigQuery API connector and writes the results to a Sheets spreadsheet using the Google Sheets API connector.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Write to Google Sheets from a workflow](https://docs.cloud.google.com/workflows/docs/write-to-google-sheets)



## Code sample

### YAML
    
    
    main:
        steps:
        - init:
            assign:
            # Replace with your sheetId and make sure the service account
            # for the workflow has write permissions to the sheet
            - sheetId: "1D8n7uoU8kGwQvR4rcLkF10CdAfnUKE2o0yl6P-Z7nfM"
            - limit: 100
        - runQuery:
            call: googleapis.bigquery.v2.jobs.query
            args:
                projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                body:
                    useLegacySql: false
                    # Query name and gender of most popular names
                    query: ${"SELECT name, gender, SUM(number) AS total
                        FROM `bigquery-public-data.usa_names.usa_1910_2013`
                        GROUP BY name, gender
                        ORDER BY total DESC
                        LIMIT " + limit}
            result: queryResult
        - init_header_row:
            assign:
            - rows:
                - ["Name", "Gender", "Total"]
        - process_query_result:
            for:
                value: row
                in: ${queryResult.rows}
                steps:
                - process_each_row:
                    assign:
                    - name: ${row.f[0].v}
                    - gender: ${row.f[1].v}
                    - total: ${row.f[2].v}
                    - row: ["${name}", "${gender}", "${total}"]
                    - rows: ${list.concat(rows, row)}
        - clear_existing_values:
            call: googleapis.sheets.v4.spreadsheets.values.clear
            args:
                range: "Sheet1"
                spreadsheetId: ${sheetId}
            result: clearResult
        - update_sheet:
            call: googleapis.sheets.v4.spreadsheets.values.update
            args:
                range: ${"Sheet1!A1:C" + (limit + 1)}
                spreadsheetId: ${sheetId}
                valueInputOption: RAW
                body:
                    majorDimension: "ROWS"
                    values: ${rows}
            result: updateResult
        - returnResult:
            return: ${updateResult}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=workflows). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
