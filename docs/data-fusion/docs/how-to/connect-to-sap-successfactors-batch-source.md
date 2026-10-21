---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-successfactors-batch-source/
title: SAP SuccessFactors batch source \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:26.662972+00:00
---

# SAP SuccessFactors batch source  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-sap-successfactors-batch-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  SAP SuccessFactors batch source Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to extract data from any entity within the [SAP SuccessFactors Employee Central module](https://api.sap.com/package/SuccessFactorsEmployeeCentral/odata) into Google Cloud with Cloud Data Fusion.

**Note:** This documentation applies to Cloud Data Fusion 6.7 and later, and SAP SuccessFactors plugin 1.2.3 and later.

For more information, see the [overview of SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).

## Before you begin

Set up the following systems and services that are used by the SAP SuccessFactors plugin:

  1. **Configure the SAP SuccessFactors system**. You must [set up permissions in your SAP system](https://help.sap.com/docs/SAP_SUCCESSFACTORS_EMPLOYEE_CENTRAL_INTEGRATION_TO_SAP_BUSINESS_SUITE/d16c7ad18be3425ea8387bb50ed7b379/d46f434080ae4f31842492eaedeedc20.html?version=2311).
  2. [**Deploy the SAP SuccessFactors plugin in Cloud Data Fusion**](https://docs.cloud.google.com/data-fusion/docs/how-to/deploy-a-plugin#deploy-sap-plugin). You must deploy a plugin version that's compatible with the Cloud Data Fusion version. 
     * If you upgrade the version of your Cloud Data Fusion instance or plugin, evaluate the impact of the changes to the pipeline's functional scope and performance.
  3. **Establish connectivity between Cloud Data Fusion and SAP SuccessFactors**. 
     * Ensure that communication is enabled between the Cloud Data Fusion instance and the SAP SuccessFactors instance.
     * For private instances, set up [VPC network peering](https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip#set-up-vpc-peering).



## Configure the plugin

  1. [Go to the Cloud Data Fusion web interface](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline#navigate-web-interface) and click **Studio**.
  2. Check that **Data Pipeline - Batch** is selected (not **Realtime**).
  3. In the **Source** menu, click **SuccessFactors**. The SAP SuccessFactors node appears in your pipeline.
  4. To configure the source, go to the SAP SuccessFactors node and click **Properties**.
  5. Enter the following properties. For a complete list, see Properties.

     1. Enter a **Label** for the SAP SuccessFactorsnode—for example, `SAP SuccessFactors tables`.
     2. Enter the connection details. You can set up a new, one-time connection, or an existing, reusable connection.

### One-time connection

To add a one-time connection to SAP, follow these steps:

        1. Keep **Use connection** turned off.
        2. In the **Connection** section, enter the following information from the SAP account in these fields:

           1. Provide the SAP credentials.
           2. In the **SAP SuccessFactors Base URL** field, enter your SAP SuccessFactors account base URL.
           3. In the **Reference name** field, enter a name for the connection that identifies this source for lineage.
           4. In the **Entity Name** field, enter the name of the entity you're extracting—for example, `people`.
           5. To generate a schema based on the metadata from SAP that maps SAP data types to corresponding Cloud Data Fusion data types, click **Get schema**. For more information, see Data type mappings.
           6. In the **Proxy URL** field, enter the Proxy URL, including the protocol, address, and port.
           7. Optional: to optimize the ingestion load from SAP, enter the following information:

              1. To extract records based on selection conditions, click **Filter options** and **Select fields**.
              2. In the **Expand fields** , enter a list of navigation fields to be expanded in the extracted output data. For example, `customManager`.
              3. In **Additional query parameters** , enter parameters to add to the URL—for example, `fromDate=2023-01-01&toDate=2023-01-31`.
              4. In the **Associated entity name** field, enter the name of the entity to be extracted—for example, `EmpCompensationCalculated`.
              5. In the **Pagination type** field, enter a type—for example, [`Server-side pagination`](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/2cd6a3c92f2547c99cfd612c6867582f.html).

### Reusable connection

To reuse an existing connection, follow these steps:

        1. Turn on **Use connection**.
        2. Click **Browse connections**.
        3. Click the connection name.

**Note:** For more information about adding, importing, and editing the connections that appear when you browse connections, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).

If a connection doesn't exist, create a reusable connection by following these steps:

        1. Click **Add connection > SAP SuccessFactors**.
        2. On the **Create a SAP SuccessFactors connection** page that opens, enter a connection name and description.
        3. Provide the SAP credentials. You can ask the SAP administrator for the SAP logon username and password values.
        4. In the **Proxy URL** field, enter the Proxy URL, including the protocol, address, and port.
        5. Click **Create**.




### Properties

Property | Macro enabled | Required property | Description  
---|---|---|---  
**Label** | No | Yes | The name of the node in your data pipeline.  
**Use connection** | No | No | Use a reusable connection. If a connection is used, you don't need to provide the credentials. For more information, see [Manage connections](https://docs.cloud.google.com/data-fusion/docs/how-to/managing-connections).  
**Name** | No | Yes | The name of the reusable connection.  
**Reference Name** | No | Yes | Uniquely identifies the source for lineage and annotates the metadata.   
**SAP SuccessFactors Base URL** | Yes | Yes | The base URL of SuccessFactors API.  
**Entity Name** | Yes | Yes | The name of the Entity to be extracted. Doesn't support entities that have properties with the Binary data type or large volumes of data. For example, `UserBadges` and `BadgeTemplates` aren't supported.  
**SAP SuccessFactors Username** | Yes | Yes | The user ID for authentication, similar to `USER_ID@COMPANY_ID`. For example, `sfadmin@cymbalgroup`.  
**SAP SuccessFactors Password** | Yes | Yes | The SAP SuccessFactors Password for user authentication.  
**Filter Options** | Yes | No | The filter condition that restricts the output data volume, for example, `Price gt 200`. See the supported filter options.  
**Select Fields** | Yes | No | Fields to be preserved in the extracted data. For example, `Category`, `Price`, `Name`, `Address`. If the field is left blank, then all the non-navigation fields will be preserved in the extracted data.  
  
All fields must be comma (,) separated.  
**Expand Fields** | Yes | No | List of navigation fields to be expanded in the extracted output data. For example, `customManager`. If an entity has hierarchical records, the source outputs a record for each row in the entity it reads, with each record containing an extra field that holds the value from the navigational property specified in the Expand Fields.  
**Associated Entity Name** | Yes | No | Name of the Associated Entity that is being extracted. For example, `EmpCompensationCalculated`.  
**Pagination Type** | Yes | Yes | The type of pagination to be used. Server-side pagination uses snapshot-based pagination. If snapshot-based pagination is attempted on an entity that doesn't support the feature, the server automatically forces client-offset pagination on the query.  
Examples of entities that only support server-side pagination are `BadgeTemplates`, `UserBadges`, and `EPCustomBackgroundPortlet`. No records are transferred if client-side pagination is chosen on these entities, as it relies on the Count API, which returns `-1` as the response.  
  
Default is [Server-side Pagination](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/2cd6a3c92f2547c99cfd612c6867582f.html).  
  
### Supported filter options

The following operators are supported:

Operator | Description | Example  
---|---|---  
**Logical Operators**  
`Eq` | Equal | `/EmpGlobalAssignment?$filter=assignmentClass eq 'GA'`  
`Ne` | Not equal | `/RecurringDeductionItem?$filter=amount ne 18`  
`Gt` | Greater than | `/RecurringDeductionItem?$filter=amount gt 4`  
`Ge` | Greater than or equal | `/RecurringDeductionItem?$filter=amount ge 18`  
`Lt` | Less than | `/RecurringDeductionItem?$filter=amount lt 18`  
`Le` | Less than or equal | `/RecurringDeductionItem?$filter=amount le 20`  
`And` | Logical and | `/RecurringDeductionItem?$filter=amount le 20 and amount gt 4`  
`Or` | Logical or | `/RecurringDeductionItem?$filter=amount le 20 or amount gt 4`  
`Not` | Logical negation | `/RecurringDeductionItem?$filter=not endswith(payComponentType, 'SUPSPEE_US')`  
**Arithmetic Operators**  
`Add` | Addition | `/RecurringDeductionItem?$filter=amount add 5 gt 18`  
`Sub` | Subtraction | `/RecurringDeductionItem?$filter=amount sub 5 gt 18`  
`Mul` | Multiplication | `/RecurringDeductionItem?$filter=amount mul 2 gt 18`  
`Div` | Division | `/RecurringDeductionItem?$filter=amount div 2 gt 18`  
`Mod` | Modulo | `/RecurringDeductionItem?$filter=amount mod 2 eq 0`  
**Grouping Operators**  
`( )` | Precedence grouping | `/RecurringDeductionItem?$filter=(amount sub 5) gt 8`  
  
### Data type mappings

The following table is a list of SAP data types with corresponding Cloud Data Fusion types.

SuccessFactors Data Type | Cloud Data Fusion Schema Data Type  
---|---  
`Binary` | `Bytes`  
`Boolean` | `Boolean`  
`Byte` | `Bytes`  
`DateTime` | `DateTime`  
`DateTimeOffset` | `Timestamp_Micros`  
`Decimal` | `Decimal`  
`Double` | `Double`  
`Float` | `Float`  
`Int16` | `Integer`  
`Int32` | `Integer`  
`Int64` | `Long`  
`SByte` | `Integer`  
`String` | `String`  
`Time` | `Time_Micros`  
  
## Use cases

The following example use case is the data for a single employee in `EmployeePayrollRunResults`:

Example property | Example value  
---|---  
externalCode | SAP_EC_PAYROLL_1000_0101201501312015_456_416  
Person ID | 456  
User | user-1  
Employment ID | 416  
Payroll Provider ID | SAP_EC_PAYROLL  
Start of Effective Payment Period | 01/01/2015  
End of Effective Payment Period | 01/31/2015  
Company ID | BestRun Germany (1000)  
Payout | 01/28/2015  
Currency | EUR (EUR)  
Payroll Run Type | Regular (REGULAR)  
System ID | X0B  
  
The example shows the results for an employee in `EmployeePayrollRunResults`:

`EmployeePayrollRunResults_externalCod`e | `EmployeePayrollRunResults_mdfSystemEffectiveStartDate` | `amount` | `createdBy` | `createdDate`  
---|---|---|---|---  
`SAP_EC_PAYROLL_2800_0101201901312019_305_265` | `1/31/2019 0:00:00` | `70923.9` | `sfadmin` | `12/10/2019 15:32:20`  
`SAP_EC_PAYROLL_2800_0101201901312019_310_270` | `1/31/2019 0:00:00` | `64500` | `sfadmin` | `12/10/2019 15:32:20`  
`SAP_EC_PAYROLL_2800_0201201902282019_305_265` | `2/28/2019 0:00:00` | `70923.9` | `sfadmin` | `12/10/2019 15:32:20`  
`SAP_EC_PAYROLL_2800_0201201902282019_310_270` | `2/28/2019 0:00:00` | `64500` | `sfadmin` | `12/10/2019 15:32:20`  
`SAP_EC_PAYROLL_2800_0301201903312019_305_265` | `3/31/2019 0:00:00` | `70923.9` | `sfadmin` | `12/10/2019 15:32:20`  
  
## Example pipeline

See sample configurations in the following JSON file:
    
    
      {
          "artifact": {
              "name": "data-pipeline-1",
              "version": "DATA_FUSION_VERSION",
              "scope": "SYSTEM"
          },
          "description": "",
          "name": "Demo_SuccessFactors_BatchSource",
          "config": {
              "resources": {
                  "memoryMB": 2048,
                  "virtualCores": 1
              },
              "driverResources": {
                  "memoryMB": 2048,
                  "virtualCores": 1
              },
              "connections": [
                  {
                      "from": "SAP SuccessFactors",
                      "to": "BigQuery"
                  }
              ],
              "comments": [],
              "postActions": [],
              "properties": {},
              "processTimingEnabled": true,
              "stageLoggingEnabled": false,
              "stages": [
                  {
                      "name": "SAP SuccessFactors",
                      "plugin": {
                          "name": "SuccessFactors",
                          "type": "batchsource",
                          "label": "SAP SuccessFactors",
                          "artifact": {
                              "name": "successfactors-plugins",
                              "version": "PLUGIN_VERSION",
                              "scope": "USER"
                          },
                          "properties": {
                            "useConnection": "false",
                            "username": "${username}",
                            "password": "${password}",
                            "baseURL": "${baseUrl}",
                            "referenceName": "test",
                            "entityName": "${EmpCompensation}",
                            "proxyUrl": "${ProxyUrl}",
                            "paginationType": "serverSide",
                            "initialRetryDuration": "2",
                            "maxRetryDuration": "300",
                            "maxRetryCount": "3",
                            "retryMultiplier": "2",
                            "proxyUsername": "${Proxyusername}",
                            "proxyPassword": "${Proxypassword}"
                          }
                      },
                      "outputSchema": [
                          {
                              "name": "etlSchemaBody",
                              "schema": ""
                          }
                      ],
                      "id": "SAP-SuccessFactors"
                  },
                  {
                      "name": "BigQuery",
                      "plugin": {
                          "name": "BigQueryTable",
                          "type": "batchsink",
                          "label": "BigQuery",
                          "artifact": {
                              "name": "google-cloud",
                              "version": "BIGQUERY_PLUGIN_VERSION",
                              "scope": "SYSTEM"
                          },
                          "properties": {
                            "useConnection": "false",
                            "project": "auto-detect",
                            "serviceAccountType": "filePath",
                            "serviceFilePath": "auto-detect",
                            "referenceName": "Reff",
                            "dataset": "SF_Aug",
                            "table": "testdata_proxy",
                            "operation": "insert",
                            "truncateTable": "true",
                            "allowSchemaRelaxation": "true",
                            "location": "US",
                            "createPartitionedTable": "false",
                            "partitioningType": "TIME",
                            "partitionFilterRequired": "false"
                          }
                      },
                      "outputSchema": [
                          {
                              "name": "etlSchemaBody",
                              "schema": ""
                          }
                      ],
                      "inputSchema": [
                          {
                              "name": "SAP SuccessFactors",
                              "schema": ""
                          }
                      ],
                      "id": "BigQuery"
                  }
              ],
               "schedule": "0 1 */1 * *",
            "engine": "spark",
            "numOfRecordsPreview": 100,
            "rangeRecordsPreview": {
                "min": 1,
                "max": "5000"
            },
            "description": "Data Pipeline Application",
            "maxConcurrentRuns": 1,
            "pushdownEnabled": false,
            "transformationPushdown": {}
          }
      }
      

## Release notes

  * [January 13, 2025](https://docs.cloud.google.com/data-fusion/docs/release-notes#January_13_2025)
  * [May 21, 2024](https://docs.cloud.google.com/data-fusion/docs/release-notes#May_21_2024)
  * [September 5, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#September_05_2023)
  * [July 26, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#July_26_2023)
  * [June 2, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#June_02_2023)
  * [January 5, 2023](https://docs.cloud.google.com/data-fusion/docs/release-notes#January_05_2023)



## What's next

  * Learn more about [SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
