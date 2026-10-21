---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-update/
title: Update an uptime check \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:55.417488+00:00
---

# Update an uptime check  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Update an uptime check Stay organized with collections  Save and categorize content based on your preferences. 

Change an update check.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object UpdateUptimeCheck(string configName,
        string newHttpPath, string newDisplayName)
    {
        var client = UptimeCheckServiceClient.Create();
        var config = client.GetUptimeCheckConfig(configName);
        var fieldMask = new FieldMask();
        if (newDisplayName != null)
        {
            config.DisplayName = newDisplayName;
            fieldMask.Paths.Add("display_name");
        }
        if (newHttpPath != null)
        {
            config.HttpCheck.Path = newHttpPath;
            fieldMask.Paths.Add("http_check.path");
        }
        client.UpdateUptimeCheckConfig(config);
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // update is an example of updating an uptime check. resourceName should be
    // of the form `projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID]`.
    func update(w io.Writer, resourceName, displayName, httpCheckPath string) (*monitoringpb.UptimeCheckConfig, error) {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	getReq := &monitoringpb.GetUptimeCheckConfigRequest{
    		Name: resourceName,
    	}
    	config, err := client.GetUptimeCheckConfig(ctx, getReq)
    	if err != nil {
    		return nil, fmt.Errorf("GetUptimeCheckConfig: %w", err)
    	}
    	config.DisplayName = displayName
    	config.GetHttpCheck().Path = httpCheckPath
    	req := &monitoringpb.UpdateUptimeCheckConfigRequest{
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"display_name", "http_check.path"},
    		},
    		UptimeCheckConfig: config,
    	}
    	config, err = client.UpdateUptimeCheckConfig(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("UpdateUptimeCheckConfig: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully updated %v", resourceName)
    	return config, nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void updateUptimeCheck(String checkName, String hostName, String pathName)
        throws IOException {
    
      UpdateUptimeCheckConfigRequest request =
          UpdateUptimeCheckConfigRequest.newBuilder()
              .setUpdateMask(FieldMask.newBuilder().addPaths("http_check.path"))
              .setUptimeCheckConfig(
                  UptimeCheckConfig.newBuilder()
                      .setName(checkName)
                      .setMonitoredResource(
                          MonitoredResource.newBuilder()
                              .setType("uptime_url")
                              .putLabels("host", hostName))
                      .setHttpCheck(HttpCheck.newBuilder().setPath(pathName).setPort(80))
                      .setTimeout(Duration.newBuilder().setSeconds(10))
                      .setPeriod(Duration.newBuilder().setSeconds(300)))
              .build();
      try (UptimeCheckServiceClient client = UptimeCheckServiceClient.create()) {
        UptimeCheckConfig config = client.updateUptimeCheckConfig(request);
        System.out.println("Uptime check updated: \n" + config.toString());
      } catch (Exception e) {
        usage("Exception updating uptime check: " + e.toString());
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
    // const displayName = 'A New Display Name';
    // const path = '/some/path';
    
    const request = {
      // i.e. name: 'projects/my-project-id/uptimeCheckConfigs/My-Uptime-Check
      name: client.projectUptimeCheckConfigPath(projectId, uptimeCheckConfigId),
    };
    
    console.log(`Updating ${request.name} to ${displayName}`);
    
    // Updates the display name and path on an uptime check config
    request.uptimeCheckConfig = {
      name: request.name,
      displayName: displayName,
      httpCheck: {
        path: path,
      },
    };
    
    request.updateMask = {
      paths: ['display_name', 'http_check.path'],
    };
    
    const [response] = await client.updateUptimeCheckConfig(request);
    console.log(`${response.name} config updated.`);
    

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\UptimeCheckServiceClient;
    use Google\Cloud\Monitoring\V3\GetUptimeCheckConfigRequest;
    use Google\Cloud\Monitoring\V3\UpdateUptimeCheckConfigRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Example:
     * ```
     * update_uptime_checks($projectId);
     * ```
     */
    function update_uptime_checks(
        string $projectId,
        string $configName,
        string $newDisplayName = null,
        string $newHttpCheckPath = null
    ): void {
        $uptimeCheckClient = new UptimeCheckServiceClient([
            'projectId' => $projectId,
        ]);
        $getUptimeCheckConfigRequest = (new GetUptimeCheckConfigRequest())
            ->setName($configName);
    
        $uptimeCheck = $uptimeCheckClient->getUptimeCheckConfig($getUptimeCheckConfigRequest);
        $fieldMask = new FieldMask();
        if ($newDisplayName) {
            $fieldMask->getPaths()[] = 'display_name';
            $uptimeCheck->setDisplayName($newDisplayName);
        }
        if ($newHttpCheckPath) {
            $paths = $fieldMask->getPaths()[] = 'http_check.path';
            $uptimeCheck->getHttpCheck()->setPath($newHttpCheckPath);
        }
        $updateUptimeCheckConfigRequest = (new UpdateUptimeCheckConfigRequest())
            ->setUptimeCheckConfig($uptimeCheck)
            ->setUpdateMask($fieldMask);
    
        $uptimeCheckClient->updateUptimeCheckConfig($updateUptimeCheckConfigRequest);
    
        print($uptimeCheck->serializeToString() . PHP_EOL);
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_uptime_check_config(
        config_name: str, new_display_name: str = None, new_http_check_path: str = None
    ) -> uptime.UptimeCheckConfig:
        """Creates a new uptime check configuration
    
        Args:
            config_name: Uptime check configuration identity
            new_display_name: A new human friendly name of the configuration
            new_http_check_path: A new HTTP endpoint of the configuration
    
        Returns:
            A structure that describes the updated uptime check
        """
        client = monitoring_v3.UptimeCheckServiceClient()
        config = client.get_uptime_check_config(request={"name": config_name})
        field_mask = field_mask_pb2.FieldMask()
        if new_display_name:
            field_mask.paths.append("display_name")
            config.display_name = new_display_name
        if new_http_check_path:
            field_mask.paths.append("http_check.path")
            config.http_check.path = new_http_check_path
        changed_config = client.update_uptime_check_config(
            request={"uptime_check_config": config, "update_mask": field_mask}
        )
        pprint.pprint(changed_config)
        return changed_config
    
    

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    def update_uptime_check_config config_name:         nil,
                                   new_display_name:    nil,
                                   new_http_check_path: nil
      client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html).[uptime_check_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
      config = { name: config_name }
      field_mask = { paths: [] }
      unless new_display_name.to_s.empty?
        field_mask[:paths].push "display_name"
        config[:display_name] = new_display_name
      end
      unless new_http_check_path.to_s.empty?
        field_mask[:paths].push "http_check.path"
        config[:http_check] = { path: new_http_check_path }
      end
      client.update_uptime_check_config uptime_check_config: config,
                                        update_mask:         field_mask
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
