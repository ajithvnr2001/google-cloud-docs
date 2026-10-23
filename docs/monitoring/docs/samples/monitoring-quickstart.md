---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-quickstart/
title: Using the client libraries \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:29.567837+00:00
---

# Using the client libraries  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Using the client libraries Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to write time series data to custom sales metrics.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Monitoring client libraries](https://docs.cloud.google.com/monitoring/docs/reference/libraries)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Cloud.Monitoring.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using [Google.Api](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    
    namespace GoogleCloudSamples
    {
        public class QuickStart
        {
            public static void Main(string[] args)
            {
                // Your Google Cloud Platform project ID.
                string projectId = "YOUR-PROJECT-ID";
    
                // Create client.
                [MetricServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient.html) metricServiceClient = [MetricServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient.html#Google_Cloud_Monitoring_V3_MetricServiceClient_Create)();
    
                // Initialize request argument(s).
                [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) name = new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)(projectId);
    
                // Prepare a data point.
                [TypedValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TypedValue.html) salesTotal = new [TypedValue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TypedValue.html)
                {
                    DoubleValue = 123.45
                };
                [Point](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.Point.html) dataPoint = new [Point](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.Point.html)
                {
                    Value = salesTotal
                };
                // Sets data point's interval end time to current time.
                DateTime UnixEpoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);
                [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html) timeStamp = new [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)
                {
                    Seconds = (long)(DateTime.UtcNow - UnixEpoch).TotalSeconds
                };
                [TimeInterval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeInterval.html) interval = new [TimeInterval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeInterval.html)
                {
                    EndTime = timeStamp
                };
                dataPoint.[Interval](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.Point.html#Google_Cloud_Monitoring_V3_Point_Interval) = interval;
    
                // Prepare custom metric.
                [Metric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Metric.html) metric = new [Metric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Metric.html)
                {
                    Type = "custom.googleapis.com/my_metric"
                };
                metric.[Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.Metric.html#Google_Api_Metric_Labels).[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_)("store_id", "Pittsburgh");
    
                // Prepare monitored resource.
                [MonitoredResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html) resource = new [MonitoredResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html)
                {
                    Type = "gce_instance"
                };
    
                resource.[Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html#Google_Api_MonitoredResource_Labels).[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_)("project_id", projectId);
                resource.[Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html#Google_Api_MonitoredResource_Labels).[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_)("instance_id", "1234567890123456789");
                resource.[Labels](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Api.MonitoredResource.html#Google_Api_MonitoredResource_Labels).[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_)("zone", "us-central1-f");
    
                // Create a new time series using inputs.
                [TimeSeries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeries.html) timeSeriesData = new [TimeSeries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeries.html)
                {
                    Metric = metric,
                    Resource = resource
                };
                timeSeriesData.[Points](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.TimeSeries.html#Google_Cloud_Monitoring_V3_TimeSeries_Points).[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Requests.Parameters.ParameterCollection.html#Google_Apis_Requests_Parameters_ParameterCollection_Add_System_String_System_String_)(dataPoint);
    
                // Add newly created time series to list of time series to be written.
                IEnumerable<TimeSeries> timeSeries = new List<TimeSeries> { timeSeriesData };
                // Write time series data.
                metricServiceClient.[CreateTimeSeries](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Monitoring.V3/latest/Google.Cloud.Monitoring.V3.MetricServiceClient.html#Google_Cloud_Monitoring_V3_MetricServiceClient_CreateTimeSeries_Google_Api_Gax_ResourceNames_ProjectName_System_Collections_Generic_IEnumerable_Google_Cloud_Monitoring_V3_TimeSeries__Google_Api_Gax_Grpc_CallSettings_)(name, timeSeries);
                Console.WriteLine("Done writing time series data.");
            }
        }
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample monitoring-quickstart writes a data point to Stackdriver Monitoring.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	monitoring "cloud.google.com/go/monitoring/apiv3/v2"
    	"cloud.google.com/go/monitoring/apiv3/v2/monitoringpb"
    	googlepb "github.com/golang/protobuf/ptypes/timestamp"
    	metricpb "google.golang.org/genproto/googleapis/api/metric"
    	monitoredrespb "google.golang.org/genproto/googleapis/api/monitoredres"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := monitoring.[NewMetricClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/apiv3/v2.html#cloud_google_com_go_monitoring_apiv3_v2_MetricClient_NewMetricClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    
    	// Sets your Google Cloud Platform project ID.
    	projectID := "YOUR_PROJECT_ID"
    
    	// Prepares an individual data point
    	dataPoint := &monitoringpb.Point{
    		Interval: &monitoringpb.TimeInterval{
    			EndTime: &googlepb.Timestamp{
    				Seconds: time.Now().Unix(),
    			},
    		},
    		Value: &monitoringpb.TypedValue{
    			Value: &monitoringpb.TypedValue_DoubleValue{
    				DoubleValue: 123.45,
    			},
    		},
    	}
    
    	// Writes time series data.
    	if err := client.CreateTimeSeries(ctx, &monitoringpb.CreateTimeSeriesRequest{
    		Name: fmt.Sprintf("projects/%s", projectID),
    		TimeSeries: []*monitoringpb.TimeSeries{
    			{
    				Metric: &metricpb.Metric{
    					Type: "custom.googleapis.com/stores/daily_sales",
    					Labels: map[string]string{
    						"store_id": "Pittsburg",
    					},
    				},
    				Resource: &monitoredrespb.MonitoredResource{
    					Type: "global",
    					Labels: map[string]string{
    						"project_id": projectID,
    					},
    				},
    				Points: []*monitoringpb.Point{
    					dataPoint,
    				},
    			},
    		},
    	}); err != nil {
    		log.Fatalf("Failed to write time series data: %v", err)
    	}
    
    	// Closes the client and flushes the data to Stackdriver.
    	if err := client.Close(); err != nil {
    		log.Fatalf("Failed to close client: %v", err)
    	}
    
    	fmt.Printf("Done writing time series data.\n")
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.[Metric](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.Metric.html);
    import com.google.api.[MonitoredResource](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MonitoredResource.html);
    import com.google.cloud.monitoring.v3.[MetricServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.MetricServiceClient.html);
    import com.google.monitoring.v3.[CreateTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateTimeSeriesRequest.html);
    import com.google.monitoring.v3.[Point](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.Point.html);
    import com.google.monitoring.v3.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html);
    import com.google.monitoring.v3.[TimeInterval](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeInterval.html);
    import com.google.monitoring.v3.[TimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.html);
    import com.google.monitoring.v3.[TypedValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TypedValue.html);
    import com.google.protobuf.util.[Timestamps](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Timestamps.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.HashMap;
    import java.util.List;
    import java.util.Map;
    
    public class QuickstartSample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        quickstart(projectId);
      }
    
      public static void quickstart(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([MetricServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.MetricServiceClient.html) metricServiceClient = [MetricServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.MetricServiceClient.html).create()) {
    
          // Prepares an individual data point
          [TimeInterval](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeInterval.html) interval =
              [TimeInterval](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeInterval.html).newBuilder()
                  .setEndTime([Timestamps](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.Timestamps.html).fromMillis(System.currentTimeMillis()))
                  .build();
          [TypedValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TypedValue.html) value = [TypedValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TypedValue.html).newBuilder().setDoubleValue(123.45).build();
          [Point](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.Point.html) point = [Point](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.Point.html).newBuilder().setInterval(interval).setValue(value).build();
    
          List<Point> pointList = new ArrayList<>();
          pointList.add(point);
    
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html) name = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html).of(projectId);
    
          // Prepares the metric descriptor
          Map<String, String> metricLabels = new HashMap<>();
          metricLabels.put("store_id", "Pittsburg");
          [Metric](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.Metric.html) metric =
              [Metric](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.Metric.html).newBuilder()
                  .setType("custom.googleapis.com/stores/daily_sales")
                  .putAllLabels(metricLabels)
                  .build();
    
          // Prepares the monitored resource descriptor
          Map<String, String> resourceLabels = new HashMap<>();
          resourceLabels.put("project_id", projectId);
          [MonitoredResource](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MonitoredResource.html) resource =
              [MonitoredResource](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.api.MonitoredResource.html).newBuilder().setType("global").putAllLabels(resourceLabels).build();
    
          // Prepares the time series request
          [TimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.html) timeSeries =
              [TimeSeries](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.html).newBuilder()
                  .setMetric(metric)
                  .[setResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.Builder.html#com_google_monitoring_v3_TimeSeries_Builder_setResource_com_google_api_MonitoredResource_)(resource)
                  .[addAllPoints](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.TimeSeries.Builder.html#com_google_monitoring_v3_TimeSeries_Builder_addAllPoints_java_lang_Iterable___extends_com_google_monitoring_v3_Point__)(pointList)
                  .build();
          List<TimeSeries> timeSeriesList = new ArrayList<>();
          timeSeriesList.add(timeSeries);
    
          [CreateTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateTimeSeriesRequest.html) request =
              [CreateTimeSeriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateTimeSeriesRequest.html).newBuilder()
                  .setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ProjectName.html#com_google_monitoring_v3_ProjectName_toString__)())
                  .addAllTimeSeries(timeSeriesList)
                  .build();
    
          // Writes time series data
          metricServiceClient.createTimeSeries(request);
    
          System.out.printf("Done writing time series data.%n");
        }
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    async function quickstart() {
      // Creates a client
      const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
      // TODO(developer): Uncomment and set the following variables
      // const projectId = "PROJECT_ID"
    
      // Prepares an individual data point
      const dataPoint = {
        interval: {
          endTime: {
            seconds: Date.now() / 1000,
          },
        },
        value: {
          // The amount of sales
          doubleValue: 123.45,
        },
      };
    
      // Prepares the time series request
      const request = {
        name: client.projectPath(projectId),
        timeSeries: [
          {
            // Ties the data point to a custom metric
            metric: {
              type: 'custom.googleapis.com/stores/daily_sales',
              labels: {
                store_id: 'Pittsburgh',
              },
            },
            resource: {
              type: 'global',
              labels: {
                project_id: projectId,
              },
            },
            points: [dataPoint],
          },
        ],
      };
    
      // Writes time series data
      const [result] = await client.createTimeSeries(request);
      console.log('Done writing time series data.', result);
    }
    quickstart();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Includes the autoloader for libraries installed with composer
    require_once __DIR__ . '/vendor/autoload.php';
    
    # Imports the Google Cloud client library
    use Google\Api\Metric;
    use Google\Api\MonitoredResource;
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\CreateTimeSeriesRequest;
    use Google\Cloud\Monitoring\V3\Point;
    use Google\Cloud\Monitoring\V3\TimeInterval;
    use Google\Cloud\Monitoring\V3\TimeSeries;
    use Google\Cloud\Monitoring\V3\TypedValue;
    use Google\Protobuf\Timestamp;
    
    // These variables are set by the App Engine environment. To test locally,
    // ensure these are set or manually change their values.
    $projectId = getenv('GCLOUD_PROJECT') ?: 'YOUR_PROJECT_ID';
    $instanceId = '1234567890123456789';
    $zone = 'us-central1-f';
    
    try {
        $client = new MetricServiceClient();
        $formattedProjectName = 'projects/' . $projectId;
        $labels = [
            'instance_id' => $instanceId,
            'zone' => $zone,
        ];
    
        $m = new Metric();
        $m->setType('custom.googleapis.com/my_metric');
    
        $r = new MonitoredResource();
        $r->setType('gce_instance');
        $r->setLabels($labels);
    
        $value = new TypedValue();
        $value->setDoubleValue(3.14);
    
        $timestamp = new Timestamp();
        $timestamp->setSeconds(time());
    
        $interval = new TimeInterval();
        $interval->setStartTime($timestamp);
        $interval->setEndTime($timestamp);
    
        $point = new Point();
        $point->setValue($value);
        $point->setInterval($interval);
        $points = [$point];
    
        $timeSeries = new TimeSeries();
        $timeSeries->setMetric($m);
        $timeSeries->setResource($r);
        $timeSeries->setPoints($points);
        $createTimeSeriesRequest = (new CreateTimeSeriesRequest())
            ->setName($formattedProjectName)
            ->setTimeSeries([$timeSeries]);
    
        $client->createTimeSeries($createTimeSeriesRequest);
        print('Successfully submitted a time series' . PHP_EOL);
    } finally {
        $client->close();
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    import time
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    # project_id = 'my-project'  # TODO: Update to your project ID.
    project_name = f"projects/{project_id}"
    
    series = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[TimeSeries](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeSeries.html)()
    series.metric.type = "custom.googleapis.com/my_metric"
    series.metric.labels["store_id"] = "Pittsburgh"
    series.resource.type = "gce_instance"
    series.resource.labels["instance_id"] = "1234567890123456789"
    series.resource.labels["zone"] = "us-central1-f"
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[TimeInterval](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeInterval.html)(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[Point](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Point.html)({"interval": interval, "value": {"double_value": 3.14}})
    series.points = [point]
    client.[create_time_series](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_time_series)(request={"name": project_name, "time_series": [series]})
    print("Successfully wrote time series.")
    return True

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    # Example metric label
    # metric_label = "my-value"
    
    # Instantiates a client
    metric_service_client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    project_path = metric_service_client.project_path project: project_id
    
    series = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TimeSeries.new
    series.[metric](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) = Google::Api::[Metric](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Metric.html).new type:   "custom.googleapis.com/my_metric",
                                            labels: { "my_key" => metric_label }
    
    resource = Google::Api::[MonitoredResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_usage-v1/latest/Google-Api-MonitoredResource.html).new type: "gce_instance"
    resource.labels["project_id"] = project_id
    resource.labels["instance_id"] = "1234567890123456789"
    resource.labels["zone"] = "us-central1-f"
    series.[resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) = resource
    
    point = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::Point.new
    point.value = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TypedValue.new double_value: 3.14
    now = Time.now
    end_time = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i, nanos: now.nsec
    point.interval = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TimeInterval.new end_time: end_time
    series.[points](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) << point
    
    metric_service_client.create_time_series name: project_path, time_series: [series]
    
    puts "Successfully wrote time series."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
