---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer
title: Class Answer (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:36.908040+00:00
---

# Class Answer (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Answer (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    Answer(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Defines an answer.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/engines/{engine}/sessions/*/answers/*`  
`state` |  `[google.cloud.discoveryengine_v1.types.Answer.State](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.State)`   
The state of the answer generation.   
`answer_text` |  `str`   
The textual answer.   
`grounding_score` |  `float`   
A score in the range of [0, 1] describing how grounded the answer is by the reference chunks. This field is a member of `oneof`_ `_grounding_score`.   
`citations` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.Answer.Citation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Citation)]`   
Citations.   
`grounding_supports` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.Answer.GroundingSupport](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.GroundingSupport)]`   
Optional. Grounding supports.   
`references` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.Answer.Reference](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Reference)]`   
References.   
`related_questions` |  `MutableSequence[str]`   
Suggested related questions.   
`steps` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.Answer.Step](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step)]`   
Answer generation steps.   
`query_understanding_info` |  `[google.cloud.discoveryengine_v1.types.Answer.QueryUnderstandingInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.QueryUnderstandingInfo)`   
Query understanding information.   
`answer_skipped_reasons` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.Answer.AnswerSkippedReason](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.AnswerSkippedReason)]`   
Additional answer-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Answer creation timestamp.   
`complete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Answer completed timestamp.   
`safety_ratings` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.SafetyRating](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SafetyRating)]`   
Optional. Safety ratings.   
  
## Classes 

### AnswerSkippedReason
    
    
    AnswerSkippedReason(value)

An enum for answer skipped reasons.
    
    
        Google skips the answer if the query is chit
        chat.
    OUT_OF_DOMAIN_QUERY_IGNORED (3):
        The out-of-domain query ignored case.
    
        Google skips the answer if there are no
        high-relevance search results.
    POTENTIAL_POLICY_VIOLATION (4):
        The potential policy violation case.
    
        Google skips the answer if there is a potential
        policy violation detected. This includes content
        that may be violent or toxic.
    NO_RELEVANT_CONTENT (5):
        The no relevant content case.
    
        Google skips the answer if there is no relevant
        content in the retrieved search results.
    JAIL_BREAKING_QUERY_IGNORED (6):
        The jail-breaking query ignored case.
    
        For example, "Reply in the tone of a competing
        company's CEO". Google skips the answer if the
        query is classified as a jail-breaking query.
    CUSTOMER_POLICY_VIOLATION (7):
        The customer policy violation case.
    
        Google skips the summary if there is a customer
        policy violation detected. The policy is defined
        by the customer.
    NON_ANSWER_SEEKING_QUERY_IGNORED_V2 (8):
        The non-answer seeking query ignored case.
    
        Google skips the answer if the query doesn't
        have clear intent.
    LOW_GROUNDED_ANSWER (9):
        The low-grounded answer case.
    
        Google skips the answer if a well grounded
        answer was unable to be generated.
    USER_DEFINED_CLASSIFICATION_QUERY_IGNORED (10):
        The user defined query classification ignored
        case.
        Google skips the answer if the query is
        classified as a user defined query
        classification.
    UNHELPFUL_ANSWER (11):
        The unhelpful answer case.
    
        Google skips the answer if the answer is not
        helpful. This can be due to a variety of
        factors, including but not limited to: the query
        is not answerable, the answer is not relevant to
        the query, or the answer is not well-formatted.
    

### Citation
    
    
    Citation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Citation info for a segment.

### CitationSource
    
    
    CitationSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Citation source.

### GroundingSupport
    
    
    GroundingSupport(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Grounding support for a claim in `answer_text`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### QueryUnderstandingInfo
    
    
    QueryUnderstandingInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Query understanding information.

### Reference
    
    
    Reference(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Reference.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### State
    
    
    State(value)

Enumeration of the state of the answer generation.

### Step
    
    
    Step(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Step information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
