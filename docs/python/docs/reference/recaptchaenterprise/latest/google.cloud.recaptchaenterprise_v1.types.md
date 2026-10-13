---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types
title: Package types (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:52.001556+00:00
---

# Package types (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 

API documentation for `recaptchaenterprise_v1.types` package.

## Classes 

### [AccountDefenderAssessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AccountDefenderAssessment)

Account defense risk assessment.

### [AccountVerificationInfo](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AccountVerificationInfo)

Information about account verification, used for identity verification.

### [AddIpOverrideRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AddIpOverrideRequest)

The AddIpOverride request message.

### [AddIpOverrideResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AddIpOverrideResponse)

Response for AddIpOverride.

### [AndroidKeySettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AndroidKeySettings)

Settings specific to keys that can be used by Android apps.

### [AnnotateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest)

The request message to annotate an Assessment.

### [AnnotateAssessmentResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentResponse)

Empty response for AnnotateAssessment.

### [AppleDeveloperId](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AppleDeveloperId)

Contains fields that are required to perform Apple-specific integrity checks.

### [Assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment)

A reCAPTCHA Enterprise assessment resource.

### [AssessmentEnvironment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AssessmentEnvironment)

The environment creating the assessment. This describes your environment (the system invoking CreateAssessment), NOT the environment of your user.

### [Bot](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Bot)

Bot information and metadata.

### [ChallengeMetrics](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeMetrics)

Metrics related to challenges.

### [ChallengeRule](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeRule)

A rule to configure the behavior of reCAPTCHA for conditionally presenting a challenge.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ChallengeRuleEvaluation](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeRuleEvaluation)

Information about the evaluation of a `ChallengeRule`.

### [ChallengeRuleGroup](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeRuleGroup)

A collection of challenge rules that applies to one or more actions.

### [ChallengeType](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ChallengeType)

Enum of challenge types for Universal, `POLICY_BASED_CHALLENGE` and `INVISIBLE` keys. Ensure that applications can handle values not explicitly listed.

### [ClientSettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ClientSettings)

Configuration for clients to protect with reCAPTCHA.

### [CreateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateAssessmentRequest)

The create assessment request message.

### [CreateFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateFirewallPolicyRequest)

The create firewall policy request message.

### [CreateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateKeyRequest)

The create key request message.

### [DeleteFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.DeleteFirewallPolicyRequest)

The delete firewall policy request message.

### [DeleteKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.DeleteKeyRequest)

The delete key request message.

### [EndpointVerificationInfo](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.EndpointVerificationInfo)

Information about a verification endpoint that can be used for 2FA.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Event](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Event)

The event being assessed.

### [ExpressKeySettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ExpressKeySettings)

Settings specific to keys that can be used for reCAPTCHA Express.

### [FirewallAction](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallAction)

An individual action. Each action represents what to do if a policy matches.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FirewallPolicy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallPolicy)

A FirewallPolicy represents a single matching pattern and resulting actions to take.

### [FirewallPolicyAssessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallPolicyAssessment)

Policy config assessment.

### [FraudPreventionAssessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FraudPreventionAssessment)

Assessment for Fraud Prevention.

### [FraudSignals](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FraudSignals)

Fraud signals describing users and cards involved in the transaction.

### [GetFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetFirewallPolicyRequest)

The get firewall policy request message.

### [GetKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetKeyRequest)

The get key request message.

### [GetMetricsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetMetricsRequest)

The get metrics request message.

### [GetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetPolicyRequest)

The request message to get a policy.

### [IOSKeySettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.IOSKeySettings)

Settings specific to keys that can be used by iOS apps.

### [IpOverrideData](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.IpOverrideData)

Information about the IP or IP range override.

### [Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key)

A key used to identify and configure applications (web and/or mobile) that use reCAPTCHA Enterprise.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListFirewallPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesRequest)

The list firewall policies request message.

### [ListFirewallPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesResponse)

Response to request to list firewall policies belonging to a project.

### [ListIpOverridesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListIpOverridesRequest)

The ListIpOverrides request message.

### [ListIpOverridesResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListIpOverridesResponse)

Response for ListIpOverrides.

### [ListKeysRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListKeysRequest)

The list keys request message.

### [ListKeysResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListKeysResponse)

Response to request to list keys in a project.

### [ListRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsRequest)

The request message to list memberships in a related account group.

### [ListRelatedAccountGroupMembershipsResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsResponse)

The response to a `ListRelatedAccountGroupMemberships` call.

### [ListRelatedAccountGroupsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsRequest)

The request message to list related account groups.

### [ListRelatedAccountGroupsResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsResponse)

The response to a `ListRelatedAccountGroups` call.

### [Metrics](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Metrics)

Metrics for a single Key.

### [MigrateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.MigrateKeyRequest)

The migrate key request message.

### [PhoneAuthenticationEvent](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.PhoneAuthenticationEvent)

Details on a phone authentication event

### [PhoneFraudAssessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.PhoneFraudAssessment)

Assessment for Phone Fraud

### [Policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Policy)

A complete configuration set containing multiple grouped rules defining the behavior of reCAPTCHA for fraud detection and prevention.

### [PolicyEvaluation](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.PolicyEvaluation)

Information about the policy evaluation.

### [PrivatePasswordLeakVerification](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.PrivatePasswordLeakVerification)

Private password leak verification info.

### [ProtectedEndpoint](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ProtectedEndpoint)

Configuration for an API endpoint to protect with reCAPTCHA.

### [ProtectedEndpointGroup](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ProtectedEndpointGroup)

Configuration for API endpoints to protect with reCAPTCHA.

### [RelatedAccountGroup](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RelatedAccountGroup)

A group of related accounts.

### [RelatedAccountGroupMembership](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RelatedAccountGroupMembership)

A membership in a group of related accounts.

### [RemoveIpOverrideRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideRequest)

The RemoveIpOverride request message.

### [RemoveIpOverrideResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideResponse)

Response for RemoveIpOverride.

### [ReorderFirewallPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesRequest)

The reorder firewall policies request message.

### [ReorderFirewallPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesResponse)

The reorder firewall policies response message.

### [RetrieveLegacySecretKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyRequest)

The retrieve legacy secret key request message.

### [RetrieveLegacySecretKeyResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyResponse)

Secret key is used only in legacy reCAPTCHA. It must be used in a 3rd party integration with legacy reCAPTCHA.

### [RiskAnalysis](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RiskAnalysis)

Risk analysis result for an event.

### [ScoreDistribution](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ScoreDistribution)

Score distribution.

### [ScoreMetrics](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ScoreMetrics)

Metrics related to scoring.

### [SearchRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsRequest)

The request message to search related account group memberships.

### [SearchRelatedAccountGroupMembershipsResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsResponse)

The response to a `SearchRelatedAccountGroupMemberships` call.

### [SmsTollFraudVerdict](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.SmsTollFraudVerdict)

Information about SMS toll fraud.

### [TestingOptions](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.TestingOptions)

Options for user acceptance testing.

### [TokenProperties](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.TokenProperties)

Properties of the provided event token.

### [TransactionData](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.TransactionData)

Transaction data associated with a payment protected by reCAPTCHA Enterprise.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TransactionEvent](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.TransactionEvent)

Describes an event in the lifecycle of a payment transaction.

### [UniversalKeySettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UniversalKeySettings)

Settings for keys that are configured through their Policy.

### [UpdateFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdateFirewallPolicyRequest)

The update firewall policy request message.

### [UpdateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdateKeyRequest)

The update key request message.

### [UpdatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdatePolicyRequest)

The request message to update a policy.

### [UserId](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UserId)

An identifier associated with a user.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UserInfo](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UserInfo)

User information associated with a request protected by reCAPTCHA Enterprise.

### [WafSettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.WafSettings)

Settings specific to keys that can be used for WAF (Web Application Firewall).

### [WebKeySettings](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.WebKeySettings)

Settings specific to keys that can be used by websites.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
