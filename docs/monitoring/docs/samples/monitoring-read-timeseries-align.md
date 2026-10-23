---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-read-timeseries-align/
title: Read metric data aligned by mean \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:19.067282+00:00
---

# Read metric data aligned by mean  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-read-timeseries-align/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Read metric data aligned by mean Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to read time series data aligned by mean.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object ReadTimeSeriesAggregate(string projectId,
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
        // Aggregate results per matching instance
        Aggregation aggregation = new Aggregation();
        Duration alignmentPeriod = new Duration();
        alignmentPeriod.Seconds = 600;
        aggregation.AlignmentPeriod = alignmentPeriod;
        aggregation.PerSeriesAligner = Aggregation.Types.Aligner.AlignMean;
        // Add the aggregation to the request.
        request.Aggregation = aggregation;
        // Make the request.
        PagedEnumerable<ListTimeSeriesResponse, TimeSeries> response =
            metricServiceClient.ListTimeSeries(request);
        // Iterate over all response items, lazily performing RPCs as required.
        Console.WriteLine($"{projectId} CPU utilization:");
        foreach (var item in response)
        {
            var points = item.Points;
            var labels = item.Metric.Labels;
            Console.WriteLine($"{labels.Values.FirstOrDefault()}");
            if (points.Count > 0)
            {
                Console.WriteLine($"  Now: {points[0].Value.DoubleValue}");
            }
            if (points.Count > 1)
            {
                Console.WriteLine($"  10 min ago: {points[1].Value.DoubleValue}");
            }
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
    	"github.com/golang/protobuf/ptypes/duration"
    	"github.com/golang/protobuf/ptypes/timestamp"
    	"google.golang.org/api/iterator"
    )
    
    // readTimeSeriesAlign reads the last 20 minutes of the given metric and aligns
    // everything on 10 minute intervals.
    func readTimeSeriesAlign(w io.Writer, projectID string) error {
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
    		Aggregation: &monitoringpb.Aggregation{
    			PerSeriesAligner: monitoringpb.[Aggregation_ALIGN_MEAN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/apiv3/v2/monitoringpb.html#cloud_google_com_go_monitoring_apiv3_v2_monitoringpb_Aggregation_ALIGN_NONE_Aggregation_ALIGN_DELTA_Aggregation_ALIGN_RATE_Aggregation_ALIGN_INTERPOLATE_Aggregation_ALIGN_NEXT_OLDER_Aggregation_ALIGN_MIN_Aggregation_ALIGN_MAX_Aggregation_ALIGN_MEAN_Aggregation_ALIGN_COUNT_Aggregation_ALIGN_SUM_Aggregation_ALIGN_STDDEV_Aggregation_ALIGN_COUNT_TRUE_Aggregation_ALIGN_COUNT_FALSE_Aggregation_ALIGN_FRACTION_TRUE_Aggregation_ALIGN_PERCENTILE_99_Aggregation_ALIGN_PERCENTILE_95_Aggregation_ALIGN_PERCENTILE_50_Aggregation_ALIGN_PERCENTILE_05_Aggregation_ALIGN_PERCENT_CHANGE),
    			AlignmentPeriod: &duration.Duration{
    				Seconds: 600,
    			},
    		},
    	}
    	it := client.ListTimeSeries(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("could not read time series value: %w", err)
    		}
    		fmt.Fprintln(w, resp.GetMetric().GetLabels()["instance_name"])
    		fmt.Fprintf(w, "\tNow: %.4f\n", resp.GetPoints()[0].GetValue().GetDoubleValue())
    		if len(resp.GetPoints()) > 1 {
    			fmt.Fprintf(w, "\t10 minutes ago: %.4f\n", resp.GetPoints()[1].GetValue().GetDoubleValue())
    		}
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
    
    Aggregation aggregation =
        Aggregation.newBuilder()
            .setAlignmentPeriod(Duration.newBuilder().setSeconds(600).build())
            .setPerSeriesAligner(Aggregation.Aligner.ALIGN_MEAN)
            .build();
    
    ListTimeSeriesRequest.Builder requestBuilder =
        ListTimeSeriesRequest.newBuilder()
            .setName(name.toString())
            .setFilter("metric.type=\"compute.googleapis.com/instance/cpu/utilization\"")
            .setInterval(interval)
            .setAggregation(aggregation);
    
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
    
    async function readTimeSeriesAggregate() {
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
        // Aggregate results per matching instance
        aggregation: {
          alignmentPeriod: {
            seconds: 600,
          },
          perSeriesAligner: 'ALIGN_MEAN',
        },
      };
    
      // Writes time series data
      const [timeSeries] = await client.listTimeSeries(request);
      console.log('CPU utilization:');
      timeSeries.forEach(data => {
        console.log(data.metric.labels.instance_name);
        console.log(`  Now: ${data.points[0].value.doubleValue}`);
        if (data.points.length > 1) {
          console.log(`  10 min ago: ${data.points[1].value.doubleValue}`);
        }
        console.log('=====');
      });
    }
    readTimeSeriesAggregate();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Aggregation;
    use Google\Cloud\Monitoring\V3\Aggregation\Aligner;
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\ListTimeSeriesRequest;
    use Google\Cloud\Monitoring\V3\ListTimeSeriesRequest\TimeSeriesView;
    use Google\Cloud\Monitoring\V3\TimeInterval;
    use Google\Protobuf\Duration;
    use Google\Protobuf\Timestamp;
    
    /**
     * Example:
     * ```
     * read_timeseries_align($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function read_timeseries_align(string $projectId, int $minutesAgo = 20): void
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
    
        $alignmentPeriod = new Duration();
        $alignmentPeriod->setSeconds(600);
        $aggregation = new Aggregation();
        $aggregation->setAlignmentPeriod($alignmentPeriod);
        $aggregation->setPerSeriesAligner(Aligner::ALIGN_MEAN);
    
        $view = TimeSeriesView::FULL;
        $listTimeSeriesRequest = (new ListTimeSeriesRequest())
            ->setName($projectName)
            ->setFilter($filter)
            ->setInterval($interval)
            ->setView($view)
            ->setAggregation($aggregation);
    
        $result = $metrics->listTimeSeries($listTimeSeriesRequest);
    
        printf('CPU utilization:' . PHP_EOL);
        foreach ($result->iterateAllElements() as $timeSeries) {
            printf($timeSeries->getMetric()->getLabels()['instance_name'] . PHP_EOL);
            printf('  Now: ');
            printf($timeSeries->getPoints()[0]->getValue()->getDoubleValue() . PHP_EOL);
            if (count($timeSeries->getPoints()) > 1) {
                printf('  10 minutes ago: ');
                printf($timeSeries->getPoints()[1]->getValue()->getDoubleValue() . PHP_EOL);
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
            "start_time": {"seconds": (seconds - 3600), "nanos": nanos},
        }
    )
    aggregation = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).Aggregation(
        {
            "alignment_period": {"seconds": 1200},  # 20 minutes
            "per_series_aligner": [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).Aggregation.Aligner.ALIGN_MEAN,
        }
    )
    
    results = client.[list_time_series](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_list_time_series)(
        request={
            "name": project_name,
            "filter": 'metric.type = "compute.googleapis.com/instance/cpu/utilization"',
            "interval": interval,
            "view": [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ListTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest.html).[TimeSeriesView](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest.TimeSeriesView.html).FULL,
            "aggregation": aggregation,
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
    aggregation = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::Aggregation.new(
      alignment_period:   { seconds: 1200 },
      per_series_aligner: Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::Aggregation::Aligner::ALIGN_MEAN
    )
    
    results = client.list_time_series name:        project_name,
                                      filter:      filter,
                                      interval:    interval,
                                      view:        view,
                                      aggregation: aggregation
    results.each do |result|
      p result
    end
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
