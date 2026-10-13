---
url: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.CacheSessionPool
title: Cloud Spanner Client - Class CacheSessionPool (1.106.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:45.971598+00:00
---

# Cloud Spanner Client - Class CacheSessionPool (1.106.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.CacheSessionPool

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Spanner Client - Class CacheSessionPool (1.106.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.11.2 (latest)  2.11.1  2.10.1  2.9.0  2.8.1  2.7.0  2.6.1  2.5.1  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1-RC1  1.106.0  1.105.1  1.104.1  1.103.0  1.102.0  1.101.0  1.100.0  1.98.0  1.97.0  1.96.0  1.95.0  1.94.0  1.93.1  1.92.1  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.1  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.2  1.62.1  1.61.0  1.60.0  1.59.0  1.58.4  1.57.0  1.56.0  1.55.0  1.54.2 

Reference documentation and code samples for the Cloud Spanner Client class CacheSessionPool.

This session pool implementation accepts a PSR-6 compatible cache implementation and utilizes it to store sessions between requests.

We provide `Google\Auth\Cache\SysVCacheItemPool`, which is a fast PSR-6 implementation in `google/auth` library. If your PHP has `sysvshm` extension enabled (most binary distributions have it compiled in), consider using it. Please note the SysVCacheItemPool implementation defaults to a memory allotment that may not meet your requirements. We recommend setting the memsize setting to 250000 (250kb) as it should safely contain the default 500 maximum sessions the pool can handle. Please modify this value accordingly depending on the number of maximum sessions you would like for the pool to handle.

Please note that when [CacheSessionPool::acquire()](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.CacheSessionPool#_Google_Cloud_Spanner_Session_CacheSessionPool__acquire__) is called at most only a single session is created. Due to this, it is possible to sit under the minimum session value declared when constructing this instance. In order to have the pool match the minimum session value please use the [CacheSessionPool::warmup()](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.CacheSessionPool#_Google_Cloud_Spanner_Session_CacheSessionPool__warmup__) method. This will create as many sessions as needed to match the minimum value, and is the recommended way to bootstrap the session pool.

Sessions are created on demand up to the maximum session value set during instantiation of the pool. To help ensure the minimum number of sessions required are managed by the pool, attempts will be made to automatically downsize after every 10 minute window. This feature is configurable and one may also downsize at their own choosing via [CacheSessionPool::downsize()](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.CacheSessionPool#_Google_Cloud_Spanner_Session_CacheSessionPool__downsize__). Downsizing will help ensure you never run into issues where the Spanner backend is locked up after having met the maximum number of sessions assigned per node. For reference, the current maximum sessions per database per node is 10k. For more information on limits please see [here](https://cloud.google.com/spanner/docs/limits).

When expecting a long period of inactivity (such as a maintenance window), please make sure to call [CacheSessionPool::clear()](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.CacheSessionPool#_Google_Cloud_Spanner_Session_CacheSessionPool__clear__) in order to delete any active sessions.

If you're on Windows, or your PHP doesn't have `sysvshm` extension, unfortunately you can not use `Google\Auth\Cache\SysVCacheItemPool`. In such cases, it will be necessary to include a separate dependency to fulfill this requirement. The below example makes use of [Symfony's Cache Component](https://github.com/symfony/cache). For more implementations please see the [Packagist PHP Package Repository](https://packagist.org/providers/psr/cache-implementation).

Example:
    
    
    use Google\Cloud\Spanner\SpannerClient;
    use Google\Cloud\Spanner\Session\CacheSessionPool;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    
    $spanner = new SpannerClient();
    $cache = new FilesystemAdapter();
    $sessionPool = new CacheSessionPool($cache);
    
    $database = $spanner->connect('my-instance', 'my-database', [
        'sessionPool' => $sessionPool
    ]);
    
    
    
    // Labels configured on the pool will be applied to each session created by the pool.
    use Google\Cloud\Spanner\Session\CacheSessionPool;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    
    $cache = new FilesystemAdapter();
    $sessionPool = new CacheSessionPool($cache, [
        'labels' => [
            'environment' => getenv('APPLICATION_ENV')
        ]
    ]);
    

Database role configured on the pool will be applied to each session created by the pool.
    
    
    use Google\Cloud\Spanner\SpannerClient;
    use Google\Cloud\Spanner\Session\CacheSessionPool;
    use Symfony\Component\Cache\Adapter\FilesystemAdapter;
    
    $spanner = new SpannerClient();
    $cache = new FilesystemAdapter();
    $sessionPool = new CacheSessionPool($cache, [
        'databaseRole' => 'Reader'
    ]);
    
    $database = $spanner->connect('my-instance', 'my-database', [
        'sessionPool' => $sessionPool
    ]);
    

## Namespace

Google \ Cloud \ Spanner \ Session

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`cacheItemPool` |  `Psr\Cache\CacheItemPoolInterface`   
A PSR-6 compatible cache implementation used to store the session data.  
`config` |  `array`   
Configuration Options.  
`↳ maxSessions` |  `int`   
The maximum number of sessions to store in the pool. **Defaults to** `500`.  
`↳ minSessions` |  `int`   
The minimum number of sessions to store in the pool. **Defaults to** `1`.  
`↳ shouldWaitForSession` |  `bool`   
If the pool is full, whether to block until a new session is available. _*Defaults to_ `true`.  
`↳ maxCyclesToWaitForSession` |  `int`   
The maximum number cycles to wait for a session before throwing an exception. **Defaults to** `30`. Ignored when $shouldWaitForSession is `false`.  
`↳ sleepIntervalSeconds` |  `float`   
The sleep interval between cycles. **Defaults to** `0.5`. Ignored when $shouldWaitForSession is `false`.  
`↳ lock` |  `LockInterface`   
A lock implementation capable of blocking. **Defaults to** a semaphore based implementation if the required extensions are installed, otherwise an flock based implementation.  
`↳ shouldAutoDownsize` |  `bool`   
Determines whether or not to automatically attempt to downsize the pool after every 10 minute window. **Defaults to** `true`.  
`↳ labels` |  `array`   
Labels to be applied to each session created in the pool. Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`. Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`. No more than 64 labels can be associated with a given session. See <https://goo.gl/xmQnxf> for more information on and examples of labels.  
`↳ databaseRole` |  `string`   
The user created database role which creates the session.  
  
### acquire

Acquire a session from the pool.

**Parameter**  
---  
**Name** | **Description**  
`context` |  `string`   
The type of session to fetch. May be either `r` (READ) or `rw` (READ/WRITE). **Defaults to** `r`.  
**Returns**  
---  
**Type** | **Description**  
`[Session](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.Session)` |   
  
### release

Release a session back to the pool.

**Parameter**  
---  
**Name** | **Description**  
`session` |  `[Session](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.Session)`   
The session.  
  
### keepAlive

Keeps a checked out session alive.

In use sessions that have not had their `lastActive` time updated in the last 20 minutes will be considered eligible to be moved back into the queue if the max sessions value has been met. In order to work around this when performing a large streaming execute or read call please make sure to call this method roughly every 15 minutes between reading rows to keep your session active.

**Parameter**  
---  
**Name** | **Description**  
`session` |  `[Session](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Session.Session)`   
The session to keep alive.  
  
### downsize

Downsizes the queue of available sessions by the given percentage. This is relative to the minimum sessions value. For example: Assuming a full queue, with maximum sessions of 10 and a minimum of 2, downsizing by 50% would leave 6 sessions in the queue. The count of items to be deleted will be rounded up in the case of a fraction.

Please note this method will attempt to synchronously delete sessions and will block until complete.

**Parameter**  
---  
**Name** | **Description**  
`percent` |  `int`   
The percentage to downsize the pool by. Must be between 1 and 100.  
**Returns**  
---  
**Type** | **Description**  
`int` | The number of sessions removed from the pool.  
  
### warmup

Create enough sessions to meet the minimum session constraint.

**Returns**  
---  
**Type** | **Description**  
`int` | The number of sessions created and added to the queue.  
  
### clear

Clear the cache and attempt to delete all sessions in the pool.

A session may be removed from the cache, but still tracked as active by the Spanner backend if a delete operation failed. To ensure you do not exceed the maximum number of sessions available per node, please be sure to check the return value of this method to be certain all sessions have been deleted.

**Returns**  
---  
**Type** | **Description**  
`bool` | Returns false if some delete operations failed to delete. True if $waitForPromises flag is false or all delete are successful.  
  
### setDatabase

Set the database used to make calls to manage sessions.

**Parameter**  
---  
**Name** | **Description**  
`database` |  `[Google\Cloud\Spanner\Database](https://docs.cloud.google.com/php/docs/reference/cloud-spanner/latest/Database)`   
The database.  
  
### cacheItemPool

Get the underlying cache implementation.

**Returns**  
---  
**Type** | **Description**  
`Psr\Cache\CacheItemPoolInterface` |   
  
### maintain

Maintain queued sessions for selected database and keep them alive.

This method drops expired sessions and refreshes "old" ones (expiring in next 10 minutes). It can also refresh some non-"old" sessions to distribute refresh calls more or less evenly between maintenance calls. Only up to `minSessions` sessions are maintained, all excess ones are left to expire.

## Constants 

### CACHE_KEY_TEMPLATE
    
    
    Value: 'cache-session-pool.%s.%s.%s'

### DURATION_SESSION_LIFETIME
    
    
    Value: 28 * 24 * 3600

### DURATION_TWENTY_MINUTES
    
    
    Value: 1200

### DURATION_ONE_MINUTE
    
    
    Value: 60

### WINDOW_SIZE
    
    
    Value: 600

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
