---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/
title: Google Cloud Spanner for PHP \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:11:22.100889+00:00
---

# Google Cloud Spanner for PHP  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Spanner for PHP Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

> Idiomatic PHP client for [Cloud Spanner](https://cloud.google.com/spanner/).

[![Latest Stable Version](https://poser.pugx.org/google/cloud-spanner/v/stable)](https://packagist.org/packages/google/cloud-spanner) [![Packagist](https://img.shields.io/packagist/dm/google/cloud-spanner.svg)](https://packagist.org/packages/google/cloud-spanner)

**NOTE:** This repository is part of [Google Cloud PHP](https://github.com/googleapis/google-cloud-php). Any support requests, bug reports, or development contributions should be directed to that project.

A fully managed, mission-critical, relational database service that offers transactional consistency at global scale, schemas, SQL (ANSI 2011 with extensions), and automatic, synchronous replication for high availability.

### Installation

To begin, install the preferred dependency manager for PHP, [Composer](https://getcomposer.org/).

Now install this component:
    
    
    $ composer require google/cloud-spanner
    

This component requires the gRPC extension. Please see our [gRPC installation guide](https://cloud.google.com/php/grpc) for more information on how to configure the extension.

### Authentication

Please see our [Authentication guide](https://github.com/googleapis/google-cloud-php/blob/main/AUTHENTICATION.md) for more information on authenticating your client. Once authenticated, you'll be ready to start making requests.

### Sample
    
    
    use Google\Cloud\Spanner\SpannerClient;
    
    // Create a client.
    $spannerClient = new SpannerClient();
    
    $db = $spanner->connect('my-instance', 'my-database');
    
    $userQuery = $db->execute('SELECT * FROM Users WHERE id = @id', [
        'parameters' => [
            'id' => $userId
        ]
    ]);
    
    $user = $userQuery->rows()->current();
    
    echo 'Hello ' . $user['firstName'];
    

### Multiplexed Sessions

The V2 version of the Spanner Client Library for PHP uses [Multiplexed Sessions](https://cloud.google.com/spanner/docs/sessions#multiplexed_sessions). Multiplexed Sessions allow your application to create a large number of concurrent requests on a single session. Some advantages include reduced backend resource consumption due to a more straightforward session management protocol, and less management as sessions no longer require cleanup after use or keep-alive requests when idle.

#### Session Caching

The session cache is configured with a default cache which uses the PSR-6 compatible [`SysvCacheItemPool`](https://github.com/googleapis/google-auth-library-php/blob/main/src/Cache/SysVCacheItemPool.php) when the [`sysvshm`](https://www.php.net/manual/en/book.sem.php) extension is enabled, and [`FileSystemCacheItemPool`](https://github.com/googleapis/google-auth-library-php/blob/main/src/Cache/FileSystemCacheItemPool.php) when `sysvshm` is not available. This ensures that your processes share a single multiplex session for each database and creator role.

To change the default cache pool, use the option `cacheItemPool` when instantiating your Spanner client:
    
    
    use Google\Cloud\Spanner\SpannerClient;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    // available by running `composer install symfony/cache`
    $fileCacheItemPool = new FilesystemAdapter();
    // configure through SpannerClient constructor
    $spanner = new SpannerClient(['cacheItemPool' => $fileCacheItemPool]);
    $database = $spanner->instance($instanceId)->database($databaseId);
    

This can also be passed in as an option to the `instance` or `database` methods:
    
    
    $spanner = new SpannerClient();
    // configure through instance method
    $database = $spanner
        ->instance($instanceId, ['cacheItemPool' => $fileCacheItemPool])
        ->database($databaseId);
    // configure through database method
    $database = $spanner
        ->instance($instanceId)
        ->database($databaseId, ['cacheItemPool' => $fileCacheItemPool]);
    

#### Refreshing Sessions

Sessions will refresh synchronously every 7 days. You can use this script to refresh the session asynchronously, in to avoid latency in your application (recommended every ~24 hours):
    
    
    // If you are using a custom PSR-6 cache via the "cacheItemPool" client option in your
    // application, you will need to supply a cache with the same configuration here in
    // order to properly refresh the session.
    $spanner = new SpannerClient();
    
    $sessionCache = $spanner
        ->instance($instanceId)
        ->database($databaseId)
        ->session();
    
    // this will force-refresh the session
    $sessionCache->refresh();
    

#### Session Locking

Locking occurs when a new session is created, and ensures no race conditions occur when a session expires. Locking uses a [`Semaphore`](https://github.com/googleapis/google-cloud-php/blob/main/Core/src/Lock/SemaphoreLock.php) lock when `sysvmsg`, `sysvsem`, and `sysvshm` extensions are enabled, and a [`Flock`](https://github.com/googleapis/google-cloud-php/blob/main/Core/src/Lock/FlockLock.php) lock otherwise. To configure a custom lock, supply a class implementing [`LockInterface`](https://github.com/googleapis/google-cloud-php/blob/main/Core/src/Lock/LockInterface.php) when calling `Instance::database`. Here's an example which encorporates the [Symfony Lock component](https://symfony.com/doc/current/components/lock.html):
    
    
    use Google\Cloud\Core\Lock\LockInterface;
    use Google\Cloud\Spanner\SpannerClient;
    use Symfony\Component\Lock\LockFactory;
    use Symfony\Component\Lock\SharedLockInterface;
    use Symfony\Component\Lock\Store\SemaphoreStore;
    
    // Available by running `composer install symfony/lock`
    $store = new SemaphoreStore();
    $factory = new LockFactory($store);
    
    // Create an adapter for Symfony's SharedLockInterface and Google's LockInterface
    $lock = new class ($factory->createLock($databaseId)) implements LockInterface {
        public function __construct(private SharedLockInterface $lock) {
        }
    
        public function acquire(array $options = []) {
            return $this->lock->acquire()
        }
    
        public function release() {
            return $this->lock->acquire()
        }
    
        public function synchronize(callable $func, array $options = []) {
            if ($this->lock->acquire($options['blocking'] ?? true)) {
                return $func();
            }
        }
    }
    
    // Configure our custom lock on our database using the "lock" option
    $spanner = new SpannerClient();
    $database = $spanner
        ->instance($instanceId)
        ->database($databaseId, ['lock' => $lock]);
    

### Client-Side Metrics

The Cloud Spanner client library supports exporting built-in client-side metrics to Google Cloud Monitoring using OpenTelemetry. These metrics provide detailed observability into operations, RPC attempts, and Google Front End (GFE) or Spanner API Frontend (AFE) latencies.

To enable client-side metrics:
    
    
    use Google\Cloud\Spanner\SpannerClient;
    
    $spanner = new SpannerClient([
        'enableBuiltInMetrics' => true,
        // optional: timeout in milliseconds for metric export calls
        'metricsTimeoutMillis' => 100 
    ]);
    

All captured metrics are aggregated in-memory and exported synchronously during the PHP process shutdown phase.

Warning

**Performance Caveat** : Because PHP has a share-nothing architecture, exporting metrics synchronously at shutdown will add to the total request execution latency of the PHP process. For this reason, it is advised to enable built-in metrics primarily for debugging and active performance monitoring. 

To minimize this performance overhead, installing the PECL [`ext-opentelemetry`](https://pecl.php.net/package/opentelemetry) extension is **highly recommended**.

#### Prerequisites

  1. **IAM Permissions & OAuth Scopes**: The credentials used by your application require the `monitoring.timeSeries.create` permission (provided by the **Metric Writer** role `roles/monitoring.metricWriter`). Standard Spanner roles (`roles/spanner.databaseAdmin`, `roles/spanner.databaseUser`, and `roles/spanner.databaseReader`) already include this permission.
     * When using Application Default Credentials (ADC) or keyfiles, the required `https://www.googleapis.com/auth/monitoring.write` OAuth scope is automatically configured.
     * If you supply a pre-instantiated credentials object (implementing `FetchAuthTokenInterface` or `CredentialsWrapper`), ensure that `https://www.googleapis.com/auth/monitoring.write` (or `https://www.googleapis.com/auth/cloud-platform`) scope is included when creating your credentials object.
  2. **OpenTelemetry Extension** : Installing the [`ext-opentelemetry`](https://pecl.php.net/package/opentelemetry) PHP extension is highly advised to optimize metrics collection and export performance.



### Setting a Default Timeout for Every Call

Individual calls accept a `timeoutMillis` option. To change the default deadline for _every_ call a client makes, pass a `clientConfig` array. `SpannerClient` builds three generated clients from the same options, so the config has to cover all three interfaces:
    
    
    use Google\Cloud\Spanner\SpannerClient;
    
    $timeoutMillis = 5000;
    $configFiles = [
        'src/V1/resources/spanner_client_config.json',
        'src/Admin/Instance/V1/resources/instance_admin_client_config.json',
        'src/Admin/Database/V1/resources/database_admin_client_config.json',
    ];
    
    $clientConfig = ['interfaces' => []];
    foreach ($configFiles as $configFile) {
        $path = $vendorDir . '/google/cloud-spanner/' . $configFile;
        $decoded = json_decode(file_get_contents($path), true);
        foreach ($decoded['interfaces'] as $interface => $settings) {
            foreach (array_keys($settings['methods']) as $method) {
                $settings['methods'][$method]['timeout_millis'] = $timeoutMillis;
            }
            foreach (array_keys($settings['retry_params']) as $name) {
                $settings['retry_params'][$name]['initial_rpc_timeout_millis'] = $timeoutMillis;
                $settings['retry_params'][$name]['max_rpc_timeout_millis'] = $timeoutMillis;
                $settings['retry_params'][$name]['total_timeout_millis'] = $timeoutMillis;
            }
            $clientConfig['interfaces'][$interface] = $settings;
        }
    }
    
    $spanner = new SpannerClient(['clientConfig' => $clientConfig]);
    

Warning

Setting `timeout_millis` on its own has no effect on retryable methods — it only supplies `noRetriesRpcTimeoutMillis`. The `retry_params` values are what determine the deadline, which is why they are overridden above. Likewise, a config containing only `google.spanner.v1.Spanner` leaves the admin clients without retry settings and calls to them fail with a `TypeError`. Read the shipped JSON files at runtime rather than copying them into your project, so that methods added in later releases are picked up.

See the [Client Configuration guide](https://github.com/googleapis/google-cloud-php/blob/main/CLIENT_CONFIGURATION.md) for the full set of retry and timeout options.

### Debugging

Please see our [Debugging guide](https://github.com/googleapis/google-cloud-php/blob/main/DEBUG.md) for more information about the debugging tools.

### Version

This component is considered GA (generally available). As such, it will not introduce backwards-incompatible changes in any minor or patch releases. We will address issues and requests with the highest priority.

### Next Steps

  1. Understand the [official documentation](https://cloud.google.com/spanner/docs/).
  2. Take a look at [in-depth usage samples](https://github.com/GoogleCloudPlatform/php-docs-samples/tree/master/spanner/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
