---
url: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment/
title: Create an enrollment to receive events \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:12.366087+00:00
---

# Create an enrollment to receive events  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Create an enrollment to receive events Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

An enrollment identifies a subscription to a particular bus. The enrollment defines the matching criteria that determines which messages are routed to a destination. It also specifies the pipeline that matched messages should be routed through. A pipeline lets you configure a target destination and also provides the option of transforming any matched events prior to delivering them to the destination.

Note the following:

  * A pipeline and enrollment must be in the same Google Cloud project. (The bus being subscribed to can be in the same or a different project.)
  * One pipeline can be used for multiple enrollments.
  * Only one destination can be the target of messages routed by a pipeline.



## Before you begin

Before configuring either a pipeline or an enrollment, you should have already [created an Eventarc Advanced bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus).

## Required roles

An Identity and Access Management (IAM) role contains a set of permissions that lets you perform specific actions on Google Cloud resources. The following roles and permissions are required when creating a pipeline and an enrollment to route messages:

  * To get the permission that you need to **create a pipeline** , ask your administrator to grant you the [Eventarc Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.developer) (`roles/eventarc.developer`) IAM role on your pipeline project. This predefined role contains the `eventarc.pipelines.create` permission, which is required to create a pipeline.
  * To get the permission that you need to **create an enrollment** , ask your administrator to grant you the [Eventarc Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.developer) (`roles/eventarc.developer`) IAM role on your enrollment project. This predefined role contains the `eventarc.enrollments.create` permission, which is required to create an enrollment.
  * To get the permission that you need to **use a bus** , ask your administrator to grant you the [Eventarc Message Bus User](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.messageBusUser) (`roles/eventarc.messageBusUser`) IAM role on your bus project. This predefined role contains the `eventarc.buses.use` permission, which is required to use a bus.



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Create an enrollment and pipeline

You can create a pipeline and an enrollment in the following ways:

  * In the Google Cloud console
  * By using the Google Cloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API

**Note:** Creating a pipeline might take more than 10 minutes.

### Console

In the Google Cloud console, you can create both the pipeline and enrollment at the same time from the **Pipelines** page.

  1. To create an enrollment, in the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. Click add_box **Create pipeline**.

  3. In the **Pipeline details** pane, do the following:

     1. Enter a **Pipeline name**. This is the ID for your pipeline.
     2. In the **Region** list, select a region to deploy your pipeline in. The pipeline must be created in the same region as the bus. For more information, see [Eventarc Advanced locations](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).
     3. Optional: In the **Log severity** list, select the minimum severity for events described in log entries. The default is **None**. For more information, see [`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity).
     4. Optional: In the **Retry policy** section, you can modify the default configuration to [retry events](https://docs.cloud.google.com/eventarc/advanced/docs/retry-events).
     5. For **Encryption** , accept the default **Google-managed encryption key** or select **Cloud KMS key**. For more information, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek).
     6. If you select **Cloud KMS key** , do the following:

        1. In the **Key type** list, select a method to manage your keys.

You can manage your keys manually or you can use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) which lets you generate key rings and keys on-demand. If the Autokey option is disabled, it isn't yet integrated with the current resource type.

        2. In the **Select a customer-managed key** , select a key.

Note that you must select a region before you can view your customer-managed keys.

        3. Optional: To manually enter the resource name of the key, in the **Select a customer-managed key** list, click **Enter key manually** , and enter the key name in the specified format.

        4. If prompted, grant the [`cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) to the [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#eventarc-service-agent).

     7. Optional: To add labels, click add **Add label**. Labels are key-value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)

     8. Click **Continue**.

  4. In the **Enrollments** pane, do the following:

     1. Click **Add an enrollment**.
     2. Enter an **Enrollment name**.
     3. In the **Bus** list, select a bus to subscribe to.
     4. In the **CEL expression** field, write an evaluation expression [using CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel). For example:

`message.type == "google.cloud.dataflow.job.v1beta3.statusChanged"`

Note that the default expression, **true** , indicates that all messages are routed, unfiltered.

     5. Click **Done**.

     6. You can add another enrollment or click **Continue**.

  5. Optional: In the **Event mediation** pane, do the following or click **Continue** :

     1. Select the **Apply a transformation** checkbox.
     2. In the **Inbound format** list, select the applicable format.

Note that when applying a transformation, you **must** specify an inbound data format for a pipeline, and that all events must match that format.

     3. For Avro or Protobuf formats, you must specify an inbound schema. Optionally, you can upload an inbound schema. For more information, see [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events).

     4. In the **CEL expression** field, write a transformation expression [using CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel).

     5. Click **Continue**.

  6. In the **Destination** pane, do the following:

     1. In the **Destination type** list, select a destination type to route messages to. Depending on the destination type, do the following:

        * **HTTP endpoint** : specify the destination URI. The host can be either a static IP addressable from a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc), or the internal [Domain Name System (DNS)](https://docs.cloud.google.com/dns/docs/dns-overview) hostname of a service resolvable using Cloud DNS.

For example, you can target a Cloud Run service URL that will receive events as HTTP `POST` requests. Use the stable, [auto-assigned `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request) provided on the first deployment of the Cloud Run-hosted service. Or, you can target a [BigQuery table](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/insertAll) that will receive events as HTTP `POST` requests. Define a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding) to construct the HTTP request for the BigQuery API. For more information, see [Publish events to a BigQuery table](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-bigquery-table).

You can also use this destination type to specify an HTTP endpoint for Cloud Run functions ([1st gen](https://docs.cloud.google.com/functions/1stgendocs/calling/http) and [current version](https://docs.cloud.google.com/functions/docs/calling/http)). When you specify an HTTP trigger for a Cloud Run function, the function is assigned a URL at which it can receive requests.

        * **Eventarc Advanced bus** : select an [Eventarc Advanced bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus). The bus must be deployed in the same project and region as the pipeline.

        * **Workflows** : select a [Workflows workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow). You can trigger the [execution of a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow) which is a single run of the logic contained in a workflow definition. The workflow must be deployed in the same project as the pipeline.

        * **Pub/Sub topic** : select or create a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic). The topic must be created before messages can be routed to it and must be located in the same project as the pipeline. If using a [topic schema](https://docs.cloud.google.com/pubsub/docs/create-topic#use_a_schema), make sure to [transform your event message](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events) appropriately.

        * **Cloud Run service (via HTTP)** : select a [Cloud Run service](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#services) that will receive events as HTTP `POST` requests sent to its root URL path (`/`); optionally, you can specify a relative URL path on the destination service to which events should be sent. For more information, see the [quickstart](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-create-bus-console).

        * **Cloud Run job (via HTTP)** : select a [Cloud Run job](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#cloud-run-jobs) that will receive events as HTTP `POST` requests. Define a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding) that transforms the event into the format expected by the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/run). For more information, see [Publish events to a Cloud Run job](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-cloud-run-job).

     2. If applicable, in the **Outbound format** list, select a format.

Note that if an inbound data format is _not_ specified for a pipeline, an outbound format _can't_ be set.

     3. If applicable, apply a **Message binding**. For more information, see [Define a message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding).

     4. To enable authentication, select the **Enable authentication** checkbox.

        1. In the **Auth header** list, select the type of token to generate and attach as an `Authorization` header in the HTTP request:

           * An [OAuth token](https://developers.google.com/identity/protocols/OAuth2) should generally be used only when calling Google APIs hosted on `*.googleapis.com`. Optionally, specify the **Scope** of this token; otherwise, it defaults to `https://www.googleapis.com/auth/cloud-platform`. For Google Cloud services, it's a best practice to use the `https://www.googleapis.com/auth/cloud-platform` scope, which includes all Google Cloud APIs, together with [Identity and Access Management (IAM)](https://docs.cloud.google.com/eventarc/advanced/docs/access-control), which provides fine-grained access control.

Note that all requests to another Eventarc Advanced bus, Pub/Sub, or Workflows must have an HTTP Authorization header containing an OAuth token signed by Google for one of the authorized service accounts.

           * An [OIDC token](https://developers.google.com/identity/protocols/OpenIDConnect) can be used for many scenarios, including endpoints where you intend to validate the token yourself. Additionally, specify the **Audience** that this token is intended for. Generally, it should match the URL of the target pipeline. If not specified, the entire URL is used, including any request parameters.

Note that Cloud Run performs an IAM check on every request and you can use the [`run.routes.invoke`](https://docs.cloud.google.com/run/docs/reference/iam/permissions#routes) permission to configure who can access your Cloud Run service in either of the following ways:

             * Grant the permission to select service accounts or groups to allow access to the service. All requests must have an HTTP Authorization header containing an OpenID Connect token signed by Google for one of the authorized service accounts.

             * Grant the permission to [allUsers](https://docs.cloud.google.com/iam/docs/principals-overview#all-users) to allow public access.

For more information, see [Access control for Cloud Run](https://docs.cloud.google.com/run/docs/securing/security#access-control).

Learn more about [token types](https://docs.cloud.google.com/docs/authentication/token-types).

        2. In the **Service account** list, select the service account that will invoke your destination service. Or, you can create a new service account.

This specifies the IAM service account email associated with the pipeline and to which you previously granted specific roles required by Eventarc Advanced.

  7. Click **Create**.




###  gcloud 

When using the gcloud CLI, first create the pipeline, and then create the enrollment using the appropriate commands.

###  Pipeline 

  1. Open a terminal.

  2. Create a pipeline using the [`gcloud eventarc pipelines create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/create) command:
         
         gcloud eventarc pipelines create PIPELINE_NAME \
             --destinations=DESTINATION_KEY \
             --location=LOCATION

**Note:** The `--destinations` and `--mediations` flags use a hash symbol (`#`) as the default delimiter. If your expression contains a hash, specify a different delimiter to avoid parsing conflicts. For more information, see [gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping). For example, to use a semicolon (`;`) as a delimiter:  
`--destinations=^;^DESTINATION_KEY`

Replace the following:

     * `PIPELINE_NAME`: the ID of the pipeline or a fully qualified name
     * `DESTINATION_KEY`: one or more key-value pairs to configure a destination for the pipeline

You must set _only one_ of the following keys:

       * `http_endpoint_uri`—a destination URI. The host can be either a static IP addressable from a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc), or the internal [Domain Name System (DNS)](https://docs.cloud.google.com/dns/docs/dns-overview) hostname of a service resolvable using Cloud DNS. Optionally, set `http_endpoint_message_binding_template` to specify a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding).

For example, you can use this key to target a Cloud Run service URL that will receive events as HTTP `POST` requests. Use the stable, [auto-assigned `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request) provided on the first deployment of the Cloud Run-hosted service. Or, you can target a BigQuery table or a Cloud Run job. If necessary, define a message binding to construct the HTTP request for the destination API. For Cloud Run jobs, you must define a message binding that transforms the event into the format expected by the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/run).

You can also use this destination type to specify an HTTP endpoint for Cloud Run functions ([1st gen](https://docs.cloud.google.com/functions/1stgendocs/calling/http) and [current version](https://docs.cloud.google.com/functions/docs/calling/http)). When you specify an HTTP trigger for a Cloud Run function, the function is assigned a URL at which it can receive requests.

For more information, see the quickstarts for the following event destinations: [BigQuery table](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-bigquery-table), [Cloud Run job](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-cloud-run-job), and [Cloud Run service](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-create-bus).

       * `message_bus`—the ID of an [Eventarc Advanced bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus). The bus must be deployed in the same project and region as the pipeline.

       * `pubsub_topic`—the ID of a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic). The topic must be created before messages can be routed to it and, if using a [topic schema](https://docs.cloud.google.com/pubsub/docs/create-topic#use_a_schema), make sure to [transform your event message](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events) appropriately.

       * `workflow`—the ID of a [Workflows workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow). You can trigger the [execution of a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow) which is a single run of the logic contained in a workflow definition. The workflow must be deployed in the same project as the pipeline.

To enable authentication, you can set _one_ of the following keys:

       * `google_oidc_authentication_service_account`—the service account email used to generate an an [OIDC token](https://developers.google.com/identity/protocols/OpenIDConnect) which can be used for many scenarios, including endpoints where you intend to validate the token yourself. Optionally, you can set `google_oidc_authentication_audience` to specify the audience that this token is intended for. Generally, it should match the URL of the target pipeline. If not specified, the entire URL is used, including any request parameters.

Note that Cloud Run performs an IAM check on every request and you can use the [`run.routes.invoke`](https://docs.cloud.google.com/run/docs/reference/iam/permissions#routes) permission to configure who can access your Cloud Run service in either of the following ways:

         * Grant the permission to select service accounts or groups to allow access to the service. All requests must have an HTTP Authorization header containing an OpenID Connect token signed by Google for one of the authorized service accounts.

         * Grant the permission to [allUsers](https://docs.cloud.google.com/iam/docs/principals-overview#all-users) to allow public access.

For more information, see [Access control for Cloud Run ](https://docs.cloud.google.com/run/docs/securing/security#access-control).

       * `oauth_token_authentication_service_account`—the service account email used to generate an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) which should generally be used only when calling Google APIs hosted on `*.googleapis.com`. Optionally, you can set `oauth_token_authentication_scope` to specify the scope of this token; otherwise, it defaults to `https://www.googleapis.com/auth/cloud-platform`. For Google Cloud services, it's a best practice to use the `https://www.googleapis.com/auth/cloud-platform` scope, which includes all Google Cloud APIs, together with [Identity and Access Management (IAM)](https://docs.cloud.google.com/eventarc/advanced/docs/access-control), which provides fine-grained access control.

Note that all requests to another Eventarc Advanced bus, Pub/Sub, or Workflows must have an HTTP Authorization header containing an OAuth token signed by Google for one of the authorized service accounts.

Learn more about [token types](https://docs.cloud.google.com/docs/authentication/token-types).

Optional: You can set _one_ of the following keys:

       * `output_payload_format_avro_schema_definition`
       * `output_payload_format_json`
       * `output_payload_format_protobuf_schema_definition`

Note that if you set an [output format](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events), you must also specify an input format (see the following `input-payload-format-*` flags).

Optional: If `http_endpoint_uri` is _not_ used as a destination key, you can set the following keys:

       * `project`—the Google Cloud project ID of the destination resource; by default, the project ID for the pipeline is used.
       * `location`—the location of the destination resource; by default, the location for the pipeline is used.
     * `LOCATION`: a [supported Eventarc Advanced region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions)

Alternatively, you can set the gcloud CLI location property:
           
           gcloud config set eventarc/location LOCATION
           

Optional: You can use the following flags:

     * `--async` to return from the command immediately, without waiting for the operation in progress to complete.
     * `--crypto-key` to specify the fully qualified name of a [customer-managed encryption key](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek); if unspecified, Google-owned and managed keys are used.
     * `--logging-config` to configure the logging level which must be one of the following: `NONE`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`.
     * `--mediations` to apply a [transformation](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events); `transformation_template` is the only supported template and only one mediation per pipeline is supported; for example:

`--mediations=transformation_template='message.removeFields(["id\ ","credit_card_number","age"])'`

Note that if you are applying a transformation, you **must** use one of the following flags to specify an input format.

     * One of the following to specify an [input format](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events):

       * `--input-payload-format-avro-schema-definition`
       * `--input-payload-format-json`
       * `--input-payload-format-protobuf-schema-definition`
     * `--max-retry-attempts`, `--max-retry-delay`, and `--min-retry-delay` to [retry events](https://docs.cloud.google.com/eventarc/advanced/docs/retry-events)

For example:
    
    gcloud eventarc pipelines create my-pipeline \
        --destinations=http_endpoint_uri='https://example-endpoint.com',oauth_token_authentication_service_account=example-service-account@example-project.gserviceaccount.iam.com,oauth_token_authentication_scope='https://www.googleapis.com/auth/cloud-platform',output_payload_format_avro_schema_definition='{"type": "record","name": "my_record", "fields": [{"name": "my_field", "type":"string"}]}' \
        --input-payload-format-avro-schema-definition='{"type":"record", "name": "my_record", "fields": [{"name": "my_field","type": "string"}]}' \
        --location=us-central1 \
        --async
    

For more details and examples, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/create).




###  Enrollment 

  1. Open a terminal.

  2. Create an enrollment using the [`gcloud eventarc enrollments create`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/enrollments/create) command:
         
         gcloud eventarc enrollments create ENROLLMENT_NAME \
             --cel-match=MATCH_EXPRESSION \
             --destination-pipeline=PIPELINE_NAME \
             --message-bus=BUS_NAME \
             --message-bus-project=PROJECT_ID \
             --location=LOCATION

Replace the following:

     * `ENROLLMENT_NAME`: the ID of the enrollment or a fully qualified name
     * `MATCH_EXPRESSION`: the matching expression for this enrollment [using CEL](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel)—for example, `"message.type == 'google.cloud.dataflow.job.v1beta3.statusChanged'"`
     * `PIPELINE_NAME`: the target pipeline ID or its fully qualified name for this enrollment
     * `BUS_NAME`: the ID of the Eventarc Advanced bus or its fully qualified name
     * `PROJECT_ID`: the Google Cloud project ID for the bus
     * `LOCATION`: a [supported Eventarc Advanced region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions)

Alternatively, you can set the gcloud CLI location property:
           
           gcloud config set eventarc/location LOCATION
           

Optional: You can use the following flag:

     * `--async` to return from the command immediately, without waiting for the operation in progress to complete

For example:
    
    gcloud eventarc enrollments create my-enrollment \
        --cel-match="message.type == 'google.cloud.dataflow.job.v1beta3.statusChanged'" \
        --destination-pipeline=my-pipeline \
        --message-bus=my-message-bus \
        --message-bus-project=another-google-cloud-project \
        --location=us-central1 \
        --async
    




### REST API

When sending requests to the Eventarc API, first create the pipeline, and then create the enrollment.

### Pipeline

To create a pipeline, use the [`projects.locations.pipelines.create`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines/create) method.

Before using any of the request data, make the following replacements: 

  * `name`: the full resource name of the pipeline in the format `projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME`

Replace the following:

    * `PROJECT_ID`: the Google Cloud project ID for the pipeline project
    * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the pipeline is to be deployed—for example, `us-central1`
    * `PIPELINE_NAME`: the name of the pipeline
  * `LABEL_KEY` and `LABEL_VALUE`: optional. A map of label key and value pairs that help you organize your Google Cloud resources. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)
  * `ANNOTATION_KEY` and `ANNOTATION_VALUE`: optional. A map of annotation key and value pairs of free-form text. You can use them to attach arbitrary information associated with the resource. For more information, see [Annotations](https://google.aip.dev/148#annotations). 
  * `LOG_SEVERITY`: optional. The minimum severity of the event described in a log entry. One of: `NONE`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`. The default is `NONE`. For more information, see [`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity). 
  * `destinations`: the destination to which messages will be forwarded. Optionally, you can set `messageBindingTemplate` to specify a [message binding](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events#message-binding). For more information, see the [`Destination` target](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines#Destination). Only one destination is supported: 
    * `httpEndpoint`: a destination URI (`HTTP_URI`). The host can be either a static IP addressable from a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc), or the internal [Domain Name System (DNS)](https://docs.cloud.google.com/dns/docs/dns-overview) hostname of a service resolvable using Cloud DNS. 

For example, you can target a Cloud Run service URL that will receive events as HTTP `POST` requests. Use the stable, [auto-assigned `run.app` URL](https://docs.cloud.google.com/run/docs/triggering/https-request) provided on the first deployment of the Cloud Run-hosted service. Or, you can target a BigQuery table or a Cloud Run job. If necessary, define a message binding to construct the HTTP request for the destination API. For Cloud Run jobs, you must define a message binding that transforms the event into the format expected by the [Cloud Run Admin API](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/run). 

You can also use this destination type to specify an HTTP endpoint for Cloud Run functions ([1st gen](https://docs.cloud.google.com/functions/1stgendocs/calling/http) and [current version](https://docs.cloud.google.com/functions/docs/calling/http)). When you specify an HTTP trigger for a Cloud Run function, the function is assigned a URL at which it can receive requests.

For more information, see the quickstarts for the following event destinations: [BigQuery table](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-bigquery-table), [Cloud Run job](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-cloud-run-job), and [Cloud Run service](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-create-bus). 

    * `messageBus`: an [Eventarc Advanced bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus). The bus must be deployed in the same project and region as the pipeline.
    * `topic`: a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic) which must first be created in the same project as the pipeline. If using a [topic schema](https://docs.cloud.google.com/pubsub/docs/create-topic#use_a_schema), make sure to [transform your event message](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events) appropriately.
    * `workflow`: a [Workflows workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#create_a_workflow). You can trigger the [execution of a workflow](https://docs.cloud.google.com/workflows/docs/executing-workflow) which is a single run of the logic contained in a workflow definition. The workflow must be deployed in the same project as the pipeline.
  * `SERVICE_ACCOUNT_EMAIL`: the name of the service account email used to generate an [OIDC token](https://developers.google.com/identity/protocols/OpenIDConnect) which can be used for many scenarios, including endpoints where you intend to validate the token yourself. Optionally, you can set `audience` to specify the audience that this token is intended for. Generally, it should match the URL of the target pipeline. If not specified, the entire URL is used, including any request parameters. 

Alternatively, you can use `oauthToken` to specify the service account email used to generate an [OAuth token](https://developers.google.com/identity/protocols/OAuth2) which should generally be used only when calling Google APIs hosted on `*.googleapis.com`. Optionally, you can set `scope` to specify the scope of this token; otherwise, it defaults to `https://www.googleapis.com/auth/cloud-platform`. For Google Cloud services, it's a best practice to use the `https://www.googleapis.com/auth/cloud-platform` scope, which includes all Google Cloud APIs, together with [Identity and Access Management (IAM)](https://docs.cloud.google.com/eventarc/advanced/docs/access-control), which provides fine-grained access control.

Note that all requests to another Eventarc Advanced bus, Pub/Sub, or Workflows must have an HTTP Authorization header containing an OAuth token signed by Google for one of the authorized service accounts.

Learn more about [token types](https://docs.cloud.google.com/docs/authentication/token-types).




Request JSON body: 
    
    
    {
      "name": "projects/PROJECT_ID/regions/LOCATION/pipelines/PIPELINE_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "loggingConfig": {"logSeverity":"LOG_SEVERITY"},
      "destinations": [{"httpEndpoint": {"uri": "HTTP_URI"},
      "authenticationConfig": {"googleOidc": {"serviceAccount": "SERVICE_ACCOUNT_EMAIL"}}}]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "name": "projects/PROJECT_ID/regions/LOCATION/pipelines/PIPELINE_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "loggingConfig": {"logSeverity":"LOG_SEVERITY"},
      "destinations": [{"httpEndpoint": {"uri": "HTTP_URI"},
      "authenticationConfig": {"googleOidc": {"serviceAccount": "SERVICE_ACCOUNT_EMAIL"}}}]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/pipelines?pipeline_id=PIPELINE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "name": "projects/PROJECT_ID/regions/LOCATION/pipelines/PIPELINE_NAME",
      "labels": {"LABEL_KEY":"LABEL_VALUE"},
      "annotations": {"ANNOTATION_KEY":"ANNOTATION_VALUE"},
      "loggingConfig": {"logSeverity":"LOG_SEVERITY"},
      "destinations": [{"httpEndpoint": {"uri": "HTTP_URI"},
      "authenticationConfig": {"googleOidc": {"serviceAccount": "SERVICE_ACCOUNT_EMAIL"}}}]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/pipelines?pipeline_id=PIPELINE_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Enrollment

To create an enrollment, use the [`projects.locations.enrollments.create`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments/create) method.

Before using any of the request data, make the following replacements: 

  * `ENROLLMENT_NAME`: the display name of your enrollment—for example, `my_enrollment`.
  * `MATCH_EXPRESSION`: a [CEL expression](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel) identifying which messages this enrollment applies to. For example, `message.type == 'hello-world-type'`.
  * `destination`: the full resource name of the target pipeline in the format `projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME`. 

Replace the following:

    * `PROJECT_ID`: the Google Cloud project ID for the pipeline project
    * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the pipeline is deployed—for example, `us-central1`.
    * `PIPELINE_NAME`: the name of the pipeline
  * `message_bus`: the full resource name of the bus identifying the source of the messages in the format `projects/BUS_PROJECT_ID/locations/BUS_LOCATION/messageBuses/BUS_NAME`. 

Replace the following:

    * `BUS_PROJECT_ID`: the Google Cloud project ID for the bus project
    * `BUS_LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the bus is deployed—for example, `us-central1`
    * `BUS_NAME`: the name of the message bus



Request JSON body: 
    
    
    {
      "display_name": "ENROLLMENT_NAME",
      "cel_match": "MATCH_EXPRESSION",
      "message_bus": "projects/BUS_PROJECT_ID/locations/BUS_LOCATION/messageBuses/BUS_NAME",
      "destination": "projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "display_name": "ENROLLMENT_NAME",
      "cel_match": "MATCH_EXPRESSION",
      "message_bus": "projects/BUS_PROJECT_ID/locations/BUS_LOCATION/messageBuses/BUS_NAME",
      "destination": "projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/enrollments?enrollment_id=ENROLLMENT_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "display_name": "ENROLLMENT_NAME",
      "cel_match": "MATCH_EXPRESSION",
      "message_bus": "projects/BUS_PROJECT_ID/locations/BUS_LOCATION/messageBuses/BUS_NAME",
      "destination": "projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/enrollments?enrollment_id=ENROLLMENT_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/enrollments/ENROLLMENT_NAME",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## List enrollments

You can list enrollments in the following ways:

  * In the Google Cloud console
  * By using the gcloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API




### Console

  1. To list enrollments for a specific pipeline, in the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. Click the name of the pipeline for which you want to list enrollments.

The **Pipeline details** page opens.

In the **Enrollments** tab, any enrollments associated with the pipeline are listed.




###  gcloud 

  1. Open a terminal.

  2. List enrollments using the [`gcloud eventarc enrollments list`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/enrollments/list) command:
         
         gcloud eventarc enrollments list \
             --location=LOCATION

Replace `LOCATION` with a [supported Eventarc Advanced region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).




### REST API

To list enrollments, use the [`projects.locations.enrollments.list`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments/list) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the enrollments are created—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/enrollments"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/enrollments" | Select-Object -Expand Content

If successful, the response body contains instances of [`Enrollment`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments#resource:-enrollment) and the response should be similar to the following: 
    
    
    {
      "enrollments": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/enrollments/ENROLLMENT_NAME",
          "uid": "06e396f5-2d4f-43d2-961f-fd2c88403326",
          "createTime": "2025-03-26T17:57:25.214845320Z",
          "updateTime": "2025-03-26T17:57:45.136172180Z",
          "celMatch": "message.type == \"hello-world-type\"",
          "messageBus": "projects/PROJECT_ID/locations/LOCATION/messageBuses/BUS_NAME",
          "destination": "projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME"
        },
        {...}
      ]
    }
    

## Delete an enrollment

You can delete an enrollment in the following ways:

  * In the Google Cloud console
  * By using the gcloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API




### Console

  1. To delete an enrollment, in the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. Click the name of the pipeline from which you want to delete the enrollment.

The **Pipeline details** pane opens.

  3. Click edit **Edit**.

  4. Click **Continue**.

The **Enrollments** pane opens.

  5. For the enrollment that you want to delete, click the delete delete icon.

  6. Click **Save**.




###  gcloud 

  1. Open a terminal.

  2. Delete an enrollment using the [`gcloud eventarc enrollments delete`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/enrollments/delete) command:
         
         gcloud eventarc enrollments delete ENROLLMENT_NAME \
               --location=LOCATION

Replace the following:

     * `ENROLLMENT_NAME`: the ID of the enrollment or a fully qualified name
     * `LOCATION`: the [supported Eventarc Advanced region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) of the enrollment



### REST API

To delete an enrollment, use the [`projects.locations.enrollments.delete`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments/delete) method.

Before using any of the request data, make the following replacements: 

  * `ENROLLMENT_NAME`: the display name of the enrollment you want to delete—for example, `my_enrollment`.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the enrollment is deployed—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/enrollments/ENROLLMENT_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/enrollments/ENROLLMENT_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.enrollments/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/enrollments/ENROLLMENT_NAME",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## List pipelines

You can list pipelines in the following ways:

  * In the Google Cloud console
  * By using the gcloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API




### Console

In the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

Any pipelines are listed. You can optionally use the filter_list **Filter** to constrain a search.

###  gcloud 

  1. Open a terminal.

  2. List enrollments using the [`gcloud eventarc pipelines list`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/list) command:
         
         gcloud eventarc pipelines list \
             --location=LOCATION

Replace `LOCATION` with a [supported Eventarc Advanced region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).




### REST API

To list pipelines, use the [`projects.locations.pipelines.list`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines/list) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the pipelines are created—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/pipelines"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/pipelines" | Select-Object -Expand Content

If successful, the response body contains instances of [`Pipeline`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines#resource:-pipeline) and the response should be similar to the following: 
    
    
    {
      "pipelines": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME",
          "createTime": "2025-01-10T20:32:11.606516066Z",
          "updateTime": "2025-03-26T18:02:34.886616683Z",
          "uid": "7d58dd18-323a-43f6-a456-4f8c20a70218",
          "destinations": [
            {
              "httpEndpoint": {
                "uri": "HTTP_URI"
              },
              "authenticationConfig": {
                "googleOidc": {
                  "serviceAccount": "SERVICE_ACCOUNT_EMAIL"
                }
              }
            }
          ],
          "loggingConfig": {
            "logSeverity": "NONE"
          },
          "retryPolicy": {
            "maxAttempts": 5,
            "minRetryDelay": "1s",
            "maxRetryDelay": "60s"
          }
        },
        {...}
      ]
    }
    

## Delete a pipeline

You can delete a pipeline in the following ways:

  * In the Google Cloud console
  * By using the gcloud CLI in either your terminal or Cloud Shell
  * By sending a request to the Eventarc API



Note that deleting a pipeline might take more than 10 minutes.

### Console

  1. To delete a pipeline, in the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. In the list of pipelines, select the checkbox next to the name of the pipeline that you want to delete.

  3. Click delete **Delete**.

  4. Confirm the deletion by entering `Delete`.

  5. Click **Delete**.




###  gcloud 

  1. Open a terminal.

  2. Delete a pipeline using the [`gcloud eventarc pipelines delete`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/delete) command:
         
         gcloud eventarc pipelines delete PIPELINE_NAME \
               --location=LOCATION

Replace the following:

     * `PIPELINE_NAME`: the ID of the pipeline or a fully qualified name
     * `LOCATION`: the [supported Eventarc Advanced region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) of the pipeline



### REST API

To delete a pipeline, use the [`projects.locations.pipelines.delete`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines/delete) method.

Before using any of the request data, make the following replacements: 

  * `PIPELINE_NAME`: the display name of the pipeline you want to delete—for example, `my_pipeline`.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) in which the pipeline is deployed—for example, `us-central1`.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.pipelines/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/Shared.Types/ListOperationsResponse#operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/pipelines/PIPELINE_NAME",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## What's next

  * [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events)
  * [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
