---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis/
title: Re-identification risk analysis \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:50.934677+00:00
---

# Re-identification risk analysis  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Re-identification risk analysis Stay organized with collections  Save and categorize content based on your preferences. 

_Re-identification risk analysis_ (or just _risk analysis_) is the process of analyzing sensitive data to find properties that might increase the risk of subjects being identified, or of sensitive information about individuals being revealed. You can use risk analysis methods before de-identification to help determine an effective de-identification strategy, or after de-identification to monitor for any changes or outliers.

De-identification is the process of removing identifying information from data. Sensitive Data Protection can [detect and de-identify sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data) for you according to how you've configured it to conform to your organization's requirements.

Conversely, [re-identification](https://en.wikipedia.org/wiki/Data_Re-Identification) is the process of matching up de-identified data with other available data to determine the person to whom the data belongs. Re-identification is most often talked about in the context of sensitive personal information, such as medical or financial data.

For more information about using Sensitive Data Protection to measure various types of risk, see [Measuring re-identification and disclosure risk](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis).

## When to use re-identification risk analysis

The following are some common use cases:

  * **Quantify re-identification vulnerability before sharing data** : Measure k-anonymity and l-diversity across quasi-identifying columns before releasing research, healthcare, or demographic datasets to external partners.
  * **Evaluate disclosure risk against population benchmarks** : Compute k-map metrics against public demographic datasets (such as US Census data) to gauge the probability that an individual can be identified.
  * **Assess membership disclosure sensitivity with delta-presence** : Estimate the risk that an attacker can determine whether a specific individual is included in a sensitive cohort or registry.
  * **Optimize de-identification and masking parameters** : Run iterative risk evaluations to fine-tune bucketing, date-shifting, and tokenization transformations to achieve the ideal balance between privacy and utility.



## Risk analysis terms and techniques

If you don't correctly or adequately de-identify sensitive data, you risk an attacker re-identifying the data or learning sensitive information about individuals, which can have serious privacy implications. Sensitive Data Protection can help compute this risk, according to several metrics.

Before diving into the metrics, we'll first define a few common terms:

  * _Identifiers_ : Identifiers can be used to uniquely identify an individual. For example, someone's full name or government ID number are considered identifiers.
  * _Quasi-identifiers_ : Quasi-identifiers don't uniquely identify an individual, but, when combined and cross-referenced with individual records, they can substantially increase the likelihood that an attacker will be able to re-identify an individual. For example, ZIP codes and ages are considered quasi-identifiers.
  * _Sensitive data_ : Sensitive data is data that is protected against unauthorized exposure. Attributes like health conditions, salary, criminal offenses, and geographic location are typically considered sensitive data. Note that there can be overlap between identifiers and sensitive data.
  * _Equivalence classes_ : An equivalence class is a group of rows with identical quasi-identifiers.



There are four techniques that Sensitive Data Protection can use to quantify the level of risk associated with a dataset:

  * [_k-anonymity_](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-k-anonymity): A property of a dataset that indicates the re-identifiability of its records. A dataset is _k_ -anonymous if quasi-identifiers for each person in the dataset are identical to at least _k_ – 1 other people also in the dataset.
  * [_l-diversity_](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-l-diversity): An extension of _k_ -anonymity that additionally measures the diversity of sensitive values for each column in which they occur. A dataset has _l_ -diversity if, for every set of rows with identical quasi-identifiers, there are at least _l_ distinct values for each sensitive attribute.
  * [_k-map_](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-k-map): Computes re-identifiability risk by comparing a given de-identified dataset of subjects with a larger re-identification—or "attack"—dataset. Sensitive Data Protection doesn't know the attack dataset, but it statistically models it by using publicly available data like the US Census, by using a custom statistical model (indicated as one or more BigQuery tables), or by extrapolating from the distribution of values in the input dataset. Each dataset—the sample dataset and the re-identification dataset—shares one or more quasi-identifier columns.
  * Delta-presence ([_δ_ -presence](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis#about-delta-presence)): Estimates the probability that a given user in a larger population is present in the dataset. This is used when membership in the dataset is itself sensitive information. Similarly to _k_ -map, Sensitive Data Protection doesn't know the attack dataset, but statistically models it using publicly available data, user-specified distributions, or extrapolation from the input dataset.



## About _k_ -anonymity

When collecting data for research purposes, de-identification can be essential for helping maintain participants' privacy. At the same time, de-identification may result in a dataset losing its practical usefulness. _k_ -anonymity was created from a need both to quantify the re-identifiability of a dataset and to balance the usefulness of de-identified people data and the privacy of the people whose data is being used. It is a property of a dataset that can be used to assess the re-identifiability of records within the dataset.

As an example, consider a set of patient data:

Patient ID | Full Name | ZIP Code | Age | Condition | ...  
---|---|---|---|---|---  
746572 | John J. Jacobsen | 98122 | 29 | Heart disease |   
652978 | Debra D. Dreb | 98115 | 29 | Diabetes, Type II |   
075321 | Abraham A. Abernathy | 98122 | 54 | Cancer, Liver |   
339012 | Karen K. Krakow | 98115 | 88 | Heart disease |   
995212 | William W. Wertheimer | 98115 | 54 | Asthma |   
... |  |  |  |  |   
  
This dataset contains all three types of data we described previously: identifiers, quasi-identifiers, and sensitive data.

If sensitive data like health conditions aren't masked or redacted, an attacker could potentially use the quasi-identifiers to which each one is attached, potentially cross-referencing with another dataset that contains similar quasi-identifiers, and re-identify the people to whom that sensitive data applies.

A dataset is said to be _k_ -anonymous if every combination of values for demographic columns in the dataset appears for at least _k_ different records. Recall that a group of rows with identical quasi-identifiers is called an "equivalence class." For example, if you've de-identified the quasi-identifiers enough that there is a minimum of four rows whose quasi-identifier values are identical, the dataset's _k_ -anonymity value is 4.

### Entity IDs and computing _k_ -anonymity

An important option that Sensitive Data Protection includes when calculating _k_ -anonymity is the optional _entity identifier (ID)_. An entity ID enables you to more accurately determine _k_ -anonymity in the common scenario wherein several rows of your dataset correspond to the same user. Otherwise, if every row, regardless of user, is counted separately, the total user count used for calculating the dataset's _k_ -anonymity value is made artificially high. This makes computed _k_ -anonymity values inaccurate.

Consider the following simple set of data:

User ID | ZIP code  
---|---  
01 | 42000  
02 | 17000  
02 | 42000  
03 | 17000  
03 | 42000  
03 | 42000  
04 | 42000  
04 | 17000  
  
Without using an entity ID to note when different rows belong to the same user, the total user count that is used when calculating _k_ -anonymity is 8, even though the actual number of users is 4. In this dataset, using traditional _k_ -anonymity calculation methods (without an entity ID), 3 people have a _k_ -anonymity value of 3, and 5 people have a _k_ -anonymity value of 5, even though there are just 4 actual people in the database.

Using an entity ID causes Sensitive Data Protection to consider the multiset of ZIP codes that a user is associated with as a quasi-identifier when calculating _k_ -anonymity. In the case of our example, there are actually three "composite" quasi-identifier values because there are three distinct combinations of quasi-identifier that are assigned to users: 42000, the multiset of 17000 and 42000, and the multiset of 17000, 42000, and 42000. They correspond to users as follows:

  * [42000] is associated with 1 unique user (01).
  * [17000, 42000] is associated with 2 unique users (02 and 04).
  * [17000, 42000, 42000] is associated with 1 unique user (03).



As you can see, this method takes into account that users may occur more than once in our ZIP code database, and it treats them accordingly when calculating _k_ -anonymity.

### _k_ -anonymity resources

For more information about _k_ -anonymity, see [Protecting Privacy when Disclosing Information: _k_ -Anonymity and Its Enforcement through Generalization and Suppression](http://scholar.google.com/scholar?q=Protecting+Privacy+when+Disclosing+Information:+k-Anonymity+and+Its+Enforcement+through+Generalization+and+Suppression), by Pierangela Samarati and Latanya Sweeney of the Harvard University Data Privacy Lab.

To learn how to compute _k_ -anonymity with Sensitive Data Protection, with or without entity IDs, see [Computing _k_ -anonymity for a dataset](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-anonymity).

## About _l_ -diversity

_l_ -diversity is closely related to _k_ -anonymity, and was created to help address a de-identified dataset's susceptibility to attacks such as:

  * Homogeneity attacks, in which attackers predict sensitive values for a set of _k_ -anonymized data by taking advantage of the homogeneity of values within a set of _k_ records.
  * Background knowledge attacks, in which attackers take advantage of associations between quasi-identifier values that have a certain sensitive attribute to narrow down the attribute's possible values.



_l_ -diversity attempts to measure how much an attacker can learn about people in terms of _k_ -anonymity and equivalence classes (sets of rows with identical quasi-identifier values). A dataset has _l_ -diversity if, for every equivalence class, there are at least _l_ unique values for each sensitive attribute. For each equivalence class, how many sensitive attributes are there in the dataset? For example, if _l_ -diversity = 1, that means everyone has the same sensitive attribute, if _l_ -diversity = 2, that means everyone has one of two sensitive attributes, and so on.

### _l_ -diversity resources

For more information about _l_ -diversity, see [_l_ -Diversity: Privacy Beyond _k_ -Anonymity](https://scholar.google.com/scholar?q=l-Diversity:+Privacy+Beyond+k-Anonymity), by Ashwin Machanavajjhala, Johannes Gerke, and Daniel Kifer of the Cornell University Department of Computer Science.

To learn how to compute _l_ -diversity with Sensitive Data Protection, see [Computing _l_ -diversity for a dataset](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-l-diversity).

## About _k_ -map

_k_ -map is very similar to _k_ -anonymity, except that it assumes that the attacker most likely doesn't know who is in the dataset. Use _k_ -map if your dataset is relatively small, or if the level of effort involved in generalizing attributes would be too high.

Just like _k_ -anonymity, _k_ -map requires you to determine which columns of your database are quasi-identifiers. In doing this, you are stating what data an attacker will most likely use to re-identify subjects. In addition, computing a _k_ -map value requires a re-identification dataset: a larger table with which to compare rows in the original dataset.

Consider the following small example dataset. This sample data is part of a larger hypothetical database, gathered from a survey whose answers included sensitive information.

ZIP code | age  
---|---  
85535 | 79  
60629 | 42  
  
Taken on its own, this appears to be the same amount of information for both individuals. In fact, considering k-anonymity for the larger dataset might lead to the assertion that the subject corresponding to the second row is highly identifiable. However, if you back up and consider the data, you'll realize it's not. In particular, consider the United States ZIP code 85535, in which about 20 people currently live. There is probably only one person of exactly 79 years of age living in the 85535 ZIP code. Compare this to ZIP code 60629, which is part of the Chicago metropolitan area and houses over 100,000 people. There are approximately 1,000 people of exactly 42 years of age in that ZIP code.

The first row in our small dataset was easily re-identified, but not the second. According to _k_ -anonymity, however, both rows might be completely unique in the larger dataset.

_k_ -map, like _k_ -anonymity, requires you to determine which columns of your database are quasi-identifiers. Sensitive Data Protection's risk analysis APIs simulate a re-identification dataset to approximate the steps an attacker might go through to compare the original dataset in order to re-identify the data. For our previous example, because it deals with US locations (ZIP codes) and personal data (ages), and because we assume that the attacker doesn't know who participated in the survey, the re-identification dataset could be everyone living in the US.

Now that you have quasi-identifiers and a re-identification dataset, you can compute the _k_ -map value: Your data satisfies _k_ -map with value _k_ if every combination of values for the quasi-identifiers appears at least _k_ times in the re-identification dataset.

Given this definition, and that the first row in our database likely only corresponds to one person in the US, the example dataset doesn't satisfy a _k_ -map value requirement of 2 or more. To get a larger _k_ -map value, we could remove age values like we've done here:

ZIP code | age  
---|---  
85535 | **  
60629 | **  
  
As previously mentioned, the 85535 ZIP code has about 20 people and 60629 has over 100,000. Therefore, we can estimate that this new, generalized dataset has a _k_ -map value of around 20.

### _k_ -map resources

For more information about _k_ -map and its relationship to _k_ -anonymity, see [Protecting Privacy Using k-Anonymity](https://scholar.google.com/scholar?q=Protecting+Privacy+Using+k-Anonymity), by Khaled El Emam and Fida Kamal Dankar, in the _Journal of the American Medical Informatics Association_.

To learn how to compute _k_ -map estimates with Sensitive Data Protection, see [Computing _k_ -map for a dataset](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-k-map).

## About _δ_ -presence

Delta-presence (_δ_ -presence) estimates the risk associated with an attacker who wants to find out whether their target is in the dataset. This is slightly different than re-identification risk in that the goal is not to find which exact record corresponds to which individual, only to know whether an individual is part of the dataset. Using this metric is particularly appropriate if all individuals in the dataset share a common sensitive attribute; for example, they all have the same medical diagnosis.

Like the other risk metrics, _δ_ -presence requires you to determine which columns of your database are quasi-identifiers. In doing this, you are stating what data an attacker will most likely use to find out which individuals are in the dataset. Like _k_ -map, computing _δ_ -presence requires an attack dataset: a larger table with which to compare rows in the original dataset.

Consider the following small example dataset. This sample data is part of a larger hypothetical database of people with a certain genetic disease.

ZIP code | age  
---|---  
85942 | 72  
85942 | 72  
62083 | 53  
  
In the United States ZIP code 85942, there are approximately 2 people aged 72, and in ZIP code 62083, there are approximately 5 people aged 53. The first two records are not exactly re-identifiable because both have the same quasi-identifiers. But since only two individuals share these quasi-identifiers in the larger population, an attacker can deduce that both of them suffer from the genetic disease. _δ_ -presence quantifies this particular risk by computing the ratio of people with certain quasi-identifiers that are in the dataset.

_δ_ -presence, like the other risk metrics, requires you to determine which columns of your database are quasi-identifiers. And like for _k_ -map estimation, Sensitive Data Protection's risk analysis APIs simulate a population dataset to approximate the dataset that an attacker might use to find out who is in the dataset. For our previous example, because it deals with US locations (ZIP codes) and personal data (ages), and because we assume that the attacker doesn't know who has the genetic disease, this population dataset could be everyone living in the US.

Now that you have quasi-identifiers and a re-identification dataset, you can compute the _δ_ -presence value: your data satisfies the _δ_ -presence with value _δ_ if every combination of values for the quasi-identifiers appears at most _δ_ * _k_ times in your dataset, where _k_ is the total number of people with these quasi-identifier values in the population dataset. Unlike _k_ in _k_ -anonymity or _k_ -map, the _δ_ in _δ_ -presence is a real number between 0 and 1.

Given this definition, and that both people of age 72 in ZIP code 85942 in the general population are also in our database, this dataset doesn't satisfy _δ_ -presence for any _δ_ strictly smaller than 1. To get a lower _δ_ -presence value, we could remove the age value of the first two rows:

ZIP code | age  
---|---  
85942 | **  
85942 | **  
62083 | 53  
  
Now, since 80 people live in ZIP code 85942, the _δ_ value for the first two records is approximately 2 / 80 = 2.5%; and the _δ_ value for the third record is approximately 1 / 5 = 20%. Therefore, we can estimate that this new, generalized dataset has a _δ_ -presence value of around 20%.

### _δ_ -presence resources

For more information about _δ_ -presence estimation based on statistical data, see [δ-Presence Without Complete World Knowledge](https://www.semanticscholar.org/paper/S-Presence-Without-Complete-World-Knlowedge-Nergiz-Clifton/9844b86be108d54193fc149d4901fac815a08845), by Mehmet Ercan Nergiz and Chris Clifton from the Purdue University _Department of Computer Science Technical Reports_.

To learn how to compute _δ_ -presence estimates with Sensitive Data Protection, see [Computing _δ_ -presence for a dataset](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-d-presence).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
