---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configure-traffic-differentiation/
title: Configure traffic differentiation \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:41.589078+00:00
---

# Configure traffic differentiation  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configure-traffic-differentiation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure traffic differentiation Stay organized with collections  Save and categorize content based on your preferences. 

Application awareness helps you use your Dedicated Interconnect connections more efficiently by using [differentiated services field codepoint (DSCP)](https://www.iana.org/assignments/dscp-registry/dscp-registry.xhtml) for traffic differentiation.

You can configure traffic differentiation for outbound Dedicated Interconnect data transfers using application awareness on Cloud Interconnect.

When you enable application awareness on your Cloud Interconnect and mark the DSCP in the IP headers of your outbound data transfers to map them to traffic classes, your outbound data transfers receive differentiated treatment on Cloud Interconnect.

Application awareness lets you do the following:

  * Choose one of two policy types, either a strict priority policy or a bandwidth percentage policy, to specify how Cloud Interconnect treats your outbound data transfers that are classified into different traffic classes.

  * Allocate your Dedicated Interconnect outbound data transfer bandwidth among six different traffic classes.

  * Use traffic shaping controls in addition to either policy type to set the maximum bandwidth that each traffic class can use on your Dedicated Interconnect outbound data transfers.




The following sections describe application awareness on Cloud Interconnect and how to configure it for your Dedicated Interconnect connection.

Contact your account team to enable application awareness on your Dedicated Interconnect.

## Before you begin

Before you begin, do the following:

  * Understand the best practices when [configuring Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices), in particular, for [creating redundant Cloud Interconnect connections with sufficient capacity](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#capacity).

  * Ensure that there is no network traffic on the Dedicated Interconnect connection.

  * Consider the following information about configuring application awareness:

    * DSCP in your outbound data traffic IP header determines the application awareness traffic class for providing traffic differentiation. Mark the DSCP in your outbound IP data traffic headers accordingly.

    * In order to mark a specific DSCP in your outbound Cloud Interconnect data transfers that originate from Google APIs, mark the same DSCP in your Google API request packets as your intended DSCP for the Google API response traffic. Google APIs echo back (copy) the DSCP from the corresponding customer request IP packet in their response traffic, which lets you control the DSCP for the Google API response traffic.

    * When you use Private Service Connect, the DSCP echo-back behavior is supported for Google APIs. You can control the DSCP in your Google API response traffic by setting the request DSCP accordingly. This lets you control the DSCP in your outbound data transfers from Google APIs that you connect to with Private Service Connect.

    * When you use Private Service Connect, DSCP echo-back isn't supported for published Virtual Private Cloud (VPC)-hosted services. Therefore, the DSCP in the response data traffic from published VPC-hosted services can't be controlled with the request traffic DSCP. Instead, the corresponding VPC-hosted service backends determine the DSCP in the response packets.




## Traffic classes

Application awareness uses the concept of a traffic class, based upon DSCP ranges, to differentiate traffic on Dedicated Interconnect. The following table describes the six traffic classes:

Traffic class | Inner DSCP range (binary) | Inner DSCP range (decimal) | Description and examples  
---|---|---|---  
TC1 | 000xxx | 0-7 | Best effort traffic  
TC2 | 001xxx | 8-15 | Bulk trafficExample: file transfer  
TC3 | 010xxx | 16-23 | Operations, administration and management trafficExamples: SNMP, SSH, ping, telnet  
TC4 | 011xxx | 24-31 | Streaming or live video  
TC5 | 10xxxx | 32-47 | Interactive or user-facing traffic  
TC6 | 11xxxx | 48-63 | Essential network control trafficExamples: control traffic from protocols like BGP and BFD  
  
## Available policy types

Application awareness on Cloud Interconnect offers two policy types to determine how outbound data transfers are differentiated on your Cloud Interconnect:

Strict priority
    

A strict priority policy type assigns a priority level to each traffic class for outbound data transfers. The highest-priority outbound data transfers are assigned to traffic class `TC6`, while the lowest-priority outbound data transfers are assigned to traffic class `TC1`.

Strict priority differentiation doesn't require that you specify class-specific configurations because the priority for each traffic class is prespecified. However, to prevent starving lower-priority traffic classes during congestion events, we recommend that you specify a traffic shaping profile to limit the maximum bandwidth used by each of your higher-priority traffic classes.

Bandwidth percentage
    

A bandwidth percentage policy type lets you specify the target bandwidth share that each traffic class can use during congestion events on your Cloud Interconnect. Assigning percentages to each traffic class helps ensure that each traffic class can use its specified share of Cloud Interconnect bandwidth during congestion events on your Cloud Interconnect.

If excess bandwidth is available because a traffic class isn't using its assigned share fully, the remaining bandwidth is shared equally among all other traffic classes.

## Traffic shaping control

In addition to the two policy types, application awareness also provides traffic shaping controls that let you specify the maximum bandwidth that each traffic class can use. You can use traffic shaping controls with strict priority policies and with bandwidth percentage policies.

## Configure a strict priority policy type

Use the following steps to configure a strict priority policy type.

###  gcloud 

Use the following command:
    
    
    gcloud compute interconnects application-awareness \
        configure-strict-priority-policy INTERCONNECT_NAME \
        --profile-description=DESCRIPTION \
        --enabled
    

Replace the following:

  * `INTERCONNECT_NAME`: the name of the interconnect to patch
  * `DESCRIPTION`: a profile description for application awareness



###  API 

Send the following JSON object to the [`interconnects.patch` endpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/patch):
    
    
    {
      "aaiEnabled":true,
      "applicationAwareInterconnect":
        {
          "profileDescription": "DESCRIPTION",
          "strictPriorityPolicy":{}
      },
    }
    

Replace `DESCRIPTION` with a description for this profile.

### Configure a strict priority policy type with a traffic shaping profile

Optionally, you can configure a strict priority policy type along with a traffic shaping profile. We recommend that you use a traffic shaping profile to help ensure that lower-priority traffic classes aren't starved due to higher-priority traffic classes during congestion events.

Use the following steps to configure a strict priority policy type with a traffic shaping profile. Specify a numerical value representing the maximum bandwidth percentage for each included traffic class. You can define the traffic shaping profile for a subset or all 6 traffic classes, `TC1` through `TC6`.

###  gcloud 

  1. Use the following command to configure the strict priority policy:
         
         gcloud compute interconnects application-awareness \
             configure-strict-priority-policy INTERCONNECT_NAME \
             --profile-description=DESCRIPTION \
             --enabled
         

Replace the following:

     * `INTERCONNECT_NAME`: the name of the interconnect to patch
     * `DESCRIPTION`: a profile description for application awareness
  2. Use the following command to configure the traffic shaping profile:
         
         gcloud compute interconnects application-awareness \
             configure-shaper-average-percentage INTERCONNECT_NAME \
             --profile-description=DESCRIPTION \
             --bandwidth-percentages="TC1=TC1_SHAPE_PERCENTAGE,TC2=TC2_SHAPE_PERCENTAGE,TC3=TC3_SHAPE_PERCENTAGE,TC4=TC4_SHAPE_PERCENTAGE,TC5=TC5_SHAPE_PERCENTAGE,TC6=TC6_SHAPE_PERCENTAGE" \
             --enabled
         

Replace the following:

     * `INTERCONNECT_NAME`: the name of the interconnect to patch
     * `DESCRIPTION`: a profile description for application awareness
     * `TC1_SHAPE_PERCENTAGE ... TC6_SHAPE_PERCENTAGE`: a numerical value representing the shape average percentage for each traffic class. Each value must be less than or equal to 100. You can define the traffic shaping profile for a subset or all 6 traffic classes, `TC1` through `TC6`.



###  API 

Send the following JSON object to the [`interconnects.patch` endpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/patch):
    
    
    {
      "aaiEnabled": true,
      "applicationAwareInterconnect":
        {
          "profileDescription": "DESCRIPTION",
          "strictPriorityPolicy": {},
          "shapeAveragePercentages": [
              {
                "trafficClass": "TC1",
                "percentage": TC1_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC2",
                "percentage": TC2_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC3",
                "percentage": TC3_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC4",
                "percentage": TC4_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC5",
                "percentage": TC5_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC6",
                "percentage": TC6_SHAPE_PERCENTAGE
              }
            ]
        }
    }
    

Replace `TC1_SHAPE_PERCENTAGE ... TC6__SHAPE_PERCENTAGE` with a numerical value representing the maximum bandwidth percentage for each traffic class. You can define the traffic shaping profile for a subset or all 6 traffic classes, `TC1` through `TC6`.

To prevent network failure, ensure that network control traffic, such as BGP and BFD, are included in the highest `strict_policy` priority class.

## Configure bandwidth percentage

Use the following steps to configure the bandwidth percentage policy.

###  gcloud 

Use the following command:
    
    
    gcloud compute interconnects application-awareness \
        configure-bandwidth-percentage-policy INTERCONNECT_NAME \
        --profile-description=DESCRIPTION \
        --bandwidth-percentages="TC1=TC1_PERCENTAGE,TC2=TC2_PERCENTAGE,TC3=TC3_PERCENTAGE,TC4=TC4_PERCENTAGE,TC5=TC5_PERCENTAGE,TC6=TC6_PERCENTAGE" \
        --enabled
    

Replace the following:

  * `INTERCONNECT_NAME`: the name of the interconnect to patch
  * `DESCRIPTION`: a profile description for application awareness
  * `TC1_PERCENTAGE ... TC6_PERCENTAGE`: a numerical value representing the bandwidth percentage for each traffic class. Each value must be less than or equal to 100.



###  API 

Send the following JSON object to the [`interconnects.patch` endpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/patch):
    
    
    {
      "aaiEnabled": true,
      "applicationAwareInterconnect":
        {
          "profileDescription": "DESCRIPTION",
          "bandwidthPercentagePolicy": {
            "bandwidthPercentages": [
              {
                "trafficClass": "TC1",
                "percentage": TC1_PERCENTAGE
              },
              {
                "trafficClass": "TC2",
                "percentage": TC2_PERCENTAGE
              },
              {
                "trafficClass": "TC3",
                "percentage": TC3_PERCENTAGE
              },
              {
                "trafficClass": "TC4",
                "percentage": TC4_PERCENTAGE
              },
              {
                "trafficClass": "TC5",
                "percentage": TC5_PERCENTAGE
              },
              {
                "trafficClass": "TC6",
                "percentage": TC6_PERCENTAGE
              }
            ]
        }
      }
    }
    

Replace the following:

  * `DESCRIPTION`: a description for this profile.
  * `TC1_PERCENTAGE ... TC6_PERCENTAGE`: a nonzero numerical value representing the percentage for each traffic class. The bandwidth percentages for all the traffic classes must sum up to 100.



### Configure bandwidth percentage with a traffic shaping profile

Optionally, you can configure a bandwidth percentage policy along with a traffic shaping profile. A traffic shaping profile helps you set the maximum bandwidth that each traffic class can consume.

Use the following steps to configure a bandwidth percentage policy with a traffic shaping profile. A nonzero value must be specified for each traffic class, and the bandwidth percentages for all traffic classes must sum up to 100.

###  gcloud 

  1. Use the following command to configure the bandwidth percentage policy:
         
         gcloud compute interconnects application-awareness \
             configure-bandwidth-percentage-policy INTERCONNECT_NAME \
             --profile-description=DESCRIPTION \
             --bandwidth-percentages="TC1=TC1_PERCENTAGE,TC2=TC2_PERCENTAGE,TC3=TC3_PERCENTAGE,TC4=TC4_PERCENTAGE,TC5=TC5_PERCENTAGE,TC6=TC6_PERCENTAGE" \
             --enabled
         

Replace the following:

     * `INTERCONNECT_NAME`: the name of the interconnect to patch
     * `DESCRIPTION`: a profile description for application awareness
     * `TC1_PERCENTAGE ... TC6_PERCENTAGE`: a numerical value representing the bandwidth percentage for each traffic class. Each value must be less than or equal to 100.
  2. Use the following command to configure the traffic shaping profile:
         
         gcloud compute interconnects application-awareness \
             configure-shaper-average-percentage INTERCONNECT_NAME \
             --profile-description=DESCRIPTION \
             --bandwidth-percentages="TC1=TC1_SHAPE_PERCENTAGE,TC2=TC2_SHAPE_PERCENTAGE,TC3=TC3_SHAPE_PERCENTAGE,TC4=TC4_SHAPE_PERCENTAGE,TC5=TC5_SHAPE_PERCENTAGE,TC6=TC6_SHAPE_PERCENTAGE" \
             --enabled
         

Replace the following:

     * `INTERCONNECT_NAME`: the name of the interconnect to patch
     * `DESCRIPTION`: a profile description for application awareness
     * `TC1_SHAPE_PERCENTAGE ... TC6_SHAPE_PERCENTAGE`: a numerical value representing the shape average percentage for each traffic class. Each value must be less than or equal to 100. You can define the traffic shaping profile for a subset or all 6 traffic classes, `TC1` through `TC6`.



###  API 

Send the following JSON object to the [`interconnects.patch` endpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/patch):
    
    
    {
      "aaiEnabled": true,
      "applicationAwareInterconnect":
        {
          "profileDescription": "DESCRIPTION",
          "bandwidthPercentagePolicy": {
            "bandwidthPercentages": [
              {
                "trafficClass": "TC1",
                "percentage": TC1_PERCENTAGE
              },
              {
                "trafficClass": "TC2",
                "percentage": TC2_PERCENTAGE
              },
              {
                "trafficClass": "TC3",
                "percentage": TC3_PERCENTAGE
              },
              {
                "trafficClass": "TC4",
                "percentage": TC4_PERCENTAGE
              },
              {
                "trafficClass": "TC5",
                "percentage": TC5_PERCENTAGE
              },
              {
                "trafficClass": "TC6",
                "percentage": TC6_PERCENTAGE
              }
            ]
        },
          "shapeAveragePercentages": [
              {
                "trafficClass": "TC1",
                "percentage": TC1_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC2",
                "percentage": TC2_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC3",
                "percentage": TC3_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC4",
                "percentage": TC4_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC5",
                "percentage": TC5_SHAPE_PERCENTAGE
              },
              {
                "trafficClass": "TC6",
                "percentage": TC6_SHAPE_PERCENTAGE
              }
            ]
        }
    }
    

Replace the following:

  * `DESCRIPTION`: a description for this profile
  * `TC1_PERCENTAGE ... TC6_PERCENTAGE`: a numerical value representing the percentage for each traffic class
  * `TC1_SHAPE_PERCENTAGE ... TC6_SHAPE_PERCENTAGE`: a numerical value representing the shape average percentage for each traffic class. Each value must be less than or equal to 100. You can define the traffic shaping profile for a subset or all 6 traffic classes, `TC1` through `TC6`.



To prevent network failure, ensure that network control traffic, such as BGP and BFD, are included in the appropriate bandwidth percentage configuration.

## Delete traffic differentiation policies

To delete traffic differentiation policies, use the following steps.

###  gcloud 

Use the following command:
    
    
    gcloud compute interconnects application-awareness delete INTERCONNECT_NAME
    

Replace `INTERCONNECT_NAME` with the name of the interconnect on which you configured a traffic differentiation policy.

###  API 

Send the following JSON object to the [`interconnects.patch` endpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/patch):
    
    
    {
      "applicationAwareInterconnect":
      {
        "profileDescription": null,
        "strictPriorityPolicy": null,
        "bandwidthPercentagePolicy": null,
        "shapeAveragePercentages": null
      }
    }
    
    

## Turn off traffic differentiation

To turn off traffic differentiation, use the following steps:

###  gcloud 

Use the following command:
    
    
    gcloud compute interconnects application-awareness update INTERCONNECT_NAME \
        --no-enabled
    

Replace `INTERCONNECT_NAME` with the name of the interconnect to update.

###  API 

Send the following JSON object to the [`interconnects.patch` endpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnects/patch):
    
    
    {
      "aaiEnabled": false
    }
    
    

## What's next

  * [View Cloud Interconnect Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-interconnect)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
