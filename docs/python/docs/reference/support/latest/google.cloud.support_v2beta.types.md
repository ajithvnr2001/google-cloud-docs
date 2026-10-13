---
url: https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types
title: Package types (0.5.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:01.962115+00:00
---

# Package types (0.5.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.5.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.4 (latest)  0.5.3  0.4.0  0.3.0  0.2.0  0.1.19 

API documentation for `support_v2beta.types` package.

## Classes 

### [Actor](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.Actor)

An Actor represents an entity that performed an action. For example, an actor could be a user who posted a comment on a support case, a user who uploaded an attachment, or a service account that created a support case.

### [Attachment](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.Attachment)

An Attachment contains metadata about a file that was uploaded to a case - it is NOT a file itself. That being said, the name of an Attachment object can be used to download its accompanying file through the `media.download` endpoint.

While attachments can be uploaded in the console at the same time as a comment, they're associated on a "case" level, not a "comment" level.

### [Case](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.Case)

A Case is an object that contains the details of a support case. It contains fields for the time it was created, its priority, its classification, and more. Cases can also have comments and attachments that get added over time.

A case is parented by a Google Cloud organization or project.

Organizations are identified by a number, so the name of a case parented by an organization would look like this:

::

organizations/123/cases/456

Projects have two unique identifiers, an ID and a number, and they look like this:

::

projects/abc/cases/456

::

projects/123/cases/456

You can use either of them when calling the API. To learn more about project identifiers, see `AIP-2510 <https://google.aip.dev/cloud/2510>`__.

### [CaseClassification](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.CaseClassification)

A Case Classification represents the topic that a case is about. It's very important to use accurate classifications, because they're used to route your cases to specialists who can help you.

A classification always has an ID that is its unique identifier. A valid ID is required when creating a case.

### [CloseCaseRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.CloseCaseRequest)

The request message for the CloseCase endpoint.

### [Comment](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.Comment)

A comment associated with a support case.

Case comments are the primary way for Google Support to communicate with a user who has opened a case. When a user responds to Google Support, the user's responses also appear as comments.

### [CreateCaseRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.CreateCaseRequest)

The request message for the CreateCase endpoint.

### [CreateCommentRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.CreateCommentRequest)

The request message for the CreateComment endpoint.

### [CreateSupportEventSubscriptionRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.CreateSupportEventSubscriptionRequest)

Request message for CreateSupportEventSubscription.

### [DeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.DeleteSupportEventSubscriptionRequest)

Request message for DeleteSupportEventSubscription.

### [EmailMessage](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.EmailMessage)

An email associated with a support case.

### [EscalateCaseRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.EscalateCaseRequest)

The request message for the EscalateCase endpoint.

### [Escalation](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.Escalation)

An escalation of a support case.

### [ExpungeSupportEventSubscriptionRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ExpungeSupportEventSubscriptionRequest)

Request message for ExpungeSupportEventSubscription.

### [FeedItem](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.FeedItem)

A feed item associated with a support case.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetAttachmentRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.GetAttachmentRequest)

Request for getting an attachment.

### [GetCaseRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.GetCaseRequest)

The request message for the GetCase endpoint.

### [GetCommentRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.GetCommentRequest)

The request message for the GetComment endpoint.

### [GetSupportEventSubscriptionRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.GetSupportEventSubscriptionRequest)

Request message for GetSupportEventSubscription.

### [ListAttachmentsRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ListAttachmentsRequest)

The request message for the ListAttachments endpoint.

### [ListAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ListAttachmentsResponse)

The response message for the ListAttachments endpoint.

### [ListCasesRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ListCasesRequest)

The request message for the ListCases endpoint.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListCasesResponse](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ListCasesResponse)

The response message for the ListCases endpoint.

### [ListCommentsRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ListCommentsRequest)

The request message for the ListComments endpoint.

### [ListCommentsResponse](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ListCommentsResponse)

The response message for the ListComments endpoint.

### [ListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ListSupportEventSubscriptionsRequest)

Request message for ListSupportEventSubscriptions.

### [ListSupportEventSubscriptionsResponse](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ListSupportEventSubscriptionsResponse)

Response message for ListSupportEventSubscriptions.

### [Product](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.Product)

The product a case may be associated with.

### [ProductLine](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ProductLine)

The product line a support case may be associated with.

### [SearchCaseClassificationsRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.SearchCaseClassificationsRequest)

The request message for the SearchCaseClassifications endpoint.

### [SearchCaseClassificationsResponse](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.SearchCaseClassificationsResponse)

The response message for SearchCaseClassifications endpoint.

### [SearchCasesRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.SearchCasesRequest)

The request message for the SearchCases endpoint.

### [SearchCasesResponse](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.SearchCasesResponse)

The response message for the SearchCases endpoint.

### [ShowFeedRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ShowFeedRequest)

The request message for the ShowFeed endpoint.

### [ShowFeedResponse](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.ShowFeedResponse)

The response message for the ShowFeed endpoint.

### [SupportEventSubscription](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.SupportEventSubscription)

A support event subscription.

You can also manage support event subscriptions using other tools:

  * `gcloud support support-event-subscriptions`` </sdk/gcloud/reference/support/support-event-subscriptions>`__ (or`gcloud beta`` </sdk/gcloud/reference/beta/support/support-event-subscriptions>`__ for beta)
  * `Terraform`google_cloud_support_support_event_subscription`<https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_support_support_event_subscription>`**(or`google-beta provider <https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/cloud_support_support_event_subscription>`** for beta)



### [TextContent](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.TextContent)

Stores text attached to a support object.

### [UndeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.UndeleteSupportEventSubscriptionRequest)

Request message for UndeleteSupportEventSubscription.

### [UpdateCaseRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.UpdateCaseRequest)

The request message for the UpdateCase endpoint

### [UpdateSupportEventSubscriptionRequest](https://docs.cloud.google.com/python/docs/reference/support/latest/google.cloud.support_v2beta.types.UpdateSupportEventSubscriptionRequest)

Request message for UpdateSupportEventSubscription.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
