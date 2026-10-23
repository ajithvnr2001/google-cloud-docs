---
url: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-list-ips/
title: List uptime check IP addresses \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:35.530306+00:00
---

# List uptime check IP addresses  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/docs/samples/monitoring-uptime-check-list-ips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Samples ](https://docs.cloud.google.com/monitoring/docs/samples)



#  List uptime check IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list uptime check IP addresses.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List uptime-check server IP addresses](https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks)



## Code sample

### C#

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    public static object ListUptimeCheckIps()
    {
        var client = UptimeCheckServiceClient.Create();
        var ips = client.ListUptimeCheckIps(new ListUptimeCheckIpsRequest());
        foreach (UptimeCheckIp ip in ips)
        {
            Console.WriteLine("{0,20} {1}", ip.IpAddress, ip.Location);
        }
        return 0;
    }
    

### Go

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // listIPs is an example of listing uptime check IPs.
    func listIPs(w io.Writer) error {
    	ctx := context.Background()
    	client, err := monitoring.NewUptimeCheckClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewUptimeCheckClient: %w", err)
    	}
    	defer client.Close()
    	req := &monitoringpb.ListUptimeCheckIpsRequest{}
    	it := client.ListUptimeCheckIps(ctx, req)
    	for {
    		config, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListUptimeCheckIps: %w", err)
    		}
    		fmt.Fprintln(w, config)
    	}
    	fmt.Fprintln(w, "Done listing uptime check IPs")
    	return nil
    }
    

### Java

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private static void listUptimeCheckIps() throws IOException {
      try (UptimeCheckServiceClient client = UptimeCheckServiceClient.create()) {
        ListUptimeCheckIpsPagedResponse response =
            client.listUptimeCheckIps(ListUptimeCheckIpsRequest.newBuilder().build());
        for (UptimeCheckIp config : response.iterateAll()) {
          System.out.println(config.getRegion() + " - " + config.getIpAddress());
        }
      } catch (Exception e) {
        usage("Exception listing uptime IPs: " + e.toString());
        throw e;
      }
    }

### Node.js

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const monitoring = require('[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)');
    
    // Creates a client
    const client = new monitoring.[UptimeCheckServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)();
    
    // List uptime check IPs
    const [uptimeCheckIps] = await client.listUptimeCheckIps();
    uptimeCheckIps.forEach(uptimeCheckIp => {
      console.log(
        uptimeCheckIp.region,
        uptimeCheckIp.location,
        uptimeCheckIp.ipAddress
      );
    });
    

### PHP

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Monitoring\V3\Client\UptimeCheckServiceClient;
    use Google\Cloud\Monitoring\V3\ListUptimeCheckIpsRequest;
    
    /**
     * Example:
     * ```
     * list_uptime_check_ips($projectId);
     * ```
     */
    function list_uptime_check_ips(string $projectId): void
    {
        $uptimeCheckClient = new UptimeCheckServiceClient([
            'projectId' => $projectId,
        ]);
        $listUptimeCheckIpsRequest = new ListUptimeCheckIpsRequest();
    
        $pages = $uptimeCheckClient->listUptimeCheckIps($listUptimeCheckIpsRequest);
    
        foreach ($pages->iteratePages() as $page) {
            $ips = $page->getResponseObject()->getUptimeCheckIps();
            foreach ($ips as $ip) {
                printf(
                    'ip address: %s, region: %s, location: %s' . PHP_EOL,
                    $ip->getIpAddress(),
                    $ip->getRegion(),
                    $ip->getLocation()
                );
            }
        }
    }

### Python

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_uptime_check_ips() -> pagers.ListUptimeCheckIpsPager:
        """Gets all locations and IP addresses used by uptime check servers
    
        Returns:
            A list of locations and IP addresses of uptime check servers.
            Iterating over this object will yield results and resolve additional pages automatically.
        """
        client = monitoring_v3.UptimeCheckServiceClient()
        ips = client.list_uptime_check_ips(request={})
        print(
            tabulate.tabulate(
                [(ip.region, ip.location, ip.ip_address) for ip in ips],
                ("region", "location", "ip_address"),
            )
        )
        return ips
    
    

### Ruby

To authenticate to Monitoring, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    gem "google-cloud-monitoring"
    require "google/cloud/monitoring"
    
    def list_ips
      client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html).[uptime_check_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    
      # Iterate over all results.
      client.list_uptime_check_ips({}).each do |element|
        puts "#{element.location} #{element.[ip_address](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckIp.html)}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudmonitoring). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
