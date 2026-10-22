---
url: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-custom-metrics-direct-exporter/
title: Custom metrics exporter source code \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:30.362400+00:00
---

# Custom metrics exporter source code  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-custom-metrics-direct-exporter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/kubernetes-engine/docs/samples)



#  Custom metrics exporter source code Stay organized with collections  Save and categorize content based on your preferences. 

Source code for custom Cloud Monitoring exporter. 

## Code sample

### Go

To authenticate to GKE, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func exportMetric(client *monitoring.MetricClient, metricName string,
    	metricValue int64, metricLabels map[string]string, monitoredResource string, resourceLabels map[string]string) error {
    	dataPoint := &monitoringpb.Point{
    		Interval: &monitoringpb.TimeInterval{
    			EndTime: timestamppb.New(time.Now()),
    		},
    		Value: &monitoringpb.TypedValue{
    			Value: &monitoringpb.TypedValue_Int64Value{Int64Value: metricValue},
    		},
    	}
    	// Write time series data.
    	projectName := fmt.Sprintf("projects/%s", resourceLabels["project_id"])
    	request := &monitoringpb.CreateTimeSeriesRequest{
    		Name: projectName,
    		TimeSeries: []*monitoringpb.TimeSeries{
    			{
    				Metric: &metric.Metric{
    					Type:   "custom.googleapis.com/" + metricName,
    					Labels: metricLabels,
    				},
    				Resource: &monitoredres.MonitoredResource{
    					Type:   monitoredResource,
    					Labels: resourceLabels,
    				},
    				Points: []*monitoringpb.Point{
    					dataPoint,
    				},
    			},
    		},
    	}
    	err := client.CreateTimeSeries(context.Background(), request)
    	return err
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=container). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
