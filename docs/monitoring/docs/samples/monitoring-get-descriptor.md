---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-get-descriptor/
title: Get a metric descriptor \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:40.126301+00:00
---

# Get a metric descriptor  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-get-descriptor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Get a metric descriptor Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to get the details of a metric descriptor.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List metric and resource types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object GetMetricDetails(string projectId, string metricType)
    {
        MetricServiceClient client = MetricServiceClient.Create();
        MetricDescriptorName name = new MetricDescriptorName(projectId, metricType);
        try
        {
            var response = client.GetMetricDescriptor(name);
            string metric = JObject.Parse($"{response}").ToString();
            Console.WriteLine($"{ metric }");
        }
        catch (Grpc.Core.RpcException ex)
            when (ex.Status.StatusCode == Grpc.Core.StatusCode.NotFound)
        { }
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	monitoring "cloud.google.com/go/monitoring/apiv3"
    	"cloud.google.com/go/monitoring/apiv3/v2/monitoringpb"
    )
    
    // getMetricDescriptor gets the descriptor for the given metricType and prints
    // information about it. metricType is the type of the metric, for example
    // compute.googleapis.com/firewall/dropped_packets_count.
    func getMetricDescriptor(w io.Writer, projectID, metricType string) error {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewMetricClient: %w", err)
    	}
    	defer c.Close()
    	req := &monitoringpb.GetMetricDescriptorRequest{
    		Name: fmt.Sprintf("projects/%s/metricDescriptors/%s", projectID, metricType),
    	}
    	resp, err := c.GetMetricDescriptor(ctx, req)
    	if err != nil {
    		return fmt.Errorf("could not get custom metric: %w", err)
    	}
    
    	fmt.Fprintf(w, "Name: %v\n", resp.GetName())
    	fmt.Fprintf(w, "Description: %v\n", resp.GetDescription())
    	fmt.Fprintf(w, "Type: %v\n", resp.GetType())
    	fmt.Fprintf(w, "Metric Kind: %v\n", resp.GetMetricKind())
    	fmt.Fprintf(w, "Value Type: %v\n", resp.GetValueType())
    	fmt.Fprintf(w, "Unit: %v\n", resp.GetUnit())
    	fmt.Fprintf(w, "Labels:\n")
    	for _, l := range resp.GetLabels() {
    		fmt.Fprintf(w, "\t%s (%s) - %s", l.GetKey(), l.GetValueType(), l.GetDescription())
    	}
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Your Google Cloud Platform project ID
    final String projectId = System.getProperty("projectId");
    
    MetricDescriptorName descriptorName = MetricDescriptorName.of(projectId, type);
    
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      MetricDescriptor response = client.getMetricDescriptor(descriptorName);
    
      System.out.println("Printing metrics descriptor: " + response);
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function getMetricDescriptor() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const metricId = 'custom.googleapis.com/your/id';
    
      const request = {
        name: client.[projectMetricDescriptorPath](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/v3.metricserviceclient.html)(projectId, metricId),
      };
    
      // Retrieves a metric descriptor
      const [descriptor] = await client.getMetricDescriptor(request);
      console.log(`Name: ${descriptor.displayName}`);
      console.log(`Description: ${descriptor.description}`);
      console.log(`Type: ${descriptor.type}`);
      console.log(`Kind: ${descriptor.metricKind}`);
      console.log(`Value Type: ${descriptor.valueType}`);
      console.log(`Unit: ${descriptor.unit}`);
      console.log('Labels:');
      descriptor.labels.forEach(label => {
        console.log(`  ${label.key} (${label.valueType}) - ${label.description}`);
      });
    }
    getMetricDescriptor();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\GetMetricDescriptorRequest;
    
    /**
     * Example:
     * ```
     * get_descriptor($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     * @param string $metricId  The ID of the Metric Descriptor to get
     */
    function get_descriptor($projectId, $metricId)
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $metricName = $metrics->metricDescriptorName($projectId, $metricId);
        $getMetricDescriptorRequest = (new GetMetricDescriptorRequest())
            ->setName($metricName);
        $descriptor = $metrics->getMetricDescriptor($getMetricDescriptorRequest);
    
        printf('Name: ' . $descriptor->getDisplayName() . PHP_EOL);
        printf('Description: ' . $descriptor->getDescription() . PHP_EOL);
        printf('Type: ' . $descriptor->getType() . PHP_EOL);
        printf('Metric Kind: ' . $descriptor->getMetricKind() . PHP_EOL);
        printf('Value Type: ' . $descriptor->getValueType() . PHP_EOL);
        printf('Unit: ' . $descriptor->getUnit() . PHP_EOL);
        printf('Labels:' . PHP_EOL);
        foreach ($descriptor->getLabels() as $labels) {
            printf('  %s (%s) - %s' . PHP_EOL,
                $labels->getKey(),
                $labels->getValueType(),
                $labels->getDescription());
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    descriptor = client.[get_metric_descriptor](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_get_metric_descriptor)(name=metric_name)
    pprint.pprint(descriptor)

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    # Example metric type
    # metric_type = "custom.googleapis.com/my_metric"
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    metric_name = client.[metric_descriptor_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Paths.html) project:           project_id,
                                                metric_descriptor: metric_type
    
    descriptor = client.get_metric_descriptor name: metric_name
    p descriptor

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
