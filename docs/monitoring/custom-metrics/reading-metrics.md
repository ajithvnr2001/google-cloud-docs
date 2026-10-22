---
url: https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics/
title: Retrieve time-series data \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:26.274554+00:00
---

# Retrieve time-series data  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Retrieve time-series data Stay organized with collections  Save and categorize content based on your preferences. 

The [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method in the Monitoring API lets you retrieve, filter, and aggregate raw or processed time-series data over a specified time interval. You can invoke `timeSeries.list` by using a language-specific client library, the forms-based [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer) in the **Protocol** tabs of this document, or the Metrics Explorer.

To query metric data by using Monitoring Query Language (MQL) instead, use the [`timeSeries.query`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/query) method; see [Retrieving data with `timeSeries.query`](https://docs.cloud.google.com/monitoring/mql/qn-from-api#ql-timeseries-query).

## Overview

Each call to the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method can return any number of time series from a single metric type. For example, if you are using Compute Engine, then the `compute.googleapis.com/instance/cpu/usage_time` metric type has a separate time series for each of your VM instances. For an introduction to metrics and time series, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

You specify the time-series data that you want by providing the following information to the `timeSeries.list` method:

  * A filter expression that specifies the metric type. Optionally, the filter selects a subset of the metric's time series by specifying the resources producing the time series or specifying values for certain labels in the time series.
  * A time interval that limits how much data is returned.
  * Optionally, a specification of how to combine multiple time series to produce an aggregate summary of the data. For more information and examples, see Aggregating data.



## Time-series filters

You specify which time series to retrieve by passing a [time-series filter](https://docs.cloud.google.com/monitoring/api/v3/filters#time-series-filter) to the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method. The following lists the common filter components:

  * The filter must specify a single metric type. For example:
        
        metric.type = "compute.googleapis.com/instance/cpu/usage_time"
        

To retrieve user-defined metrics, change the `metric.type` prefix in the **filter** to `custom.googleapis.com` or another prefix if used; `external.googleapis.com` is frequently used.

  * The filter can specify values for the metric's dimension labels. The metric type determines which labels are present. For example:
        
        (metric.label.instance_name = "your-instance-id" OR
        metric.label.instance_name = "your-other-instance-id")
        

In the previous expression, `label` is correct even though the actual metric object uses `labels` as its key.

  * The filter can select only those time series that contain a specific monitored resource type:
        
        resource.type = "gce_instance"
        




The filter components can be combined into a single time-series filter, such as the following:
    
    
    metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
    (metric.label.instance_name = "your-instance-id" OR
    metric.label.instance_name = "your-other-instance-id")
    

If you don't specify values for all metric labels, then the `list` method returns a time series for each combination of values in the unspecified labels. The method returns only time series that have data.

## Time intervals

When you use the API to read data, you specify the time interval for which you want to retrieve data by setting start and end times. The API retrieves data from the interval `(start, end]`, that is, from after the start time through the end time.

The start time must be no later than the end time. If you specify a start time that is later than the end time, then the API returns an error.

If you want to retrieve only data with a specific timestamp, then set the start time equal to the end time, or equivalently, don't set the start time.

### Time format

Start and end times must be specified as strings in RFC 3339 format. For example:
    
    
    2024-03-01T12:34:56+04:00
    2024-03-01T12:34:56.992Z
    

The `date -Iseconds` command on Linux is useful for generating timestamps.

## Basic list operations

The [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method can be used to return raw data, or it can be used to return highly processed data. This section illustrates how to list the available time series and how to get the values in a specific time series.

### Example: Listing available time series

This example shows how to list only the names and descriptions of the time series that match a filter, rather than returning all the available data:

### Protocol

  1. Open the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) reference page.
  2. In the pane labeled **Try this method** , enter the following: 
     * **name** : Enter the path to your project. 
           
           projects/PROJECT_ID
           

     * **filter** : Specify the metric type. 
           
           metric.type = "compute.googleapis.com/instance/cpu/utilization"
           

     * **interval.endTime** : Enter the end time. 
     * **interval.startTime** : Enter the start time and ensure that it is 20 minutes earlier than the end time. 
     * Click **Show standard parameters** , and in the **fields** field, enter the following: 
           
           timeSeries.metric

  3. Click **Execute**.

The sample output shows time series for two different VM instances: 
    
    
    {
      "timeSeries": [
        {
          "metric": {
            "labels": {
              "instance_name": "your-first-instance"
            },
            "type": "compute.googleapis.com/instance/cpu/utilization"
          },
        },
        {
          "metric": {
            "labels": {
              "instance_name": "your-second-instance"
            },
            "type": "compute.googleapis.com/instance/cpu/utilization"
          },
        }
      ]
    }
    

To view the request as a `curl` command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer. 

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
    interval.[end_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-iam-credentials-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i,
                                                        nanos:   now.nsec
    interval.[start_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-iam-credentials-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i - 1200,
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

If you have difficulty, see [Troubleshoot the Monitoring API](https://docs.cloud.google.com/monitoring/api/troubleshooting).

### Example: Getting time-series data

This example returns the CPU utilization measurements that were recorded over a 20-minute interval for a specific Compute Engine instance. The amount of data returned depends on the sampling rate of the metric. Because the CPU utilization is sampled every minute, the result of this query is about 20 data points. When multiple data points are returned for a time series, the API returns the data points in each time series in reverse time order; there is no override for this point ordering.

### Protocol

The protocol example further limits the output, to make the returned data more manageable in the response box:

  * The **filter** value limits the time series to a single VM instance.
  * The **field** value specifies only the time and value of the
measurements. 


These settings limit the amount of time-series data returned in the result.

  1. Open the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) reference page.
  2. In the pane labeled **Try this method** , enter the following: 
     * **name** : Enter the path to your project. 
           
           projects/PROJECT_ID
           

     * **filter** : Specify the metric type. 
           
           metric.type = "compute.googleapis.com/instance/cpu/utilization" AND metric.label.instance_name = "INSTANCE_NAME"

     * **interval.endTime** : Enter the end time. 
     * **interval.startTime** : Enter the start time and ensure that it is 20 minutes earlier than the end time. 
     * Click **Show standard parameters** , and in the **fields** field, enter the following: 
           
           timeSeries.points.interval.endTime,timeSeries.points.value

  3. Click **Execute**.



The request returns a result like the following:
    
    
    {
      "timeSeries": [
      {
        "points": [
        {
          "interval": {
          "endTime": "2024-03-01T00:19:01Z"
          },
          "value": {
          "doubleValue": 0.06763074536575005
          }
        },
        {
          "interval": {
          "endTime": "2024-03-01T00:18:01Z"
          },
          "value": {
          "doubleValue": 0.06886174467702706
          }
        },
        ...
        {
          "interval": {
          "endTime": "2024-03-01T00:17:01Z"
          },
          "value": {
          "doubleValue": 0.06929610064253211
          }
        }
        ]
      }
      ]
    }
    

To view the request as a `curl` command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer. 

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
    interval.[end_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-iam-credentials-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i,
                                                        nanos:   now.nsec
    interval.[start_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-iam-credentials-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i - 1200,
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

If you have difficulty, see [Troubleshoot the Monitoring API](https://docs.cloud.google.com/monitoring/api/troubleshooting).

## Aggregating data

The [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method can perform statistical aggregations and reductions on the returned time-series data. The following sections demonstrate two examples. To learn more, see [Filtering and aggregation: manipulating time series](https://docs.cloud.google.com/monitoring/api/v3/aggregation).

### Example: Aligning time series

This example reduces the 20 individual utilization measurements in each time series to 2 measurements: the mean utilization for the two 10-minute periods within the 20-minute interval. The data from each time series is first aligned into 10-minute periods, and then the values in each 10-minute period are averaged.

The alignment operation has two advantages: it smooths out the data, and it aligns the data from all time series on exact 10-minute boundaries. The aligned data can then be processed further.

### Protocol

  1. Open the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) reference page.
  2. In the pane labeled **Try this method** , enter the following: 
     * **name** : Enter the path to your project. 
           
           projects/PROJECT_ID
           

     * **aggregation.alignmentPeriod** : Enter `600s`
     * **aggregation.perSeriesAligner** : Select `ALIGN_MEAN`
     * **filter** : Specify the metric type. 
           
           metric.type = "compute.googleapis.com/instance/cpu/utilization"
           

     * **interval.endTime** : Enter the end time. 
     * **interval.startTime** : Enter the start time and ensure that it is 20 minutes earlier than the end time. 
     * Click **Show standard parameters** , and in the **fields** field, enter the following: 
           
           timeSeries.metric,timeSeries.points
           

  3. Click **Execute**.



The filter for a single instance shown in the previous example is removed: this query returns much less data, so there is less need to restrict it to one VM instance.

The following sample result has a time series for each of three VM instances. Each time series has two data points, the mean utilization for the 10-minute alignment periods:
    
    
    {
      "timeSeries": [
      {
        "metric": {
        "labels": {"instance_name": "your-first-instance"},
        "type": "compute.googleapis.com/instance/cpu/utilization"
        },
        "points": [
        {
          "interval": {
          "startTime": "2024-03-01T00:20:00.000Z",
          "endTime": "2024-03-01T00:20:00.000Z"
          },
          "value": { "doubleValue": 0.06688481346044381 }
        },
        {
          "interval": {
          "startTime": "2024-03-01T00:10:00.000Z",
          "endTime": "2024-03-01T00:10:00.000Z"
          },
          "value": {"doubleValue": 0.06786652821310177 }
        }
        ]
      },
      {
        "metric": {
        "labels": { "instance_name": "your-second-instance" },
        "type": "compute.googleapis.com/instance/cpu/utilization"
        },
        "points": [
        {
          "interval": {
          "startTime": "2024-03-01T00:20:00.000Z",
          "endTime": "2024-03-01T00:20:00.000Z"
          },
          "value": { "doubleValue": 0.04144239874207415 }
        },
        {
          "interval": {
          "startTime": "2024-03-01T00:10:00.000Z",
          "endTime": "2024-03-01T00:10:00.000Z"
          },
          "value": { "doubleValue": 0.04045793689050091 }
        }
        ]
      },
      {
        "metric": {
        "labels": { "instance_name": "your-third-instance" },
        "type": "compute.googleapis.com/instance/cpu/utilization"
        },
        "points": [
        {
          "interval": {
          "startTime": "2024-03-01T00:20:00.000Z",
          "endTime": "2024-03-01T00:20:00.000Z"
          },
          "value": { "doubleValue": 0.029650046587339607 }
        },
        {
          "interval": {
          "startTime": "2024-03-01T00:10:00.000Z",
          "endTime": "2024-03-01T00:10:00.000Z"
          },
          "value": { "doubleValue": 0.03053874224715402 }
        }
        ]
      }
      ]
    }
    

To view the request as a `curl` command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer. 

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
    interval.[end_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-iam-credentials-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i,
                                                        nanos:   now.nsec
    interval.[start_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-iam-credentials-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i - 1200,
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
    

If you have difficulty, see [Troubleshoot the Monitoring API](https://docs.cloud.google.com/monitoring/api/troubleshooting).

### Example: Reducing across time series

This example extends the previous example by combining the aligned time series from the three VM instances into a single time series that measures the average utilization of all instances.

### Protocol

  1. Open the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) reference page.
  2. In the pane labeled **Try this method** , enter the following: 
     * **name** : Enter the path to your project. 
           
           projects/PROJECT_ID
           

     * **aggregation.alignmentPeriod** : Enter `600s`
     * **aggregation.perSeriesAligner** : Select `ALIGN_MEAN`
     * **aggregation.crossSeriesReducer** : Select `REDUCE_MEAN`
     * **filter** : Specify the metric type. 
           
           metric.type = "compute.googleapis.com/instance/cpu/utilization"
           

     * **interval.endTime** : Enter the end time. 
     * **interval.startTime** : Enter the start time and ensure that it is 20 minutes earlier than the end time. 
     * Click **Show standard parameters** , and in the **fields** field, enter the following: 
           
           timeSeries.metric,timeSeries.points
           

  3. Click **Execute**.



The following sample result has only one time series and two data points. Each point is the average of the utilization among the three VM instances during the time period:
    
    
    {
      "timeSeries": [
      {
        "metric": {
        "type": "compute.googleapis.com/instance/cpu/utilization"
        },
        "points": [
        {
          "interval": {
          "startTime": "2024-03-01T00:20:00.000Z",
          "endTime": "2024-03-01T00:20:00.000Z"
          },
          "value": {
          "doubleValue": 0.045992419596619184
          }
        },
        {
          "interval": {
          "startTime": "2024-03-01T00:10:00.000Z",
          "endTime": "2024-03-01T00:10:00.000Z"
          },
          "value": {
          "doubleValue": 0.04628773578358556
          }
        }
        ]
      }
      ]
    }
    

To view the request as a `curl` command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer. 

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object ReadTimeSeriesReduce(string projectId,
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
        // Aggregate results per matching instance.
        Aggregation aggregation = new Aggregation();
        Duration alignmentPeriod = new Duration();
        alignmentPeriod.Seconds = 600;
        aggregation.AlignmentPeriod = alignmentPeriod;
        aggregation.CrossSeriesReducer = Aggregation.Types.Reducer.ReduceMean;
        aggregation.PerSeriesAligner = Aggregation.Types.Aligner.AlignMean;
        // Add the aggregation to the request.
        request.Aggregation = aggregation;
        // Make the request.
        PagedEnumerable<ListTimeSeriesResponse, TimeSeries> response =
            metricServiceClient.ListTimeSeries(request);
        // Iterate over all response items, lazily performing RPCs as required.
        Console.WriteLine("CPU utilization:");
        foreach (var item in response)
        {
            var points = item.Points;
            Console.WriteLine("Average CPU utilization across all GCE instances:");
            Console.WriteLine($"  Last 10 min: {points[0].Value.DoubleValue}");
            Console.WriteLine($"  Last 10-20 min ago: {points[1].Value.DoubleValue}");
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
    
    // readTimeSeriesReduce reads the last 20 minutes of the given metric, aligns
    // everything on 10 minute intervals, and combines values from different
    // instances.
    func readTimeSeriesReduce(w io.Writer, projectID string) error {
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
    			CrossSeriesReducer: monitoringpb.[Aggregation_REDUCE_MEAN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/apiv3/v2/monitoringpb.html#cloud_google_com_go_monitoring_apiv3_v2_monitoringpb_Aggregation_REDUCE_NONE_Aggregation_REDUCE_MEAN_Aggregation_REDUCE_MIN_Aggregation_REDUCE_MAX_Aggregation_REDUCE_SUM_Aggregation_REDUCE_STDDEV_Aggregation_REDUCE_COUNT_Aggregation_REDUCE_COUNT_TRUE_Aggregation_REDUCE_COUNT_FALSE_Aggregation_REDUCE_FRACTION_TRUE_Aggregation_REDUCE_PERCENTILE_99_Aggregation_REDUCE_PERCENTILE_95_Aggregation_REDUCE_PERCENTILE_50_Aggregation_REDUCE_PERCENTILE_05),
    			PerSeriesAligner:   monitoringpb.[Aggregation_ALIGN_MEAN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/monitoring/latest/apiv3/v2/monitoringpb.html#cloud_google_com_go_monitoring_apiv3_v2_monitoringpb_Aggregation_ALIGN_NONE_Aggregation_ALIGN_DELTA_Aggregation_ALIGN_RATE_Aggregation_ALIGN_INTERPOLATE_Aggregation_ALIGN_NEXT_OLDER_Aggregation_ALIGN_MIN_Aggregation_ALIGN_MAX_Aggregation_ALIGN_MEAN_Aggregation_ALIGN_COUNT_Aggregation_ALIGN_SUM_Aggregation_ALIGN_STDDEV_Aggregation_ALIGN_COUNT_TRUE_Aggregation_ALIGN_COUNT_FALSE_Aggregation_ALIGN_FRACTION_TRUE_Aggregation_ALIGN_PERCENTILE_99_Aggregation_ALIGN_PERCENTILE_95_Aggregation_ALIGN_PERCENTILE_50_Aggregation_ALIGN_PERCENTILE_05_Aggregation_ALIGN_PERCENT_CHANGE),
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
    		fmt.Fprintln(w, "Average CPU utilization across all GCE instances:")
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
            .setCrossSeriesReducer(Aggregation.Reducer.REDUCE_MEAN)
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
    
    async function readTimeSeriesReduce() {
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
          crossSeriesReducer: 'REDUCE_MEAN',
          perSeriesAligner: 'ALIGN_MEAN',
        },
      };
    
      // Writes time series data
      const [result] = await client.listTimeSeries(request);
      if (result.length === 0) {
        console.log('No data');
        return;
      }
      const reductions = result[0].points;
    
      console.log('Average CPU utilization across all GCE instances:');
      console.log(`  Last 10 min: ${reductions[0].value.doubleValue}`);
      console.log(`  10-20 min ago: ${reductions[0].value.doubleValue}`);
    }
    readTimeSeriesReduce();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Aggregation;
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\ListTimeSeriesRequest;
    use Google\Cloud\Monitoring\V3\ListTimeSeriesRequest\TimeSeriesView;
    use Google\Cloud\Monitoring\V3\TimeInterval;
    use Google\Protobuf\Duration;
    use Google\Protobuf\Timestamp;
    
    /**
     * Example:
     * ```
     * read_timeseries_reduce($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function read_timeseries_reduce(string $projectId, int $minutesAgo = 20): void
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
        $aggregation->setCrossSeriesReducer(Aggregation\Reducer::REDUCE_MEAN);
        $aggregation->setPerSeriesAligner(Aggregation\Aligner::ALIGN_MEAN);
    
        $view = TimeSeriesView::FULL;
        $listTimeSeriesRequest = (new ListTimeSeriesRequest())
            ->setName($projectName)
            ->setFilter($filter)
            ->setInterval($interval)
            ->setView($view)
            ->setAggregation($aggregation);
    
        $result = $metrics->listTimeSeries($listTimeSeriesRequest);
    
        printf('Average CPU utilization across all GCE instances:' . PHP_EOL);
        if ($timeSeries = $result->iterateAllElements()->current()) {
            $reductions = $timeSeries->getPoints();
            printf('  Last 10 minutes: ');
            printf($reductions[0]->getValue()->getDoubleValue() . PHP_EOL);
            if (count($reductions) > 1) {
                printf('  10-20 minutes ago: ');
                printf($reductions[1]->getValue()->getDoubleValue() . PHP_EOL);
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
            "cross_series_reducer": [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).Aggregation.Reducer.REDUCE_MEAN,
            "group_by_fields": ["resource.zone"],
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
    interval.[end_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-iam-credentials-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i,
                                                        nanos:   now.nsec
    interval.[start_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeInterval.html) = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-iam-credentials-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i - 1200,
                                                          nanos:   now.nsec
    filter = 'metric.type = "compute.googleapis.com/instance/cpu/utilization"'
    view = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::ListTimeSeriesRequest::TimeSeriesView::FULL
    aggregation = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::Aggregation.new(
      alignment_period:     { seconds: 1200 },
      per_series_aligner:   Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::Aggregation::Aligner::ALIGN_MEAN,
      cross_series_reducer: Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::Aggregation::Reducer::REDUCE_MEAN,
      group_by_fields:      ["resource.zone"]
    )
    
    results = client.list_time_series name:        project_name,
                                      filter:      filter,
                                      interval:    interval,
                                      view:        view,
                                      aggregation: aggregation
    results.each do |result|
      p result
    end
    

If you have difficulty, see [Troubleshoot the Monitoring API](https://docs.cloud.google.com/monitoring/api/troubleshooting).

## What's next

  * Learn about [Retention and latency of metric data](https://docs.cloud.google.com/monitoring/api/v3/latency-n-retention).
  * Learn about [Filtering and aggregation: manipulating time series](https://docs.cloud.google.com/monitoring/api/v3/aggregation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
