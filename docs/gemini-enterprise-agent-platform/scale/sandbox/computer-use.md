---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use/
title: Computer Use \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:41:50.078588+00:00
---

# Computer Use  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Computer Use Stay organized with collections  Save and categorize content based on your preferences. 

Agent Platform Computer Use sandboxes provide a secure, isolated browser environment that your agents can interact with. These sandboxes allow agents to automate tasks that mimic human interactions (such as clicking, navigating sites, and taking screenshots).

## How it works

When you create a Computer Use sandbox, Gemini Enterprise Agent Platform provisions a containerized environment that runs a web browser agent. You can control the browser in two ways:

  * **API requests** : Send commands to the sandbox to perform actions like navigating to a URL, clicking on elements, or typing text.
  * **Browser control** : Connect to the browser by using a standard Chrome DevTools Protocol (CDP) connection, letting you use browser automation tools (such as Playwright) to automate the browser.



### Control the browser using API

You can send API requests to the sandbox to perform common browser actions. The sandbox handles the execution of these actions within its isolated environment.

Supported actions include:

  * Navigating to a URL.
  * Clicking at specific coordinates.
  * Typing text into fields.
  * Taking screenshots.



For an example of how to send commands, see the [Computer Use quickstart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use-quickstart).

### Control the browser using a CDP connection

For more advanced automation, you can connect to the sandbox browser over a Chrome DevTools Protocol (CDP) connection. This method lets you use standard browser automation tools, such as Playwright, to interact with the webpage.

To connect Playwright to the sandbox:

  1. Generate the WebSocket URL and required headers for your sandbox by using the Python SDK `generate_browser_ws_headers` method.
         
         service_account_email = "SERVICE_ACCOUNT_EMAIL"
           ws_url, ws_headers = client.agent_engines.sandboxes.generate_browser_ws_headers(
               sandbox_environment=sandbox,
               service_account_email=service_account_email,
           )
         

  2. Use Playwright's `connect_over_cdp` method to establish a connection.

Use the generated WebSocket URL and headers to connect over CDP using Playwright:
         
         import asyncio
           from playwright.async_api import async_playwright
           import nest_asyncio
           nest_asyncio.apply()
         
           async def connect_over_cdp(ws_url, ws_headers):
               async with async_playwright() as p:
                   try:
                       browser = await p.chromium.connect_over_cdp(
                           endpoint_url=ws_url,
                           headers=ws_headers
                       )
                       print("Successfully connected to browser over CDP.")
         
                       # You can now interact with the browser
                       page = browser.contexts[0].pages[0]
                       await page.goto("https://www.example.com")
                       print(f"Page title: {await page.title()}")
         
                       await browser.close()
                       print("Browser connection closed.")
                   except Exception as e:
                       print(f"An error occurred: {e}")
         
           # Run CDP connection
           asyncio.run(connect_over_cdp(ws_url, ws_headers))
         




## Live streaming view

Computer Use sandboxes support a live streaming view (VNC), letting you to visually monitor the agent's actions in real-time. You can debug and observe the agent's behavior.

For example, you can use noVNC to connect to the sandbox through WebSocket.

## What's next

  * [Computer Use quickstart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use-quickstart)
  * [Configure VPC Service Controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/configure-vpc-sc)
  * [Configure customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/configure-cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
