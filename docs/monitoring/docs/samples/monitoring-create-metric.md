---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-create-metric/
title: Create a custom metric \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:54.652478+00:00
---

# Create a custom metric  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-create-metric/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Create a custom metric Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to create a custom metric.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create user-defined metrics with the API](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object CreateMetric(string projectId,
        string metricType = "custom.googleapis.com/stores/daily_sales")
    {
        // Create client.
        MetricServiceClient metricServiceClient = MetricServiceClient.Create();
    
        // Prepare custom metric descriptor.      
        MetricDescriptor metricDescriptor = new MetricDescriptor();
        metricDescriptor.DisplayName = "Daily Sales";
        metricDescriptor.Description = "Daily sales records from all branch stores.";
        metricDescriptor.MetricKind = MetricKind.Gauge;
        metricDescriptor.ValueType = MetricDescriptor.Types.ValueType.Double;
        metricDescriptor.Type = metricType;
        metricDescriptor.Unit = "{USD}";
        LabelDescriptor labels = new LabelDescriptor();
        labels.Key = "store_id";
        labels.ValueType = LabelDescriptor.Types.ValueType.String;
        labels.Description = "The ID of the store.";
        metricDescriptor.Labels.Add(labels);
        CreateMetricDescriptorRequest request = new CreateMetricDescriptorRequest
        {
            ProjectName = new ProjectName(projectId),
        };
        request.MetricDescriptor = metricDescriptor;
        // Make the request.
        MetricDescriptor response = metricServiceClient.CreateMetricDescriptor(request);
        Console.WriteLine("Done creating metric descriptor:");
        Console.WriteLine(JObject.Parse($"{response}").ToString());
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
    	"google.golang.org/genproto/googleapis/api/label"
    	"google.golang.org/genproto/googleapis/api/metric"
    	metricpb "google.golang.org/genproto/googleapis/api/metric"
    )
    
    // createCustomMetric creates a custom metric specified by the metric type.
    func createCustomMetric(w io.Writer, projectID, metricType string) (*metricpb.MetricDescriptor, error) {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return nil, err
    	}
    	defer c.Close()
    	md := &metric.MetricDescriptor{
    		Name: "Custom Metric",
    		Type: metricType,
    		Labels: []*label.LabelDescriptor{{
    			Key:         "environment",
    			ValueType:   label.LabelDescriptor_STRING,
    			Description: "An arbitrary measurement",
    		}},
    		MetricKind:  metric.MetricDescriptor_GAUGE,
    		ValueType:   metric.MetricDescriptor_INT64,
    		Unit:        "s",
    		Description: "An arbitrary measurement",
    		DisplayName: "Custom Metric",
    	}
    	req := &monitoringpb.CreateMetricDescriptorRequest{
    		Name:             "projects/" + projectID,
    		MetricDescriptor: md,
    	}
    	m, err := c.CreateMetricDescriptor(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("could not create custom metric: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created %s\n", m.GetName())
    	return m, nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Your Google Cloud Platform project ID
    final String projectId = System.getProperty("projectId");
    
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      ProjectName projectName = ProjectName.of(projectId);
    
      MetricDescriptor descriptor =
          MetricDescriptor.newBuilder()
              .setType(type)
              .addLabels(
                  LabelDescriptor.newBuilder()
                      .setKey("store_id")
                      .setValueType(LabelDescriptor.ValueType.STRING))
              .setDescription("This is a simple example of a custom metric.")
              .setMetricKind(MetricDescriptor.MetricKind.GAUGE)
              .setValueType(MetricDescriptor.ValueType.DOUBLE)
              .build();
    
      CreateMetricDescriptorRequest request =
          CreateMetricDescriptorRequest.newBuilder()
              .setName(projectName.toString())
              .setMetricDescriptor(descriptor)
              .build();
    
      descriptor = client.createMetricDescriptor(request);
      System.out.println("Created descriptor " + descriptor.getName());
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment and edit the following lines of code.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    async function createMetricDescriptor() {
      const request = {
        name: client.projectPath(projectId),
        metricDescriptor: {
          description: 'Daily sales records from all branch stores.',
          displayName: 'Daily Sales',
          type: 'custom.googleapis.com/stores/daily_sales',
          metricKind: '[GAUGE](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.api.metricdescriptor.metrickind.html)',
          valueType: '[DOUBLE](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.api.metricdescriptor.valuetype.html)',
          unit: '{USD}',
          labels: [
            {
              key: 'store_id',
              valueType: 'STRING',
              description: 'The ID of the store.',
            },
          ],
        },
      };
    
      // Creates a custom metric descriptor
      const [descriptor] = await client.createMetricDescriptor(request);
      console.log('Created custom Metric:\n');
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
    createMetricDescriptor();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Api\LabelDescriptor;
    use Google\Api\MetricDescriptor;
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\CreateMetricDescriptorRequest;
    
    /**
     * Create a new metric in Stackdriver Monitoring.
     * Example:
     * ```
     * create_metric($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function create_metric($projectId)
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $projectName = 'projects/' . $projectId;
    
        $descriptor = new MetricDescriptor();
        $descriptor->setDescription('Daily sales records from all branch stores.');
        $descriptor->setDisplayName('Daily Sales');
        $descriptor->setType('custom.googleapis.com/stores/daily_sales');
        $descriptor->setMetricKind(MetricDescriptor\MetricKind::GAUGE);
        $descriptor->setValueType(MetricDescriptor\ValueType::DOUBLE);
        $descriptor->setUnit('{USD}');
        $label = new LabelDescriptor();
        $label->setKey('store_id');
        $label->setValueType(LabelDescriptor\ValueType::STRING);
        $label->setDescription('The ID of the store.');
        $labels = [$label];
        $descriptor->setLabels($labels);
        $createMetricDescriptorRequest = (new CreateMetricDescriptorRequest())
            ->setName($projectName)
            ->setMetricDescriptor($descriptor);
    
        $descriptor = $metrics->createMetricDescriptor($createMetricDescriptorRequest);
        printf('Created a metric: ' . $descriptor->getName() . PHP_EOL);
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api import label_pb2 as ga_label
    from google.api import metric_pb2 as ga_metric
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    project_name = f"projects/{project_id}"
    descriptor = ga_metric.MetricDescriptor()
    descriptor.type = "custom.googleapis.com/my_metric" + str(uuid.uuid4())
    descriptor.metric_kind = ga_metric.MetricDescriptor.MetricKind.GAUGE
    descriptor.value_type = ga_metric.MetricDescriptor.ValueType.DOUBLE
    descriptor.description = "This is a simple example of a custom metric."
    
    labels = ga_label.LabelDescriptor()
    labels.key = "TestLabel"
    labels.value_type = ga_label.LabelDescriptor.ValueType.STRING
    labels.description = "This is a test label"
    descriptor.labels.append(labels)
    
    descriptor = client.[create_metric_descriptor](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_metric_descriptor)(
        name=project_name, metric_descriptor=descriptor
    )
    print("Created {}.".format(descriptor.name))

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    # Your Google Cloud Platform project ID
    # project_id = "YOUR_PROJECT_ID"
    
    # Example metric type
    # metric_type = "custom.googleapis.com/my_metric"
    
    client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html).[metric_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    project_name = client.project_path project: project_id
    
    descriptor = Google::Api::[MetricDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Api-MetricDescriptor.html).new(
      type:        metric_type,
      metric_kind: Google::Api::[MetricDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Api-MetricDescriptor.html)::[MetricKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Api-MetricDescriptor-MetricKind.html)::GAUGE,
      value_type:  Google::Api::[MetricDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Api-MetricDescriptor.html)::[ValueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Api-MetricDescriptor-ValueType.html)::DOUBLE,
      description: "This is a simple example of a custom metric."
    )
    
    result = client.create_metric_descriptor name:              project_name,
                                             metric_descriptor: descriptor
    p "Created #{result.name}"
    p result

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
