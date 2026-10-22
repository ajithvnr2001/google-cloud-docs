---
url: https://docs.cloud.google.com/memorystore/docs/redis/use-client-side-metrics/
title: Use client-side metrics to troubleshoot high latency \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:04.282525+00:00
---

# Use client-side metrics to troubleshoot high latency  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/use-client-side-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Use client-side metrics to troubleshoot high latency Stay organized with collections  Save and categorize content based on your preferences. 

While Memorystore for Redis provides real-time, server-side metrics to monitor throughput, CPU utilization, and memory usage, this data alone might not explain why your client application experiences high latency within complex distributed systems.

Client-side metrics solve this by providing transparency into the full request-response cycle. They measure a command from the time the application initiates it until the application processes the response. By capturing these data points, you can accurately determine whether the latency originates from the application logic, the network path, or the Redis server.

## Before you begin

Ensure that your client application uses a service account and the following Identity and Access Management (IAM) roles are assigned to it:

  * `roles/cloudtrace.agent` (Cloud Trace Agent)
  * `roles/monitoring.metricWriter` (Monitoring Metric Writer)



For more information about granting roles, see the [Grant an IAM role by using the Google Cloud console](https://docs.cloud.google.com/iam/docs/grant-role-console) quickstart.

## Enable the Cloud Monitoring API

To export client-side metrics to [Monitoring](https://docs.cloud.google.com/monitoring/docs), your application requires the Monitoring API to be enabled. Exporting and visualizing these metrics in Monitoring lets you pinpoint the root cause of bottlenecks to determine whether the latency originates.

To enable the Monitoring API, do the following:

  1. In the Google Cloud console, go to the **APIs & Services** page.

[Go to APIs and services](https://console.cloud.google.com/apis/dashboard)

  2. Select the project where you created the Memorystore for Redis instance.

  3. Click **Enable APIs and services**.

  4. Search for `monitoring`.

  5. In the search results, click **Cloud Monitoring API**.

  6. If **API enabled** appears, then the API is already enabled. Otherwise, click **Enable**.




## Enable the Cloud Trace API

To view distributed traces in [Trace](https://docs.cloud.google.com/trace/docs), you must enable the Trace API. You can then use Trace Explorer to view these traces, diagnose bottlenecks, and isolate the source of latency in your application.

To enable the Trace API, do the following:

  1. In the Google Cloud console, go to the **APIs & Services** page.

[Go to APIs and services](https://console.cloud.google.com/apis/dashboard)

  2. Select the project where you created the Memorystore for Redis instance.

  3. Click **Enable APIs and services**.

  4. Search for `trace`.

  5. In the search results, click **Cloud Trace API**.

  6. If **API enabled** appears, then the API is already enabled. Otherwise, click **Enable**.




## Enable client-side metrics

To enable client-side metrics, add the [OpenTelemetry](https://opentelemetry.io/) SDK, the Cloud Monitoring exporter, and the Cloud Trace exporter to your application's code. The OpenTelemetry instrumentation, which runs directly inside of your application's Redis client library, captures the metrics. This lets your application record latency data points and export them to Monitoring and Trace for visualization.

To enable client-side metrics, you can use [Go](https://github.com/gomodule/redigo), [Java](https://github.com/redis/jedis), [Node.js](https://github.com/redis/node-redis), or [Python](https://github.com/redis/redis-py). Information for enabling the metrics for each language appears in the tabs that follow.

### Go

  1. To install the required OpenTelemetry and Google Cloud exporter dependencies, run the following commands in your terminal:
         
         go get github.com/gomodule/redigo/redis@latest
           go get go.opentelemetry.io/otel
           go get go.opentelemetry.io/otel/sdk/trace
           go get go.opentelemetry.io/otel/sdk/metric
           go get github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace
           go get github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric

  2. To enable the client-side metrics, create a `main.go` file and add the following code to it:
         
         package main
         
         import (
         	"context"
         	"fmt"
         	"log"
         	"os"
         	"time"
         
         	"github.com/gomodule/redigo/redis"
         	"go.opentelemetry.io/otel"
         	"go.opentelemetry.io/otel/attribute"
         	"go.opentelemetry.io/otel/codes"
         	"go.opentelemetry.io/otel/metric"
         	"go.opentelemetry.io/otel/trace"
         
         	gcpmetric "github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/metric"
         	gcptrace "github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/trace"
         	sdkmetric "go.opentelemetry.io/otel/sdk/metric"
         	sdktrace "go.opentelemetry.io/otel/sdk/trace"
         )
         
         // MetricClient encapsulates the tracer and metric histograms to avoid package-level globals.
         type MetricClient struct {
         	tracer           trace.Tracer
         	rttHist          metric.Float64Histogram
         	clientBlockHist  metric.Float64Histogram
         	appBlockHist     metric.Float64Histogram
         	retryCounter     metric.Int64Counter
         	connErrorCounter metric.Int64Counter
         }
         
         // sleep hook enables lightning-fast unit tests by stubbing out real time.Sleep
         var sleep = time.Sleep
         
         // sinceMs calculates elapsed time in fractional milliseconds to avoid truncating sub-millisecond durations.
         func sinceMs(start time.Time) float64 {
         	return float64(time.Since(start).Microseconds()) / 1000.0
         }
         
         func initTelemetry(ctx context.Context) (*MetricClient, func(), error) {
         	traceExporter, err := gcptrace.New()
         	if err != nil {
         		return nil, nil, fmt.Errorf("gcptrace.New: %w", err)
         	}
         	tp := sdktrace.NewTracerProvider(sdktrace.WithBatcher(traceExporter))
         	otel.SetTracerProvider(tp)
         	tracer := tp.Tracer("redigo.client")
         
         	metricExporter, err := gcpmetric.New()
         	if err != nil {
         		return nil, nil, fmt.Errorf("gcpmetric.New: %w", err)
         	}
         	mp := sdkmetric.NewMeterProvider(sdkmetric.WithReader(sdkmetric.NewPeriodicReader(metricExporter, sdkmetric.WithInterval(10*time.Second))))
         	otel.SetMeterProvider(mp)
         	meter := mp.Meter("redigo.metrics")
         
         	rttHist, err := meter.Float64Histogram("redis_client_rtt", metric.WithUnit("ms"))
         	if err != nil {
         		return nil, nil, fmt.Errorf("redis_client_rtt histogram: %w", err)
         	}
         	clientBlockHist, err := meter.Float64Histogram("redis_client_blocking_latency", metric.WithUnit("ms"))
         	if err != nil {
         		return nil, nil, fmt.Errorf("redis_client_blocking_latency histogram: %w", err)
         	}
         	appBlockHist, err := meter.Float64Histogram("redis_application_blocking_latency", metric.WithUnit("ms"))
         	if err != nil {
         		return nil, nil, fmt.Errorf("redis_application_blocking_latency histogram: %w", err)
         	}
         	retryCounter, err := meter.Int64Counter("redis_retry_count")
         	if err != nil {
         		return nil, nil, fmt.Errorf("redis_retry_count counter: %w", err)
         	}
         	connErrorCounter, err := meter.Int64Counter("redis_connectivity_error_count")
         	if err != nil {
         		return nil, nil, fmt.Errorf("redis_connectivity_error_count counter: %w", err)
         	}
         
         	client := &MetricClient{
         		tracer:           tracer,
         		rttHist:          rttHist,
         		clientBlockHist:  clientBlockHist,
         		appBlockHist:     appBlockHist,
         		retryCounter:     retryCounter,
         		connErrorCounter: connErrorCounter,
         	}
         
         	initAttrs := metric.WithAttributes(attribute.String("operation", "startup"))
         	client.retryCounter.Add(ctx, 0, initAttrs)
         	client.connErrorCounter.Add(ctx, 0, initAttrs)
         
         	shutdown := func() {
         		tp.Shutdown(ctx)
         		mp.Shutdown(ctx)
         	}
         
         	return client, shutdown, nil
         }
         
         func (c *MetricClient) smartRedisCall(ctx context.Context, pool *redis.Pool, operationName string, commandName string, args ...interface{}) (interface{}, error) {
         	// Create a dedicated child span for the Redis command
         	ctx, span := c.tracer.Start(ctx, operationName)
         	span.SetAttributes(attribute.String("redis.command", commandName))
         	defer span.End()
         
         	maxRetries := 3
         	attempt := 0
         	metricOpts := metric.WithAttributes(attribute.String("operation", operationName))
         	var lastErr error
         
         	for attempt < maxRetries {
         		poolStart := time.Now()
         		// Use GetContext to respect context deadlines and cancellation
         		conn, err := pool.GetContext(ctx)
         		c.clientBlockHist.Record(ctx, sinceMs(poolStart), metricOpts)
         
         		if err != nil {
         			c.connErrorCounter.Add(ctx, 1, metricOpts)
         			c.retryCounter.Add(ctx, 1, metricOpts)
         			span.RecordError(err)
         			span.SetStatus(codes.Error, err.Error())
         			lastErr = err
         			attempt++
         			if attempt >= maxRetries {
         				break
         			}
         			sleep(time.Duration(100<<attempt) * time.Millisecond)
         			continue
         		}
         
         		// Check if the connection is dead
         		if err := conn.Err(); err != nil {
         			conn.Close()
         			c.connErrorCounter.Add(ctx, 1, metricOpts)
         			c.retryCounter.Add(ctx, 1, metricOpts)
         			span.RecordError(err)
         			span.SetStatus(codes.Error, err.Error())
         			lastErr = err
         			attempt++
         			if attempt >= maxRetries {
         				break
         			}
         			sleep(time.Duration(100<<attempt) * time.Millisecond)
         			continue
         		}
         
         		reqStart := time.Now()
         		// Redigo has no native DoContext; pass timeouts using redis.DoWithTimeout when context has a deadline
         		var reply interface{}
         		if deadline, ok := ctx.Deadline(); ok {
         			reply, err = redis.DoWithTimeout(conn, time.Until(deadline), commandName, args...)
         		} else {
         			reply, err = conn.Do(commandName, args...)
         		}
         		c.rttHist.Record(ctx, sinceMs(reqStart), metricOpts)
         		conn.Close()
         
         		if err != nil {
         			c.retryCounter.Add(ctx, 1, metricOpts)
         			span.RecordError(err)
         			span.SetStatus(codes.Error, err.Error())
         			lastErr = err
         			attempt++
         			if attempt >= maxRetries {
         				break
         			}
         			sleep(time.Duration(100<<attempt) * time.Millisecond)
         			continue
         		}
         
         		appStart := time.Now()
         		// Replace fmt.Sprintf to remove unnecessary string formatting overhead
         		sleep(2 * time.Millisecond)
         		c.appBlockHist.Record(ctx, sinceMs(appStart), metricOpts)
         
         		// Reset span status to Ok if the retry or execution eventually succeeds
         		span.SetStatus(codes.Ok, "")
         
         		return reply, nil
         	}
         	return nil, fmt.Errorf("max retries reached for %s: %w", operationName, lastErr)
         }
         
         func main() {
         	ctx := context.Background()
         	client, shutdown, err := initTelemetry(ctx)
         	if err != nil {
         		log.Printf("Failed to initialize telemetry: %v", err)
         		os.Exit(1)
         	}
         	defer shutdown()
         
         	redisHost := os.Getenv("REDISHOST")
         	redisPort := os.Getenv("REDISPORT")
         	if redisPort == "" {
         		redisPort = "6379"
         	}
         
         	pool := &redis.Pool{
         		MaxIdle:     10,
         		MaxActive:   20,
         		IdleTimeout: 240 * time.Second,
         		Wait:        true,
         		Dial: func() (redis.Conn, error) {
         			return redis.Dial("tcp", fmt.Sprintf("%s:%s", redisHost, redisPort))
         		},
         	}
         	defer pool.Close()
         
         	ctx, span := client.tracer.Start(ctx, "fetch_data_span")
         	defer span.End()
         
         	// Simple write and read operations
         	_, err = client.smartRedisCall(ctx, pool, "set_user", "SET", "user:123", "active")
         	if err != nil {
         		log.Printf("Error setting data: %v", err)
         	}
         	val, err := client.smartRedisCall(ctx, pool, "get_user", "GET", "user:123")
         	if err != nil {
         		log.Printf("Error fetching data: %v", err)
         	} else {
         		log.Printf("Retrieved value: %s", val)
         	}
         }
         

  3. Run your application for at least a minute to give the exporter enough time to batch and send the published metrics to Monitoring.




### Java

  1. To install the required OpenTelemetry and Google Cloud exporter dependencies, add the following code to your application's `pom.xml` file:
         
         <dependencies>
             <dependency>
                 <groupId>redis.clients</groupId>
                 <artifactId>jedis</artifactId>
                 <version>5.1.0</version>
             </dependency>
             <dependency>
                 <groupId>io.opentelemetry</groupId>
                 <artifactId>opentelemetry-api</artifactId>
                 <version>1.36.0</version>
             </dependency>
             <dependency>
                 <groupId>io.opentelemetry</groupId>
                 <artifactId>opentelemetry-sdk</artifactId>
                 <version>1.36.0</version>
             </dependency>
             <dependency>
                 <groupId>com.google.cloud.opentelemetry</groupId>
                 <artifactId>exporter-trace</artifactId>
                 <version>0.28.0</version>
             </dependency>
             <dependency>
                 <groupId>com.google.cloud.opentelemetry</groupId>
                 <artifactId>exporter-metrics</artifactId>
                 <version>0.28.0</version>
             </dependency>
         
             <!-- Testing Dependencies -->
             <dependency>
                 <groupId>junit</groupId>
                 <artifactId>junit</artifactId>
                 <version>4.13.2</version>
                 <scope>test</scope>
             </dependency>
             <dependency>
                 <groupId>org.mockito</groupId>
                 <artifactId>mockito-core</artifactId>
                 <version>4.11.0</version>
                 <scope>test</scope>
             </dependency>
             <dependency>
                 <groupId>org.slf4j</groupId>
                 <artifactId>slf4j-simple</artifactId>
                 <version>1.7.36</version>
                 <scope>test</scope>
             </dependency>
         </dependencies>

  2. To enable the client-side metrics, create a `RedisTelemetryApp.java` file and add the following code to it:
         
         import com.google.cloud.opentelemetry.metric.GoogleCloudMetricExporter;
         import com.google.cloud.opentelemetry.trace.TraceExporter;
         import io.opentelemetry.api.OpenTelemetry;
         import io.opentelemetry.api.common.AttributeKey;
         import io.opentelemetry.api.common.Attributes;
         import io.opentelemetry.api.metrics.DoubleHistogram;
         import io.opentelemetry.api.metrics.LongCounter;
         import io.opentelemetry.api.metrics.Meter;
         import io.opentelemetry.api.trace.Span;
         import io.opentelemetry.api.trace.Tracer;
         import io.opentelemetry.sdk.OpenTelemetrySdk;
         import io.opentelemetry.sdk.metrics.export.MetricExporter;
         import io.opentelemetry.sdk.metrics.SdkMeterProvider;
         import io.opentelemetry.sdk.metrics.export.PeriodicMetricReader;
         import io.opentelemetry.sdk.trace.SdkTracerProvider;
         import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;
         import io.opentelemetry.sdk.trace.export.SpanExporter;
         import redis.clients.jedis.Jedis;
         import redis.clients.jedis.JedisPool;
         import redis.clients.jedis.JedisPoolConfig;
         import redis.clients.jedis.exceptions.JedisConnectionException;
         
         import java.time.Duration;
         import java.util.function.Function;
         
         /**
          * Sample application demonstrating client-side metrics and tracing for
          * Google Cloud Memorystore for Redis.
          */
         public final class RedisTelemetryApp {
             /** Attribute key for Redis operation names. */
             private static final AttributeKey<String> ATTR_OPERATION =
                     AttributeKey.stringKey("operation");
         
             /** Maximum number of Redis reconnection attempts. */
             private static final int MAX_RETRIES = 3;
         
             /** Maximum total connections for the Jedis pool. */
             private static final int POOL_MAX_TOTAL = 20;
         
             /** Interval in seconds for exporting metrics to Google Cloud. */
             private static final long METRIC_INTERVAL_SECONDS = 10L;
         
             /** Base multiplier for exponential backoff sleep (in milliseconds). */
             private static final long RETRY_BACKOFF_BASE_MS = 100L;
         
             /** Conversion factor from Nanoseconds to Milliseconds. */
             private static final double NANO_TO_MS = 1_000_000.0;
         
             /** Default Redis port. */
             private static final int DEFAULT_REDIS_PORT = 6379;
         
             /** OpenTelemetry Tracer instance for recording trace spans. */
             private static Tracer tracer;
         
             /** OpenTelemetry Histogram for Redis round-trip time. */
             private static DoubleHistogram rttHist;
         
             /** OpenTelemetry Histogram for pool blocking latency. */
             private static DoubleHistogram clientBlockHist;
         
             /** OpenTelemetry Histogram for application logic blocking latency. */
             private static DoubleHistogram appBlockHist;
         
             /** OpenTelemetry Counter for Redis reconnection retry events. */
             private static LongCounter retryCounter;
         
             /** OpenTelemetry Counter for Redis connectivity errors. */
             private static LongCounter connErrorCounter;
         
             /** Shared Jedis connection pool. */
             private static JedisPool jedisPool;
         
             /**
              * Private constructor to prevent instantiation of this utility class.
              */
             private RedisTelemetryApp() {
             }
         
             /**
              * Main entry point for running the sample application.
              *
              * @param args Command line arguments (not used).
              */
             public static void main(final String[] args) {
                 setupTelemetry();
         
                 final String host = System.getenv()
                         .getOrDefault("REDISHOST", "localhost");
                 final int port = Integer.parseInt(System.getenv()
                         .getOrDefault("REDISPORT",
                                 String.valueOf(DEFAULT_REDIS_PORT)));
         
                 final JedisPoolConfig poolConfig = new JedisPoolConfig();
                 poolConfig.setMaxTotal(POOL_MAX_TOTAL);
                 poolConfig.setBlockWhenExhausted(true);
                 jedisPool = new JedisPool(poolConfig, host, port);
         
                 try {
                     run();
                 } finally {
                     if (jedisPool != null) {
                         jedisPool.close();
                     }
                 }
             }
         
             /**
              * Executes the core business logic of reading and writing to Redis.
              *
              * @return The string retrieved from the Redis 'get' operation.
              */
             static String run() {
                 final Span span = tracer.spanBuilder("process_user_span")
                         .startSpan();
                 try {
                     smartRedisCall("set_user", jedis ->
                             jedis.set("user:123", "active"));
         
                     final String result = smartRedisCall("get_user", jedis ->
                             jedis.get("user:123"));
                     System.out.println("Retrieved: " + result);
                     return result;
                 } catch (Exception e) {
                     span.recordException(e);
                     throw e;
                 } finally {
                     span.end();
                 }
             }
         
             /**
              * Injects mocked or no-op telemetry and pool instances for unit testing.
              *
              * @param pool                The mocked or test JedisPool instance.
              * @param testOpenTelemetry The OpenTelemetry instance to use for testing.
              */
             static void initForTest(
                     final JedisPool pool,
                     final OpenTelemetry testOpenTelemetry) {
                 jedisPool = pool;
                 tracer = testOpenTelemetry.getTracer("jedis.client");
                 final Meter meter = testOpenTelemetry.getMeter("jedis.metrics");
         
                 rttHist = meter.histogramBuilder("redis_client_rtt")
                         .setUnit("ms").build();
                 clientBlockHist = meter
                         .histogramBuilder("redis_client_blocking_latency")
                         .setUnit("ms").build();
                 appBlockHist = meter
                         .histogramBuilder("redis_application_blocking_latency")
                         .setUnit("ms").build();
                 retryCounter = meter.counterBuilder("redis_retry_count").build();
                 connErrorCounter = meter
                         .counterBuilder("redis_connectivity_error_count")
                         .build();
         
                 retryCounter.add(0, Attributes.of(ATTR_OPERATION, "startup"));
                 connErrorCounter.add(0, Attributes.of(ATTR_OPERATION, "startup"));
             }
         
             /**
              * Configures the production OpenTelemetry SDK to export Traces and Metrics
              * to Google Cloud Operations.
              */
             private static void setupTelemetry() {
                 final SpanExporter traceExporter =
                         TraceExporter.createWithDefaultConfiguration();
                 final SdkTracerProvider tracerProvider =
                         SdkTracerProvider.builder()
                                 .addSpanProcessor(
                                         BatchSpanProcessor.builder(traceExporter)
                                                 .build())
                                 .build();
         
                 final MetricExporter metricExporter =
                         GoogleCloudMetricExporter.createWithDefaultConfiguration();
                 final SdkMeterProvider meterProvider =
                         SdkMeterProvider.builder()
                                 .registerMetricReader(
                                         PeriodicMetricReader.builder(metricExporter)
                                                 .setInterval(Duration.ofSeconds(
                                                         METRIC_INTERVAL_SECONDS))
                                                 .build())
                                 .build();
         
                 final OpenTelemetry openTelemetry = OpenTelemetrySdk.builder()
                         .setTracerProvider(tracerProvider)
                         .setMeterProvider(meterProvider)
                         .buildAndRegisterGlobal();
         
                 tracer = openTelemetry.getTracer("jedis.client");
                 final Meter meter = openTelemetry.getMeter("jedis.metrics");
         
                 rttHist = meter.histogramBuilder("redis_client_rtt")
                         .setUnit("ms").build();
                 clientBlockHist = meter
                         .histogramBuilder("redis_client_blocking_latency")
                         .setUnit("ms").build();
                 appBlockHist = meter
                         .histogramBuilder("redis_application_blocking_latency")
                         .setUnit("ms").build();
                 retryCounter = meter.counterBuilder("redis_retry_count").build();
                 connErrorCounter = meter
                         .counterBuilder("redis_connectivity_error_count")
                         .build();
         
                 retryCounter.add(0, Attributes.of(ATTR_OPERATION, "startup"));
                 connErrorCounter.add(0, Attributes.of(ATTR_OPERATION, "startup"));
             }
         
             /**
              * Wraps a Redis operation with latency metrics, reconnection retry logic,
              * and trace spans.
              *
              * @param <T>           The return type of the Redis operation.
              * @param operationName The name of the operation for metric attributes.
              * @param operation     The Redis command lambda to execute safely.
              * @return The return value from the Redis command.
              */
             private static <T> T smartRedisCall(
                     final String operationName,
                     final Function<Jedis, T> operation) {
                 int attempt = 0;
                 final Attributes attrs = Attributes.of(ATTR_OPERATION,
                         operationName);
         
                 final Span span = tracer.spanBuilder(operationName).startSpan();
         
                 try {
                     while (attempt < MAX_RETRIES) {
                         final long poolStart = System.nanoTime();
                         try (Jedis jedis = jedisPool.getResource()) {
                             clientBlockHist.record((System.nanoTime() - poolStart)
                                     / NANO_TO_MS, attrs);
         
                             final long reqStart = System.nanoTime();
                             final T response = operation.apply(jedis);
                             rttHist.record((System.nanoTime() - reqStart)
                                     / NANO_TO_MS, attrs);
         
                             final long appStart = System.nanoTime();
                             @SuppressWarnings("unused")
                             final String dummy = String.valueOf(response);
                             appBlockHist.record((System.nanoTime() - appStart)
                                     / NANO_TO_MS, attrs);
         
                             return response;
                         } catch (JedisConnectionException e) {
                             attempt++;
                             connErrorCounter.add(1, attrs);
                             retryCounter.add(1, attrs);
                             span.recordException(e);
                             if (attempt >= MAX_RETRIES) {
                                 throw e;
                             }
                             try {
                                 Thread.sleep((long) (Math.pow(2, attempt)
                                         * RETRY_BACKOFF_BASE_MS));
                             } catch (InterruptedException ie) {
                                 Thread.currentThread().interrupt();
                             }
                         }
                     }
                     return null;
                 } finally {
                     span.end();
                 }
             }
         }

  3. Run your application for at least a minute to give the exporter enough time to batch and send the published metrics to Monitoring.




### Node.js

  1. To install the required OpenTelemetry and Google Cloud exporter dependencies, run the following commands in your terminal:
         
         npm install redis@^4.6.0 @opentelemetry/api@^1.9.0
           @opentelemetry/sdk-trace-node@^2.1.0
           @opentelemetry/sdk-trace-base@^2.1.0
           @opentelemetry/sdk-metrics@^2.1.0
           @opentelemetry/instrumentation@^0.205.0
           @opentelemetry/instrumentation-redis@^0.67.0
           @google-cloud/opentelemetry-cloud-trace-exporter@^3.0.0
           @google-cloud/opentelemetry-cloud-monitoring-exporter@^0.21.0
           @opentelemetry/resources@^2.1.0

  2. To enable the client-side metrics, create a `server.js` file and add the following code to it:
         
         'use strict';
         
         const {trace, metrics} = require('@opentelemetry/api');
         const {NodeTracerProvider} = require('@opentelemetry/sdk-trace-node');
         const {BatchSpanProcessor} = require('@opentelemetry/sdk-trace-base');
         const {
           TraceExporter,
         } = require('@google-cloud/opentelemetry-cloud-trace-exporter');
         const {
           MeterProvider,
           PeriodicExportingMetricReader,
         } = require('@opentelemetry/sdk-metrics');
         const {
           MetricExporter,
         } = require('@google-cloud/opentelemetry-cloud-monitoring-exporter');
         const {RedisInstrumentation} = require('@opentelemetry/instrumentation-redis');
         const {registerInstrumentations} = require('@opentelemetry/instrumentation');
         const {performance} = require('perf_hooks');
         
         // FIX: Pass spanProcessors in the constructor options for NodeTracerProvider in SDK 2.x
         const provider = new NodeTracerProvider({
           spanProcessors: [new BatchSpanProcessor(new TraceExporter())],
         });
         provider.register();
         
         registerInstrumentations({
           instrumentations: [new RedisInstrumentation()],
         });
         
         const redis = require('redis');
         
         const metricExporter = new MetricExporter();
         const metricReader = new PeriodicExportingMetricReader({
           exporter: metricExporter,
           exportIntervalMillis: 10000,
         });
         const meterProvider = new MeterProvider({readers: [metricReader]});
         metrics.setGlobalMeterProvider(meterProvider);
         
         const tracer = trace.getTracer('redis.client.node');
         const meter = metrics.getMeter('redis.metrics.node');
         
         const rttHist = meter.createHistogram('redis_client_rtt', {unit: 'ms'});
         const appBlockHist = meter.createHistogram(
           'redis_application_blocking_latency',
           {unit: 'ms'}
         );
         const retryCounter = meter.createCounter('redis_retry_count');
         const connErrorCounter = meter.createCounter('redis_connectivity_error_count');
         
         retryCounter.add(0, {operation: 'startup'});
         connErrorCounter.add(0, {operation: 'startup'});
         
         const REDISHOST = process.env.REDISHOST || 'localhost';
         const REDISPORT = process.env.REDISPORT || 6379;
         
         const client = redis.createClient({
           socket: {
             host: REDISHOST,
             port: REDISPORT,
             reconnectStrategy: retries => {
               connErrorCounter.add(1, {error: 'socket_reconnect'});
               if (retries > 5) return new Error('Max retries reached');
               return Math.min(retries * 100, 3000);
             },
           },
         });
         client.on('error', err => console.log('Redis Client Error', err));
         
         async function smartRedisCall(operationName, func, ...args) {
           let attempt = 0;
           while (attempt < 3) {
             try {
               const reqStart = performance.now();
               const response = await func(...args);
               rttHist.record(performance.now() - reqStart, {operation: operationName});
         
               const appParseStart = performance.now();
               // eslint-disable-next-line no-unused-vars
               const _ = String(response);
               appBlockHist.record(performance.now() - appParseStart, {
                 operation: operationName,
               });
         
               return response;
             } catch (e) {
               attempt++;
               retryCounter.add(1, {operation: operationName});
               if (attempt >= 3) throw e;
               await new Promise(resolve =>
                 setTimeout(resolve, Math.pow(2, attempt) * 100)
               );
             }
           }
         }
         
         async function main() {
           await client.connect();
         
           await tracer.startActiveSpan('process_user_span', async span => {
             try {
               // Simple write and read operations
               await smartRedisCall(
                 'set_user',
                 client.set.bind(client),
                 'user:123',
                 'active'
               );
         
               const result = await smartRedisCall(
                 'get_user',
                 client.get.bind(client),
                 'user:123'
               );
               console.log('Retrieved:', result);
             } catch (e) {
               span.recordException(e);
             } finally {
               span.end();
             }
           });
         
           await client.quit();
           await provider.forceFlush();
           await meterProvider.forceFlush();
         }
         
         // Only run the script automatically if it is executed directly (e.g. `node server.js`)
         if (require.main === module) {
           main().catch(console.error);
         }
         
         // Export for testability
         module.exports = {
           main,
           smartRedisCall,
         };
         

  3. Run your application for at least a minute to give the exporter enough time to batch and send the published metrics to Monitoring.




### Python

  1. To install the required OpenTelemetry and Google Cloud exporter dependencies, run the following commands in your terminal:
         
         pip install redis==7.0.1 opentelemetry-api==1.39.1
           opentelemetry-sdk==1.39.1
           opentelemetry-instrumentation-redis==0.60b1
           opentelemetry-exporter-gcp-trace==1.11.0
           opentelemetry-exporter-gcp-monitoring==1.11.0a0

  2. To enable the client-side metrics, create a `main.py` file and add the following code to your application:
         
         import os
         import time
         
         from opentelemetry import metrics, trace
         from opentelemetry.exporter.cloud_monitoring import (
             CloudMonitoringMetricsExporter,
         )
         from opentelemetry.exporter.cloud_trace import CloudTraceSpanExporter
         from opentelemetry.instrumentation.redis import RedisInstrumentor
         from opentelemetry.sdk.metrics import MeterProvider
         from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
         from opentelemetry.sdk.trace import TracerProvider
         from opentelemetry.sdk.trace.export import BatchSpanProcessor
         import redis
         from redis.exceptions import ConnectionError, TimeoutError
         
         
         
         
         def init_telemetry():
             """Initializes OpenTelemetry with GCP Exporters and returns the SDK objects."""
             # 1. Initialize Tracing
             tracer_provider = TracerProvider()
             tracer_provider.add_span_processor(
                 BatchSpanProcessor(CloudTraceSpanExporter())
             )
             trace.set_tracer_provider(tracer_provider)
             tracer = trace.get_tracer("redis.client")
         
             # 2. Initialize Metrics
             metrics_exporter = CloudMonitoringMetricsExporter()
             metric_reader = PeriodicExportingMetricReader(
                 metrics_exporter, export_interval_millis=10000
             )
             meter_provider = MeterProvider(metric_readers=[metric_reader])
             metrics.set_meter_provider(meter_provider)
             meter = metrics.get_meter("redis.metrics")
         
             # Bundle all metric handlers safely into a dictionary
             redis_metrics = {
                 "rtt_hist": meter.create_histogram("redis_client_rtt", unit="ms"),
                 "client_block_hist": meter.create_histogram(
                     "redis_client_blocking_latency", unit="ms"
                 ),
                 "app_block_hist": meter.create_histogram(
                     "redis_application_blocking_latency", unit="ms"
                 ),
                 "retry_counter": meter.create_counter("redis_retry_count"),
                 "conn_error_counter": meter.create_counter(
                     "redis_connectivity_error_count"
                 ),
             }
         
             redis_metrics["retry_counter"].add(0, {"operation": "startup"})
             redis_metrics["conn_error_counter"].add(0, {"operation": "startup"})
         
             # 3. Setup Redis Auto-Instrumentation
             RedisInstrumentor().instrument()
         
             return tracer, redis_metrics, tracer_provider, meter_provider
         
         
         def init_redis_pool():
             """Initializes and returns the Redis ConnectionPool and Client."""
             redis_host = os.environ.get("REDISHOST", "localhost")
             redis_port = int(os.environ.get("REDISPORT", 6379))
         
             redis_pool = redis.ConnectionPool(
                 host=redis_host,
                 port=redis_port,
                 max_connections=10,
                 decode_responses=True,
             )
             redis_client = redis.Redis(connection_pool=redis_pool)
             return redis_pool, redis_client
         
         
         def smart_redis_call(
             operation_name, func, redis_pool, metrics, *args, **kwargs
         ):
             """Executes a Redis operation with metrics and retry handling (No Globals!)."""
             max_retries = 3
             attempt = 0
         
             pool_start = time.time()
             try:
                 conn = redis_pool.get_connection()
                 redis_pool.release(conn)
             except Exception:
                 pass
         
             if metrics and metrics.get("client_block_hist"):
                 metrics["client_block_hist"].record(
                     (time.time() - pool_start) * 1000, {"operation": operation_name}
                 )
         
             while attempt < max_retries:
                 try:
                     req_start = time.time()
                     response = func(*args, **kwargs)
         
                     if metrics and metrics.get("rtt_hist"):
                         metrics["rtt_hist"].record(
                             (time.time() - req_start) * 1000,
                             {"operation": operation_name},
                         )
         
                     app_start = time.time()
                     _ = str(response)
         
                     if metrics and metrics.get("app_block_hist"):
                         metrics["app_block_hist"].record(
                             (time.time() - app_start) * 1000,
                             {"operation": operation_name},
                         )
         
                     return response
         
                 except (ConnectionError, TimeoutError) as e:
                     attempt += 1
                     if metrics and metrics.get("conn_error_counter"):
                         metrics["conn_error_counter"].add(
                             1, {"operation": operation_name}
                         )
                     if metrics and metrics.get("retry_counter"):
                         metrics["retry_counter"].add(1, {"operation": operation_name})
                     if attempt >= max_retries:
                         raise e
                     time.sleep((2**attempt) * 0.1)
         
         if __name__ == "__main__":
             tracer, redis_metrics, tracer_provider, meter_provider = init_telemetry()
             redis_pool, redis_client = init_redis_pool()
         
             if tracer:
                 with tracer.start_as_current_span("process_user_span"):
                     try:
                         # Simple write and read operations
                         smart_redis_call(
                             "set_user",
                             redis_client.set,
                             redis_pool,
                             redis_metrics,
                             "user:123",
                             "active",
                         )
         
                         result = smart_redis_call(
                             "get_user",
                             redis_client.get,
                             redis_pool,
                             redis_metrics,
                             "user:123",
                         )
                         print(f"Retrieved: {result}")
                     except Exception as e:
                         print(f"Error: {e}")
         
                 tracer_provider.force_flush()
                 meter_provider.force_flush()

  3. Run your application for at least a minute to give the exporter enough time to batch and send the published metrics to Monitoring.




## View metrics in Monitoring

After you enable client-side metrics and run your application for at least a minute to give the exporter enough time to batch and send metrics to Monitoring, use Monitoring to visualize your metrics, group them by operation or instance, and apply aggregators to monitor your application's performance.

To view metrics in Monitoring, do the following:

  1. In the Google Cloud console, go to the **Metrics explorer** page.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer?supportedpurview=project,folder,organizationId)

  2. Select your Google Cloud project.

  3. Click **Select a metric**.

  4. Search for `workload.googleapis.com/redis`.

  5. Select a client-side metric. Group the data by `operation` and `instance` as needed, and pick an aggregator. To explore more options, see [Select metrics when using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector).


**Important** : Because latency is rarely uniform, never rely on the average (mean). When you graph `redis_client_rtt`, configure the aggregation to show the 95th (p95) or 99th (p99) percentile. This reveals the latency experienced by your slowest requests.

## View distributed traces in Trace

After your application begins exporting data, you can use Trace to visualize the full request-response cycle of your Redis commands. Viewing your distributed traces in Trace lets you diagnose bottlenecks so that you can quickly isolate the exact source of latency in your application.

To view distributed traces in Trace, do the following:

  1. In the Google Cloud console, go to the **Trace explorer** page.

[Go to Trace Explorer](https://console.cloud.google.com/traces?supportedpurview=project,folder,organizationId)

  2. Select a recent trace represented by a dot on the scatter plot.

  3. Examine the waterfall view to isolate the source of latency by identifying the following bottlenecks:

     * **Total request duration** : the top-level (parent) bar shows the total time that you must wait for the operation to finish.

     * **Network and server latency (RTT)** : the child bars (such as those labeled `GET` or `SET`) show the time the command spent traveling across the network and running on the Memorystore for Redis server.

     * **Client connection blocking** : if there's a large, empty horizontal gap _before_ the Redis child span begins, then the application thread is stuck waiting for an available TCP connection from the connection pool.

     * **Application parsing blocking** : if there's a large, empty horizontal gap _after_ the Redis child span ends, then the application struggles to parse or process the returned payload. This often happens with multi-megabyte JSON strings.

     * **Retries** : if you see multiple, short child spans for the same command occurring sequentially within the same parent trace, then your client might experience network packet loss and has to trigger its exponential backoff retry loop.




## Troubleshoot

This section lists common performance issues that you can identify using client-side metrics, explains their root causes, and provides guidance on troubleshooting the issues.

Issue | Cause | Troubleshoot  
---|---|---  
Your application experiences a sudden latency spike, but Memorystore for Redis appears completely healthy.

  * `workload.googleapis.com/  
redis_client_blocking_latency` (client-side metric): spiking
  * `workload.googleapis.com/redis_client_rtt` (client-side metric): low / typical
  * `redis.googleapis.com/commands/  
usec_per_call` (Memorystore for Redis server metric): low / typical
  * `redis.googleapis.com/clients/connected` (Memorystore for Redis server metric): flatlines at a specific number 

| The bottleneck is strictly inside your application. Your threads attempt to run Redis commands, but the connection pool is fully exhausted. The high `redis_client_blocking_latency` represents the time your code spends waiting for an available TCP socket before the command is sent to the network. | To handle the higher concurrent traffic, increase the connection pool size limits in your Redis client configuration (for example, `MaxActive` for Go, `MaxTotal` for Java, or `max_connections` for Node.js and Python).  
The request completes, but the endpoint takes significantly longer than expected. There aren't issues associated with the health of your network or server.

  * `workload.googleapis.com/  
redis_application_blocking_latency` (client-side metric): spiking
  * `workload.googleapis.com/redis_client_rtt` (client-side metric): low / typical
  * `redis.googleapis.com/commands/  
usec_per_call` (Memorystore for Redis server metric): low / typical
  * `redis.googleapis.com/stats/  
network_traffic` (Bytes out) (Memorystore for Redis server metric): spikes heavily

| Memorystore for Redis runs the command and the network transfers the payload quickly (low RTT). However, the payload that returns is large (for example, a 15-MB JSON string). Your application experiences a high `redis_application_blocking_latency` because the application consumes excessive resources while allocating memory and deserializing that large string into an object. | Optimize your data model. Don't store massive JSON blobs in single keys. Break the data down using Redis hashes (`HSET`) and use `HGET` or `HMGET` to retrieve only the specific fields that you need.   
Your user-facing application latency spikes, but your Redis metrics report a low server latency and typical connection pool checkouts.

  * `workload.googleapis.com/redis_retry_count` (client-side metric): spikes
  * `workload.googleapis.com/  
redis_connectivity_error_count` (client-side metric): might show transient increments
  * `workload.googleapis.com/redis_client_rtt` (client-side metric): low / typical for successful requests
  * `redis.googleapis.com/commands/  
usec_per_call` (Memorystore for Redis server metric): low / typical

| Because `redis_client_rtt` only captures the RTT of successful requests, it doesn't reflect the timeout duration of a failed packet. When your application experiences transient packet drops or TCP resets, your instrumented client's retry logic increments the `redis_retry_count` and triggers its exponential backoff loop. This introduces a sleep time between attempts (for example, `100ms`, `200ms`, or `400ms`). The user experiences high total latency, but the underlying root cause is a network packet loss, which triggers client-side sleep delays. | Check your VPC Flow Logs for dropped packets, bandwidth throttling, or cross-region routing anomalies. If you experience aggressive timeouts, then ensure your client connection timeouts (`socket_timeout` or `connect_timeout`) are greater than the expected RTT to account for transient network jitter.  
Everything stops and all layers of the telemetry pipeline report high latency.

  * `workload.googleapis.com/redis_client_rtt` (client-side metric): high
  * `redis.googleapis.com/commands/  
usec_per_call` (Memorystore for Redis server metric): high
  * `redis.googleapis.com/stats/  
cpu_utilization_main_thread` (Memorystore for Redis server metric): high (for example, close to 1 s/s, or 100%)
  * Trace waterfall: shows a command taking a large amount of time

| Redis is single-threaded. When you run an `O(N)` time-complexity command—such as `KEYS *`, `SMEMBERS` on a massive set, or `HGETALL` on a hash with millions of fields—the Redis engine pauses to fulfill that request. While that command runs, every other application request queues, causing a system-wide latency spike. Because your custom `redis_client_rtt` matches the server's latency (`commands/usec_per_call`), the server that runs the command is the bottleneck. | Open Trace and look at the Redis commands on the slow spans to identify which query causes the blockage. Replace blocking commands with non-blocking ones in your code.  To iterate through large datasets incrementally without locking the server thread, use `SCAN`, `SSCAN`, or `HSCAN`.  
Your application reports a consistent, elevated baseline latency for all Redis commands, even when traffic is low.

  * `workload.googleapis.com/redis_client_rtt` (client-side metric): consistently elevated (p50 and p99 are both ~30-100ms+)
  * `redis.googleapis.com/commands/  
usec_per_call` (Memorystore for Redis server metric): extremely low (< 1ms)
  * `workload.googleapis.com/  
redis_client_blocking_latency`  
and `redis_application_blocking_latency`: low / typical

| The Redis server runs commands instantly, but your application and your instance are deployed in different regions (for example, `us-central1` and `us-east1`). Every network packet must travel across the physical Google Cloud infrastructure between these geographical data centers. This results in a mandatory speed-of-light cross-region latency penalty for every round trip. | To reduce latency, deploy your application to reside in the same region and zone as your instance. To view the region of your application and instance, use the Google Cloud console.  
  
## What's next

  * Learn more about [client-side metrics](https://docs.cloud.google.com/memorystore/docs/redis/about-client-side-metrics).
  * Learn about the [client-side metrics that are available for Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/supported-monitoring-metrics#client-side-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
