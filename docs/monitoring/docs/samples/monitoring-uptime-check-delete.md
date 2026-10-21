---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-delete/
title: Delete an uptime check \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:53.741399+00:00
---

# Delete an uptime check  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  Delete an uptime check Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to delete an uptime check config.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object DeleteUptimeCheckConfig(string configName)
    {
        var client = UptimeCheckServiceClient.Create();
        client.DeleteUptimeCheckConfig(configName);
        Console.WriteLine($"Deleted {configName}");
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // delete is an example of deleting an uptime check. resourceName should be
    // of the form `projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID]`.
    func delete(w io.Writer, resourceName string) error {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	req := &monitoringpb.DeleteUptimeCheckConfigRequest{
    		Name: resourceName,
    	}
    	if err := client.DeleteUptimeCheckConfig(ctx, req); err != nil {
    		return fmt.Errorf("DeleteUptimeCheckConfig: %w", err)
    	}
    	fmt.Fprintf(w, "Successfully deleted %q", resourceName)
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void deleteUptimeCheckConfig(String checkName) throws IOException {
      try (UptimeCheckServiceClient client = UptimeCheckServiceClient.create()) {
        client.deleteUptimeCheckConfig(checkName);
      } catch (Exception e) {
        usage("Exception deleting uptime check: " + e.toString());
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
    
    console.log(`Deleting ${request.name}`);
    
    // Delete an uptime check config
    await client.deleteUptimeCheckConfig(request);
    console.log(`${request.name} deleted.`);
    

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\UptimeCheckServiceClient;
    use Google\Cloud\Monitoring\V3\DeleteUptimeCheckConfigRequest;
    
    /**
     * Example:
     * ```
     * delete_uptime_check($projectId, $configName);
     * ```
     *
     * @param string $projectId Your project ID
     * @param string $configName
     */
    function delete_uptime_check($projectId, $configName)
    {
        $uptimeCheckClient = new UptimeCheckServiceClient([
            'projectId' => $projectId,
        ]);
        $deleteUptimeCheckConfigRequest = (new DeleteUptimeCheckConfigRequest())
            ->setName($configName);
    
        $uptimeCheckClient->deleteUptimeCheckConfig($deleteUptimeCheckConfigRequest);
    
        printf('Deleted an uptime check: ' . $configName . PHP_EOL);
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # `config_name` is the `name` field of an UptimeCheckConfig.
    # See https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs#UptimeCheckConfig.
    def delete_uptime_check_config(config_name: str) -> None:
        """Deletes the uptime check configuration
    
        Args:
            config_name: Uptime check configuration identity
        """
        client = monitoring_v3.UptimeCheckServiceClient()
        client.delete_uptime_check_config(request={"name": config_name})
        print("Deleted ", config_name)
    
    

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    def delete_uptime_check_config config_name
      client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html).[uptime_check_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
      client.delete_uptime_check_config name: config_name
      puts "Deleted #{config_name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
