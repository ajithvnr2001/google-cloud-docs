---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-get-resource/
title: Get a monitored resource \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:55.209004+00:00
---

# Get a monitored resource  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-get-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Get a monitored resource Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to get the details of a monitored resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List metric and resource types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object GetMonitoredResource(string projectId, string resourceId)
    {
        MetricServiceClient client = MetricServiceClient.Create();
        MonitoredResourceDescriptorName name = new MonitoredResourceDescriptorName(projectId, resourceId);
        var response = client.GetMonitoredResourceDescriptor(name);
        string resource = JObject.Parse($"{response}").ToString();
        Console.WriteLine($"{ resource }");
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
    
    // getMonitoredResource gets the descriptor for the given resourceType and
    // prints information about it. resource should be of the form
    // "projects/[PROJECT_ID]/monitoredResourceDescriptors/[RESOURCE_TYPE]".
    func getMonitoredResource(w io.Writer, resource string) error {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewMetricClient: %w", err)
    	}
    	defer c.Close()
    	req := &monitoringpb.GetMonitoredResourceDescriptorRequest{
    		Name: resource,
    	}
    	resp, err := c.GetMonitoredResourceDescriptor(ctx, req)
    	if err != nil {
    		return fmt.Errorf("could not get custom metric: %w", err)
    	}
    
    	fmt.Fprintf(w, "Name: %v\n", resp.GetName())
    	fmt.Fprintf(w, "Description: %v\n", resp.GetDescription())
    	fmt.Fprintf(w, "Type: %v\n", resp.GetType())
    	fmt.Fprintf(w, "Labels:\n")
    	for _, l := range resp.GetLabels() {
    		fmt.Fprintf(w, "\t%s (%s) - %s", l.GetKey(), l.GetValueType(), l.GetDescription())
    	}
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    void getMonitoredResource(String resourceId) throws IOException {
      String projectId = System.getProperty("projectId");
    
      try (final MetricServiceClient client = MetricServiceClient.create();) {
        MonitoredResourceDescriptorName name =
            MonitoredResourceDescriptorName.of(projectId, resourceId);
        MonitoredResourceDescriptor response = client.getMonitoredResourceDescriptor(name);
        System.out.println("Retrieved Monitored Resource: " + gson.toJson(response));
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function getMonitoredResourceDescriptor() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
      // const resourceType = 'some_resource_type, e.g. cloudsql_database';
    
      const request = {
        name: client.[projectMonitoredResourceDescriptorPath](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/v3.metricserviceclient.html)(
          projectId,
          resourceType
        ),
      };
    
      // Lists monitored resource descriptors
      const [descriptor] = await client.getMonitoredResourceDescriptor(request);
    
      console.log(`Name: ${descriptor.displayName}`);
      console.log(`Description: ${descriptor.description}`);
      console.log(`Type: ${descriptor.type}`);
      console.log('Labels:');
      descriptor.labels.forEach(label => {
        console.log(`  ${label.key} (${label.valueType}) - ${label.description}`);
      });
    }
    getMonitoredResourceDescriptor();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\GetMonitoredResourceDescriptorRequest;
    
    /**
     * Example:
     * ```
     * get_resource('your-project-id', 'gcs_bucket');
     * ```
     *
     * @param string $projectId Your project ID
     * @param string $resourceType The resource type of the monitored resource.
     */
    function get_resource($projectId, $resourceType)
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $metricName = $metrics->monitoredResourceDescriptorName($projectId, $resourceType);
        $getMonitoredResourceDescriptorRequest = (new GetMonitoredResourceDescriptorRequest())
            ->setName($metricName);
        $resource = $metrics->getMonitoredResourceDescriptor($getMonitoredResourceDescriptorRequest);
    
        printf('Name: %s' . PHP_EOL, $resource->getName());
        printf('Type: %s' . PHP_EOL, $resource->getType());
        printf('Display Name: %s' . PHP_EOL, $resource->getDisplayName());
        printf('Description: %s' . PHP_EOL, $resource->getDescription());
        printf('Labels:' . PHP_EOL);
        foreach ($resource->getLabels() as $labels) {
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
    resource_path = (
        f"projects/{project_id}/monitoredResourceDescriptors/{resource_type_name}"
    )
    descriptor = client.[get_monitored_resource_descriptor](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_get_monitored_resource_descriptor)(name=resource_path)
    pprint.pprint(descriptor)

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    # The resource type
    # resource_type = "gce_instance"
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    resource_path = client.[monitored_resource_descriptor_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Paths.html)(
      project:                       project_id,
      monitored_resource_descriptor: resource_type
    )
    
    result = client.get_monitored_resource_descriptor name: resource_path
    p result

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
