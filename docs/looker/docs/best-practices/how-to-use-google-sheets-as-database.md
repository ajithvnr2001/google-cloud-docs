---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-google-sheets-as-database/
title: Live spreadsheets in databases \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:35.792588+00:00
---

# Live spreadsheets in databases  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-google-sheets-as-database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Live spreadsheets in databases Stay organized with collections  Save and categorize content based on your preferences. 

The BigQuery team has developed the ability to treat a Google Sheet like a table in a database. That means you can join a billion-row BigQuery table with a 100-row mapping table that you type into a spreadsheet in a single query. 

This feature lets you configure data models, create a data pipeline for ad hoc data, or compare up-to-date numbers to your latest goals and projections. 

##  Example 

For example, you might want to model usernames in Looker that were collected using a Google form. 

To collect and model the information in Looker, you would perform the following steps: 

  1. Using Google Forms, [collect the data into a Google sheet](https://support.google.com/docs/answer/2917686). Every submission adds a row in the sheet. 
  2. Share the spreadsheet with the service account that you use to connect to Looker, or grant access to users with a link (view only). 
  3. Make sure that the [Drive API and Sheets API are enabled for your project](https://console.developers.google.com/apis/library). 
  4. Create a table from the [BigQuery interface](https://docs.cloud.google.com/bigquery) that gets its content from the spreadsheet. 
  5. In your Looker project, [generate a data model](https://docs.cloud.google.com/looker/docs/generating-a-model) that joins the spreadsheet table with other user data that you might already have collected, such as users' locations. You can also use SQL to normalize the names that are coming from the database. The data can be cached in BigQuery to avoid heavy load on the spreadsheet. 



The following is an example of what the resulting LookML might look like: 
    
    
    explore: names_sheet {
      persist_for: "60 seconds"
    
      join: names_facts {
        sql_on: ${names_sheet.normalized_name} = ${names_facts.normalized_name} ;;
        sql_where: ${names_facts.city} ;;
        relationship: one_to_one
      }
    
      view_name: names_sheet {
        derived_table: {
          persist_for: "2 minutes"
          sql:
            SELECT row_number() OVER() as id, name, UPPER(CASE WHEN REGEXP_MATCH(name, r'\,')
              THEN REGEXP_EXTRACT(name, r', (\w+)')
              ELSE REGEXP_EXTRACT(name, r'^(\w+)')
              END
              ) as normalized_name FROM namesheet.names ;;
        }
    
        dimension: id {
          type: number
        }
    
        dimension: name {
          order_by_field: id    # keep the rows in the original order
        }
    
        dimension: normalized_name {
        }
    
        measure: count {
          type: count
          drill_fields: [id, name, names_facts.city]
        }
    
        measure: count_from_new_york_city {
          type: count
          filters: [names_facts.city: "New York City"]
        }
    
        measure: percentage_from_new_york_city {
          type: number
          sql: ${count_from_new_york_city}/${count} ;;
          value_format_name: percent_2
        }
    
        measure: average_age_median {
          type: average
          sql: ${names_facts.age_median} ;;
          value_format: "0000"
        }
      }
    }
    

From this model, you can create [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) with your data and build [Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks) and [dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards) that show metrics about all the usernames that you've collected from Google Forms and entered into the Google Sheet, as well as other information about each individual user. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
