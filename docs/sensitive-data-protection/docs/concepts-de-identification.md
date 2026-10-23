---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-de-identification/
title: De-identification \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:16.029124+00:00
---

# De-identification  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-de-identification/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)



Send feedback 

#  De-identification Stay organized with collections  Save and categorize content based on your preferences. 

Sensitive Data Protection uses _information types_ —or _infoTypes_ —to define what it scans for. An infoType is a type of sensitive data, such as a name, email address, telephone number, identification number, credit card number, and so on.

**Note:** If you're looking for an up-to-date list of all built-in infoType detectors, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

Every infoType defined in Sensitive Data Protection has a corresponding _detector_. Sensitive Data Protection uses infoType detectors in the configuration for its scans to determine what to inspect for and how to transform findings. InfoType names are also used when displaying or reporting scan results.

This topic describes infoTypes and infoType detectors in detail, and provides guidance for how to use infoType detectors when scanning content for sensitive data using Sensitive Data Protection.

## When to use de-identification

The following are some common use cases:

  * **Share data with external analytics partners** : Tokenize or pseudonymize direct identifiers (such as names, national IDs, and account numbers) so third-party partners and researchers can analyze datasets without accessing plaintext personal identity.
  * **Stage production datasets into non-production environments** : Mask or generalize sensitive customer attributes before replicating production databases into development, testing, or training environments.
  * **Comply with regulatory privacy mandates** : Obfuscate sensitive personally identifiable information (PII) and protected health information (PHI) across BigQuery and Cloud Storage repositories to meet compliance standards like GDPR and HIPAA.
  * **Sanitize sensitive fields in streaming event pipelines** : Transform sensitive records in real time as events flow through Pub/Sub before persisting data into downstream warehouses or application databases.
  * **Maintain referential integrity across relational datasets** : Use deterministic cryptographic transformations to allow secure joins and cross-table analytics across distinct systems without exposing the underlying identifiers.



## Specifying infoType detectors

When you set up Sensitive Data Protection to scan your content, you include the infoType detectors to use in the scan configuration.

For example, the following JSON demonstrates a simple scan request to the DLP API. Notice that the `PHONE_NUMBER` detector is specified in [`inspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig), which instructs Sensitive Data Protection to scan the given string for a phone number.
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT_ID]/content:inspect?key={YOUR_API_KEY}
    
    {
      "item":{
        "value":"My phone number is (415) 555-0890"
      },
      "inspectConfig":{
        "includeQuote":true,
        "minLikelihood":"POSSIBLE",
        "infoTypes":{
          "name":"PHONE_NUMBER"
        }
      }
    }
    

The preceding request returns the following:
    
    
    {
      "result":{
        "findings":[
          {
            "quote":"(415) 555-0890",
            "infoType":{
              "name":"PHONE_NUMBER"
            },
            "likelihood":"VERY_LIKELY",
            "location":{
              "byteRange":{
                "start":"19",
                "end":"33"
              },
              "codepointRange":{
                "start":"19",
                "end":"33"
              }
            },
            "createTime":"2018-10-29T23:46:34.535Z"
          }
        ]
      }
    }
    

Always specify [infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) in your scan configuration. If you don't specify any infoTypes, Sensitive Data Protection uses a default infoTypes list. Depending on the amount of content to scan, scanning for default infoTypes can be prohibitively time-consuming or expensive.

For more information on how to use infoType detectors to scan your content, see one of the [how-to topics](https://docs.cloud.google.com/sensitive-data-protection/docs/how-to) about inspecting, redacting, or de-identifying.

## Kinds of infoType detectors

Information type (or "infoType") detectors are the mechanisms that Sensitive Data Protection uses to find sensitive data.

Sensitive Data Protection includes several kinds of infoType detectors, all of which are summarized here:

  * _Built-in infoType detectors_ are built into Sensitive Data Protection. They include detectors for country- or region-specific sensitive data types as well as globally applicable data types.
  * _Custom infoType detectors_ are detectors that you create yourself. There are three kinds of custom infoType detectors: 
    * _Regular custom dictionary detectors_ are simple word lists that Sensitive Data Protection matches on. Use regular custom dictionary detectors when you have a list of up to several tens of thousands of words or phrases. Regular custom dictionary detectors are preferred if you don't anticipate your word list changing significantly.
    * _Stored custom dictionary detectors_ are generated by Sensitive Data Protection using large lists of words or phrases stored in either Cloud Storage or BigQuery. Use stored custom dictionary detectors when you have a large list of words or phrases—up to tens of millions.
    * _Regular expressions (regex) detectors_ enable Sensitive Data Protection to detect matches based on a regular expression pattern.



To refine scan results, you can [create inspection rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules).

## Built-in infoType detectors

Built-in infoType detectors are built into Sensitive Data Protection, and include detectors for country- or region-specific sensitive data types such as the French _Numéro d'Inscription au Répertoire (NIR)_ (`FRANCE_NIR`), UK driver's license number (`UK_DRIVERS_LICENSE_NUMBER`), and US Social Security number (`US_SOCIAL_SECURITY_NUMBER`). They also include globally applicable data types such as a person name (`PERSON_NAME`), telephone numbers (`PHONE_NUMBER`), email addresses (`EMAIL_ADDRESS`), and credit card numbers (`CREDIT_CARD_NUMBER`). To detect content that corresponds to infoTypes, Sensitive Data Protection leverages various techniques including pattern matching, checksums, machine learning, context analysis, and others.

The list of built-in infoType detectors is always being updated. For a complete list of currently supported built-in infoType detectors, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).

You can also view a complete list of all built-in infoType detectors by calling Sensitive Data Protection's [`infoTypes.list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/infoTypes/list) method.

**Important:** Built-in infoType detectors are not a perfectly accurate detection method. For example, they can't guarantee compliance with regulatory requirements. You must decide what data is sensitive and how to best protect it. Google recommends that you test your settings to make sure that your configuration meets your requirements. 

## Custom infoType detectors

There are three kinds of custom infoType detectors:

  * Regular custom dictionary detectors
  * Stored custom dictionary detectors
  * Regular expressions (regex)



To refine scan results, you can [create inspection rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules).

### Regular custom dictionary detectors

Use [regular custom dictionary detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary) to match a short (up to several tens of thousands) list of words or phrases. A regular custom dictionary can act as its own unique detector.

Custom dictionary detectors are useful when you want to scan for a list of words or phrases that are not easily matched by a regular expression or a built-in detector. For example, suppose you want to scan for conference rooms that are commonly referred to by their assigned room names rather than their room numbers, such as state or region names, landmarks, fictional characters, and so on. You can make a regular custom dictionary detector that contains a list of these room names. Sensitive Data Protection can scan your content for each of the room names and return a match when it encounters one of them in context. Learn more about how Sensitive Data Protection matches dictionary words and phrases in the "[Dictionary matching specifics](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary#specifics)" section of [Creating a Regular Custom Dictionary Detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary).

For more details about how regular dictionary custom infoType detectors work, as well as examples in action, see [Creating a Regular Custom Dictionary Detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary).

### Stored custom dictionary detectors

Use [stored custom dictionary detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes) when you have more than a few words or phrases to scan for, or if your list of words or phrases changes frequently. Stored custom dictionary detectors can match on up to tens of millions of words or phrases.

Stored custom dictionary detectors, by their nature as very large custom detectors, are created differently from both regular expression custom detectors and regular custom dictionary detectors. Each stored custom dictionary has two components:

  * A list of phrases that you create and define. The list is stored as either a text file within Cloud Storage or a column in a BigQuery table.
  * The generated dictionary files, which are built by Sensitive Data Protection based on your phrase list. The dictionary files are stored in Cloud Storage, and are comprised of a copy of the source phrase data plus bloom filters, which aid in searching and matching. You can't edit these files directly.



Once you've created a word list and then used Sensitive Data Protection to generate a custom dictionary, you initiate or schedule a scan using a stored custom dictionary detector in a similar way as other infoType detectors.

For more details about how stored custom dictionary detectors work, as well as examples in action, see [Creating a Stored Custom Dictionary Detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary).

### Regular expressions

A regular expression (regex) custom infoType detector allows you to create your own infoType detectors that enable Sensitive Data Protection to detect matches based on a regex pattern. For example, suppose that you had medical record numbers in the form `###-#-#####`. You could define a regex pattern such as the following:
    
    
    [1-9]{3}-[1-9]{1}-[1-9]{5}
    

The Sensitive Data Protection would then match items like this:
    
    
    123-4-56789
    

You can also specify a [likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood) to assign to each custom infoType match. That is, when Sensitive Data Protection matches the sequence you specify, it will assign the likelihood that you have indicated. This is useful because if your custom regex defines a sequence that is common enough it could easily match some other random sequence, you would not want Sensitive Data Protection to label every match as `VERY_LIKELY`. Doing so would erode confidence in scan results and potentially cause the wrong information to be de-identified.

For more information about regular expression custom infoType detectors, and to see them in action, see [Creating a Custom Regex Detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-regex).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
