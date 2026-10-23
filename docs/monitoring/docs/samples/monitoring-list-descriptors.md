---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-list-descriptors/
title: List metric descriptors \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:33.021668+00:00
---

# List metric descriptors  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-list-descriptors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  List metric descriptors Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list available metric descriptors.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List metric and resource types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object ListMetrics(string projectId)
    {
        MetricServiceClient client = MetricServiceClient.Create();
        ProjectName projectName = new ProjectName(projectId);
        PagedEnumerable<ListMetricDescriptorsResponse, MetricDescriptor> metrics = client.ListMetricDescriptors(projectName);
        foreach (MetricDescriptor metric in metrics)
        {
            Console.WriteLine($"{metric.Name}: {metric.DisplayName}");
        }
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
    	"google.golang.org/api/iterator"
    )
    
    // listMetrics lists all the metrics available to be monitored in the API.
    func listMetrics(w io.Writer, projectID string) error {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer c.Close()
    
    	req := &monitoringpb.ListMetricDescriptorsRequest{
    		Name: "projects/" + projectID,
    	}
    	iter := c.ListMetricDescriptors(ctx, req)
    
    	for {
    		resp, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Could not list metrics: %w", err)
    		}
    		fmt.Fprintf(w, "%v\n", resp.GetType())
    	}
    	fmt.Fprintln(w, "Done")
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Your Google Cloud Platform project ID
    String projectId = System.getProperty("projectId");
    ProjectName name = ProjectName.of(projectId);
    
    ListMetricDescriptorsRequest request =
        ListMetricDescriptorsRequest.newBuilder().setName(name.toString()).build();
    
    // Instantiates a client
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      ListMetricDescriptorsPagedResponse response = client.listMetricDescriptors(request);
    
      System.out.println("Listing descriptors: ");
    
      for (MetricDescriptor d : response.iterateAll()) {
        System.out.println(d.getName() + " " + d.getDisplayName());
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function listMetricDescriptors() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
    
      const request = {
        name: client.projectPath(projectId),
      };
    
      // Lists metric descriptors
      const [descriptors] = await client.listMetricDescriptors(request);
      console.log('Metric Descriptors:');
      descriptors.forEach(descriptor => console.log(descriptor.name));
    }
    listMetricDescriptors();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\ListMetricDescriptorsRequest;
    
    /**
     * Example:
     * ```
     * list_descriptors($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function list_descriptors($projectId)
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $projectName = 'projects/' . $projectId;
        $listMetricDescriptorsRequest = (new ListMetricDescriptorsRequest())
            ->setName($projectName);
        $descriptors = $metrics->listMetricDescriptors($listMetricDescriptorsRequest);
    
        printf('Metric Descriptors:' . PHP_EOL);
        foreach ($descriptors->iterateAllElements() as $descriptor) {
            printf($descriptor->getName() . PHP_EOL);
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    project_name = f"projects/{project_id}"
    descriptors = client.[list_metric_descriptors](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_list_metric_descriptors)(name=project_name)
    for descriptor in descriptors:
        print(descriptor.type)

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    project_name = client.project_path project: project_id
    
    results = client.list_metric_descriptors name: project_name
    results.each do |descriptor|
      p descriptor.type
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
