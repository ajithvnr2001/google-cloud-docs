---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/crm-personalization/
title: Enhance AI Commerce Search with CRM personalization \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:01.698794+00:00
---

# Enhance AI Commerce Search with CRM personalization  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/crm-personalization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Enhance AI Commerce Search with CRM personalization Stay organized with collections  Save and categorize content based on your preferences. 

This API implementation guide for AI Commerce Search outlines how to use your Customer Relationship Management (CRM) data to personalize search experiences within AI Commerce Search. By integrating user attributes from your CRM, you can deliver more relevant search results, ultimately improving customer engagement and conversion. This document details the process of integrating these user attributes, including data considerations and technical specifications.

## Select data for personalization

The effectiveness of personalization hinges on the quality, coverage, and relevance of the CRM data you provide. Consider what information about a customer would genuinely influence the search results a knowledgeable sales associate might offer.

**Tip:** Ask yourself, _Would an in-store associate show this user a different product if the associate knew this data about the customer?_

When you have pilot tests complete, you will have stronger recommendations on what data is (and isn't) impactful.

### Recommended data categories for impact

These data categories constitute the most telling information for your commerce site user behavior.

  * **Geographic information** : Customer location, such as state or country. ZIP code information is too granular. See the section on [Excessive granularity](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/crm-personalization#overgranularity) for more information.
  * **Demographic data** : Core customer characteristics, such as age and gender. 
    * Knowing a customer's age group (18-24 as opposed to 55-64 years of age) would likely inform different product display strategies for items like apparel or electronics. This is highly impactful data.
  * **Customer personas** : For example, a budget conscious or frugal shopper as opposed to a big spender.



### Data categories less likely to be impactful

These data categories have a marginal impact on your commerce data capture.

  * Attributes derived from purchase history: 
    * Our system already incorporates past purchase behavior for personalization.
    * Sending attributes like `user bought a green dress yesterday` is redundant, because this information is natively captured and utilized.
    * Focus on novel insights from your CRM.
  * Specific marketing response data, such as `Clicked email #7`: 
    * While relevant for marketing campaign analysis, it doesn't tell the AI what search result to show.



### Data completeness

Beyond relevance, the completeness of your data across your user base significantly impacts its utility for personalization. An attribute is most valuable when it's available for a substantial portion of your users, allowing the system to identify broader patterns and apply personalization more widely.

  * **Highly useful** : 
    * Attributes you have for a significant majority of your users, such as `shipping_state:MA` if available for 70% of your user base.
    * This allows for robust pattern recognition and widespread application of personalization.
  * **Less useful** : 
    * Attributes available for only a small fraction of your users, such as `hair_color:blonde` if available for just 0.1% of your user base.



While interesting, such sparse data makes it difficult for the system to derive meaningful personalization signals due to the lack of sufficient examples. Instead, prioritize attributes that offer broader coverage across your customer profiles.

## Data granularity guidelines

The appropriate level of data granularity is crucial for effective personalization. Data that's too broad or too specific can diminish the system's ability to identify meaningful patterns. Aim for attributes that segment your customer base into actionable groups.

**Tip:** For optimal granularity, strive for attributes that yield 2 to 50 distinct categories.

### Appropriate granularity

Examples of appropriate granularity are fields for:

  * Gender
  * State
  * City
  * Age group (such as 30-39 years of age)



This granularity level provides differentiation for personalization without creating an unmanageable number of categories.

### Insufficient granularity

An example of insufficient granularity is `country:US` if the vast majority of your customer base resides in the United States. This is because an attribute that has little variance across your customer base offers minimal value for personalization.

### Excessive granularity

Examples of excessive granularity are:

  * **Exact zip or postal codes (`zipcode:12345`)**: With tens of thousands of potential zip codes, most will have very few associated customers. This atomization dilutes the signal. If using zip codes, truncate them to the first two digits to achieve a more appropriate level of granularity. The first two digits of ZIP codes are approximately mapped to state-sized areas.
  * **Exact ages (`age:37`)**: This creates an excessive number of age categories. To reduce the number, group numerical data like age into **~10 predefined bins or buckets** (such as `age:30-39`).



## Further data guidelines

This section addresses categorical and other data formats.

### Categorical data format

This system is optimized for categorical data: distinct, named values, such as:

  * `state:MA`
  * `gender:male`



### Numerical data

**Key Point:** The system treats all values (including numbers) as categories rather than inherently understanding numerical proximity or order. For example, `age:37`, `age:37.1`, and `age:37.0` will be processed as three distinct, unrelated categories. The system won't infer that `age:37` and `age:38` are close, nor will it understand that `age:37` and `age:82` are distant.

For this reason, any numerical attributes such as age, income, or frequency should be grouped into meaningful buckets before data transmission.

These are incorrect and correct examples, respectively:

  * `age:37`
  * `age:30-39`



### Additional data constraints

  * **Attribute limit** : Each query supports up to **100 key-value pairs**. Support for more pairs may be added in future releases.
  * **Duplicate keys** : Duplicate keys are not allowed within a single query. However, multiple values per key are supported.
  * **Prohibited PII** : Under no circumstances should you send specific Personally Identifiable Information (PII) such as customer email addresses, Social Security Numbers, full names, or financial data, such as credit card numbers, not in any form.



## API integration and data transmission

Customer data should be transmitted within the **`query`** field of your search requests, not in the events.

### Protocol buffer structure (for developers)

The user attributes are defined within the `SearchRequest` message as a map of strings to a `StringList` message.

View protobuf sample
    
    
    // A list of string values.
    message StringList {
    // String values.
    repeated string values;
    }
    
    // Request message for [SearchService.Search][] method.
    message SearchRequest {
    ...
    // The user attributes that could be used for personalization of search.
    maptring, StringList> user_attributes;
    }

### JSON request example

This example illustrates how to structure `user_attributes` within a JSON search request.

View JSON sample
    
    
    {
    ...
    
    user_attributes: [
           { key: "pets" # note keys can be hashed or unhashed
             value {
               values: "dog" # Note: these values MUST be hashed
               values: "cat"
             }
           },
           { key: "state"
             value {
               values: "CA"
             }
           }
          ]
    }

### API response

There are no changes to the `SearchResponse` API when utilizing this feature. Personalization occurs internally based on the provided user attributes.

## Data hashing requirements

To ensure data privacy and security, attribute values _must be hashed._ Keys can be sent hashed or unhashed.

### Hashing keys

Attribute keys, such as `pet_owner` and `state`, can be sent in their original string form or hashed. Both are acceptable.

For example: 

  * Acceptable — `pet_owner`
  * Acceptable — `hash(pet_owner)`



### Hashing values

Attribute values, such as `dog` and `CA`, must be hashed. Sending plain text values is not permitted.

For example: 

  * Acceptable — `hash(dog)`
  * Not acceptable — `"Dog"`



### Combined key-value hashing

If both the key and the value are to be hashed, they _must be hashed independently._ Do not hash the combined key-value string.

For example: 

  * Acceptable — `pet_owner:hash("dog")`
  * Acceptable — `hash(pet_owner):hash("dog")`
  * Not acceptable — `hash("Pet_owner:dog")`



## Best practices for data transmission

This section outlines several best practices for data transmission, including how to handle repeated values, data consistency, attribute key naming flexibility, and handling varied user profiles.

### How to handle repeated values

If a user has multiple values for a single attribute, such as owning both a dog and a cat, provide all values under a single `key` within the `StringList`.

These code samples demonstrate examples of incorrect and correct usage, respectively:

View sample
    
    
    // This is incorrect because it sends the same key multiple times for different
    // values, causing only one of the two values for pets to be used, choosing one
    // value or the other in an inconsistent manner.
    {
      key: "pets",
      value {
        values: "dog"
      }
    },
    {
      key: "pets",
      value {
        values: "cat"
      }
    }

View sample
    
    
    {
      key: "pets",
      value {
        values: "dog",
        values: "cat"
      }
    }

### Data consistency

Maintain strict consistency in the spelling, spacing, and capitalization of all keys and values. The system interprets even minor variations as distinct categories. 

For example, `State:MA`, `state:MA`, `state:ma`, `STATE:MA`, and `residence_state:MA` will all be treated as separate and unrelated attributes.

**Caution:** The same key must always be used for a given attribute. 

For example:

  * Don't swap between `pets:` and `pets_owned:`.
  * _Don't change spacing, punctuation, or capitalization_ for a given key or value attribute, after it's established.



### Attribute key-naming flexibility

While consistent, the specific naming convention for your attribute keys (for example, `pet_owner`, `pets`, `codeabc`) does not inherently impact the system's ability to use the data. The crucial aspect is the consistency of the data you transmit.

### How to handle varied user profiles

It is acceptable for different users to have different sets of attributes.

  * **Example** : User A might have `age:30-39` and `pet:dog`, while User B has `gender:male` but no pet or age data. The system handles partial profiles gracefully.



### Dynamic data updates

User attributes can evolve over time. You can update a user's profile with new information as it becomes available.

  * **Example** : A user initially identified with `age:30-39` and `pet:dog` can later have `state:MA` added if their location is acquired.



### Cross-platform consistency

Strive for consistent attribute transmission for a given user across all touchpoints, such as mobile app or website. This ensures a unified personalization experience.

  * **Optimal** : User A is consistently `age:30-39` on both the mobile app and website.
  * **Suboptimal** : User A is `age:30-39` on the mobile app, but only `pet:dog` on the website.



### How to handle missing data

If a specific piece of information about a user is unavailable, _do not send a placeholder or an empty value._ Just omit that key-value pair from the request.

  * **Example** : Avoid `pet:unknown` or `pet:`



## SDK and library access

Access to these libraries can be found at the following versions and later:

  * [Java](https://github.com/googleapis/google-cloud-java/releases/tag/v1.61.0)
  * [Python](https://github.com/googleapis/google-cloud-python/releases/tag/google-cloud-retail-v2.2.0)
  * [Node.js](https://github.com/googleapis/google-cloud-node/releases/tag/retail-v4.1.0)
  * [Go](https://github.com/googleapis/google-cloud-go/releases/tag/retail/v1.21.0)
  * [PHP](https://github.com/googleapis/google-cloud-php/releases/tag/v0.294.0)
  * [Ruby](https://github.com/googleapis/google-cloud-ruby/releases/tag/google-cloud-retail-v2%2Fv2.3.0)
  * [C# .NET](https://github.com/googleapis/google-cloud-dotnet/releases/tag/Google.Cloud.Retail.V2-2.14.0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
