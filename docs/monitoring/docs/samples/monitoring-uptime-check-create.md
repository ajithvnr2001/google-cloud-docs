---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-create/
title: Create an uptime check \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:55.621405+00:00
---

# Create an uptime check  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Create an uptime check Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to create an uptime check.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create public uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object CreateUptimeCheck(string projectId, string hostName,
        string displayName)
    {
        // Define a new config.
        var config = new UptimeCheckConfig()
        {
            DisplayName = displayName,
            MonitoredResource = new MonitoredResource()
            {
                Type = "uptime_url",
                Labels = { { "host", hostName } }
            },
            HttpCheck = new UptimeCheckConfig.Types.HttpCheck()
            {
                Path = "/",
                Port = 80,
            },
            Timeout = TimeSpan.FromSeconds(10).ToDuration(),
            Period = TimeSpan.FromMinutes(5).ToDuration()
        };
        // Create a client.
        var client = UptimeCheckServiceClient.Create();
        ProjectName projectName = new ProjectName(projectId);
        // Create the config.
        var newConfig = client.CreateUptimeCheckConfig(
            projectName,
            config,
            CallSettings.FromExpiration(
                Expiration.FromTimeout(
                    TimeSpan.FromMinutes(2))));
        Console.WriteLine(newConfig.Name);
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // createGet creates an example uptime check on a GET request.
    func createGet(w io.Writer, projectID string) (*monitoringpb.UptimeCheckConfig, error) {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	req := &monitoringpb.CreateUptimeCheckConfigRequest{
    		Parent: "projects/" + projectID,
    		UptimeCheckConfig: &monitoringpb.UptimeCheckConfig{
    			DisplayName: "new GET uptime check",
    			Resource: &monitoringpb.UptimeCheckConfig_MonitoredResource{
    				MonitoredResource: &monitoredres.MonitoredResource{
    					Type: "uptime_url",
    					Labels: map[string]string{
    						"host": "example.com",
    					},
    				},
    			},
    			CheckRequestType: &monitoringpb.UptimeCheckConfig_HttpCheck_{
    				HttpCheck: &monitoringpb.UptimeCheckConfig_HttpCheck{
    					RequestMethod: monitoringpb.UptimeCheckConfig_HttpCheck_GET,
    					Path:          "/",
    					Port:          80,
    				},
    			},
    			Timeout: &duration.Duration{Seconds: 10},
    			Period:  &duration.Duration{Seconds: 300},
    		},
    	}
    	config, err := client.CreateUptimeCheckConfig(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CreateUptimeCheckConfig GET: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully created GET uptime check %q\n", config.GetDisplayName())
    	return config, nil
    }
    
    // createPost creates an example uptime check on a POST request.
    func createPost(w io.Writer, projectID string) (*monitoringpb.UptimeCheckConfig, error) {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	req := &monitoringpb.CreateUptimeCheckConfigRequest{
    		Parent: "projects/" + projectID,
    		UptimeCheckConfig: &monitoringpb.UptimeCheckConfig{
    			DisplayName: "new POST uptime check",
    			Resource: &monitoringpb.UptimeCheckConfig_MonitoredResource{
    				MonitoredResource: &monitoredres.MonitoredResource{
    					Type: "uptime_url",
    					Labels: map[string]string{
    						"host": "example.com",
    					},
    				},
    			},
    			CheckRequestType: &monitoringpb.UptimeCheckConfig_HttpCheck_{
    				HttpCheck: &monitoringpb.UptimeCheckConfig_HttpCheck{
    					RequestMethod: monitoringpb.UptimeCheckConfig_HttpCheck_POST,
    					ContentType:   monitoringpb.UptimeCheckConfig_HttpCheck_URL_ENCODED,
    					Path:          "/",
    					Port:          80,
    					Body:          []byte(base64.URLEncoding.EncodeToString([]byte("key: value"))),
    				},
    			},
    			Timeout: &duration.Duration{Seconds: 10},
    			Period:  &duration.Duration{Seconds: 300},
    		},
    	}
    	config, err := client.CreateUptimeCheckConfig(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("CreateUptimeCheckConfig POST: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully created POST uptime check %q\n", config.GetDisplayName())
    	return config, nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void createUptimeCheck(
        String projectId, String displayName, String hostName, String pathName) throws IOException {
      CreateUptimeCheckConfigRequest request =
          CreateUptimeCheckConfigRequest.newBuilder()
              .setParent(ProjectName.format(projectId))
              .setUptimeCheckConfig(
                  UptimeCheckConfig.newBuilder()
                      .setDisplayName(displayName)
                      .setMonitoredResource(
                          MonitoredResource.newBuilder()
                              .setType("uptime_url")
                              .putLabels("host", hostName))
                      .setHttpCheck(HttpCheck.newBuilder().setPath(pathName).setPort(80))
                      .setTimeout(Duration.newBuilder().setSeconds(10))
                      .setPeriod(Duration.newBuilder().setSeconds(300)))
              .build();
      try (UptimeCheckServiceClient client = UptimeCheckServiceClient.create()) {
        UptimeCheckConfig config = client.createUptimeCheckConfig(request);
        System.out.println("Uptime check created: " + config.getName());
      } catch (Exception e) {
        usage("Exception creating uptime check: " + e.toString());
        throw e;
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[UptimeCheckServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment and edit the following lines of code.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const hostname = 'mydomain.com';
    
    const request = {
      // i.e. parent: 'projects/my-project-id'
      parent: client.projectPath(projectId),
      uptimeCheckConfig: {
        displayName: 'My Uptime Check',
        monitoredResource: {
          // See the Uptime Check docs for supported MonitoredResource types
          type: 'uptime_url',
          labels: {
            host: hostname,
          },
        },
        httpCheck: {
          path: '/',
          port: 80,
        },
        timeout: {
          seconds: 10,
        },
        period: {
          seconds: 300,
        },
      },
    };
    
    // Creates an uptime check config for a GCE instance
    const [uptimeCheckConfig] = await client.createUptimeCheckConfig(request);
    console.log('Uptime check created:');
    console.log(`ID: ${uptimeCheckConfig.name}`);
    console.log(`Display Name: ${uptimeCheckConfig.displayName}`);
    console.log('Resource: %j', uptimeCheckConfig.monitoredResource);
    console.log('Period: %j', uptimeCheckConfig.period);
    console.log('Timeout: %j', uptimeCheckConfig.timeout);
    console.log(`Check type: ${uptimeCheckConfig.check_request_type}`);
    console.log(
      'Check: %j',
      uptimeCheckConfig.httpCheck || uptimeCheckConfig.tcpCheck
    );
    console.log(
      `Content matchers: ${uptimeCheckConfig.contentMatchers
        .map(matcher => matcher.content)
        .join(', ')}`
    );
    console.log(`Regions: ${uptimeCheckConfig.selectedRegions.join(', ')}`);
    

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Api\MonitoredResource;
    use Google\Cloud\Monitoring\V3\Client\UptimeCheckServiceClient;
    use Google\Cloud\Monitoring\V3\CreateUptimeCheckConfigRequest;
    use Google\Cloud\Monitoring\V3\UptimeCheckConfig;
    
    /**
     * Example:
     * ```
     * create_uptime_check($projectId, 'myproject.appspot.com', 'Test Uptime Check!');
     * ```
     *
     * @param string $projectId Your project ID
     * @param string $hostName
     * @param string $displayName
     */
    function create_uptime_check($projectId, $hostName = 'example.com', $displayName = 'New uptime check')
    {
        $projectName = 'projects/' . $projectId;
        $uptimeCheckClient = new UptimeCheckServiceClient([
            'projectId' => $projectId,
        ]);
    
        $monitoredResource = new MonitoredResource();
        $monitoredResource->setType('uptime_url');
        $monitoredResource->setLabels(['host' => $hostName]);
    
        $uptimeCheckConfig = new UptimeCheckConfig();
        $uptimeCheckConfig->setDisplayName($displayName);
        $uptimeCheckConfig->setMonitoredResource($monitoredResource);
        $createUptimeCheckConfigRequest = (new CreateUptimeCheckConfigRequest())
            ->setParent($projectName)
            ->setUptimeCheckConfig($uptimeCheckConfig);
    
        $uptimeCheckConfig = $uptimeCheckClient->createUptimeCheckConfig($createUptimeCheckConfigRequest);
    
        printf('Created an uptime check: %s' . PHP_EOL, $uptimeCheckConfig->getName());
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_uptime_check_config_get(
        project_id: str, host_name: str = None, display_name: str = None
    ) -> uptime.UptimeCheckConfig:
        """Creates a new uptime check configuration
    
        Args:
            project_id: Google Cloud project id where the uptime check is created
            host_name: An example label's value for the "host" label
            display_name: A human friendly name of the configuration
    
        Returns:
            A structure that describes a new created uptime check
        """
        config = monitoring_v3.UptimeCheckConfig()
        config.display_name = display_name or "New GET uptime check"
        config.monitored_resource = {
            "type": "uptime_url",
            "labels": {"host": host_name or "example.com"},
        }
        config.http_check = {
            "request_method": monitoring_v3.UptimeCheckConfig.HttpCheck.RequestMethod.GET,
            "path": "/",
            "port": 80,
        }
        config.timeout = {"seconds": 10}
        config.period = {"seconds": 300}
    
        client = monitoring_v3.UptimeCheckServiceClient()
        new_config = client.create_uptime_check_config(
            request={"parent": project_id, "uptime_check_config": config}
        )
        pprint.pprint(new_config)
        return new_config
    
    
    def create_uptime_check_config_post(
        project_id: str, host_name: str = None, display_name: str = None
    ) -> uptime.UptimeCheckConfig:
        """Creates a new uptime check configuration
    
        Args:
            project_id: Google Cloud project id where the uptime check is created
            host_name: An example label's value for the "host" label
            display_name: A human friendly name of the configuration
    
        Returns:
            A structure that describes a new created uptime check
        """
        config = monitoring_v3.UptimeCheckConfig()
        config.display_name = display_name or "New POST uptime check"
        config.monitored_resource = {
            "type": "uptime_url",
            "labels": {"host": host_name or "example.com"},
        }
        config.http_check = {
            "request_method": monitoring_v3.UptimeCheckConfig.HttpCheck.RequestMethod.POST,
            "content_type": monitoring_v3.UptimeCheckConfig.HttpCheck.ContentType.URL_ENCODED,
            "body": "foo=bar".encode("utf-8"),
            "path": "/",
            "port": 80,
        }
        config.timeout = {"seconds": 10}
        config.period = {"seconds": 300}
    
        client = monitoring_v3.UptimeCheckServiceClient()
        new_config = client.create_uptime_check_config(
            request={"parent": project_id, "uptime_check_config": config}
        )
        pprint.pprint(new_config)
        return new_config
    
    

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    def create_uptime_check_config project_id: nil, host_name: nil, display_name: nil
      client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html).[uptime_check_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
      project_name = client.project_path project: project_id
      config = {
        display_name:       display_name.nil? ? "New uptime check" : display_name,
        monitored_resource: {
          type:   "uptime_url",
          labels: { "host" => host_name.nil? ? "example.com" : host_name }
        },
        http_check:         { path: "/", port: 80 },
        timeout:            { seconds: 10 },
        period:             { seconds: 300 }
      }
      new_config = client.create_uptime_check_config \
        parent:              project_name,
        uptime_check_config: config
      puts new_config.name
      new_config
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
