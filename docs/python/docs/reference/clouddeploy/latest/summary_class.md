---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/summary_class/
title: Package Classes (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:34.118857+00:00
---

# Package Classes (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 

Summary of entries of Classes for clouddeploy.

## Classes 

### [CloudDeployAsyncClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployAsyncClient)

CloudDeploy service creates and manages Continuous Delivery operations on Google Cloud Platform via Skaffold (<https://skaffold.dev>).

### [CloudDeployClient](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.CloudDeployClient)

CloudDeploy service creates and manages Continuous Delivery operations on Google Cloud Platform via Skaffold (<https://skaffold.dev>).

### [ListAutomationRunsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager)

A pager for iterating through `list_automation_runs` requests.

This class thinly wraps an initial [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse) object, and provides an `__aiter__` method to iterate through its `automation_runs` field.

If there are more pages, the `__aiter__` method will make additional `ListAutomationRuns` requests and continue to iterate through the `automation_runs` field on the corresponding responses.

All the usual [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutomationRunsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsPager)

A pager for iterating through `list_automation_runs` requests.

This class thinly wraps an initial [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse) object, and provides an `__iter__` method to iterate through its `automation_runs` field.

If there are more pages, the `__iter__` method will make additional `ListAutomationRuns` requests and continue to iterate through the `automation_runs` field on the corresponding responses.

All the usual [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutomationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager)

A pager for iterating through `list_automations` requests.

This class thinly wraps an initial [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse) object, and provides an `__aiter__` method to iterate through its `automations` field.

If there are more pages, the `__aiter__` method will make additional `ListAutomations` requests and continue to iterate through the `automations` field on the corresponding responses.

All the usual [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutomationsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsPager)

A pager for iterating through `list_automations` requests.

This class thinly wraps an initial [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse) object, and provides an `__iter__` method to iterate through its `automations` field.

If there are more pages, the `__iter__` method will make additional `ListAutomations` requests and continue to iterate through the `automations` field on the corresponding responses.

All the usual [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListCustomTargetTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager)

A pager for iterating through `list_custom_target_types` requests.

This class thinly wraps an initial [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse) object, and provides an `__aiter__` method to iterate through its `custom_target_types` field.

If there are more pages, the `__aiter__` method will make additional `ListCustomTargetTypes` requests and continue to iterate through the `custom_target_types` field on the corresponding responses.

All the usual [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListCustomTargetTypesPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesPager)

A pager for iterating through `list_custom_target_types` requests.

This class thinly wraps an initial [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse) object, and provides an `__iter__` method to iterate through its `custom_target_types` field.

If there are more pages, the `__iter__` method will make additional `ListCustomTargetTypes` requests and continue to iterate through the `custom_target_types` field on the corresponding responses.

All the usual [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeliveryPipelinesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager)

A pager for iterating through `list_delivery_pipelines` requests.

This class thinly wraps an initial [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse) object, and provides an `__aiter__` method to iterate through its `delivery_pipelines` field.

If there are more pages, the `__aiter__` method will make additional `ListDeliveryPipelines` requests and continue to iterate through the `delivery_pipelines` field on the corresponding responses.

All the usual [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeliveryPipelinesPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesPager)

A pager for iterating through `list_delivery_pipelines` requests.

This class thinly wraps an initial [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse) object, and provides an `__iter__` method to iterate through its `delivery_pipelines` field.

If there are more pages, the `__iter__` method will make additional `ListDeliveryPipelines` requests and continue to iterate through the `delivery_pipelines` field on the corresponding responses.

All the usual [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeployPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager)

A pager for iterating through `list_deploy_policies` requests.

This class thinly wraps an initial [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `deploy_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListDeployPolicies` requests and continue to iterate through the `deploy_policies` field on the corresponding responses.

All the usual [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeployPoliciesPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesPager)

A pager for iterating through `list_deploy_policies` requests.

This class thinly wraps an initial [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse) object, and provides an `__iter__` method to iterate through its `deploy_policies` field.

If there are more pages, the `__iter__` method will make additional `ListDeployPolicies` requests and continue to iterate through the `deploy_policies` field on the corresponding responses.

All the usual [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobRunsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager)

A pager for iterating through `list_job_runs` requests.

This class thinly wraps an initial [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse) object, and provides an `__aiter__` method to iterate through its `job_runs` field.

If there are more pages, the `__aiter__` method will make additional `ListJobRuns` requests and continue to iterate through the `job_runs` field on the corresponding responses.

All the usual [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobRunsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsPager)

A pager for iterating through `list_job_runs` requests.

This class thinly wraps an initial [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse) object, and provides an `__iter__` method to iterate through its `job_runs` field.

If there are more pages, the `__iter__` method will make additional `ListJobRuns` requests and continue to iterate through the `job_runs` field on the corresponding responses.

All the usual [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListReleasesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager)

A pager for iterating through `list_releases` requests.

This class thinly wraps an initial [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse) object, and provides an `__aiter__` method to iterate through its `releases` field.

If there are more pages, the `__aiter__` method will make additional `ListReleases` requests and continue to iterate through the `releases` field on the corresponding responses.

All the usual [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListReleasesPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesPager)

A pager for iterating through `list_releases` requests.

This class thinly wraps an initial [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse) object, and provides an `__iter__` method to iterate through its `releases` field.

If there are more pages, the `__iter__` method will make additional `ListReleases` requests and continue to iterate through the `releases` field on the corresponding responses.

All the usual [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRolloutsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager)

A pager for iterating through `list_rollouts` requests.

This class thinly wraps an initial [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse) object, and provides an `__aiter__` method to iterate through its `rollouts` field.

If there are more pages, the `__aiter__` method will make additional `ListRollouts` requests and continue to iterate through the `rollouts` field on the corresponding responses.

All the usual [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRolloutsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsPager)

A pager for iterating through `list_rollouts` requests.

This class thinly wraps an initial [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse) object, and provides an `__iter__` method to iterate through its `rollouts` field.

If there are more pages, the `__iter__` method will make additional `ListRollouts` requests and continue to iterate through the `rollouts` field on the corresponding responses.

All the usual [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager)

A pager for iterating through `list_targets` requests.

This class thinly wraps an initial [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse) object, and provides an `__aiter__` method to iterate through its `targets` field.

If there are more pages, the `__aiter__` method will make additional `ListTargets` requests and continue to iterate through the `targets` field on the corresponding responses.

All the usual [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsPager)

A pager for iterating through `list_targets` requests.

This class thinly wraps an initial [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse) object, and provides an `__iter__` method to iterate through its `targets` field.

If there are more pages, the `__iter__` method will make additional `ListTargets` requests and continue to iterate through the `targets` field on the corresponding responses.

All the usual [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AbandonReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AbandonReleaseRequest)

The request object used by `AbandonRelease`.

### [AbandonReleaseResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AbandonReleaseResponse)

The response object for `AbandonRelease`.

### [AdvanceChildRolloutJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceChildRolloutJob)

An advanceChildRollout Job.

### [AdvanceChildRolloutJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceChildRolloutJobRun)

AdvanceChildRolloutJobRun contains information specific to a advanceChildRollout `JobRun`.

### [AdvanceRolloutOperation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceRolloutOperation)

Contains the information of an automated advance-rollout operation.

### [AdvanceRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceRolloutRequest)

The request object used by `AdvanceRollout`.

### [AdvanceRolloutResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceRolloutResponse)

The response object from `AdvanceRollout`.

### [AdvanceRolloutRule](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AdvanceRolloutRule)

The `AdvanceRollout` automation rule will automatically advance a successful Rollout to the next phase.

### [AnthosCluster](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AnthosCluster)

Information specifying an Anthos Cluster.

### [ApproveRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ApproveRolloutRequest)

The request object used by `ApproveRollout`.

### [ApproveRolloutResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ApproveRolloutResponse)

The response object from `ApproveRollout`.

### [AssociatedEntities](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AssociatedEntities)

Information about entities associated with a `Target`.

### [Automation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation)

An `Automation` resource in the Cloud Deploy API.

An `Automation` enables the automation of manually driven actions for a Delivery Pipeline, which includes Release promotion among Targets, Rollout repair and Rollout deployment strategy advancement. The intention of Automation is to reduce manual intervention in the continuous delivery process.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation.AnnotationsEntry)

The abstract base class for a message.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Automation.LabelsEntry)

The abstract base class for a message.

### [AutomationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationEvent)

Payload proto for "clouddeploy.googleapis.com/automation" Platform Log event that describes the Automation related events.

### [AutomationResourceSelector](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationResourceSelector)

AutomationResourceSelector contains the information to select the resources to which an Automation is going to be applied.

### [AutomationRolloutMetadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRolloutMetadata)

AutomationRolloutMetadata contains Automation-related actions that were performed on a rollout.

### [AutomationRule](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRule)

`AutomationRule` defines the automation activities.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AutomationRuleCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRuleCondition)

`AutomationRuleCondition` contains conditions relevant to an `Automation` rule.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AutomationRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRun)

An `AutomationRun` resource in the Cloud Deploy API.

An `AutomationRun` represents an execution instance of an automation rule.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRun.State)

Valid state of an `AutomationRun`.

### [AutomationRunEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.AutomationRunEvent)

Payload proto for "clouddeploy.googleapis.com/automation_run" Platform Log event that describes the AutomationRun related events.

### [BackoffMode](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.BackoffMode)

The pattern of how wait time is increased.

### [BuildArtifact](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.BuildArtifact)

Description of an a image to use during Skaffold rendering.

### [Canary](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Canary)

Canary represents the canary deployment strategy.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CanaryDeployment](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CanaryDeployment)

CanaryDeployment represents the canary deployment configuration

### [CancelAutomationRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelAutomationRunRequest)

The request object used by `CancelAutomationRun`.

### [CancelAutomationRunResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelAutomationRunResponse)

The response object from `CancelAutomationRun`.

### [CancelRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelRolloutRequest)

The request object used by `CancelRollout`.

### [CancelRolloutResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CancelRolloutResponse)

The response object from `CancelRollout`.

### [ChildRolloutJobs](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ChildRolloutJobs)

ChildRollouts job composition

### [CloudRunConfig](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CloudRunConfig)

CloudRunConfig contains the Cloud Run runtime configuration.

### [CloudRunLocation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CloudRunLocation)

Information specifying where to deploy a Cloud Run Service.

### [CloudRunMetadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CloudRunMetadata)

CloudRunMetadata contains information from a Cloud Run deployment.

### [CloudRunRenderMetadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CloudRunRenderMetadata)

CloudRunRenderMetadata contains Cloud Run information associated with a `Release` render.

### [Config](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Config)

Service-wide configuration.

### [CreateAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateAutomationRequest)

The request object for `CreateAutomation`.

### [CreateChildRolloutJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateChildRolloutJob)

A createChildRollout Job.

### [CreateChildRolloutJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateChildRolloutJobRun)

CreateChildRolloutJobRun contains information specific to a createChildRollout `JobRun`.

### [CreateCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateCustomTargetTypeRequest)

The request object for `CreateCustomTargetType`.

### [CreateDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateDeliveryPipelineRequest)

The request object for `CreateDeliveryPipeline`.

### [CreateDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateDeployPolicyRequest)

The request object for `CreateDeployPolicy`.

### [CreateReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateReleaseRequest)

The request object for `CreateRelease`,

### [CreateRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateRolloutRequest)

CreateRolloutRequest is the request object used by `CreateRollout`.

### [CreateTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CreateTargetRequest)

The request object for `CreateTarget`.

### [CustomCanaryDeployment](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomCanaryDeployment)

CustomCanaryDeployment represents the custom canary deployment configuration.

### [PhaseConfig](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomCanaryDeployment.PhaseConfig)

PhaseConfig represents the configuration for a phase in the custom canary deployment.

### [CustomMetadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomMetadata)

CustomMetadata contains information from a user-defined operation.

### [ValuesEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomMetadata.ValuesEntry)

The abstract base class for a message.

### [CustomTarget](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTarget)

Information specifying a Custom Target.

### [CustomTargetDeployMetadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetDeployMetadata)

CustomTargetDeployMetadata contains information from a Custom Target deploy operation.

### [CustomTargetSkaffoldActions](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetSkaffoldActions)

CustomTargetSkaffoldActions represents the `CustomTargetType` configuration using Skaffold custom actions.

### [CustomTargetType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType)

A `CustomTargetType` resource in the Cloud Deploy API.

A `CustomTargetType` defines a type of custom target that can be referenced in a `Target` in order to facilitate deploying to other systems besides the supported runtimes.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType.AnnotationsEntry)

The abstract base class for a message.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetType.LabelsEntry)

The abstract base class for a message.

### [CustomTargetTypeNotificationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.CustomTargetTypeNotificationEvent)

Payload proto for "clouddeploy.googleapis.com/customtargettype_notification" Platform Log event that describes the failure to send a custom target type status change Pub/Sub notification.

### [DefaultPool](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DefaultPool)

Execution using the default Cloud Build pool.

### [DeleteAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteAutomationRequest)

The request object for `DeleteAutomation`.

### [DeleteCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteCustomTargetTypeRequest)

The request object for `DeleteCustomTargetType`.

### [DeleteDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteDeliveryPipelineRequest)

The request object for `DeleteDeliveryPipeline`.

### [DeleteDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteDeployPolicyRequest)

The request object for `DeleteDeployPolicy`.

### [DeleteTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeleteTargetRequest)

The request object for `DeleteTarget`.

### [DeliveryPipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline)

A `DeliveryPipeline` resource in the Cloud Deploy API.

A `DeliveryPipeline` defines a pipeline through which a Skaffold configuration can progress.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline.AnnotationsEntry)

The abstract base class for a message.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipeline.LabelsEntry)

The abstract base class for a message.

### [DeliveryPipelineAttribute](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipelineAttribute)

Contains criteria for selecting DeliveryPipelines.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipelineAttribute.LabelsEntry)

The abstract base class for a message.

### [DeliveryPipelineNotificationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeliveryPipelineNotificationEvent)

Payload proto for "clouddeploy.googleapis.com/deliverypipeline_notification" Platform Log event that describes the failure to send delivery pipeline status change Pub/Sub notification.

### [DeployArtifact](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployArtifact)

The artifacts produced by a deploy operation.

### [DeployJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployJob)

A deploy Job.

### [DeployJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployJobRun)

DeployJobRun contains information specific to a deploy `JobRun`.

### [FailureCause](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployJobRun.FailureCause)

Well-known deploy failures.

### [DeployJobRunMetadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployJobRunMetadata)

DeployJobRunMetadata surfaces information associated with a `DeployJobRun` to the user.

### [DeployParameters](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployParameters)

DeployParameters contains deploy parameters information.

### [MatchTargetLabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployParameters.MatchTargetLabelsEntry)

The abstract base class for a message.

### [ValuesEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployParameters.ValuesEntry)

The abstract base class for a message.

### [DeployPolicy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy)

A `DeployPolicy` resource in the Cloud Deploy API.

A `DeployPolicy` inhibits manual or automation-driven actions within a Delivery Pipeline or Target.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy.AnnotationsEntry)

The abstract base class for a message.

### [Invoker](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy.Invoker)

What invoked the action. Filters enforcing the policy depending on what invoked the action.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicy.LabelsEntry)

The abstract base class for a message.

### [DeployPolicyEvaluationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicyEvaluationEvent)

Payload proto for "clouddeploy.googleapis.com/deploypolicy_evaluation" Platform Log event that describes the deploy policy evaluation event.

### [PolicyVerdict](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicyEvaluationEvent.PolicyVerdict)

The policy verdict of the request.

### [PolicyVerdictOverride](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicyEvaluationEvent.PolicyVerdictOverride)

Things that could have overridden the policy verdict. When overrides are used, the request will be allowed even if it is DENIED_BY_POLICY.

### [DeployPolicyNotificationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicyNotificationEvent)

Payload proto for "clouddeploy.googleapis.com/deploypolicy_notification". Platform Log event that describes the failure to send a pub/sub notification when there is a DeployPolicy status change.

### [DeployPolicyResourceSelector](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeployPolicyResourceSelector)

Contains information on the resources to select for a deploy policy. Attributes provided must all match the resource in order for policy restrictions to apply. For example, if delivery pipelines attributes given are an id "prod" and labels "foo: bar", a delivery pipeline resource must match both that id and have that label in order to be subject to the policy.

### [DeploymentJobs](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.DeploymentJobs)

Deployment job composition.

### [ExecutionConfig](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ExecutionConfig)

Configuration of the environment to use when calling Skaffold.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExecutionEnvironmentUsage](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ExecutionConfig.ExecutionEnvironmentUsage)

Possible usages of this configuration.

### [GetAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetAutomationRequest)

The request object for `GetAutomation`

### [GetAutomationRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetAutomationRunRequest)

The request object for `GetAutomationRun`

### [GetConfigRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetConfigRequest)

Request to get a configuration.

### [GetCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetCustomTargetTypeRequest)

The request object for `GetCustomTargetType`.

### [GetDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetDeliveryPipelineRequest)

The request object for `GetDeliveryPipeline`

### [GetDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetDeployPolicyRequest)

The request object for `GetDeployPolicy`

### [GetJobRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetJobRunRequest)

GetJobRunRequest is the request object used by `GetJobRun`.

### [GetReleaseRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetReleaseRequest)

The request object for `GetRelease`.

### [GetRolloutRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetRolloutRequest)

GetRolloutRequest is the request object used by `GetRollout`.

### [GetTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GetTargetRequest)

The request object for `GetTarget`.

### [GkeCluster](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.GkeCluster)

Information specifying a GKE Cluster.

### [IgnoreJobRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.IgnoreJobRequest)

The request object used by `IgnoreJob`.

### [IgnoreJobResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.IgnoreJobResponse)

The response object from `IgnoreJob`.

### [Job](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Job)

Job represents an operation for a `Rollout`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Job.State)

Valid states of a Job.

### [JobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.JobRun)

A `JobRun` resource in the Cloud Deploy API.

A `JobRun` contains information of a single `Rollout` job evaluation.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.JobRun.State)

Valid states of a `JobRun`.

### [JobRunNotificationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.JobRunNotificationEvent)

Payload proto for "clouddeploy.googleapis.com/jobrun_notification" Platform Log event that describes the failure to send JobRun resource update Pub/Sub notification.

### [KubernetesConfig](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.KubernetesConfig)

KubernetesConfig contains the Kubernetes runtime configuration.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GatewayServiceMesh](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh)

Information about the Kubernetes Gateway API service mesh configuration.

### [RouteDestinations](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.KubernetesConfig.GatewayServiceMesh.RouteDestinations)

Information about route destinations for the Gateway API service mesh.

### [ServiceNetworking](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.KubernetesConfig.ServiceNetworking)

Information about the Kubernetes Service networking configuration.

### [ListAutomationRunsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsRequest)

The request object for `ListAutomationRuns`.

### [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse)

The response object from `ListAutomationRuns`.

### [ListAutomationsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsRequest)

The request object for `ListAutomations`.

### [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse)

The response object from `ListAutomations`.

### [ListCustomTargetTypesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesRequest)

The request object for `ListCustomTargetTypes`.

### [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse)

The response object from `ListCustomTargetTypes.`

### [ListDeliveryPipelinesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesRequest)

The request object for `ListDeliveryPipelines`.

### [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse)

The response object from `ListDeliveryPipelines`.

### [ListDeployPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesRequest)

The request object for `ListDeployPolicies`.

### [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse)

The response object from `ListDeployPolicies`.

### [ListJobRunsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsRequest)

ListJobRunsRequest is the request object used by `ListJobRuns`.

### [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse)

ListJobRunsResponse is the response object returned by `ListJobRuns`.

### [ListReleasesRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesRequest)

The request object for `ListReleases`.

### [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse)

The response object from `ListReleases`.

### [ListRolloutsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsRequest)

ListRolloutsRequest is the request object used by `ListRollouts`.

### [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse)

ListRolloutsResponse is the response object returned by `ListRollouts`.

### [ListTargetsRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsRequest)

The request object for `ListTargets`.

### [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse)

The response object from `ListTargets`.

### [Metadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Metadata)

Metadata includes information associated with a `Rollout`.

### [MultiTarget](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.MultiTarget)

Information specifying a multiTarget.

### [OneTimeWindow](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.OneTimeWindow)

One-time window within which actions are restricted. For example, blocking actions over New Year's Eve from December 31st at 5pm to January 1st at 9am.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [Phase](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Phase)

Phase represents a collection of jobs that are logically grouped together for a `Rollout`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Phase.State)

Valid states of a Phase.

### [PipelineCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PipelineCondition)

PipelineCondition contains all conditions relevant to a Delivery Pipeline.

### [PipelineReadyCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PipelineReadyCondition)

PipelineReadyCondition contains information around the status of the Pipeline.

### [PolicyRule](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PolicyRule)

Deploy Policy rule.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PolicyViolation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PolicyViolation)

Returned from an action if one or more policies were violated, and therefore the action was prevented. Contains information about what policies were violated and why.

### [PolicyViolationDetails](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PolicyViolationDetails)

Policy violation details.

### [Postdeploy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Postdeploy)

Postdeploy contains the postdeploy job configuration information.

### [PostdeployJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PostdeployJob)

A postdeploy Job.

### [PostdeployJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PostdeployJobRun)

PostdeployJobRun contains information specific to a postdeploy `JobRun`.

### [FailureCause](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PostdeployJobRun.FailureCause)

Well-known postdeploy failures.

### [Predeploy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Predeploy)

Predeploy contains the predeploy job configuration information.

### [PredeployJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PredeployJob)

A predeploy Job.

### [PredeployJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PredeployJobRun)

PredeployJobRun contains information specific to a predeploy `JobRun`.

### [FailureCause](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PredeployJobRun.FailureCause)

Well-known predeploy failures.

### [PrivatePool](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PrivatePool)

Execution using a private Cloud Build pool.

### [PromoteReleaseOperation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PromoteReleaseOperation)

Contains the information of an automated promote-release operation.

### [PromoteReleaseRule](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.PromoteReleaseRule)

The `PromoteRelease` rule will automatically promote a release from the current target to a specified target.

### [Release](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release)

A `Release` resource in the Cloud Deploy API.

A `Release` defines a specific Skaffold configuration instance that can be deployed.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.AnnotationsEntry)

The abstract base class for a message.

### [DeployParametersEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.DeployParametersEntry)

The abstract base class for a message.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.LabelsEntry)

The abstract base class for a message.

### [ReleaseCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.ReleaseCondition)

ReleaseCondition contains all conditions relevant to a Release.

### [ReleaseReadyCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.ReleaseReadyCondition)

ReleaseReadyCondition contains information around the status of the Release. If a release is not ready, you cannot create a rollout with the release.

### [RenderState](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.RenderState)

Valid states of the render operation.

### [SkaffoldSupportedCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.SkaffoldSupportedCondition)

SkaffoldSupportedCondition contains information about when support for the release's version of Skaffold ends.

### [TargetArtifactsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.TargetArtifactsEntry)

The abstract base class for a message.

### [TargetRender](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.TargetRender)

Details of rendering for a single target.

### [FailureCause](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.TargetRender.FailureCause)

Well-known rendering failures.

### [TargetRenderState](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.TargetRender.TargetRenderState)

Valid states of the render operation.

### [TargetRendersEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Release.TargetRendersEntry)

The abstract base class for a message.

### [ReleaseNotificationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ReleaseNotificationEvent)

Payload proto for "clouddeploy.googleapis.com/release_notification" Platform Log event that describes the failure to send release status change Pub/Sub notification.

### [ReleaseRenderEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ReleaseRenderEvent)

Payload proto for "clouddeploy.googleapis.com/release_render" Platform Log event that describes the render status change.

### [RenderMetadata](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RenderMetadata)

RenderMetadata includes information associated with a `Release` render.

### [RepairPhase](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RepairPhase)

RepairPhase tracks the repair attempts that have been made for each `RepairPhaseConfig` specified in the `Automation` resource.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RepairPhaseConfig](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RepairPhaseConfig)

Configuration of the repair phase.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RepairRolloutOperation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RepairRolloutOperation)

Contains the information for an automated `repair rollout` operation.

### [RepairRolloutRule](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RepairRolloutRule)

The `RepairRolloutRule` automation rule will automatically repair a failed `Rollout`.

### [RepairState](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RepairState)

Valid state of a repair attempt.

### [Retry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Retry)

Retries the failed job.

### [RetryAttempt](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RetryAttempt)

RetryAttempt represents an action of retrying the failed Cloud Deploy job.

### [RetryJobRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RetryJobRequest)

RetryJobRequest is the request object used by `RetryJob`.

### [RetryJobResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RetryJobResponse)

The response object from 'RetryJob'.

### [RetryPhase](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RetryPhase)

RetryPhase contains the retry attempts and the metadata for initiating a new attempt.

### [Rollback](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollback)

Rolls back a `Rollout`.

### [RollbackAttempt](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RollbackAttempt)

RollbackAttempt represents an action of rolling back a Cloud Deploy 'Target'.

### [RollbackTargetConfig](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RollbackTargetConfig)

Configs for the Rollback rollout.

### [RollbackTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RollbackTargetRequest)

The request object for `RollbackTarget`.

### [RollbackTargetResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RollbackTargetResponse)

The response object from `RollbackTarget`.

### [Rollout](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout)

A `Rollout` resource in the Cloud Deploy API.

A `Rollout` contains information around a specific deployment to a `Target`.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout.AnnotationsEntry)

The abstract base class for a message.

### [ApprovalState](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout.ApprovalState)

Valid approval states of a `Rollout`.

### [FailureCause](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout.FailureCause)

Well-known rollout failures.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Rollout.State)

Valid states of a `Rollout`.

### [RolloutNotificationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RolloutNotificationEvent)

Payload proto for "clouddeploy.googleapis.com/rollout_notification" Platform Log event that describes the failure to send rollout status change Pub/Sub notification.

### [RolloutRestriction](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RolloutRestriction)

Rollout restrictions.

### [RolloutActions](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RolloutRestriction.RolloutActions)

Rollout actions to be restricted as part of the policy.

### [RolloutUpdateEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RolloutUpdateEvent)

Payload proto for "clouddeploy.googleapis.com/rollout_update" Platform Log event that describes the rollout update event.

### [RolloutUpdateType](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RolloutUpdateEvent.RolloutUpdateType)

RolloutUpdateType indicates the type of the rollout update.

### [RuntimeConfig](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.RuntimeConfig)

RuntimeConfig contains the runtime specific configurations for a deployment strategy.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SerialPipeline](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SerialPipeline)

SerialPipeline defines a sequential set of stages for a `DeliveryPipeline`.

### [SkaffoldModules](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules)

Skaffold Config modules and their remote source.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SkaffoldGCBRepoSource](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCBRepoSource)

Cloud Build V2 Repository containing Skaffold Configs.

### [SkaffoldGCSSource](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGCSSource)

Cloud Storage bucket containing Skaffold Config modules.

### [SkaffoldGitSource](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldModules.SkaffoldGitSource)

Git repository containing Skaffold Config modules.

### [SkaffoldSupportState](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldSupportState)

The support state of a specific Skaffold version.

### [SkaffoldVersion](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.SkaffoldVersion)

Details of a supported Skaffold version.

### [Stage](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Stage)

Stage specifies a location to which to deploy.

### [Standard](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Standard)

Standard represents the standard deployment strategy.

### [Strategy](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Strategy)

Strategy contains deployment strategy information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Target](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target)

A `Target` resource in the Cloud Deploy API.

A `Target` defines a location to which a Skaffold configuration can be deployed.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target.AnnotationsEntry)

The abstract base class for a message.

### [AssociatedEntitiesEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target.AssociatedEntitiesEntry)

The abstract base class for a message.

### [DeployParametersEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target.DeployParametersEntry)

The abstract base class for a message.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Target.LabelsEntry)

The abstract base class for a message.

### [TargetArtifact](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TargetArtifact)

The artifacts produced by a target render operation.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PhaseArtifact](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TargetArtifact.PhaseArtifact)

Contains the paths to the artifacts, relative to the URI, for a phase.

### [PhaseArtifactsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TargetArtifact.PhaseArtifactsEntry)

The abstract base class for a message.

### [TargetAttribute](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TargetAttribute)

Contains criteria for selecting Targets. This could be used to select targets for a Deploy Policy or for an Automation.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TargetAttribute.LabelsEntry)

The abstract base class for a message.

### [TargetNotificationEvent](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TargetNotificationEvent)

Payload proto for "clouddeploy.googleapis.com/target_notification" Platform Log event that describes the failure to send target status change Pub/Sub notification.

### [TargetsPresentCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TargetsPresentCondition)

`TargetsPresentCondition` contains information on any Targets referenced in the Delivery Pipeline that do not actually exist.

### [TargetsTypeCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TargetsTypeCondition)

TargetsTypeCondition contains information on whether the Targets defined in the Delivery Pipeline are of the same type.

### [TerminateJobRunRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TerminateJobRunRequest)

The request object used by `TerminateJobRun`.

### [TerminateJobRunResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TerminateJobRunResponse)

The response object from `TerminateJobRun`.

### [TimeWindows](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TimeWindows)

Time windows within which actions are restricted. See the `documentation <https://cloud.google.com/deploy/docs/deploy-policy#dates_times>`__ for more information on how to configure dates/times.

### [TimedPromoteReleaseCondition](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TimedPromoteReleaseCondition)

`TimedPromoteReleaseCondition` contains conditions specific to an Automation with a Timed Promote Release rule defined.

### [Targets](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TimedPromoteReleaseCondition.Targets)

The targets involved in a single timed promotion.

### [TimedPromoteReleaseOperation](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TimedPromoteReleaseOperation)

Contains the information of an automated timed promote-release operation.

### [TimedPromoteReleaseRule](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.TimedPromoteReleaseRule)

The `TimedPromoteReleaseRule` will automatically promote a release from the current target(s) to the specified target(s) on a configured schedule.

### [Type](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.Type)

Type indicates the type of the log entry and can be used as a filter.

### [UpdateAutomationRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateAutomationRequest)

The request object for `UpdateAutomation`.

### [UpdateCustomTargetTypeRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateCustomTargetTypeRequest)

The request object for `UpdateCustomTargetType`.

### [UpdateDeliveryPipelineRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateDeliveryPipelineRequest)

The request object for `UpdateDeliveryPipeline`.

### [UpdateDeployPolicyRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateDeployPolicyRequest)

The request object for `UpdateDeployPolicy`.

### [UpdateTargetRequest](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.UpdateTargetRequest)

The request object for `UpdateTarget`.

### [VerifyJob](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.VerifyJob)

A verify Job.

### [VerifyJobRun](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.VerifyJobRun)

VerifyJobRun contains information specific to a verify `JobRun`.

### [FailureCause](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.VerifyJobRun.FailureCause)

Well-known verify failures.

### [WeeklyWindow](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.WeeklyWindow)

Weekly windows. For example, blocking actions every Saturday and Sunday. Another example would be blocking actions every weekday from 5pm to midnight.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers)

API documentation for `deploy_v1.services.cloud_deploy.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
