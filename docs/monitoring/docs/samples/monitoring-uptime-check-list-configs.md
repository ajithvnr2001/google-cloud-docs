---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-list-configs/
title: List uptime checks \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:32.894646+00:00
---

# List uptime checks  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-list-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  List uptime checks Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list uptime check configs.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object ListUptimeCheckConfigs(string projectId)
    {
        var client = UptimeCheckServiceClient.Create();
        var configs = client.ListUptimeCheckConfigs(new ProjectName(projectId));
        foreach (UptimeCheckConfig config in configs)
        {
            Console.WriteLine(config.Name);
        }
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // list is an example of listing the uptime checks in projectID.
    func list(w io.Writer, projectID string) error {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	req := &monitoringpb.ListUptimeCheckConfigsRequest{
    		Parent: "projects/" + projectID,
    	}
    	it := client.ListUptimeCheckConfigs(ctx, req)
    	for {
    		config, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListUptimeCheckConfigs: %w", err)
    		}
    		fmt.Fprintln(w, config)
    	}
    	fmt.Fprintln(w, "Done listing uptime checks")
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void listUptimeChecks(String projectId) throws IOException {
      ListUptimeCheckConfigsRequest request =
          ListUptimeCheckConfigsRequest.newBuilder().setParent(ProjectName.format(projectId)).build();
      try (UptimeCheckServiceClient client = UptimeCheckServiceClient.create()) {
        ListUptimeCheckConfigsPagedResponse response = client.listUptimeCheckConfigs(request);
        for (UptimeCheckConfig config : response.iterateAll()) {
          System.out.println(config.getDisplayName());
        }
      } catch (Exception e) {
        usage("Exception listing uptime checks: " + e.toString());
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
    
    const request = {
      parent: client.projectPath(projectId),
    };
    
    // Retrieves an uptime check config
    const [uptimeCheckConfigs] = await client.listUptimeCheckConfigs(request);
    
    uptimeCheckConfigs.forEach(uptimeCheckConfig => {
      console.log(`ID: ${uptimeCheckConfig.name}`);
      console.log(`  Display Name: ${uptimeCheckConfig.displayName}`);
      console.log('  Resource: %j', uptimeCheckConfig.monitoredResource);
      console.log('  Period: %j', uptimeCheckConfig.period);
      console.log('  Timeout: %j', uptimeCheckConfig.timeout);
      console.log(`  Check type: ${uptimeCheckConfig.check_request_type}`);
      console.log(
        '  Check: %j',
        uptimeCheckConfig.httpCheck || uptimeCheckConfig.tcpCheck
      );
      console.log(
        `  Content matchers: ${uptimeCheckConfig.contentMatchers
          .map(matcher => matcher.content)
          .join(', ')}`
      );
      console.log(`  Regions: ${uptimeCheckConfig.selectedRegions.join(', ')}`);
    });
    

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\UptimeCheckServiceClient;
    use Google\Cloud\Monitoring\V3\ListUptimeCheckConfigsRequest;
    
    /**
     * Example:
     * ```
     * list_uptime_checks($projectId);
     * ```
     */
    function list_uptime_checks(string $projectId): void
    {
        $projectName = 'projects/' . $projectId;
        $uptimeCheckClient = new UptimeCheckServiceClient([
            'projectId' => $projectId,
        ]);
        $listUptimeCheckConfigsRequest = (new ListUptimeCheckConfigsRequest())
            ->setParent($projectName);
    
        $pages = $uptimeCheckClient->listUptimeCheckConfigs($listUptimeCheckConfigsRequest);
    
        foreach ($pages->iteratePages() as $page) {
            foreach ($page as $uptimeCheck) {
                print($uptimeCheck->getName() . PHP_EOL);
            }
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_uptime_check_configs(project_id: str) -> pagers.ListUptimeCheckConfigsPager:
        """Gets all uptime checks defined in the Google Cloud project
    
        Args:
            project_id: Google Cloud project id
    
        Returns:
            A list of configurations.
            Iterating over this object will yield results and resolve additional pages automatically.
        """
        client = monitoring_v3.UptimeCheckServiceClient()
        configs = client.list_uptime_check_configs(request={"parent": project_id})
    
        for config in configs:
            pprint.pprint(config)
        return configs
    
    

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    def list_uptime_check_configs project_id
      client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[uptime_check_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
      project_name = client.project_path project: project_id
      configs = client.list_uptime_check_configs parent: project_name
    
      configs.each { |config| puts config.name }
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
