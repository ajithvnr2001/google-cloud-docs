---
url: https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics/
title: Create user-defined metrics with the API \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:29.106162+00:00
---

# Create user-defined metrics with the API  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Create user-defined metrics with the API Stay organized with collections  Save and categorize content based on your preferences. 

Creating user-defined metrics (also called _custom metrics_) with the Cloud Monitoring API lets you capture application-specific measurements and chart or alert on them just like built-in Cloud Monitoring metrics. Like built-in metrics, each user-defined metric combines data points, a metric type that defines what the points represent, and a monitored resource that identifies where the data originated.

To instrument your application, we recommend that you use an open-source, vendor-neutral instrumentation framework, such as [OpenTelemetry](https://opentelemetry.io/), instead of vendor- and product-specific APIs or client libraries. For information about these frameworks, see [ Instrumentation and observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview) and [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

You can't use the Monitoring API to create log-based metrics, which derive metric data from log entries. Instead, Cloud Logging creates the metric structures and sends the data to Cloud Monitoring for you; see [Create counter metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics) and [Create distribution metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics). User-defined metrics are a chargeable feature of Cloud Monitoring; for pricing details, see the Cloud Monitoring sections of the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## Before you begin

To learn about the structures that underlie all metrics, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

To use Cloud Monitoring, you must have a Google Cloud project with billing enabled. When necessary, do the following:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Ensure the Monitoring API is enabled. For details, see [Enabling the Monitoring API](https://docs.cloud.google.com/monitoring/api/enable-api). 
  4. For applications running outside of Google Cloud, your Google Cloud project must authenticate your application using local Application Default Credentials (ADC). For more information, see [Set up ADC for on-premises or another cloud provider](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises). 



## Create a user-defined metric type

To create a user-defined metric, you either define a [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) object that specifies various information about the metric, or you write metric data. When you write metric data, Monitoring creates the metric descriptor for you based on the structure of the data you provide. For information about designing a metric descriptor, see [Metric descriptors for user-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics#using-custom).

### Auto-creation of metric descriptors

If you write metric data when a metric descriptor for that user-defined metric doesn't yet exist, then a metric descriptor is created automatically. However, this new metric descriptor might not be exactly what you want; auto-creation of metric descriptors involves some assumptions and defaults.

Cloud Monitoring creates a new [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) when the [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) object included in a call to [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) references a [`Metric`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric) object that specifies a nonexistent metric-type name. Cloud Monitoring uses the following rules to populate the [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor):

  * `type`: The type is copied from the [`Metric`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric) object's `type` field.
  * `name`: The name is created from the project ID in the method call and the value of the `type` in the `Metric` object.
  * `labels`: The labels that appear in the `Metric` object. Each label descriptor in the new metric descriptor has the following fields: 
    * `key`: the label key in the `Metric` object.
    * `valueType`: `STRING`
    * `description`: not set
  * `metricKind`: The metric kind is set to `GAUGE` unless you specify the `metricKind` parameter of the [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) object. When you specify the `metricKind`, the new metric has that kind. You can specify only `GAUGE` and `CUMULATIVE` kinds.
  * `valueType`: The value type is taken from the typed value of the [`Point`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#Point) being written. The value type must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`. When you specify a value type in the `valueType` field of the [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries), that type must match the type of the [`Point`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#Point).
  * `unit`: not set
  * `description`: `"Auto created custom metric."`.
  * `displayName`: not set



In a single [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) call, you can include multiple [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) objects that refer to the same nonexistent metric type. In that case, the labels in the new metric descriptor consist of the union of all the labels in the [`Metric`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts#Metric) objects in all the time series in this call to `create`.

**Next step** : See [Write user-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#writing-ts).

### Manual creation of metric descriptors

To create a metric descriptor, do the following:

  1. Determine the structure of your metric descriptor. For help in making these choices, you can [browse the built-in metrics](https://docs.cloud.google.com/monitoring/custom-metrics/browsing-metrics#list-metric-descriptors) and [look at their time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics):

     1. Choose a [metric name](https://docs.cloud.google.com/monitoring/api/v3/naming-conventions) for your user-defined metric.

     2. Choose a display name and description for your metric. The display name is used in the Google Cloud console.

     3. Choose a project or projects in which to define your user-defined metric and write its time-series data. When you need the same metric in several projects, make identical definitions of the metric in each project.

     4. Determine the metric's kind, value type, and (optionally) units. Not all value types and metric kinds are supported for user-defined metrics. For more information on these fields, see [Value types and metric kinds](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types).

     5. Choose the metric's labels—their names, value types, and descriptions.

  2. Determine the monitored resources against which the metric data is written. Choose from the following list:

     * [`aws_ec2_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance): Amazon EC2 instance.
     * [`dataflow_job`](https://docs.cloud.google.com/monitoring/api/resources#tag_dataflow_job): Dataflow job.
     * [`gae_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gae_instance): App Engine instance.
     * [`gce_instance`](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance): Compute Engine instance.
     * [`generic_node`](https://docs.cloud.google.com/monitoring/api/resources#tag_generic_node): User-specified computing node.
     * [`generic_task`](https://docs.cloud.google.com/monitoring/api/resources#tag_generic_task): User-defined task.
     * [`gke_container`](https://docs.cloud.google.com/monitoring/api/resources#tag_gke_container): GKE container instance.
     * [`global`](https://docs.cloud.google.com/monitoring/api/resources#tag_global): Use this resource when no other resource type is suitable. For most use cases, `generic_node` or `generic_task` are better choices than `global`.
     * [`k8s_cluster`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_cluster): Kubernetes cluster.
     * [`k8s_container`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container): Kubernetes container.
     * [`k8s_node`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_node): Kubernetes node.
     * [`k8s_pod`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_pod): Kubernetes pod.
  3. Create a [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) object, and then pass it as an argument to a call to the [`metricDescriptors.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create) method.




It is usually an error to call [`metricDescriptors.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create) using the same type name as an existing metric descriptor. However, if all the fields of the new [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) object match the fields of the existing descriptor exactly, then it isn't an error but it has no effect.

In the following example, you create a gauge metric.

### Protocol

To create a metric descriptor, use the [`metricDescriptors.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create) method. You can execute this method by using the APIs Explorer widget on the method's reference page. See [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer) for more information.

The following are the sample parameters to [`metricDescriptors.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create):

  * **name** (URL): `projects/[PROJECT_ID]`
  * **Request body** : Supply a [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) object such as the following:
        
        {
          "name": "",
          "description": "Daily sales records from all branch stores.",
          "displayName": "Sales",
          "type": "custom.googleapis.com/stores/sales",
          "metricKind": "GAUGE",
          "valueType": "DOUBLE",
          "unit": "{USD}",
          "labels": [
            {
              "key": "store_id",
              "valueType": "STRING",
              "description": "The ID of the store."
            },
          ],
        }
        




Supply these values to the fields in the widget, using your project's ID in place of `[PROJECT_ID]`:

![Try this API dialog populated with the request body to create a metric descriptor.](https://docs.cloud.google.com/static/monitoring/images/metricDescriptors-create.png)

Click the **Execute** button to run the method.

[Try It!](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create?apix_params=%7B%22name%22:%22projects/%5BPROJECT_ID%5D%22,%22resource%22:%7B%22name%22:%22%22,%22description%22:%22Daily%20sales%20records%20from%20all%20branch%20stores.%22,%22displayName%22:%22Sales%22,%22type%22:%22custom.googleapis.com/stores/sales%22,%22metricKind%22:%22CUMULATIVE%22,%22valueType%22:%22DOUBLE%22,%22unit%22:%22%7BUSD%7D%22,%22labels%22:%5B%7B%22key%22:%22store_id%22,%22valueType%22:%22STRING%22,%22description%22:%22The%20ID%20of%20the%20store.%22%7D%5D%7D%7D)

**Note:** To view the request as a curl command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer.

When creating a new metric, the `name` field in the `MetricDescriptor` is ignored and can be omitted. The `create` method returns the new metric descriptor with the `name` field filled in, which in this example would be the following:
    
    
    "name": "projects/[PROJECT_ID]/metricDescriptors/custom.googleapis.com/stores/daily_sales"
    

If, for example, you want to get a metric's descriptor, you use this name. 

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

See [Troubleshoot API calls](https://docs.cloud.google.com/monitoring/api/troubleshooting) if you have difficulty.

**Next step** : See [Write user-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#writing-ts).

## Write user-defined metrics

You can write data only to metric types for user-defined metrics. To write your data, use the [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) method. When the time series exists, this method appends a new data point to the existing time series. When the time series doesn't exist, this method creates it and appends the data.

You write data points by passing a list of [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) objects to [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create). The maximum list size is 200 and each object in the list must specify a different time series:

  * The values of the `metric` and `resource` fields identify a specific [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) object. These fields represent the metric type of the data and the monitored resource from which the data was collected.
  * Omit the fields `metricKind` and `valueType`; they are ignored when writing data points.
  * Each [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) object must contain only a single [`Point`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#Point) object:

    * The point's value and time interval must be consistent with the metric type's definition. For information on time intervals for different metric kinds, see [`TimeInterval`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval).
    * The point's time interval must be later than any point already in the time series.
    * The end time of the interval must not be more than 25 hours in the past or more than five minutes in the future.
  * To write more than one point to the same time series, use a separate call to the [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) method for each point. Don't write data to a single time series faster than one point each 5 seconds. When you add data points to different time series, there is no rate limitation.




### Protocol

To write metric data, use the [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) method. You can execute this method by using the APIs Explorer widget on the method's reference page. See [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer) for more information.

To write a point to the `stores/daily_sales` metric created in [Manual creation of metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#create-metric-desc):

  1. Go to the [reference page for `timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create).
  2. Supply the parameters below to the APIs Explorer widget.
  3. Click the **Execute** button.



Use the following sample parameters:

  * **name** : `projects/[PROJECT_ID]`
  * **Request body** : Include a list of [`TimeSeries`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) objects. The following sample has only one time series in the list.

**Note:** You **must change** the `project_id` and `endTime` values in the following request body. Use the ID of your project. The `endTime` must be close to the current time; `date -Iseconds` returns the current time in a usable format.
        
        {
         "timeSeries": [
          {
           "metric": {
            "type": "custom.googleapis.com/my_metric",
            "labels": {
             "my_label": "my_value"
            }
           },
           "resource": {
            "type": "gce_instance",
            "labels": {
             "project_id": "[PROJECT_ID]",
             "instance_id": "1234567890123456789",
             "zone": "us-central1-f"
            }
           },
           "points": [
            {
             "interval": {
              "endTime": "2018-06-01T10:00:00-04:00"
             },
             "value": {
              "doubleValue": 123.45
             }
            }
           ]
          }
         ]
        }
        




[Try It!](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create?apix_params=%7B%22name%22%3A%22projects%2F%5BPROJECT_ID%5D%22%2C%22resource%22%3A%7B%22timeSeries%22%3A%5B%7B%22metric%22%3A%7B%22type%22%3A%22custom.googleapis.com%2Fmy_metric%22%2C%22labels%22%3A%7B%22my_label%22%3A%22my_value%22%7D%7D%2C%22resource%22%3A%7B%22type%22%3A%22gce_instance%22%2C%22labels%22%3A%7B%22project_id%22%3A%22%5BPROJECT_ID%5D%22%2C%22instance_id%22%3A%221234567890123456789%22%2C%22zone%22%3A%22us-central1-f%22%7D%7D%2C%22points%22%3A%5B%7B%22interval%22%3A%7B%22endTime%22%3A%222018-06-01T10%3A00%3A00-04%3A00%22%7D%2C%22value%22%3A%7B%22doubleValue%22%3A123.45%7D%7D%5D%7D%5D%7D%7D)

**Note:** To view the request as a curl command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer.

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object WriteTimeSeriesData(string projectId)
    {
        // Create client.
        MetricServiceClient metricServiceClient = MetricServiceClient.Create();
        // Initialize request argument(s).
        ProjectName name = new ProjectName(projectId);
        // Prepare a data point. 
        Point dataPoint = new Point();
        TypedValue salesTotal = new TypedValue();
        salesTotal.DoubleValue = 123.45;
        dataPoint.Value = salesTotal;
        Timestamp timeStamp = new Timestamp();
        timeStamp.Seconds = (long)(DateTime.UtcNow - s_unixEpoch).TotalSeconds;
        TimeInterval interval = new TimeInterval();
        interval.EndTime = timeStamp;
        dataPoint.Interval = interval;
    
        // Prepare custom metric.
        Metric metric = new Metric();
        metric.Type = "custom.googleapis.com/stores/daily_sales";
        metric.Labels.Add("store_id", "Pittsburgh");
    
        // Prepare monitored resource.
        MonitoredResource resource = new MonitoredResource();
        resource.Type = "global";
        resource.Labels.Add("project_id", projectId);
    
        // Create a new time series using inputs.
        TimeSeries timeSeriesData = new TimeSeries();
        timeSeriesData.Metric = metric;
        timeSeriesData.Resource = resource;
        timeSeriesData.Points.Add(dataPoint);
    
        // Add newly created time series to list of time series to be written.
        IEnumerable<TimeSeries> timeSeries = new List<TimeSeries> { timeSeriesData };
        // Write time series data.
        metricServiceClient.CreateTimeSeries(name, timeSeries);
        Console.WriteLine("Done writing time series data:");
        Console.WriteLine(JObject.Parse($"{timeSeriesData}").ToString());
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // writeTimeSeriesValue writes a value for the custom metric created
    func writeTimeSeriesValue(projectID, metricType string) error {
    	ctx := context.Background()
    	c, err := monitoring.NewMetricClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer c.Close()
    	now := &timestamp.Timestamp{
    		Seconds: time.Now().Unix(),
    	}
    	req := &monitoringpb.CreateTimeSeriesRequest{
    		Name: "projects/" + projectID,
    		TimeSeries: []*monitoringpb.TimeSeries{{
    			Metric: &metricpb.Metric{
    				Type: metricType,
    				Labels: map[string]string{
    					"environment": "STAGING",
    				},
    			},
    			Resource: &monitoredres.MonitoredResource{
    				Type: "gce_instance",
    				Labels: map[string]string{
    					"instance_id": "test-instance",
    					"zone":        "us-central1-f",
    				},
    			},
    			Points: []*monitoringpb.Point{{
    				Interval: &monitoringpb.TimeInterval{
    					StartTime: now,
    					EndTime:   now,
    				},
    				Value: &monitoringpb.TypedValue{
    					Value: &monitoringpb.TypedValue_Int64Value{
    						Int64Value: rand.Int63n(10),
    					},
    				},
    			}},
    		}},
    	}
    	log.Printf("writeTimeseriesRequest: %+v\n", req)
    
    	err = c.CreateTimeSeries(ctx, req)
    	if err != nil {
    		return fmt.Errorf("could not write time series value, %w ", err)
    	}
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    String projectId = System.getProperty("projectId");
    
    // Prepares an individual data point
    TimeInterval interval =
        TimeInterval.newBuilder()
            .setEndTime(Timestamps.fromMillis(System.currentTimeMillis()))
            .build();
    TypedValue value = TypedValue.newBuilder().setDoubleValue(123.45).build();
    Point point = Point.newBuilder().setInterval(interval).setValue(value).build();
    
    List<Point> pointList = new ArrayList<>();
    pointList.add(point);
    
    ProjectName name = ProjectName.of(projectId);
    
    // Prepares the metric descriptor
    Map<String, String> metricLabels = new HashMap<>();
    Metric metric =
        Metric.newBuilder()
            .setType("custom.googleapis.com/my_metric")
            .putAllLabels(metricLabels)
            .build();
    
    // Prepares the monitored resource descriptor
    Map<String, String> resourceLabels = new HashMap<>();
    resourceLabels.put("instance_id", "1234567890123456789");
    resourceLabels.put("zone", "us-central1-f");
    
    MonitoredResource resource =
        MonitoredResource.newBuilder().setType("gce_instance").putAllLabels(resourceLabels).build();
    
    // Prepares the time series request
    TimeSeries timeSeries =
        TimeSeries.newBuilder()
            .setMetric(metric)
            .setResource(resource)
            .addAllPoints(pointList)
            .build();
    
    List<TimeSeries> timeSeriesList = new ArrayList<>();
    timeSeriesList.add(timeSeries);
    
    CreateTimeSeriesRequest request =
        CreateTimeSeriesRequest.newBuilder()
            .setName(name.toString())
            .addAllTimeSeries(timeSeriesList)
            .build();
    
    // Writes time series data
    try (final MetricServiceClient client = MetricServiceClient.create();) {
      client.createTimeSeries(request);
    }
    System.out.println("Done writing time series value.");

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[MetricServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    async function writeTimeSeriesData() {
      /**
       * TODO(developer): Uncomment and edit the following lines of code.
       */
      // const projectId = 'YOUR_PROJECT_ID';
    
      const dataPoint = {
        interval: {
          endTime: {
            seconds: Date.now() / 1000,
          },
        },
        value: {
          doubleValue: 123.45,
        },
      };
    
      const timeSeriesData = {
        metric: {
          type: 'custom.googleapis.com/stores/daily_sales',
          labels: {
            store_id: 'Pittsburgh',
          },
        },
        resource: {
          type: 'global',
          labels: {
            project_id: projectId,
          },
        },
        points: [dataPoint],
      };
    
      const request = {
        name: client.projectPath(projectId),
        timeSeries: [timeSeriesData],
      };
    
      // Writes time series data
      const result = await client.createTimeSeries(request);
      console.log('Done writing time series data.', result);
    }
    writeTimeSeriesData();

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Api\Metric;
    use Google\Api\MonitoredResource;
    use Google\Cloud\Monitoring\V3\Client\MetricServiceClient;
    use Google\Cloud\Monitoring\V3\CreateTimeSeriesRequest;
    use Google\Cloud\Monitoring\V3\Point;
    use Google\Cloud\Monitoring\V3\TimeInterval;
    use Google\Cloud\Monitoring\V3\TimeSeries;
    use Google\Cloud\Monitoring\V3\TypedValue;
    use Google\Protobuf\Timestamp;
    
    /**
     * Example:
     * ```
     * write_timeseries($projectId);
     * ```
     *
     * @param string $projectId Your project ID
     */
    function write_timeseries($projectId)
    {
        $metrics = new MetricServiceClient([
            'projectId' => $projectId,
        ]);
    
        $projectName = 'projects/' . $projectId;
    
        $endTime = new Timestamp();
        $endTime->setSeconds(time());
        $interval = new TimeInterval();
        $interval->setEndTime($endTime);
    
        $value = new TypedValue();
        $value->setDoubleValue(123.45);
    
        $point = new Point();
        $point->setValue($value);
        $point->setInterval($interval);
        $points = [$point];
    
        $metric = new Metric();
        $metric->setType('custom.googleapis.com/stores/daily_sales');
        $labels = ['store_id' => 'Pittsburg'];
        $metric->setLabels($labels);
    
        $resource = new MonitoredResource();
        $resource->setType('global');
        $labels = ['project_id' => $projectId];
        $resource->setLabels($labels);
    
        $timeSeries = new TimeSeries();
        $timeSeries->setMetric($metric);
        $timeSeries->setResource($resource);
        $timeSeries->setPoints($points);
        $createTimeSeriesRequest = (new CreateTimeSeriesRequest())
            ->setName($projectName)
            ->setTimeSeries([$timeSeries]);
    
        $metrics->createTimeSeries($createTimeSeriesRequest);
    
        printf('Done writing time series data.' . PHP_EOL);
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    project_name = f"projects/{project_id}"
    
    series = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[TimeSeries](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeSeries.html)()
    series.metric.type = "custom.googleapis.com/my_metric" + str(uuid.uuid4())
    series.resource.type = "gce_instance"
    series.resource.labels["instance_id"] = "1234567890123456789"
    series.resource.labels["zone"] = "us-central1-c"
    series.metric.labels["TestLabel"] = "My Label Data"
    now = time.time()
    seconds = int(now)
    nanos = int((now - seconds) * 10**9)
    interval = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[TimeInterval](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeInterval.html)(
        {"end_time": {"seconds": seconds, "nanos": nanos}}
    )
    point = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[Point](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.Point.html)({"interval": interval, "value": {"double_value": 3.14}})
    series.points = [point]
    client.[create_time_series](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_time_series)(name=project_name, time_series=[series])

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
    
    series = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TimeSeries.new
    series.[metric](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) = Google::Api::[Metric](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging-v2/latest/Google-Api-Metric.html).new type: metric_type
    
    resource = Google::Api::[MonitoredResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Api-MonitoredResource.html).new type: "global"
    resource.labels["project_id"] = project_id
    series.[resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) = resource
    
    point = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::Point.new
    point.value = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TypedValue.new double_value: 3.14
    now = Time.now
    end_time = Google::Protobuf::[Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Protobuf-Timestamp.html).new seconds: now.to_i, nanos: now.nsec
    point.interval = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html)::[V3](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3.html)::TimeInterval.new end_time: end_time
    series.[points](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-TimeSeries.html) << point
    
    client.create_time_series name: project_name, time_series: [series]
    p "Time series created."

See [Troubleshoot API calls](https://docs.cloud.google.com/monitoring/api/troubleshooting) if you have difficulty.

## Delete user-defined metrics

To delete a user-defined metric, delete its metric descriptor. You can't delete the time-series data stored in your Google Cloud project; however, deleting the metric descriptor renders the data inaccessible. The data expires and is deleted according to the [data retention policy](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

You can't delete the metric descriptor for a built-in metric.

**Note:** Deleting a metric descriptor makes its existing time-series data inaccessible. If you recreate a deleted metric descriptor, exactly as it was before deletion, then you might regain access to the data. Don't depend on this behavior.

To delete your metric descriptor, call the [`metricDescriptors.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete) method.

### Protocol

To delete a metric descriptor, use the [`metricDescriptors.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete) method. You can execute this method by using the APIs Explorer widget on the method's reference page. See [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer) for more information.

To delete the `stores/daily_sales` metric created in [Manual creation of metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#create-metric-desc):

  1. Go to the [reference page for `metricDescriptors.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete).
  2. Supply the name of the metric descriptor to the APIs Explorer widget:

**name** : `projects/[PROJECT_ID]/metricDescriptors/custom.googleapis.com/stores/daily_sales`

  3. Click the **Execute** button.




[Try It!](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete?apix_params=%7B%22name%22%3A%22projects%2F%5BPROJECT_ID%5D%2FmetricDescriptors%2Fcustom.googleapis.com%2Fstores%2Fdaily_sales%22%7D)

**Note:** To view the request as a curl command, as an HTTP request, or in JavaScript, click _fullscreen_ **Full screen** in APIs Explorer.

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

See [Troubleshoot API calls](https://docs.cloud.google.com/monitoring/api/troubleshooting) if you have difficulty.

## Modify a user-defined metric

To modify a user-defined metric, you must update the [`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) object that defines the metric. The only supported modification is to add labels.

To add labels to an existing user-defined metric, use the [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) method and include the new labels with the time-series data. The labels are added to the metric descriptor when the labels you attempt to write are valid and the total number of labels is less than 30.

The time-series data is then written as though the label had been there from the beginning.

If you want to do more than add new labels, then you must delete and recreate the metric descriptor. In this case, you lose all the time-series data previously collected for the old metric descriptor. See [Delete user-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#deleting_metrics) for more information.

You can't rename a metric.

## What's next

  * [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management)
  * [List of built-in metrics](https://docs.cloud.google.com/monitoring/api/metrics)
  * [List of monitored resources](https://docs.cloud.google.com/monitoring/api/resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
