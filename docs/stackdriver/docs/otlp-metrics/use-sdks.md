---
url: https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/use-sdks/
title: Use SDKs to send metrics from applications \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:03.392144+00:00
---

# Use SDKs to send metrics from applications  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/otlp-metrics/use-sdks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Use SDKs to send metrics from applications Stay organized with collections  Save and categorize content based on your preferences. 

This document illustrates how you can send metrics directly from applications to the OTLP endpoint by using an SDK and the gRPC exporter, which is the recommended exporter for use with SDKs. The OTLP endpoint supports all of the OTLP protocols, including `http/proto`, `http/json`, and `grpc`. For more information, see [Protocol support](https://docs.cloud.google.com/stackdriver/docs/otlp/overview#protocol-support).

When you send application metrics directly to the OTLP endpoint, the OpenTelemetry Collector does not handle authentication, resource detection, or batching for you. When using SDKs to send metrics from applications, you need to do the following:

  * Configure credentials for the OTLP gRPC exporter to use Google [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc), as described in Get authentication credentials.
  * Detect Google Cloud and Kubernetes resources from the application. How you do this depends on the application you're running.
  * Configure a maximum export batch size of 200 metric data points so that requests don't exceed the [Telemetry API limit](https://docs.cloud.google.com/stackdriver/quotas#telemetry-api-limits) of 200 data points per request.



## Before you begin

To run the examples, you must enable the necessary APIs and acquire authentication credentials.

### Enable APIs

Enable the Cloud Monitoring API and the Telemetry API in your Google Cloud project by running the following command:
    
    
    gcloud services enable monitoring.googleapis.com telemetry.googleapis.com
    

### Get authentication credentials

Configure credentials for the OTLP gRPC exporter to use Google [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) by running the following command:
    
    
    gcloud auth application-default login
    

## Language-specific examples

This section provides a selection of language-specific samples that create and write a counter metric. Select a tab for information about running the sample and to view the code.

###  Go 

For information about configuring and running this example, see the `README` file for the [Go sample](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/golang/metric/otlpgrpc).
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     http://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    package main
    
    import (
    	"context"
    	"errors"
    	"log"
    
    	"go.opentelemetry.io/contrib/detectors/gcp"
    	"go.opentelemetry.io/otel/attribute"
    	"go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc"
    	"go.opentelemetry.io/otel/metric"
    	sdkmetric "go.opentelemetry.io/otel/sdk/metric"
    	"go.opentelemetry.io/otel/sdk/resource"
    	semconv "go.opentelemetry.io/otel/semconv/v1.37.0"
    	"google.golang.org/grpc"
    	"google.golang.org/grpc/credentials/oauth"
    )
    
    func main() {
    	ctx := context.Background()
    
    	creds, err := oauth.NewApplicationDefault(ctx)
    	if err != nil {
    		panic(err)
    	}
    
    	res, err := resource.New(
    		ctx,
    		// Use the GCP resource detector to detect information about the GCP platform
    		resource.WithDetectors(gcp.NewDetector()),
    		// Keep the default detectors
    		resource.WithTelemetrySDK(),
    		// Add attributes from environment variables
    		resource.WithFromEnv(),
    		// Add your own custom attributes to identify your application
    		resource.WithAttributes(
    			semconv.ServiceNameKey.String("example-application"),
    		),
    	)
    	if errors.Is(err, resource.ErrPartialResource) || errors.Is(err, resource.ErrSchemaURLConflict) {
    		log.Println(err)
    	} else if err != nil {
    		panic(err)
    	}
    
    	// Set endpoint with OTEL_EXPORTER_OTLP_ENDPOINT or OTEL_EXPORTER_OTLP_METRICS_ENDPOINT
    	metricExporter, err := otlpmetricgrpc.New(ctx, otlpmetricgrpc.WithDialOption(grpc.WithPerRPCCredentials(creds)))
    	if err != nil {
    		panic(err)
    	}
    
    	meterProvider := sdkmetric.NewMeterProvider(
    		sdkmetric.WithResource(res),
    		sdkmetric.WithReader(
    			sdkmetric.NewPeriodicReader(
    				metricExporter,
    				sdkmetric.WithMaxExportBatchSize(200),
    			),
    		),
    	)
    
    	defer func() {
    		if err = meterProvider.Shutdown(ctx); err != nil {
    			log.Println(err)
    		}
    	}()
    
    	meter := meterProvider.Meter("github.com/GoogleCloudPlatform/opentelemetry-samples/golang/metric/otlpgrpc")
    
    	// Register counter value
    	counter, err := meter.Int64Counter("counter-a")
    	if err != nil {
    		log.Fatalf("Failed to create counter: %v", err)
    	}
    	clabels := []attribute.KeyValue{attribute.Key("key").String("value")}
    	counter.Add(ctx, 100, metric.WithAttributes(clabels...))
    }
    

###  Java 

For information about configuring and running this example, see the `README` file for the [Java sample](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/java/otlpmetric).
    
    
    /*
     * Copyright 2026 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     * http://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    package com.google.cloud.opentelemetry.samples.otlpmetric;
    
    import io.opentelemetry.api.metrics.LongCounter;
    import io.opentelemetry.sdk.OpenTelemetrySdk;
    import io.opentelemetry.sdk.autoconfigure.AutoConfiguredOpenTelemetrySdk;
    import io.opentelemetry.sdk.common.CompletableResultCode;
    import java.util.Random;
    import java.util.concurrent.TimeUnit;
    
    public class OTLPMetricExample {
      private static final String INSTRUMENTATION_SCOPE_NAME = OTLPMetricExample.class.getName();
      private static final Random RANDOM = new Random();
    
      private static OpenTelemetrySdk openTelemetrySdk;
    
      private static void myUseCase() {
        LongCounter counter =
            openTelemetrySdk
                .getMeter(INSTRUMENTATION_SCOPE_NAME)
                .counterBuilder("example_counter")
                .setDescription("Processed jobs")
                .setUnit("1")
                .build();
        doWork(counter);
      }
    
      private static void doWork(LongCounter counter) {
        try {
          for (int i = 0; i < 10; i++) {
            counter.add(RANDOM.nextInt(100));
            Thread.sleep(RANDOM.nextInt(1000));
          }
        } catch (InterruptedException e) {
          throw new RuntimeException(e);
        }
      }
    
      public static void main(String[] args) {
        // Configure the OpenTelemetry pipeline with Auto configuration
        openTelemetrySdk = AutoConfiguredOpenTelemetrySdk.initialize().getOpenTelemetrySdk();
    
        // Application-specific logic
        myUseCase();
    
        // Flush all buffered metrics
        CompletableResultCode completableResultCode = openTelemetrySdk.getSdkMeterProvider().shutdown();
        // wait till export finishes
        completableResultCode.join(10000, TimeUnit.MILLISECONDS);
      }
    }
    

###  NodeJS 

For information about configuring and running this example, see the `README` file for the [NodeJS sample](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/javascript/otlpmetricexport).
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //      https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    import * as opentelemetry from '@opentelemetry/sdk-node';
    import {AuthClient, GoogleAuth} from 'google-auth-library';
    import {credentials} from '@grpc/grpc-js';
    import {getResourceDetectors as getResourceDetectorsFromEnv} from '@opentelemetry/auto-instrumentations-node';
    import {metrics, diag, DiagConsoleLogger} from '@opentelemetry/api';
    import {OTLPMetricExporter} from '@opentelemetry/exporter-metrics-otlp-grpc';
    import {PeriodicExportingMetricReader} from '@opentelemetry/sdk-metrics';
    
    async function getAuthenticatedClient(): Promise<AuthClient> {
      const auth: GoogleAuth = new GoogleAuth({
        scopes: 'https://www.googleapis.com/auth/cloud-platform',
      });
      return await auth.getClient();
    }
    
    diag.setLogger(
      new DiagConsoleLogger(),
      opentelemetry.core.diagLogLevelFromString(
        opentelemetry.core.getStringFromEnv('OTEL_LOG_LEVEL'),
      ),
    );
    
    // App that exports metrics via gRPC with protobuf
    async function main() {
      const authenticatedClient: AuthClient = await getAuthenticatedClient();
    
      const sdk = new opentelemetry.NodeSDK({
        metricReaders: [
          new PeriodicExportingMetricReader({
            // Export metrics every 10 seconds. 5 seconds is the smallest sample period allowed by
            // Cloud Monitoring.
            exportIntervalMillis: 10_000,
            // Cloud Monitoring allows at most 200 time series per write request.
            maxExportBatchSize: 200,
            exporter: new OTLPMetricExporter({
              credentials: credentials.combineChannelCredentials(
                credentials.createSsl(),
                credentials.createFromGoogleCredential(authenticatedClient),
              ),
            }),
          }),
        ],
        resourceDetectors: getResourceDetectorsFromEnv(),
      });
      sdk.start();
    
      // Create a meter
      const meter = metrics.getMeter('metrics-sample');
    
      // Create a counter instrument
      const counter = meter.createCounter('metric_name');
      // Record a measurement
      counter.add(10, {key: 'value'});
    
      // Wait for the metric to be exported
      await new Promise(resolve => {
        setTimeout(resolve, 11_000);
      });
    
      // Gracefully shut down the SDK to flush telemetry when the program exits
      process.on('SIGTERM', () => {
        sdk
          .shutdown()
          .then(() => diag.debug('OpenTelemetry SDK terminated'))
          .catch(error => diag.error('Error terminating OpenTelemetry SDK', error));
      });
    }
    
    main().catch(console.error);
    

###  Python 

For information about running this example, see the `README` file for the [Python sample](https://github.com/GoogleCloudPlatform/opentelemetry-samples/tree/main/python/otlpmetric).
    
    
    #!/usr/bin/env python3
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    import time
    
    import google.auth
    import google.auth.transport.grpc
    import google.auth.transport.requests
    import grpc
    from google.auth.transport.grpc import AuthMetadataPlugin
    from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import (
        OTLPMetricExporter,
    )
    from opentelemetry.resourcedetector.gcp_resource_detector import (
        GoogleCloudResourceDetector,
    )
    from opentelemetry.sdk.resources import get_aggregated_resources
    from opentelemetry.sdk.metrics import MeterProvider
    from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
    
    """
    Sample script exporting OTLP metrics encoded as protobufs via gRPC.
    """
    
    credentials, project_id = google.auth.default()
    request = google.auth.transport.requests.Request()
    resource = get_aggregated_resources([GoogleCloudResourceDetector(raise_on_error=True)])
    
    auth_metadata_plugin = AuthMetadataPlugin(credentials=credentials, request=request)
    channel_creds = grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(),
        grpc.metadata_call_credentials(auth_metadata_plugin),
    )
    
    exporter = OTLPMetricExporter(
        credentials=channel_creds,
        max_export_batch_size=200,
    )
    reader = PeriodicExportingMetricReader(exporter)
    provider = MeterProvider(metric_readers=[reader], resource=resource)
    meter = provider.get_meter("gcp.otlp.sample")
    counter = meter.create_counter("sample.otlp.counter")
    
    
    def do_work():
        counter.add(1)
        # do some work that the 'counter' will track
        print("doing some work...")
    
    
    def do_work_repeatedly():
        try:
            while True:
                do_work()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nKeyboard Interrupt: Stopping work.")
    
    
    do_work_repeatedly()
    

## Use the downward API for applications running as pods

If you are running the application as a pod in Kubernetes and aren't sending telemetry through the OpenTelemetry Collector, then make sure to use the [downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/) to set Kubernetes resource attributes:
    
    
    env:
    - name: POD_NAME
      valueFrom:
        fieldRef:
          fieldPath: metadata.name
    - name: NAMESPACE_NAME
      valueFrom:
        fieldRef:
          fieldPath: metadata.namespace
    - name: CONTAINER_NAME
      value: my-container-name
    - name: OTEL_RESOURCE_ATTRIBUTES
      value: k8s.pod.name=$(POD_NAME),k8s.namespace.name=$(NAMESPACE_NAME),k8s.container.name=$(CONTAINER_NAME)
    

## What's next

  * For information about using an OpenTelemetry Collector and the Telemetry API with OpenTelemetry zero-code instrumentation, see [Use OpenTelemetry zero-code instrumentation for Java](https://docs.cloud.google.com/stackdriver/docs/instrumentation/otel-zerocode-java-gke).
  * For information about migrating to the `otlphttp` exporter from another exporter, see [Migrate to the OTLP exporter](https://docs.cloud.google.com/stackdriver/docs/otlp/migrate-collector-to-otlp-exporters).
  * To learn more about the Telemetry API, see [Telemetry (OTLP) API overview](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
