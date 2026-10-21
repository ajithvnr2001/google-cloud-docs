---
url: https://docs.cloud.google.com/vpc/docs/multicast/update-domain-parameters/
title: Update multicast domain parameters \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:43.969289+00:00
---

# Update multicast domain parameters  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/update-domain-parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update multicast domain parameters

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes how to resize the multicast infrastructure for your domain by updating the traffic parameters of existing zonal multicast domain activations for Cloud Multicast.

For information about creating and activating multicast domains, see [Create multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/create-domains#activate-domain).

## Before you begin

Before you update multicast domain parameters, review the following and plan for your update accordingly:

  * **Service availability during update** : This procedure might cause a temporary service disruption while Google Cloud re-provisions your multicast infrastructure according to the new parameters that you provide.

    * The service disruption applies to the multicast infrastructure for the specific multicast domain activation that you are updating. During the update, multicast producers and consumers can't send or receive traffic for the corresponding multicast domain and zone.

    * The duration of the service disruption depends on several factors, such as the scale of your current multicast infrastructure, the number of multicast group range activations created by using the domain activation, and the scale of the new parameters that you provide. For large-scale configurations, the update can take between 30 minutes and 1 hour to complete.

  * **Changes to billing charges after update** : Multicast domain activations incur billing charges as described in [Billing](https://docs.cloud.google.com/vpc/docs/multicast/overview#billing). Updating the traffic parameters of a multicast domain activation might affect its billing charges to your project. For more information, contact your Google Cloud sales representative.

  * **Action required by multicast consumers after update** : After the update is complete, to begin receiving traffic again, multicast consumers must rejoin any multicast groups in the domain and zone. If necessary, coordinate with the multicast consumer network administrator or multicast consumer application owners.




## Update a multicast domain activation

This section describes how to update the parameters of a multicast domain activation that determine the scale of your multicast infrastructure.

If you activated a multicast domain in multiple zones, follow this procedure for each zonal multicast domain activation that you want to update.

###  gcloud 

To update a multicast domain activation, use the [`network-services multicast-domain-activations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-activations/update).

The following command takes around 10 to 30 minutes to complete. After the command completes successfully, it can take several more minutes for the infrastructure to be ready to receive and distribute multicast traffic. For large-scale configurations, this entire process can take between 30 minutes and 1 hour to fully complete.

**Note:** If the following command returns an unexpected error, such as a timeout error, then run the command again to complete the update.
    
    
       gcloud network-services multicast-domain-activations update DOMAIN_ACTIVATION_NAME \
          --location=ZONE \
          --aggr-egress-pps=AGGR_EGRESS_PPS \
          --aggr-ingress-pps=AGGR_INGRESS_PPS \
          --avg-packet-size=AVG_PACKET_SIZE \
          --max-per-group-ingress-pps=MAX_PER_GROUP_INGRESS_PPS \
          --max-per-group-subscribers=MAX_PER_GROUP_SUBSCRIBERS
    

Replace the following values:

  * `DOMAIN_ACTIVATION_NAME`: the name of the multicast domain activation
  * `ZONE`: the zone where the multicast domain was activated
  * Specify the following parameters according to your needs for the multicast traffic in this zone. Google Cloud uses these parameters to determine the scale of your multicast infrastructure.

Before you specify these parameters, see the following:

    * Review the corresponding [limitations for multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/overview#limitations-domain-activation) described in the Cloud Multicast overview.
    * See the following information about optional and required flags:

      * If you previously specified `--aggr-egress-pps` when you created the multicast domain activation, then specifying `--aggr-egress-pps` is optional. Otherwise, this flag is required.
      * All other flags are optional.

For more information about each flag, see the following:

    * `AGGR_EGRESS_PPS`: aggregate egress packets per second (pps) for all multicast groups in the domain in the specified zone. Egress refers to packets distributed from the multicast infrastructure to multicast consumers.

You can enter a value from 0 to 500000000 (500 million). The default is value is 1000000 (1 million). Default values for the other fields are set dynamically based on the value that you enter for this flag.

**Note:** If you don't know your aggregate egress pps, then you can estimate it by using the following formula: `AGGR_EGRESS_PPS = AGGR_INGRESS_PPS * MAX_PER_GROUP_SUBSCRIBERS / 2`.
    * `AGGR_INGRESS_PPS`: aggregate ingress pps for all multicast groups in the domain in the specified zone. Ingress refers to packets sent from multicast producers to the multicast infrastructure.

You can enter a value from 0 to 2000000 (2 million). The value that you enter for `--aggr-ingress-pps` can't be greater than the value of `--aggr-egress-pps`.

    * `AVG_PACKET_SIZE`: average packet size in bytes. You can enter a value from 64 to 1500.

    * `MAX_PER_GROUP_INGRESS_PPS`: maximum ingress pps for a single multicast group in the domain in the specified zone. Use this flag to specify the most active multicast group in the domain, which helps Google Cloud more accurately determine the required scale of your multicast infrastructure.

You can enter a value from 0 to 2000000 (2 million). The value that you enter for `--max-per-group-ingress-pps` can't be greater than the value of `--aggr-ingress-pps`.

    * `MAX_PER_GROUP_SUBSCRIBERS`: maximum number of multicast consumers for a single multicast group in the domain in the specified zone. Use this flag to specify the group with the most multicast consumers, which helps Google Cloud more accurately determine the required scale of your multicast infrastructure. Including this flag does not enforce a limit on the number of multicast consumers for a group.

You can enter a value from 1 to 500.




###  API 

To update a multicast domain activation, use the [`multicastDomainActivations.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/patch).

The following command takes around 10 to 30 minutes to complete. After the command completes successfully, it can take several more minutes for the infrastructure to be ready to receive and distribute multicast traffic. For large-scale configurations, this entire process can take between 30 minutes and 1 hour to fully complete.

**Note:** If the following request returns an unexpected error, such as a timeout error, then make the request again to complete the update.
    
    
    PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME?updateMask=trafficSpec
    
    {
      "trafficSpec": {
        "aggrEgressPps": "AGGR_EGRESS_PPS",
        "aggrIngressPps": "AGGR_INGRESS_PPS",
        "avgPacketSize": "AVG_PACKET_SIZE",
        "maxPerGroupIngressPps": "MAX_PER_GROUP_INGRESS_PPS",
        "maxPerGroupSubscribers": "MAX_PER_GROUP_SUBSCRIBERS"
      }
    }
    

Replace the following values:

  * `PROJECT_ID`: the ID of the multicast administrator project
  * `DOMAIN_ACTIVATION_NAME`: the name of the multicast domain activation
  * `ZONE`: the zone where the multicast domain was activated
  * Specify values for the `trafficSpec` object according to your needs for the multicast traffic in this zone. Google Cloud uses these parameters to determine the scale of your multicast infrastructure.

Before you specify these parameters, see the following:

    * Review the corresponding [limitations for multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/overview#limitations-domain-activation) described in the Cloud Multicast overview.
    * See the following information about optional and required fields:

      * If you previously specified `aggrEgressPps` when you created the multicast domain activation, then specifying `aggrEgressPps` is optional. Otherwise, this field is required.
      * All other fields in `trafficSpec` are optional.

For more information about each field, see the following:

    * `AGGR_EGRESS_PPS`: aggregate egress packets per second (pps) for all multicast groups in the domain in the specified zone. Egress refers to packets distributed from the multicast infrastructure to multicast consumers.

You can enter a value from 0 to 500000000 (500 million). The default is value is 1000000 (1 million). Default values for the other fields are set dynamically based on the value that you enter for this field.

**Note:** If you don't know your aggregate egress pps, then you can estimate it by using the following formula: `AGGR_EGRESS_PPS = AGGR_INGRESS_PPS * MAX_PER_GROUP_SUBSCRIBERS / 2`.
    * `AGGR_INGRESS_PPS`: aggregate ingress pps for all multicast groups in the domain in the specified zone. Ingress refers to packets sent from multicast producers to the multicast infrastructure.

You can enter a value from 0 to 2000000 (2 million). The value that you enter for `aggrIngressPps` can't be greater than the value of `aggrEgressPps`.

    * `AVG_PACKET_SIZE`: average packet size in bytes. You can enter a value from 64 to 1500.

    * `MAX_PER_GROUP_INGRESS_PPS`: maximum ingress pps for a single multicast group in the domain in the specified zone. Use this field to specify the most active multicast group in the domain, which helps Google Cloud more accurately determine the required scale of your multicast infrastructure.

You can enter a value from 0 to 2000000 (2 million). The value that you enter for `maxPerGroupIngressPps` can't be greater than the value of `aggrIngressPps`.

    * `MAX_PER_GROUP_SUBSCRIBERS`: maximum number of multicast consumers for a single multicast group in the domain in the specified zone. Use this field to specify the group with the most multicast consumers, which helps Google Cloud more accurately determine the required scale of your multicast infrastructure. Providing this specification does not enforce a limit on the number of multicast consumers for a group.

You can enter a value from 1 to 500.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
