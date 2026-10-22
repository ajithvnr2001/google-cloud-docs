---
url: https://docs.cloud.google.com/pubsub/docs/release-notes/
title: Pub/Sub release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:26:50.458650+00:00
---

# Pub/Sub release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Resources ](https://docs.cloud.google.com/pubsub/docs/resources)



Send feedback 

#  Pub/Sub release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains production updates and feature announcements for the Pub/Sub service. For language-specific updates about Pub/Sub [ Client Library](https://docs.cloud.google.com/pubsub/docs/reference/libraries) releases, use the following links: [C#](https://github.com/googleapis/google-cloud-dotnet/releases), [Go](https://github.com/googleapis/google-cloud-go/releases), [Java](https://github.com/googleapis/java-pubsub/releases), [Node.js](https://github.com/googleapis/nodejs-pubsub/releases), [PHP](https://github.com/googleapis/google-cloud-php/releases), [Python](https://github.com/googleapis/python-pubsub/releases), and [Ruby](https://github.com/googleapis/google-cloud-ruby/releases). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/pubsub-release-notes.xml) directly. 

## October 01, 2026

Feature

You can use Gemini Enterprise to generate code for user-defined function (UDF) single-message transforms (SMTs). For more information, see [Create a UDF SMT](https://docs.cloud.google.com/pubsub/docs/smts/udfs-overview#create-udf-smt).

## April 17, 2026

Feature

The [Pub/Sub remote MCP server](https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp) is [generally available](https://cloud.google.com/products/#product-launch-stages) (GA).

## April 16, 2026

Feature

You can stream messages from Pub/Sub directly to a [Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) table using [Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions). This feature lets you write streaming messages to Bigtable without needing a separate subscriber such as Dataflow. This feature is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

## April 06, 2026

Feature

Pub/Sub now offers the AI Inference Single Method Transform (SMT). This SMT lets you get inferences on Pub/Sub messages from Vertex AI models. The model's inferences are added to each message, making them available for downstream processing along with the original message data.

The change is being rolled out in a phased manner over the rest of the week. For more information, see [AI Inference SMT](https://docs.cloud.google.com/pubsub/docs/smts/ai-inference-smt). This feature is [generally available](https://cloud.google.com/products/#product-launch-stages).

## March 13, 2026

Feature

You can now use the [Pub/Sub remote MCP server](https://docs.cloud.google.com/pubsub/docs/use-pubsub-mcp) to manage Pub/Sub resources. You can create, list, get, update, and delete Pub/Sub topics, subscriptions, and snapshots, as well as publish messages to topics.

This feature is in [Preview](https://cloud.google.com/products/#product-launch-stages).

## January 20, 2026

Feature

Pub/Sub is now available in the Bangkok region (`asia-southeast3`). For more information, see [Cloud locations](https://cloud.google.com/about/locations).

## December 29, 2025

Libraries

### Java

#### [1.144.1](https://github.com/googleapis/java-pubsub/compare/v1.144.0...v1.144.1) (2025-12-22)

##### Bug Fixes

  * Lower the Subscriber protocol version to disable the streaming pull keepalive feature ([#2652](https://github.com/googleapis/java-pubsub/issues/2652)) ([ca99c2a](https://github.com/googleapis/java-pubsub/commit/ca99c2a2cea8201ea6f71e7383bd6123ec32ebdc))



## December 22, 2025

Libraries

### Python

#### [2.34.0](https://github.com/googleapis/python-pubsub/compare/v2.33.0...v2.34.0) (2025-12-16)

##### Features

  * support mTLS certificates when available (#1566) ([24761a2f](https://github.com/googleapis/python-pubsub/commit/24761a2f))



### Java

#### [1.145.0-rc1](https://github.com/googleapis/java-pubsub/compare/v1.144.0...v1.145.0-rc1) (2025-12-16)

##### Features

  * [java] allow passing libraries_bom_version from env ([#1967](https://github.com/googleapis/java-pubsub/issues/1967)) ([#2033](https://github.com/googleapis/java-pubsub/issues/2033)) ([825c5f8](https://github.com/googleapis/java-pubsub/commit/825c5f83e0fd2fd6b1f4856b9c555d71110a03e1))
  * Add IngestionFailureEvent to the external proto ([6c67798](https://github.com/googleapis/java-pubsub/commit/6c67798c6b7442d77eb30fbba874344f32a926b4))
  * Add Kafka-based sources to IngestionDataSourceSettings proto and IngestionFailureEvent proto ([2947169](https://github.com/googleapis/java-pubsub/commit/2947169c009fa553202bc1e44276cf5a7954cd96))
  * add keepalive feature to tear down streams in their absence ([#2605](https://github.com/googleapis/java-pubsub/issues/2605)) ([99aca4f](https://github.com/googleapis/java-pubsub/commit/99aca4f3fd1792b02da78320bed39e53dc8af23c))
  * Add MessageTransformationFailureReason to IngestionFailureEvent ([8271399](https://github.com/googleapis/java-pubsub/commit/8271399cc6348f69ba034b676cce2aa7592122a4))
  * Add OpenTelemetry tracing to the Publisher and Subscriber ([#2086](https://github.com/googleapis/java-pubsub/issues/2086)) ([db522b6](https://github.com/googleapis/java-pubsub/commit/db522b60f1bbec9cc1bfa0c37477044fd2f807c7))
  * Add SchemaViolationReason to IngestionFailureEvent ([21cc376](https://github.com/googleapis/java-pubsub/commit/21cc3764aaa6fc05eb4a5078a72dae30694fba91))
  * add service_account_email for export subscriptions ([#2054](https://github.com/googleapis/java-pubsub/issues/2054)) ([670db3e](https://github.com/googleapis/java-pubsub/commit/670db3e1b665e6f5aec3cd7bf3639e9242f20151))
  * add support for message transforms to Topic and Subscription ([3889a05](https://github.com/googleapis/java-pubsub/commit/3889a05a5c5d7479d3cc6b6dc0b0c425d41efd5d))
  * add use_topic_schema for Cloud Storage Subscriptions ([#2082](https://github.com/googleapis/java-pubsub/issues/2082)) ([11d67d4](https://github.com/googleapis/java-pubsub/commit/11d67d44152ccca008dda071683d9932c59af41d))
  * Annotate some resource fields with their corresponding API types ([ab60afa](https://github.com/googleapis/java-pubsub/commit/ab60afa012bd3fc81977ba24c416205ce9280943))
  * deprecate `enabled` field for message transforms and add `disabled` field ([76b2a3d](https://github.com/googleapis/java-pubsub/commit/76b2a3dc1f001dfeb3f8974a4cc4de843b7383bc))
  * enable hermetic library generation ([#2048](https://github.com/googleapis/java-pubsub/issues/2048)) ([283a5e8](https://github.com/googleapis/java-pubsub/commit/283a5e89837071678f8dd94b8b8adfad91a6766c))
  * generate renamed go pubsub admin clients ([4472d7b](https://github.com/googleapis/java-pubsub/commit/4472d7baff4894a7c5cf0efc7eadd83ec8801d7a))
  * Implement SubscriberShutdownSettings ([#2569](https://github.com/googleapis/java-pubsub/issues/2569)) ([8195f6f](https://github.com/googleapis/java-pubsub/commit/8195f6fd3bbd33a178535994a94a79822ae2d4d6))
  * introduce `java.time` variables and methods ([#2271](https://github.com/googleapis/java-pubsub/issues/2271)) ([7edfd9c](https://github.com/googleapis/java-pubsub/commit/7edfd9c315405c7703509fb9b7bc4f0d2686d870))
  * next release from main branch is 1.138.0 ([#2361](https://github.com/googleapis/java-pubsub/issues/2361)) ([b6ba56c](https://github.com/googleapis/java-pubsub/commit/b6ba56c04619660d2660a660eaacbda7de9f8608))
  * next release from main branch is 1.141.0 ([#2481](https://github.com/googleapis/java-pubsub/issues/2481)) ([bd9f385](https://github.com/googleapis/java-pubsub/commit/bd9f3850efa77ce759b4f281aecd9645666cb0f7))
  * support the protocol version in StreamingPullRequest ([af40810](https://github.com/googleapis/java-pubsub/commit/af40810ea0668ce4e8c4d69bdbb4b281073976d0))
  * track batch size using serialized size of PublishRequest ([#2113](https://github.com/googleapis/java-pubsub/issues/2113)) ([be78e64](https://github.com/googleapis/java-pubsub/commit/be78e64f9fdfc9ddf0790189311fac673754e219))
  * update with latest from main ([#2644](https://github.com/googleapis/java-pubsub/issues/2644)) ([96513b2](https://github.com/googleapis/java-pubsub/commit/96513b2382813847882dc9928cfaf7ceea481074))
  * Upgrade protobuf gen code to 4.33 ([#2645](https://github.com/googleapis/java-pubsub/issues/2645)) ([db3c75f](https://github.com/googleapis/java-pubsub/commit/db3c75f9ea3e905b5423b2d5b2bb1e67f30343bc))



##### Bug Fixes

  * Add retries for ack and modack operations that don't return with a metadata map ([#2385](https://github.com/googleapis/java-pubsub/issues/2385)) ([00070b7](https://github.com/googleapis/java-pubsub/commit/00070b74e54fcb62b91a4d72a88d3b20b2425a94))
  * Deflake WaiterTest ([#2600](https://github.com/googleapis/java-pubsub/issues/2600)) ([298c8db](https://github.com/googleapis/java-pubsub/commit/298c8db04616341da040935636b1a04ce5f022a0))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.47.0 ([ccd23af](https://github.com/googleapis/java-pubsub/commit/ccd23afd99e7cb5a28747b06d0a97d1cb8163391))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.49.0 ([77546e0](https://github.com/googleapis/java-pubsub/commit/77546e0548e72e331523fb4f30edd1577b5fe6ea))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.50.0 ([3f21af3](https://github.com/googleapis/java-pubsub/commit/3f21af3e3fbc6ef49ecbe80712350d8712133c59))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.51.0 ([0b0d52c](https://github.com/googleapis/java-pubsub/commit/0b0d52c8fca179a913a8b04d76b44748f1886f45))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.51.1 ([9c166f7](https://github.com/googleapis/java-pubsub/commit/9c166f76db78b0c6b2e0218460d5c0336102717a))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.52.0 ([0d8c8bf](https://github.com/googleapis/java-pubsub/commit/0d8c8bffc85804d5a64ec0d35893ad9e0062807e))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.53.0 ([b952e58](https://github.com/googleapis/java-pubsub/commit/b952e5826748bc680936a79b14d75f5873e6db06))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.54.0 ([ccf670f](https://github.com/googleapis/java-pubsub/commit/ccf670f9dc755770d40b9d1bf2c870c0452aa39e))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.55.1 ([76b2a3d](https://github.com/googleapis/java-pubsub/commit/76b2a3dc1f001dfeb3f8974a4cc4de843b7383bc))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.56.2 ([4472d7b](https://github.com/googleapis/java-pubsub/commit/4472d7baff4894a7c5cf0efc7eadd83ec8801d7a))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.56.3 ([2b928a8](https://github.com/googleapis/java-pubsub/commit/2b928a8a946ebf84470bd2e2bb064b52c4f11ea2))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.57.0 ([017eb0f](https://github.com/googleapis/java-pubsub/commit/017eb0f78423fde3edd42a07677df49512085633))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.58.0 ([3713edb](https://github.com/googleapis/java-pubsub/commit/3713edb9420f792b7c7ad4e430ca05b5942656ff))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.59.0 ([0eece50](https://github.com/googleapis/java-pubsub/commit/0eece5012fbaf887a5c062beba433dbb30edbf43))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.60.1 ([c9ef2cd](https://github.com/googleapis/java-pubsub/commit/c9ef2cda2c6ad20d5e57fe3ccf69f845f7ef36b7))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.60.2 ([7afae21](https://github.com/googleapis/java-pubsub/commit/7afae21e5e3df16742646363ca199ec14c42bc21))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.61.0 ([42eb599](https://github.com/googleapis/java-pubsub/commit/42eb5992557457a5ae4512334267113266c220ac))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.0 ([65e324e](https://github.com/googleapis/java-pubsub/commit/65e324e11b74e8cf78534dea2e5835c1d5f24506))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.1 ([ac08d5f](https://github.com/googleapis/java-pubsub/commit/ac08d5f6ead8071ab0e068e32fd5ae0ae2731c34))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.2 ([c02d304](https://github.com/googleapis/java-pubsub/commit/c02d304f5213410eda5f26fe98c96a5c1d4bf9d8))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.62.3 ([af40810](https://github.com/googleapis/java-pubsub/commit/af40810ea0668ce4e8c4d69bdbb4b281073976d0))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.63.0 ([ab60afa](https://github.com/googleapis/java-pubsub/commit/ab60afa012bd3fc81977ba24c416205ce9280943))
  * **deps:** update the Java code generator (gapic-generator-java) to 2.64.1 ([b210251](https://github.com/googleapis/java-pubsub/commit/b2102516bf833c2704c85cb348b67bb7cbfdb3a6))
  * next release candidate ([cf06e2d](https://github.com/googleapis/java-pubsub/commit/cf06e2da4317d3ffa965e0a33be5c0769cda84f7))
  * Prevent excessive string parsing when publishing and receiving messages to improve performance ([#2317](https://github.com/googleapis/java-pubsub/issues/2317)) ([07b1350](https://github.com/googleapis/java-pubsub/commit/07b135001b4726c9bafafe90c80d369f25f04956))
  * Remove element_count_limit and request_byte_limit from pubsub_gapic.yaml ([7afae21](https://github.com/googleapis/java-pubsub/commit/7afae21e5e3df16742646363ca199ec14c42bc21))
  * Update .OwlBot-hermetic.yaml to preserve SubscriberShutdownSettings files ([#2583](https://github.com/googleapis/java-pubsub/issues/2583)) ([f3cf5e7](https://github.com/googleapis/java-pubsub/commit/f3cf5e725c12173ade0275fd0526885309dc553a))
  * Use a separate cached thread pool for handling ack and modack response callback for EOD-enabled subscriptions ([#2505](https://github.com/googleapis/java-pubsub/issues/2505)) ([224c269](https://github.com/googleapis/java-pubsub/commit/224c269e3bd0ae4cfc4b24ac85495911b8e2b90c))
  * Use the system executor instead of a separate thread pool for EOD ack/modack callbacks ([#2526](https://github.com/googleapis/java-pubsub/issues/2526)) ([ffeb017](https://github.com/googleapis/java-pubsub/commit/ffeb017a58ca486688105738f180d70df33a74de))



##### Dependencies

  * Change scope of grpc-inprocess dependency from runtime to test ([#2038](https://github.com/googleapis/java-pubsub/issues/2038)) ([1ab45c9](https://github.com/googleapis/java-pubsub/commit/1ab45c9eaee35d4bfeb332244c74f1253b77c166))
  * Remove OpenTelemetry semconv dependency ([#2611](https://github.com/googleapis/java-pubsub/issues/2611)) ([240fc37](https://github.com/googleapis/java-pubsub/commit/240fc3784db3860eb2668946fbf861beed2647d7))
  * update actions/checkout action to v5 ([#2520](https://github.com/googleapis/java-pubsub/issues/2520)) ([409398a](https://github.com/googleapis/java-pubsub/commit/409398a40f71866d5a84b4542d582777ee240a08))
  * update actions/checkout action to v5 ([#2531](https://github.com/googleapis/java-pubsub/issues/2531)) ([f687f11](https://github.com/googleapis/java-pubsub/commit/f687f117fc435ee8b1f15b8802ecc989f1e2747e))
  * update actions/checkout action to v5 ([#2539](https://github.com/googleapis/java-pubsub/issues/2539)) ([83144e6](https://github.com/googleapis/java-pubsub/commit/83144e6d4110fbe15f4357270a292cfcbcc35dd6))
  * update actions/checkout action to v5 ([#2562](https://github.com/googleapis/java-pubsub/issues/2562)) ([b7fa499](https://github.com/googleapis/java-pubsub/commit/b7fa49968e85dfeba8a84ea29f8ddf9d33ef22c5))
  * update actions/checkout action to v5 ([#2573](https://github.com/googleapis/java-pubsub/issues/2573)) ([4153dba](https://github.com/googleapis/java-pubsub/commit/4153dbacb386b130780c8d1e5596e3502af8e32b))
  * update actions/checkout action to v5 ([#2576](https://github.com/googleapis/java-pubsub/issues/2576)) ([1375f6d](https://github.com/googleapis/java-pubsub/commit/1375f6d9a71c78d973a71f1df449640a95bc0bc7))
  * update actions/checkout action to v5 ([#2584](https://github.com/googleapis/java-pubsub/issues/2584)) ([25059ce](https://github.com/googleapis/java-pubsub/commit/25059ce001e3273fcec9d1c40e3b09c89ddf487e))
  * update actions/checkout action to v5 ([#2592](https://github.com/googleapis/java-pubsub/issues/2592)) ([6ca466d](https://github.com/googleapis/java-pubsub/commit/6ca466d382ddde9780ae1c8627092d731e314f90))
  * update actions/checkout action to v5 ([#2613](https://github.com/googleapis/java-pubsub/issues/2613)) ([a69ffdd](https://github.com/googleapis/java-pubsub/commit/a69ffdd9ecb5dae557a847ae7ec5c1a06431bef7))
  * update actions/github-script action to v8 ([#2542](https://github.com/googleapis/java-pubsub/issues/2542)) ([0e6f0da](https://github.com/googleapis/java-pubsub/commit/0e6f0daccfdca248b3b80ef7dfb0bd7a4baa607c))
  * update actions/setup-java action to v5 ([#2535](https://github.com/googleapis/java-pubsub/issues/2535)) ([2ed87d2](https://github.com/googleapis/java-pubsub/commit/2ed87d2b7e28af99cfda00b4b69fb5cb2f448584))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.40.1 ([#2021](https://github.com/googleapis/java-pubsub/issues/2021)) ([0873594](https://github.com/googleapis/java-pubsub/commit/0873594c000f470c6193ebe8b4d091701670ef06))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.40.2 ([#2046](https://github.com/googleapis/java-pubsub/issues/2046)) ([f81c5e1](https://github.com/googleapis/java-pubsub/commit/f81c5e1b977e6da19aac6a40c1389ddcc4643e3c))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.40.3 ([#2071](https://github.com/googleapis/java-pubsub/issues/2071)) ([0844bfb](https://github.com/googleapis/java-pubsub/commit/0844bfb0a500ae0b4a0f63fcb45ffffeaf609e3d))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.41.0 ([#2093](https://github.com/googleapis/java-pubsub/issues/2093)) ([217b8a3](https://github.com/googleapis/java-pubsub/commit/217b8a3f5419f80402d349b8873d7302eeb35e3f))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.42.0 ([#2124](https://github.com/googleapis/java-pubsub/issues/2124)) ([24ebe24](https://github.com/googleapis/java-pubsub/commit/24ebe2402fe6278348d87b5a4259c365a819877f))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.42.1 ([#2152](https://github.com/googleapis/java-pubsub/issues/2152)) ([1457489](https://github.com/googleapis/java-pubsub/commit/1457489cb51c12bc7ad8ab8ddcf2252a2f513a79))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.42.2 ([#2157](https://github.com/googleapis/java-pubsub/issues/2157)) ([d671347](https://github.com/googleapis/java-pubsub/commit/d671347004a68c53cdf3fdfb9d1a7ed992ee162f))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.42.3 ([#2173](https://github.com/googleapis/java-pubsub/issues/2173)) ([294d039](https://github.com/googleapis/java-pubsub/commit/294d03974ab236c2ee5d0e420e8913eb6fc65fc9))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.43.1 ([#2202](https://github.com/googleapis/java-pubsub/issues/2202)) ([acaf5f2](https://github.com/googleapis/java-pubsub/commit/acaf5f2e3686a939d4b972c73a4d039142f753df))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.43.3 ([#2256](https://github.com/googleapis/java-pubsub/issues/2256)) ([f7fbc6c](https://github.com/googleapis/java-pubsub/commit/f7fbc6c7e4f7d8a8b31d4778d2cd8c55efcb9be1))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.44.0 ([#2270](https://github.com/googleapis/java-pubsub/issues/2270)) ([a5f70a9](https://github.com/googleapis/java-pubsub/commit/a5f70a9c2397a2c8f4642729922b742a3df01ed6))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.45.0 ([#2292](https://github.com/googleapis/java-pubsub/issues/2292)) ([79a8982](https://github.com/googleapis/java-pubsub/commit/79a89823c6cbcc9a718f44856040b1525863cab6))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.46.0 ([#2309](https://github.com/googleapis/java-pubsub/issues/2309)) ([97bd44e](https://github.com/googleapis/java-pubsub/commit/97bd44e04c440320e45c2b4336677d8d266a39a2))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.47.0 ([#2331](https://github.com/googleapis/java-pubsub/issues/2331)) ([216feef](https://github.com/googleapis/java-pubsub/commit/216feef976595cd03e282f8d8effa2ac8430c419))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.48.0 ([#2343](https://github.com/googleapis/java-pubsub/issues/2343)) ([3bbd7e1](https://github.com/googleapis/java-pubsub/commit/3bbd7e1e812a7a00cfff36a0c1d8a5212d4e134a))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.48.1 ([#2356](https://github.com/googleapis/java-pubsub/issues/2356)) ([7d3d2e4](https://github.com/googleapis/java-pubsub/commit/7d3d2e4690539ebbe7ab521c2c345b06cba766ea))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.49.0 ([#2380](https://github.com/googleapis/java-pubsub/issues/2380)) ([405e485](https://github.com/googleapis/java-pubsub/commit/405e485bbe503357a0616ec72de8fea00cb91c9c))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.49.2 ([#2399](https://github.com/googleapis/java-pubsub/issues/2399)) ([ff48708](https://github.com/googleapis/java-pubsub/commit/ff4870815864a6216a1ce4b606fcec3df7f58fd4))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.50.0 ([#2422](https://github.com/googleapis/java-pubsub/issues/2422)) ([993b2d0](https://github.com/googleapis/java-pubsub/commit/993b2d06ce6b45bb72faa9d6959cddc14a9cf60e))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.50.1 ([#2435](https://github.com/googleapis/java-pubsub/issues/2435)) ([b37c557](https://github.com/googleapis/java-pubsub/commit/b37c5573e1d0d7eada4ce4ec6a052521ea11cff1))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.51.0 ([#2457](https://github.com/googleapis/java-pubsub/issues/2457)) ([d74215a](https://github.com/googleapis/java-pubsub/commit/d74215a6f1e641ba75997e2e43bef348fb9c4a3c))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.52.0 ([#2467](https://github.com/googleapis/java-pubsub/issues/2467)) ([fe08a6f](https://github.com/googleapis/java-pubsub/commit/fe08a6f1f6ee18e97c752f82786016999f6ab12c))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.53.0 ([#2489](https://github.com/googleapis/java-pubsub/issues/2489)) ([5a454b9](https://github.com/googleapis/java-pubsub/commit/5a454b9c36419dcfaf79edb1ec1d066b20836f87))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.54.0 ([#2506](https://github.com/googleapis/java-pubsub/issues/2506)) ([6bf8e62](https://github.com/googleapis/java-pubsub/commit/6bf8e62b1144568292e832dc8031a70a2c5b9ad7))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.54.1 ([#2523](https://github.com/googleapis/java-pubsub/issues/2523)) ([0678a74](https://github.com/googleapis/java-pubsub/commit/0678a74dc22f73cd8ec8c4893c1a8dd60449b128))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.54.2 ([#2538](https://github.com/googleapis/java-pubsub/issues/2538)) ([10a8283](https://github.com/googleapis/java-pubsub/commit/10a8283292e58b0c73b9c57ff36ddd71b8b83467))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.55.0 ([#2553](https://github.com/googleapis/java-pubsub/issues/2553)) ([15b9e66](https://github.com/googleapis/java-pubsub/commit/15b9e66f27cd6e57b808b96f3e15f08b1f0d7727))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.55.1 ([#2566](https://github.com/googleapis/java-pubsub/issues/2566)) ([66c9ec4](https://github.com/googleapis/java-pubsub/commit/66c9ec4a26b76ca384dce71a8ab6bce8cd34b8a3))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.55.2 ([#2582](https://github.com/googleapis/java-pubsub/issues/2582)) ([d0f9673](https://github.com/googleapis/java-pubsub/commit/d0f96737a74453c3db54ee59e98d4b6636cd55d4))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.55.3 ([#2602](https://github.com/googleapis/java-pubsub/issues/2602)) ([d14106c](https://github.com/googleapis/java-pubsub/commit/d14106cc278c98d3f954f959e2dd3764ebd20fc2))
  * update dependency com.google.cloud:google-cloud-core to v2.38.1 ([#2027](https://github.com/googleapis/java-pubsub/issues/2027)) ([535edf6](https://github.com/googleapis/java-pubsub/commit/535edf6496700bc5c5fb0b5cfa1cac6be5d62875))
  * update dependency com.google.cloud:google-cloud-core to v2.39.0 ([#2057](https://github.com/googleapis/java-pubsub/issues/2057)) ([43446d2](https://github.com/googleapis/java-pubsub/commit/43446d22ad2140f1b18fd1dde5dab03a901580bc))
  * update dependency com.google.cloud:google-cloud-core to v2.40.0 ([#2087](https://github.com/googleapis/java-pubsub/issues/2087)) ([26b01c9](https://github.com/googleapis/java-pubsub/commit/26b01c921f2700947a1653702be0234cf84cccef))
  * update dependency com.google.cloud:google-cloud-core to v2.41.0 ([#2120](https://github.com/googleapis/java-pubsub/issues/2120)) ([1f6428a](https://github.com/googleapis/java-pubsub/commit/1f6428a8b79369a239664b9ea7cd38e024db9724))
  * update dependency com.google.cloud:google-cloud-core to v2.42.0 ([#2140](https://github.com/googleapis/java-pubsub/issues/2140)) ([80dca35](https://github.com/googleapis/java-pubsub/commit/80dca35cebb1061f3d2a852ff9929519e69283cc))
  * update dependency com.google.cloud:google-cloud-core to v2.43.0 ([#2161](https://github.com/googleapis/java-pubsub/issues/2161)) ([05a37b7](https://github.com/googleapis/java-pubsub/commit/05a37b786686c24f87eec5e9919c16b2b67465be))
  * update dependency com.google.cloud:google-cloud-core to v2.44.0 ([#2184](https://github.com/googleapis/java-pubsub/issues/2184)) ([faecb3b](https://github.com/googleapis/java-pubsub/commit/faecb3b90cb259ae376b8481ec30511ce19279bf))
  * update dependency com.google.cloud:google-cloud-core to v2.44.1 ([#2190](https://github.com/googleapis/java-pubsub/issues/2190)) ([9ea45dc](https://github.com/googleapis/java-pubsub/commit/9ea45dc13f11076890cfff35e7acf2eafc2af70a))
  * update dependency com.google.cloud:google-cloud-core to v2.45.0 ([#2213](https://github.com/googleapis/java-pubsub/issues/2213)) ([5ee969b](https://github.com/googleapis/java-pubsub/commit/5ee969bb9ed873073895881062ec72f419bbc837))
  * update dependency com.google.cloud:google-cloud-core to v2.46.0 ([#2238](https://github.com/googleapis/java-pubsub/issues/2238)) ([dc06d54](https://github.com/googleapis/java-pubsub/commit/dc06d5456ab6fe8d94b7b845ca9159391949517f))
  * update dependency com.google.cloud:google-cloud-core to v2.47.0 ([#2249](https://github.com/googleapis/java-pubsub/issues/2249)) ([3df5729](https://github.com/googleapis/java-pubsub/commit/3df572918523738e8f2f28299efa811aa23e297b))
  * update dependency com.google.cloud:google-cloud-core to v2.48.0 ([#2263](https://github.com/googleapis/java-pubsub/issues/2263)) ([d7e5588](https://github.com/googleapis/java-pubsub/commit/d7e55886b62826f54f0bb12a6bfa4ef67dee6521))
  * update dependency com.google.cloud:google-cloud-core to v2.49.0 ([#2285](https://github.com/googleapis/java-pubsub/issues/2285)) ([cd94a19](https://github.com/googleapis/java-pubsub/commit/cd94a1987271eea4d7744286a7daeb071bb9456a))
  * update dependency com.google.cloud:google-cloud-core to v2.49.1 ([#2300](https://github.com/googleapis/java-pubsub/issues/2300)) ([cf2822b](https://github.com/googleapis/java-pubsub/commit/cf2822b7363e13e4730753cbb5ca3510c77f5f55))
  * update dependency com.google.cloud:google-cloud-core to v2.50.0 ([#2321](https://github.com/googleapis/java-pubsub/issues/2321)) ([5c40bcd](https://github.com/googleapis/java-pubsub/commit/5c40bcd4d401d919b990e6a7d3151660ead76eb0))
  * update dependency com.google.cloud:google-cloud-core to v2.51.0 ([#2338](https://github.com/googleapis/java-pubsub/issues/2338)) ([ac2403e](https://github.com/googleapis/java-pubsub/commit/ac2403ecd21aad0d44c5b06fce2853f9a433adbd))
  * update dependency com.google.cloud:google-cloud-core to v2.52.0 ([#2348](https://github.com/googleapis/java-pubsub/issues/2348)) ([f0977b4](https://github.com/googleapis/java-pubsub/commit/f0977b40479823ce5b7e90f864261f11115610ca))
  * update dependency com.google.cloud:google-cloud-core to v2.53.1 ([#2365](https://github.com/googleapis/java-pubsub/issues/2365)) ([748058f](https://github.com/googleapis/java-pubsub/commit/748058fc018e3a36dedd576404037bf8c016c794))
  * update dependency com.google.cloud:google-cloud-core to v2.54.3 ([#2393](https://github.com/googleapis/java-pubsub/issues/2393)) ([0ffa26a](https://github.com/googleapis/java-pubsub/commit/0ffa26ac3abceabcfba5d57cdb36f27f5a164ce3))
  * update dependency com.google.cloud:google-cloud-core to v2.55.0 ([#2413](https://github.com/googleapis/java-pubsub/issues/2413)) ([3e181e7](https://github.com/googleapis/java-pubsub/commit/3e181e7c4469eadcf6f148ee0a30aae1cfa825f3))
  * update dependency com.google.cloud:google-cloud-core to v2.56.0 ([#2427](https://github.com/googleapis/java-pubsub/issues/2427)) ([b2a3e35](https://github.com/googleapis/java-pubsub/commit/b2a3e35ced2d1715c37207f98740889635326dc1))
  * update dependency com.google.cloud:google-cloud-core to v2.58.0 ([#2443](https://github.com/googleapis/java-pubsub/issues/2443)) ([d4599d9](https://github.com/googleapis/java-pubsub/commit/d4599d93b780b6ef20ad44582aeb8c1cd35f99d4))
  * update dependency com.google.cloud:google-cloud-core to v2.58.1 ([#2476](https://github.com/googleapis/java-pubsub/issues/2476)) ([96a2354](https://github.com/googleapis/java-pubsub/commit/96a23544fce609c7b19a00638a767926c304d3f8))
  * update dependency com.google.cloud:google-cloud-core to v2.58.2 ([#2493](https://github.com/googleapis/java-pubsub/issues/2493)) ([9a1c17e](https://github.com/googleapis/java-pubsub/commit/9a1c17e50e5fc9a807532d289a7f6e8b5d412f59))
  * update dependency com.google.cloud:google-cloud-core to v2.59.0 ([#2507](https://github.com/googleapis/java-pubsub/issues/2507)) ([070cf07](https://github.com/googleapis/java-pubsub/commit/070cf07b1d529c34d4f633b37ce1d35d14768325))
  * update dependency com.google.cloud:google-cloud-core to v2.60.0 ([#2527](https://github.com/googleapis/java-pubsub/issues/2527)) ([0166e21](https://github.com/googleapis/java-pubsub/commit/0166e21012f0bc2ccb2e832d6f27e60ad3382456))
  * update dependency com.google.cloud:google-cloud-core to v2.60.1 ([#2543](https://github.com/googleapis/java-pubsub/issues/2543)) ([fbb45ce](https://github.com/googleapis/java-pubsub/commit/fbb45cee9e3740f8ac94b5fbaa65b97b8db09b1e))
  * update dependency com.google.cloud:google-cloud-core to v2.60.2 ([#2557](https://github.com/googleapis/java-pubsub/issues/2557)) ([460bcd9](https://github.com/googleapis/java-pubsub/commit/460bcd9158e7058f710f43200b7b7737eb47839c))
  * update dependency com.google.cloud:google-cloud-core to v2.60.3 ([#2571](https://github.com/googleapis/java-pubsub/issues/2571)) ([ac2c85a](https://github.com/googleapis/java-pubsub/commit/ac2c85ad62525aee236af54f6b5c9b1eacf4d22a))
  * update dependency com.google.cloud:google-cloud-core to v2.61.0 ([#2588](https://github.com/googleapis/java-pubsub/issues/2588)) ([244cf75](https://github.com/googleapis/java-pubsub/commit/244cf758bf46f8431a17b1d8e76d1d90c494fc76))
  * update dependency com.google.cloud:google-cloud-core to v2.62.1 ([#2608](https://github.com/googleapis/java-pubsub/issues/2608)) ([fee0500](https://github.com/googleapis/java-pubsub/commit/fee0500bf6a0e309ca5f162810e22a2ca4c5b7eb))
  * update dependency com.google.cloud:google-cloud-storage to v2.39.0 ([#2040](https://github.com/googleapis/java-pubsub/issues/2040)) ([eb6bd9c](https://github.com/googleapis/java-pubsub/commit/eb6bd9c559073429d8338b9d8fa83e0e3f61b8e9))
  * update dependency com.google.cloud:google-cloud-storage to v2.40.0 ([#2066](https://github.com/googleapis/java-pubsub/issues/2066)) ([dfcaeb5](https://github.com/googleapis/java-pubsub/commit/dfcaeb5b59466d86ac5b5bf74655ce359e7d5713))
  * update dependency com.google.cloud:google-cloud-storage to v2.40.1 ([#2095](https://github.com/googleapis/java-pubsub/issues/2095)) ([0d64d6c](https://github.com/googleapis/java-pubsub/commit/0d64d6cf7799a176297ceaa1475b7cb29a64bebc))
  * update dependency com.google.cloud:google-cloud-storage to v2.41.0 ([#2129](https://github.com/googleapis/java-pubsub/issues/2129)) ([2348d20](https://github.com/googleapis/java-pubsub/commit/2348d2022bc400b7f187d3db7f43aff94d8884a8))
  * update dependency com.google.cloud:google-cloud-storage to v2.42.0 ([#2145](https://github.com/googleapis/java-pubsub/issues/2145)) ([77c3e78](https://github.com/googleapis/java-pubsub/commit/77c3e78d34e894c05653371027cd2b1d12cea9d0))
  * update dependency com.google.cloud:google-cloud-storage to v2.43.0 ([#2174](https://github.com/googleapis/java-pubsub/issues/2174)) ([ae800d7](https://github.com/googleapis/java-pubsub/commit/ae800d7b3ffd19302b416f03fad8b20e93afce8f))
  * update dependency com.google.cloud:google-cloud-storage to v2.43.1 ([#2194](https://github.com/googleapis/java-pubsub/issues/2194)) ([979e420](https://github.com/googleapis/java-pubsub/commit/979e420377327cf3843ac23151d8b44a7e5188c5))
  * update dependency com.google.cloud:google-cloud-storage to v2.43.2 ([#2226](https://github.com/googleapis/java-pubsub/issues/2226)) ([eb87c04](https://github.com/googleapis/java-pubsub/commit/eb87c04619f7bdaf59ce2b562a96b8c25d3c8196))
  * update dependency com.google.cloud:google-cloud-storage to v2.44.1 ([#2240](https://github.com/googleapis/java-pubsub/issues/2240)) ([f8dae4d](https://github.com/googleapis/java-pubsub/commit/f8dae4d68c1835930d4e39522a354cdfcc4cdd84))
  * update dependency com.google.cloud:google-cloud-storage to v2.45.0 ([#2268](https://github.com/googleapis/java-pubsub/issues/2268)) ([80a09e6](https://github.com/googleapis/java-pubsub/commit/80a09e69111229080c413eff8426bd0b3d50458d))
  * update dependency com.google.cloud:google-cloud-storage to v2.46.0 ([#2291](https://github.com/googleapis/java-pubsub/issues/2291)) ([7b60884](https://github.com/googleapis/java-pubsub/commit/7b60884cc4e17df616155f7530a056c4c5e3af29))
  * update dependency com.google.cloud:google-cloud-storage to v2.47.0 ([#2303](https://github.com/googleapis/java-pubsub/issues/2303)) ([707f842](https://github.com/googleapis/java-pubsub/commit/707f84271559dfe96fa11edffb307df145ceea47))
  * update dependency com.google.cloud:google-cloud-storage to v2.48.0 ([#2322](https://github.com/googleapis/java-pubsub/issues/2322)) ([93b9419](https://github.com/googleapis/java-pubsub/commit/93b9419d210cedeab03f408dab4c74c9fcf18b59))
  * update dependency com.google.cloud:google-cloud-storage to v2.48.1 ([#2332](https://github.com/googleapis/java-pubsub/issues/2332)) ([23fd7a8](https://github.com/googleapis/java-pubsub/commit/23fd7a8f4ab2438b72f3a6da5613f5deb0ac307e))
  * update dependency com.google.cloud:google-cloud-storage to v2.48.2 ([#2341](https://github.com/googleapis/java-pubsub/issues/2341)) ([eeb99a9](https://github.com/googleapis/java-pubsub/commit/eeb99a997fa2e7154dcc228b964ff47867738122))
  * update dependency com.google.cloud:google-cloud-storage to v2.49.0 ([#2358](https://github.com/googleapis/java-pubsub/issues/2358)) ([81d3435](https://github.com/googleapis/java-pubsub/commit/81d34352d332ee9c4935e7908b6b9a2383d3a8ba))
  * update dependency com.google.cloud:google-cloud-storage to v2.50.0 ([#2372](https://github.com/googleapis/java-pubsub/issues/2372)) ([b81164a](https://github.com/googleapis/java-pubsub/commit/b81164aa5682c8046ebfa44e1e47579e4c3fcd28))
  * update dependency com.google.cloud:google-cloud-storage to v2.52.1 ([#2396](https://github.com/googleapis/java-pubsub/issues/2396)) ([283a6e1](https://github.com/googleapis/java-pubsub/commit/283a6e14f61764c210ed23f4ada23ad21bbdb306))
  * update dependency com.google.cloud:google-cloud-storage to v2.52.2 ([#2421](https://github.com/googleapis/java-pubsub/issues/2421)) ([1224ee5](https://github.com/googleapis/java-pubsub/commit/1224ee51da27e447560076b0d51ba90515566bd9))
  * update dependency com.google.cloud:google-cloud-storage to v2.52.3 ([#2436](https://github.com/googleapis/java-pubsub/issues/2436)) ([4f309d1](https://github.com/googleapis/java-pubsub/commit/4f309d151d4bd584a33a0bb8882d0614a1b9d533))
  * update dependency com.google.cloud:google-cloud-storage to v2.53.1 ([#2452](https://github.com/googleapis/java-pubsub/issues/2452)) ([b4af237](https://github.com/googleapis/java-pubsub/commit/b4af2370bb875ee8d0047f67a72e8c6d62547a12))
  * update dependency com.google.cloud:google-cloud-storage to v2.53.2 ([#2469](https://github.com/googleapis/java-pubsub/issues/2469)) ([fa51a01](https://github.com/googleapis/java-pubsub/commit/fa51a01ed39393b7cad25fb39a1c87099def830a))
  * update dependency com.google.cloud:google-cloud-storage to v2.53.3 ([#2486](https://github.com/googleapis/java-pubsub/issues/2486)) ([9416cc9](https://github.com/googleapis/java-pubsub/commit/9416cc99f826b80412b0e5eba0068a35b82390c6))
  * update dependency com.google.cloud:google-cloud-storage to v2.54.0 ([#2510](https://github.com/googleapis/java-pubsub/issues/2510)) ([0fd589e](https://github.com/googleapis/java-pubsub/commit/0fd589e2ee80730b442f569b770fe16208feb4ba))
  * update dependency com.google.cloud:google-cloud-storage to v2.55.0 ([#2517](https://github.com/googleapis/java-pubsub/issues/2517)) ([b67acf1](https://github.com/googleapis/java-pubsub/commit/b67acf1294249be308568f49f287897ae55ced08))
  * update dependency com.google.cloud:google-cloud-storage to v2.56.0 ([#2536](https://github.com/googleapis/java-pubsub/issues/2536)) ([80d9ca1](https://github.com/googleapis/java-pubsub/commit/80d9ca10d3a2656852422858f032bb6629102cfb))
  * update dependency com.google.cloud:google-cloud-storage to v2.57.0 ([#2547](https://github.com/googleapis/java-pubsub/issues/2547)) ([133f8c7](https://github.com/googleapis/java-pubsub/commit/133f8c7995880c2d1e75b69d61c50254d4f9fede))
  * update dependency com.google.cloud:google-cloud-storage to v2.58.0 ([#2561](https://github.com/googleapis/java-pubsub/issues/2561)) ([0189388](https://github.com/googleapis/java-pubsub/commit/0189388edb4d618d65f33718922ca1b11f71cb15))
  * update dependency com.google.cloud:google-cloud-storage to v2.58.1 ([#2580](https://github.com/googleapis/java-pubsub/issues/2580)) ([d156cdb](https://github.com/googleapis/java-pubsub/commit/d156cdb27a8d68b6fa8c97f558df7088e6634320))
  * update dependency com.google.cloud:google-cloud-storage to v2.59.0 ([#2603](https://github.com/googleapis/java-pubsub/issues/2603)) ([d9d05bf](https://github.com/googleapis/java-pubsub/commit/d9d05bfa18580cdacdfa9378d30b56ce0ae0d4d2))
  * update dependency com.google.cloud:google-cloud-storage to v2.60.0 ([#2610](https://github.com/googleapis/java-pubsub/issues/2610)) ([1cae247](https://github.com/googleapis/java-pubsub/commit/1cae247322fff1b6588a4b523e601e41a4284c64))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.30.1 ([#2028](https://github.com/googleapis/java-pubsub/issues/2028)) ([aedcffd](https://github.com/googleapis/java-pubsub/commit/aedcffdaedbaa30627c96f96bfa5430bd4666cf0))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.31.0 ([#2058](https://github.com/googleapis/java-pubsub/issues/2058)) ([a998ef5](https://github.com/googleapis/java-pubsub/commit/a998ef5359942486ea47bfd50f154314ae37be33))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.32.0 ([#2088](https://github.com/googleapis/java-pubsub/issues/2088)) ([aebc3ed](https://github.com/googleapis/java-pubsub/commit/aebc3ed779e0847077742dedc7c2c0a9d8a1ab10))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.33.0 ([#2121](https://github.com/googleapis/java-pubsub/issues/2121)) ([7fbea6d](https://github.com/googleapis/java-pubsub/commit/7fbea6d0c922dd3485f19eafccc42869efd0e5ed))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.34.0 ([#2141](https://github.com/googleapis/java-pubsub/issues/2141)) ([273fbf3](https://github.com/googleapis/java-pubsub/commit/273fbf3f752444a397b0e743c5c6de1a539291ea))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.35.0 ([#2162](https://github.com/googleapis/java-pubsub/issues/2162)) ([27eaffd](https://github.com/googleapis/java-pubsub/commit/27eaffd5fa55789b456eaeba98f6800343f3685e))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.36.0 ([#2185](https://github.com/googleapis/java-pubsub/issues/2185)) ([5ca2c7c](https://github.com/googleapis/java-pubsub/commit/5ca2c7c52497514af30e4522f0ae245d0f8d73ce))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.36.1 ([#2191](https://github.com/googleapis/java-pubsub/issues/2191)) ([555216e](https://github.com/googleapis/java-pubsub/commit/555216ee5bf9cfbba6664f133fc7cde1101f5f0b))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.37.0 ([#2214](https://github.com/googleapis/java-pubsub/issues/2214)) ([d938709](https://github.com/googleapis/java-pubsub/commit/d93870934f610cffb705837ed8391eb276a18c05))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.39.0 ([#2251](https://github.com/googleapis/java-pubsub/issues/2251)) ([083cc7c](https://github.com/googleapis/java-pubsub/commit/083cc7c930fa2728d2322c1343b0fc025f9e255d))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.41.0 ([#2286](https://github.com/googleapis/java-pubsub/issues/2286)) ([0c0a1b9](https://github.com/googleapis/java-pubsub/commit/0c0a1b9231953e5c9878e0dfcf5a55d01794f6c4))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#2301](https://github.com/googleapis/java-pubsub/issues/2301)) ([53c1a8a](https://github.com/googleapis/java-pubsub/commit/53c1a8abdd3114e0f432b3b6618133fb93e44636))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.42.0 ([#2324](https://github.com/googleapis/java-pubsub/issues/2324)) ([84e8562](https://github.com/googleapis/java-pubsub/commit/84e856250867b2441cceed2315c312bd661c353c))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#2336](https://github.com/googleapis/java-pubsub/issues/2336)) ([996f4eb](https://github.com/googleapis/java-pubsub/commit/996f4ebdfa6b5cb38dbe37d4be981ca7d941bc0d))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.44.0 ([#2349](https://github.com/googleapis/java-pubsub/issues/2349)) ([90ed10b](https://github.com/googleapis/java-pubsub/commit/90ed10b474f7a59286365d8a6ad676d9a4f4113b))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.45.1 ([#2366](https://github.com/googleapis/java-pubsub/issues/2366)) ([15899d1](https://github.com/googleapis/java-pubsub/commit/15899d127131747c51c71c94d66ff581f70278f3))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#2394](https://github.com/googleapis/java-pubsub/issues/2394)) ([17f7fd7](https://github.com/googleapis/java-pubsub/commit/17f7fd77553a7ccd55029edb74829f1fe86a680c))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.46.3 ([#2406](https://github.com/googleapis/java-pubsub/issues/2406)) ([8963ed0](https://github.com/googleapis/java-pubsub/commit/8963ed0acbe8bf3a110a05ced27979f102cd3035))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#2414](https://github.com/googleapis/java-pubsub/issues/2414)) ([d78823f](https://github.com/googleapis/java-pubsub/commit/d78823ffc93307c14f44e992cf13e926880fbe94))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#2418](https://github.com/googleapis/java-pubsub/issues/2418)) ([5f87661](https://github.com/googleapis/java-pubsub/commit/5f876612eb4a54faec3af2c9043aec0adf51e2ec))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#2428](https://github.com/googleapis/java-pubsub/issues/2428)) ([cfa91fa](https://github.com/googleapis/java-pubsub/commit/cfa91fa0e85f3f1e517627da3e5befcd46f0803a))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#2444](https://github.com/googleapis/java-pubsub/issues/2444)) ([a59135c](https://github.com/googleapis/java-pubsub/commit/a59135c6859d0aa5c247a6a1f60872c959123cc7))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#2446](https://github.com/googleapis/java-pubsub/issues/2446)) ([6434be1](https://github.com/googleapis/java-pubsub/commit/6434be16560fdc8797b7c930b06df38c0972c96c))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#2448](https://github.com/googleapis/java-pubsub/issues/2448)) ([d89a14d](https://github.com/googleapis/java-pubsub/commit/d89a14d6569fc914d877cc24d66c42684a812eba))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#2461](https://github.com/googleapis/java-pubsub/issues/2461)) ([715916a](https://github.com/googleapis/java-pubsub/commit/715916aeedbe696b9c4b922e4fb2bbf76f8b201a))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#2477](https://github.com/googleapis/java-pubsub/issues/2477)) ([e1657cb](https://github.com/googleapis/java-pubsub/commit/e1657cbeae5f2c3c9680ef6b5ff2b1ea5549f4ba))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#2494](https://github.com/googleapis/java-pubsub/issues/2494)) ([9f73ef0](https://github.com/googleapis/java-pubsub/commit/9f73ef0dcaabb4a536741336eb6cfc6601b75f65))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#2508](https://github.com/googleapis/java-pubsub/issues/2508)) ([a7be2a7](https://github.com/googleapis/java-pubsub/commit/a7be2a74327499b1acb2fe159e6f7465d6c8f798))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#2528](https://github.com/googleapis/java-pubsub/issues/2528)) ([e424d11](https://github.com/googleapis/java-pubsub/commit/e424d11ffe0fbe242c59dec44ac1af2f9bd80173))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#2544](https://github.com/googleapis/java-pubsub/issues/2544)) ([9fe7550](https://github.com/googleapis/java-pubsub/commit/9fe75506eedf42f31b95ddf2699cf332334caf0d))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#2558](https://github.com/googleapis/java-pubsub/issues/2558)) ([0623ac5](https://github.com/googleapis/java-pubsub/commit/0623ac54f735b076ccee165fc59a4a088309766a))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#2572](https://github.com/googleapis/java-pubsub/issues/2572)) ([0785ee4](https://github.com/googleapis/java-pubsub/commit/0785ee490e858c104c420046e0098d81154ae273))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#2589](https://github.com/googleapis/java-pubsub/issues/2589)) ([ce7cb09](https://github.com/googleapis/java-pubsub/commit/ce7cb09ac5e86953815e2ead9ae9202e9b034ba6))
  * update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#2609](https://github.com/googleapis/java-pubsub/issues/2609)) ([c99373f](https://github.com/googleapis/java-pubsub/commit/c99373f2d25c6b9f1bcb6aace3c6625375310a16))
  * update dependency com.google.cloud.opentelemetry:exporter-trace to v0.32.0 ([#2205](https://github.com/googleapis/java-pubsub/issues/2205)) ([76f17e4](https://github.com/googleapis/java-pubsub/commit/76f17e4149bf369f2be12fe9d316a23a7f49f137))
  * update dependency com.google.cloud.opentelemetry:exporter-trace to v0.33.0 ([#2225](https://github.com/googleapis/java-pubsub/issues/2225)) ([cc1b072](https://github.com/googleapis/java-pubsub/commit/cc1b0726009524ddee3c2ce7f1446608dd3bc752))
  * update dependency com.google.cloud.opentelemetry:exporter-trace to v0.34.0 ([#2376](https://github.com/googleapis/java-pubsub/issues/2376)) ([06768cd](https://github.com/googleapis/java-pubsub/commit/06768cd1ac86ae7ae7b91b020cc174b4423e1b9a))
  * update dependency com.google.cloud.opentelemetry:exporter-trace to v0.36.0 ([#2440](https://github.com/googleapis/java-pubsub/issues/2440)) ([50a3eb9](https://github.com/googleapis/java-pubsub/commit/50a3eb9276b4711b8161a021d055238abc0e20de))
  * update dependency com.google.protobuf:protobuf-java-util to v4.27.0 ([#2044](https://github.com/googleapis/java-pubsub/issues/2044)) ([37e94ce](https://github.com/googleapis/java-pubsub/commit/37e94ce13a2998b5e3f69e9ad3d4ab68af108d64))
  * update dependency com.google.protobuf:protobuf-java-util to v4.27.1 ([#2065](https://github.com/googleapis/java-pubsub/issues/2065)) ([6baf69a](https://github.com/googleapis/java-pubsub/commit/6baf69a99adb75fba49c2289bca3ffd08720f8f4))
  * update dependency com.google.protobuf:protobuf-java-util to v4.27.2 ([#2091](https://github.com/googleapis/java-pubsub/issues/2091)) ([9859f11](https://github.com/googleapis/java-pubsub/commit/9859f1181a12bc683eaf4a6345bf2528a5463c59))
  * update dependency com.google.protobuf:protobuf-java-util to v4.27.3 ([#2127](https://github.com/googleapis/java-pubsub/issues/2127)) ([8523b4f](https://github.com/googleapis/java-pubsub/commit/8523b4f67f45ac219671c0d588bac7e9dc450dcb))
  * update dependency com.google.protobuf:protobuf-java-util to v4.27.4 ([#2153](https://github.com/googleapis/java-pubsub/issues/2153)) ([32c78b3](https://github.com/googleapis/java-pubsub/commit/32c78b31e7a904fb6b6a2b55f81e7e3ab7525add))
  * update dependency com.google.protobuf:protobuf-java-util to v4.28.0 ([#2155](https://github.com/googleapis/java-pubsub/issues/2155)) ([5f61fe1](https://github.com/googleapis/java-pubsub/commit/5f61fe13f6fea1d30ab0e85be0221e70056369f6))
  * update dependency com.google.protobuf:protobuf-java-util to v4.28.1 ([#2167](https://github.com/googleapis/java-pubsub/issues/2167)) ([bb8ea71](https://github.com/googleapis/java-pubsub/commit/bb8ea717ed0234fdbb582f2915a016fd37657448))
  * update dependency com.google.protobuf:protobuf-java-util to v4.28.2 ([#2179](https://github.com/googleapis/java-pubsub/issues/2179)) ([c9bbd2c](https://github.com/googleapis/java-pubsub/commit/c9bbd2cf3525e3ebdf9ce3af7fe50a16a87c9837))
  * update dependency com.google.protobuf:protobuf-java-util to v4.28.3 ([#2237](https://github.com/googleapis/java-pubsub/issues/2237)) ([75abe83](https://github.com/googleapis/java-pubsub/commit/75abe83a9b14c2e5cc3f136ff97b5340bfa904db))
  * update dependency com.google.protobuf:protobuf-java-util to v4.29.0 ([#2276](https://github.com/googleapis/java-pubsub/issues/2276)) ([54ef88d](https://github.com/googleapis/java-pubsub/commit/54ef88d7f822d8130717e3be9bcf7fe9901d6cb0))
  * update dependency com.google.protobuf:protobuf-java-util to v4.29.1 ([#2279](https://github.com/googleapis/java-pubsub/issues/2279)) ([de3c9e1](https://github.com/googleapis/java-pubsub/commit/de3c9e1c7f2fe6413d0ae7a18955f16611df95c6))
  * update dependency com.google.protobuf:protobuf-java-util to v4.29.2 ([#2294](https://github.com/googleapis/java-pubsub/issues/2294)) ([48d4ac1](https://github.com/googleapis/java-pubsub/commit/48d4ac1ab2f0b9f9005292977c288f55322dd16a))
  * update dependency com.google.protobuf:protobuf-java-util to v4.29.3 ([#2302](https://github.com/googleapis/java-pubsub/issues/2302)) ([9e90e2c](https://github.com/googleapis/java-pubsub/commit/9e90e2ca26b2aea48563859358dde84640eb40d0))
  * update dependency com.google.protobuf:protobuf-java-util to v4.30.1 ([#2364](https://github.com/googleapis/java-pubsub/issues/2364)) ([05eb9c0](https://github.com/googleapis/java-pubsub/commit/05eb9c0ce5179ff9e8656544258adc02a59336e5))
  * update dependency com.google.protobuf:protobuf-java-util to v4.30.2 ([#2383](https://github.com/googleapis/java-pubsub/issues/2383)) ([4119cc0](https://github.com/googleapis/java-pubsub/commit/4119cc03895873f94ddef10850753fb59384a8fc))
  * update dependency com.google.protobuf:protobuf-java-util to v4.31.0 ([#2430](https://github.com/googleapis/java-pubsub/issues/2430)) ([232fac1](https://github.com/googleapis/java-pubsub/commit/232fac1c47e0d3680dcc8d56b69d65ed0d379dde))
  * update dependency com.google.protobuf:protobuf-java-util to v4.31.1 ([#2442](https://github.com/googleapis/java-pubsub/issues/2442)) ([a0be1bb](https://github.com/googleapis/java-pubsub/commit/a0be1bbe601575f05fb00f6d616b51de8f23238d))
  * update dependency com.google.protobuf:protobuf-java-util to v4.32.0 ([#2524](https://github.com/googleapis/java-pubsub/issues/2524)) ([44ff087](https://github.com/googleapis/java-pubsub/commit/44ff0873171f8fe2e7cd79b4550f8ec94ea2c99a))
  * update dependency com.google.protobuf:protobuf-java-util to v4.32.1 ([#2551](https://github.com/googleapis/java-pubsub/issues/2551)) ([49722cb](https://github.com/googleapis/java-pubsub/commit/49722cb65e3b7cad01cf4389e1cf716a6ac1eb03))
  * update dependency com.google.protobuf:protobuf-java-util to v4.33.0 ([#2587](https://github.com/googleapis/java-pubsub/issues/2587)) ([33724ce](https://github.com/googleapis/java-pubsub/commit/33724cef79e3f7e798c5ef222ee7dff3565555f8))
  * update dependency com.google.protobuf:protobuf-java-util to v4.33.1 ([#2612](https://github.com/googleapis/java-pubsub/issues/2612)) ([e92debc](https://github.com/googleapis/java-pubsub/commit/e92debccf9e87971c2d9fee34baffb4b534f24a3))
  * update dependency org.apache.avro:avro to v1.11.4 [security](https://docs.cloud.google.com/pubsub/docs/release-notes/%5B#2223%5D\(https://github.com/googleapis/java-pubsub/issues/2223\)%7B:%20rel=%22noreferrer%20noopener%22%7D) ([31f276b](https://github.com/googleapis/java-pubsub/commit/31f276b10a96c53ecbd828972a9e3457c0c7c700))
  * update dependency org.assertj:assertj-core to v3.26.3 ([#2204](https://github.com/googleapis/java-pubsub/issues/2204)) ([71c2e76](https://github.com/googleapis/java-pubsub/commit/71c2e762e94895c465c4e737ed8bf7bc583a9c14))
  * update dependency org.assertj:assertj-core to v3.27.2 ([#2296](https://github.com/googleapis/java-pubsub/issues/2296)) ([e5b68a5](https://github.com/googleapis/java-pubsub/commit/e5b68a563aa6ebb2bd69665624fc7fc6aef50b64))
  * update dependency org.assertj:assertj-core to v3.27.3 ([#2313](https://github.com/googleapis/java-pubsub/issues/2313)) ([5e80b57](https://github.com/googleapis/java-pubsub/commit/5e80b57d2ffd58e6a0bb9f5e0e78bb46d6fe2530))
  * update dependency org.assertj:assertj-core to v3.27.4 ([#2518](https://github.com/googleapis/java-pubsub/issues/2518)) ([67695bc](https://github.com/googleapis/java-pubsub/commit/67695bc50eafc475866eb6c300b3359083ecfe00))
  * update dependency org.assertj:assertj-core to v3.27.6 ([#2560](https://github.com/googleapis/java-pubsub/issues/2560)) ([c82766a](https://github.com/googleapis/java-pubsub/commit/c82766a9efb2bb4df01fb7fdcb35259db39e05c7))
  * update dependency org.easymock:easymock to v5.6.0 ([#2069](https://github.com/googleapis/java-pubsub/issues/2069)) ([5f144a4](https://github.com/googleapis/java-pubsub/commit/5f144a461c6749ec7e2cf900399f386094451244))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.2 ([#2035](https://github.com/googleapis/java-pubsub/issues/2035)) ([40fdd7a](https://github.com/googleapis/java-pubsub/commit/40fdd7a71aa07d6c64ac6f96d7c6642af3563280))
  * update dependency org.junit.vintage:junit-vintage-engine to v5.10.3 ([#2096](https://github.com/googleapis/java-pubsub/issues/2096)) ([42f12ed](https://github.com/googleapis/java-pubsub/commit/42f12ed3270e66beae316deb729b445c94dcb1a8))
  * update dependency org.xerial.snappy:snappy-java to v1.1.10.6 ([#2135](https://github.com/googleapis/java-pubsub/issues/2135)) ([102ff84](https://github.com/googleapis/java-pubsub/commit/102ff844594687b3bbaca1ff92e650fe9e8d3f1e))
  * update dependency org.xerial.snappy:snappy-java to v1.1.10.7 ([#2165](https://github.com/googleapis/java-pubsub/issues/2165)) ([e7fb60e](https://github.com/googleapis/java-pubsub/commit/e7fb60ecccb8bb9fbc6147210491a52ee0f5a817))
  * update dependency org.xerial.snappy:snappy-java to v1.1.10.8 ([#2492](https://github.com/googleapis/java-pubsub/issues/2492)) ([a55e214](https://github.com/googleapis/java-pubsub/commit/a55e214ffad8371eb82a1d49b8b1eadcacf15392))
  * update dependency ubuntu to v24 ([#2193](https://github.com/googleapis/java-pubsub/issues/2193)) ([f295b01](https://github.com/googleapis/java-pubsub/commit/f295b01cb93fe26612c79c3d2ba0bb68f0404d7e))
  * update googleapis/sdk-platform-java action to v2.47.0 ([#2212](https://github.com/googleapis/java-pubsub/issues/2212)) ([6a9723d](https://github.com/googleapis/java-pubsub/commit/6a9723d2872c82bbb525119cac7471d1a2f3b7cd))
  * update googleapis/sdk-platform-java action to v2.49.0 ([#2250](https://github.com/googleapis/java-pubsub/issues/2250)) ([af0f194](https://github.com/googleapis/java-pubsub/commit/af0f194369d4a9f16dd14378aa90280adc194d98))
  * update googleapis/sdk-platform-java action to v2.50.0 ([#2261](https://github.com/googleapis/java-pubsub/issues/2261)) ([d0aab7d](https://github.com/googleapis/java-pubsub/commit/d0aab7d157c628ff5b8787b8c75dfaedc7a7305f))
  * update googleapis/sdk-platform-java action to v2.51.0 ([#2284](https://github.com/googleapis/java-pubsub/issues/2284)) ([0be820e](https://github.com/googleapis/java-pubsub/commit/0be820e2044253bf484d88d703ce2dfade7aa137))
  * update googleapis/sdk-platform-java action to v2.51.1 ([#2298](https://github.com/googleapis/java-pubsub/issues/2298)) ([16e0144](https://github.com/googleapis/java-pubsub/commit/16e0144d83c149b60e7b8fca6c4e61546d93462f))
  * update googleapis/sdk-platform-java action to v2.52.0 ([#2320](https://github.com/googleapis/java-pubsub/issues/2320)) ([01dd3de](https://github.com/googleapis/java-pubsub/commit/01dd3deaef392aa51c60d28c1f3cbb81bff2a5cb))
  * update googleapis/sdk-platform-java action to v2.54.0 ([#2347](https://github.com/googleapis/java-pubsub/issues/2347)) ([ac8db2d](https://github.com/googleapis/java-pubsub/commit/ac8db2dda6cd5f0bdf689052bb37cb2eaab08c46))
  * update googleapis/sdk-platform-java action to v2.55.1 ([#2367](https://github.com/googleapis/java-pubsub/issues/2367)) ([de6f84a](https://github.com/googleapis/java-pubsub/commit/de6f84a43a27e954c0dc635158c43c5db4d07dfa))
  * update googleapis/sdk-platform-java action to v2.57.0 ([#2415](https://github.com/googleapis/java-pubsub/issues/2415)) ([1ddf9b8](https://github.com/googleapis/java-pubsub/commit/1ddf9b81e432aeb9af9e6b8bb2d2e9786159faba))
  * update googleapis/sdk-platform-java action to v2.59.0 ([#2445](https://github.com/googleapis/java-pubsub/issues/2445)) ([12d4cfb](https://github.com/googleapis/java-pubsub/commit/12d4cfb7d67dbb163b3a545ea2ebae450e88283d))
  * update googleapis/sdk-platform-java action to v2.60.0 ([#2462](https://github.com/googleapis/java-pubsub/issues/2462)) ([ee8e5c7](https://github.com/googleapis/java-pubsub/commit/ee8e5c7166f2ac4eb706241e42f4ce84afcc2668))
  * update googleapis/sdk-platform-java action to v2.60.0 ([#2464](https://github.com/googleapis/java-pubsub/issues/2464)) ([7a0af37](https://github.com/googleapis/java-pubsub/commit/7a0af37c01e747d8f40145b7b4438eaadab9e01a))
  * update googleapis/sdk-platform-java action to v2.60.0 ([#2471](https://github.com/googleapis/java-pubsub/issues/2471)) ([2b0e8e0](https://github.com/googleapis/java-pubsub/commit/2b0e8e0b58432f0975c15d0d01f185dc81de6caf))
  * update googleapis/sdk-platform-java action to v2.60.1 ([#2475](https://github.com/googleapis/java-pubsub/issues/2475)) ([e7c0b5d](https://github.com/googleapis/java-pubsub/commit/e7c0b5d44f0ad53adfac6ec26572baad54d04dee))
  * update googleapis/sdk-platform-java action to v2.61.0 ([#2509](https://github.com/googleapis/java-pubsub/issues/2509)) ([32df6b6](https://github.com/googleapis/java-pubsub/commit/32df6b694f9aee2cf7132c2d817f9736d69060f3))
  * update googleapis/sdk-platform-java action to v2.62.1 ([#2545](https://github.com/googleapis/java-pubsub/issues/2545)) ([17f28ef](https://github.com/googleapis/java-pubsub/commit/17f28ef853a21303346a305e4d8e9b63a916edc7))
  * update googleapis/sdk-platform-java action to v2.62.2 ([#2559](https://github.com/googleapis/java-pubsub/issues/2559)) ([3f1d901](https://github.com/googleapis/java-pubsub/commit/3f1d90186899efe035179363408979a372e85a56))
  * update sdk platform java dependencies ([#2239](https://github.com/googleapis/java-pubsub/issues/2239)) ([8f4f855](https://github.com/googleapis/java-pubsub/commit/8f4f8556414aaef731a7226dcbffe59d91819775))
  * update sdk platform java dependencies ([#2262](https://github.com/googleapis/java-pubsub/issues/2262)) ([b689fe2](https://github.com/googleapis/java-pubsub/commit/b689fe262b3a4c90264669ec87408bfeb6dc7659))
  * update sdk-platform-java-config to 3.55.0-rc1 ([#2642](https://github.com/googleapis/java-pubsub/issues/2642)) ([ed86f36](https://github.com/googleapis/java-pubsub/commit/ed86f3671cfb78f4c7f357cc426a57a4a7f4256d))



##### Documentation

  * A comment for field `code` in message `.google.pubsub.v1.JavaScriptUDF` is changed ([3889a05](https://github.com/googleapis/java-pubsub/commit/3889a05a5c5d7479d3cc6b6dc0b0c425d41efd5d))
  * Add ingestion from GCS sample ([#2211](https://github.com/googleapis/java-pubsub/issues/2211)) ([ddb7391](https://github.com/googleapis/java-pubsub/commit/ddb739113b38d4e2f4617a105cd0ab071f21d4de))
  * Add OpenTelemetry samples ([#2208](https://github.com/googleapis/java-pubsub/issues/2208)) ([c447fe5](https://github.com/googleapis/java-pubsub/commit/c447fe500ba48ba4fde27d97f10ef7664d09363b))
  * Add samples and tests for ingestion from Kafka sources ([#2315](https://github.com/googleapis/java-pubsub/issues/2315)) ([eea603b](https://github.com/googleapis/java-pubsub/commit/eea603ba3f05be85d58a69cd5c3469e2088a7446))
  * Fix repository URL in samples README ([#2280](https://github.com/googleapis/java-pubsub/issues/2280)) ([8aeff1a](https://github.com/googleapis/java-pubsub/commit/8aeff1a375f3aa989d2c4bde0ed3dd2f329601fc))
  * **sample:** Add samples for topic and subscription SMTs ([#2388](https://github.com/googleapis/java-pubsub/issues/2388)) ([f35de28](https://github.com/googleapis/java-pubsub/commit/f35de28396fda595e6ea68c1755a4253d6b097d6))
  * **samples:** Optimistic subscribe sample ([#2063](https://github.com/googleapis/java-pubsub/issues/2063)) ([53a4844](https://github.com/googleapis/java-pubsub/commit/53a4844f09eace777142b8cdcd06bc07cef0b432))
  * **sample:** Update the subscribe with error listener and subscribe with exactly-once samples ([#2437](https://github.com/googleapis/java-pubsub/issues/2437)) ([17c142b](https://github.com/googleapis/java-pubsub/commit/17c142b20efb79f9c71fc6306cb3ee4e15c5e06f))
  * update documentation for JavaScriptUDF to indicate that the `message_id` metadata field is optional instead of required ([f904786](https://github.com/googleapis/java-pubsub/commit/f904786f87e80cdc09bba947cd53e42dffb7132e))
  * Update emulator sample to create a topic and publish to it ([#2039](https://github.com/googleapis/java-pubsub/issues/2039)) ([21d5cfc](https://github.com/googleapis/java-pubsub/commit/21d5cfc3b9484ffc2c1a0084b8bc2f6f76b6bf62))



## December 15, 2025

Libraries

### Java

#### [1.144.0](https://github.com/googleapis/java-pubsub/compare/v1.143.1...v1.144.0) (2025-12-11)

##### Features

  * Add keepalive feature to tear down streams in their absence ([#2605](https://github.com/googleapis/java-pubsub/issues/2605)) ([99aca4f](https://github.com/googleapis/java-pubsub/commit/99aca4f3fd1792b02da78320bed39e53dc8af23c))
  * Make v1 the default protocolVersion ([#2623](https://github.com/googleapis/java-pubsub/issues/2623)) ([12f014d](https://github.com/googleapis/java-pubsub/commit/12f014d9030b2472e508fa75a71f43e671a64583))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.2 ([b4b7f83](https://github.com/googleapis/java-pubsub/commit/b4b7f839b2be1ce003667018a10d9c460e4b63b1))



##### Dependencies

  * Update actions/checkout action to v5 ([#2613](https://github.com/googleapis/java-pubsub/issues/2613)) ([a69ffdd](https://github.com/googleapis/java-pubsub/commit/a69ffdd9ecb5dae557a847ae7ec5c1a06431bef7))
  * Update actions/checkout action to v6 ([#2619](https://github.com/googleapis/java-pubsub/issues/2619)) ([6cd2bb6](https://github.com/googleapis/java-pubsub/commit/6cd2bb6e9c927dd192833efc7c3549dfa9c84f57))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.56.0 ([#2617](https://github.com/googleapis/java-pubsub/issues/2617)) ([13d5e3d](https://github.com/googleapis/java-pubsub/commit/13d5e3d8e4069a0e94db3cf825eb821d06cc9345))
  * Update dependency com.google.cloud:google-cloud-core to v2.62.1 ([#2608](https://github.com/googleapis/java-pubsub/issues/2608)) ([fee0500](https://github.com/googleapis/java-pubsub/commit/fee0500bf6a0e309ca5f162810e22a2ca4c5b7eb))
  * Update dependency com.google.cloud:google-cloud-core to v2.62.2 ([#2632](https://github.com/googleapis/java-pubsub/issues/2632)) ([2d567d1](https://github.com/googleapis/java-pubsub/commit/2d567d16f7f546586156e2e2ee17c433fbec5fc2))
  * Update dependency com.google.cloud:google-cloud-storage to v2.60.0 ([#2610](https://github.com/googleapis/java-pubsub/issues/2610)) ([1cae247](https://github.com/googleapis/java-pubsub/commit/1cae247322fff1b6588a4b523e601e41a4284c64))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.2 ([#2633](https://github.com/googleapis/java-pubsub/issues/2633)) ([5081aac](https://github.com/googleapis/java-pubsub/commit/5081aac1fc26fcaca004c730982d0e56ed36e32f))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.33.1 ([#2612](https://github.com/googleapis/java-pubsub/issues/2612)) ([e92debc](https://github.com/googleapis/java-pubsub/commit/e92debccf9e87971c2d9fee34baffb4b534f24a3))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.33.2 ([#2625](https://github.com/googleapis/java-pubsub/issues/2625)) ([900783f](https://github.com/googleapis/java-pubsub/commit/900783ff8b135b42088c37b48cdc1a7ee44d4e08))



##### Documentation

  * Add the IDENTIFIER field behavior annotation to fields of Cloud Pub/Sub methods that represent a specific identity and need to be sourced with additional care ([b4b7f83](https://github.com/googleapis/java-pubsub/commit/b4b7f839b2be1ce003667018a10d9c460e4b63b1))



## November 17, 2025

Libraries

### Java

#### [1.143.1](https://github.com/googleapis/java-pubsub/compare/v1.143.0...v1.143.1) (2025-11-13)

##### Bug Fixes

  * Deflake WaiterTest ([#2600](https://github.com/googleapis/java-pubsub/issues/2600)) ([298c8db](https://github.com/googleapis/java-pubsub/commit/298c8db04616341da040935636b1a04ce5f022a0))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.1 ([b210251](https://github.com/googleapis/java-pubsub/commit/b2102516bf833c2704c85cb348b67bb7cbfdb3a6))



##### Dependencies

  * Remove OpenTelemetry semconv dependency ([#2611](https://github.com/googleapis/java-pubsub/issues/2611)) ([240fc37](https://github.com/googleapis/java-pubsub/commit/240fc3784db3860eb2668946fbf861beed2647d7))
  * Update actions/checkout action to v5 ([#2592](https://github.com/googleapis/java-pubsub/issues/2592)) ([6ca466d](https://github.com/googleapis/java-pubsub/commit/6ca466d382ddde9780ae1c8627092d731e314f90))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.55.3 ([#2602](https://github.com/googleapis/java-pubsub/issues/2602)) ([d14106c](https://github.com/googleapis/java-pubsub/commit/d14106cc278c98d3f954f959e2dd3764ebd20fc2))
  * Update dependency com.google.cloud:google-cloud-core to v2.61.0 ([#2588](https://github.com/googleapis/java-pubsub/issues/2588)) ([244cf75](https://github.com/googleapis/java-pubsub/commit/244cf758bf46f8431a17b1d8e76d1d90c494fc76))
  * Update dependency com.google.cloud:google-cloud-storage to v2.59.0 ([#2603](https://github.com/googleapis/java-pubsub/issues/2603)) ([d9d05bf](https://github.com/googleapis/java-pubsub/commit/d9d05bfa18580cdacdfa9378d30b56ce0ae0d4d2))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.54.1 ([#2609](https://github.com/googleapis/java-pubsub/issues/2609)) ([c99373f](https://github.com/googleapis/java-pubsub/commit/c99373f2d25c6b9f1bcb6aace3c6625375310a16))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.33.0 ([#2587](https://github.com/googleapis/java-pubsub/issues/2587)) ([33724ce](https://github.com/googleapis/java-pubsub/commit/33724cef79e3f7e798c5ef222ee7dff3565555f8))



## November 03, 2025

Libraries

### Python

#### [2.32.0](https://github.com/googleapis/python-pubsub/compare/v2.31.1...v2.32.0) (2025-10-28)

##### Features

  * Adds Python 3.14 support ([#1512](https://github.com/googleapis/python-pubsub/issues/1512)) ([95a2690](https://github.com/googleapis/python-pubsub/commit/95a26907efecfa5d56b140b7f833640b7fbb21d7))
  * Debug logs ([#1460](https://github.com/googleapis/python-pubsub/issues/1460)) ([b5d4a45](https://github.com/googleapis/python-pubsub/commit/b5d4a458ca9319bebbe3142a1f05d4d4471c8d4d))
  * Support the protocol version in StreamingPullRequest ([#1455](https://github.com/googleapis/python-pubsub/issues/1455)) ([e6294a1](https://github.com/googleapis/python-pubsub/commit/e6294a1883abf9809cb56d5cd4ad25cc501bc994))



##### Bug Fixes

  * Ignore future warnings on python versions ([#1546](https://github.com/googleapis/python-pubsub/issues/1546)) ([8e28dea](https://github.com/googleapis/python-pubsub/commit/8e28dea5b68fc940266d0b1a9f2a07a7b5f10b34))



### Python

#### [2.33.0](https://github.com/googleapis/python-pubsub/compare/v2.32.0...v2.33.0) (2025-10-30)

##### Features

  * Add AwsKinesisFailureReason.ApiViolationReason ([ac68093](https://github.com/googleapis/python-pubsub/commit/ac6809350758306f28fa1ab46939bc438b5a5e19))
  * Add tags to Subscription, Topic, and CreateSnapshotRequest messages for use in CreateSubscription, CreateTopic, and CreateSnapshot requests respectively ([ac68093](https://github.com/googleapis/python-pubsub/commit/ac6809350758306f28fa1ab46939bc438b5a5e19))
  * Annotate some resource fields with their corresponding API types ([ac68093](https://github.com/googleapis/python-pubsub/commit/ac6809350758306f28fa1ab46939bc438b5a5e19))



##### Bug Fixes

  * Deprecate credentials_file argument ([ac68093](https://github.com/googleapis/python-pubsub/commit/ac6809350758306f28fa1ab46939bc438b5a5e19))



##### Documentation

  * A comment for field `received_messages` in message `.google.pubsub.v1.StreamingPullResponse` is changed ([ac68093](https://github.com/googleapis/python-pubsub/commit/ac6809350758306f28fa1ab46939bc438b5a5e19))



## October 27, 2025

Libraries

### Java

#### [1.143.0](https://github.com/googleapis/java-pubsub/compare/v1.142.0...v1.143.0) (2025-10-20)

##### Features

  * Annotate some resource fields with their corresponding API types ([ab60afa](https://github.com/googleapis/java-pubsub/commit/ab60afa012bd3fc81977ba24c416205ce9280943))
  * Implement SubscriberShutdownSettings ([#2569](https://github.com/googleapis/java-pubsub/issues/2569)) ([8195f6f](https://github.com/googleapis/java-pubsub/commit/8195f6fd3bbd33a178535994a94a79822ae2d4d6))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([ab60afa](https://github.com/googleapis/java-pubsub/commit/ab60afa012bd3fc81977ba24c416205ce9280943))
  * Update .OwlBot-hermetic.yaml to preserve SubscriberShutdownSettings files ([#2583](https://github.com/googleapis/java-pubsub/issues/2583)) ([f3cf5e7](https://github.com/googleapis/java-pubsub/commit/f3cf5e725c12173ade0275fd0526885309dc553a))



##### Dependencies

  * Update actions/checkout action to v5 ([#2576](https://github.com/googleapis/java-pubsub/issues/2576)) ([1375f6d](https://github.com/googleapis/java-pubsub/commit/1375f6d9a71c78d973a71f1df449640a95bc0bc7))
  * Update actions/checkout action to v5 ([#2584](https://github.com/googleapis/java-pubsub/issues/2584)) ([25059ce](https://github.com/googleapis/java-pubsub/commit/25059ce001e3273fcec9d1c40e3b09c89ddf487e))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.55.2 ([#2582](https://github.com/googleapis/java-pubsub/issues/2582)) ([d0f9673](https://github.com/googleapis/java-pubsub/commit/d0f96737a74453c3db54ee59e98d4b6636cd55d4))
  * Update dependency com.google.cloud:google-cloud-storage to v2.58.1 ([#2580](https://github.com/googleapis/java-pubsub/issues/2580)) ([d156cdb](https://github.com/googleapis/java-pubsub/commit/d156cdb27a8d68b6fa8c97f558df7088e6634320))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.53.0 ([#2589](https://github.com/googleapis/java-pubsub/issues/2589)) ([ce7cb09](https://github.com/googleapis/java-pubsub/commit/ce7cb09ac5e86953815e2ead9ae9202e9b034ba6))



### Go

#### [2.3.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v2.2.1...pubsub/v2.3.0) (2025-10-22)

##### Features

  * Annotate some resource fields with their corresponding API types (PiperOrigin-RevId: 820071518) ([0241a9ca](https://github.com/googleapis/google-cloud-go/commit/0241a9ca))

  * Add tags to Subscription, Topic, and CreateSnapshotRequest messages for use in CreateSubscription, CreateTopic, and CreateSnapshot requests respectively (PiperOrigin-RevId: 820071518) ([0241a9ca](https://github.com/googleapis/google-cloud-go/commit/0241a9ca))

  * Add AwsKinesisFailureReason.ApiViolationReason (PiperOrigin-RevId: 820071518) ([0241a9ca](https://github.com/googleapis/google-cloud-go/commit/0241a9ca))




##### Documentation

  * A comment for field `received_messages` in message `.google.pubsub.v1.StreamingPullResponse` is changed (PiperOrigin-RevId: 820071518) ([0241a9ca](https://github.com/googleapis/google-cloud-go/commit/0241a9ca))



## October 20, 2025

Libraries

### Go

#### [2.2.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v2/v2.2.0...pubsub/v2/v2.2.1) (2025-10-14)

##### Bug Fixes

  * **pubsub/v2:** Avoid Receive hang on context cancellation ([#13114](https://github.com/googleapis/google-cloud-go/issues/13114)) ([e7e169d](https://github.com/googleapis/google-cloud-go/commit/e7e169d1c1e48ad0fb78bcfe23d73f2de76d1f01))
  * **pubsub/v2:** Upgrade gRPC service registration func ([8fffca2](https://github.com/googleapis/google-cloud-go/commit/8fffca2819fa3dc858c213aa0c503e0df331b084))



## October 13, 2025

Libraries

### Java

#### [1.142.0](https://github.com/googleapis/java-pubsub/compare/v1.141.5...v1.142.0) (2025-10-07)

##### Features

  * Support the protocol version in StreamingPullRequest ([af40810](https://github.com/googleapis/java-pubsub/commit/af40810ea0668ce4e8c4d69bdbb4b281073976d0))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([af40810](https://github.com/googleapis/java-pubsub/commit/af40810ea0668ce4e8c4d69bdbb4b281073976d0))



##### Dependencies

  * Update actions/checkout action to v5 ([#2562](https://github.com/googleapis/java-pubsub/issues/2562)) ([b7fa499](https://github.com/googleapis/java-pubsub/commit/b7fa49968e85dfeba8a84ea29f8ddf9d33ef22c5))
  * Update actions/checkout action to v5 ([#2573](https://github.com/googleapis/java-pubsub/issues/2573)) ([4153dba](https://github.com/googleapis/java-pubsub/commit/4153dbacb386b130780c8d1e5596e3502af8e32b))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.55.1 ([#2566](https://github.com/googleapis/java-pubsub/issues/2566)) ([66c9ec4](https://github.com/googleapis/java-pubsub/commit/66c9ec4a26b76ca384dce71a8ab6bce8cd34b8a3))
  * Update dependency com.google.cloud:google-cloud-core to v2.60.2 ([#2557](https://github.com/googleapis/java-pubsub/issues/2557)) ([460bcd9](https://github.com/googleapis/java-pubsub/commit/460bcd9158e7058f710f43200b7b7737eb47839c))
  * Update dependency com.google.cloud:google-cloud-core to v2.60.3 ([#2571](https://github.com/googleapis/java-pubsub/issues/2571)) ([ac2c85a](https://github.com/googleapis/java-pubsub/commit/ac2c85ad62525aee236af54f6b5c9b1eacf4d22a))
  * Update dependency com.google.cloud:google-cloud-storage to v2.58.0 ([#2561](https://github.com/googleapis/java-pubsub/issues/2561)) ([0189388](https://github.com/googleapis/java-pubsub/commit/0189388edb4d618d65f33718922ca1b11f71cb15))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.3 ([#2572](https://github.com/googleapis/java-pubsub/issues/2572)) ([0785ee4](https://github.com/googleapis/java-pubsub/commit/0785ee490e858c104c420046e0098d81154ae273))
  * Update dependency org.assertj:assertj-core to v3.27.6 ([#2560](https://github.com/googleapis/java-pubsub/issues/2560)) ([c82766a](https://github.com/googleapis/java-pubsub/commit/c82766a9efb2bb4df01fb7fdcb35259db39e05c7))



## October 06, 2025

Libraries

### Go

#### [2.2.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v2/v2.1.0...pubsub/v2/v2.2.0) (2025-10-03)

##### Features

  * **pubsub/v2:** Support the protocol version in StreamingPullRequest ([#12985](https://github.com/googleapis/google-cloud-go/issues/12985)) ([4e8c9d5](https://github.com/googleapis/google-cloud-go/commit/4e8c9d50a07d209417d4a5807ab1990160a4fd0b))



##### Bug Fixes

  * **pubsub/v2:** Respect ShutdownBehavior when handling timeout ([#13021](https://github.com/googleapis/google-cloud-go/issues/13021)) ([0135d93](https://github.com/googleapis/google-cloud-go/commit/0135d9305581444e1ddcdd8f4fe63e4c588b575f))



## September 29, 2025

Libraries

### Java

#### [1.141.5](https://github.com/googleapis/java-pubsub/compare/v1.141.4...v1.141.5) (2025-09-24)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.2 ([c02d304](https://github.com/googleapis/java-pubsub/commit/c02d304f5213410eda5f26fe98c96a5c1d4bf9d8))



##### Dependencies

  * Update actions/checkout action to v5 ([#2539](https://github.com/googleapis/java-pubsub/issues/2539)) ([83144e6](https://github.com/googleapis/java-pubsub/commit/83144e6d4110fbe15f4357270a292cfcbcc35dd6))
  * Update actions/github-script action to v8 ([#2542](https://github.com/googleapis/java-pubsub/issues/2542)) ([0e6f0da](https://github.com/googleapis/java-pubsub/commit/0e6f0daccfdca248b3b80ef7dfb0bd7a4baa607c))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.55.0 ([#2553](https://github.com/googleapis/java-pubsub/issues/2553)) ([15b9e66](https://github.com/googleapis/java-pubsub/commit/15b9e66f27cd6e57b808b96f3e15f08b1f0d7727))
  * Update dependency com.google.cloud:google-cloud-core to v2.60.1 ([#2543](https://github.com/googleapis/java-pubsub/issues/2543)) ([fbb45ce](https://github.com/googleapis/java-pubsub/commit/fbb45cee9e3740f8ac94b5fbaa65b97b8db09b1e))
  * Update dependency com.google.cloud:google-cloud-storage to v2.57.0 ([#2547](https://github.com/googleapis/java-pubsub/issues/2547)) ([133f8c7](https://github.com/googleapis/java-pubsub/commit/133f8c7995880c2d1e75b69d61c50254d4f9fede))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.2 ([#2558](https://github.com/googleapis/java-pubsub/issues/2558)) ([0623ac5](https://github.com/googleapis/java-pubsub/commit/0623ac54f735b076ccee165fc59a4a088309766a))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.32.1 ([#2551](https://github.com/googleapis/java-pubsub/issues/2551)) ([49722cb](https://github.com/googleapis/java-pubsub/commit/49722cb65e3b7cad01cf4389e1cf716a6ac1eb03))
  * Update googleapis/sdk-platform-java action to v2.62.2 ([#2559](https://github.com/googleapis/java-pubsub/issues/2559)) ([3f1d901](https://github.com/googleapis/java-pubsub/commit/3f1d90186899efe035179363408979a372e85a56))



### Go

#### [2.1.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v2/v2.0.1...pubsub/v2/v2.1.0) (2025-09-25)

##### Features

  * **pubsub/v2:** Add subscriber shutdown options ([#12829](https://github.com/googleapis/google-cloud-go/issues/12829)) ([14c3887](https://github.com/googleapis/google-cloud-go/commit/14c3887819c7bfdf3de661ec807fa82b6bb3183e))



## September 15, 2025

Libraries

### Java

#### [1.141.4](https://github.com/googleapis/java-pubsub/compare/v1.141.3...v1.141.4) (2025-09-11)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.1 ([ac08d5f](https://github.com/googleapis/java-pubsub/commit/ac08d5f6ead8071ab0e068e32fd5ae0ae2731c34))



##### Dependencies

  * Update actions/checkout action to v5 ([#2531](https://github.com/googleapis/java-pubsub/issues/2531)) ([f687f11](https://github.com/googleapis/java-pubsub/commit/f687f117fc435ee8b1f15b8802ecc989f1e2747e))
  * Update actions/setup-java action to v5 ([#2535](https://github.com/googleapis/java-pubsub/issues/2535)) ([2ed87d2](https://github.com/googleapis/java-pubsub/commit/2ed87d2b7e28af99cfda00b4b69fb5cb2f448584))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.54.2 ([#2538](https://github.com/googleapis/java-pubsub/issues/2538)) ([10a8283](https://github.com/googleapis/java-pubsub/commit/10a8283292e58b0c73b9c57ff36ddd71b8b83467))
  * Update dependency com.google.cloud:google-cloud-storage to v2.56.0 ([#2536](https://github.com/googleapis/java-pubsub/issues/2536)) ([80d9ca1](https://github.com/googleapis/java-pubsub/commit/80d9ca10d3a2656852422858f032bb6629102cfb))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#2544](https://github.com/googleapis/java-pubsub/issues/2544)) ([9fe7550](https://github.com/googleapis/java-pubsub/commit/9fe75506eedf42f31b95ddf2699cf332334caf0d))
  * Update googleapis/sdk-platform-java action to v2.62.1 ([#2545](https://github.com/googleapis/java-pubsub/issues/2545)) ([17f28ef](https://github.com/googleapis/java-pubsub/commit/17f28ef853a21303346a305e4d8e9b63a916edc7))



## September 08, 2025

Libraries

### Go

#### [2.0.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v2/v2.0.0...pubsub/v2/v2.0.1) (2025-09-03)

##### Bug Fixes

  * **pubsub/v2:** Update flowcontrol metrics even when disabled ([#12590](https://github.com/googleapis/google-cloud-go/issues/12590)) ([c153495](https://github.com/googleapis/google-cloud-go/commit/c1534952c4a6c3a52dd9e3aab295d27d4107016c))



##### Documentation

  * **pubsub/v2:** Move wiki to package doc ([#12605](https://github.com/googleapis/google-cloud-go/issues/12605)) ([3de795e](https://github.com/googleapis/google-cloud-go/commit/3de795ecaf1782df76d9ac49499988369601d334))



### Go

#### [1.50.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.50.0...pubsub/v1.50.1) (2025-09-04)

##### Bug Fixes

  * **pubsub/v2:** Update flowcontrol metrics even when disabled ([#12590](https://github.com/googleapis/google-cloud-go/issues/12590)) ([c153495](https://github.com/googleapis/google-cloud-go/commit/c1534952c4a6c3a52dd9e3aab295d27d4107016c))



##### Documentation

  * **pubsub:** Update migration docs with seek ([#12642](https://github.com/googleapis/google-cloud-go/issues/12642)) ([40538c3](https://github.com/googleapis/google-cloud-go/commit/40538c3a8cbbd9a54deb6cdb204809d487aef21b))



## August 25, 2025

Libraries

### Java

#### [1.141.3](https://github.com/googleapis/java-pubsub/compare/v1.141.2...v1.141.3) (2025-08-19)

##### Bug Fixes

  * Use the system executor instead of a separate thread pool for EOD ack/modack callbacks ([#2526](https://github.com/googleapis/java-pubsub/issues/2526)) ([ffeb017](https://github.com/googleapis/java-pubsub/commit/ffeb017a58ca486688105738f180d70df33a74de))



##### Dependencies

  * Update actions/checkout action to v5 ([#2520](https://github.com/googleapis/java-pubsub/issues/2520)) ([409398a](https://github.com/googleapis/java-pubsub/commit/409398a40f71866d5a84b4542d582777ee240a08))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.54.1 ([#2523](https://github.com/googleapis/java-pubsub/issues/2523)) ([0678a74](https://github.com/googleapis/java-pubsub/commit/0678a74dc22f73cd8ec8c4893c1a8dd60449b128))
  * Update dependency com.google.cloud:google-cloud-core to v2.60.0 ([#2527](https://github.com/googleapis/java-pubsub/issues/2527)) ([0166e21](https://github.com/googleapis/java-pubsub/commit/0166e21012f0bc2ccb2e832d6f27e60ad3382456))
  * Update dependency com.google.cloud:google-cloud-storage to v2.55.0 ([#2517](https://github.com/googleapis/java-pubsub/issues/2517)) ([b67acf1](https://github.com/googleapis/java-pubsub/commit/b67acf1294249be308568f49f287897ae55ced08))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.0 ([#2528](https://github.com/googleapis/java-pubsub/issues/2528)) ([e424d11](https://github.com/googleapis/java-pubsub/commit/e424d11ffe0fbe242c59dec44ac1af2f9bd80173))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.32.0 ([#2524](https://github.com/googleapis/java-pubsub/issues/2524)) ([44ff087](https://github.com/googleapis/java-pubsub/commit/44ff0873171f8fe2e7cd79b4550f8ec94ea2c99a))
  * Update dependency org.assertj:assertj-core to v3.27.4 ([#2518](https://github.com/googleapis/java-pubsub/issues/2518)) ([67695bc](https://github.com/googleapis/java-pubsub/commit/67695bc50eafc475866eb6c300b3359083ecfe00))



## August 11, 2025

Libraries

### Java

#### [1.141.2](https://github.com/googleapis/java-pubsub/compare/v1.141.1...v1.141.2) (2025-08-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.61.0 ([42eb599](https://github.com/googleapis/java-pubsub/commit/42eb5992557457a5ae4512334267113266c220ac))
  * Use a separate cached thread pool for handling ack and modack response callback for EOD-enabled subscriptions ([#2505](https://github.com/googleapis/java-pubsub/issues/2505)) ([224c269](https://github.com/googleapis/java-pubsub/commit/224c269e3bd0ae4cfc4b24ac85495911b8e2b90c))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.54.0 ([#2506](https://github.com/googleapis/java-pubsub/issues/2506)) ([6bf8e62](https://github.com/googleapis/java-pubsub/commit/6bf8e62b1144568292e832dc8031a70a2c5b9ad7))
  * Update dependency com.google.cloud:google-cloud-core to v2.59.0 ([#2507](https://github.com/googleapis/java-pubsub/issues/2507)) ([070cf07](https://github.com/googleapis/java-pubsub/commit/070cf07b1d529c34d4f633b37ce1d35d14768325))
  * Update dependency com.google.cloud:google-cloud-storage to v2.54.0 ([#2510](https://github.com/googleapis/java-pubsub/issues/2510)) ([0fd589e](https://github.com/googleapis/java-pubsub/commit/0fd589e2ee80730b442f569b770fe16208feb4ba))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.51.0 ([#2508](https://github.com/googleapis/java-pubsub/issues/2508)) ([a7be2a7](https://github.com/googleapis/java-pubsub/commit/a7be2a74327499b1acb2fe159e6f7465d6c8f798))
  * Update googleapis/sdk-platform-java action to v2.61.0 ([#2509](https://github.com/googleapis/java-pubsub/issues/2509)) ([32df6b6](https://github.com/googleapis/java-pubsub/commit/32df6b694f9aee2cf7132c2d817f9736d69060f3))



## August 04, 2025

Libraries

### Java

#### [1.141.1](https://github.com/googleapis/java-pubsub/compare/v1.141.0...v1.141.1) (2025-07-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([7afae21](https://github.com/googleapis/java-pubsub/commit/7afae21e5e3df16742646363ca199ec14c42bc21))
  * Remove element_count_limit and request_byte_limit from pubsub_gapic.yaml ([7afae21](https://github.com/googleapis/java-pubsub/commit/7afae21e5e3df16742646363ca199ec14c42bc21))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.53.0 ([#2489](https://github.com/googleapis/java-pubsub/issues/2489)) ([5a454b9](https://github.com/googleapis/java-pubsub/commit/5a454b9c36419dcfaf79edb1ec1d066b20836f87))
  * Update dependency com.google.cloud:google-cloud-core to v2.58.2 ([#2493](https://github.com/googleapis/java-pubsub/issues/2493)) ([9a1c17e](https://github.com/googleapis/java-pubsub/commit/9a1c17e50e5fc9a807532d289a7f6e8b5d412f59))
  * Update dependency com.google.cloud:google-cloud-storage to v2.53.3 ([#2486](https://github.com/googleapis/java-pubsub/issues/2486)) ([9416cc9](https://github.com/googleapis/java-pubsub/commit/9416cc99f826b80412b0e5eba0068a35b82390c6))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.2 ([#2494](https://github.com/googleapis/java-pubsub/issues/2494)) ([9f73ef0](https://github.com/googleapis/java-pubsub/commit/9f73ef0dcaabb4a536741336eb6cfc6601b75f65))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.8 ([#2492](https://github.com/googleapis/java-pubsub/issues/2492)) ([a55e214](https://github.com/googleapis/java-pubsub/commit/a55e214ffad8371eb82a1d49b8b1eadcacf15392))



### Go

#### [1.50.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.49.0...pubsub/v1.50.0) (2025-07-28)

##### Features

  * **pubsub/v2:** Add new v2 library ([#12218](https://github.com/googleapis/google-cloud-go/issues/12218)) ([c798f62](https://github.com/googleapis/google-cloud-go/commit/c798f62f908140686b8e2a365cccf9608fb5ab95))



##### Bug Fixes

  * **pubsub:** Update google.golang.org/api to 0.229.0 ([3319672](https://github.com/googleapis/google-cloud-go/commit/3319672f3dba84a7150772ccb5433e02dab7e201))



##### Documentation

  * **pubsub:** Add docs comment to MaxOutstandingBytes ([#12601](https://github.com/googleapis/google-cloud-go/issues/12601)) ([76ddb34](https://github.com/googleapis/google-cloud-go/commit/76ddb3498f2c986b156abaeaf7efeab1c9490725))



### Python

#### [2.31.1](https://github.com/googleapis/python-pubsub/compare/v2.31.0...v2.31.1) (2025-07-28)

##### Bug Fixes

  * Change Log Severities for Terminated Streams ([#1433](https://github.com/googleapis/python-pubsub/issues/1433)) ([3a3aa79](https://github.com/googleapis/python-pubsub/commit/3a3aa79040d656a3391a153386ec662d002f9368))
  * Propagate Otel Context to Subscriber Callback if Provided ([#1429](https://github.com/googleapis/python-pubsub/issues/1429)) ([b0f6f49](https://github.com/googleapis/python-pubsub/commit/b0f6f49f65752e88523f9c4209366d2a18140416))



## July 31, 2025

Deprecated

**Deprecated:** The v2 Pub/Sub Ruby client library, [google-cloud-pubsub/v2.x](https://rubygems.org/gems/google-cloud-pubsub/versions/2.23.0), is now deprecated. Effective July 31st, 2026, this version will no longer receive security or bug fixes. To receive new features, [migrate](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md) to the newest version, [google-cloud-pubsub/v3.x](https://rubygems.org/gems/google-cloud-pubsub/versions/3.0.0).

## July 21, 2025

Libraries

### Java

#### [1.141.0](https://github.com/googleapis/java-pubsub/compare/v1.140.2...v1.141.0) (2025-07-11)

##### Features

  * Add MessageTransformationFailureReason to IngestionFailureEvent ([8271399](https://github.com/googleapis/java-pubsub/commit/8271399cc6348f69ba034b676cce2aa7592122a4))
  * Next release from main branch is 1.141.0 ([#2481](https://github.com/googleapis/java-pubsub/issues/2481)) ([bd9f385](https://github.com/googleapis/java-pubsub/commit/bd9f3850efa77ce759b4f281aecd9645666cb0f7))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.1 ([c9ef2cd](https://github.com/googleapis/java-pubsub/commit/c9ef2cda2c6ad20d5e57fe3ccf69f845f7ef36b7))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.52.0 ([#2467](https://github.com/googleapis/java-pubsub/issues/2467)) ([fe08a6f](https://github.com/googleapis/java-pubsub/commit/fe08a6f1f6ee18e97c752f82786016999f6ab12c))
  * Update dependency com.google.cloud:google-cloud-core to v2.58.1 ([#2476](https://github.com/googleapis/java-pubsub/issues/2476)) ([96a2354](https://github.com/googleapis/java-pubsub/commit/96a23544fce609c7b19a00638a767926c304d3f8))
  * Update dependency com.google.cloud:google-cloud-storage to v2.53.2 ([#2469](https://github.com/googleapis/java-pubsub/issues/2469)) ([fa51a01](https://github.com/googleapis/java-pubsub/commit/fa51a01ed39393b7cad25fb39a1c87099def830a))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.1 ([#2477](https://github.com/googleapis/java-pubsub/issues/2477)) ([e1657cb](https://github.com/googleapis/java-pubsub/commit/e1657cbeae5f2c3c9680ef6b5ff2b1ea5549f4ba))
  * Update googleapis/sdk-platform-java action to v2.60.0 ([#2471](https://github.com/googleapis/java-pubsub/issues/2471)) ([2b0e8e0](https://github.com/googleapis/java-pubsub/commit/2b0e8e0b58432f0975c15d0d01f185dc81de6caf))
  * Update googleapis/sdk-platform-java action to v2.60.1 ([#2475](https://github.com/googleapis/java-pubsub/issues/2475)) ([e7c0b5d](https://github.com/googleapis/java-pubsub/commit/e7c0b5d44f0ad53adfac6ec26572baad54d04dee))



### Go

#### 2.0.0 (2025-07-16)

To migrate from the v1 cloud.google.com/go/pubsub, please follow the [migration guide](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md)

##### Features

  * **pubsub/v2:** Add MessageTransformationFailureReason to IngestionFailureEvent ([208745b](https://github.com/googleapis/google-cloud-go/commit/208745bbc1f4fc9122ec71d6cf42f512ae570d13))
  * **pubsub/v2:** Add new v2 library ([#12218](https://github.com/googleapis/google-cloud-go/issues/12218)) ([c798f62](https://github.com/googleapis/google-cloud-go/commit/c798f62f908140686b8e2a365cccf9608fb5ab95))
  * **pubsub/v2:** Add SchemaViolationReason to IngestionFailureEvent ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
  * **pubsub/v2:** Generate renamed go pubsub admin clients ([a95a0bf](https://github.com/googleapis/google-cloud-go/commit/a95a0bf4172b8a227955a0353fd9c845f4502411))
  * **pubsub/v2:** Release 2.0.0 ([#12568](https://github.com/googleapis/google-cloud-go/issues/12568)) ([704efce](https://github.com/googleapis/google-cloud-go/commit/704efce43ffd2e81e9fe8e19f7573913b86840e8))



##### Documentation

  * **pubsub/v2:** Document that the `acknowledge_confirmation` and `modify_ack_deadline_confirmation` fields in message `.google.pubsub.v1.StreamingPullResponse` are not guaranteed to be populated ([208745b](https://github.com/googleapis/google-cloud-go/commit/208745bbc1f4fc9122ec71d6cf42f512ae570d13))
  * **pubsub/v2:** Standardize spelling of "acknowledgment" in Pub/Sub protos ([d8ae687](https://github.com/googleapis/google-cloud-go/commit/d8ae6874a54b48fce49968664f14db63c055c6e2))
  * **pubsub/v2:** Update v2 package docs with migration guide ([#12564](https://github.com/googleapis/google-cloud-go/issues/12564)) ([5ef6068](https://github.com/googleapis/google-cloud-go/commit/5ef606838a84f1c56225fc4e33f4ee394eb34725))



## July 15, 2025

Deprecated

**Deprecated:** The v1 Pub/Sub Go client library, [cloud.google.com/go/pubsub](http://cloud.google.com/go/pubsub), is now deprecated. Effective July 31st, 2026, this library will no longer receive security or bug fixes. To receive new features, [migrate](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md) to the newest version, [cloud.google.com/go/pubsub/v2](http://cloud.google.com/go/pubsub/v2).

## July 14, 2025

Libraries

### Python

#### [2.31.0](https://github.com/googleapis/python-pubsub/compare/v2.30.0...v2.31.0) (2025-06-26)

##### Features

  * Add MessageTransformationFailureReason to IngestionFailureEvent ([#1427](https://github.com/googleapis/python-pubsub/issues/1427)) ([8ab13e1](https://github.com/googleapis/python-pubsub/commit/8ab13e1b71c151f0146548e7224dd38c9d719a88))



##### Bug Fixes

  * Surface Fatal Stream Errors to Future; Adjust Retryable Error Codes ([#1422](https://github.com/googleapis/python-pubsub/issues/1422)) ([e081beb](https://github.com/googleapis/python-pubsub/commit/e081beb29056035304d365ec9c50fa7ffbac6886))



## June 30, 2025

Libraries

### Java

#### [1.140.2](https://github.com/googleapis/java-pubsub/compare/v1.140.1...v1.140.2) (2025-06-25)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.51.0 ([#2457](https://github.com/googleapis/java-pubsub/issues/2457)) ([d74215a](https://github.com/googleapis/java-pubsub/commit/d74215a6f1e641ba75997e2e43bef348fb9c4a3c))
  * Update dependency com.google.cloud:google-cloud-core to v2.58.0 ([#2443](https://github.com/googleapis/java-pubsub/issues/2443)) ([d4599d9](https://github.com/googleapis/java-pubsub/commit/d4599d93b780b6ef20ad44582aeb8c1cd35f99d4))
  * Update dependency com.google.cloud:google-cloud-storage to v2.53.1 ([#2452](https://github.com/googleapis/java-pubsub/issues/2452)) ([b4af237](https://github.com/googleapis/java-pubsub/commit/b4af2370bb875ee8d0047f67a72e8c6d62547a12))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.50.0 ([#2461](https://github.com/googleapis/java-pubsub/issues/2461)) ([715916a](https://github.com/googleapis/java-pubsub/commit/715916aeedbe696b9c4b922e4fb2bbf76f8b201a))
  * Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.36.0 ([#2440](https://github.com/googleapis/java-pubsub/issues/2440)) ([50a3eb9](https://github.com/googleapis/java-pubsub/commit/50a3eb9276b4711b8161a021d055238abc0e20de))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.31.1 ([#2442](https://github.com/googleapis/java-pubsub/issues/2442)) ([a0be1bb](https://github.com/googleapis/java-pubsub/commit/a0be1bbe601575f05fb00f6d616b51de8f23238d))
  * Update dependency org.easymock:easymock to v5.6.0 ([#2069](https://github.com/googleapis/java-pubsub/issues/2069)) ([5f144a4](https://github.com/googleapis/java-pubsub/commit/5f144a461c6749ec7e2cf900399f386094451244))
  * Update googleapis/sdk-platform-java action to v2.60.0 ([#2462](https://github.com/googleapis/java-pubsub/issues/2462)) ([ee8e5c7](https://github.com/googleapis/java-pubsub/commit/ee8e5c7166f2ac4eb706241e42f4ce84afcc2668))
  * Update googleapis/sdk-platform-java action to v2.60.0 ([#2464](https://github.com/googleapis/java-pubsub/issues/2464)) ([7a0af37](https://github.com/googleapis/java-pubsub/commit/7a0af37c01e747d8f40145b7b4438eaadab9e01a))



## June 16, 2025

Libraries

### Python

#### [2.30.0](https://github.com/googleapis/python-pubsub/compare/v2.29.1...v2.30.0) (2025-06-07)

##### Features

  * Add SchemaViolationReason to IngestionFailureEvent ([#1411](https://github.com/googleapis/python-pubsub/issues/1411)) ([c046ca2](https://github.com/googleapis/python-pubsub/commit/c046ca22e9bddff6b50f7670bf6b9b9470bf78e8))



## June 09, 2025

Libraries

### Java

#### [1.140.0](https://github.com/googleapis/java-pubsub/compare/v1.139.4...v1.140.0) (2025-06-03)

##### Features

  * Add SchemaViolationReason to IngestionFailureEvent ([21cc376](https://github.com/googleapis/java-pubsub/commit/21cc3764aaa6fc05eb4a5078a72dae30694fba91))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.50.1 ([#2435](https://github.com/googleapis/java-pubsub/issues/2435)) ([b37c557](https://github.com/googleapis/java-pubsub/commit/b37c5573e1d0d7eada4ce4ec6a052521ea11cff1))
  * Update dependency com.google.cloud:google-cloud-storage to v2.52.3 ([#2436](https://github.com/googleapis/java-pubsub/issues/2436)) ([4f309d1](https://github.com/googleapis/java-pubsub/commit/4f309d151d4bd584a33a0bb8882d0614a1b9d533))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#2444](https://github.com/googleapis/java-pubsub/issues/2444)) ([a59135c](https://github.com/googleapis/java-pubsub/commit/a59135c6859d0aa5c247a6a1f60872c959123cc7))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#2446](https://github.com/googleapis/java-pubsub/issues/2446)) ([6434be1](https://github.com/googleapis/java-pubsub/commit/6434be16560fdc8797b7c930b06df38c0972c96c))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.31.0 ([#2430](https://github.com/googleapis/java-pubsub/issues/2430)) ([232fac1](https://github.com/googleapis/java-pubsub/commit/232fac1c47e0d3680dcc8d56b69d65ed0d379dde))
  * Update googleapis/sdk-platform-java action to v2.59.0 ([#2445](https://github.com/googleapis/java-pubsub/issues/2445)) ([12d4cfb](https://github.com/googleapis/java-pubsub/commit/12d4cfb7d67dbb163b3a545ea2ebae450e88283d))



##### Documentation

  * **sample:** Update the subscribe with error listener and subscribe with exactly-once samples ([#2437](https://github.com/googleapis/java-pubsub/issues/2437)) ([17c142b](https://github.com/googleapis/java-pubsub/commit/17c142b20efb79f9c71fc6306cb3ee4e15c5e06f))



### Java

#### [1.140.1](https://github.com/googleapis/java-pubsub/compare/v1.140.0...v1.140.1) (2025-06-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([0eece50](https://github.com/googleapis/java-pubsub/commit/0eece5012fbaf887a5c062beba433dbb30edbf43))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.49.0 ([#2448](https://github.com/googleapis/java-pubsub/issues/2448)) ([d89a14d](https://github.com/googleapis/java-pubsub/commit/d89a14d6569fc914d877cc24d66c42684a812eba))



### Go

## June 02, 2025

Libraries

### Python

#### [2.29.1](https://github.com/googleapis/python-pubsub/compare/v2.29.0...v2.29.1) (2025-05-23)

##### Bug Fixes

  * Remove setup.cfg configuration for creating universal wheels ([#1376](https://github.com/googleapis/python-pubsub/issues/1376)) ([60639c4](https://github.com/googleapis/python-pubsub/commit/60639c4928105ae8a72c8e37b1f48f75cc2ffcc3))



##### Documentation

  * **sample:** Add samples for topic and subscription SMTs ([#1386](https://github.com/googleapis/python-pubsub/issues/1386)) ([4d072e0](https://github.com/googleapis/python-pubsub/commit/4d072e088b59f692dc3d59c3197a2993c125917e))
  * Update documentation for JavaScriptUDF to indicate that the `message_id` metadata field is optional instead of required ([#1380](https://github.com/googleapis/python-pubsub/issues/1380)) ([be90054](https://github.com/googleapis/python-pubsub/commit/be9005412fea06bea917c8b6861546b7e6c62a1e))
  * Update readme links ([#1409](https://github.com/googleapis/python-pubsub/issues/1409)) ([77ba05d](https://github.com/googleapis/python-pubsub/commit/77ba05d4ba5b84a25c1a07c5397bbc184fa6041d))



Feature

General availability: Pub/Sub now offers Single Message Transforms (SMTs) that enable lightweight modifications to message data and attributes directly within Pub/Sub. SMTs can be set as properties of topics or subscriptions. The change is being rolled out in a phased manner over the rest of the week. For more information about SMTs, see [Single Message Transforms (SMTs) overview](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).

## May 26, 2025

Libraries

### Go

This is an **alpha** release for the Pub/Sub v2 library and should not be used for production.

## May 19, 2025

Libraries

### Java

#### [1.139.4](https://github.com/googleapis/java-pubsub/compare/v1.139.3...v1.139.4) (2025-05-15)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.57.0 ([017eb0f](https://github.com/googleapis/java-pubsub/commit/017eb0f78423fde3edd42a07677df49512085633))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.58.0 ([3713edb](https://github.com/googleapis/java-pubsub/commit/3713edb9420f792b7c7ad4e430ca05b5942656ff))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.50.0 ([#2422](https://github.com/googleapis/java-pubsub/issues/2422)) ([993b2d0](https://github.com/googleapis/java-pubsub/commit/993b2d06ce6b45bb72faa9d6959cddc14a9cf60e))
  * Update dependency com.google.cloud:google-cloud-core to v2.55.0 ([#2413](https://github.com/googleapis/java-pubsub/issues/2413)) ([3e181e7](https://github.com/googleapis/java-pubsub/commit/3e181e7c4469eadcf6f148ee0a30aae1cfa825f3))
  * Update dependency com.google.cloud:google-cloud-core to v2.56.0 ([#2427](https://github.com/googleapis/java-pubsub/issues/2427)) ([b2a3e35](https://github.com/googleapis/java-pubsub/commit/b2a3e35ced2d1715c37207f98740889635326dc1))
  * Update dependency com.google.cloud:google-cloud-storage to v2.52.2 ([#2421](https://github.com/googleapis/java-pubsub/issues/2421)) ([1224ee5](https://github.com/googleapis/java-pubsub/commit/1224ee51da27e447560076b0d51ba90515566bd9))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#2418](https://github.com/googleapis/java-pubsub/issues/2418)) ([5f87661](https://github.com/googleapis/java-pubsub/commit/5f876612eb4a54faec3af2c9043aec0adf51e2ec))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.48.0 ([#2428](https://github.com/googleapis/java-pubsub/issues/2428)) ([cfa91fa](https://github.com/googleapis/java-pubsub/commit/cfa91fa0e85f3f1e517627da3e5befcd46f0803a))
  * Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.34.0 ([#2376](https://github.com/googleapis/java-pubsub/issues/2376)) ([06768cd](https://github.com/googleapis/java-pubsub/commit/06768cd1ac86ae7ae7b91b020cc174b4423e1b9a))



##### Documentation

  * **sample:** Add samples for topic and subscription SMTs ([#2388](https://github.com/googleapis/java-pubsub/issues/2388)) ([f35de28](https://github.com/googleapis/java-pubsub/commit/f35de28396fda595e6ea68c1755a4253d6b097d6))



## May 12, 2025

Libraries

### Java

#### [1.139.2](https://github.com/googleapis/java-pubsub/compare/v1.139.1...v1.139.2) (2025-05-05)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.3 ([2b928a8](https://github.com/googleapis/java-pubsub/commit/2b928a8a946ebf84470bd2e2bb064b52c4f11ea2))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.49.2 ([#2399](https://github.com/googleapis/java-pubsub/issues/2399)) ([ff48708](https://github.com/googleapis/java-pubsub/commit/ff4870815864a6216a1ce4b606fcec3df7f58fd4))
  * Update dependency com.google.cloud:google-cloud-core to v2.54.3 ([#2393](https://github.com/googleapis/java-pubsub/issues/2393)) ([0ffa26a](https://github.com/googleapis/java-pubsub/commit/0ffa26ac3abceabcfba5d57cdb36f27f5a164ce3))
  * Update dependency com.google.cloud:google-cloud-storage to v2.52.1 ([#2396](https://github.com/googleapis/java-pubsub/issues/2396)) ([283a6e1](https://github.com/googleapis/java-pubsub/commit/283a6e14f61764c210ed23f4ada23ad21bbdb306))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.3 ([#2406](https://github.com/googleapis/java-pubsub/issues/2406)) ([8963ed0](https://github.com/googleapis/java-pubsub/commit/8963ed0acbe8bf3a110a05ced27979f102cd3035))



### Java

#### [1.139.3](https://github.com/googleapis/java-pubsub/compare/v1.139.2...v1.139.3) (2025-05-06)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.47.0 ([#2414](https://github.com/googleapis/java-pubsub/issues/2414)) ([d78823f](https://github.com/googleapis/java-pubsub/commit/d78823ffc93307c14f44e992cf13e926880fbe94))
  * Update googleapis/sdk-platform-java action to v2.57.0 ([#2415](https://github.com/googleapis/java-pubsub/issues/2415)) ([1ddf9b8](https://github.com/googleapis/java-pubsub/commit/1ddf9b81e432aeb9af9e6b8bb2d2e9786159faba))



## April 28, 2025

Libraries

### Java

#### [1.139.0](https://github.com/googleapis/java-pubsub/compare/v1.138.0...v1.139.0) (2025-04-25)

##### Features

  * Generate renamed go pubsub admin clients ([4472d7b](https://github.com/googleapis/java-pubsub/commit/4472d7baff4894a7c5cf0efc7eadd83ec8801d7a))



##### Bug Fixes

  * Add retries for ack and modack operations that don't return with a metadata map ([#2385](https://github.com/googleapis/java-pubsub/issues/2385)) ([00070b7](https://github.com/googleapis/java-pubsub/commit/00070b74e54fcb62b91a4d72a88d3b20b2425a94))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([4472d7b](https://github.com/googleapis/java-pubsub/commit/4472d7baff4894a7c5cf0efc7eadd83ec8801d7a))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.49.0 ([#2380](https://github.com/googleapis/java-pubsub/issues/2380)) ([405e485](https://github.com/googleapis/java-pubsub/commit/405e485bbe503357a0616ec72de8fea00cb91c9c))
  * Update dependency com.google.cloud:google-cloud-core to v2.53.1 ([#2365](https://github.com/googleapis/java-pubsub/issues/2365)) ([748058f](https://github.com/googleapis/java-pubsub/commit/748058fc018e3a36dedd576404037bf8c016c794))
  * Update dependency com.google.cloud:google-cloud-storage to v2.50.0 ([#2372](https://github.com/googleapis/java-pubsub/issues/2372)) ([b81164a](https://github.com/googleapis/java-pubsub/commit/b81164aa5682c8046ebfa44e1e47579e4c3fcd28))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.30.1 ([#2364](https://github.com/googleapis/java-pubsub/issues/2364)) ([05eb9c0](https://github.com/googleapis/java-pubsub/commit/05eb9c0ce5179ff9e8656544258adc02a59336e5))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.30.2 ([#2383](https://github.com/googleapis/java-pubsub/issues/2383)) ([4119cc0](https://github.com/googleapis/java-pubsub/commit/4119cc03895873f94ddef10850753fb59384a8fc))



##### Documentation

  * Update documentation for JavaScriptUDF to indicate that the `message_id` metadata field is optional instead of required ([f904786](https://github.com/googleapis/java-pubsub/commit/f904786f87e80cdc09bba947cd53e42dffb7132e))



### Java

#### [1.139.1](https://github.com/googleapis/java-pubsub/compare/v1.139.0...v1.139.1) (2025-04-25)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.46.2 ([#2394](https://github.com/googleapis/java-pubsub/issues/2394)) ([17f7fd7](https://github.com/googleapis/java-pubsub/commit/17f7fd77553a7ccd55029edb74829f1fe86a680c))



## April 14, 2025

Libraries

### Go

#### [1.49.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.48.1...pubsub/v1.49.0) (2025-04-07)

##### Features

  * **pubsub:** Support message transforms ([#11957](https://github.com/googleapis/google-cloud-go/issues/11957)) ([84bf25b](https://github.com/googleapis/google-cloud-go/commit/84bf25ba1c0e01b2f19167d4d3c914c56f87b924))



## April 07, 2025

Libraries

### Go

#### [1.48.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.48.0...pubsub/v1.48.1) (2025-04-01)

##### Bug Fixes

  * **pubsub/pstest:** Message ordering issue ([#11603](https://github.com/googleapis/google-cloud-go/issues/11603)) ([1d6ffc0](https://github.com/googleapis/google-cloud-go/commit/1d6ffc02cd211368eabbc8e4f02392952c603703))
  * **pubsub:** Update golang.org/x/net to 0.37.0 ([1144978](https://github.com/googleapis/google-cloud-go/commit/11449782c7fb4896bf8b8b9cde8e7441c84fb2fd))



##### Documentation

  * **pubsub:** Update documentation for JavaScriptUDF to indicate that the `message_id` metadata field is optional instead of required ([f437f08](https://github.com/googleapis/google-cloud-go/commit/f437f0871a88abbeb918ce7364d0299a513cc311))



## March 24, 2025

Libraries

### Python

#### [2.29.0](https://github.com/googleapis/python-pubsub/compare/v2.28.0...v2.29.0) (2025-03-19)

##### Features

  * Add REST Interceptors which support reading metadata ([4363179](https://github.com/googleapis/python-pubsub/commit/43631790781ccfe071a7ecad41949399d3dbd063))
  * Add support for opt-in debug logging ([4363179](https://github.com/googleapis/python-pubsub/commit/43631790781ccfe071a7ecad41949399d3dbd063))
  * Deprecate `enabled` field for message transforms and add `disabled` field ([4363179](https://github.com/googleapis/python-pubsub/commit/43631790781ccfe071a7ecad41949399d3dbd063))



##### Bug Fixes

  * Allow logs to propagate upstream for caplog testing ([#1374](https://github.com/googleapis/python-pubsub/issues/1374)) ([fa39b0e](https://github.com/googleapis/python-pubsub/commit/fa39b0e87695da40036c1daec1b3108374672d61))
  * Allow Protobuf 6.x ([#1369](https://github.com/googleapis/python-pubsub/issues/1369)) ([c95b7a5](https://github.com/googleapis/python-pubsub/commit/c95b7a5bad7138a70e56c278970f5b54939a68f8))
  * Fix typing issue with gRPC metadata when key ends in -bin ([4363179](https://github.com/googleapis/python-pubsub/commit/43631790781ccfe071a7ecad41949399d3dbd063))



##### Documentation

  * A comment for field `code` in message `.google.pubsub.v1.JavaScriptUDF` is changed ([4363179](https://github.com/googleapis/python-pubsub/commit/43631790781ccfe071a7ecad41949399d3dbd063))
  * Add samples and test for ingestion from Kafka sources ([#1354](https://github.com/googleapis/python-pubsub/issues/1354)) ([820f986](https://github.com/googleapis/python-pubsub/commit/820f986104ca39fd0c92ba6816319e939be1ed63))
  * Deprecate `enabled` field for message transforms and add `disabled` field ([4363179](https://github.com/googleapis/python-pubsub/commit/43631790781ccfe071a7ecad41949399d3dbd063))
  * **samples:** Increase example max_bytes setting for cloud storage subscriptions to encourage more performant subscribe ([#1324](https://github.com/googleapis/python-pubsub/issues/1324)) ([cb760a7](https://github.com/googleapis/python-pubsub/commit/cb760a71cd4ad035d0c2c4c0f7b66bf52f18808c))



## March 17, 2025

Libraries

### Go

#### [1.48.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.47.0...pubsub/v1.48.0) (2025-03-12)

##### Features

  * **pubsub/pstest:** Support listening on custom address ([#11606](https://github.com/googleapis/google-cloud-go/issues/11606)) ([63865a2](https://github.com/googleapis/google-cloud-go/commit/63865a202b95fe0ab283b032b15b198f10188861))
  * **pubsub:** Add support for message transforms to Topic and Subscription ([59fe58a](https://github.com/googleapis/google-cloud-go/commit/59fe58aba61abf69bfb7549c0a03b21bdb4b8b2f))
  * **pubsub:** Deprecate `enabled` field for message transforms and add `disabled` field ([dd0d1d7](https://github.com/googleapis/google-cloud-go/commit/dd0d1d7b41884c9fc9b5fe808139cccd29e1e486))



##### Documentation

  * **pubsub:** A comment for field `code` in message `.google.pubsub.v1.JavaScriptUDF` is changed ([#11553](https://github.com/googleapis/google-cloud-go/issues/11553)) ([678944b](https://github.com/googleapis/google-cloud-go/commit/678944b30e389781687209caf3e3b9d35739a6f0))
  * **pubsub:** Deprecate `enabled` field for message transforms and add `disabled` field ([dd0d1d7](https://github.com/googleapis/google-cloud-go/commit/dd0d1d7b41884c9fc9b5fe808139cccd29e1e486))
  * **pubsub:** Fix link for AnalyticsHubSubscriptionInfo ([59fe58a](https://github.com/googleapis/google-cloud-go/commit/59fe58aba61abf69bfb7549c0a03b21bdb4b8b2f))



### Java

#### [1.138.0](https://github.com/googleapis/java-pubsub/compare/v1.137.1...v1.138.0) (2025-03-14)

##### Features

  * Deprecate `enabled` field for message transforms and add `disabled` field ([76b2a3d](https://github.com/googleapis/java-pubsub/commit/76b2a3dc1f001dfeb3f8974a4cc4de843b7383bc))
  * Next release from main branch is 1.138.0 ([#2361](https://github.com/googleapis/java-pubsub/issues/2361)) ([b6ba56c](https://github.com/googleapis/java-pubsub/commit/b6ba56c04619660d2660a660eaacbda7de9f8608))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.55.1 ([76b2a3d](https://github.com/googleapis/java-pubsub/commit/76b2a3dc1f001dfeb3f8974a4cc4de843b7383bc))
  * Prevent excessive string parsing when publishing and receiving messages to improve performance ([#2317](https://github.com/googleapis/java-pubsub/issues/2317)) ([07b1350](https://github.com/googleapis/java-pubsub/commit/07b135001b4726c9bafafe90c80d369f25f04956))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.48.1 ([#2356](https://github.com/googleapis/java-pubsub/issues/2356)) ([7d3d2e4](https://github.com/googleapis/java-pubsub/commit/7d3d2e4690539ebbe7ab521c2c345b06cba766ea))
  * Update dependency com.google.cloud:google-cloud-storage to v2.49.0 ([#2358](https://github.com/googleapis/java-pubsub/issues/2358)) ([81d3435](https://github.com/googleapis/java-pubsub/commit/81d34352d332ee9c4935e7908b6b9a2383d3a8ba))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.45.1 ([#2366](https://github.com/googleapis/java-pubsub/issues/2366)) ([15899d1](https://github.com/googleapis/java-pubsub/commit/15899d127131747c51c71c94d66ff581f70278f3))
  * Update googleapis/sdk-platform-java action to v2.55.1 ([#2367](https://github.com/googleapis/java-pubsub/issues/2367)) ([de6f84a](https://github.com/googleapis/java-pubsub/commit/de6f84a43a27e954c0dc635158c43c5db4d07dfa))



## March 04, 2025

Feature

Pub/Sub is now available in the `europe-north2` region (Stockholm, Sweden, Europe). For more information, see [Cloud locations](https://cloud.google.com/about/locations?_gl=1*lhbyi0*_ga*MTg1NTEwMDE4Ny4xNzQxMDE5MTkz*_ga_4LYFWVHBEB*MTc0MTAyNjM2MC4yLjEuMTc0MTAyNjY5OC4wLjAuMA..).

## March 03, 2025

Feature

You can now ingest streaming data into Pub/Sub by using an import topic, from the following external sources:

  * [Azure Event Hubs](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic)
  * [Amazon Managed Streaming for Apache Kafka (MSK)](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic)
  * [Confluent Cloud](https://docs.cloud.google.com/pubsub/docs/create-confluent-cloud-import-topic)



Libraries

### Java

#### [1.137.1](https://github.com/googleapis/java-pubsub/compare/v1.137.0...v1.137.1) (2025-02-26)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.54.0 ([ccf670f](https://github.com/googleapis/java-pubsub/commit/ccf670f9dc755770d40b9d1bf2c870c0452aa39e))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.48.0 ([#2343](https://github.com/googleapis/java-pubsub/issues/2343)) ([3bbd7e1](https://github.com/googleapis/java-pubsub/commit/3bbd7e1e812a7a00cfff36a0c1d8a5212d4e134a))
  * Update dependency com.google.cloud:google-cloud-core to v2.52.0 ([#2348](https://github.com/googleapis/java-pubsub/issues/2348)) ([f0977b4](https://github.com/googleapis/java-pubsub/commit/f0977b40479823ce5b7e90f864261f11115610ca))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.44.0 ([#2349](https://github.com/googleapis/java-pubsub/issues/2349)) ([90ed10b](https://github.com/googleapis/java-pubsub/commit/90ed10b474f7a59286365d8a6ad676d9a4f4113b))
  * Update googleapis/sdk-platform-java action to v2.54.0 ([#2347](https://github.com/googleapis/java-pubsub/issues/2347)) ([ac8db2d](https://github.com/googleapis/java-pubsub/commit/ac8db2dda6cd5f0bdf689052bb37cb2eaab08c46))



## February 17, 2025

Libraries

### Java

#### [1.137.0](https://github.com/googleapis/java-pubsub/compare/v1.136.1...v1.137.0) (2025-02-12)

##### Features

  * Add support for message transforms to Topic and Subscription ([3889a05](https://github.com/googleapis/java-pubsub/commit/3889a05a5c5d7479d3cc6b6dc0b0c425d41efd5d))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.53.0 ([b952e58](https://github.com/googleapis/java-pubsub/commit/b952e5826748bc680936a79b14d75f5873e6db06))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.47.0 ([#2331](https://github.com/googleapis/java-pubsub/issues/2331)) ([216feef](https://github.com/googleapis/java-pubsub/commit/216feef976595cd03e282f8d8effa2ac8430c419))
  * Update dependency com.google.cloud:google-cloud-core to v2.51.0 ([#2338](https://github.com/googleapis/java-pubsub/issues/2338)) ([ac2403e](https://github.com/googleapis/java-pubsub/commit/ac2403ecd21aad0d44c5b06fce2853f9a433adbd))
  * Update dependency com.google.cloud:google-cloud-storage to v2.48.1 ([#2332](https://github.com/googleapis/java-pubsub/issues/2332)) ([23fd7a8](https://github.com/googleapis/java-pubsub/commit/23fd7a8f4ab2438b72f3a6da5613f5deb0ac307e))
  * Update dependency com.google.cloud:google-cloud-storage to v2.48.2 ([#2341](https://github.com/googleapis/java-pubsub/issues/2341)) ([eeb99a9](https://github.com/googleapis/java-pubsub/commit/eeb99a997fa2e7154dcc228b964ff47867738122))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#2336](https://github.com/googleapis/java-pubsub/issues/2336)) ([996f4eb](https://github.com/googleapis/java-pubsub/commit/996f4ebdfa6b5cb38dbe37d4be981ca7d941bc0d))



##### Documentation

  * A comment for field `code` in message `.google.pubsub.v1.JavaScriptUDF` is changed ([3889a05](https://github.com/googleapis/java-pubsub/commit/3889a05a5c5d7479d3cc6b6dc0b0c425d41efd5d))



## February 03, 2025

Libraries

### Java

#### [1.136.1](https://github.com/googleapis/java-pubsub/compare/v1.136.0...v1.136.1) (2025-01-28)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.52.0 ([0d8c8bf](https://github.com/googleapis/java-pubsub/commit/0d8c8bffc85804d5a64ec0d35893ad9e0062807e))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.46.0 ([#2309](https://github.com/googleapis/java-pubsub/issues/2309)) ([97bd44e](https://github.com/googleapis/java-pubsub/commit/97bd44e04c440320e45c2b4336677d8d266a39a2))
  * Update dependency com.google.cloud:google-cloud-core to v2.49.1 ([#2300](https://github.com/googleapis/java-pubsub/issues/2300)) ([cf2822b](https://github.com/googleapis/java-pubsub/commit/cf2822b7363e13e4730753cbb5ca3510c77f5f55))
  * Update dependency com.google.cloud:google-cloud-core to v2.50.0 ([#2321](https://github.com/googleapis/java-pubsub/issues/2321)) ([5c40bcd](https://github.com/googleapis/java-pubsub/commit/5c40bcd4d401d919b990e6a7d3151660ead76eb0))
  * Update dependency com.google.cloud:google-cloud-storage to v2.47.0 ([#2303](https://github.com/googleapis/java-pubsub/issues/2303)) ([707f842](https://github.com/googleapis/java-pubsub/commit/707f84271559dfe96fa11edffb307df145ceea47))
  * Update dependency com.google.cloud:google-cloud-storage to v2.48.0 ([#2322](https://github.com/googleapis/java-pubsub/issues/2322)) ([93b9419](https://github.com/googleapis/java-pubsub/commit/93b9419d210cedeab03f408dab4c74c9fcf18b59))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.42.0 ([#2324](https://github.com/googleapis/java-pubsub/issues/2324)) ([84e8562](https://github.com/googleapis/java-pubsub/commit/84e856250867b2441cceed2315c312bd661c353c))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.29.3 ([#2302](https://github.com/googleapis/java-pubsub/issues/2302)) ([9e90e2c](https://github.com/googleapis/java-pubsub/commit/9e90e2ca26b2aea48563859358dde84640eb40d0))
  * Update dependency org.assertj:assertj-core to v3.27.3 ([#2313](https://github.com/googleapis/java-pubsub/issues/2313)) ([5e80b57](https://github.com/googleapis/java-pubsub/commit/5e80b57d2ffd58e6a0bb9f5e0e78bb46d6fe2530))
  * Update googleapis/sdk-platform-java action to v2.52.0 ([#2320](https://github.com/googleapis/java-pubsub/issues/2320)) ([01dd3de](https://github.com/googleapis/java-pubsub/commit/01dd3deaef392aa51c60d28c1f3cbb81bff2a5cb))



##### Documentation

  * Add samples and tests for ingestion from Kafka sources ([#2315](https://github.com/googleapis/java-pubsub/issues/2315)) ([eea603b](https://github.com/googleapis/java-pubsub/commit/eea603ba3f05be85d58a69cd5c3469e2088a7446))



### Go

#### [1.46.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.45.3...pubsub/v1.46.0) (2025-01-24)

##### Features

  * **pubsub:** Add Kafka-based sources to IngestionDataSourceSettings proto and IngestionFailureEvent proto ([e4e1a49](https://github.com/googleapis/google-cloud-go/commit/e4e1a498f21b0792e0a7662f82f9e062e5aa0fe9))



##### Bug Fixes

  * **pubsub:** Fix defer call in for loop ([#11175](https://github.com/googleapis/google-cloud-go/issues/11175)) ([7aec711](https://github.com/googleapis/google-cloud-go/commit/7aec711200d8e79686370f5d40915e21df7651a4))
  * **pubsub:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))



### Python

#### [2.28.0](https://github.com/googleapis/python-pubsub/compare/v2.27.3...v2.28.0) (2025-01-30)

##### Features

  * Add support for message transforms to Topic and Subscription ([#1274](https://github.com/googleapis/python-pubsub/issues/1274)) ([e5e2f3f](https://github.com/googleapis/python-pubsub/commit/e5e2f3f732f451d14dfb4c37ae979e5c04045305))



##### Bug Fixes

  * Get channel target for a gRPC request ([#1339](https://github.com/googleapis/python-pubsub/issues/1339)) ([16ea766](https://github.com/googleapis/python-pubsub/commit/16ea76611d121700a3f3119d18919063d12c81c1))
  * Set creds only if transport not provided ([#1348](https://github.com/googleapis/python-pubsub/issues/1348)) ([59965a4](https://github.com/googleapis/python-pubsub/commit/59965a4804a434467a47815cdbdd5ce31bbb3662))



### Go

#### [1.47.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.46.0...pubsub/v1.47.0) (2025-01-31)

##### Features

  * **pubsub:** Support new forms of topic ingestion ([#11537](https://github.com/googleapis/google-cloud-go/issues/11537)) ([46d6ed4](https://github.com/googleapis/google-cloud-go/commit/46d6ed475e6ae6b96f3e11e17496fd75fd8ea7c4))



## January 27, 2025

Libraries

### Python

#### [2.27.3](https://github.com/googleapis/python-pubsub/compare/v2.27.2...v2.27.3) (2025-01-24)

##### Bug Fixes

  * Stop using api_core default timeouts in publish since they are broken ([#1326](https://github.com/googleapis/python-pubsub/issues/1326)) ([ba2c2ee](https://github.com/googleapis/python-pubsub/commit/ba2c2eef7da89a3c14c14d9b6191cd8738c30341))



## January 13, 2025

Libraries

### Python

#### [2.27.2](https://github.com/googleapis/python-pubsub/compare/v2.27.1...v2.27.2) (2025-01-06)

##### Bug Fixes

  * Handle TransportError Exceptions thrown from gapic_publish ([#1318](https://github.com/googleapis/python-pubsub/issues/1318)) ([0e058c7](https://github.com/googleapis/python-pubsub/commit/0e058c73487384100847adcb2f4ab95a61c072c4))



### Java

#### [1.136.0](https://github.com/googleapis/java-pubsub/compare/v1.135.0...v1.136.0) (2025-01-10)

##### Features

  * Add Kafka-based sources to IngestionDataSourceSettings proto and IngestionFailureEvent proto ([2947169](https://github.com/googleapis/java-pubsub/commit/2947169c009fa553202bc1e44276cf5a7954cd96))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.1 ([9c166f7](https://github.com/googleapis/java-pubsub/commit/9c166f76db78b0c6b2e0218460d5c0336102717a))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.45.0 ([#2292](https://github.com/googleapis/java-pubsub/issues/2292)) ([79a8982](https://github.com/googleapis/java-pubsub/commit/79a89823c6cbcc9a718f44856040b1525863cab6))
  * Update dependency com.google.cloud:google-cloud-storage to v2.46.0 ([#2291](https://github.com/googleapis/java-pubsub/issues/2291)) ([7b60884](https://github.com/googleapis/java-pubsub/commit/7b60884cc4e17df616155f7530a056c4c5e3af29))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#2301](https://github.com/googleapis/java-pubsub/issues/2301)) ([53c1a8a](https://github.com/googleapis/java-pubsub/commit/53c1a8abdd3114e0f432b3b6618133fb93e44636))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.29.2 ([#2294](https://github.com/googleapis/java-pubsub/issues/2294)) ([48d4ac1](https://github.com/googleapis/java-pubsub/commit/48d4ac1ab2f0b9f9005292977c288f55322dd16a))
  * Update dependency org.assertj:assertj-core to v3.27.2 ([#2296](https://github.com/googleapis/java-pubsub/issues/2296)) ([e5b68a5](https://github.com/googleapis/java-pubsub/commit/e5b68a563aa6ebb2bd69665624fc7fc6aef50b64))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#2298](https://github.com/googleapis/java-pubsub/issues/2298)) ([16e0144](https://github.com/googleapis/java-pubsub/commit/16e0144d83c149b60e7b8fca6c4e61546d93462f))



## December 20, 2024

Announcement

Documentation is now available to help you troubleshoot Pub/Sub issues by using audit logs. You can use audit logs to troubleshoot issues related to identifying who created, deleted, or modified Pub/Sub resources, tracking configuration changes to topics or subscriptions, and verifying the existence and status of topics and subscriptions. For more information, see [Troubleshoot Pub/Sub issues with audit logs](https://docs.cloud.google.com/pubsub/docs/troubleshooting-audit-logs) and [General troubleshooting](https://docs.cloud.google.com/pubsub/docs/troubleshooting).

## December 19, 2024

Announcement

Documentation is now available to help you choose between Pub/Sub and Google Cloud Managed Service for Apache Kafka. The comparison is based on factors such as operational ease, portability, existing Kafka setup, and integration with other Google Cloud products. A detailed feature comparison table is also included. For more information, see [Choose Pub/Sub or Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/docs/choose-pubsub-kafka).

## December 16, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.135.0](https://github.com/googleapis/java-pubsub/compare/v1.134.2...v1.135.0) (2024-12-12)

##### Features

  * Introduce `java.time` variables and methods ([#2271](https://github.com/googleapis/java-pubsub/issues/2271)) ([7edfd9c](https://github.com/googleapis/java-pubsub/commit/7edfd9c315405c7703509fb9b7bc4f0d2686d870))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.0 ([0b0d52c](https://github.com/googleapis/java-pubsub/commit/0b0d52c8fca179a913a8b04d76b44748f1886f45))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.44.0 ([#2270](https://github.com/googleapis/java-pubsub/issues/2270)) ([a5f70a9](https://github.com/googleapis/java-pubsub/commit/a5f70a9c2397a2c8f4642729922b742a3df01ed6))
  * Update dependency com.google.cloud:google-cloud-core to v2.48.0 ([#2263](https://github.com/googleapis/java-pubsub/issues/2263)) ([d7e5588](https://github.com/googleapis/java-pubsub/commit/d7e55886b62826f54f0bb12a6bfa4ef67dee6521))
  * Update dependency com.google.cloud:google-cloud-core to v2.49.0 ([#2285](https://github.com/googleapis/java-pubsub/issues/2285)) ([cd94a19](https://github.com/googleapis/java-pubsub/commit/cd94a1987271eea4d7744286a7daeb071bb9456a))
  * Update dependency com.google.cloud:google-cloud-storage to v2.45.0 ([#2268](https://github.com/googleapis/java-pubsub/issues/2268)) ([80a09e6](https://github.com/googleapis/java-pubsub/commit/80a09e69111229080c413eff8426bd0b3d50458d))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.0 ([#2286](https://github.com/googleapis/java-pubsub/issues/2286)) ([0c0a1b9](https://github.com/googleapis/java-pubsub/commit/0c0a1b9231953e5c9878e0dfcf5a55d01794f6c4))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.29.0 ([#2276](https://github.com/googleapis/java-pubsub/issues/2276)) ([54ef88d](https://github.com/googleapis/java-pubsub/commit/54ef88d7f822d8130717e3be9bcf7fe9901d6cb0))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.29.1 ([#2279](https://github.com/googleapis/java-pubsub/issues/2279)) ([de3c9e1](https://github.com/googleapis/java-pubsub/commit/de3c9e1c7f2fe6413d0ae7a18955f16611df95c6))
  * Update googleapis/sdk-platform-java action to v2.51.0 ([#2284](https://github.com/googleapis/java-pubsub/issues/2284)) ([0be820e](https://github.com/googleapis/java-pubsub/commit/0be820e2044253bf484d88d703ce2dfade7aa137))



##### Documentation

  * Fix repository URL in samples README ([#2280](https://github.com/googleapis/java-pubsub/issues/2280)) ([8aeff1a](https://github.com/googleapis/java-pubsub/commit/8aeff1a375f3aa989d2c4bde0ed3dd2f329601fc))



## December 09, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.45.3](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.45.2...pubsub/v1.45.3) (2024-12-04)

##### Bug Fixes

  * **pubsub:** Convert stream ack deadline seconds from duration ([#11214](https://github.com/googleapis/google-cloud-go/issues/11214)) ([b2b05e4](https://github.com/googleapis/google-cloud-go/commit/b2b05e4515d8e59d7b3bf39432c6356b4450a17b))



#### [1.45.2](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.45.1...pubsub/v1.45.2) (2024-12-03)

##### Bug Fixes

  * **pubsub/pstest:** Make invalid filter return error instead of panic ([#11087](https://github.com/googleapis/google-cloud-go/issues/11087)) ([45e1ce7](https://github.com/googleapis/google-cloud-go/commit/45e1ce70e2757b78b868768b93e05da8858bab85))
  * **pubsub:** Only init batch span if trace enabled ([#11193](https://github.com/googleapis/google-cloud-go/issues/11193)) ([f843d50](https://github.com/googleapis/google-cloud-go/commit/f843d50f849c5014eba33d923085f0add41365a6))
  * **pubsub:** Use official semconv variable whenever possible ([#10904](https://github.com/googleapis/google-cloud-go/issues/10904)) ([1ce4b6d](https://github.com/googleapis/google-cloud-go/commit/1ce4b6dc31653ca6f28c50d5149d74b827caaeaa))



##### Documentation

  * **pubsub:** MinExtensionPeriod defaults to 60 seconds ([#10791](https://github.com/googleapis/google-cloud-go/issues/10791)) ([cc88fe1](https://github.com/googleapis/google-cloud-go/commit/cc88fe1c8d834903e2b5f8d3a7cc9bbd65c70b29))



## November 25, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.134.2](https://github.com/googleapis/java-pubsub/compare/v1.134.1...v1.134.2) (2024-11-18)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.49.0 ([77546e0](https://github.com/googleapis/java-pubsub/commit/77546e0548e72e331523fb4f30edd1577b5fe6ea))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.50.0 ([3f21af3](https://github.com/googleapis/java-pubsub/commit/3f21af3e3fbc6ef49ecbe80712350d8712133c59))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.43.3 ([#2256](https://github.com/googleapis/java-pubsub/issues/2256)) ([f7fbc6c](https://github.com/googleapis/java-pubsub/commit/f7fbc6c7e4f7d8a8b31d4778d2cd8c55efcb9be1))
  * Update dependency com.google.cloud:google-cloud-core to v2.47.0 ([#2249](https://github.com/googleapis/java-pubsub/issues/2249)) ([3df5729](https://github.com/googleapis/java-pubsub/commit/3df572918523738e8f2f28299efa811aa23e297b))
  * Update dependency com.google.cloud:google-cloud-storage to v2.44.1 ([#2240](https://github.com/googleapis/java-pubsub/issues/2240)) ([f8dae4d](https://github.com/googleapis/java-pubsub/commit/f8dae4d68c1835930d4e39522a354cdfcc4cdd84))
  * Update googleapis/sdk-platform-java action to v2.50.0 ([#2261](https://github.com/googleapis/java-pubsub/issues/2261)) ([d0aab7d](https://github.com/googleapis/java-pubsub/commit/d0aab7d157c628ff5b8787b8c75dfaedc7a7305f))
  * Update sdk platform java dependencies ([#2262](https://github.com/googleapis/java-pubsub/issues/2262)) ([b689fe2](https://github.com/googleapis/java-pubsub/commit/b689fe262b3a4c90264669ec87408bfeb6dc7659))



## November 18, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.9.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.8.0...v4.9.0) (2024-11-12)

##### Features

  * Add IngestionFailureEvent to the external proto ([#1984](https://github.com/googleapis/nodejs-pubsub/issues/1984)) ([7075430](https://github.com/googleapis/nodejs-pubsub/commit/70754309fb600c54d0a573f2d49ad4c419577550))



##### Bug Fixes

  * KiB, not MiB for ack size limits ([#1999](https://github.com/googleapis/nodejs-pubsub/issues/1999)) ([798270d](https://github.com/googleapis/nodejs-pubsub/commit/798270db9c5ef71f75c3e24e70d9592bbd068212))



Feature

Pub/Sub is now available in the `northamerica-south1` region (Querétaro, Mexico, North America). For more information, see [Cloud locations](https://cloud.google.com/about/locations).

## November 11, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.27.1](https://github.com/googleapis/python-pubsub/compare/v2.27.0...v2.27.1) (2024-11-08)

##### Bug Fixes

  * Add support for Python3.13 ([#1302](https://github.com/googleapis/python-pubsub/issues/1302)) ([ab22e27](https://github.com/googleapis/python-pubsub/commit/ab22e27954450b4e06ec98fe2e3458056aa8ca60))



## November 06, 2024

Feature

General availability: You can now create Cloud Storage import topics in Pub/Sub that lets you ingest data from Cloud Storage into Pub/Sub. The change is being rolled out in a phased manner over the rest of the week. For more information about Cloud Storage import topics, see [Create a Cloud Storage import topic ](https://docs.cloud.google.com/pubsub/docs/create-cloud-storage-import-topic).

Feature

General availability: You can now enable Google Cloud platform logs to help you troubleshoot issues when you are using Cloud Storage import topics to ingest data. For more information, see [Use platform logs to troubleshoot Cloud Storage import topics](https://docs.cloud.google.com/pubsub/docs/platform-logs-pubsub).

## November 04, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.134.1](https://github.com/googleapis/java-pubsub/compare/v1.134.0...v1.134.1) (2024-10-26)

##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.39.0 ([#2251](https://github.com/googleapis/java-pubsub/issues/2251)) ([083cc7c](https://github.com/googleapis/java-pubsub/commit/083cc7c930fa2728d2322c1343b0fc025f9e255d))
  * Update googleapis/sdk-platform-java action to v2.49.0 ([#2250](https://github.com/googleapis/java-pubsub/issues/2250)) ([af0f194](https://github.com/googleapis/java-pubsub/commit/af0f194369d4a9f16dd14378aa90280adc194d98))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.27.0](https://github.com/googleapis/python-pubsub/compare/v2.26.1...v2.27.0) (2024-11-02)

##### Features

  * Add support for Python 3.13 ([#1281](https://github.com/googleapis/python-pubsub/issues/1281)) ([0b46a33](https://github.com/googleapis/python-pubsub/commit/0b46a3321d6f19cd72e4f2ccdba73d062c7bd832))



##### Bug Fixes

  * Mark test_streaming_pull_max_messages flaky ([#1288](https://github.com/googleapis/python-pubsub/issues/1288)) ([d6635a0](https://github.com/googleapis/python-pubsub/commit/d6635a00dc2c614dd8608ef32ad4e79f9124e040))



## October 28, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.45.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.45.0...pubsub/v1.45.1) (2024-10-24)

##### Bug Fixes

  * **pubsub:** Update google.golang.org/api to v0.203.0 ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))
  * **pubsub:** WARNING: On approximately Dec 1, 2024, an update to Protobuf will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go files. This change is expected to affect very few if any users of this client library. For more information, see https://togithub.com/googleapis/google-cloud-go/issues/11020. ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))



##### Documentation

  * **pubsub:** Add doc links to top level package doc ([#11029](https://github.com/googleapis/google-cloud-go/issues/11029)) ([fe2ec56](https://github.com/googleapis/google-cloud-go/commit/fe2ec569029d2052885063b6fca90e1a27424b4e))



#### [1.45.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.44.0...pubsub/v1.45.0) (2024-10-22)

##### Features

  * **pubsub:** Add IngestionFailureEvent to the external proto ([f0b05e2](https://github.com/googleapis/google-cloud-go/commit/f0b05e260435d5e8889b9a0ca0ab215fcde169ab))
  * **pubsub:** Add support for ingestion platform logging settings ([#10969](https://github.com/googleapis/google-cloud-go/issues/10969)) ([c60241f](https://github.com/googleapis/google-cloud-go/commit/c60241f46db2b021d799f621851a352f2baec96e))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.134.0](https://github.com/googleapis/java-pubsub/compare/v1.133.1...v1.134.0) (2024-10-23)

##### Features

  * Add IngestionFailureEvent to the external proto ([6c67798](https://github.com/googleapis/java-pubsub/commit/6c67798c6b7442d77eb30fbba874344f32a926b4))
  * Track batch size using serialized size of PublishRequest ([#2113](https://github.com/googleapis/java-pubsub/issues/2113)) ([be78e64](https://github.com/googleapis/java-pubsub/commit/be78e64f9fdfc9ddf0790189311fac673754e219))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.43.1 ([#2202](https://github.com/googleapis/java-pubsub/issues/2202)) ([acaf5f2](https://github.com/googleapis/java-pubsub/commit/acaf5f2e3686a939d4b972c73a4d039142f753df))
  * Update dependency com.google.cloud:google-cloud-core to v2.46.0 ([#2238](https://github.com/googleapis/java-pubsub/issues/2238)) ([dc06d54](https://github.com/googleapis/java-pubsub/commit/dc06d5456ab6fe8d94b7b845ca9159391949517f))
  * Update dependency com.google.cloud:google-cloud-storage to v2.43.2 ([#2226](https://github.com/googleapis/java-pubsub/issues/2226)) ([eb87c04](https://github.com/googleapis/java-pubsub/commit/eb87c04619f7bdaf59ce2b562a96b8c25d3c8196))
  * Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.33.0 ([#2225](https://github.com/googleapis/java-pubsub/issues/2225)) ([cc1b072](https://github.com/googleapis/java-pubsub/commit/cc1b0726009524ddee3c2ce7f1446608dd3bc752))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.28.3 ([#2237](https://github.com/googleapis/java-pubsub/issues/2237)) ([75abe83](https://github.com/googleapis/java-pubsub/commit/75abe83a9b14c2e5cc3f136ff97b5340bfa904db))
  * Update dependency org.apache.avro:avro to v1.11.4 [security](https://docs.cloud.google.com/pubsub/docs/release-notes/%5B#2223%5D\(https://github.com/googleapis/java-pubsub/issues/2223\)%7B:%20.external%20target=%22_blank%22%20rel=%22noreferrer%20noopener%22%7D) ([31f276b](https://github.com/googleapis/java-pubsub/commit/31f276b10a96c53ecbd828972a9e3457c0c7c700))
  * Update sdk platform java dependencies ([#2239](https://github.com/googleapis/java-pubsub/issues/2239)) ([8f4f855](https://github.com/googleapis/java-pubsub/commit/8f4f8556414aaef731a7226dcbffe59d91819775))



##### Documentation

  * Add OpenTelemetry samples ([#2208](https://github.com/googleapis/java-pubsub/issues/2208)) ([c447fe5](https://github.com/googleapis/java-pubsub/commit/c447fe500ba48ba4fde27d97f10ef7664d09363b))



## October 21, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.8.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.7.2...v4.8.0) (2024-10-15)

##### Features

  * Add ingestion Cloud Storage fields and Platform Logging fields to Topic ([#1974](https://github.com/googleapis/nodejs-pubsub/issues/1974)) ([afec9a1](https://github.com/googleapis/nodejs-pubsub/commit/afec9a1ad3f665a71f08e748623f0fdaa332d17b))
  * Return listing information for subscriptions created via Analytics Hub ([afec9a1](https://github.com/googleapis/nodejs-pubsub/commit/afec9a1ad3f665a71f08e748623f0fdaa332d17b))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.26.1](https://github.com/googleapis/python-pubsub/compare/v2.26.0...v2.26.1) (2024-10-10)

##### Documentation

  * Add ingestion from GCS sample ([#1273](https://github.com/googleapis/python-pubsub/issues/1273)) ([b59cc8d](https://github.com/googleapis/python-pubsub/commit/b59cc8d4fae593eb7592455a1696d7ab996a53dd))



## October 14, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.44.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.43.0...pubsub/v1.44.0) (2024-10-08)

##### Features

  * **pubsub:** Add ingestion Cloud Storage fields and Platform Logging fields to Topic ([7250d71](https://github.com/googleapis/google-cloud-go/commit/7250d714a638dcd5df3fbe0e91c5f1250c3f80f9))
  * **pubsub:** Add support for cloud storage ingestion topics ([#10959](https://github.com/googleapis/google-cloud-go/issues/10959)) ([1a11675](https://github.com/googleapis/google-cloud-go/commit/1a116759ce0d25fdcb5776bf73c52408ae1ec985))
  * **pubsub:** Return listing information for subscriptions created via Analytics Hub ([fdb4ea9](https://github.com/googleapis/google-cloud-go/commit/fdb4ea99189657880e5f0e0dce16bef1c3aa0d2f))



##### Documentation

  * **pubsub:** Update documentation for 31 day subscription message retention ([#10845](https://github.com/googleapis/google-cloud-go/issues/10845)) ([9b4b2fa](https://github.com/googleapis/google-cloud-go/commit/9b4b2fa87864906aeae3a8fda460466f951bc6c9))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.133.1](https://github.com/googleapis/java-pubsub/compare/v1.133.0...v1.133.1) (2024-10-07)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.47.0 ([ccd23af](https://github.com/googleapis/java-pubsub/commit/ccd23afd99e7cb5a28747b06d0a97d1cb8163391))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.45.0 ([#2213](https://github.com/googleapis/java-pubsub/issues/2213)) ([5ee969b](https://github.com/googleapis/java-pubsub/commit/5ee969bb9ed873073895881062ec72f419bbc837))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.37.0 ([#2214](https://github.com/googleapis/java-pubsub/issues/2214)) ([d938709](https://github.com/googleapis/java-pubsub/commit/d93870934f610cffb705837ed8391eb276a18c05))
  * Update googleapis/sdk-platform-java action to v2.47.0 ([#2212](https://github.com/googleapis/java-pubsub/issues/2212)) ([6a9723d](https://github.com/googleapis/java-pubsub/commit/6a9723d2872c82bbb525119cac7471d1a2f3b7cd))



##### Documentation

  * Add ingestion from GCS sample ([#2211](https://github.com/googleapis/java-pubsub/issues/2211)) ([ddb7391](https://github.com/googleapis/java-pubsub/commit/ddb739113b38d4e2f4617a105cd0ab071f21d4de))
  * Update emulator sample to create a topic and publish to it ([#2039](https://github.com/googleapis/java-pubsub/issues/2039)) ([21d5cfc](https://github.com/googleapis/java-pubsub/commit/21d5cfc3b9484ffc2c1a0084b8bc2f6f76b6bf62))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.26.0](https://github.com/googleapis/python-pubsub/compare/v2.25.2...v2.26.0) (2024-10-09)

##### Features

  * Add ingestion Cloud Storage fields and Platform Logging fields to Topic ([#1248](https://github.com/googleapis/python-pubsub/issues/1248)) ([a7a4caa](https://github.com/googleapis/python-pubsub/commit/a7a4caaa5a73e9b15369471dc892688e24bf52e0))



## October 07, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.133.0](https://github.com/googleapis/java-pubsub/compare/v1.132.4...v1.133.0) (2024-10-01)

##### Features

  * Add OpenTelemetry tracing to the Publisher and Subscriber ([#2086](https://github.com/googleapis/java-pubsub/issues/2086)) ([db522b6](https://github.com/googleapis/java-pubsub/commit/db522b60f1bbec9cc1bfa0c37477044fd2f807c7))



##### Dependencies

  * Update dependency com.google.cloud.opentelemetry:exporter-trace to v0.32.0 ([#2205](https://github.com/googleapis/java-pubsub/issues/2205)) ([76f17e4](https://github.com/googleapis/java-pubsub/commit/76f17e4149bf369f2be12fe9d316a23a7f49f137))
  * Update dependency org.assertj:assertj-core to v3.26.3 ([#2204](https://github.com/googleapis/java-pubsub/issues/2204)) ([71c2e76](https://github.com/googleapis/java-pubsub/commit/71c2e762e94895c465c4e737ed8bf7bc583a9c14))



#### [1.132.4](https://github.com/googleapis/java-pubsub/compare/v1.132.3...v1.132.4) (2024-09-30)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-storage to v2.43.1 ([#2194](https://github.com/googleapis/java-pubsub/issues/2194)) ([979e420](https://github.com/googleapis/java-pubsub/commit/979e420377327cf3843ac23151d8b44a7e5188c5))
  * Update dependency ubuntu to v24 ([#2193](https://github.com/googleapis/java-pubsub/issues/2193)) ([f295b01](https://github.com/googleapis/java-pubsub/commit/f295b01cb93fe26612c79c3d2ba0bb68f0404d7e))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.25.2](https://github.com/googleapis/python-pubsub/compare/v2.25.1...v2.25.2) (2024-09-30)

##### Documentation

  * Add command line args for OpenTelemetry Subscribe sample ([#1265](https://github.com/googleapis/python-pubsub/issues/1265)) ([0ff7f2a](https://github.com/googleapis/python-pubsub/commit/0ff7f2a64b5aa1b0e014e0933e4edaef0fb3f222))



## October 01, 2024

Feature

Pub/Sub adds support for [OpenTelemetry tracing](https://docs.cloud.google.com/pubsub/docs/open-telemetry-tracing). OpenTelemetry tracing lets you identify and trace the latency of various Pub/Sub client library operations.

## September 30, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.25.1](https://github.com/googleapis/python-pubsub/compare/v2.25.0...v2.25.1) (2024-09-29)

##### Bug Fixes

  * Update the requirements.txt for samples directory ([#1263](https://github.com/googleapis/python-pubsub/issues/1263)) ([5cce8b1](https://github.com/googleapis/python-pubsub/commit/5cce8b103ab7085613b7ee0efb5c8342d41ebae1))



Feature

The message retention duration option for a subscription specifies how long Pub/Sub retains messages after publication. The maximum value for this property is now increased to 31 days. For more information, see [Message retention duration](https://docs.cloud.google.com/pubsub/docs/subscription-properties#message-retention-duration).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.132.3](https://github.com/googleapis/java-pubsub/compare/v1.132.2...v1.132.3) (2024-09-26)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.42.3 ([#2173](https://github.com/googleapis/java-pubsub/issues/2173)) ([294d039](https://github.com/googleapis/java-pubsub/commit/294d03974ab236c2ee5d0e420e8913eb6fc65fc9))
  * Update dependency com.google.cloud:google-cloud-core to v2.44.0 ([#2184](https://github.com/googleapis/java-pubsub/issues/2184)) ([faecb3b](https://github.com/googleapis/java-pubsub/commit/faecb3b90cb259ae376b8481ec30511ce19279bf))
  * Update dependency com.google.cloud:google-cloud-core to v2.44.1 ([#2190](https://github.com/googleapis/java-pubsub/issues/2190)) ([9ea45dc](https://github.com/googleapis/java-pubsub/commit/9ea45dc13f11076890cfff35e7acf2eafc2af70a))
  * Update dependency com.google.cloud:google-cloud-storage to v2.43.0 ([#2174](https://github.com/googleapis/java-pubsub/issues/2174)) ([ae800d7](https://github.com/googleapis/java-pubsub/commit/ae800d7b3ffd19302b416f03fad8b20e93afce8f))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.36.0 ([#2185](https://github.com/googleapis/java-pubsub/issues/2185)) ([5ca2c7c](https://github.com/googleapis/java-pubsub/commit/5ca2c7c52497514af30e4522f0ae245d0f8d73ce))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.36.1 ([#2191](https://github.com/googleapis/java-pubsub/issues/2191)) ([555216e](https://github.com/googleapis/java-pubsub/commit/555216ee5bf9cfbba6664f133fc7cde1101f5f0b))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.28.2 ([#2179](https://github.com/googleapis/java-pubsub/issues/2179)) ([c9bbd2c](https://github.com/googleapis/java-pubsub/commit/c9bbd2cf3525e3ebdf9ce3af7fe50a16a87c9837))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.25.0](https://github.com/googleapis/python-pubsub/compare/v2.24.0...v2.25.0) (2024-09-28)

##### Features

  * Add OpenTelemetry publish sample ([#1258](https://github.com/googleapis/python-pubsub/issues/1258)) ([bc13ff0](https://github.com/googleapis/python-pubsub/commit/bc13ff05c3d1104c17169c360bdc09340430da37))



#### [2.24.0](https://github.com/googleapis/python-pubsub/compare/v2.23.1...v2.24.0) (2024-09-24)

##### Features

  * Add OpenTelemetry support for Subscribe Side ([#1252](https://github.com/googleapis/python-pubsub/issues/1252)) ([1b6f3d2](https://github.com/googleapis/python-pubsub/commit/1b6f3d284095e138943576de8551df263f73a506))
  * Open Telemetry Publish Side Support ([#1241](https://github.com/googleapis/python-pubsub/issues/1241)) ([bb5f3d1](https://github.com/googleapis/python-pubsub/commit/bb5f3d1a7df2d661cccc336edc8eceb2161c6921))



##### Bug Fixes

  * Fix flaky test ([#1254](https://github.com/googleapis/python-pubsub/issues/1254)) ([1ae49de](https://github.com/googleapis/python-pubsub/commit/1ae49de09996a5cf19f592f996c46e0222d540fc))



## September 16, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.7.2](https://github.com/googleapis/nodejs-pubsub/compare/v4.7.1...v4.7.2) (2024-09-13)

##### Bug Fixes

  * Set MaxBytes for AckQueue ([#1963](https://github.com/googleapis/nodejs-pubsub/issues/1963)) ([5945563](https://github.com/googleapis/nodejs-pubsub/commit/594556315f159f4197ffc0e7249ce1b0339c12ec))



### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.43.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.42.0...pubsub/v1.43.0) (2024-09-09)

##### Features

  * **pubsub:** Add support for Go 1.23 iterators ([84461c0](https://github.com/googleapis/google-cloud-go/commit/84461c0ba464ec2f951987ba60030e37c8a8fc18))
  * **pubsub:** Allow trace extraction from protobuf message ([#10827](https://github.com/googleapis/google-cloud-go/issues/10827)) ([caa826c](https://github.com/googleapis/google-cloud-go/commit/caa826cea826473ebf4c806b57b0c3b0a2f0f365))



##### Bug Fixes

  * **pubsub:** Add attributes before startSpan ([#10800](https://github.com/googleapis/google-cloud-go/issues/10800)) ([48addbf](https://github.com/googleapis/google-cloud-go/commit/48addbff725ee2bb226ce0ab926415c27fd4ffad))
  * **pubsub:** Bump dependencies ([2ddeb15](https://github.com/googleapis/google-cloud-go/commit/2ddeb1544a53188a7592046b98913982f1b0cf04))
  * **pubsub:** Close grpc streams on retry ([#10624](https://github.com/googleapis/google-cloud-go/issues/10624)) ([79a0e11](https://github.com/googleapis/google-cloud-go/commit/79a0e118c88190cbe1b56250a75b67bd98b0d7f2))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.132.2](https://github.com/googleapis/java-pubsub/compare/v1.132.1...v1.132.2) (2024-09-11)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.42.1 ([#2152](https://github.com/googleapis/java-pubsub/issues/2152)) ([1457489](https://github.com/googleapis/java-pubsub/commit/1457489cb51c12bc7ad8ab8ddcf2252a2f513a79))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.42.2 ([#2157](https://github.com/googleapis/java-pubsub/issues/2157)) ([d671347](https://github.com/googleapis/java-pubsub/commit/d671347004a68c53cdf3fdfb9d1a7ed992ee162f))
  * Update dependency com.google.cloud:google-cloud-core to v2.43.0 ([#2161](https://github.com/googleapis/java-pubsub/issues/2161)) ([05a37b7](https://github.com/googleapis/java-pubsub/commit/05a37b786686c24f87eec5e9919c16b2b67465be))
  * Update dependency com.google.cloud:google-cloud-storage to v2.42.0 ([#2145](https://github.com/googleapis/java-pubsub/issues/2145)) ([77c3e78](https://github.com/googleapis/java-pubsub/commit/77c3e78d34e894c05653371027cd2b1d12cea9d0))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.35.0 ([#2162](https://github.com/googleapis/java-pubsub/issues/2162)) ([27eaffd](https://github.com/googleapis/java-pubsub/commit/27eaffd5fa55789b456eaeba98f6800343f3685e))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.27.4 ([#2153](https://github.com/googleapis/java-pubsub/issues/2153)) ([32c78b3](https://github.com/googleapis/java-pubsub/commit/32c78b31e7a904fb6b6a2b55f81e7e3ab7525add))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.28.0 ([#2155](https://github.com/googleapis/java-pubsub/issues/2155)) ([5f61fe1](https://github.com/googleapis/java-pubsub/commit/5f61fe13f6fea1d30ab0e85be0221e70056369f6))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.28.1 ([#2167](https://github.com/googleapis/java-pubsub/issues/2167)) ([bb8ea71](https://github.com/googleapis/java-pubsub/commit/bb8ea717ed0234fdbb582f2915a016fd37657448))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.7 ([#2165](https://github.com/googleapis/java-pubsub/issues/2165)) ([e7fb60e](https://github.com/googleapis/java-pubsub/commit/e7fb60ecccb8bb9fbc6147210491a52ee0f5a817))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.23.1](https://github.com/googleapis/python-pubsub/compare/v2.23.0...v2.23.1) (2024-09-09)

##### Bug Fixes

  * Replace asserts with None checks for graceful shutdown ([#1244](https://github.com/googleapis/python-pubsub/issues/1244)) ([ced4f52](https://github.com/googleapis/python-pubsub/commit/ced4f527c7f918a87d1b89c2b5da59dbdf00e2c3))



## September 09, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.7.1](https://github.com/googleapis/nodejs-pubsub/compare/v4.7.0...v4.7.1) (2024-08-26)

##### Bug Fixes

  * **deps:** Update dependency @opentelemetry/semantic-conventions to ~1.26.0 ([#1945](https://github.com/googleapis/nodejs-pubsub/issues/1945)) ([f082869](https://github.com/googleapis/nodejs-pubsub/commit/f082869a185c059463654c76c744e44e7b28415e))
  * **deps:** Update dependency protobufjs to ~7.4.0 ([#1959](https://github.com/googleapis/nodejs-pubsub/issues/1959)) ([25946e0](https://github.com/googleapis/nodejs-pubsub/commit/25946e0d4fe794202984cdad6cf48121f72063cf))
  * Propagate set options to LeaseManager (from https://github.com/googleapis/nodejs-pubsub/pull/1880) ([#1954](https://github.com/googleapis/nodejs-pubsub/issues/1954)) ([cdb0916](https://github.com/googleapis/nodejs-pubsub/commit/cdb0916bd30da67f5153c9aead09e7f505954253))



## September 02, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.7.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.6.0...v4.7.0) (2024-08-24)

##### Features

  * Add support for OTel context propagation and harmonized spans ([#1833](https://github.com/googleapis/nodejs-pubsub/issues/1833)) ([4b5c90d](https://github.com/googleapis/nodejs-pubsub/commit/4b5c90dc334e90cefb4da3c6fe9ce027b50aacb8))



## August 26, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.6.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.5.0...v4.6.0) (2024-07-12)

##### Features

  * Add max messages batching for Cloud Storage subscriptions ([#1956](https://github.com/googleapis/nodejs-pubsub/issues/1956)) ([90546f6](https://github.com/googleapis/nodejs-pubsub/commit/90546f634cc4e510185e20a4d1ba1c74ebc59b85))
  * Add use_topic_schema for Cloud Storage Subscriptions ([#1948](https://github.com/googleapis/nodejs-pubsub/issues/1948)) ([120fa1b](https://github.com/googleapis/nodejs-pubsub/commit/120fa1bca0516185e109260c69ea91eb7ddeecd0))



##### Bug Fixes

  * **docs samples:** Update missing argv in sample metadata for push subscription ([#1946](https://github.com/googleapis/nodejs-pubsub/issues/1946)) ([34b8c03](https://github.com/googleapis/nodejs-pubsub/commit/34b8c03f90618ba6ae506764b9d97d9db84dcada))



### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.42.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.41.0...pubsub/v1.42.0) (2024-08-19)

##### Features

  * **pubsub:** Add opentelemetry tracing support ([#10709](https://github.com/googleapis/google-cloud-go/issues/10709)) ([bbd3366](https://github.com/googleapis/google-cloud-go/commit/bbd3366b01afc28c6137668c29d2895738ed849d))



##### Bug Fixes

  * **pubsub:** Update google.golang.org/api to v0.191.0 ([5b32644](https://github.com/googleapis/google-cloud-go/commit/5b32644eb82eb6bd6021f80b4fad471c60fb9d73))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.132.1](https://github.com/googleapis/java-pubsub/compare/v1.132.0...v1.132.1) (2024-08-20)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.42.0 ([#2140](https://github.com/googleapis/java-pubsub/issues/2140)) ([80dca35](https://github.com/googleapis/java-pubsub/commit/80dca35cebb1061f3d2a852ff9929519e69283cc))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.34.0 ([#2141](https://github.com/googleapis/java-pubsub/issues/2141)) ([273fbf3](https://github.com/googleapis/java-pubsub/commit/273fbf3f752444a397b0e743c5c6de1a539291ea))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.27.3 ([#2127](https://github.com/googleapis/java-pubsub/issues/2127)) ([8523b4f](https://github.com/googleapis/java-pubsub/commit/8523b4f67f45ac219671c0d588bac7e9dc450dcb))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.6 ([#2135](https://github.com/googleapis/java-pubsub/issues/2135)) ([102ff84](https://github.com/googleapis/java-pubsub/commit/102ff844594687b3bbaca1ff92e650fe9e8d3f1e))



## August 20, 2024

Feature

BigQuery subscriptions with `use table schema` enabled now support type conversions for `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `NUMERIC`, and `BIGNUMERIC` data types. For more information about these conversions, see the [Use table schema documentation](https://docs.cloud.google.com/pubsub/docs/subscription-properties#use-table-schema).

Feature

Pub/Sub has increased the limit on schema definition size to 300 KB. For more information, see [Resource limits](https://docs.cloud.google.com/pubsub/quotas#resource_limits).

Feature

Cloud Storage subscriptions now support using the schema of the Pub/Sub topic to which the subscription is attached when writing Avro files. For more information, see the [file format documentation](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription#file_format).

## August 05, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

Beta release for the pubsub opentelemetry tracing feature

OpenTelemetry tracing standards are in active development, and thus attributes, links, and span names are EXPERIMENTAL and subject to change or removal without notice.

#### [1.41.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.40.0...pubsub/v1.41.0) (2024-08-01)

##### Features

  * **pubsub/pstest:** Add Message.Topic field and populate on publish ([#10510](https://github.com/googleapis/google-cloud-go/issues/10510)) ([01bf051](https://github.com/googleapis/google-cloud-go/commit/01bf0519093f2e9d6a579bcb312004eba0fbd895))
  * **pubsub:** Add max messages batching for Cloud Storage subscriptions ([1bb4c84](https://github.com/googleapis/google-cloud-go/commit/1bb4c846ec1ff37f394afb1684823ea76c18d16e))



##### Bug Fixes

  * **pubsub:** Bump google.golang.org/api@v0.187.0 ([8fa9e39](https://github.com/googleapis/google-cloud-go/commit/8fa9e398e512fd8533fd49060371e61b5725a85b))
  * **pubsub:** Bump google.golang.org/grpc@v1.64.1 ([8ecc4e9](https://github.com/googleapis/google-cloud-go/commit/8ecc4e9622e5bbe9b90384d5848ab816027226c5))
  * **pubsub:** Update dependencies ([257c40b](https://github.com/googleapis/google-cloud-go/commit/257c40bd6d7e59730017cf32bda8823d7a232758))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.132.0](https://github.com/googleapis/java-pubsub/compare/v1.131.0...v1.132.0) (2024-08-01)

##### Features

  * Enable hermetic library generation ([#2048](https://github.com/googleapis/java-pubsub/issues/2048)) ([283a5e8](https://github.com/googleapis/java-pubsub/commit/283a5e89837071678f8dd94b8b8adfad91a6766c))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.41.0 ([#2093](https://github.com/googleapis/java-pubsub/issues/2093)) ([217b8a3](https://github.com/googleapis/java-pubsub/commit/217b8a3f5419f80402d349b8873d7302eeb35e3f))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.42.0 ([#2124](https://github.com/googleapis/java-pubsub/issues/2124)) ([24ebe24](https://github.com/googleapis/java-pubsub/commit/24ebe2402fe6278348d87b5a4259c365a819877f))
  * Update dependency com.google.cloud:google-cloud-core to v2.41.0 ([#2120](https://github.com/googleapis/java-pubsub/issues/2120)) ([1f6428a](https://github.com/googleapis/java-pubsub/commit/1f6428a8b79369a239664b9ea7cd38e024db9724))
  * Update dependency com.google.cloud:google-cloud-storage to v2.40.1 ([#2095](https://github.com/googleapis/java-pubsub/issues/2095)) ([0d64d6c](https://github.com/googleapis/java-pubsub/commit/0d64d6cf7799a176297ceaa1475b7cb29a64bebc))
  * Update dependency com.google.cloud:google-cloud-storage to v2.41.0 ([#2129](https://github.com/googleapis/java-pubsub/issues/2129)) ([2348d20](https://github.com/googleapis/java-pubsub/commit/2348d2022bc400b7f187d3db7f43aff94d8884a8))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.33.0 ([#2121](https://github.com/googleapis/java-pubsub/issues/2121)) ([7fbea6d](https://github.com/googleapis/java-pubsub/commit/7fbea6d0c922dd3485f19eafccc42869efd0e5ed))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.27.2 ([#2091](https://github.com/googleapis/java-pubsub/issues/2091)) ([9859f11](https://github.com/googleapis/java-pubsub/commit/9859f1181a12bc683eaf4a6345bf2528a5463c59))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.10.3 ([#2096](https://github.com/googleapis/java-pubsub/issues/2096)) ([42f12ed](https://github.com/googleapis/java-pubsub/commit/42f12ed3270e66beae316deb729b445c94dcb1a8))



##### Documentation

  * **samples:** Optimistic subscribe sample ([#2063](https://github.com/googleapis/java-pubsub/issues/2063)) ([53a4844](https://github.com/googleapis/java-pubsub/commit/53a4844f09eace777142b8cdcd06bc07cef0b432))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.23.0](https://github.com/googleapis/python-pubsub/compare/v2.22.0...v2.23.0) (2024-07-29)

##### Features

  * Add max messages batching for Cloud Storage subscriptions ([#1224](https://github.com/googleapis/python-pubsub/issues/1224)) ([91c89d3](https://github.com/googleapis/python-pubsub/commit/91c89d36c5099591408ab0661c55929e786b1b04))



## July 22, 2024

Change

If you retain unacknowledged messages in a subscription for more than 24 hours, you incur additional charges. For more information, see [Storage costs](https://cloud.google.com/pubsub/pricing#storage_costs).

## July 08, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.22.0](https://github.com/googleapis/python-pubsub/compare/v2.21.5...v2.22.0) (2024-07-06)

##### Features

  * Add service_account_email for export subscriptions ([ec0cc34](https://github.com/googleapis/python-pubsub/commit/ec0cc349b344b6882979838171b6cae4209a9b02))
  * Add use_topic_schema for Cloud Storage Subscriptions ([ec0cc34](https://github.com/googleapis/python-pubsub/commit/ec0cc349b344b6882979838171b6cae4209a9b02))



## July 01, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.40.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.39.0...pubsub/v1.40.0) (2024-06-26)

##### Features

  * **pubsub:** Add client ID to initial streaming pull request ([#10436](https://github.com/googleapis/google-cloud-go/issues/10436)) ([a3d70ed](https://github.com/googleapis/google-cloud-go/commit/a3d70ed0bf3b4bfe2544d86db05b11b4b51cf754))
  * **pubsub:** Add use_topic_schema for Cloud Storage Subscriptions ([d6c543c](https://github.com/googleapis/google-cloud-go/commit/d6c543c3969016c63e158a862fc173dff60fb8d9))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.131.0](https://github.com/googleapis/java-pubsub/compare/v1.130.1...v1.131.0) (2024-06-25)

##### Features

  * Add use_topic_schema for Cloud Storage Subscriptions ([#2082](https://github.com/googleapis/java-pubsub/issues/2082)) ([11d67d4](https://github.com/googleapis/java-pubsub/commit/11d67d44152ccca008dda071683d9932c59af41d))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.40.0 ([#2087](https://github.com/googleapis/java-pubsub/issues/2087)) ([26b01c9](https://github.com/googleapis/java-pubsub/commit/26b01c921f2700947a1653702be0234cf84cccef))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.32.0 ([#2088](https://github.com/googleapis/java-pubsub/issues/2088)) ([aebc3ed](https://github.com/googleapis/java-pubsub/commit/aebc3ed779e0847077742dedc7c2c0a9d8a1ab10))



Feature

Public preview: Data publishers can now [share Pub/Sub topics and manage subscriptions](https://docs.cloud.google.com/bigquery/docs/analytics-hub-stream-sharing) in Analytics Hub.

## June 24, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.39.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.38.0...pubsub/v1.39.0) (2024-06-18)

##### Features

  * **pubsub/pstest:** Add support to register other servers into grpc.Server ([#9722](https://github.com/googleapis/google-cloud-go/issues/9722)) ([db8216e](https://github.com/googleapis/google-cloud-go/commit/db8216e54c8d9d23dd90bc47a081eb2754f7c92a))
  * **pubsub:** Add service_account_email for export subscriptions ([92dc381](https://github.com/googleapis/google-cloud-go/commit/92dc381da281197567a2c9eb8dc941292000a3da))
  * **pubsub:** Batch receipt modacks ([#10234](https://github.com/googleapis/google-cloud-go/issues/10234)) ([4c2cd10](https://github.com/googleapis/google-cloud-go/commit/4c2cd10fb73b7167c15d6dc24162ad0dac01ce8e))
  * **pubsub:** Make lease management RPCs concurrent ([#10238](https://github.com/googleapis/google-cloud-go/issues/10238)) ([426a8c2](https://github.com/googleapis/google-cloud-go/commit/426a8c27a9d11f24e8c331b6375f87d29829e021))



##### Bug Fixes

  * **pubsub:** Closes [#10094](https://github.com/googleapis/google-cloud-go/issues/10094) \- memory leak in pubsub receive ([#10153](https://github.com/googleapis/google-cloud-go/issues/10153)) ([66581c4](https://github.com/googleapis/google-cloud-go/commit/66581c44f2309984475fe5053fa11707f6f93b8d))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.21.5](https://github.com/googleapis/python-pubsub/compare/v2.21.4...v2.21.5) (2024-06-20)

##### Bug Fixes

  * Allow Protobuf 5.x ([a369f04](https://github.com/googleapis/python-pubsub/commit/a369f04c46e4b3db34dcf8cc2ef7cda4ea491e26))



#### [2.21.4](https://github.com/googleapis/python-pubsub/compare/v2.21.3...v2.21.4) (2024-06-18)

##### Documentation

  * **samples:** Add code sample for optimistic subscribe ([#1182](https://github.com/googleapis/python-pubsub/issues/1182)) ([d8e8aa5](https://github.com/googleapis/python-pubsub/commit/d8e8aa59ab0288fdaf5a1cc5e476581e73d0f82c))



## June 17, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.5.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.4.1...v4.5.0) (2024-06-11)

##### Features

  * Add service_account_email for export subscriptions ([#1927](https://github.com/googleapis/nodejs-pubsub/issues/1927)) ([c532854](https://github.com/googleapis/nodejs-pubsub/commit/c53285473c2c0973baf5932e52d2d135958c6948))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.130.1](https://github.com/googleapis/java-pubsub/compare/v1.130.0...v1.130.1) (2024-06-13)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.40.3 ([#2071](https://github.com/googleapis/java-pubsub/issues/2071)) ([0844bfb](https://github.com/googleapis/java-pubsub/commit/0844bfb0a500ae0b4a0f63fcb45ffffeaf609e3d))
  * Update dependency com.google.cloud:google-cloud-storage to v2.40.0 ([#2066](https://github.com/googleapis/java-pubsub/issues/2066)) ([dfcaeb5](https://github.com/googleapis/java-pubsub/commit/dfcaeb5b59466d86ac5b5bf74655ce359e7d5713))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.27.1 ([#2065](https://github.com/googleapis/java-pubsub/issues/2065)) ([6baf69a](https://github.com/googleapis/java-pubsub/commit/6baf69a99adb75fba49c2289bca3ffd08720f8f4))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.21.3](https://github.com/googleapis/python-pubsub/compare/v2.21.2...v2.21.3) (2024-06-10)

##### Bug Fixes

  * Race condition where future callbacks invoked before client is in paused state ([#1145](https://github.com/googleapis/python-pubsub/issues/1145)) ([d12bac6](https://github.com/googleapis/python-pubsub/commit/d12bac6d94b337aa8978006600fb00e5b13d741d))
  * Suppress warnings caused during pytest runs ([#1189](https://github.com/googleapis/python-pubsub/issues/1189)) ([cd51149](https://github.com/googleapis/python-pubsub/commit/cd51149c9e0d3c59d1c75395c05308e860908bf9))
  * Typecheck errors in samples/snippets/subscriber.py ([#1186](https://github.com/googleapis/python-pubsub/issues/1186)) ([3698450](https://github.com/googleapis/python-pubsub/commit/3698450041cb4db0e2957832c24450f674b89c11))



## June 10, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.130.0](https://github.com/googleapis/java-pubsub/compare/v1.129.7...v1.130.0) (2024-06-03)

##### Features

  * [java] allow passing libraries_bom_version from env ([#1967](https://github.com/googleapis/java-pubsub/issues/1967)) ([#2033](https://github.com/googleapis/java-pubsub/issues/2033)) ([825c5f8](https://github.com/googleapis/java-pubsub/commit/825c5f83e0fd2fd6b1f4856b9c555d71110a03e1))
  * Add service_account_email for export subscriptions ([#2054](https://github.com/googleapis/java-pubsub/issues/2054)) ([670db3e](https://github.com/googleapis/java-pubsub/commit/670db3e1b665e6f5aec3cd7bf3639e9242f20151))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.39.0 ([#2057](https://github.com/googleapis/java-pubsub/issues/2057)) ([43446d2](https://github.com/googleapis/java-pubsub/commit/43446d22ad2140f1b18fd1dde5dab03a901580bc))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.31.0 ([#2058](https://github.com/googleapis/java-pubsub/issues/2058)) ([a998ef5](https://github.com/googleapis/java-pubsub/commit/a998ef5359942486ea47bfd50f154314ae37be33))



## June 03, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.4.1](https://github.com/googleapis/nodejs-pubsub/compare/v4.4.0...v4.4.1) (2024-05-30)

##### Bug Fixes

  * An existing message `UpdateVehicleLocationRequest` is removed ([5451d15](https://github.com/googleapis/nodejs-pubsub/commit/5451d150e77d46a475e7a8e150a7f6b5d04d6448))
  * An existing method `SearchFuzzedVehicles` is removed from service `VehicleService` ([5451d15](https://github.com/googleapis/nodejs-pubsub/commit/5451d150e77d46a475e7a8e150a7f6b5d04d6448))
  * An existing method `UpdateVehicleLocation` is removed from service `VehicleService` ([5451d15](https://github.com/googleapis/nodejs-pubsub/commit/5451d150e77d46a475e7a8e150a7f6b5d04d6448))
  * **deps:** Update dependency protobufjs to ~7.3.0 ([#1921](https://github.com/googleapis/nodejs-pubsub/issues/1921)) ([c5afd34](https://github.com/googleapis/nodejs-pubsub/commit/c5afd3400cc8ff9f920b4b232c4e4a5fb41eb07b))
  * Pull in new gax for protobufjs vuln fix ([#1925](https://github.com/googleapis/nodejs-pubsub/issues/1925)) ([8024c6d](https://github.com/googleapis/nodejs-pubsub/commit/8024c6d2e4ce69f97fd8b64bb9f076e33d47c662))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.129.7](https://github.com/googleapis/java-pubsub/compare/v1.129.6...v1.129.7) (2024-05-29)

##### Dependencies

  * Change scope of grpc-inprocess dependency from runtime to test ([#2038](https://github.com/googleapis/java-pubsub/issues/2038)) ([1ab45c9](https://github.com/googleapis/java-pubsub/commit/1ab45c9eaee35d4bfeb332244c74f1253b77c166))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.40.2 ([#2046](https://github.com/googleapis/java-pubsub/issues/2046)) ([f81c5e1](https://github.com/googleapis/java-pubsub/commit/f81c5e1b977e6da19aac6a40c1389ddcc4643e3c))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.27.0 ([#2044](https://github.com/googleapis/java-pubsub/issues/2044)) ([37e94ce](https://github.com/googleapis/java-pubsub/commit/37e94ce13a2998b5e3f69e9ad3d4ab68af108d64))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.21.2](https://github.com/googleapis/python-pubsub/compare/v2.21.1...v2.21.2) (2024-05-30)

##### Bug Fixes

  * Test failures due to grpcio changes ([#1178](https://github.com/googleapis/python-pubsub/issues/1178)) ([086dd46](https://github.com/googleapis/python-pubsub/commit/086dd4660ec56d9ff2d41a32ec0b8e8dc44acc55))



## May 27, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.129.6](https://github.com/googleapis/java-pubsub/compare/v1.129.5...v1.129.6) (2024-05-23)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-storage to v2.39.0 ([#2040](https://github.com/googleapis/java-pubsub/issues/2040)) ([eb6bd9c](https://github.com/googleapis/java-pubsub/commit/eb6bd9c559073429d8338b9d8fa83e0e3f61b8e9))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.2 ([#2035](https://github.com/googleapis/java-pubsub/issues/2035)) ([40fdd7a](https://github.com/googleapis/java-pubsub/commit/40fdd7a71aa07d6c64ac6f96d7c6642af3563280))



## May 20, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.129.5](https://github.com/googleapis/java-pubsub/compare/v1.129.4...v1.129.5) (2024-05-16)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.38.1 ([#2027](https://github.com/googleapis/java-pubsub/issues/2027)) ([535edf6](https://github.com/googleapis/java-pubsub/commit/535edf6496700bc5c5fb0b5cfa1cac6be5d62875))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.30.1 ([#2028](https://github.com/googleapis/java-pubsub/issues/2028)) ([aedcffd](https://github.com/googleapis/java-pubsub/commit/aedcffdaedbaa30627c96f96bfa5430bd4666cf0))



## May 13, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.4.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.3.3...v4.4.0) (2024-05-03)

##### Features

  * Add several fields to manage state of database encryption update ([#1904](https://github.com/googleapis/nodejs-pubsub/issues/1904)) ([aba9aee](https://github.com/googleapis/nodejs-pubsub/commit/aba9aee0c8ecc840c150aa077892b7bb88f18eca))



##### Bug Fixes

  * **deps:** Update dependency @types/long to v5 ([#1901](https://github.com/googleapis/nodejs-pubsub/issues/1901)) ([d13d395](https://github.com/googleapis/nodejs-pubsub/commit/d13d395341efacf926a126bf756873922f6bbab7))



### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.38.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.37.0...pubsub/v1.38.0) (2024-05-06)

##### Features

  * **pubsub:** Add custom datetime format for Cloud Storage subscriptions ([4834425](https://github.com/googleapis/google-cloud-go/commit/48344254a5d21ec51ffee275c78a15c9345dc09c))
  * **pubsub:** Support publisher compression ([#9711](https://github.com/googleapis/google-cloud-go/issues/9711)) ([4940c3c](https://github.com/googleapis/google-cloud-go/commit/4940c3c5ab31b6e66ec8f29f9cf60298f8de630a))
  * **pubsub:** Use Streaming Pull response for ordering check ([#9682](https://github.com/googleapis/google-cloud-go/issues/9682)) ([7bf4904](https://github.com/googleapis/google-cloud-go/commit/7bf49049cdc44ca260d1c1354bc7661de9ed8585))



##### Bug Fixes

  * **pubsub:** Bump x/net to v0.24.0 ([ba31ed5](https://github.com/googleapis/google-cloud-go/commit/ba31ed5fda2c9664f2e1cf972469295e63deb5b4))
  * **pubsub:** Respect gRPC dial option when PUBSUB_EMULATOR_HOST is set ([#10040](https://github.com/googleapis/google-cloud-go/issues/10040)) ([95bf6b2](https://github.com/googleapis/google-cloud-go/commit/95bf6b255d8ff7bb385567da498b90252efb338f))
  * **pubsub:** Update protobuf dep to v1.33.0 ([30b038d](https://github.com/googleapis/google-cloud-go/commit/30b038d8cac0b8cd5dd4761c87f3f298760dd33a))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.129.4](https://github.com/googleapis/java-pubsub/compare/v1.129.3...v1.129.4) (2024-05-10)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.40.0 ([#2016](https://github.com/googleapis/java-pubsub/issues/2016)) ([beee523](https://github.com/googleapis/java-pubsub/commit/beee523ffc501a33b99a4ee82ccdb04b83391403))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.40.1 ([#2021](https://github.com/googleapis/java-pubsub/issues/2021)) ([0873594](https://github.com/googleapis/java-pubsub/commit/0873594c000f470c6193ebe8b4d091701670ef06))
  * Update dependency com.google.cloud:google-cloud-storage to v2.38.0 ([#2019](https://github.com/googleapis/java-pubsub/issues/2019)) ([ba3dffc](https://github.com/googleapis/java-pubsub/commit/ba3dffc3ac8cf173362307c24bc46e815c64db40))



#### [1.129.3](https://github.com/googleapis/java-pubsub/compare/v1.129.2...v1.129.3) (2024-05-06)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.38.0 ([#2011](https://github.com/googleapis/java-pubsub/issues/2011)) ([4a547d0](https://github.com/googleapis/java-pubsub/commit/4a547d08d02f3abaf23bfb8e5ed65e40c131bb94))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.30.0 ([#2012](https://github.com/googleapis/java-pubsub/issues/2012)) ([811d0e6](https://github.com/googleapis/java-pubsub/commit/811d0e609b5eb6eaf9c921828255407d9db68293))



## May 06, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.129.2](https://github.com/googleapis/java-pubsub/compare/v1.129.1...v1.129.2) (2024-04-30)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.39.1 ([#2006](https://github.com/googleapis/java-pubsub/issues/2006)) ([a7f4afb](https://github.com/googleapis/java-pubsub/commit/a7f4afbc870536a7964594bc1d5b9a2eb5076cce))



## April 29, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.129.1](https://github.com/googleapis/java-pubsub/compare/v1.129.0...v1.129.1) (2024-04-25)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.39.0 ([#2000](https://github.com/googleapis/java-pubsub/issues/2000)) ([09ee49a](https://github.com/googleapis/java-pubsub/commit/09ee49a8304089f4388cfbde58127d46fe07a5a1))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.39.0 ([#2002](https://github.com/googleapis/java-pubsub/issues/2002)) ([88517fe](https://github.com/googleapis/java-pubsub/commit/88517fe69a7a9577aa79b693957bf56a56d0980c))
  * Update dependency com.google.cloud:google-cloud-core to v2.37.0 ([#1997](https://github.com/googleapis/java-pubsub/issues/1997)) ([b4573ae](https://github.com/googleapis/java-pubsub/commit/b4573ae6c93ca47bc802616ae3715fc10163bf2e))
  * Update dependency com.google.cloud:google-cloud-storage to v2.37.0 ([#1999](https://github.com/googleapis/java-pubsub/issues/1999)) ([cff6d6a](https://github.com/googleapis/java-pubsub/commit/cff6d6a5fc297eb5254a409d495bda458dfebcd6))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.29.0 ([#1998](https://github.com/googleapis/java-pubsub/issues/1998)) ([bb80924](https://github.com/googleapis/java-pubsub/commit/bb80924e55bc97db82650d4ae2bdebf406c68f98))



## April 22, 2024

Fixed

Resolved an issue where Pub/Sub pull RPCs incorrectly return a "cancelled" status when the configured deadline is reached in the absence of a backlog. This fix ensures deadlines are honored.

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.129.0](https://github.com/googleapis/java-pubsub/compare/v1.128.1...v1.129.0) (2024-04-17)

##### Features

  * Add `libraries_bom_version` in metadata ([#1956](https://github.com/googleapis/java-pubsub/issues/1956)) ([#1990](https://github.com/googleapis/java-pubsub/issues/1990)) ([18cfa73](https://github.com/googleapis/java-pubsub/commit/18cfa73208bdf9b6a1a597bac740056abfcb03ef))



##### Dependencies

  * Update actions/setup-java action to v4 ([#1978](https://github.com/googleapis/java-pubsub/issues/1978)) ([64a0df3](https://github.com/googleapis/java-pubsub/commit/64a0df337c91f965e4d8960801e10f90f78c46cd))



## April 15, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

This is the second preview release of the Pub/Sub client that includes OpenTelemetry Tracing.

#### CHANGES

  * Fix leak of ackIDs in `activeSpans` map
  * Allow passing of context into user callback
  * Align attributes for batch operation spans (publish, ack, nack, modack) with that of the main message spans



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.128.1](https://github.com/googleapis/java-pubsub/compare/v1.128.0...v1.128.1) (2024-04-10)

##### Dependencies

  * Update actions/checkout action to v4 ([#1975](https://github.com/googleapis/java-pubsub/issues/1975)) ([618abdd](https://github.com/googleapis/java-pubsub/commit/618abdd44dd9670a5d6a1ca3c923e3d0621c6248))
  * Update actions/github-script action to v7 ([#1976](https://github.com/googleapis/java-pubsub/issues/1976)) ([c836172](https://github.com/googleapis/java-pubsub/commit/c8361722544ec4170b94651e77b02634938c7883))



## April 11, 2024

Feature

If you use Pub/Sub metrics as a signal to autoscale your pipeline, refer to [Best practices for using Pub/Sub metrics as a scaling signal](https://docs.cloud.google.com/pubsub/docs/metrics-autoscaling-best-practices).

## April 08, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.128.0](https://github.com/googleapis/java-pubsub/compare/v1.127.3...v1.128.0) (2024-04-03)

##### Features

  * Add custom datetime format for Cloud Storage subscriptions ([#1970](https://github.com/googleapis/java-pubsub/issues/1970)) ([7113f06](https://github.com/googleapis/java-pubsub/commit/7113f065973bb8b56ab811e0589ffb7975873679))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.38.2 ([#1965](https://github.com/googleapis/java-pubsub/issues/1965)) ([ec3b386](https://github.com/googleapis/java-pubsub/commit/ec3b38665ddc6336f975d597d27c4aa25732c474))
  * Update dependency com.google.cloud:google-cloud-storage to v2.36.1 ([#1968](https://github.com/googleapis/java-pubsub/issues/1968)) ([524109c](https://github.com/googleapis/java-pubsub/commit/524109c1afc5118c79fd97769e194a1325322107))
  * Update dependency com.google.protobuf:protobuf-java-util to v4.26.1 ([#1972](https://github.com/googleapis/java-pubsub/issues/1972)) ([53c1120](https://github.com/googleapis/java-pubsub/commit/53c112033dc721cf91aceddfc1eeb3c6daddb45e))



##### Documentation

  * Add Kinesis ingestion samples ([#1947](https://github.com/googleapis/java-pubsub/issues/1947)) ([5b5c14b](https://github.com/googleapis/java-pubsub/commit/5b5c14ba31636c037c2b8d6a166bd48670e23688))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.21.1](https://github.com/googleapis/python-pubsub/compare/v2.21.0...v2.21.1) (2024-04-04)

##### Bug Fixes

  * Set timeout to infinite for publishing with ordering keys enabled ([#1134](https://github.com/googleapis/python-pubsub/issues/1134)) ([67daf3c](https://github.com/googleapis/python-pubsub/commit/67daf3c64239d22eabe59c3df214057a4e59a39e))



Feature

You can now ingest streaming data from Amazon Kinesis Data Streams into Pub/Sub by using an import topic. For more information about import topics, including required roles and permissions and how to create an import topic, see [Create an import topic](https://docs.cloud.google.com/pubsub/docs/create-import-topic). The change is being rolled out in a phased manner over the rest of the week.

## April 01, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.21.0](https://github.com/googleapis/python-pubsub/compare/v2.20.3...v2.21.0) (2024-03-26)

##### Features

  * Add custom datetime format for Cloud Storage subscriptions ([#1131](https://github.com/googleapis/python-pubsub/issues/1131)) ([4da6744](https://github.com/googleapis/python-pubsub/commit/4da67441ddab01a173620d8c03bc640271c785c6))



## March 25, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.127.3](https://github.com/googleapis/java-pubsub/compare/v1.127.2...v1.127.3) (2024-03-20)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.36.0 ([#1955](https://github.com/googleapis/java-pubsub/issues/1955)) ([d25d14a](https://github.com/googleapis/java-pubsub/commit/d25d14ad4694c5a914f9d07018cb0f6b9af4f9aa))
  * Update dependency com.google.cloud:google-cloud-core to v2.36.1 ([#1962](https://github.com/googleapis/java-pubsub/issues/1962)) ([96c1c97](https://github.com/googleapis/java-pubsub/commit/96c1c971fa4dced85cb2ed4e9db3e3fb47eb82c6))
  * Update dependency com.google.cloud:google-cloud-storage to v2.36.0 ([#1957](https://github.com/googleapis/java-pubsub/issues/1957)) ([0d8c182](https://github.com/googleapis/java-pubsub/commit/0d8c182653ea1ffd429465e91075760c1501eb34))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.28.0 ([#1956](https://github.com/googleapis/java-pubsub/issues/1956)) ([183df2c](https://github.com/googleapis/java-pubsub/commit/183df2caeed8e0df53ef9668232e4949ec4719a9))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.28.1 ([#1960](https://github.com/googleapis/java-pubsub/issues/1960)) ([faa45a4](https://github.com/googleapis/java-pubsub/commit/faa45a4efeaee5b45f9a4cc89dc2917f56a66797))
  * Update dependency com.google.protobuf:protobuf-java-util to v4 ([#1951](https://github.com/googleapis/java-pubsub/issues/1951)) ([243ec9a](https://github.com/googleapis/java-pubsub/commit/243ec9ab47212bbe701b16882c92a9b3d5d4aeaa))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.20.3](https://github.com/googleapis/python-pubsub/compare/v2.20.2...v2.20.3) (2024-03-21)

##### Documentation

  * **samples:** Update Region Tags ([#1128](https://github.com/googleapis/python-pubsub/issues/1128)) ([e3bc89e](https://github.com/googleapis/python-pubsub/commit/e3bc89eaa51337c93144d6c3100486353d494ad9))



## March 18, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

This is a beta release of the Pub/Sub client that includes OpenTelemetry Tracing.

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.20.2](https://github.com/googleapis/python-pubsub/compare/v2.20.1...v2.20.2) (2024-03-15)

##### Documentation

  * **samples:** Add Create Topic with Kinesis IngestionDataSourceSettings Sample ([#1120](https://github.com/googleapis/python-pubsub/issues/1120)) ([83dc9ff](https://github.com/googleapis/python-pubsub/commit/83dc9fff13aa35518fb9b6a73472816da852d975))
  * **samples:** Update Topic with Kinesis Ingestion Settings ([#1123](https://github.com/googleapis/python-pubsub/issues/1123)) ([e0e2d83](https://github.com/googleapis/python-pubsub/commit/e0e2d831da8d17288c3ae8900bea2388ce8758af))



## March 11, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.127.2](https://github.com/googleapis/java-pubsub/compare/v1.127.1...v1.127.2) (2024-03-10)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.37.0 ([#1938](https://github.com/googleapis/java-pubsub/issues/1938)) ([1435c4e](https://github.com/googleapis/java-pubsub/commit/1435c4e4d25d789fadbfc2c54c2f90b138693b40))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.38.1 ([#1944](https://github.com/googleapis/java-pubsub/issues/1944)) ([76317e1](https://github.com/googleapis/java-pubsub/commit/76317e1fe60467b4bbe9b4867d0a29e983ce687f))
  * Update dependency com.google.cloud:google-cloud-storage to v2.35.0 ([#1942](https://github.com/googleapis/java-pubsub/issues/1942)) ([989f7ba](https://github.com/googleapis/java-pubsub/commit/989f7bac5bada7ac5d6e68c742af0290cb757e4b))
  * Update dependency com.google.cloud:google-cloud-storage to v2.35.0 ([#1946](https://github.com/googleapis/java-pubsub/issues/1946)) ([b94989d](https://github.com/googleapis/java-pubsub/commit/b94989df6c5ae6f62e648016cef2e008a3b9ed05))



Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.3.3](https://github.com/googleapis/nodejs-pubsub/compare/v4.3.2...v4.3.3) (2024-03-03)

##### Bug Fixes

  * Add client library version to headers ([#1891](https://github.com/googleapis/nodejs-pubsub/issues/1891)) ([6b59195](https://github.com/googleapis/nodejs-pubsub/commit/6b59195aed8b6c6576e50512aeca9123ad0cc016))



### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.37.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.36.2...pubsub/v1.37.0) (2024-03-07)

##### Features

  * **pubsub:** Support kinesis ingestion admin ([#9458](https://github.com/googleapis/google-cloud-go/issues/9458)) ([9bba269](https://github.com/googleapis/google-cloud-go/commit/9bba269d1c3165c312871903fbd649c08b3809fb))



##### Documentation

  * **pubsub:** Check for nil responses for receive examples ([#9516](https://github.com/googleapis/google-cloud-go/issues/9516)) ([6deb969](https://github.com/googleapis/google-cloud-go/commit/6deb96914ecbdaaea521c175db4c2ee1f223590c))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.127.1](https://github.com/googleapis/java-pubsub/compare/v1.127.0...v1.127.1) (2024-03-04)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.38.0 ([#1931](https://github.com/googleapis/java-pubsub/issues/1931)) ([357c901](https://github.com/googleapis/java-pubsub/commit/357c901029a8bc5fb9800a7fae6f3d93080c0a0d))
  * Update dependency com.google.cloud:google-cloud-core to v2.35.0 ([#1936](https://github.com/googleapis/java-pubsub/issues/1936)) ([785e6d1](https://github.com/googleapis/java-pubsub/commit/785e6d1e4f2234d2c49183fc06d3f73de537171b))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.27.0 ([#1937](https://github.com/googleapis/java-pubsub/issues/1937)) ([75e7e5e](https://github.com/googleapis/java-pubsub/commit/75e7e5e9eede53e87a6bc8ccda957990ea9b0673))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.20.1](https://github.com/googleapis/python-pubsub/compare/v2.20.0...v2.20.1) (2024-03-06)

##### Bug Fixes

  * Catch and surface BaseException() ([#1108](https://github.com/googleapis/python-pubsub/issues/1108)) ([07e427f](https://github.com/googleapis/python-pubsub/commit/07e427f675464b9aa79c68dede67082529054980))



#### [2.20.0](https://github.com/googleapis/python-pubsub/compare/v2.19.8...v2.20.0) (2024-03-05)

##### Features

  * Add include_recaptcha_script for as a new action in firewall policies ([#1109](https://github.com/googleapis/python-pubsub/issues/1109)) ([54041a5](https://github.com/googleapis/python-pubsub/commit/54041a527398eb0ec5daa97a346ba3202ce349f3))



##### Documentation

  * **samples:** Correct type and description of `timeout` parameter in subscriber quickstart ([#1051](https://github.com/googleapis/python-pubsub/issues/1051)) ([141a473](https://github.com/googleapis/python-pubsub/commit/141a473561bd0e45d3137a02cbefddb454ab3af4))



#### [2.19.8](https://github.com/googleapis/python-pubsub/compare/v2.19.7...v2.19.8) (2024-03-05)

##### Bug Fixes

  * **deps:** Exclude google-auth 2.24.0 and 2.25.0 ([#1102](https://github.com/googleapis/python-pubsub/issues/1102)) ([165c983](https://github.com/googleapis/python-pubsub/commit/165c983803c48a17141765395cf9ec2e6a7056fa))



## March 04, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.36.2](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.36.1...pubsub/v1.36.2) (2024-02-28)

##### Bug Fixes

  * **pubsub:** Fix out of order issue when exactly once is enabled ([#9472](https://github.com/googleapis/google-cloud-go/issues/9472)) ([e89fd6c](https://github.com/googleapis/google-cloud-go/commit/e89fd6cc3b4489537c71cca1e40547313c24924b))



##### Documentation

  * **pubsub:** Small fix in Pub/Sub ingestion comments ([a86aa8e](https://github.com/googleapis/google-cloud-go/commit/a86aa8e962b77d152ee6cdd433ad94967150ef21))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.127.0](https://github.com/googleapis/java-pubsub/compare/v1.126.6...v1.127.0) (2024-02-28)

##### Features

  * Add an API method for reordering firewall policies ([#1868](https://github.com/googleapis/java-pubsub/issues/1868)) ([2039f7e](https://github.com/googleapis/java-pubsub/commit/2039f7e9bee9db1991fae1118e4a6b8ad88ea30c))
  * Add universe domain support for Java ([#1904](https://github.com/googleapis/java-pubsub/issues/1904)) ([1e316d3](https://github.com/googleapis/java-pubsub/commit/1e316d33d2b7c87f6b76580cd9f905fe90a664c7))
  * Next release from main branch is 1.126.0 ([#1933](https://github.com/googleapis/java-pubsub/issues/1933)) ([255d8bc](https://github.com/googleapis/java-pubsub/commit/255d8bca3509e9a9dc2d82c95fabb32590423565))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.37.2 ([#1918](https://github.com/googleapis/java-pubsub/issues/1918)) ([b8846f9](https://github.com/googleapis/java-pubsub/commit/b8846f9dbf71854af1379c40669e017dd4e005d1))
  * Update dependency com.google.cloud:google-cloud-storage to v2.34.0 ([#1917](https://github.com/googleapis/java-pubsub/issues/1917)) ([4a7d6b9](https://github.com/googleapis/java-pubsub/commit/4a7d6b971f0d16d867c56679d1e7bfbba4e4a67a))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.25.3 ([#1919](https://github.com/googleapis/java-pubsub/issues/1919)) ([4bf13bb](https://github.com/googleapis/java-pubsub/commit/4bf13bb5f346a53ecf8e1e73e5f3b6d1c99ddf93))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.1 ([#1923](https://github.com/googleapis/java-pubsub/issues/1923)) ([cd704bd](https://github.com/googleapis/java-pubsub/commit/cd704bd57b2596d82f2f791476a109a771995b4d))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.19.7](https://github.com/googleapis/python-pubsub/compare/v2.19.6...v2.19.7) (2024-02-24)

##### Bug Fixes

  * **deps:** Require `google-api-core&gt;=1.34.1` ([#1080](https://github.com/googleapis/python-pubsub/issues/1080)) ([1a5a134](https://github.com/googleapis/python-pubsub/commit/1a5a1342de8736c6a2b1ac63476667f8a02b5bb8))



## February 26, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.19.6](https://github.com/googleapis/python-pubsub/compare/v2.19.5...v2.19.6) (2024-02-23)

##### Bug Fixes

  * Remove LOGGER.exception() line ([#1087](https://github.com/googleapis/python-pubsub/issues/1087)) ([a395d26](https://github.com/googleapis/python-pubsub/commit/a395d26ed0fffaee8662f988da97dd35c480af4f))



#### [2.19.5](https://github.com/googleapis/python-pubsub/compare/v2.19.4...v2.19.5) (2024-02-22)

##### Bug Fixes

  * Update system_test_python_versions ([#1096](https://github.com/googleapis/python-pubsub/issues/1096)) ([c659ac7](https://github.com/googleapis/python-pubsub/commit/c659ac777f177e54d7272a8de93fa9f554b15d46))



## February 22, 2024

Feature

If you have filtering enabled, the backlog metrics only include data from messages that match the filter. To learn more, see [How filters affect backlog metrics](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter#filters-metrics).

## February 19, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.3.2](https://github.com/googleapis/nodejs-pubsub/compare/v4.3.1...v4.3.2) (2024-02-13)

##### Bug Fixes

  * Update minimum google-gax versions for auth fixes ([#1888](https://github.com/googleapis/nodejs-pubsub/issues/1888)) ([08acade](https://github.com/googleapis/nodejs-pubsub/commit/08acadee042c6a3b85344575d5d0be09ae6e4202))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.126.6](https://github.com/googleapis/java-pubsub/compare/v1.126.5...v1.126.6) (2024-02-14)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.33.0 ([#1912](https://github.com/googleapis/java-pubsub/issues/1912)) ([9691c6f](https://github.com/googleapis/java-pubsub/commit/9691c6fabd82eb07fcb5135019be8d6fb260ce6f))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.25.0 ([#1913](https://github.com/googleapis/java-pubsub/issues/1913)) ([9636c55](https://github.com/googleapis/java-pubsub/commit/9636c5526e5cf4507bed69349321b686ddf7ab27))



#### [1.126.5](https://github.com/googleapis/java-pubsub/compare/v1.126.4...v1.126.5) (2024-02-12)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.37.1 ([#1898](https://github.com/googleapis/java-pubsub/issues/1898)) ([fc0dc96](https://github.com/googleapis/java-pubsub/commit/fc0dc962bcb7467fe4008263a80d1ed1e29167a0))
  * Update dependency com.google.cloud:google-cloud-storage to v2.33.0 ([#1900](https://github.com/googleapis/java-pubsub/issues/1900)) ([0efceb4](https://github.com/googleapis/java-pubsub/commit/0efceb4f4068c70565676dc2ddcf629ec4f0489f))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.10.0 ([#1887](https://github.com/googleapis/java-pubsub/issues/1887)) ([2bfa5cc](https://github.com/googleapis/java-pubsub/commit/2bfa5cc894e5a14b1d890bdcad348eeb14520f95))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.0 ([#1888](https://github.com/googleapis/java-pubsub/issues/1888)) ([5017789](https://github.com/googleapis/java-pubsub/commit/5017789c996246ece0c5428c68c9c6681b760bca))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.10.2 ([#1891](https://github.com/googleapis/java-pubsub/issues/1891)) ([231ba51](https://github.com/googleapis/java-pubsub/commit/231ba51c8bd2e6a8f3e0171626d35761bd07ae19))



## February 12, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.3.1](https://github.com/googleapis/nodejs-pubsub/compare/v4.3.0...v4.3.1) (2024-02-08)

##### Bug Fixes

  * Add option to disable emulator auth handling (temp fix) ([#1861](https://github.com/googleapis/nodejs-pubsub/issues/1861)) ([761cdc8](https://github.com/googleapis/nodejs-pubsub/commit/761cdc898c69715e6775d2f5913ead1fca2def02))



#### [4.3.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.2.0...v4.3.0) (2024-02-05)

##### Features

  * Trusted Private Cloud support, use the universeDomain parameter ([#1878](https://github.com/googleapis/nodejs-pubsub/issues/1878)) ([d89fd1d](https://github.com/googleapis/nodejs-pubsub/commit/d89fd1d90b352f0cc7a50a72c5fec4aab6660f8f))



##### Bug Fixes

  * Updated google-gax required for TPC ([#1882](https://github.com/googleapis/nodejs-pubsub/issues/1882)) ([1445856](https://github.com/googleapis/nodejs-pubsub/commit/144585699595b97f1a4cc28551e45fe23305f480))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.126.4](https://github.com/googleapis/java-pubsub/compare/v1.126.3...v1.126.4) (2024-02-09)

##### Bug Fixes

  * Message ordering fix for [#1889](https://github.com/googleapis/java-pubsub/issues/1889) ([#1903](https://github.com/googleapis/java-pubsub/issues/1903)) ([22a87c6](https://github.com/googleapis/java-pubsub/commit/22a87c67f07b55266e277f83f5ceb17d9f32f67e))



#### [1.126.3](https://github.com/googleapis/java-pubsub/compare/v1.126.2...v1.126.3) (2024-02-08)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.32.0 ([#1885](https://github.com/googleapis/java-pubsub/issues/1885)) ([a2063cf](https://github.com/googleapis/java-pubsub/commit/a2063cf8f1f792f5ad1994bff00f367b399c0ff2))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.19.4](https://github.com/googleapis/python-pubsub/compare/v2.19.3...v2.19.4) (2024-02-09)

##### Bug Fixes

  * **diregapic:** S/bazel/bazelisk/ in DIREGAPIC build GitHub action ([#1064](https://github.com/googleapis/python-pubsub/issues/1064)) ([d56ad12](https://github.com/googleapis/python-pubsub/commit/d56ad12f197e9e379d2a4a0a38be108808985c23))



#### [2.19.3](https://github.com/googleapis/python-pubsub/compare/v2.19.2...v2.19.3) (2024-02-08)

##### Bug Fixes

  * Add google-auth as a direct dependency ([#1076](https://github.com/googleapis/python-pubsub/issues/1076)) ([5ce7301](https://github.com/googleapis/python-pubsub/commit/5ce7301b3056191203bc89bbcf1f33083de72a2d))



#### [2.19.2](https://github.com/googleapis/python-pubsub/compare/v2.19.1...v2.19.2) (2024-02-08)

##### Bug Fixes

  * Unit test failures in https://github.com/googleapis/python-pubsu… ([#1074](https://github.com/googleapis/python-pubsub/issues/1074)) ([3c6d128](https://github.com/googleapis/python-pubsub/commit/3c6d128a53d83439036aaec1f1fd48331152935b))



## February 05, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.2.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.1.1...v4.2.0) (2024-02-01)

##### Features

  * Add enforce_in_transit fields and optional annotations ([#1873](https://github.com/googleapis/nodejs-pubsub/issues/1873)) ([09fc424](https://github.com/googleapis/nodejs-pubsub/commit/09fc4241c8782d2f60c1a78dda316628eca5f751))
  * Add schema revision samples ([#1870](https://github.com/googleapis/nodejs-pubsub/issues/1870)) ([044e149](https://github.com/googleapis/nodejs-pubsub/commit/044e1494d82fd64010f7c6f872982d659e753499))



##### Bug Fixes

  * **deps:** Update dependency @opentelemetry/semantic-conventions to ~1.20.0 ([#1871](https://github.com/googleapis/nodejs-pubsub/issues/1871)) ([2ee0dba](https://github.com/googleapis/nodejs-pubsub/commit/2ee0dba67e6d66d9a678796de6172bcafd28796b))
  * **deps:** Update dependency @opentelemetry/semantic-conventions to ~1.21.0 ([#1876](https://github.com/googleapis/nodejs-pubsub/issues/1876)) ([0fe61a9](https://github.com/googleapis/nodejs-pubsub/commit/0fe61a95b3bfc21bd1a5176c7fbd7f822ece5a5c))



### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.36.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.36.0...pubsub/v1.36.1) (2024-01-30)

##### Bug Fixes

  * **pubsub:** Enable universe domain resolution options ([fd1d569](https://github.com/googleapis/google-cloud-go/commit/fd1d56930fa8a747be35a224611f4797b8aeb698))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.19.1](https://github.com/googleapis/python-pubsub/compare/v2.19.0...v2.19.1) (2024-02-02)

##### Documentation

  * **samples:** Swap writer and reader schema to correct places ([265f410](https://github.com/googleapis/python-pubsub/commit/265f4106f499ec5d2d01a127ba192404c1836a28))



## January 31, 2024

Feature

Pub/Sub is available in Johannesburg, South Africa (africa-south1).

## January 29, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.36.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.35.0...pubsub/v1.36.0) (2024-01-26)

##### Features

  * **pubsub:** Add `ingestion_data_source_settings` field to `Topic` ([97d62c7](https://github.com/googleapis/google-cloud-go/commit/97d62c7a6a305c47670ea9c147edc444f4bf8620))
  * **pubsub:** Add enforce_in_transit fields and optional annotations ([97d62c7](https://github.com/googleapis/google-cloud-go/commit/97d62c7a6a305c47670ea9c147edc444f4bf8620))



##### Bug Fixes

  * **pubsub:** Move flow control release to callback completion ([#9311](https://github.com/googleapis/google-cloud-go/issues/9311)) ([2b6b0da](https://github.com/googleapis/google-cloud-go/commit/2b6b0da48517fd0b682077b0fdf6f6a8f162910b))



#### [1.35.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.34.0...pubsub/v1.35.0) (2024-01-25)

##### Features

  * **pubsub:** Support message filtering in pstest ([#9015](https://github.com/googleapis/google-cloud-go/issues/9015)) ([49231bf](https://github.com/googleapis/google-cloud-go/commit/49231bf3d1e96cfa91d72085391ee19fca16ef0a))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.126.2](https://github.com/googleapis/java-pubsub/compare/v1.126.1...v1.126.2) (2024-01-26)

##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.32.0 ([#1875](https://github.com/googleapis/java-pubsub/issues/1875)) ([0aac3e4](https://github.com/googleapis/java-pubsub/commit/0aac3e4c9c5671ce8f3b98056cc3710cd5ca9d07))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.37.0 ([#1878](https://github.com/googleapis/java-pubsub/issues/1878)) ([16dee8b](https://github.com/googleapis/java-pubsub/commit/16dee8bce115f59d8518ca1ae0e39dd87d81f802))



#### [1.126.1](https://github.com/googleapis/java-pubsub/compare/v1.126.0...v1.126.1) (2024-01-25)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.36.0 ([#1840](https://github.com/googleapis/java-pubsub/issues/1840)) ([8c5117d](https://github.com/googleapis/java-pubsub/commit/8c5117d02511acd5469d863ea483f6e765e29292))
  * Update dependency com.google.cloud:google-cloud-core to v2.30.0 ([#1853](https://github.com/googleapis/java-pubsub/issues/1853)) ([db36def](https://github.com/googleapis/java-pubsub/commit/db36deff6a4187cb98ddd68259efd6034762060e))
  * Update dependency com.google.cloud:google-cloud-core to v2.31.0 ([#1872](https://github.com/googleapis/java-pubsub/issues/1872)) ([06db9a0](https://github.com/googleapis/java-pubsub/commit/06db9a05a80b2d7f38aefff2d5e0b33e3fa1a2c9))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.22.0 ([#1865](https://github.com/googleapis/java-pubsub/issues/1865)) ([f4c6f51](https://github.com/googleapis/java-pubsub/commit/f4c6f5112e8285264a497b3a141c31f77fea6ee2))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.23.0 ([#1873](https://github.com/googleapis/java-pubsub/issues/1873)) ([0d445f1](https://github.com/googleapis/java-pubsub/commit/0d445f173574433aed2770d9cc949672221b839e))
  * Update dependency com.google.cloud:google-cloud-storage to v2.32.0 ([#1857](https://github.com/googleapis/java-pubsub/issues/1857)) ([d673e55](https://github.com/googleapis/java-pubsub/commit/d673e55e69f60f5a6f6bae10e2f62d7fd0dfa89f))
  * Update dependency com.google.cloud:google-cloud-storage to v2.32.1 ([#1874](https://github.com/googleapis/java-pubsub/issues/1874)) ([adae8a4](https://github.com/googleapis/java-pubsub/commit/adae8a4aadb08532076fd02710d0e41336ec096c))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.25.2 ([#1858](https://github.com/googleapis/java-pubsub/issues/1858)) ([8fa6354](https://github.com/googleapis/java-pubsub/commit/8fa635427927e1859332896b8373abccd5881949))



## January 22, 2024

Feature

BigQuery subscriptions now support the ability to parse JSON messages by using the schema of a BigQuery table. For more information, see [use table schema](https://docs.cloud.google.com/pubsub/docs/subscription-properties#use-table-schema). The change is being rolled out in a phased manner over the rest of the week.

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.34.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.33.0...pubsub/v1.34.0) (2024-01-19)

##### Features

  * **pubsub/pstest:** Update max topic retention duration to 31 days ([#8605](https://github.com/googleapis/google-cloud-go/issues/8605)) ([d4f90ec](https://github.com/googleapis/google-cloud-go/commit/d4f90ecfec017071ef4eb42beb4135c825494524))
  * **pubsub:** Add `use_table_schema` field to BigQueryConfig ([5132d0f](https://github.com/googleapis/google-cloud-go/commit/5132d0fea3a5ac902a2c9eee865241ed4509a5f4))



##### Bug Fixes

  * **pubsub:** Add veneer header to sub client ([#8608](https://github.com/googleapis/google-cloud-go/issues/8608)) ([04c380d](https://github.com/googleapis/google-cloud-go/commit/04c380d84d096d0f5d33ec6caac133b73b49a9df))
  * **pubsub:** Bump google.golang.org/api to v0.149.0 ([8d2ab9f](https://github.com/googleapis/google-cloud-go/commit/8d2ab9f320a86c1c0fab90513fc05861561d0880))
  * **pubsub:** Make retry policy back off more aggressively for RPCs that retry RESOURCE_EXHAUSTD ([#8438](https://github.com/googleapis/google-cloud-go/issues/8438)) ([81a33c0](https://github.com/googleapis/google-cloud-go/commit/81a33c0e11f2f3f94cc13de2ff899f44bc041fd6))
  * **pubsub:** Set x-goog-request-params for streaming pull request ([#8753](https://github.com/googleapis/google-cloud-go/issues/8753)) ([21ec815](https://github.com/googleapis/google-cloud-go/commit/21ec8158d9e3c14082f76a75f182c98253b4273b))
  * **pubsub:** Update golang.org/x/net to v0.17.0 ([174da47](https://github.com/googleapis/google-cloud-go/commit/174da47254fefb12921bbfc65b7829a453af6f5d))
  * **pubsub:** Update grpc-go to v1.56.3 ([343cea8](https://github.com/googleapis/google-cloud-go/commit/343cea8c43b1e31ae21ad50ad31d3b0b60143f8c))
  * **pubsub:** Update grpc-go to v1.59.0 ([81a97b0](https://github.com/googleapis/google-cloud-go/commit/81a97b06cb28b25432e4ece595c55a9857e960b7))



##### Documentation

  * **pubsub:** Clarified where ordering_key will be written if write_metadata is set ([327e101](https://github.com/googleapis/google-cloud-go/commit/327e10188a2e22dd7b7e6c12a8cf66729f65974c))
  * **pubsub:** Modified some descriptions ([e864fbc](https://github.com/googleapis/google-cloud-go/commit/e864fbcbc4f0a49dfdb04850b07451074c57edc8))
  * **pubsub:** Update allowed message retention duration by server ([#8559](https://github.com/googleapis/google-cloud-go/issues/8559)) ([78c178b](https://github.com/googleapis/google-cloud-go/commit/78c178b44cd014db38cd65aa6d804705f47c0fba))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.126.0](https://github.com/googleapis/java-pubsub/compare/v1.125.13...v1.126.0) (2024-01-13)

##### Features

  * Add `use_table_schema` field to BigQueryConfig ([#1838](https://github.com/googleapis/java-pubsub/issues/1838)) ([8653f4f](https://github.com/googleapis/java-pubsub/commit/8653f4f3dbd61466b8ea05b342c5f66c9e536cf1))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.31.0 ([#1855](https://github.com/googleapis/java-pubsub/issues/1855)) ([7e733d2](https://github.com/googleapis/java-pubsub/commit/7e733d20093e0cd492758dd1ff3efc3a72eb1e0c))
  * Swap writer and reader schema to correct places in sample ([#1849](https://github.com/googleapis/java-pubsub/issues/1849)) ([1c79ad7](https://github.com/googleapis/java-pubsub/commit/1c79ad7336f51ffd4e177be5c2f2a7de902b47b8))
  * Temporarily remove publisher tests causing timeouts ([#1860](https://github.com/googleapis/java-pubsub/issues/1860)) ([a8fa24d](https://github.com/googleapis/java-pubsub/commit/a8fa24d7185d5345e746f8e2563afffe08f3bd6e))
  * Use message ordering enabled property that comes with streaming pull responses ([#1851](https://github.com/googleapis/java-pubsub/issues/1851)) ([d816138](https://github.com/googleapis/java-pubsub/commit/d8161380e232fd4be408e6298827423907a027fb))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.21.0 ([#1854](https://github.com/googleapis/java-pubsub/issues/1854)) ([b36825b](https://github.com/googleapis/java-pubsub/commit/b36825bf476f8bf83a7ca594932e03d06bc05f07))
  * Update dependency com.google.cloud:google-cloud-storage to v2.30.1 ([#1841](https://github.com/googleapis/java-pubsub/issues/1841)) ([d6f1352](https://github.com/googleapis/java-pubsub/commit/d6f1352ec3debe106ba238343c0c05b9278dc964))



## January 15, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.1.1](https://github.com/googleapis/nodejs-pubsub/compare/v4.1.0...v4.1.1) (2024-01-05)

##### Bug Fixes

  * Correct long audio synthesis HTTP binding ([#1867](https://github.com/googleapis/nodejs-pubsub/issues/1867)) ([65940a4](https://github.com/googleapis/nodejs-pubsub/commit/65940a40fe8f2301690d26f769571a198f747dd3))
  * **deps:** Update dependency @opentelemetry/semantic-conventions to ~1.19.0 ([#1862](https://github.com/googleapis/nodejs-pubsub/issues/1862)) ([92259f5](https://github.com/googleapis/nodejs-pubsub/commit/92259f5bffee05036f1746990b021299ea3ea4e7))



## December 18, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.1.0](https://github.com/googleapis/nodejs-pubsub/compare/v4.0.7...v4.1.0) (2023-12-04)

##### Features

  * Add `use_table_schema` field to BigQueryConfig ([#1858](https://github.com/googleapis/nodejs-pubsub/issues/1858)) ([2875d83](https://github.com/googleapis/nodejs-pubsub/commit/2875d8383831563e5b748e96094faa94bf25fc15))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.19.0](https://github.com/googleapis/python-pubsub/compare/v2.18.4...v2.19.0) (2023-12-10)

##### Features

  * Add `use_table_schema` field to BigQueryConfig ([#1035](https://github.com/googleapis/python-pubsub/issues/1035)) ([ac6d912](https://github.com/googleapis/python-pubsub/commit/ac6d9126413b5c8e2b00727f7d74f03b7fb9d9ed))
  * Add support for Python 3.12 ([#1025](https://github.com/googleapis/python-pubsub/issues/1025)) ([660b8ea](https://github.com/googleapis/python-pubsub/commit/660b8eaf0daf975834a8333aedf8415867a4874d))
  * Introduce compatibility with native namespace packages ([#1024](https://github.com/googleapis/python-pubsub/issues/1024)) ([0432420](https://github.com/googleapis/python-pubsub/commit/0432420dcf18304dc1912075482eff0d2dc73009))



##### Bug Fixes

  * Use `retry_async` instead of `retry` in async client ([#1030](https://github.com/googleapis/python-pubsub/issues/1030)) ([05dd571](https://github.com/googleapis/python-pubsub/commit/05dd571760b71ae2930072f0677616dfc19d9511))



## December 04, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.13](https://github.com/googleapis/java-pubsub/compare/v1.125.12...v1.125.13) (2023-11-30)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.28.0 ([#1830](https://github.com/googleapis/java-pubsub/issues/1830)) ([8990b7c](https://github.com/googleapis/java-pubsub/commit/8990b7ca7cfbb08cd117f59bbf18c67dd1e7fb18))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.20.0 ([#1831](https://github.com/googleapis/java-pubsub/issues/1831)) ([d188af8](https://github.com/googleapis/java-pubsub/commit/d188af8815927b409f72c968cbd6a8685976d08b))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.25.1 ([#1816](https://github.com/googleapis/java-pubsub/issues/1816)) ([e4f2b26](https://github.com/googleapis/java-pubsub/commit/e4f2b2605b17024f983a8ccf50ed19d169c15d90))



## November 27, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.12](https://github.com/googleapis/java-pubsub/compare/v1.125.11...v1.125.12) (2023-11-21)

##### Bug Fixes

  * Concurrent modification of processing receievd messages ([#1807](https://github.com/googleapis/java-pubsub/issues/1807)) ([d162126](https://github.com/googleapis/java-pubsub/commit/d16212627b0d9b6616e0a9b20af2c430e2f6b36f))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.34.2 ([#1821](https://github.com/googleapis/java-pubsub/issues/1821)) ([c21ba1a](https://github.com/googleapis/java-pubsub/commit/c21ba1a51acf3411e7f9793f579a103ee1d36f38))
  * Update dependency com.google.cloud:google-cloud-storage to v2.29.1 ([#1817](https://github.com/googleapis/java-pubsub/issues/1817)) ([e179b94](https://github.com/googleapis/java-pubsub/commit/e179b94b7034fbb6c10775b0fe469ab129c0d6c8))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.10.1 ([#1819](https://github.com/googleapis/java-pubsub/issues/1819)) ([af84aa3](https://github.com/googleapis/java-pubsub/commit/af84aa3f5434d3e8ff2122b72cae0fc1c7323742))



## November 13, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.0.7](https://github.com/googleapis/nodejs-pubsub/compare/v4.0.6...v4.0.7) (2023-11-09)

##### Bug Fixes

  * **deps:** Update dependency @opentelemetry/semantic-conventions to ~1.18.0 ([#1852](https://github.com/googleapis/nodejs-pubsub/issues/1852)) ([d9a0432](https://github.com/googleapis/nodejs-pubsub/commit/d9a0432a37c6d741c9694a5bcff047f4c85b2feb))
  * Set x-goog-request-params for streaming pull request ([#1849](https://github.com/googleapis/nodejs-pubsub/issues/1849)) ([7b82ff0](https://github.com/googleapis/nodejs-pubsub/commit/7b82ff01e5c654b3e339dfdec5b3da8bf45da049))



## November 06, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.11](https://github.com/googleapis/java-pubsub/compare/v1.125.10...v1.125.11) (2023-11-01)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.27.0 ([#1810](https://github.com/googleapis/java-pubsub/issues/1810)) ([edd89f3](https://github.com/googleapis/java-pubsub/commit/edd89f36061cd1518f81eb7b33e42cf5c35c659d))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.19.0 ([#1811](https://github.com/googleapis/java-pubsub/issues/1811)) ([d671bcb](https://github.com/googleapis/java-pubsub/commit/d671bcb9b0e6c425eb33bdafea9c20b543020363))



#### [1.125.10](https://github.com/googleapis/java-pubsub/compare/v1.125.9...v1.125.10) (2023-10-31)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-storage to v2.29.0 ([#1800](https://github.com/googleapis/java-pubsub/issues/1800)) ([8c43cc2](https://github.com/googleapis/java-pubsub/commit/8c43cc2443f333c646c27cee4ee70434167213ba))



##### Documentation

  * Adding a GCS subscription example ([#1762](https://github.com/googleapis/java-pubsub/issues/1762)) ([3ce824c](https://github.com/googleapis/java-pubsub/commit/3ce824c78c7eaf37fc3bc0ed2a4b3b1d952ed9bc))
  * Renaming the CreateUnwrappedPushSubscription File ([#1794](https://github.com/googleapis/java-pubsub/issues/1794)) ([3264290](https://github.com/googleapis/java-pubsub/commit/326429092ac73d184b5e887ce5107220f96199b7))



## October 30, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.9](https://github.com/googleapis/java-pubsub/compare/v1.125.8...v1.125.9) (2023-10-27)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.34.0 ([#1795](https://github.com/googleapis/java-pubsub/issues/1795)) ([670daf1](https://github.com/googleapis/java-pubsub/commit/670daf1c74242dfa54e9747924d094cbcaac4d37))



#### [1.125.8](https://github.com/googleapis/java-pubsub/compare/v1.125.7...v1.125.8) (2023-10-23)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.26.0 ([#1780](https://github.com/googleapis/java-pubsub/issues/1780)) ([2d38175](https://github.com/googleapis/java-pubsub/commit/2d381751b51cb69b6ab248ee56fe9ce5bf7f5cd5))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.18.0 ([#1781](https://github.com/googleapis/java-pubsub/issues/1781)) ([5b6cb15](https://github.com/googleapis/java-pubsub/commit/5b6cb15ce9f459061875329ba1fc6d4b84909666))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.28 ([#1782](https://github.com/googleapis/java-pubsub/issues/1782)) ([c9be478](https://github.com/googleapis/java-pubsub/commit/c9be478c3558928fc603c81fc07c4d8ba6d853b4))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.28 ([#1783](https://github.com/googleapis/java-pubsub/issues/1783)) ([5e39b79](https://github.com/googleapis/java-pubsub/commit/5e39b799d5d7b41325f9564a6044c0f0b4b05fdc))



##### Documentation

  * Modified some descriptions ([#1773](https://github.com/googleapis/java-pubsub/issues/1773)) ([17bd055](https://github.com/googleapis/java-pubsub/commit/17bd05512ba71083eb898a3ff8c5dc53c9bbb08d))



## October 23, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.7](https://github.com/googleapis/java-pubsub/compare/v1.125.6...v1.125.7) (2023-10-17)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.33.2 ([#1770](https://github.com/googleapis/java-pubsub/issues/1770)) ([db73af7](https://github.com/googleapis/java-pubsub/commit/db73af7bca53faae2e135ec9a1899e36ac19025c))



## October 16, 2023

Feature

Public preview: [Pub/Sub BigQuery](https://docs.cloud.google.com/pubsub/docs/bigquery#change_data_capture) subscriptions now support BigQuery change data capture.

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.6](https://github.com/googleapis/java-pubsub/compare/v1.125.5...v1.125.6) (2023-10-10)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.33.1 ([#1756](https://github.com/googleapis/java-pubsub/issues/1756)) ([239f474](https://github.com/googleapis/java-pubsub/commit/239f474fefd2313a6842c63c4202d835008647e3))
  * Update dependency com.google.cloud:google-cloud-core to v2.25.0 ([#1764](https://github.com/googleapis/java-pubsub/issues/1764)) ([72404ea](https://github.com/googleapis/java-pubsub/commit/72404eabcc3695b8072091587515562d852a6108))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.17.0 ([#1765](https://github.com/googleapis/java-pubsub/issues/1765)) ([a447292](https://github.com/googleapis/java-pubsub/commit/a447292d07ae1d9b03866dbdd9549c1b10564b28))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.24.4 ([#1760](https://github.com/googleapis/java-pubsub/issues/1760)) ([10a64c6](https://github.com/googleapis/java-pubsub/commit/10a64c6b872a14decf3a799ebd985395358dc32c))



## October 02, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.5](https://github.com/googleapis/java-pubsub/compare/v1.125.4...v1.125.5) (2023-09-28)

##### Dependencies

  * Update gapic-generator-java to 2.26.0 ([935849c](https://github.com/googleapis/java-pubsub/commit/935849cedbb70a0821be56828dd0abeccbccc21c))



#### [1.125.4](https://github.com/googleapis/java-pubsub/compare/v1.125.3...v1.125.4) (2023-09-28)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.33.0 ([#1750](https://github.com/googleapis/java-pubsub/issues/1750)) ([bcbfcd0](https://github.com/googleapis/java-pubsub/commit/bcbfcd0dd65c2ca0f20d3579109728737f1292bc))



#### [1.125.3](https://github.com/googleapis/java-pubsub/compare/v1.125.2...v1.125.3) (2023-09-27)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.24.1 ([#1737](https://github.com/googleapis/java-pubsub/issues/1737)) ([48a4432](https://github.com/googleapis/java-pubsub/commit/48a44321ad34edd8c297ccc57445ec36916171cb))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.16.1 ([#1738](https://github.com/googleapis/java-pubsub/issues/1738)) ([e2cf7c1](https://github.com/googleapis/java-pubsub/commit/e2cf7c110b72dff695a46a972687a595216934e6))
  * Update dependency org.apache.avro:avro to v1.11.3 ([#1740](https://github.com/googleapis/java-pubsub/issues/1740)) ([971b35f](https://github.com/googleapis/java-pubsub/commit/971b35f5d26263ef3c1d83b6282680ac1608c032))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.4 [security](https://docs.cloud.google.com/pubsub/docs/release-notes/%5B#1742%5D\(https://github.com/googleapis/java-pubsub/issues/1742\)%7B:%20.external%20target=%22_blank%22%20rel=%22noreferrer%20noopener%22%7D) ([70ba500](https://github.com/googleapis/java-pubsub/commit/70ba500cc014cb9d0e1799997aa0682239b97cde))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.5 ([#1746](https://github.com/googleapis/java-pubsub/issues/1746)) ([a4b1994](https://github.com/googleapis/java-pubsub/commit/a4b199414cad5cb061330832b2bf2a8bbe76bcbd))



## September 25, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.7.5](https://github.com/googleapis/nodejs-pubsub/compare/v3.7.4...v3.7.5) (2023-09-20)

##### Bug Fixes

  * Bump to activate release-please ([#1819](https://github.com/googleapis/nodejs-pubsub/issues/1819)) ([83f3813](https://github.com/googleapis/nodejs-pubsub/commit/83f3813c2b636e2e6dea6ce8ccc87bba316b5687))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.2](https://github.com/googleapis/java-pubsub/compare/v1.125.1...v1.125.2) (2023-09-18)

##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.27 ([#1730](https://github.com/googleapis/java-pubsub/issues/1730)) ([687a855](https://github.com/googleapis/java-pubsub/commit/687a855580a9c8fe7f0d4a8952cb3ca46ff6f736))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.27 ([#1731](https://github.com/googleapis/java-pubsub/issues/1731)) ([403b7e7](https://github.com/googleapis/java-pubsub/commit/403b7e72c275464a67f6998bb975d95026a8480d))



## September 19, 2023

Feature

Pub/Sub is now available in Dammam, Saudi Arabia (`me-central2`).

Feature

Messages written to a dead letter topic configured for a BigQuery subscription contain an attribute with the reason the message could not be written to BigQuery. For more information, see [Handle message failures](https://docs.cloud.google.com/pubsub/docs/bigquery#handle_message_failures).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.0.6](https://github.com/googleapis/nodejs-pubsub/compare/v4.0.5...v4.0.6) (2023-09-15)

##### Bug Fixes

  * Bump the minimum gax up to 4.0.4 to get grpc-js fixes ([#1829](https://github.com/googleapis/nodejs-pubsub/issues/1829)) ([cc86e2b](https://github.com/googleapis/nodejs-pubsub/commit/cc86e2b4f3593d3d6046dc5baee76e1431832acb))
  * **deps:** Update dependency @opentelemetry/semantic-conventions to ~1.17.0 ([#1824](https://github.com/googleapis/nodejs-pubsub/issues/1824)) ([679c6b8](https://github.com/googleapis/nodejs-pubsub/commit/679c6b82bdb6fe28c3bc8c31db2e10de1ee7e089))



#### [3.7.4](https://github.com/googleapis/nodejs-pubsub/compare/v3.7.3...v3.7.4) (2023-09-08)

##### Bug Fixes

  * Always fill the topic and sub names when creating from a PubSub object ([#1816](https://github.com/googleapis/nodejs-pubsub/issues/1816)) ([ddf8b8a](https://github.com/googleapis/nodejs-pubsub/commit/ddf8b8ab288387e51db816df825594cb5190b837))
  * Make retry policy back off more aggressively for RPCs that retry RESOURCE_EXHAUSTD ([#1806](https://github.com/googleapis/nodejs-pubsub/issues/1806)) ([bfcf523](https://github.com/googleapis/nodejs-pubsub/commit/bfcf523da4786d44cc35560aa91962363f475fbb))
  * Set grpc keepalive time|outs by default ([#1814](https://github.com/googleapis/nodejs-pubsub/issues/1814)) ([dedfdea](https://github.com/googleapis/nodejs-pubsub/commit/dedfdea7a47fc19de981218a1d7502c75fdde488))
  * Simplify logic for HTTP/1.1 REST fallback option ([#1809](https://github.com/googleapis/nodejs-pubsub/issues/1809)) ([ee09b69](https://github.com/googleapis/nodejs-pubsub/commit/ee09b69092a16e2e12bc8e2647d48f627e013afd))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.125.1](https://github.com/googleapis/java-pubsub/compare/v1.125.0...v1.125.1) (2023-09-14)

##### Dependencies

  * Update actions/checkout action to v4 - abandoned ([#1719](https://github.com/googleapis/java-pubsub/issues/1719)) ([b82f15a](https://github.com/googleapis/java-pubsub/commit/b82f15a099f3366620f5e22764b043911ebd88d1))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.32.0 ([#1725](https://github.com/googleapis/java-pubsub/issues/1725)) ([f40f09a](https://github.com/googleapis/java-pubsub/commit/f40f09a185c035cc03b6be6ec62f880da9f7b377))



#### [1.125.0](https://github.com/googleapis/java-pubsub/compare/v1.124.2...v1.125.0) (2023-09-12)

##### Features

  * Receipt modack ([#1540](https://github.com/googleapis/java-pubsub/issues/1540)) ([74d8da9](https://github.com/googleapis/java-pubsub/commit/74d8da97c42b672e3f9f26b9a535d6bac948a402))



##### Bug Fixes

  * Make retry policy back off more aggressively for RPCs that retry RESOURCE_EXHAUSTD ([#1704](https://github.com/googleapis/java-pubsub/issues/1704)) ([f61e7e0](https://github.com/googleapis/java-pubsub/commit/f61e7e0e2895a90e30ecf4dcbfa8c70022947d9e))



##### Dependencies

  * Update actions/checkout action to v4 ([#1712](https://github.com/googleapis/java-pubsub/issues/1712)) ([404c492](https://github.com/googleapis/java-pubsub/commit/404c492823306c1448c62383b9ea88cf9e43b970))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.31.2 ([#1713](https://github.com/googleapis/java-pubsub/issues/1713)) ([32cb43c](https://github.com/googleapis/java-pubsub/commit/32cb43cce40f7a39602eb7d9b39a88eb229fc4ef))
  * Update dependency com.google.cloud:google-cloud-core to v2.23.0 ([#1717](https://github.com/googleapis/java-pubsub/issues/1717)) ([929f778](https://github.com/googleapis/java-pubsub/commit/929f778e341aefe61206e55de828bf5a86e4efd3))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.15.0 ([#1718](https://github.com/googleapis/java-pubsub/issues/1718)) ([0eeaa19](https://github.com/googleapis/java-pubsub/commit/0eeaa19a640513e80d595ca7c4016e26fc30871b))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.24.3 ([#1698](https://github.com/googleapis/java-pubsub/issues/1698)) ([1157fbf](https://github.com/googleapis/java-pubsub/commit/1157fbff92204eae55bb24ad803f0b8e1336ac10))
  * Update dependency org.easymock:easymock to v5.2.0 ([#1711](https://github.com/googleapis/java-pubsub/issues/1711)) ([313f6dd](https://github.com/googleapis/java-pubsub/commit/313f6dd8b82fbc57df066615e285325969b6d2e4))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.25 ([#1709](https://github.com/googleapis/java-pubsub/issues/1709)) ([1cc8a53](https://github.com/googleapis/java-pubsub/commit/1cc8a53a416acdd5f9cd4fc598f2f5f182a2ad44))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.26 ([#1715](https://github.com/googleapis/java-pubsub/issues/1715)) ([f2cc75f](https://github.com/googleapis/java-pubsub/commit/f2cc75f960521e8be50cf354e00024d66fb8f7fb))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.25 ([#1710](https://github.com/googleapis/java-pubsub/issues/1710)) ([9764c3f](https://github.com/googleapis/java-pubsub/commit/9764c3f740cd726ad09cef82039561bd145fbe0c))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.26 ([#1716](https://github.com/googleapis/java-pubsub/issues/1716)) ([6c9e949](https://github.com/googleapis/java-pubsub/commit/6c9e9493ec7aeaa0711ad2155fa6a549937284df))



## September 11, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.18.4](https://github.com/googleapis/python-pubsub/compare/v2.18.3...v2.18.4) (2023-09-09)

##### Documentation

  * Minor formatting ([#988](https://github.com/googleapis/python-pubsub/issues/988)) ([4eea8c5](https://github.com/googleapis/python-pubsub/commit/4eea8c5c757da6800ba6958e4b8e66085b0e9ddb))



Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.0.5](https://github.com/googleapis/nodejs-pubsub/compare/v4.0.4...v4.0.5) (2023-09-07)

##### Bug Fixes

  * Always fill the topic and sub names when creating from a PubSub object ([#1816](https://github.com/googleapis/nodejs-pubsub/issues/1816)) ([be8ed53](https://github.com/googleapis/nodejs-pubsub/commit/be8ed530e327e2bd08a49200492f0a163b3b91d7))



#### [4.0.4](https://github.com/googleapis/nodejs-pubsub/compare/v4.0.3...v4.0.4) (2023-09-05)

##### Bug Fixes

  * Set grpc keepalive time|outs by default ([#1814](https://github.com/googleapis/nodejs-pubsub/issues/1814)) ([13d89a2](https://github.com/googleapis/nodejs-pubsub/commit/13d89a2b4e25f340ef492d586bfa8cc3a9a6d6cf))



#### [4.0.3](https://github.com/googleapis/nodejs-pubsub/compare/v4.0.2...v4.0.3) (2023-08-31)

##### Bug Fixes

  * Simplify logic for HTTP/1.1 REST fallback option ([#1809](https://github.com/googleapis/nodejs-pubsub/issues/1809)) ([f26008d](https://github.com/googleapis/nodejs-pubsub/commit/f26008de84f201ec6e0180582d8a4bebc3d5ced0))



## August 28, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.124.2](https://github.com/googleapis/java-pubsub/compare/v1.124.1...v1.124.2) (2023-08-15)

##### Bug Fixes

  * Update Publish retry backoff settings ([#1686](https://github.com/googleapis/java-pubsub/issues/1686)) ([63a74d9](https://github.com/googleapis/java-pubsub/commit/63a74d98fdee56a98819d135a676a67fcc24961a))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.31.1 ([#1697](https://github.com/googleapis/java-pubsub/issues/1697)) ([9e90790](https://github.com/googleapis/java-pubsub/commit/9e907901e0f5f78adfffb3e61974e9f8fd756f96))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.24 ([#1695](https://github.com/googleapis/java-pubsub/issues/1695)) ([ec64036](https://github.com/googleapis/java-pubsub/commit/ec640361a471111001f22667fa7e38123b731025))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.24 ([#1696](https://github.com/googleapis/java-pubsub/issues/1696)) ([cc9ae19](https://github.com/googleapis/java-pubsub/commit/cc9ae19865c0ece3789a8c2fa22afb5fbd306dc9))



Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.0.2](https://github.com/googleapis/nodejs-pubsub/compare/v4.0.1...v4.0.2) (2023-08-24)

##### Bug Fixes

  * Make retry policy back off more aggressively for RPCs that retry RESOURCE_EXHAUSTD ([#1806](https://github.com/googleapis/nodejs-pubsub/issues/1806)) ([e9969ba](https://github.com/googleapis/nodejs-pubsub/commit/e9969bab92c38f1509b157034fcdbe5d5ec63903))



## August 22, 2023

Feature

Pub/Sub is now available in `europe-west10` (Berlin, Germany).

## August 21, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.0.1](https://github.com/googleapis/nodejs-pubsub/compare/v4.0.0...v4.0.1) (2023-08-11)

##### Bug Fixes

  * **deps:** Update dependency @google-cloud/paginator to v5 ([#1799](https://github.com/googleapis/nodejs-pubsub/issues/1799)) ([3195d21](https://github.com/googleapis/nodejs-pubsub/commit/3195d21bf817cf10daa86b019532c9405dc42405))
  * **deps:** Update dependency @google-cloud/precise-date to v4 ([#1803](https://github.com/googleapis/nodejs-pubsub/issues/1803)) ([2c22d67](https://github.com/googleapis/nodejs-pubsub/commit/2c22d67b0fbaf3409101a830ee0c5be002ed6c7b))
  * **deps:** Update dependency @google-cloud/projectify to v4 ([#1800](https://github.com/googleapis/nodejs-pubsub/issues/1800)) ([5787d56](https://github.com/googleapis/nodejs-pubsub/commit/5787d56b95d46544bf8c59fe4bc4cb374bc53d0a))
  * **deps:** Update dependency @google-cloud/promisify to v4 ([#1798](https://github.com/googleapis/nodejs-pubsub/issues/1798)) ([093c46b](https://github.com/googleapis/nodejs-pubsub/commit/093c46bd0a4713ad9702bde03eaa5e8b0acedb28))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.18.3](https://github.com/googleapis/python-pubsub/compare/v2.18.2...v2.18.3) (2023-08-18)

##### Bug Fixes

  * Make retry policy back off more aggressively for RPCs that retry RESOURCE_EXHAUSTD ([#979](https://github.com/googleapis/python-pubsub/issues/979)) ([4073b3d](https://github.com/googleapis/python-pubsub/commit/4073b3dd6a6989e86d5e19bdb9b9c47ae2b0db87))



## August 14, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.18.2](https://github.com/googleapis/python-pubsub/compare/v2.18.1...v2.18.2) (2023-08-07)

##### Bug Fixes

  * Change retry multiplier from 1.3 to 4, for requests that retry Resour… ([#971](https://github.com/googleapis/python-pubsub/issues/971)) ([e4364d2](https://github.com/googleapis/python-pubsub/commit/e4364d2a061bb73fe3410d2ef213a04f3315e282))



## August 07, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [4.0.0](https://github.com/googleapis/nodejs-pubsub/compare/v3.7.3...v4.0.0) (2023-08-03)

##### ⚠ BREAKING CHANGES

  * node 12 eos ([#1774](https://github.com/googleapis/nodejs-pubsub/issues/1774)) (#1784)



##### Features

  * Node 12 eos ([#1774](https://github.com/googleapis/nodejs-pubsub/issues/1774)) ([#1784](https://github.com/googleapis/nodejs-pubsub/issues/1784)) ([47b83c1](https://github.com/googleapis/nodejs-pubsub/commit/47b83c18c543a7c8763256f79927a7340db56568))



##### Bug Fixes

  * Fix typings for IAM methods ([#1785](https://github.com/googleapis/nodejs-pubsub/issues/1785)) ([9a6bdbc](https://github.com/googleapis/nodejs-pubsub/commit/9a6bdbce952c81cb1a43fecbce16a3e3ab0f1420))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.124.1](https://github.com/googleapis/java-pubsub/compare/v1.124.0...v1.124.1) (2023-08-03)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.22.0 ([#1687](https://github.com/googleapis/java-pubsub/issues/1687)) ([220f318](https://github.com/googleapis/java-pubsub/commit/220f3181562a848cd786cc0126e8e3ad382787c7))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.14.0 ([#1688](https://github.com/googleapis/java-pubsub/issues/1688)) ([0ded9f1](https://github.com/googleapis/java-pubsub/commit/0ded9f172af637db5d4302b146a24ecdd5b1bde2))



## July 31, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.7.3](https://github.com/googleapis/nodejs-pubsub/compare/v3.7.2...v3.7.3) (2023-07-26)

##### Bug Fixes

  * Update masks for topic should be snake case ([#1778](https://github.com/googleapis/nodejs-pubsub/issues/1778)) ([ba72638](https://github.com/googleapis/nodejs-pubsub/commit/ba7263836e6951454f77f631c9d2eb0a4df98da5))



#### [3.7.2](https://github.com/googleapis/nodejs-pubsub/compare/v3.7.1...v3.7.2) (2023-07-24)

##### Bug Fixes

  * Update to gax 3.6.1 for vuln fix ([#1775](https://github.com/googleapis/nodejs-pubsub/issues/1775)) ([98460db](https://github.com/googleapis/nodejs-pubsub/commit/98460dbd1f31e4ee06356e88fec676a04a68ac88))



### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.33.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.32.0...pubsub/v1.33.0) (2023-07-24)

##### Features

  * **pubsub:** Support payload wrapping for push subs ([#8292](https://github.com/googleapis/google-cloud-go/issues/8292)) ([fd49db5](https://github.com/googleapis/google-cloud-go/commit/fd49db50cd333a2c918f6a1c94f779b8936876fc))



##### Bug Fixes

  * **pubsub/pstest:** Update maxMessageRetentionDuration to be 31 days ([#8199](https://github.com/googleapis/google-cloud-go/issues/8199)) ([1fa4bb8](https://github.com/googleapis/google-cloud-go/commit/1fa4bb8b3f22aad0b97ccae610408720522a8b31))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.124.0](https://github.com/googleapis/java-pubsub/compare/v1.123.20...v1.124.0) (2023-07-27)

##### Features

  * Setup 1.123.x lts branch ([#1676](https://github.com/googleapis/java-pubsub/issues/1676)) ([a60b887](https://github.com/googleapis/java-pubsub/commit/a60b88772d69d367f90bbe61bc4e157338193b0f))



##### Documentation

  * Clarified where ordering_key will be written if write_metadata is set ([#1675](https://github.com/googleapis/java-pubsub/issues/1675)) ([462746c](https://github.com/googleapis/java-pubsub/commit/462746cfbf9b712118b67349f2f4f4cebf45932a))



#### [1.123.20](https://github.com/googleapis/java-pubsub/compare/v1.123.19...v1.123.20) (2023-07-25)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.31.0 ([#1671](https://github.com/googleapis/java-pubsub/issues/1671)) ([c51d396](https://github.com/googleapis/java-pubsub/commit/c51d39688464c51ffdb046368b4f8e926360d72e))



#### [1.123.19](https://github.com/googleapis/java-pubsub/compare/v1.123.18...v1.123.19) (2023-07-25)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.30.1 ([#1656](https://github.com/googleapis/java-pubsub/issues/1656)) ([4fe4bc4](https://github.com/googleapis/java-pubsub/commit/4fe4bc49d82753e3e185f0a2c4694d80e48808f7))
  * Update dependency com.google.cloud:google-cloud-core to v2.21.1 ([#1662](https://github.com/googleapis/java-pubsub/issues/1662)) ([e10292c](https://github.com/googleapis/java-pubsub/commit/e10292c16f24870a91584f716545ff210302a7bc))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.13.1 ([#1663](https://github.com/googleapis/java-pubsub/issues/1663)) ([50f4ff1](https://github.com/googleapis/java-pubsub/commit/50f4ff10140699a02d1ec550b05ff6d1aa39c762))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.10.0 ([#1666](https://github.com/googleapis/java-pubsub/issues/1666)) ([d8712a3](https://github.com/googleapis/java-pubsub/commit/d8712a31459b8f9497dff7a866c8a8795ca60af9))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.3 ([#1665](https://github.com/googleapis/java-pubsub/issues/1665)) ([ad1c515](https://github.com/googleapis/java-pubsub/commit/ad1c5157eadc4bf2d43b7dc332ac4150d732912d))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.18.1](https://github.com/googleapis/python-pubsub/compare/v2.18.0...v2.18.1) (2023-07-26)

##### Documentation

  * Clarified where ordering_key will be written if write_metadata is set ([#965](https://github.com/googleapis/python-pubsub/issues/965)) ([3d95034](https://github.com/googleapis/python-pubsub/commit/3d95034f94426cdcf5b87323b9e463a7e8ce4f91))



## July 28, 2023

Feature

General availability: You can now create [Cloud Storage](https://docs.cloud.google.com/pubsub/docs/cloudstorage) subscriptions in Pub/Sub to write messages directly to an existing Cloud Storage bucket. The change is being rolled out in a phased manner over the rest of the week.

## July 24, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.18](https://github.com/googleapis/java-pubsub/compare/v1.123.17...v1.123.18) (2023-07-17)

##### Documentation

  * Tightened requirements on cloud storage subscription filename suffixes ([#1639](https://github.com/googleapis/java-pubsub/issues/1639)) ([34a182a](https://github.com/googleapis/java-pubsub/commit/34a182a1655c843cd728850b278ba2e9ce9a5680))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.21.0 ([#1650](https://github.com/googleapis/java-pubsub/issues/1650)) ([69879d4](https://github.com/googleapis/java-pubsub/commit/69879d4c9d7a220f9c5a38b144d49e71ad3b94d0))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.13.0 ([#1651](https://github.com/googleapis/java-pubsub/issues/1651)) ([83fdbe2](https://github.com/googleapis/java-pubsub/commit/83fdbe2435d8fa03b5648272a794874ff910fcb6))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.23.4 ([#1649](https://github.com/googleapis/java-pubsub/issues/1649)) ([9f9c5ca](https://github.com/googleapis/java-pubsub/commit/9f9c5ca2abddde274c79cf36bf2aea91b7b8b455))
  * Update dependency org.apache.avro:avro to v1.11.2 ([#1646](https://github.com/googleapis/java-pubsub/issues/1646)) ([5859fe4](https://github.com/googleapis/java-pubsub/commit/5859fe4c6540fa577942f38e117798d3c3cdc498))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.2 ([#1654](https://github.com/googleapis/java-pubsub/issues/1654)) ([05445f0](https://github.com/googleapis/java-pubsub/commit/05445f0ccf1cd78a604ec267d7a146cdd1770c59))



## July 18, 2023

Feature

[Payload unwrapping](https://docs.cloud.google.com/pubsub/docs/payload-unwrapping) for push subscriptions is now available. Payload unwrapping lets you deliver Pub/Sub messages stripped of all message metadata, except for the message data. With payload unwrapping enabled, message data is delivered directly as the HTTP body.

## July 17, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.18.0](https://github.com/googleapis/python-pubsub/compare/v2.17.1...v2.18.0) (2023-07-12)

##### Features

  * Add push config wrapper fields ([#925](https://github.com/googleapis/python-pubsub/issues/925)) ([8e803cf](https://github.com/googleapis/python-pubsub/commit/8e803cf4ab136d606a0be459ab6d281b65560599))



##### Bug Fixes

  * Add async context manager return types ([#944](https://github.com/googleapis/python-pubsub/issues/944)) ([a3b2061](https://github.com/googleapis/python-pubsub/commit/a3b2061c4edf42123335fcfee6fcc4a44e90a5eb))



##### Documentation

  * Tightened requirements on cloud storage subscription filename suffixes ([#938](https://github.com/googleapis/python-pubsub/issues/938)) ([f54dcd0](https://github.com/googleapis/python-pubsub/commit/f54dcd0e7324218d87c37c0266c441a62012866d))
  * Update Community section in README.rst ([#945](https://github.com/googleapis/python-pubsub/issues/945)) ([dea258c](https://github.com/googleapis/python-pubsub/commit/dea258cff3ad19ffba67659bb03a2edcc44889d9))



## July 03, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.32.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.31.0...pubsub/v1.32.0) (2023-06-27)

##### Features

  * **pubsub:** Add push config wrapper fields ([ca94e27](https://github.com/googleapis/google-cloud-go/commit/ca94e2724f9e2610b46aefd0a3b5ddc06102e91b))
  * **pubsub:** Add support for cloud storage subscriptions ([#7977](https://github.com/googleapis/google-cloud-go/issues/7977)) ([54218e9](https://github.com/googleapis/google-cloud-go/commit/54218e963bb5a6d47411a490985b54053825064f))
  * **pubsub:** Enable project autodetection and detect empty project ([#8168](https://github.com/googleapis/google-cloud-go/issues/8168)) ([c7e05d8](https://github.com/googleapis/google-cloud-go/commit/c7e05d81502b4ff8d92aad4a3d45a3940e0ead9d))
  * **pubsub:** Update all direct dependencies ([b340d03](https://github.com/googleapis/google-cloud-go/commit/b340d030f2b52a4ce48846ce63984b28583abde6))



##### Bug Fixes

  * **pubsub/pstest:** Align fake handling of bqconfig subscription to server behavior ([#8066](https://github.com/googleapis/google-cloud-go/issues/8066)) ([57914ec](https://github.com/googleapis/google-cloud-go/commit/57914ec4d5d2c894edb564c918606feb89bad5bc))
  * **pubsub/pstest:** Fix failing bq config test ([#8060](https://github.com/googleapis/google-cloud-go/issues/8060)) ([fb9db66](https://github.com/googleapis/google-cloud-go/commit/fb9db661d49237d25b20544625edc541670f41ad))
  * **pubsub:** Fix issue preventing clearing BQ subscription ([#8040](https://github.com/googleapis/google-cloud-go/issues/8040)) ([0366bf3](https://github.com/googleapis/google-cloud-go/commit/0366bf39b90c38d3139d4aa65c0cdaed1a4d80f1))
  * **pubsub:** REST query UpdateMask bug ([df52820](https://github.com/googleapis/google-cloud-go/commit/df52820b0e7721954809a8aa8700b93c5662dc9b))
  * **pubsub:** Use fieldmask directly instead of field_mask genproto alias ([#8030](https://github.com/googleapis/google-cloud-go/issues/8030)) ([087a5fc](https://github.com/googleapis/google-cloud-go/commit/087a5fca29d2c21f73e336a0ff714294af7af958))



##### Documentation

  * **pubsub:** Tightened requirements on cloud storage subscription filename suffixes ([1da334c](https://github.com/googleapis/google-cloud-go/commit/1da334c0cbeed9cfb8df0551714721284d164d60))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.17](https://github.com/googleapis/java-pubsub/compare/v1.123.16...v1.123.17) (2023-06-26)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.29.0 ([#1633](https://github.com/googleapis/java-pubsub/issues/1633)) ([20096e7](https://github.com/googleapis/java-pubsub/commit/20096e7b64f9b62051f51ad28aa49b95f78b3e6b))



#### [1.123.16](https://github.com/googleapis/java-pubsub/compare/v1.123.15...v1.123.16) (2023-06-26)

##### Dependencies

  * Update dependency com.google.protobuf:protobuf-java-util to v3.23.3 ([#1634](https://github.com/googleapis/java-pubsub/issues/1634)) ([2481c4b](https://github.com/googleapis/java-pubsub/commit/2481c4b8799bbe78542b4a8dd6c2484be08f30a1))



## June 26, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.15](https://github.com/googleapis/java-pubsub/compare/v1.123.14...v1.123.15) (2023-06-22)

##### Bug Fixes

  * Fixing the shutdown logic for streaming subscriber connection ([#1613](https://github.com/googleapis/java-pubsub/issues/1613)) ([09aff9c](https://github.com/googleapis/java-pubsub/commit/09aff9c59bab646c0bae857f3bca9dc8e9eeebd1))



##### Documentation

  * Adding pubsub emulator example ([#1602](https://github.com/googleapis/java-pubsub/issues/1602)) ([8ded110](https://github.com/googleapis/java-pubsub/commit/8ded11041c63f1f75f0612c081ba6b476b6b89b8))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.27.0 ([#1599](https://github.com/googleapis/java-pubsub/issues/1599)) ([3b4b7d0](https://github.com/googleapis/java-pubsub/commit/3b4b7d0522d8eb136800dd546acb8880b8b28e9e))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.27.1 ([#1614](https://github.com/googleapis/java-pubsub/issues/1614)) ([a974e08](https://github.com/googleapis/java-pubsub/commit/a974e08b45d49ca275c19a4e94e66b4b831a0fad))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.28.0 ([#1626](https://github.com/googleapis/java-pubsub/issues/1626)) ([a4a02b4](https://github.com/googleapis/java-pubsub/commit/a4a02b4fd0a3827c3e321c56223731f0a828e8c5))
  * Update dependency com.google.cloud:google-cloud-core to v2.20.0 ([#1629](https://github.com/googleapis/java-pubsub/issues/1629)) ([5f88f4f](https://github.com/googleapis/java-pubsub/commit/5f88f4f5f6fd1c8f2c0e7523b6919a6a477d785c))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.12.0 ([#1630](https://github.com/googleapis/java-pubsub/issues/1630)) ([b444a9d](https://github.com/googleapis/java-pubsub/commit/b444a9d825300519681a205a833ae9d816e89cf2))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.23 ([#1623](https://github.com/googleapis/java-pubsub/issues/1623)) ([b5f8e49](https://github.com/googleapis/java-pubsub/commit/b5f8e4961dd473c98641d8b78c958db1e0e8d01e))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.23 ([#1624](https://github.com/googleapis/java-pubsub/issues/1624)) ([68ada24](https://github.com/googleapis/java-pubsub/commit/68ada243897a763e04d4858ad052050e09326371))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.1 - abandoned ([#1616](https://github.com/googleapis/java-pubsub/issues/1616)) ([48ec282](https://github.com/googleapis/java-pubsub/commit/48ec282753f8068df135cee55febe5dba97be1b5))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.1 [security](https://docs.cloud.google.com/pubsub/docs/release-notes/%5B#1620%5D\(https://github.com/googleapis/java-pubsub/issues/1620\)%7B:%20.external%20target=%22_blank%22%20rel=%22noreferrer%20noopener%22%7D) ([a1cb267](https://github.com/googleapis/java-pubsub/commit/a1cb2673f5e6556472a87a0fb2acbc3e0ddfd933))



## June 19, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.14](https://github.com/googleapis/java-pubsub/compare/v1.123.13...v1.123.14) (2023-06-12)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.19.0 ([#1604](https://github.com/googleapis/java-pubsub/issues/1604)) ([7ac609e](https://github.com/googleapis/java-pubsub/commit/7ac609e44c20db73460fe39919439c3a2b597454))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.11.0 ([#1605](https://github.com/googleapis/java-pubsub/issues/1605)) ([077ac04](https://github.com/googleapis/java-pubsub/commit/077ac04214be23f6693734c157925a5607ada869))



## June 12, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.7.1](https://github.com/googleapis/nodejs-pubsub/compare/v3.7.0...v3.7.1) (2023-06-08)

##### Bug Fixes

  * Don't crash if an already-drained/removed queue gets flushed again ([#1747](https://github.com/googleapis/nodejs-pubsub/issues/1747)) ([52ea441](https://github.com/googleapis/nodejs-pubsub/commit/52ea441fee302aa6c400b58d4ecebbc96a2ea5ea))



## June 05, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.13](https://github.com/googleapis/java-pubsub/compare/v1.123.12...v1.123.13) (2023-05-30)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.26.0 ([#1582](https://github.com/googleapis/java-pubsub/issues/1582)) ([a7c09b7](https://github.com/googleapis/java-pubsub/commit/a7c09b763845fc78e5382f79365467d4bdb8a24d))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.26.1 ([#1585](https://github.com/googleapis/java-pubsub/issues/1585)) ([e2c37bf](https://github.com/googleapis/java-pubsub/commit/e2c37bfcee74a6f95cc3c15cf1f9d3d1602b77ff))
  * Update dependency com.google.cloud:google-cloud-core to v2.18.1 ([#1591](https://github.com/googleapis/java-pubsub/issues/1591)) ([1637f0d](https://github.com/googleapis/java-pubsub/commit/1637f0db2a89b20d28a6812b6abb4f36bfd46f80))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.10.0 ([#1592](https://github.com/googleapis/java-pubsub/issues/1592)) ([a6be7b7](https://github.com/googleapis/java-pubsub/commit/a6be7b7870ba776fd9b39a0b16d45ba51fcc8ad6))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.10.1 ([#1594](https://github.com/googleapis/java-pubsub/issues/1594)) ([52263ce](https://github.com/googleapis/java-pubsub/commit/52263ce63d4cbda649121e465f4bdc78bbfa8e44))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.10.0 ([#1590](https://github.com/googleapis/java-pubsub/issues/1590)) ([338f31f](https://github.com/googleapis/java-pubsub/commit/338f31f96deb09fe93e1306986a7887d285a9d06))



## May 29, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.7.0](https://github.com/googleapis/nodejs-pubsub/compare/v3.6.0...v3.7.0) (2023-05-26)

##### Features

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.31.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.30.1...pubsub/v1.31.0) (2023-05-24)

##### Features

  * **pubsub:** Expose common errors for easier handling ([#7940](https://github.com/googleapis/google-cloud-go/issues/7940)) ([983105d](https://github.com/googleapis/google-cloud-go/commit/983105dd86d2ee34a09a5fd665d112f31062cf56))



##### Bug Fixes

  * **pubsub:** Allow clearing of topic schema ([#7980](https://github.com/googleapis/google-cloud-go/issues/7980)) ([46fc060](https://github.com/googleapis/google-cloud-go/commit/46fc06099852412071be8c8a02d0d9416fd08817))
  * **pubsub:** Update grpc to v1.55.0 ([1147ce0](https://github.com/googleapis/google-cloud-go/commit/1147ce02a990276ca4f8ab7a1ab65c14da4450ef))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.17.1](https://github.com/googleapis/python-pubsub/compare/v2.17.0...v2.17.1) (2023-05-23)

##### Documentation

  * Add attributes to pubsub_v1.types ([#921](https://github.com/googleapis/python-pubsub/issues/921)) ([4607dca](https://github.com/googleapis/python-pubsub/commit/4607dca983a8f5d4043c5661165da99453f2ef4a))



## May 22, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.12](https://github.com/googleapis/java-pubsub/compare/v1.123.11...v1.123.12) (2023-05-12)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.25.0 ([#1566](https://github.com/googleapis/java-pubsub/issues/1566)) ([7e63280](https://github.com/googleapis/java-pubsub/commit/7e632806b83b5c849ea50fdf3085b2db7bdbeff3))
  * Update dependency com.google.cloud:google-cloud-core to v2.17.0 ([#1574](https://github.com/googleapis/java-pubsub/issues/1574)) ([9c80f14](https://github.com/googleapis/java-pubsub/commit/9c80f1493a5149a76b55d9f1d178684e1b5dde80))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.9.0 ([#1576](https://github.com/googleapis/java-pubsub/issues/1576)) ([03a027f](https://github.com/googleapis/java-pubsub/commit/03a027fb2619444511d25ef7100c7ac850c1dca1))
  * Update dependency org.easymock:easymock to v5.1.0 ([#1448](https://github.com/googleapis/java-pubsub/issues/1448)) ([5ad86fe](https://github.com/googleapis/java-pubsub/commit/5ad86fe783a2fcdfe6102a9916c65b1c4139b3da))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.22 ([#1570](https://github.com/googleapis/java-pubsub/issues/1570)) ([bbe9a8b](https://github.com/googleapis/java-pubsub/commit/bbe9a8b6594a0e6b777ceb3b97e8d625446e34e4))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.22 ([#1571](https://github.com/googleapis/java-pubsub/issues/1571)) ([e7b62d3](https://github.com/googleapis/java-pubsub/commit/e7b62d35aa3c73f55a474d406da094ded02d07f1))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.9.0 - abandoned ([#1471](https://github.com/googleapis/java-pubsub/issues/1471)) ([1620e00](https://github.com/googleapis/java-pubsub/commit/1620e00cf1632699fa37a78059dfb86e707dbccc))
  * Update dependency org.xerial.snappy:snappy-java to v1.1.9.1 ([#1572](https://github.com/googleapis/java-pubsub/issues/1572)) ([1ec2fec](https://github.com/googleapis/java-pubsub/commit/1ec2feca66ab8b29edf8f9dd0d4b8df8261e709a))



## May 15, 2023

Feature

BigQuery subscriptions now support the `NUMERIC` and `BIGNUMERIC` data types. For more information, see [Schema compatibility](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).

## May 08, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.30.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.30.0...pubsub/v1.30.1) (2023-05-03)

##### Bug Fixes

  * **pubsub/pstest:** Clear Subscription when calling `ClearMessages`. ([6de8eda](https://github.com/googleapis/google-cloud-go/commit/6de8edada13c751ded733e924174e5b46277fcc6))
  * **pubsub/pstest:** Start `DeliveryAttempt` at 1 ([2bf6e14](https://github.com/googleapis/google-cloud-go/commit/2bf6e14ef5d04f9ac2be786086538d395a8e7393))



##### Documentation

  * **pubsub:** Clarify NumGoroutines configures number of streams ([#7874](https://github.com/googleapis/google-cloud-go/issues/7874)) ([8ac4432](https://github.com/googleapis/google-cloud-go/commit/8ac4432e5d3e77a61119943537915230c0e5b7e9))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.16.1](https://github.com/googleapis/python-pubsub/compare/v2.16.0...v2.16.1) (2023-05-05)

##### Bug Fixes

  * Allow dropping cleaned-up keys ([#911](https://github.com/googleapis/python-pubsub/issues/911)) ([4b3157c](https://github.com/googleapis/python-pubsub/commit/4b3157ccb83771a2e613fc3475035f24d358ccf6))



##### Documentation

  * Add comment to setup.py ([#905](https://github.com/googleapis/python-pubsub/issues/905)) ([9825109](https://github.com/googleapis/python-pubsub/commit/9825109a826e63cd076c21367157be7a3c01c45b))



## May 01, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.5.2](https://github.com/googleapis/nodejs-pubsub/compare/v3.5.1...v3.5.2) (2023-04-26)

##### Bug Fixes

  * Avoid zalgo when calling down to publish messages ([#1710](https://github.com/googleapis/nodejs-pubsub/issues/1710)) ([dedae1e](https://github.com/googleapis/nodejs-pubsub/commit/dedae1e46cb3214abc33578a878a2298cdae6cac))



#### [3.5.1](https://github.com/googleapis/nodejs-pubsub/compare/v3.5.0...v3.5.1) (2023-04-20)

##### Bug Fixes

  * Handle receipt modAck and lease extensions with exactly-once delivery correctly ([#1709](https://github.com/googleapis/nodejs-pubsub/issues/1709)) ([d786d22](https://github.com/googleapis/nodejs-pubsub/commit/d786d22bfec61b91891e5049f1b5ae2d9a81d788))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.11](https://github.com/googleapis/java-pubsub/compare/v1.123.10...v1.123.11) (2023-04-27)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.15.0 ([#1558](https://github.com/googleapis/java-pubsub/issues/1558)) ([acf0a4f](https://github.com/googleapis/java-pubsub/commit/acf0a4f1b893b5be19167e87b958e722e53b2aee))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.8.0 ([#1561](https://github.com/googleapis/java-pubsub/issues/1561)) ([13bfd09](https://github.com/googleapis/java-pubsub/commit/13bfd09a9ba81e725a61f2b36c5d38fabcd8df56))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.9.3 ([#1563](https://github.com/googleapis/java-pubsub/issues/1563)) ([c2329d2](https://github.com/googleapis/java-pubsub/commit/c2329d289d3447e72904d20e9c89065b59d7e6de))



## April 24, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.5.0](https://github.com/googleapis/nodejs-pubsub/compare/v3.4.1...v3.5.0) (2023-04-16)

##### Features

  * Rework low level message stream retries, add debugging ([#1713](https://github.com/googleapis/nodejs-pubsub/issues/1713)) ([c1cc6e0](https://github.com/googleapis/nodejs-pubsub/commit/c1cc6e043ab2e532f9c8c9f9158c46e9a424d3dd))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.10](https://github.com/googleapis/java-pubsub/compare/v1.123.9...v1.123.10) (2023-04-17)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.24.5 ([#1555](https://github.com/googleapis/java-pubsub/issues/1555)) ([7d81b06](https://github.com/googleapis/java-pubsub/commit/7d81b063465f23b1779c2137bc1706dafdaea042))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.7.0 ([#1551](https://github.com/googleapis/java-pubsub/issues/1551)) ([bccf566](https://github.com/googleapis/java-pubsub/commit/bccf566c6072aa34ebad451880835625217f9fe4))



## April 17, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.9](https://github.com/googleapis/java-pubsub/compare/v1.123.8...v1.123.9) (2023-04-13)

##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.21 ([#1547](https://github.com/googleapis/java-pubsub/issues/1547)) ([e78f210](https://github.com/googleapis/java-pubsub/commit/e78f210c9b72b0b9fb561ef8f41eb1aa2d8be4d7))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.21 ([#1548](https://github.com/googleapis/java-pubsub/issues/1548)) ([42957f8](https://github.com/googleapis/java-pubsub/commit/42957f8c93a07c7db5e3f007644b9508ef9dfe73))



## April 10, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.8](https://github.com/googleapis/java-pubsub/compare/v1.123.7...v1.123.8) (2023-04-04)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.6.0 ([#1541](https://github.com/googleapis/java-pubsub/issues/1541)) ([828db7c](https://github.com/googleapis/java-pubsub/commit/828db7cfde91284db019b85552d64ca92e8ebe07))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.16.0](https://github.com/googleapis/python-pubsub/compare/v2.15.2...v2.16.0) (2023-04-06)

##### Features

  * Enable "rest" transport in Python for services supporting numeric enums ([#863](https://github.com/googleapis/python-pubsub/issues/863)) ([a80c1d1](https://github.com/googleapis/python-pubsub/commit/a80c1d1f6f880cd13c247231bdc86c824edab8cb))



##### Documentation

  * Fix formatting of request arg in docstring ([#894](https://github.com/googleapis/python-pubsub/issues/894)) ([ee2ea73](https://github.com/googleapis/python-pubsub/commit/ee2ea7341268fd5428d98208b8af2fc96efe8d03))



## March 27, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.30.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.29.0...pubsub/v1.30.0) (2023-03-22)

##### Features

  * **pubsub:** Update iam and longrunning deps ([91a1f78](https://github.com/googleapis/google-cloud-go/commit/91a1f784a109da70f63b96414bba8a9b4254cddd))



##### Bug Fixes

  * **pubsub:** Check response of receipt modacks for exactly once delivery ([#7568](https://github.com/googleapis/google-cloud-go/issues/7568)) ([94d0408](https://github.com/googleapis/google-cloud-go/commit/94d040898cc9e85fdac76560765b01cfd019d0b4))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.7](https://github.com/googleapis/java-pubsub/compare/v1.123.6...v1.123.7) (2023-03-21)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.5.0 ([#1532](https://github.com/googleapis/java-pubsub/issues/1532)) ([d63fba7](https://github.com/googleapis/java-pubsub/commit/d63fba73d5ea445144f625f7b67622351694c818))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.15.2](https://github.com/googleapis/python-pubsub/compare/v2.15.1...v2.15.2) (2023-03-20)

##### Documentation

  * Update missing docstrings ([#890](https://github.com/googleapis/python-pubsub/issues/890)) ([5849e04](https://github.com/googleapis/python-pubsub/commit/5849e048f48074e3a8ecddbe3bfbcfc9da094a28))



## March 21, 2023

Feature

Generally available: In projects protected by a service perimeter, and if using Eventarc to route events to Workflows destinations, you can create a new push subscription through Eventarc where the endpoint is set to a Workflows execution. To know more, see [Set up a service perimeter using VPC Service Controls](https://docs.cloud.google.com/eventarc/docs/using-vpc-service-controls).

Feature

Pub/Sub is now available in Turin, Italy (`europe-west12`).

## March 20, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.29.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.28.0...pubsub/v1.29.0) (2023-03-13)

##### Features

  * **pubsub:** Add google.api.method.signature to update methods ([aeb6fec](https://github.com/googleapis/google-cloud-go/commit/aeb6fecc7fd3f088ff461a0c068ceb9a7ae7b2a3))
  * **pubsub:** Add REST client ([06a54a1](https://github.com/googleapis/google-cloud-go/commit/06a54a16a5866cce966547c51e203b9e09a25bc0))
  * **pubsub:** Add schema evolution methods and fields ([ee41485](https://github.com/googleapis/google-cloud-go/commit/ee41485860bcbbd09ce4e28ee6ddca81a5f17211))
  * **pubsub:** Add support for schema revisions ([#7295](https://github.com/googleapis/google-cloud-go/issues/7295)) ([369b16f](https://github.com/googleapis/google-cloud-go/commit/369b16f9525f9ac9a0811c66ce61eda9f6c566e4))
  * **pubsub:** Add temporary_failed_ack_ids to ModifyAckDeadlineConfirmation ([aeb6fec](https://github.com/googleapis/google-cloud-go/commit/aeb6fecc7fd3f088ff461a0c068ceb9a7ae7b2a3))
  * **pubsub:** Make INTERNAL a retryable error for Pull ([aeb6fec](https://github.com/googleapis/google-cloud-go/commit/aeb6fecc7fd3f088ff461a0c068ceb9a7ae7b2a3))



##### Bug Fixes

  * **pubsub/pstest:** Fix panic on undelivered message ([#7377](https://github.com/googleapis/google-cloud-go/issues/7377)) ([98dd29d](https://github.com/googleapis/google-cloud-go/commit/98dd29d372073605145f78f08205a9786c698881))
  * **pubsub:** Allow updating topic schema fields individually ([#7362](https://github.com/googleapis/google-cloud-go/issues/7362)) ([f09e059](https://github.com/googleapis/google-cloud-go/commit/f09e059e3203de5294648d7434d5e65626a6dff5))
  * **pubsub:** Dont compare revision fields in schema config test ([#7317](https://github.com/googleapis/google-cloud-go/issues/7317)) ([e364f7a](https://github.com/googleapis/google-cloud-go/commit/e364f7abfe3ec8fc20db78abcdaeaaf27d19269c))
  * **pubsub:** Fix bug with AckWithResult with exactly once disabled ([#7319](https://github.com/googleapis/google-cloud-go/issues/7319)) ([c88fbdf](https://github.com/googleapis/google-cloud-go/commit/c88fbdf299205e8118b347430cf66540ffa68b27))
  * **pubsub:** Pipe revision ID in name in DeleteSchemaRevision ([#7519](https://github.com/googleapis/google-cloud-go/issues/7519)) ([e211635](https://github.com/googleapis/google-cloud-go/commit/e211635216e553a9a6b00f9e8f2c5d2082ff68a8))



##### Documentation

  * **pubsub:** Add x-ref for ordering messages docs: Clarify subscription expiration policy ([aeb6fec](https://github.com/googleapis/google-cloud-go/commit/aeb6fecc7fd3f088ff461a0c068ceb9a7ae7b2a3))
  * **pubsub:** Clarify BigQueryConfig PERMISSION_DENIED state ([aeb6fec](https://github.com/googleapis/google-cloud-go/commit/aeb6fecc7fd3f088ff461a0c068ceb9a7ae7b2a3))
  * **pubsub:** Clarify subscription description ([aeb6fec](https://github.com/googleapis/google-cloud-go/commit/aeb6fecc7fd3f088ff461a0c068ceb9a7ae7b2a3))
  * **pubsub:** Mark revision_id in CommitSchemaRevisionRequest deprecated ([2fef56f](https://github.com/googleapis/google-cloud-go/commit/2fef56f75a63dc4ff6e0eea56c7b26d4831c8e27))
  * **pubsub:** Replacing HTML code with Markdown docs: Fix PullResponse description docs: Fix Pull description ([aeb6fec](https://github.com/googleapis/google-cloud-go/commit/aeb6fecc7fd3f088ff461a0c068ceb9a7ae7b2a3))
  * **pubsub:** Update Pub/Sub topic retention limit from 7 days to 31 days ([aeb6fec](https://github.com/googleapis/google-cloud-go/commit/aeb6fecc7fd3f088ff461a0c068ceb9a7ae7b2a3))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.6](https://github.com/googleapis/java-pubsub/compare/v1.123.5...v1.123.6) (2023-03-14)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.23.2 ([#1512](https://github.com/googleapis/java-pubsub/issues/1512)) ([60e889e](https://github.com/googleapis/java-pubsub/commit/60e889e587511cc948af440be7733dc4af531dd1))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.15.1](https://github.com/googleapis/python-pubsub/compare/v2.15.0...v2.15.1) (2023-03-14)

##### Bug Fixes

  * Set x-goog-request-params for streaming pull request ([#884](https://github.com/googleapis/python-pubsub/issues/884)) ([0d247e6](https://github.com/googleapis/python-pubsub/commit/0d247e6b189409b4d57c95dbbbf3df3e0fac0fa2))



## March 13, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.4.1](https://github.com/googleapis/nodejs-pubsub/compare/v3.4.0...v3.4.1) (2023-03-08)

##### Bug Fixes

  * Update minimum google-gax to avoid taffydb vulnerabilities ([#1695](https://github.com/googleapis/nodejs-pubsub/issues/1695)) ([11372e6](https://github.com/googleapis/nodejs-pubsub/commit/11372e6d40577704a8a22b6c010623be7e36b34a))



#### [3.4.0](https://github.com/googleapis/nodejs-pubsub/compare/v3.3.0...v3.4.0) (2023-03-06)

##### Features

  * Add google.api.method.signature to update methods ([1e28405](https://github.com/googleapis/nodejs-pubsub/commit/1e2840529a8451c94d5d845062da84729b7843db))
  * Add temporary_failed_ack_ids to ModifyAckDeadlineConfirmation ([1e28405](https://github.com/googleapis/nodejs-pubsub/commit/1e2840529a8451c94d5d845062da84729b7843db))
  * Make INTERNAL a retryable error for Pull ([#1681](https://github.com/googleapis/nodejs-pubsub/issues/1681)) ([1e28405](https://github.com/googleapis/nodejs-pubsub/commit/1e2840529a8451c94d5d845062da84729b7843db))



##### Bug Fixes

  * Don't do multiple drains per publish() in message queues unless requested ([#1691](https://github.com/googleapis/nodejs-pubsub/issues/1691)) ([d9b3a63](https://github.com/googleapis/nodejs-pubsub/commit/d9b3a63ddbfec0581a0e05fdbfcf9e9326b3dcf9))



Feature

General availability: You can now [update the schemas](https://docs.cloud.google.com/pubsub/docs/schemas) that you create in Pub/Sub. Before you do so, read the [guidelines](https://docs.cloud.google.com/pubsub/docs/schemas#commit-schema-revision). The change is being rolled out in a phased manner over the rest of the week.

## March 06, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.5](https://github.com/googleapis/java-pubsub/compare/v1.123.4...v1.123.5) (2023-03-03)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.12.0 ([#1509](https://github.com/googleapis/java-pubsub/issues/1509)) ([6f70d8a](https://github.com/googleapis/java-pubsub/commit/6f70d8a96577ac93647f4d13adc6b31889efeddf))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.4.0 ([#1510](https://github.com/googleapis/java-pubsub/issues/1510)) ([0d0ece7](https://github.com/googleapis/java-pubsub/commit/0d0ece70f1527932abb04d9719de68a1367c5881))



## February 27, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.4](https://github.com/googleapis/java-pubsub/compare/v1.123.3...v1.123.4) (2023-02-22)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.23.0 ([#1496](https://github.com/googleapis/java-pubsub/issues/1496)) ([713d727](https://github.com/googleapis/java-pubsub/commit/713d727db447f02e3c6cc7dfbb656fcebba54121))



#### [1.123.3](https://github.com/googleapis/java-pubsub/compare/v1.123.2...v1.123.3) (2023-02-22)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.21.0 ([#1470](https://github.com/googleapis/java-pubsub/issues/1470)) ([105c293](https://github.com/googleapis/java-pubsub/commit/105c2933d3f71389e2629e4871767199fe53f7f4))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.22.0 ([#1489](https://github.com/googleapis/java-pubsub/issues/1489)) ([665436c](https://github.com/googleapis/java-pubsub/commit/665436cb9a0900fd62a6197e73baecf13de21597))
  * Update dependency com.google.cloud:google-cloud-core to v2.10.0 ([#1464](https://github.com/googleapis/java-pubsub/issues/1464)) ([8cab4e2](https://github.com/googleapis/java-pubsub/commit/8cab4e2f0b8455a30aa71a7915a836730ee7f059))
  * Update dependency com.google.cloud:google-cloud-core to v2.11.0 ([#1490](https://github.com/googleapis/java-pubsub/issues/1490)) ([c42474a](https://github.com/googleapis/java-pubsub/commit/c42474a8c1a98e7533edef47acf9c7210b99a56e))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.3.0 ([#1491](https://github.com/googleapis/java-pubsub/issues/1491)) ([e5e3227](https://github.com/googleapis/java-pubsub/commit/e5e32273a515cf9ce22ffffb58a8f7a252556526))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.20 ([#1484](https://github.com/googleapis/java-pubsub/issues/1484)) ([8206d12](https://github.com/googleapis/java-pubsub/commit/8206d129d819617a3dd8ebdab531d3fc7b7289f1))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.20 ([#1485](https://github.com/googleapis/java-pubsub/issues/1485)) ([d0e9b2a](https://github.com/googleapis/java-pubsub/commit/d0e9b2a8197f91029ae26fdec7e88f7ca38dab79))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.15.0](https://github.com/googleapis/python-pubsub/compare/v2.14.1...v2.15.0) (2023-02-22)

##### Features

  * Add google.api.method.signature to update methods ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))
  * Add temporary_failed_ack_ids to ModifyAckDeadlineConfirmation ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))



##### Bug Fixes

  * Add service_yaml_parameters to py_gapic_library BUILD.bazel targets ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))
  * Move global import in publisher sample ([#866](https://github.com/googleapis/python-pubsub/issues/866)) ([271a46d](https://github.com/googleapis/python-pubsub/commit/271a46d4da0c668674a36c0f58bbe0fe70985b75))
  * Port proto changes ([#871](https://github.com/googleapis/python-pubsub/issues/871)) ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))



##### Documentation

  * Clarify BigQueryConfig PERMISSION_DENIED state ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))
  * Clarify subscription description ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))
  * Fix Pull description ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))
  * Fix PullResponse description ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))
  * Replacing HTML code with Markdown ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))
  * Update Pub/Sub topic retention limit from 7 days to 31 days ([3dd43d6](https://github.com/googleapis/python-pubsub/commit/3dd43d6c9facc59c7c4913cac605aa95176cc857))



## February 13, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.2](https://github.com/googleapis/java-pubsub/compare/v1.123.1...v1.123.2) (2023-02-06)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.2.0 ([#1474](https://github.com/googleapis/java-pubsub/issues/1474)) ([5fccae4](https://github.com/googleapis/java-pubsub/commit/5fccae49f912a24c14d144fdcc9617d5a5ae110a))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.14.1](https://github.com/googleapis/python-pubsub/compare/v2.14.0...v2.14.1) (2023-02-08)

##### Bug Fixes

  * Add context manager return types ([4f690b9](https://github.com/googleapis/python-pubsub/commit/4f690b9287beefbca6505cf88637f4a8c5077152))



##### Documentation

  * Add documentation for enums ([4f690b9](https://github.com/googleapis/python-pubsub/commit/4f690b9287beefbca6505cf88637f4a8c5077152))
  * Mark revision_id in CommitSchemaRevisionRequest as deprecated ([#861](https://github.com/googleapis/python-pubsub/issues/861)) ([09b846d](https://github.com/googleapis/python-pubsub/commit/09b846ddd066519c0570522b8525ec5705714b0a))



## January 30, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.3.0](https://github.com/googleapis/nodejs-pubsub/compare/v3.2.1...v3.3.0) (2023-01-23)

##### Features

  * Add schema evolution methods and fields ([#1672](https://github.com/googleapis/nodejs-pubsub/issues/1672)) ([7a5bc29](https://github.com/googleapis/nodejs-pubsub/commit/7a5bc29e8a39e5c1991a5eae4200a5045f21997d))



##### Bug Fixes

  * Remove redundant .then() ([#1671](https://github.com/googleapis/nodejs-pubsub/issues/1671)) ([108edc3](https://github.com/googleapis/nodejs-pubsub/commit/108edc3cd2d3d512e2a9777a68541dae1f6aba23))



## January 23, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.1](https://github.com/googleapis/java-pubsub/compare/v1.123.0...v1.123.1) (2023-01-20)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.20.2 ([#1441](https://github.com/googleapis/java-pubsub/issues/1441)) ([a675556](https://github.com/googleapis/java-pubsub/commit/a67555664a070eb03b6f8bb7115e32e2b9d9a11a))
  * Update dependency com.google.cloud:google-cloud-core to v2.9.2 ([#1449](https://github.com/googleapis/java-pubsub/issues/1449)) ([e68c9e0](https://github.com/googleapis/java-pubsub/commit/e68c9e0e0808c441e04049154fb0c44f42fed562))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.2 ([#1463](https://github.com/googleapis/java-pubsub/issues/1463)) ([e9e6649](https://github.com/googleapis/java-pubsub/commit/e9e664951b027979969e983c7e525aff6e4ddc68))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.21.12 ([#1437](https://github.com/googleapis/java-pubsub/issues/1437)) ([88f7a99](https://github.com/googleapis/java-pubsub/commit/88f7a991c43e6358ccc3ad248473400a2a0e50e8))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.9.2 ([#1451](https://github.com/googleapis/java-pubsub/issues/1451)) ([054572a](https://github.com/googleapis/java-pubsub/commit/054572a86ecc2cedcdbcf3eae8c9fb07caed504a))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.14.0](https://github.com/googleapis/python-pubsub/compare/v2.13.12...v2.14.0) (2023-01-18)

##### Features

  * Add schema evolution methods and fields ([9479356](https://github.com/googleapis/python-pubsub/commit/9479356029f28c565a06ab759330c6e430a47c51))
  * Add support for python 3.11 ([9479356](https://github.com/googleapis/python-pubsub/commit/9479356029f28c565a06ab759330c6e430a47c51))



## January 16, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.123.0](https://github.com/googleapis/java-pubsub/compare/v1.122.2...v1.123.0) (2023-01-10)

##### Features

  * Add schema evolution methods and fields ([#1384](https://github.com/googleapis/java-pubsub/issues/1384)) ([746a6e0](https://github.com/googleapis/java-pubsub/commit/746a6e040eb94d73bfbaece051d08c60c9885326))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.1 ([#1450](https://github.com/googleapis/java-pubsub/issues/1450)) ([2dcbcad](https://github.com/googleapis/java-pubsub/commit/2dcbcadfa56282733ab7998ec9cf360f0a71eaca))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.13.12](https://github.com/googleapis/python-pubsub/compare/v2.13.11...v2.13.12) (2023-01-06)

##### Bug Fixes

  * **deps:** Require google-api-core >=1.34.0, >=2.11.0 ([060f00b](https://github.com/googleapis/python-pubsub/commit/060f00bcea5cd129be3a2d37078535cc97b4f5e8))
  * Drop usage of pkg_resources ([060f00b](https://github.com/googleapis/python-pubsub/commit/060f00bcea5cd129be3a2d37078535cc97b4f5e8))
  * Fix timeout default values ([060f00b](https://github.com/googleapis/python-pubsub/commit/060f00bcea5cd129be3a2d37078535cc97b4f5e8))



##### Documentation

  * **samples:** Snippetgen should call await on the operation coroutine before calling result ([060f00b](https://github.com/googleapis/python-pubsub/commit/060f00bcea5cd129be3a2d37078535cc97b4f5e8))



## December 19, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.122.2](https://github.com/googleapis/java-pubsub/compare/v1.122.1...v1.122.2) (2022-12-15)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.9.0 ([#1435](https://github.com/googleapis/java-pubsub/issues/1435)) ([786c493](https://github.com/googleapis/java-pubsub/commit/786c49303bc196e548b00ef0cf39d766e8fd71a8))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.0 ([#1436](https://github.com/googleapis/java-pubsub/issues/1436)) ([a40337b](https://github.com/googleapis/java-pubsub/commit/a40337b493454d20a12f70b7817de7b0f2584b84))



## December 14, 2022

Announcement

The Pull subscription guide is now updated with improved conceptual information regarding the following topics:

  * [StreamingPull and the Pull API](https://docs.cloud.google.com/pubsub/docs/pull#service_apis)

  * [Asynchronous and synchronous pull mode](https://docs.cloud.google.com/pubsub/docs/pull#types_of_message_processing_modes)

  * [Pub/Sub client libraries](https://docs.cloud.google.com/pubsub/docs/pull#client_libraries)




## December 12, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.28.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.27.1...pubsub/v1.28.0) (2022-12-05)

##### Features

  * **pubsub:** rewrite signatures and type in terms of new location ([620e6d8](https://github.com/googleapis/google-cloud-go/commit/620e6d828ad8641663ae351bfccfe46281e817ad))



## December 05, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.27.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.27.0...pubsub/v1.27.1) (2022-12-02)

##### Bug Fixes

  * **pubsub:** downgrade some dependencies ([7540152](https://github.com/googleapis/google-cloud-go/commit/754015236d5af7c82a75da218b71a87b9ead6eb5))



#### [1.27.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.26.0...pubsub/v1.27.0) (2022-11-29)

##### Features

  * **pubsub:** start generating proto stubs ([cf89415](https://github.com/googleapis/google-cloud-go/commit/cf894154e451a32b431fef2af3781a0d2d8080ff))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.122.1](https://github.com/googleapis/java-pubsub/compare/v1.122.0...v1.122.1) (2022-12-02)

##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.19 ([#1428](https://github.com/googleapis/java-pubsub/issues/1428)) ([bfa9c3d](https://github.com/googleapis/java-pubsub/commit/bfa9c3d5f8f7b0d3103fe5d398ed3f753e1bedca))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.19 ([#1429](https://github.com/googleapis/java-pubsub/issues/1429)) ([d3c44e7](https://github.com/googleapis/java-pubsub/commit/d3c44e77532068e53d7d64dd182295ab6b9644bd))



#### [1.122.0](https://github.com/googleapis/java-pubsub/compare/v1.121.1...v1.122.0) (2022-12-01)

##### Features

  * Next release from main branch is 1.122.0 ([#1409](https://github.com/googleapis/java-pubsub/issues/1409)) ([dad2c82](https://github.com/googleapis/java-pubsub/commit/dad2c82cc22ed40def105514a4bc8446375dc70e))



##### Dependencies

  * Update dependency com.google.protobuf:protobuf-java-util to v3.21.10 ([#1425](https://github.com/googleapis/java-pubsub/issues/1425)) ([39c22cb](https://github.com/googleapis/java-pubsub/commit/39c22cb99dadd1dea874e0a57cf2c9fb0dd67328))



## December 01, 2022

Announcement

[Exactly once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery) is now GA.

## November 28, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.121.1](https://github.com/googleapis/java-pubsub/compare/v1.121.0...v1.121.1) (2022-11-21)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.18.0 ([#1375](https://github.com/googleapis/java-pubsub/issues/1375)) ([b6ada4e](https://github.com/googleapis/java-pubsub/commit/b6ada4e06397d785b6747bd989fe6cd9d6e76801))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.19.1 ([#1416](https://github.com/googleapis/java-pubsub/issues/1416)) ([e140a49](https://github.com/googleapis/java-pubsub/commit/e140a4975a5bff4c73254784409f4f3dda27db09))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.18 ([#1413](https://github.com/googleapis/java-pubsub/issues/1413)) ([b3fb828](https://github.com/googleapis/java-pubsub/commit/b3fb828480f491e4275adf0b6367aeb51ac0569e))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.18 ([#1414](https://github.com/googleapis/java-pubsub/issues/1414)) ([74d2dc3](https://github.com/googleapis/java-pubsub/commit/74d2dc3329f6d4e33c977fa1e73df1aca278b9b3))



## November 21, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.121.0](https://github.com/googleapis/java-pubsub/compare/v1.120.25...v1.121.0) (2022-11-16)

##### Features

  * Next release from main branch is 1.121.0 ([#1406](https://github.com/googleapis/java-pubsub/issues/1406)) ([1b25b0e](https://github.com/googleapis/java-pubsub/commit/1b25b0e01a7b1068dbebaa5d6516419c11e31b96))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.8.28 ([#1399](https://github.com/googleapis/java-pubsub/issues/1399)) ([ec1cae8](https://github.com/googleapis/java-pubsub/commit/ec1cae87596921078478ed96a22b9ca5b138f729))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.6 ([#1395](https://github.com/googleapis/java-pubsub/issues/1395)) ([a3c32ea](https://github.com/googleapis/java-pubsub/commit/a3c32eadb8e6d4ce730f2f2d1f8960ccd6269ecb))



## November 18, 2022

Feature

The [Kafka Connector library](https://github.com/googleapis/java-pubsub-group-kafka-connector) for Pub/Sub and Pub/Sub Lite is now generally available.

## November 15, 2022

Feature

BigQuery subscriptions now support the JSON type for all string fields, including `data` and `attributes`. For more information about JSON type compatibility, see [Properties of a BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery#properties_subscription).

## November 14, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.25](https://github.com/googleapis/java-pubsub/compare/v1.120.24...v1.120.25) (2022-11-09)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.8.27 ([#1391](https://github.com/googleapis/java-pubsub/issues/1391)) ([dd9f1c3](https://github.com/googleapis/java-pubsub/commit/dd9f1c366c9aa5f78dccc01a4dc3e2ee42290be3))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.21.9 ([#1370](https://github.com/googleapis/java-pubsub/issues/1370)) ([8b753a4](https://github.com/googleapis/java-pubsub/commit/8b753a452a3f778402b61565d38a9a2ce90f084a))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.17 ([#1389](https://github.com/googleapis/java-pubsub/issues/1389)) ([6def6bb](https://github.com/googleapis/java-pubsub/commit/6def6bbff8c31af6a008fee89654a13b0db1550f))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.17 ([#1388](https://github.com/googleapis/java-pubsub/issues/1388)) ([0924923](https://github.com/googleapis/java-pubsub/commit/0924923039e30716d66ad8ca519fbdae88946807))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.13.11](https://github.com/googleapis/python-pubsub/compare/v2.13.10...v2.13.11) (2022-11-11)

##### Bug Fixes

  * Remove suboptimal logic in leasing behavior ([#816](https://github.com/googleapis/python-pubsub/issues/816)) ([f067af3](https://github.com/googleapis/python-pubsub/commit/f067af348b8d3deb72981c58d942e887c0efb5ff))



## November 07, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.2.1](https://github.com/googleapis/nodejs-pubsub/compare/v3.2.0...v3.2.1) (2022-11-04)

##### Bug Fixes

  * **deps:** Use google-gax v3.5.2 ([#1652](https://github.com/googleapis/nodejs-pubsub/issues/1652)) ([ee308b5](https://github.com/googleapis/nodejs-pubsub/commit/ee308b596802ad5537a89804a95429d630595eb4))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.111.0-sp.3](https://github.com/googleapis/java-pubsub/compare/v1.111.0-sp.2...v1.111.0-sp.3) (2022-11-03)

##### Dependencies

  * Regenerating with new Protobuf (1.111.0-sp) ([#1382](https://github.com/googleapis/java-pubsub/issues/1382)) ([58d55aa](https://github.com/googleapis/java-pubsub/commit/58d55aa1290a62d2f3e9708e815c7392a49903df))



## November 01, 2022

Feature

BigQuery subscriptions now support the Avro logical types timestamp-micros, date, and time-micros. For more information about schema compatibility between a Pub/Sub topic and a BigQuery table, see [Schema compatibility](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).

## October 31, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.26.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.25.1...pubsub/v1.26.0) (2022-10-24)

##### Features

  * **pubsub:** Add support for snapshot labels ([#6835](https://github.com/googleapis/google-cloud-go/issues/6835)) ([c17851b](https://github.com/googleapis/google-cloud-go/commit/c17851b5c3d811cd3e6a28162f0e399bb31a1363))



##### Bug Fixes

  * **pubsub:** Remove unused AckResult map ([#6656](https://github.com/googleapis/google-cloud-go/issues/6656)) ([5f69002](https://github.com/googleapis/google-cloud-go/commit/5f690022551ac584e5c66af4324a17d7044a898d))



##### Documentation

  * **pubsub:** Fix comments on message for exactly once delivery ([#6878](https://github.com/googleapis/google-cloud-go/issues/6878)) ([a8109e2](https://github.com/googleapis/google-cloud-go/commit/a8109e2d3257d1698ce1b751618428ef25cbb859)), refs [#6877](https://github.com/googleapis/google-cloud-go/issues/6877)
  * **pubsub:** Update streams section ([#6682](https://github.com/googleapis/google-cloud-go/issues/6682)) ([7b4e2b4](https://github.com/googleapis/google-cloud-go/commit/7b4e2b412058f965a9f9159231afe551a6f58a74))
  * **pubsub:** Update subscription retry policy defaults ([#6909](https://github.com/googleapis/google-cloud-go/issues/6909)) ([c5c2f8f](https://github.com/googleapis/google-cloud-go/commit/c5c2f8f7125034c611edf1d08ca35ece6554c454)), refs [#6903](https://github.com/googleapis/google-cloud-go/issues/6903)



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.24](https://github.com/googleapis/java-pubsub/compare/v1.120.23...v1.120.24) (2022-10-28)

##### Bug Fixes

  * Adding an explicit check to prevent empty publishes ([#1376](https://github.com/googleapis/java-pubsub/issues/1376)) ([689d7da](https://github.com/googleapis/java-pubsub/commit/689d7da1fee7c7def401ba114feef3607cd12cf5))



#### [1.120.23](https://github.com/googleapis/java-pubsub/compare/v1.120.22...v1.120.23) (2022-10-27)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.8.22 ([#1361](https://github.com/googleapis/java-pubsub/issues/1361)) ([0355868](https://github.com/googleapis/java-pubsub/commit/03558680b9fb6493c2c3f1f4b65d8a35668b440f))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.24 ([#1368](https://github.com/googleapis/java-pubsub/issues/1368)) ([9776aad](https://github.com/googleapis/java-pubsub/commit/9776aad7391544b1e0bd2fbe8576180206943bef))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.5 ([#1362](https://github.com/googleapis/java-pubsub/issues/1362)) ([d32c591](https://github.com/googleapis/java-pubsub/commit/d32c591af87b66d8ca9df599ad18183aae31bf15))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.21.8 ([#1356](https://github.com/googleapis/java-pubsub/issues/1356)) ([dc1e0ca](https://github.com/googleapis/java-pubsub/commit/dc1e0ca44c3668d7c9e780d50261dd81ce1d4ee9))
  * Update dependency org.easymock:easymock to v5.0.1 ([#1365](https://github.com/googleapis/java-pubsub/issues/1365)) ([2a807a5](https://github.com/googleapis/java-pubsub/commit/2a807a5b319ed3821da7dac84e4cb4923d07fed7))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.16 ([#1358](https://github.com/googleapis/java-pubsub/issues/1358)) ([226e105](https://github.com/googleapis/java-pubsub/commit/226e1050b0b643cea46bad7cf77d2a9e8857fb02))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.16 ([#1359](https://github.com/googleapis/java-pubsub/issues/1359)) ([3f10227](https://github.com/googleapis/java-pubsub/commit/3f10227cfd7d9029e92e7575771544c7e4b4dd67))



## October 24, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.22](https://github.com/googleapis/java-pubsub/compare/v1.120.21...v1.120.22) (2022-10-18)

##### Dependencies

  * Update dependency org.easymock:easymock to v5 ([#1350](https://github.com/googleapis/java-pubsub/issues/1350)) ([1e88543](https://github.com/googleapis/java-pubsub/commit/1e88543393ac16a79288c80d3561f7e5c50f11af))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.15 ([#1351](https://github.com/googleapis/java-pubsub/issues/1351)) ([2af7579](https://github.com/googleapis/java-pubsub/commit/2af757971fd54855936ad95e0cd3f6ab13d50edc))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.15 ([#1352](https://github.com/googleapis/java-pubsub/issues/1352)) ([379e39b](https://github.com/googleapis/java-pubsub/commit/379e39bdb6ed3cd50c5f034fb5ecd40905b43bda))



## October 17, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.21](https://github.com/googleapis/java-pubsub/compare/v1.120.20...v1.120.21) (2022-10-14)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.17.0 ([#1334](https://github.com/googleapis/java-pubsub/issues/1334)) ([d2edb44](https://github.com/googleapis/java-pubsub/commit/d2edb4457a5a5fdee006b34b1de265b7e73a26e1))
  * Update dependency com.google.cloud:google-cloud-bigquery to v2.17.1 ([#1340](https://github.com/googleapis/java-pubsub/issues/1340)) ([2b9c2e8](https://github.com/googleapis/java-pubsub/commit/2b9c2e8af4f83dd8d51272a0539c7ade05041a68))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.21 ([#1341](https://github.com/googleapis/java-pubsub/issues/1341)) ([d219a56](https://github.com/googleapis/java-pubsub/commit/d219a56de3c5a3e5455c3ca063bf0e363a4c476a))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.14 ([#1296](https://github.com/googleapis/java-pubsub/issues/1296)) ([00f61aa](https://github.com/googleapis/java-pubsub/commit/00f61aab905300986945bb67a8737779c3f72da6))



#### [1.117.1](https://github.com/googleapis/java-pubsub/compare/v1.117.0-sp.1...v1.117.1) (2022-10-13)

##### Dependencies

  * Regenerating with new Protobuf (1.117.x) ([#1342](https://github.com/googleapis/java-pubsub/issues/1342)) ([c0945b8](https://github.com/googleapis/java-pubsub/commit/c0945b8d6d29173cac8d68be64c0f4bbe7a88416))



##### Miscellaneous Chores

  * fixing sp.1 version in 1.117.x branch ([4399010](https://github.com/googleapis/java-pubsub/commit/43990102f0f752780c4d430c310d57c6d6b12c82))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.13.9](https://github.com/googleapis/python-pubsub/compare/v2.13.8...v2.13.9) (2022-10-10)

##### Bug Fixes

  * **deps:** Allow protobuf 3.19.5 ([#801](https://github.com/googleapis/python-pubsub/issues/801)) ([fa23503](https://github.com/googleapis/python-pubsub/commit/fa235033481783c2ec378b2a26b223bdff206461))



#### [2.13.9](https://github.com/googleapis/python-pubsub/compare/v2.13.8...v2.13.9) (2022-10-10)

##### Bug Fixes

  * **deps:** Allow protobuf 3.19.5 ([#801](https://github.com/googleapis/python-pubsub/issues/801)) ([fa23503](https://github.com/googleapis/python-pubsub/commit/fa235033481783c2ec378b2a26b223bdff206461))



#### [2.13.10](https://github.com/googleapis/python-pubsub/compare/v2.13.8...v2.13.10) (2022-10-14)

##### Bug Fixes

  * Batch at most 1,000 ack ids per request ([#802](https://github.com/googleapis/python-pubsub/issues/802)) ([4361e67](https://github.com/googleapis/python-pubsub/commit/4361e6735004a5600ee73979b99e6b9dd587c49b))
  * **deps:** Allow protobuf 3.19.5 ([#801](https://github.com/googleapis/python-pubsub/issues/801)) ([fa23503](https://github.com/googleapis/python-pubsub/commit/fa235033481783c2ec378b2a26b223bdff206461))
  * Silence invalid_ack_id warnings for receipt modacks ([#798](https://github.com/googleapis/python-pubsub/issues/798)) ([17feea5](https://github.com/googleapis/python-pubsub/commit/17feea5783f3a878b4dcfb3a8570585f7637378f))



##### Miscellaneous Chores

  * release as 2.13.10 ([34f022b](https://github.com/googleapis/python-pubsub/commit/34f022b4ee62d53a193bc2babafad508e2f2540b))



## October 10, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.20](https://github.com/googleapis/java-pubsub/compare/v1.120.19...v1.120.20) (2022-10-05)

##### Bug Fixes

  * update protobuf to v3.21.7 ([7c3ea60](https://github.com/googleapis/java-pubsub/commit/7c3ea6016e4288beab722a0c53c5ea132794e2bd))



#### [1.120.19](https://github.com/googleapis/java-pubsub/compare/v1.120.18...v1.120.19) (2022-10-03)

##### Dependencies

  * Update dependency cachetools to v5 ([#1324](https://github.com/googleapis/java-pubsub/issues/1324)) ([72b6d5f](https://github.com/googleapis/java-pubsub/commit/72b6d5f7ce6b464c1f1653699178e989c7eb6a75))
  * Update dependency certifi to v2022.9.24 ([#1303](https://github.com/googleapis/java-pubsub/issues/1303)) ([dc05237](https://github.com/googleapis/java-pubsub/commit/dc052371a1a83a194cb0098f93a8e8dd57d8e5d4))
  * Update dependency charset-normalizer to v2.1.1 ([#1308](https://github.com/googleapis/java-pubsub/issues/1308)) ([fedf2e1](https://github.com/googleapis/java-pubsub/commit/fedf2e1f98bf77de6d6cac18e745819e8250df57))
  * Update dependency click to v8.1.3 ([#1309](https://github.com/googleapis/java-pubsub/issues/1309)) ([0ddcb5b](https://github.com/googleapis/java-pubsub/commit/0ddcb5b324ecc4e3a8cc98bc2ef0d210061a79d5))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.15 ([#1299](https://github.com/googleapis/java-pubsub/issues/1299)) ([11f220c](https://github.com/googleapis/java-pubsub/commit/11f220ca32bf82c87746837e12ae878ee9578704))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.16 ([#1301](https://github.com/googleapis/java-pubsub/issues/1301)) ([186c794](https://github.com/googleapis/java-pubsub/commit/186c79497057847aa577b47d169e3535274b0a2d))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.17 ([#1326](https://github.com/googleapis/java-pubsub/issues/1326)) ([361a2f2](https://github.com/googleapis/java-pubsub/commit/361a2f2ae44098d280c1244479954638d4321a69))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.18 ([#1328](https://github.com/googleapis/java-pubsub/issues/1328)) ([ae23532](https://github.com/googleapis/java-pubsub/commit/ae23532092c80e3b4abe8e1b51f2ef67bb991428))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.20 ([#1329](https://github.com/googleapis/java-pubsub/issues/1329)) ([c37b88e](https://github.com/googleapis/java-pubsub/commit/c37b88e209dd1d58035385676d7c1dfca0da2c4e))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.4 ([#1330](https://github.com/googleapis/java-pubsub/issues/1330)) ([0f6cc6c](https://github.com/googleapis/java-pubsub/commit/0f6cc6c01e6afeb717487e7435575d243bd0203d))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.21.7 ([#1327](https://github.com/googleapis/java-pubsub/issues/1327)) ([6355eb0](https://github.com/googleapis/java-pubsub/commit/6355eb0ed1fa94a36fbb0169e4b6dc7faed165ff))
  * Update dependency gcp-releasetool to v1.8.8 ([#1304](https://github.com/googleapis/java-pubsub/issues/1304)) ([1c7c6eb](https://github.com/googleapis/java-pubsub/commit/1c7c6eb10a184919d36f7738f4594cd7aff9f87b))
  * Update dependency google-api-core to v2.10.1 ([#1310](https://github.com/googleapis/java-pubsub/issues/1310)) ([14725f2](https://github.com/googleapis/java-pubsub/commit/14725f248082c4397b0058d25984a61a9bf2c5c9))
  * Update dependency google-auth to v2.11.1 ([#1305](https://github.com/googleapis/java-pubsub/issues/1305)) ([a6954d1](https://github.com/googleapis/java-pubsub/commit/a6954d1cf17cb0247e5e153001ec983fb957b410))
  * Update dependency google-auth to v2.12.0 ([#1313](https://github.com/googleapis/java-pubsub/issues/1313)) ([ffcebe4](https://github.com/googleapis/java-pubsub/commit/ffcebe43542d4ab3b2cea1c2dcb5e6b345c4905b))
  * Update dependency google-cloud-core to v2.3.2 ([#1306](https://github.com/googleapis/java-pubsub/issues/1306)) ([fbb4460](https://github.com/googleapis/java-pubsub/commit/fbb44605794a350889ae300f697b76ed9ff41af2))
  * Update dependency importlib-metadata to v4.12.0 ([#1314](https://github.com/googleapis/java-pubsub/issues/1314)) ([e319df0](https://github.com/googleapis/java-pubsub/commit/e319df0bce76b1d8ba25b410225377d624070926))
  * Update dependency jeepney to v0.8.0 ([#1315](https://github.com/googleapis/java-pubsub/issues/1315)) ([5ed336e](https://github.com/googleapis/java-pubsub/commit/5ed336ef0b29fa89a1a508fbc2d3870b5ecff6d3))
  * Update dependency jinja2 to v3.1.2 ([#1316](https://github.com/googleapis/java-pubsub/issues/1316)) ([14ecdc6](https://github.com/googleapis/java-pubsub/commit/14ecdc6f3492e404957f1b16744a4928198d9e92))
  * Update dependency keyring to v23.9.3 ([#1317](https://github.com/googleapis/java-pubsub/issues/1317)) ([3e783d4](https://github.com/googleapis/java-pubsub/commit/3e783d47e8face65ef33b5bc7ca0bf7f0e35ca02))
  * Update dependency markupsafe to v2.1.1 ([#1318](https://github.com/googleapis/java-pubsub/issues/1318)) ([ecd9c76](https://github.com/googleapis/java-pubsub/commit/ecd9c76e2a9cce5c7f9dd6e9a8b84f748f69666a))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.14 ([#1297](https://github.com/googleapis/java-pubsub/issues/1297)) ([7e7ce60](https://github.com/googleapis/java-pubsub/commit/7e7ce60533386afdcd1b313603c468125ad0cb7d))
  * Update dependency protobuf to v3.20.2 ([#1319](https://github.com/googleapis/java-pubsub/issues/1319)) ([f5123fa](https://github.com/googleapis/java-pubsub/commit/f5123fa69ec7ac191d13c86823d105332853d944))
  * Update dependency pyjwt to v2.5.0 ([#1320](https://github.com/googleapis/java-pubsub/issues/1320)) ([a568462](https://github.com/googleapis/java-pubsub/commit/a568462b971908eb3424c9bbb5f49a6543c80fd3))
  * Update dependency requests to v2.28.1 ([#1321](https://github.com/googleapis/java-pubsub/issues/1321)) ([41b105a](https://github.com/googleapis/java-pubsub/commit/41b105a798aa9bcf2ce7ccde34efe119e76d963b))
  * Update dependency typing-extensions to v4.3.0 ([#1322](https://github.com/googleapis/java-pubsub/issues/1322)) ([288cd7e](https://github.com/googleapis/java-pubsub/commit/288cd7eaf90e219c735a89822e3858085e8423fd))
  * Update dependency zipp to v3.8.1 ([#1323](https://github.com/googleapis/java-pubsub/issues/1323)) ([e78a284](https://github.com/googleapis/java-pubsub/commit/e78a284cf07b9bac56087bbbb9f940ee976a3b4a))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.13.8](https://github.com/googleapis/python-pubsub/compare/v2.13.7...v2.13.8) (2022-10-03)

##### Bug Fixes

  * **deps:** Require protobuf >= 3.20.2 ([#792](https://github.com/googleapis/python-pubsub/issues/792)) ([1a54f7c](https://github.com/googleapis/python-pubsub/commit/1a54f7cd3d997270e0a5d70f7caea32d8753be76))



## September 29, 2022

Feature

The [Kafka Connector library](https://github.com/googleapis/java-pubsub-group-kafka-connector) for Pub/Sub and Pub/Sub Lite is now in preview.

## September 26, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.2.0](https://github.com/googleapis/nodejs-pubsub/compare/v3.1.1...v3.2.0) (2022-09-22)

##### Features

  * Add support for exactly once subscriptions ([#1572](https://github.com/googleapis/nodejs-pubsub/issues/1572)) ([998de35](https://github.com/googleapis/nodejs-pubsub/commit/998de35d4bffde4fcffd217347307c04031df3e2))



##### Bug Fixes

  * Preserve default values in x-goog-request-params header ([#1622](https://github.com/googleapis/nodejs-pubsub/issues/1622)) ([76c0ab5](https://github.com/googleapis/nodejs-pubsub/commit/76c0ab55ecfcf0cee5fad1314ecf2317d471c13a))
  * Wait for 'drain' as well ([#1636](https://github.com/googleapis/nodejs-pubsub/issues/1636)) ([d72db50](https://github.com/googleapis/nodejs-pubsub/commit/d72db503bfa3b9b6d7481ce44eb161a031f76715))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.18](https://github.com/googleapis/java-pubsub/compare/v1.120.17...v1.120.18) (2022-09-21)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-core to v2.8.13 ([#1288](https://github.com/googleapis/java-pubsub/issues/1288)) ([708a1df](https://github.com/googleapis/java-pubsub/commit/708a1df692b64d86915133ac4ae87e45f4d669d8))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.14 ([#1291](https://github.com/googleapis/java-pubsub/issues/1291)) ([1c479de](https://github.com/googleapis/java-pubsub/commit/1c479de525a28fc323697d9a4e92f6ee3215a18f))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.9.1 ([#1289](https://github.com/googleapis/java-pubsub/issues/1289)) ([216ba7d](https://github.com/googleapis/java-pubsub/commit/216ba7db4f0fab29c4bf9fc785387b23f64beb5e))



#### [1.120.17](https://github.com/googleapis/java-pubsub/compare/v1.120.16...v1.120.17) (2022-09-20)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.16.1 ([#1281](https://github.com/googleapis/java-pubsub/issues/1281)) ([aca8ee9](https://github.com/googleapis/java-pubsub/commit/aca8ee98dc74ecc53045f7b84326d85406163338))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.12 ([#1278](https://github.com/googleapis/java-pubsub/issues/1278)) ([4ae1156](https://github.com/googleapis/java-pubsub/commit/4ae115666ba195dca90171a7e1ff81bb6cfcf123))
  * Update dependency com.google.protobuf:protobuf-java-util to v3.21.6 ([#1277](https://github.com/googleapis/java-pubsub/issues/1277)) ([a5aa281](https://github.com/googleapis/java-pubsub/commit/a5aa281787b7a92516ebcc7654d419d9cbd5abc3))



### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.13.7](https://github.com/googleapis/python-pubsub/compare/v2.13.6...v2.13.7) (2022-09-22)

##### Bug Fixes

  * Remove expired ack_ids ([#787](https://github.com/googleapis/python-pubsub/issues/787)) ([b4b809d](https://github.com/googleapis/python-pubsub/commit/b4b809d616cf93881815d6baadf2dd322ab566d1))



## September 20, 2022

Feature

Pub/Sub introduces new monitoring dashboards for topics and subscriptions which you can access from the **Topics** and **Subscriptions** console pages. See [Monitor topics](https://docs.cloud.google.com/pubsub/docs/monitor-topic) and [Monitor subscriptions](https://docs.cloud.google.com/pubsub/docs/monitor-subscription).

## September 19, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.16](https://github.com/googleapis/java-pubsub/compare/v1.120.15...v1.120.16) (2022-09-15)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.3 ([#1279](https://github.com/googleapis/java-pubsub/issues/1279)) ([654ea40](https://github.com/googleapis/java-pubsub/commit/654ea400f5df0b2544f4b668e1f5ee72f3ea54d2))



#### [1.120.15](https://github.com/googleapis/java-pubsub/compare/v1.120.14...v1.120.15) (2022-09-13)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.16.0 ([#1271](https://github.com/googleapis/java-pubsub/issues/1271)) ([439215a](https://github.com/googleapis/java-pubsub/commit/439215aaee1572859d323139c7a86e086a331486))



## September 14, 2022

Feature

BigQuery subscriptions support writing `string` fields in a Pub/Sub message to `TIMESTAMP`, `DATETIME`, `DATE`, or `TIME` columns in a BigQuery table. For more information about schema compatibility between a Pub/Sub topic and a BigQuery table, see [Schema compatibility](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).

## September 13, 2022

Feature

Pub/Sub is now available in `me-west1` (Tel Aviv, Israel).

## September 12, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/pubsub](https://github.com/googleapis/nodejs-pubsub)

#### [3.1.1](https://github.com/googleapis/nodejs-pubsub/compare/v3.1.0...v3.1.1) (2022-09-01)

##### Bug Fixes

  * Add hashes to requirements.txt ([#1544](https://github.com/googleapis/nodejs-pubsub/issues/1544)) ([#1614](https://github.com/googleapis/nodejs-pubsub/issues/1614)) ([359d098](https://github.com/googleapis/nodejs-pubsub/commit/359d098b60422b37230024128ed10f04018670a0))
  * Allow passing gax instance to client constructor ([#1617](https://github.com/googleapis/nodejs-pubsub/issues/1617)) ([8eabe38](https://github.com/googleapis/nodejs-pubsub/commit/8eabe3802bbc50309f3d6a0b9997752ab7f367e1))
  * Better support for fallback mode ([#1610](https://github.com/googleapis/nodejs-pubsub/issues/1610)) ([d9e7311](https://github.com/googleapis/nodejs-pubsub/commit/d9e7311d6f6bb78bb3f06454a7ce3cf02fff314c))
  * Change import long to require ([#1611](https://github.com/googleapis/nodejs-pubsub/issues/1611)) ([5553af2](https://github.com/googleapis/nodejs-pubsub/commit/5553af2684ba87ed361d9d79bf2e2a6d7cd3763c))
  * **deps:** Update dependency protobufjs to v7 ([#1602](https://github.com/googleapis/nodejs-pubsub/issues/1602)) ([6e0ec60](https://github.com/googleapis/nodejs-pubsub/commit/6e0ec60a8f6efc7d8e7b67c431dddd7073895ae6))
  * Do not import the whole google-gax from proto JS ([#1553](https://github.com/googleapis/nodejs-pubsub/issues/1553)) ([#1616](https://github.com/googleapis/nodejs-pubsub/issues/1616)) ([31c7fa2](https://github.com/googleapis/nodejs-pubsub/commit/31c7fa234ca3d0455979065199d0da1599ed216b))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.14](https://github.com/googleapis/java-pubsub/compare/v1.120.13...v1.120.14) (2022-09-10)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-bigquery to v2.15.0 ([#1259](https://github.com/googleapis/java-pubsub/issues/1259)) ([257cb8f](https://github.com/googleapis/java-pubsub/commit/257cb8f1b38a885dc4c8fb473a79fee1f01a2b57))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.10 ([#1258](https://github.com/googleapis/java-pubsub/issues/1258)) ([37e0034](https://github.com/googleapis/java-pubsub/commit/37e0034660855fc327d3843f8aa78bcda03fe158))
  * Update dependency com.google.cloud:google-cloud-core to v2.8.11 ([#1264](https://github.com/googleapis/java-pubsub/issues/1264)) ([a19bc7a](https://github.com/googleapis/java-pubsub/commit/a19bc7a6bd54a9223575c23df1cac7b2583eb61a))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.2 ([#1265](https://github.com/googleapis/java-pubsub/issues/1265)) ([52da9da](https://github.com/googleapis/java-pubsub/commit/52da9dae19399e03af8d20c0c29aa600b7e31ed3))



## August 29, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Go

### Changes for [pubsub/apiv1](https://github.com/googleapis/google-cloud-go/tree/main/pubsub/apiv1)

#### [1.25.1](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.25.0...pubsub/v1.25.1) (2022-08-24)

##### Bug Fixes

  * **pubsub:** up version of cloud.google.com/go ([#6558](https://github.com/googleapis/google-cloud-go/issues/6558)) ([be9dcfb](https://github.com/googleapis/google-cloud-go/commit/be9dcfbdfa5876a548eb3c60337c38e1d282bb88)), refs [#6555](https://github.com/googleapis/google-cloud-go/issues/6555)



#### [1.25.0](https://github.com/googleapis/google-cloud-go/compare/pubsub/v1.24.0...pubsub/v1.25.0) (2022-08-23)

##### Features

  * **pubsub:** support exactly once delivery ([#6506](https://github.com/googleapis/google-cloud-go/issues/6506)) ([74da335](https://github.com/googleapis/google-cloud-go/commit/74da335fea6cd70b27808507f2e58ae53f5f4910))



##### Documentation

  * **pubsub:** typo ([#6453](https://github.com/googleapis/google-cloud-go/issues/6453)) ([34d839e](https://github.com/googleapis/google-cloud-go/commit/34d839ec546633a0fb7f73448337ac8d8c796acd))



### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.13](https://github.com/googleapis/java-pubsub/compare/v1.120.12...v1.120.13) (2022-08-24)

##### Dependencies

  * update dependency com.google.cloud:google-cloud-bigquery to v2.14.7 ([#1254](https://github.com/googleapis/java-pubsub/issues/1254)) ([775c993](https://github.com/googleapis/java-pubsub/commit/775c99353d96bcbc0704626999a7af79cf0e557f))



## August 22, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.12](https://github.com/googleapis/java-pubsub/compare/v1.120.11...v1.120.12) (2022-08-18)

##### Dependencies

  * update dependency com.google.cloud:google-cloud-bigquery to v2.14.4 ([#1242](https://github.com/googleapis/java-pubsub/issues/1242)) ([08cfe80](https://github.com/googleapis/java-pubsub/commit/08cfe805e71831e040f63755acde17ec45c21418))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.14.6 ([#1245](https://github.com/googleapis/java-pubsub/issues/1245)) ([7f933ee](https://github.com/googleapis/java-pubsub/commit/7f933ee35055c608e9f5b72251583060943a79ea))
  * update dependency com.google.cloud:google-cloud-core to v2.8.9 ([#1250](https://github.com/googleapis/java-pubsub/issues/1250)) ([7c8fd41](https://github.com/googleapis/java-pubsub/commit/7c8fd4183523b876983c89d4b7994746b11964c3))
  * update dependency com.google.protobuf:protobuf-java-util to v3.21.5 ([#1243](https://github.com/googleapis/java-pubsub/issues/1243)) ([37eaff8](https://github.com/googleapis/java-pubsub/commit/37eaff859422bb215ace202ffd0adf8a651dadb5))



## August 15, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-pubsub](https://github.com/googleapis/python-pubsub)

#### [2.13.6](https://github.com/googleapis/python-pubsub/compare/v2.13.5...v2.13.6) (2022-08-11)

##### Bug Fixes

  * **deps:** allow protobuf < 5.0.0 ([#762](https://github.com/googleapis/python-pubsub/issues/762)) ([260bd18](https://github.com/googleapis/python-pubsub/commit/260bd183ffe19992be9a1c1d298438c1f44d3fa9))
  * **deps:** require proto-plus >= 1.22.0 ([260bd18](https://github.com/googleapis/python-pubsub/commit/260bd183ffe19992be9a1c1d298438c1f44d3fa9))
  * set stream_ack_deadline to max_duration_per_lease_extension or 60 s, set ack_deadline to min_duration_per_lease_extension or 10 s ([#760](https://github.com/googleapis/python-pubsub/issues/760)) ([4444129](https://github.com/googleapis/python-pubsub/commit/4444129b28a19296752e865b73827b78e99adea5))
  * Update stream_ack_deadline with ack_deadline ([#763](https://github.com/googleapis/python-pubsub/issues/763)) ([e600ad8](https://github.com/googleapis/python-pubsub/commit/e600ad8228930445765ffa0c45500a7779e25817))



#### [2.13.5](https://github.com/googleapis/python-pubsub/compare/v2.13.4...v2.13.5) (2022-08-10)

##### Documentation

  * reorganize sphinx structure ([#751](https://github.com/googleapis/python-pubsub/issues/751)) ([b6de574](https://github.com/googleapis/python-pubsub/commit/b6de57458a1976a068dd229208b9b678a9d3f866))



## August 08, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.9](https://github.com/googleapis/java-pubsub/compare/v1.120.8...v1.120.9) (2022-08-03)

##### Dependencies

  * update dependency com.google.cloud:google-cloud-core to v2.8.7 ([#1227](https://github.com/googleapis/java-pubsub/issues/1227)) ([e967b2c](https://github.com/googleapis/java-pubsub/commit/e967b2c393a601c7e9dfba33ec2f19ef6e9757c1))
  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.1 ([#1226](https://github.com/googleapis/java-pubsub/issues/1226)) ([8fab566](https://github.com/googleapis/java-pubsub/commit/8fab566e2b0ff726bd9a1dff842b11f5c6c9b00b))



#### [1.120.8](https://github.com/googleapis/java-pubsub/compare/v1.120.7...v1.120.8) (2022-08-02)

##### Dependencies

  * update dependency com.google.cloud:google-cloud-core to v2.8.6 ([#1222](https://github.com/googleapis/java-pubsub/issues/1222)) ([55eebf5](https://github.com/googleapis/java-pubsub/commit/55eebf55785a700a67dc3a97b21837acf14d9a64))



#### [1.120.7](https://github.com/googleapis/java-pubsub/compare/v1.120.6...v1.120.7) (2022-08-01)

##### Bug Fixes

  * Updated log level from WARNING -> INFO for EOD failures ([#1218](https://github.com/googleapis/java-pubsub/issues/1218)) ([8782533](https://github.com/googleapis/java-pubsub/commit/8782533204fcc312c1063763f5073db83c72382f))



#### [1.120.6](https://github.com/googleapis/java-pubsub/compare/v1.120.5...v1.120.6) (2022-08-01)

##### Dependencies

  * update dependency com.google.cloud:google-cloud-bigquery to v2.14.1 ([#1215](https://github.com/googleapis/java-pubsub/issues/1215)) ([5667492](https://github.com/googleapis/java-pubsub/commit/56674928f2e671487c8d4c0dad4e45368da47e0e))
  * update dependency com.google.cloud:google-cloud-core to v2.8.5 ([#1213](https://github.com/googleapis/java-pubsub/issues/1213)) ([5db0c2c](https://github.com/googleapis/java-pubsub/commit/5db0c2cafcf27a80ac4e18c623fc22c2af252774))
  * update dependency com.google.protobuf:protobuf-java-util to v3.21.4 ([#1214](https://github.com/googleapis/java-pubsub/issues/1214)) ([bfc53d9](https://github.com/googleapis/java-pubsub/commit/bfc53d9fb616b4ee22e2c39dbaf1eed7354142a7))
  * update dependency org.apache.avro:avro to v1.11.1 ([#1210](https://github.com/googleapis/java-pubsub/issues/1210)) ([fafcded](https://github.com/googleapis/java-pubsub/commit/fafcdede6b4e5ef5098b8b04a53d9e42b59cda3d))



#### [1.120.11](https://github.com/googleapis/java-pubsub/compare/v1.120.10...v1.120.11) (2022-08-06)

##### Bug Fixes

  * fix dependency declaration to properly include runtime scope ([#1238](https://github.com/googleapis/java-pubsub/issues/1238)) ([e9a4ce5](https://github.com/googleapis/java-pubsub/commit/e9a4ce59fdf3773fa41698579984af525a277f38))



##### Dependencies

  * update dependency com.google.cloud:google-cloud-bigquery to v2.14.2 ([#1235](https://github.com/googleapis/java-pubsub/issues/1235)) ([e2af6c3](https://github.com/googleapis/java-pubsub/commit/e2af6c358ef9e7a0d35179bc4a7c793bbc6a0960))
  * update dependency com.google.cloud:google-cloud-bigquery to v2.14.3 ([#1236](https://github.com/googleapis/java-pubsub/issues/1236)) ([399e8d7](https://github.com/googleapis/java-pubsub/commit/399e8d71d5b4aed2fa48e8cba2dce963d25693e3))



#### [1.120.10](https://github.com/googleapis/java-pubsub/compare/v1.120.9...v1.120.10) (2022-08-04)

##### Dependencies

  * update dependency com.google.cloud:google-cloud-core to v2.8.8 ([#1231](https://github.com/googleapis/java-pubsub/issues/1231)) ([9d13dd8](https://github.com/googleapis/java-pubsub/commit/9d13dd8bc43e24815884dde421409136958d4b0f))



## August 01, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-pubsub](https://github.com/googleapis/java-pubsub)

#### [1.120.5](https://github.com/googleapis/java-pubsub/compare/v1.120.4...v1.120.5) (2022-07-30)

##### Dependencies

  * update dependency com.google.cloud:google-cloud-shared-dependencies to v3 ([#1207](https://github.com/googleapis/java-pubsub/issues/1207)) ([d355509](https://github.com/googleapis/java-pubsub/commit/d355509be963b7d2c357d2c9dd3f97eaa5fd8717))



#### [1.120.4](https://github.com/googleapis/java-pubsub/compare/v1.120.3...v1.120.4) (2022-07-29)

##### Bug Fixes

  * updating return types of ack/nack futures to be consistent with publish ([#1204](https://github.com/googleapis/java-pubsub/issues/1204)) ([6e73ab9](https://github.com/googleapis/java-pubsub/commit/6e73ab9618f61ee1915e52abe3b80e356bc3c13f))



#### [1.120.3](https://github.com/googleapis/java-pubsub/compare/v1.120.2...v1.120.3) (2022-07-27)

##### Dependencies

  * update dependency org.junit.vintage:junit-vintage-engine to v5.9.0 ([#1201](https://github.com/googleapis/java-pubsub/issues/1201)) ([f18e562](https://github.com/googleapis/java-pubsub/commit/f18e5628f54b0ae6858cd046a11824a1698c50c6))



#### [1.120.2](https://github.com/googleapis/java-pubsub/compare/v1.120.1...v1.120.2) (2022-07-25)

##### Bug Fixes

  * enable longpaths support for windows test (#1485) ([#1191](https://github.com/googleapis/java-pubsub/issues/1191)) ([c4b8d90](https://github.com/googleapis/java-pubsub/commit/c4b8d90a158a3360d626df8ca6378212e09f5a47))
  * PubSubMessage leak on MessageDispatcher ([#1197](https://github.com/googleapis/java-pubsub/issues/1197)) ([1b8c440](https://github.com/googleapis/java-pubsub/commit/1b8c440fccc51dc2291c43b2972b1f5c08dfd65a))



##### Dependencies

  * update dependency org.graalvm.buildtools:junit-platform-native to v0.9.13 ([#1189](https://github.com/googleapis/java-pubsub/issues/1189)) ([0d96f8e](https://github.com/googleapis/java-pubsub/commit/0d96f8e2006c145de039d2f00c5eb1d8830eae3d))
  * update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.13 ([#1190](https://github.com/googleapis/java-pubsub/issues/1190)) ([c604080](https://github.com/googleapis/java-pubsub/commit/c6040802bcf97d063e2b91cdb5fa7fe3c3e3b807))



## July 25, 2022

Feature

You can now create [BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/bigquery) in Pub/Sub to write messages directly to an existing BigQuery table. The change is being rolled out in a phased manner over the rest of the week.

## June 07, 2022

Feature

Pub/Sub is now available in `us-south1` (Dallas, Texas).

Deprecated

The following Pub/Sub metrics are deprecated and will be discontinued in 12 months.

  * subscription/streaming_pull_message_operation_count
  * subscription/streaming_pull_ack_message_operation_count
  * subscription/streaming_pull_mod_ack_deadline_message_operation_count
  * subscription/pull_message_operation_count
  * subscription/pull_ack_message_operation_count
  * subscription/mod_ack_deadline_message_operation_count
  * topic/send_message_operation_count



## May 31, 2022

Feature

The Pub/Sub Java client library now supports [gRPC compression](https://docs.cloud.google.com/pubsub/docs/publisher#compressing) to save networking costs before your publisher client sends out the publish request.

## May 24, 2022

Feature

Pub/Sub is now available in `us-east5` (Columbus, Ohio).

## May 10, 2022

Feature

Pub/Sub is now available in `europe-southwest1` (Madrid) .

## May 03, 2022

Feature

Pub/Sub is now available in `europe-west9` (Paris).

## April 20, 2022

Feature

Pub/Sub is now available in `europe-west8` (Milan).

## March 07, 2022

Feature

Exactly once delivery gives you the ability to receive any successfully published message exactly once.

For more information, see [Exactly once delivery](https://docs.cloud.google.com/pubsub/docs/exactly-once-delivery).

## December 08, 2021

Feature

Extended topic retention allows you to retain published messages for a maximum of 31 days.

For more information, see [Topic message retention](https://docs.cloud.google.com/pubsub/docs/replay-overview#topic_message_retention).

## November 16, 2021

Feature

Pub/Sub is now available in `southamerica-west1` (Santiago).

## August 03, 2021

Feature

Pub/Sub Lite is now available in `northamerica-northeast2` (Toronto).

## July 27, 2021

Feature

[Pub/Sub push subscriptions](https://docs.cloud.google.com/pubsub/docs/push#push_subscription_and) created with Cloud Run service endpoints and protected by VPC Service Controls is now available in the GA launch stage.

## July 19, 2021

Feature

The [Pub/Sub Lite Python client library](https://github.com/googleapis/python-pubsublite) is now GA.

## July 08, 2021

Feature

The [Pub/Sub Lite Go client library](https://pkg.go.dev/cloud.google.com/go/pubsublite) is now GA.

## June 30, 2021

Feature

Pub/Sub [message schemas](https://docs.cloud.google.com/pubsub/docs/schemas) are now GA.

## May 04, 2021

Feature

Pub/Sub Lite is now available in the following regions:

  * Hong Kong (`asia-east2`)
  * Tokyo (`asia-northeast1`)
  * Osaka (`asia-northeast2`)
  * Seoul (`asia-northeast3`)
  * Mumbai (`asia-south1`)
  * Jakarta (`asia-southeast2`)
  * Warsaw (`europe-central2`)
  * Montreal (`northamerica-northeast1`)
  * Sao Paulo (`southamerica-east1`)
  * Northern Virginia (`us-east4`)
  * Salt Lake City (`us-west3`)
  * Las Vegas (`us-west4`)



For the full list of available regions, see [Pub/Sub Lite locations](https://docs.cloud.google.com/pubsub/lite/docs/locations).

## March 24, 2021

Feature

Pub/Sub is now available in the `europe-central2` region (Warsaw).

## March 22, 2021

Feature

Pub/Sub Lite now supports [increasing the number of partitions in a topic](https://docs.cloud.google.com/pubsub/lite/docs/topics#scaling_throughput_capacity).

## March 10, 2021

Feature

Pub/Sub push subscriptions can now be created with Cloud Run service endpoints protected by [VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls). This feature is available in the [Preview launch stage](https://cloud.google.com/products/#product-launch-stages).

## March 01, 2021

Feature

Pub/Sub [message schemas](https://docs.cloud.google.com/pubsub/docs/schemas) are now available in the [Preview launch stage](https://cloud.google.com/products/#product-launch-stages).

## February 24, 2021

Feature

An [Apache Spark connector](https://github.com/googleapis/java-pubsublite-spark) is now available for Pub/Sub Lite, allowing you to read messages from Pub/Sub Lite in your Spark clusters.

## November 19, 2020

Feature

The Pub/Sub Lite [Python client library](https://github.com/googleapis/python-pubsublite) is now in Beta.

## November 18, 2020

Feature

Pub/Sub [message filtering](https://docs.cloud.google.com/pubsub/docs/filtering) is now available in GA.

## October 30, 2020

Feature

A [Kafka Shim Java client library](https://github.com/googleapis/java-pubsublite-kafka) is now available for Pub/Sub Lite, allowing you to use the Kafka API while using Pub/Sub Lite as a backend.

## October 19, 2020

Feature

Pub/Sub [message ordering](https://docs.cloud.google.com/pubsub/docs/ordering) is now available in GA.

## October 09, 2020

Feature

[Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) is now available in GA.

## August 28, 2020

Feature

Pub/Sub [subscription detachment](https://docs.cloud.google.com/pubsub/docs/admin#detaching_subscriptions) is now generally available.

## August 05, 2020

Feature

Pub/Sub [message ordering](https://docs.cloud.google.com/pubsub/docs/ordering) is now available at the [beta launch stage](https://cloud.google.com/products/#product-launch-stages).

## June 16, 2020

Feature

[Retry policies for Pub/Sub subscriptions](https://docs.cloud.google.com/pubsub/docs/admin#creating_subscriptions) are now available at the GA launch stage.

## June 08, 2020

Feature

Pub/Sub is now available in the `asia-southeast2` region (Jakarta).

Feature

Pub/Sub [message filtering](https://docs.cloud.google.com/pubsub/docs/filtering) is now available at the [beta launch stage](https://cloud.google.com/products/#product-launch-stages).

## May 26, 2020

Feature

[Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite) is now available at the [beta launch stage](https://cloud.google.com/products/#product-launch-stages).

## May 18, 2020

Feature

The Pub/Sub Lite [Java client library](https://github.com/googleapis/java-pubsublite) is now in Beta.

## April 20, 2020

Feature

Pub/Sub is now available in the `us-west4` region (Las Vegas).

Feature

[Dead-letter topics](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics) for Pub/Sub are now available at the [General Availability release level](https://cloud.google.com/products/#product-launch-stages).

## February 24, 2020

Feature

Cloud Pub/Sub is now available in the `us-west3` region (Salt Lake City).

## January 24, 2020

Feature

Cloud Pub/Sub is now available in the `asia-northeast3` region (Seoul).

## December 12, 2019

Change

[Push subscriptions](https://docs.cloud.google.com/pubsub/docs/push) can now send HTTP POST requests to webhook URLs without proof of domain ownership.

## September 23, 2019

Feature

[Resource location restrictions](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) are available for Cloud Pub/Sub at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels). This feature allows you to manage the location in which your topics' messages are stored.

## September 05, 2019

Feature

[Custom-managed encryption keys (CMEK)](https://docs.cloud.google.com/pubsub/docs/cmek) are available at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels).

## August 29, 2019

Feature

The [Cloud Pub/Sub Python client library](https://github.com/googleapis/python-pubsub/tree/master) is available at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels).

## July 17, 2019

Feature

[Authentication for push subscriptions](https://docs.cloud.google.com/pubsub/docs/push#setting_up_for_push_authentication) is available at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels).

Feature

[Resource location restrictions](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) are available for Cloud Pub/Sub at the [beta release level](https://docs.cloud.google.com/sdk/gcloud#release_levels). This feature allows you to manage the location in which your topics' messages are stored.

## June 26, 2019

Feature

[Custom-managed encryption keys (CMEK)](https://docs.cloud.google.com/pubsub/docs/cmek) are in the process of being rolled out at the [beta release level](https://docs.cloud.google.com/sdk/gcloud#release_levels). This feature will be fully available to Cloud Pub/Sub users as of June 28, 2019.

## May 16, 2019

Feature

The ability to [modify subscription expiration policies](https://docs.cloud.google.com/pubsub/docs/admin#modifying_subscription_expiration_policies) is now available at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels).

## April 15, 2019

Feature

Cloud Pub/Sub is now available in the `asia-northeast2` region (Osaka, Japan).

## April 09, 2019

Feature

[Authentication for push subscriptions](https://docs.cloud.google.com/pubsub/docs/push#setting_up_for_push_authentication) is available at the [beta release level](https://docs.cloud.google.com/sdk/gcloud#release_levels).

## March 20, 2019

Feature

[New pricing](https://cloud.google.com/pubsub/pricing) has been announced. The announcement includes a lower base price for in-region users and new region egress fees.

## March 11, 2019

Feature

Cloud Pub/Sub is now available in the `europe-west6` region (Zürich, Switzerland).

## February 05, 2019

Feature

[Seek](https://docs.cloud.google.com/pubsub/docs/replay-overview) for Cloud Pub/Sub is available at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels) and is recommended for production loads. The Seek feature extends subscriber functionality by allowing you to to alter the acknowledgement state of messages in bulk. For example, you can replay previously acknowledged messages or discard obsolete messages.

## October 29, 2018

Feature

[Seek](https://docs.cloud.google.com/pubsub/docs/replay-overview) for Cloud Pub/Sub is available at the [beta release level](https://docs.cloud.google.com/sdk/gcloud#release_levels).

## October 22, 2018

Feature

Cloud Pub/Sub is now available in the `asia-east2` region (Hong Kong).

## September 19, 2018

Feature

[Labels](https://docs.cloud.google.com/pubsub/docs/labels) for Cloud Pub/Sub are available at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels) and are recommended for production loads.

## July 31, 2018

Feature

[Labels](https://docs.cloud.google.com/pubsub/docs/labels) for Cloud Pub/Sub are available at the [beta release level](https://docs.cloud.google.com/sdk/gcloud#release_levels).

## July 10, 2018

Feature

Cloud Pub/Sub is now available in the `us-west2` region (Los Angeles).

## June 11, 2018

Feature

Cloud Pub/Sub is now available in the `europe-north1` region (Finland).

## May 31, 2018

Feature

The C#, GO, and Java [client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries) are now at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels) and are recommended for production loads.

## May 23, 2018

Feature

[Audit Logging](https://docs.cloud.google.com/pubsub/docs/audit-logging) for Cloud Pub/Sub is now at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels) and is recommended for production loads.

## April 20, 2018

Feature

The gRPC service APIs, including StreamingPull, are now available at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels) and are recommended for production loads. Note that the [Cloud Client Libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries) for Cloud Pub/Sub already use these APIs.

## February 20, 2018

Feature

Added support for [generating Google Cloud Audit logs](https://docs.cloud.google.com/pubsub/docs/audit-logging) that enable you to track usage and access.

## January 24, 2018

Feature

The Cloud Pub/Sub `gcloud` commands are now at the [General Availability release level](https://docs.cloud.google.com/sdk/gcloud#release_levels). The `beta` label is no longer required.

## January 10, 2018

Feature

Cloud Pub/Sub is now available in the `europe-west4` region (Netherlands).

Feature

Cloud Pub/Sub is now available in the `northamerica-northeast1` region (Montréal).

## August 30, 2017

Feature

The [StreamingPull API](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1) is now in Beta. Users of client libraries should see improvements in end-to-end message latency and CPU utilization without any changes in code after updating to the most recent version of the client library.

## August 01, 2017

Feature

Cloud Pub/Sub is now available in the `europe-west3` region (Frankfurt).

## June 20, 2017

Feature

Cloud Pub/Sub is now available in the `australia-southeast1` region (Sydney).

## June 06, 2017

Feature

Cloud Pub/Sub is now available in the `europe-west2` region (London).

## April 19, 2017

Feature

Announced beta availability of [gRPC](https://docs.cloud.google.com/pubsub/docs/reference/rpc).

## January 20, 2017

Change

Published changes to the Cloud Pub/Sub [pricing model](https://cloud.google.com/pubsub/pricing).

## December 01, 2015

Feature

Support added for quota metrics per topic and subscription (`pubsub.googleapis.com/topic/byte_cost` and `pubsub.googleapis.com/subscription/byte_cost`, respectively).

## November 01, 2015

Feature

Added publish timestamp field on pulled messages.

## June 01, 2015

Feature

**Stable API suitable for production development** \- v1 released.

## February 01, 2015

Feature

**Beta release** \- v1beta2 released.

## November 01, 2014

Feature

**Batch request support added** \- Support added for batch Publish and Pull requests.

## June 01, 2014

Feature

**Initial release** \- v1beta1 released.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
