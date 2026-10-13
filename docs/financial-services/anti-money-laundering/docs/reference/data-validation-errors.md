---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/data-validation-errors/
title: Data validation errors \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:11.277739+00:00
---

# Data validation errors  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/data-validation-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Data validation errors Stay organized with collections  Save and categorize content based on your preferences. 

Gathering and merging the core data needed to run AML AI may be error-prone. To address this, AML AI has built-in data validation checks to provide you actionable feedback on how to address dataset-related issues.

The data validation checks are executed during two phases of the model deployment process, with any resulting errors included in the long-running operation (LRO) response.

  * One check is executed as part of the creation of the dataset.
  * Validation is also run at the beginning of other operations (tune, train, backtest, and predict).

**Note:** If a dataset fails validation as part of tuning or training, the operation stops and you are not charged for that AML AI API request. See the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing).

The LRO [`Status`](https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto) contains one [`ErrorInfo`](https://github.com/googleapis/googleapis/blob/6f3fcc058ff29989f6d3a71557a44b5e81b897bd/google/rpc/error_details.proto#L27-L76) message for each failed check. The `ErrorInfo` message's `reason` field contains a stable string constant while other relevant information is provided in the `metadata` field. For more information on RPC errors, see [AIP-193](https://google.aip.dev/193).

## Data validation checks and error output

Every validation failure contains the following corresponding error information:

Field | Description  
---|---  
`reason` | Unique identifier for this type of error  
`metadata["count"]` | Number of occurrences of this error  
`metadata["data_table"]` | The name of the input table in which the error occurred  
`metadata["data_field"]` | The name of the field in the input table in which the error occurred  
`metadata["description"]` | Detailed, actionable error description exposed in metadata  
`metadata["test"]` | Illustrative (pseudo-SQL) statement explaining the logic of the validation  
  
The following table lists all data validation checks performed by AML AI, their descriptions, and an example test response:

`reason` | `metadata["description"]` | `metadata["test"]`  
---|---|---  
`NOT_NULL_COLUMN_WITH_NULLS` | One or more NOT NULL columns contain one or more null values. | `X IS NULL`  
`DATE_TIME_DIFFERENCE` | The `validity_start_time` cannot include dates that are greater than today's date and `validity_start_time` must be greater than threshold. | `DATETIME_DIFF(CURRENT_TIMESTAMP(), validity_start_time, DAY) < 0`  
`EXCESSIVE_ACCOUNTS_FOR_PARTY` | Number of accounts for the party exceeds the predefined threshold. | `COUNT(DISTINCT account_id) > {{ var('overlarge_account_count')}}`  
`EXCESSIVE_PARTIES_FOR_SHARED_ACCOUNT` | Number of account holders for the account exceeds the predefined threshold. | `COUNT(DISTINCT party_id) > {{ var('overlarge_account_holders')}} GROUP BY account_id`  
`MISSING_AML_EXIT_LABELS` | All, or no parties have AML exit events. Useful AML model labels cannot be created. | `COUNT(party_id) WHERE type IN {{ positive_event_types}}) IN (0, count(party)`  
`DUPLICATE_PRIMARY_KEY` | There is a duplicate primary key value in the database resulting in a unique key violation. Note that for tables with `validity_start_time`, the primary key includes `validity_start_time`. | `GROUP BY X, validity_start_time HAVING count(1) > 1`  
`NAN_VALUE_IN_FLOAT_COLUMN` | One or more columns contains a NaN (Not a Number) floating point value. | `X is NAN`  
`INSUFFICIENT_DATE_RANGE` | **(Only up to v004.002)** The date range in the dataset specifies an insufficient number of months for any AML AI operation. The sufficient number of months for prediction is 24, and more for other operations. | `COUNTIF((MAX({{transaction_time_column}}) - MIN({{transaction_time_column}})) > 3 years)/COUNT(*) < {{ var('short_timeframe_ratio') }} GROUP BY account_id`  
`EMPTY_TABLE` | One or more required tables in the database is empty. | `COUNT(*) FROM X < 1`  
`UNSUPPORTED_VALUE` | One or more columns include values that are not in the set of allowed values. | `X NOT IN ("a1", "b2", "c3")`  
`DUPLICATE_RISK_CASE_EVENTS_TYPE_AML_EXIT` | Party was exited from the bank multiple times. `AML_EXIT` risk case event type is not allowed to occur multiple times. | `party_id, risk_case_id, countif(type = "AML_EXIT") > 1`  
`DUPLICATE_RISK_CASE_EVENTS_TYPE_AML_PROCESS_START` | Multiple AML investigation processes were initiated against the party in this risk case. | `party_id, risk_case_id, countif(type = "AML_PROCESS_START") > 1`  
`DUPLICATE_RISK_CASE_EVENTS_TYPE_AML_PROCESS_END` | Multiple AML investigation processes were closed against the party in this risk case. | `Party_id, risk_case_id countif(type = "AML_PROCESS_END") > 1`  
`UNNORMALIZED_BOOKED_AMOUNT_CURRENCY` | Normalized booked amount includes multiple currencies in the [Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction) table. All normalized amounts need to be in the same currency. | `COUNT(DISTINCT normalized_booked_amount.currency_code) != 1`  
`NEGATIVE_TRANSACTION_NORMALIZED_BOOKED_AMOUNT` | Normalized booked amount value for one or more transactions is negative. Data schema prohibits negative values for this field. | `normalized_booked_amount.units < 0 OR normalized_booked_amount.nanos < 0`  
`COLUMN_EXISTENCE` | One or more required columns don't exist in the database. | `X DOES NOT EXIST IN {{table_name}}`  
`TABLE_EXISTENCE` | One or more required tables don't exist in the database. | `TABLE {{table_name}} DOES NOT EXIST`  
`SUPPLEMENTARY_DATA_COLUMN_NAMES` | One or more `party_supplementary_data_id` values is not in the range of allowed values. IDs may use alphanumeric characters as well as underscores, and should start with an alphanumeric character. | `NOT EXISTS REGEXP_CONTAINS(party_supplementary_data_id, "^[a-zA-Z0-9][a-zA-Z0-9_]*$") AND supplementary_data_payload.value IS NOT NULL`  
`EXCESSIVE_PARTY_SUPPLEMENTARY_DATA_IDS` | Number of distinct party_supplementary_data_id values exceeds the maximum of 100. | `COUNT(DISTINCT party_supplementary_data_id) > 100`  
`MISSING_PARTY_SUPPLEMENTARY_DATA_ID` | One or more party supplementary data IDs that was present in the dataset used for model creation is missing in this dataset. | `X NOT IN (DISTINCT {party_supplementary_data_ids used in model})`  
`AML_SUSPICIOUS_ACTIVITY_START_AFTER_AML_PROCESS_START` | AML suspicious activity starts after the AML process starts for at least one risk case and party. | `EXISTS(RCE1, RCE2) WHERE RCE1.party_id = RCE2.party_id AND RCE1.risk_case_id = RCE2.risk_case_id AND RCE1.type = "AML_PROCESS_START" AND RCE2.type = "AML_SUSPICIOUS_ACTIVITY_START" AND RCE1.event_time <= RCE2.event_time`  
`EXCESSIVE_NUMBER_OF_PARTIES` | The dataset contains more parties than supported by this engine version. | `COUNT(DISTINCT party_id) >= THRESHOLD`  
`EXCESSIVE_RISK_CASES_PER_PARTY` | Number of risk cases for at least one party exceeds the predefined threshold. | `COUNT(DISTINCT risk_case_id) > THRESHOLD GROUP BY party_id`  
`INCONSISTENT_SUSPICIOUS_PERIOD` | Suspicious period for at least one party and risk case doesn't conform to requirements - suspicious activity start without corresponding end, or suspicious activity end without corresponding start. | `(party_id, risk_case_id, type = "AML_SUSPICIOUS_ACTIVITY_END") MUTEX (party_id, risk_case_id, type = "AML_SUSPICIOUS_ACTIVITY_START")`  
`INCONSISTENT_SUSPICIOUS_PERIOD` | Suspicious period for at least one party and risk case doesn't conform to requirements - more than one suspicious activity start or end. | `COUNT(party_id, risk_case_id, type = "AML_SUSPICIOUS_ACTIVITY_END" OR "AML_SUSPICIOUS_ACTIVITY_START") > 1`  
`INCONSISTENT_SUSPICIOUS_PERIOD` | Suspicious period for at least one party and risk case doesn't conform to requirements - suspicious activity period end before suspicious activity start. | `party_id, risk_case_id, type = "AML_SUSPICIOUS_ACTIVITY_END" event time < party_id, risk_case_id, type = "AML_SUSPICIOUS_ACTIVITY_START" event time`  
`JOINABILITY_ISSUE_ACCOUNT_ID` | The account_id in the table cannot be found in the AccountPartyLink table. The account_id must exist in the AccountPartyLink table. | `account_id NOT IN (SELECT account_id FROM account_party_link)`  
`JOINABILITY_ISSUE_ACCOUNT_ID_IS_DELETED` | The account_id is deleted from the AccountPartyLink table (without undeletion) at the validity start / event times in the other tables. | `account_id (FROM account_party_link) is_entity_deleted = TRUE WHEN account_id (FROM transaction) validity_start_time`  
`JOINABILITY_ISSUE_MIN_ACCOUNT_ID_VALIDITY_START_TIME` | The minimum account_id validity start time in the AccountPartyLink table is later than the validity start time in Transactions table. | `account_id (FROM account_party_link) MIN validity_start_time > account_id (FROM transaction) validity_start_time`  
`JOINABILITY_ISSUE_PARTY_ID` | The party_id in the table cannot be found in the Party table. The party_id must exist in the Party table. | `party_id NOT IN (SELECT party_id FROM party)`  
`JOINABILITY_ISSUE_PARTY_ID_IS_DELETED` | The party_id is deleted from the Party table (without undeletion) at the validity start / event times in the other tables. | `party_id (FROM party) is_entity_deleted = TRUE WHEN party_id (FROM account_party_link) validity_start_time`  
`NO_AML_PROCESS_START_FOR_RISK_CASE` | One or multiple positive risk cases that resulted in an exit or SAR don't include AML PROCESS START event. | `(party_id, risk_case_id COUNTIF(type = "AML_PROCESS_START") = 0) WHEN party_id, risk_case_id COUNTIF(type = "AML_EXIT" OR "AML_SAR" ) = 1)`  
`UNSUPPORTED_DATA_TYPE` | Column present with incorrect data type. See AML AI Input Data model documentation for correct types. | `X DATA_TYPE IS NOT "expected_data_type"`  
`MISSING_DATA_FOR_REQUIRED_TIME_RANGE` | **(Starting from major engine version v004.007)** There are one or multiple periods in the required time range without any valid entries in the Party, Transaction, or AccountPartyLink table. | No valid entry in the required time range for some months.  
`EXCESSIVE_NUMBER_OF_RISK_TYPOLOGIES` | **(Starting from major engine version v004.009)** The dataset contains more distinct risk typologies than supported by this engine version.  
The threshold of supported risk typologies is 100. | `COUNT(DISTINCT risk_typology_id) > [EV THRESHOLD]`  
`REPEATED_RISK_TYPOLOGY_FOR_RISK_CASE_EVENT` | **(Starting from major engine version v004.009)** The risk_typology_measurements field includes the same risk_typology_id multiple times within the same risk case event. | `COUNT(DISTINCT risk_case_event_id, risk_typology_id)) > 1`  
  
## Accessing data validation errors

Data validation errors are included in the LRO response. See [Manage long-running operations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations#get-operation) for more information. The [platform logs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/logging) also contain an entry with the LRO response.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
