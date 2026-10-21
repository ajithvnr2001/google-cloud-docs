---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood/
title: Match likelihood \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:28.341878+00:00
---

# Match likelihood  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Match likelihood Stay organized with collections  Save and categorize content based on your preferences. 

Scan results are categorized based on how likely they are to represent a match. Sensitive Data Protection uses a bucketized representation of likelihood, which is intended to indicate how likely it is that a piece of data matches a given [infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference "InfoTypes reference").

## How likelihood works

When you configure a Sensitive Data Protection scan, you set the infoTypes that you want Sensitive Data Protection to scan for. To narrow the scan results, you can set a _minimum likelihood level_ in your request.

For each potential match (_finding_) that is detected during the scan, Sensitive Data Protection assigns a likelihood level. The likelihood level of a finding describes how likely it is that the finding matches an infoType that you're scanning for. For example, Sensitive Data Protection might assign a likelihood of `LIKELY` to a finding that looks like an email address.

When Sensitive Data Protection returns the results, it filters out any findings that have a lower likelihood than the minimum likelihood level that you set in your request. For example, if you set the minimum likelihood to `POSSIBLE`, you get only the findings that were evaluated as `POSSIBLE`, `LIKELY`, and `VERY_LIKELY`. If you set the minimum likelihood to `VERY_LIKELY`, you get the smallest number of findings.

**Tip:** In your request, you can set the same minimum likelihood level for all infoTypes that you're scanning for. Alternatively, you can [set specific minimum likelihood levels for specific infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#FIELDS.min_likelihood_per_info_type).

## Likelihood levels

The following table lists the possible likelihood values that Sensitive Data Protection can assign to a finding.

ENUM | Description  
---|---  
`VERY_UNLIKELY` | Characterized by the following:  


  * A weak signal.


  * Absence of contextual clues.


  * Negative signals for a given infoType.

  
`UNLIKELY` | Characterized by the following:  


  * One or more weak signals. 


  * A stronger signal for another infoType.

  
`POSSIBLE` | Characterized by the following:  


  * One or more signals toward a given infoType. Signals can include passing checksums.


  * Lack of a strong contextual clue and unique, specific formatting.

  
`LIKELY` | Characterized by one or more strong signals for a given infoType. Signals can include passing checksums, strong contextual clues, and unique, specific formatting.   
`VERY_LIKELY` | Characterized by having many strong signals for a given infoType. Signals can include passing checksums, strong contextual clues, and unique, specific formatting.   
  
## Choosing a minimum likelihood level for the scan results

In general, when you set a higher minimum likelihood level in your Sensitive Data Protection request, the results have a lower number of false positives (sometimes called _noise_). However, the results can also exclude more true positives. Choosing a minimum likelihood level involves finding the right balance between [recall and precision](https://en.wikipedia.org/wiki/Precision_and_recall).

For example, suppose that there are 10 street addresses in a document and Sensitive Data Protection identified 5 street addresses. However, among the findings that Sensitive Data Protection identified, there are actually only 4 street addresses.

  * _Recall_ is the number of true positive instances out of the total number of relevant instances. In this example, the recall is 4/10.
  * _Precision_ is the number of true positive instances out of the total number of instances that Sensitive Data Protection identifies. In this example, the precision is 4/5.



In this example, the precision is high but the recall is relatively low.

The minimum likelihood level that you set affects the level of recall and precision that you get in your scan results. The following table describes when each minimum likelihood level is useful and how recall and precision vary at each level.

Minimum likelihood level | Description  
---|---  
`LIKELIHOOD_UNSPECIFIED` | Default value; same as `POSSIBLE`.  
`VERY_UNLIKELY` | Useful if you need the highest recall. This minimum likelihood level generates the most noise.  
`UNLIKELY` | Useful if you need higher recall. This minimum likelihood level generates some noise.  
`POSSIBLE` | Useful if you want a balance of precision and recall.  
`LIKELY` | Useful if you need a higher precision at the expense of some recall.  
`VERY_LIKELY` | Useful if you want the highest precision at the expense of recall.  
  
## Default minimum likelihood

If you don't set a minimum likelihood in your request, or if you set it to `LIKELIHOOD_UNSPECIFIED`, Sensitive Data Protection returns only the findings with a likelihood of `POSSIBLE` and higher.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
