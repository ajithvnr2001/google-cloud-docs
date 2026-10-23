---
url: https://docs.cloud.google.com/appengine/docs/standard/outbound-ip-addresses/
title: Outbound IP addresses for App Engine services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:18.006994+00:00
---

# Outbound IP addresses for App Engine services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/outbound-ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Outbound IP addresses for App Engine services Stay organized with collections  Save and categorize content based on your preferences. 

The outbound services in the App Engine standard environment, such as the URL Fetch, Sockets, and Mail APIs, make use of a large pool of IP addresses. The IP address ranges in this pool are subject to routine changes. In fact, two sequential API calls from the same application may appear to originate from two different IP addresses.

If you need to know the IP addresses associated with outbound traffic from your service, you can either find the current IP address ranges that include the App Engine IP addresses, or set up a static IP address for your service.

## IP addresses for App Engine services

You can find the current IP address ranges for App Engine services by using two json files that are published by Google:

  * Google publishes a list of Google-owned IP addresses in [goog.json](https://www.gstatic.com/ipranges/goog.json).

  * Google also publishes a list of global and regional external IP addresses ranges available for customers' Google Cloud resources in [cloud.json](https://www.gstatic.com/ipranges/cloud.json).




Taking away all ranges in `cloud.json` from those in `goog.json` results in a large set of IP addresses that are used by global Google APIs and other Google services, including customer-facing products outside of Google Cloud. These lists are updated frequently.

You can use the following Python script to create a list of IP address ranges that include those used by Google APIs and services.

For information about running this script, see [How to run](https://github.com/GoogleCloudPlatform/networking-tools-python/tree/main/tools/cidr#how-to-run).
    
    
    from __future__ import print_function
    
    import json
    
    try:
        from urllib import urlopen
    except ImportError:
        from urllib.request import urlopen
        from urllib.error import HTTPError
    
    import netaddr
    
    IPRANGE_URLS = {
        "goog": "https://www.gstatic.com/ipranges/goog.json",
        "cloud": "https://www.gstatic.com/ipranges/cloud.json",
    }
    
    
    def read_url(url):
        try:
            return json.loads(urlopen(url).read())
        except (IOError, HTTPError):
            print("ERROR: Invalid HTTP response from %s" % url)
        except json.decoder.JSONDecodeError:
            print("ERROR: Could not parse HTTP response from %s" % url)
    
    
    def get_data(link):
        data = read_url(link)
        if data:
            print("{} published: {}".format(link, data.get("creationTime")))
            cidrs = netaddr.IPSet()
            for e in data["prefixes"]:
                if "ipv4Prefix" in e:
                    cidrs.add(e.get("ipv4Prefix"))
                if "ipv6Prefix" in e:
                    cidrs.add(e.get("ipv6Prefix"))
            return cidrs
    
    
    def main():
        cidrs = {group: get_data(link) for group, link in IPRANGE_URLS.items()}
        if len(cidrs) != 2:
            raise ValueError("ERROR: Could process data from Google")
        print("IP ranges for Google APIs and services default domains:")
        for ip in (cidrs["goog"] - cidrs["cloud"]).iter_cidrs():
            print(ip)
    
    
    if __name__ == "__main__":
        main()

**Note:** In the past, Google Cloud published a list of IP address ranges in the `_spf.google.com` DNS TXT record (and the records it referenced). While this DNS TXT record continues to be accurate for [SPF purposes](https://support.google.com/a/answer/33786), it does not contain the complete set of possible IP address ranges used by Google APIs and services.

## Set up a static outbound IP address

To set up a static IP address for your App Engine standard environment service, use [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access) with Cloud Router and [Cloud NAT](https://docs.cloud.google.com/nat/docs). By using Serverless VPC Access, you can send egress traffic to your Virtual Private Cloud (VPC) network. By using a network address translation (NAT) gateway on your VPC, you can route the App Engine traffic through a dedicated IP address.

Routing your traffic through Cloud NAT does not cause an additional hop in your networking stack since the Cloud NAT gateway and the Cloud Router provide only a control plane and the packets do not pass through the Cloud NAT gateway or the Cloud Router.

**Note:** Serverless VPC Access and Cloud NAT can both incur costs. Review [Serverless VPC Access pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing) and [Cloud NAT pricing](https://docs.cloud.google.com/vpc/network-pricing#nat-pricing).

The following steps show how to set up a static outbound IP address for your App Engine standard environment service.

  1. Make sure that you have the [roles/compute.networkAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) role or a custom role with the same permissions.

  2. Create a subnetwork (subnet) inside your VPC network for App Engine traffic. This ensures that other resources in your VPC network cannot use the static IP address.
         
         gcloud compute networks subnets create SUBNET_NAME \
             --range=RANGE \
             --network=NETWORK_NAME \
             --region=REGION

In the command above, replace:

     * `SUBNET_NAME` with a name you want to give to the subnet.
     * `RANGE` with the [IP range](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges) in CIDR format you want to assign to this subnet (e.g. `10.124.0.0/28`)
     * `NETWORK_NAME` with the name of your VPC network.
     * `REGION` with the region of your App Engine service.
  3. Connect your App Engine service to the subnet.

Follow the guide [Connecting to a VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc), and specify the name of the subnet you created in the previous step for the connector subnet.

  4. Create a new Cloud Router. Cloud Router is a necessary control plane component for Cloud NAT.
         
         gcloud compute routers create ROUTER_NAME \
             --network=NETWORK_NAME \
             --region=REGION

In the command above, replace:

     * `ROUTER_NAME` with a name for the Cloud Router resource you want to create.
     * `NETWORK_NAME` with the name of your VPC network.
     * `REGION` with the region in which you want to create a NAT gateway.
  5. Reserve a static IP address.

This is the address that your service will use to send outgoing traffic. A reserved IP address resource retains the underlying IP address when the resource it is associated with is deleted and re-created. This IP address counts towards the static IP address quotas in your Google Cloud project.
         
         gcloud compute addresses create ORIGIN_IP_NAME \
             --region=REGION

In the command above, replace:

     * `ORIGIN_IP_NAME` with the name you want to assign to the IP address resource.
     * `REGION` with the region that will run the Cloud NAT router. Ideally the same region as your App Engine service to minimize latency and network costs.

Use the [`compute addresses describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/describe) to view the result:
    
    gcloud compute addresses describe ORIGIN_IP_NAME

  6. Create a Cloud NAT gateway and specify your IP address.

Traffic originating from your subnet will go through this gateway and use the static IP address that you reserved in the previous step.
         
         gcloud compute routers nats create NAT_NAME \
             --router=ROUTER_NAME \
             --region=REGION \
             --nat-custom-subnet-ip-ranges=SUBNET_NAME \
             --nat-external-ip-pool=ORIGIN_IP_NAME
           

In the command above, replace:

     * `NAT_NAME` with a name for the Cloud NAT gateway resource you want to create.
     * `ROUTER_NAME` with the name of your Cloud Router.
     * `REGION` with the region in which you want to create a NAT gateway.
     * `ORIGIN_IP_NAME` with the name of the reserved IP address resource you created in the previous step.
  7. Set the Serverless VPC Access [egress setting](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#egress) to `all-traffic`.

By default, App Engine services that use Serverless VPC Access only send internal traffic to your VPC network. In order to send traffic with external destinations to your VPC network so that it will have the static IP address that you specified, you must change the egress setting.

Specify the egress setting in the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) file for your service:
         
         vpc_access_connector:
         name: projects/PROJECT_ID/locations/REGION/connectors/CONNECTOR_NAME
         egress_setting: all-traffic

Replace:

     * `PROJECT_ID` with your Google Cloud project ID.
     * `REGION` with the region your connector is in.
     * `CONNECTOR_NAME` with the [name](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#create-connector) of your connector.



Deploy the service:
    
    
     gcloud app deploy

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
