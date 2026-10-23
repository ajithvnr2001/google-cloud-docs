---
url: https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics/
title: List metric and resource types \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:17.447560+00:00
---

# List metric and resource types  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  List metric and resource types Stay organized with collections  Save and categorize content based on your preferences. 

Listing metric descriptors and monitored resource types with the Cloud Monitoring API lets you inspect metric schemas and labels to query time-series data or design metrics. You can browse built-in Google Cloud, user-defined, and third-party metric types, as well as monitored resource types in your project. Third-party metrics, such as those from [Bindplane](https://bindplane.com/docs/getting-started/quickstart-guide), use the prefix `workload.googleapis.com/3rd-party-app-name/`; see the Bindplane [Sources documentation](https://bindplane.com/docs/resources/sources). For reference lists of built-in types, see [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) and [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources).

You can run these API methods without writing code in the **Protocol** tabs by using [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer), or use the code samples in your preferred language.

## Before you begin

For an introduction to metrics and monitored resources, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

## List metric descriptors

_Metric descriptors_ are the schemas that define metrics. To find details about the metrics you're interested in, browse the available metric descriptors: 

  * Built-in metrics: You can issue API requests to any existing project, or you can use [Metrics lists](https://docs.cloud.google.com/monitoring/api/metrics) documentation.
  * User-defined and external metrics: You must issue the API request to a project where the user-defined metric is defined or where time-series data for the metric exists. 



For more information on how metric types are named, see [Naming conventions](https://docs.cloud.google.com/monitoring/api/v3/naming-conventions).

### List metric types

To get a current list of metric descriptors, use the [`metricDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list) method. To narrow the set of metric types that are returned, use a filter. For help deciding which metric types to search for, see [Value types and metric kinds](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

### Protocol

  1. Open the [`metricDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list) reference page.
  2. In the pane labeled **Try this method** , enter the following: 
     * **name** : Enter the path and ID of your project: 
           
           projects/PROJECT_ID

     * **filter** : Enter the following: 
           
           metric.type = starts_with("compute.googleapis.com")

  3. Click **Execute**.



The following sample response shows some of the retrieved metric descriptors:
    
    
    "metricDescriptors": [
      {
        "name": "projects/PROJECT_ID/metricDescriptors/compute.googleapis.com/firewall/dropped_bytes_count",
        "labels": [{...}],
          ...
          "description": "Count of incoming bytes dropped by the firewall.",
          "displayName": "Dropped bytes",
          "type": "compute.googleapis.com/firewall/dropped_bytes_count",
          ...
      },
      {
          "name": "projects/PROJECT_ID/metricDescriptors/compute.googleapis.com/firewall/dropped_packets_count",
          "labels": [{...}],
          ...
          "description": "Count of incoming packets dropped by the firewall.",
          "displayName": "Dropped packets",
          "type": "compute.googleapis.com/firewall/dropped_packets_count",
      },
      ...
    ]
    

The `type` value in each descriptor identifies the metric descriptor, for example, `compute.googleapis.com/firewall/dropped_packets_count`. This value is sometimes also called the “metric type” or the “metric type name”.

To view the request as a `curl` command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer. 

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

If you have difficulty, see [Troubleshooting API calls](https://docs.cloud.google.com/monitoring/api/troubleshooting).

### Get metric descriptors

To get information about a single metric type, use the [`metricDescriptors.get` method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/get). This method returns a metric descriptor.

To retrieve a specific metric descriptor, you must provide the full name of the metric to the API. The full name is constructed from two components:

  * A prefix consisting of `projects/PROJECT_ID/metricDescriptors`.
  * The `type` value that identifies the metric descriptor, for example, `compute.googleapis.com/firewall/dropped_packets_count`. See the **Protocol** tab in [List metric types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics#list-metric-descriptors) for more on the `type` value.



The following is an example of the full name of a metric:
    
    
    projects/PROJECT_ID/metricDescriptors/compute.googleapis.com/firewall/dropped_packets_count
    

### Protocol

To get the descriptor for the Compute Engine `/firewall/dropped_packets_count` metric, do the following:

  1. Open the [`metricDescriptors.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/get) reference page.
  2. In the pane labeled **Try this method** , enter the following: 
     * **name** : Enter the ID of your project and the name of the metric: 
           
           projects/PROJECT_ID/metricDescriptors/compute.googleapis.com/firewall/dropped_packets_count

Replace PROJECT_ID with the ID of your Google Cloud project.

  3. Click **Execute**.



The following sample response shows the metric's descriptor:
    
    
    {
        "name": "projects/PROJECT_ID/metricDescriptors/compute.googleapis.com/firewall/dropped_packets_count",
        "labels": [
          {
            "key": "instance_name",
            "description": "The name of the VM instance."
          }
        ],
        "metricKind": "DELTA",
        "valueType": "INT64",
        "unit": "1",
        "description": "Count of incoming packets dropped by the firewall.",
        "displayName": "Dropped packets",
        "type": "compute.googleapis.com/firewall/dropped_packets_count",
      }
    

To view the request as a `curl` command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer. 

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

If you have difficulty, see [Troubleshooting API calls](https://docs.cloud.google.com/monitoring/api/troubleshooting).

## List monitored resources

_Monitored resources_ are cloud entities that can be monitored. To find the kinds of entities that have metrics, browse the list of monitored resource types.

To get information about monitored resources, you can issue API requests to any existing project, or you can use the [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources) documentation.

### List resource types

To get a current list of monitored resource types from the Monitoring API, use the [`monitoredResourceDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/list) method and supply your project ID.

### Protocol

  1. Open the [`monitoredResourceDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/list) reference page.
  2. In the pane labeled **Try this method** , enter the following: 
     * **name** : Enter the path and ID of your project: 
           
           projects/PROJECT_ID

  3. Click **Execute**.



The following sample response shows some of the returned monitored resource types:
    
    
    {
      "resourceDescriptors": [
      {
        "type": "aiplatform.googleapis.com/Endpoint",
        "displayName": "AI Platform Endpoint",
        "description": "A Cloud AI Platform API Endpoint where Models are deployed into it.",
        "labels": [{...}],
        "name": "projects/PROJECT_ID/monitoredResourceDescriptors/aiplatform.googleapis.com/Endpoint",
      },
      {
        "type": "aiplatform.googleapis.com/Featurestore",
        "displayName": "AI Platform Feature Store",
        "description": "A Cloud AI Platform Feature Store.",
        "labels": [{...}],
        "name": "projects/PROJECT_ID/monitoredResourceDescriptors/aiplatform.googleapis.com/Featurestore",
      },
      ]
    }
    

To view the request as a `curl` command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer. 

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object ListMonitoredResources(string projectId)
    {
        Console.WriteLine("Starting to List Monitored Resources...");
        MetricServiceClient client = MetricServiceClient.Create();
        ProjectName projectName = new ProjectName(projectId);
    
        PagedEnumerable<ListMonitoredResourceDescriptorsResponse, MonitoredResourceDescriptor>
            resources = client.ListMonitoredResourceDescriptors(projectName);
        if (resources.Any())
        {
            foreach (MonitoredResourceDescriptor resource in resources.Take(10))
            {
                Console.WriteLine($"{resource.Name}: {resource.DisplayName}");
            }
        }
        else
        { 
            Console.WriteLine("No resources found.");
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
    
    // listMonitoredResources lists all the resources available to be monitored.
    func listMonitoredResources(w io.Writer, projectID string) error {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer c.Close()
    
    	req := &monitoringpb.ListMonitoredResourceDescriptorsRequest{
    		Name: "projects/" + projectID,
    	}
    	iter := c.ListMonitoredResourceDescriptors(ctx, req)
    
    	for {
    		resp, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Could not list time series: %w", err)
    		}
    		fmt.Fprintf(w, "%v\n", resp)
    	}
    	fmt.Fprintln(w, "Done")
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Your Google Cloud Platform project ID
    String projectId = System.getProperty("projectId");
    ProjectName name = ProjectName.of(projectId);
    
    ListMonitoredResourceDescriptorsRequest request =
        ListMonitoredResourceDescriptorsRequest.newBuilder().setName(name.toString()).build();
    
    System.out.println("Listing monitored resource descriptors: ");
    
    // Instantiates a client
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      ListMonitoredResourceDescriptorsPagedResponse response =
          client.listMonitoredResourceDescriptors(request);
    
      for (MonitoredResourceDescriptor d : response.iterateAll()) {
        System.out.println(d.getType());
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function listMonitoredResourceDescriptors() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
    
      const request = {
        name: client.projectPath(projectId),
      };
    
      // Lists monitored resource descriptors
      const [descriptors] =
        await client.listMonitoredResourceDescriptors(request);
      console.log('Monitored Resource Descriptors:');
      descriptors.forEach(descriptor => {
        console.log(descriptor.name);
        console.log(`  Type: ${descriptor.type}`);
        if (descriptor.labels) {
          console.log('  Labels:');
          descriptor.labels.forEach(label => {
            console.log(
              `    ${label.key} (${label.valueType}): ${label.description}`
            );
          });
        }
        console.log();
      });
    }
    listMonitoredResourceDescriptors();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\ListMonitoredResourceDescriptorsRequest;
    
    /**
     * Example:
     * ```
     * list_resources('your-project-id');
     * ```
     *
     * @param string $projectId Your project ID
     */
    function list_resources($projectId)
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
        $projectName = 'projects/' . $projectId;
        $listMonitoredResourceDescriptorsRequest = (new ListMonitoredResourceDescriptorsRequest())
            ->setName($projectName);
        $descriptors = $metrics->listMonitoredResourceDescriptors($listMonitoredResourceDescriptorsRequest);
        foreach ($descriptors->iterateAllElements() as $descriptor) {
            print($descriptor->getType() . PHP_EOL);
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    project_name = f"projects/{project_id}"
    resource_descriptors = client.[list_monitored_resource_descriptors](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_list_monitored_resource_descriptors)(name=project_name)
    for descriptor in resource_descriptors:
        print(descriptor.type)

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    project_name = client.project_path project: project_id
    
    results = client.list_monitored_resource_descriptors name: project_name
    results.each do |descriptor|
      p descriptor.type
    end

If you have difficulty, see [Troubleshooting API calls](https://docs.cloud.google.com/monitoring/api/troubleshooting).

### Get resource descriptors

To get a specific monitored-resource descriptor, use the [`monitoredResourceDescriptors.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/get) method.

To retrieve a specific monitored-resource descriptor, you must provide the full name of the descriptor to the API. The full name is constructed from two components:

  * A prefix consisting of `projects/PROJECT_ID/monitoredResourceDescriptors`.
  * The `type` value that identifies the monitored-resource descriptor, for example, `gce_instance`. See the **Protocol** tab in [List resource types](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics#res-list-basic) for more on the `type` value.



The following is an example of the full name of a monitored resource:
    
    
    projects/PROJECT_ID/monitoredResourceDescriptors/gce_instance
    

### Protocol

To get the descriptor for the `gce_instance` resource type, do the following:

  1. Open the [`monitoredResourceDescriptors.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/get) reference page.
  2. In the pane labeled **Try this method** , enter the following: 
     * **name** : Enter the path and ID of your project and the name of the resource: 
           
           projects/PROJECT_ID/monitoredResourceDescriptors/gce_instance

  3. Click **Execute**.



The following sample response shows the descriptor for this monitored resource:
    
    
        {
          "type": "gce_instance",
          "displayName": "VM Instance",
          "description": "A virtual machine instance hosted in Compute Engine.",
          "labels": [
            {
              "key": "project_id",
              "description": "The identifier of the Google Cloud project associated with this resource, such as \"my-project\"."
            },
            {
              "key": "instance_id",
              "description": "The numeric VM instance identifier assigned by Compute Engine."
            },
            {
              "key": "zone",
              "description": "The Compute Engine zone in which the VM is running."
            }
          ],
          "name": "projects/PROJECT_ID/monitoredResourceDescriptors/gce_instance"
        }
    

To view the request as a `curl` command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer. 

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
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    resource_path = client.[monitored_resource_descriptor_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-MetricService-Paths.html)(
      project:                       project_id,
      monitored_resource_descriptor: resource_type
    )
    
    result = client.get_monitored_resource_descriptor name: resource_path
    p result

If you have difficulty, see [Troubleshooting API calls](https://docs.cloud.google.com/monitoring/api/troubleshooting).

## What's next

  * For information about how to use the Cloud Monitoring API to read time-series data, see [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics). 
  * For a list of monitored-resource types available for your use with user-defined metrics, see [Choose a monitored-resource type](https://docs.cloud.google.com/monitoring/custom-metrics#which-resource). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
