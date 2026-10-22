---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-adapter-ip-allow-list/
title: Agent adapter IP allow list \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:15.863894+00:00
---

# Agent adapter IP allow list  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-adapter-ip-allow-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent adapter IP allow list Stay organized with collections  Save and categorize content based on your preferences. 

For the agent adapter to function properly, certain domains, IP addresses, and ports must be permitted in your network infrastructure. The domains and IP addresses also need to be permitted on any system utilities such as Norton, ESET, McAfee, ZoneAlarm or any other software that controls external connectivity.

CCAI Platform uses carriers' Global Low Latency routing capabilities by default. This dynamic capability uses latency-based DNS lookups to determine your location and routes requests through the nearest data center. You can also set a fixed location if your users are using a DNS server in another region.

If you use a restricted network that requires media IP access to be permitted, Google recommends that you specify the region within your network allowances. As our global presence continues to expand, the media IP address list will be updated.

**Note:** Connections can be established to regions that are not permitted by your infrastructure.

## Ports

The following ports should be permitted for egress connectivity:

  * 443 UDP/TCP
  * 10,000 to 60,000 UDP (Ephemeral Port Range)
  * 4080 UDP/TCP
  * 3478 UDP/TCP
  * 5349, 5066, 7443 TCP (STUN/TURN)



## Media IP ranges

The following table shows the IP address ranges that must be permitted in your network infrastructure to allow the passing of voice traffic through the agent adapter.

### Agent adapter (webRTC)

  * 36.255.198.128/25
  * 50.114.136.128/25
  * 50.114.144.0/21
  * 64.16.226.0/24
  * 64.16.227.0/24
  * 64.16.228.0/24
  * 64.16.229.0/24
  * 64.16.230.0/24
  * 64.16.248.0/24
  * 64.16.249.0/24



## Domains (TCP Traffic on Port 443)

The following domains must be permitted in your network infrastructure:

  * General: 
    * api.ujet.co
    * externals.ujet.co
    * firebaseio.com
    * gstatic.com
    * firebasedatabase.app
    * ccaiplatform.com
    * stun.l.google.com
    * stun1.l.google.com
    * stun2.l.google.com
    * stun3.l.google.com
    * stun4.l.google.com
  * Twilio: 
    * chunderw-gll.twilio.com
    * chunderw-vpc-gll.twilio.com
    * chunderw-vpc-gll-au1.twilio.com
    * chunderw-vpc-gll-br1.twilio.com
    * chunderw-vpc-gll-de1.twilio.com
    * chunderw-vpc-gll-ie1.twilio.com
    * chunderw-vpc-gll-jp1.twilio.com
    * chunderw-vpc-gll-sg1.twilio.com
    * chunderw-vpc-gll-us1.twilio.com
    * chunderw-vpc-gll-us2.twilio.com
    * voice-js.roaming.twilio.com
    * voice-js.au1.twilio.com
    * voice-js.br1.twilio.com
    * voice-js.de1.twilio.com
    * voice-js.ie1.twilio.com
    * voice-js.jp1.twilio.com
    * voice-js.sg1.twilio.com
    * voice-js.us1.twilio.com
    * voice-js.us2.twilio.com
    * global.stun.twilio.com
    * global.turn.twilio.com
    * matrix.twilio.com
    * eventgw.twilio.com
    * eventgw.us1.twilio.com
    * twiliocdn.com
    * networktest.twilio.com
    * sdk.twilio.com
  * Nexmo: 
    * api-us-1.nexmo.com
    * api-us-2.nexmo.com
    * api-sg-1.nexmo.com
    * api-eu-1.nexmo.com
    * api-eu-2.nexmo.com
    * ws-us-1.nexmo.com
    * ws-us-2.nexmo.com
    * ws-sg-1.nexmo.com
    * ws-eu-1.nexmo.com
    * ws-eu-2.nexmo.com
  * Vonage: 
    * api-us-3.vonage.com
    * api-us-4.vonage.com
    * api-eu-3.vonage.com
    * api-eu-4.vonage.com
    * api-ap-3.vonage.com
    * api-ap-4.vonage.com
    * ws-us-3.vonage.com
    * ws-us-4.vonage.com
    * ws-eu-3.vonage.com
    * ws-eu-4.vonage.com
    * ws-ap-3.vonage.com
    * ws-ap-4.vonage.com
  * Telnyx: 
    * stun.telnyx.com
    * turn.telynx.com
    * sip.telnyx.com
    * sip.telnyx.ca
    * sip.telnyx.eu
    * sip.telnyx.com.au
    * rtc.telnyx.com



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
