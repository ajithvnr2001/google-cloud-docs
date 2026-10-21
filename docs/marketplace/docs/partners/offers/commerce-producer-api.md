---
url: https://docs.cloud.google.com/marketplace/docs/partners/offers/commerce-producer-api/
title: Create and manage private offers using the API \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:56.330744+00:00
---

# Create and manage private offers using the API  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/offers/commerce-producer-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Go to market ](https://docs.cloud.google.com/marketplace/docs/partners/gtm)



Send feedback 

#  Create and manage private offers using the API Stay organized with collections  Save and categorize content based on your preferences. 

The Commerce Producer API provides programmatic access to private offer creation and publishing for partners and integrators. This API replaces manual operations in Producer Portal, letting partners create, manage, and publish private offers directly from their internal systems or third-party platforms.

## Key benefits

  * **Scale and automation** : Moving from manual portal clicks to programmatic control lets partners scale their transacting volume more efficiently.
  * **Operational efficiency** : Integrating the API reduces deal-desk friction and helps prevent manual errors in the offer creation process.
  * **Speed to market** : By building against the API during the preview, partners are ready to go live immediately upon general availability.



## Target audience

This API is for strategic ISV partners and marketplace integrators who want to automate the creation and management of private offers. When you list or retrieve services, the API returns all of your services. The `productType` field of the `Service` resource identifies the following product types:

  * [Software as a service (SaaS)](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas) (`SOFTWARE_AS_A_SERVICE`)
  * [Professional services](https://docs.cloud.google.com/marketplace/docs/partners/professional-services) (`PROFESSIONAL_SERVICES`)
  * [Data products on BigQuery sharing (formerly Analytics Hub)](https://docs.cloud.google.com/marketplace/docs/partners/data) (`ANALYTICS_HUB_LISTING`)



Services of any other product type report a `productType` of `PRODUCT_TYPE_UNSPECIFIED`. Additional `productType` values might be added over time, so your integration must handle unrecognized values and changes to an existing service's `productType`.

## Before you begin

Before you use the Commerce Producer API, complete the following prerequisites:

  1. **Enable the Commerce Producer API** : Enable the `commerceproducer.googleapis.com` service in your project:
         
         gcloud services enable commerceproducer.googleapis.com
         

For instructions about enabling services, see [Enabling services](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable).

  2. **Set up client libraries** : Download the required SDKs and client libraries. For details, see Client libraries.

  3. **API reference** : To access the API reference, see the [Commerce Producer API reference](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference).




## Standard API flow

Programmatically creating and publishing a private offer requires a specific sequence of API calls. The standard flow consists of the following steps:

  1. **List services** : List the services in your project to find the service to create the private offer against.
  2. **List standard offers** : List the active standard offers under the selected service to find the base standard offer resource name. The resource name is required to create a private offer. 
     * You should list the standard offers that have not expired.
     * If you see multiple standard offers for the same service level with different durations, you can select any of them. They are functionally identical because the private offer duration overrides the standard offer duration.
     * You can only use standard offers that are effective and not expired.
  3. **Find out which offer to amend** : Call [`resolveAmendmentTarget`](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/resolveAmendmentTarget) to see whether your new offer should amend an existing offer or not.
  4. **Create the offer ([`create PrivateOffer`](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/create))**: Call the API to create a new `PrivateOffer` resource in the `DRAFT` state, defining the base details, the customer `billing_name` account, and custom pricing models.
  5. **Attach a document ([`create PrivateOfferDocument`](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers.documents/create) )**: Create a `PrivateOfferDocument` resource and attach it to your draft offer to specify your terms or the EULA. Every private offer must include at least one document before it can be published. A private offer can have at most one document of each type, and can't have both a Standard EULA and a Custom EULA. To check per-type document rules for a service, inspect the `documentRequirement` field of the `Service` resource: 
     * For most services, such as SaaS and data products, `documentRequirement` lists both `STANDARD_END_USER_LICENSE_AGREEMENT_V2` (Standard EULA) and `CUSTOM_END_USER_LICENSE_AGREEMENT` (Custom EULA) as `OPTIONAL` because `documentRequirement` only expresses per-type rules. You must still attach either `STANDARD_END_USER_LICENSE_AGREEMENT_V2` or `CUSTOM_END_USER_LICENSE_AGREEMENT`.
     * For professional services, `STATEMENT_OF_WORK` (SOW) is `REQUIRED`, `CUSTOM_END_USER_LICENSE_AGREEMENT` is `OPTIONAL`, and Standard EULAs are `NOT_ALLOWED`.
     * `STANDARD_END_USER_LICENSE_AGREEMENT_V1` is superseded by `STANDARD_END_USER_LICENSE_AGREEMENT_V2` and is always `NOT_ALLOWED` for new offers.
  6. **Publish the offer ([`publish`](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/publish))**: Call the `publish` method to finalize the offer and make it available for the customer to accept. You can use the `validate_only` flag to validate the offer details without publishing it.



## Key terms and concepts

  * **`PrivateOffer`** : The core resource that represents a custom offer extended to a specific customer. It supports states such as `DRAFT`, `PUBLISHED`, and `ACCEPTED`.
  * **`PrivateOfferDocument`** : An unstructured document attached to a draft private offer, such as a Standard EULA (`STANDARD_END_USER_LICENSE_AGREEMENT_V2`), a Custom EULA (`CUSTOM_END_USER_LICENSE_AGREEMENT`), or a statement of work (`STATEMENT_OF_WORK`). Every private offer must include at least one document before it can be published. A private offer can have at most one document of each type, and can't have both a Standard EULA and a Custom EULA. Which document types are required, optional, or not allowed depends on the `documentRequirement` field of the `Service` resource. Note that `STANDARD_END_USER_LICENSE_AGREEMENT_V1` is superseded and is not allowed for new offers. These documents are immutable once the offer leaves the `DRAFT` state.
  * **`Service`** : The name of the service, which is a read-only resource that represents a product. When this value is set, it helps you find what `StandardOffers` are available under this product. Listing or retrieving services returns all of your services and includes the following fields: 
    * `productType`: The type of product that the service commercializes (`SOFTWARE_AS_A_SERVICE`, `PROFESSIONAL_SERVICES`, or `ANALYTICS_HUB_LISTING`), or `PRODUCT_TYPE_UNSPECIFIED` for any other product type.
    * `documentRequirement`: The per-type requirement levels (`REQUIRED`, `OPTIONAL`, or `NOT_ALLOWED`) for documents attached to private offers on the service. A document type that isn't listed is not allowed. Because `documentRequirement` only expresses per-type rules, it lists both `STANDARD_END_USER_LICENSE_AGREEMENT_V2` and `CUSTOM_END_USER_LICENSE_AGREEMENT` as `OPTIONAL` for services where you must attach one of those two EULA types.
  * **`Sku`** : A stock keeping unit (SKU) representing the atomic unit of pricing and billing. Each customer charge is associated with and originates from exactly one SKU.
  * **`SkuGroup`** : A resource representing a group of SKUs.
  * **`StandardOffer`** : When a `Service` is selected, this lets you determine which service level to create private offers against. Standard offers must be effective and not expired to be used as a base standard offer.



## Client libraries

Use Google Cloud Client Libraries to interact with the API.

  * **Available SDKs** : Google provides auto-generated libraries for Ruby, Java, Python, Go, C#, PHP, and Node.js.
  * **SDK download** : Client library packages are available on GitHub.
  * **General guidance** : For more information about using Google Cloud Client Libraries, see [Cloud Client Libraries by language](https://docs.cloud.google.com/apis/docs/cloud-client-libraries#by_language).
  * **UI equivalents** : To understand how these operations map to the Google Cloud console, read [Create a private offer for a customer](https://docs.cloud.google.com/marketplace/docs/partners/offers/create-private-offers).



## Limitations

The API has the following limitations:

  * **UI visibility for drafts** : Offers that you create or update using the API are not viewable or editable in the Producer Portal UI until you publish them. Similarly, if you create an offer in the Producer Portal but modify it using the API, you can't view or modify the draft in the Producer Portal.



## Roles and permissions

To interact with the Commerce Producer API, you must have the following Identity and Access Management (IAM) roles on the producer project:

  * For read and write actions: `roles/commerceproducer.admin` or `roles/commercepricemanagement.privateOffersAdmin`
    * Alternatively, the basic `roles/editor` role also grants access.
  * For read-only actions: `roles/commerceproducer.viewer` or `roles/commercepricemanagement.viewer`
    * Alternatively, the basic `roles/viewer` role also grants access.



## Configure pricing and schedules

Use the following configurations to set up [pricing models](https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model) and time schedules for your private offers.

### Configure pricing models

To configure different pricing models, set the fields in the `PrivateOffer` resource as described in the following examples:

  * **Flat fee, monthly charge $100, with a 20% usage discount** : 
    * `standard_interval_price.standard_interval`: `MONTHLY_NOT_PRORATED`
    * `standard_interval_price.price_model.flat_fee.flat_fee_override`: `100` (USD)
    * `standard_interval_price.price_model.usage.default_discount_percent`: `20`
  * **Usage-only, 20% usage discount** : 
    * `standard_interval_price.standard_interval`: `STANDARD_INTERVAL_UNSPECIFIED`
    * `standard_interval_price.price_model.usage.default_discount_percent`: `20`
  * **Committed use discount (CUD) with 30% default usage discount (quarterly charge is $100 and quarterly credit is $100; discount applies to usage) and a custom 40% discount on SKU1, quarterly commitment, with credit rollover (unused credits from the previous quarter roll over to the next quarter)** : 
    * `standard_interval_price.standard_interval`: `QUARTERLY_NOT_PRORATED`
    * `standard_interval_price` `.price_model.commitment.commitment_amount`: `100` (USD)
    * `standard_interval_price` `.price_model.commitment.discard_previous_credit_balance`: `false` (Don't discard previous balance to allow credit rollover)
    * `standard_interval_price.price_model.usage.default_discount_percent`: `30`
    * `standard_interval_price` `.price_model.usage.sku_discounts[0].sku`: `SKU1` (Selects `SKU1` to apply a custom discount)
    * `standard_interval_price` `.price_model.usage.sku_discounts[0].discount_percent`: `40` (Specifies a 40% discount on `SKU1` to override the default 30% discount)
  * **CUD with monthly $100 commitment, 20% subscription discount (customer pays $80 monthly charge and receives $100 monthly credit), no credit rollover (unused credits from the previous month do not roll over to the next month)** : 
    * `standard_interval_price.standard_interval`: `MONTHLY_NOT_PRORATED`
    * `standard_interval_price` `.price_model.commitment.commitment_amount`: `100` (USD)
    * `standard_interval_price.price_model.commitment.discount_percent`: `20`
    * `standard_interval_price` `.price_model.commitment.discard_previous_credit_balance`: `true` (Discard previous balance to prevent credit rollover)
  * **Custom installments** : Use `custom_interval_price.installments`. The rules for flat fee and CUD models still apply.
  * **Three installments (Example)** : 
    * Installment 1: $100 commitment, 20% discount (customer pays $80), $25 additional credit (for a total credit of $125). 
      * `custom_interval_price` `.installments[0].price_model.commitment.commitment_amount`: `100`
      * `custom_interval_price` `.installments[0].price_model.commitment.discount_percent`: `20`
      * `custom_interval_price` `.installments[0].price_model.commitment.additional_credit`: `25`
      * `custom_interval_price` `.installments[0].price_model.commitment` `.discard_previous_credit_balance`: `true` or `false` (Unused credits don't exist yet since this is the first installment).
    * Installment 2: $200 commitment, 10% discount (customer pays $180), $25 additional credit (for a total credit of $225). Unused credits from installment 1 won't rollover to installment 2. 
      * `custom_interval_price` `.installments[1].price_model.commitment.commitment_amount`: `200`
      * `custom_interval_price` `.installments[1].price_model.commitment.discount_percent`: `10`
      * `custom_interval_price` `.installments[1].price_model.commitment.additional_credit`: `25`
      * `custom_interval_price` `.installments[1].price_model.commitment` `.discard_previous_credit_balance`: `true` (Discard the previous balance to prevent rollover).
    * Installment 3: $200 commitment, 10% discount (customer pays $180), $0 additional credit (for a total credit of $200). Unused credits from installment 2 will roll over to installment 3. 
      * `custom_interval_price` `.installments[2].price_model.commitment.commitment_amount`: `200`
      * `custom_interval_price` `.installments[2].price_model.commitment.discount_percent`: `10`
      * `custom_interval_price` `.installments[2].price_model.commitment.additional_credit`: `0`
      * `custom_interval_price` `.installments[2].price_model.commitment` `.discard_previous_credit_balance`: `false` (Don't discard the previous balance to allow rollover).



### Configure time schedules

**Note** : In the UI, fields containing "start time," such as the installment start time, represent the start of the day. For example, if you enter `2026-12-31`, the start time is 12:00 AM Pacific Time on `2026-12-31`. In the API, you specify 12:00 AM on `2026-12-31`, so the dates in the UI and the API match.

However, UI fields containing "end time," such as the offer acceptance deadline, represent the end of the day. For example, if you set the deadline to `2026-12-31`, the effective deadline is 12:00 AM Pacific Time on `2027-01-01`. The API displays the date as `2027-01-01`, which means the UI and API dates don't match.

To configure different time schedules, set the fields in the `PrivateOffer` resource as described in the following examples:

  * **Offer starting immediately, with a duration** : 
    * `term.start_policy`: `IMMEDIATE`
    * `term.end_policy`: `AFTER_DURATION`
    * `term.duration_months`: `12`
    * If you use custom installments, the first installment must not set a start time.
  * **Offer starting immediately, ending on a specific date** : 
    * `term.start_policy`: `IMMEDIATE`
    * `term.end_policy`: `SCHEDULED_END_TIME`
    * `term.scheduled_end_time`: `2029-01-01`
    * If you use custom installments, the first installment must not set a start time.
  * **Offer starting on a scheduled date, with a duration** : 
    * `term.start_policy`: `SCHEDULED_START_TIME`
    * `term.scheduled_start_time`: `2027-01-01`
    * `term.end_policy`: `AFTER_DURATION`
    * `term.duration_months`: `12`
    * If you use custom installments, the first installment's start time must match this scheduled start time.
  * **Offer starting on a scheduled date, ending on a specific date** : 
    * `term.start_policy`: `SCHEDULED_START_TIME`
    * `term.scheduled_start_time`: `2027-01-01`
    * `term.end_policy`: `SCHEDULED_END_TIME`
    * `term.scheduled_end_time`: `2029-01-01`
    * If you use custom installments, the first installment's start time must match this scheduled start time.
  * **Offer ending when the amended offer ends** : 
    * `term.end_policy`: `MATCH_AMENDED_OFFER`
    * `term.duration_months`: `12` (Must match the amended offer's duration).



## Commands for each step

Use the following `curl` commands to perform each step in the workflow.

### Step 1: List services

List all services in your project. Use this command to find the service name required to list standard offers.
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
       "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services"
    

To retrieve the full view of a single service, run the following command:
    
    
    curl -G -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/SERVICE_NAME" \
      --data-urlencode 'view=SERVICE_VIEW_FULL'
    

### Step 2: List standard offers

Before you create a private offer, you must associate it with a standard offer by setting the `baseStandardOffer` field. To find active standard offers, list the standard offers and filter by `expire_time`. You should set `expire_time` to now, to ensure all expired standard offers are filtered out.
    
    
    curl -G -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/SERVICE_NAME/standardOffers" \
      --data-urlencode 'filter=expire_time > "2026-05-27T11:30:00-04:00"'
    

To retrieve the full view of a standard offer, run the following command:
    
    
    curl -G -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/SERVICE_NAME/standardOffers/OFFER_ID" \
      --data-urlencode 'view=STANDARD_OFFER_VIEW_FULL'
    

### Step 3: Determine which offer to amend

To determine which offer to amend, call the `resolveAmendmentTarget` method. Depending on the response, you can set the `amendedPrivateOffer` or `amendedStandardOffer` field on the new offer.
    
    
    curl -G \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers:resolveAmendmentTarget" \
      --data-urlencode "targetBillingAccount=billingAccounts/CUSTOMER_BILLING_ACCOUNT" \
      --data-urlencode "baseStandardOffer=projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/SERVICE_NAME/standardOffers/OFFER_ID"
    

When you call `resolveAmendmentTarget`, you must provide the following query parameters:

  * `targetBillingAccount`: The customer's Cloud Billing account that you want to create the private offer for in Step 4.
  * `baseStandardOffer`: The base standard offer that you selected in Step 2.



The following list describes the possible responses from `resolveAmendmentTarget` and how to handle them in Step 4:

  * **Empty response** : Don't set either `amendedPrivateOffer` or `amendedStandardOffer` in the offer that you create.
  * **`requiredPrivateOffer`** : Set the `amendedPrivateOffer` field of the new offer to this value. Format: `projects/PROJECT/locations/global/privateOffers/PRIVATE_OFFER_ID`
  * **`requiredStandardOffer`** : Set the `amendedStandardOffer` field of the new offer to this value. Format: `projects/PROJECT/locations/global/services/SERVICE/standardOffers/OFFER_ID`
  * **`optionalOffers`** : A list of eligible offers that you can amend. Format: `projects/PROJECT/locations/global/privateOffers/PRIVATE_OFFER_ID`

You can perform one of the following actions:

    * Set both `amendedPrivateOffer` and `amendedStandardOffer` to empty. The new offer doesn't amend another offer.
    * Set `amendedPrivateOffer` to one of the resources from the `optionalOffers` list.
  * **`4XX` error**: You can't proceed to Step 4. The error message indicates the reason. For example, one reason this might occur is when multiple subscriptions are disabled and a purchase is pending. You must wait for the pending purchase to be activated or rejected before you continue.


**Note:** You might see subtle differences between the UI flow and the API flow in terms of what is considered as an amendment. If the previous private offer has an `ENDED` state, then the API will require you to specify the `ENDED` offer as the `amendedPrivateOffer`. However, the UI does not show the amendment flow for this case. This difference is by design.

### Step 4: Create a private offer

Create a draft private offer. The following command creates a draft private offer with two installments and an immediate start. Replace the placeholders with your offer details, such as dates, discounts, and the standard offer ID.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
      "title": "Your title",
      "acceptDeadlineTime": {
        "year": 2026,
        "month": 4,
        "day": 24,
        "timeZone": {
          "id": "America/Los_Angeles"
        }
      },
      "singleProductOffer": {
        "baseStandardOffer": "projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/YOUR_SERVICE_NAME/standardOffers/STANDARD_OFFER_ID_FROM_EARLIER",
        "customIntervalPrice": {
          "installments": [
            {
              "priceModel": {
                "commitment": {
                  "commitmentAmount": {
                    "currencyCode": "USD",
                    "units": 500
                  },
                  "discountPercent": {
                    "value": "30"
                  }
                }
              }
            },
            {
              "startTime": {
                "year": 2026,
                "month": 5,
                "day": 17,
                "timeZone": {
                  "id": "America/Los_Angeles"
                }
              },
              "priceModel": {
                "commitment": {
                  "commitmentAmount": {
                    "currencyCode": "USD",
                    "units": 800
                  },
                  "discountPercent": {
                    "value": "20"
                  }
                }
              }
            }
          ]
        }
      },
      "customer": {
        "entityTitle": "customer title",
        "contact": "customer contact",
        "targetBillingAccount": "billingAccounts/CUSTOMER_BILLING_ACCOUNT"
      },
      "partnerContact": {
        "contact": "partner contact",
        "email": "partner@email.com"
      },
      "term": {
        "startPolicy": "IMMEDIATE",
        "endPolicy": "AFTER_DURATION",
        "durationMonths": 2,
        "maxRenewalCount": 0
      },
      "offerDealType": "NEW"
    }' \
    "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers"
    

To verify the creation, list the private offers in your project:
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers"
    

To list private offers and filter by update time, run the following command.
    
    
    curl -G -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers" \
      --data-urlencode 'filter=update_time > "2026-06-25T11:30:00-04:00"' \
      --data-urlencode 'orderBy=update_time desc'
    

To retrieve a specific private offer:
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers/PRIVATE_OFFER_ID"
    

To retrieve the full view of a private offer, which includes additional fields, run the following command:
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers/PRIVATE_OFFER_ID?view=PRIVATE_OFFER_VIEW_FULL"
    

### Step 5: Create a private offer document

You must attach a document, such as a EULA or statement of work (SOW), to publish a private offer. The following command creates and attaches a Standard EULA:
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
      "documentType": "STANDARD_END_USER_LICENSE_AGREEMENT_V2"
    }' \
    "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers/PRIVATE_OFFER_ID/documents"
    

### Step 6: Publish the private offer

Publish the private offer to make it available for the customer to accept. Replace `PRIVATE_OFFER_ID` with the ID of your draft offer.
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{}' \
    "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers/PRIVATE_OFFER_ID:publish"
    

## Examples of private offer configurations

The following examples show how to configure different types of private offers.

**Note:** The following are partial examples, which show only pricing and term related fields.

### Immediate start, multiple installments, commitment discount
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
      "singleProductOffer": {
        "baseStandardOffer": "projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/YOUR_SERVICE_NAME/standardOffers/STANDARD_OFFER_ID",
        "customIntervalPrice": {
          "installments": [
            {
              # This installment is set to start immediately since it does not have a startTime
              "priceModel": {
                "commitment": {
                  "commitmentAmount": {
                    "currencyCode": "USD",
                    "units": 100
                  },
                  "discountPercent": {
                    # The discount % set here will apply to the subscription cost. In this case, customer will
                    # pay $90 and get $100 in credit for this installment.
                    "value": "10"
                  }
                }
              }
            },
            {
              "startTime": {
                "year": 2026,
                "month": 5,
                "day": 17,
                "timeZone": {
                  "id": "America/Los_Angeles"
                }
              },
              "priceModel": {
                "commitment": {
                  "commitmentAmount": {
                    "currencyCode": "USD",
                    "units": 800
                  },
                  "discountPercent": {
                    "value": "20"
                  }
                }
              }
            }
          ]
        }
      },
      "term": {
        "startPolicy": "IMMEDIATE",
        "endPolicy": "AFTER_DURATION",
        "durationMonths": 2,
        "maxRenewalCount": 0
      }
    }' \
    "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers"
    

### Immediate start, multiple installments, usage discount with metric overrides
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
      "singleProductOffer": {
        "baseStandardOffer": "projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/YOUR_SERVICE_NAME/standardOffers/STANDARD_OFFER_ID",
        "customIntervalPrice": {
          "installments": [
            {
              # This installment starts immediately (no startTime is set).
              "priceModel": {
                "usage": {
                  "defaultDiscountPercent": {
                    # This is the default discount percentage on the usage skus.
                    "value": "20"
                  },
                  "skuDiscounts": [
                    {
                      # Sku IDs are retrieved from the standard offer.
                      "sku": "projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/YOUR_SERVICE_NAME/skus/SKU1_ID",
                      "discountPercent": {
                        "value": "50"
                      }
                    },
                    {
                      "sku": "projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/YOUR_SERVICE_NAME/skus/SKU2_ID",
                      "discountPercent": {
                        "value": "30"
                      }
                    }
                  ]
                },
                "commitment": {
                  # The customer receives usage discounts: they pay $200 for this
                  # installment, receive $200 in credit, and get 20% discount on
                  # usage skus except SKU1 and SKU2.
                  "commitmentAmount": {
                    "currencyCode": "USD",
                    "units": "200"
                  }
                }
              }
            },
            {
              "startTime": {
                "year": 2026,
                "month": 5,
                "day": 14,
                "timeZone": {
                  "id": "America/Los_Angeles"
                }
              },
              "priceModel": {
                "usage": {
                  "defaultDiscountPercent": {
                    "value": "20"
                  }
                },
                "commitment": {
                  "commitmentAmount": {
                    "currencyCode": "USD",
                    "units": "10000"
                  }
                }
              }
            }
          ]
        }
      },
      "term": {
        "startPolicy": "IMMEDIATE",
        "endPolicy": "AFTER_DURATION",
        "durationMonths": 2,
        "maxRenewalCount": 0
      }
    }' \
    "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers"
    

### Immediate start, pay-as-you-go (PAYG) only
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
      "singleProductOffer": {
        "baseStandardOffer": "projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/YOUR_SERVICE_NAME/standardOffers/STANDARD_OFFER_ID",
        "standardIntervalPrice": {
          "priceModel": {
            "usage": {
              "defaultDiscountPercent": {
                # This is the default discount percentage on the usage skus.
                "value": "34"
              }
            }
          }
        }
      },
      "term": {
        "startPolicy": "IMMEDIATE",
        "endPolicy": "AFTER_DURATION",
        "durationMonths": 3,
        "maxRenewalCount": 0
      }
    }' \
    "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers"
    

### Scheduled start, monthly interval, flat fee and usage
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
      "singleProductOffer": {
        "baseStandardOffer": "projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/services/YOUR_SERVICE_NAME/standardOffers/STANDARD_OFFER_ID",
        "standardIntervalPrice": {
          "standardInterval": "MONTHLY_NOT_PRORATED",
          "priceModel": {
            "usage": {
              "defaultDiscountPercent": {
                # This is the default discount percentage on the usage skus.
                "value": "20"
              }
            },
            "flatFee": {
              "flatFeeOverride": {
                "currencyCode": "USD",
                "units": "400"
              }
            }
          }
        },
        "features": [
          {
            "displayName": "Feature display name",
            "value": "Feature value"
          }
        ]
      },
      "term": {
        "startPolicy": "SCHEDULED_START_TIME",
        "scheduledStartTime": {
          "year": 2026,
          "month": 5,
          "day": 6,
          "timeZone": {
            "id": "America/Los_Angeles"
          }
        },
        "endPolicy": "AFTER_DURATION",
        "durationMonths": 12,
        "maxRenewalCount": 1
      }
    }' \
    "https://commerceproducer.googleapis.com/v1beta/projects/YOUR_PROJECT_ID_OR_NUMBER/locations/global/privateOffers"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
