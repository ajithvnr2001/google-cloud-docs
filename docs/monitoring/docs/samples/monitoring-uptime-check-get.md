---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-get/
title: Get an uptime check \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:36.671684+00:00
---

# Get an uptime check  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Get an uptime check Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to get details of an uptime check config.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object GetUptimeCheckConfig(string configName)
    {
        var client = UptimeCheckServiceClient.Create();
        UptimeCheckConfig config = client.GetUptimeCheckConfig(configName);
        if (config == null)
        {
            Console.Error.WriteLine(
                "No configuration found with the name {0}", configName);
            return -1;
        }
        Console.WriteLine("Name: {0}", config.Name);
        Console.WriteLine("Display Name: {0}", config.DisplayName);
        Console.WriteLine("Http Path: {0}", config.HttpCheck.Path);
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // get is an example of getting an uptime check. resourceName should be
    // of the form `projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID]`.
    func get(w io.Writer, resourceName string) (*monitoringpb.UptimeCheckConfig, error) {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	req := &monitoringpb.GetUptimeCheckConfigRequest{
    		Name: resourceName,
    	}
    	config, err := client.GetUptimeCheckConfig(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("GetUptimeCheckConfig: %w", err)
    	}
    	fmt.Fprintf(w, "Config: %v", config)
    	return config, nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void getUptimeCheckConfig(String checkName) throws IOException {
      // Create UptimeCheckServiceSettings instance for add retry mechanism
      UptimeCheckServiceSettings.Builder uptimeCheckServiceSettingsBuilder =
          UptimeCheckServiceSettings.newBuilder();
      uptimeCheckServiceSettingsBuilder
          .getUptimeCheckConfigSettings()
          .setRetrySettings(
              uptimeCheckServiceSettingsBuilder
                  .getUptimeCheckConfigSettings()
                  .getRetrySettings()
                  .toBuilder()
                  .setInitialRetryDelay(org.threeten.bp.Duration.ofMillis(100L))
                  .setRetryDelayMultiplier(1.3)
                  .setMaxRetryDelay(MAX_RECONNECT_BACKOFF_TIME)
                  .setInitialRpcTimeout(MAX_RECONNECT_BACKOFF_TIME)
                  .setRpcTimeoutMultiplier(1.0)
                  .setMaxRpcTimeout(MAX_RECONNECT_BACKOFF_TIME)
                  .setTotalTimeout(MAX_RECONNECT_BACKOFF_TIME)
                  .setMaxAttempts(6)
                  .build());
      UptimeCheckServiceSettings uptimeCheckServiceSettings =
          uptimeCheckServiceSettingsBuilder.build();
    
      // create UptimeCheckServiceClient with retry setting
      try (UptimeCheckServiceClient client =
          UptimeCheckServiceClient.create(uptimeCheckServiceSettings)) {
        UptimeCheckConfig config = client.getUptimeCheckConfig(checkName);
        if (config != null) {
          System.out.println(config.toString());
        } else {
          System.out.println("No uptime check config found with ID " + checkName);
        }
      } catch (Exception e) {
        usage("Exception getting uptime check: " + e.toString());
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
    // const uptimeCheckConfigId = 'YOUR_UPTIME_CHECK_CONFIG_ID';
    
    const request = {
      // i.e. name: 'projects/my-project-id/uptimeCheckConfigs/My-Uptime-Check
      name: client.projectUptimeCheckConfigPath(projectId, uptimeCheckConfigId),
    };
    
    console.log(`Retrieving ${request.name}`);
    
    // Retrieves an uptime check config
    const [uptimeCheckConfig] = await client.getUptimeCheckConfig(request);
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
    
    
    use Google\Cloud\Monitoring\V3\Client\UptimeCheckServiceClient;
    use Google\Cloud\Monitoring\V3\GetUptimeCheckConfigRequest;
    
    /**
     * Example:
     * ```
     * get_uptime_check($projectId, $configName);
     * ```
     *
     * @param string $projectId Your project ID
     * @param string $configName
     */
    function get_uptime_check($projectId, $configName)
    {
        $uptimeCheckClient = new UptimeCheckServiceClient([
            'projectId' => $projectId,
        ]);
        $getUptimeCheckConfigRequest = (new GetUptimeCheckConfigRequest())
            ->setName($configName);
    
        $uptimeCheck = $uptimeCheckClient->getUptimeCheckConfig($getUptimeCheckConfigRequest);
    
        print('Retrieved an uptime check:' . PHP_EOL);
        print($uptimeCheck->serializeToJsonString() . PHP_EOL);
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_uptime_check_config(config_name: str) -> uptime.UptimeCheckConfig:
        """Reads the uptime check configuration
    
        Args:
            config_name: Uptime check configuration identity
    
        Returns:
            A structure that describes the updated uptime check
        """
        client = monitoring_v3.UptimeCheckServiceClient()
        config = client.get_uptime_check_config(request={"name": config_name})
        pprint.pprint(config)
        return config
    
    

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    def get_uptime_check_config config_name
      client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[uptime_check_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
      config = client.get_uptime_check_config name: config_name
      pp config.to_h
      config
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
