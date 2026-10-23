---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-read-timeseries-simple/
title: Read metric data \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:29.428229+00:00
---

# Read metric data  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-read-timeseries-simple/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Read metric data Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to read time series data.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics)
  * [View metrics and quotas](https://docs.cloud.google.com/functions/1stgendocs/monitoring/metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object ReadTimeSeriesData(string projectId,
        string metricType = "compute.googleapis.com/instance/cpu/utilization")
    {
        // Create client.
        MetricServiceClient metricServiceClient = MetricServiceClient.Create();
        // Initialize request argument(s).
        string filter = $"metric.type=\"{metricType}\"";
        ListTimeSeriesRequest request = new ListTimeSeriesRequest
        {
            ProjectName = new ProjectName(projectId),
            Filter = filter,
            Interval = new TimeInterval(),
            View = ListTimeSeriesRequest.Types.TimeSeriesView.Full,
        };
        // Create timestamp for current time formatted in seconds.
        long timeStamp = (long)(DateTime.UtcNow - s_unixEpoch).TotalSeconds;
        Timestamp startTimeStamp = new Timestamp();
        // Set startTime to limit results to the last 20 minutes.
        startTimeStamp.Seconds = timeStamp - (60 * 20);
        Timestamp endTimeStamp = new Timestamp();
        // Set endTime to current time.
        endTimeStamp.Seconds = timeStamp;
        TimeInterval interval = new TimeInterval();
        interval.StartTime = startTimeStamp;
        interval.EndTime = endTimeStamp;
        request.Interval = interval;
        // Make the request.
        PagedEnumerable<ListTimeSeriesResponse, TimeSeries> response =
            metricServiceClient.ListTimeSeries(request);
        // Iterate over all response items, lazily performing RPCs as required.
        foreach (TimeSeries item in response)
        {
            Console.WriteLine(JObject.Parse($"{item}").ToString());
        }
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // readTimeSeriesValue reads the TimeSeries for the value specified by metric type in a time window from the last 20 minutes.
    func readTimeSeriesValue(projectID, metricType string) error {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer c.Close()
    	startTime := time.Now().UTC().Add(time.Minute * -20).Unix()
    	endTime := time.Now().UTC().Unix()
    
    	req := &monitoringpb.ListTimeSeriesRequest{
    		Name:   "projects/" + projectID,
    		Filter: fmt.Sprintf("metric.type=\"%s\"", metricType),
    		Interval: &monitoringpb.TimeInterval{
    			StartTime: &timestamp.Timestamp{Seconds: startTime},
    			EndTime:   &timestamp.Timestamp{Seconds: endTime},
    		},
    	}
    	iter := c.ListTimeSeries(ctx, req)
    
    	for {
    		resp, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("could not read time series value, %w ", err)
    		}
    		log.Printf("%+v\n", resp)
    	}
    
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    String projectId = System.getProperty("projectId");
    ProjectName name = ProjectName.of(projectId);
    
    // Restrict time to last 20 minutes
    long startMillis = System.currentTimeMillis() - ((60 * 20) * 1000);
    TimeInterval interval =
        TimeInterval.newBuilder()
            .setStartTime(Timestamps.fromMillis(startMillis))
            .setEndTime(Timestamps.fromMillis(System.currentTimeMillis()))
            .build();
    
    ListTimeSeriesRequest.Builder requestBuilder =
        ListTimeSeriesRequest.newBuilder()
            .setName(name.toString())
            .setFilter(filter)
            .setInterval(interval);
    
    ListTimeSeriesRequest request = requestBuilder.build();
    
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      ListTimeSeriesPagedResponse response = client.listTimeSeries(request);
    
      System.out.println("Got timeseries: ");
      for (TimeSeries ts : response.iterateAll()) {
        System.out.println(ts);
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function readTimeSeriesData() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const filter = 'metric.type="compute.googleapis.com/instance/cpu/utilization"';
    
      const request = {
        name: client.projectPath(projectId),
        filter: filter,
        interval: {
          startTime: {
            // Limit results to the last 20 minutes
            seconds: Date.now() / 1000 - 60 * 20,
          },
          endTime: {
            seconds: Date.now() / 1000,
          },
        },
      };
    
      // Writes time series data
      const [timeSeries] = await client.listTimeSeries(request);
      timeSeries.forEach(data => {
        console.log(`${data.metric.labels.instance_name}:`);
        data.points.forEach(point => {
          console.log(JSON.stringify(point.value));
        });
      });
    }
    readTimeSeriesData();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\ListTimeSeriesRequest;
    use Google\Cloud\Monitoring\V3\ListTimeSeriesRequest\TimeSeriesView;
    use Google\Cloud\Monitoring\V3\TimeInterval;
    use Google\Protobuf\Timestamp;
    
    /**
     * Example:
     * ```
     * read_timeseries_simple($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function read_timeseries_simple(string $projectId, int $minutesAgo = 20): void
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $projectName = 'projects/' . $projectId;
        $filter = 'metric.type="compute.googleapis.com/instance/cpu/utilization"';
    
        // Limit results to the last 20 minutes
        $startTime = new Timestamp();
        $startTime->setSeconds(time() - (60 * $minutesAgo));
        $endTime = new Timestamp();
        $endTime->setSeconds(time());
    
        $interval = new TimeInterval();
        $interval->setStartTime($startTime);
        $interval->setEndTime($endTime);
    
        $view = TimeSeriesView::FULL;
        $listTimeSeriesRequest = (new ListTimeSeriesRequest())
            ->setName($projectName)
            ->setFilter($filter)
            ->setInterval($interval)
            ->setView($view);
    
        $result = $metrics->listTimeSeries($listTimeSeriesRequest);
    
        printf('CPU utilization:' . PHP_EOL);
        foreach ($result->iterateAllElements() as $timeSeries) {
            $instanceName = $timeSeries->getMetric()->getLabels()['instance_name'];
            printf($instanceName . ':' . PHP_EOL);
            foreach ($timeSeries->getPoints() as $point) {
                printf('  ' . $point->getValue()->getDoubleValue() . PHP_EOL);
            }
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    project_name = f"projects/{project_id}"
    
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[TimeInterval](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeInterval.html)(
        {
            "end_time": {"seconds": seconds, "nanos": nanos},
            "start_time": {"seconds": (seconds - 1200), "nanos": nanos},
        }
    )
    
    results = client.[list_time_series](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_list_time_series)(
        request={
            "name": project_name,
            "filter": 'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
            "interval": interval,
            "view": [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ListTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest.html).[TimeSeriesView](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest.TimeSeriesView.html).FULL,
        }
    )
    for result in results:
        print(result)

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    project_name = client.project_path project: project_id
    
    interval = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TimeInterval.new
    now = Time.now
    interval.[end_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i,
                                                        nanos:   now.nsec
    interval.[start_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataqna-v1alpha/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i - 1200,
                                                          nanos:   now.nsec
    filter = 'metric.type = "compute.googleapis.com/instance/cpu/utilization"'
    view = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::ListTimeSeriesRequest::TimeSeriesView::FULL
    
    results = client.list_time_series name:     project_name,
                                      filter:   filter,
                                      interval: interval,
                                      view:     view
    results.each do |result|
      p result
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
