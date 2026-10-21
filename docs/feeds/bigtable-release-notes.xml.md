---
url: https://docs.cloud.google.com/feeds/bigtable-release-notes.xml
title: Bigtable - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:55.234974+00:00
---

# Bigtable - Release notes

> Source: https://docs.cloud.google.com/feeds/bigtable-release-notes.xml

tag:google.com,2016:bigtable-release-notesBigtable - Release notesGoogle Cloud Platform2026-10-01T00:00:00-07:00October 01, 2026tag:google.com,2016:bigtable-release-notes#October_01_20262026-10-01T00:00:00-07:00Feature 

You can use [Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview) to browse Bigtable instances and tables, design schemas, and run GoogleSQL queries from your IDE or coding agent. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Data Agent Kit is now GA: Bring Google Data Cloud to any coding agent](https://cloud.google.com/blog/topics/developers-practitioners/data-agent-kit-is-now-ga-bring-google-data-cloud-to-any-coding-agent).

]]> September 22, 2026tag:google.com,2016:bigtable-release-notes#September_22_20262026-09-22T00:00:00-07:00Feature 

You can use the Google Cloud console to create and manage protobuf schemas (schema bundles) for your Bigtable tables. You can also view schema bundle definitions in Bigtable Studio. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create and manage protobuf schemas](https://docs.cloud.google.com/bigtable/docs/create-manage-protobuf-schemas).

]]> September 14, 2026tag:google.com,2016:bigtable-release-notes#September_14_20262026-09-14T00:00:00-07:00Feature 

You can use the Google Cloud console to create, list, and query [parameterized views](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview) for your Bigtable instances. You can also configure view parameters and run queries in Bigtable Studio. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create and manage parameterized views](https://docs.cloud.google.com/bigtable/docs/create-manage-parameterized-views).

]]> September 01, 2026tag:google.com,2016:bigtable-release-notes#September_01_20262026-09-01T00:00:00-07:00Feature 

You can use the Google Cloud console to create and manage [aggregate column families](https://docs.cloud.google.com/bigtable/docs/aggregates) for your Bigtable tables. You can also view and query aggregate column families in Bigtable Studio. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables#add-column-families) and [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).

]]> August 20, 2026tag:google.com,2016:bigtable-release-notes#August_20_20262026-08-20T00:00:00-07:00Feature 

You can use the `allow_incomplete_view` query hint in SQL queries to read data from a continuous materialized view before its initial population finishes. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Read data during initial population](https://docs.cloud.google.com/bigtable/docs/reads#read-during-initial-population).

]]> August 12, 2026tag:google.com,2016:bigtable-release-notes#August_12_20262026-08-12T00:00:00-07:00Feature 

You can use parameterized views in Bigtable to dynamically filter data ranges for logical views based on application context and mitigate SQL injection risks. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Parameterized views overview](https://docs.cloud.google.com/bigtable/docs/parameterized-views-overview).

### Feature

You can use the `CLUSTER_ATTRIBUTE()` filter to restrict continuous materialized view processing to specific clusters. This function lets you isolate views within an instance. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Non-deterministic SQL functions](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views#non-deterministic-functions).

]]> August 10, 2026tag:google.com,2016:bigtable-release-notes#August_10_20262026-08-10T00:00:00-07:00Libraries 

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



]]> July 30, 2026tag:google.com,2016:bigtable-release-notes#July_30_20262026-07-30T00:00:00-07:00Feature 

You can use Bigtable as a remote storage backend for [LMCache](https://docs.lmcache.ai/kv_cache/storage_backends/bigtable.html). By storing the large language model (LLM) key-value (KV) cache externally in Bigtable, multiple AI serving instances can share and reuse precomputed attention tensors. This reduces compute overhead and significantly improves time-to-first-token (TTFT) for repeated prompts and shared documents. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> July 29, 2026tag:google.com,2016:bigtable-release-notes#July_29_20262026-07-29T00:00:00-07:00Feature 

You can use the Google Cloud console to [manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas) for your Bigtable tables. This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> July 27, 2026tag:google.com,2016:bigtable-release-notes#July_27_20262026-07-27T00:00:00-07:00Feature 

The Bigtable remote MCP server supports the Bigtable Data API, which provides the `execute_sql` tool that you can use to query Bigtable data using natural language prompts. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Use the Bigtable remote MCP server](https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp).

### Libraries

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



]]> July 14, 2026tag:google.com,2016:bigtable-release-notes#July_14_20262026-07-14T00:00:00-07:00Feature 

AI agents can use the [`list_hot_tablets` Model Context Protocol (MCP) tool](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/bigtable/mcp/tools_list/list_hot_tablets) to programmatically query Bigtable cluster health to isolate resource-intensive tablets (hot tablets) and detect overutilized node CPUs. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> July 09, 2026tag:google.com,2016:bigtable-release-notes#July_09_20262026-07-09T00:00:00-07:00Feature 

You can use the [Bigtable client library for Go](https://docs.cloud.google.com/bigtable/docs/reference/libraries) to execute read jobs and queries using [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview).

]]> July 07, 2026tag:google.com,2016:bigtable-release-notes#July_07_20262026-07-07T00:00:00-07:00Feature 

You can bind existing [tags](https://docs.cloud.google.com/bigtable/docs/tags) to Bigtable instances when you create an instance and use policies to enforce mandatory tag assignments. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).

### Feature

The Bigtable agent skill (`bigtable-basics`) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) in the public [Google Agent Skills repository](https://github.com/google/skills/tree/main/skills/cloud/bigtable-basics). This skill lets you equip AI agents with capabilities for Bigtable tasks, such as provisioning instances and tables, designing schemas, querying data using GoogleSQL and key-value APIs, and diagnosing performance issues or hotspots.

### Feature

You can use Organization Policy Service custom constraints to manage specific operations on continuous materialized views. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Use custom organization policies](https://docs.cloud.google.com/bigtable/docs/custom-constraints).

]]> July 06, 2026tag:google.com,2016:bigtable-release-notes#July_06_20262026-07-06T00:00:00-07:00Feature 

Bigtable supports direct connectivity, which bypasses the Google frontend and optimizes performance for application traffic that meets certain criteria. For more information, see [Direct connectivity](https://docs.cloud.google.com/bigtable/docs/performance#direct-connectivity).

]]> June 24, 2026tag:google.com,2016:bigtable-release-notes#June_24_20262026-06-24T00:00:00-07:00Feature 

You can create [hot backups](https://docs.cloud.google.com/bigtable/docs/backups#hot-backups) and modify all backups in Bigtable Studio. For more information, see [Manage backups](https://docs.cloud.google.com/bigtable/docs/managing-backups).

]]> June 22, 2026tag:google.com,2016:bigtable-release-notes#June_22_20262026-06-22T00:00:00-07:00Libraries 

### Go

#### [1.50.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.49.0...bigtable/v1.50.0) (2026-06-17)

##### Features

  * **bigtable:** Enable JWT ([#19957](https://github.com/googleapis/google-cloud-go/issues/19957)) ([af93528](https://github.com/googleapis/google-cloud-go/commit/af93528c6eb18e841783987820b9f586293459e4))
  * **bigtable:** Generate Admin API client using selective gapic ([#19962](https://github.com/googleapis/google-cloud-go/issues/19962)) ([a37509d](https://github.com/googleapis/google-cloud-go/commit/a37509ddadc60a81e5dfb0f373e47d0d578d8cca))
  * **bigtable:** Refactor channel_pool_factory as we need to maintain two channel factory one for session and another for unary ([#14652](https://github.com/googleapis/google-cloud-go/issues/14652)) ([0c0b6ce](https://github.com/googleapis/google-cloud-go/commit/0c0b6ceba693dbe8af778117f6ca10faf0ca67ff))
  * **bigtable:** Wrap admin client ([#14534](https://github.com/googleapis/google-cloud-go/issues/14534)) ([0bea4ba](https://github.com/googleapis/google-cloud-go/commit/0bea4ba37832608dc05293a1eb2a3c756a9f27d9))
  * Update API sources and regenerate ([#19950](https://github.com/googleapis/google-cloud-go/issues/19950)) ([c7607be](https://github.com/googleapis/google-cloud-go/commit/c7607be52757b803df345670b5d0621c2bb9ba30))



]]> June 19, 2026tag:google.com,2016:bigtable-release-notes#June_19_20262026-06-19T00:00:00-07:00Feature 

You can use the Bigtable Studio explorer to search for all resources except for authorized views and column families. For more information, see [Manage your data using Bigtable Studio](https://docs.cloud.google.com/bigtable/docs/manage-data-using-console).

]]> June 15, 2026tag:google.com,2016:bigtable-release-notes#June_15_20262026-06-15T00:00:00-07:00Libraries 

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




]]> June 01, 2026tag:google.com,2016:bigtable-release-notes#June_01_20262026-06-01T00:00:00-07:00Libraries 

### Go

#### [v1.48.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.47.0...bigtable/v1.48.0) (2026-05-26)

##### Features

  * expose a client option to disable direct access: (#14626) ([f22b29f5](https://github.com/googleapis/google-cloud-go/commit/f22b29f5))



##### Known Issue: heap growth on long-running clients (DirectAccess Eligible)

Long-running clients using DirectAccess may observe steady heap growth caused by an upstream memory leak in the gRPC-Go xDS client ([#14582](https://github.com/googleapis/google-cloud-go/issues/14582)). The leak is amplified in this release by the default connection recycler, which recycles connections roughly every 45 minutes.

**Workarounds:** \- Disable the connection recycler: ```go cfg := bigtable.ClientConfig{DisableConnectionRecycler: true} client, err := bigtable.NewClientWithConfig(ctx, project, instance, cfg)

  * OR Disable the connpool via env var `CBT_BIGTABLE_CONN_POOL=false`

  * OR upgrade to bigtable/v1.49.0 (or later), which fixes the problem by disabling connection recycler.




]]> May 28, 2026tag:google.com,2016:bigtable-release-notes#May_28_20262026-05-28T00:00:00-07:00Feature 

As part of Bigtable Enterprise Plus [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can configure a retention period of up to 365 days for backups. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Bigtable backups overview](https://docs.cloud.google.com/bigtable/docs/backups).

]]> May 18, 2026tag:google.com,2016:bigtable-release-notes#May_18_20262026-05-18T00:00:00-07:00Feature 

You can enable [row-affinity routing](https://docs.cloud.google.com/bigtable/docs/routing#row-affinity) for a standard app profile in the Google Cloud console. For more information, see [Create a standard app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#create-standard-app-profile).

]]> May 07, 2026tag:google.com,2016:bigtable-release-notes#May_07_20262026-05-07T00:00:00-07:00Feature 

You can use [Aerospike migration tools](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem/tree/main/aerospike-bigtable-migration-tools) to migrate data from Aerospike to Bigtable with minimal or zero downtime. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Migrate Aerospike to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-aerospike-to-bigtable).

]]> May 04, 2026tag:google.com,2016:bigtable-release-notes#May_04_20262026-05-04T00:00:00-07:00Libraries 

### Go

#### [v1.47.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.46.0...bigtable/v1.47.0) (2026-05-01)

##### Known Issue: heap growth on long-running clients (DirectAccess Eligible)

Long-running clients using DirectAccess may observe steady heap growth caused by an upstream memory leak in the gRPC-Go xDS client ([#14582](https://github.com/googleapis/google-cloud-go/issues/14582)). The leak is amplified in this release by the default connection recycler, which recycles connections roughly every 45 minutes.

**Workarounds:**

  * Disable the connection recycler: ```go cfg := bigtable.ClientConfig{DisableConnectionRecycler: true} client, err := bigtable.NewClientWithConfig(ctx, project, instance, cfg)


  * OR Disable the connpool via env var `CBT_BIGTABLE_CONN_POOL=false`

  * Or upgrade to bigtable/v1.49.0 (or later), which fixes the problem by disabling connection recycler.




]]> April 30, 2026tag:google.com,2016:bigtable-release-notes#April_30_20262026-04-30T00:00:00-07:00Feature 

You can use Bigtable [agent skills](https://github.com/GoogleCloudPlatform/cloud-bigtable-ecosystem#ai-agent-skills) to let AI agents assist with Bigtable-related tasks, such as schema design, generating SQL queries, and infrastructure management.

]]> April 23, 2026tag:google.com,2016:bigtable-release-notes#April_23_20262026-04-23T00:00:00-07:00Feature 

You can use window functions with GoogleSQL in Bigtable to perform advanced analytic operations over multiple table rows. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Window functions](https://docs.cloud.google.com/bigtable/docs/reference/sql/window-functions).

]]> April 22, 2026tag:google.com,2016:bigtable-release-notes#April_22_20262026-04-22T00:00:00-07:00Feature 

The Bigtable editions feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). Bigtable editions introduces advanced features in performance, analytic query capability, and resource management. You can choose between the Enterprise and Enterprise Plus edition to select the right capabilities for your workloads. For more information, see [Editions overview](https://docs.cloud.google.com/bigtable/docs/editions-overview).

### Feature

Bigtable provides an in-memory tier as part of its hybrid storage architecture. This tier provides sub-millisecond read latency and high throughput for time-sensitive data with independent vertical scaling to handle traffic surges. The in-memory tier is available only in the Enterprise Plus [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview) in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [In-memory tier overview](https://docs.cloud.google.com/bigtable/docs/in-memory-overview).

### Feature

Bigtable [tiered storage](https://docs.cloud.google.com/bigtable/docs/tiered-storage) limit increases from 32 TB to 64 TB per node. This expansion provides higher storage density to support retention of larger volumes of infrequently accessed data and is available only in the Enterprise Plus [edition](https://docs.cloud.google.com/bigtable/docs/editions-overview). Tiered storage is available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can use [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) to read data from tiered storage and HDD clusters. This feature is available only in the Enterprise Plus edition and is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can use [Data Boost](https://docs.cloud.google.com/bigtable/docs/data-boost-overview) to run GoogleSQL queries. This feature is available only in the Enterprise Plus edition and is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [High-throughput SQL analysis with Data Boost](https://docs.cloud.google.com/bigtable/docs/googlesql-examples#data-boost-analysis).

### Feature

As part of Bigtable [editions](https://docs.cloud.google.com/bigtable/docs/editions-overview), you can configure which cluster in a replicated instance is used for automated backups. This feature provides greater cost control and backup resource management. This feature is available only in the Enterprise Plus edition and is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Bigtable backups overview](https://docs.cloud.google.com/bigtable/docs/backups).

]]> April 20, 2026tag:google.com,2016:bigtable-release-notes#April_20_20262026-04-20T00:00:00-07:00Feature 

You can use the [Database Insights remote MCP server](https://docs.cloud.google.com/bigtable/docs/reference/admin/mcp/databaseinsights/mcp) to analyze Bigtable's performance and system metrics. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Feature

Bigtable [continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views) are [generally available (GA)](https://cloud.google.com/products#product-launch-stages). These views let you create precomputed tables that Bigtable automatically keeps in sync with your source data for low-latency queries and real-time insights.

### Feature

Bigtable free trial instances are [generally available (GA)](https://cloud.google.com/products#product-launch-stages). These instances let you learn and explore Bigtable features for 90 days at no cost, providing a 1-node SSD cluster and up to 500 GB of storage. For more information, see [Free trial instances overview](https://docs.cloud.google.com/bigtable/docs/free-trial-instance).

### Feature

The [Bigtable remote MCP server](https://docs.cloud.google.com/bigtable/docs/use-bigtable-mcp) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). The Bigtable remote MCP server lets you interact with Bigtable instances from LLMs, AI applications, and AI-enabled development platforms.

]]> April 16, 2026tag:google.com,2016:bigtable-release-notes#April_16_20262026-04-16T00:00:00-07:00Feature 

You can stream messages from [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/subscription-overview) directly to a Bigtable table using [Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions). This feature lets you write streaming messages to Bigtable without needing a separate subscriber such as Dataflow. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> April 15, 2026tag:google.com,2016:bigtable-release-notes#April_15_20262026-04-15T00:00:00-07:00Feature 

Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and Identity and Access Management (IAM) names remain unchanged. For more information about how Bigtable metadata interacts with Knowledge Catalog, see [Manage data assets using Knowledge Catalog](https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-knowledge-catalog).

]]> April 13, 2026tag:google.com,2016:bigtable-release-notes#April_13_20262026-04-13T00:00:00-07:00Feature 

You can now use GoogleSQL geography functions to work with geospatial data in Bigtable. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). For more information, see [Work with geospatial data](https://docs.cloud.google.com/bigtable/docs/work-with-geo-data) and [Geography functions reference](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions).

### Feature

Bigtable supports [pipe syntax](https://docs.cloud.google.com/bigtable/docs/reference/sql/pipe-syntax), an extension to GoogleSQL that lets you build simpler and more concise queries. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

### Libraries

### Go

#### [v1.46.0](https://github.com/googleapis/google-cloud-go/compare/bigtable/v1.45.0...bigtable/v1.46.0) (2026-04-09)

##### Known Issue: heap growth on long-running clients (DirectAccess Eligible)

Long-running clients using DirectAccess may observe steady heap growth caused by an upstream memory leak in the gRPC-Go xDS client ([#14582](https://github.com/googleapis/google-cloud-go/issues/14582)). The leak is amplified in this release by the default connection recycler, which recycles connections roughly every 45 minutes.

**Workarounds:**

  * Disable the connection recycler: ```go cfg := bigtable.ClientConfig{DisableConnectionRecycler: true} client, err := bigtable.NewClientWithConfig(ctx, project, instance, cfg)


  * OR Disable the connpool via env var `CBT_BIGTABLE_CONN_POOL=false`

  * Or upgrade to bigtable/v1.49.0 (or later), which fixes the problem by disabling connection recycler.




]]>
