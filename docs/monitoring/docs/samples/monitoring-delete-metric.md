---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-delete-metric/
title: Delete a custom metric \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:54.259155+00:00
---

# Delete a custom metric  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-delete-metric/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Delete a custom metric Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to delete a custom metric.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create user-defined metrics with the API](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object DeleteMetric(string projectId, string metricType)
    {
        // Create client.
        MetricServiceClient metricServiceClient = MetricServiceClient.Create();
        // Initialize request argument(s).
        MetricDescriptorName name = new MetricDescriptorName(projectId, metricType);
        // Make the request.
        metricServiceClient.DeleteMetricDescriptor(name);
        Console.WriteLine($"Done deleting metric descriptor: {name}");
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
    
    // deleteMetric deletes the given metric. name should be of the form
    // "projects/PROJECT_ID/metricDescriptors/METRIC_TYPE".
    func deleteMetric(w io.Writer, name string) error {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer c.Close()
    	req := &monitoringpb.DeleteMetricDescriptorRequest{
    		Name: name,
    	}
    
    	if err := c.DeleteMetricDescriptor(ctx, req); err != nil {
    		return fmt.Errorf("could not delete metric: %w", err)
    	}
    	fmt.Fprintf(w, "Deleted metric: %q\n", name)
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    final String projectId = System.getProperty("projectId");
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      MetricDescriptorName metricName = MetricDescriptorName.of(projectId, type);
      client.deleteMetricDescriptor(metricName);
      System.out.println("Deleted descriptor " + type);
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function deleteMetricDescriptor() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const metricId = 'custom.googleapis.com/stores/daily_sales';
    
      const request = {
        name: client.[projectMetricDescriptorPath](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/v3.metricserviceclient.html)(projectId, metricId),
      };
    
      // Deletes a metric descriptor
      const [result] = await client.deleteMetricDescriptor(request);
      console.log(`Deleted ${metricId}`, result);
    }
    deleteMetricDescriptor();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\DeleteMetricDescriptorRequest;
    
    /**
     * Example:
     * ```
     * delete_metric($projectId, $databaseId);
     * ```
     *
     * @param string $projectId Your project ID
     * @param string $metricId  The ID of the Metric Descriptor to delete
     */
    function delete_metric($projectId, $metricId)
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $metricPath = $metrics->metricDescriptorName($projectId, $metricId);
        $deleteMetricDescriptorRequest = (new DeleteMetricDescriptorRequest())
            ->setName($metricPath);
        $metrics->deleteMetricDescriptor($deleteMetricDescriptorRequest);
    
        printf('Deleted a metric: ' . $metricPath . PHP_EOL);
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    client.[delete_metric_descriptor](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_delete_metric_descriptor)(name=descriptor_name)
    print("Deleted metric descriptor {}.".format(descriptor_name))

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    # Example metric type
    # metric_type = "custom.googleapis.com/my_metric"
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    metric_name = client.[metric_descriptor_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Paths.html) project:           project_id,
                                                metric_descriptor: metric_type
    
    client.delete_metric_descriptor name: metric_name
    p "Deleted metric descriptor #{metric_name}."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
