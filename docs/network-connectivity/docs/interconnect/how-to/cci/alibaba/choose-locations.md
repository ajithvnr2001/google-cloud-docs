---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations/
title: Choose your locations \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:27.534440+00:00
---

# Choose your locations  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Choose your locations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page includes instructions about Alibaba products. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For the most current information, refer to the [Alibaba Cloud documentation](https://www.alibabacloud.com/help/) . 

When you use Cross-Cloud Interconnect, Google provisions physical connections on your behalf between the Google Cloud network and the Alibaba Cloud network. 

Before Google can establish these connections, you must order ports from both Google and Alibaba. In preparation for that process, identify the Google Cloud locations and the corresponding Alibaba locations that you want to use for your connections.

## Best practices for selecting a location

When deciding where to place your connections, consider questions such as the following: 

  * Where are most of your Google Cloud resources?
  * Where are most of your Alibaba resources?



If your resources from both clouds are in the same place, then the choice is simple. However, if they are not, consider whether you want your connections to be closer to your Google Cloud resources or closer to your Alibaba resources. If the connections are closer to your Alibaba resources, then your traffic spends more time traveling on the Google network, which in general is desirable. However, you should also consider the outbound data transfer costs that you're likely to incur from both clouds.

## Factors affected by location

This section describes factors that are affected by your location choice.

### VLAN attachments 

After your Cross-Cloud Interconnect connection is established, you must configure VLAN attachments in Google Cloud. A VLAN attachment is a logical connection between your remote cloud network and a single region in your Virtual Private Cloud (VPC) network.

When you choose a location for your ports, you limit the number of regions where you can place both VLAN attachments and Express Connect virtual circuits. For this reason, the supported locations table includes a column for the Google Cloud and Alibaba Cloud regions that are served by each port location.

**Note:** In Google Cloud, the location of the VLAN attachment doesn't have to limit which Google Cloud regions receive your Alibaba routes. To advertise Alibaba routes to all of your Google Cloud regions, configure [global dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes).

### Edge availability domains

Each metropolitan area has two Google Cloud edge availability domains. Two domains in the same metropolitan area are not scheduled to be down for maintenance at the same time. For this reason, when you select a location for a primary and redundant port, each port must use a different edge availability domain within the same metropolitan area. This is true regardless of how you order your ports. However, when you use the Google Cloud CLI, you must specify each edge availability domain explicitly. When you use the Google Cloud console, you simply select a location, and Google Cloud reserves a port for you in each domain.

In the gcloud CLI version of the location name, the edge availability domain is the second piece of information. For example, if the location name is `iad-zone1-1`, the edge availability domain is `zone1`. If the location name is `iad-zone2-1`, the edge availability zone is `zone2`.

### Colocation facilities

Google typically provisions each connection within a single colocation facility. However, sometimes connections are created between adjoining facilities that are operated by the same provider. In either case, generally you don't need to know the facility name. For this reason, the supported locations table does not identify specific facilities. 

## List of supported locations

The following table lists the supported Alibaba locations and the corresponding Google Cloud locations. 

You must specify the Google Cloud location of your Cross-Cloud Interconnect port, and additionally specify where in your other cloud provider to connect it. This latter Alibaba location is referred to as the _remote location_ in this documentation set and within Google Cloud. Make sure to use the remote location name when you order the Cross-Cloud Interconnect. Your remote cloud provider has a different, although similar, name for the location, which you use when you order the port with that cloud provider.

For each location name, some syntax variations exist. For example:

  * The remote location name varies depending on whether you are interacting with Alibaba or Google Cloud.
  * When interacting with Google Cloud, the Google Cloud console displays the remote location _description_ next to the location name to help you choose the correct location.
  * In Google Cloud, the Google Cloud console Cloud Interconnect location (not the remote location) shows facility information rather than the actual Cloud Interconnect location name.



**Note:** You can also use the gcloud CLI to list locations. For more information, see the reference page for the [`gcloud compute interconnects remote-locations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/remote-locations/list). 

**Note:** For the most up-to-date information about Alibaba Cloud locations, see [Alibaba Cloud Regions](https://www.alibabacloud.com/global-locations) in the Alibaba Cloud documentation.Google Cloud regions | Alibaba Cloud regions | Metropolitan area | Remote location | Google Cloud locations  
---|---|---|---|---  
Google Cloud | Alibaba Cloud  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * cn-hongkong (Hong Kong)

| Hong Kong|  alibaba-hk-kwaichung-a  | HK-KwaiChung-A | 

  * hkg-zone1-1118
  * hkg-zone2-1118

  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * ap-southeast-1 (Singapore)

| Singapore|  alibaba-ap-sg-singapore-a  | Singapore-A | 

  * sin-zone1-2260
  * sin-zone2-2260

  
  
  * me-central1
  * me-central2
  * me-west1
  * europe-central1
  * europe-central2
  * europe-north1
  * europe-southwest1
  * europe-west1
  * europe-west2
  * europe-west3
  * europe-west4
  * europe-west6
  * europe-west8
  * europe-west9
  * europe-west10
  * europe-west12

| 

  * eu-central-1 (Frankfurt)

| Frankfurt|  alibaba-germany-frankfurt-b  | Germany-Frankfurt-B | 

  * fra-zone1-683
  * fra-zone2-683

  
  
  * northamerica-northeast1
  * northamerica-northeast2
  * us-central1
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4

| 

  * us-east-1 (Virginia)

| Washington D.C.|  alibaba-us-ashburn-a  | US-Ashburn-A | 

  * iad-zone1-1
  * iad-zone2-1

  
  
  * northamerica-northeast1
  * northamerica-northeast2
  * us-central1
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4

| 

  * us-east-1 (Virginia)

| Virginia|  alibaba-us-virginia-d  | US-Virginia-D | 

  * iad-zone1-5467
  * iad-zone2-5467

  
  
## Verify availability

After you've identified a location that you want to use, double-check that it has an available Express Connect port with your intended capacity. This step is helpful because the availability of ports can change without notice.

## Note locations and regions

After you've reviewed the previous sections, make a note of the following values:

  * The remote location, as it's known in Google Cloud, and the Google Cloud location. You need these values when you [order your Cross-Cloud Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-google-connections).
  * The remote location, as it's known in Alibaba Cloud, and the region where you want to place the connection resources. You need these values when you [order your Alibaba Cloud ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-alibaba-ports) and [configure your Alibaba Cloud resources.](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-alibaba)
  * The Google Cloud region where you want to place your VLAN attachments. You need this value when you create the attachment, as described in [Configure your Google Cloud resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources).



[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/connectivity-overview)

[ Next Order Cross-Cloud Interconnect connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-google-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
