---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-read-timeseries-fields/
title: List VM instances generating metric data \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:30.093171+00:00
---

# List VM instances generating metric data  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-read-timeseries-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  List VM instances generating metric data Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list VMs that have time series data that match a given filter.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object ReadTimeSeriesFields(string projectId,
        string metricType = "compute.googleapis.com/instance/cpu/utilization")
    {
        Console.WriteLine($"metricType{ metricType}");
        // Create client.
        MetricServiceClient metricServiceClient = MetricServiceClient.Create();
        // Initialize request argument(s).
        string filter = $"metric.type=\"{metricType}\"";
        ListTimeSeriesRequest request = new ListTimeSeriesRequest
        {
            ProjectName = new ProjectName(projectId),
            Filter = filter,
            Interval = new TimeInterval(),
            View = ListTimeSeriesRequest.Types.TimeSeriesView.Headers,
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
        Console.Write("Found data points for the following instances:");
        foreach (var item in response)
        {
            Console.WriteLine(JObject.Parse($"{item}").ToString());
        }
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	monitoring "cloud.google.com/go/monitoring/apiv3"
    	"cloud.google.com/go/monitoring/apiv3/v2/monitoringpb"
    	"github.com/golang/protobuf/ptypes/timestamp"
    	"google.golang.org/api/iterator"
    )
    
    // readTimeSeriesFields reads the last 20 minutes of the given metric, aligns
    // everything on 10 minute intervals, and combines values from different
    // instances.
    func readTimeSeriesFields(w io.Writer, projectID string) error {
    	ctx := context.Background()
    	client, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewMetricClient: %w", err)
    	}
    	defer client.Close()
    	startTime := time.Now().UTC().Add(time.Minute * -20)
    	endTime := time.Now().UTC()
    	req := &monitoringpb.ListTimeSeriesRequest{
    		Name:   "projects/" + projectID,
    		Filter: `metric.type="compute.googleapis.com/instance/cpu/utilization"`,
    		Interval: &monitoringpb.TimeInterval{
    			StartTime: &timestamp.Timestamp{
    				Seconds: startTime.Unix(),
    			},
    			EndTime: &timestamp.Timestamp{
    				Seconds: endTime.Unix(),
    			},
    		},
    		View: monitoringpb.[ListTimeSeriesRequest_HEADERS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/apiv3/v2/monitoringpb.html#cloud_google_com_go_monitoring_apiv3_v2_monitoringpb_ListTimeSeriesRequest_FULL_ListTimeSeriesRequest_HEADERS),
    	}
    	fmt.Fprintln(w, "Found data points for the following instances:")
    	it := client.ListTimeSeries(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("could not read time series value: %w", err)
    		}
    		fmt.Fprintf(w, "\t%v\n", resp.GetMetric().GetLabels()["instance_name"])
    	}
    	fmt.Fprintln(w, "Done")
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
            .setFilter("metric.type=\"compute.googleapis.com/instance/cpu/utilization\"")
            .setInterval(interval)
            .setView(ListTimeSeriesRequest.TimeSeriesView.HEADERS);
    
    ListTimeSeriesRequest request = requestBuilder.build();
    
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      ListTimeSeriesPagedResponse response = client.listTimeSeries(request);
      System.out.println("Got timeseries headers: ");
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
    
    async function readTimeSeriesFields() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
    
      const request = {
        name: client.projectPath(projectId),
        filter: 'metric.type="compute.googleapis.com/instance/cpu/utilization"',
        interval: {
          startTime: {
            // Limit results to the last 20 minutes
            seconds: Date.now() / 1000 - 60 * 20,
          },
          endTime: {
            seconds: Date.now() / 1000,
          },
        },
        // Don't return time series data, instead just return information about
        // the metrics that match the filter
        view: '[HEADERS](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.listtimeseriesrequest.timeseriesview.html)',
      };
    
      // Writes time series data
      const [timeSeries] = await client.listTimeSeries(request);
      console.log('Found data points for the following instances:');
      timeSeries.forEach(data => {
        console.log(data.metric.labels.instance_name);
      });
    }
    readTimeSeriesFields();

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
     * read_timeseries_fields($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function read_timeseries_fields(string $projectId, int $minutesAgo = 20): void
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $projectName = 'projects/' . $projectId;
        $filter = 'metric.type="compute.googleapis.com/instance/cpu/utilization"';
    
        $startTime = new Timestamp();
        $startTime->setSeconds(time() - (60 * $minutesAgo));
        $endTime = new Timestamp();
        $endTime->setSeconds(time());
    
        $interval = new TimeInterval();
        $interval->setStartTime($startTime);
        $interval->setEndTime($endTime);
    
        $view = TimeSeriesView::HEADERS;
        $listTimeSeriesRequest = (new ListTimeSeriesRequest())
            ->setName($projectName)
            ->setFilter($filter)
            ->setInterval($interval)
            ->setView($view);
    
        $result = $metrics->listTimeSeries($listTimeSeriesRequest);
    
        printf('Found data points for the following instances:' . PHP_EOL);
        foreach ($result->iterateAllElements() as $timeSeries) {
            printf($timeSeries->getMetric()->getLabels()['instance_name'] . PHP_EOL);
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
            "view": [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ListTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest.html).[TimeSeriesView](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest.TimeSeriesView.html).HEADERS,
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
    view = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::ListTimeSeriesRequest::TimeSeriesView::HEADERS
    
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
