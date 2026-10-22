---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options/
title: Cloud Storage FUSE CLI reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:22.990051+00:00
---

# Cloud Storage FUSE CLI reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Cloud Storage FUSE CLI reference Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage FUSE command line interface (CLI), or `gcsfuse` CLI, lets you mount Cloud Storage buckets as file systems on a local machine. This document describes the `gcsfuse` command options that you can use to interact with [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview).

If you're using the Cloud Storage FUSE CSI driver to mount your buckets to your local file system in Google Kubernetes Engine, see [Mount options for the Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options).

**Note:** For specific high-performance machine types, some `gcsfuse` command options are automatically set to specific values by default to maximize performance. Values that are manually set at the time of mount will override these defaults. For more information, see [Automated configuration values for high-performance machine types](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations).

## `gcsfuse` CLI command structure

The following example shows the structure of the `gcsfuse` command, including required commands and optional `gcsfuse` options.
    
    
    gcsfuse GLOBAL_OPTIONS BUCKET_NAME MOUNT_POINT

Replace the following:

  * `GLOBAL_OPTIONS` are the `gcsfuse` options that control how the mount is set up and how Cloud Storage FUSE behaves.

  * `BUCKET_NAME` is the name of the bucket to mount. For example, `my-mount-bucket`. Optional. Exclude a bucket name from this command to perform dynamic mounting.

  * `MOUNT_POINT` is the local directory where the bucket will be mounted. For example, `/path/to/mount/point`.




## `gcsfuse` CLI options

`gcsfuse` option | Description | Valid value | Default value  
---|---|---|---  
  
### `--anonymous-access`

| Disables authentication for requests. This option should be set if you're using a custom endpoint that doesn't support authentication. This option should also be set if you're using Cloud Storage FUSE with public buckets. | Boolean value: `true`, `false`. | `false`  
  
### `--app-name`

| The application name of the mount. | String value, for example: `my-bucket-mount`. | `""`  
  
### `--billing-project`

| Specifies a project to use for billing when the mounted bucket is accessed. This option is [often required](https://docs.cloud.google.com/storage/docs/requester-pays#requirements) when mounting a bucket enabled with [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays). | String value representing a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). | `""`  
  
### `--cache-dir`

| Enables the [file cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching) and specifies the directory for storing file cache data. **Note** : The Cloud Storage FUSE CSI driver for Google Kubernetes Engine uses a different method to enable file caching. To learn how to enable file caching on Google Kubernetes Engine, see [Enable and use file caching](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#enable-and-use-file-caching). | A path, for example: `/tmp/gcsfuse-cache-path`. An empty value indicates this option is disabled. This `gcsfuse` option is disabled by default. | `""`  
  
### `--client-protocol`

| Specifies the protocol used for communicating with the Cloud Storage backend. | 

  * `http1` for HTTP/1.1
  * `http2` for HTTP/2
  * `grpc` for [gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api). To use gRPC with Cloud Storage FUSE, we recommend using [Cloud Storage FUSE versions 2.10.0](https://github.com/GoogleCloudPlatform/gcsfuse/releases/tag/v2.10.0) or later.

| `http1`  
  
### `--cloud-metrics-export-interval-secs`

| Exports metrics to Cloud Monitoring with the specified interval. **Note** : Using this option requires additional setup. For more information, see [Set up the Cloud Monitoring exporter](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/metrics#set-up-cloud-exporter). | Integer representing a value in seconds, for example: `10` (10 seconds). `0` specifies no exporting. | `0`  
  
### `--config-file`

| Specifies the path to the [configuration file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file) you want to use to configure Cloud Storage FUSE behaviors. | A path, for example: `/etc/gcsfuse.yaml`. | `""`  
  
### `--custom-endpoint`

| Specifies an alternative custom endpoint for fetching data. The custom endpoint must support the equivalent resources and operations as the Cloud Storage gRPC endpoint, `storage.googleapis.com:443`, or the Cloud Storage JSON endpoint, `https://storage.googleapis.com/storage/v1`. If a custom endpoint isn't specified, Cloud Storage FUSE uses the global Cloud Storage JSON endpoint. If authentication isn't supported on the custom endpoint you specify, set the `--anonymous-access` `gcsfuse` option to `true` to bypass authentication. | An endpoint, for example: `storage.googleapis.com:443`. | `""`  
  
### `--debug_fuse` (deprecated)

| Enables [FUSE-related](https://www.kernel.org/doc/html/next/filesystems/fuse.html) debugging output. This option has been replaced by the `--log-severity` `gcsfuse` option. To enable debugging output, set the `--log-severity` `gcsfuse` option to `trace`, which includes trace, debug, info, warning, and error logs. | Boolean value: `true`, `false`. | `false`  
  
### `--debug_gcs` (deprecated)

| Prints Cloud Storage request and timing information. This `gcsfuse` option has been replaced by the `--log-severity` `gcsfuse` option. To enable debugging output, set the `--log-severity` `gcsfuse` option to `trace`, which includes trace, debug, info, warning, and error logs. | Boolean value: `true`, `false`. | `false`  
  
### `--debug_invariants`

| Exits the program when internal invariant violations are detected. | Boolean value: `true`, `false`. | `false`  
  
### `--debug_mutex`

| Prints debug messages when a mutex is held too long. If this `gcsfuse` option is specified, the severity level of logs is automatically set to `trace`, which includes trace, debug, info, warning, and error logs. | Boolean value: `true`, `false`. | `false`  
  
### `--dir-mode`

| Permissions bits for directories, in octal. | String value representing an octal integer between `"000"` and `"777"` (inclusive), for example: `"755"`. | `755`  
  
### `--enable-buffered-read`

| Specifies asynchronous prefetching of parts of a Cloud Storage object into an in-memory buffer, allowing subsequent reads to be served from the buffer instead of requiring network calls. | Boolean value: `true`, `false` | `false`  
  
### `--enable-nonexistent-type-cache` (deprecated)

| Creates a type cache entry with the type `NonexistentType` if a file isn't found in Cloud Storage. If the file gets created in Cloud Storage but the `NonexistentType` entry for the file is cached, then Cloud Storage FUSE cannot request that file until the `NonexistentType` entry is removed from the type cache. | Boolean value: `true`, `false`. | `false`  
  
### `--enable-streaming-writes`

| Controls the write path flow so that data is uploaded directly to Cloud Storage as its written instead of fully staging the write locally and uploading it upon `close()` or `fsync()`. For more information about streaming writes, see [Cloud Storage FUSE semantics](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md) in the Cloud Storage FUSE GitHub documentation. | Boolean value: `true`, `false`. | `true`  
  
### `--file-cache-max-size-mb`

| Specifies the maximum size in MiB that the [file cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching) can use and lets you limit the total capacity the file cache can use within its mounted directory. **Note** : Before you set the `--file-cache-max-size-mb` `gcsfuse` option, you must first specify the [`cache-dir` `gcsfuse` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#cache-dir). For Compute Engine VMs (including standalone Cloud Storage FUSE or non-Google Kubernetes Engine based deployments), enabling `cache-dir` automatically sets `--file-cache-max-size-mb` to `-1`. | 

  * Integer
  * `-1`: Specifies the use of the cache's entire available capacity in the directory you specify for `cache-dir`. This is the default only if `cache-dir` is passed.
  * `0`: Disables the file cache.

| `-1`  
  
### `--file-cache-cache-file-for-range-read`

| Determines whether the full object should be downloaded asynchronously and stored in the Cloud Storage FUSE cache directory when the first read is completed from a non-zero offset. This `gcsfuse` option should be set to `true` if you plan to perform several random reads or partial reads. **Note** : If you perform a partial read starting at offset `0`, Cloud Storage FUSE asynchronously downloads and caches the full object. | Boolean value: `true`, `false`. | `false`  
  
### `--file-cache-download-chunk-size-mb`

| Specifies the size of each read request in MiB that each [goroutine](https://go.dev/tour/concurrency/1) makes to Cloud Storage when downloading the object into the file cache. | Integer | `200`  
  
### `--file-cache-enable-parallel-downloads`

| Accelerates reads of large files by using the file cache directory as a prefetch buffer using multiple workers to download multiple parts of a file in parallel. Parallel downloads are automatically enabled when you enable file caching. To learn more about file caching, see [File caching in Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching). To learn more about parallel downloads and how to configure supporting properties, [Parallel downloads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching#parallel-downloads). | Boolean value: `true`, `false`. | `true`  
  
### `--file-cache-exclude-regex`

| A regular expression that specifies files to exclude from caching. If a file matches this regular expression, it isn't cached, even if it also matches `--file-cache-include-regex`. The regular expression is matched against file paths in the format `bucket_name/object_key`. For more information, see [Control cacheability at file granularity using regular expressions](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching#filter-files). | String value representing a regular expression. | `""`  
  
### `--file-cache-include-regex`

| A regular expression that specifies files to include in caching. If this option is used, only files matching this regular expression are cached. The regular expression is matched against file paths in the format `bucket_name/object_key`. For more information, see [Control cacheability at file granularity using regular expressions](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching#filter-files). | String value representing a regular expression. | `""`  
  
### `--file-cache-max-parallel-downloads`

| The maximum number of goroutines that can be spawned at any given time across all the download jobs of files. | 

  * Integer
  * `-1`: Specifies unlimited parallel downloads.
  * `0`: Disables parallel downloads. Can only be used if `--enable-parallel-downloads` is not passed or is passed as `false`.

| Twice the number of CPU cores on your machine or `16`, whichever is higher.  
  
### `--file-cache-parallel-downloads-per-file`

| The number of concurrent download requests per file. | Integer | `16`  
  
### `--file-mode`

| Specifies permissions bits for files, in octal. | String value representing an octal integer between `"000"` and `"777"` (inclusive), for example: `"644"`. | `644`  
  
### `--foreground`

| Runs the `gcsfuse` command in the foreground. | Boolean value: `true`, `false`. | `false`  
  
### `--gid`

| Specifies the Group Identifier (GID) owner of all inodes. | 

  * Integer representing a GID.
  * `-1`: The GID of the caller is used.

| `-1`  
  
### `--help`

| Displays help about Cloud Storage FUSE. | None | None  
  
### `--version`

| Displays the Cloud Storage FUSE version you have installed. | None | None  
  
### `--http-client-timeout`

| Specifies how long the Cloud Storage FUSE HTTP client can wait to get a response from the server before timing out. | Duration, for example: `1h10m10s` for 1 hour, 10 minutes, and 10 seconds. `0s` specifies no timeout. | `0s`  
  
### `--ignore-interrupts`

| Instructs Cloud Storage FUSE to ignore system interrupt signals, like SIGINT triggered by `Control+C`. This prevents signals from terminating in-flight operations. | Boolean value: `true`, `false`. | `true`  
  
### `--implicit-dirs`

| Implicitly includes [folders](https://docs.cloud.google.com/storage/docs/objects#simulated-folders) and [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders). See [Files and directories](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/docs/semantics.md#files-and-directories) in the Cloud Storage FUSE GitHub documentation for more information. | Boolean value: `true`, `false`. | `false`  
  
### `--kernel-list-cache-ttl-secs`

| Enables the [list cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/list-caching) and defines the time to live (TTL) in seconds of cached list entries. The list cache is kept in memory in the page cache, which is controlled by the kernel based on available memory. **Note** : Recommended for read-only mounts to avoid consistency issues. For more information, see the [performance tuning best practices for list caching](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance#kernel-list-caching).  | 

  * Integer representing seconds, for example: `10` (10 seconds).
  * `0`: Disables list caching.
  * `-1`: Bypasses entry expiration and always returns the list response from the cache when it's available.

| `0`  
  
### `--key-file`

| Specifies an absolute path to the credential JSON key file for authenticating requests to Cloud Storage. By default, Cloud Storage FUSE uses [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) to authenticate requests. | A path, for example: `/home/example_user/gcloud-key.json`. | When this option is not set, Application Default Credentials are used.  
  
### `--limit-bytes-per-sec`

| Specifies the bandwidth limit at which Cloud Storage FUSE can read data from Cloud Storage, measured over a 30-second window. | Floating point number. `-1` specifies no limit. | `-1`  
  
### `--limit-ops-per-sec`

| Specifies a limit for operations performed per second, measured over a 30-second window. | Floating point number. `-1` specifies no limit. | `-1`  
  
### `--log-file`

| Specifies the file for storing logs that can be parsed by [Fluentd](https://www.fluentd.org/). | A path, for example: `/tmp/user-example-bucket-gcsfuse-logs.txt`. | `stdout` when Cloud Storage FUSE is run in the foreground or `syslog` when Cloud Storage FUSE is run in the background  
  
### `--log-format`

| Specifies the format of the log file. | 

  * `text`
  * `json`

| `json`  
  
### `--log-rotate-backup-file-count`

| The maximum number of rotated log files to retain, excluding the active file that logs are written to. | 

  * Integer
  * `0`: Retains all rotated log files

| `10`  
  
### `--log-rotate-compress`

| Specifies whether rotated log files are compressed using [`gzip`](https://www.gzip.org/). | Boolean value: `true`, `false`. | `true`  
  
### `--log-rotate-max-file-size-mb`

| The maximum size in megabytes (MB) that log files can reach before being rotated. | Integer. The minimum value is `1`. | `512`  
  
### `--log-severity`

| The severity level you want Cloud Storage FUSE to generate logs for. The severity levels are ordered from lowest severity to highest severity. For example, when you specify `warning`, Cloud Storage FUSE generates logs for warnings and errors. Generally, we recommend using the `info` severity level. **Note:** If you specify `--debug_mutex` as part of your command, the severity level is automatically set to `trace` and overrides `log-severity`.**Note:** Using either the `trace` or `debug` severity levels when file caching is enabled can result in performance degradation due to logging overhead and should only be used temporarily such as during troubleshooting. | 

  * `off`: disables all logging.
  * `error`: contains messages about serious issues that prevent Cloud Storage FUSE from completing an operation, or indicate a failure such as mount failures, permission errors, and critical input/output (I/O) errors.
  * `warning`: contains messages indicating potential issues that aren't critical but can lead to issues if not addressed. Potential issues include non-fatal connection issues, deprecation warnings, resource contention that might cause slight performance degradation, and retries for transient failures. This severity level also includes information provided in the `error` severity level.
  * `info`: contains general logging information such as startup and shutdown messages, or information about successful mount operations, progress updates, and configuration settings. This severity level also includes information about the `warning` and `error` severity levels.
  * `debug`: contains logging information such as startup and shutdown messages, or information about successful mount operations, progress updates, and configuration settings. This severity level also includes the information provided in the `info`, `warning`, and `error` severity levels.
  * `trace`: contains granular details about each Cloud Storage FUSE operation and function call, outlining the `gcsfuse` interaction with the kernel FUSE driver and Cloud Storage. This severity level also includes the details provided in `debug`, `info`, `warning`, and `error` severity levels.

| `info`  
  
### `--max-conns-per-host`

| Specifies the maximum number of TCP connections allowed per server. This becomes effective when `--client-protocol` is set to `http1`. | Integer between `0` and `2147483647`. `0` specifies no limit on TCP connections. | `0`  
  
### `--max-idle-conns-per-host`

| Specifies the maximum number of idle connections allowed per server. This becomes effective when `--client-protocol` is set to `http1`. | Integer between `0` and `2147483647`. `0` specifies no limit on idle connections. | `0`  
  
### `--max-retry-attempts`

| Specifies the maximum number of times an operation is retried if the operation fails, preventing endless retry loops. | 

  * Integer representing the maximum number of retry attempts, for example: `10`.
  * `0`: Allows unlimited retry attempts.

| `0`  
  
### `--max-retry-sleep`

| Specifies the maximum duration that Cloud Storage FUSE is allowed to sleep in a retry loop with [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy). Once the backoff duration exceeds the specified maximum duration, the retry continues with the specified maximum duration. | Duration, for example: `1h5m50s` (1 hour, 5 minutes, and 50 seconds) or `60s` (60 seconds). | `30s`  
  
### `--metadata-cache-negative-ttl-secs`

| Defines the time to live (TTL) in seconds of [negative stat cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/stat-caching#negative-stat-caching) entries, which store results for non-existent files in the cache. | 

  * Integer representing seconds, for example: `10` (10 seconds).
  * `0`: Disables negative stat caching.
  * `-1`: Allows unlimited negative stat caching and disables a TTL expiration.

| `5`  
  
### `--metadata-cache-ttl-secs`

| Defines the time to live (TTL) in seconds of cached metadata entries. | 

  * Integer representing seconds, for example: `30` (30 seconds).
  * `-1`: Bypass TTL expiration and serve files from the cache whenever they're available.
  * `0`: Use the most up-to-date file. Using this value issues a `Get` metadata call to make sure that the object generation for the file in the cache matches what's stored in Cloud Storage.

| `60`  
  
### `-o`

| Specifies additional system-specific mount options. Most generic mount options in `FUSE` such as `suid` are supported by Cloud Storage FUSE and can be passed along with the `-o` option. | [Mount options in FUSE](https://man7.org/linux/man-pages/man8/mount.fuse3.8.html), for example: 

  * `rw`: Mount as read-write.
  * `ro`: Mount as read-only.

| `""`  
  
### `--only-dir`

| Mounts only a specific directory within a bucket. | A path, for example: `/etc/gcsfuse.yaml`. | `""`  
  
### `--profile`

| Applies a predefined, optimized set of Cloud Storage FUSE configurations for caching, threading, and buffer sizes to help you achieve high performance for a specific workload type, such as training, serving, and checkpointing. To learn more about each predefined configuration based on your workload type, see [Profile-based configurations for AI/ML workloads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/profile-based-configurations). | 

  * A string, for example, `"aiml-checkpointing"`.
  * `"aiml-training"`: optimizes performance for high throughput reads of large datasets and prevents Cloud GPUs and Cloud TPU hardware from waiting for data.
  * `aiml-checkpointing`: optimizes performance for high throughput writes for large files by drastically reducing the time it takes to save multi-gigabyte checkpoints, minimizing training pauses.
  * `aiml-serving`: optimizes performance for serving workloads by streamlining data access and applying caching mechanisms.

| `""`  
  
### `--prometheus-port`

| Exposes Prometheus metrics endpoint on the specified port and `/metrics` path. **Note** : Using this option requires additional setup. For more information, see [Set up the Prometheus exporter](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/metrics#prometheus-port-exporter). | Integer representing the port you want to specify. | `0`  
  
### `--read-global-max-blocks`

| Specifies the maximum number of blocks available for buffered reads across all file handles. **Note** : Using this `gcsfuse` option requires enabling the `--enable-buffered-read` option. For more information, see the [`--enable-buffered-read` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#enable-buffered-read). | 

  * Integer
  * `0`: disables buffered reads.
  * `-1`: sets the value to unlimited blocks.

| `40`  
  
### `--rename-dir-limit`

| Allows the renaming of directories containing fewer descendants than the specified limit. | Integer between `0` and `2147483647`. | `0`  
  
### `--retry-multiplier`

| Specifies the multiplier for exponential backoff between consecutive retries. | Floating-point number. | `2`  
  
### `--reuse-token-from-url`

| Specifies whether to reuse the token acquired from `--token-url`. | Boolean value: `true`, `false`. | `true`  
  
### `--sequential-read-size-mb`

| Specifies the chunk size of the data to be downloaded from Cloud Storage, in megabytes (MB). | Integer between `1` and `1024`. | `200`  
  
### `--stat-cache-capacity` (deprecated)

| Specifies the number of entries that the [stat cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/stat-caching) can hold. This `gcsfuse` option has been replaced by the `--stat-cache-max-size-mb` `gcsfuse` option. | Integer | `4096`  
  
### `--stat-cache-max-size-mb`

| The maximum size memory that the [stat cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/stat-caching) can use, in MiB. The stat cache is always entirely kept in memory. | 

  * Integer. We recommend the following:
    * `34` if your workload involves up to 20,000 files.
    * If your workload is larger than 20,000 files, increase the size by values of 10 for every additional 6,000 files, where the stat cache uses an average of 1,720 bytes per file (including 220 for type information).
  * `-1`: Sets no limit, where the stat cache use as much memory as needed.
  * `0`: Disables the stat cache.

| `34`  
  
### `--stat-cache-ttl` (deprecated)

| Specifies how long to cache `StatObject` results and inode attributes. This option has been replaced by the `--metadata-cache-ttl-secs` `gcsfuse` option. | Duration, for example: `20s` (20 seconds). | `60s`  
  
### `--temp-dir`

| Specifies a path to the temporary directory where writes are staged prior to being uploaded to Cloud Storage. | A path, for example: `/mnt/ssd/example-user-gcsfuse-temp-dir`. | ``/tmp``  
  
### `--token-url`

| Specifies a URL for getting an access token when the `--key-file` is absent. | A URL. | `""`  
  
### `--type-cache-ttl` (deprecated)

| Specifies how long to cache the mapping between names and files or directories in directory inodes, in seconds. This `gcsfuse` option has been replaced by the `--metadata-cache-ttl-secs` `gcsfuse` option. | Duration in seconds, for example: `20s` (20 seconds). | `60s`  
  
### `--type-cache-max-size-mb` (deprecated)

| The maximum size in MiB per directory that the type cache can use. The type cache is always entirely kept in memory. | 

  * Integer. We recommend the following: 
    * `4` if the maximum number of files within a single directory from the bucket you're mounting contains 20,000 files or less.
    * If the maximum number of files within a single directory that you're mounting contains more than 20,000 files, increase the value by `1` for every 5,000 files, which is an average of around 200 bytes per file.
  * `-1`: Specifies no limit and lets the type cache use as much memory as needed.
  * `0`: Disables the type cache.

| `4`  
  
### `--enable-metadata-prefetch`

| Enables background prefetching of metadata for objects within a directory during a cache miss. This flag performs a batch update to the metadata cache, significantly reducing latency for subsequent lookups of files in the directory.  | Boolean value: `true`, `false`. | `false`  
  
### `--metadata-prefetch-entries-limit`

|  Specifies the maximum metadata entries to prefetch per directory. Values specifying more than 5000 metadata entries results in multiple sequential Cloud Storage `Objects: list` calls, as each individual call is limited to 5000 results.  | Integer between `-1` and `2147483647`. Set to `-1` to prefetch all entries. | `5000`  
  
### `--metadata-prefetch-max-workers`

| The maximum number of concurrent background workers allowed to perform metadata prefetching across all directories.  | Integer between `-1` and `2147483647`. Set to `-1` for unlimited workers. | `10`  
  
### `--uid`

| Specifies the User Identifier (UID) owner of all inodes. | 

  * Integer representing a UID.
  * `-1`: The UID of the caller is used.

| `-1`  
  
### `--write-global-max-blocks`

| Specifies the maximum number of data chunks available for streaming writes across all files. Each file uses one 32 MiB data chunk by default. | 

  * Integer
  * `0`: disables streaming writes.
  * `-1`: sets the value to unlimited chunks.

| 

  * Default value for low-specification machines with limited resources: `4`
  * Default value for high-specification machines with a large amount of resources: `1600`

  
  
Back to top

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
