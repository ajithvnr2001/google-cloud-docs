---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-write-timeseries/
title: Write metric data \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:31.618179+00:00
---

# Write metric data  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-write-timeseries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Write metric data Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to write time series data.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create user-defined metrics with the API](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object WriteTimeSeriesData(string projectId)
    {
        // Create client.
        MetricServiceClient metricServiceClient = MetricServiceClient.Create();
        // Initialize request argument(s).
        ProjectName name = new ProjectName(projectId);
        // Prepare a data point. 
        Point dataPoint = new Point();
        TypedValue salesTotal = new TypedValue();
        salesTotal.DoubleValue = 123.45;
        dataPoint.Value = salesTotal;
        Timestamp timeStamp = new Timestamp();
        timeStamp.Seconds = (long)(DateTime.UtcNow - s_unixEpoch).TotalSeconds;
        TimeInterval interval = new TimeInterval();
        interval.EndTime = timeStamp;
        dataPoint.Interval = interval;
    
        // Prepare custom metric.
        Metric metric = new Metric();
        metric.Type = "custom.googleapis.com/stores/daily_sales";
        metric.Labels.Add("store_id", "Pittsburgh");
    
        // Prepare monitored resource.
        MonitoredResource resource = new MonitoredResource();
        resource.Type = "global";
        resource.Labels.Add("project_id", projectId);
    
        // Create a new time series using inputs.
        TimeSeries timeSeriesData = new TimeSeries();
        timeSeriesData.Metric = metric;
        timeSeriesData.Resource = resource;
        timeSeriesData.Points.Add(dataPoint);
    
        // Add newly created time series to list of time series to be written.
        IEnumerable<TimeSeries> timeSeries = new List<TimeSeries> { timeSeriesData };
        // Write time series data.
        metricServiceClient.CreateTimeSeries(name, timeSeries);
        Console.WriteLine("Done writing time series data:");
        Console.WriteLine(JObject.Parse($"{timeSeriesData}").ToString());
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // writeTimeSeriesValue writes a value for the custom metric created
    func writeTimeSeriesValue(projectID, metricType string) error {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer c.Close()
    	now := &timestamp.Timestamp{
    		Seconds: time.Now().Unix(),
    	}
    	req := &monitoringpb.CreateTimeSeriesRequest{
    		Name: "projects/" + projectID,
    		TimeSeries: []*monitoringpb.TimeSeries{{
    			Metric: &metricpb.Metric{
    				Type: metricType,
    				Labels: map[string]string{
    					"environment": "STAGING",
    				},
    			},
    			Resource: &monitoredres.MonitoredResource{
    				Type: "gce_instance",
    				Labels: map[string]string{
    					"instance_id": "test-instance",
    					"zone":        "us-central1-f",
    				},
    			},
    			Points: []*monitoringpb.Point{{
    				Interval: &monitoringpb.TimeInterval{
    					StartTime: now,
    					EndTime:   now,
    				},
    				Value: &monitoringpb.TypedValue{
    					Value: &monitoringpb.TypedValue_Int64Value{
    						Int64Value: rand.Int63n(10),
    					},
    				},
    			}},
    		}},
    	}
    	log.Printf("writeTimeseriesRequest: %+v\n", req)
    
    	err = c.CreateTimeSeries(ctx, req)
    	if err != nil {
    		return fmt.Errorf("could not write time series value, %w ", err)
    	}
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    String projectId = System.getProperty("projectId");
    
    // Prepares an individual data point
    TimeInterval interval =
        TimeInterval.newBuilder()
            .setEndTime(Timestamps.fromMillis(System.currentTimeMillis()))
            .build();
    TypedValue value = TypedValue.newBuilder().setDoubleValue(123.45).build();
    Point point = Point.newBuilder().setInterval(interval).setValue(value).build();
    
    List<Point> pointList = new ArrayList<>();
    pointList.add(point);
    
    ProjectName name = ProjectName.of(projectId);
    
    // Prepares the metric descriptor
    Map<String, String> metricLabels = new HashMap<>();
    Metric metric =
        Metric.newBuilder()
            .setType("custom.googleapis.com/my_metric")
            .putAllLabels(metricLabels)
            .build();
    
    // Prepares the monitored resource descriptor
    Map<String, String> resourceLabels = new HashMap<>();
    resourceLabels.put("instance_id", "1234567890123456789");
    resourceLabels.put("zone", "us-central1-f");
    
    MonitoredResource resource =
        MonitoredResource.newBuilder().setType("gce_instance").putAllLabels(resourceLabels).build();
    
    // Prepares the time series request
    TimeSeries timeSeries =
        TimeSeries.newBuilder()
            .setMetric(metric)
            .setResource(resource)
            .addAllPoints(pointList)
            .build();
    
    List<TimeSeries> timeSeriesList = new ArrayList<>();
    timeSeriesList.add(timeSeries);
    
    CreateTimeSeriesRequest request =
        CreateTimeSeriesRequest.newBuilder()
            .setName(name.toString())
            .addAllTimeSeries(timeSeriesList)
            .build();
    
    // Writes time series data
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      client.createTimeSeries(request);
    }
    System.out.println("Done writing time series value.");

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function writeTimeSeriesData() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
    
      const dataPoint = {
        interval: {
          endTime: {
            seconds: Date.now() / 1000,
          },
        },
        value: {
          doubleValue: 123.45,
        },
      };
    
      const timeSeriesData = {
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
      };
    
      const request = {
        name: client.projectPath(projectId),
        timeSeries: [timeSeriesData],
      };
    
      // Writes time series data
      const result = await client.createTimeSeries(request);
      console.log('Done writing time series data.', result);
    }
    writeTimeSeriesData();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Api\Metric;
    use Google\Api\MonitoredResource;
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\CreateTimeSeriesRequest;
    use Google\Cloud\Monitoring\V3\Point;
    use Google\Cloud\Monitoring\V3\TimeInterval;
    use Google\Cloud\Monitoring\V3\TimeSeries;
    use Google\Cloud\Monitoring\V3\TypedValue;
    use Google\Protobuf\Timestamp;
    
    /**
     * Example:
     * ```
     * write_timeseries($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function write_timeseries($projectId)
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $projectName = 'projects/' . $projectId;
    
        $endTime = new Timestamp();
        $endTime->setSeconds(time());
        $interval = new TimeInterval();
        $interval->setEndTime($endTime);
    
        $value = new TypedValue();
        $value->setDoubleValue(123.45);
    
        $point = new Point();
        $point->setValue($value);
        $point->setInterval($interval);
        $points = [$point];
    
        $metric = new Metric();
        $metric->setType('custom.googleapis.com/stores/daily_sales');
        $labels = ['store_id' => 'Pittsburg'];
        $metric->setLabels($labels);
    
        $resource = new MonitoredResource();
        $resource->setType('global');
        $labels = ['project_id' => $projectId];
        $resource->setLabels($labels);
    
        $timeSeries = new TimeSeries();
        $timeSeries->setMetric($metric);
        $timeSeries->setResource($resource);
        $timeSeries->setPoints($points);
        $createTimeSeriesRequest = (new CreateTimeSeriesRequest())
            ->setName($projectName)
            ->setTimeSeries([$timeSeries]);
    
        $metrics->createTimeSeries($createTimeSeriesRequest);
    
        printf('Done writing time series data.' . PHP_EOL);
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    project_name = f"projects/{project_id}"
    
    series = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[TimeSeries](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeSeries.html)()
    series.metric.type = "custom.googleapis.com/my_metric" + str(uuid.uuid4())
    series.resource.type = "gce_instance"
    series.resource.labels["instance_id"] = "1234567890123456789"
    series.resource.labels["zone"] = "us-central1-c"
    series.metric.labels["TestLabel"] = "My Label Data"
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[TimeInterval](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeInterval.html)(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[Point](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Point.html)({"interval": interval, "value": {"double_value": 3.14}})
    series.points = [point]
    client.[create_time_series](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_time_series)(name=project_name, time_series=[series])

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    # Example metric type
    # metric_type = "custom.googleapis.com/my_metric"
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    project_name = client.project_path project: project_id
    
    series = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TimeSeries.new
    series.[metric](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) = Google::Api::[Metric](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Metric.html).new type: metric_type
    
    resource = Google::Api::[MonitoredResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_usage-v1/latest/Google-Api-MonitoredResource.html).new type: "global"
    resource.labels["project_id"] = project_id
    series.[resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) = resource
    
    point = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::Point.new
    point.value = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TypedValue.new double_value: 3.14
    now = Time.now
    end_time = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i, nanos: now.nsec
    point.interval = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TimeInterval.new end_time: end_time
    series.[points](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) << point
    
    client.create_time_series name: project_name, time_series: [series]
    p "Time series created."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
