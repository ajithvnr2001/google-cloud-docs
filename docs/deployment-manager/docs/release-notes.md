---
url: https://docs.cloud.google.com/deployment-manager/docs/release-notes/
title: Deployment Manager release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:27.033501+00:00
---

# Deployment Manager release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/release-notes/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Resources ](https://docs.cloud.google.com/deployment-manager/docs/resources)



Send feedback 

#  Deployment Manager release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for Google Cloud Deployment Manager.

**Current Version: v2**

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/deploymentmanager-release-notes.xml) directly. 

## April 15, 2020

Feature

Added support for [Cloud Scheduler](https://docs.cloud.google.com/scheduler) through `gcp-types/cloudscheduler-v1:projects.locations.jobs`.

Fixed

Deployment Manager now correctly deletes [Compute Engine](https://docs.cloud.google.com/compute/docs) forwarding rules of type `compute.v1.forwardingRule`, `compute.beta.forwardingRule`, `gcp-types/compute-v1:forwardingRules` and `gcp-types/compute-beta:forwardingRules` when the resource name does not match the forwarding rule name.

Change

Updates on [Cloud Functions](https://docs.cloud.google.com/functions) resources using `gcp-types/cloudfunctions-v1` now retry on 429 errors.

Change

Performance improvements when handling large Swagger / OpenAPI specs when [adding an API as a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider).

Fixed

Deployment Manager now acquires existing GKE cluster resources of type `gcp-types/container-v1:projects.locations.clusters`.

Change

You can now apply granular [IAM Permissions](https://docs.cloud.google.com/iam/docs/permissions-reference) to the [Google APIs service account used by Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/access-control#access_control_for), as we've removed the requirement for `roles/editor` being assigned to the service account.

Change

GKE clusters and node pools will wait for maintenance to complete before attempting to apply any updates. Affected collections:

  * `gcp-types/container-v1:projects.zones.clusters`
  * `gcp-types/container-v1:projects.locations.clusters`
  * `gcp-types/container-v1:projects.zones.clusters.nodePools`
  * `gcp-types/container-v1:projects.locations.clusters.nodePools`
  * `gcp-types/container-v1beta1:projects.zones.clusters`
  * `gcp-types/container-v1beta1:projects.locations.clusters`
  * `gcp-types/container-v1beta1:projects.zones.clusters.nodePools`
  * `gcp-types/container-v1beta1:projects.locations.clusters.nodePools`



Fixed

Deployment Manager now correctly acquires [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs) resources of type `gcp-types/accesscontextmanager-v1:accessPolicies.accessLevels` and `gcp-types/accesscontextmanager-v1beta:accessPolicies.accessLevels` if the resources already exist.

Change

Added support for updating [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub) subscriptions using `gcp-types/pubsub-v1:projects.subscriptions`.

Change

Added support for updating the following properties on `gcp-types/container-v1:projects.zones.clusters` and `gcp-types/container-v1:projects.locations.clusters`: 

  * binaryAuthorization
  * databaseEncryption
  * masterAuthorizedNetworksConfig
  * autoscaling
  * resourceUsageExportConfig
  * verticalPodAutoscaling



Additionally, for `gcp-types/container-v1beta1:projects.zones.clusters` and `gcp-types/container-v1beta1:projects.locations.clusters` the following fields can also be updated:

  * podSecurityPolicyConfig
  * privateClusterConfig
  * shieldedNodes
  * workloadIdentityConfig



Fixed

Deployment Manager now correctly updates autoscaling properties for resources of type `gcp-types/container-v1:projects.locations.clusters.nodePools` and `gcp-types/container-v1beta1:projects.locations.clusters.nodePools`.

## March 30, 2020

Change

If your Python templates use features that are only for Python 2.x, your templates will now continue to work until **June 2020**.

Learn about [migrating your templates to Python 3](https://docs.cloud.google.com/deployment-manager/docs/migrate-to-python3).

## December 05, 2019

Change

Deployment Manager now supports templates written in Python 3.

The Python community announced that it will [sunset Python 2](https://www.python.org/doc/sunset-python-2/) on January 1, 2020, and is encouraging all developers to upgrade to Python 3 as soon as they can.

We recommend that you make sure that your Python templates are [compatible with Python 3](https://docs.cloud.google.com/deployment-manager/docs/migrate-to-python3) as soon as possible.

## November 26, 2019

Change

When you're creating your deployments, we recommend using the production-ready templates from the [Cloud Foundation Toolkit](https://docs.cloud.google.com/foundation-toolkit). The templates use Google Cloud's best practices for managing resources.

[See the list of sample templates](https://docs.cloud.google.com/deployment-manager/docs/reference/cloud-foundation-toolkit).

## October 02, 2019

Feature

You can now use the `gcp-types/compute-v1:externalVpnGateways` type to create [Compute Engine v1 ExternalVpnGateway resources](https://docs.cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways).

Feature

You can now use the `gcp-types/compute-v1:vpnGateways` type to create [Compute Engine v1 VpnGateway resources](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways).

## September 30, 2019

Change

The [walkthrough of Deployment Manager's best practices](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide) has been updated, with an optional interactive version that runs in Cloud Shell.

Try the interactive version here:

[Open in Cloud Shell](https://console.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fdeploymentmanager-samples&cloudshell_tutorial=walkthroughtutorial.md)

## July 01, 2019

Feature

You can now use the `gcp-types/cloudresourcemanager-v1` type provider to create IAM mappings for projects and organizations.

For a list of supported type providers, see [Supported GCP type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

## June 03, 2019

Change

In type providers, the input mappings for header fields are now applied to getting long-running operations.

For information on creating custom type providers, read the [guidelines for creating a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api).

Feature

You can now use Deployment Manager to update labels for Cloud Pub/Sub resources.

## May 28, 2019

Change

If you are using the Deployment Manager API, read the [guidelines for managing long-running operations](https://docs.cloud.google.com/deployment-manager/docs/reference/managing-long-running-operations).

## February 27, 2019

Feature

Added support for Redis v1 API using the type-provider `gcp-types/redis-v1`.

Feature

Deployment Manager templates can be used in [Private Catalog](https://docs.cloud.google.com/private-catalog).

## November 21, 2018

Feature

Added support for Cloud DNS v1 RecordSets using the type-provider `gcp-types/dns-v1:resourceRecordSets`.

Feature

Added a new template environment variable, `username`, which you can use in Python templates using `context.env["username"]`, and in Jinja templates using `env["username"]`.

For information on using environment variables in templates, see [Using environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables).

Feature

Added support for Access Context Manager v1beta using the type provider `gcp-types/accesscontextmanager-v1beta`.

For a list of supported type providers, see [Supported GCP type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

## September 12, 2018

Feature

Expanded support for creating and acquiring project folders using the type-provider `gcp-types/cloudresourcemanager-v2:folders`.

For a list of supported type providers, see [Supported GCP type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

## August 07, 2018

Feature

Added glob import support to `gcloud`. You can import templates using wildcards in template paths.

For the syntax to enable glob imports, see the [SDK release notes](https://docs.cloud.google.com/sdk/docs/release-notes).

## July 03, 2018

Feature

When you are creating or updating deployments, you can select a `CREATE` policy for new resources. This ensures that if a resource you are trying to create already exists in the project, the deployment fails.

For information on policies for creating resources, see [Setting policies for creating resources](https://docs.cloud.google.com/deployment-manager/docs/deployments#create-policy).

## April 24, 2018

Deprecated

The `appengine.v1beta4` and `appengine.v1beta5` resource types are no longer supported.

Feature

Updated the `gcloud` tool so that you can create deployments directly with [composite types](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types#compositetypepropertiescommandline). Also added new `--template` flag to support [creating deployments with templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties#templatepropertiescommandline).

## July 24, 2017

Feature

Added support for [labels on deployments](https://docs.cloud.google.com/deployment-manager/docs/deployments/add-labels-deployments).

## April 20, 2017

Feature

Added new `returnValues` query parameter for the [`variables().list`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list) method to return values for variables that the caller has `runtimeconfig.variables.get` permission on.

## April 12, 2017

Feature

Added new [`project_number` environment variable](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates#environment_variables).

## March 27, 2017

Feature

Added new Type Registry feature that allows users to add [composite types](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#composite_types) and add third-party APIs as [type providers](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#basetypes). This feature is in **Beta**.

## February 23, 2017

Feature

[Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator) updates: * Converted `gcloud` commands so that the command group is now under `runtime-config` * Updated `gcloud` commands to the `gcloud beta` component.

## January 27, 2017

Feature

Added support to the `gcloud` command-line tool for creating [plaintext variable values](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).

## January 11, 2017

Feature

Updated `gcloud` command-line tool syntax so that the `--properties` flag now accepts `key:value` pairs. The old syntax, `key=value`, will still work but users should transition to using the new syntax. For more information, read [Specifying template properties on the command-line](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates#specifying_template_properties_on_the_command-line).

## November 20, 2016

Feature

Added documentation on configuring Deployment Manager to [use images from another project](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-images-from-other-projects-for-vm-instances).

## November 01, 2016

Feature

[Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator) updates:

  * Added support for [plaintext variable values](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables) when creating a variable in the API. This is not yet supported with the `gcloud` command-line tool.
  * Added optional [`requestId`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/create) field for `create()` requests to ensure that requests are unique.



## October 06, 2016

Feature

Added support for specifying IAM policies in your configurations. Read the [documentation](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-configuration-file#setting_access_control_for_resources_in_a_deployment) for more information.

## September 28, 2016

Change

Published a [Syntax Reference](https://docs.cloud.google.com/deployment-manager/docs/configuration/syntax-reference) that describes the syntax of Deployment Manager.

## August 26, 2016

Feature

Added support for predefined Deployment Manager [IAM roles](https://docs.cloud.google.com/deployment-manager/docs/access-control#predefined_roles) in **Beta**.

## August 25, 2016

Feature

Updated [resource quotas](https://cloud.google.com/deployment-manager/pricing-and-quotas) for [Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator) so that it is now based on amount of data per user instead of the number of resources. The default quota is 4 MB of data per user. Also, updated quota for API requests.

Feature

Removed the 4 KB limit on variable values for Runtime Configurator.

## May 10, 2016

Feature

Added support for hosting templates externally on Google Cloud Storage or on another publicly-accessible URL. Read [Hosting Templates Externally](https://docs.cloud.google.com/deployment-manager/docs/configuration/hosting-templates-externally) for more information.

## February 29, 2016

Feature

Added support for [outputs](https://docs.cloud.google.com/deployment-manager/docs/configuration/expose-information-outputs) so you can expose key properties of your configuration for others to use.

## November 13, 2015

Feature

Added support for [schemas](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-schemas) that allow you to define rules for using templates. Read [Using Schemas](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-schemas) for more information.

## November 04, 2015

Feature

Added support for new `cluster.v1.cluster` resource type.

Deprecated

Removed support for `cluster.v1beta1.cluster` resource type since Container Engine v1beta1 API is now [deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#july_24_2015).

## July 22, 2015

Feature

Added new boolean `preview` query parameter to the API; to preview deployments, use the query parameter.

Feature

Added new custom methods, `stop` and `cancelPreview`, to the API.

Deprecated

Removed `--update-policy` flag because `PATCH` is no longer supported.

Feature

Added new `fingerprint` requirements to the API, for updating, canceling, or stopping a deployment.

Feature

Replaced `deployments cancel` subcommand with new `cancel-preview` and `stop` subcommands.

Change

Updated API error codes.

Deprecated

Removed `PATCH` as possible update policy for the API.

Feature

**Launched Deployment Manager into General Availability with v2 API!**

Deployment Manager is now generally available for all users and projects. We have also:

  * Added new intermediate guide
  * Updated the navigation structure



For more information, see the new [Step-by-step guide](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide).

Feature

Refreshed API manifest structure so that templates are now explicitly shown in the new `imports` section of the manifest file.

See [Updating a Deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments) and [Viewing a Manifest](https://docs.cloud.google.com/deployment-manager/docs/deployments/viewing-manifest) for more information.

Deprecated

Removed `intent` and `state` properties from Deployment resources.

## July 13, 2015

Feature

Updated quota limits so that **delete** and **read requests** are now unlimited. See [Quotas](https://cloud.google.com/deployment-manager/pricing-and-quotas) for more information.

## June 18, 2015

Change

Changed `creationTimestamp` field to `insertTime`.

Feature

Added new field called `updateTime`.

## April 30, 2015

Feature

Launched Deployment Manager into **Beta**! Also, launched new [v2beta2](https://docs.cloud.google.com/deployment-manager/docs/reference/latest) API that includes a number of new and improved features, including server-side expansion, manifest layouts, update capabilities, and more. See the [migration guide](https://docs.cloud.google.com/deployment-manager/docs/reference/latest/migration-guide) for more information.

## February 20, 2015

Deprecated

Disabled support for external references due to a known bug.

## February 06, 2015

Feature

Added support for [external references](https://docs.cloud.google.com/deployment-manager/docs/configuration-files#external_references).

## January 21, 2015

Feature

  * Added new Google Container Engine cluster type, `container.v1beta1.cluster` that allows you to declare and deploy new Google Container Engine Clusters.



Feature

2015-01-21

FEATURE * Added new tutorial for [creating a HTTP load-balanced deployment](https://docs.cloud.google.com/deployment-manager/docs/create-advanced-http-load-balanced-deployment).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
