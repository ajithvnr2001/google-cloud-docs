---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/choose-locations/
title: Choose your locations \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:51.265473+00:00
---

# Choose your locations  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/choose-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Choose your locations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page includes instructions about OCI products. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For the most current information, refer to the [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm) . 

When you use Cross-Cloud Interconnect, Google provisions physical connections on your behalf between the Google Cloud network and the Oracle Cloud Infrastructure (OCI) network. 

Before Google can establish these connections, you must order ports from both Google and OCI. In preparation for that process, identify the Google Cloud locations and the corresponding OCI locations that you want to use for your connections.

## Best practices for selecting a location

When deciding where to place your connections, consider questions such as the following: 

  * Where are most of your Google Cloud resources?
  * Where are most of your OCI resources?



If your resources from both clouds are in the same place, then the choice is simple. However, if they are not, consider whether you want your connections to be closer to your Google Cloud resources or closer to your OCI resources. If the connections are closer to your OCI resources, then your traffic spends more time traveling on the Google network, which in general is desirable. However, you should also consider the outbound data transfer costs that you're likely to incur from both clouds.

## Factors affected by location

This section describes factors that are affected by your location choice.

### VLAN attachments 

After your Cross-Cloud Interconnect connection is established, you must configure VLAN attachments in Google Cloud. A VLAN attachment is a logical connection between your remote cloud network and a single region in your Virtual Private Cloud (VPC) network.

When you choose a location for your ports, you limit the number of regions where you can place both VLAN attachments and FastConnect virtual circuits. For this reason, the supported locations table includes a column for the Google Cloud and OCI regions that are served by each port location.

**Note:** In Google Cloud, the location of the VLAN attachment doesn't have to limit which Google Cloud regions receive your OCI routes. To advertise OCI routes to all of your Google Cloud regions, configure [global dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes).

### Edge availability domains

Each metropolitan area has two Google Cloud edge availability domains. Two domains in the same metropolitan area are not scheduled to be down for maintenance at the same time. For this reason, when you select a location for a primary and redundant port, each port must use a different edge availability domain within the same metropolitan area. This is true regardless of how you order your ports. However, when you use the Google Cloud CLI, you must specify each edge availability domain explicitly. When you use the Google Cloud console, you simply select a location, and Google Cloud reserves a port for you in each domain.

In the gcloud CLI version of the location name, the edge availability domain is the second piece of information. For example, if the location name is `iad-zone1-1`, the edge availability domain is `zone1`. If the location name is `iad-zone2-1`, the edge availability zone is `zone2`.

### Colocation facilities

Google typically provisions each connection within a single colocation facility. However, sometimes connections are created between adjoining facilities that are operated by the same provider. In either case, generally you don't need to know the facility name. For this reason, the supported locations table does not identify specific facilities. 

## List of supported locations

The following table lists the supported OCI locations and the corresponding Google Cloud locations. 

You must specify the Google Cloud location of your Cross-Cloud Interconnect port, and additionally specify where in your other cloud provider to connect it. This latter OCI location is referred to as the _remote location_ in this documentation set and within Google Cloud. Make sure to use the remote location name when you order the Cross-Cloud Interconnect. Your remote cloud provider has a different, although similar, name for the location, which you use when you order the port with that cloud provider.

For each location name, some syntax variations exist. For example:

  * The remote location name varies depending on whether you are interacting with OCI or Google Cloud.
  * When interacting with Google Cloud, the Google Cloud console displays the remote location _description_ next to the location name to help you choose the correct location.
  * In Google Cloud, the Google Cloud console Cloud Interconnect location (not the remote location) shows facility information rather than the actual Cloud Interconnect location name.



**Note:** You can also use the gcloud CLI to list locations. For more information, see the reference page for the [`gcloud compute interconnects remote-locations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/remote-locations/list). 

**Note:** For the most up-to-date information about OCI locations, see [OCI Data Regions](https://www.oracle.com/cloud/public-cloud-regions/data-regions/) in the Oracle documentation.Google Cloud regions | Oracle Cloud Infrastructure regions | Metropolitan area | Remote location | Google Cloud locations  
---|---|---|---|---  
Google Cloud | Oracle Cloud Infrastructure  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * Singapore (Singapore)

| Singapore|  oci-equinix-sg1  | Equinix SG1 | 

  * sin-zone1-2260
  * sin-zone2-2260

  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * Japan East (Tokyo)

| Tokyo|  oci-equinix-ty4  | Equinix TY4 | 

  * nrt-zone1-1893
  * nrt-zone2-1893

  
  
  * australia-southeast1
  * australia-southeast2

| 

  * Australia Southeast (Melbourne)

| Melbourne|  oci-equinix-me1  | Equinix ME1 | 

  * mel-zone1-1988
  * mel-zone2-1988

  
  
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

  * Netherlands Northwest (Amsterdam)

| Amsterdam|  oci-equinix-am4  | Equinix AM4 | 

  * ams-zone1-1320
  * ams-zone2-1320

  
  
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

  * Germany Central (Frankfurt)

| Frankfurt|  oci-equinix-fr5  | Equinix FR5 | 

  * fra-zone1-683
  * fra-zone2-683

  
  
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

  * UK South (London)
  * UK Gov South (London)

| London|  oci-equinix-ld6  | Equinix LD6 | 

  * lhr-zone1-2262
  * lhr-zone2-2262

  
  
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

  * Spain Central (Madrid)

| Madrid|  oci-interxion-mad2  | Interxion MAD2 | 

  * mad-zone1-130
  * mad-zone2-130

  
  
  * asia-southeast1
  * asia-south1
  * asia-south2

| 

  * India West (Mumbai)

| Mumbai|  oci-equinix-mb1  | Equinix MB1 | 

  * bom-zone1-2310
  * bom-zone2-2310

  
  
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

  * US East (Ashburn)
  * US Gov East (Ashburn)

| Washington D.C.|  oci-equinix-dc6  | Equinix DC6 | 

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

  * US Midwest (Chicago)

| Chicago|  oci-coresite-ch1  | Coresite CH1 | 

  * ord-zone1-440
  * ord-zone2-440

  
  
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

  * Canada Southeast (Montréal)

| Montréal|  oci-cologix-mtl3  | Cologix MTL3 | 

  * yul-zone1-1944
  * yul-zone2-1944

  
  
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

  * US West (San Jose)

| San Francisco|  oci-equinix-sv10  | Equinix SV10 | 

  * sjc-zone1-6
  * sjc-zone2-6

  
  
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

  * Canada Southeast (Toronto)

| Toronto|  oci-cologix-tor1  | Cologix TOR1 | 

  * yyz-zone1-392
  * yyz-zone2-392

  
  
  * southamerica-east1
  * southamerica-west1
  * us-east1

| 

  * Brazil East (São Paulo)

| São Paulo|  oci-equinix-sp4  | Equinix SP4 | 

  * gru-zone1-165
  * gru-zone2-165

  
  
## Verify availability

After you've identified a location that you want to use, double-check that it has an available FastConnect port with your intended capacity. This step is helpful because the availability of ports can change without notice.

If you're working in the OCI console, you can verify availability in an OCI region while ordering your connections. To verify availability in advance, use Oracle Cloud Shell.

### Oracle Cloud Shell 

Use the [`oci network cross-connect-port-speed-shape list` command](https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.23.4/oci_cli_docs/cmdref/network/cross-connect-port-speed-shape/list.html) to get information about ports that are available in your region. For example:
    
    
    oci network cross-connect-port-speed-shape list \
             --compartment-id=ORACLE_CLOUD_ID \
             --region=REGION
             --all

Replace the following:

  * `ORACLE_CLOUD_ID`: the [`Oracle-assigned unique ID`](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm) for your tenancy; in OCI, a _tenancy_ is similar to a Google Cloud organization
  * `REGION`: the region where you want to locate your connection; if you need help selecting a region, refer to the table in the prededing section



In the command output, look for 10-Gbps and 100-Gbps ports. For example, the following output shows that ports are available in both capacities:
    
    
             {
                "data": [
                  {
                    "name": "100 Gbps",
                    "port-speed-in-gbps": 100
                  },
                  {
                    "name": "10 Gbps",
                    "port-speed-in-gbps": 10
                  },
                  {
                    "name": "1 Gbps",
                    "port-speed-in-gbps": 1
                  }
                ]
              }
            

## Note locations and regions

After you've reviewed the previous sections, make a note of the following values:

  * The remote location, as it's known in Google Cloud, and the Google Cloud location. You need these values when you [order your Cross-Cloud Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/order-google-connections).
  * The remote location, as it's known in OCI, and the region where you want to place the connection resources. You need these values when you [order your OCI ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/order-oci-ports) and [configure your OCI resources.](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-oci)
  * The Google Cloud region where you want to place your VLAN attachments. You need this value when you create the attachment, as described in [Configure your Google Cloud resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/configure-google-resources).



[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/connectivity-overview)

[ Next Order Cross-Cloud Interconnect connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/order-google-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
