---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/capture-monetization-data/
title: Capturing monetization data \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:36.959463+00:00
---

# Capturing monetization data  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/capture-monetization-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Capturing monetization data Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee uses the monetization variables for rating, calculating revenue share, and analytics. If you want your Apigee analytics to show the monetization information. By using the monetization variables, you can enhance the monetization capabilities of your transactions. 

## Monetization variables

The monetization variable names are predefined, and you can't create, edit, or delete the variables. You can assign either request or response variables to the monetization variables. 

If you want to override monetization variables, you can do so by capturing them using the [DataCapture policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/data-capture-policy). 

This table describes the monetization variables available in Apigee:

Monetization variable | Data type | Description  
---|---|---  
currency | String | Specifies the currency for calculating the revenue from a transaction.  
perUnitPriceMultiplier | Float | Specifies the factor (multiplier) by which the per-transaction cost is multiplied. The per-transaction cost is specified in the rate plan's **[Consumption-based fees](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-rate-plans#create)** pricing. The multiplication is performed for a transaction only if the transaction is monetizable. A transaction is monetizable if any one of the following condition is satisfied: 

  * If the `transactionSuccess` variable is `true`.
  * If the `transactionSuccess` variable is `NULL` and the `message.status.code` is `2xx` (success).

  
revShareGrossPrice | Float | Specifies the revenue of the transaction for calculating the app developer's or AppGroup's share. Apigee calculates the share only if you have enabled revenue sharing in your rate plan.  
transactionSuccess | boolean | Specifies if the transaction should be monetized. 

  * If the variable is set to `true`, the transaction is monetized.
  * If the variable is set to `false`, the transaction is not monetized.
If you don't specify this variable, the transactions are monetization based on the value of the HTTP status code available in the `message.status.code` variable. If the HTTP status code of the response is NULL or >=300, a transaction is not monetized; for all other status codes, the transaction is monetized. 
**Note:** If the value of `transactionSuccess` is anything other than a boolean, then the DataCapture policy evaluates the [`mint.tx_success_result`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#mint) variable to `false`.  
**Note** : 

  * The monetization variables are not visible in the Apigee's `Admin > Data Collectors` page.
  * The monetization variables are case sensitive.
  * Apart from the variable names listed in the table, you cannot provide any other names for the monetization variables.
  * The monetization variables are not listed in the [organizations.datacollectors.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/list) API.



## Value assignment examples

The following examples show how to assign values to the monetization variables:

### currency

The following example assigns the value of the `booking[0].currency` JSON element in the response to the `currency` variable:
    
    
    <Capture>
      <Collect>
        <Source>response</Source>
        <JSONPayload>
          <JSONPath>booking[0].currency</JSONPath>
        </JSONPayload>
      </Collect>
      <DataCollector scope="monetization">currency</DataCollector>
    </Capture>
        

### perUnitPriceMultiplier

The following example assigns the value of the `booking[0].factor` JSON element in the response to the `perUnitPriceMultiplier` variable:
    
    
    <Capture>
      <Collect>
        <Source>response</Source>
        <JSONPayload>
          <JSONPath>booking[0].factor</JSONPath>
        </JSONPayload>
      </Collect>
      <DataCollector scope="monetization">perUnitPriceMultiplier</DataCollector>
    </Capture>
        

### revShareGrossPrice

The following example assigns the value of the `minPrice` variable in the response header to the `revShareGrossPrice` variable:
    
    
    <Capture>
      <Collect>
        <Source>response</Source>
        <Header name="minPrice">
          <Pattern ignoreCase="true">{$}</Pattern>
        </Header>
      </Collect>
      <DataCollector scope="monetization">revShareGrossPrice</DataCollector>
    </Capture>
        

### transactionSuccess

The following example assigns the value of the `bookingStatus` variable in the response header to the `transactionSuccess` variable:
    
    
    <Capture>
      <Collect>
        <Source>response</Source>
        <Header name="bookingStatus">
          <Pattern ignoreCase="true">{$}</Pattern>
        </Header>
      </Collect>
      <DataCollector scope="monetization">transactionSuccess</DataCollector>
    </Capture>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
