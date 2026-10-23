---
url: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-rate-plans/
title: Managing rate plans for API products \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:54.797498+00:00
---

# Managing rate plans for API products  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-rate-plans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing rate plans for API products Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Using rate plans, API product owners can monetize their API products by configuring the following:

  * Billing account model
  * Currency used for billing
  * Frequency at which customers are billed (monthly only)
  * Initial setup fees for using an API product
  * Consumption-based charges for using an API product
  * Any recurring fees not based on consumption, such as monthly fees for access to your API product
  * Time interval during which the rate plan is in effect for an API product (rate plan activation and expiration times)
  * Revenue sharing with developer partners

**Note:** You can associate multiple rate plans with the same API product but **only one** rate plan can be active at any point of time.

Manage rate plans for your API products as described in the following sections.

**Important:** If your Apigee organization uses [ data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts), you can use either the Apigee UI or the Apigee APIs to manage monetization.

##  Viewing rate plans 

View rate plans in your organization as described in the following sections. 

### Apigee UI

View rate plans as described in the following sections: 

  * Viewing rate plans defined for your organization
  * Viewing rate plans associated with an API product



#### Viewing rate plans defined for your organization

View rate plans defined for your organization on the Rate plans page. 

To access the Rate plans page: 

In the Google Cloud console, go to the **Apigee > Distribution > Monetization** page.

[Go to Monetization](https://console.cloud.google.com/apigee/monetization)

The Rate Plans page opens and lists the current rate plans.

![List of rate plans showing rate plan name, API product, and activation and expiration times for each, plus the menu that can be used to manage the rate plan](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/rate-plans-console.png)

The Rate Plans page enables you to: 

  * Create new rate plans by clicking **Create**.
  * Update rate plans by clicking the rate plan name.
  * Manage rate plans from the more_vert menu: 
    * Set the activation and expiration times for a rate plan
    * Publish a rate plan (only available for draft rate plans)
    * Move a published rate plan to draft status (only available for published rate plans)
    * Clone a rate plan
    * Delete a rate plan
  * View details about each rate plan including associated API product, status (`Published` or `Draft`) and whether it is active, and activation and expiration times



#### Viewing rate plans associated with an API product

When [managing an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products), you can view and manage the rate plans associated with an API product. Scroll down to the **Rate plan** section to see the rate plans. 

### Apigee API

The following sections describe how to view rate plans for an organization using the API: 

  * Listing the rate plans for an API product
  * Viewing details for a rate plan



#### Listing the rate plans for an API product using the API

To list the rate plans for the organization, issue a `GET` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans`

For example using curl:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans?expand=true" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output, including the two rate plans, `myrateplan1` and `myrateplan2` associated with `HelloworldProduct` API product:
    
    
    {
        "ratePlans": [
            {
                "name": "6b51b501-ac15-41b7-bb3e-621edb849e13",
                "apiproduct": "HelloworldProduct",
                "displayName": "myrateplan2",
                "billingPeriod": "MONTHLY",
                "currencyCode": "USD",
                "setupFee": {
                    "currencyCode": "USD",
                    "units": "20"
                },
                "fixedRecurringFee": {
                    "currencyCode": "USD",
                    "units": "25"
                },
                "fixedFeeFrequency": 1,
                "consumptionPricingType": "FIXED_PER_UNIT",
                "consumptionPricingRates": [
                    {
                        "fee": {
                            "currencyCode": "USD",
                            "nanos": 500000000
                        }
                    }
                ],
                "revenueShareType": "FIXED",
                "revenueShareRates": [
                    {
                        "sharePercentage": 2
                    }
                ],
                "state": "DRAFT"
            },
            {
                "name": "8c0b527c-ba2f-45f1-ac1c-b9e891546fc2",
                "apiproduct": "HelloworldProduct",
                "displayName": "myrateplan1",
                "billingPeriod": "MONTHLY",
                "currencyCode": "USD",
                "consumptionPricingType": "FIXED_PER_UNIT",
                "consumptionPricingRates": [
                    {
                        "fee": {
                            "currencyCode": "USD",
                            "units": "3"
                        }
                    }
                ],
                "state": "PUBLISHED",
                "startTime": "1617302588000"
            }
        ]
    }

For more information about the API and its response payload, see the [List rate plans API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/list)

#### Viewing details for a rate plan using the API

To view details for a rate plan, issue a `GET` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME`

To determine the name of the rate plan to pass in the resource path, see Listing the rate plans in an organization. 

For example using curl:
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output for the rate plan with the name `6b51b501-ac15-41b7-bb3e-621edb849e13` and display name `myrateplan2`:
    
    
    {
        "name": "6b51b501-ac15-41b7-bb3e-621edb849e13",
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan2",
        "billingPeriod": "MONTHLY",
        "currencyCode": "USD",
        "setupFee": {
            "currencyCode": "USD",
            "units": "20"
        },
        "fixedRecurringFee": {
            "currencyCode": "USD",
            "units": "25"
        },
        "fixedFeeFrequency": 1,
        "consumptionPricingType": "FIXED_PER_UNIT",
        "consumptionPricingRates": [
            {
                "fee": {
                    "currencyCode": "USD",
                    "nanos": 500000000
                }
            }
        ],
        "revenueShareType": "FIXED",
        "revenueShareRates": [
            {
                "sharePercentage": 2
            }
        ],
        "state": "DRAFT"
    }

For more information about the API and its response payload, see the [Get rate plan API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/get).

## Creating rate plans

Create rate plans as described in the following sections. 

### Apigee UI

To create a rate plan:

  1. In the Google Cloud console, go to the **Apigee > Distribution > Monetization** page.

[Go to Monetization](https://console.cloud.google.com/apigee/monetization)

  2. Perform one of the following tasks: 
     * Click **Create**.
     * [Edit an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#edit) and click **Add rate plan** in the **Rate plans** section.
  3. Enter **Rate plan details** , as follows: Field | Description  
---|---  
Rate plan name | Enter the name of the rate plan.  
API product | Select an API product to which you want to associate the rate plan from the drop-down.  
  4. Click **Next**.
  5. Enter **Billing** details, as follows: Field | Description | Default  
---|---|---  
Billing currency | Select the currency to use for billing from the drop-down. | USD  
Billing period | Select the frequency at which the customer will be billed from the drop-down. **Note:** `Monthly` is the only valid option in this release. | Monthly  
Initialization fee | A one-time fee that is charged to each developer on the start date of the rate plan (that is, the date the developer purchases the API product). If you want to charge the setup fee, select **Charge initialization fee** and enter the amount to be charged in the **Initialization fee** field.  | Disabled  
  6. Click **Next**.
  7. Enter **Pricing** details as follows. Field | Description | Default  
---|---|---  
Fixed recurring fee | Enable a fixed recurring fee per unit: 
     1. Select **Charge fixed recurring fee**.
     2. Configure the **Fixed fee frequency** and **Fixed recurring fee** amount.
The fee will be prorated for the first billing period.  If enabled, you can preview the effects that the fixed recurring fee will have on the itemized and total charges, as described in Previewing your rate plan. To disable the fee, deselect **Charge fixed recurring fee**.  | Disabled  
Consumption based fees | Enable consumption-based pricing: 
     1. Select **Charge consumption-based fee**. 
     2. Select any one of the following options: 
        * Fixed fee per unit (flat fee per unit consumed)
        * Banded (a variable fee per unit consumed, determined by consumption ranges)
     * **Fixed fee per unit:** A fixed fee is charged for each monetized transaction. Enter a value in the **Fixed fee per unit** field which should be charged for every transaction.
     * **Banded:** A variable fee is charged for each monetized transaction. The transaction band and the consumption determine the fees of a transaction. A band refers to an API consumption range, and each band has a different fee. In the `Ranges of unit consumption` section, you can specify the band ranges and the corresponding fees for the band. You can specify as many bands you want by clicking **\+ BAND**. **Example:** Consider you want to charge the first 1000 API calls at USD 2 per call and all subsequent API calls at USD 1 per call. To configure this, specify the following two bands in the `Ranges of unit consumption` section:
       * In the first row, enter the following values: 
         * **Start:** 0
         * **End:** 1000
         * **Fee:** 2
       * In the second row, enter the following values: 
         * **Start:** 1001
         * **End:** unlimited units
         * **Fee:** 1
In this example, if a developer consumes 1500 APIs, the total fees will be USD 2500 `((1000 * 2) + (500 * 1))`.
If you enable any consumption-based fees, you can preview the effects of the selected fee type on the overall revenue as described in Previewing your rate plan. To disable the fee, deselect **Charge consumption-based pricing model**.  If you have configured the `[perUnitPriceMultiplier](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/capture-monetization-data#monetization-variables)` monetization variable in your DataCapture policy, the per-transaction cost specified in any type (Fixed fee per unit or Banded) of consumption-based fees is multiplied by the value of `perUnitPriceMultiplier`. **Note:** A transaction is monetized based on the value of the `transactionSuccess` monetization variable. For more information, see [ Monetization variables](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/capture-monetization-data#monetization-variables). | Disabled  
  8. Click **Next**.
  9. Enter **Revenue sharing** details, as follows: Field | Description | Default  
---|---|---  
Revenue share | Enable revenue sharing to share a percentage of revenue with developer partners. 
     1. Select **Enable revenue sharing**.
     2. Enter a percentage of revenue to share in the **Percentage (%) of revenue to share with developer** field.
You can get the shared revenue for each monetized transaction by configuring the `revShareGrossPrice` monetization variable in your DataCapture policy. For more information, see [ Monetization variables](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/capture-monetization-data#monetization-variables). If you enable revenue sharing, you can preview the effects of the entered **Percentage (%)** value on the itemized and total charges, as described in Previewing your rate plan. To disable the fee, deselect **Enable revenue sharing**.  | Disabled  
  10. Click **Next**.
  11. Click one of the following: 
     * **Save and publish** to save and publish the rate plan. You will be prompted for an activation date. For more information, see Setting the activation date for your rate plan.
     * **Save** to save a draft of the rate plan.
     * **Cancel** to cancel.



### Apigee API

To create a rate plan, issue a `POST` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans`

Configure the rate plan by passing the required fields in the request body, as described in [Resource: RatePlans](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans). 

The following table summarizes the required fields when creating a draft and published rate plan. 

Required fields for draft rate plan | Required fields for published rate plan  
---|---  
  
  * `apiproduct`
  * `displayName`
  * `state`

| 

  * `apiproduct`
  * `billingPeriod`
  * `currencyCode`
  * `displayName`
  * `startTime`
  * `state`

  
**Note:** To publish a rate plan, see Publishing a rate plan

For example, the following API call creates a draft rate plan named `myrateplan5` associated with the `HelloworldProduct` API product: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/HelloworldProduct/rateplans" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "apiproduct":"HelloworldProduct",
        "billingPeriod":"MONTHLY",
        "consumptionPricingType":"FIXED_PER_UNIT",
        "consumptionPricingRates":[{
           "fee":{
              "units":"3",
              "nanos":0
            }
        }],
        "currencyCode":"USD",
        "displayName":"myrateplan5",
        "revenueShareType":"FIXED",
        "revenueShareRates":[{
           "sharePercentage":"1"
        }],
        "setupFee":{
           "units":"10",
           "nanos":0
         },
    	 "state":"DRAFT"
        }'
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
        "name": "4403a3a5-b366-44f0-aa4d-bd54dcfd3239",
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan5",
        "billingPeriod": "MONTHLY",
        "currencyCode": "USD",
        "setupFee": {
            "currencyCode": "USD",
            "units": "10"
        },
        "consumptionPricingType": "FIXED_PER_UNIT",
        "consumptionPricingRates": [
            {
                "fee": {
                    "currencyCode": "USD",
                    "units": "3"
                }
            }
        ],
        "revenueShareType": "FIXED",
        "revenueShareRates": [
            {
                "sharePercentage": 1
            }
        ],
        "state": "DRAFT"
    }

For more information, see the [Create rate plan API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/create)

##  Previewing your rate plan in the UI 

  1. In the Google Cloud console, go to the **Distribution > Monetization** page.

[Go to Monetization](https://console.cloud.google.com/apigee/monetization)

  2. Click an existing Rate plan or click **Create**.
  3. Based on your pricing and revenue share configuration, you can preview the itemized charges and billed totals in the **Rate plan preview** section of the **Rate plan** page, as shown in the following figure. 

![Enter example values, see results in the rate plan preview](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/rate-plan-preview.png)

  4. Update the **API unit consumption** field in the **Example consumer data** section to change the estimates in the preview. The itemized charges and totals update based on your input. 

  5. Update the following fields in the **Example consumer data** section:

     * **API unit consumption**  
If **Charge consumption-based fee** is selected under **Pricing**.
     * **Revenue**  
If **Enable revenue sharing** is selected under **Revenue sharing**.



## Setting the activation and expiration times for rate plans

Set activation and expiration times for a rate plan to indicate when a published rate plan is **active** and that the associated API product is available for developers to use in their apps.

Consider the following when setting activation and expiration times: 

  * Only **one rate plan can be active** for an API product at any given time.
  * You can publish multiple rate plans for the same API product with non-overlapping activation and expiration times.
  * You must set the activation time for a rate plan before it can be published.   
When publishing a rate plan using the UI, you will be prompted to set the activation time if it is not set.
  * The activation time must occur before the expiration time (if set), and the expiration time must occur after the activation time.
  * The expiration time is not required. If not specified, the expiration defaults to `Never` (the rate plan never expires).
  * When setting the activation and expiration times using the UI, you can specify only the date and not the time of day (`hh:mm:ss:mmm`). The time of day for the activation and expiration values defaults to `12:00:00:000 AM` and `11:59:59:999 PM`, respectively. 



Set the activation and expiration times for rate plans as described in the following sections.

### Apigee UI

To set the **activation time** for a rate plan:

  1. Access the Rate Plans page.
  2. Click more_vert**More** and then **Set activation** for the rate plan for which you want to set the activation time.
  3. Select one of the following options: 
     * **Undetermined** to unset the rate plan activation time (available for draft rate plans only).
     * **Immediately** to set the rate plan as active immediately.
     * **On a future date** to select the date on which the rate plan will be active. 
  4. Click **Set activation**.
  5. Publish the rate plan if it is not yet published to make it available to developers to use in their apps.



To set the **expiration time** for a rate plan:

  1. Access the Rate Plans page.
  2. Click more_vert**More** and then **Set expiration** for the rate plan for which you want to set the expiration time.
  3. Select one of the following options: 
     * **Never** (default) to never expire the rate plan.
     * **Immediately** to set the rate plan as active immediately.
     * **On a future date** to select the date on which the rate plan will be active.
  4. Click **Set expiration**.



### Apigee API

To set the activation or expiration times for a rate plan using the API: 

  1. View the details for the rate plan you want to update.
  2. Use the response to create the request body and update the following fields: 
     * **startTime** to set the activation time
     * **endTime** to set the expiration time
**Note:** When updating a rate plan using the API, the configuration settings you specify in your request **replace** all existing settings. Be sure to specify values for all settings that you want to maintain even if they are not changing; otherwise, the settings will be removed. 
  3. To update the rate plan with the new configuration, issue a `PUT` request to the following API, passing the modified request body in your request: `https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME`




For example, the following sets the activation time to April 1, 2021 (`1617302588000` epoch time): 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME" \
      -X PUT \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "currencyCode":"USD",
        "billingPeriod":"MONTHLY",
        "consumptionPricingType":"FIXED_PER_UNIT",
        "consumptionPricingRates":[{
           "fee":{
              "units":"3",
              "nanos":0
            }
        }],
        "revenueShareType":"FIXED",
        "revenueShareRates":[{
           "sharePercentage":"5"
        }],
        "state":"DRAFT",
        **"startTime": 1617302588000**
        }'
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

For more information about the fields you can specify in the request body, see [Resource: RatePlans](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans). 

The following provides an example of the response output:
    
    
    {
        "name": "cb9f420e-313d-4900-aa4f-e07b2b76918d",
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "billingPeriod": "MONTHLY",
        "currencyCode": "USD",
        "consumptionPricingType": "FIXED_PER_UNIT",
        "consumptionPricingRates": [
            {
                "fee": {
                    "currencyCode": "USD",
                    "units": "3"
                }
            }
        ],
        "revenueShareType": "FIXED",
        "revenueShareRates": [
            {
                "sharePercentage": 5
            }
        ],
        "state": "DRAFT",
        "startTime": "1617302588000"
    }
    

For more information, see the [Update rate plan API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/update)

##  Publishing rate plans 

Publish rate plans as described in the following sections. 

**Note:** Only **one rate plan can be active** for an API product at any given time. You can publish rate plans for the same API product with non-overlapping activation and expiration times.

### Apigee UI

To publish a rate plan using the UI, use one of the following methods: 

  * When creating or updating a rate plan, you can click **Save and Publish** to save and publish the rate plan. You will be prompted to set the activation date.
  * Access the Rate Plans page and click more_vert and then **Publish** for the draft rate plan you want to publish. 

This option appears only if you have set an activation date for the draft rate plan.




### Apigee API

To publish a rate plan using the API: 

  1. View the details for the rate plan you want to publish.
  2. Use the response to create the request body and update the following fields: 
     * Set **state** to **PUBLISHED**.
     * Set **startTime** to the activation time in milliseconds since epoch.
     * Optionally, set **endTime** to the expiration time in milliseconds since epoch or to **Never**. If omitted, the expiration time defaults to `Never`.
     * Set any other fields that you wish to maintain. **Note:** When updating a rate plan using the API, the configuration settings you specify in your request **replace** all existing settings. Be sure to specify values for all settings that you want to maintain even if they are not changing; otherwise, the settings will be removed. 
  3. To publish the rate plan, issue a `PUT` request to the following API, passing the modified request body in your request: `https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME`




For example, the following changes the status of the `rateplan1` rate plan to `PUBLISHED` and sets the activation time to April 1, 2021, specified as milliseconds since epoch: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME" \
      -X PUT \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "currencyCode":"USD",
        "billingPeriod":"MONTHLY",
        "consumptionPricingType":"FIXED_PER_UNIT",
        "consumptionPricingRates":[{
           "fee":{
              "units":"3",
              "nanos":0
            }
        }],
        "revenueShareType":"FIXED",
        "revenueShareRates":[{
           "sharePercentage":"5"
        }],
        "state":"PUBLISHED",
        "startTime": 1617302588000
        }'
    

For more information about the fields you can specify in the request body, see [Resource: RatePlans](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans). 

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
        "name": "cb9f420e-313d-4900-aa4f-e07b2b76918d",
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "billingPeriod": "MONTHLY",
        "currencyCode": "USD",
        "consumptionPricingType": "FIXED_PER_UNIT",
        "consumptionPricingRates": [
            {
                "fee": {
                    "currencyCode": "USD",
                    "units": "3"
                }
            }
        ],
        "revenueShareType": "FIXED",
        "revenueShareRates": [
            {
                "sharePercentage": 5
            }
        ],
        "state": "PUBLISHED",
        "startTime": "1617302588000"
    }

For more information, see the [Update rate plan API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/update)

##  Moving published rate plans to draft status 

Move published rate plans to draft status as described in the following sections. 

### Apigee UI

To move a published rate plan to draft status:

  1. Access the Rate Plans page.
  2. Select more_vert**More** and then **Move to draft**.



The rate plan is updated and the `Status` field is changed to **Draft**.

### Apigee API

To move a published rate plan to draft status using the API: 

  1. View the details for the published rate plan you want to move to draft status.
  2. Use the response to create the request body and update the following fields: 
     * Set **state** to **DRAFT**.
     * Set any other fields that you wish to maintain. **Note:** When updating a rate plan using the API, the configuration settings you specify in your request **replace** all existing settings. Be sure to specify values for all settings that you want to maintain even if they are not changing; otherwise, the settings will be removed. 
  3. To move the published rate plan to draft status, issue a `PUT` request to the following API, passing the modified request body in your request: `https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME`




For example, the following changes the status of the `rateplan1` rate plan to `DRAFT`: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME" \
      -X PUT \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "currencyCode":"USD",
        "billingPeriod":"MONTHLY",
        "consumptionPricingType":"FIXED_PER_UNIT",
        "consumptionPricingRates":[{
           "fee":{
              "units":"3",
              "nanos":0
            }
        }],
        "revenueShareType":"FIXED",
        "revenueShareRates":[{
           "sharePercentage":"5"
        }],
        **"state":"DRAFT",**
        "startTime": 1617302588000
        }'
    

For more information about the fields you can specify in the request body, see [Resource: RatePlans](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans). 

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
        "name": "cb9f420e-313d-4900-aa4f-e07b2b76918d",
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "billingPeriod": "MONTHLY",
        "currencyCode": "USD",
        "consumptionPricingType": "FIXED_PER_UNIT",
        "consumptionPricingRates": [
            {
                "fee": {
                    "currencyCode": "USD",
                    "units": "3"
                }
            }
        ],
        "revenueShareType": "FIXED",
        "revenueShareRates": [
            {
                "sharePercentage": 5
            }
        ],
        "state": "DRAFT",
        "startTime": "1617302588000"
    }
    

For more information, see the [Update rate plan API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/update)

## Updating rate plans

Update a rate plan as described in the following sections. 

### Apigee UI

To update a rate plan using the UI:

  1. Access the Rate Plans page.
  2. Click the name of the rate plan that you want to update in the list.
  3. Update the rate plan, as required.
  4. Click one of the following: 
     * **Save and publish** to save and publish the rate plan. You will be prompted for an activation date. For more information, see Setting the activation date for a rate plan.
     * **Save** to save a draft of the rate plan.
     * **Cancel** to cancel your updates.



### Apigee API

To update a rate plan using the API: 

  1. View the details for the rate plan you want to update.
  2. Use the response to create the request body and update any other configuration settings, as required. **Note:** When updating a rate plan using the API, the configuration settings you specify in your request **replace** all existing settings. Be sure to specify values for all settings that you want to maintain even if they are not changing; otherwise, the settings will be removed. 
  3. To update a rate plan, issue a `PUT` request to the following API, passing the modified request body in your request: `https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME`




For example, the following changes the consumption-based fee to **5** ; and the revenue share percentage to **6.5%** all other configuration settings are included to ensure that they are maintained: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME" \
      -X PUT \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "currencyCode":"USD",
        "billingPeriod":"MONTHLY",
        "consumptionPricingType":"FIXED_PER_UNIT",
        "consumptionPricingRates":[{
           "fee":{
              **"units":"5"** ,
              "nanos":0
            }
        }],
        "revenueShareType":"FIXED",
        "revenueShareRates":[{
           **"sharePercentage":"6.5"**
        }],
        "state":"DRAFT",
        "startTime": 1617302588000
        }'
    

For more information about the fields you can specify in the request body, see [Resource: RatePlans](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans). 

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
        "name": "cb9f420e-313d-4900-aa4f-e07b2b76918d",
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "billingPeriod": "MONTHLY",
        "currencyCode": "USD",
        "consumptionPricingType": "FIXED_PER_UNIT",
        "consumptionPricingRates": [
            {
                "fee": {
                    "currencyCode": "USD",
                    "units": "5"
                }
            }
        ],
        "revenueShareType": "FIXED",
        "revenueShareRates": [
            {
                "sharePercentage": 6.5
            }
        ],
        "state": "DRAFT",
        "startTime": "1617302588000"
    }
    

For more information, see the [Update rate plan API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/update)

When updating the **active published rate plan** , choose one of the following methods: Method | Considerations  
---|---  
Update the rate plan | Changes take effect immediately for the active published rate plan. In this case, it may not be immediately apparent why the rate plan changes have taken effect.  
Publish a new version of the rate plan | Charges are tracked against the new active published rate plan which may facilitate tracking. To publish a new version of the rate plan:

  1. Clone the existing rate plan. 
  2. Edit the cloned version of the rate plan, as required.
  3. Expire immediately or move to draft the existing rate plan.
  4. Publish immediately the new version of the rate plan.

  
See also: 

  * Publishing rate plans
  * Setting the activation and expiration times for a rate plan



## Cloning rate plans

Clone rate plans to create duplicate rate plans based on existing rate plans. 

### Apigee UI

To clone a rate plan using the UI:

  1. Access the Rate Plans page.
  2. Select more_vert and then **Clone**.
  3. Update the **Rate plan name** and **API product** fields.
  4. Click **Clone**.



The rate plan is added to the list of rate plans.

### Apigee API

To clone a rate plan using the API:

  1. View the details for the rate plan you want to clone.
  2. Use the response to create the request body and update the following fields: 
     * Remove the **name** field.
     * Update any other configuration settings, as required. **Note:** When updating a rate plan using the API, the configuration settings you specify in your request **replace** all existing settings. Be sure to specify values for all settings that you want to maintain even if they are not changing; otherwise, the settings will be removed. 
  3. Create a rate plan by passing the modified request body in your request.



##  Deleting rate plans 

Deleting a rate plan is permanent. The rate plan will be deleted immediately and cannot be restored.

**Caution:** Before deleting a rate plan, ensure that there are no active transactions in progress. 

Delete rate plans as described in the following sections.

### Apigee UI

To delete a rate plan using the UI:

  1. Access the Rate Plans page.
  2. Select more_vert and then **Delete** for the rate plan that you want to delete.
  3. Confirm that this is the correct rate plan to delete and click **Delete**.



The rate plan is deleted and removed from the list.

### Apigee API

To delete a rate plan, issue a `DELETE` request to the following API: `https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME`.

To determine the name of the rate plan to pass in the resource path, see Listing the rate plans in an organization. 

For example, the following deletes the rate plan with name `cc6252c0-c5d0-4aaf-85f2-203ec8fa5707` and display name `myrateplan3`: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/**$ORG** /apiproducts/**$APIPRODUCT** /rateplans/$RATEPLAN_NAME" \
      -X DELETE \
      -H "Authorization: Bearer $TOKEN
    

Where `$TOKEN` is set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). For a description of environment variables you can use, see [Setting environment variables for Apigee API requests](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#api-environment-variables).

The following provides an example of the response output:
    
    
    {
        "name": "93ca14aa-7a48-4384-ae09-c85a0e8a8df8",
        "apiproduct": "HelloworldProduct",
        "displayName": "myrateplan3",
        "billingPeriod": "MONTHLY",
        "currencyCode": "USD",
        "consumptionPricingType": "FIXED_PER_UNIT",
        "consumptionPricingRates": [
            {
                "fee": {
                    "currencyCode": "USD",
                    "units": "5"
                }
            }
        ],
        "revenueShareType": "FIXED",
        "revenueShareRates": [
            {
                "sharePercentage": 6.5
            }
        ],
        "state": "DRAFT",
        "startTime": "1617302588000"
    }

For more information, see the [Delete rate plans API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans/delete).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
