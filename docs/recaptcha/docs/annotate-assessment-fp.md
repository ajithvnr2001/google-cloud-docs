---
url: https://docs.cloud.google.com/recaptcha/docs/annotate-assessment-fp/
title: Annotate assessments with transaction events \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:04.642880+00:00
---

# Annotate assessments with transaction events  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/annotate-assessment-fp/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Annotate assessments with transaction events Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to annotate assessments with transaction events to refine your site-specific model.

For best performance, Transaction defense needs visibility into payment lifecycle events for transactions. Therefore, we recommend that you send annotations for the assessments that you created with transaction data. For example, you can provide the transaction information to Transaction defense as a transaction event in the following scenarios:

  * The payment provider accepts or declines the transaction.

  * The merchant issues a refund.

  * The payment issuer files a refund.




To learn more about how to send annotations, see [Annotate assessments](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment).

We recommend that you make these requests automatically as part of the corresponding logic in your system when the data is available, such as when the status of a transaction changes.

After you create an assessment with included transaction data, Transaction defense returns a verdict and an [assessment name](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#Assessment). Annotate the assessment with transaction events at the following important stages in the payment lifecycle when they occur:

Event type | Description | Reason example | Value example  
---|---|---|---  
`MERCHANT_APPROVE` | `MERCHANT_DENY` |  When you decide whether the transaction should be allowed to proceed.  | `IN_HOUSE` | N/A  
`AUTHORIZATION` | `AUTHORIZATION_DECLINE` |  When you submit the transaction to be processed, and the card issuer decides whether to allow the transaction to proceed.  | `82` (a reason code meaning that the CVV was incorrect) | N/A  
`CHARGEBACK` | When the transaction is charged back. | `Card Reported Stolen` | 20 (representing a partial chargeback of 20 units of currency)  
  
Along with the `CHARGEBACK` event type, include the chargeback reason code that was provided by the card issuer by using the `reason` field. Also, include the monetary amount charged back in the `value` field if the transaction was partially charged back.

In the transaction event `reason` field, either include clarifying terms to provide more context on the reason for the event, or provide reason codes that are obtained directly from the payment network or card issuer. These terms and codes differ depending on the event type.

The following table specifies the complete list of transaction event types:

Annotation reason | Description  
---|---  
`MERCHANT_APPROVE` |  Indicates that the transaction is approved by the merchant. The accompanying reasons can include terms such as `IN_HOUSE`, `ACCERTIFY`, `CYBERSOURCE`, or `MANUAL_REVIEW`.   
`MERCHANT_DENY` |  Indicates that the transaction is denied and concluded due to risks detected by the merchant. The accompanying reasons can include terms such as `IN_HOUSE`, `ACCERTIFY`, `CYBERSOURCE`, or `MANUAL_REVIEW`.   
`MANUAL_REVIEW` |  Indicates that the transaction is being evaluated by a human, due to suspicion or risk.   
`AUTHORIZATION` |  Indicates that the authorization attempt with the card issuer succeeded.   
`AUTHORIZATION_DECLINE` |  Indicates that the authorization attempt with the card issuer failed. The accompanying reasons can include Visa's `54` indicating that the card is expired or `82` indicating that the CVV is incorrect.   
`PAYMENT_CAPTURE` |  Indicates that the transaction is completed because the funds were settled.   
`PAYMENT_CAPTURE_DECLINE` |  Indicates that the transaction couldn't be completed because the funds were not settled.   
`CANCEL` |  Indicates that the transaction is canceled. Specify the reason for the cancellation. For example, `INSUFFICIENT_INVENTORY`.   
`CHARGEBACK_INQUIRY` |  Indicates that the merchant has received a chargeback inquiry due to fraud for the transaction, requesting additional information before a fraud chargeback is officially issued and a formal chargeback notification is sent.   
`CHARGEBACK_ALERT` |  Indicates that the merchant has received a chargeback alert due to fraud for the transaction. The process of resolving the dispute without involving the payment network is started.   
`FRAUD_NOTIFICATION` |  Indicates that a fraud notification is issued for the transaction, sent by the payment instrument's issuing bank because the transaction appears to be fraudulent. We recommend including `TC40` or `SAFE` data in the `reason` field for this event type. For partial chargebacks, we recommend that you include an amount in the `value` field.   
`CHARGEBACK` |  Indicates that the merchant is informed by the payment network that the transaction has entered the chargeback process due to fraud. Reason code examples include Discover's `6005` and `6041`. For partial chargebacks, we recommend that you include an amount in the `value` field.   
`CHARGEBACK_REPRESENTMENT` |  Indicates that the transaction has entered the chargeback process due to fraud, and that the merchant has chosen to enter representment. Reason examples include Discover's `6005` and `6041`. For partial chargebacks, we recommend that you include an amount in the `value` field.   
`CHARGEBACK_REVERSE` |  Indicates that the transaction has had a fraud chargeback which was illegitimate and was reversed as a result. For partial chargebacks, we recommend that you include an amount in the `value` field.   
`REFUND_REQUEST` |  Indicates that the merchant has received a refund for a completed transaction. For partial refunds, we recommend that you include an amount in the `value` field. Reason example: `FRAUD`.   
`REFUND_DECLINE` |  Indicates that the merchant has received a refund request for this transaction, but that they have declined it. For partial refunds, we recommend that you include an amount in the `value` field. Reason example: `FRAUD`.   
`REFUND` |  Indicates that the completed transaction was refunded by the merchant. For partial refunds, we recommend that you include an amount in the `value` field. Reason example: `PROACTIVE_FRAUD`.   
`REFUND_REVERSE` |  Indicates that the completed transaction was refunded by the merchant, and that this refund was reversed. For partial refunds, we recommend that you include an amount in the `value` field.   
  
The following example shows a sample annotation payload containing a transaction event. For more details, see [Annotate assessments](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment#annotate_assessment).
    
    
    POST https://recaptchaenterprise.googleapis.com/v1/ASSESSMENT_ID:annotate
    {
      "transaction_event": {
        "event_type": "CHARGEBACK",
        "reason": "Card Reported Stolen",
        "value": 20
      }
    }

## What's next

  * To learn about user accounts protection features, see [User accounts protection features](https://docs.cloud.google.com/recaptcha/docs/protect-accounts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
