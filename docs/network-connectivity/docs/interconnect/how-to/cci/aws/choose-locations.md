---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/choose-locations/
title: Choose your locations \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:28.687502+00:00
---

# Choose your locations  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/choose-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Choose your locations Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page includes instructions about AWS products. Google doesn't guarantee that this guidance is up to date or that the sample configuration choices are ideal for your use case. For the most current information, refer to the [AWS documentation](https://docs.aws.amazon.com/) . 

When you use Cross-Cloud Interconnect, Google provisions physical connections on your behalf between the Google Cloud network and the Amazon Web Services (AWS) network. 

Before Google can establish these connections, you must order ports from both Google and AWS. In preparation for that process, identify the Google Cloud locations and the corresponding AWS locations that you want to use for your connections.

## Best practices for selecting a location

When deciding where to place your connections, consider questions such as the following: 

  * Where are most of your Google Cloud resources?
  * Where are most of your AWS resources?



If your resources from both clouds are in the same place, then the choice is simple. However, if they are not, consider whether you want your connections to be closer to your Google Cloud resources or closer to your AWS resources. If the connections are closer to your AWS resources, then your traffic spends more time traveling on the Google network, which in general is desirable. However, you should also consider the outbound data transfer costs that you're likely to incur from both clouds.

## Factors affected by location

This section describes factors that are affected by your location choice.

### VLAN attachments 

After your Cross-Cloud Interconnect connection is established, you must configure VLAN attachments in Google Cloud. A VLAN attachment is a logical connection between your remote cloud network and a single region in your Virtual Private Cloud network.

When you choose a location for your ports, you limit the number of regions where you can place VLAN attachments. For this reason, the supported locations table includes a column for the Google Cloud regions that are served by each port location.

**Note:** In Google Cloud, the location of the VLAN attachment doesn't have to limit which Google Cloud regions receive your AWS routes. To advertise AWS routes to all of your Google Cloud regions, configure [global dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes).

### Edge availability domains

Each metropolitan area has two Google Cloud edge availability domains. Two domains in the same metropolitan area are not scheduled to be down for maintenance at the same time. For this reason, when you select a location for a primary and redundant port, each port must use a different edge availability domain within the same metropolitan area. This is true regardless of how you order your ports. However, when you use the Google Cloud CLI, you must specify each edge availability domain explicitly. When you use the Google Cloud console, you simply select a location, and Google Cloud reserves a port for you in each domain.

In the gcloud CLI version of the location name, the edge availability domain is the second piece of information. For example, if the location name is `iad-zone1-1`, the edge availability domain is `zone1`. If the location name is `iad-zone2-1`, the edge availability zone is `zone2`.

### Colocation facilities

Google typically provisions each connection within a single colocation facility. However, sometimes connections are created between adjoining facilities that are operated by the same provider. In either case, generally you don't need to know the facility name. For this reason, the supported locations table does not identify specific facilities. 

## List of supported locations

The following table lists the supported AWS locations and the corresponding Google Cloud locations. 

You must specify the Google Cloud location of your Cross-Cloud Interconnect port, and additionally specify where in your other cloud provider to connect it. This latter AWS location is referred to as the _remote location_ in this documentation set and within Google Cloud. Make sure to use the remote location name when you order the Cross-Cloud Interconnect. Your remote cloud provider has a different, although similar, name for the location, which you use when you order the port with that cloud provider.

For each location name, some syntax variations exist. For example:

  * The remote location name varies depending on whether you are interacting with AWS or Google Cloud.
  * When interacting with Google Cloud, the Google Cloud console displays the remote location _description_ next to the location name to help you choose the correct location.
  * In Google Cloud, the Google Cloud console Cloud Interconnect location (not the remote location) shows facility information rather than the actual Cloud Interconnect location name.



**Note:** You can also use the gcloud CLI to list locations. For more information, see the reference page for the [`gcloud compute interconnects remote-locations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/remote-locations/list). 

Google Cloud regions | Amazon Web Services regions | Metropolitan area | Remote location | Google Cloud locations  
---|---|---|---|---  
Google Cloud | Amazon Web Services  
  
  * africa-south1


  * europe-west2

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Johannesburg|  aws-tejb1  | TEJB1 | 

  * jnb-zone1-850
  * jnb-zone2-850

  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Hong Kong|  aws-eqhk1  | EQHK1 | 

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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Jakarta|  aws-dcij3  | DCIJ3 | 

  * cgk-zone1-8168
  * cgk-zone2-8168

  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Osaka|  aws-eqos1  | EqOS1 | 

  * kix-zone1-1791
  * kix-zone2-1791

  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Seoul|  aws-lgu57  | LGU57 | 

  * icn-zone1-7573
  * icn-zone2-7573

  
aws-lgknx  | LGKNX | 

  * icn-zone1-7674
  * icn-zone2-7674

  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Singapore|  aws-gss52  | GSS52 | 

  * sin-zone1-388
  * sin-zone2-388

  
  
  * asia-east1
  * asia-east2
  * asia-northeast1
  * asia-northeast2
  * asia-northeast3
  * asia-southeast1
  * asia-southeast2

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Tokyo|  aws-eqty2  | EqTY2 | 

  * nrt-zone1-452
  * nrt-zone2-452

  
  
  * australia-southeast1
  * australia-southeast2

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Sydney|  aws-eqsy3  | EqSY3 | 

  * syd-zone1-1605
  * syd-zone2-1605

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Frankfurt|  aws-inx6  | INX6 | 

  * fra-zone1-58
  * fra-zone2-58

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| London|  aws-eqld5  | EqLD5 | 

  * lhr-zone1-832
  * lhr-zone2-832

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Madrid|  aws-itcm2  | ITCM2 | 

  * mad-zone1-127
  * mad-zone2-127

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Paris|  aws-itxp7  | ITXP7 | 

  * cdg-zone1-1536
  * cdg-zone2-1536

  
aws-thv52  | THV52 | 

  * cdg-zone1-53
  * cdg-zone2-53

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Stockholm|  aws-eqsk1  | EQSK1 | 

  * arn-zone1-156
  * arn-zone2-156

  
  
  * asia-southeast1
  * asia-south1
  * asia-south2

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Mumbai|  aws-gpx51  | GPX51 | 

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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Washington D.C.|  aws-eqdc2  | EqDC2 | 

  * iad-zone1-1
  * iad-zone2-1

  
aws-csva1  | CSVA1 | 

  * iad-zone1-5467
  * iad-zone2-5467

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Chicago|  aws-eqc50  | EQC50 | 

  * ord-zone1-7
  * ord-zone2-7

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Ohio|  aws-col67  | COL67 | 

  * cmh-zone1-2377
  * cmh-zone2-2377

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Dallas, Texas|  aws-eqda2  | Equinix EqDA2 | 

  * dfw-zone1-4
  * dfw-zone2-4

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Montréal|  aws-cgm60  | CGM60 | 

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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Portland, Oregon|  aws-ecpo1  | ECPO1 | 

  * pdx-zone1-1922
  * pdx-zone2-1922

  
  
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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| San Francisco|  aws-eqsv5  | EqSV5 | 

  * sjc-zone1-6
  * sjc-zone2-6

  
aws-eqsvg  | GovCloud EqSvG | 

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

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| Seattle|  aws-eqse2-eq  | EqSe2-EQ, sublocation Equinix SE2 | 

  * sea-zone1-86
  * sea-zone2-86

  
  
  * southamerica-east1
  * southamerica-west1
  * us-east1

| 

  * af-south-1
  * ap-east-1
  * ap-northeast-1
  * ap-northeast-2
  * ap-northeast-3
  * ap-south-1
  * ap-south-2
  * ap-southeast-1
  * ap-southeast-2
  * ap-southeast-3
  * ca-central-1
  * eu-central-1
  * eu-central-2
  * eu-north-1
  * eu-south-1
  * eu-south-2
  * eu-west-1
  * eu-west-2
  * eu-west-3
  * me-central-1
  * me-south-1
  * sa-east-1
  * us-east-1
  * us-east-2
  * us-west-1
  * us-west-2

| São Paulo|  aws-tndb  | TNDB | 

  * gru-zone1-165
  * gru-zone2-165

  
  
## Verify availability

After you've identified a location that you want to use, double-check that it has an available Direct Connect port with your intended capacity. This step is helpful because the availability of ports can change without notice.

If you're working in the AWS console, you can verify availability while ordering your connections. To verify availability in advance, use the AWS CLI.

### AWS CLI

Use the [`describe-locations` command](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-locations.html) to get information about connections that are available in an AWS location. For example:
    
    
    aws directconnect describe-locations --region REGION | jq -r '.locations[] | select(.locationCode | test("REMOTE_LOCATION"; "i")) | .availablePortSpeeds'

Replace the following:

  * `REGION`: the name of the AWS region—for example, `us-east-2`
  * `REMOTE_LOCATION`: the AWS name of the remote location—for example, `CSVA1`



The command output shows the available port speeds.
    
    
          [
            "400 Gbps",
            "100 Gbps",
            "10 Gbps",
            "1 Gbps"
          ]

## Note locations and regions

After you've reviewed the previous sections, make a note of the following values:

  * The remote location, as it's known in Google Cloud, and the Google Cloud location. You need these values when you [order your Cross-Cloud Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/order-google-connections).
  * The remote location, as it's known in AWS, and the region where you want to place the connection resources. You need these values when you [order your AWS ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/order-aws-ports) and [configure your AWS resources.](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-aws)
  * The Google Cloud region where you want to place your VLAN attachments. You need this value when you create the attachment, as described in [Configure your Google Cloud resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/configure-google-resources).



[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/connectivity-overview)

[ Next Order Cross-Cloud Interconnect connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/aws/order-google-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
