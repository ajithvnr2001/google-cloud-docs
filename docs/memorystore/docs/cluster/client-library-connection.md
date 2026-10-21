---
url: https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection/
title: Client library connection code samples \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:10.367975+00:00
---

# Client library connection code samples  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/client-library-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Client library connection code samples Stay organized with collections  Save and categorize content based on your preferences. 

This page provides code samples for configuring client libraries to connect to clusters in Memorystore for Redis Cluster.

## Client library code sample

This section shows a [Lettuce](https://lettuce.io/) client library code sample for connecting to a cluster. For this sample, the cluster doesn't use [Identity and Access Management (IAM) authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth) or [in-transit encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption).

**Caution** : If you use Lettuce to connect to a cluster, then change the `validateClusterNodeMembership` parameter to `false`. Otherwise, when the topology changes, you might get `unknownPartition` errors.

### Lettuce

We recommend using Lettuce, versions 6.2.4 and later.
    
    
    // Create RedisURI from the MRC discovery endpoint
    RedisURI redisUri = RedisURI.Builder.redis(CLUSTER_DISC_EP_ADDR, CLUSTER_DISC_EP_PORT).build();
    
    // Configure client' resources
    // Configure reconnectDelay with exponential backoff and full jitter
    ClientResources resources = DefaultClientResources.builder()
                            .reconnectDelay(Delay.fullJitter(
        Duration.ofMillis(100),     // minimum 100 millisecond delay
        Duration.ofSeconds(5),      // maximum 5 second delay
        100, TimeUnit.MILLISECONDS) // 100 millisecond base
    ).build();
    
    // Create a cluster client with the URI and resources
    RedisClusterClient clusterClient = RedisClusterClient.create(resources, redisUri);
    
    // Configure the topology refreshment options
    // Enable periodic cluster topology updates so that the client updates the cluster topology in the intervals of
    // 60 seconds
    // Enable adaptive topology refresh that uses all triggers: MOVED_REDIRECT, ASK_REDIRECT,
    // PERSISTENT_RECONNECTS, UNCOVERED_SLOT, UNKNOWN_NODE
    // By enabling dynamicRefreshSources, the Lettuce client can query other healthy, discovered
    // nodes for topology updates if the main discovery endpoint is temporarily unavailable. This
    // prevents client-side topology desynchronization and reconnection loops during maintenance
    // events such as rolling OS upgrades where the discovery endpoint might be rotated.
    // Enable closing stale connections when refreshing the cluster topology. This reduces the need to handle
    // failed connections during command runtime.
    ClusterTopologyRefreshOptions topologyRefreshOptions = ClusterTopologyRefreshOptions.builder()
                                    .enablePeriodicRefresh(1, TimeUnit.MINUTES)
                                    .enableAllAdaptiveRefreshTriggers()
                                    .dynamicRefreshSources(true)
                                    .closeStaleConnections(true)
                                    .build();
    
    // Configure the socket options
    // Set connectTimeout based on your application requirements and workload
    // Enable TCP keepAlive to reduce the need to handle failed connections during command runtime
    SocketOptions socketOptions = SocketOptions.builder()
        .connectTimeout(CONNECT_TIMEOUT)
        .keepAlive(true)
        .build();
    
    // Configure the client options
    // Enable AutoReconnect when connection is lost
    // Set nodeFilter to filter out failed nodes from the topology
    // Disable validateClusterNodeMembership to allow redirecting commands to newly added nodes
    
    clusterClient.setOptions(ClusterClientOptions.builder()
                                    .topologyRefreshOptions(topologyRefreshOptions)
                .socketOptions(socketOptions)
                                    .autoReconnect(true)
                                    .nodeFilter(it ->
                                        ! (it.is(RedisClusterNode.NodeFlag.FAIL)
                                        || it.is(RedisClusterNode.NodeFlag.EVENTUAL_FAIL)
                                        || it.is(RedisClusterNode.NodeFlag.NOADDR)))
                                    .validateClusterNodeMembership(false)
                                    .build());
    
    // Create a connection pool
    GenericObjectPool<StatefulRedisClusterConnection<String, String> pool = ConnectionPoolSupport.createGenericObjectPool(() -> clusterClient.connect(), new GenericObjectPoolConfig());
    pool.setMaxTotal(MAX_CONNECTIONS_IN_CONNECTION_POOL);
    
    // Get a connection from the connection pool
    StatefulRedisClusterConnection<String, String> connection = pool.borrowObject();
    
    // Get a cluster sync command and call 'set'
    RedisAdvancedClusterCommands<String, String> syncCommands = connection.sync();
    syncCommands.set(key, value);

## In-transit encryption client library code sample

This section gives an example of client code for authenticating with in-transit encryption for your Memorystore cluster with the [go-redis](https://github.com/redis/go-redis) client library.

### go-redis

We recommend using go-redis, versions 9.11.0 and later.
    
    
    import (
      "context"
      "crypto/tls"
      "crypto/x509"
      "io/ioutil"
      "log"
      "time"
    
      "github.com/go-redis/redis/v9"
    )
    func example() {
            // Load CA cert
            caFilePath :=         caCert, err := ioutil.ReadFile(caFilePath)
            if err != nil {
                    log.Fatal(err)
            }
            caCertPool := x509.NewCertPool()
            caCertPool.AppendCertsFromPEM(caCert)
    
            // Setup Redis Connection pool
            client := redis.NewClusterClient(&redis.ClusterOptions{
                    Addrs: []string{"CLUSTER_DISC_EP_ADDR:CLUSTER_DISC_EP_PORT"},
                    // PoolSize applies per cluster node and not for the whole cluster.
                    PoolSize:        10,
                    ConnMaxIdleTime: 60 * time.Second,
                    MinIdleConns:    1,
                    TLSConfig: &tls.Config{
                            RootCAs: caCertPool,
                    },
            })
    
            ctx := context.Background()
            err = client.Set(ctx, "key", "value", 0).Err()
            if err != nil {
                    log.Fatal(err)
            }
    }

## IAM authentication and in-transit encryption code sample

This section gives an example of how to authenticate and connect to a cluster by using both IAM authentication and in-transit encryption with various client libraries:

### redis-py

We recommend using [redis-py](https://github.com/redis/redis-py), versions 5.1 and later.
    
    
    from google.cloud import [iam_credentials](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.html)_v1
    from redis.backoff import ConstantBackoff
    from redis.retry import Retry
    from redis.exceptions import (
     ConnectionError,
     AuthenticationWrongNumberOfArgsError,
     AuthenticationError
    )
    from redis.utils import (str_if_bytes)
    
    import redis
    
    service_account="projects/-/serviceAccounts/<TO-DO-1: email of service account used to authenticate to Redis Cluster>"
    
    host=<TO-DO-2: your Redis Cluster discovery endpoint ip>
    
    ssl_ca_certs=<TO-DO-3, your trusted server ca file name>
    
    def generate_access_token():
      # Create a client
      client = iam_credentials_v1.[IAMCredentialsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html)()
    
      # Initialize request argument(s)
      request = iam_credentials_v1.[GenerateAccessTokenRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateAccessTokenRequest.html)(
          name=service_account,
          scope=['https://www.googleapis.com/auth/cloud-platform'],
      )
    
      # Make the request
      response = client.[generate_access_token](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_generate_access_token)(request=request)
    
      # Handle the response
      return str(response.access_token)
    
    def iam_connect(connection: redis.Connection):
      "Initialize the connection and authenticate"
      connection._parser.on_connect(connection)
    
      auth_args = (generate_access_token(),)
      connection.send_command("AUTH", *auth_args, check_health=False)
    
      try:
          auth_response = connection.read_response()
      except AuthenticationWrongNumberOfArgsError:
          connection.send_command("AUTH", connection.password, check_health=False)
          auth_response = connection.read_response()
    
      if str_if_bytes(auth_response) != "OK":
          raise AuthenticationError("Invalid Username or Password")
    
    # Connect to Memorystore for Redis Cluster
    backoff = ConstantBackoff(3)
    retry = Retry(retries=-1, backoff=backoff, supported_errors=(ConnectionError, ConnectionResetError))
    r=redis.cluster.RedisCluster(host=host, port=6379,redis_connect_func=iam_connect, retry=retry, ssl=True, ssl_ca_certs=ssl_ca_certs)
    
    print(r.get('key'))

### Lettuce

We recommend using [Lettuce](https://lettuce.io/), versions 6.2.4 and later.
    
    
    import com.google.cloud.iam.credentials.v1.[GenerateAccessTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.GenerateAccessTokenResponse.html);
    import com.google.cloud.iam.credentials.v1.[IamCredentialsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html);
    import io.lettuce.core.RedisCredentials;
    import io.lettuce.core.RedisCredentialsProvider;
    import io.lettuce.core.RedisURI;
    import io.lettuce.core.SocketOptions;
    import io.lettuce.core.SslOptions;
    import io.lettuce.core.cluster.ClusterClientOptions;
    import io.lettuce.core.cluster.ClusterTopologyRefreshOptions;
    import io.lettuce.core.cluster.RedisClusterClient;
    import io.lettuce.core.cluster.api.StatefulRedisClusterConnection;
    import io.lettuce.core.cluster.api.sync.RedisAdvancedClusterCommands;
    import io.lettuce.core.cluster.models.partitions.RedisClusterNode;
    import io.lettuce.core.resource.ClientResources;
    import io.lettuce.core.resource.DefaultClientResources;
    import io.lettuce.core.resource.Delay;
    import java.io.Closeable;
    import java.io.File;
    import java.time.Duration;
    import java.time.Instant;
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.List;
    import java.util.concurrent.Executors;
    import java.util.concurrent.ScheduledExecutorService;
    import java.util.concurrent.TimeUnit;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    import reactor.core.publisher.Mono;
    
    public class IAMAuth {
        /**
        * This thread-safe implementation (excluding the main app below) is intended for production use.
        * It provides a background refresh logic that shouldn't overload IAM service in case. the
        * application has many many connections (connection storms can result in IAM throttles
        * otherwise).   
        *   
        * Guidelines for implementing similar logic for other clients:  
        * 1. Refresh IAM tokens in the background using a single thread/routine per client process  
        * 2. Provide last error feedback inline for token retrieval to aid debugging  
        * 3. Provide initial setup validation by fast-failing if the token couldn't be retrieved  
        * 4. Inline getToken shouldn't execute direct IAM calls as it can overload the token retrieval
        * resulting in throttles  
        * 5. Typical scale is tens of thousands of Redis connections and the IAM token is required for
        * every connection being established.  
        */
        private static final class RedisClusterCredentialsProvider
        implements RedisCredentialsProvider, Runnable, Closeable {
            private static final Logger logger =
            Logger.getLogger(RedisClusterCredentialsProvider.class.getName());
    
            private final ScheduledExecutorService service = Executors.newSingleThreadScheduledExecutor();
    
            private final [IamCredentialsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html) iamClient;
            private final String accountName;
            private final Duration refreshDuration;
            private final Duration lifetime;
    
            private volatile RedisCredentials credentials;
            private volatile Instant lastRefreshInstant;
            private volatile Exception lastException;
    
            /**
            * AccountName:
            * "projects/-/serviceAccounts/example-service-account@example-project.iam.gserviceaccount.com";
            * RefreshDuration: Duration.ofSeconds(300) Lifetime: Duration.ofSeconds(3600);
            */
            public RedisClusterCredentialsProvider(
            String accountName, Duration refreshDuration, Duration lifetime) throws Exception {
                this.iamClient = [IamCredentialsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html).create();
                this.accountName = accountName;
                this.refreshDuration = refreshDuration;
                this.lifetime = lifetime;
    
                // execute on initialization to fast-fail if there are any setup issues
                refreshTokenNow();
                // refresh much more frequently than the expiry time to allow for multiple retries in case of
                // failures
                service.scheduleWithFixedDelay(this, 10, 10, TimeUnit.SECONDS);
            }
    
            @Override
            public Mono resolveCredentials() {
                if (hasTokenExpired()) {
                    throw new RuntimeException("Background IAM token refresh failed", lastException);
                }
                return Mono.just(this.credentials);
            }
    
            private boolean hasTokenExpired() {
                if (this.lastRefreshInstant == null || this.lifetime == null) {
                    return true;
                }
                return Instant.now().isAfter(this.lastRefreshInstant.plus(this.lifetime));
            }
    
            // To be invoked by customer app on shutdown
            @Override
            public void close() {
                service.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_shutdown__)();
                iamClient.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_close__)();
            }
    
            @Override
            public void run() {
                try {
                    // fetch token if it is time to refresh
                    if (this.lastRefreshInstant != null
                        && this.refreshDuration != null
                    && Instant.now().isBefore(this.lastRefreshInstant.plus(this.refreshDuration))) {
                        // nothing to do
                        return;
                    }
                    refreshTokenNow();
                } catch (Exception e) {
                    // suppress all errors as we cannot allow the task to die
                    // log for visibility
                    logger.log(Level.[parse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.ServiceAccountName.html#com_google_cloud_iam_credentials_v1_ServiceAccountName_parse_java_lang_String_)("SEVERE"), "Background IAM token refresh failed", e);
                }
            }
    
            private void refreshTokenNow() {
                try {
                    logger.info("Refreshing IAM token");
                    com.google.protobuf.Duration lifetimeProto =
                    com.google.protobuf.Duration.newBuilder()
                    .setSeconds(lifetime.getSeconds())
                    .setNanos(lifetime.getNano())
                    .build();
                    [GenerateAccessTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.GenerateAccessTokenResponse.html) response =
                    this.iamClient.generateAccessToken(
                    this.accountName,
                    new ArrayList<>(),
                    Collections.singletonList("https://www.googleapis.com/auth/cloud-platform"),
                    lifetimeProto);
    
                    // got a successful token refresh
                    this.credentials =
                    new RedisCredentials() {
    
                        @Override
                        public boolean hasUsername() {
                            return false;
                        }
    
                        @Override
                        public boolean hasPassword() {
                            return true;
                        }
    
                        @Override
                        public String getUsername() {
                            return "default";
                        }
    
                        @Override
                        public char[] getPassword() {
                            return response.[getAccessToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.GenerateAccessTokenResponse.html#com_google_cloud_iam_credentials_v1_GenerateAccessTokenResponse_getAccessToken__)().toCharArray();
                        }
                    };
                    this.lastRefreshInstant = Instant.now();
                    // clear the last saved exception
                    this.lastException = null;
                    logger.info(
                    "IAM token refreshed with lastRefreshInstant ["
                    + lastRefreshInstant
                    + "], refreshDuration ["
                    + this.refreshDuration
                    + "], accountName ["
                    + this.accountName
                    + "] and lifetime ["
                    + this.lifetime
                    + "]");
                } catch (Exception e) {
                    // Save last exception for inline feedback
                    this.lastException = e;
                    // Bubble up for direct feedback
                    throw e;
                }
            }
        }
    
        /** Sample code to demonstrate how to use IAMAuth; not intended for production use */
        public static void main(String[] args) throws Exception {
            // These are the parameters the user needs to replace
            String discoveryEndpointIp = "CLUSTER_DISCOVERY_ENDPOINT_IP_ADDRESS";
            int discoveryEndpointPort = CLUSTER_DISCOVERY_ENDPOINT_PORT_NUMBER;
            String accountName = "ACCOUNT_NAME";
            String caFileName = "CA_FILE_NAME";
            int refreshDurationSec = REFRESH_DURATION_SEC;
            int lifetimeSec = LIFETIME_SEC;
    
            RedisCredentialsProvider credentialsProvider =
            new RedisClusterCredentialsProvider(
            accountName, Duration.ofSeconds(refreshDurationSec), Duration.ofSeconds(lifetimeSec));
    
            RedisURI redisUri =
            RedisURI.Builder.redis(discoveryEndpointIp, discoveryEndpointPort)
            .withSsl(true)
            .withAuthentication(credentialsProvider)
            .build();
            ClientResources resources =
            DefaultClientResources.builder()
            .reconnectDelay(
            Delay.fullJitter(
            Duration.ofMillis(100), Duration.ofSeconds(5), 100, TimeUnit.MILLISECONDS))
            .build();
            ClusterTopologyRefreshOptions topologyRefreshOptions =
            ClusterTopologyRefreshOptions.builder()
            .enablePeriodicRefresh(1, TimeUnit.MINUTES)
            .enableAllAdaptiveRefreshTriggers()
            .dynamicRefreshSources(false)
            .closeStaleConnections(true)
            .build();
    
            SslOptions sslOptions =
            SslOptions.builder().jdkSslProvider().trustManager(new File(caFileName)).build();
    
            SocketOptions socketOptions =
            SocketOptions.builder().connectTimeout(Duration.ofSeconds(5)).keepAlive(true).build();
    
            // Create Redis Cluster Client
            RedisClusterClient clusterClient = RedisClusterClient.create(resources, redisUri);
            clusterClient.setOptions(
            ClusterClientOptions.builder()
            .topologyRefreshOptions(topologyRefreshOptions)
            .socketOptions(socketOptions)
            .sslOptions(sslOptions)
            .autoReconnect(true)
            .nodeFilter(
            it ->
            !(it.is(RedisClusterNode.NodeFlag.FAIL)
            || it.is(RedisClusterNode.NodeFlag.EVENTUAL_FAIL)
            || it.is(RedisClusterNode.NodeFlag.NOADDR)))
            .validateClusterNodeMembership(false)
            .build());
    
            // Establish connection to Redis Cluster
            StatefulRedisClusterConnection<String, String> connection = clusterClient.connect();
    
            // Retrieve synchronous Redis Cluster commands
            RedisAdvancedClusterCommands<String, String> syncCommands = connection.sync();
    
            // Perform Redis operations
            syncCommands.set("key1", "value1");
            String value = syncCommands.get("key1");
            System.out.println("Retrieved value: " + value);
    
            int count = 0;
            for (int i = 0; i < 1000; i++) {
                String k = "lettucekey" + String.valueOf(i);
                String v = "lettucevalue" + String.valueOf(i);
                syncCommands.set(k, v);
                String got = syncCommands.get(k);
                if (got.equals(v)) {
                    count++;
                } else {
                    System.out.println("unexpected value");
                }
            }
            System.out.println("Successfully got " + String.valueOf(count) + " keys");
    
            // Close the connection and shutdown the client
            connection.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_close__)();
            clusterClient.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_shutdown__)();
            ((Closeable) credentialsProvider).[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_close__)();
        }
    }

### Jedis

We recommend using [Jedis](https://github.com/redis/jedis), versions 4.4.0 and later.
    
    
    import com.google.cloud.iam.credentials.v1.[GenerateAccessTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.GenerateAccessTokenResponse.html);
    import com.google.cloud.iam.credentials.v1.[IamCredentialsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html);
    import java.io.Closeable;
    import java.io.FileInputStream;
    import java.io.InputStream;
    import java.security.KeyStore;
    import java.security.cert.CertificateFactory;
    import java.security.cert.X509Certificate;
    import java.time.Duration;
    import java.time.Instant;
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.List;
    import java.util.concurrent.Executors;
    import java.util.concurrent.ScheduledExecutorService;
    import java.util.concurrent.TimeUnit;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    import javax.net.ssl.SSLContext;
    import javax.net.ssl.TrustManagerFactory;
    import org.apache.commons.pool2.impl.GenericObjectPoolConfig;
    import redis.clients.jedis.Connection;
    import redis.clients.jedis.DefaultJedisClientConfig;
    import redis.clients.jedis.DefaultRedisCredentials;
    import redis.clients.jedis.HostAndPort;
    import redis.clients.jedis.JedisCluster;
    import redis.clients.jedis.RedisCredentials;
    import redis.clients.jedis.RedisCredentialsProvider;
    
    /** Customers are free to update/replace code as they see fit. */
    public class IAMAuth {
    
        /**
        * This thread-safe implementation (excluding the main app below) is intended for production use.
        * It provides a background refresh logic that shouldn't overload IAM service in case. the
        * application has many many connections (connection storms can result in IAM throttles
        * otherwise).   
        *   
        * Guidelines for implementing similar logic for other clients:  
        * 1. Refresh IAM tokens in the background using a single thread/routine per client process  
        * 2. Provide last error feedback inline for token retrieval to aid debugging  
        * 3. Provide initial setup validation by fast-failing if the token couldn't be retrieved  
        * 4. Inline getToken shouldn't execute direct IAM calls as it can overload the token retrieval
        * resulting in throttles  
        * 5. Typical scale is tens of thousands of Redis connections and the IAM token is required for
        * every connection being established.  
        */
        private static final class RedisClusterCredentialsProvider
        implements RedisCredentialsProvider, Runnable, Closeable {
            private static final Logger logger =
            Logger.getLogger(RedisClusterCredentialsProvider.class.getName());
    
            private final [IamCredentialsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html) iamClient;
            private final ScheduledExecutorService service;
            private final String accountName;
            private final Duration refreshDuration;
            private final Duration lifetime;
    
            private volatile RedisCredentials credentials;
            private volatile Instant lastRefreshInstant;
            private volatile Exception lastException;
    
            // AccountName:
            // "projects/-/serviceAccounts/example-service-account@example-project.iam.gserviceaccount.com";
            // RefreshDuration: Duration.ofSeconds(300);
            // Lifetime: Duration.ofSeconds(3600);
            public RedisClusterCredentialsProvider(
            String accountName, Duration refreshDuration, Duration lifetime) throws Exception {
                this.iamClient = [IamCredentialsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html).create();
                this.service = Executors.newSingleThreadScheduledExecutor();
    
                this.accountName = accountName;
                this.refreshDuration = refreshDuration;
                this.lifetime = lifetime;
    
                // execute on initialization to fast-fail if there are any setup issues
                refreshTokenNow();
                // refresh much more frequently than the expiry time to allow for multiple retries in case of
                // failures
                service.scheduleWithFixedDelay(this, 10, 10, TimeUnit.SECONDS);
            }
    
            public RedisCredentials get() {
                if (hasTokenExpired()) {
                    throw new RuntimeException("Background IAM token refresh failed", lastException);
                }
                return this.credentials;
            }
    
            private boolean hasTokenExpired() {
                if (this.lastRefreshInstant == null || this.lifetime == null) {
                    return true;
                }
                return Instant.now().isAfter(this.lastRefreshInstant.plus(this.lifetime));
            }
    
            // To be invoked by customer app on shutdown
            @Override
            public void close() {
                service.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_shutdown__)();
                iamClient.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_close__)();
            }
    
            @Override
            public void run() {
                try {
                    // fetch token if it is time to refresh
                    if (this.lastRefreshInstant != null
                        && this.refreshDuration != null
                    && Instant.now().isBefore(this.lastRefreshInstant.plus(this.refreshDuration))) {
                        // nothing to do
                        return;
                    }
                    refreshTokenNow();
                } catch (Exception e) {
                    // suppress all errors as we cannot allow the task to die
                    // log for visibility
                    logger.log(Level.[parse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.ServiceAccountName.html#com_google_cloud_iam_credentials_v1_ServiceAccountName_parse_java_lang_String_)("SEVERE"), "Background IAM token refresh failed", e);
                }
            }
    
            private void refreshTokenNow() {
                try {
                    logger.info("Refreshing IAM token");
                    List delegates = new ArrayList<>();
                    com.google.protobuf.Duration lifetimeProto =
                    com.google.protobuf.Duration.newBuilder()
                    .setSeconds(lifetime.getSeconds())
                    .setNanos(lifetime.getNano())
                    .build();
                    [GenerateAccessTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.GenerateAccessTokenResponse.html) response =
                    iamClient.[generateAccessToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_generateAccessToken__org_jspecify_annotations_Nullable_com_google_cloud_iam_credentials_v1_ServiceAccountName_java_util_List_java_lang_String__java_util_List_java_lang_String__com_google_protobuf_Duration_)(
                    this.accountName,
                    delegates,
                    Collections.singletonList("https://www.googleapis.com/auth/cloud-platform"),
                    lifetimeProto);
    
                    // got a successful token refresh
                    this.credentials = new DefaultRedisCredentials("default", response.[getAccessToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.GenerateAccessTokenResponse.html#com_google_cloud_iam_credentials_v1_GenerateAccessTokenResponse_getAccessToken__)());
                    this.lastRefreshInstant = Instant.now();
                    // clear the last saved exception
                    this.lastException = null;
                    logger.info(
                    "IAM token refreshed with lastRefreshInstant ["
                    + lastRefreshInstant
                    + "], refreshDuration ["
                    + this.refreshDuration
                    + "], accountName ["
                    + this.accountName
                    + "] and lifetime ["
                    + this.lifetime
                    + "]");
                } catch (Exception e) {
                    // Save last exception for inline feedback
                    this.lastException = e;
                    // Bubble up for direct feedback
                    throw e;
                }
            }
        }
    
        /** Sample code to demonstrate how to use IAMAuth; not intended for production use */
        public static void main(String[] args) throws Exception {
            String discoveryEndpointIp = "CLUSTER_DISCOVERY_ENDPOINT_IP_ADDRESS";
            int discoveryEndpointPort = CLUSTER_DISCOVERY_ENDPOINT_PORT_NUMBER;
    
            GenericObjectPoolConfig config = new GenericObjectPoolConfig();
            config.setTestWhileIdle(true);
            int timeout = 5000;
            int maxAttempts = 5;
            HostAndPort discovery = new HostAndPort(discoveryEndpointIp, discoveryEndpointPort);
    
            RedisCredentialsProvider credentialsProvider =
            new RedisClusterCredentialsProvider(
            "projects/-/serviceAccounts/example-service-account@example-project.iam.gserviceaccount.com",
            Duration.ofSeconds(300),
            Duration.ofSeconds(3600));
    
            // Create JedisCluster cluster
            InputStream is = new FileInputStream("server-ca.pem");
            // You could get a resource as a stream instead.
    
            CertificateFactory cf = CertificateFactory.getInstance("X.509");
            X509Certificate caCert = (X509Certificate) cf.generateCertificate(is);
    
            TrustManagerFactory tmf =
            TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
            KeyStore ks = KeyStore.getInstance(KeyStore.getDefaultType());
            ks.load(null); // You don't need the KeyStore cluster to come from a file.
            ks.setCertificateEntry("caCert", caCert);
    
            tmf.init(ks);
    
            SSLContext sslContext = SSLContext.getInstance("TLS");
            sslContext.init(null, tmf.getTrustManagers(), null);
    
            JedisCluster jedisCluster =
            new JedisCluster(
            discovery,
            DefaultJedisClientConfig.builder()
            .connectionTimeoutMillis(timeout)
            .socketTimeoutMillis(timeout)
            .credentialsProvider(credentialsProvider)
            .ssl(true)
            .sslSocketFactory(sslContext.getSocketFactory())
            .build(),
            maxAttempts,
            config);
    
            // Perform operations on the cluster
            jedisCluster.set("myKey", "Hello, Redis Cluster!");
            String value = jedisCluster.get("myKey");
            System.out.println("Value for myKey: " + value);
    
            int count = 0;
            for (int i = 0; i < 1000; i++) {
                String k = "jediskey" + String.valueOf(i);
                String v = "jedisvalue" + String.valueOf(i);
                jedisCluster.set(k, v);
                String got = jedisCluster.get(k);
                if (got.equals(v)) {
                    count++;
                } else {
                    System.out.println("unexpected value");
                }
            }
            System.out.println("Successfully got " + String.valueOf(count) + " keys");
    
            // Disconnect from the cluster
            jedisCluster.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_close__)();
            // Cleanup the resources used by the provider
            ((Closeable) credentialsProvider).[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-iamcredentials/latest/com.google.cloud.iam.credentials.v1.IamCredentialsClient.html#com_google_cloud_iam_credentials_v1_IamCredentialsClient_close__)();
        }
    }

### Go

We recommend using [Go](https://go.dev/), versions 1.24.5 and later.
    
    
    package main
    
    import (
        "context"
        "crypto/tls"
        "crypto/x509"
        "flag"
        "fmt"
        "io/ioutil"
        "log"
        "sync"
        "time"
    
        credentials "google.golang.org/genproto/googleapis/iam/credentials/v1"
    
        "github.com/golang/protobuf/ptypes"
        "github.com/redis/go-redis/v9"
        "google.golang.org/api/option"
        gtransport "google.golang.org/api/transport/grpc"
    )
    
    var (
        svcAccount               = flag.String("a", "projects/-/serviceAccounts/example-service-account@example-project.iam.gserviceaccount.com", "service account email")
        lifetime                 = flag.Duration("d", time.Hour, "lifetime of token")
        refreshDuration          = flag.Duration("r", 5*time.Minute, "token refresh duration")
        checkTokenExpiryInterval = flag.Duration("e", 10*time.Second, "check token expiry interval")
        lastRefreshInstant       = time.Time{}
        errLastSeen              = error(nil)
        token                    = ""
        mu                       = sync.RWMutex{}
    )
    
    func retrieveToken() (string, error) {
        ctx := context.Background()
        conn, err := gtransport.Dial(ctx,
            option.WithEndpoint("iamcredentials.googleapis.com:443"),
            option.WithScopes("https://www.googleapis.com/auth/cloud-platform"))
    
        if err != nil {
            log.Printf("Failed to dial API, error: %v", err)
            return token, err
        }
        client := credentials.NewIAMCredentialsClient(conn)
        req := credentials.GenerateAccessTokenRequest{
            Name:     *svcAccount,
            Scope:    []string{"https://www.googleapis.com/auth/cloud-platform"},
            Lifetime: ptypes.DurationProto(*lifetime),
        }
        rsp, err := client.GenerateAccessToken(ctx, &req)
        if err != nil {
            log.Printf"Failed to call GenerateAccessToken with request: %v, error: %v", req, err)
            return token, err
        }
        return rsp.AccessToken, nil
    }
    
    func refreshTokenLoop() {
        if *refreshDuration > *lifetime {
            log.Fatal("Refresh should not happen after token is already expired.")
        }
        for {
            mu.RLock()
            lastRefreshTime := lastRefreshInstant
            mu.RUnlock()
            if time.Now().After(lastRefreshTime.Add(*refreshDuration)) {
                var err error
                retrievedToken, err := retrieveToken()
                mu.Lock()
                token = retrievedToken
                if err != nil {
                    errLastSeen = err
                } else {
                    lastRefreshInstant = time.Now()
                }
                mu.Unlock()
            }
            time.Sleep(*checkTokenExpiryInterval)
        }
    }
    
    func retrieveTokenFunc() (string, string) {
        mu.RLock()
        defer mu.RUnlock()
        if time.Now().After(lastRefreshInstant.Add(*refreshDuration)) {
            log.Printf("Token is expired. last refresh instant: %v, refresh duration: %v, error that was last seen: %v", lastRefreshInstant, *refreshDuration, errLastSeen)
            return "", ""
        }
        username := "default"
        password := token
        return username, password
    }
    
    func main() {
        // Load CA cert
        caFilePath := CA_FILE_PATH
        clusterDicEpAddr := CLUSTER_DISCOVERY_ENDPOINT_IP_ADDRESS_AND_PORT
        caCert, err := ioutil.ReadFile(caFilePath)
        if err != nil {
            log.Fatal(err)
        }
        caCertPool := x509.NewCertPool()
        caCertPool.AppendCertsFromPEM(caCert)
        token, err = retrieveToken()
        if err != nil {
            log.Fatal("Cannot retrieve IAM token to authenticate to the cluster, error: %v", err)
        }
        lastRefreshInstant = time.Now()
        go refreshTokenLoop()
    
        // Setup Redis Connection pool
        client := redis.NewClusterClient(&redis.ClusterOptions{
            Addrs: []string{clusterDicEpAddr},
            // PoolSize applies per cluster node and not for the whole cluster.
            PoolSize:            10,
            ConnMaxIdleTime:     60 * time.Second,
            MinIdleConns:        1,
            CredentialsProvider: retrieveTokenFunc,
            TLSConfig: &tls.Config{
                RootCAs: caCertPool,
            },
        })
    
        ctx := context.Background()
        err = client.Set(ctx, "key", "value", 0).Err()
        if err != nil {
            log.Fatal(err)
        }
        val, err := client.Get(ctx, "key").Result()
        if err != nil {
            log.Fatal(err)
        }
        fmt.Printf("Got the value for key: key, which is %s \n", val)
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
