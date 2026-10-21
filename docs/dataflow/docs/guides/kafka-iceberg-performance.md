---
url: https://docs.cloud.google.com/dataflow/docs/guides/kafka-iceberg-performance/
title: Performance characteristics of Kafka to Iceberg pipelines \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:41.220877+00:00
---

# Performance characteristics of Kafka to Iceberg pipelines  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/kafka-iceberg-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Performance characteristics of Kafka to Iceberg pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes performance characteristics, as of Apache Beam version 2.75.0, for Dataflow streaming jobs that read from Apache Kafka and write to Apache Iceberg tables. It evaluates the performance differences between direct Apache Iceberg writes and writes routed through the Managed BigQuery API, and compares these results against baseline benchmarks from [Kafka to BigQuery pipelines](https://docs.cloud.google.com/dataflow/docs/guides/kafka-bigquery-performance). Because optimizations for Apache Iceberg I/O are ongoing, these performance metrics are subject to change.

Benchmark comparisons are available across three primary **stateless** mapping configurations (meaning they read from the source, convert the message to a record, and write to the sink without tracking state or applying complex business logic; referred to as `map_only` or `mapping` in benchmarks):

  1. Kafka to BigQuery (`map_only`) (baseline from [Kafka to BigQuery performance](https://docs.cloud.google.com/dataflow/docs/guides/kafka-bigquery-performance))
  2. Kafka to Iceberg Direct (`map_only`, `autosharding=false`)
  3. Kafka to Iceberg using Managed BigQuery API (`map_only`)



Additionally, this guide evaluates direct Apache Iceberg streaming patterns—such as stateful batching using `groupbykey`—and details crucial downstream considerations regarding **file size distributions** , **autosharding behavior** , and **read-side query latency**.

## Test methodology

Benchmarks were conducted using the following resources:

  * **Managed Service for Apache Kafka cluster:** Traffic was generated using the Dataflow Streaming Data Generator template. 
    * **Input Throughput:** 1 GBps
    * **Message Rate:** ~1,000,000 messages per second
    * **Message Format:** JSON text with a fixed schema (~1 KB per message)
    * **Partitions:** 1,000 Kafka partitions
  * **Destination Sinks:**
    * **BigQuery:** Standard table (unpartitioned) written using BigQuery Storage Write API.
    * **Apache Iceberg:** Catalog backed by Cloud Storage. The **Direct sink** is partitioned using `bucket(id, 64)` (bucketed into 64 shards on the primary key) and uses `hash` distribution mode.



After horizontal autoscaling stabilized, each pipeline configuration ran in steady state for 24 hours. The benchmarks for each pipeline case were executed 3 separate times, and all reported values represent the calculated averages across those runs to ensure sustained, reliable performance metrics.

## Ingestion performance: Mapping workloads

Stateless mapping pipelines read from the source, convert the message format to a record, and write to the sink without tracking state across records. The following sections analyze reference architectures executing at 1 GBps.

### Job configuration

Setting | Kafka to BigQuery (`map_only`) | Kafka to Iceberg Direct (`autosharding=false`) | Kafka to Iceberg using Managed BigQuery API  
---|---|---|---  
**Worker machine type** | `e2-standard-2` | `e2-standard-4` | `e2-standard-4`  
**vCPUs per Worker** | 2 | 4 | 4  
**RAM per Worker** | 8 GB | 16 GB | 16 GB  
**Streaming Engine** | Enabled | Enabled | Enabled  
**Horizontal Autoscaling** | Enabled | Enabled | Enabled  
**Triggering Frequency** | 5 seconds | 60 seconds | 60 seconds  
  
### Throughput and resource usage

Writing directly to physical Parquet files in object storage incurs higher I/O overhead than BigQuery streaming ingestion. Compared to direct Iceberg writes, routing writes through the Managed BigQuery API improves worker CPU utilization (~70% versus ~60%) and modestly reduces Streaming Engine consumption (~180 SECU/h versus ~200 SECU/h), though overall worker compute requirements remain similar (~440 vCPUs versus ~450 vCPUs).

Metric | Kafka to BigQuery (`map_only`) | Kafka to Iceberg Direct (`autosharding=false`) | Kafka to Iceberg using Managed BigQuery API  
---|---|---|---  
**Avg Input Throughput per Worker** | **~15 MBps** | ~9 MBps | ~9 MBps  
**Avg CPU Utilization** | **~70%** | ~60% | **~70%**  
**Est. vCPUs for 1 GBps Input** | **~126 vCPUs** | ~450 vCPUs | ~440 vCPUs  
**Est. Workers for 1 GBps Input** | **~63 workers** | ~110 workers | ~110 workers  
**Est. SECU per Hour for 1 GBps** | **~58 SECU/h** | ~200 SECU/h | ~180 SECU/h  
  
### Write latency profile

Direct Iceberg writes exhibit severe tail latency (P99) due to object storage metadata commit constraints. Using the Managed BigQuery API eliminates tail latency spikes while maintaining low median latency.

End-to-End Write Latency | Kafka to BigQuery | Kafka to Iceberg Direct (`autosharding=false`) | Kafka to Iceberg using Managed BigQuery API  
---|---|---|---  
**P50 (Median)** | ~1,200 ms | ~1,000 ms | **~1,000 ms**  
**P95** | ~3,000 ms | ~7,400 ms | **~1,900 ms**  
**P99 (Tail)** | ~5,400 ms | ~14,000 ms | **~2,700 ms**  
  
## Autosharding considerations & design choices

This section discusses the implications of autosharding on file sizes and pipeline latency when writing to Apache Iceberg.

### Why `autosharding=false` was chosen as the baseline

In initial testing, enabling autosharding caused file sizes to collapse into tiny chunks and fluctuate arbitrarily due to dynamic shard splitting triggered by localized thread-level load surges—even under a constant aggregate input load.

To maintain stable, predictable Parquet file layouts (~800 KB on average) and ensure a fair baseline without premature flushes, **`autosharding=false`** was chosen for the direct sink configuration.

### What happens if you disable autosharding versus keep it enabled?

  * **With`autosharding=false` (Baseline):** You achieve larger initial file sizes (~800 KB average) compared to autosharding. While this is still small compared to ideal Iceberg file sizes (128–512 MB), it requires significantly less downstream compaction. However, the trade-off is a high write tail latency (P99 reaching ~14.0s) due to object storage metadata bottlenecks.
  * **If autosharding is enabled:** Dataflow dynamically scales writer threads to absorb local throughput spikes, which reduces write tail latency. However, it compromises the storage layer by producing a high volume of small, fragmented Parquet files (~100 KB or smaller). These file sizes exhibit high variance and fluctuate arbitrarily across runs (ranging from ~39 KB to ~100 KB on average), escalating the need for aggressive downstream compaction maintenance.



### Partition Tuning & Recommendations

During our evaluation, we experimented with various fixed partition values for the destination table to find an optimal balance. We found that using **64 buckets** (example, `bucket(id, 64)`) for destination table partitioning yielded our targeted file sizes while maintaining decent utilization and throughput. This approach helped us match the performance benefits of autosharding while avoiding the arbitrary file-size fragmentation issues tied to fully dynamic scaling.

**Recommendation for Practitioners:** Customers are encouraged to perform similar preliminary testing with targeted partition settings to locate the sweet spot that maximizes pipeline parallelism without compromising Parquet file sizes.

## Downstream read implications: File sizes and compaction

While write-side metrics favor the Managed BigQuery API for Iceberg ingestion, overall pipeline efficiency depends heavily on downstream read performance:

  * **Small File Generation in Managed BigQuery API:** The Managed BigQuery API flushes data frequently to ensure low write latency. This behavior results in a high volume of small Parquet files written to the target Iceberg catalog.
  * **Read Query Latency Impact:** Query engines (example, Starburst/Trino, Apache Spark, BigQuery, Dremio) reading tables with millions of small Parquet files incur heavy metadata parsing overhead and partition scanning penalties.
  * **Compaction Requirements:** To prevent read performance degradation when using the Managed BigQuery API (or if autosharding is enabled on direct writes), run regular Iceberg compaction maintenance jobs (example, `REWRITE DATA FILES`). Compute overhead for compaction should be factored into overall architecture design.
  * **Direct Write (`autosharding=false`) File Distribution:** Direct Iceberg writes with fixed sharding produce larger average Parquet files (~800 KB), yielding a less fragmented layout for immediate query access without immediate compaction demands (though still below the ideal range).



## Stateful direct Iceberg pipelines (`groupbykey`)

To evaluate manual batching strategies, stateful key grouping (`groupbykey`) was tested against the baseline **Kafka to Iceberg Direct (`map_only`, `autosharding=false`)** pipeline. Both configurations write Parquet files directly to object storage.

### Benchmark comparison

Metric / Feature | Direct Sink Baseline (`autosharding=false`) | Stateful Direct Sink (`groupbykey`) | Performance Impact  
---|---|---|---  
**Est. vCPUs for 1 GBps** | **~450 vCPUs** | ~520 vCPUs | ~+16% compute required  
**Avg CPU Utilization** | **~60%** | ~50% | ~-17% worker efficiency  
**Est. SECU/h for 1 GBps** | **~200 SECU/h** | ~300 SECU/h | ~+50% Streaming Engine load  
**Average File Size** | **~800 KB** | ~100 KB | Generates smaller file batches  
**P50 Latency** | **~1,000 ms** | ~1,200 ms | ~+20% slower median  
**P95 Latency** | ~7,400 ms | **~5,500 ms** | ~-26% lower latency  
**P99 Latency** | ~14,000 ms | **~13,000 ms** | Marginal tail latency change  
  
### Trade-off analysis

  1. **Streaming Engine Overhead:** Adding a stateful `groupbykey` step requires Beam to store intermediate state across window boundaries. This increases Streaming Engine Compute Unit consumption by **~50%** (from **~200 SECU/h** to **~300 SECU/h**).
  2. **Buffering Latency:** Manual key aggregation introduces mandatory window buffering, increasing median write latency (P50) to **~1,200 ms** and P95 latency to **~5.5s**.



## Reverse pipelines: Streaming from Iceberg to Kafka

To evaluate bidirectional lakehouse capabilities, benchmarks were also conducted for streaming data flowing in reverse—reading append-only streams from an Apache Iceberg table and publishing back to Apache Kafka.

**Note:** The benchmarks discussed in this section reflect the older, append-only source behavior available for Iceberg in Apache Beam 2.75.0. A dedicated streaming Iceberg Change Data Capture (CDC) source is introduced in Beam 2.76.0, which may exhibit different performance characteristics.

### Job configuration and efficiency

Unlike ingestion pipelines that must deal with heavy object store file writes or metadata commit bottlenecks, reading and streaming changes out of Iceberg operates with high efficiency:

Metric | Iceberg to Kafka (Append-Only, Exactly-Once)  
---|---  
**Worker machine type** | `e2-standard-4`  
**Est. vCPUs for 1 GBps Input** | ~30 vCPUs  
**Est. Workers for 1 GBps Input** | ~7 workers  
**Est. SECU per Hour for 1 GBps** | ~0.2 SECU/h  
  
### Key takeaways for reverse pipelines

  * **Significantly Lower Compute Overhead:** Reading and projecting CDC streams from Iceberg requires substantially fewer compute resources (~30 vCPUs versus ~450 vCPUs for direct writes) because it avoids the heavy lifting of partitioning, encoding, and committing large volumes of Parquet files to object storage.
  * **Resource Efficiency:** Downstream event-driven consumption or replication out of a lakehouse format back to streaming layers is highly efficient compared to inbound ingestion paths.



## Architectural recommendation summary

Architecture Pattern | P99 Write Latency | File Layout | Downstream Read Considerations  
---|---|---|---  
**Kafka to BigQuery (`map_only`)** | ~5.4s | N/A | **Optimal** (Managed BigQuery Storage Engine)  
**Kafka to Iceberg using Managed BigQuery API** | **~2.7s** | Arbitrarily Small Files | **Requires periodic compaction** for high-volume reads  
**Kafka to Iceberg Direct (`autosharding=false`)** | ~14.0s | **~800 KB** | **Good** (Larger initial file sizes, lower compaction demand)  
**Kafka to Iceberg Direct (`groupbykey`)** | ~13.0s | ~100 KB | **Moderate** (Higher compute and state overhead)  
  
## Estimate costs

You can estimate the baseline cost of your own, comparable pipeline with [Resource-based billing](https://docs.cloud.google.com/dataflow/docs/streaming-engine#pricing) by using the Google Cloud [pricing calculator](https://cloud.google.com/products/calculator), as follows:

  1. Open the [pricing calculator](https://cloud.google.com/products/calculator).
  2. Click **Add to estimate**.
  3. Select Dataflow.
  4. For **Service type** , select "Dataflow Classic".
  5. Select **Advanced settings** to show the full set of options.
  6. Choose the location where the job runs.
  7. For **Job type** , select "Streaming".
  8. Select **Enable Streaming Engine**.
  9. Enter information for the job run hours, worker nodes, worker machines, and Persistent Disk storage.
  10. Enter the estimated number of Streaming Engine Compute Units.



Resource usage and cost scales roughly linearly with the input throughput, although for small jobs with only a few workers, the total cost is dominated by fixed costs. As a starting point, you can extrapolate the number of worker nodes and the resource consumption from the benchmark results.

For example, suppose that you run a pipeline using the **Kafka to Iceberg Direct (`autosharding=false`)** architecture, with an input data rate of 100 MBps. Based on the benchmark results for a 1 GBps pipeline, you can estimate the resource requirements as follows:

  * Scaling Factor: (100 MBps) / (1024 MBps) = ~0.1
  * Projected worker nodes: 110 workers × 0.1 = ~11 workers
  * Projected number of Streaming Engine Compute Units per hour: 200 × 0.1 = ~20 units per hour



This value should only be used as an initial estimate. The actual throughput and cost can vary significantly, based on factors such as machine type, message size distribution, user code, aggregation type, key parallelism, and window size. For more information, see [Best practices for Dataflow cost optimization](https://docs.cloud.google.com/dataflow/docs/optimize-costs).

## Run a test pipeline

To deploy an Apache Iceberg streaming job using the Dataflow Flex template, use the [`gcloud dataflow flex-template run`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run) command.
    
    
    gcloud dataflow flex-template run JOB_NAME \
      --project=PROJECT_ID \
      --region=REGION \
      --template-file-gcs-location=gs://dataflow-templates-us-central1/latest/flex/Kafka_To_Iceberg_Yaml \
      --enable-streaming-engine \
      --parameters ^@^bootstrapServers="KAFKA_BOOTSTRAP_ADDRESS"\
    @topic="KAFKA_TOPIC"\
    @table="ICEBERG_TABLE_IDENTIFIER"\
    @catalogName="CATALOG_NAME"\
    @catalogProperties='{"type":"CATALOG_TYPE","warehouse":"gs://BUCKET_NAME/warehouse/"}'\
    @triggeringFrequencySeconds=60\
    @schema='SCHEMA_DEFINITION'
    

Replace the following:

  * `JOB_NAME`: the name of your Dataflow job
  * `PROJECT_ID`: your Google Cloud project ID
  * `REGION`: the Google Cloud region where your job runs (for example, `us-central1`)
  * `KAFKA_BOOTSTRAP_ADDRESS`: the bootstrap address of your Apache Kafka cluster
  * `KAFKA_TOPIC`: the name of your Kafka topic
  * `ICEBERG_TABLE_IDENTIFIER`: the identifier of your target Iceberg table
  * `CATALOG_NAME`: the name of your Iceberg catalog
  * `CATALOG_TYPE`: the type of catalog to use (for example, `hadoop` or `bigquery`)
  * `BUCKET_NAME`: the name of the Cloud Storage bucket for your warehouse location
  * `SCHEMA_DEFINITION`: the schema definition for your Kafka topic data (for example, `{"type": "record", "name": "Record", "fields": [{"name": "id", "type": "string"}]}`)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
