---
url: https://docs.cloud.google.com/feeds/deploymentmanager-release-notes.xml
title: Cloud Deployment Manager - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:35.021975+00:00
---

# Cloud Deployment Manager - Release notes

> Source: https://docs.cloud.google.com/feeds/deploymentmanager-release-notes.xml

tag:google.com,2016:deploymentmanager-release-notesCloud Deployment Manager - Release notesGoogle Cloud Platform2020-04-15T00:00:00-07:00April 15, 2020tag:google.com,2016:deploymentmanager-release-notes#April_15_20202020-04-15T00:00:00-07:00Feature 

Added support for [Cloud Scheduler](https://docs.cloud.google.com/scheduler) through `gcp-types/cloudscheduler-v1:projects.locations.jobs`.

### Fixed

Deployment Manager now correctly deletes [Compute Engine](https://docs.cloud.google.com/compute/docs) forwarding rules of type `compute.v1.forwardingRule`, `compute.beta.forwardingRule`, `gcp-types/compute-v1:forwardingRules` and `gcp-types/compute-beta:forwardingRules` when the resource name does not match the forwarding rule name.

### Change

Updates on [Cloud Functions](https://docs.cloud.google.com/functions) resources using `gcp-types/cloudfunctions-v1` now retry on 429 errors.

### Change

Performance improvements when handling large Swagger / OpenAPI specs when [adding an API as a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider).

### Fixed

Deployment Manager now acquires existing GKE cluster resources of type `gcp-types/container-v1:projects.locations.clusters`.

### Change

You can now apply granular [IAM Permissions](https://docs.cloud.google.com/iam/docs/permissions-reference) to the [Google APIs service account used by Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs/access-control#access_control_for), as we've removed the requirement for `roles/editor` being assigned to the service account.

### Change

GKE clusters and node pools will wait for maintenance to complete before attempting to apply any updates. Affected collections:

  * `gcp-types/container-v1:projects.zones.clusters`
  * `gcp-types/container-v1:projects.locations.clusters`
  * `gcp-types/container-v1:projects.zones.clusters.nodePools`
  * `gcp-types/container-v1:projects.locations.clusters.nodePools`
  * `gcp-types/container-v1beta1:projects.zones.clusters`
  * `gcp-types/container-v1beta1:projects.locations.clusters`
  * `gcp-types/container-v1beta1:projects.zones.clusters.nodePools`
  * `gcp-types/container-v1beta1:projects.locations.clusters.nodePools`



### Fixed

Deployment Manager now correctly acquires [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs) resources of type `gcp-types/accesscontextmanager-v1:accessPolicies.accessLevels` and `gcp-types/accesscontextmanager-v1beta:accessPolicies.accessLevels` if the resources already exist.

### Change

Added support for updating [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub) subscriptions using `gcp-types/pubsub-v1:projects.subscriptions`.

### Change

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



### Fixed

Deployment Manager now correctly updates autoscaling properties for resources of type `gcp-types/container-v1:projects.locations.clusters.nodePools` and `gcp-types/container-v1beta1:projects.locations.clusters.nodePools`.

]]> March 30, 2020tag:google.com,2016:deploymentmanager-release-notes#March_30_20202020-03-30T00:00:00-07:00Change 

If your Python templates use features that are only for Python 2.x, your templates will now continue to work until **June 2020**.

Learn about [migrating your templates to Python 3](https://docs.cloud.google.com/deployment-manager/docs/migrate-to-python3).

]]> December 05, 2019tag:google.com,2016:deploymentmanager-release-notes#December_05_20192019-12-05T00:00:00-08:00Change 

Deployment Manager now supports templates written in Python 3.

The Python community announced that it will [sunset Python 2](https://www.python.org/doc/sunset-python-2/) on January 1, 2020, and is encouraging all developers to upgrade to Python 3 as soon as they can.

We recommend that you make sure that your Python templates are [compatible with Python 3](https://docs.cloud.google.com/deployment-manager/docs/migrate-to-python3) as soon as possible.

]]> November 26, 2019tag:google.com,2016:deploymentmanager-release-notes#November_26_20192019-11-26T00:00:00-08:00Change 

When you're creating your deployments, we recommend using the production-ready templates from the [Cloud Foundation Toolkit](https://docs.cloud.google.com/foundation-toolkit/). The templates use Google Cloud's best practices for managing resources.

[See the list of sample templates](https://docs.cloud.google.com/deployment-manager/docs/reference/cloud-foundation-toolkit).

]]> October 02, 2019tag:google.com,2016:deploymentmanager-release-notes#October_02_20192019-10-02T00:00:00-07:00Feature 

You can now use the `gcp-types/compute-v1:externalVpnGateways` type to create [Compute Engine v1 ExternalVpnGateway resources](https://docs.cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways).

### Feature

You can now use the `gcp-types/compute-v1:vpnGateways` type to create [Compute Engine v1 VpnGateway resources](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways).

]]> September 30, 2019tag:google.com,2016:deploymentmanager-release-notes#September_30_20192019-09-30T00:00:00-07:00Change 

The [walkthrough of Deployment Manager's best practices](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/) has been updated, with an optional interactive version that runs in Cloud Shell.

Try the interactive version here:

[Open in Cloud Shell](https://console.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fdeploymentmanager-samples&cloudshell_tutorial=walkthroughtutorial.md)

]]> July 01, 2019tag:google.com,2016:deploymentmanager-release-notes#July_01_20192019-07-01T00:00:00-07:00Feature 

You can now use the `gcp-types/cloudresourcemanager-v1` type provider to create IAM mappings for projects and organizations.

For a list of supported type providers, see [Supported GCP type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

]]> June 03, 2019tag:google.com,2016:deploymentmanager-release-notes#June_03_20192019-06-03T00:00:00-07:00Change 

In type providers, the input mappings for header fields are now applied to getting long-running operations.

For information on creating custom type providers, read the [guidelines for creating a type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/process-adding-api).

### Feature

You can now use Deployment Manager to update labels for Cloud Pub/Sub resources.

]]> May 28, 2019tag:google.com,2016:deploymentmanager-release-notes#May_28_20192019-05-28T00:00:00-07:00Change 

If you are using the Deployment Manager API, read the [guidelines for managing long-running operations](https://docs.cloud.google.com/deployment-manager/docs/reference/managing-long-running-operations).

]]> February 27, 2019tag:google.com,2016:deploymentmanager-release-notes#February_27_20192019-02-27T00:00:00-08:00Feature 

Added support for Redis v1 API using the type-provider `gcp-types/redis-v1`.

### Feature

Deployment Manager templates can be used in [Private Catalog](https://docs.cloud.google.com/private-catalog).

]]> November 21, 2018tag:google.com,2016:deploymentmanager-release-notes#November_21_20182018-11-21T00:00:00-08:00Feature 

Added support for Cloud DNS v1 RecordSets using the type-provider `gcp-types/dns-v1:resourceRecordSets`.

### Feature

Added a new template environment variable, `username`, which you can use in Python templates using `context.env["username"]`, and in Jinja templates using `env["username"]`.

For information on using environment variables in templates, see [Using environment variables](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/use-environment-variables).

### Feature

Added support for Access Context Manager v1beta using the type provider `gcp-types/accesscontextmanager-v1beta`.

For a list of supported type providers, see [Supported GCP type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

]]> September 12, 2018tag:google.com,2016:deploymentmanager-release-notes#September_12_20182018-09-12T00:00:00-07:00Feature 

Expanded support for creating and acquiring project folders using the type-provider `gcp-types/cloudresourcemanager-v2:folders`.

For a list of supported type providers, see [Supported GCP type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).

]]> August 07, 2018tag:google.com,2016:deploymentmanager-release-notes#August_07_20182018-08-07T00:00:00-07:00Feature 

Added glob import support to `gcloud`. You can import templates using wildcards in template paths.

For the syntax to enable glob imports, see the [SDK release notes](https://docs.cloud.google.com/sdk/docs/release-notes).

]]> July 03, 2018tag:google.com,2016:deploymentmanager-release-notes#July_03_20182018-07-03T00:00:00-07:00Feature 

When you are creating or updating deployments, you can select a `CREATE` policy for new resources. This ensures that if a resource you are trying to create already exists in the project, the deployment fails.

For information on policies for creating resources, see [Setting policies for creating resources](https://docs.cloud.google.com/deployment-manager/docs/deployments/#create-policy).

]]> April 24, 2018tag:google.com,2016:deploymentmanager-release-notes#April_24_20182018-04-24T00:00:00-07:00Deprecated 

The `appengine.v1beta4` and `appengine.v1beta5` resource types are no longer supported.

### Feature

Updated the `gcloud` tool so that you can create deployments directly with [composite types](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types#compositetypepropertiescommandline). Also added new `--template` flag to support [creating deployments with templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties#templatepropertiescommandline).

]]> July 24, 2017tag:google.com,2016:deploymentmanager-release-notes#July_24_20172017-07-24T00:00:00-07:00Feature 

Added support for [labels on deployments](https://docs.cloud.google.com/deployment-manager/docs/deployments/add-labels-deployments).

]]> April 20, 2017tag:google.com,2016:deploymentmanager-release-notes#April_20_20172017-04-20T00:00:00-07:00Feature 

Added new `returnValues` query parameter for the [`variables().list`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list) method to return values for variables that the caller has `runtimeconfig.variables.get` permission on.

]]> April 12, 2017tag:google.com,2016:deploymentmanager-release-notes#April_12_20172017-04-12T00:00:00-07:00Feature 

Added new [`project_number` environment variable](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates#environment_variables).

]]> March 27, 2017tag:google.com,2016:deploymentmanager-release-notes#March_27_20172017-03-27T00:00:00-07:00Feature 

Added new Type Registry feature that allows users to add [composite types](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#composite_types) and add third-party APIs as [type providers](https://docs.cloud.google.com/deployment-manager/docs/fundamentals#basetypes). This feature is in **Beta**.

]]> February 23, 2017tag:google.com,2016:deploymentmanager-release-notes#February_23_20172017-02-23T00:00:00-08:00Feature 

[Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator) updates: * Converted `gcloud` commands so that the command group is now under `runtime-config` * Updated `gcloud` commands to the `gcloud beta` component.

]]> January 27, 2017tag:google.com,2016:deploymentmanager-release-notes#January_27_20172017-01-27T00:00:00-08:00Feature 

Added support to the `gcloud` command-line tool for creating [plaintext variable values](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables).

]]> January 11, 2017tag:google.com,2016:deploymentmanager-release-notes#January_11_20172017-01-11T00:00:00-08:00Feature 

Updated `gcloud` command-line tool syntax so that the `--properties` flag now accepts `key:value` pairs. The old syntax, `key=value`, will still work but users should transition to using the new syntax. For more information, read [Specifying template properties on the command-line](https://docs.cloud.google.com/deployment-manager/docs/configuration/adding-templates#specifying_template_properties_on_the_command-line).

]]> November 20, 2016tag:google.com,2016:deploymentmanager-release-notes#November_20_20162016-11-20T00:00:00-08:00Feature 

Added documentation on configuring Deployment Manager to [use images from another project](https://docs.cloud.google.com/deployment-manager/docs/configuration/using-images-from-other-projects-for-vm-instances).

]]> November 01, 2016tag:google.com,2016:deploymentmanager-release-notes#November_01_20162016-11-01T00:00:00-07:00Feature 

[Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator) updates:

  * Added support for [plaintext variable values](https://docs.cloud.google.com/deployment-manager/runtime-configurator/set-and-get-variables) when creating a variable in the API. This is not yet supported with the `gcloud` command-line tool.
  * Added optional [`requestId`](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/create) field for `create()` requests to ensure that requests are unique.

]]> October 06, 2016tag:google.com,2016:deploymentmanager-release-notes#October_06_20162016-10-06T00:00:00-07:00Feature 

Added support for specifying IAM policies in your configurations. Read the [documentation](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-configuration-file#setting_access_control_for_resources_in_a_deployment) for more information.

]]> September 28, 2016tag:google.com,2016:deploymentmanager-release-notes#September_28_20162016-09-28T00:00:00-07:00Change 

Published a [Syntax Reference](https://docs.cloud.google.com/deployment-manager/docs/configuration/syntax-reference) that describes the syntax of Deployment Manager.

]]> August 26, 2016tag:google.com,2016:deploymentmanager-release-notes#August_26_20162016-08-26T00:00:00-07:00Feature 

Added support for predefined Deployment Manager [IAM roles](https://docs.cloud.google.com/deployment-manager/docs/access-control#predefined_roles) in **Beta**.

]]> August 25, 2016tag:google.com,2016:deploymentmanager-release-notes#August_25_20162016-08-25T00:00:00-07:00Feature 

Updated [resource quotas](https://cloud.google.com/deployment-manager/pricing-and-quotas) for [Runtime Configurator](https://docs.cloud.google.com/deployment-manager/runtime-configurator) so that it is now based on amount of data per user instead of the number of resources. The default quota is 4 MB of data per user. Also, updated quota for API requests.

### Feature

Removed the 4 KB limit on variable values for Runtime Configurator.

]]> May 10, 2016tag:google.com,2016:deploymentmanager-release-notes#May_10_20162016-05-10T00:00:00-07:00Feature 

Added support for hosting templates externally on Google Cloud Storage or on another publicly-accessible URL. Read [Hosting Templates Externally](https://docs.cloud.google.com/deployment-manager/docs/configuration/hosting-templates-externally) for more information.

]]> February 29, 2016tag:google.com,2016:deploymentmanager-release-notes#February_29_20162016-02-29T00:00:00-08:00Feature 

Added support for [outputs](https://docs.cloud.google.com/deployment-manager/docs/configuration/expose-information-outputs) so you can expose key properties of your configuration for others to use.

]]>
