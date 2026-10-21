---
url: https://docs.cloud.google.com/application-integration/docs/release-notes/
title: Application Integration release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:29:00.763158+00:00
---

# Application Integration release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Resources ](https://docs.cloud.google.com/application-integration/docs/release-notes)



Send feedback 

#  Application Integration release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Application Integration. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/application-integration-release-notes.xml) directly. 

## October 14, 2026

Security

An Incorrect Authorization vulnerability in the `AuthConfig` validation and integration execution runtime in Application Integration versions prior to August 27, 2026. For more information, see the [GCP-2026-068](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-068) security bulletin.

## October 12, 2026

Security

Starting October 15, 2026, Application Integration enforces security fixes for IAM, run-as service accounts, and `iam.serviceAccounts.actAs` checks, requiring the correct permissions for the test feature and any new integrations. For more information, see the [GCP-2026-067](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-067) security bulletin and [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes).

## September 28, 2026

Security

A Confused Deputy vulnerability was discovered in the Email Task component in Application Integration versions prior to June 30, 2026. For more information, see the [GCP-2026-066](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-066) security bulletin.

Security

A Deserialization of Untrusted Data vulnerability was discovered in the JavaScript Task in Application Integration versions prior to June 28, 2026. For more information, see the [GCP-2026-065](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-065) security bulletin.

Security

An Incorrect Authorization vulnerability was discovered in the task configuration in Application Integration versions prior to June 17, 2026. For more information, see the [GCP-2026-064](https://docs.cloud.google.com/application-integration/docs/security-bulletins#gcp-2026-064) security bulletin.

## August 28, 2026

Announcement

**Upcoming authorization changes for integration runs**

Application Integration is updating how identities are handled for integration runs. Every run will act as either the person who triggered it or a run-as service account that you configure, and running an integration will require permission to act as that service account. Integrations that run without a person, such as those started by a schedule or an event, will need an explicitly configured run-as service account.

Action might be required before the change takes effect. For guidance on identifying affected integrations and updating them, see [Prepare for upcoming authorization changes](https://docs.cloud.google.com/application-integration/docs/prepare-for-authorization-changes).

## August 21, 2026

Security

**Missing authorization in QueryEngineTask (CVE-2026-12710)**

A missing authorization vulnerability ([CVE-2026-12710](https://nvd.nist.gov/vuln/detail/CVE-2026-12710)) in `QueryEngineTask` in [Application Integration](https://docs.cloud.google.com/application-integration/docs) was patched on April 4, 2026, and no customer action is needed.

## June 25, 2026

Security

**Security bulletins page**

See the new security bulletins page for Application Integration. Use it to stay informed about related security updates, vulnerabilities, and remediations. For more information, see [Security bulletins](https://docs.cloud.google.com/application-integration/docs/security-bulletins).

## February 02, 2026

Feature

**FIFO message processing with Pub/Sub ordering keys**

Application Integration now supports publishing messages to Google Cloud Pub/Sub topics using ordering keys, enabling First-In, First-Out (FIFO) message processing. By setting an ordering key in the Pub/Sub trigger's `Publish Message` action, you can ensure messages are received in the correct order, enhancing reliability for integrations requiring ordered message processing. For more information on how to use ordering keys to publish messages, see [Using ordering keys](https://cloud.google.com/pubsub/docs/publisher#using-ordering-keys).

## October 31, 2025

Feature

**Troubleshoot failed execution logs using AI**

You can now use AI-powered troubleshooting with Google Gemini to analyze failed execution logs, identify root causes, and receive precise, actionable steps to resolve errors. To use this feature, you must enable AI capabilities in your Google Cloud region. For more information, see [ Troubleshoot failed execution logs using AI](https://cloud.google.com/application-integration/docs/troubleshoot-execution-logs-using-AI).

## October 10, 2025

Feature

**Manage Application Integration resources using custom constraints**

You can now use custom constraints with Organization Policy to provide more granular control over specific fields for some Application Integration resources. For more information, see [Manage Application Integration resources using custom constraints](https://cloud.google.com/application-integration/docs/custom-constraints). This feature is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 16, 2025

Change

**Salesforce connected app requires installation for OAuth 2.0 authentication**

A new security requirement from Salesforce restricts the use of uninstalled connected apps. To ensure your Salesforce triggers remain functional, you must install the [connected app](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create.htm&type=5) in your Salesforce account.

When establishing a new Salesforce trigger using OAuth 2.0 authentication, you are now required to install the connected app within your Salesforce account. This step is also necessary for existing triggers using OAuth 2.0 authentication if the connected app is not already installed, as failure to do so may cause them to stop working.

For more information, see [Install the OAuth 2.0 connected app](https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger#post-setup).

## August 18, 2025

Change

**Standard canvas view**

The integration editor now features a single, standard [canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view). The legacy canvas is no longer available.

## May 05, 2025

Change

**Cloud Function Task adds support for Cloud Functions v2 API**

The Cloud Function task in Application Integration now lets you create, link, and run the latest generation of serverless functions, called Cloud Run functions, using the Cloud Functions v2 API.

For more information, see [Cloud Function Task](https://cloud.google.com/application-integration/docs/configure-cloud-function-task).

Change

**Control HTTP call access by region in Application Integration**

Application Integration now offers a new control within the **Regions** page to enable or disable HTTP calls for integrations on a per-region basis. 

For more information, see [Manage regions](https://cloud.google.com/application-integration/docs/enable-new-region).

## April 21, 2025

Change

**New Canvas View is enabled by default in the Integration Editor**

The new Canvas View is now enabled by default in the integration editor. This change is a default setting and no manual enablement is required. You can switch to the old canvas view by disabling the **New canvas view** toggle.

For more information, see [Use the new canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view).

## April 02, 2025

Feature

**Build Conversational Agents with Dialogflow CX** ([Preview](https://cloud.google.com/products#product-launch-stages))

Application Integration now simplifies the creation of conversational experiences with direct integration with Conversational Agents (Dialogflow CX). Using API triggers, you can now build intelligent chatbots and automated tools directly within your integration workflows, enhancing user interactions and automating tasks.

For more information, see [Build conversational agents with Application Integration](https://docs.cloud.google.com/application-integration/docs/conversational-agents).

Change

**Enhancements to Replay Execution**

Application Integration Replay Execution now provides the following enhancements:

  * **Modify input parameters on replay:** You can now modify the input parameters of an integration execution when initiating a replay. This provides greater flexibility in fixing failed executions.
  * **Continue execution from point of failure:** When replaying an integration, you can now choose to continue the execution from the point of the last failure. This will retry the failed task and, upon success, continue the execution from that point, saving time and effort.



For more information, see [Introduction to replay executions](https://docs.cloud.google.com/application-integration/docs/replay-executions).

## February 19, 2025

Change

**Enhancements to Execution Logs**

Application Integration Execution Logs now provides the following enhancements:

  * **View detailed task execution information:** The dedicated **Task Execution pane** displays comprehensive execution details, including start and end times, status, type, and variable payload information , enabling improved debugging.
  * **Download execution logs in JSON format:** You can now download integration execution logs as structured JSON files, facilitating easier log analysis.
  * **View sub-integration execution logs:** The **Execution Logs page** now displays all sub-integration execution logs within the same stack trace as the main integration, simplifying troubleshooting of complex integration flows.



For more information, see [View execution logs](https://docs.cloud.google.com/application-integration/docs/integration-execution-logs).

## January 23, 2025

Deprecated

**Deprecation of Rhino engine for JavaScript Task**

Effective January 24, 2025, Application Integration will no longer support Rhino as the JavaScript execution engine. All existing published JavaScript tasks will continue to use Rhino and can be [migrated to V8 manually](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task#migrate-javascript-tasks). Newly created JavaScript tasks will exclusively use V8. 

For more information, see [JavaScript execution engine](https://docs.cloud.google.com/application-integration/docs/configure-javascript-task#javascript-execution-engine). This deprecation is related with [CVE-2025-0982](https://www.cve.org/cverecord?id=CVE-2025-0982).

Change

You will not be able to use the [Send email task](https://docs.cloud.google.com/application-integration/docs/configure-send-email-task) in your integrations if you have enabled VPC service perimeter for the Application Integration service.

## January 13, 2025

Change

**Config variables pane** ([Preview](https://cloud.google.com/products#product-launch-stages))

You can now view and edit all the config variables defined within your integration using the new **Config Variables** pane. For more information, See [View and edit config variables](https://docs.cloud.google.com/application-integration/docs/variables#view_config_var).

## December 20, 2024

Change

**Dynamic Backend Authentication support for Connectors**

Application Integration now supports dynamic backend authentication for connectors. Enable **Authentication Override** in Integration Connectors to allow your connections to seamlessly switch between authentication methods during runtime. 

For more information, see [Configure authentication override](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override).

## December 19, 2024

Feature

You can now [build and publish custom connectors for Google Cloud Marketplace](https://docs.cloud.google.com/integration-connectors/docs/marketplace/marketplace-connector-overview). This feature is in [preview](https://cloud.google.com/products#product-launch-stages). 

The following connectors built by partners are available in the Google Cloud Marketplace. You can use these connectors to create connections and use them in Application Integration.

  * Exact HR
  * Openlegacy IBMi/AS/400 API
  * Salesforce Commerce Cloud B2B



## December 13, 2024

Feature

**Integration templates** ([Preview](https://cloud.google.com/products#product-launch-stages))

Save time and effort building integrations with integration templates. These pre-defined blueprints provide a starting point for common integration flows, allowing you to quickly create and customize integrations without starting from scratch. 

For more information, see [Templates](https://docs.cloud.google.com/application-integration/docs/templates).

Feature

**Generate and view OpenAPI Specification** ([Preview](https://cloud.google.com/products#product-launch-stages))

You can now generate and view the OpenAPI Specification for any published integration that uses API triggers. This allows for greater understanding and analysis of your integration's API interactions. 

For more information, see [View OpenAPI Specification for your integration](https://docs.cloud.google.com/application-integration/docs/view-openapi-spec).

Change

**API trigger input and output variables**

You can now set request and response payloads for an API trigger using trigger specific input and output variables. For more information, see [API trigger](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger).

## November 18, 2024

Feature

**JavaScript task using Gemini**

If your integration flow requires any complex data mapping logic, Gemini can now recommend a JavaScript task. For more information, see [Create an integration using Gemini](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#create-an-integration).

You can add a JavaScript task, edit an existing task, or use Gemini to help understand the JavaScript code. For more information, see [Configure JavaScript tasks](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#configure-javascript-tasks).

## October 28, 2024

Feature

**Add failure policy** ([Generally available (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages))

You can now configure more complicated [retry strategies for tasks](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy), such as retries based on the error codes or the variable values during the execution:

  * Configure multiple ordered conditional failure policies for each task.
  * Configure a default failure policy that will be applied if no conditional failure policies matches.
  * Use [system auto-generated variables](https://docs.cloud.google.com/application-integration/docs/variables#system-variables) in the failure policies. For example, `ExecutionMode` and `ErrorInfo`.



For more information, see [Example for error handling](https://docs.cloud.google.com/application-integration/docs/error-handling#example).

## October 08, 2024

Feature

**Build integrations with Gemini Code Assist (GA)**

Building integrations with Gemini Code Assist is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). 

Additionally, if you have API Hub enabled in your project, then Gemini can assist you to provide contextually appropriate Call REST Endpoint tasks and task configuration recommendations based on the logical flow of your existing integration. For more information see, [Configure Call REST API tasks](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#configure-call-rest-api-tasks).

## October 06, 2024

Feature

**Diagram mode in the Data Transformer Task** ([Preview](https://cloud.google.com/products#product-launch-stages))

The **Diagram** mode provides a console-based experience to select the input and output variables and perform transformations in the data transformation editor. For more information, see the [Data Transformer task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task).

Feature

**Replay execution** ([Preview](https://cloud.google.com/products#product-launch-stages))

You can now rerun a failed integration with the same parameters as the previous execution. For more information, see [Replay executions](https://docs.cloud.google.com/application-integration/docs/replay-executions).

**Cancel execution** ([Preview](https://cloud.google.com/products#product-launch-stages))

If you have executions that are suspended due to an approval task or a technical issue, you can now choose to cancel those executions. For more information, see [Cancel executions](https://docs.cloud.google.com/application-integration/docs/cancel-executions).

Feature

**Test cases** ([Preview](https://cloud.google.com/products#product-launch-stages))

You can now test if your integration is working as intended by creating and running test cases on your complex integrations.

For information about test case, see [Introduction to test cases](https://docs.cloud.google.com/application-integration/docs/test-cases). Learn how to do the following:

  * [Create test cases](https://docs.cloud.google.com/application-integration/docs/create-test-cases)
  * [Configure test cases](https://docs.cloud.google.com/application-integration/docs/configure-test-cases)
  * [Manage test cases](https://docs.cloud.google.com/application-integration/docs/manage-test-cases)
  * [Run test cases](https://docs.cloud.google.com/application-integration/docs/run-test-cases)
  * [Upload and download test cases](https://docs.cloud.google.com/application-integration/docs/upload-download-test-cases)



Feature

**Local logging in async mode** ([Generally available (GA)](https://cloud.google.com/products#product-launch-stages))

By default, local logging for new integrations is now enabled in async mode. With this change, the log data is persisted (written) at fixed intervals or after the completion of the integration's execution, whichever is earlier. You can change the default settings by [editing the integration details](https://docs.cloud.google.com/application-integration/docs/view-integration-details#edit-integration-details).

For more information, see [Local logging](https://docs.cloud.google.com/application-integration/docs/local-logging).

## September 25, 2024

Feature

**View logs in Cloud Logging**

Viewing integration execution logs in Cloud Logging is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [View logs in Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging)

## September 24, 2024

Feature

The [Resolve JSON Path ](https://docs.cloud.google.com/application-integration/docs/reference/data-transformer-reference/json-functions-reference#resolve-json-path) data transformer function is now available. This function resolves a JSON path on a given JSON object by using the `JSONPath` reference.

## September 12, 2024

Feature

The [XSLT Transform](https://docs.cloud.google.com/application-integration/docs/reference/data-transformer-reference/xml-functions-reference#xslt-transform) data transformer function is now available. This function transforms the specified XML string using the specified XSL string.

## August 22, 2024

Feature

**New canvas view**

In the integration editor layout, you can try the [new canvas view](https://docs.cloud.google.com/application-integration/docs/canvas-view) to create integration flows. This feature is in [preview](https://cloud.google.com/products#product-launch-stages). The canvas view offers the following benefits:

  * Improved responsiveness of the canvas interaction
  * Clearer view of your integration
  * Minimap view
  * Easier to build integrations



## August 18, 2024

Feature

In the Application Integration editor, you can now search, browse, and select tasks and connectors in the **[Tasks](https://docs.cloud.google.com/application-integration/docs/tasks)** list. For more information, see [Add a Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task#add-a-connectors-task).

## July 22, 2024

Feature

The [Solace trigger](https://docs.cloud.google.com/application-integration/docs/configure-solace-trigger) is now available in [preview](https://cloud.google.com/products#product-launch-stages).

## July 15, 2024

Feature

You can now share custom connectors between different Google Cloud projects by [exporting and importing the connector specification](https://docs.cloud.google.com/application-integration/docs/manage-custom-connector-versions#export-import). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## July 11, 2024

Feature

The following [Connector Event triggers](https://docs.cloud.google.com/application-integration/docs/triggers#event-triggers) are [generally available](https://cloud.google.com/products#product-launch-stages):

  * [SAP ERP trigger](https://docs.cloud.google.com/application-integration/docs/configure-sap-erp-trigger)
  * [SAP Gateway trigger](https://docs.cloud.google.com/application-integration/docs/configure_sap_gateway_trigger)



## May 26, 2024

Feature

The [TIBCO EMS trigger](https://docs.cloud.google.com/application-integration/docs/configure-tibcoems-trigger) is now available in [preview](https://cloud.google.com/products#product-launch-stages).

## May 21, 2024

Announcement

Application Integration is now available in Milan (`europe-west8`). For a list of supported regions, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).

## May 20, 2024

Feature

**Terraform support**

You can now use Terraform to [provision new regions](https://docs.cloud.google.com/application-integration/docs/enable-new-region#provision-new-region) and [create authentication profiles](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles#createAuthProfile). For a detailed reference document about terraform resources, see [`google_integrations_client`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integrations_client) and [`google_integrations_auth_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integrations_auth_config).

## May 03, 2024

Issue

**Loop Metadata variables are changing**

In the [For each loop](https://cloud.google.com/application-integration/docs/configure-for-each-loop-task) and [While loop](https://cloud.google.com/application-integration/docs/configure-while-loop-task) tasks, there's a `Loop metadata` variable in which you will find duplicate keys for the output variable–for example, `Current Iteration Count` and `current_iteration_count`. We recommend you to use the variables that contain the underscore (`_`) symbol because the other keys are being deprecated. 

For more information, see [Known issue: Duplicate keys in the Loop metadata](https://docs.cloud.google.com/application-integration/docs/known-issue#duplicate_keys_in_the_loop_metadata).

## April 29, 2024

Feature

With Gemini, you can now [build integrations in Application Integration](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini):

  * [Create and build integrations](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#create-and-build-integrations)
  * [Configure connector tasks in an integration](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#configure-connector-tasks)
  * [Add edge conditions and append additional tasks to an integration](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#append)
  * [Generate integration description](https://docs.cloud.google.com/application-integration/docs/build-integrations-gemini#generate-integration-description)



This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## April 28, 2024

Feature

While configuring a [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger#configure-a-cloud-pubsub-trigger), you can now add a config variable for your service account. [Config variables](https://docs.cloud.google.com/application-integration/docs/variables#config_var) let you externalize configuration for integrations.

## April 24, 2024

Change

For [Cloud Pub/Sub triggers](https://cloud.google.com/application-integration/docs/configure-pubsub-trigger), the default value of the [expiration period option](https://cloud.google.com/pubsub/docs/subscription-properties#expiration_period) for subscriptions is changed from `31 days` to `never expire`. If you want to change the value of the expiration period, then you must update the Cloud Pub/Sub subscription in the Google Cloud console.

## April 21, 2024

Feature

[Apache Kafka trigger](https://docs.cloud.google.com/application-integration/docs/configure-apache-kafka-trigger) is now in [preview](https://cloud.google.com/products#product-launch-stages).

## March 06, 2024

Feature

Application Integration now supports [config variables](https://docs.cloud.google.com/application-integration/docs/variables#config_var). Config variables let you to [build CICD for your integration](https://docs.cloud.google.com/application-integration/docs/build-cicd). This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## February 23, 2024

Feature

Application Integration now supports [private triggers](https://docs.cloud.google.com/application-integration/docs/configure-private-trigger) that enable you to break large flows into various subflows. This feature is in [preview](https://cloud.google.com/products#product-launch-stages).

## February 19, 2024

Feature

**Data masking in logs**

You can now prevent sensitive data from appearing the integration execution logs. For more information, see [Mask sensitive data in logs](https://docs.cloud.google.com/application-integration/docs/mask-sensitive-data-logs).

## February 12, 2024

Feature

You can now also view the integration execution logs in Cloud Logging. For more information, see [View logs in Cloud Logging](https://docs.cloud.google.com/application-integration/docs/cloud-logging).

## January 24, 2024

Feature

**Custom connectors [Preview]**

Application Integration now supports custom connectors. The custom connectors feature (based on the Open API specification) lets you create your own connectors that aren't a part of the standard connectors provided by Integration Connectors. You can use these connectors in your integrations. For more information, see [Custom connectors](https://docs.cloud.google.com/integration-connectors/docs/custom-connectors).

## January 23, 2024

Feature

The following new [data transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference) are available:

  * [`getIntegrationVersionId ()`](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference#integration-version-id): Get the integration version ID of the current integration.

  * [`getIntegrationVersionNumber()`](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference#integration-version-number): Get the version number of the current integration.




## January 16, 2024

Feature

[Webhook triggers](https://docs.cloud.google.com/application-integration/docs/configure-webhook-trigger) are now supported in [preview](https://cloud.google.com/products#product-launch-stages). With webhook triggers, you can build integrations for your data sources that don't have specific triggers but support webhook for event listening.

## December 13, 2023

Announcement

Application Integration is now available in the following regions:

  * `asia-east2` (Taiwan)
  * `asia-northeast2` (Osaka)
  * `asia-northeast3` (Seoul)
  * `asia-south2` (Delhi)
  * `asia-southeast2` (Jakarta)
  * `europe-central2` (Warsaw)
  * `europe-west10` (Berlin)
  * `europe-west12` (Turin)
  * `northamerica-northeast2` (Toronto)
  * `southamerica-west1` (Santiago)
  * `us-east5` (Columbus)
  * `us-west3` (Salt Lake City)
  * `us-west4` (Las Vegas)
  * `us-south1` (Dallas)



For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/application-integration/docs/locations).

## December 01, 2023

Feature

**Cloud Pub/Sub trigger supports cross-project topics**

You can now configure your [Cloud Pub/Sub trigger](https://docs.cloud.google.com/application-integration/docs/configure-pubsub-trigger) for a Pub/Sub topic that isn't in the same Google Cloud project as your integration. The Pub/Sub topic can be in any Google Cloud project.

Starting with this release, you must specify a service account when configuring the Cloud Pub/Sub trigger. Your existing Cloud Pub/Sub triggers, that don't have any service account associated with them, will continue to work as before. However, if you want to modify the Pub/Sub topic in any of the existing Cloud Pub/Sub triggers, you must also configure a service account for those triggers to continue using them.

## November 29, 2023

Change

The **Database persistence** feature is now renamed to **Local logging** , which also supports logging in **ASYNC** mode. For more information, see [Local logging](https://docs.cloud.google.com/application-integration/docs/local-logging).

Announcement

Application Integration is now available in the Dammam (`me-central2`) region. For the list of all the supported regions, see [Locations](https://docs.cloud.google.com/application-integration/docs/locations).

## November 23, 2023

Feature

[HubSpot trigger](https://docs.cloud.google.com/application-integration/docs/configure-hubspot-trigger) is now available in [preview](https://cloud.google.com/products#product-launch-stages).

## November 21, 2023

Feature

The following [Connector Event triggers](https://docs.cloud.google.com/application-integration/docs/triggers#connector-event-triggers-preview) are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [IBM MQ trigger](https://docs.cloud.google.com/application-integration/docs/configure-ibmmq-trigger)
  * [Rabbit MQ trigger](https://docs.cloud.google.com/application-integration/docs/configure-rabbitmq-trigger)



## October 19, 2023

Announcement

The maximum memory available for script evaluation in the [Data Transformer Script task](https://docs.cloud.google.com/application-integration/docs/configure-data-transformer-script-task) is 300 MB. For the list of all the applicable limits, see [Quotas and Limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## October 10, 2023

Feature

The following new [data transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference) are available:

  * [Manifest XML](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference#manifest-xml) \- Converts the specified input JSON object into an XML string.

  * [Parse XML](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference#parse-xml) \- Parses the specified input XML string into a JSON object.




Feature

**IAM Conditions for fine-grained access**

[IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) lets you define and enforce conditional, attribute-based access control for Google Cloud resources, including Application Integration resources. For more information, see [Add IAM conditions](https://docs.cloud.google.com/application-integration/docs/add-iam-conditions).

Feature

You can now view the detailed summary of an integration from the Integration designer. For more information, see [View integration details](https://docs.cloud.google.com/application-integration/docs/view-integration-details).

Change

**Support for user-defined service account**

You can now configure a service account of your choice for an integration. The option to select a service account is displayed to you during the integration creation step.

## September 22, 2023

Feature

**Vertex AI - Predict task**

Starting with this release, Application Integration provides the [Vertex AI - Predict task](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-vertex-ai-predict-task) that lets you perform online predictions on your ML models.

## September 06, 2023

Feature

**Application Integration Quick setup ([GA](https://cloud.google.com/products/#product-launch-stages))**

Application Integration **Quick setup** is now generally available in all the supported [Google Cloud locations](https://docs.cloud.google.com/application-integration/docs/locations). 

**Quick setup** is a single-click operation that automatically provisions Application Integration with the default configurations needed to get you started with the product.

For more information, see [Set up Application Integration](https://docs.cloud.google.com/application-integration/docs/setup-application-integration#quick).

## July 20, 2023

Feature

**Connector Event triggers** ([Preview](https://cloud.google.com/products#product-launch-stages))

Application Integration introduces **Connector Event triggers** ; specialized triggers that let you invoke an integration based on the [event subscriptions](https://docs.cloud.google.com/integration-connectors/docs/eventsubscription) created in various business applications using [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs).

The following Connector Event triggers are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [Jira Cloud trigger](https://docs.cloud.google.com/application-integration/docs/configure-jira-cloud-trigger)
  * [ServiceNow trigger](https://docs.cloud.google.com/application-integration/docs/configure-servicenow-trigger)
  * [Zendesk trigger](https://docs.cloud.google.com/application-integration/docs/configure-zendesk-trigger)



For more information, see [Connector Event triggers](https://docs.cloud.google.com/application-integration/docs/triggers#connector-event-triggers-preview).

Issue

**Known issues**

  * [Integration fails to publish when duplicate Connector Event triggers are configured](https://docs.cloud.google.com/application-integration/docs/known-issue#integration_fails_to_publish_when_duplicate_connector_event_triggers_are_configured)
  * [Event subscription error when an integration containing Connector Event triggers is uploaded](https://docs.cloud.google.com/application-integration/docs/known-issue#event_subscription_error_when_an_integration_containing_connector_event_triggers_is_uploaded)



For more information, see [Application Integration known issues](https://docs.cloud.google.com/application-integration/docs/known-issue).

## July 05, 2023

Fixed

The issue relating to [Application Integration setup failure in a new Google Cloud project](https://docs.cloud.google.com/application-integration/docs/known-issue#application_integration_fails_to_set_up_in_a_new_google_cloud_project) has been resolved.

## June 26, 2023

Feature

**Data Transformer Script task** ([Preview](https://cloud.google.com/products#product-launch-stages))

The Data Transformer Script task is a template engine based data mapping feature available in Application Integration. With the Data Transformer Script task and the supported [Data Transformer functions](https://docs.cloud.google.com/application-integration/docs/data-transformer-functions-reference), you can create and evaluate custom Jsonnet templates in order to perform data mapping in your integration.

For more information, see [Data Transformer Script task](https://docs.cloud.google.com/application-integration/docs/data-mapping-overview#data-transformer).

## June 13, 2023

Announcement

**Application Integration is now[generally available (GA)](https://cloud.google.com/products/#product-launch-stages)**

[Application Integration](https://docs.cloud.google.com/application-integration/docs) is now generally available in all the supported [Google Cloud locations](https://docs.cloud.google.com/application-integration/docs/locations). 

Preview features such as [Cloud Scheduler trigger](https://docs.cloud.google.com/application-integration/docs/configuring-cloud-scheduler-trigger), [Error catcher trigger](https://docs.cloud.google.com/application-integration/docs/configure-error-catcher-trigger), [JavaScript task](https://docs.cloud.google.com/application-integration/docs/run-javascript-task), [Return task](https://docs.cloud.google.com/application-integration/docs/configure-return-task), and [Google-managed encryption keys](https://docs.cloud.google.com/application-integration/docs/encryption) are now moved to GA.

**Important:** The billing cycle for Application Integration will start from **July 1, 2023**.

Change

**Integration designer changes**

Several styling and user experience enhancements have been made to the integration designer layout and user interface. The new enhancements include a new _variable pane_ that lets you create and manage all your integration variables in one place, a revamped _designer toolbar_ and _navigation bar_ design, and a refreshed _Integration designer canvas_.

For more information, see [Integration designer](https://docs.cloud.google.com/application-integration/docs/integration-designer-layout).

Feature

The following new features are added in this GA release:

**Cloud Monitoring**

Application Integration is integrated with Cloud Monitoring to provide visibility into the usage, performance, alerts, and the overall health of your integration resources. 

For more information, see [Monitor Application Integration resources](https://docs.cloud.google.com/application-integration/docs/monitoring-overview).

**Inline connection creation**

You can now use the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) in Application Integration to directly create a new connection in the [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs) platform.

For more information, see [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task).

Issue

**Known issues**

  * [Application Integration fails to set up in a new Google Cloud project](https://docs.cloud.google.com/application-integration/docs/known-issue#application_integration_fails_to_set_up_in_a_new_google_cloud_project)
  * [Integration designer screen compatibility issue](https://docs.cloud.google.com/application-integration/docs/known-issue#integration_designer_screen_compatibility_issue)



For more information, see [Application Integration known issues](https://docs.cloud.google.com/application-integration/docs/known-issue).

Libraries

Application Integration v2 REST API is available in [preview](https://cloud.google.com/products#product-launch-stages). 

For more information, see [REST API reference (v2)](https://docs.cloud.google.com/application-integration/docs/reference/rest/v2).

## May 23, 2023

Feature

**New tasks for Google Cloud services**

The following new integration tasks are available in [preview](https://cloud.google.com/products#product-launch-stages):

  * [AI Platform - Prediction](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-ml-prediction-task)
  * [Cloud KMS - encrypt](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-cloudkms-encrypt-task)
  * [Cloud KMS - decrypt](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-cloudkms-decrypt-task)
  * [Dataflow - Create Job](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-dataflow-createjob-task)
  * [Drive - List](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-drive-list-task)
  * [Doc AI - Batch Process](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-documentai-batchprocess-task)
  * [Doc AI - Process](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-documentai-process-task)
  * [Doc AI - Operation](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-documentai-operation-task)
  * [Firestore - Batch Get](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-firestore-batchget-task)
  * [Firestore - Batch Write](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-firestore-batchwrite-task)
  * [Firestore - Document Get](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-firestore-documentget-task)
  * [Language - Annotate Text](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-language-annotatetext-task)
  * [Language - Classify Text](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-language-classifytext-task)
  * [Sheets - Append](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-sheets-append-task)
  * [Sheets - Batch Get](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-sheets-batchget-task)
  * [Sheets - Get](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-sheets-get-task)
  * [Translate - Document](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-translate-document-task)
  * [Translate - Text](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-translate-text-task)
  * [Workflows - Execute](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-workflowexecutions-execute-task)



## May 22, 2023

Feature

**Support for Google-managed encryption keys**

Application Integration now uses Google-managed encryption keys as the default method of data encryption for your provisioned regions. You can optionally modify your encryption method with customer-managed encryption keys (CMEK).

For more information, see [Encryption methods](https://docs.cloud.google.com/application-integration/docs/encryption).

Feature

**Return task**

The Return task lets you customize the error messages corresponding to the HTTP response codes that are returned during an integration execution failure.

For more information, see [Return task](https://docs.cloud.google.com/application-integration/docs/configure-return-task).

Feature

**Error catcher trigger**

The Error Catcher trigger lets you invoke an [error catcher](https://docs.cloud.google.com/application-integration/docs/error-catcher) that is defined or customized to handle the failure of an identified trigger, task, or edge condition in your integration.

For more information, see [Error catcher trigger](https://docs.cloud.google.com/application-integration/docs/configure-error-catcher-trigger).

## May 09, 2023

Feature

**Cloud logs support for Connectors tasks**

You can now view the execution logs of a failed [Connectors task](https://docs.cloud.google.com/application-integration/docs/connectors-task) in Application Integration.

For more information, see [Execution Logs](https://docs.cloud.google.com/application-integration/docs/viewing-logs#use-logs-to-troubleshoot-and-trace-connector-failures).

Fixed

The issue relating to the validation of incorrect variable assignments in an integration has been resolved.

## May 01, 2023

Feature

Application Integration is now available in the following locations:

  * Melbourne (`australia-southeast2`)
  * Finland (`europe-north1`)
  * Paris (`europe-west9`)
  * Madrid (`europe-southwest1`)
  * Doha (`me-central1`)
  * Tel Aviv (`me-west1`)



For more information about the supported locations, see [Application Integration locations](https://docs.cloud.google.com/application-integration/docs/locations).

## April 20, 2023

Issue

Application Integration fails to validate incorrect variable assignments in an integration. For example, you can currently assign a JSON value to an unassigned variable of String data type. This behaviour might cause data mapping and integration failures.

Until this issue is resolved, we recommend that you do the following:

  * Assign values to an integration variable as per the variable data type.
  * Verify and update existing integration variable values as per its respective variable data type.



## April 03, 2023

Feature

**Secret Manager - Access task**

The Secret Manager - Access task lets you access secret versions that are stored in [Cloud Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) from your integration. 

For more information, see [Secret Manager - Access task](https://docs.cloud.google.com/application-integration/docs/gcp-tasks/run-secretmanager-access-task).

**Note:** Rollouts of this feature will begin on April 3, 2023, and may take four or more business days to be completed across all Google Cloud zones. You may not be able to provision Application Integration until the rollout is complete.

## February 09, 2023

Change

**Data Mapping Editor improvements**

**Transform expression changes:**

  * You can now add, modify, or remove a function or a function parameter in-between an existing transform expression without losing the subsequent transform functions in the expression.
  * When applying a pre-defined transform function to a variable in the **Data Mapping Editor** , the function selection menu now displays the list of functions as per the return type of the preceding function or the data type of the preceding parameter.



**Data Mapping Editor UI changes:**

  * _Input_ rows are updated to display indent guides to improve readability and structure recognition.
  * Mapping validation errors are now highlighted for each function in an _Input_ row.



For more information, see [Data Mapping editor](https://docs.cloud.google.com/application-integration/docs/data-mapping-overview#data-mapping-editor).

## February 06, 2023

Feature

**JavaScript task**

The JavaScript task lets you write custom JavaScript code snippets for your integration.

Using the JavaScript Editor, you can code complex data mapping logic for your integration, perform variable assignments, and add or modify integration variables.

For more information, see [JavaScript task](https://docs.cloud.google.com/application-integration/docs/run-javascript-task).

Feature

**Delete integration**

You can now delete an entire integration without the need to individually delete all the respective integration versions. 

When you delete an integration, you permanently delete all the versions of that integration, including all the integration variables, configured triggers, tasks, and data mappings. 

For more information, see [Delete integrations](https://docs.cloud.google.com/application-integration/docs/delete-integration).

Change

**New Overview page**

A new [Overview page](https://console.cloud.google.com/integrations) is now introduced in Application Integration. It's the first place you land when opening Application Integration in your Google Cloud console, and helps you understand and get started with setting up Application Integration in your Google Cloud project. 

**Note:** Rollouts of this release will begin on February 6, 2023, and may take four or more business days to be completed across all Google Cloud zones. You may not be able to provision Application Integration until the rollout is complete.

## January 10, 2023

Feature

**Cloud Scheduler trigger**

The Cloud Scheduler trigger lets you schedule your integration executions for defined time periods or regular intervals across multiple regions. Cloud Scheduler triggers leverage the [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) services to provide a fully managed enterprise-grade cron job scheduler within Application Integration. 

For more information, see [Cloud Scheduler trigger](https://docs.cloud.google.com/application-integration/docs/configuring-cloud-scheduler-trigger).

## December 26, 2022

Feature

**Test without publishing an integration**

You can now test your integration without the need to publish or create a new integration version. Testing an integration lets you experiment with the integration input variable values, and helps in identifying any faults in the integration connection flow before you finalize and publish the integration.

For more information, see [Test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).

## September 28, 2022

Announcement

**Application Integration Preview Release**

Application Integration is now available in [preview](https://cloud.google.com/products#product-launch-stages). Application Integration is an Integration-Platform-as-a-Service (iPaaS) solution in Google Cloud that offers a comprehensive set of core integration tools to connect and manage the multitude of applications and data required to support various business operations.

For more information about the Application Integration features and functionalities, see [Application Integration documentation](https://docs.cloud.google.com/application-integration/docs).

**Note:** Rollouts of this release will begin today and may take four or more business days to be completed across all Google Cloud zones. You may not be able to provision Application Integration until the rollout is complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
