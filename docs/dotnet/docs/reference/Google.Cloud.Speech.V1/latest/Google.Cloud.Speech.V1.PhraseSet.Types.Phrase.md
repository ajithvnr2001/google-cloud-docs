---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase
title: Google Cloud Speech v1 API - Class PhraseSet.Types.Phrase (3.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:55.895054+00:00
---

# Google Cloud Speech v1 API - Class PhraseSet.Types.Phrase (3.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Speech v1 API - Class PhraseSet.Types.Phrase (3.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.8.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.7.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.6.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.5.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.4.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.3.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.2.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.1.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.0.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.9.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.8.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.7.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.6.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.5.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.4.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.3.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.2.0/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)


    
    
    public sealed class PhraseSet.Types.Phrase : IMessage<PhraseSet.Types.Phrase>, IEquatable<PhraseSet.Types.Phrase>, IDeepCloneable<PhraseSet.Types.Phrase>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Speech v1 API class PhraseSet.Types.Phrase.

A phrases containing words and phrase "hints" so that the speech recognition is more likely to recognize them. This can be used to improve the accuracy for specific words and phrases, for example, if specific commands are typically spoken by the user. This can also be used to add additional words to the vocabulary of the recognizer. See [usage limits](https://cloud.google.com/speech-to-text/quotas#content).

List items can also include pre-built or custom classes containing groups of words that represent common concepts that occur in natural language. For example, rather than providing a phrase hint for every month of the year (e.g. "i was born in january", "i was born in febuary", ...), use the pre-built `$MONTH` class improves the likelihood of correctly transcribing audio that includes months (e.g. "i was born in $month"). To refer to pre-built classes, use the class' symbol prepended with `$` e.g. `$MONTH`. To refer to custom classes that were defined inline in the request, set the class's `custom_class_id` to a string unique to all class resources and inline classes. Then use the class' id wrapped in $`{...}` e.g. "${my-months}". To refer to custom classes resources, use the class' id wrapped in `${}` (e.g. `${my-months}`).

Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PhraseSet.Types.Phrase

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PhraseSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types)[Phrase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PhraseSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types)[Phrase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PhraseSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types)[Phrase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1)

## Assembly

Google.Cloud.Speech.V1.dll

## Constructors 

### Phrase()
    
    
    public Phrase()

### Phrase(Phrase)
    
    
    public Phrase(PhraseSet.Types.Phrase other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PhraseSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types)[Phrase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.PhraseSet.Types.Phrase)`  
  
  
## Properties 

### Boost
    
    
    public float Boost { get; set; }

Hint Boost. Overrides the boost set at the phrase set level. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost will simply be ignored. Though `boost` can accept a wide range of positive values, most use cases are best served with values between 0 and 20. We recommend using a binary search approach to finding the optimal value for your use case as well as adding phrases both with and without boost to your requests.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### Value
    
    
    public string Value { get; set; }

The phrase itself.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
