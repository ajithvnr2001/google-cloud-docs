---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/contextual-information/
title: Add contextual information \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:46.532251+00:00
---

# Add contextual information  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/contextual-information/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Add contextual information Stay organized with collections  Save and categorize content based on your preferences. 

In your prompt, you can include instructions and information that the model needs to solve a problem instead of assuming that the model has all of the required information. This contextual information helps the model understand the constraints and details of what you're asking for it to do.

Effective contextual information includes the following:

  * Background information (context) for the model to refer to when generating responses.
  * Rules or pre-programmed responses to steer the model behavior.



## Examples

The following example asks the model to give troubleshooting guidance for a router:

No contextual information  
---  
**Prompt:**
    
    
    What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and
    blinking slowly.
      

**Response:**
    
    
    1. **Check the Cables:**
    - Make sure that all cables are securely connected to your Google Wifi router and modem.
    - Try replacing the cables with new ones to ensure they are not faulty.
    
    
    2. **Reboot the Router:**
    - Unplug your Google Wifi router and modem from the power outlet.
    - Wait for at least 30 seconds.
    - Plug the modem and router back in and wait for them to start up.
    
    
    3. **Factory Reset the Router:**
    - Resetting the router will restore it to its default settings.
    - Find the small reset button on the back of the router.
    - Press and hold the reset button with a paper clip or similar object for 10 seconds.
    - Release the button and wait for the router to restart.
    
    
    4. **Check Your Internet Connection:**
    - Use a wired connection to connect a device directly to your modem.
    - If the internet works, the issue may be with your router.
    - If the internet still doesn't work, contact your Internet Service Provider (ISP).
    
    
    5. **Update Router's Firmware:**
    - Check if there is a firmware update available for your Google Wifi router.
    - Download and install the latest firmware update from the Google Wifi app.
    
    
    6. **Interference and Obstacles:**
    - Make sure the router is not near electronic devices that can cause interference, like microwaves or cordless phones.
    - Remove any obstacles between the router and your devices, such as furniture or thick walls.
    
    
    7. **Change Wi-Fi Channel:**
    - In the Google Wifi app, go to Settings > Network & General > Advanced Networking.
    - Try changing the Wi-Fi channel to a less congested one.
    
    
    8. **Contact Google Support:**
    - If you've tried the above steps and the issue persists, contact Google support for further assistance.
      

(gemini-pro)  
The response looks like generic troubleshooting information that's not specific to the router or the status of the LED indicator lights. To customize the response for the specific router, you can add to the prompt the router's troubleshooting guide as context for it to refer to when providing a response. Includes contextual information  
---  
**Prompt:**
    
    
    Answer the question using the text below. Respond with only the text provided.
    Question: What should I do to fix my disconnected wifi? The light on my Google Wifi router is yellow and blinking slowly.
    
    Text:
    Color: Slowly pulsing yellow
    What it means: There is a network error.
    What to do:
    Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.
    
    Color: Fast blinking yellow
    What it means: You are holding down the reset button and are factory resetting this device.
    What to do:
    If you keep holding down the reset button, after about 12 seconds, the light will turn solid yellow. Once it is solid yellow, let go of the factory reset button.
    
    Color: Solid yellow
    What it means: Router is factory resetting.
    What to do:
    This can take up to 10 minutes. When it's done, the device will reset itself and start pulsing white, letting you know it's ready for setup.
    
    Color: Solid red
    What it means: Something is wrong.
    What to do:
    Critical failure. Factory reset the router. If the light stays red, contact Wifi customer support.
      

**Response:**
    
    
    Check that the Ethernet cable is connected to both your router and your modem and both devices are turned on. You might need to unplug and plug in each device again.
      

(gemini-pro)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
