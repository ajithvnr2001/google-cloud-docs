---
url: https://docs.cloud.google.com/bigtable/docs/release-notes/
title: Bigtable release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:17.243392+00:00
---

# Bigtable release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Resources ](https://docs.cloud.google.com/bigtable/docs/resources)



Send feedback 

#  Bigtable release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Bigtable. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. Note: To view release notes for the Bigtable HBase client for Java, see the client library's [GitHub releases page](https://github.com/googleapis/java-bigtable-hbase/releases). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/bigtable-release-notes.xml) directly. 

## October 01, 2026

Feature

You can use [Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview) to browse Bigtable instances and tables, design schemas, and run GoogleSQL queries from your IDE or coding agent. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Data Agent Kit is now GA: Bring Google Data Cloud to any coding agent](https://cloud.google.com/blog/topics/developers-practitioners/data-agent-kit-is-now-ga-bring-google-data-cloud-to-any-coding-agent).

## September 22, 2026

Feature

You can use the Google Cloud console to create and manage protobuf schemas (schema bundles) for your Bigtable tables. You can also view schema bundle definitions in Bigtable Studio. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create and manage protobuf schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas).

## September 14, 2026

Feature

You can use the Google Cloud console to create, list, and query [parameterized views](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview) for your Bigtable instances. You can also configure view parameters and run queries in Bigtable Studio. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create and manage parameterized views](https://docs.cloud.google.com/bigtable/docs/create-manage-parameterized-views).

## September 01, 2026

Feature

You can use the Google Cloud console to create and manage [aggregate column families](https://docs.cloud.google.com/bigtable/docs/aggregates) for your Bigtable tables. You can also view and query aggregate column families in Bigtable Studio. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables#add-column-families) and [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).

## August 20, 2026

Feature

You can use the `allow_incomplete_view` query hint in SQL queries to read data from a continuous materialized view before its initial population finishes. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Read data during initial population](https://docs.cloud.google.com/bigtable/docs/reads#read-during-initial-population).

## August 12, 2026

Feature

You can use parameterized views in Bigtable to dynamically filter data ranges for logical views based on application context and mitigate SQL injection risks. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Parameterized views overview](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview).

Feature

You can use the `CLUSTER_ATTRIBUTE()` filter to restrict continuous materialized view processing to specific clusters. This function lets you isolate views within an instance. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Non-deterministic SQL functions](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views#non-deterministic-functions).

## August 10, 2026

Libraries

### Go

#### [1.52.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.51.0...bigtable/v1.52.0) (2026-08-03)

##### Features

  * **bigtable:** Add AFE picker (Simple / LeastInFlight / LeastLatency) ([#20204](https://github.com/googleapis/google-cloud-go/issues/20204)) ([bcbf714](https://github.com/googleapis/google-cloud-go/commit/bcbf71431d1742e2e13a13d1cbe8b0fc0433aede))
  * **bigtable:** Add ClientConfig.DisableSession to opt out of session backend ([#20297](https://github.com/googleapis/google-cloud-go/issues/20297)) ([7ee5e44](https://github.com/googleapis/google-cloud-go/commit/7ee5e44e0304c5509b9b77fe0760d97771657cd9))
  * **bigtable:** Add getClientConfigDirectAccessChecker for session pools ([#20209](https://github.com/googleapis/google-cloud-go/issues/20209)) ([3b8d30a](https://github.com/googleapis/google-cloud-go/commit/3b8d30adeaf03c8452207b056d69922646d63bf2))
  * **bigtable:** Add NoOpChannelPrimer for session channel pools ([#20208](https://github.com/googleapis/google-cloud-go/issues/20208)) ([d055a8a](https://github.com/googleapis/google-cloud-go/commit/d055a8a1b23980ad4b53c0cd690e291c9aa6248c))
  * **bigtable:** Add per-AFE sessionList for the two-tier session pool ([#20224](https://github.com/googleapis/google-cloud-go/issues/20224)) ([dbf0c3f](https://github.com/googleapis/google-cloud-go/commit/dbf0c3f3ea37279a2aa00803ded8e489229b15c9))
  * **bigtable:** Add protoRowToRow conversion helper for TableShim ([#20257](https://github.com/googleapis/google-cloud-go/issues/20257)) ([1297143](https://github.com/googleapis/google-cloud-go/commit/1297143a4fab4bf58cbd0bd6e44db4653a818c47))
  * **bigtable:** Add Session debug surface (observability fields + methods) ([#20211](https://github.com/googleapis/google-cloud-go/issues/20211)) ([d8d3e16](https://github.com/googleapis/google-cloud-go/commit/d8d3e160c3e63150ef5d14e83a2ea0fd25a7e214))
  * **bigtable:** Add Session lifecycle (Start, Close, ForceClose, readLoop, heartBeatLoop) ([#20215](https://github.com/googleapis/google-cloud-go/issues/20215)) ([b9e53c6](https://github.com/googleapis/google-cloud-go/commit/b9e53c6276efe28428adfcd4671d7ac8c7e8d330))
  * **bigtable:** Add Session struct + state machine ([#20117](https://github.com/googleapis/google-cloud-go/issues/20117)) ([09acbb3](https://github.com/googleapis/google-cloud-go/commit/09acbb37a385d2c6fca465adb70a3eb03ea4a38e))
  * **bigtable:** Add session.Config.EnableDebug to gate sessionz debug state ([#20247](https://github.com/googleapis/google-cloud-go/issues/20247)) ([ce74c31](https://github.com/googleapis/google-cloud-go/commit/ce74c315d41371b0ddf2c1ba7342446695a53900))
  * **bigtable:** Add SessionClient + SessionTable + lazyPool ([#20228](https://github.com/googleapis/google-cloud-go/issues/20228)) ([ab2c96c](https://github.com/googleapis/google-cloud-go/commit/ab2c96c3ed62514dcf6526bb32259267fbe63e97))
  * **bigtable:** Add SessionPoolImpl (two-tier pool + scaling + debug) ([#20225](https://github.com/googleapis/google-cloud-go/issues/20225)) ([683eda8](https://github.com/googleapis/google-cloud-go/commit/683eda8c690fd2b948bd3b56777039d28421ee7c))
  * **bigtable:** Rename session pool display to <resource-id>-<PERM> ([#20248](https://github.com/googleapis/google-cloud-go/issues/20248)) ([35e146e](https://github.com/googleapis/google-cloud-go/commit/35e146e25d2897082f2d1b78b9273087efd855fd))
  * **bigtable:** Route Client.Open()-returned *Table through the Diverter ([#20273](https://github.com/googleapis/google-cloud-go/issues/20273)) ([2b81c7d](https://github.com/googleapis/google-cloud-go/commit/2b81c7dc2d73739f4d5f87aa43cc9a3ac031822d))
  * **bigtable:** State-based classification for abnormal session close ([#20243](https://github.com/googleapis/google-cloud-go/issues/20243)) ([f2905b7](https://github.com/googleapis/google-cloud-go/commit/f2905b793d062ae597d9c39597d15a680e9e9967))
  * **bigtable:** TableShim fallback to classic on session UNIMPLEMENTED ([#20269](https://github.com/googleapis/google-cloud-go/issues/20269)) ([36540af](https://github.com/googleapis/google-cloud-go/commit/36540af84ab5f7360c5c1a92bbfb5a631d4c5cc6))
  * **bigtable:** TTL-on-idle cache for per-resource session.TableAPI ([#20263](https://github.com/googleapis/google-cloud-go/issues/20263)) ([00b2a49](https://github.com/googleapis/google-cloud-go/commit/00b2a49de38fe600736cf10c496f85e082ae8871))
  * **bigtable:** Wire Diverter on Client and route Open* via TableShim ([#20256](https://github.com/googleapis/google-cloud-go/issues/20256)) ([b32fbd7](https://github.com/googleapis/google-cloud-go/commit/b32fbd7d02f835e8f83b4be1926e5826c27fa8a9))



##### Bug Fixes

  * **bigtable:** AFE picker latency signal — subtract poolWait and compute TransportLatency = wire − backend at source ([#20281](https://github.com/googleapis/google-cloud-go/issues/20281)) ([bb8c4d5](https://github.com/googleapis/google-cloud-go/commit/bb8c4d56bf5bb53e5e1f1d510be326821fe4ddee))
  * **bigtable:** Guard NewStream OnFinish against grpc-go double-fire ([#20295](https://github.com/googleapis/google-cloud-go/issues/20295)) ([b51da29](https://github.com/googleapis/google-cloud-go/commit/b51da29536de5aa59582d2a9633a07186f8636ae))
  * **bigtable:** Real per-resource pool teardown on sessionTable.Close + cache close-race gate ([#20264](https://github.com/googleapis/google-cloud-go/issues/20264)) ([599aea9](https://github.com/googleapis/google-cloud-go/commit/599aea9e67ca2526b7822eb1e873e3aaf7b5124e))
  * **bigtable:** Session.durations / session.uptime — set explicit histogram bucket boundaries ([#20276](https://github.com/googleapis/google-cloud-go/issues/20276)) ([97eee22](https://github.com/googleapis/google-cloud-go/commit/97eee225c412db9288bb7813e6b9cc856e6aba44))
  * **bigtable:** SessionTableHandle self-heals across cache eviction ([#20296](https://github.com/googleapis/google-cloud-go/issues/20296)) ([0dd98cd](https://github.com/googleapis/google-cloud-go/commit/0dd98cd75383bd5902f3bec936d9ae68c64e6682))
  * **bigtable:** Translate ctx errors to gRPC status on session vRPC ([#20299](https://github.com/googleapis/google-cloud-go/issues/20299)) ([0f3b2a5](https://github.com/googleapis/google-cloud-go/commit/0f3b2a519e07eccdfacad1129aa0fb69bc8f06e6))
  * **bigtable:** Treat PingAndWarm NotFound as a successful prime ([#20219](https://github.com/googleapis/google-cloud-go/issues/20219)) ([a1557ad](https://github.com/googleapis/google-cloud-go/commit/a1557adec2fc8a579f70cdb4de5f959ceb8d51a1))



##### Performance Improvements

  * **bigtable:** Delete periodic Tick loop; sizing is event-driven ([#20285](https://github.com/googleapis/google-cloud-go/issues/20285)) ([2c096bd](https://github.com/googleapis/google-cloud-go/commit/2c096bddf6fc5353a3804d222b3683a55eda13e5))
  * **bigtable:** Drop pick_lost_race debug tag from CheckoutSession hot path ([#20280](https://github.com/googleapis/google-cloud-go/issues/20280)) ([bd0e400](https://github.com/googleapis/google-cloud-go/commit/bd0e400948a15639546f150d5d2b1a1a7ceb5741))



## July 30, 2026

Feature

You can use Bigtable as a remote storage backend for [LMCache](https://docs.lmcache.ai/kv_cache/storage_backends/bigtable.html). By storing the large language model (LLM) key-value (KV) cache externally in Bigtable, multiple AI serving instances can share and reuse precomputed attention tensors. This reduces compute overhead and significantly improves time-to-first-token (TTFT) for repeated prompts and shared documents. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 29, 2026

Feature

You can use the Google Cloud console to [manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas) for your Bigtable tables. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 27, 2026

Feature

The Bigtable remote MCP server supports the Bigtable Data API, which provides the `execute_sql` tool that you can use to query Bigtable data using natural language prompts. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Use the Bigtable remote MCP server](https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp).

Libraries

### Go

#### [1.51.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.50.0...bigtable/v1.51.0) (2026-07-23)

##### Features

  * **bigtable:** Add ChainInterceptors and RetryingVRpc for vRPC pipeline ([#20185](https://github.com/googleapis/google-cloud-go/issues/20185)) ([c7a832a](https://github.com/googleapis/google-cloud-go/commit/c7a832aa13bad0896c3906f491d798482dd8c02a))
  * **bigtable:** Add ClientConfigurationManager ([#19986](https://github.com/googleapis/google-cloud-go/issues/19986)) ([3a8f927](https://github.com/googleapis/google-cloud-go/commit/3a8f9270d9c2831b5d76efe89c913555577ace6a))
  * **bigtable:** Add debug tag counter (recordDebugTag / assertDebugTag) ([#20114](https://github.com/googleapis/google-cloud-go/issues/20114)) ([3c97590](https://github.com/googleapis/google-cloud-go/commit/3c97590192a19306612389e9d55b93b538e8584b))
  * **bigtable:** Add lazyPool helper for on-demand session pool opening ([#20182](https://github.com/googleapis/google-cloud-go/issues/20182)) ([f6ae3fb](https://github.com/googleapis/google-cloud-go/commit/f6ae3fbf65e9e41a1c2d64f281f881ebe8828439))
  * **bigtable:** Add PeakEwma continuous time-decay latency tracker ([#20187](https://github.com/googleapis/google-cloud-go/issues/20187)) ([9d124ef](https://github.com/googleapis/google-cloud-go/commit/9d124ef7773dae916dfbb97657f83ae633d15220))
  * **bigtable:** Add PoolSizer for server-driven session pool capacity ([#20189](https://github.com/googleapis/google-cloud-go/issues/20189)) ([57ebbeb](https://github.com/googleapis/google-cloud-go/commit/57ebbeb8e846f574034e93060682309bc1a00dc1))
  * **bigtable:** Add session package with SessionClient + SessionTableAPI interfaces ([#20180](https://github.com/googleapis/google-cloud-go/issues/20180)) ([4b82fd2](https://github.com/googleapis/google-cloud-go/commit/4b82fd25cc81cdee5563d5a049b48d2694bca088))
  * **bigtable:** Add Session primitives (AttemptOutcome, vRPC ctx, msgtype) ([#20116](https://github.com/googleapis/google-cloud-go/issues/20116)) ([e1011e2](https://github.com/googleapis/google-cloud-go/commit/e1011e2d2c43a838abe080ad9d3f614f8c92e55a))
  * **bigtable:** Add Session state enum ([#19981](https://github.com/googleapis/google-cloud-go/issues/19981)) ([0748972](https://github.com/googleapis/google-cloud-go/commit/07489725b63174375f7faa68b7aad18cc638c27b))
  * **bigtable:** Add SessionThrottler / AdaptiveSessionThrottler for OpenSession pacing ([#20184](https://github.com/googleapis/google-cloud-go/issues/20184)) ([02e3c6d](https://github.com/googleapis/google-cloud-go/commit/02e3c6d19e8ff5b6a12803bc9b0636575e070dff))
  * **bigtable:** Add SessionThrottler / AdaptiveSessionThrottler for OpenSession pacing ([#20184](https://github.com/googleapis/google-cloud-go/issues/20184)) ([29be83e](https://github.com/googleapis/google-cloud-go/commit/29be83ed3b631a472e28be4d8569d34f0a071d86))
  * **bigtable:** Add sessionTracer for per-Session lifecycle + vRPC metrics ([#20190](https://github.com/googleapis/google-cloud-go/issues/20190)) ([a466345](https://github.com/googleapis/google-cloud-go/commit/a4663459260ba054af918c29a94570d5ec69f399))
  * **bigtable:** Enable new auth library and JWT for instance admin client ([#20013](https://github.com/googleapis/google-cloud-go/issues/20013)) ([21c4a44](https://github.com/googleapis/google-cloud-go/commit/21c4a448adf789e8acaebfaed7df5c49ac434aab))
  * **bigtable:** Modularize channel priming behind a ChannelPrimer interface ([#20027](https://github.com/googleapis/google-cloud-go/issues/20027)) ([5214ab7](https://github.com/googleapis/google-cloud-go/commit/5214ab7033bd8a5aa672878ae17ce828d5d78c3c))
  * **bigtable:** Modularize Direct Access compatibility check ([#19987](https://github.com/googleapis/google-cloud-go/issues/19987)) ([a25e93d](https://github.com/googleapis/google-cloud-go/commit/a25e93d25635b8fd42985edbe0290ba9a8cf2169))
  * **o11y:** Regenerate clients for LRO tracing ([#20107](https://github.com/googleapis/google-cloud-go/issues/20107)) ([779074e](https://github.com/googleapis/google-cloud-go/commit/779074edd267a26520bae459307660953129eb07))



##### Bug Fixes

  * **bigtable:** Default cluster/zone in toOtelMetricAttrs to avoid Monitoring reject ([#20178](https://github.com/googleapis/google-cloud-go/issues/20178)) ([14493f4](https://github.com/googleapis/google-cloud-go/commit/14493f4de7298b8fac36c1ee67f2647fbc2e6ba9))
  * **bigtable:** Eliminate stats-handler MD race in internal/metrics tracer ([#20158](https://github.com/googleapis/google-cloud-go/issues/20158)) ([c387066](https://github.com/googleapis/google-cloud-go/commit/c38706633aa13da88e8c54b0b6340b9ce7209007))



## July 14, 2026

Feature

AI agents can use the [`list_hot_tablets` Model Context Protocol (MCP) tool](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/list_hot_tablets) to programmatically query Bigtable cluster health to isolate resource-intensive tablets (hot tablets) and detect overutilized node CPUs. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## July 09, 2026

Feature

You can use the [Bigtable client library for Go](https://docs.cloud.google.com/bigtable/docs/reference/libraries) to execute read jobs and queries using [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

## July 07, 2026

Feature

You can bind existing [tags](https://docs.cloud.google.com/bigtable/docs/tags) to Bigtable instances when you create an instance and use policies to enforce mandatory tag assignments. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).

Feature

The Bigtable agent skill (`bigtable-basics`) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) in the public [Google Agent Skills repository](https://github.com/google/skills/tree/main/skills/cloud/bigtable-basics). This skill lets you equip AI agents with capabilities for Bigtable tasks, such as provisioning instances and tables, designing schemas, querying data using GoogleSQL and key-value APIs, and diagnosing performance issues or hotspots.

Feature

You can use Organization Policy Service custom constraints to manage specific operations on continuous materialized views. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Use custom organization policies](https://docs.cloud.google.com/bigtable/docs/custom-constraints).

## July 06, 2026

Feature

Bigtable supports direct connectivity, which bypasses the Google frontend and optimizes performance for application traffic that meets certain criteria. For more information, see [Direct connectivity](https://docs.cloud.google.com/bigtable/docs/performance#direct-connectivity).

## June 24, 2026

Feature

You can create [hot backups](https://docs.cloud.google.com/bigtable/docs/backups#hot-backups) and modify all backups in Bigtable Studio. For more information, see [Manage backups](https://docs.cloud.google.com/bigtable/docs/managing-backups).

## June 22, 2026

Libraries

### Go

#### [1.50.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.49.0...bigtable/v1.50.0) (2026-06-17)

##### Features

  * **bigtable:** Enable JWT ([#19957](https://github.com/googleapis/google-cloud-go/issues/19957)) ([af93528](https://github.com/googleapis/google-cloud-go/commit/af93528c6eb18e841783987820b9f586293459e4))
  * **bigtable:** Generate Admin API client using selective gapic ([#19962](https://github.com/googleapis/google-cloud-go/issues/19962)) ([a37509d](https://github.com/googleapis/google-cloud-go/commit/a37509ddadc60a81e5dfb0f373e47d0d578d8cca))
  * **bigtable:** Refactor channel_pool_factory as we need to maintain two channel factory one for session and another for unary ([#14652](https://github.com/googleapis/google-cloud-go/issues/14652)) ([0c0b6ce](https://github.com/googleapis/google-cloud-go/commit/0c0b6ceba693dbe8af778117f6ca10faf0ca67ff))
  * **bigtable:** Wrap admin client ([#14534](https://github.com/googleapis/google-cloud-go/issues/14534)) ([0bea4ba](https://github.com/googleapis/google-cloud-go/commit/0bea4ba37832608dc05293a1eb2a3c756a9f27d9))
  * Update API sources and regenerate ([#19950](https://github.com/googleapis/google-cloud-go/issues/19950)) ([c7607be](https://github.com/googleapis/google-cloud-go/commit/c7607be52757b803df345670b5d0621c2bb9ba30))



## June 19, 2026

Feature

You can use the Bigtable Studio explorer to search for all resources except for authorized views and column families. For more information, see [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).

## June 15, 2026

Libraries

### Go

#### [v1.49.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.48.0...bigtable/v1.49.0) (2026-06-10)

##### Features

  * enable new auth library and remove async refresh (#19943) ([0d3697b2](https://github.com/googleapis/google-cloud-go/commit/0d3697b2))

  * add traffic diverter and table shim for bigtable (#14633) ([2f3c9184](https://github.com/googleapis/google-cloud-go/commit/2f3c9184))

  * add virtual RPC descriptors (#14648) ([5eedda18](https://github.com/googleapis/google-cloud-go/commit/5eedda18))

  * add opensession descriptors for bigtable (#14647) ([8968f4fd](https://github.com/googleapis/google-cloud-go/commit/8968f4fd))

  * update API sources and regenerate (#14701) ([a9b79215](https://github.com/googleapis/google-cloud-go/commit/a9b79215))




##### Bug Fixes

  * retry unexpected EOF errors (#13157) ([2b4ac429](https://github.com/googleapis/google-cloud-go/commit/2b4ac429))

  * disable dynamic channel pool by default and raise default pool size to 10 (#19945) ([5ddf8d46](https://github.com/googleapis/google-cloud-go/commit/5ddf8d46))

  * raise default connection-recycler MaxAge to 7 days (#19940) ([a7959efc](https://github.com/googleapis/google-cloud-go/commit/a7959efc))




## June 01, 2026

Libraries

### Go

#### [v1.48.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.47.0...bigtable/v1.48.0) (2026-05-26)

##### Features

  * expose a client option to disable direct access: (#14626) ([f22b29f5](https://github.com/googleapis/google-cloud-go/commit/f22b29f5))



##### Known Issue: heap growth on long-running clients (DirectAccess Eligible)

Long-running clients using DirectAccess may observe steady heap growth caused by an upstream memory leak in the gRPC-Go xDS client ([#14582](https://github.com/googleapis/google-cloud-go/issues/14582)). The leak is amplified in this release by the default connection recycler, which recycles connections roughly every 45 minutes.

**Workarounds:** \- Disable the connection recycler: ```go cfg := bigtable.ClientConfig{DisableConnectionRecycler: true} client, err := bigtable.NewClientWithConfig(ctx, project, instance, cfg)

  * OR Disable the connpool via env var `CBT_BIGTABLE_CONN_POOL=false`

  * OR upgrade to bigtable/v1.49.0 (or later), which fixes the problem by disabling connection recycler.




## May 28, 2026

Feature

As part of Bigtable Enterprise Plus [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can configure a retention period of up to 365 days for backups. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Bigtable backups overview](https://docs.cloud.google.com/bigtable/docs/backups).

## May 18, 2026

Feature

You can enable [row-affinity routing](https://docs.cloud.google.com/bigtable/docs/routing#row-affinity) for a standard app profile in the Google Cloud console. For more information, see [Create a standard app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#create-standard-app-profile).

## May 07, 2026

Feature

You can use [Aerospike migration tools](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/tree/main/aerospike-bigtable-migration-tools) to migrate data from Aerospike to Bigtable with minimal or zero downtime. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Migrate Aerospike to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-aerospike-to-bigtable).

## May 04, 2026

Libraries

### Go

#### [v1.47.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.46.0...bigtable/v1.47.0) (2026-05-01)

##### Known Issue: heap growth on long-running clients (DirectAccess Eligible)

Long-running clients using DirectAccess may observe steady heap growth caused by an upstream memory leak in the gRPC-Go xDS client ([#14582](https://github.com/googleapis/google-cloud-go/issues/14582)). The leak is amplified in this release by the default connection recycler, which recycles connections roughly every 45 minutes.

**Workarounds:**

  * Disable the connection recycler: ```go cfg := bigtable.ClientConfig{DisableConnectionRecycler: true} client, err := bigtable.NewClientWithConfig(ctx, project, instance, cfg)


  * OR Disable the connpool via env var `CBT_BIGTABLE_CONN_POOL=false`

  * Or upgrade to bigtable/v1.49.0 (or later), which fixes the problem by disabling connection recycler.




## April 30, 2026

Feature

You can use Bigtable [agent skills](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem#ai-agent-skills) to let AI agents assist with Bigtable-related tasks, such as schema design, generating SQL queries, and infrastructure management.

## April 23, 2026

Feature

You can use window functions with GoogleSQL in Bigtable to perform advanced analytic operations over multiple table rows. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Window functions](https://docs.cloud.google.com/bigtable/docs/reference/sql/window-functions).

## April 22, 2026

Feature

The Bigtable editions feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). Bigtable editions introduces advanced features in performance, analytic query capability, and resource management. You can choose between the Enterprise and Enterprise Plus edition to select the right capabilities for your workloads. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

Feature

Bigtable provides an in-memory tier as part of its hybrid storage architecture. This tier provides sub-millisecond read latency and high throughput for time-sensitive data with independent vertical scaling to handle traffic surges. The in-memory tier is available only in the Enterprise Plus [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview) in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [In-memory tier overview](https://docs.cloud.google.com/bigtable/docs/in-memory-overview).

Feature

Bigtable [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) limit increases from 32 TB to 64 TB per node. This expansion provides higher storage density to support retention of larger volumes of infrequently accessed data and is available only in the Enterprise Plus [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview). Tiered storage is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can use [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) to read data from tiered storage and HDD clusters. This feature is available only in the Enterprise Plus edition and is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can use [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) to run GoogleSQL queries. This feature is available only in the Enterprise Plus edition and is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [High-throughput SQL analysis with Data Boost](https://docs.cloud.google.com/bigtable/docs/googlesql-examples#data-boost-analysis).

Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can configure which cluster in a replicated instance is used for automated backups. This feature provides greater cost control and backup resource management. This feature is available only in the Enterprise Plus edition and is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Bigtable backups overview](https://docs.cloud.google.com/bigtable/docs/backups).

## April 20, 2026

Feature

You can use the [Database Insights remote MCP server](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/databaseinsights/mcp) to analyze Bigtable's performance and system metrics. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

Bigtable [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) are [generally available (GA)](https://cloud.google.com/products#product-launch-stages). These views let you create precomputed tables that Bigtable automatically keeps in sync with your source data for low-latency queries and real-time insights.

Feature

Bigtable free trial instances are [generally available (GA)](https://cloud.google.com/products#product-launch-stages). These instances let you learn and explore Bigtable features for 90 days at no cost, providing a 1-node SSD cluster and up to 500 GB of storage. For more information, see [Free trial instances overview](https://docs.cloud.google.com/bigtable/docs/free-trial-instance).

Feature

The [Bigtable remote MCP server](https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). The Bigtable remote MCP server lets you interact with Bigtable instances from LLMs, AI applications, and AI-enabled development platforms.

## April 16, 2026

Feature

You can stream messages from [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/subscription-overview) directly to a Bigtable table using [Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions). This feature lets you write streaming messages to Bigtable without needing a separate subscriber such as Dataflow. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 15, 2026

Feature

Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and Identity and Access Management (IAM) names remain unchanged. For more information about how Bigtable metadata interacts with Knowledge Catalog, see [Manage data assets using Knowledge Catalog](https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-knowledge-catalog).

## April 13, 2026

Feature

You can now use GoogleSQL geography functions to work with geospatial data in Bigtable. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Work with geospatial data](https://docs.cloud.google.com/bigtable/docs/work-with-geo-data) and [Geography functions reference](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions).

Feature

Bigtable supports [pipe syntax](https://docs.cloud.google.com/bigtable/docs/reference/sql/pipe-syntax), an extension to GoogleSQL that lets you build simpler and more concise queries. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Libraries

### Go

#### [v1.46.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.45.0...bigtable/v1.46.0) (2026-04-09)

##### Known Issue: heap growth on long-running clients (DirectAccess Eligible)

Long-running clients using DirectAccess may observe steady heap growth caused by an upstream memory leak in the gRPC-Go xDS client ([#14582](https://github.com/googleapis/google-cloud-go/issues/14582)). The leak is amplified in this release by the default connection recycler, which recycles connections roughly every 45 minutes.

**Workarounds:**

  * Disable the connection recycler: ```go cfg := bigtable.ClientConfig{DisableConnectionRecycler: true} client, err := bigtable.NewClientWithConfig(ctx, project, instance, cfg)


  * OR Disable the connpool via env var `CBT_BIGTABLE_CONN_POOL=false`

  * Or upgrade to bigtable/v1.49.0 (or later), which fixes the problem by disabling connection recycler.




## April 09, 2026

Feature

You can use Gemini in Bigtable Studio to help you write GoogleSQL queries. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Write SQL with Gemini assistance](https://docs.cloud.google.com/bigtable/docs/write-sql-gemini).

## April 07, 2026

Feature

You can connect to Bigtable from Java applications and other reporting tools that support a generic JDBC adapter by using the [Bigtable JDBC driver](https://docs.cloud.google.com/bigtable/docs/reference/jdbc). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

You can use [protocol buffer (protobuf) schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas) to query individual fields within protobuf messages stored as bytes in Bigtable. You can query your protobuf data using GoogleSQL for Bigtable, continuous materialized views, logical views, or BigQuery external tables. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## April 06, 2026

Libraries

### Go

#### [v1.44.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.43.0...bigtable/v1.44.0) (2026-03-30)

### Go

#### [v1.45.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.44.0...bigtable/v1.45.0) (2026-03-31)

## March 30, 2026

Feature

You can view the [details of Bigtable continuous materialized views](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views#view-details) in the Google Cloud console.

## March 25, 2026

Announcement

Bigtable client for Java has modernized its Admin API. For detailed migration steps and code examples, see [Upgrading client libraries](https://docs.cloud.google.com/bigtable/docs/upgrading-clients#java).

## March 24, 2026

Feature

You can manage Bigtable [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) configuration in the Google Cloud console and view tiered storage metrics in [system insights](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring-resources). For more information, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables).

## March 23, 2026

Libraries

### Go

#### [1.43.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.42.0...bigtable/v1.43.0) (2026-03-16)

##### Features

  * Add support for creating Instance with tags (#13459) ([1bce843e](https://github.com/googleapis/google-cloud-go/commit/1bce843e))

  * support tiered storage (#13793) ([39a25b92](https://github.com/googleapis/google-cloud-go/commit/39a25b92))

  * add handling of longupdown metrics aka gauge (#13871) ([519ed9b0](https://github.com/googleapis/google-cloud-go/commit/519ed9b0))

  * Use direct access when supported. Guarded by enabling… (#13873) ([5ea1f5f9](https://github.com/googleapis/google-cloud-go/commit/5ea1f5f9))

  * add preemptive connection recycler (#13860) ([6b69ee38](https://github.com/googleapis/google-cloud-go/commit/6b69ee38))

  * make downscalling less aggressive (#14123) ([7ac72cc8](https://github.com/googleapis/google-cloud-go/commit/7ac72cc8))

  * add pacemaker in connpool (#13862) ([9af047f7](https://github.com/googleapis/google-cloud-go/commit/9af047f7))

  * populate ip protocol for direct access checker and rename a method to be concise (#14011) ([9c5e6551](https://github.com/googleapis/google-cloud-go/commit/9c5e6551))

  * add connection factory to abstract connection (#13755) ([b08ea15f](https://github.com/googleapis/google-cloud-go/commit/b08ea15f))

  * make pow of 2 default lb policy (#14131) ([b5f7bf27](https://github.com/googleapis/google-cloud-go/commit/b5f7bf27))

  * derive conn pool from resolver (#14147) ([b903e299](https://github.com/googleapis/google-cloud-go/commit/b903e299))

  * add load balancing penalty for channel (#14149) ([bb649988](https://github.com/googleapis/google-cloud-go/commit/bb649988))

  * cap increase in conn for dynamic chan pool (#14144) ([e0701a46](https://github.com/googleapis/google-cloud-go/commit/e0701a46))

  * switch to rand v2 (#14008) ([ee6f4251](https://github.com/googleapis/google-cloud-go/commit/ee6f4251))




##### Bug Fixes

  * slighly change instruction for direct access (#14119) ([7dd4948d](https://github.com/googleapis/google-cloud-go/commit/7dd4948d))

  * refactor bigtable.go into separate file path per interfaces (#13818) ([c8ae2e2a](https://github.com/googleapis/google-cloud-go/commit/c8ae2e2a))




## March 06, 2026

Feature

[Bigtable tools in the Agent Development Kit (ADK)](https://google.github.io/adk-docs/integrations/bigtable/) are [generally available (GA)](https://cloud.google.com/products#product-launch-stages). With these tools, you can build AI agents that interact with Bigtable to discover metadata about Bigtable tables and instances and execute LLM-powered SQL queries.

## February 18, 2026

Announcement

New best practices are available for securing generative AI agents using Model Context Protocol (MCP) with Google Cloud databases. This guide covers key security measures like least privilege, native database controls, and secure agent design to help you build safer AI applications. For more information, see [Best practices for securing agent interactions with Model Context Protocol](https://docs.cloud.google.com/bigtable/docs/secure-agent-interactions-mcp).

Feature

You can migrate a machine learning feature management workload from Vertex AI Feature Store (Legacy) to a Bigtable instance. For more information, see [Migrate from Vertex AI Feature Store (Legacy) to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-vertex-ai-legacy-bigtable).

## February 17, 2026

Feature

You can use the [Bigtable Admin API MCP server](https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp) to enable agents and AI applications to perform a range of data-related tasks. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 13, 2026

Breaking

You can use the [Flink Bigtable connector](https://docs.cloud.google.com/bigtable/docs/flink-connector) version 0.3.2 to connect to Bigtable from Apache Flink version 2.1.0. Additionally, this version of the connector lets you specify the number of mutations to include in each batch sent to Bigtable. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## February 09, 2026

Libraries

### Go

#### [1.42.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.41.0...bigtable/v1.42.0) (2026-02-04)

##### Features

  * add TieredStorageConfig to table admin api (PiperOrigin-RevId: 863493708) ([611f2392](https://github.com/googleapis/google-cloud-go/commit/611f2392))

  * add dynamic channel support (#2) (#13504) ([65a3c4ec](https://github.com/googleapis/google-cloud-go/commit/65a3c4ec))

  * add ip protocol for bigtable connection (#13520) ([6f86983e](https://github.com/googleapis/google-cloud-go/commit/6f86983e))

  * add metrics exporter for outstandingrpcs and perconnectionerror count (#13510) ([7f1b36ac](https://github.com/googleapis/google-cloud-go/commit/7f1b36ac))

  * add client startup time metrics. (#13521) ([8f90da38](https://github.com/googleapis/google-cloud-go/commit/8f90da38))

  * introduce prime() method and load counting based on unary,streaming and ability to remove connection (#13419) ([c6773ceb](https://github.com/googleapis/google-cloud-go/commit/c6773ceb))




##### Bug Fixes

  * handle client region and client host name based on ote… (#13752) ([0429170f](https://github.com/googleapis/google-cloud-go/commit/0429170f))

  * fix a nil pointer deference in remove connections when… (#13535) ([9d2ba82e](https://github.com/googleapis/google-cloud-go/commit/9d2ba82e))




##### Performance Improvements

  * use passthrough with emulator endpoint (#13739) ([dafbca22](https://github.com/googleapis/google-cloud-go/commit/dafbca22))



## February 02, 2026

Libraries

### Java

#### [2.72.0](https://github.com/googleapis/java-bigtable/compare/v2.71.0...v2.72.0) (2026-01-30)

##### Features

  * Add GcRuleBuilder for safe GC rule construction ([#2758](https://github.com/googleapis/java-bigtable/issues/2758)) ([4a99a8c](https://github.com/googleapis/java-bigtable/commit/4a99a8ccad8469933b63aa63205bc2c800a24fef))
  * Handle StatusRuntimeException in CbtTestProxy, increase inbound message / metadata size ([#2763](https://github.com/googleapis/java-bigtable/issues/2763)) ([3e27d28](https://github.com/googleapis/java-bigtable/commit/3e27d2895816685743ee59d566cd8870447c02f1))
  * Regenerate protos using protoc 4



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.66.0 ([ca24007](https://github.com/googleapis/java-bigtable/commit/ca240078ea4400cd071d796259ed4b8c9501a6f6))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.56.0 ([#2765](https://github.com/googleapis/java-bigtable/issues/2765)) ([d1020a1](https://github.com/googleapis/java-bigtable/commit/d1020a1ea1e296273408262a33a09427a20d8156))



## January 30, 2026

Feature

Bigtable has a unified, customizable system insights dashboard. This dashboard includes predefined metrics and other Google Cloud metrics. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Customize the system insights dashboard](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#customize-system-insights).

## January 21, 2026

Feature

Bigtable is available in the `asia-southeast3` (Bangkok) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## January 19, 2026

Libraries

### Java

#### [2.71.0](https://github.com/googleapis/java-bigtable/compare/v2.70.1...v2.71.0) (2026-01-15)

##### Features

  * Add CSM for batch write flow control ([#2685](https://github.com/googleapis/java-bigtable/issues/2685)) ([62ffd1b](https://github.com/googleapis/java-bigtable/commit/62ffd1babb910bc9ef2e83482de9500e3e1a1b4f))



##### Bug Fixes

  * **bigtable:** Add handling for gauge metrics ([#2719](https://github.com/googleapis/java-bigtable/issues/2719)) ([87aa4d5](https://github.com/googleapis/java-bigtable/commit/87aa4d54c047d2de1e92d75a4ff69e6d02689bdb))
  * Create stub with BigtableClientContext so otels are closed ([#2747](https://github.com/googleapis/java-bigtable/issues/2747)) ([3d0a6d9](https://github.com/googleapis/java-bigtable/commit/3d0a6d9d52bd8a97adafe04ac7d6142b42139e51))
  * Update BigtableChannelPool to use the background executor ([#2753](https://github.com/googleapis/java-bigtable/issues/2753)) ([8f6e2df](https://github.com/googleapis/java-bigtable/commit/8f6e2df7bba6fee4e3999dd77b8b18cd85580eff))
  * Use the same background executor in otel reader and monitoring c… ([#2746](https://github.com/googleapis/java-bigtable/issues/2746)) ([3a58f9b](https://github.com/googleapis/java-bigtable/commit/3a58f9bebe416186aa8bffee8e024aef135f52c6))



##### Dependencies

  * Update dependency com.google.cloud:gapic-libraries-bom to v1.76.0 ([#2754](https://github.com/googleapis/java-bigtable/issues/2754)) ([be54ef6](https://github.com/googleapis/java-bigtable/commit/be54ef69a2c2d506fc84d08a202e1eb3dafaa849))
  * Update shared dependencies ([#2752](https://github.com/googleapis/java-bigtable/issues/2752)) ([fe1074c](https://github.com/googleapis/java-bigtable/commit/fe1074cb7631746b5bacee2fb4bbd37e4a96416a))



## December 26, 2025

Feature

Continuous materialized views support up to five continuous materialized views per table. This lets you create multiple asynchronous secondary indexes on a table or have a mix of precomputed aggregate views and asynchronous secondary indexes on the same base table. For more information, see [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views).

## December 22, 2025

Libraries

### Python

#### [2.35.0](https://github.com/googleapis/python-bigtable/compare/v2.34.0...v2.35.0) (2025-12-16)

##### Features

  * add basic interceptor to client (#1206) ([6561cfac](https://github.com/googleapis/python-bigtable/commit/6561cfac))

  * Add encodings for STRUCT and the Timestamp type ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))

  * add PeerInfo proto in Bigtable API ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))

  * Add Type API updates needed to support structured keys in materialized views ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))

  * support mTLS certificates when available (#1249) ([ca20219c](https://github.com/googleapis/python-bigtable/commit/ca20219c))




##### Bug Fixes

  * re-export AddToCell for consistency (#1241) ([2a5baf11](https://github.com/googleapis/python-bigtable/commit/2a5baf11))

  * async client uses fixed grace period (#1236) ([544db1cd](https://github.com/googleapis/python-bigtable/commit/544db1cd))

  * Deprecate credentials_file argument ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))

  * Add ReadRows/SampleRowKeys bindings for materialized views ([72dfdc44](https://github.com/googleapis/python-bigtable/commit/72dfdc44))

  * retry cancelled errors (#1235) ([e3fd5d86](https://github.com/googleapis/python-bigtable/commit/e3fd5d86))




### Java

#### [2.71.0-rc1](https://github.com/googleapis/java-bigtable/compare/v2.70.1...v2.71.0-rc1) (2025-12-19)

##### Features

  * update with latest from main ([#2740](https://github.com/googleapis/java-bigtable/issues/2740)) ([90e1a02](https://github.com/googleapis/java-bigtable/commit/90e1a02c46830751a0f158b3a337eb2f926b0ee0))
  * feat: Upgrade protobuf gen code to 4.33 ([#2741](https://github.com/googleapis/java-bigtable/issues/2741)) ([2b1d201](https://github.com/googleapis/java-bigtable/commit/2b1d201d56540cdb45b65b4ed2a1c786a519d3a0))



##### Dependencies

  * update sdk-platform-java-config to 3.55.0-rc1 ([#2738](https://github.com/googleapis/java-bigtable/issues/2738)) ([136f164](https://github.com/googleapis/java-bigtable/commit/136f16474e7ff147c68e976894070727dfc9add8))



### Go

#### [1.41.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.40.1...bigtable/v1.41.0) (2025-12-15)

##### Features

  * add PeerInfo proto in Bigtable API (PiperOrigin-RevId: 829585900) ([185951b3](https://github.com/googleapis/google-cloud-go/commit/185951b3))

  * precompute featureflags in client and reuse (#13297) ([3b3253ac](https://github.com/googleapis/google-cloud-go/commit/3b3253ac))

  * Add experimental Bigtable connection pool with custom load balancing strategy. (#12882) ([7aa96127](https://github.com/googleapis/google-cloud-go/commit/7aa96127))

  * Enable ALTS hard bound token in Bigtable w/ direct access (#13153) ([90239341](https://github.com/googleapis/google-cloud-go/commit/90239341))

  * Enable routing cookie and attempt headers for enhanced retries (#12964) ([96cfd47a](https://github.com/googleapis/google-cloud-go/commit/96cfd47a))




##### Bug Fixes

  * fix project id sent in otel (#13286) ([4865868c](https://github.com/googleapis/google-cloud-go/commit/4865868c))

  * screaming uppercase metric status (#13484) ([b35ee8fd](https://github.com/googleapis/google-cloud-go/commit/b35ee8fd))




##### Performance Improvements

  * parallelize the exportTimeSeries function (#13004) ([bafd691d](https://github.com/googleapis/google-cloud-go/commit/bafd691d))



## December 15, 2025

Libraries

### Java

#### [2.70.1](https://github.com/googleapis/java-bigtable/compare/v2.70.0...v2.70.1) (2025-12-12)

##### Dependencies

  * Update shared dependencies ([#2734](https://github.com/googleapis/java-bigtable/issues/2734)) ([2823705](https://github.com/googleapis/java-bigtable/commit/28237059edaa20028ea35a1903bdee8c02885260))



## December 12, 2025

Feature

In the Google Cloud console, you can import data into Bigtable using the [Dataflow job builder](https://docs.cloud.google.com/dataflow/docs/guides/job-builder), a web interface for building and running Dataflow pipelines. This integration provides a pre-populated template to import data from Pub/Sub to Bigtable. You can also create a custom job to import data from other sources. For more information, see [Import and export data](https://docs.cloud.google.com/bigtable/docs/import-export).

## November 24, 2025

Libraries

### Java

#### [2.69.0](https://github.com/googleapis/java-bigtable/compare/v2.68.0...v2.69.0) (2025-11-17)

##### Features

  * **bigtable:** Add internal grpc subconnections metric and add outstanding rpcs to INTERNAL_VIEW ([#2700](https://github.com/googleapis/java-bigtable/issues/2700)) ([e3e6e99](https://github.com/googleapis/java-bigtable/commit/e3e6e993ee197f897c166fb8959755db0cb9c3fc))
  * **bigtable:** Expose a metric to track the number of outstanding rpcs (unary , streaming) in channel pool ([#2696](https://github.com/googleapis/java-bigtable/issues/2696)) ([140a1ad](https://github.com/googleapis/java-bigtable/commit/140a1ad81947da26c1539632ff04748dc3498d69))
  * **bigtable:** Populate alts field in channel entry ([#2702](https://github.com/googleapis/java-bigtable/issues/2702)) ([1bfb763](https://github.com/googleapis/java-bigtable/commit/1bfb763e6e4fb6fe8c808abe5dbd4221d3a632c3))
  * Enable ALTS hard bound token in Bigtable w/ direct access ([#2695](https://github.com/googleapis/java-bigtable/issues/2695)) ([d12b37d](https://github.com/googleapis/java-bigtable/commit/d12b37dacf8712d30be05175828999af74159819))



### Java

#### [2.70.0](https://github.com/googleapis/java-bigtable/compare/v2.69.0...v2.70.0) (2025-11-18)

##### Features

  * Add PeerInfo proto in Bigtable API ([0736694](https://github.com/googleapis/java-bigtable/commit/0736694c74099a98ab9f36ecb011a31458c6d8c6))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.1 ([0736694](https://github.com/googleapis/java-bigtable/commit/0736694c74099a98ab9f36ecb011a31458c6d8c6))



##### Dependencies

  * Update shared dependencies ([#2704](https://github.com/googleapis/java-bigtable/issues/2704)) ([97a8a0e](https://github.com/googleapis/java-bigtable/commit/97a8a0e36281c3154e03e2ba74aed9af00c9a22b))



##### Documentation

  * Update javadoc sample for BigtableTableAdminClient.listTables ([#2308](https://github.com/googleapis/java-bigtable/issues/2308)) ([56237d7](https://github.com/googleapis/java-bigtable/commit/56237d7a8d420f526237e11c868fd85e9f256831))



### Java

#### [2.70.0](https://github.com/googleapis/java-bigtable/compare/v2.69.0...v2.70.0) (2025-11-18)

##### Features

  * Add PeerInfo proto in Bigtable API ([0736694](https://github.com/googleapis/java-bigtable/commit/0736694c74099a98ab9f36ecb011a31458c6d8c6))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.64.1 ([0736694](https://github.com/googleapis/java-bigtable/commit/0736694c74099a98ab9f36ecb011a31458c6d8c6))



##### Dependencies

  * Update shared dependencies ([#2704](https://github.com/googleapis/java-bigtable/issues/2704)) ([97a8a0e](https://github.com/googleapis/java-bigtable/commit/97a8a0e36281c3154e03e2ba74aed9af00c9a22b))



##### Documentation

  * Update javadoc sample for BigtableTableAdminClient.listTables ([#2308](https://github.com/googleapis/java-bigtable/issues/2308)) ([56237d7](https://github.com/googleapis/java-bigtable/commit/56237d7a8d420f526237e11c868fd85e9f256831))



## November 03, 2025

Feature

You can use protocol buffer (protobuf) schemas to query individual fields within protobuf messages stored as bytes in Bigtable. First, [create and manage your protobuf schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas). Then, [query your protobuf data](https://docs.cloud.google.com/bigtable/docs/query-protobuf-data) using GoogleSQL for Bigtable or BigQuery external tables. This feature is in [Preview](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages).

## October 28, 2025

Feature

You can use Cloud KMS Autokey in the Google Cloud console to automate the creation and use of [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/cmek) in Bigtable clusters.

## October 27, 2025

Libraries

### Java

#### [2.68.0](https://github.com/googleapis/java-bigtable/compare/v2.67.1...v2.68.0) (2025-10-22)

##### Features

  * Add Type API updates needed to support structured keys in materialized views ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))



##### Bug Fixes

  * Add ReadRows/SampleRowKeys bindings for materialized views ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.62.3 ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.63.0 ([ed6c03f](https://github.com/googleapis/java-bigtable/commit/ed6c03ff50f42a06472f5be781b68937f48228d1))
  * Don't use String.format in Preconditions messages ([#2691](https://github.com/googleapis/java-bigtable/issues/2691)) ([62a1812](https://github.com/googleapis/java-bigtable/commit/62a18128d8ec65484509dde6cd0c2b0322890cc9))
  * Fixed the bigtableadmin API name for snippet region tags and possibly other GAPIC attributes ([469290e](https://github.com/googleapis/java-bigtable/commit/469290eb188ce7155abc81d4fec9dd8319851cd9))



##### Dependencies

  * Update shared dependencies ([#2697](https://github.com/googleapis/java-bigtable/issues/2697)) ([611ad20](https://github.com/googleapis/java-bigtable/commit/611ad208359e3c1f2e675d5e4e8c8ade3616b02b))



### Python

#### [2.34.0](https://github.com/googleapis/python-bigtable/compare/v2.33.0...v2.34.0) (2025-10-16)

##### Features

  * Add support for Python 3.14 ([#1217](https://github.com/googleapis/python-bigtable/issues/1217)) ([263332a](https://github.com/googleapis/python-bigtable/commit/263332af71a229cb4fa598008a708137086a6f67))



Feature

Bigtable provides vector and key-value store integrations for LangChain, an LLM orchestration framework. For more information, see [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/bigtable/docs/langchain) and [Perform Maximal Marginal Relevance search with LangChain on Bigtable](https://docs.cloud.google.com/bigtable/docs/mmr-vector-search).

## October 20, 2025

Feature

You can [save queries](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console#save-query) and then [view and manage](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console#view_and_manage_saved_queries) the saved queries in Bigtable Studio. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 13, 2025

Libraries

### Python

#### [2.33.0](https://github.com/googleapis/python-bigtable/compare/v2.32.0...v2.33.0) (2025-10-06)

##### Features

  * Add support for Proto and Enum types ([#1202](https://github.com/googleapis/python-bigtable/issues/1202)) ([34ceb86](https://github.com/googleapis/python-bigtable/commit/34ceb86007db08d453fa25cca4968d5b498ffcd6))
  * Expose universe_domain for tpc ([#1150](https://github.com/googleapis/python-bigtable/issues/1150)) ([451fd97](https://github.com/googleapis/python-bigtable/commit/451fd97e435218ffed47d39423680ffc4feccac4))



##### Bug Fixes

  * Fix instance registration cleanup on early iterator termination ([#1216](https://github.com/googleapis/python-bigtable/issues/1216)) ([bbfd746](https://github.com/googleapis/python-bigtable/commit/bbfd746c61a6362efa42c7899ec3e34ceb541c83))
  * Refactor channel refresh ([#1174](https://github.com/googleapis/python-bigtable/issues/1174)) ([6fa3008](https://github.com/googleapis/python-bigtable/commit/6fa30084058bc34d4487d1fee5c87d7795ff167a))



### Java

#### [2.67.1](https://github.com/googleapis/java-bigtable/compare/v2.67.0...v2.67.1) (2025-10-08)

##### Dependencies

  * Update shared dependencies ([#2686](https://github.com/googleapis/java-bigtable/issues/2686)) ([d7eaa02](https://github.com/googleapis/java-bigtable/commit/d7eaa02d89a63d9f9197d26e430267eff200b126))



## October 07, 2025

Feature

The [Cassandra-Bigtable proxy adapter](https://docs.cloud.google.com/bigtable/docs/migrate-from-cassandra), which lets you connect your Apache Cassandra-based applications to Bigtable, is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Feature

You can connect to Bigtable from Java applications and other reporting tools that support a generic JDBC adapter by using the [Bigtable JDBC driver](https://docs.cloud.google.com/bigtable/docs/reference/jdbc). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 06, 2025

Feature

You can optimize storage with Bigtable [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage), reduce storage costs, and retain data for longer. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 29, 2025

Libraries

### Go

#### [1.40.1](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.40.0...bigtable/v1.40.1) (2025-09-26)

##### Features

  * **bigtable:** Add an e2e flow for direct access with instructions ([#12939](https://github.com/googleapis/google-cloud-go/issues/12939)) ([fdcdde8](https://github.com/googleapis/google-cloud-go/commit/fdcdde809db710633e3102440d11b3365bdd1fd4))



##### Bug Fixes

  * **bigtable:** Release bigtable as 1.40.1 ([#12961](https://github.com/googleapis/google-cloud-go/issues/12961)) ([33e1474](https://github.com/googleapis/google-cloud-go/commit/33e1474de4d6ea19c4341b833f926b828b32abdd))
  * **bigtable:** Use stable stats.NewMetricSet ([#12941](https://github.com/googleapis/google-cloud-go/issues/12941)) ([2c713d7](https://github.com/googleapis/google-cloud-go/commit/2c713d7b9291627b1e55757024a542180188ce3f))



#### [1.40.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.39.0...bigtable/v1.40.0) (2025-09-22)

##### Features

  * **bigtable:** Expose otel native grpc metrics in Bigtable ([#12827](https://github.com/googleapis/google-cloud-go/issues/12827)) ([e9d2efd](https://github.com/googleapis/google-cloud-go/commit/e9d2efdcec738f627260845c12994c1d28dc38d7))



### Java

#### [2.67.0](https://github.com/googleapis/java-bigtable/compare/v2.66.0...v2.67.0) (2025-09-24)

##### Features

  * Idle channel eviction ([#2651](https://github.com/googleapis/java-bigtable/issues/2651)) ([70c05c9](https://github.com/googleapis/java-bigtable/commit/70c05c9c09a63c53818384d2a66c622c9b95e00e))
  * Load balancing options for BigtableChannelPool ([#2667](https://github.com/googleapis/java-bigtable/issues/2667)) ([5adaa84](https://github.com/googleapis/java-bigtable/commit/5adaa84d80df08779da7c36a50de4632049cfe96))



##### Bug Fixes

  * Add missing break; to PROTO and ENUM value type check ([#2672](https://github.com/googleapis/java-bigtable/issues/2672)) ([337e432](https://github.com/googleapis/java-bigtable/commit/337e4325f6cb5d11309ec5f33550d47d97cbe3c3))
  * Remove beta api annotation for query paginator ([#2660](https://github.com/googleapis/java-bigtable/issues/2660)) ([f68a1fa](https://github.com/googleapis/java-bigtable/commit/f68a1fae49b701d1fb9942e2af2fa84a1e5b508a))



##### Dependencies

  * Update shared dependencies ([#2679](https://github.com/googleapis/java-bigtable/issues/2679)) ([a5b8260](https://github.com/googleapis/java-bigtable/commit/a5b82609c365ae4792ed822e59039c1a046ef3ff))



## September 15, 2025

Libraries

### Java

#### [2.66.0](https://github.com/googleapis/java-bigtable/compare/v2.65.1...v2.66.0) (2025-09-10)

##### Features

  * Add support for Proto and Enum types ([#2662](https://github.com/googleapis/java-bigtable/issues/2662)) ([da3065d](https://github.com/googleapis/java-bigtable/commit/da3065db331be191fdf9e06be71e45c7832574ea))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.52.1 ([#2668](https://github.com/googleapis/java-bigtable/issues/2668)) ([06ac93e](https://github.com/googleapis/java-bigtable/commit/06ac93e810830f9c04920b488d9a10af8995a6f3))



## September 01, 2025

Libraries

### Java

#### [2.65.1](https://github.com/googleapis/java-bigtable/compare/v2.65.0...v2.65.1) (2025-08-27)

##### Dependencies

  * Update shared dependencies ([#2664](https://github.com/googleapis/java-bigtable/issues/2664)) ([841318b](https://github.com/googleapis/java-bigtable/commit/841318b2248dcda89d8482bc2e84c838bd8be8d0))



### Go

#### [1.39.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.38.0...bigtable/v1.39.0) (2025-08-28)

##### Features

  * **bigtable/admin:** Add tags field to Instance proto (stable branch) ([a846564](https://github.com/googleapis/google-cloud-go/commit/a8465647b7166ca85e85db5093cef563e3258467))
  * **bigtable/spanner:** Allow disable gRPC DirectPath deps ([#12469](https://github.com/googleapis/google-cloud-go/issues/12469)) ([2205d27](https://github.com/googleapis/google-cloud-go/commit/2205d27d8fff56c0b25facfc60daa766f4d10ee8))
  * **bigtable:** Add client epoch for each call ([#12685](https://github.com/googleapis/google-cloud-go/issues/12685)) ([c9eac01](https://github.com/googleapis/google-cloud-go/commit/c9eac019c22e417fff32c2a4761eb3e98e5ee6ff))
  * **bigtable:** Add Idempotency to Cloud Bigtable MutateRowRequest API ([98ba6f0](https://github.com/googleapis/google-cloud-go/commit/98ba6f06e69685bca510ca85c12124434f9ba1e8))
  * **bigtable:** Add Idempotency to Cloud Bigtable MutateRowsRequest API ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
  * **bigtable:** Adding support to schema bundles ([#12516](https://github.com/googleapis/google-cloud-go/issues/12516)) ([688eb13](https://github.com/googleapis/google-cloud-go/commit/688eb13ea98a2a041513b06d47dddfbfc29a9117))
  * **bigtable:** Create first response latencies instrument ([#12706](https://github.com/googleapis/google-cloud-go/issues/12706)) ([6f34867](https://github.com/googleapis/google-cloud-go/commit/6f34867b4788f971ce2cd5fc9c4d448310d94021))
  * **bigtable:** Expose directaccess via a env variable ([#12684](https://github.com/googleapis/google-cloud-go/issues/12684)) ([0306910](https://github.com/googleapis/google-cloud-go/commit/0306910f37d7983e92e31b6a759165f5590bf9ba))
  * **bigtable:** Expose pinger in go client ([#12683](https://github.com/googleapis/google-cloud-go/issues/12683)) ([a330457](https://github.com/googleapis/google-cloud-go/commit/a330457cfe04872834f0afe353f5e92135d137ef))
  * **bigtable:** First_response_latencies and connectivity_error_count metrics ([#10616](https://github.com/googleapis/google-cloud-go/issues/10616)) ([3054593](https://github.com/googleapis/google-cloud-go/commit/3054593d1f59a65c822a0cf7b8f78440f6234a1d))
  * **bigtable:** Publish Proto and Enum types to CBT data API ([83f894e](https://github.com/googleapis/google-cloud-go/commit/83f894e372ae66b96d8d9d4379fa0ea18547fe72))
  * **bigtable:** Record client_blocking_latencies ([#12698](https://github.com/googleapis/google-cloud-go/issues/12698)) ([5f03fb3](https://github.com/googleapis/google-cloud-go/commit/5f03fb3685d34e63aacb4f62132f2978efa8e7d8))
  * **bigtable:** Support universe domain ([#12567](https://github.com/googleapis/google-cloud-go/issues/12567)) ([fc59e39](https://github.com/googleapis/google-cloud-go/commit/fc59e39b63abde64c161ec9ef67bee6312e54aea))
  * **bigtable:** Update ListSchemaBundles to returns only names ([#12563](https://github.com/googleapis/google-cloud-go/issues/12563)) ([83ea7c4](https://github.com/googleapis/google-cloud-go/commit/83ea7c420baf1a7c004796843eb377e4344f41b1))



##### Bug Fixes

  * **bigtable:** Add ReadRows/SampleRowKeys bindings for materialized views ([7616e81](https://github.com/googleapis/google-cloud-go/commit/7616e8128384e0ce9ee12fe3dd622e61a9785534))
  * **bigtable:** Fix NoopMetricsProvider panic ([#12709](https://github.com/googleapis/google-cloud-go/issues/12709)) ([8c6da0d](https://github.com/googleapis/google-cloud-go/commit/8c6da0dd99cec1bb046fac771c0404cf5476187e))
  * **bigtable:** Ignore errors while creating monitoring client and disable metrics ([#12708](https://github.com/googleapis/google-cloud-go/issues/12708)) ([2346cf1](https://github.com/googleapis/google-cloud-go/commit/2346cf159e80a3b09679c181c423972149fbafb1))
  * **bigtable:** Update routing_parameters.path_template ([c574e28](https://github.com/googleapis/google-cloud-go/commit/c574e287f49cc1c3b069b35d95b98da2bc9b948f))



##### Performance Improvements

  * **bigtable:** Create attributes only when enabled ([#12647](https://github.com/googleapis/google-cloud-go/issues/12647)) ([aa31abc](https://github.com/googleapis/google-cloud-go/commit/aa31abcefd63d6cb589dcc4d9ed45c6658941385))



##### Documentation

  * **bigtable:** Minor comment update for field `idempotency` in message `.google.bigtable.v2.MutateRowRequest` ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))
  * **bigtable:** Sync generated comments from the API Protos ([ac4970b](https://github.com/googleapis/google-cloud-go/commit/ac4970b5a6318dbfcdca7da5ee256852ca49ea23))



### Java

#### [2.65.1](https://github.com/googleapis/java-bigtable/compare/v2.65.0...v2.65.1) (2025-08-27)

##### Dependencies

  * Update shared dependencies ([#2664](https://github.com/googleapis/java-bigtable/issues/2664)) ([841318b](https://github.com/googleapis/java-bigtable/commit/841318b2248dcda89d8482bc2e84c838bd8be8d0))



## August 28, 2025

Announcement

Bigtable tools are available in [Agent Development Kit (ADK)](https://google.github.io/adk-docs/). With these tools, you can build AI agents that can interact with Bigtable data and metadata in the following ways:

  * Obtain metadata about Bigtable tables and instances.
  * Execute LLM-powered SQL queries.



## August 18, 2025

Libraries

### Java

#### [2.65.0](https://github.com/googleapis/java-bigtable/compare/v2.64.0...v2.65.0) (2025-08-12)

##### Features

  * **bigtable:** Lower the value for max rpc channels as channel resize is slow (1m, 2 channel) ([#2656](https://github.com/googleapis/java-bigtable/issues/2656)) ([d8055c1](https://github.com/googleapis/java-bigtable/commit/d8055c1fb75a616cda1503b92d7cddb9da47d42b))



## August 11, 2025

Libraries

### Python

#### [2.32.0](https://github.com/googleapis/python-bigtable/compare/v2.31.0...v2.32.0) (2025-08-01)

##### Features

  * Add Idempotency to Cloud Bigtable MutateRowsRequest API ([#1143](https://github.com/googleapis/python-bigtable/issues/1143)) ([c3e3eb0](https://github.com/googleapis/python-bigtable/commit/c3e3eb0e4ce44ece72b150dc5822846627074fba))
  * Add support for AddToCell in Data Client ([#1147](https://github.com/googleapis/python-bigtable/issues/1147)) ([1a5b4b5](https://github.com/googleapis/python-bigtable/commit/1a5b4b514cadae5c83d61296314285d3774992c5))
  * Implement SQL support in test proxy ([#1106](https://github.com/googleapis/python-bigtable/issues/1106)) ([7a91bbf](https://github.com/googleapis/python-bigtable/commit/7a91bbfb9df23f7e93c40b88648840342af6f16f))
  * Modernized Bigtable Admin Client featuring selective GAPIC generation ([#1177](https://github.com/googleapis/python-bigtable/issues/1177)) ([58e7d37](https://github.com/googleapis/python-bigtable/commit/58e7d3782df6b13a42af053263afc575222a6b83))



### Java

#### [2.64.0](https://github.com/googleapis/java-bigtable/compare/v2.63.0...v2.64.0) (2025-08-08)

##### Features

  * Add tags field to Instance proto (stable branch) ([089d527](https://github.com/googleapis/java-bigtable/commit/089d52700c225015fabfaa763163c5874b96d830))



##### Dependencies

  * Update shared dependencies ([#2654](https://github.com/googleapis/java-bigtable/issues/2654)) ([4b706f4](https://github.com/googleapis/java-bigtable/commit/4b706f4f76a8152556aa99656b440adb30f37a4c))
  * Update the Java code generator (gapic-generator-java) to 2.61.0 ([089d527](https://github.com/googleapis/java-bigtable/commit/089d52700c225015fabfaa763163c5874b96d830))



## August 04, 2025

Announcement

You can add the [Cassandra to Bigtable client for Java](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/blob/main/cassandra-bigtable-migration-tools/cassandra-bigtable-java-client/cassandra-bigtable-java-client-lib/README.md) library to your Java project from the Maven Central repository.

Libraries

### Java

#### [2.63.0](https://github.com/googleapis/java-bigtable/compare/v2.62.0...v2.63.0) (2025-07-30)

##### Features

  * Add Idempotency to Cloud Bigtable MutateRowsRequest API ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))
  * Add port as a parameter for the bigtable emulator ([#2645](https://github.com/googleapis/java-bigtable/issues/2645)) ([5acd3dc](https://github.com/googleapis/java-bigtable/commit/5acd3dc01c36072bd28248d560c5d923c34b1817))
  * Add type support for Proto and Enum ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))
  * Publish Proto and Enum types to CBT data API ([ace12d5](https://github.com/googleapis/java-bigtable/commit/ace12d53fe9f4d3779b2b1a2aed69ceeedd11600))
  * Selective GAPIC autogeneration for Python Bigtable Admin ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.60.2 ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))
  * Update routing_parameters.path_template ([e219c38](https://github.com/googleapis/java-bigtable/commit/e219c387487673869fb8bb55a5060bdc9d37bbcb))



##### Dependencies

  * Update sdk-platorm-java-config to 3.50.2 ([#2646](https://github.com/googleapis/java-bigtable/issues/2646)) ([03e6961](https://github.com/googleapis/java-bigtable/commit/03e6961e758a9a0c39cb168c73c853328c14bfd1))



##### Documentation

  * Sync generated comments from the API Protos ([bc58b4f](https://github.com/googleapis/java-bigtable/commit/bc58b4f31ef457bd322f270b044735e4b62d298f))



## July 31, 2025

Feature

[Logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views) for Bigtable are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Logical views let you save a SQL query as a specific, shareable view of your data—even with a flexible schema—and then control who has permission to see the results.

## July 21, 2025

Libraries

### Java

#### [2.62.0](https://github.com/googleapis/java-bigtable/compare/v2.61.0...v2.62.0) (2025-07-15)

##### Features

  * Add Idempotency to Cloud Bigtable MutateRowRequest API ([b5acca6](https://github.com/googleapis/java-bigtable/commit/b5acca6ac4f1eec420adb27bc77aa1bda0ec2dca))
  * Add SchemaBundles API ([b5acca6](https://github.com/googleapis/java-bigtable/commit/b5acca6ac4f1eec420adb27bc77aa1bda0ec2dca))
  * **bigtable:** Add schema bundle support ([#2619](https://github.com/googleapis/java-bigtable/issues/2619)) ([7d7b9a9](https://github.com/googleapis/java-bigtable/commit/7d7b9a966d3ef7b7a0ef3f82038ab73f4d791427))
  * Next release from main branch is 2.62.0 ([#2621](https://github.com/googleapis/java-bigtable/issues/2621)) ([202b211](https://github.com/googleapis/java-bigtable/commit/202b21102e71da71ff56f19a12d8a00a59cd8107))



##### Dependencies

  * Minor cleanup ([#2623](https://github.com/googleapis/java-bigtable/issues/2623)) ([7b230e8](https://github.com/googleapis/java-bigtable/commit/7b230e86902b5733c06e45fad90da76653ee1096))
  * Update shared dependencies ([#2616](https://github.com/googleapis/java-bigtable/issues/2616)) ([eb7cfd5](https://github.com/googleapis/java-bigtable/commit/eb7cfd526aa999c614b7b8285d32759e2739ff9a))



## July 07, 2025

Libraries

### Go

#### [1.38.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.37.0...bigtable/v1.38.0) (2025-06-27)

##### Features

  * **bigtable/admin:** Add deletion_protection support for LVs ([a95a0bf](https://github.com/googleapis/google-cloud-go/commit/a95a0bf4172b8a227955a0353fd9c845f4502411))
  * **bigtable/admin:** Add SchemaBundles API ([116a33a](https://github.com/googleapis/google-cloud-go/commit/116a33ab13c9fac6f6830dded55c24d38504707b))
  * **bigtable:** Add application blocking latencies ([#11349](https://github.com/googleapis/google-cloud-go/issues/11349)) ([8f145ed](https://github.com/googleapis/google-cloud-go/commit/8f145ed17ceb76c66df328776af1bb7137661e74))
  * **bigtable:** Add DeletionProtection support for Logical Views ([#11895](https://github.com/googleapis/google-cloud-go/issues/11895)) ([ed488b9](https://github.com/googleapis/google-cloud-go/commit/ed488b94b46b50585f91e065dd877c06d85ce879))
  * **bigtable:** Connectivity_error_count client side metric ([#12438](https://github.com/googleapis/google-cloud-go/issues/12438)) ([dd45fd7](https://github.com/googleapis/google-cloud-go/commit/dd45fd7487e7f379f26d330483e5f2b83d52ee09))
  * **bigtable:** NewServerWithListener ([#12408](https://github.com/googleapis/google-cloud-go/issues/12408)) ([59ea0de](https://github.com/googleapis/google-cloud-go/commit/59ea0de1013a4320deba227102fecbf77e8211cb))
  * **bigtable:** Use delay from RetryInfo ([#11955](https://github.com/googleapis/google-cloud-go/issues/11955)) ([0510711](https://github.com/googleapis/google-cloud-go/commit/051071159420cd199858d556186aa7dfd86ac940))



##### Bug Fixes

  * **bigtable:** Correct the Bigtable monitoring client options ([#12410](https://github.com/googleapis/google-cloud-go/issues/12410)) ([bd966bc](https://github.com/googleapis/google-cloud-go/commit/bd966bc089d6f9b4c34cdd1c954f242665dcd7d8))
  * **bigtable:** Fix: upgrade gRPC service registration func ([6a871e0](https://github.com/googleapis/google-cloud-go/commit/6a871e0f6924980da4fec78405bfe0736522afa8))
  * **bigtable:** Retry RST stream errors ([#11477](https://github.com/googleapis/google-cloud-go/issues/11477)) ([df43b4a](https://github.com/googleapis/google-cloud-go/commit/df43b4af7529ae91993361b485daff3f83234b2b))



##### Performance Improvements

  * **bigtable:** Refactor metric attributes for performance ([#12445](https://github.com/googleapis/google-cloud-go/issues/12445)) ([f734ec6](https://github.com/googleapis/google-cloud-go/commit/f734ec685a78f11a2d4acb9625aa7e457cb020cf))



##### Documentation

  * **bigtable/admin:** Improved comment formatting and product naming ([116a33a](https://github.com/googleapis/google-cloud-go/commit/116a33ab13c9fac6f6830dded55c24d38504707b))



Change

When you [undelete a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#undelete-table), Bigtable automatically enables deletion protection for that table.

## June 30, 2025

Libraries

### Java

#### [2.61.0](https://github.com/googleapis/java-bigtable/compare/v2.60.0...v2.61.0) (2025-06-27)

##### Features

  * Add getter for universe domain in JwtCredentialsWithAudience ([#2598](https://github.com/googleapis/java-bigtable/issues/2598)) ([9ad66b1](https://github.com/googleapis/java-bigtable/commit/9ad66b129923500cdeb794fc2e4570ad8b1d92fd))



##### Bug Fixes

  * Add name elements for the POM.xml files ([a873719](https://github.com/googleapis/java-bigtable/commit/a873719e7e32a0cd21dc259911a193520f20797e))
  * Populate table id for materialized view ([#2610](https://github.com/googleapis/java-bigtable/issues/2610)) ([50c3fe2](https://github.com/googleapis/java-bigtable/commit/50c3fe2ffe66acaba8cb408dc3b1a4d13a4a2556))



##### Dependencies

  * Update shared dependencies ([#2605](https://github.com/googleapis/java-bigtable/issues/2605)) ([4cc7246](https://github.com/googleapis/java-bigtable/commit/4cc7246ff8e2e0e26d2edc0aee8866a32ec1c8ab))



## June 24, 2025

Feature

You can use [Data Boost](https://docs.cloud.google.com/bigquery/docs/create-bigtable-external-table#compute) to analyze your Bigtable data with BigQuery without impacting the performance of the clusters that handle your application traffic. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## June 09, 2025

Libraries

### Java

#### [2.60.0](https://github.com/googleapis/java-bigtable/compare/v2.59.0...v2.60.0) (2025-06-06)

##### Features

  * Improve error message on malformed struct ([#2592](https://github.com/googleapis/java-bigtable/issues/2592)) ([7f5fdf0](https://github.com/googleapis/java-bigtable/commit/7f5fdf094c5fe140807ce6abcea0b891462ba809))
  * Run ExecuteQuery conformance tests ([#2557](https://github.com/googleapis/java-bigtable/issues/2557)) ([0bbc083](https://github.com/googleapis/java-bigtable/commit/0bbc083b9e798e5b557f3ffe7090b45e66c9ada5))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.59.0 ([65782aa](https://github.com/googleapis/java-bigtable/commit/65782aaf89ad78aafd7f5928e81e513c3016b471))
  * Ensure that multiple instances of a client in the same process dont clobber each other ([#2590](https://github.com/googleapis/java-bigtable/issues/2590)) ([8d3dca4](https://github.com/googleapis/java-bigtable/commit/8d3dca43224179829829bcf91972610c666b130b))



##### Dependencies

  * Update shared dependencies ([#2587](https://github.com/googleapis/java-bigtable/issues/2587)) ([8ec0339](https://github.com/googleapis/java-bigtable/commit/8ec033994f20b2b3aea0dfcdaffbdd1c6d19fdad))



## May 29, 2025

Change

The [Bigtable Spark connector](https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector) supports Scala versions 2.12 and 2.13 in all connector versions and has been updated as follows:

  * Connector versions 0.5.0 and later support [dynamic columns](https://github.com/GoogleCloudDataproc/spark-bigtable-connector?tab=readme-ov-file#catalog-with-variable-column-definitions).
  * Connector versions 0.6.0 and later support [custom authentication providers](https://github.com/GoogleCloudDataproc/spark-bigtable-connector/?tab=readme-ov-file#how-do-i-authenticate-outside-gce--dataproc) and [efficient joins with data sources](https://github.com/GoogleCloudDataproc/spark-bigtable-connector/?tab=readme-ov-file#efficient-joins-with-other-data-sources).



## May 27, 2025

Announcement

You can delete logical and continuous materialized views in the Google Cloud console. For more information, see [Delete a logical view](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views#delete) or [Delete a continuous materialized view](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views#delete).

## May 26, 2025

Libraries

### Python

#### [2.31.0](https://github.com/googleapis/python-bigtable/compare/v2.30.1...v2.31.0) (2025-05-22)

##### Features

  * Add deletion_protection support for LVs ([#1108](https://github.com/googleapis/python-bigtable/issues/1108)) ([c6d384d](https://github.com/googleapis/python-bigtable/commit/c6d384d4a104c182326e22dc3f10b7b905780dee))
  * Support authorized views ([#1034](https://github.com/googleapis/python-bigtable/issues/1034)) ([97a0198](https://github.com/googleapis/python-bigtable/commit/97a019833d82e617769c56761aa5548d3ab896b9))
  * Throw better error on invalid metadata response ([#1107](https://github.com/googleapis/python-bigtable/issues/1107)) ([2642317](https://github.com/googleapis/python-bigtable/commit/2642317077b723ca8fd62aa86322b524868c2c4d))



##### Bug Fixes

  * Re-add py-typed file for bigtable package ([#1085](https://github.com/googleapis/python-bigtable/issues/1085)) ([0c322c7](https://github.com/googleapis/python-bigtable/commit/0c322c79ecbe4cde3e79d8e83ac655a978d07877))



## May 19, 2025

Libraries

### Java

#### [2.59.0](https://github.com/googleapis/java-bigtable/compare/v2.58.2...v2.59.0) (2025-05-16)

##### Features

  * **bigtable:** Add DeletionProtection support for Logical Views ([#2539](https://github.com/googleapis/java-bigtable/issues/2539)) ([d9ba32b](https://github.com/googleapis/java-bigtable/commit/d9ba32b8e5792ceed054f67c58f5622e153e87d6))



##### Dependencies

  * Update googleapis/sdk-platform-java action to v2.58.0 ([#2581](https://github.com/googleapis/java-bigtable/issues/2581)) ([c9b0289](https://github.com/googleapis/java-bigtable/commit/c9b028902dc8aae9552181d65c9743be09d45ecf))
  * Update shared dependencies ([#2584](https://github.com/googleapis/java-bigtable/issues/2584)) ([ba82675](https://github.com/googleapis/java-bigtable/commit/ba82675c25dbe12443ac5ef48464dcb3f8c8894c))



## May 13, 2025

Feature

You can export query results from Bigtable Studio. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). 

For more information, see [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).

## May 12, 2025

Libraries

### Java

#### [2.58.2](https://github.com/googleapis/java-bigtable/compare/v2.58.1...v2.58.2) (2025-05-08)

##### Bug Fixes

  * Use service name as the default audience ([#2579](https://github.com/googleapis/java-bigtable/issues/2579)) ([af6d7bd](https://github.com/googleapis/java-bigtable/commit/af6d7bd28d9d7a4ebb90825a9b4b8a73d63172f6))



##### Dependencies

  * Update shared dependencies ([#2565](https://github.com/googleapis/java-bigtable/issues/2565)) ([043f11b](https://github.com/googleapis/java-bigtable/commit/043f11b16948c338096d9407de1e99f02656169e))



## May 07, 2025

Feature

You can [use Data Boost](https://docs.cloud.google.com/bigquery/docs/create-bigtable-external-table#compute) when you analyze your Bigtable data with BigQuery. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 05, 2025

Libraries

### Java

#### [2.58.0](https://github.com/googleapis/java-bigtable/compare/v2.57.3...v2.58.0) (2025-04-28)

##### Features

  * Add deletion_protection support for LVs ([43c97a3](https://github.com/googleapis/java-bigtable/commit/43c97a3f430ee4ee90d46b3685ae50f13949831c))
  * **bigtable:** Add integration tests for Materialized/Logical Views ([#2518](https://github.com/googleapis/java-bigtable/issues/2518)) ([4d3a7e6](https://github.com/googleapis/java-bigtable/commit/4d3a7e675b60ba6a3225a45b7463edff279f9bc4))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([43c97a3](https://github.com/googleapis/java-bigtable/commit/43c97a3f430ee4ee90d46b3685ae50f13949831c))
  * Fix retry info algorithm setting ([#2562](https://github.com/googleapis/java-bigtable/issues/2562)) ([c424ccb](https://github.com/googleapis/java-bigtable/commit/c424ccba72a191609dc726ed67d03f0d330015fc))
  * Use universe domain when creating the monitoring client ([#2570](https://github.com/googleapis/java-bigtable/issues/2570)) ([3b51e12](https://github.com/googleapis/java-bigtable/commit/3b51e1206a4f83078625705ed8d8a899839af1a9))



### Java

#### [2.58.1](https://github.com/googleapis/java-bigtable/compare/v2.58.0...v2.58.1) (2025-04-28)

##### Bug Fixes

  * Close otel instance ([#2571](https://github.com/googleapis/java-bigtable/issues/2571)) ([422fe26](https://github.com/googleapis/java-bigtable/commit/422fe26f3aae30fe74de80fad3848707452d6646))



### Java

#### [2.58.0](https://github.com/googleapis/java-bigtable/compare/v2.57.3...v2.58.0) (2025-04-28)

##### Features

  * Add deletion_protection support for LVs ([43c97a3](https://github.com/googleapis/java-bigtable/commit/43c97a3f430ee4ee90d46b3685ae50f13949831c))
  * **bigtable:** Add integration tests for Materialized/Logical Views ([#2518](https://github.com/googleapis/java-bigtable/issues/2518)) ([4d3a7e6](https://github.com/googleapis/java-bigtable/commit/4d3a7e675b60ba6a3225a45b7463edff279f9bc4))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.56.2 ([43c97a3](https://github.com/googleapis/java-bigtable/commit/43c97a3f430ee4ee90d46b3685ae50f13949831c))
  * Fix retry info algorithm setting ([#2562](https://github.com/googleapis/java-bigtable/issues/2562)) ([c424ccb](https://github.com/googleapis/java-bigtable/commit/c424ccba72a191609dc726ed67d03f0d330015fc))
  * Use universe domain when creating the monitoring client ([#2570](https://github.com/googleapis/java-bigtable/issues/2570)) ([3b51e12](https://github.com/googleapis/java-bigtable/commit/3b51e1206a4f83078625705ed8d8a899839af1a9))



## April 29, 2025

Feature

[Similarity vector search in Bigtable](https://docs.cloud.google.com/bigtable/docs/find-k-nearest-neighbors) by finding the K-nearest neighbors is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

Feature

The [MCP Toolbox for Databases](https://mcp-toolbox.dev/documentation/introduction/) includes a Bigtable connector. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 25, 2025

Feature

Bigtable is supported by [Database Center](https://docs.cloud.google.com/database-center/docs/database-health-issues), which is generally available (GA). The Database Center now provides performance, availability, and data protection in the form of recommender-related health issues. You can also view these performance recommendations in [Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/dashboard-overview).

## April 21, 2025

Libraries

### Go

#### [1.37.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.36.0...bigtable/v1.37.0) (2025-04-15)

##### Features

  * **bigtable:** Allow configuring multicluster routing and isolation ([#11980](https://github.com/googleapis/google-cloud-go/issues/11980)) ([19e2837](https://github.com/googleapis/google-cloud-go/commit/19e2837cd314b6909fd632ca3594eff7b606bb19))



##### Bug Fixes

  * **bigtable:** Correct the retry condition of QueryExpiredViolation ([#11984](https://github.com/googleapis/google-cloud-go/issues/11984)) ([44d8b86](https://github.com/googleapis/google-cloud-go/commit/44d8b86587f82721af99709ed89b7e9e5792e2ff))
  * **bigtable:** Update google.golang.org/api to 0.229.0 ([3319672](https://github.com/googleapis/google-cloud-go/commit/3319672f3dba84a7150772ccb5433e02dab7e201))
  * **bigtable:** Use the same Backoff for idempotent and internal errors ([#11985](https://github.com/googleapis/google-cloud-go/issues/11985)) ([8d1d015](https://github.com/googleapis/google-cloud-go/commit/8d1d0152cf8b96f5cc99a032f558114bb5cbe9f2))



### Python

#### [2.30.1](https://github.com/googleapis/python-bigtable/compare/v2.30.0...v2.30.1) (2025-04-17)

##### Bug Fixes

  * Populate SQL app_profile_id header even when it is unset ([#1109](https://github.com/googleapis/python-bigtable/issues/1109)) ([17b75bd](https://github.com/googleapis/python-bigtable/commit/17b75bd746cb0a616f64a05eb0ed72b46de28a17))



## April 10, 2025

Feature

The [Bigtable CQL client library for Java](https://docs.cloud.google.com/bigtable/docs/migrate-from-cassandra#bigtable-cql-client) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

The [Cassandra-Bigtable proxy adapter](https://docs.cloud.google.com/bigtable/docs/migrate-from-cassandra), which lets you connect your Apache Cassandra-based applications to Bigtable, is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

The [Bigtable Kafka sink](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/tree/main/kafka-connect-bigtable-sink), which lets you directly connect Apache Kafka and Google Cloud Managed Service for Apache Kafka, is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## April 09, 2025

Feature

[Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) for Bigtable are available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

[SQL support for Bigtable](https://docs.cloud.google.com/bigtable/docs/googlesql-overview) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)), including an [`UNPACK`](https://docs.cloud.google.com/bigtable/docs/reference/sql/table-functions-built-in#unpack) feature that lets you read time series data in a tabular format.

Feature

[Logical views](https://docs.cloud.google.com/bigtable/docs/create-manage-logical-views) of Bigtable tables are available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

The Bigtable Studio [query editor](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console#query-editor) is generally available (GA).

## April 07, 2025

Libraries

### Java

#### [2.57.2](https://github.com/googleapis/java-bigtable/compare/v2.57.1...v2.57.2) (2025-03-31)

##### Bug Fixes

  * Library should released as 2.57.2 ([#2549](https://github.com/googleapis/java-bigtable/issues/2549)) ([58d0bbd](https://github.com/googleapis/java-bigtable/commit/58d0bbdcb983e3b5ee403edf45c4e98a6eb8dc16))



### Go

#### [1.36.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.35.0...bigtable/v1.36.0) (2025-03-31)

##### Features

  * **bigtable/admin:** Add MaterializedViews and LogicalViews APIs ([b323f88](https://github.com/googleapis/google-cloud-go/commit/b323f888e349168b4e30a9edb4630dfb6060ed4d))
  * **bigtable/admin:** Add MaterializedViews and LogicalViews APIs ([dd0d1d7](https://github.com/googleapis/google-cloud-go/commit/dd0d1d7b41884c9fc9b5fe808139cccd29e1e486))
  * **bigtable/admin:** Publish row_key_schema fields in table proto and relevant admin APIs to setup a table with a row_key_schema ([3f23a91](https://github.com/googleapis/google-cloud-go/commit/3f23a9176f29a0a69b9d57b16f44b72eb3096d0c))
  * **bigtable:** Add Bind function to bind query params ([#11862](https://github.com/googleapis/google-cloud-go/issues/11862)) ([24c5ae0](https://github.com/googleapis/google-cloud-go/commit/24c5ae0ab119b2b7ba54ba0ea9c5432cdc5ec28f))
  * **bigtable:** Add datatypes for GoogleSQL ([#11816](https://github.com/googleapis/google-cloud-go/issues/11816)) ([5a9eb10](https://github.com/googleapis/google-cloud-go/commit/5a9eb101b691e79a2dae68be6a7dcae152d42868))
  * **bigtable:** Add Execute method to execute GoogleSQL queries ([#11883](https://github.com/googleapis/google-cloud-go/issues/11883)) ([0e53dcd](https://github.com/googleapis/google-cloud-go/commit/0e53dcd0005e7cecba4c7f6ef97645dbc7ce8d16))
  * **bigtable:** Add MaterializedViewName to ReadRows and SampleRowKeys ([b323f88](https://github.com/googleapis/google-cloud-go/commit/b323f888e349168b4e30a9edb4630dfb6060ed4d))
  * **bigtable:** Add methods to read ResultRow ([#11924](https://github.com/googleapis/google-cloud-go/issues/11924)) ([8b8ca9e](https://github.com/googleapis/google-cloud-go/commit/8b8ca9eefcfdbfb3f7cd4b991cd98808cfc03293))
  * **bigtable:** Add PrepareQuery api and update ExecuteQuery to support it ([dd0d1d7](https://github.com/googleapis/google-cloud-go/commit/dd0d1d7b41884c9fc9b5fe808139cccd29e1e486))
  * **bigtable:** Add PrepareStatement to run GoogleSQL queries ([#11829](https://github.com/googleapis/google-cloud-go/issues/11829)) ([ea00b17](https://github.com/googleapis/google-cloud-go/commit/ea00b177060351e695fdc657bd711c136c25212b))
  * **bigtable:** Add support for data APIs for Materialized Views ([#11796](https://github.com/googleapis/google-cloud-go/issues/11796)) ([f5ae93b](https://github.com/googleapis/google-cloud-go/commit/f5ae93b9869d1d9de0d62dfcb8dd4ebb48056b57))
  * **bigtable:** Add support for logical views ([#11792](https://github.com/googleapis/google-cloud-go/issues/11792)) ([630d751](https://github.com/googleapis/google-cloud-go/commit/630d751397a84d06d54add63464d5ad5993768ef))
  * **bigtable:** Add support for materialized views for admin client ([#11793](https://github.com/googleapis/google-cloud-go/issues/11793)) ([640be05](https://github.com/googleapis/google-cloud-go/commit/640be05c744a8bd8f1a3e4ee0673409d707aa098))
  * **bigtable:** Adding node scaling factor ([b680164](https://github.com/googleapis/google-cloud-go/commit/b6801649768f9c94f97c5eaa913d2e1f43e07641))
  * **bigtable:** Disable MV and LV tests ([#11827](https://github.com/googleapis/google-cloud-go/issues/11827)) ([42dca03](https://github.com/googleapis/google-cloud-go/commit/42dca0388c2a2b90206b81f2b7e9deec9deeabbc))
  * **bigtable:** Row key schema support in admin client ([#11777](https://github.com/googleapis/google-cloud-go/issues/11777)) ([4158bac](https://github.com/googleapis/google-cloud-go/commit/4158bac23b8b234e02ab9dcb488ac1523612a3a8))



##### Bug Fixes

  * **bigtable:** Allow GC updates on emulated aggregate column family ([#11499](https://github.com/googleapis/google-cloud-go/issues/11499)) ([0682bfa](https://github.com/googleapis/google-cloud-go/commit/0682bfa5563ec81e2cf3fa9138142ebe482fb6fd))
  * **bigtable:** Update golang.org/x/net to 0.37.0 ([1144978](https://github.com/googleapis/google-cloud-go/commit/11449782c7fb4896bf8b8b9cde8e7441c84fb2fd))



##### Documentation

  * **bigtable/admin:** Fixed formatting of resource path strings ([dd0d1d7](https://github.com/googleapis/google-cloud-go/commit/dd0d1d7b41884c9fc9b5fe808139cccd29e1e486))
  * **bigtable:** Update ExecuteQuery API docs to reflect changes ([dd0d1d7](https://github.com/googleapis/google-cloud-go/commit/dd0d1d7b41884c9fc9b5fe808139cccd29e1e486))



### Java

#### [2.57.3](https://github.com/googleapis/java-bigtable/compare/v2.57.2...v2.57.3) (2025-04-01)

##### Bug Fixes

  * Remove debug messages ([#2552](https://github.com/googleapis/java-bigtable/issues/2552)) ([6359834](https://github.com/googleapis/java-bigtable/commit/63598346ca39767d59d254fce2c718d1258e27d5))



## March 31, 2025

Libraries

### Java

#### [2.57.0](https://github.com/googleapis/java-bigtable/compare/v2.56.0...v2.57.0) (2025-03-24)

##### Features

  * Add PreparedStatement and update ExecuteQuery API to use it ([#2534](https://github.com/googleapis/java-bigtable/issues/2534)) ([49d4d09](https://github.com/googleapis/java-bigtable/commit/49d4d09fd16a1eb4eb566227a049bca2aaaa61e3))



### Java

#### [2.57.1](https://github.com/googleapis/java-bigtable/compare/v2.57.0...v2.57.1) (2025-03-24)

##### Bug Fixes

  * Handling of totalTimeout on sql plan refresh ([#2541](https://github.com/googleapis/java-bigtable/issues/2541)) ([bf49cf9](https://github.com/googleapis/java-bigtable/commit/bf49cf93f9a3b9cbdb155bb6cbb7a9f763b6f738))



## March 26, 2025

Change

The Monitoring page in the Google Cloud console for Bigtable has been renamed to System insights.

## March 24, 2025

Libraries

### Java

#### [2.56.0](https://github.com/googleapis/java-bigtable/compare/v2.55.0...v2.56.0) (2025-03-18)

##### Features

  * **bigtable:** Add support for Logical Views in Admin API ([#2519](https://github.com/googleapis/java-bigtable/issues/2519)) ([6dac3fd](https://github.com/googleapis/java-bigtable/commit/6dac3fd6443e94674af88a1dc97bedd9b3b0c834))
  * **bigtable:** Add support for Materialized Views in Admin API ([#2511](https://github.com/googleapis/java-bigtable/issues/2511)) ([55cd719](https://github.com/googleapis/java-bigtable/commit/55cd719df277a2ae1988c7cd53286558ad86835b))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.55.1 ([7992af0](https://github.com/googleapis/java-bigtable/commit/7992af08b4eb2f408ecb739a73fbdc36ca7af2b5))



##### Dependencies

  * Sdk-platform-java-config 3.45.1 ([#2517](https://github.com/googleapis/java-bigtable/issues/2517)) ([b2af258](https://github.com/googleapis/java-bigtable/commit/b2af258ed72d29644c8bd1079b1d0f223206d75b))



### Python

#### [2.30.0](https://github.com/googleapis/python-bigtable/compare/v2.29.0...v2.30.0) (2025-03-18)

##### Features

  * Update ExecuteQuery to use Prepare ([#1100](https://github.com/googleapis/python-bigtable/issues/1100)) ([8a7abc1](https://github.com/googleapis/python-bigtable/commit/8a7abc1e9c34a9122b2d648e8a358a7097ed3a5d))



##### Bug Fixes

  * Allow protobuf 6.x ([#1092](https://github.com/googleapis/python-bigtable/issues/1092)) ([1015fa8](https://github.com/googleapis/python-bigtable/commit/1015fa83c505487f09820e3a37f76690bd00ab5d))
  * Remove setup.cfg configuration for creating universal wheels ([#1097](https://github.com/googleapis/python-bigtable/issues/1097)) ([95f4b82](https://github.com/googleapis/python-bigtable/commit/95f4b8233cba2a18633e64c5e0bc177e23767a83))



## March 17, 2025

Libraries

### Java

#### [2.55.0](https://github.com/googleapis/java-bigtable/compare/v2.54.0...v2.55.0) (2025-03-11)

##### Features

  * Add MaterializedViewName to ReadRows and SampleRowKeys ([1763c6e](https://github.com/googleapis/java-bigtable/commit/1763c6e9304010ed4034e1ddd03fdb94bca615dc))
  * Add MaterializedViews and LogicalViews APIs ([1763c6e](https://github.com/googleapis/java-bigtable/commit/1763c6e9304010ed4034e1ddd03fdb94bca615dc))
  * Add MaterializedViews and LogicalViews APIs ([7340527](https://github.com/googleapis/java-bigtable/commit/73405272c3fc77ca81c1df7cce1b8d889d4a96c4))
  * Add PrepareQuery api and update ExecuteQuery to support it ([1763c6e](https://github.com/googleapis/java-bigtable/commit/1763c6e9304010ed4034e1ddd03fdb94bca615dc))
  * **bigtable:** Add support for data APIs for materialized views ([#2508](https://github.com/googleapis/java-bigtable/issues/2508)) ([6310a63](https://github.com/googleapis/java-bigtable/commit/6310a631be3345f97d73b50f3b458fe40b071286))
  * **large-row-skip:** Added large-row-skip-callable with configurable rowadapter ([#2509](https://github.com/googleapis/java-bigtable/issues/2509)) ([ba193ef](https://github.com/googleapis/java-bigtable/commit/ba193ef771f913e6e6a1aca630fe52d0921ee077))
  * Next release from main branch is 2.55.0 ([#2506](https://github.com/googleapis/java-bigtable/issues/2506)) ([4e45837](https://github.com/googleapis/java-bigtable/commit/4e458378cc25a4dc5ac3fd1362626d89f0138186))
  * Publish row_key_schema fields in table proto and relevant admin APIs to setup a table with a row_key_schema ([7340527](https://github.com/googleapis/java-bigtable/commit/73405272c3fc77ca81c1df7cce1b8d889d4a96c4))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.54.0 ([91e4369](https://github.com/googleapis/java-bigtable/commit/91e4369d280c09fd2d1b4b5dd88809b6da01b0f8))



##### Documentation

  * Fixed formatting of resource path strings ([7340527](https://github.com/googleapis/java-bigtable/commit/73405272c3fc77ca81c1df7cce1b8d889d4a96c4))



## March 11, 2025

Feature

You can use Cloud KMS Autokey to automate the creation and use of [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/cmek) in Bigtable clusters. This feature is generally available [(GA)](https://cloud.google.com/products#product-launch-stages).

Feature

[Data lineage](https://docs.cloud.google.com/dataplex/docs/about-data-lineage) for Dataflow jobs is generally available [(GA)](https://cloud.google.com/products#product-launch-stages) in the Bigtable Beam connector (`BigtableIO`) and the Bigtable HBase Beam connector (`CloudBigtableIO`). For more information, see [Tracking lineage](https://github.com/googleapis/java-bigtable-hbase/tree/v2.15.0/bigtable-dataflow-parent/bigtable-beam-import#tracking-lineage).

## March 10, 2025

Libraries

### Java

#### [2.54.0](https://github.com/googleapis/java-bigtable/compare/v2.53.0...v2.54.0) (2025-02-28)

##### Features

  * Next release from main branch is 2.54.0 ([#2498](https://github.com/googleapis/java-bigtable/issues/2498)) ([f967ded](https://github.com/googleapis/java-bigtable/commit/f967deda8b68091dcc417b6c51f451abd36696f1))



##### Dependencies

  * Update shared dependencies ([#2493](https://github.com/googleapis/java-bigtable/issues/2493)) ([e1d09e7](https://github.com/googleapis/java-bigtable/commit/e1d09e7d03365d844e957d043e21d71948f98d04))



## March 04, 2025

Feature

Bigtable is available in the `europe-north2` (Stockholm) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## March 03, 2025

Libraries

### Python

#### [2.29.0](https://github.com/googleapis/python-bigtable/compare/v2.28.1...v2.29.0) (2025-02-26)

##### Features

  * Add support for array and float32 SQL query params ([#1078](https://github.com/googleapis/python-bigtable/issues/1078)) ([89b8da8](https://github.com/googleapis/python-bigtable/commit/89b8da8a445aeb08854d9fa77cbc0e4fc042c87f))



##### Bug Fixes

  * Grpc channel refresh ([#1087](https://github.com/googleapis/python-bigtable/issues/1087)) ([f44b36b](https://github.com/googleapis/python-bigtable/commit/f44b36bf51e3e4e3b8a774f96e682d3f1f8d4b16))



### Java

#### [2.53.0](https://github.com/googleapis/java-bigtable/compare/v2.52.0...v2.53.0) (2025-02-21)

##### Features

  * Skip large rows ([#2482](https://github.com/googleapis/java-bigtable/issues/2482)) ([cd7f82e](https://github.com/googleapis/java-bigtable/commit/cd7f82e4b66dc3c34262c73b26afc2fdfd1deed7))



## February 24, 2025

Feature

[Bigtable Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview), a serverless compute service designed for high-throughput read jobs and queries, is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

Automated backup for Bigtable is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see the [Backups overview](https://docs.cloud.google.com/bigtable/docs/backups).

## February 17, 2025

Libraries

### Java

#### [2.52.0](https://github.com/googleapis/java-bigtable/compare/v2.51.2...v2.52.0) (2025-02-14)

##### Features

  * Automated backups are supported in the admin client ([#2472](https://github.com/googleapis/java-bigtable/issues/2472)) ([48633e6](https://github.com/googleapis/java-bigtable/commit/48633e6160593c84f42a02f348ec18c3d1521ef0))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.53.0 ([47ca299](https://github.com/googleapis/java-bigtable/commit/47ca29931699cae87d640185ad31e4b61c0bb212))
  * Extend timeouts for check consistency ([47ca299](https://github.com/googleapis/java-bigtable/commit/47ca29931699cae87d640185ad31e4b61c0bb212))



##### Dependencies

  * Update dependency com.google.cloud:gapic-libraries-bom to v1.52.0 ([#2490](https://github.com/googleapis/java-bigtable/issues/2490)) ([ca25d4e](https://github.com/googleapis/java-bigtable/commit/ca25d4eb6c7333d1a77d2c99b1bb95c2a2f710c1))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.43.0 ([#2481](https://github.com/googleapis/java-bigtable/issues/2481)) ([deb1f79](https://github.com/googleapis/java-bigtable/commit/deb1f79c6efa223f6c2f780724ec9386f44f018a))



## February 10, 2025

Libraries

### Java

#### [2.51.2](https://github.com/googleapis/java-bigtable/compare/v2.51.1...v2.51.2) (2025-02-03)

##### Bug Fixes

  * Add known conformance test failures ([#2474](https://github.com/googleapis/java-bigtable/issues/2474)) ([15488fe](https://github.com/googleapis/java-bigtable/commit/15488fe6cfe05e84c4b6d65565150ee7277a60e7))



##### Dependencies

  * Update shared dependencies ([#2473](https://github.com/googleapis/java-bigtable/issues/2473)) ([4d6d419](https://github.com/googleapis/java-bigtable/commit/4d6d41988c8e4b92b01851ab7ab52183254e8798))



## February 03, 2025

Feature

Tags data for Bigtable instances is now included in Cloud Billing data, letting you use tagged Bigtable instances to gain visibility into your resource usage and spending. For more information, see [Understand standard and detailed usage cost data](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/standard-usage#usage-cost-export-more-info).

## January 27, 2025

Libraries

### Go

#### [1.35.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.34.0...bigtable/v1.35.0) (2025-01-22)

##### Features

  * **bigtable:** Hot backups ([#11215](https://github.com/googleapis/google-cloud-go/issues/11215)) ([238ac1c](https://github.com/googleapis/google-cloud-go/commit/238ac1c37978b7ccdd72af453416308c511dd493))



##### Bug Fixes

  * **bigtable:** Allow nil condition in conditional mutation ([#11457](https://github.com/googleapis/google-cloud-go/issues/11457)) ([d83bc05](https://github.com/googleapis/google-cloud-go/commit/d83bc05219223027cfaa3fba127c2f03eb554c53))
  * **bigtable:** Do not retry conditional mutate ([#11437](https://github.com/googleapis/google-cloud-go/issues/11437)) ([ce8c9b1](https://github.com/googleapis/google-cloud-go/commit/ce8c9b1e5523646175b9650265928386143259fd))
  * **bigtable:** Mutate groups even after first error ([#11434](https://github.com/googleapis/google-cloud-go/issues/11434)) ([6ffe32b](https://github.com/googleapis/google-cloud-go/commit/6ffe32b76e7228d99e12eeba60a5e719f2d3e5e3))
  * **bigtable:** Retry correct mutations ([#11388](https://github.com/googleapis/google-cloud-go/issues/11388)) ([ca2c4e3](https://github.com/googleapis/google-cloud-go/commit/ca2c4e334f07e7f8f0e276db922122d47262dabf))
  * **bigtable:** Track number of readrows to set rowsLimit in subsequent requests ([#10213](https://github.com/googleapis/google-cloud-go/issues/10213)) ([abb615e](https://github.com/googleapis/google-cloud-go/commit/abb615e240e612540b24b03d95835058045275fc))



## January 20, 2025

Libraries

### Python

#### [2.28.1](https://github.com/googleapis/python-bigtable/compare/v2.28.0...v2.28.1) (2025-01-17)

##### Bug Fixes

  * Allow empty headers for btql routing ([#1072](https://github.com/googleapis/python-bigtable/issues/1072)) ([e7ecfeb](https://github.com/googleapis/python-bigtable/commit/e7ecfeb8984a45c880d9483305964fff347eb4b8))



## January 13, 2025

Libraries

### Python

#### [2.28.0](https://github.com/googleapis/python-bigtable/compare/v2.27.0...v2.28.0) (2025-01-08)

##### Features

  * Add generated sync client ([#1017](https://github.com/googleapis/python-bigtable/issues/1017)) ([f974823](https://github.com/googleapis/python-bigtable/commit/f974823bf8a74c2f8b1bc69997b13bc1acaf8bef))



### Java

#### [2.51.1](https://github.com/googleapis/java-bigtable/compare/v2.51.0...v2.51.1) (2025-01-10)

##### Dependencies

  * Update dependency com.google.cloud:gapic-libraries-bom to v1.50.0 ([#2464](https://github.com/googleapis/java-bigtable/issues/2464)) ([d63dd43](https://github.com/googleapis/java-bigtable/commit/d63dd4333e94f8ad32f260315e44b622db157002))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#2461](https://github.com/googleapis/java-bigtable/issues/2461)) ([ed24b4c](https://github.com/googleapis/java-bigtable/commit/ed24b4c0aebc2666850f103f551128f02c2ba2ae))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#2460](https://github.com/googleapis/java-bigtable/issues/2460)) ([35c979f](https://github.com/googleapis/java-bigtable/commit/35c979fff1d1194cc241f90057245de78cd5f010))



### Java

#### [2.51.1](https://github.com/googleapis/java-bigtable/compare/v2.51.0...v2.51.1) (2025-01-10)

##### Dependencies

  * Update dependency com.google.cloud:gapic-libraries-bom to v1.50.0 ([#2464](https://github.com/googleapis/java-bigtable/issues/2464)) ([d63dd43](https://github.com/googleapis/java-bigtable/commit/d63dd4333e94f8ad32f260315e44b622db157002))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.41.1 ([#2461](https://github.com/googleapis/java-bigtable/issues/2461)) ([ed24b4c](https://github.com/googleapis/java-bigtable/commit/ed24b4c0aebc2666850f103f551128f02c2ba2ae))
  * Update googleapis/sdk-platform-java action to v2.51.1 ([#2460](https://github.com/googleapis/java-bigtable/issues/2460)) ([35c979f](https://github.com/googleapis/java-bigtable/commit/35c979fff1d1194cc241f90057245de78cd5f010))



## January 06, 2025

Libraries

### Go

#### [1.34.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.33.0...bigtable/v1.34.0) (2025-01-02)

##### Features

  * **bigtable/admin:** Add support for Cloud Bigtable Node Scaling Factor for CBT Clusters ([7250d71](https://github.com/googleapis/google-cloud-go/commit/7250d714a638dcd5df3fbe0e91c5f1250c3f80f9))
  * **bigtable:** Add feature flags proto for Direct Access ([2c83297](https://github.com/googleapis/google-cloud-go/commit/2c83297a569117b0252b5b2edaecb09e4924d979))
  * **bigtable:** Async refresh dry run in parallel with sync refresh ([#11066](https://github.com/googleapis/google-cloud-go/issues/11066)) ([169e309](https://github.com/googleapis/google-cloud-go/commit/169e3096150599899788169368f96ce4470e5599))



##### Bug Fixes

  * **bigtable:** Correct the 'method' label value ([#11350](https://github.com/googleapis/google-cloud-go/issues/11350)) ([6aa27dc](https://github.com/googleapis/google-cloud-go/commit/6aa27dc79046df09e34e93044dbfe47cb3e9aa54))
  * **bigtable:** Resolve discrepancy between server and client qps ([#11224](https://github.com/googleapis/google-cloud-go/issues/11224)) ([c500179](https://github.com/googleapis/google-cloud-go/commit/c500179e771ac45ca3c2f5f7939444c8f65eafd3))
  * **bigtable:** Update golang.org/x/net to v0.33.0 ([e9b0b69](https://github.com/googleapis/google-cloud-go/commit/e9b0b69644ea5b276cacff0a707e8a5e87efafc9))
  * **bigtable:** Update google.golang.org/api to v0.203.0 ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))
  * **bigtable:** WARNING: On approximately Dec 1, 2024, an update to Protobuf will change service registration function signatures to use an interface instead of a concrete type in generated .pb.go files. This change is expected to affect very few if any users of this client library. For more information, see https://togithub.com/googleapis/google-cloud-go/issues/11020. ([8bb87d5](https://github.com/googleapis/google-cloud-go/commit/8bb87d56af1cba736e0fe243979723e747e5e11e))



##### Documentation

  * **bigtable:** Add todos ([#11280](https://github.com/googleapis/google-cloud-go/issues/11280)) ([d4f2449](https://github.com/googleapis/google-cloud-go/commit/d4f2449c5c2192b49de2bb42c7027beffb7517a2))
  * **bigtable:** Adding shut down log ([#11293](https://github.com/googleapis/google-cloud-go/issues/11293)) ([6cf33a8](https://github.com/googleapis/google-cloud-go/commit/6cf33a8d5605f37c1666de2c4e49554ec8fcc1a1))



## December 23, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.51.0](https://github.com/googleapis/java-bigtable/compare/v2.50.0...v2.51.0) (2024-12-17)

##### Features

  * Introduce `java.time` ([#2415](https://github.com/googleapis/java-bigtable/issues/2415)) ([bb96c3e](https://github.com/googleapis/java-bigtable/commit/bb96c3e395793ba324cf658bb4c985d4315cf781))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.51.0 ([a5444a5](https://github.com/googleapis/java-bigtable/commit/a5444a545ec61a1520716dfafb6f62b7e39df1c7))
  * Move resource detection to the first export to avoid slow start ([#2450](https://github.com/googleapis/java-bigtable/issues/2450)) ([cec010a](https://github.com/googleapis/java-bigtable/commit/cec010aa64f2b190f8e742915be41baae2ad2083))



##### Dependencies

  * Update sdk-platform-java dependencies ([#2448](https://github.com/googleapis/java-bigtable/issues/2448)) ([825e717](https://github.com/googleapis/java-bigtable/commit/825e717e9d8ae3853d7509d0849b58f2c47c9803))



## December 18, 2024

Feature

You can now enable [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling) when you create a new Bigtable cluster. This cluster configuration lets Bigtable treat two standard nodes as a larger, single compute node, and the cluster is always scaled in increments of two nodes. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Change

The [Preview](https://cloud.google.com/products#product-launch-stages) of Bigtable automated backup has been expanded to let you configure the backup retention period in automated backup policies, and the default is now seven days. For more information, see [Update an automated backup policy](https://docs.cloud.google.com/bigtable/docs/managing-backups#update-automated-backup).

## December 17, 2024

Feature

You can use Organization Policy Service custom constraints to manage specific operations on Bigtable resources. For more information, see [Use custom organization policies](https://docs.cloud.google.com/bigtable/docs/custom-constraints). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## December 16, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.50.0](https://github.com/googleapis/java-bigtable/compare/v2.49.0...v2.50.0) (2024-12-06)

##### Features

  * Add support for Row Affinity app profiles ([#2341](https://github.com/googleapis/java-bigtable/issues/2341)) ([cb4d60e](https://github.com/googleapis/java-bigtable/commit/cb4d60e8ce2079a270739ad91efb05cbb1ff74f8))



## December 12, 2024

Feature

Bigtable is now supported by Database Center, which is in [Preview](https://cloud.google.com/products#product-launch-stages). Database Center is an AI-assisted dashboard that gives you one centralized view across your entire database fleet. With this release, Database Center displays health issues for Bigtable availability and data protection. For more information, see [Database health issues](https://docs.cloud.google.com/database-center/docs/database-health-issues).

## December 11, 2024

Feature

You can now enable [row-affinity routing](https://docs.cloud.google.com/bigtable/docs/routing#row-affinity) to let Bigtable automatically ensure that single-row requests for a given row are routed to the same cluster. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

You can now use the Google Cloud console to [create and manage authorized views](https://docs.cloud.google.com/bigtable/docs/authorized-views-create-manage) of your Bigtable tables.

Announcement

You can now select a row in a Bigtable Studio query results table to view formatted row data. For more information, see [Query your data with SQL in the query editor](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console#query-editor).

## December 09, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.49.0](https://github.com/googleapis/java-bigtable/compare/v2.48.0...v2.49.0) (2024-12-03)

##### Features

  * Add support for table deletion protection ([#2430](https://github.com/googleapis/java-bigtable/issues/2430)) ([687b6df](https://github.com/googleapis/java-bigtable/commit/687b6df14b743358e8207cda26022dfc75338d55))



##### Bug Fixes

  * Allow factory to export to different projects ([#2374](https://github.com/googleapis/java-bigtable/issues/2374)) ([06b912c](https://github.com/googleapis/java-bigtable/commit/06b912cc5d63436757008e79edfa8286b2ccac18))
  * Send priming requests on the channel directly ([#2435](https://github.com/googleapis/java-bigtable/issues/2435)) ([b76698d](https://github.com/googleapis/java-bigtable/commit/b76698dfb2c8552185f34e01e924ecc80798ba4f))



## December 02, 2024

Change

To create a Bigtable instance, a user or account must be a principal in a role with the permission `bigtable.clusters.create`. For more information, see [Bigtable access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

## November 25, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.48.0](https://github.com/googleapis/java-bigtable/compare/v2.47.0...v2.48.0) (2024-11-19)

##### Features

  * Enable trailer optimization by default ([#2421](https://github.com/googleapis/java-bigtable/issues/2421)) ([7b2c4e4](https://github.com/googleapis/java-bigtable/commit/7b2c4e45dce828f506dac16ffc2b71995564a477))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.50.0 ([6b35b47](https://github.com/googleapis/java-bigtable/commit/6b35b478e10efce77d95bffcd7a64e84e1bcc5b0))
  * Make client side metrics tag in sync with server ([#2401](https://github.com/googleapis/java-bigtable/issues/2401)) ([bba4183](https://github.com/googleapis/java-bigtable/commit/bba41837febc10e9507afc7117e2e4ec2d15fb11))



##### Dependencies

  * Revert downgrade grpc to 1.67.1 [#2366](https://github.com/googleapis/java-bigtable/issues/2366) ([#2414](https://github.com/googleapis/java-bigtable/issues/2414)) ([710fa52](https://github.com/googleapis/java-bigtable/commit/710fa52a05ce4fc81ee8e980d87e0ca86676219f))
  * Update dependency com.google.cloud:gapic-libraries-bom to v1.48.0 ([#2422](https://github.com/googleapis/java-bigtable/issues/2422)) ([2088a39](https://github.com/googleapis/java-bigtable/commit/2088a399bd8b71e98035cc475637f41d5873082d))
  * Update sdk-platform-java dependencies ([#2418](https://github.com/googleapis/java-bigtable/issues/2418)) ([c12bb01](https://github.com/googleapis/java-bigtable/commit/c12bb01a6c5be0a72285db0505407f3e1c2534fb))



## November 18, 2024

Feature

You can now create a Data Boost app profile and view Data Boost metrics in the Google Cloud console. Data Boost for Bigtable is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Create and configure app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles).

Feature

Bigtable is now available in the `northamerica-south1` (Mexico) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.47.0](https://github.com/googleapis/java-bigtable/compare/v2.46.0...v2.47.0) (2024-11-13)

##### Features

  * Add an experimental feature to skip waiting for trailers for unary ops ([#2404](https://github.com/googleapis/java-bigtable/issues/2404)) ([cf58f26](https://github.com/googleapis/java-bigtable/commit/cf58f260fd7d3cb0dee4fee8e2d43367db6eadb1))
  * Add internal "deadline remaining" client side metric [#2341](https://github.com/googleapis/java-bigtable/issues/2341) ([#2370](https://github.com/googleapis/java-bigtable/issues/2370)) ([75d4105](https://github.com/googleapis/java-bigtable/commit/75d4105e0376dbe5810d6b96d71daa74b85e68ce))



##### Bug Fixes

  * Simplify remaining deadline metric impl ([#2410](https://github.com/googleapis/java-bigtable/issues/2410)) ([9796d57](https://github.com/googleapis/java-bigtable/commit/9796d57b60d928d3390e4ad311d5704dcbe808ec))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.27.0](https://github.com/googleapis/python-bigtable/compare/v2.26.0...v2.27.0) (2024-11-12)

##### Features

  * Add support for Cloud Bigtable Node Scaling Factor for CBT Clusters ([#1023](https://github.com/googleapis/python-bigtable/issues/1023)) ([0809c6a](https://github.com/googleapis/python-bigtable/commit/0809c6ac274e909103ad160a8bcab95f8bb46f31))
  * Surface `retry` param to `Table.read_row` api ([#982](https://github.com/googleapis/python-bigtable/issues/982)) ([a8286d2](https://github.com/googleapis/python-bigtable/commit/a8286d2a510f654f9c270c3c761c02e4ab3817d4))



##### Bug Fixes

  * Registering duplicate instance ([#1033](https://github.com/googleapis/python-bigtable/issues/1033)) ([2bca8fb](https://github.com/googleapis/python-bigtable/commit/2bca8fb220eeb1906fc6a3cf1f879f3d41fbbff8))



## November 04, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.46.0](https://github.com/googleapis/java-bigtable/compare/v2.45.1...v2.46.0) (2024-10-29)

##### Features

  * Test proxy support SSL backend ([#2381](https://github.com/googleapis/java-bigtable/issues/2381)) ([3cbf4ab](https://github.com/googleapis/java-bigtable/commit/3cbf4abe79d61daba0704abfccfb5558b026e6b7))



##### Bug Fixes

  * Fix client blocking latency ([#2346](https://github.com/googleapis/java-bigtable/issues/2346)) ([3801961](https://github.com/googleapis/java-bigtable/commit/380196174fb9b8cd97beb79d4faf49b30561be7f))
  * Fix first response latencies ([#2382](https://github.com/googleapis/java-bigtable/issues/2382)) ([8b2953e](https://github.com/googleapis/java-bigtable/commit/8b2953ed9c69c23b3e0c5c35d0538dc83f9dad80))



##### Dependencies

  * Update sdk-platform-java dependencies ([#2384](https://github.com/googleapis/java-bigtable/issues/2384)) ([81d7215](https://github.com/googleapis/java-bigtable/commit/81d72150b60d29e4e2ac17c6cb1fbdc89be0e16e))



## October 21, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.45.1](https://github.com/googleapis/java-bigtable/compare/v2.45.0...v2.45.1) (2024-10-14)

##### Dependencies

  * Update sdk-platform-java dependencies ([#2378](https://github.com/googleapis/java-bigtable/issues/2378)) ([2499a3c](https://github.com/googleapis/java-bigtable/commit/2499a3cd5e0d0404666c7f9cf0c74f9edb90d894))
  * **deps:** Update the Java code generator (gapic-generator-java) to 2.47.0 ([cdc2cc7](https://github.com/googleapis/java-bigtable/commit/cdc2cc7e085af42a2078373098b5f8ef8c752ea7))



## October 08, 2024

Feature

Hot backups, optimized backups to restore your data to production performance availability more efficiently, are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Backups overview](https://docs.cloud.google.com/bigtable/docs/backups).

## October 07, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.45.0](https://github.com/googleapis/java-bigtable/compare/v2.44.1...v2.45.0) (2024-10-03)

##### Features

  * Add support for Cloud Bigtable Node Scaling Factor for CBT Clusters ([caf879c](https://github.com/googleapis/java-bigtable/commit/caf879cb4086d74bd4571662510014b27e6113a7))



##### Bug Fixes

  * **deps:** Update the Java code generator (gapic-generator-java) to 2.46.1 ([caf879c](https://github.com/googleapis/java-bigtable/commit/caf879cb4086d74bd4571662510014b27e6113a7))
  * Support override monitoring endpoint ([#2364](https://github.com/googleapis/java-bigtable/issues/2364)) ([a341eb8](https://github.com/googleapis/java-bigtable/commit/a341eb8530d959edabac0282c52c3e928abf733d))



##### Dependencies

  * Downgrade grpc to 1.67.1 ([#2366](https://github.com/googleapis/java-bigtable/issues/2366)) ([1baecb3](https://github.com/googleapis/java-bigtable/commit/1baecb3f6cd34a1daab632c322a1fb415efb9895))
  * Update dependency com.google.cloud:gapic-libraries-bom to v1.45.0 ([#2363](https://github.com/googleapis/java-bigtable/issues/2363)) ([9d24c45](https://github.com/googleapis/java-bigtable/commit/9d24c45b389f2edef0b02f6a8c3badbca2fd3946))



## September 30, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.44.1](https://github.com/googleapis/java-bigtable/compare/v2.44.0...v2.44.1) (2024-09-26)

##### Bug Fixes

  * Add RetryCallable to the callable chain ([#2348](https://github.com/googleapis/java-bigtable/issues/2348)) ([0330d77](https://github.com/googleapis/java-bigtable/commit/0330d77ac29d47e8610ddd23c324a55d1f9912cb))
  * Pass deadline through ExecuteQuery RetrySettings ([#2355](https://github.com/googleapis/java-bigtable/issues/2355)) ([6bc9820](https://github.com/googleapis/java-bigtable/commit/6bc98202897cebe09be8a4a78316cf5463106866))
  * Time based flakiness in execute query deadline test ([#2358](https://github.com/googleapis/java-bigtable/issues/2358)) ([b474173](https://github.com/googleapis/java-bigtable/commit/b474173a778cba273d2713e667000c5633de75bd))



##### Dependencies

  * Update dependency com.google.cloud:sdk-platform-java-config to v3.36.1 ([#2351](https://github.com/googleapis/java-bigtable/issues/2351)) ([40c428e](https://github.com/googleapis/java-bigtable/commit/40c428ec8e8cccb4dc3bb10d6674c94e9527e797))



## September 25, 2024

Announcement

You can perform [similarity vector search in Bigtable](https://docs.cloud.google.com/bigtable/docs/find-k-nearest-neighbors) by finding the K-nearest neighbors. This feature is available as part of the [GoogleSQL for Bigtable Preview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview).

## September 23, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.44.0](https://github.com/googleapis/java-bigtable/compare/v2.43.0...v2.44.0) (2024-09-16)

##### Features

  * Add APIs to enable hot backups ([#2313](https://github.com/googleapis/java-bigtable/issues/2313)) ([6d004cd](https://github.com/googleapis/java-bigtable/commit/6d004cd0809d02eeff05d5e90faf5e145f13d11e))
  * Add support for awaiting Data Boost ([#2329](https://github.com/googleapis/java-bigtable/issues/2329)) ([8556574](https://github.com/googleapis/java-bigtable/commit/85565742645537d1b55a1a52521d2ccf44b4d00c))



##### Dependencies

  * Update shared dependencies ([#2337](https://github.com/googleapis/java-bigtable/issues/2337)) ([dc65bd5](https://github.com/googleapis/java-bigtable/commit/dc65bd5a39cfe0c25a6b955f9f4d9367df334211))



## August 28, 2024

Feature

The [Preview](https://cloud.google.com/products#product-launch-stages) of Data Boost for Bigtable has been expanded to let you use Data Boost compute resources when you read Bigtable data using a Spark application. For more information, see [Use the Bigtable Spark connector](https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector#compute).

## August 26, 2024

Feature

You can use `EXPORT DATA` statements to [directly export BigQuery data to Bigtable (reverse ETL)](https://docs.cloud.google.com/bigquery/docs/export-to-bigtable). This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.43.0](https://github.com/googleapis/java-bigtable/compare/v2.42.0...v2.43.0) (2024-08-22)

##### Features

  * Add fields and the BackupType proto for Hot Backups ([#2300](https://github.com/googleapis/java-bigtable/issues/2300)) ([acaa3ff](https://github.com/googleapis/java-bigtable/commit/acaa3ff26ab0d317362e2be65ac5edcf803b13a1))
  * Allow non default service account in DirectPath ([#2312](https://github.com/googleapis/java-bigtable/issues/2312)) ([09d0f23](https://github.com/googleapis/java-bigtable/commit/09d0f23032488dfa55c7a4c1c571a4f36bd94728))
  * **bigtable:** Remove deprecated Bytes from BigEndianBytesEncoding ([#2309](https://github.com/googleapis/java-bigtable/issues/2309)) ([32f244f](https://github.com/googleapis/java-bigtable/commit/32f244f13d0c8571654d314310a4756fe275d609))
  * Enable hermetic library generation ([#2234](https://github.com/googleapis/java-bigtable/issues/2234)) ([169aea5](https://github.com/googleapis/java-bigtable/commit/169aea5c43485a8d13ed53f57495609c142944df))



##### Bug Fixes

  * Add missing call to EqualsTester#testEquals ([#2307](https://github.com/googleapis/java-bigtable/issues/2307)) ([8b49f9c](https://github.com/googleapis/java-bigtable/commit/8b49f9ce84871f0f423f5837785604c3119ccd88))



##### Dependencies

  * Update shared dependencies ([#2314](https://github.com/googleapis/java-bigtable/issues/2314)) ([ab392ee](https://github.com/googleapis/java-bigtable/commit/ab392ee8d0c4535b5d3f31b3e111cbc41b399dd9))



## August 19, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.26.0](https://github.com/googleapis/python-bigtable/compare/v2.25.0...v2.26.0) (2024-08-12)

##### Features

  * Add fields and the BackupType proto for Hot Backups ([#1010](https://github.com/googleapis/python-bigtable/issues/1010)) ([b95801f](https://github.com/googleapis/python-bigtable/commit/b95801ffa8081e0072232247fbc5879105c109a6))
  * Add MergeToCell to Mutation APIs ([f029a24](https://github.com/googleapis/python-bigtable/commit/f029a242e2b0e6020d0b87ef256a414194321fad))
  * Add min, max, hll aggregators and more types ([f029a24](https://github.com/googleapis/python-bigtable/commit/f029a242e2b0e6020d0b87ef256a414194321fad))
  * Async execute query client ([#1011](https://github.com/googleapis/python-bigtable/issues/1011)) ([45bc8c4](https://github.com/googleapis/python-bigtable/commit/45bc8c4a0fe567ce5e0126a1a70e7eb3dca93e92))



##### Bug Fixes

  * Use single routing metadata header ([#1005](https://github.com/googleapis/python-bigtable/issues/1005)) ([20eeb0a](https://github.com/googleapis/python-bigtable/commit/20eeb0a68d7b44d07a6d84bc7a7e040ad63bb96d))



##### Documentation

  * Add clarification around SQL timestamps ([#1012](https://github.com/googleapis/python-bigtable/issues/1012)) ([6e80190](https://github.com/googleapis/python-bigtable/commit/6e801900bbe9385d3b579b8c3327c87c3617d92f))
  * Corrected various type documentation ([f029a24](https://github.com/googleapis/python-bigtable/commit/f029a242e2b0e6020d0b87ef256a414194321fad))



## August 13, 2024

Announcement

You can now enable client-side metrics with the Bigtable client library for Go. Used in conjunction with server-side monitoring metrics, client-side metrics can provide a complete, actionable view of Bigtable performance. For more information, see [Set up client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics-setup).

## August 12, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.42.0](https://github.com/googleapis/java-bigtable/compare/v2.41.0...v2.42.0) (2024-08-06)

##### Features

  * Support float32, float64, and array type query params ([#2297](https://github.com/googleapis/java-bigtable/issues/2297)) ([a65640e](https://github.com/googleapis/java-bigtable/commit/a65640e285950d02136544bac913b2852cfe0274))



##### Bug Fixes

  * Adapt toString tests to introduction of java.time in gax ([93f66a7](https://github.com/googleapis/java-bigtable/commit/93f66a70371f8095fd5c001a977d71e5622be46d))



##### Dependencies

  * Update shared dependencies ([93f66a7](https://github.com/googleapis/java-bigtable/commit/93f66a70371f8095fd5c001a977d71e5622be46d))



## August 01, 2024

Feature

Bigtable supports querying in **SQL**. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Introduction to SQL for Bigtable](https://docs.cloud.google.com/bigtable/docs/introduction-sql).

Feature

The Bigtable Studio **query editor** is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).

Feature

Bigtable aggregates let you build **distributed counters** and aggregate your Bigtable data at write time using min, max, sum, or HLL. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Aggregate values at write time](https://docs.cloud.google.com/bigtable/docs/aggregates).

## July 29, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [5.1.2](https://github.com/googleapis/nodejs-bigtable/compare/v5.1.1...v5.1.2) (2024-07-22)

##### Bug Fixes

  * Throw away excess data in order to avoid delivering duplicate data ([#1453](https://github.com/googleapis/nodejs-bigtable/issues/1453)) ([069239d](https://github.com/googleapis/nodejs-bigtable/commit/069239dce83498293e86851d37ad5943b5d919da))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.41.0](https://github.com/googleapis/java-bigtable/compare/v2.40.0...v2.41.0) (2024-07-24)

##### Features

  * Add MergeToCell to Mutation APIs ([#2279](https://github.com/googleapis/java-bigtable/issues/2279)) ([0ce8a2a](https://github.com/googleapis/java-bigtable/commit/0ce8a2a38703233da58208655f41f6e81e03576e))
  * Add support for MergeToCell API ([#2258](https://github.com/googleapis/java-bigtable/issues/2258)) ([191d15c](https://github.com/googleapis/java-bigtable/commit/191d15c5284dbb702e11669931272877bf05f44e))
  * Add support for new functions ([#2287](https://github.com/googleapis/java-bigtable/issues/2287)) ([dd6583a](https://github.com/googleapis/java-bigtable/commit/dd6583a22504385b7a1f7dc91b3bc3d2500ea0c5))
  * Create new environment variable to toggle directpath scoped to cloud bigtable. ([#2261](https://github.com/googleapis/java-bigtable/issues/2261)) ([9062944](https://github.com/googleapis/java-bigtable/commit/9062944610277eb7ae77f395dc79ce94239c5bee))
  * Implement ExecuteQuery API for SQL support ([#2280](https://github.com/googleapis/java-bigtable/issues/2280)) ([25218e8](https://github.com/googleapis/java-bigtable/commit/25218e8cc46f9a51d4b6515afdb8931e574b0bb1))



##### Dependencies

  * Update dependency com.google.truth.extensions:truth-proto-extension to v1.4.4 ([#2282](https://github.com/googleapis/java-bigtable/issues/2282)) ([d00a9e0](https://github.com/googleapis/java-bigtable/commit/d00a9e01b2b329f3bae50f48a15692d87ad0f3bf))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.25.0](https://github.com/googleapis/python-bigtable/compare/v2.24.0...v2.25.0) (2024-07-18)

##### Features

  * Publish ProtoRows Message ([7ac8e14](https://github.com/googleapis/python-bigtable/commit/7ac8e142f99a6891b6bc286858f764def503e89a))
  * Publish the Cloud Bigtable ExecuteQuery API ([7ac8e14](https://github.com/googleapis/python-bigtable/commit/7ac8e142f99a6891b6bc286858f764def503e89a))



##### Bug Fixes

  * Allow protobuf 5.x ([7ac8e14](https://github.com/googleapis/python-bigtable/commit/7ac8e142f99a6891b6bc286858f764def503e89a))



## July 25, 2024

Feature

The [Preview](https://cloud.google.com/products#product-launch-stages) of automated backup has been expanded to let you enable and disable automated backup in the Google Cloud console. For more information, see the [automated backup](https://docs.cloud.google.com/bigtable/docs/managing-backups#use-automated-backup) documentation.

## July 15, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [5.1.1](https://github.com/googleapis/nodejs-bigtable/compare/v5.1.0...v5.1.1) (2024-07-11)

##### Bug Fixes

  * Ensure that during resumption of a scan, rows that have not been observed by the caller are re-requested ([#1444](https://github.com/googleapis/nodejs-bigtable/issues/1444)) ([2d8de32](https://github.com/googleapis/nodejs-bigtable/commit/2d8de3247595a08c5cd0f7b42a59eb44dd255797))
  * Remove custom readrows retry logic and rely on gax for retries ([#1422](https://github.com/googleapis/nodejs-bigtable/issues/1422)) ([3e0a46e](https://github.com/googleapis/nodejs-bigtable/commit/3e0a46e1a9bf68ac8f4b74f9a202291d00681074))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.40.0](https://github.com/googleapis/java-bigtable/compare/v2.39.5...v2.40.0) (2024-06-28)

##### Features

  * Add String type with Utf8Raw encoding to Bigtable API ([#2191](https://github.com/googleapis/java-bigtable/issues/2191)) ([e7f03fc](https://github.com/googleapis/java-bigtable/commit/e7f03fc7d252a7ff6c76a8e6e0a9e6ad3dcbd9d5))



##### Bug Fixes

  * Add getServiceName() to EnhancedBigTableStubSettings ([#2256](https://github.com/googleapis/java-bigtable/issues/2256)) ([da703db](https://github.com/googleapis/java-bigtable/commit/da703db25f6702b263dbd8ded0cb0fd3422efe31))
  * Remove grpclb ([#2033](https://github.com/googleapis/java-bigtable/issues/2033)) ([7355375](https://github.com/googleapis/java-bigtable/commit/735537571a147bfdd2a986664ff7905c8f5dc3db))



##### Dependencies

  * Update dependency com.google.truth.extensions:truth-proto-extension to v1.4.3 ([#2268](https://github.com/googleapis/java-bigtable/issues/2268)) ([4573220](https://github.com/googleapis/java-bigtable/commit/45732201880a13eeced3d0332bd172aae0f73dbe))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.10.3 ([#2269](https://github.com/googleapis/java-bigtable/issues/2269)) ([69fef96](https://github.com/googleapis/java-bigtable/commit/69fef968937f4d2e4cc479279a09d7b0bed6c5a2))
  * Update shared dependencies ([#2265](https://github.com/googleapis/java-bigtable/issues/2265)) ([61014ca](https://github.com/googleapis/java-bigtable/commit/61014ca89318743cf0cc0bae97a7f875bc5243ab))



## June 17, 2024

Feature

The Python client library for Bigtable now offers an asynchronous API for use with asynchronous applications. The async API is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). To get started, see the [Python hello world](https://docs.cloud.google.com/bigtable/docs/samples-python-hello).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.39.5](https://github.com/googleapis/java-bigtable/compare/v2.39.4...v2.39.5) (2024-06-10)

##### Bug Fixes

  * Make change stream unknown mod error more actionable ([#1938](https://github.com/googleapis/java-bigtable/issues/1938)) ([e7ba045](https://github.com/googleapis/java-bigtable/commit/e7ba045967e837129adcf979ac13cd9097fab56c))
  * Rate limiting should be ineffective when RateLimitInfo is not present ([#2243](https://github.com/googleapis/java-bigtable/issues/2243)) ([a0ec901](https://github.com/googleapis/java-bigtable/commit/a0ec901a84d8d5a2729772d165e2b305d4663824))



##### Dependencies

  * Update shared dependencies ([#2252](https://github.com/googleapis/java-bigtable/issues/2252)) ([0131eb3](https://github.com/googleapis/java-bigtable/commit/0131eb33d09f0c4cb7b4984efed257f6d72b0100))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.24.0](https://github.com/googleapis/python-bigtable/compare/v2.23.1...v2.24.0) (2024-06-11)

##### Features

  * Add String type with Utf8Raw encoding to Bigtable API ([#968](https://github.com/googleapis/python-bigtable/issues/968)) ([2a2bbfd](https://github.com/googleapis/python-bigtable/commit/2a2bbfdba6737c508ab1073d37fef680ca2a8c2f))
  * Improve async sharding ([#977](https://github.com/googleapis/python-bigtable/issues/977)) ([fd1f7da](https://github.com/googleapis/python-bigtable/commit/fd1f7dafd38f7f0e714a3384a27176f485523682))



##### Bug Fixes

  * **backup:** Backup name regex ([#970](https://github.com/googleapis/python-bigtable/issues/970)) ([6ef122a](https://github.com/googleapis/python-bigtable/commit/6ef122ad49f43e3a22cde5cb6fdaefd947670136))
  * Improve rowset revision ([#979](https://github.com/googleapis/python-bigtable/issues/979)) ([da27527](https://github.com/googleapis/python-bigtable/commit/da275279a7e619e4cd3e72b10ac629d6e0e1fe47))



## June 10, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [5.1.0](https://github.com/googleapis/nodejs-bigtable/compare/v5.0.0...v5.1.0) (2024-05-28)

##### Features

  * Add feature for copying backups ([#1153](https://github.com/googleapis/nodejs-bigtable/issues/1153)) ([91f85b5](https://github.com/googleapis/nodejs-bigtable/commit/91f85b53340b9bf0bfb4620a4027333890030efe))
  * Add String type with Utf8Raw encoding to Bigtable API ([#1419](https://github.com/googleapis/nodejs-bigtable/issues/1419)) ([724b711](https://github.com/googleapis/nodejs-bigtable/commit/724b7118972e6697e3fd648b5d6ce2d047ab2b6a))
  * Publish Automated Backups protos ([#1391](https://github.com/googleapis/nodejs-bigtable/issues/1391)) ([17838ed](https://github.com/googleapis/nodejs-bigtable/commit/17838eda19b001e322765c33a83a756eeeb68963))
  * Trusted Private Cloud support, use the universeDomain parameter ([#1386](https://github.com/googleapis/nodejs-bigtable/issues/1386)) ([c0c287e](https://github.com/googleapis/nodejs-bigtable/commit/c0c287e2d386758609f57f3efee78b18fc9d8b7d))



##### Bug Fixes

  * **deps:** Update dependency @google-cloud/precise-date to v4 ([#1318](https://github.com/googleapis/nodejs-bigtable/issues/1318)) ([9dcef90](https://github.com/googleapis/nodejs-bigtable/commit/9dcef901b0cc7a52afb4c3f85622bd08e67d7429))
  * Extend timeouts for deleting snapshots, backups and tables ([#1387](https://github.com/googleapis/nodejs-bigtable/issues/1387)) ([1a6f59a](https://github.com/googleapis/nodejs-bigtable/commit/1a6f59afd238ccda4427251cbe0c71c8db37568e))
  * Fix flaky test by extending timeout ([#1350](https://github.com/googleapis/nodejs-bigtable/issues/1350)) ([906ac79](https://github.com/googleapis/nodejs-bigtable/commit/906ac796e3aaf724d00607854162bdefedcee96d))
  * Improve retry logic for streaming API calls ([#1372](https://github.com/googleapis/nodejs-bigtable/issues/1372)) ([e8083a4](https://github.com/googleapis/nodejs-bigtable/commit/e8083a4c71e0523e196911fbf6262ff8fe6272de))
  * Remove the watermarks ([#1313](https://github.com/googleapis/nodejs-bigtable/issues/1313)) ([0126a0e](https://github.com/googleapis/nodejs-bigtable/commit/0126a0ea1e4b6a845acb4e5600ddb3082443d310))



## June 03, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.39.4](https://github.com/googleapis/java-bigtable/compare/v2.39.3...v2.39.4) (2024-05-28)

##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.10.2 ([#2236](https://github.com/googleapis/java-bigtable/issues/2236)) ([2609103](https://github.com/googleapis/java-bigtable/commit/26091035ed42cfd2945092d0c909dbf9bb6fae28))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.2 ([#2237](https://github.com/googleapis/java-bigtable/issues/2237)) ([6728931](https://github.com/googleapis/java-bigtable/commit/6728931ca904e2a2fb53f7b9e9115a9c3edd38df))
  * Update shared dependencies ([#2235](https://github.com/googleapis/java-bigtable/issues/2235)) ([8d38150](https://github.com/googleapis/java-bigtable/commit/8d3815023f7fa1c8103cb8ab02d8f71cd8a7a85e))



## May 27, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.39.3](https://github.com/googleapis/java-bigtable/compare/v2.39.2...v2.39.3) (2024-05-21)

##### Bug Fixes

  * Retry INTERNAL retriable auth errors ([#2239](https://github.com/googleapis/java-bigtable/issues/2239)) ([4cdb6da](https://github.com/googleapis/java-bigtable/commit/4cdb6da8920cd3346a9d79d67432cef588d93bb0))



## May 13, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.39.2](https://github.com/googleapis/java-bigtable/compare/v2.39.1...v2.39.2) (2024-05-09)

##### Dependencies

  * Update shared dependencies ([#2221](https://github.com/googleapis/java-bigtable/issues/2221)) ([17f7a9a](https://github.com/googleapis/java-bigtable/commit/17f7a9af3991c4744256bbfb0533d9390cada23d))



#### [2.39.1](https://github.com/googleapis/java-bigtable/compare/v2.39.0...v2.39.1) (2024-05-08)

##### Bug Fixes

  * Batch time series data when exporting client-side metric ([#2222](https://github.com/googleapis/java-bigtable/issues/2222)) ([1f9f169](https://github.com/googleapis/java-bigtable/commit/1f9f1698339ae470d821963e1037e0132016d216))
  * Remove stale module from bom ([#2218](https://github.com/googleapis/java-bigtable/issues/2218)) ([7145864](https://github.com/googleapis/java-bigtable/commit/7145864868b3f7df69f9b2db7a822f9faf903f33))



## May 06, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.39.0](https://github.com/googleapis/java-bigtable/compare/v2.38.0...v2.39.0) (2024-04-29)

##### Features

  * Admin API changes for Data Boost ([#2181](https://github.com/googleapis/java-bigtable/issues/2181)) ([3b1886b](https://github.com/googleapis/java-bigtable/commit/3b1886bea79525505e41124b41985f37c490c97e))



##### Dependencies

  * Update dependency com.google.cloud:gapic-libraries-bom to v1.36.0 ([#2215](https://github.com/googleapis/java-bigtable/issues/2215)) ([5a9259e](https://github.com/googleapis/java-bigtable/commit/5a9259e3c861f1ed13c84e0bb024ddda3e1dc147))
  * Update shared dependencies ([#2190](https://github.com/googleapis/java-bigtable/issues/2190)) ([3f37d8d](https://github.com/googleapis/java-bigtable/commit/3f37d8da8b51a3fea56d1c462b9500ee2c244973))



## May 02, 2024

Feature

The [Bigtable Spark connector](https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector) lets you read and write data from and to Bigtable using Spark SQL and DataFrames inside your Spark application. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## April 22, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.38.0](https://github.com/googleapis/java-bigtable/compare/v2.37.0...v2.38.0) (2024-04-15)

##### Features

  * Add Data Boost configurations to admin API ([f29c5bb](https://github.com/googleapis/java-bigtable/commit/f29c5bba08daffe2721454db1714f6ea6f47fc66))
  * Add feature flag for client side metrics ([#2179](https://github.com/googleapis/java-bigtable/issues/2179)) ([f29c5bb](https://github.com/googleapis/java-bigtable/commit/f29c5bba08daffe2721454db1714f6ea6f47fc66))
  * Migrate to OTEL and enable metrics by default ([#2166](https://github.com/googleapis/java-bigtable/issues/2166)) ([1682939](https://github.com/googleapis/java-bigtable/commit/168293937cc7f438a3ec2dee46805aa8e12089c4))



##### Bug Fixes

  * Add more error handling ([#2203](https://github.com/googleapis/java-bigtable/issues/2203)) ([c2a63f7](https://github.com/googleapis/java-bigtable/commit/c2a63f7627f2aa6e2e51ec3e185abfa5234ad3e4))
  * Fix export to log detect resource errors ([#2197](https://github.com/googleapis/java-bigtable/issues/2197)) ([d32fbb7](https://github.com/googleapis/java-bigtable/commit/d32fbb78bbde2ad04103ab7b2c1176a6df72d0a3))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.23.1](https://github.com/googleapis/python-bigtable/compare/v2.23.0...v2.23.1) (2024-04-15)

##### Bug Fixes

  * Use insecure grpc channel with emulator ([#946](https://github.com/googleapis/python-bigtable/issues/946)) ([aa31706](https://github.com/googleapis/python-bigtable/commit/aa3170663f9bd09d70c99d4e76c07f7f293ad935))



## April 16, 2024

Change

[Client-side metrics](https://docs.cloud.google.com/bigtable/docs/client-side-metrics) are enabled by default in the Bigtable client library for Java versions 2.38.0 and later.

## April 11, 2024

Feature

Bigtable now integrates with LangChain, an LLM orchestration framework. For more information, see [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/bigtable/docs/langchain). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 09, 2024

Feature

[Bigtable Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview), a serverless compute service designed for high-throughput read jobs and queries, is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

You can control access to data in your Bigtable tables with [authorized views](https://docs.cloud.google.com/bigtable/docs/authorized-views). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

Bigtable app profiles let you [configure request priorities](https://docs.cloud.google.com/bigtable/docs/request-priorities) to prioritize certain workload data requests over others. This feature is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

You can now build distributed counters with Bigtable with write-time [aggregates](https://docs.cloud.google.com/bigtable/docs/aggregates). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Change

Bigtable now lets you increase the retention period in the garbage collection policy for a column family in a replicated table. For more information, see [Changing age-based garbage collection policies](https://docs.cloud.google.com/bigtable/docs/garbage-collection#change-age-based).

## April 01, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.37.0](https://github.com/googleapis/java-bigtable/compare/v2.36.0...v2.37.0) (2024-03-27)

##### Features

  * Add admin APIs for AuthorizedView ([#2175](https://github.com/googleapis/java-bigtable/issues/2175)) ([13d1df3](https://github.com/googleapis/java-bigtable/commit/13d1df3910e3041b57485a09317f717932b21727))
  * Support AuthorizedView in bigtable data client ([#2177](https://github.com/googleapis/java-bigtable/issues/2177)) ([4b255d0](https://github.com/googleapis/java-bigtable/commit/4b255d0160b0ea30a4ab6453ccae278f40d32ee2))



##### Bug Fixes

  * Update the accounting of partial batch mutations ([#2149](https://github.com/googleapis/java-bigtable/issues/2149)) ([4158094](https://github.com/googleapis/java-bigtable/commit/4158094c34c85b1540197256f98e8880962fb13d))



##### Dependencies

  * Update shared dependencies ([#2174](https://github.com/googleapis/java-bigtable/issues/2174)) ([f313f14](https://github.com/googleapis/java-bigtable/commit/f313f1410f28df15438d83acaa74b715c752abdd))



## March 21, 2024

Feature

You can now view Bigtable cost data with instance granularity in the Google Cloud Billing detailed export to BigQuery. For more information, see [Structure of detailed cost data export](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery-tables/detailed-usage).

## March 19, 2024

Feature

You can now create daily backups of your Bigtable table by enabling automated backup. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For details, see [Automated backup](https://docs.cloud.google.com/bigtable/docs/managing-backups#use-automated-backup).

## March 18, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.36.0](https://github.com/googleapis/java-bigtable/compare/v2.35.1...v2.36.0) (2024-03-13)

##### Features

  * Add models for type APIs ([#2160](https://github.com/googleapis/java-bigtable/issues/2160)) ([8277ea8](https://github.com/googleapis/java-bigtable/commit/8277ea828491d39b9c3c2e67c1a03927e2a744d9))
  * Publish new bigtable APIs for types and aggregates ([#2158](https://github.com/googleapis/java-bigtable/issues/2158)) ([430dffe](https://github.com/googleapis/java-bigtable/commit/430dffe0ff5916d9c3d7cfd7d35ca13514fd8934))



## March 11, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.35.1](https://github.com/googleapis/java-bigtable/compare/v2.35.0...v2.35.1) (2024-03-07)

##### Dependencies

  * Update shared dependencies ([#2140](https://github.com/googleapis/java-bigtable/issues/2140)) ([a6c9f9b](https://github.com/googleapis/java-bigtable/commit/a6c9f9bc7781535d80c4a44cb350052d6771b2e0))



#### [2.35.0](https://github.com/googleapis/java-bigtable/compare/v2.34.0...v2.35.0) (2024-03-05)

##### Features

  * Add authorized view bindings to Cloud Bigtable data APIs and messages ([#2144](https://github.com/googleapis/java-bigtable/issues/2144)) ([ae89709](https://github.com/googleapis/java-bigtable/commit/ae89709514921f7f362b7bf6057ec2f01e50046d))



##### Bug Fixes

  * Per-connection metrics issue when using a different Bigtable project ([#2143](https://github.com/googleapis/java-bigtable/issues/2143)) ([8dbd680](https://github.com/googleapis/java-bigtable/commit/8dbd680abc1ad13ad33981c67f8349f63432b7ea))



## February 26, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.34.0](https://github.com/googleapis/java-bigtable/compare/v2.33.0...v2.34.0) (2024-02-21)

##### Features

  * Add the export logic for per-connection error rate metric ([#2121](https://github.com/googleapis/java-bigtable/issues/2121)) ([d053f2d](https://github.com/googleapis/java-bigtable/commit/d053f2dc98eb8576f33471d728c6fbf32d537ece))
  * Create the backbone of counting errors per connection each minute. ([#2094](https://github.com/googleapis/java-bigtable/issues/2094)) ([7d27816](https://github.com/googleapis/java-bigtable/commit/7d27816b959a06412f59f49023611f0bca8e3536))



##### Dependencies

  * Update actions/setup-java action to v4 ([#2106](https://github.com/googleapis/java-bigtable/issues/2106)) ([a694296](https://github.com/googleapis/java-bigtable/commit/a694296a76faefe31585aabc9dce0adcf4a342bf))
  * Update dependency com.google.cloud:gapic-libraries-bom to v1.30.0 ([#2126](https://github.com/googleapis/java-bigtable/issues/2126)) ([f613bd0](https://github.com/googleapis/java-bigtable/commit/f613bd0dd449d218a0d8b6d20344155f9762cfb1))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.25.0 ([#2113](https://github.com/googleapis/java-bigtable/issues/2113)) ([ba1973e](https://github.com/googleapis/java-bigtable/commit/ba1973e20c4cbb9be778840cc202eb7e4daf04f4))
  * Update dependency com.google.truth.extensions:truth-proto-extension to v1.4.1 ([#2119](https://github.com/googleapis/java-bigtable/issues/2119)) ([0a7ad66](https://github.com/googleapis/java-bigtable/commit/0a7ad66fa9e2c1858f51c25d1ea01b26da0b944f))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.10.1 ([#2122](https://github.com/googleapis/java-bigtable/issues/2122)) ([99ec284](https://github.com/googleapis/java-bigtable/commit/99ec28425c2caac6a992cb7edd83f2029cce92ec))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.10.1 ([#2123](https://github.com/googleapis/java-bigtable/issues/2123)) ([12d961a](https://github.com/googleapis/java-bigtable/commit/12d961aad5d15feb27a7996de8b9a626fcdfbc5b))



## February 19, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.33.0](https://github.com/googleapis/java-bigtable/compare/v2.32.0...v2.33.0) (2024-02-12)

##### Features

  * Define the metrics for collecting per connection error count. ([#2088](https://github.com/googleapis/java-bigtable/issues/2088)) ([b212bbf](https://github.com/googleapis/java-bigtable/commit/b212bbfcfb2d8c2e2fdc2fc3609976c8a462f677))



##### Bug Fixes

  * Deflake backup integration tests due to deleteBackup timeouts ([#2105](https://github.com/googleapis/java-bigtable/issues/2105)) ([0948da7](https://github.com/googleapis/java-bigtable/commit/0948da7885958556c85ce333cf13b36896ddc154))
  * Extend timeouts for deleting snapshots, backups and tables ([#2108](https://github.com/googleapis/java-bigtable/issues/2108)) ([df1d307](https://github.com/googleapis/java-bigtable/commit/df1d307255abbe77050c2c24f934b13bb82eb212))



##### Dependencies

  * **Autogen:** Set packed = false on field_behavior extension ([#2101](https://github.com/googleapis/java-bigtable/issues/2101)) ([7c438c6](https://github.com/googleapis/java-bigtable/commit/7c438c603f3893946f73b2d69f2e0901ac9b044a))
  * Update actions/setup-java action to v4 ([#2099](https://github.com/googleapis/java-bigtable/issues/2099)) ([a6c7c77](https://github.com/googleapis/java-bigtable/commit/a6c7c779df39b151202d765728c853a7bdcd3d18))
  * Update dependency com.google.cloud:gapic-libraries-bom to v1.29.0 ([#2109](https://github.com/googleapis/java-bigtable/issues/2109)) ([ef88519](https://github.com/googleapis/java-bigtable/commit/ef8851976898f595f53bbc239d4f1731893d924b))
  * Update dependency com.google.cloud:sdk-platform-java-config to v3.24.0 ([#2085](https://github.com/googleapis/java-bigtable/issues/2085)) ([3851a5e](https://github.com/googleapis/java-bigtable/commit/3851a5e7db5ae3d3c1d29e6f97fc37815c8b70d1))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.10.0 ([#2091](https://github.com/googleapis/java-bigtable/issues/2091)) ([2516a09](https://github.com/googleapis/java-bigtable/commit/2516a095c8305a4193bbadf6c08395f6d718e1d0))
  * Update protobuf to 25.2 in WORKSPACE ([#2086](https://github.com/googleapis/java-bigtable/issues/2086)) ([3eafcee](https://github.com/googleapis/java-bigtable/commit/3eafcee16f7a5e357fc8617120ee875d32fc415d))



## February 12, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.23.0](https://github.com/googleapis/python-bigtable/compare/v2.22.0...v2.23.0) (2024-02-07)

##### Features

  * Add async data client preview ([7088e39](https://github.com/googleapis/python-bigtable/commit/7088e39c6bac10e5f830e8fa68e181412910ec5a))
  * Adding feature flags for routing cookie and retry info ([#905](https://github.com/googleapis/python-bigtable/issues/905)) ([1859e67](https://github.com/googleapis/python-bigtable/commit/1859e67961629663a8749eea849b5b005fcbc09f))



##### Bug Fixes

  * Fix `ValueError` in `test__validate_universe_domain` ([#929](https://github.com/googleapis/python-bigtable/issues/929)) ([aa76a5a](https://github.com/googleapis/python-bigtable/commit/aa76a5aaa349386d5972d96e1255389e30df8764))



## February 01, 2024

Feature

The Bigtable Studio query builder is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). The query builder lets you create and run queries and view the results directly from the Google Cloud console. For details, see [Build queries in the console](https://docs.cloud.google.com/bigtable/docs/query-builder).

## January 31, 2024

Feature

Bigtable is available in the `africa-south1` (Johannesburg) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## January 29, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.32.0](https://github.com/googleapis/java-bigtable/compare/v2.31.0...v2.32.0) (2024-01-25)

##### Features

  * Append version to the client name in client-side metrics. ([#2062](https://github.com/googleapis/java-bigtable/issues/2062)) ([9a0cdc8](https://github.com/googleapis/java-bigtable/commit/9a0cdc8cb8e2c52fde403eb316d28bf99c55a1e7))



##### Bug Fixes

  * **Deps:** Update the Java code generator (gapic-generator-java) to 2.32.0 ([#2060](https://github.com/googleapis/java-bigtable/issues/2060)) ([c218ac3](https://github.com/googleapis/java-bigtable/commit/c218ac3571360c85171dac71b915ad6776d97589))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.23.0 ([#2076](https://github.com/googleapis/java-bigtable/issues/2076)) ([5d1079c](https://github.com/googleapis/java-bigtable/commit/5d1079c2d1ced39b656773ff17743cb4e08a6126))
  * Update dependency com.google.truth.extensions:truth-proto-extension to v1.3.0 ([#2058](https://github.com/googleapis/java-bigtable/issues/2058)) ([1622a9f](https://github.com/googleapis/java-bigtable/commit/1622a9f34d6818952eb283eba01992dc48a9df25))
  * Update shared dependencies ([#2056](https://github.com/googleapis/java-bigtable/issues/2056)) ([f73ba40](https://github.com/googleapis/java-bigtable/commit/f73ba4099b497a78f82a1ad61b91035380955c21))



## January 22, 2024

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.31.0](https://github.com/googleapis/java-bigtable/compare/v2.30.0...v2.31.0) (2024-01-12)

##### Features

  * Add a flag to add / remove routing cookie from callable chain ([#2032](https://github.com/googleapis/java-bigtable/issues/2032)) ([201e631](https://github.com/googleapis/java-bigtable/commit/201e631f893b1edacdd5760c1d180b212dc9e38a))
  * Adding feature flags for routing cookie and retry info ([#2031](https://github.com/googleapis/java-bigtable/issues/2031)) ([08c5bf1](https://github.com/googleapis/java-bigtable/commit/08c5bf1fd76258387135c8c3abe75f13bcdcc1f6))
  * Count row merging errors as internal errors ([#2045](https://github.com/googleapis/java-bigtable/issues/2045)) ([fc7845b](https://github.com/googleapis/java-bigtable/commit/fc7845bd4cefca05bccc4dc3a9f727fd20f5adf6))
  * Enable feature flag when setting is enabled ([#2043](https://github.com/googleapis/java-bigtable/issues/2043)) ([e0d90db](https://github.com/googleapis/java-bigtable/commit/e0d90db67b3ea52d833f7d6bcd78e3f7e91ff301))
  * Handle retry info so client respect the delay server sets ([#2026](https://github.com/googleapis/java-bigtable/issues/2026)) ([f1b7fc7](https://github.com/googleapis/java-bigtable/commit/f1b7fc79ad3fd9006e430e48430331b360bb22e3))



##### Bug Fixes

  * **Deps:** Update the Java code generator (gapic-generator-java) to 2.31.0 ([#2044](https://github.com/googleapis/java-bigtable/issues/2044)) ([d9042a5](https://github.com/googleapis/java-bigtable/commit/d9042a567f284424efb4af69f757883c9781dce3))
  * Fix RetryInfo algorithm and tests ([#2041](https://github.com/googleapis/java-bigtable/issues/2041)) ([dad7517](https://github.com/googleapis/java-bigtable/commit/dad751736112323c578b3c90d9587fc182105747))



##### Dependencies

  * Update dependency com.google.cloud:gapic-libraries-bom to v1.27.0 ([#2030](https://github.com/googleapis/java-bigtable/issues/2030)) ([a492d02](https://github.com/googleapis/java-bigtable/commit/a492d02bdc52cb81d8804a4d7cd363b5807bdd47))
  * Update dependency com.google.truth.extensions:truth-proto-extension to v1.2.0 ([#2035](https://github.com/googleapis/java-bigtable/issues/2035)) ([46e1e03](https://github.com/googleapis/java-bigtable/commit/46e1e0335f9969fa1b60acdf17e9b8abbc312ca2))



## December 28, 2023

Announcement

The Cloud Bigtable documentation now includes a [Bigtable for DynamoDB users](https://docs.cloud.google.com/bigtable/docs/dynamodb-users) guide for those considering a migration to Bigtable.

## December 18, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.22.0](https://github.com/googleapis/python-bigtable/compare/v2.21.0...v2.22.0) (2023-12-12)

##### Features

  * Add support for Cloud Bigtable request priorities in app profiles ([#871](https://github.com/googleapis/python-bigtable/issues/871)) ([a4d551e](https://github.com/googleapis/python-bigtable/commit/a4d551e34006202ee96a395a2107d7acdc5881de))
  * Add support for Python 3.12 ([#888](https://github.com/googleapis/python-bigtable/issues/888)) ([4f050aa](https://github.com/googleapis/python-bigtable/commit/4f050aa5aed9a9dcf209779d5c10e5de8e2ff19e))
  * Introduce compatibility with native namespace packages ([#893](https://github.com/googleapis/python-bigtable/issues/893)) ([d218f4e](https://github.com/googleapis/python-bigtable/commit/d218f4ebd4ed6705721dca9318df955b40b0d0ac))
  * Publish CopyBackup protos to external customers ([#855](https://github.com/googleapis/python-bigtable/issues/855)) ([4105df7](https://github.com/googleapis/python-bigtable/commit/4105df762f1318c49bba030063897f0c50e4daee))



##### Bug Fixes

  * Add feature flag for improved mutate rows throttling ([e5af359](https://github.com/googleapis/python-bigtable/commit/e5af3597f45fc4c094c59abca876374f5a866c1b))
  * Add lock to flow control ([#899](https://github.com/googleapis/python-bigtable/issues/899)) ([e4e63c7](https://github.com/googleapis/python-bigtable/commit/e4e63c7b5b91273b3aae04fda59cc5a21c848de2))
  * Mutations batcher race condition ([#896](https://github.com/googleapis/python-bigtable/issues/896)) ([fe58f61](https://github.com/googleapis/python-bigtable/commit/fe58f617c7364d7e99e2ec50abd5f080852bf033))
  * Require google-cloud-core 1.4.4 ([#866](https://github.com/googleapis/python-bigtable/issues/866)) ([09f8a46](https://github.com/googleapis/python-bigtable/commit/09f8a4667d8b68a9f2048ba1aa57db4f775a2c03))
  * Use `retry_async` instead of `retry` in async client ([597efd1](https://github.com/googleapis/python-bigtable/commit/597efd11d15f20549010b4301be4d9768326e6a2))



##### Documentation

  * Minor formatting ([e5af359](https://github.com/googleapis/python-bigtable/commit/e5af3597f45fc4c094c59abca876374f5a866c1b))



## December 13, 2023

Feature

Reverse scans in Cloud Bigtable let you read a range of rows backwards. This feature is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For details, see [Reverse scans](https://docs.cloud.google.com/bigtable/docs/reads#reverse-scan).

## December 11, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.30.0](https://github.com/googleapis/java-bigtable/compare/v2.29.1...v2.30.0) (2023-12-05)

##### Features

  * Client sends routing cookie back to server ([#1888](https://github.com/googleapis/java-bigtable/issues/1888)) ([4c73abd](https://github.com/googleapis/java-bigtable/commit/4c73abd2f4a07808b591dd9178e87715d2f3008d))



##### Dependencies

  * Update dependency org.junit.vintage:junit-vintage-engine to v5.10.1 ([#1990](https://github.com/googleapis/java-bigtable/issues/1990)) ([7ad70e3](https://github.com/googleapis/java-bigtable/commit/7ad70e3abc1af7dfab715386978bf14f02b34e5d))
  * Update shared dependencies ([#2016](https://github.com/googleapis/java-bigtable/issues/2016)) ([4e49dff](https://github.com/googleapis/java-bigtable/commit/4e49dffa72db8dd04e75ca86178d875fab6f566b))



## November 13, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.29.1](https://github.com/googleapis/java-bigtable/compare/v2.29.0...v2.29.1) (2023-11-07)

##### Bug Fixes

  * Add getPageSize() to QueryPaginator ([42a7e36](https://github.com/googleapis/java-bigtable/commit/42a7e36ae5902c08ed3a1b553bec645291f1778a))



##### Dependencies

  * Update shared dependencies ([#1985](https://github.com/googleapis/java-bigtable/issues/1985)) ([0d1f620](https://github.com/googleapis/java-bigtable/commit/0d1f6203dd2317fa877e31c113bdca1e8174a492))



#### [2.25.3](https://github.com/googleapis/java-bigtable/compare/v2.25.2...v2.25.3) (2023-11-08)

##### Bug Fixes

  * A rare race condition in the row merger ([#1939](https://github.com/googleapis/java-bigtable/issues/1939)) ([#2002](https://github.com/googleapis/java-bigtable/issues/2002)) ([6de74f3](https://github.com/googleapis/java-bigtable/commit/6de74f31a72668bb76e5a25922b38b3889aa5850))



#### [2.23.5](https://github.com/googleapis/java-bigtable/compare/v2.23.4...v2.23.5) (2023-11-07)

##### Bug Fixes

  * Remove javadoc external link configuration ([#1815](https://github.com/googleapis/java-bigtable/issues/1815)) ([#1999](https://github.com/googleapis/java-bigtable/issues/1999)) ([e7752be](https://github.com/googleapis/java-bigtable/commit/e7752be1a76b72842e3fd2e6d4ad1d0300566c23))



#### [2.23.4](https://github.com/googleapis/java-bigtable/compare/v2.23.3...v2.23.4) (2023-11-06)

##### Bug Fixes

  * A rare race condition in the row merger ([#1939](https://github.com/googleapis/java-bigtable/issues/1939)) ([#1988](https://github.com/googleapis/java-bigtable/issues/1988)) ([31b084a](https://github.com/googleapis/java-bigtable/commit/31b084abc9c4d609314f232e616b59a4016b991f))



## November 08, 2023

Feature

Cloud Bigtable app profiles now let you [configure request priorities](https://docs.cloud.google.com/bigtable/docs/request-priorities) to prioritize certain workload data requests over others. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 30, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.29.0](https://github.com/googleapis/java-bigtable/compare/v2.28.0...v2.29.0) (2023-10-26)

##### Features

  * Add APIs to enable request priorities ([#1959](https://github.com/googleapis/java-bigtable/issues/1959)) ([befd140](https://github.com/googleapis/java-bigtable/commit/befd1402a0f324b365b72e3b237d33d2f3fe8bbc))



##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.28 ([#1966](https://github.com/googleapis/java-bigtable/issues/1966)) ([8fb09e5](https://github.com/googleapis/java-bigtable/commit/8fb09e53a3d85273578ba26c522931047b249333))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.28 ([#1967](https://github.com/googleapis/java-bigtable/issues/1967)) ([117e0ec](https://github.com/googleapis/java-bigtable/commit/117e0ec546343798cbc69eb23fef539de0b8bb8d))
  * Update shared dependencies ([#1964](https://github.com/googleapis/java-bigtable/issues/1964)) ([bf5a9b7](https://github.com/googleapis/java-bigtable/commit/bf5a9b774f79005ee9980a12931597ddc1ec5bb3))



## October 16, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.28.0](https://github.com/googleapis/java-bigtable/compare/v2.27.4...v2.28.0) (2023-10-12)

##### Features

  * Add support for Cloud Bigtable Request Priorities in App Profiles ([#1954](https://github.com/googleapis/java-bigtable/issues/1954)) ([8822571](https://github.com/googleapis/java-bigtable/commit/88225717b870032b8892123262d2529ba1dbd481))
  * Add test profile to push metrics to test environment ([#1921](https://github.com/googleapis/java-bigtable/issues/1921)) ([2104315](https://github.com/googleapis/java-bigtable/commit/210431523ce54029db846a0d6777d5e417e039dd))



##### Dependencies

  * Update shared dependencies ([#1955](https://github.com/googleapis/java-bigtable/issues/1955)) ([f29717e](https://github.com/googleapis/java-bigtable/commit/f29717e3f1af03a78ce9468cdafa8c09dfb1b216))



## October 09, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.27.4](https://github.com/googleapis/java-bigtable/compare/v2.27.3...v2.27.4) (2023-09-29)

##### Dependencies

  * Update dependency com.google.cloud:gapic-libraries-bom to v1.21.0 ([#1942](https://github.com/googleapis/java-bigtable/issues/1942)) ([f8d533f](https://github.com/googleapis/java-bigtable/commit/f8d533f4dcfd60a3eac9656bdc7339ac25f06fad))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.16.1 ([#1933](https://github.com/googleapis/java-bigtable/issues/1933)) ([159636a](https://github.com/googleapis/java-bigtable/commit/159636ac82e7bb19b425075a006ee98a39af1d57))



## October 06, 2023

Feature

Cloud Bigtable instance, cluster, and table metadata is automatically synced to [Data Catalog](https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-data-catalog), a feature of Dataplex, for improved data discovery and governance. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## October 02, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.27.3](https://github.com/googleapis/java-bigtable/compare/v2.27.2...v2.27.3) (2023-09-29)

##### Bug Fixes

  * A rare race condition in the row merger ([#1939](https://github.com/googleapis/java-bigtable/issues/1939)) ([fccd710](https://github.com/googleapis/java-bigtable/commit/fccd7100578da3e2ee2a315c6e956c06dbf41668))



##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.27 ([#1919](https://github.com/googleapis/java-bigtable/issues/1919)) ([56d6b40](https://github.com/googleapis/java-bigtable/commit/56d6b40b9f874ec4ad78618c1cf0d365ddc9276b))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.27 ([#1920](https://github.com/googleapis/java-bigtable/issues/1920)) ([ca1dd5b](https://github.com/googleapis/java-bigtable/commit/ca1dd5b258c7fa5cfd90811dc8b9492c19d1f104))
  * Update gapic-generator-java to 2.26.0 ([#1936](https://github.com/googleapis/java-bigtable/issues/1936)) ([15cd486](https://github.com/googleapis/java-bigtable/commit/15cd4868ff807513914095a3758134eaa14f0ea3))



## September 25, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.25.2](https://github.com/googleapis/java-bigtable/compare/v2.25.0...v2.25.2) (2023-09-18)

##### Bug Fixes

  * Check that all bulk mutation entries are accounted for ([#1907](https://github.com/googleapis/java-bigtable/issues/1907)) ([#1923](https://github.com/googleapis/java-bigtable/issues/1923)) ([e4db745](https://github.com/googleapis/java-bigtable/commit/e4db74534690eb090347c00047eecbd45f5a22b7))
  * Make sure to propagate the response when throttling is enabled ([#1908](https://github.com/googleapis/java-bigtable/issues/1908)) ([#1922](https://github.com/googleapis/java-bigtable/issues/1922)) ([7ec5dd5](https://github.com/googleapis/java-bigtable/commit/7ec5dd5bc9499b01f5e330c28c9c5ee8cfadad68))



##### Miscellaneous Chores

  * Update release tag to 2.25.2 ([#1926](https://github.com/googleapis/java-bigtable/issues/1926)) ([9d5868b](https://github.com/googleapis/java-bigtable/commit/9d5868b2350f2b24b5988ebe3adb2e77e36c8a5a))



## September 19, 2023

Feature

Cloud Bigtable is available in the `me-central2` (Dammam) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## September 18, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.27.2](https://github.com/googleapis/java-bigtable/compare/v2.27.1...v2.27.2) (2023-09-13)

##### Bug Fixes

  * Check that all bulk mutation entries are accounted for ([#1907](https://github.com/googleapis/java-bigtable/issues/1907)) ([9ad8a00](https://github.com/googleapis/java-bigtable/commit/9ad8a00ec4f10a75952fa566a7effc980936dee1))
  * Set wait timeout on watchdog ([#1913](https://github.com/googleapis/java-bigtable/issues/1913)) ([f8ba6fe](https://github.com/googleapis/java-bigtable/commit/f8ba6fe554dd02bb99fb03859cc5c8b04561b0c3))



##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.26 ([#1896](https://github.com/googleapis/java-bigtable/issues/1896)) ([dfc4231](https://github.com/googleapis/java-bigtable/commit/dfc4231af9b74a4d5db3beaf26dd611a27cc6a67))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.26 ([#1897](https://github.com/googleapis/java-bigtable/issues/1897)) ([d446856](https://github.com/googleapis/java-bigtable/commit/d4468560db62f2102c404b3907cd5ae76d1e08b6))
  * Update shared dependencies ([#1901](https://github.com/googleapis/java-bigtable/issues/1901)) ([96f2690](https://github.com/googleapis/java-bigtable/commit/96f2690e219714e497208e8be5e46b7f38340625))



#### [2.27.1](https://github.com/googleapis/java-bigtable/compare/v2.27.0...v2.27.1) (2023-09-12)

##### Bug Fixes

  * Aggregate batching throttling latency per attempt and reset it between ([#1905](https://github.com/googleapis/java-bigtable/issues/1905)) ([e6cc5f6](https://github.com/googleapis/java-bigtable/commit/e6cc5f615630d15b717df1056ceed98f21f2297b))
  * Make sure to propagate the response when throttling is enabled ([#1908](https://github.com/googleapis/java-bigtable/issues/1908)) ([f743187](https://github.com/googleapis/java-bigtable/commit/f7431871ba4ea64351fc5710089f8308e91d7978))



##### Dependencies

  * Update the Java code generator (gapic-generator-java) to 2.25.0 ([#1902](https://github.com/googleapis/java-bigtable/issues/1902)) ([f4fe6a0](https://github.com/googleapis/java-bigtable/commit/f4fe6a054194f68da1d7a548dec7a1cec68c1a2c))



## September 11, 2023

Feature

You can now choose not to specify the number of nodes when creating a Cloud Bigtable cluster using the `gcloud CLI`. This configuration lets Bigtable automatically calculate the number of nodes based on your data footprint and optimize for 50% storage utilization. To learn more, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## September 05, 2023

Announcement

Dataflow templates are available to stream Cloud Bigtable data change records to BigQuery or Pub/Sub. For more information, see [Reading a change stream](https://docs.cloud.google.com/bigtable/docs/change-streams-overview#reading-change-stream).

## August 31, 2023

Feature

You can now use `EXPORT DATA` statements to [directly export BigQuery data to Cloud Bigtable](https://docs.cloud.google.com/bigquery/docs/export-to-bigtable). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 28, 2023

Feature

Cloud Bigtable is available in the `europe-west10` (Berlin) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## August 21, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.27.0](https://github.com/googleapis/java-bigtable/compare/v2.26.0...v2.27.0) (2023-08-17)

##### Features

  * Copy backup API support ([#1398](https://github.com/googleapis/java-bigtable/issues/1398)) ([558a408](https://github.com/googleapis/java-bigtable/commit/558a408f5fa0566652df923799cf9f7bc03f7194))
  * Publish CopyBackup protos to external customers ([#1883](https://github.com/googleapis/java-bigtable/issues/1883)) ([d6e934f](https://github.com/googleapis/java-bigtable/commit/d6e934fc71e1c1dd4e13492d2f6c4688b6b0d59d))



## August 17, 2023

Feature

You can now create a copy of a Cloud Bigtable backup and store it in any project or region where you have a Bigtable instance. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). To learn more, see [About Bigtable backups](https://docs.cloud.google.com/bigtable/docs/backups).

## August 14, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [5.0.0](https://github.com/googleapis/nodejs-bigtable/compare/v4.6.1...v5.0.0) (2023-08-10)

##### ⚠ BREAKING CHANGES

  * Upgrade to Node 14 ([#1311](https://github.com/googleapis/nodejs-bigtable/issues/1311))



##### Miscellaneous Chores

  * Upgrade to Node 14 ([#1311](https://github.com/googleapis/nodejs-bigtable/issues/1311)) ([4330cb2](https://github.com/googleapis/nodejs-bigtable/commit/4330cb238ec887e85456cde0f18f3881caca5e14))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.26.0](https://github.com/googleapis/java-bigtable/compare/v2.25.1...v2.26.0) (2023-08-09)

##### Features

  * Add last_scanned_row_key feature ([#1856](https://github.com/googleapis/java-bigtable/issues/1856)) ([ef30dde](https://github.com/googleapis/java-bigtable/commit/ef30dde4bdbedb8f04feb0604d66c95309468a2e))
  * Enable last_scanned_row_responses feature flag ([#1862](https://github.com/googleapis/java-bigtable/issues/1862)) ([c2288c9](https://github.com/googleapis/java-bigtable/commit/c2288c9f1f97571b7b12394a4697ebf5abfc5cfc))
  * Setup 2.25.x lts branch ([#1866](https://github.com/googleapis/java-bigtable/issues/1866)) ([220cf4b](https://github.com/googleapis/java-bigtable/commit/220cf4b142adeb63802e27fb5effdb343f832563))



##### Bug Fixes

  * Fix batcher metric labels ([#1829](https://github.com/googleapis/java-bigtable/issues/1829)) ([6245c12](https://github.com/googleapis/java-bigtable/commit/6245c12b37d8c1398cdfd497129a6fc1ef767508))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.24.0 ([#1878](https://github.com/googleapis/java-bigtable/issues/1878)) ([0de458d](https://github.com/googleapis/java-bigtable/commit/0de458d919cdef4284da98b830c26027b9ae8941))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.14.0 ([#1873](https://github.com/googleapis/java-bigtable/issues/1873)) ([bb83064](https://github.com/googleapis/java-bigtable/commit/bb830647358e66bddc392e0cffbe7e63a7036ce6))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.24 ([#1876](https://github.com/googleapis/java-bigtable/issues/1876)) ([d397c33](https://github.com/googleapis/java-bigtable/commit/d397c337ab17d000a331bade8fca8b49f5f2355e))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.24 ([#1877](https://github.com/googleapis/java-bigtable/issues/1877)) ([1a8be60](https://github.com/googleapis/java-bigtable/commit/1a8be60a20498d6fa321841fa561ab7c3d9fe9a2))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.21.0](https://github.com/googleapis/python-bigtable/compare/v2.20.0...v2.21.0) (2023-08-02)

##### Features

  * Add last_scanned_row_responses to FeatureFlags ([#845](https://github.com/googleapis/python-bigtable/issues/845)) ([14a6739](https://github.com/googleapis/python-bigtable/commit/14a673901f82fa247c8027730a0bba41e0ec4757))



##### Documentation

  * Minor formatting ([#851](https://github.com/googleapis/python-bigtable/issues/851)) ([5ebe231](https://github.com/googleapis/python-bigtable/commit/5ebe2312dab70210811fca68c6625d2546442afd))



## July 31, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.25.1](https://github.com/googleapis/java-bigtable/compare/v2.25.0...v2.25.1) (2023-07-25)

##### Bug Fixes

  * Update the readRow attempt timeouts to be in line with unary RPCs instead of scans ([#1834](https://github.com/googleapis/java-bigtable/issues/1834)) ([168c33e](https://github.com/googleapis/java-bigtable/commit/168c33e3135755cc5a1105f18bf93ade5e1219dc))



##### Dependencies

  * Update dependency org.junit.vintage:junit-vintage-engine to v5.10.0 ([#1847](https://github.com/googleapis/java-bigtable/issues/1847)) ([825faaa](https://github.com/googleapis/java-bigtable/commit/825faaad93a5062e6f34ff699cc02701b69e56ab))
  * Update shared dependencies ([#1845](https://github.com/googleapis/java-bigtable/issues/1845)) ([88e1892](https://github.com/googleapis/java-bigtable/commit/88e18922b4e1da398c51441aff014bca5f3bb746))
  * Update the Java code generator (gapic-generator-java) to 2.23.1 ([#1846](https://github.com/googleapis/java-bigtable/issues/1846)) ([78fd837](https://github.com/googleapis/java-bigtable/commit/78fd837987780c62137354fbbe41e71050948405))



## July 24, 2023

Feature

Cloud Bigtable is available in the europe-west12 (Turin) and me-central1 (Doha) regions. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.25.0](https://github.com/googleapis/java-bigtable/compare/v2.24.1...v2.25.0) (2023-07-14)

##### Features

  * Change stream retention to create and update table ([#1823](https://github.com/googleapis/java-bigtable/issues/1823)) ([05fca58](https://github.com/googleapis/java-bigtable/commit/05fca581d4225769cc581e26e679e6bca105055b))



##### Bug Fixes

  * Fix batch mutation limit ([#1808](https://github.com/googleapis/java-bigtable/issues/1808)) ([ed24d4f](https://github.com/googleapis/java-bigtable/commit/ed24d4fdc67c6d0af66ea055ba1ad7f7c037a361))
  * Update default sample row key attempt timeout to 5 min ([#1827](https://github.com/googleapis/java-bigtable/issues/1827)) ([2f363ef](https://github.com/googleapis/java-bigtable/commit/2f363ef3636c2810c322bb5978cc586f8aec2ef2))



##### Documentation

  * Fix formatting for reversed order field example ([#1836](https://github.com/googleapis/java-bigtable/issues/1836)) ([10a0426](https://github.com/googleapis/java-bigtable/commit/10a0426f580b86b26541b95a778bb8b7f6562383))
  * Increase the maximum retention period for a Cloud Bigtable backup from 30 days to 90 days ([#1826](https://github.com/googleapis/java-bigtable/issues/1826)) ([159fe38](https://github.com/googleapis/java-bigtable/commit/159fe3857735c9061672fc951388215edb0a324c))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.22.0 ([#1838](https://github.com/googleapis/java-bigtable/issues/1838)) ([fba2c49](https://github.com/googleapis/java-bigtable/commit/fba2c49e9e71209289497f53868aa561c0fba7a3))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.13.0 ([#1833](https://github.com/googleapis/java-bigtable/issues/1833)) ([cb160af](https://github.com/googleapis/java-bigtable/commit/cb160af8e66ec6693ed0d3286c654a93094b68a3))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.20.0](https://github.com/googleapis/python-bigtable/compare/v2.19.0...v2.20.0) (2023-07-17)

##### Features

rel="noreferrer noopener"})

  * Increase the maximum retention period for a Cloud Bigtable backup from 30 days to 90 days ([d5720f8](https://github.com/googleapis/python-bigtable/commit/d5720f8f5b5a81572f31d40051b3ec0f1d104304))



##### Bug Fixes

  * Add async context manager return types ([#828](https://github.com/googleapis/python-bigtable/issues/828)) ([475a160](https://github.com/googleapis/python-bigtable/commit/475a16072f3ad41357bdb765fff608a39141ec00))



##### Documentation

  * Fix formatting for reversed order field example ([#831](https://github.com/googleapis/python-bigtable/issues/831)) ([fddd0ba](https://github.com/googleapis/python-bigtable/commit/fddd0ba97155e112af92a98fd8f20e59b139d177))



## July 18, 2023

Feature

Cloud Bigtable change streams are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). A change stream captures changes to data in a table as the changes happen, letting you stream them for processing or analysis. For more information, see [Change streams overview](https://docs.cloud.google.com/bigtable/docs/change-streams-overview).

## July 10, 2023

Feature

Committed use discounts are now [generally available (GA)](https://cloud.google.com/products#product-launch-stages) for Cloud Bigtable in exchange for a commitment to continuously spend a certain amount on Bigtable nodes for one year or three years. For details, see [Committed use discounts](https://docs.cloud.google.com/bigtable/docs/cuds).

## July 03, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.24.1](https://github.com/googleapis/java-bigtable/compare/v2.24.0...v2.24.1) (2023-06-27)

##### Bug Fixes

  * Remove javadoc external link configuration ([#1815](https://github.com/googleapis/java-bigtable/issues/1815)) ([9c71a93](https://github.com/googleapis/java-bigtable/commit/9c71a934f8354477b0e229b83047c8203d4ab978))



#### [2.24.0](https://github.com/googleapis/java-bigtable/compare/v2.23.3...v2.24.0) (2023-06-27)

##### Features

  * Add experimental reverse scan for public preview ([#1809](https://github.com/googleapis/java-bigtable/issues/1809)) ([f4f2e2e](https://github.com/googleapis/java-bigtable/commit/f4f2e2ebac535372ebfb8ebd60ca78f0f7ca010b))
  * Reverse scans public preview ([#1711](https://github.com/googleapis/java-bigtable/issues/1711)) ([176360f](https://github.com/googleapis/java-bigtable/commit/176360f2689966dccbe95c401cf2bfe9ca64f274))



##### Dependencies

  * Update dependency com.google.truth.extensions:truth-proto-extension to v1.1.5 ([#1801](https://github.com/googleapis/java-bigtable/issues/1801)) ([a8961e8](https://github.com/googleapis/java-bigtable/commit/a8961e8f45f5cb2812c185a68a8892bed958ae6a))
  * Update dependency kr.motd.maven:os-maven-plugin to v1.7.1 ([#1792](https://github.com/googleapis/java-bigtable/issues/1792)) ([80acca0](https://github.com/googleapis/java-bigtable/commit/80acca0922060e932dedd31e8079f432b7de9785))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.23 ([#1800](https://github.com/googleapis/java-bigtable/issues/1800)) ([a9172c4](https://github.com/googleapis/java-bigtable/commit/a9172c4570a053d28ab90232b98ab716cc8b6f80))
  * Update shared dependencies to 3.12.0, monitoring to 3.21.0, update renovate config ([#1807](https://github.com/googleapis/java-bigtable/issues/1807)) ([12fc8cd](https://github.com/googleapis/java-bigtable/commit/12fc8cded38d64c9e4d997d83ff8cdbffe373120))



## June 30, 2023

Feature

Reverse scans in Cloud Bigtable are now available in [Preview](https://cloud.google.com/products#product-launch-stages). For details, see [Reverse scans](https://docs.cloud.google.com/bigtable/docs/reads#reverse-scan).

Feature

The maximum retention period for a Cloud Bigtable backup has been increased from 30 days to 90 days, giving you more robust data protection and data quality control. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information on how Bigtable backups work, see [About backups](https://docs.cloud.google.com/bigtable/docs/backups).

## June 28, 2023

Feature

The Cloud Bigtable metric `Five-second maximum requests per minute` is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). This metric measures the maximum number of requests received in a five-second span per minute to help you identify short bursts of traffic. For a full description, see [Metrics](https://docs.cloud.google.com/bigtable/docs/metrics).

## June 27, 2023

Feature

You can now enable batch write flow control when you use Dataflow to send batch writes to Cloud Bigtable. This [generally available (GA)](https://cloud.google.com/products#product-launch-stages) feature automatically rate-limits traffic to avoid cluster overload and works with Bigtable autoscaling to ensure the optimal number of nodes is available to handle the batch write. For more information, see [Batch write flow control](https://docs.cloud.google.com/bigtable/docs/writes#flow-control).

## June 12, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.23.3](https://github.com/googleapis/java-bigtable/compare/v2.23.2...v2.23.3) (2023-06-08)

##### Bug Fixes

  * Set wait timeout and update default attempt timeout to 30 minutes ([#1779](https://github.com/googleapis/java-bigtable/issues/1779)) ([11019b8](https://github.com/googleapis/java-bigtable/commit/11019b87fe32b5b9c9f2d947ffd9191b56120381))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.20.0 ([#1785](https://github.com/googleapis/java-bigtable/issues/1785)) ([8ddd370](https://github.com/googleapis/java-bigtable/commit/8ddd370bf747bcc7ad7ccb6f00cc5ef188fa3511))
  * Update gapic-generator-java to 2.21.0 ([#1760](https://github.com/googleapis/java-bigtable/issues/1760)) ([05545f8](https://github.com/googleapis/java-bigtable/commit/05545f87692c05c22d17e431551b4a5f91475286))
  * Update shared dependencies to 3.11.0 ([#1783](https://github.com/googleapis/java-bigtable/issues/1783)) ([96aaa2a](https://github.com/googleapis/java-bigtable/commit/96aaa2a5a5a70feeb8ff0fd20b9dfc4a8a464bb7))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.19.0](https://github.com/googleapis/python-bigtable/compare/v2.18.1...v2.19.0) (2023-06-08)

##### Features

  * Add ChangeStreamConfig to CreateTable and UpdateTable ([#786](https://github.com/googleapis/python-bigtable/issues/786)) ([cef70f2](https://github.com/googleapis/python-bigtable/commit/cef70f243541820225f86a520e0b2abd3a7354f7))



##### Bug Fixes

  * Add a callback function on flush_rows ([#796](https://github.com/googleapis/python-bigtable/issues/796)) ([589aa5d](https://github.com/googleapis/python-bigtable/commit/589aa5d04f6b5a2bd310d0bf06aeb7058fb6fcd2))



##### Documentation

  * **samples:** Add region tags ([#788](https://github.com/googleapis/python-bigtable/issues/788)) ([ecf539c](https://github.com/googleapis/python-bigtable/commit/ecf539c4c976fd9e5505b8abf0b697b218f09fef))



## June 05, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.6.1](https://github.com/googleapis/nodejs-bigtable/compare/v4.6.0...v4.6.1) (2023-05-30)

##### Bug Fixes

  * Properly handle asynchronous read from stream ([#1284](https://github.com/googleapis/nodejs-bigtable/issues/1284)) ([55d86ba](https://github.com/googleapis/nodejs-bigtable/commit/55d86baaf554247c0c3d063fc790a37569f3e77b)). This could result in silently dropped rows in a `createReadStream`. The bug is active when the `ReadRows` stream would be piped into a consumer that would defer the processing of the rows until the next event loop run (i.e. use a `Transform` that would defer the callback invocation via `setTimeout()`).



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.23.2](https://github.com/googleapis/java-bigtable/compare/v2.23.1...v2.23.2) (2023-05-30)

##### Documentation

  * **samples:** Add bigtable filter snippet ([#1762](https://github.com/googleapis/java-bigtable/issues/1762)) ([48a6ed0](https://github.com/googleapis/java-bigtable/commit/48a6ed028a56302d6dc6554b2ecdabc8fbdb68cf))
  * **samples:** Remove client initialization as the snippets are not used standalone ([#1768](https://github.com/googleapis/java-bigtable/issues/1768)) ([a6ac97c](https://github.com/googleapis/java-bigtable/commit/a6ac97c08a851977a76e82fddb16690cff17a1fe))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.19.0 ([#1769](https://github.com/googleapis/java-bigtable/issues/1769)) ([956c851](https://github.com/googleapis/java-bigtable/commit/956c851b5d7dadb44c589a3f982e603d0a768105))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.10.1 ([#1767](https://github.com/googleapis/java-bigtable/issues/1767)) ([901b88f](https://github.com/googleapis/java-bigtable/commit/901b88f56c7b97bc08826604ed80120f07f04a64))
  * Update dependency com.google.truth.extensions:truth-proto-extension to v1.1.4 ([#1770](https://github.com/googleapis/java-bigtable/issues/1770)) ([a94a522](https://github.com/googleapis/java-bigtable/commit/a94a522a1fa4c67245f1827d8f8137cbfdbd5a45))
  * Update doclet version to v1.9.0 ([#1761](https://github.com/googleapis/java-bigtable/issues/1761)) ([a5d4215](https://github.com/googleapis/java-bigtable/commit/a5d42159643c652a9625fee620fe5ee8dee7fa2e))



## May 29, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.6.0](https://github.com/googleapis/nodejs-bigtable/compare/v4.5.2...v4.6.0) (2023-05-26)

##### Features

  * Add ChangeStreamConfig to CreateTable and UpdateTable ([#1269](https://github.com/googleapis/nodejs-bigtable/issues/1269)) ([2b05fa4](https://github.com/googleapis/nodejs-bigtable/commit/2b05fa4c7ad37fa4478f5de3cf5645b44b34ecfc))



#### [4.5.2](https://github.com/googleapis/nodejs-bigtable/compare/v4.5.1...v4.5.2) (2023-05-24)

##### Bug Fixes

  * Parsing for qualifiers with colon characters ([#1277](https://github.com/googleapis/nodejs-bigtable/issues/1277)) ([b80f533](https://github.com/googleapis/nodejs-bigtable/commit/b80f5338ae1721659c61e48d80ba976c148c8087))



## May 23, 2023

Change

You can now view information about which customer-managed encryption keys (CMEK) are used to protect your Cloud Bigtable resources and projects using Cloud Key Management Service (KMS). This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [View key usage](https://docs.cloud.google.com/bigtable/docs/use-cmek#view-key-usage).

## May 22, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.18.1](https://github.com/googleapis/python-bigtable/compare/v2.18.0...v2.18.1) (2023-05-11)

##### Bug Fixes

  * Revert "Feat: Threaded MutationsBatcher" ([#773](https://github.com/googleapis/python-bigtable/issues/773)) ([a767cff](https://github.com/googleapis/python-bigtable/commit/a767cff95d990994f85f5fd05cc10f952087b49d))



## May 15, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.23.1](https://github.com/googleapis/java-bigtable/compare/v2.23.0...v2.23.1) (2023-05-11)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.18.0 ([#1749](https://github.com/googleapis/java-bigtable/issues/1749)) ([1d7d391](https://github.com/googleapis/java-bigtable/commit/1d7d39145eefc5cbf6d015fd60a4d49441f88d1f))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.9.0 ([#1744](https://github.com/googleapis/java-bigtable/issues/1744)) ([60df07f](https://github.com/googleapis/java-bigtable/commit/60df07fcfa653291d9e5882cf3386f13813e2883))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.22 ([#1746](https://github.com/googleapis/java-bigtable/issues/1746)) ([86ea9db](https://github.com/googleapis/java-bigtable/commit/86ea9db830f6d5f7dc0b08886bce084b4650d281))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.22 ([#1747](https://github.com/googleapis/java-bigtable/issues/1747)) ([caa4462](https://github.com/googleapis/java-bigtable/commit/caa44627d6a124d1a58d85a510962c8a7caee69b))



#### [2.23.0](https://github.com/googleapis/java-bigtable/compare/v2.22.0...v2.23.0) (2023-05-09)

##### Features

  * Resizing channel pool size based on the work load ([#1271](https://github.com/googleapis/java-bigtable/issues/1271)) ([7fb1a09](https://github.com/googleapis/java-bigtable/commit/7fb1a09224e1ea05cfec6eb35deaba670d1d82d2))



##### Documentation

  * Clean up BetaApi annotations from built in metrics API ([#1741](https://github.com/googleapis/java-bigtable/issues/1741)) ([c2fbd04](https://github.com/googleapis/java-bigtable/commit/c2fbd04eb64ddcfe7ea0f234f22d0691094646a4))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.18.0](https://github.com/googleapis/python-bigtable/compare/v2.17.0...v2.18.0) (2023-05-10)

##### Features

  * Publish RateLimitInfo and FeatureFlag protos ([#768](https://github.com/googleapis/python-bigtable/issues/768)) ([171fea6](https://github.com/googleapis/python-bigtable/commit/171fea6de57a47f92a2a56050f8bfe7518144df7))
  * Threaded MutationsBatcher ([#722](https://github.com/googleapis/python-bigtable/issues/722)) ([7521a61](https://github.com/googleapis/python-bigtable/commit/7521a617c121ead96a21ca47959a53b2db2da090))



##### Bug Fixes

  * Pass the "retry" when calling read_rows. ([#759](https://github.com/googleapis/python-bigtable/issues/759)) ([505273b](https://github.com/googleapis/python-bigtable/commit/505273b72bf83d8f92d0e0a92d62f22bce96cc3d))



##### Documentation

  * Fix delete from column family example ([#764](https://github.com/googleapis/python-bigtable/issues/764)) ([128b4e1](https://github.com/googleapis/python-bigtable/commit/128b4e1f3eea2dad903d84c8f2933b17a5f0d226))
  * Fix formatting of request arg in docstring ([#756](https://github.com/googleapis/python-bigtable/issues/756)) ([45d3e43](https://github.com/googleapis/python-bigtable/commit/45d3e4308c4f494228c2e6e18a36285c557cb0c3))



## May 08, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.5.1](https://github.com/googleapis/nodejs-bigtable/compare/v4.5.0...v4.5.1) (2023-04-28)

##### Bug Fixes

  * Remove bigtable instances left over when system tests run ([#1265](https://github.com/googleapis/nodejs-bigtable/issues/1265)) ([0526612](https://github.com/googleapis/nodejs-bigtable/commit/0526612c1023816053775fa1956cbb8b97f49b00))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.22.0](https://github.com/googleapis/java-bigtable/compare/v2.21.0...v2.22.0) (2023-05-02)

##### Features

  * Add APIs to enable batch write flow control ([#1730](https://github.com/googleapis/java-bigtable/issues/1730)) ([b518d68](https://github.com/googleapis/java-bigtable/commit/b518d6851429db640e80ab78b3f827bb334f5409))
  * Add rate limiting callable ([#1729](https://github.com/googleapis/java-bigtable/issues/1729)) ([ee0da11](https://github.com/googleapis/java-bigtable/commit/ee0da11664d978e808d1088a419cdbd2270da147))
  * Send feature flag when flow control is enabled ([#1731](https://github.com/googleapis/java-bigtable/issues/1731)) ([ba147c3](https://github.com/googleapis/java-bigtable/commit/ba147c3520be27f4f3e622f3ef69fab716895dbe))



##### Bug Fixes

  * Add feature flag proto to BUILD file ([#1726](https://github.com/googleapis/java-bigtable/issues/1726)) ([7e5c646](https://github.com/googleapis/java-bigtable/commit/7e5c646031de22c42bb3dd81774ccd6762bd91ed))



## May 01, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.21.0](https://github.com/googleapis/java-bigtable/compare/v2.20.4...v2.21.0) (2023-04-27)

##### Features

  * Track the latency a request is queued on the grpc channel ([#1604](https://github.com/googleapis/java-bigtable/issues/1604)) ([bf3e7dd](https://github.com/googleapis/java-bigtable/commit/bf3e7dd58170bd058cedba8eea69b8c412ae68d3))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.17.0 ([#1722](https://github.com/googleapis/java-bigtable/issues/1722)) ([c6f7767](https://github.com/googleapis/java-bigtable/commit/c6f776730bd1d78489be69d09744782e8b46c9b0))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.8.0 ([#1720](https://github.com/googleapis/java-bigtable/issues/1720)) ([aa230b5](https://github.com/googleapis/java-bigtable/commit/aa230b5be4e282ccaa506d360ce95fdbe58ed4bb))



## April 24, 2023

Change

Cloud Bigtable is not available in the `europe-west12` (Turin) region.

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.20.4](https://github.com/googleapis/java-bigtable/compare/v2.20.3...v2.20.4) (2023-04-17)

##### Documentation

  * Make delete examples consistent with other languages ([#1710](https://github.com/googleapis/java-bigtable/issues/1710)) ([2d80188](https://github.com/googleapis/java-bigtable/commit/2d80188c65f454e037b758426b8747b5992db0de))



##### Dependencies

  * Update actions/setup-go action to v4 ([#1700](https://github.com/googleapis/java-bigtable/issues/1700)) ([1fd13ba](https://github.com/googleapis/java-bigtable/commit/1fd13ba9fdfa0322ee419f405c92ebe3979d85c7))
  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.16.0 ([#1712](https://github.com/googleapis/java-bigtable/issues/1712)) ([f3bb088](https://github.com/googleapis/java-bigtable/commit/f3bb088cd670805e5c6975e7154ee7e1e320acc6))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.21 ([#1704](https://github.com/googleapis/java-bigtable/issues/1704)) ([d60c946](https://github.com/googleapis/java-bigtable/commit/d60c94630f60d01241eecf9e3061ed197435b55e))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.21 ([#1705](https://github.com/googleapis/java-bigtable/issues/1705)) ([8f3d69d](https://github.com/googleapis/java-bigtable/commit/8f3d69d2498a7c0b5f760a40054e17d07502764d))
  * Update shared dependencies ([#1703](https://github.com/googleapis/java-bigtable/issues/1703)) ([076b411](https://github.com/googleapis/java-bigtable/commit/076b411b3c834c4ed1b98551f08befab78743c8f))
  * Upgrade maven-enforcer-plugin to 3.3.0, remove duplicate entry in pom ([#1702](https://github.com/googleapis/java-bigtable/issues/1702)) ([392fc69](https://github.com/googleapis/java-bigtable/commit/392fc697b9b75d172ba5bfd98ead45a6074c47f7))



## April 17, 2023

Announcement

The Cloud Bigtable documentation has been updated to include guidance on deleting data. For details, see [Deletes](https://docs.cloud.google.com/bigtable/docs/delete-data).

## April 10, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.20.3](https://github.com/googleapis/java-bigtable/compare/v2.20.2...v2.20.3) (2023-04-03)

##### Dependencies

  * Upgrade shared dependencies to 3.6.0 and monitoring to 3.15.0 ([#1688](https://github.com/googleapis/java-bigtable/issues/1688)) ([c0bad0d](https://github.com/googleapis/java-bigtable/commit/c0bad0d637179e0e8ed80e9716203ae8f11e5cb4))



## April 04, 2023

Announcement

The Cloud Bigtable documentation has been updated to include guidance on using regional endpoints. For details, see [Regional endpoints](https://docs.cloud.google.com/bigtable/docs/regional-endpoints).

## April 03, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.5.0](https://github.com/googleapis/nodejs-bigtable/compare/v4.4.0...v4.5.0) (2023-03-20)

##### Features

  * Add npm run compile to the testproxy command ([#1258](https://github.com/googleapis/nodejs-bigtable/issues/1258)) ([52c06a2](https://github.com/googleapis/nodejs-bigtable/commit/52c06a2684824f10e218856f632da7e4e252b2bf))



##### Bug Fixes

  * Always set the retry attempt to 0 for now ([#1251](https://github.com/googleapis/nodejs-bigtable/issues/1251)) ([5ee6f19](https://github.com/googleapis/nodejs-bigtable/commit/5ee6f19f6dd6fee0d48e692242e99c1966bb8df6))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.20.2](https://github.com/googleapis/java-bigtable/compare/v2.20.1...v2.20.2) (2023-03-29)

##### Bug Fixes

  * Higher application blocking latency precision ([#1676](https://github.com/googleapis/java-bigtable/issues/1676)) ([45ce93b](https://github.com/googleapis/java-bigtable/commit/45ce93bb52112391b9c3a90f10f51279839bea1b))
  * Make ChangeStreamRecord interface serializable ([#1685](https://github.com/googleapis/java-bigtable/issues/1685)) ([b97badb](https://github.com/googleapis/java-bigtable/commit/b97badbaa30588c578bfacc8183e77baaa656bd9))
  * Mark readRow requests as unary operations ([#1679](https://github.com/googleapis/java-bigtable/issues/1679)) ([f88bb67](https://github.com/googleapis/java-bigtable/commit/f88bb67a7a63450b8cd29f01660cf677ddfe436c))



## March 31, 2023

Feature

Cloud Bigtable instance and table metadata is now automatically synced to Data Catalog, a feature of Dataplex, for improved data discovery and governance. Metadata is not synced for a project with an organization policy that restricts resource locations. To get started, see [Manage data assets using Data Catalog](https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-data-catalog). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Change

You can now use Key Visualizer for Cloud Bigtable to analyze tables that are at least 1 GB. Previously, the minimum table size required for Key Visualizer was 30 GB. For more information on troubleshooting with Key Visualizer, see the [Key Visualizer overview](https://docs.cloud.google.com/bigtable/docs/keyvis-overview).

## March 27, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.20.1](https://github.com/googleapis/java-bigtable/compare/v2.20.0...v2.20.1) (2023-03-21)

##### Bug Fixes

  * If new_partitions is size 0, do not enforce size check ([#1673](https://github.com/googleapis/java-bigtable/issues/1673)) ([07bcfd9](https://github.com/googleapis/java-bigtable/commit/07bcfd9a0967f781fb8e5e0d764654dbf7bcda91))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.14.0 ([#1668](https://github.com/googleapis/java-bigtable/issues/1668)) ([06f9615](https://github.com/googleapis/java-bigtable/commit/06f96156705a2a7897a31d11dad864afe94de693))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.5.0 ([#1670](https://github.com/googleapis/java-bigtable/issues/1670)) ([74cebf3](https://github.com/googleapis/java-bigtable/commit/74cebf3a5ab58f3fd3ae95583ba2421b733deda8))



## March 23, 2023

Feature

Cloud Bigtable is now available in the `europe-west12` (Turin) region. This note is incorrect; see entry for  April 24, 2023.

## March 14, 2023

Change

When you restore a backup, if the destination cluster doesn't have enough nodes to store the new table, Cloud Bigtable returns a `FAILED_PRECONDITON` error message. Previously, a `RESOURCE_EXHAUSTED` error was returned.

## March 06, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.4.0](https://github.com/googleapis/nodejs-bigtable/compare/v4.3.0...v4.4.0) (2023-03-01)

##### Features

  * Add new_partitions field for CloseStream for Cloud Bigtable ChangeStream ([#1247](https://github.com/googleapis/nodejs-bigtable/issues/1247)) ([ecbdb52](https://github.com/googleapis/nodejs-bigtable/commit/ecbdb52ddc920bd493b284fb7d96b359a2f773f9))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.20.0](https://github.com/googleapis/java-bigtable/compare/v2.19.2...v2.20.0) (2023-03-02)

##### Features

  * Add getNewPartitions method to CloseStream for Bigtable ChangeStream ([#1655](https://github.com/googleapis/java-bigtable/issues/1655)) ([8847fed](https://github.com/googleapis/java-bigtable/commit/8847fed7f77ce4715c197ca1cfcc3108e0fa1004))
  * Add new_partitions field for CloseStream for Cloud Bigtable ChangeStream ([#1654](https://github.com/googleapis/java-bigtable/issues/1654)) ([0e283bf](https://github.com/googleapis/java-bigtable/commit/0e283bff0a12f5e4da8b0975d4bd747229c3780c))



##### Bug Fixes

  * Fix StackOverflow in ChangeStreamStateMachine due to excessive mods ([#1648](https://github.com/googleapis/java-bigtable/issues/1648)) ([9e11106](https://github.com/googleapis/java-bigtable/commit/9e1110600dc64defcd9143753f45b5b8226aa339))
  * Use org.threeten.bp.Duration for ReadChangeStreamQuery::heartbeatDura… ([#1652](https://github.com/googleapis/java-bigtable/issues/1652)) ([87261a9](https://github.com/googleapis/java-bigtable/commit/87261a977d6fc7877d7d253c67ea34c264f63f7c))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.13.0 ([#1656](https://github.com/googleapis/java-bigtable/issues/1656)) ([1c632ec](https://github.com/googleapis/java-bigtable/commit/1c632ec63987958e469e2b5861c29724c5cb8970))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.4.0 ([#1657](https://github.com/googleapis/java-bigtable/issues/1657)) ([c7a3e29](https://github.com/googleapis/java-bigtable/commit/c7a3e29dc717e2fa3d9b15f1ae9fb9f795d6f78a))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.17.0](https://github.com/googleapis/python-bigtable/compare/v2.16.0...v2.17.0) (2023-03-01)

##### Features

  * Add new_partitions field for CloseStream for Cloud Bigtable ChangeStream ([#740](https://github.com/googleapis/python-bigtable/issues/740)) ([1adcad4](https://github.com/googleapis/python-bigtable/commit/1adcad440368f6d7df6710a013e7fab076461aed))



#### [2.16.0](https://github.com/googleapis/python-bigtable/compare/v2.15.0...v2.16.0) (2023-02-27)

##### Features

  * Enable "rest" transport in Python for services supporting numeric enums ([c5116e0](https://github.com/googleapis/python-bigtable/commit/c5116e097aacf9ddae249de57fab1849aff10d86))
  * Publish the Cloud Bigtable Change Streams ([c5116e0](https://github.com/googleapis/python-bigtable/commit/c5116e097aacf9ddae249de57fab1849aff10d86))



##### Bug Fixes

  * Add context manager return types ([beb5bf3](https://github.com/googleapis/python-bigtable/commit/beb5bf3bca4b517d095de3faa17d20e4d89fb295))
  * **deps:** Require google-api-core>=1.34.0,>=2.11.0 ([c5116e0](https://github.com/googleapis/python-bigtable/commit/c5116e097aacf9ddae249de57fab1849aff10d86))



##### Documentation

  * Add documentation for enums ([beb5bf3](https://github.com/googleapis/python-bigtable/commit/beb5bf3bca4b517d095de3faa17d20e4d89fb295))



## February 27, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.19.2](https://github.com/googleapis/java-bigtable/compare/v2.19.1...v2.19.2) (2023-02-21)

##### Bug Fixes

  * Change types for Cloud Bigtable Changestream methods ([#1639](https://github.com/googleapis/java-bigtable/issues/1639)) ([908d70f](https://github.com/googleapis/java-bigtable/commit/908d70fdfa22e563031e2d8780b574ee7350cadc))



##### Dependencies

  * Update shared deps to 3.3.0 and monitoring to 3.12.0 ([#1643](https://github.com/googleapis/java-bigtable/issues/1643)) ([1a54fbf](https://github.com/googleapis/java-bigtable/commit/1a54fbf22490e5a83df0b0d73dc4b30472175102))



## February 20, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.3.0](https://github.com/googleapis/nodejs-bigtable/compare/v4.2.0...v4.3.0) (2023-02-10)

##### Features

  * Publish the Cloud Bigtable Change Streams ([#1237](https://github.com/googleapis/nodejs-bigtable/issues/1237)) ([000a353](https://github.com/googleapis/nodejs-bigtable/commit/000a353f05fa65bc0a7dc551c777ac55c6c08875))



##### Bug Fixes

  * Out of order read rows fix ([#1231](https://github.com/googleapis/nodejs-bigtable/issues/1231)) ([7dbaa6e](https://github.com/googleapis/nodejs-bigtable/commit/7dbaa6eebc5df6c073c78ff77f38b70c3e6f29d5))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.19.1](https://github.com/googleapis/java-bigtable/compare/v2.19.0...v2.19.1) (2023-02-16)

##### Bug Fixes

  * Change the return type of Heartbeat::getEstimatedLowWatermark to long ([#1631](https://github.com/googleapis/java-bigtable/issues/1631)) ([a101494](https://github.com/googleapis/java-bigtable/commit/a101494909226114fd951c94348878bf38453793))
  * Fix connectivity error count calculation ([#1632](https://github.com/googleapis/java-bigtable/issues/1632)) ([0803785](https://github.com/googleapis/java-bigtable/commit/0803785694874001a6ffbfe3245e84a23cb905ae))
  * **test:** Fix flaky test ([#1633](https://github.com/googleapis/java-bigtable/issues/1633)) ([fc29cd3](https://github.com/googleapis/java-bigtable/commit/fc29cd35101fd6a6262aea8648bc06bd20ce3d10))



##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.20 ([#1626](https://github.com/googleapis/java-bigtable/issues/1626)) ([0865023](https://github.com/googleapis/java-bigtable/commit/08650238a806367c94072b51029010272c966148))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.20 ([#1627](https://github.com/googleapis/java-bigtable/issues/1627)) ([782e81f](https://github.com/googleapis/java-bigtable/commit/782e81f6e64c1d8015fddf2219d590c77217584d))



## February 13, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.19.0](https://github.com/googleapis/java-bigtable/compare/v2.18.4...v2.19.0) (2023-02-10)

##### Features

  * Support Cloud Bigtable Changestream ([#1569](https://github.com/googleapis/java-bigtable/issues/1569)) ([c7b4fdf](https://github.com/googleapis/java-bigtable/commit/c7b4fdf70f02b89f178a130d7fdcfcf8b2a6b790))



##### Bug Fixes

  * Modify ConvertExceptionCallable to retry on Goaway ([#1588](https://github.com/googleapis/java-bigtable/issues/1588)) ([cf752ea](https://github.com/googleapis/java-bigtable/commit/cf752eaf3b5fb2cddb11a2fbb5acb5a72c9862c2))



##### Documentation

  * Fix javadoc code example for awaitOptimizeRestoredTableAsync ([#1617](https://github.com/googleapis/java-bigtable/issues/1617)) ([8b23bb9](https://github.com/googleapis/java-bigtable/commit/8b23bb93d40dbfd9591c7d7546216e2543f9f418))



#### [2.18.4](https://github.com/googleapis/java-bigtable/compare/v2.18.3...v2.18.4) (2023-02-06)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.11.0 ([#1609](https://github.com/googleapis/java-bigtable/issues/1609)) ([88be13e](https://github.com/googleapis/java-bigtable/commit/88be13e2db9635e124ed169850a18fc968895f2b))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.2.0 ([#1610](https://github.com/googleapis/java-bigtable/issues/1610)) ([15db117](https://github.com/googleapis/java-bigtable/commit/15db11712956410636fffcc827c971181fcad2ee))



## February 06, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.2.0](https://github.com/googleapis/nodejs-bigtable/compare/v4.1.1...v4.2.0) (2023-01-31)

##### Features

  * Added SuggestConversationSummary RPC ([#1182](https://github.com/googleapis/nodejs-bigtable/issues/1182)) ([355925e](https://github.com/googleapis/nodejs-bigtable/commit/355925ee519fa27e216a76c500ab8c94de1d2c96))



#### [4.1.1](https://github.com/googleapis/nodejs-bigtable/compare/v4.1.0...v4.1.1) (2023-01-30)

##### Bug Fixes

  * **deps:** Use google-gax v3.5.2 ([#1186](https://github.com/googleapis/nodejs-bigtable/issues/1186)) ([4b1dd6e](https://github.com/googleapis/nodejs-bigtable/commit/4b1dd6e8d0f1b215a3e8183e5893e9dd01c15eed))
  * Pipe metadata along ([#1178](https://github.com/googleapis/nodejs-bigtable/issues/1178)) ([0822e4d](https://github.com/googleapis/nodejs-bigtable/commit/0822e4d17d28e47b5377d6d3853a4c5bc125a2e9))



## January 30, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.18.3](https://github.com/googleapis/java-bigtable/compare/v2.18.2...v2.18.3) (2023-01-24)

##### Bug Fixes

  * Make channel priming work with batch endpoint ([#1600](https://github.com/googleapis/java-bigtable/issues/1600)) ([133c7e5](https://github.com/googleapis/java-bigtable/commit/133c7e50a5a84e880f23cfc7ed88ea2250a2994d))



#### [2.18.2](https://github.com/googleapis/java-bigtable/compare/v2.18.1...v2.18.2) (2023-01-24)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.10.0 ([#1597](https://github.com/googleapis/java-bigtable/issues/1597)) ([1724d4e](https://github.com/googleapis/java-bigtable/commit/1724d4ee6b63085b035082bd299668ceadd8bd01))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.2 ([#1595](https://github.com/googleapis/java-bigtable/issues/1595)) ([e466191](https://github.com/googleapis/java-bigtable/commit/e466191ef8562b767218dcd4811a271ec6e98257))



## January 23, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.18.1](https://github.com/googleapis/java-bigtable/compare/v2.18.0...v2.18.1) (2023-01-17)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.9.0 ([#1579](https://github.com/googleapis/java-bigtable/issues/1579)) ([70c0500](https://github.com/googleapis/java-bigtable/commit/70c050001379214d5577a896e280d04101891a08))



## January 18, 2023

Announcement

Client-side metrics are now available to customers who use the Cloud Bigtable HBase client for Java version 2.6.4 or later. To learn more about using client-side monitoring metrics for performance optimization and troubleshooting, see the [Client-side metrics overview](https://docs.cloud.google.com/bigtable/docs/client-side-metrics).

## January 16, 2023

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.18.0](https://github.com/googleapis/java-bigtable/compare/v2.17.1...v2.18.0) (2023-01-12)

##### Features

  * Enable channel priming by default ([#1555](https://github.com/googleapis/java-bigtable/issues/1555)) ([303959c](https://github.com/googleapis/java-bigtable/commit/303959cc88e8cf164a45026d79de67e3f58d09fe))



##### Bug Fixes

  * Call attemptStarted method with the request ([#1562](https://github.com/googleapis/java-bigtable/issues/1562)) ([325f09c](https://github.com/googleapis/java-bigtable/commit/325f09c9e257d53871a9071e6bfcbb0887298641))
  * Defer instance admin api errors to RPC time rather then client construction time ([#1576](https://github.com/googleapis/java-bigtable/issues/1576)) ([06a0ced](https://github.com/googleapis/java-bigtable/commit/06a0ced03dbac91145bac6d5d01f327c3ff4a83f))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.1 ([#1572](https://github.com/googleapis/java-bigtable/issues/1572)) ([a68fb80](https://github.com/googleapis/java-bigtable/commit/a68fb8028a338b937b4baf8c50fad1080e137849))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.9.2 ([#1573](https://github.com/googleapis/java-bigtable/issues/1573)) ([e1362aa](https://github.com/googleapis/java-bigtable/commit/e1362aa4e47b2da089b21a8cfd124d7e935af8de))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.15.0](https://github.com/googleapis/python-bigtable/compare/v2.14.1...v2.15.0) (2023-01-10)

##### Features

  * Add support for python 3.11 ([#718](https://github.com/googleapis/python-bigtable/issues/718)) ([803a15e](https://github.com/googleapis/python-bigtable/commit/803a15ef0cd3713411eeb5d21258c12bbe1dcab6))



## December 19, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.17.1](https://github.com/googleapis/java-bigtable/compare/v2.17.0...v2.17.1) (2022-12-13)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.8.0 ([#1548](https://github.com/googleapis/java-bigtable/issues/1548)) ([48f136d](https://github.com/googleapis/java-bigtable/commit/48f136dc1422d601d5470a33763e37514cf620de))



## December 12, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.17.0](https://github.com/googleapis/java-bigtable/compare/v2.16.0...v2.17.0) (2022-12-07)

##### Features

  * Add a query paginator ([#1530](https://github.com/googleapis/java-bigtable/issues/1530)) ([5c8e1f6](https://github.com/googleapis/java-bigtable/commit/5c8e1f656b15177ecef4709b9e502cef58cca479))
  * Add test proxy to java-bigtable client ([#1498](https://github.com/googleapis/java-bigtable/issues/1498)) ([132b4e4](https://github.com/googleapis/java-bigtable/commit/132b4e4fe340ca316de8eef2e2133b6dabd9dec3))
  * Implement cross-project table restore ([#1536](https://github.com/googleapis/java-bigtable/issues/1536)) ([335977c](https://github.com/googleapis/java-bigtable/commit/335977c499b1776c8fa861d13195ffc49e468e0a))
  * Next release from main branch is 2.17.0 ([#1514](https://github.com/googleapis/java-bigtable/issues/1514)) ([4fc6a93](https://github.com/googleapis/java-bigtable/commit/4fc6a93a25362df7bc107d48f94e1c00b6bd608d))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom … ([#1531](https://github.com/googleapis/java-bigtable/issues/1531)) ([ee98338](https://github.com/googleapis/java-bigtable/commit/ee9833835a84cee202b142950b28704db682ac0c))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.1.0 ([#1539](https://github.com/googleapis/java-bigtable/issues/1539)) ([3244cef](https://github.com/googleapis/java-bigtable/commit/3244cefd4d77a44bab6ccaa8f5c03e3d31575625))
  * Update dependency kr.motd.maven:os-maven-plugin to v1.7.1 ([#1518](https://github.com/googleapis/java-bigtable/issues/1518)) ([8309681](https://github.com/googleapis/java-bigtable/commit/830968109a3754a12bd0bc92674fe42ae529b924))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.19 ([#1537](https://github.com/googleapis/java-bigtable/issues/1537)) ([7f7c478](https://github.com/googleapis/java-bigtable/commit/7f7c478a2163c46d10ed39ea3c1b046f971d4569))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.19 ([#1538](https://github.com/googleapis/java-bigtable/issues/1538)) ([9d3df57](https://github.com/googleapis/java-bigtable/commit/9d3df57d7bfeafd9cbcf56ecd58b52cc1b14ba7b))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.14.1](https://github.com/googleapis/python-bigtable/compare/v2.14.0...v2.14.1) (2022-12-06)

##### Bug Fixes

  * **Deps:** Require google-api-core >=1.34.0, >=2.11.0 ([e5875cb](https://github.com/googleapis/python-bigtable/commit/e5875cbe8551329fbb64f273ca21d6b7ada641ec))
  * Drop usage of pkg_resources ([e5875cb](https://github.com/googleapis/python-bigtable/commit/e5875cbe8551329fbb64f273ca21d6b7ada641ec))
  * Fix timeout default values ([e5875cb](https://github.com/googleapis/python-bigtable/commit/e5875cbe8551329fbb64f273ca21d6b7ada641ec))



##### Documentation

  * **Samples:** Snippetgen should call await on the operation coroutine before calling result ([e5875cb](https://github.com/googleapis/python-bigtable/commit/e5875cbe8551329fbb64f273ca21d6b7ada641ec))



## December 08, 2022

Feature

Cloud Bigtable now lets you restore from a backup to a different project. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). To learn more, see [Bigtable backups](https://docs.cloud.google.com/bigtable/docs/backups).

Feature

The ability to configure deletion protection for a Cloud Bigtable table is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). This setting prevents deletion of the table, its column families, and the instance containing the table. See [Modify deletion protection](https://docs.cloud.google.com/bigtable/docs/managing-tables#modify-deletion-protection) for instructions.

## December 07, 2022

Feature

You can now retrieve information about a Cloud Bigtable query to help you evaluate the query's performance. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Get query stats](https://docs.cloud.google.com/bigtable/docs/query-stats).

## December 05, 2022

Feature

A new suite of client-side metrics for the Cloud Bigtable client for Java is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) in versions 2.16.0 and later. To learn more about using the new monitoring metrics for performance optimization and troubleshooting, see the [Client-side metrics overview](https://docs.cloud.google.com/bigtable/docs/client-side-metrics).

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.14.0](https://github.com/googleapis/python-bigtable/compare/v2.13.2...v2.14.0) (2022-11-30)

##### Features

  * Add typing to proto.Message based class attributes ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
  * Remove enum value ReadRowsRequest.RequestStatsView.REQUEST_STATS_EFFICIENCY ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
  * Remove field ReadIterationStats.deletes_seen ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
  * Remove field RequestStats.read_efficiency_stats ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
  * Remove proto ReadEfficiencyStats ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
  * Rename field RequestStats.all_read_stats to full_read_stats_view ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
  * Rename proto AllReadStats to FullReadStatsView ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))
  * Rename proto ReadIteratorStats to ReadIterationStats ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))



##### Bug Fixes

  * Add dict typing for client_options ([c1538d5](https://github.com/googleapis/python-bigtable/commit/c1538d5c5a001a9febb4b466d3d09fd1fd167f66))



## November 21, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [1.7.3](https://github.com/googleapis/python-bigtable/compare/v1.7.2...v1.7.3) (2022-11-18)

##### Bug Fixes

  * First pass on making retry configuration more consistent ([#695](https://github.com/googleapis/python-bigtable/issues/695)) ([c707c30](https://github.com/googleapis/python-bigtable/commit/c707c309a4095e14ecc678f327d417d5a2a55243))
  * Make internal rst_stream errors retriable ([#699](https://github.com/googleapis/python-bigtable/issues/699)) ([770feb8](https://github.com/googleapis/python-bigtable/commit/770feb840c5bc30ebf30447e9460d581c1a5c5b0))
  * Make sure that the proper exception type is bubbled up for ReadRows ([#696](https://github.com/googleapis/python-bigtable/issues/696)) ([5c72780](https://github.com/googleapis/python-bigtable/commit/5c727802ea55611a103bca1d4fff2a3d305be758))
  * Prevent sending full table scan when retrying (backport [#554](https://github.com/googleapis/python-bigtable/issues/554)) ([#697](https://github.com/googleapis/python-bigtable/issues/697)) ([c4ae6ad](https://github.com/googleapis/python-bigtable/commit/c4ae6ad5d2ce8e495250b1df41a4ba1877dacca2))



## November 15, 2022

Feature

Cloud Bigtable now lets you retrieve metadata about a table, giving you greater observability when troubleshooting. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Table stats](https://docs.cloud.google.com/bigtable/docs/table-stats).

## November 14, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.16.0](https://github.com/googleapis/java-bigtable/compare/v2.15.1...v2.16.0) (2022-11-11)

##### Features

  * Remove proto ReadEfficiencyStats ([#1455](https://github.com/googleapis/java-bigtable/issues/1455)) ([f6b243d](https://github.com/googleapis/java-bigtable/commit/f6b243db39c0370f0d9a4e47e553cfe62493b240))



##### Bug Fixes

  * Fix metric client settings ([#1509](https://github.com/googleapis/java-bigtable/issues/1509)) ([38ac115](https://github.com/googleapis/java-bigtable/commit/38ac115af07432e9c178064b59729a0b358105cd))



#### [2.15.1](https://github.com/googleapis/java-bigtable/compare/v2.15.0...v2.15.1) (2022-11-08)

##### Bug Fixes

  * Call record attempt compeletion on permanent failures ([#1502](https://github.com/googleapis/java-bigtable/issues/1502)) ([f409c47](https://github.com/googleapis/java-bigtable/commit/f409c4769b526b38590671178c007a9c57f9c182))
  * Fix the connectivity error count caculation ([#1401](https://github.com/googleapis/java-bigtable/issues/1401)) ([1f8cfd7](https://github.com/googleapis/java-bigtable/commit/1f8cfd722c749a8d3e30572fbdda6a2e3594d7a6))
  * Only record retry count when it's > 0 ([#1488](https://github.com/googleapis/java-bigtable/issues/1488)) ([445a667](https://github.com/googleapis/java-bigtable/commit/445a66737b45835444b26261b6f017f7fc278f45))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.6 ([#1501](https://github.com/googleapis/java-bigtable/issues/1501)) ([8f61c64](https://github.com/googleapis/java-bigtable/commit/8f61c64aba815a942daae17ccb024d325c03df8a))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.17 ([#1495](https://github.com/googleapis/java-bigtable/issues/1495)) ([1b7c21a](https://github.com/googleapis/java-bigtable/commit/1b7c21abc793db0e4706f119e934eecdcfce9994))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.17 ([#1496](https://github.com/googleapis/java-bigtable/issues/1496)) ([74779e3](https://github.com/googleapis/java-bigtable/commit/74779e3621c9893bf3a84dc68ddcb624785c8d71))



#### [1.22.0-sp.4](https://github.com/googleapis/java-bigtable/compare/v1.22.0-sp.3...v1.22.0-sp.4) (2022-11-08)

##### Dependencies

  * Regenerating with new Protobuf (1.22.0-sp) ([#1491](https://github.com/googleapis/java-bigtable/issues/1491)) ([b31cafd](https://github.com/googleapis/java-bigtable/commit/b31cafd1d05d2b4727504e04ebc70ad79d41e1cb))



## October 31, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.15.0](https://github.com/googleapis/java-bigtable/compare/v2.14.1...v2.15.0) (2022-10-26)

##### Features

  * Add APIs for Mutation and RowMutationEntry ([#1454](https://github.com/googleapis/java-bigtable/issues/1454)) ([a86934f](https://github.com/googleapis/java-bigtable/commit/a86934f4f70e1998e7368688df8695a4bac7006e))



##### Bug Fixes

  * Catch all throwables so version mismatch won't hang the client ([#1402](https://github.com/googleapis/java-bigtable/issues/1402)) ([c03b8a4](https://github.com/googleapis/java-bigtable/commit/c03b8a4245beab7258b8ed8ec76153e6a0275211))
  * Fix attempt status tag for metrics ([#1477](https://github.com/googleapis/java-bigtable/issues/1477)) ([e54cf7d](https://github.com/googleapis/java-bigtable/commit/e54cf7d61128049cea2817b409a8524636b4a6cf))
  * Rename metric names to match the external name ([#1479](https://github.com/googleapis/java-bigtable/issues/1479)) ([28ca7c3](https://github.com/googleapis/java-bigtable/commit/28ca7c310d9a157529555ab6865f89802161443b))
  * Set a longer timeout to wait for callbacks to be executed ([#1478](https://github.com/googleapis/java-bigtable/issues/1478)) ([0d9ff6a](https://github.com/googleapis/java-bigtable/commit/0d9ff6ab3bd5bf853f1d371312036b14c924ae5e))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.5.0 ([#1464](https://github.com/googleapis/java-bigtable/issues/1464)) ([d8e58a5](https://github.com/googleapis/java-bigtable/commit/d8e58a5d88de7ea249d7bc141f1ac65592088da6))
  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.6.0 ([#1476](https://github.com/googleapis/java-bigtable/issues/1476)) ([331dcfb](https://github.com/googleapis/java-bigtable/commit/331dcfbd06ab578cfe9673ca70cab1f6abd5ddcd))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.5 ([#1470](https://github.com/googleapis/java-bigtable/issues/1470)) ([557a4fb](https://github.com/googleapis/java-bigtable/commit/557a4fbed77157c3ccfc3e84a0c952b647844f9b))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.15 ([#1462](https://github.com/googleapis/java-bigtable/issues/1462)) ([69540cb](https://github.com/googleapis/java-bigtable/commit/69540cb2df25d5fb716e81e7513930b01c310b72))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.16 ([#1467](https://github.com/googleapis/java-bigtable/issues/1467)) ([53599ca](https://github.com/googleapis/java-bigtable/commit/53599caa0f92bad1365adbc4b58a1dcb1e8a393e))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.15 ([#1463](https://github.com/googleapis/java-bigtable/issues/1463)) ([a6612f9](https://github.com/googleapis/java-bigtable/commit/a6612f90cd4a0ec9589ca797ff3a42d23478a6e6))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.16 ([#1468](https://github.com/googleapis/java-bigtable/issues/1468)) ([fe0ddb1](https://github.com/googleapis/java-bigtable/commit/fe0ddb1b183cfdf368c2387a645a613bbfd52a69))



## October 24, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.13.2](https://github.com/googleapis/python-bigtable/compare/v2.13.1...v2.13.2) (2022-10-20)

##### Bug Fixes

  * Respect deadlines for column family operations ([#687](https://github.com/googleapis/python-bigtable/issues/687)) ([df2e64a](https://github.com/googleapis/python-bigtable/commit/df2e64a79bbd8b28d0991706607af99d539320d1))



## October 17, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.6.3](https://github.com/googleapis/java-bigtable/compare/v2.6.2...v2.6.3) (2022-10-14)

##### Dependencies

  * Regenerating with new Protobuf (v2.6.x) ([#1459](https://github.com/googleapis/java-bigtable/issues/1459)) ([3d330ca](https://github.com/googleapis/java-bigtable/commit/3d330ca33cc807437bd3e1f8de15ba5e4b053c28))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.13.1](https://github.com/googleapis/python-bigtable/compare/v2.13.0...v2.13.1) (2022-10-10)

##### Bug Fixes

  * **Deps:** Allow protobuf 3.19.5 ([#682](https://github.com/googleapis/python-bigtable/issues/682)) ([0bb3420](https://github.com/googleapis/python-bigtable/commit/0bb3420decac74058ee099d72f8932556409f2aa))



## October 10, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.14.1](https://github.com/googleapis/java-bigtable/compare/v2.14.0...v2.14.1) (2022-10-05)

##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.4.6 ([#1450](https://github.com/googleapis/java-bigtable/issues/1450)) ([96b1e80](https://github.com/googleapis/java-bigtable/commit/96b1e80af5e17689a84318e9a797195cde3dab45))



#### [2.14.0](https://github.com/googleapis/java-bigtable/compare/v2.13.0...v2.14.0) (2022-10-03)

##### Features

  * Publish the RequestStats proto ([#1400](https://github.com/googleapis/java-bigtable/issues/1400)) ([e989200](https://github.com/googleapis/java-bigtable/commit/e989200980510b14d602925df7430e01bc2f8db7))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.4 ([#1446](https://github.com/googleapis/java-bigtable/issues/1446)) ([81034c5](https://github.com/googleapis/java-bigtable/commit/81034c51722d973cf5545feb33665b4e08265303))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.13.0](https://github.com/googleapis/python-bigtable/compare/v2.12.0...v2.13.0) (2022-09-29)

##### Features

  * Publish the RequestStats proto ([#676](https://github.com/googleapis/python-bigtable/issues/676)) ([199949b](https://github.com/googleapis/python-bigtable/commit/199949b2a930706654680b91a93f2a903bf112bf))



##### Bug Fixes

  * **Deps:** Require protobuf >= 3.20.2 ([#679](https://github.com/googleapis/python-bigtable/issues/679)) ([030ef38](https://github.com/googleapis/python-bigtable/commit/030ef3868c442a8a21c4b4d6217b99cab09a1be7))



## October 03, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.1.0](https://github.com/googleapis/nodejs-bigtable/compare/v4.0.5...v4.1.0) (2022-09-26)

##### Features

  * Publish the RequestStats proto ([#1177](https://github.com/googleapis/nodejs-bigtable/issues/1177)) ([89dfc83](https://github.com/googleapis/nodejs-bigtable/commit/89dfc83b4fed199d70934c34ab7f4c4d17796418))



#### [4.0.5](https://github.com/googleapis/nodejs-bigtable/compare/v4.0.4...v4.0.5) (2022-09-23)

##### Bug Fixes

  * Test is less restrictive to allow changes ([#1160](https://github.com/googleapis/nodejs-bigtable/issues/1160)) ([7d05b96](https://github.com/googleapis/nodejs-bigtable/commit/7d05b96f0adcbcdab2598ea52bc6a60005c7251b))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.13.0](https://github.com/googleapis/java-bigtable/compare/v2.12.0...v2.13.0) (2022-09-27)

##### Features

  * Add gRPC RLS dependency ([#1248](https://github.com/googleapis/java-bigtable/issues/1248)) ([e829b92](https://github.com/googleapis/java-bigtable/commit/e829b923d97a00dcb55a14b0877bec2c8cf5ece2))



##### Bug Fixes

  * Add a UUID in the task value ([#1430](https://github.com/googleapis/java-bigtable/issues/1430)) ([3bfc7bc](https://github.com/googleapis/java-bigtable/commit/3bfc7bc246488a37b4470e3a75ffdd34f6761804))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.4.5 ([#1406](https://github.com/googleapis/java-bigtable/issues/1406)) ([d906729](https://github.com/googleapis/java-bigtable/commit/d906729a4bb9a51907bf4879e8d063d5103565ac))
  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.14 ([#1411](https://github.com/googleapis/java-bigtable/issues/1411)) ([ef7d741](https://github.com/googleapis/java-bigtable/commit/ef7d7419293f9f046dcf941148a86da713feae17))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.14 ([#1412](https://github.com/googleapis/java-bigtable/issues/1412)) ([dcae319](https://github.com/googleapis/java-bigtable/commit/dcae3195871b78aa6e102c4bc570b18c303c7760))
  * Update dependency org.junit.vintage:junit-vintage-engine to v5.9.1 ([#1409](https://github.com/googleapis/java-bigtable/issues/1409)) ([c1e195d](https://github.com/googleapis/java-bigtable/commit/c1e195d4e0470b30d97231c44b09fcb5c4881514))



## September 29, 2022

Feature

The Cloud Bigtable observability metric `high-granularity CPU utilization of hottest node` is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). Because of more frequent sampling, this metric is more accurate than `CPU utilization of hottest node`. For more information on using Bigtable metrics, see [Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

## September 19, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.0.4](https://github.com/googleapis/nodejs-bigtable/compare/v4.0.3...v4.0.4) (2022-09-14)

##### Bug Fixes

  * Use grpc-gcp v1.0.0 ([#1156](https://github.com/googleapis/nodejs-bigtable/issues/1156)) ([6196424](https://github.com/googleapis/nodejs-bigtable/commit/61964246cc79b0cb70f18d6bc1e524c01fdd51b0))



#### [4.0.3](https://github.com/googleapis/nodejs-bigtable/compare/v4.0.2...v4.0.3) (2022-09-09)

##### Bug Fixes

  * Update dependency uuid to v9 ([#1152](https://github.com/googleapis/nodejs-bigtable/issues/1152)) ([dea0425](https://github.com/googleapis/nodejs-bigtable/commit/dea0425df05218cf7fb42e4ef72f3952782f7bbb))
  * Wait for instances to get created in all samples ([#1149](https://github.com/googleapis/nodejs-bigtable/issues/1149)) ([c9dd9c6](https://github.com/googleapis/nodejs-bigtable/commit/c9dd9c614b963763b361394332ad227a86eb0de9))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.12.0](https://github.com/googleapis/java-bigtable/compare/v2.11.2...v2.12.0) (2022-09-15)

##### Features

  * **generated:** Publish CBT deletion_protection field in Table, UpdateTableRequest, and UpdateTable API ([f1f3f05](https://github.com/googleapis/java-bigtable/commit/f1f3f05ae2dc84a8dc853eb5467fbd157b7293c3))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.4.3 ([#1386](https://github.com/googleapis/java-bigtable/issues/1386)) ([f460373](https://github.com/googleapis/java-bigtable/commit/f460373eb74776fae1787b74392b508643e6139f))
  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.4.3 ([#1387](https://github.com/googleapis/java-bigtable/issues/1387)) ([e339cb1](https://github.com/googleapis/java-bigtable/commit/e339cb186289fa53a0d65c3d77fb7edbae737882))
  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.4.4 ([#1395](https://github.com/googleapis/java-bigtable/issues/1395)) ([a2db183](https://github.com/googleapis/java-bigtable/commit/a2db183dea46cd83ea70bb89848e0579b9c61fac))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.2 ([#1384](https://github.com/googleapis/java-bigtable/issues/1384)) ([ee3b256](https://github.com/googleapis/java-bigtable/commit/ee3b256a62c2665e2c4230d9acfc14c3d5c2aebf))
  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3.0.3 ([#1393](https://github.com/googleapis/java-bigtable/issues/1393)) ([df6c6c7](https://github.com/googleapis/java-bigtable/commit/df6c6c79715ecc7b99e026ce8dfa8645765fc9d5))



## September 13, 2022

Feature

Cloud Bigtable is available in the `me-west1` (Tel Aviv) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## September 12, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.11.2](https://github.com/googleapis/java-bigtable/compare/v2.11.1...v2.11.2) (2022-09-07)

##### Bug Fixes

  * Make cloud-monitoring a runtime dependency ([#1371](https://github.com/googleapis/java-bigtable/issues/1371)) ([930d043](https://github.com/googleapis/java-bigtable/commit/930d0439086d2b43735f9583175adf0626952c9b))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.4.2 ([#1373](https://github.com/googleapis/java-bigtable/issues/1373)) ([43b8052](https://github.com/googleapis/java-bigtable/commit/43b80523cc00932a414702ad96cfd86984c0f649))
  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.4.2 ([#1374](https://github.com/googleapis/java-bigtable/issues/1374)) ([4174f0d](https://github.com/googleapis/java-bigtable/commit/4174f0dc1b61f954ccd1c2fcf88066179a4d430b))



## September 05, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Node.js

### Changes for [@google-cloud/bigtable](https://github.com/googleapis/nodejs-bigtable)

#### [4.0.2](https://github.com/googleapis/nodejs-bigtable/compare/v4.0.1...v4.0.2) (2022-08-27)

##### Bug Fixes

  * Add operation ([#1145](https://github.com/googleapis/nodejs-bigtable/issues/1145)) ([3a1e282](https://github.com/googleapis/nodejs-bigtable/commit/3a1e2827990729df078fe1d075c100ace1833a96))
  * Do not import whole google-gax from proto JS ([#1553](https://github.com/googleapis/nodejs-bigtable/issues/1553)) ([#1148](https://github.com/googleapis/nodejs-bigtable/issues/1148)) ([262d3d7](https://github.com/googleapis/nodejs-bigtable/commit/262d3d729211da7fa23043c64de59ba67de2ce5b))
  * Use google-gax v3.3.0 ([262d3d7](https://github.com/googleapis/nodejs-bigtable/commit/262d3d729211da7fa23043c64de59ba67de2ce5b))



### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.11.1](https://github.com/googleapis/java-bigtable/compare/v2.11.0...v2.11.1) (2022-08-26)

##### Bug Fixes

  * Reset a measure map every time the stats are recorded ([#1364](https://github.com/googleapis/java-bigtable/issues/1364)) ([1683365](https://github.com/googleapis/java-bigtable/commit/1683365938178bb61b1e9c871f1971449ee942c2))



## August 29, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.11.0](https://github.com/googleapis/java-bigtable/compare/v2.10.3...v2.11.0) (2022-08-17)

##### Features

  * Add Stackdriver exporter ([#1247](https://github.com/googleapis/java-bigtable/issues/1247)) ([7ce915e](https://github.com/googleapis/java-bigtable/commit/7ce915e34c1ccce30bee78bda9e024a620cde737))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-monitoring-bom to v3.4.1 ([#1352](https://github.com/googleapis/java-bigtable/issues/1352)) ([f8d97e5](https://github.com/googleapis/java-bigtable/commit/f8d97e557318eab214f3d916c029bfa153cf7455))



## August 22, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.11.3](https://github.com/googleapis/python-bigtable/compare/v2.11.2...v2.11.3) (2022-08-17)

##### Performance Improvements

  * Optimize row merging ([#628](https://github.com/googleapis/python-bigtable/issues/628)) ([c71ec70](https://github.com/googleapis/python-bigtable/commit/c71ec70e55f6e236e46127870a9ed4717eee5da5))



#### [2.11.2](https://github.com/googleapis/python-bigtable/compare/v2.11.1...v2.11.2) (2022-08-11)

##### Bug Fixes

  * **Deps:** allow protobuf < 5.0.0 ([#631](https://github.com/googleapis/python-bigtable/issues/631)) ([fd54fc6](https://github.com/googleapis/python-bigtable/commit/fd54fc63340a3e01fae1ccc4c648dd90900f8a94))
  * **Deps:** require proto-plus >= 1.22.0 ([fd54fc6](https://github.com/googleapis/python-bigtable/commit/fd54fc63340a3e01fae1ccc4c648dd90900f8a94))



## August 19, 2022

Feature

You can now use tags to allow or deny security policies on a Cloud Bigtable instance. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). To learn more, see [Create and manage tags](https://docs.cloud.google.com/bigtable/docs/tags).

## August 15, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.10.3](https://github.com/googleapis/java-bigtable/compare/v2.10.2...v2.10.3) (2022-08-08)

##### Bug Fixes

  * Declare 2 http libraries as runtime ([#1341](https://github.com/googleapis/java-bigtable/issues/1341)) ([8071de6](https://github.com/googleapis/java-bigtable/commit/8071de6235a6c1aa5873902ca55beaa2a8d64276))



#### [2.10.2](https://github.com/googleapis/java-bigtable/compare/v2.10.1...v2.10.2) (2022-08-03)

##### Bug Fixes

  * Add a ReadFirstRow callable to set future in onComplete ([#1326](https://github.com/googleapis/java-bigtable/issues/1326)) ([cb539b5](https://github.com/googleapis/java-bigtable/commit/cb539b50d98ec2a8538ce4691b2639426ca95464))
  * The metadata could be returned in trailer or header depends on i… ([#1337](https://github.com/googleapis/java-bigtable/issues/1337)) ([c4b8c03](https://github.com/googleapis/java-bigtable/commit/c4b8c03ece7b3f6ec2cea42ff0ca5ac617528060))



##### Dependencies

  * Update dependency com.google.cloud:google-cloud-shared-dependencies to v3 ([#1328](https://github.com/googleapis/java-bigtable/issues/1328)) ([bee0ca0](https://github.com/googleapis/java-bigtable/commit/bee0ca036ab6e711f6069159364f6d3b691e6bfd))
  * Upgrade shared config to 1.5.3, exclude google-http-client and google-http-client-gson from gax in google-cloud-bigtable-stats ([#1336](https://github.com/googleapis/java-bigtable/issues/1336)) ([98b3349](https://github.com/googleapis/java-bigtable/commit/98b33498d85325d22737fb4bd66826519e96755a))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.11.1](https://github.com/googleapis/python-bigtable/compare/v2.11.0...v2.11.1) (2022-08-08)

##### Bug Fixes

  * Retry the RST Stream error in mutate rows and read rows([#624](https://github.com/googleapis/python-bigtable/issues/624)) ([d24574a](https://github.com/googleapis/python-bigtable/commit/d24574a722de61bdeffa6588bcb08f56e62ba3bd))



## August 12, 2022

Feature

Cloud Bigtable-BigQuery federation is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). You can use BigQuery to query data from Cloud Bigtable and blend it with data from other federated data sources. For more information, see [Querying Cloud Bigtable data](https://docs.cloud.google.com/bigquery/docs/external-data-bigtable).

## August 11, 2022

Feature

New tooling is available to help you migrate to Cloud Bigtable from HBase clusters that are hosted on another Google Cloud service. For more information, see [Migrate from HBase on Google Cloud](https://docs.cloud.google.com/bigtable/docs/migrate-hbase-on-google-cloud-to-bigtable).

## August 08, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.10.1](https://github.com/googleapis/java-bigtable/compare/v2.10.0...v2.10.1) (2022-08-01)

##### Bug Fixes

  * Retry rst stream in mutations ([#1327](https://github.com/googleapis/java-bigtable/issues/1327)) ([1a5b3a2](https://github.com/googleapis/java-bigtable/commit/1a5b3a215b5388678241cadec26a962a512157ac))



##### Dependencies

  * Update dependency `org.junit.vintage:junit-vintage-engine` to v5.9.0 ([#1323](https://github.com/googleapis/java-bigtable/issues/1323)) ([7655747](https://github.com/googleapis/java-bigtable/commit/76557476744a6404b9df30c97c59f0a7e38a1ed8))



### Python

### Changes for [google-cloud-bigtable](https://github.com/googleapis/python-bigtable)

#### [2.11.0](https://github.com/googleapis/python-bigtable/compare/v2.10.1...v2.11.0) (2022-08-04)

##### Features

  * Add audience parameter ([a7a7699](https://github.com/googleapis/python-bigtable/commit/a7a76998fad3c12215527e4ebb517a1526cc152e))
  * Add `satisfies_pzs` output-only field ([#614](https://github.com/googleapis/python-bigtable/issues/614)) ([7dc1469](https://github.com/googleapis/python-bigtable/commit/7dc1469fef2dc38f1509b35a37e9c97381ab7601))
  * Add `storage_utilization_gib_per_node` to Autoscaling target ([a7a7699](https://github.com/googleapis/python-bigtable/commit/a7a76998fad3c12215527e4ebb517a1526cc152e))
  * Cloud Bigtable Undelete Table service and message proto files ([a7a7699](https://github.com/googleapis/python-bigtable/commit/a7a76998fad3c12215527e4ebb517a1526cc152e))



##### Bug Fixes

  * **Deps:** require `google-api-core` >=1.32.0 and >=2.8.0 ([a7a7699](https://github.com/googleapis/python-bigtable/commit/a7a76998fad3c12215527e4ebb517a1526cc152e))
  * Require Python 3.7+ ([#610](https://github.com/googleapis/python-bigtable/issues/610)) ([10d00f5](https://github.com/googleapis/python-bigtable/commit/10d00f5af5d5878c26529f5e48a5fb8d8385696d))



##### Performance Improvements

  * Improve row merging ([#619](https://github.com/googleapis/python-bigtable/issues/619)) ([b4853e5](https://github.com/googleapis/python-bigtable/commit/b4853e59d0efd8a7b37f3fcb06b14dbd9f5d20a4))



## August 01, 2022

Libraries

A weekly digest of client library updates from across the [Cloud SDK](https://docs.cloud.google.com/sdk).

### Java

### Changes for [google-cloud-bigtable](https://github.com/googleapis/java-bigtable)

#### [2.10.0](https://github.com/googleapis/java-bigtable/compare/v2.9.0...v2.10.0) (2022-07-26)

##### Features

  * Add response protos ([#1246](https://github.com/googleapis/java-bigtable/issues/1246)) ([52d59ce](https://github.com/googleapis/java-bigtable/commit/52d59ce18fb5536a17a5cb59da39e563e4afede4))
  * Add response_params proto to clients ([#1303](https://github.com/googleapis/java-bigtable/issues/1303)) ([93edfe1](https://github.com/googleapis/java-bigtable/commit/93edfe1e43dcfefda6bba3e9ee53ed80eaf2e5c2))
  * Add storage utilization gib per node for autoscaling ([#1317](https://github.com/googleapis/java-bigtable/issues/1317)) ([5282589](https://github.com/googleapis/java-bigtable/commit/52825891af0e4ec2dd76c0c6fa1379a98a77a08f))
  * Use PingAndWarm request for channel priming ([#1179](https://github.com/googleapis/java-bigtable/issues/1179)) ([6629821](https://github.com/googleapis/java-bigtable/commit/6629821ea3200d3a5b93c9d45aab6d57485fcebf))



##### Bug Fixes

  * Enable integration test for google-cloud-bigtable-stats ([#1311](https://github.com/googleapis/java-bigtable/issues/1311)) ([7c77879](https://github.com/googleapis/java-bigtable/commit/7c7787998b164ceb55472c0d06c083a835e5d000))
  * Fix race condition in BuiltinMetricsTracer ([#1320](https://github.com/googleapis/java-bigtable/issues/1320)) ([644454a](https://github.com/googleapis/java-bigtable/commit/644454a9723da359677052b7a4b9201e91e9a78a))
  * Ignore repackaged files to fix clirr ([#1300](https://github.com/googleapis/java-bigtable/issues/1300)) ([99b67ba](https://github.com/googleapis/java-bigtable/commit/99b67ba5b1625686ac7802a6e40dafc2edceade0))



##### Dependencies

  * Update dependency org.graalvm.buildtools:junit-platform-native to v0.9.13 ([#1306](https://github.com/googleapis/java-bigtable/issues/1306)) ([ddae354](https://github.com/googleapis/java-bigtable/commit/ddae3540fd68e8f79d94d49c96c5685e1bad2f66))
  * Update dependency org.graalvm.buildtools:native-maven-plugin to v0.9.13 ([#1307](https://github.com/googleapis/java-bigtable/issues/1307)) ([c0740fe](https://github.com/googleapis/java-bigtable/commit/c0740fe30c5cd2bdf6dedf901e2fdb9a84ce64a1))



## July 11, 2022

Feature

Cloud Bigtable is available in the `us-south1` (Dallas) and `europe-southwest1` (Madrid) regions. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## June 30, 2022

Feature

You are now able to configure the [storage utilization target](https://docs.cloud.google.com/bigtable/docs/autoscaling#parameters) for a cluster when you use autoscaling for Cloud Bigtable. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## June 28, 2022

Feature

Cloud Bigtable now gives you the option to [undelete a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#undelete-table) for up to seven days from the time of deletion using the `gcloud CLI`. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## June 24, 2022

Feature

Cloud Bigtable is available in the `us-east5` (Columbus) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## June 02, 2022

Feature

Cloud Bigtable now provides increased observability by letting you identify and monitor hot tablets in a cluster. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). To learn more, see [Hot tablets](https://docs.cloud.google.com/bigtable/docs/hot-tablets).

## May 05, 2022

Feature

A Cloud Bigtable [table overview page](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#table-overview) in the Cloud console is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). The table overview displays monitoring metrics and replication details for a selected table.

## May 03, 2022

Feature

Cloud Bigtable is available in the `europe-west9` (Paris) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## April 20, 2022

Feature

Cloud Bigtable is available in the `europe-west8` (Milan) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## April 05, 2022

Feature

The [Cloud Bigtable HBase replication library](https://docs.cloud.google.com/bigtable/docs/hbase-replication) lets you replicate data from HBase to Bigtable. You can use the replication library in conjunction with existing migration tools to migrate your HBase data to Bigtable without pausing writes or taking your application offline. The replication library is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## March 25, 2022

Feature

Cloud Bigtable support for [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can now choose an externally managed key when you protect your data using customer managed encryption keys ([CMEK](https://docs.cloud.google.com/bigtable/docs/cmek)). Cloud EKM includes [Key Access Justification](https://docs.cloud.google.com/cloud-provider-access-management/key-access-justifications/docs/overview), which lets you view the reason for each Cloud EKM request.

## December 20, 2021

Feature

[System Event audit logs](https://docs.cloud.google.com/bigtable/docs/audit-logging) for Cloud Bigtable autoscaling are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## December 13, 2021

Change

A Cloud Bigtable instance can now have clusters in up to 8 regions. This lets you create an instance with as many clusters as there are zones in your chosen [Bigtable regions](https://docs.cloud.google.com/bigtable/docs/locations). Previously, an instance was limited to 4 clusters.

## December 09, 2021

Feature

[Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling) for Cloud Bigtable is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Autoscaling helps prevent over-provisioning or under-provisioning by letting Cloud Bigtable automatically add or remove nodes to a cluster when usage changes. In addition, [new metrics](https://docs.cloud.google.com/bigtable/docs/autoscaling#monitoring) are available to help you understand how autoscaling is working.

Feature

You can now use customer managed encryption keys ([CMEK](https://docs.cloud.google.com/bigtable/docs/cmek)) in Cloud Bigtable instances that are replicated across multiple regions. Previously, CMEK was limited to instances that had clusters in a single region. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## December 03, 2021

Announcement

A new tutorial is available that uses open-source benchmarking tools to evaluate Cloud Bigtable performance. For more information, see [Benchmarking Bigtable with PerfKit Benchmarker – Batch Testing](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker/tree/master/tutorials/bigtable_walkthrough) on GitHub.

## November 16, 2021

Feature

Cloud Bigtable is available in the `southamerica-west1` (Santiago) region. For more information, see [Bigtable locations](https://docs.cloud.google.com/bigtable/docs/locations).

## October 27, 2021

Change

The guidance on [migrating data from HBase to Cloud Bigtable](https://docs.cloud.google.com/architecture/hadoop/hadoop-gcp-migration-data-hbase-to-bigtable) has been updated. You can now use new tooling designed to create Bigtable tables from existing HBase tables, import snapshots of your HBase tables, and validate the integrity of migrated data.

## October 21, 2021

Feature

Cloud Bigtable [app profile cluster groups](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing) let you route an app profile's traffic to a subset of an instance's clusters. This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## October 04, 2021

Feature

Cloud Bigtable provides a `CPU utilization by app profile, method, and table` metric that gives you more granular observability into the cluster's [CPU usage](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu). This metric is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## September 30, 2021

Feature

[Storage limits](https://docs.cloud.google.com/bigtable/quotas#storage-per-node) for Cloud Bigtable nodes have been doubled. Each node now supports twice as much storage, with no increase in per-node costs. This feature is generally available ([GA)](https://cloud.google.com/products#product-launch-stages).

## August 03, 2021

Feature

Cloud Bigtable is now available in the [`northamerica-northeast2` (Toronto) region](https://docs.cloud.google.com/bigtable/docs/locations).

## July 16, 2021

Announcement

New [Dataflow templates](https://github.com/googleapis/java-bigtable-hbase/tree/master/bigtable-dataflow-parent/bigtable-beam-import) are now available to help you import data into Cloud Bigtable. The `importsnapshot` template lets you import HBase snapshots into Cloud Bigtable, without the need to export data as SequenceFiles or Avro files. The `sync-table` template lets you validate the integrity of your imported data.

Announcement

The Cloud Bigtable documentation has been updated to include information about [connection pools](https://docs.cloud.google.com/bigtable/docs/connection-pools) and when to consider resizing them.

## June 29, 2021

Feature

Cloud Bigtable is now available in the [`asia-south2` (Delhi) region](https://docs.cloud.google.com/bigtable/docs/locations).

## June 23, 2021

Feature

Console [Table Management](https://docs.cloud.google.com/bigtable/docs/managing-tables) for Cloud Bigtable is now generally available. You can now use the Google Cloud Console to create, edit, and delete Cloud Bigtable tables, column families, and garbage collection policies.

## June 21, 2021

Feature

Cloud Bigtable is now available in the [`australia-southeast2` (Melbourne) region](https://docs.cloud.google.com/bigtable/docs/locations).

## May 26, 2021

Change

The [Cloud Bigtable Service Level Agreement (SLA)](https://cloud.google.com/bigtable/sla) has been updated.

## May 11, 2021

Announcement

The Cloud Bigtable documentation on [schema design for time series data](https://docs.cloud.google.com/bigtable/docs/schema-design-time-series) has been updated with an emphasis on recommended design patterns.

## May 10, 2021

Feature

You can now use [IAM conditions](https://docs.cloud.google.com/bigtable/docs/access-control#conditions) to define and enforce conditional access control for Cloud Bigtable instances, clusters, and tables. This feature is generally available.

## May 07, 2021

Announcement

New guidance is available to help you [schedule Cloud Bigtable backups](https://cloud.google.com/blog/topics/developers-practitioners/scheduling-cloud-bigtable-backups) using Cloud Scheduler, Pub/Sub, and Cloud Functions.

## May 06, 2021

Announcement

Cloud Bigtable now provides a Cloud Monitoring metric that reports the amount of logical storage bytes that a backup is using. The metric is [`backup/bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-bigtable), and it includes information about the source table and storage type.

## May 03, 2021

Feature

The ability to restore from a Cloud Bigtable backup to a different instance is now generally available. This feature enhancement lets you use backups for a [wider variety of use cases](https://docs.cloud.google.com/bigtable/docs/backups#key-features).

## April 08, 2021

Feature

Cloud Bigtable support for [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/bigtable/docs/cmek) is now generally available.

## April 06, 2021

Feature

[Data Access audit logging](https://docs.cloud.google.com/bigtable/docs/audit-logging) for Cloud Bigtable is now generally available. 

If you previously enabled Data Access audit logs for all Google Cloud services in the Cloud Audit Logs [default configuration](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-default), you might need to take additional steps to enable Data Access audit logging for Cloud Bigtable. Affected customers will see a notification at the top of the Cloud Bigtable page of the Cloud Console.

## March 24, 2021

Feature

Cloud Bigtable is now available in the [`europe-central2` (Warsaw) region](https://docs.cloud.google.com/bigtable/docs/locations).

## March 22, 2021

Change

Cloud Bigtable's Cloud Console navigation has been improved. On the **Instances** page, the **Create Instance** button is more prominent. After you navigate to an instance, the following updates are visible:

  * Left-pane navigation is now organized in sections.
  * New breadcrumb navigation on each page shows the ID of the selected instance.
  * Page headings are more prominent.
  * You can now edit or delete an instance from every page.



## December 14, 2020

Fixed

Key Visualizer diagnostic messages are visible to all Cloud Bigtable customers. Review the [message descriptions](https://docs.cloud.google.com/bigtable/docs/keyvis-diagnostics) to learn how diagnostic messages can help you troubleshoot your Cloud Bigtable tables.

## November 06, 2020

Change

The default data points used for disk load charts on the [Cloud Bigtable Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#disk) page have changed to reflect the maximum for a displayed alignment period. Previously, data points on the charts reflected the mean for the alignment period. This change ensures that charts clearly show the peaks that are important for monitoring the health of a Cloud Bigtable instance. Disk load charts are only applicable for HDD clusters.

## October 16, 2020

Change

A [tutorial](https://docs.cloud.google.com/bigtable/docs/use-cloud-functions) is now available that demonstrates how to send a Cloud Bigtable read request using a Cloud Functions HTTP(S) request.

## October 15, 2020

Change

The steps to [create a new](https://docs.cloud.google.com/bigtable/docs/creating-instance) Cloud Bigtable instance and [edit an existing](https://docs.cloud.google.com/bigtable/docs/modifying-instance) instance have been streamlined and improved in the Google Cloud Console.

## July 22, 2020

Feature

Cloud Bigtable's fully integrated [backups feature](https://docs.cloud.google.com/bigtable/docs/backups) is now generally available. Backups let you save a copy of a table's schema and data and restore the backup to a new table at a later time.

## July 13, 2020

Change

The default data points used for CPU utilization charts on the [Cloud Bigtable Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance) page have changed. Previously, data points on the charts reflected the mean for a displayed alignment period. Now the data points reflect the maximum for the alignment period. This change ensures that charts clearly show the peaks that are important for monitoring the health of a Cloud Bigtable instance.

## June 08, 2020

Feature

Cloud Bigtable is now available in the [`asia-southeast2` (Jakarta) region](https://docs.cloud.google.com/bigtable/docs/locations).

## May 18, 2020

Change

The [Cloud Bigtable Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance) page in the Cloud Console has been redesigned. Changes to the visual experience include the following:

  * Views that are now split into separate tabs
  * A new time range picker
  * Updated styling on the graphs



## April 20, 2020

Feature

Cloud Bigtable is now available in the [`us-west4` (Las Vegas) region](https://docs.cloud.google.com/bigtable/docs/locations).

## April 06, 2020

Feature

Key Visualizer for Cloud Bigtable is now integrated into the [Google Cloud Console](https://console.cloud.google.com). The following enhancements have been added:

  * Eligibility has been simplified to a minimum of 30 GB of data per table.
  * You can now specify the start and end time for a scan.
  * Performance data is now more recent.
  * Your performance data is retained for 14 days.



## March 19, 2020

Feature

You can now create a production [Cloud Bigtable instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) that has one or two nodes per cluster. Prior to this change, production instances had a minimum of three nodes per cluster, and the only way to create smaller clusters was in a development instance.

Change

The [Cloud Bigtable Service Level Agreement (SLA)](https://cloud.google.com/bigtable/sla) has been updated.

## February 24, 2020

Feature

Cloud Bigtable is now available in the [`us-west3` (Salt Lake City) region](https://docs.cloud.google.com/bigtable/docs/locations).

## January 24, 2020

Feature

Cloud Bigtable is now available in the [`asia-northeast3` (Seoul) region](https://docs.cloud.google.com/bigtable/docs/locations).

## December 11, 2019

Feature

[Table-level IAM](https://docs.cloud.google.com/bigtable/docs/access-control#iam-management-table) for Cloud Bigtable is now generally available.

## December 05, 2019

Feature

The [Ruby client library for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now generally available.

## November 05, 2019

Feature

Cloud Bigtable is now available in the [`europe-west3` (Frankfurt) region](https://docs.cloud.google.com/bigtable/docs/locations).

## October 14, 2019

Feature

[Admin Activity audit logging](https://docs.cloud.google.com/bigtable/docs/audit-logging) is now generally available.

## September 25, 2019

Feature

The [Cloud Bigtable client library for Java](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now generally available.

## September 18, 2019

Feature

The [PHP client library](https://docs.cloud.google.com/bigtable/docs/reference/libraries) for Cloud Bigtable is now generally available.

## September 06, 2019

Feature

The [Python client library for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now generally available.

## September 03, 2019

Change

Detailed descriptions and examples of [write requests](https://docs.cloud.google.com/bigtable/docs/writing-data) are now available in the Cloud Bigtable documentation.

## June 27, 2019

Feature

The [C++ client library for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now generally available.

## June 17, 2019

Feature

The [Cloud Bigtable client library for Java](https://docs.cloud.google.com/bigtable/docs/reference/libraries) for is now available in beta.

## June 05, 2019

Feature

The [C# client library for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now generally available.

## May 14, 2019

Change

A section on [garbage collection](https://docs.cloud.google.com/bigtable/docs/garbage-collection) is now available in the Cloud Bigtable documentation.

## April 18, 2019

Feature

Cloud Bigtable is now available in the [`asia-northeast2` (Osaka) region](https://docs.cloud.google.com/bigtable/docs/locations).

## April 08, 2019

Feature

[Multi-region replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) for Cloud Bigtable is now generally available.

## March 14, 2019

Feature

A [PHP client library](https://docs.cloud.google.com/bigtable/docs/reference/libraries) for Cloud Bigtable is now available in beta.

## March 11, 2019

Feature

Cloud Bigtable is now available in the [`europe-west6`(Zürich) region](https://docs.cloud.google.com/bigtable/docs/locations).

## March 06, 2019

Feature

A [Ruby client library](https://docs.cloud.google.com/bigtable/docs/reference/libraries) for Cloud Bigtable is now available in beta.

## March 05, 2019

Feature

[Multi-region replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) for Cloud Bigtable is now available in beta. Regional replication continues to be generally available.

## February 22, 2019

Feature

Cloud Bigtable is now available in the [`southamerica-east1` (São Paulo) region](https://docs.cloud.google.com/bigtable/docs/locations).

## November 27, 2018

Feature

Cloud Bigtable is now available in the [`asia-east2` (Hong Kong) region](https://docs.cloud.google.com/bigtable/docs/locations).

## November 13, 2018

Feature

The [Node.js client library for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now generally available.

## October 08, 2018

Change

Cloud Bigtable now enforces the [limits on the amount of storage per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node):

  * If a cluster in an instance exceeds the storage limits, all writes to the instance will fail until you [add nodes to the cluster](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes).
  * If you try to remove nodes from a cluster, and the change would cause the cluster to exceed the storage limits, Cloud Bigtable will deny the request.



## October 05, 2018

Feature

A [Python client library](https://docs.cloud.google.com/bigtable/docs/reference/libraries#client-libraries-install-python) for Cloud Bigtable is now available in beta.

## October 02, 2018

Feature

Cloud Bigtable is now available in the [`australia-southeast1` (Sydney) region](https://docs.cloud.google.com/bigtable/docs/locations).

## September 18, 2018

Feature

[Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview) is now generally available.

## September 06, 2018

Feature

Cloud Bigtable is now available in the [`asia-south1` (Mumbai) region](https://docs.cloud.google.com/bigtable/docs/locations).

## September 04, 2018

Feature

Key Visualizer now includes the ability to [view multiple metrics at once](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps#finding-connections).

## August 03, 2018

Feature

A [C++ client library for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now available in beta.

## July 25, 2018

Change

The [Cloud Bigtable Service Level Agreement (SLA)](https://cloud.google.com/bigtable/sla) has been updated.

Change

[Regional replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) is now generally available.

## July 11, 2018

Change

The [Quotas & Limits](https://docs.cloud.google.com/bigtable/quotas) page now includes all of the quotas that appear in the Google Cloud Platform Console, and it now shows quotas and limits related to [application profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles). These quotas and limits are not new, but they were not previously listed in the documentation.

## July 10, 2018

Feature

[Key Visualizer for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/keyvis-overview) is now available in beta. Use Key Visualizer to analyze your Cloud Bigtable usage in detail and troubleshoot performance issues.

Feature

Cloud Bigtable is now available in the [`us-west2` (Los Angeles) region](https://docs.cloud.google.com/bigtable/docs/locations).

## July 09, 2018

Feature

A [C# client library for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now available in beta.

## June 29, 2018

Change

Cloud Bigtable will start enforcing the [limit on the amount of storage per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node) on October 1, 2018, rather than on July 1.

We're updating the Google Cloud Platform Console to show the new date. Until we finish rolling out that change, you'll still see the old enforcement date in the GCP Console.

## June 28, 2018

Feature

A [Node.js client library for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/reference/libraries) is now available in beta.

## June 11, 2018

Feature

Cloud Bigtable is now available in the [`europe-north1` (Finland) region](https://docs.cloud.google.com/bigtable/docs/locations).

## May 07, 2018

Feature

[Instance-level IAM](https://docs.cloud.google.com/bigtable/docs/access-control#iam-management-instance) for Cloud Bigtable is now generally available.

Change

Removed the column-family permissions (`bigtable.columnfamilies.*`) from the list of [IAM permissions](https://docs.cloud.google.com/bigtable/docs/access-control#permissions) for Cloud Bigtable. These permissions are deprecated and will not be supported in the future.

  * If you need to view information about a table's column families, make sure your IAM role includes the `bigtable.tables.get` permission.
  * If you need to modify a table's column families, make sure your IAM role includes the `bigtable.tables.update` permission.



## May 03, 2018

Feature

Cloud Bigtable is now available in the [`us-east4` (Northern Virginia) and `northamerica-northeast1` (Montréal) regions](https://docs.cloud.google.com/bigtable/docs/locations).

## April 30, 2018

Feature

Cloud Bigtable is now available in the [`europe-west2` (London) region](https://docs.cloud.google.com/bigtable/docs/locations).

## April 25, 2018

Change

The GCP Console now shows whether your instance's clusters are using too much storage based on the number of nodes they contain. [Learn more about storage limits per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node).

**Important:** Starting on July 1, 2018, Cloud Bigtable will enforce the limit on the amount of storage per node. If any cluster in an instance exceeds the limit, writes to all clusters in that instance will fail until you [add nodes to each cluster that is over the limit](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes). Also, if you try to remove nodes from your cluster, and the reduced number of nodes would cause the cluster to exceed the storage limit, Cloud Bigtable will deny the request.

Feature

[Regional replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) is now available in beta. Regional replication automatically makes your data available in two different zones within the same region, improving availability and durability.

Feature

The GCP Console now provides improved [monitoring for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring), including new charts that show each cluster's storage utilization, node count, and replication status.

## March 15, 2018

Feature

Cloud Bigtable is now available in the [`us-west1` (Oregon) region](https://docs.cloud.google.com/bigtable/docs/locations).

## February 06, 2018

Feature

Cloud Bigtable is now available in the [`europe-west4` (Netherlands) region](https://docs.cloud.google.com/bigtable/docs/locations).

## February 02, 2018

Feature

Cloud Bigtable is now available in the [`asia-southeast1` (Singapore) region](https://docs.cloud.google.com/bigtable/docs/locations).

## January 31, 2018

Change

[IAM custom roles](https://docs.cloud.google.com/bigtable/docs/access-control#custom-roles) are now generally available.

## January 02, 2018

Change

Updated this page to provide release notes for the Cloud Bigtable service. To view release notes for the Cloud Bigtable HBase client for Java, see the client library's [GitHub releases page](https://github.com/googleapis/java-bigtable-hbase/releases).

## December 20, 2017

Feature

[Admin Activity audit logging](https://docs.cloud.google.com/bigtable/docs/audit-logging) is now available in beta.

## December 15, 2017

Feature

You can now [add labels to your Cloud Bigtable instances](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels).

Fixed

The REST Admin API now correctly implements the method for [listing Cloud Bigtable operations](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/operations.projects.operations/list).

## December 07, 2017

Feature

Cloud Bigtable is now available in the [`asia-northeast1` (Tokyo) region](https://docs.cloud.google.com/bigtable/docs/locations).

## November 28, 2017

Feature

You can now use Stackdriver Monitoring to [set up alerting policies and create custom dashboards](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#stackdriver) that include Cloud Bigtable metrics.

## October 18, 2017

Change

The [schema design documentation](https://docs.cloud.google.com/bigtable/docs/schema-design) no longer recommends using hashed values in row keys. Use human-readable values instead.

## September 19, 2017

Feature

The Identity and Access Management predefined roles for Cloud Bigtable now include a [viewer role](https://docs.cloud.google.com/bigtable/docs/access-control#roles). This role provides access to basic Cloud Bigtable functionality in the Google Cloud Platform Console.

## September 06, 2017

Feature

The Google Cloud Platform Console now provides graphs that show the [number of rows read and written per second](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring).

## July 25, 2017

Feature

V2 of the [Cloud Bigtable REST Admin API](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest) is now available. You can use this API to manage your Cloud Bigtable instances.

## July 24, 2017

Feature

[Identity and Access Management custom roles for Cloud Bigtable](https://docs.cloud.google.com/bigtable/docs/access-control#custom-roles) are now available in beta.

## May 01, 2017

Feature

Cloud Bigtable now supports [Identity and Access Management](https://docs.cloud.google.com/bigtable/docs/access-control).

FEATURE

You can now [monitor a Cloud Bigtable instance with Stackdriver Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#stackdriver).

## March 10, 2017

Feature

The Google Cloud Platform Console now provides graphs that show the [following information about your instance](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#console-monitoring):

  * The number of nodes in the instance's cluster.
  * The average CPU utilization across all nodes in the instance's cluster.
  * The CPU utilization of the busiest node in the instance's cluster.



## March 09, 2017

Feature

You can now [create a development instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) of Cloud Bigtable. A development instance is a low-cost instance with performance limited to the equivalent of a single node.

## June 29, 2016

Feature

Cloud Bigtable is now available in the [`us-east1` (South Carolina) region](https://docs.cloud.google.com/bigtable/docs/locations).

Change

Each Cloud Bigtable cluster is now contained within an instance, which is a container for your cluster. For instances created before June 29, 2016, the instance ID is identical to the cluster ID. (There is one exception to this rule: If you had multiple clusters with the same ID before June 29, 2016, your instance IDs will end with `-1`, `-2`, and so on, so that each instance has a unique ID.)

Feature

V2 of the Cloud Bigtable RPC API is now available. You can write custom gRPC clients that target the [Data API](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc) or the [Admin API](https://docs.cloud.google.com/bigtable/docs/reference/admin/rpc).

Change

Cloud Bigtable is now generally available.

## May 06, 2015

Change

Cloud Bigtable is now available in beta.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
