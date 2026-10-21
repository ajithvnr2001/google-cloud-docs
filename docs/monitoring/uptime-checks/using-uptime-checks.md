---
url: https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks/
title: List uptime-check server IP addresses \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:25.927042+00:00
---

# List uptime-check server IP addresses  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/uptime-checks/using-uptime-checks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  List uptime-check server IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

To allow incoming probes through your firewall, you can retrieve the list of IP addresses used by Cloud Monitoring uptime-check servers. You can also use these IP addresses and the `User-Agent` request header to identify uptime-check traffic in your service's logs.

## List IP addresses

When you're checking a service that is behind a firewall, you can configure your service's firewall to accept traffic from the current set of IP addresses used for uptime checking. To get these IP addresses, use the following instructions:

### Console

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Uptime checks** page: 

[Go to **Uptime checks**](https://console.cloud.google.com/monitoring/uptime)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the **Uptime checks** menu, click _get_app_ **Download**. A file `uptime-source-ips.txt` is downloaded and contains the IP addresses.



### gcloud

Run the [`gcloud monitoring uptime list-ips`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/list-ips) command:
    
    
    gcloud monitoring uptime list-ips
    

The method returns the following information for each IP address:

  * The IP address, not a range, in IPv4 or IPv6 format.
  * The region: `USA`, `EUROPE`, `SOUTH_AMERICA`, or `ASIA_PACIFIC`.
  * The location within the region.



### API

Call the [`uptimeCheckIps.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/uptimeCheckIps/list) method of the Monitoring API.

The method returns the following information for each IP address:

  * The region: `USA`, `EUROPE`, `SOUTH_AMERICA`, or `ASIA_PACIFIC`.
  * A more specific location within the region.
  * The IP address, not a range, in IPv4 or IPv6 format.



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
      client = Google::Cloud::[Monitoring](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring.html).[uptime_check_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring.html)
    
      # Iterate over all results.
      client.list_uptime_check_ips({}).each do |element|
        puts "#{element.location} #{element.[ip_address](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckIp.html)}"
      end
    end

Uptime checks can come from any of the IP addresses, but only one address from each geographic location is used for each time interval. The geographic locations are listed in the uptime checks dashboard. You can also use free, web-based services to identify the registered locations of the IP addresses you downloaded.

## Identify uptime-check traffic in logs

You can identify requests from the uptime-check servers by the following information in your service's [request logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface):

  * **ip** : The `ip` field contains one of the addresses used by the uptime-check servers. For information about how to list all IP addresses, see List IP addresses.
  * **User-Agent** : The `User-Agent` header value is always the following:
        
        GoogleStackdriverMonitoring-UptimeChecks(https://cloud.google.com/monitoring)
        

Specifying a `User-Agent` custom header results in a form validation error and prevents the check configuration from being saved.




## What's next

  * [Manage uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/manage)
  * [Create alerting policies for uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/uptime-alerting-policies)
  * [Chart uptime-check metrics](https://docs.cloud.google.com/monitoring/charts/uptime-charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
