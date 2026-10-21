---
url: https://docs.cloud.google.com/data-fusion/docs/use-case/salesforce-soql-queries/
title: Use case: SOQL queries for the Salesforce source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:26.921064+00:00
---

# Use case: SOQL queries for the Salesforce source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/use-case/salesforce-soql-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Use case: SOQL queries for the Salesforce source Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to use SOQL relationship queries when you use the Salesforce source in Cloud Data Fusion.

The Salesforce source lets you seamlessly connect to Salesforce and load large amounts of data into Google Cloud. To simplify loading the data, you can use [SOQL relationship queries](http://www.salesforce.com/us/developer/docs/dbcom_soql_sosl/Content/sforce_api_calls_soql_relationships.htm) to retrieve records and reduce the number of API calls in Salesforce.

## Before you begin

  1. Deploy and configure the properties for the Salesforce source in Cloud Data Fusion. For more information, see [Salesforce batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source#confirgure).

  2. On the **Salesforce** node in your pipeline, click **Properties**. This opens the Salesforce plugin properties page.




The following sections describe how to configure the **SOQL query** field on the **Properties** page.

## Scenario 1: Relationship query with polymorphic key and limits

The following relationship query example has a polymorphic key and a limit:
    
    
    SELECT Id, Owner.Name FROM Task WHERE Owner.FirstName like 'B%' Limit 100
    

This query fetches data from a `Task` SObject related to `Owner`. It reads data from the selected fields in the `Task` SObject. It has a `WHERE` clause and a placeholder, which you can assign a suitable value.

This query lets you access the required fields using a placeholder variable. It limits the quantity of records fetched to `100`.

## Scenario 2: Relationship query with child-to-parent with custom objects

The following query fetches data from a custom object with child-to-parent relationship:
    
    
    SELECT Email,newsales__c,Account__r.OwnerId FROM lead WHERE Account__r.Lead Source LIKE 'C%
    

This query uses a `SELECT` clause to fetch data from the `Lead` SObject in Salesforce with the reference field, `Account__r.OwnerId`.

The query returns data from the selected fields in the `Lead` SObject and the relational fields from the lookup linked to the `Account` parent object. You can query multiple data fields from a cluster of relational SObjects.

**Note:** In the Salesforce plugin, reference object fields are case sensitive, where the other fields aren't.

### Scenario 3: Relationship query with WHERE and OFFSET clauses

The following query fetches data from multiple SObjects: `Account` and `Contacts`, related to a specific `Industry` type and `OFFSET` clause:
    
    
    SELECT Name, (SELECT LastName FROM Contacts WHERE CreatedBy.Alias = 'x') FROM Account WHERE Industry = 'media'
    offset 4
    

The `OFFSET` clause lets you to return results on multiple pages, which is an efficient way to handle large results sets.

## What's next

  * Configure the [Salesforce batch source](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-salesforce-batch-source#properties) in Cloud Data Fusion.
  * Work through a [Salesforce plugin tutorial](https://docs.cloud.google.com/data-fusion/docs/tutorials/connect-salesforce-to-bq).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
