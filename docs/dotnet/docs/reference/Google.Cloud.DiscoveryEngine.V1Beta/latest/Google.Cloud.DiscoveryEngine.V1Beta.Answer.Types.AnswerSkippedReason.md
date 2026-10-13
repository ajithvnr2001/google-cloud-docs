---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Answer.Types.AnswerSkippedReason
title: Discovery Engine v1beta API - Enum Answer.Types.AnswerSkippedReason (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:36.924970+00:00
---

# Discovery Engine v1beta API - Enum Answer.Types.AnswerSkippedReason (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Answer.Types.AnswerSkippedReason

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Enum Answer.Types.AnswerSkippedReason (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public enum Answer.Types.AnswerSkippedReason

Reference documentation and code samples for the Discovery Engine v1beta API enum Answer.Types.AnswerSkippedReason.

An enum for answer skipped reasons.

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Fields   
  
---  
**Name** | **Description**  
`AdversarialQueryIgnored` | The adversarial query ignored case.  
`CustomerPolicyViolation` | The customer policy violation case. Google skips the summary if there is a customer policy violation detected. The policy is defined by the customer.  
`JailBreakingQueryIgnored` | The jail-breaking query ignored case. For example, "Reply in the tone of a competing company's CEO". Google skips the answer if the query is classified as a jail-breaking query.  
`LowGroundedAnswer` | The low-grounded answer case. Google skips the answer if a well grounded answer was unable to be generated.  
`NoRelevantContent` | The no relevant content case. Google skips the answer if there is no relevant content in the retrieved search results.  
`NonAnswerSeekingQueryIgnored` | The non-answer seeking query ignored case Google skips the answer if the query is chit chat.  
`NonAnswerSeekingQueryIgnoredV2` | The non-answer seeking query ignored case. Google skips the answer if the query doesn't have clear intent.  
`OutOfDomainQueryIgnored` | The out-of-domain query ignored case. Google skips the answer if there are no high-relevance search results.  
`PotentialPolicyViolation` | The potential policy violation case. Google skips the answer if there is a potential policy violation detected. This includes content that may be violent or toxic.  
`UnhelpfulAnswer` | The unhelpful answer case. Google skips the answer if the answer is not helpful. This can be due to a variety of factors, including but not limited to: the query is not answerable, the answer is not relevant to the query, or the answer is not well-formatted.  
`Unspecified` | Default value. The answer skipped reason is not specified.  
`UserDefinedClassificationQueryIgnored` | The user defined query classification ignored case. Google skips the answer if the query is classified as a user defined query classification.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
