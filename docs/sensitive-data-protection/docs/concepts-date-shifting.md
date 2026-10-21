---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting/
title: Date shifting \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:47.783787+00:00
---

# Date shifting  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Date shifting Stay organized with collections  Save and categorize content based on your preferences. 

Dates are a very common type of data. In cases where dates can be considered sensitive data or personally identifiable information (PII), you may need to generalize, obfuscate, or redact them.

One method for doing this is [generalization, or bucketing](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing). Depending on the use case and configuration, though, bucketing can remove the utility in the dates. For example, if you generalize all dates to just a year, then you could lose the order in which events happen within that year. An alternate method for obfuscating dates that addresses this problem is _date shifting_.

Date shifting techniques randomly shift a set of dates but preserve the sequence and duration of a period of time. Shifting dates is usually done in the context of an individual or an entity. That is, each individual's dates are shifted by an amount of time that is unique to that individual.

## When to use date shifting

The following are some common use cases:

  * **Preserve patient privacy in healthcare research** : Obfuscate patient admission and discharge dates to meet HIPAA Safe Harbor de-identification requirements while preserving temporal intervals between events.
  * **Sanitize audit and transaction logs** : Mask absolute transaction dates when preparing test databases while keeping the relative event order necessary to validate batch workflows.
  * **Analyze user retention cohorts** : Anonymize customer activity timestamps for cohort analysis while retaining chronological trends over days or months.
  * **Maintain event sequences in longitudinal studies** : Protect individual privacy in multi-year tracking studies by shifting timestamps uniformly per participant without distorting causal or chronological relationships.



## Date shifting example

Consider the following data:

user_id | date | action  
---|---|---  
1 | 2009-06-09 | run  
1 | 2009-06-03 | walk  
1 | 2009-05-23 | crawl  
2 | 2010-11-03 | crawl  
2 | 2010-11-22 | walk  
... | ... | ...  
  
If you generalize these dates by year, the output is as follows:

user_id | date_year | action  
---|---|---  
1 | 2009 | run  
1 | 2009 | walk  
1 | 2009 | crawl  
2 | 2010 | crawl  
2 | 2010 | walk  
... | ... | ...  
  
However, the chronological sequence of events for each user is lost.

Instead try date shifting:

user_id | date | action  
---|---|---  
1 | 2009-07-17 | run  
1 | 2009-07-11 | walk  
1 | 2009-06-30 | crawl  
2 | 2011-01-26 | crawl  
2 | 2011-02-14 | walk  
... | ... | ...  
  
Note how the dates are different but the sequence and duration are preserved. The magnitude that the dates were shifted was different between `user_id`s 1 and 2.

## Date shifting in Sensitive Data Protection

A JSON object to configure this for Sensitive Data Protection's [`content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify) method follows:
    
    
    deidentify_config {
      record_transformations {
        field_transformations {
          fields {
            name: "date"
          }
          primitive_transformation {
            date_shift_config {
              upper_bound_days: 100
              lower_bound_days: -100
              entity_field_id {
                name: "user_id"
              }
              crypto_key {
                unwrapped {
                  key: "123456789012345678901234567890ab"
                }
              }
            }
          }
        }
      }
    }
    

The upper and lower bounds of the shift are specified by the `upper_bound_days` and `lower_bound_days` values, respectively. The context or scope that that shift will apply to is based on the `entity_id_field` value, which in this case is `"user_id"`.

Note the use of a `crypto_key` as well. This is similar to how it's used in [pseudonymization](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization). The key will allow you to keep integrity of these date shifts across multiple requests or data runs.

**Warning:** For better security in production environments, use a [`KmsWrappedCryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#kmswrappedcryptokey) instead of an unwrapped key as illustrated in this example.

## Resources

For more information about how to de-identify data using date shifting and other methods in Sensitive Data Protection, see:

  * [De-identifying sensitive data in text content](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#infotype_transformations)



For API reference information about primitive transformations in Sensitive Data Protection, see:

  * [`DeidentifyConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig) object: The object in which you configure de-identification options.
  * [`PrimitiveTransformations`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#primitivetransformation) object: Date shifting is a "primitive transformation" in Sensitive Data Protection.
  * [`DateShiftConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#dateshiftconfig) object: Object with which to configure the [`PrimitiveTransformations`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#primitivetransformation) object. By specifying the `DateShiftConfig` object, you can shift dates by a random number of days.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
