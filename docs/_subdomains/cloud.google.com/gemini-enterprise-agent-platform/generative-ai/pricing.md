---
url: https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing/
title: Agent Platform Pricing | Google Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:19:11.494280+00:00
---

# Agent Platform Pricing | Google Cloud

> Source: https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing/

Page Contents




Gemini 3.8 Flash, Gemini 3.7 Flash, Gemini 3.6 Flash, and CodeMender using these models are offered with introductory pricing of $0.75 / $3.75 per 1M tokens input / output through December 31, 2026. Starting January 1, 2027, standard pricing of $1.5 / $7.5 per 1M tokens input / output will apply.

## 

Cost of building and deploying AI models in Agent Platform

Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

You're charged only for requests that return a 200 response code. Requests returning any other response codes, such as 4xx and 5xx codes, aren't charged for the input or output.

This page covers pricing for Generative AI on Agent Platform. For all other Agent Platform pricing including ML Platform and MLOps services please refer to [Agent Platform pricing page](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing).

Flexible Savings Plans (FSPs) are spend-based committed use discounts that help you save money on your usage across eligible products on Google Cloud. For more information about how FSPs work and eligible products, see [Flexible Savings Plans](https://docs.cloud.google.com/docs/cuds-flexible-savings-plans).

# 

Google models

## 

Gemini 4

Standard ModelPriorityBatch / Flex

Model| Type| Region| Price (/1M tokens)| Price (/1M tokens) Cached input  
---|---|---|---|---  
Gemini 4 Argon*through November 30, 2026| Input (text, image, video, audio)| Global| $2| $0.1  
| | Non-global| $2.2| $0.11  
| Text output (response and reasoning)| Global| $10| $10  
| | Non-global| $11| $11  
Gemini 4 Argon(Starting December 1, 2026),Gemini 4 Argon Cyber Permissive| Input (text, image, video, audio)| Global| $4| $0.2  
| | Non-global| $4.4| $0.22  
| Text output (response and reasoning)| Global| $20| $20  
| | Non-global| $22| $22  
  
* Promotional pricing provided through 50% credits back on net spend on select models within a given period. Promotional pricing does not apply to Gemini 4 Argon Cyber Permissive.

Model| Type| Region| Price (/1M tokens)| Price (/1M tokens) Cached input  
---|---|---|---|---  
Gemini 4 Argon*through November 30, 2026| Input (text, image, video, audio)| Global| $3.6| $0.18  
| | Non-global| $3.96| $0.198  
| Text output (response and reasoning)| Global| $18| $18  
| | Non-global| $19.8| $19.8  
Gemini 4 Argon(Starting December 1, 2026),Gemini 4 Argon Cyber Permissive| Input (text, image, video, audio)| Global| $7.2| $0.36  
| | Non-global| $7.92| $0.396  
| Text output (response and reasoning)| Global| $36| $36  
| | Non-global| $39.6| $39.6  
  
* Promotional pricing provided through 50% credits back on net spend on select models within a given period. Promotional pricing does not apply to Gemini 4 Argon Cyber Permissive.

Model| Type| Region| Price (/1M tokens)| Price (/1M tokens) Cached input  
---|---|---|---|---  
Gemini 4 Argon*through November 30, 2026| Input (text, image, video, audio)| Global| $1| $0.05  
| | Non-global| $1.1| $0.055  
| Text output (response and reasoning)| Global| $5| $5  
| | Non-global| $5.5| $5.5  
Gemini 4 Argon(Starting December 1, 2026),Gemini 4 Argon Cyber Permissive| Input (text, image, video, audio)| Global| $2| $0.1  
| | Non-global| $2.2| $0.11  
| Text output (response and reasoning)| Global| $10| $10  
| | Non-global| $11| $11  
  
* Promotional pricing provided through 50% credits back on net spend on select models within a given period. Promotional pricing does not apply to Gemini 4 Argon Cyber Permissive.

Pricing with grounding

Show discount options

Feature| Usage| Price (USD)  
---|---|---  
Grounding with Google Search & Web Grounding for Enterprise| Includes 5,000 Grounding Queries per month at no charge, aggregated across all Gemini 3 and Gemini 4 models.Grounding Queries exceeding those limits are billed at **$14 per 1,000 Grounding Queries**. Please contact your account team if you require more than 1 million Grounding Prompts per day.A “**Grounding Prompt** ” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to a Google web index (each a “**Grounding Query** ”) . You will be charged for each individual Grounding Query performed.Input tokens provided by Grounding with Google Search or Web Grounding for Enterprise are not charged.Customers may decide not to display Search Suggestions with Grounded Results in their Customer Applications at standard pricing for under 1 million Grounding Prompts per day.| 0 count to 5,000 count$0.00 (Free) / 1,000 count, per 1 month / account5,000 count and above$14.00 / 1,000 count, per 1 month / account  
Grounding with Google Maps| Includes 5,000 search queries per month at no charge, aggregated across all Gemini 3 and Gemini 4 models.Maps queries exceeding those limits are billed at $14 per 1,000 queries. A customer-submitted request to Gemini may result in one or more queries to Google Maps. You will be charged for each individual query performed.Input tokens provided by Google Maps are not charged.| 0 count to 5,000 count$0.00 (Free) / 1,000 count, per 1 month / account5,000 count and above$14.00 / 1,000 count, per 1 month / account  
Grounding with your data| $2.50 per 1,000 prompts.| $2.50 / 1,000 count  
Computer Use Tool| Pricing is based on the total number of input tokens sent to the model and resulting output tokens generated. Token prices are based on the [respective model used](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#gemini-4).Function declarations are included in the input token count.For additional detail, see [documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/computer-use).|   
  
* For non-global endpoints, pricing will go into effect for the Generally available Gemini 3 and later families of all Google models starting on July 1, 2026. Before July 1, 2026, Global endpoint pricing applies to Non-global endpoints.

* If a query input context is longer than 200K tokens, all tokens (input and output) are charged at long context rates.

* Tuned model endpoint will be 1.5 times of the base model.

** Gemini 3 Pro Image charges 560 tokens per input image, with output image costs scaling by resolution: 1120 tokens ($0.134) for 1K and 2K (roughly 1MP and 4MP), and 2000 tokens ($0.24) for 4K (roughly 16MP).

*** Gemini 3.1 Flash Image charges 1120 tokens per input image, with output image costs scaling by resolution: 747 tokens ($0.045) for 512 (roughly 0.25MP), 1120 tokens ($0.067) for 1K (roughly 1MP), 1680 tokens ($0.101) for 2K (roughly 4MP), and 2,520 tokens ($0.15) for 4K (roughly 16MP).

**** Gemini 3.1 Flash-Lite Image charges 1120 tokens per input image, and 1120 tokens ($0.034) for 1K (roughly 1MP) output images

## 

Gemini 3

Standard ModelPriorityFlex/Batch

Show discount options

Model| Type| Region| Price (/1M tokens)<= 200K input tokens| Price (/1M tokens)> 200K input tokens| Price (/1M tokens)<= 200K cached input tokens| Price (/1M tokens)> 200K cached input tokens  
---|---|---|---|---|---|---  
Gemini 3.8 Live API | Input: text| Non-global| $0.75| $0.75| N/A| N/A  
| Input: video, image| Non-global| $1.00| $1.00| N/A| N/A  
| Input: Audio| Non-global| $3.00| $3.00| N/A| N/A  
| Output: text (response and reasoning)| Non-global| $4.50| $4.50| N/A| N/A  
| Output: audio| Non-global| $12.00| $12.00| N/A| N/A  
| Output: video (avatar)| Non-global| $1.00| $1.00| N/A| N/A  
Gemini 3.1 Pro Preview| Input (text, image, video, audio)| Global| $2.00| $4.00| $0.20| $0.40  
| Text output (response and reasoning)| Global| $12.00| $18.00| N/A| N/A  
Gemini 3.8 Flash Cyber| Input (text, image, video, audio)| Global| $1.50| $1.50| $0.15| $0.15  
| | Non-global| $1.65| $1.65| $0.165| $0.165  
| Text output (response and reasoning)| Global| $7.50| $7.50| N/A| N/A  
| | Non-global| $8.25| $8.25| N/A| N/A  
Gemini 3.8 Flash*through December 31, 2026| Input (text, image, video, audio)| Global| $0.75| $0.75| $0.075| $0.075  
| | Non-global| $0.825| $0.825| $0.0825| $0.0825  
| Text output (response and reasoning)| Global| $3.75| $3.75| N/A| N/A  
| | Non-global| $4.125| $4.125| N/A| N/A  
Gemini 3.8 FlashStarting January 1, 2027| Input (text, image, video, audio)| Global| $1.50| $1.50| $0.15| $0.15  
| | Non-global| $1.65| $1.65| $0.165| $0.165  
| Text output (response and reasoning)| Global| $7.50| $7.50| N/A| N/A  
| | Non-global| $8.25| $8.25| N/A| N/A  
Gemini 3.7 Flash *through December 31, 2026| Input (text, image, video, audio)| Global| $0.75| $0.75| $0.075| $0.075  
| | Non-global| $0.825| $0.825| $0.0825| $0.0825  
| Text output (response and reasoning)| Global| $3.75| $3.75| N/A| N/A  
| | Non-global| $4.125| $4.125| N/A| N/A  
Gemini 3.7 Flashstarting January 1, 2027| Input (text, image, video, audio)| Global| $1.50| $1.50| $0.15| $0.15  
| | Non-global| $1.65| $1.65| $0.165| $0.165  
| Text output (response and reasoning)| Global| $7.50| $7.50| N/A| N/A  
| | Non-global| $8.25| $8.25| N/A| N/A  
Gemini 3.6 Flash *through December 31, 2026| Input (text, image, video, audio)| Global| $0.75| $0.75| $0.075| $0.075  
| | Non-global| $0.825| $0.825| $0.0825| $0.0825  
| Text output (response and reasoning)| Global| $3.75| $3.75| N/A| N/A  
| | Non-global| $4.125| $4.125| N/A| N/A  
Gemini 3.6 Flashstarting January 1, 2027|  Input (text, image, video, audio)| Global| $1.50| $1.50| $0.15| $0.15  
| | Non-global| $1.65| $1.65| $0.165| $0.165  
| Text output (response and reasoning)| Global| $7.50| $7.50| N/A| N/A  
| | Non-global| $8.25| $8.25| N/A| N/A  
Gemini 3 Flash Preview| Input (text, image, video)| Global| $0.50| $0.50| $0.05| $0.05  
| Input (audio)| Global| $1.00| $1.00| $0.10| $0.10  
Gemini 3.5 Flash| Input (text, image, video, audio)| Global| $1.50| $1.50| $0.15| $0.15  
| | Non-global*  
| $1.65| $1.65| $0.165| $0.165  
| Text output (response and reasoning)| Global| $9.00| $9.00| N/A| N/A  
| | Non-global*| $9.90| $9.90| N/A| N/A  
Gemini 3.5 Flash-Lite  
| Input (text, image, video, audio)| Global| $0.30| $0.30| $0.03| $0.03  
| | Non-global*| $0.33| $0.33| $0.033| $0.033  
| Text output (response and reasoning)| Global| $2.50| $2.50| N/A| N/A  
| | Non-global*| $2.75| $2.75| N/A| N/A  
Gemini 3.1 Flash-Lite| Input (text, image, video)| Global| $0.25| $0.25| $0.025| $0.025  
| | Non-global*| $0.275| $0.275| $0.0275| $0.0275  
| Input (audio)| Global| $0.50| $0.50| $0.05| $0.05  
| | Non-global*| $0.55| $0.55| $0.055| $0.055  
| Text output (response and reasoning)| Global| $1.50| $1.50| N/A| N/A  
| | Non-global*| $1.65| $1.65| N/A| N/A  
  
* Promotional pricing provided through 50% credits back on net spend on select models within a given period.

**** Live API Billing Details:**

**Session Context Window:** tokens consumption is calculated per turn (defined as one user input and the model's corresponding response). Users are charged for all tokens present in the Session Context Window during that turn.

**Tokens accumulation:** The context window includes new tokens for the current turn plus all accumulated tokens from previous turns. Tokens from past turns are re-processed and billed in every new turn, up to the configured context window size limit.

**Token Conversion Rates:** To help users estimate costs, the following conversion metrics apply:

  * Audio: 25 tokens /second of audio.
  * Image Input: 258 tokens per image.
  * Avatar Video Output: 6,192 tokens /second of video. Video output charges only apply when the avatar is actively speaking; users are not billed for idle time (when avatar is listening).
  * Audio-to-Text Transcription: charged at the standard text output rate for all text tokens generated when transcription is enabled.



**Thinking Tokens:** To audit how many thinking tokens a specific request used, review the **_thoughts_** field within the API response metadata.

Show discount options

Model| Type| Region| Price (/1M tokens)<= 200K input tokens with Priority| Price (/1M tokens)> 200K input tokens with Priority| Price (/1M tokens)<= 200K cached input tokens with Priority| Price (/1M tokens)> 200K cached input tokens with Priority  
---|---|---|---|---|---|---  
Gemini 3.1 Pro Preview| Input (text, image, video, audio)| Global| $3.60| $7.20| $0.36| $0.72  
| Text output (response and reasoning)| Global| $21.60| $32.40| N/A| N/A  
Gemini 3.8 Flash Cyber| Input (text, image, video, audio)| Global| $2.70| $2.70| $0.27| $0.27  
| | Non-global| $2.97| $2.97| $0.297| $0.297  
| Text output (response and reasoning)| Global| $13.50| $13.50| N/A| N/A  
| | Non-global| $14.85| $14.85| N/A| N/A  
Gemini 3.8 Flash*through December 31, 2026| Input (text, image, video, audio)| Global| $1.35| $1.35| $0.135| $0.135  
| | Non-global| $1.485| $1.485| $0.1485| $0.1485  
| Text output (response and reasoning)| Global| $6.75| $6.75| N/A| N/A  
| | Non-global| $7.425| $7.425| N/A| N/A  
Gemini 3.8 FlashStarting January 1, 2027| Input (text, image, video, audio)| Global| $2.70| $2.70| $0.27| $0.27  
| | Non-global| $2.97| $2.97| $0.297| $0.297  
| Text output (response and reasoning)| Global| $13.50| $13.50| N/A| N/A  
| | Non-global| $14.85| $14.85| N/A| N/A  
Gemini 3.7 Flash *through December 31, 2026| Input (text, image, video, audio)| Global| $1.35| $1.35| $0.135| $0.135  
| | Non-global| $1.485| $1.485| $0.1485| $0.1485  
| Text output (response and reasoning)| Global| $6.75| $6.75| N/A| N/A  
| | Non-global| $7.425| $7.425| N/A| N/A  
Gemini 3.7 Flashstarting January 1, 2027| Input (text, image, video, audio)| Global| $2.70| $2.70| $0.27| $0.27  
| | Non-global| $2.97| $2.97| $0.297| $0.297  
| Text output (response and reasoning)| Global| $13.50| $13.50| N/A| N/A  
| | Non-global| $14.85| $14.85| N/A| N/A  
Gemini 3.6 Flash *through December 31, 2026| Input (text, image, video, audio)| Global| $1.35| $1.35| $0.135| $0.135  
| | Non-global| $1.485| $1.485| $0.1485| $0.1485  
| Text output (response and reasoning)| Global| $6.75| $6.75| N/A| N/A  
| | Non-global| $7.425| $7.425| N/A| N/A  
Gemini 3.6 Flashstarting January 1, 2027| Input (text, image, video, audio)| Global| $2.70| $2.70| $0.27| $0.27  
| | Non-global| $2.97| $2.97| $0.297| $0.297  
| Text output (response and reasoning)| Global| $13.50| $13.50| N/A| N/A  
| | Non-global| $14.85| $14.85| N/A| N/A  
Gemini 3 Flash Preview| Input (text, image, video)| Global| $0.90| $0.90| $0.09| $0.09  
| Input (audio)| Global| $1.80| $1.80| $0.18| $0.18  
| Text output (response and reasoning)  
| Global| $5.40| $5.40| N/A| N/A  
Gemini 3.5 Flash| Input (text, image, video, audio)| Global| $2.70| $2.70| $0.27| $0.27  
| | Non-global*| $2.97| $2.97| $0.297| $0.297  
| Text output (response and reasoning)| Global| $16.20| $16.20| N/A| N/A  
| | Non-global*| $17.82| $17.82| N/A| N/A  
Gemini 3.5 Flash-Lite| Input (text, image, video, audio)| Global| $0.54| $0.54| $0.054| $0.054  
| | Non-global*| $0.594| $0.594| $0.0594| $0.0594  
| Text output (response and reasoning)| Global| $4.50| $4.50| N/A| N/A  
| | Non-global*| $4.95| $4.95| N/A| N/A  
Gemini 3.1 Flash-Lite| Input (text, image, video)| Global| $0.45| $0.45| $0.045| $0.045  
| | Non-global*| $0.495| $0.495| $0.0495| $0.0495  
| Input (audio)| Global| $0.90| $0.90| $0.09| $0.09  
| | Non-global*| $0.99| $0.99| $0.099| $0.099  
| Text output (response and reasoning)| Global| $2.70| $2.70| N/A| N/A  
| | Non-global*| $2.97| $2.97| N/A| N/A  
  
* Promotional pricing provided through 50% credits back on net spend on select models within a given period.

Show discount options

Model| Type| Region| Price (/1M tokens)<= 200K input tokens with Flex/Batch| Price (/1M tokens)> 200K input tokens with Flex/Batch| Price (/1M tokens)<= 200K cached input tokens with Flex/Batch| Price (/1M tokens)> 200K cached input tokens with Flex/Batch  
---|---|---|---|---|---|---  
Gemini 3.1 Pro Preview| Input (text, image, video, audio)| Global| $1.00| $2.00| N/A| N/A  
| Text output (response and reasoning)| Global| $6.00| $9.00| N/A| N/A  
Gemini 3.8 Flash Cyber| Input (text, image, video, audio)| Global| $0.75| $0.75| $0.075| $0.075  
| | Non-global| $0.825| $0.825| $0.0825| $0.0825  
| Text output (response and reasoning)| Global| $3.75| $3.75| N/A| N/A  
| | Non-global| $4.125| $4.125| N/A| N/A  
Gemini 3.8 Flash*through December 31, 2026| Input (text, image, video, audio)| Global| $0.375| $0.375| $0.0375| $0.0375  
| | Non-global| $0.4125| $0.4125| $0.04125| $0.04125  
| Text output (response and reasoning)| Global| $1.875| $1.875| N/A| N/A  
| | Non-global| $2.0625| $2.0625| N/A| N/A  
Gemini 3.8 FlashStarting January 1, 2027| Input (text, image, video, audio)| Global| $0.75| $0.75| $0.075| $0.075  
| | Non-global| $0.825| $0.825| $0.0825| $0.0825  
| Text output (response and reasoning)| Global| $3.75| $3.75| N/A| N/A  
| | Non-global| $4.125| $4.125| N/A| N/A  
Gemini 3.7 Flash *through December 31, 2026| Input (text, image, video, audio)| Global| $0.375| $0.375| $0.0375| $0.0375  
| | Non-global| $0.4125| $0.4125| $0.04125| $0.04125  
| Text output (response and reasoning)| Global| $1.875| $1.875| N/A| N/A  
| | Non-global| $2.0625| $2.0625| N/A| N/A  
Gemini 3.7 Flashstarting January 1, 2027| Input (text, image, video, audio)  
| Global| $0.75| $0.75| $0.075| $0.075  
| | Non-global| $0.825| $0.825| $0.0825| $0.0825  
| Text output (response and reasoning)| Global| $3.75| $3.75| N/A| N/A  
| | Non-global| $4.125| $4.125| N/A| N/A  
Gemini 3.6 Flash *through December 31, 2026| Input (text, image, video, audio)| Global| $0.375| $0.375| $0.0375| $0.0375  
| | Non-global| $0.4125| $0.4125| $0.04125| $0.04125  
| Text output (response and reasoning)| Global| $1.875| $1.875| N/A| N/A  
| | Non-global| $2.0625| $2.0625| N/A| N/A  
Gemini 3.6 Flashstarting January 1, 2027| Input (text, image, video, audio)| Global| $0.75| $0.75| $0.075| $0.075  
| | Non-global| $0.825| $0.825| $0.0825| $0.0825  
| Text output (response and reasoning)| Global| $3.75| $3.75| N/A| N/A  
| | Non-global| $4.125| $4.125| N/A| N/A  
Gemini 3 Flash Preview| Input (text, image, video)| Global| $0.25| $0.25| N/A| N/A  
| Input (audio)| Global| $0.50| $0.50| N/A| N/A  
| Text output (response and reasoning)| Global| $1.50| $1.50| N/A| N/A  
Gemini 3.5 Flash| Input (text, image, video, audio)| Global (Batch)| $0.75| $0.75| $0.075| $0.075  
| | Global (Flex)| $0.75| $0.75| $0.075| $0.075  
| | Non-global*| $0.825| $0.825| $0.0825| $0.0825  
| Text output (response and reasoning)| Global| $4.50| $4.50| N/A| N/A  
| | Non-global*| $4.95| $4.95| N/A| N/A  
Gemini 3.5 Flash-Lite| Input (text, image, video, audio)| Global| $0.15| $0.15| $0.015| $0.015  
| | Non-global*| $0.165| $0.165| $0.0165| $0.0165  
| Text output (response and reasoning)| Global| $1.25| $1.25| N/A| N/A  
| | Non-global*| $1.375| $1.375| N/A| N/A  
Gemini 3.1 Flash-Lite| Input (text, image, video)| Global| $0.125| $0.125| $0.0125| $0.0125  
| | Non-global*| $0.1375| $0.1375| $0.01375| $0.01375  
| Input (audio)| Global| $0.25| $0.25| $0.025| $0.025  
| | Non-global*| $0.275| $0.275| $0.0275| $0.0275  
| Text output (response and reasoning)| Global| $0.75| $0.75| N/A| N/A  
| | Non-global*| $0.825| $0.825| N/A| N/A  
  
* Promotional pricing provided through 50% credits back on net spend on select models within a given period.

Pricing with grounding

Show discount options

Feature| Usage| Price (USD)  
---|---|---  
Grounding with Google Search & Web Grounding for Enterprise| Includes 5,000 Grounding Queries per month at no charge, aggregated across all Gemini 3 and Gemini 4 models.Grounding Queries exceeding those limits are billed at **$14 per 1,000 Grounding Queries**. Please contact your account team if you require more than 1 million Grounding Prompts per day.A “**Grounding Prompt** ” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to a Google web index (each a “**Grounding Query** ”) . You will be charged for each individual Grounding Query performed. Billing will start January 5, 2026. Input tokens provided by Grounding with Google Search or Web Grounding for Enterprise are not charged.Customers may decide not to display Search Suggestions with Grounded Results in their Customer Applications at standard pricing for under 1 million Grounding Prompts per day.| 0 count to 5,000 count$0.00 (Free)5,000 count and above$14.00  
Grounding with Google Maps| Includes 5,000 search queries per month at no charge, aggregated across all Gemini 3 and Gemini 4 models.Maps queries exceeding those limits are billed at $14 per 1,000 queries. A customer-submitted request to Gemini may result in one or more queries to Google Maps. You will be charged for each individual query performed. Billing will start January 5, 2026Input tokens provided by Google Maps are not charged.| 0 count to 5,000 count$0.00 (Free)5,000 count and above$14.00  
Grounding with your data| $2.50 per 1,000 prompts.| $2.50  
Computer Use Tool| Pricing is based on the total number of input tokens sent to the model and resulting output tokens generated. Token prices are based on the [respective model used](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#googlemodels).Starting with Gemini 3.5, function declarations are included in the input token count.For additional detail, see [documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/computer-use).|   
  
* For non-global endpoints, pricing will go into effect for the Generally available Gemini 3 and later families of all Google models starting on July 1, 2026. Before July 1, 2026, Global endpoint pricing applies to Non-global endpoints.

* If a query input context is longer than 200K tokens, all tokens (input and output) are charged at long context rates.

* Tuned model endpoint will be 1.5 times of the base model.

** Gemini 3 Pro Image charges 560 tokens per input image, with output image costs scaling by resolution: 1120 tokens ($0.134) for 1K and 2K (roughly 1MP and 4MP), and 2000 tokens ($0.24) for 4K (roughly 16MP).

*** Gemini 3.1 Flash Image charges 1120 tokens per input image, with output image costs scaling by resolution: 747 tokens ($0.045) for 512 (roughly 0.25MP), 1120 tokens ($0.067) for 1K (roughly 1MP), 1680 tokens ($0.101) for 2K (roughly 4MP), and 2,520 tokens ($0.15) for 4K (roughly 16MP).

**** Gemini 3.1 Flash-Lite Image charges 1120 tokens per input image, and 1120 tokens ($0.034) for 1K (roughly 1MP) output images

## 

Gemini 2.5

StandardPriorityFlex/Batch

Show discount options

Model| Type| Token Price <= 200K tokens| Price > 200K tokens| Price <= 200K cached input tokens| Price > 200K cached input tokens  
---|---|---|---|---|---  
Gemini 2.5 Pro| Input (text, image, video, audio)| $1.25| $2.50| $0.125| $0.25  
| Text output (response and reasoning)| $10.00| $15.00| N/A| N/A  
Gemini 2.5 ProComputer Use-Preview| Input (text, image, video, audio)| $1.25| $2.50| N/A| N/A  
| Text output (response and reasoning)| $10.00| $15.00| N/A| N/A  
Gemini 2.5 Flash| Input (text, image, video)| $0.30| $0.30| $0.03| $0.03  
| Audio Input| $1.00| $0.30| $0.10| $0.10  
| Text output (response and reasoning)| $2.50| $2.50| N/A| N/A  
Gemini 2.5 Flash Image| Input (text, image)***| $0.30| N/A| N/A| N/A  
| Text output (response and reasoning)| $2.50| N/A| N/A| N/A  
| Image output***| $30.00| N/A| N/A| N/A  
Gemini 2.5 Flash Live API| Input text| $0.50| $0.50| N/A| N/A  
| Input (video, image)| $3.00| $3.00| N/A| N/A  
| Audio Input| $3.00| $3.00| N/A| N/A  
| Text output| $2.00| $2.00| N/A| N/A  
| 1M output audio tokens| $12.00| $12.00| N/A| N/A  
Gemini 2.5 Flash Lite| Input (text, image, video)| $0.10| $0.10| $0.01| $0.01  
| Audio Input| $0.30| $0.30| $0.03| $0.03  
| Text output (response and reasoning)| $0.40| $0.40| N/A| N/A  
  
Show discount options

Model| Type| Price (/1M tokens) <= 200K input tokens with Priority| Price (/1M tokens) > 200K input tokens with Priority| Price (/1M tokens) <= 200K cached input tokens with Priority| Price (/1M tokens) > 200K cached input tokens with Priority  
---|---|---|---|---|---  
Gemini 2.5 Pro| Input (text, image, video, audio)| $2.25| $4.50| $0.225| $0.45  
| Text output (response and reasoning)| $18.00| $27.00| N/A| N/A  
Gemini 2.5 ProComputer Use-Preview| Input (text, image, video, audio)| N/A| N/A| N/A| N/A  
| Text output (response and reasoning)| N/A| N/A| N/A| N/A  
Gemini 2.5 Flash| Input (text, image, video)| $0.54| $0.54| $0.054| $0.054  
| Audio Input| $1.80| $1.80| $0.18| $0.18  
| Text output (response and reasoning)| $4.50| $4.50| N/A| N/A  
Gemini 2.5 Flash Image| Input (text, image)***| N/A| N/A| N/A| N/A  
| Text output (response and reasoning)| N/A| N/A| N/A| N/A  
| Image output***| N/A| N/A| N/A| N/A  
Gemini 2.5 Flash Live API| 1M input text tokens| N/A| N/A| N/A| N/A  
| 1M input audio tokens| N/A| N/A| N/A| N/A  
| 1M input video/image tokens| N/A| N/A| N/A| N/A  
| 1M output text tokens| N/A| N/A| N/A| N/A  
| 1M output audio tokens| N/A| N/A| N/A| N/A  
Gemini 2.5 Flash Lite| Input (text, image, video)| $0.18| $0.18| $0.018| $0.018  
| Audio Input| $0.54| $0.54| $0.054| $0.054  
| Text output (response and reasoning)| $0.72| $0.72| N/A| N/A  
  
Show discount options

Model| Type| Price (/1M tokens) <= 200K input tokens with Flex/Batch| Price (/1M tokens) > 200K input tokens with Flex/Batch  
---|---|---|---  
Gemini 2.5 Pro| Input (text, image, video, audio)| $0.625| $1.25  
| Text output (response and reasoning)| $5.00| $7.50  
Gemini 2.5 ProComputer Use-Preview| Input (text, image, video, audio)| N/A| N/A  
| Text output (response and reasoning)| N/A| N/A  
Gemini 2.5 Flash| Input (text, image, video)| $0.15| $0.15  
| Audio Input| $0.50| $0.50  
| Text output (response and reasoning)| $1.25| $1.25  
Gemini 2.5 Flash Image| Input (text, image, video)***| $0.15| N/A  
| Text output (response and reasoning)| $1.25 | N/A  
| Image output***| $15.00| N/A  
Gemini 2.5 Flash Live API| 1M input text tokens| N/A| N/A  
| 1M input audio tokens| N/A| N/A  
| 1M input video/image tokens| N/A| N/A  
| 1M output text tokens| N/A| N/A  
| 1M output audio tokens| N/A| N/A  
Gemini 2.5 Flash Lite| Input (text, image, video)| $0.05| $0.05  
| Audio Input| $0.05| $0.05  
| Text output (response and reasoning)| $0.20| $0.20  
  
Pricing with grounding

Show discount options

Feature| Usage| Price (USD)  
---|---|---  
Grounding with Google Search| Gemini 2.0 Flash, 2.5 Flash and 2.5 Flash-Lite include a combined 1,500 Grounding Prompts per day at no additional charge. Gemini 2.5 Pro includes 10,000 Grounding Prompts per day at no additional charge.Grounding Prompts exceeding those limits are billed at **$35 per 1,000 Grounding Prompts**. Please contact your account team if you require more than 1 million Grounding Prompts per day.A “**Grounding Prompt** ” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to a Google web index (each a “**Grounding Query** ”)**. Even if multiple Grounding Queries are sent, there is only one charge for a Grounding Prompt.| 0 count to 10,000 count$0.00 (Free)10,000 count and above$35.00  
Web Grounding for enterprise| **$45 per 1,000 Grounding Prompts.** Please contact your account team if you require more than 1 million Grounding Prompts per day.A “**Grounding Prompt** ” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to a Google web index (each a “**Grounding Query** ”)**. Even if multiple Grounding Queries are sent, there is only one charge for a Grounding Prompt.| $45.00  
Grounding with your data| $2.5 per 1,000 requests.| $2.50  
Grounding with Google Maps| **$25 per 1,000 grounded prompts.** One grounded prompt is a request sent to Gemini that makes at least 1 query to Google Maps.| 0 count to 1,500 count$0.00 (Free)1,500 count and above$25.00  
  
* If a query input context is longer than 200K tokens, all tokens (input and output) are charged at long context rates.

* Tuned model endpoint has the same prediction price as the base model.

** Grounding with Google Search and Web Grounding for Enterprise are billed only when a Grounding Prompt successfully returns sources (i.e., results containing at least one support URL from the web). Gemini model usage fees apply separately.

*** A 1024x1024 image consumes 1290 tokens ($0.039 per 1K output image). Per image token count varies by image resolution. For more information on how to calculate tokens, you can refer to our [documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding#image-requirements).

**** Computer Use billing uses the Gemini 2.5 Pro SKU, to split out Computer Use costs, apply billing tags. See more [here](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/add-labels-to-api-calls).

  * **LiveAPI Session's Context Window billing explained** : You are charged per turn for all tokens present in the Session Context Window. The Session Context Window includes new tokens (current turn) + all accumulated tokens from previous turns. This means tokens from past turns are re-processed and accounted for in each new turn, up to your configured context window size. A "turn" is one user input and the model's response.
  * **Proactive Audio Mode** : When enabled, input tokens are charged while LiveAPI is listening. Output tokens are only charged when the API responds.
  * When audio to text transcription is enabled, all text tokens generated for transcription are charged at the text token output rate.



## 

Gemini 2.0

Gemini 2.0 is billed based on tokens. To calculate the number of input tokens in your request prior to sending the request, you can use the [_SDK tokenizer_](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/list-token) or the [_countTokens API_](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/get-token-count). If your request fails with a 400 or 500 error, you won't be charged for the tokens used.

Use the toggle in the pricing table to compare token-based pricing and modality-based pricing.

Token-based pricingModality-based pricing

Show discount options

Model| Type| Price /1M tokens (USD)| Price /1M tokens (USD) with Batch API  
---|---|---|---  
Gemini 2.0 Flash| Input text| $0.15| $0.075  
|  Input audio| $1.00| $0.50  
| Output text| $0.60| $0.30  
| Tuning training| $0.003|   
Gemini 2.0 Flash Image Generation| Input tokens| $0.15|   
| Input audio tokens| $1.00|   
| Input video tokens| $0.15|   
| Output text tokens| $0.60|   
| Output image tokens| $30.00|   
Gemini 2.0 Flash Live API| Input text tokens| $0.50|   
| Input audio tokens| $3.00|   
| Input video/image tokens| $3.00|   
| Output text tokens| $2.00|   
| Output audio tokens| $12.00|   
Gemini 2.0 Flash Lite| Input tokens| $0.075| $0.0375  
| Input audio tokens| $0.075| $0.0375  
| Output text tokens| $0.30| $0.15  
| Tuning for training tokens| $0.001|   
  
* Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

* Training tokens are calculated by the total number of tokens in your training dataset, multiplied by your number of epochs.

* PDFs are billed as image input, with one PDF page equivalent to one image.

* Tuned model endpoint has the same prediction price as the base model.

* Gemini 2.0 Flash Live API: 25 tokens per second of audio (input/output), 258 tokens per second of video (input). Grounding with Google Search remains free of charge while Gemini 2.0 Flash Live API is in Preview.

The below modality pricing is based on average use cases for reference only. Actual billing will only be based on tokens:

  * 4 characters result in approximately 1 text token including white space.
  * For an 1024x1024 image, it consumes 1290 tokens. Per image token count varies by image resolution. For more information on how to calculate tokens, you can refer to our [documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding#image-requirements).
  * Video input consumes 258 tokens per second at the sample rate of one frame per second. Video with audio bills for both video tokens and audio tokens.
  * Audio input consumes 25 tokens per second without timestamp.



Model| Type| Price (/1M tokens) (USD)| Price (/1M tokens) (USD) with Batch API  
---|---|---|---  
Gemini 2.0 Flash| Input text ($/M char)| $0.0375| $0.01875  
| Input image ($/image)| $0.0001935| $0.00009675  
| Input video ($/sec)| $0.0000387| $0.00001935  
| Input audio ($/sec)| $0.000025| $0.0000125  
| Output text ($/M char)| $0.15| $0.075  
Gemini 2.0 Flash Image Generation| Input text ($/M char)| $0.0375|   
| Input image ($/image)| $0.0001935|   
| Input video ($/sec)| $0.0000387|   
| Input audio ($/sec)| $0.000025|   
| Output text ($/M char)| $0.15|   
| Output image image ($/image)| $0.04|   
Gemini 2.0 Flash Lite| Input text ($/M char)| $0.01875| $0.009375  
| Input image ($/image)| $0.00009675| $0.000048375  
| Input video ($/sec)| $0.00001935| $0.000009675  
| Input audio ($/sec)| $0.000001875| $0.000000938  
| Output text ($/M char)| $0.075| $0.0375  
  
* Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

* Training tokens are calculated by the total number of tokens in your training dataset, multiplied by your number of epochs.

* PDFs are billed as image input, with one PDF page equivalent to one image.

* Tuned model endpoint has the same prediction price as the base model.

* Gemini 2.0 Flash Live API: 25 tokens per second of audio (input/output), 258 tokens per second of video (input). Grounding with Google Search remains free of charge while Gemini 2.0 Flash Live API is in Preview.

Price with Grounding

Show discount options

Feature| Usage| Price (USD)  
---|---|---  
Grounding with Google Search*, **| Gemini 2.0 Flash, 2.5 Flash and 2.5 Flash-Lite include a combined 1,500 Grounding Prompts per day at no additional charge. Gemini 2.5 Pro includes 10,000 Grounding Prompts per day at no additional charge.Grounding Prompts exceeding those limits are billed at **$35 per 1,000 Grounding Prompts**. Please contact your account team if you require more than 1 million Grounding Prompts per day.A “**Grounding Prompt** ” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to a Google web index (each a “**Grounding Query** ”)**. Even if multiple Grounding Queries are sent, there is only one charge for a Grounding Prompt.| 0 count to 10,000 count$0.00 (Free)10,000 count and above$35.00  
Web Grounding for enterprise*, **|  **$45 per 1,000 Grounding Prompts.** Please contact your account team if you require more than 1 million Grounding Prompts per day.A “**Grounding Prompt** ” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to a Google web index (each a “**Grounding Query** ”)**. Even if multiple Grounding Queries are sent, there is only one charge for a Grounding Prompt.| $45.00  
Grounding with your data*| $2.5 per 1,000 requests.| $2.50  
Grounding with Google Maps*| Gemini models include a number of daily grounded prompts at no extra cost:

  * **Gemini Flash and Flash-Lite** : combined 1,500 grounded prompts per day.
  * **Gemini Pro** : 10,000 grounded prompts per day.

Grounded prompts exceeding those limits are billed at $25 per 1,000 grounded prompts.One grounded prompt is a request sent to Gemini that makes at least 1 query to Google Maps.Please contact your account team if you require more than 1 million grounded prompts per day.| 0 count to 1,500 count$0.00 (Free)1,500 count and above$25.00  
  
* Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

* Training tokens are calculated by the total number of tokens in your training dataset, multiplied by your number of epochs.

* PDFs are billed as image input, with one PDF page equivalent to one image.

* Tuned model endpoint has the same prediction price as the base model.

* Gemini 2.0 Flash Live API: 25 tokens per second of audio (input/output), 258 tokens per second of video (input). Grounding with Google Search remains free of charge while Gemini 2.0 Flash Live API is in Preview.

** Grounding with Google Search and Web Grounding for Enterprise is billed only when a prompt successfully returns sources (i.e., results containing at least one support URL from the web). Gemini model usage fees apply separately.

  * **LiveAPI Session's Context Window billing explained** : You are charged per turn for all tokens present in the Session Context Window. The Session Context Window includes new tokens (current turn) + all accumulated tokens from previous turns. This means tokens from past turns are re-processed and accounted for in each new turn, up to your configured context window size. A "turn" is one user input and the model's response.
  * When audio to text transcription is enabled, all text tokens generated for transcription are charged at the text token output rate.



## 

Nano Banana

StandardPriorityFlex/Batch

Show discount options

Model| Type| Region| Price (/1M tokens)| Price (/1M tokens) cached input tokens  
---|---|---|---|---  
Gemini Nano Banana 2.1| Input (text, image, video) [4]| Global| $1.50| $0.15  
| Text output (response and reasoning)| Global| $7.50| N/A  
| Image Output [4]| Global| $30.00| N/A  
Gemini 3.1 Flash-Lite Image (Nano Banana 2 Lite)| Input (text, image, video) [3]| Global| $0.25| $0.025  
| Text output (response and reasoning)| Global| $1.50| N/A  
| Image Output [3]| Global| $30.00| N/A  
Gemini 3.1 Flash Image (Nano Banana 2)| Input (text, image, video) [2]| Global| $0.50| $0.05  
| | Non-global| $0.55| $0.055  
| Text output (response and reasoning)| Global| $3.00| N/A  
| | Non-global| $3.30| N/A  
| Image Output [2]| Global| $60.00| N/A  
| | Non-global| $66.00| N/A  
Gemini 3 Pro Image (Nano Banana Pro)| Input (text, image)| Global| $2.00| $0.20  
| Text output (response and reasoning)| Global| $12.00| N/A  
| Image Output [1]| Global| $120.00| N/A  
  
[1] Gemini 3 Pro Image charges 560 tokens per input image, with approximate output image costs scaling by resolution: 1120 tokens ($0.134) for 1K and 2K (roughly 1MP and 4MP), and 2000 tokens ($0.24) for 4K (roughly 16MP).

[2] Gemini 3.1 Flash Image charges 1120 tokens per input image, with approximate output image costs scaling by resolution: 747 tokens ($0.045) for 512 (roughly 0.25MP), 1120 tokens ($0.067) for 1K (roughly 1MP), 1680 tokens ($0.101) for 2K (roughly 4MP), and 2,520 tokens ($0.15) for 4K (roughly 16MP).

[3] Gemini 3.1 Flash-Lite Image charges 1120 tokens per input image, and 1120 tokens ($0.034) for 1K (roughly 1MP) output images

[4] Gemini Nano Banana 2.1 charges 1120 tokens per input image, with approximate output image costs scaling by resolution: 1120 tokens ($0.034) for 1K (roughly 1MP), 1680 tokens ($0.05) for 2K (roughly 4MP), and 3780 tokens ($0.113) for 4K (roughly 16MP). Gemini Nano Banana 2.1 does not support Flex

Show discount options

Model| Type| Region| Price (/1M tokens) with Priority| Price (/1M tokens) cached input tokens with Priority  
---|---|---|---|---  
Gemini Nano Banana 2.1| Input (text, image, video) [4]| Global| $2.70| $0.27  
| Text output (response and reasoning)| Global| $13.50| N/A  
| Image Output [4]| Global| $54.00| N/A  
Gemini 3.1 Flash-Lite Image (Nano Banana 2 Lite)| Input (text, image, video) [3]| Global| $0.45| $0.045  
| Text output (response and reasoning)| Global| $2.70| N/A  
| Image Output [3]| Global| $54.00| N/A  
Gemini 3.1 Flash Image (Nano Banana 2)| Input (text, image, video) [2]| Global| $0.90| $0.09  
| | Non-global| $0.99| $0.099  
| Text output (response and reasoning)| Global| $5.40| N/A  
| | Non-global| $5.94| N/A  
| Image Output [2]| Global| $108.00| N/A  
| | Non-global| $118.80| N/A  
Gemini 3 Pro Image (Nano Banana Pro)| Input (text, image)| Global| $3.60| $0.36  
| Text output (response and reasoning)| Global| $21.60| N/A  
| Image Output [1]| Global| $216.00| N/A  
  
[1] Gemini 3 Pro Image charges 560 tokens per input image, with approximate output image costs scaling by resolution: 1120 tokens ($0.134) for 1K and 2K (roughly 1MP and 4MP), and 2000 tokens ($0.24) for 4K (roughly 16MP).

[2] Gemini 3.1 Flash Image charges 1120 tokens per input image, with approximate output image costs scaling by resolution: 747 tokens ($0.045) for 512 (roughly 0.25MP), 1120 tokens ($0.067) for 1K (roughly 1MP), 1680 tokens ($0.101) for 2K (roughly 4MP), and 2,520 tokens ($0.15) for 4K (roughly 16MP).

[3] Gemini 3.1 Flash-Lite Image charges 1120 tokens per input image, and 1120 tokens ($0.034) for 1K (roughly 1MP) output images

[4] Gemini Nano Banana 2.1 charges 1120 tokens per input image, with approximate output image costs scaling by resolution: 1120 tokens ($0.034) for 1K (roughly 1MP), 1680 tokens ($0.05) for 2K (roughly 4MP), and 3780 tokens ($0.113) for 4K (roughly 16MP). Gemini Nano Banana 2.1 does not support Flex

Show discount options

Model| Type| Region| Price (/1M tokens) with Flex/Batch/Off-peak| Price (/1M tokens) cached input tokens with Flex/Batch/Off-peak  
---|---|---|---|---  
Gemini Nano Banana 2.1 [4]| Input (text, image, video) [4]| Global| $0.75| $0.075  
| Text output (response and reasoning)| Global| $3.75| N/A  
| Image Output [4]| Global| $15.00| N/A  
Gemini 3.1 Flash-Lite Image (Nano Banana 2 Lite)| Input (text, image, video) [3]| Global| $0.125| $0.0125  
| Text output (response and reasoning)| Global| $0.75| N/A  
| Image Output [3]| Global| $15.00| N/A  
Gemini 3.1 Flash Image (Nano Banana 2)| Input (text, image, video) [2]| Global| $0.25| $0.025  
| | Non-global| $0.275| $0.0275  
| Text output (response and reasoning)| Global  
| $1.50| N/A  
| | Non-global| $1.65| N/A  
| Image Output [2]| Global| $30.00| N/A  
| | Non-global| $33.00| N/A  
Gemini 3 Pro Image (Nano Banana Pro)| Input (text, image) [1]| Global| $1.00| $0.10  
| Text output (response and reasoning)| Global| $6.00| N/A  
| Image Output [1]| Global| $60.00| N/A  
  
[1] Gemini 3 Pro Image charges 560 tokens per input image, with approximate output image costs scaling by resolution: 1120 tokens ($0.134) for 1K and 2K (roughly 1MP and 4MP), and 2000 tokens ($0.24) for 4K (roughly 16MP).

[2] Gemini 3.1 Flash Image charges 1120 tokens per input image, with approximate output image costs scaling by resolution: 747 tokens ($0.045) for 512 (roughly 0.25MP), 1120 tokens ($0.067) for 1K (roughly 1MP), 1680 tokens ($0.101) for 2K (roughly 4MP), and 2,520 tokens ($0.15) for 4K (roughly 16MP).

[3] Gemini 3.1 Flash-Lite Image charges 1120 tokens per input image, and 1120 tokens ($0.034) for 1K (roughly 1MP) output images

[4] Gemini Nano Banana 2.1 charges 1120 tokens per input image, with approximate output image costs scaling by resolution: 1120 tokens ($0.034) for 1K (roughly 1MP), 1680 tokens ($0.05) for 2K (roughly 4MP), and 3780 tokens ($0.113) for 4K (roughly 16MP). Gemini Nano Banana 2.1 does not support Flex

**Pricing with grounding**

Show discount options

Feature| Usage| Price (USD)  
---|---|---  
Grounding with Google Search| Includes 5,000 Grounding Queries per month at no charge, aggregated across all Gemini 3 models.Grounding Queries exceeding those limits are billed at $14 per 1,000 Grounding Queries. Please contact your account team if you require more than 1 million Grounding Prompts per day.A “Grounding Prompt” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to a Google web index (each a “Grounding Query”) . You will be charged for each individual Grounding Query performed. Billing will start January 5, 2026.Input tokens provided by Grounding with Google Search or Web Grounding for Enterprise are not charged.Customers may decide not to display Search Suggestions with Grounded Results in their Customer Applications at standard pricing for under 1 million Grounding Prompts per day.| 0 count to 5,000 count$0.00 (Free) / 1,000 count, per 1 month / account5,000 count and above$14.00 / 1,000 count, per 1 month / account  
  
## 

Other Google models

All Gemini models other than Gemini 2.0 or Gemini 2.5 are billed based on modalities such as characters, images, video/audio seconds.

  * Text input is charged by every 1,000 characters of input (prompt) and every 1,000 characters of output (response).
  * Characters are counted by UTF-8 code points and white space is excluded from the count, resulting in approximately 4 characters per token.
  * Prediction requests that lead to filtered responses are charged for the input only.
  * At the end of each billing cycle, fractions of one cent ($0.01) are rounded to one cent. Media input is charged per image or per second (video).
  * If your request fails with a 400 or 500 error, you won't be charged for the tokens used.



### 

Gemini 3.8 Flash TTS and Gemini 3.8 Flash-Lite TTS

Show discount options

Model| Feature| Description| Type| Price (USD)  
---|---|---|---|---  
Gemini 3.8 Flash TTS (Preview)*Through December 31, 2026| Expressive speech generation| Studio-quality single- and multi-speaker speech with line-by-line style direction, for media and creative workloads. Unary and streaming synthesis. Voice design and voice replication capabilities.| Text Input| $0.50 / 1,000,000 count  
| | | Audio Output| $9.00 / 1,000,000 count  
Gemini 3.8 Flash TTS (Preview)Starting January 1, 2027| | | Text Input| $1.00 / 1,000,000 count  
| | | Audio Output| $18.00 / 1,000,000 count  
Gemini 3.8 Flash-Lite TTS (Preview)* Through December 31, 2026| Low-latency speech generation| Controllable single- and multi-speaker speech for real-time and high-volume workloads. Unary and streaming synthesis, along with voice replication capability.| Text Input| $0.50 / 1,000,000 count  
| | | Audio Output| $6.00 / 1,000,000 count  
Gemini 3.8 Flash-Lite TTS (Preview) Starting January 1, 2027| | | Text Input| $1.00 / 1,000,000 count  
| | | Audio Output| $12.00 / 1,000,000 count  
  
***** Promotional pricing provided through 50% credits back on net spend on the same model within a given period.

### 

Gemini 3.5 Live Translate

Show discount options

Model| Feature| Description| Type| Price (USD)  
---|---|---|---|---  
Gemini 3.5 Live Translate| Real-time speech to speech translation| Low-latency, real-time speech to speech translation model that supports 70+ languages.| Audio Input| $3.50 / 1,000,000 count  
| | | Audio Output| $21.00 / 1,000,000 count  
  
* Billing is based on total input and output audio token consumption, calculated at a rate of 25 tokens per second of audio.

### 

Gemini 3.5 Transcribe

Show discount options

Model| Feature| Description| Type| Price (USD)  
---|---|---|---|---  
Gemini 3.5 Transcribe Live| Real-time streaming transcription| Sub-second latency streaming via Live API with automatic code-mixing. Only final committed tokens are billed.| Audio Input| $3.50 / 1,000,000 count  
| | | Text Output| $21.00 / 1,000,000 count  
| | | Effective Blended Price (audio-minute*)| $0.008925 / 1 count  
Gemini 3.5 Transcribe| Synchronous audio file processing| Batch and synchronous processing for files up to 60 minutes via GenerateContent API.| Audio Input| $2.00 / 1,000,000 count  
| | | Text Output| $12.00 / 1,000,000 count  
| | | Effective Blended Price (audio-minute*)| $0.0051 / 1 count  
  
*Estimated pricing is based on 25 audio tokens per second for audio input and 175 text tokens per minute of text output.

### 

Gemini 1.5

Show discount options

Model| Feature| Type| Price ( =< 128K input tokens)| Price ( > 128K input tokens)  
---|---|---|---|---  
Gemini 1.5 Flash| Multimodal| Image Input| $0.00002 / 1 count| $0.00004 / 1 count  
| | Video Input| $0.00002 / 1 count| $0.00004 / 1 count  
| | Text Input| $0.00001875 / 1,000 count| $0.0000375 / 1,000 count  
| | Audio Input| $0.000002 / 1 count| $0.000004 / 1 count  
| | Text Output| $0.000075 / 1,000 count| $0.00015 / 1,000 count  
| Tuning*| Training Token| $0.008 / 1,000 count|   
Gemini 1.5 Pro| Multimodal| Image Input| $0.00032875 / 1 count| $0.0006575 / 1 count  
| | Video Input| $0.00032875 / 1 count| $0.0006575 / 1 count  
| | Text Input| $0.0003125 / 1,000 count| $0.000625 / 1,000 count  
| | Audio Input| $0.00003125 / 1 count| $0.0000625 / 1 count  
| | Text Output| $0.00125 / 1,000 count| $0.0025 / 1,000 count  
| Tuning*| Training Token| $0.08 / 1,000 count|   
Gemini 1.0 Pro| Multimodal| Image Input| $0.0025 / 1 count  
| | Video Input| $0.002 / 1 count|   
| | Text Input| $0.000125 / 1,000 count  
| | Text Output| $0.000375 / 1,000 count|   
  
* Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

* If a query context is longer than 128K, all tokens are charged at long context rates.

* Gemini models are available in batch mode at 50% discount.

* Gemini 1.0 Pro only support up to 32K context window.

* PDFs are billed as image input, with one PDF page equivalent to one image.

* Tuned model endpoint has the same prediction price as the base model.

** Grounding with Google Search and Web Grounding for Enterprise is billed only when a prompt successfully returns sources (i.e., web results containing at least one support URL from the web). Gemini model usage fees apply separately.

Pricing with Grounding

Feature| Price (USD)  
---|---  
Grounding with Google Search| **$35 per 1,000 Grounding Prompts**.A “**Grounding Prompt** ” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to Google web index (each a “**Grounding Query** ”)**. Even if multiple Grounding Queries are sent, there is only one charge for a Grounding Prompt.  
Web Grounding for enterprise| **$45 per 1,000 Grounding Prompts**.A “**Grounding Prompt** ” is an End User prompt that Customer submits to Gemini for which Gemini makes one or more queries to Google web index (each a “**Grounding Query** ”)**. Even if multiple Grounding Queries are sent, there is only one charge for a Grounding Prompt.  
Grounding with your data| $2.5 per 1,000 requests starting June 16, 2025.  
  
** Grounding with Google Search and Web Grounding for Enterprise is billed only when a prompt successfully returns sources (i.e., web results containing at least one support URL from the web). Gemini model usage fees apply separately.

### 

Imagen

With Imagen on Agent Platform, you can generate novel images and edit images based on text prompts you provide, or edit only parts of images using a mask area you define along with a host of other capabilities.

Show discount options

Model| Feature| Description| Input| Output| Price / 1 count (USD)  
---|---|---|---|---|---  
Imagen 4 Ultra| Image generation| Generate an image| Text prompt| Image| $0.06  
Imagen 4| Upscaling| Increase resolution of a generated image to 2K, 3K, and 4K| Image| Image| $0.06  
Imagen 4| Image generation| Generate an image| Text prompt| Image| $0.04  
Imagen 4 Fast| Image generation| Generate an image| Text prompt| Image| $0.02  
Imagen 3| Image generation| Generate an imageEdit an imageCustomize an image| Text prompt| Image| $0.04  
Imagen 3 Fast| Image generation| Generate an image| Text prompt| Image| $0.02  
Imagen 2, Imagen 1| Image generation| Generate an image| Text prompt| Image| $0.02  
Imagen 2, Imagen 1| Image editing| Edit an image using mask free or mask approach| Image/Text prompt| Image| $0.02  
Imagen 1| Upscaling| Increase resolution of a generated image to 2k and 4k| Image| Image| $0.003  
Imagen 1| Fine-tuning| Enable a "subject" provided by the user to used in Imagen prompts (few shot training)| Subject(s) with text identifier and 4-8 images per subject| Fine-tuned model (after training with user provided subjects)| $ per node hour (Agent Platform custom training pricing)  
Imagen| Visual Captioning| Generate a short or long text caption for an image| Image| Text caption| $0.0015  
Imagen| Visual Q&A| Provide an answer based on a question referencing an image| Image/Text prompt| Text answer| $0.0015  
Imagen| Product Recontext| Re-imagine products in a new scene| 1-3 Images of the same product and a text prompt describing desired scene| Image| $0.12  
| Virtual Try-On| Create images of people wearing different clothes| 1 image of a person and 1 image of clothing| Image| $0.06  
  
Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Veo

Show discount options

Model| Feature| Description| Input| Output| Output Resolution| Price (USD)  
---|---|---|---|---|---|---  
Veo 3.1| Video + Audio generation| Generate high-quality videos with synchronized speech/sound effects from a text prompt or reference image| Text/Image prompt| Video + Audio| 720p, 1080p| $0.40 / 1 count  
| | | | | 4k| $0.60 / 1 count  
| Video generation| Generate high-quality videos from a text prompt or reference image| Text/Image prompt| Video| 720p, 1080p| $0.20 / 1 count  
| | | | | 4k| $0.40 / 1 count  
Veo 3.1 Fast| Video + Audio generation| Generate videos with synchronized speech/sound effects from a text prompt or reference image faster| Text/Image prompt| Video + Audio| 720p| $0.10 / 1 count  
| | | | | 1080p| $0.12 / 1 count  
| | | | | 4k| $0.30 / 1 count  
| Video generation| Generate videos from a text prompt or reference image faster| Text/Image prompt| Video| 720p| $0.08 / 1 count  
| | | | | 1080p| $0.10 / 1 count  
| | | | | 4k| $0.25 / 1 count  
Veo 3.1 Lite| Video + Audio generation| Generate videos with synchronized speech/sound effects from a text prompt or reference image the fastest| Text/Image prompt| Video + Audio| 720p| $0.05 / 1 count  
| | | | | 1080p| $0.08 / 1 count  
| Video generation| Generate videos from a text prompt or reference image the fastest| Text/Image prompt| Video| 720p| $0.03 / 1 count  
| | | | | 1080p| $0.05 / 1 count  
Veo 3| Video + Audio generation| Generate high-quality videos with synchronized speech/sound effects from a text prompt or reference image| Text/Image prompt| Video + Audio| 720p, 1080p| $0.40 / 1 count  
| Video generation| Generate high-quality videos from a text prompt or reference image| Text/Image prompt| Video| 720p, 1080p| $0.20 / 1 count  
Veo 3 Fast| Video + Audio generation| Generate videos with synchronized speech/sound effects from a text prompt or reference image faster| Text/Image prompt| Video + Audio| 720p| $0.10 / 1 count  
| | | | | 1080p| $0.12 / 1 count  
| Video generation| Generate videos from a text prompt or reference image faster| Text/Image prompt| Video| 720p| $0.08 / 1 count  
| | | | | 1080p| $0.10 / 1 count  
Veo 2| Video generation| Generate videos from a text prompt or reference image| Text/Image prompt| Video| 720p| $0.50 / 1 count  
| Advanced Controls| Generate videos through start and end frame interpolation, extend generated videos, and apply camera controls| Text/Image/Video prompt| Video| 720p| $0.50 / 1 count  
  
### 

Lyria

Lyria model family offers high-quality music generation that is ideal for sophisticated composition and detailed creative exploration where nuanced output is key.

Show discount options

Model| Feature| Description| Input| Output| Price (USD)  
---|---|---|---|---|---  
Lyria 3 Pro| Full song music generation| Lyria 3 Pro creates full-length musical compositions from multimodal inputs such as text or images| Text, Image| Full song| $0.08 / 1 count  
Lyria 3| 30 second music clip generation| Lyria 3 generates high-fidelity, 30-second audio clips from text or image prompts| Text, Image| 30 second music clip| $0.04 / 1 count  
Lyria 2| Music generation| Generate music from a text prompt| Text prompt| Music| $0.06 / 1 count  
  
### 

Embedding costs

The Gemini API offers embedding models to generate embeddings for text, images, video, and other content. 

Show discount options

Model| Type| Region| Request Type| Price / 1,000 count (USD)  
---|---|---|---|---  
Gemini Embedding| Input| Global| Online requests| $0.00015  
| | | Batch requests| $0.00012  
| Output| Global| Online requests| No charge  
| | | Batch requests| No charge  
Embeddings for Text (Excluding Gemini Embedding)| Input| Global| Online requests| $0.000025  
| | | Batch requests| $0.00002  
| Output| Global| Online requests| No charge  
| | | Batch requests| No charge  
  
## 

Gemini Omni

Model| Type| Token Price /1M (USD)  
---|---|---  
Gemini Omni Flash, Gemini Omni 1.1 Flash| Input (text, image, video, audio)*| $1.50  
| Text output (response and reasoning)| $9.00  
| Video Output**| $17.50  
  
* Gemini Omni Flash charges 1120 tokens per image, 32 tokens per audio second, and 5792 tokens per video second for inputs. 

** Gemini Omni Flash charges 1931 tokens per second of 360p video, 5792 tokens per second of 720p video, 8688 tokens per second of 1080p video, and 17376 tokens per second of 4k video for video outputs (with audio).

## 

Agents

StandardDeferred

Model| Type| Price (/1M tokens)| Price (/M chached input tokens)  
---|---|---|---  
Gemini Deep Research Agent| Input (text)| $2| $0.2  
| Text output (response and reasoning)| $12| N/A  
  
Model| Type| Price (/1M tokens)| Price (/M chached input tokens)  
---|---|---|---  
Gemini Deep Research Agent| Input (text)| $1| $0.1  
| Text output (response and reasoning)| $6| N/A  
  
**Pricing with grounding**

Show discount options

Feature| Usage| Price (_USD)_  
---|---|---  
Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise*| Includes 5,000 search queries per month at no charge, aggregated across all Gemini 3 models.Search queries exceeding those limits are billed at $14 per 1,000 search queries. A customer-submitted request to Gemini may result in one or more queries to Google Search (or Web Grounding for Enterprise). You will be charged for each individual search query performed. Billing will start January 5, 2026.Input tokens provided by Grounding with Google Search or Web Grounding for Enterprise are not charged.Please contact your account team if you require more than 1 million grounded prompts per day.Customers may decide not to display Search Suggestions with Grounded Results in their Customer Application interface at standard pricing.| 0 count to 5,000 count$0.00 (Free)5,000 count and above$14.00  
| | $2.50  
  
## 

CodeMender

The pricing for CodeMender is based on tokens and is determined by the model used.

Show discount options

Model| Type| Model Price /1M tokens (USD)| CodeMender Price /1M tokens (USD)  
---|---|---|---  
Gemini 4 Argon*Gemini 4 Argon Cyber Permissive | Input tokens| $4.00| $4.00  
| Cached tokens| $0.20| $0.20  
| Output tokens| $20.00| $20.00  
Gemini 3.8 Flash Cyber| Input tokens| $1.50| $1.50  
| Cache tokens| $1.50| $1.50  
| Output tokens| $7.50| $7.50  
Gemini 3.8 Flash *| Input tokens| $1.50| $1.50  
| Cached tokens| $0.15| $0.15  
| Output tokens| $7.50| $7.50  
Gemini 3.7 Flash *| Input tokens| $1.50| $1.50  
| Cached tokens| $0.15| $0.15  
| Output tokens| $7.50| $7.50  
Gemini 3.6 Flash *| Input tokens| $1.50| $1.50  
| Cached tokens| $0.15| $0.15  
| Output tokens| $7.50| $7.50  
Gemini 3.5 Flash| Input tokens| $1.50| $1.50  
| Cached tokens| $0.15| $0.15  
| Output tokens| $9.00| $9.00  
Gemini 3.1 Pro| Input tokens| $2.00| $2.00  
| Cached tokens| $0.20| $0.20  
| Output tokens| $12.00| $12.00  
  
* Promotional pricing provided through 50% credits back on net spend on select models within a given period (promotion period for CodeMender using these models is same as the promotion period on select models)

## 

AlphaEvolve

The cost of AlphaEvolve is determined by the cost of the Gemini model used plus the cost of the AlphaEvolve agent.

Show discount options

Gemini model| Type| Gemini model price /1M (USD)| AlphaEvolve agent price /1M (USD)  
---|---|---|---  
Gemini 3.1 Pro Preview| Price per 1M input tokens| $2.00| $4.00  
| Price per 1M output and thinking tokens| $12.00| $24.00  
Gemini 3.5 Flash| Price per 1M input tokens| $1.50| $3.00  
| Price per 1M output and thinking tokens| $9.00| $18.00  
Gemini 3.7 Flash, Gemini 3.8 Flash| Price per 1M input tokens| $1.50| $3.00  
| Price per 1M output and thinking tokens| $7.50| $15.00  
Gemini 4 Argon| Price per 1M input tokens| $2.00| $8.00  
| Price per 1M output and thinking tokens| $10.00| $40.00  
  
## 

Gemma

Show discount options

Model| Type| Price (/1M tokens (USD)  
---|---|---  
Gemma 4 26B| Input| $0.15  
| Output| $0.60  
| Cache Hit| $0.015  
  
## 

MultiModal Embeddings

Show discount options

Model| Type| Description| Request Type| Price /1M tokens (USD)  
---|---|---|---|---  
Gemini Embedding 2 (Unified Multimodal, Preview)| Input text| Generate embeddings using text as input| Online requests| $0.20  
| | | Batch requests| $0.10  
| Input image| Generate embeddings using image as input| Online requests| $0.45  
| | | Batch requests| $0.225  
| Input video| Generate embeddings using video as input| Online requests| $12.00  
| | | Batch requests| $6.00  
| Input audio| Generate embeddings using audio as input| Online requests| $6.50  
| | | Batch requests| $3.25  
  
*No charges for output tokens.

Show discount options

Model| Feature| Description| Input| Output| Price (USD)  
---|---|---|---|---|---  
multimodalembedding| Embeddings for Multimodal: Text| Generate embeddings using text as an input| Text| Embeddings| $0.0002 / 1,000 count  
| Embeddings for Multimodal: Image| Generate embeddings using image as an input| Image| Embeddings| $0.0001 / 1 count  
| Embeddings for Multimodal: Video Plus| Video Plus| Video| Embeddings (up to 15 embeddings per min of video)| $0.002 / 1 count  
| Embeddings for Multimodal: Video Standard| Video Standard| Video| Embeddings (up to 8 embeddings per min of video)| $0.001 / 1 count  
| Embeddings for Multimodal: Video Essential| Video Essential| Video| Embeddings (up to 4 embeddings per min of video)| $0.0005 / 1 count  
  
Show discount options

Open Source Model| Type| Request Type| Price /1M tokens (USD)  
---|---|---|---  
multilingual-e5-small| Input| Online requests| $0.015  
| Output| Online requests| No charge  
| Batch Input| Batch requests| $0.0075  
| Batch Output| Batch requests| No charge  
multilingual-e5-large| Input| Online requests| $0.025  
| Output| Online requests| No charge  
| Batch Input| Batch requests| $0.0125  
| Batch Output| Batch requests| No charge  
  
Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

# 

Pricing for Agent Platform's code completion

Generative AI on Agent Platform charges by every 1,000 characters of input (prompt) and every 1,000 characters of output (response). Characters are counted by UTF-8 code points and white space is excluded from the count. During the Preview stage, charges are 100% discounted. Prediction requests that lead to filtered responses are charged for the input only. At the end of each billing cycle, fractions of one cent ($0.01) are rounded to one cent.

**Note:** Prediction pricing for tuned model endpoints are the same as for the base foundation model.

Show discount options

Model| Type| Region| Request Type| Price /1k tokens (USD)  
---|---|---|---|---  
Codey for Code Completion| Input| Global| Online requests| $0.00025  
| Output| Global| Online requests| $0.0005  
  
Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## 

Translation (Text)

Use the Agent Platform API and Translation LLM to translate text. LLM translations tend to be more fluent and human sounding than classic translation models, but have more limited language support [(Learn More)](https://cloud.google.com/vertex-ai/generative-ai/docs/translate/translate-text).

Show discount options

Model| Method| Usage| Price Price /1M token (USD)  
---|---|---|---  
LLM| [Text translation](https://cloud.google.com/vertex-ai/generative-ai/docs/translate/translate-text)*| The number of input characters per month| $10.00  
| | The number of output characters per month| $10.00  
Translation LLM 002| [Text translation](https://cloud.google.com/vertex-ai/generative-ai/docs/models/translation-use-supervised-tuning)*| The number of input characters per month| $20.00  
| | The number of output characters per month| $20.00  
  
Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

*Price is per character processed by the model. For details about counted characters, see _[Charged characters](https://cloud.google.com/translate/pricing#charged-characters)_

## 

Context Cache Storage price for Explicit Caching

This table contains the pricing for Context Cache Storage based on Input (text, image, video, audio)

Show discount options

HourlyHourly

MonthlyMonthly

Model| Price Tok/hr<= 200K input tokens| Price Tok/hr > 200K input tokens  
---|---|---  
Gemini 3.1 Pro| $0.0000045| $0.0000045  
Gemini 3.8 Flash Cyber, Gemini 3.8 Flash, Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash, Gemini 3 Flash| $0.000001| $0.000001  
Gemini 3.5 Flash Lite, Gemini 3.1 Flash Lite| $0.000001| $0.000001  
Gemini 3 Pro| $0.0000045| $0.0000045  
Gemini 2.5 Pro| $0.0000045| $0.0000045  
Gemini 2.5 Flash| $0.000001| $0.000001  
Gemini 2.5 Flash Lite| $0.000001| $0.000001  
  
Gemini 2.0 Models

Token-based pricingModality-based pricing

Show discount options

HourlyHourly

MonthlyMonthly

Model| Type| Storage (M tok-hour)| Price /1 (USD)  
---|---|---|---  
Gemini 2.0 Flash| Input tokens| $0.000001| $0.0375  
| Input audio tokens| $0.000001| $0.25  
| Output text tokens| NA| NA  
Gemini 2.0 Flash Lite| Input tokens| $0.000001| $0.01875  
| Input audio tokens| $0.000001| $0.01875  
| Output text tokens| NA| NA  
  
* Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

* PDFs are billed as image input, with one PDF page equivalent to one image.

* Tuned model endpoint has the same prediction price as the base model.

The below modality pricing is based on average use cases for reference only. Actual billing will only be based on tokens:

  * 4 characters result in approximately 1 text token including white space.
  * For an 1024x1024 image, it consumes 1290 tokens. Per image token count varies by image resolution. For more information on how to calculate tokens, you can refer to our [documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding#image-requirements).
  * Video input consumes 258 tokens per second at the sample rate of one frame per second. Video with audio bills for both video tokens and audio tokens.
  * Audio input consumes 25 tokens per second without timestamp.



Model| Type| Storage (Modality-hour)| Price (USD)  
---|---|---|---  
Gemini 2.0 Flash| Input text ($/M char)| $0.25| $0.009375  
| Input image ($/image)| $0.00129| $0.000048375  
| Input video ($/sec)| $0.000258| $0.000009675  
| Input audio ($/sec)| $0.000025| $0.00000625  
| Output text ($/M char)| NA| NA  
Gemini 2.0 Flash Lite| Input text ($/M char)| $0.25| $0.0046875  
| Input image ($/image)| $0.00129|   
| Input video ($/sec)| $0.000258| $0.000009675  
| Input audio ($/sec)| $0.000258| $0.0000048375  
| Output text ($/M char)| NA| NA  
  
* Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

* PDFs are billed as image input, with one PDF page equivalent to one image.

* Tuned model endpoint has the same prediction price as the base model.

Pricing with grounding

Feature| Price (USD)  
---|---  
Grounding with Google Search*| Gemini 2.0 Flash includes up to 1,500 grounded requests per day at no additional charge. Grounded requests exceeding 1,500 per day are billed at $35 per 1,000 requests (up to 1 million requests per day).Please contact your account team if you require more than 1 million requests per day.Customers may decide not to display Search Suggestions with Grounded Results in their Customer Application interface; however, this is subject to alternate pricing. Please contact your Google Cloud Account team to request this waiver.  
Web Grounding for enterprise*| $45 per 1,000 request (up to 1 million requests per day) starting May 5, 2025.Please contact your account team if you require more than 1 million requests per day.Customers may decide not to display Search Suggestions with Grounded Results in their Customer Application interface; however, this is subject to alternate pricing. Please contact your Google Cloud Account team to request this waiver.  
  
* This apply to modality-based pricing.

**Note:** Grounding with Google Search is billed only for requests that return results containing at least one grounding support URL from the web. Standard Gemini model usage fees also apply.

## 

Provisioned Throughput

[ _Provisioned throughput_](https://cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput) assures throughput for your generative AI needs and is transacted via [_generative AI scale units_](https://cloud.google.com/vertex-ai/generative-ai/docs/measure-provisioned-throughput#gsu-burndown-rate), or GSUs. Learn more about how much throughput each GSU provides [_here_](https://cloud.google.com/vertex-ai/generative-ai/docs/supported-models) and use our online estimator [_here_](https://console.cloud.google.com/vertex-ai/provisioned-throughput/price-estimate;publisherModelName=;queriesPerSecond=;inputCharsPerQuery=;inputImagesPerQuery=;inputVideoSecondsPerQuery=;inputAudioSecondsPerQuery=;outputCharsPerQuery=;outputImagesPerQuery=0;tierDistribution=100,0?project=cloud-ai-frontend&e=13802955&inv=1&invt=Abo4mg&mods=allow_workbench_image_override).

Show discount options

HourlyHourly

MonthlyMonthly

Duration| Global price per GSU (USD)| Non-Global*price per GSU (USD)  
---|---|---  
1 week commit| $7.14| $7.854  
1 month commit| $3.698630137| $4.068493151  
3 month commit| $3.287671233| $3.616438356  
1 year commit| $2.739726027| $3.01369863  
  
* For non-global endpoints, pricing will go into effect for the Generally available Gemini 3 and later families of all Google models starting on July 1, 2026. Before July 1, 2026, Global endpoint pricing applies to Non-global endpoints.

### 

Example cost calculation

A user needs to ensure they can support 10 queries per second (QPS) of a query with input of 1,000 text tokens and 500 audio tokens and receive an output of 300 text tokens using gemini-2.0-flash.

Using the throughput and burndown rate _[table](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/supported-models.md)_ , for gemini-2.0-flash we know an input text token's burndown rate is 1 token, an input audio token's burndown rate is 7 tokens, and an output text token's burndown rate is 4 tokens.

The user's total input tokens is 1,000* (1 token per input text token) + 500* (7 tokens per input audio token) = 4,500 burndown adjusted input tokens. The user's total output tokens is 300* (4 tokens per output text token) = 1,200 burndown adjusted output tokens. Adding them together gives us 4,500 burndown adjusted input tokens + 1,200 burndown adjusted output tokens = 5,700 total tokens per query.

Multiplying the total tokens per query by QPS gives us 5,700 total tokens per query * 10 QPS = 57,000 total tokens per second.

Dividing this by the total throughput per second per GSU gives us 57,000 total tokens per second ÷ 3,360 per-second throughput per GSU = 16.96 GSUs. The minimum GSU purchase increment for this model is 1, so the user would need 17 GSUs.

If the user wanted to sustain this throughput for 1 week, it would cost $1,200 * 17 GSUs = $20,400 per week. If they wanted to sustain this throughput for 1 month, it would cost $2,700 * 17 GSUs = $45,900 per month. If they wanted to sustain this throughput for 3 months, it would cost $2,400 * 17 GSUs = $40,800 per month. And finally, if they wanted to sustain this throughput for 1 year, it would cost $2,000 * 17 GSUs = $34,000 per month.

### 

50% Promotional Credits on Gemini 3.8 Flash, Gemini 3.7 Flash and Gemini 3.6 Flash Provisioned Throughput Usage

Effective August 13, 2026 through December 31, 2026, Google Cloud is injecting a monthly billing credit equal to 50% of net eligible Provisioned Throughput spending on Gemini 3.8 Flash, Gemini 3.7 Flash, and Gemini 3.6 Flash models.

This credit will automatically be reflected in monthly invoices and will not alter Provisioned Throughput configurations or commitment burndown rates.

Issued credits apply to usage across On-Demand Gemini 3.8 Flash, Gemini 3.7 Flash and Gemini 3.6 Flash SKUs, as well as Provisioned Throughput SKUs across all models. Credits are issued on the 7th day of each month following the billing period, and expire 30 days after issuance, under standard [Google Cloud Credit Terms of Service](https://cloud.google.com/terms/open-source-software-tos)**.** Spend for the initial month is pro-rated strictly for active usage between August 13 and August 31, 2026.

## 

Model Tuning

Model tuning is an effective way to customize large models to your tasks. It's a key step to improve the model's quality and efficiency. Model tuning provides the following benefits:

  * Higher quality for your specific tasks
  * Increased model robustness
  * Lower inference latency and cost due to shorter prompts



Training tokens are calculated by the total number of tokens in your training dataset, multiplied by your number of epochs.

Show discount options

Model| Type| Price (USD)  
---|---|---  
Gemini 3.5 Flash Lite| Supervised fine-tuning| $0.003 / 1,000 count  
Gemini 3.5 Flash| Supervised fine-tuningReinforcement Learning fine-tuning| $0.01 / 1,000 count  
Gemini 3.1 Flash Lite| Supervised fine-tuning| $0.003 / 1,000 count  
Gemini 2.5 Pro| Supervised fine-tuning| $0.025 / 1,000 count  
Gemini 2.5 Flash| Supervised fine-tuningPreference tuning| $0.005 / 1,000 count  
Gemini 2.5 Flash Lite| Supervised fine-tuningPreference tuning| $0.0015 / 1,000 count  
Gemma 3 1B IT| Supervised fine-tuning| $0.47 / 1,000,000 count  
Gemma 3 4B IT| Supervised fine-tuning| $1.14 / 1,000,000 count  
Gemma 3 12B IT| Supervised fine-tuning| $1.82 / 1,000,000 count  
Gemma 3 27B IT| Supervised fine-tuning| $6.83 / 1,000,000 count  
Medgemma 1.5 4B IT| Supervised fine-tuning| $1.14 / 1,000,000 count  
Llama 3.1 8B| Supervised fine-tuning| $0.67 / 1,000,000 count  
Llama 3.2 1B| Supervised fine-tuning| $0.28 / 1,000,000 count  
Llama 3.2 3B| Supervised fine-tuning| $0.61 / 1,000,000 count  
Llama 3.3 70B| Supervised fine-tuning| $6.72 / 1,000,000 count  
Llama 4 Scout 17B 16E| Supervised fine-tuning| $5.77 / 1,000,000 count  
Qwen 3 4B| Supervised fine-tuning| $1.35 / 1,000,000 count  
Qwen 3 8B| Supervised fine-tuning| $4.18 / 1,000,000 count  
Qwen 3 14B| Supervised fine-tuning| $8.46 / 1,000,000 count  
Qwen 3 32B| Supervised fine-tuning| $6.57 / 1,000,000 count  
  
* For model inference starting from Gemini 3, tuned model endpoint prediction price will be 1.5 times of the base model. Old Gemini models prediction price stays the same as the base model.

Special Case of Charging by Characters

Show discount options

Model| Type| Price /1M (USD)  
---|---|---  
Translation LLM 002| Supervised fine-tuning| $6.25  
  
## 

Partner models on Agent Platform

Partner models are a curated list of generative AI models developed by Google partners. Partner models are offered as managed APIs. For more information, see [Overview of partner models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models). The following sections list pricing details for Google partner models.

## 

Anthropic’s Claude models

**Models with regional pricing**

GlobalUS Multi-Region (US)EU Multi-Region (EU)us-east5europe-west 1asia-southeast1asia-east1

Model| Type| Price (/1M tokens) =< 200K input tokens *| Price (/1M tokens) > 200K input tokens *| Price (/1M tokens) =< 100K input tokens **| Price (/1M tokens) > 100K input tokens **  
---|---|---|---|---|---  
Claude Haiku 5.5| Input| | | $0.10| $0.50  
| Output| | | $0.50| $2.50  
| Batch Input| | | $0.05|   
| Batch Output| | | $0.25|   
| 5m Cache Write| | | $0.125| $0.625  
| 1h Cache Write| | | $0.20| $1.00  
| Cache Hit| | | $0.01| $0.05  
| 5m Batch Cache Write| | | $0.0625|   
| 1h Batch Cache Write| | | $0.10|   
| Batch Cache Hit| | | $0.005|   
Sonnet 5.5| Input| $2.00| $2.00| |   
| Output| $10.00| $10.00| |   
| Batch Input| $1.00| | |   
| Batch Output| $5.00| | |   
| 5m Cache Write| $2.50| $2.50| |   
| 1h Cache Write| $4.00| $4.00| |   
| Cache Hit| $0.10| $0.10| |   
| 5m Batch Cache Write| $1.25| | |   
| 1h Batch Cache Write| $2.00| | |   
| Batch Cache Hit| $0.05| | |   
Opus 5.5| Input| $4.00| | |   
| Output| $20.00| $20.00| |   
| Batch Input| $2.50| | |   
| Batch Output| $12.50| | |   
| 5m Cache Write| $5.00| $5.00| |   
| 1h Cache Write| $8.00| $8.00| |   
| Cache Hit| $0.20| $0.20| |   
| 5m Batch Cache Write| $2.50| | |   
| 1h Batch Cache Write| $4.00| | |   
| Batch Cache Hit| $0.10| | |   
Opus 5| Input| $5.00| $5.00| |   
| Output| $25.00| $25.00| |   
| Batch Input| $2.50| | |   
| Batch Output| $12.50| | |   
| 5m Cache Write| $6.25| $6.25| |   
| 1h Cache Write| $10.00| $10.00| |   
| 1h Cache Write| $10.00| $10.00| |   
| Cache Hit| $0.50| $0.50| |   
| 5m Batch Cache Write| $3.125| | |   
| 1h Batch Cache Write| $5.00| | |   
| Batch Cache Hit| $0.25| | |   
Claude Sonnet 5| Input| $2.00| $2.00| |   
| Output| $10.00| $10.00| |   
| Batch Input| $1.00| $1.00| |   
| Batch Output| $5.00| $5.00| |   
| 5m Cache Write| $2.50| $2.50| |   
| 1h Cache Write| $4.00| $4.00| |   
| Cache Hit| $0.20| $0.20| |   
Claude Fable 5.1| Input| $10.00| $10.00| |   
| Output| $50.00| $50.00| |   
| Batch Input| $5.00| | |   
| Batch Output| $25.00| | |   
| 5m Cache Write| $12.50| $12.50| |   
| 1h Cache Write| $20.00| $20.00| |   
| Cache Hit| $0.25| $0.25| |   
| 5m Batch Cache Write| $6.25| | |   
| 1h Batch Cache Write| $10.00| | |   
| Batch Cache Hit| $0.125| | |   
Claude Fable 5| Input| $10.00| $10.00| |   
| Output| $50.00| $50.00| |   
| Batch Input| $5.00| | |   
| Batch Output| $25.00| | |   
| 5m Cache Write| $12.50| $12.50| |   
| 1h Cache Write| $20.00| $20.00| |   
| Cache Hit| $1.00| $1.00| |   
| 5m Batch Cache Write| $6.25| | |   
| 1h Batch Cache Write| $10.00| | |   
| Batch Cache Hit| $0.50| | |   
Claude Opus 4.8| Input| $5.00| $5.00| |   
| Output| $25.00| $25.00| |   
| Batch Input| $2.50| | |   
| 1h Cache Write| $10.00| | |   
| Batch Output| $12.50| | |   
| 5m Cache Write| $6.25| $6.25| |   
| 1h Cache Write| $10.00| $10.00| |   
| Cache Hit| $0.50| $0.50| |   
| 5m Batch Cache Write| $3.125| | |   
| 1h Batch Cache Write| $5.00| | |   
| Batch Cache Hit| $0.25| | |   
Claude Opus 4.7| Input| $5.00| $5.00| |   
| Output| $25.00| $25.00| |   
| Batch Input| $2.50| | |   
| Batch Output| $12.50| | |   
| 5m Cache Write| $6.25| $6.25| |   
| 1h Cache Write| $10.00| $10.00| |   
| Cache Hit| $0.50| $0.50| |   
| 5m Batch Cache Write| $3.125| | |   
| 1h Batch Cache Write| $5.00| $5.00| |   
| Batch Cache Hit| $0.25| | |   
Claude Opus 4.6| Input| $5.00| $5.00| |   
| Output| $25.00| $25.00| |   
| Batch Input| $2.50| | |   
| Batch Output| $12.50| | |   
| 5m Cache Write| $6.25| $6.25| |   
| 1h Cache Write| $10.00| $10.00| |   
| Cache Hit| $0.50| $0.50| |   
| 5m Batch Cache Write| $3.125| | |   
| 1h Batch Cache Write| $5.00| | |   
| Batch Cache Hit| $0.25| | |   
Claude Opus 4.5| Input| $5.00| | |   
| Output| $25.00| | |   
| Batch Input| $2.50| | |   
| Batch Output| $12.50| | |   
| 5m Cache Write| $6.25| | |   
| Cache Hit| $0.50| | |   
| 5m Batch Cache Write| $3.125| | |   
| 1h Batch Cache Write| $5.00| | |   
| Batch Cache Hit| $0.25| | |   
Claude Sonnet 4.6| Input| $3.00| $3.00| |   
| Output| $15.00| $15.00| |   
| Batch Input| $1.50| | |   
| Batch Output| $7.50| | |   
| 5m Cache Write| $3.75| $3.75| |   
| 1h Cache Write| $6.00| $6.00| |   
| Cache Hit| $0.30| $0.30| |   
| 5m Batch Cache Write| $1.88| | |   
| 1h Batch Cache Write| $3.00| | |   
| Batch Cache Hit| $0.15| | |   
Claude Sonnet 4.5| Input| $3.00| $6.00| |   
| Output| $15.00| $22.50| |   
| Batch Input| $1.50| | |   
| Batch Output| $7.50| | |   
| 5m Cache Write| $3.75| $7.50| |   
| 1h Cache Write| $6.00| $12.00| |   
| Cache Hit| $0.30| $0.60| |   
| 5m Batch Cache Write| $1.88| | |   
| 1h Batch Cache Write| $3.00| | |   
| Batch Cache Hit| $0.15| | |   
| 5m Batch Cache Write| $1.00| | |   
Claude Haiku 4.5| Input| $1.00| | |   
| Output| $5.00| | |   
| Batch Input| $0.50| | |   
| Batch Output| $2.50| | |   
| 5m Cache Write| $1.25| | |   
| Batch Cache Hit| $0.05| | |   
| 1h Cache Write| $2.00| | |   
| Cache Hit| $0.10| | |   
| 5m Batch Cache Write| $0.625| | |   
  
* If a query input context is longer than or equal to 200K tokens, all tokens (input and output) are charged at long context rates.

** If a query input context is longer than or equal to 100k tokens, all tokens (input and output) are charged at long context rates.

Model| Type| Price (/1M tokens) =< 200K input tokens *| Price (/1M tokens) > 200K input tokens *| Price (/1M tokens) =< 100K input tokens **| Price (/1M tokens) > 100K input tokens **  
---|---|---|---|---|---  
Claude Haiku 5.5| Input| | | $0.11| $0.55  
| Output| | | $0.55| $2.75  
| Batch Input| | | $0.055|   
| Batch Output| | | $0.275|   
| 5m Cache Write| | | $0.1375| $0.6875  
| 1hr Cache Write  
| | | $0.22| $1.10  
| Cache Hit| | | $0.011| $0.055  
| 5m Batch Cache Write| | | $0.06875|   
| 1h Batch Cache Write| | | $0.11|   
| Batch Cache Hit| | | $0.0055|   
Sonnet 5.5| Input| $2.20| $2.20| |   
| Output| $11.00| $11.00| |   
| Batch Input| $1.10| | |   
| Batch Output| $5.50| | |   
| 5m Cache Write| $2.75| $2.75| |   
| 1h Cache Write| $4.40| $4.40| |   
| Cache Hit| $0.11| $0.11| |   
| 5m Batch Cache Write| $1.375| | |   
| 1h Batch Cache Write| $2.20| | |   
| Batch Cache Hit| $0.055| | |   
Opus 5.5| Input| $4.40| $4.40| |   
| Output| $22.00| $22.00| |   
| Batch Input| $2.20| | |   
| Batch Output| $11.00| | |   
| 5m Cache Write| $5.50| | |   
| 1h Cache Write| $8.80| | |   
| Cache Hit| $0.22| | |   
| 5m Batch Cache Write| $2.75| $2.75| |   
| 1h Batch Cache Write| $4.40| $4.40| |   
| Batch Cache Hit| $0.11| $0.11| |   
Opus 5| Input| $5.50| $5.50| |   
| Output| $27.50| $27.50| |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| $6.875| |   
| 1h Cache Write| $11.00| $11.00| |   
| Cache Hit| $0.55| $0.55| |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
Claude Sonnet 5| Input| $2.20| $2.20| |   
| Output| $11.00| $11.00| |   
| Batch Input| $1.10| $1.10| |   
| Batch Output| $5.50| $5.50| |   
| 5m Cache Write| $2.75| $2.75| |   
| 1h Cache Write| $4.40| $4.40| |   
| Cache Hit| $0.22| $0.22| |   
Claude Fable 5.1| Input| $11.00| $11.00| |   
| Output| $55.00| $55.00| |   
| Batch Input| $5.50| | |   
| Batch Output| $27.50| | |   
| 5m Cache Write| $13.75| $13.75| |   
| 1h Cache Write| $22.00| $22.00| |   
| Cache Hit| $0.275| $0.275| |   
| 5m Batch Cache Write| $6.875| | |   
| 1h Batch Cache Write| $11.00| | |   
| Batch Cache Hit| $0.1375| | |   
Claude Fable 5| Input|  $11.00|  $11.00| |   
| Input|  $11.00|  $11.00| |   
| Batch Input| $5.50| | |   
| Batch Output| $27.50| | |   
| 5m Cache Write| $13.75| $13.75| |   
| 1h Cache Write| $22.00| $22.00| |   
| Cache Hit| $1.10| $1.10| |   
| 5m Batch Cache Write| $6.875| | |   
| 1h Batch Cache Write| $11.00| | |   
| Batch Cache Hit| $0.55| | |   
Claude Opus 4.8| Input| $5.50| $5.50| |   
| Output| $27.50| $27.50| |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| $6.875| |   
| 1h Cache Write| $11.00| $11.00| |   
| Cache Hit| $0.55| $0.55| |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
Claude Opus 4.7| Input| $5.50| $5.50| |   
| Output| $27.50| $27.50| |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| $6.875| |   
| 1h Cache Write| $11.00| $11.00| |   
| Cache Hit| $0.55| $0.55| |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
  
* If a query input context is longer than or equal to 200K tokens, all tokens (input and output) are charged at long context rates.

** If a query input context is longer than or equal to 100k tokens, all tokens (input and output) are charged at long context rates.

Model| Type| Price (/1M tokens) =< 200K input tokens *| Price (/1M tokens) > 200K input tokens *| Price (/1M tokens) =< 100K input tokens **| Price (/1M tokens) > 100K input tokens **  
---|---|---|---|---|---  
Claude Haiku 5.5| Input| | | $0.11| $0.55  
| Output| | | $0.55| $2.75  
| Batch Input| | | $0.055|   
| Batch Output| | | $0.275|   
| 5m Cache Write| | | $0.1375| $0.6875  
| 1h Cache Write| | | $0.22| $1.10  
| Cache Hit| | | $0.011| $0.055  
| 5m Batch Cache Write| | | $0.06875|   
| 1h Batch Cache Write| | | $0.11|   
| Batch Cache Hit| | | $0.0055|   
Sonnet 5.5| Input| $2.20| $2.20| |   
| Output| $11.00| $11.00| |   
| Batch Input| $1.10| | |   
| Batch Output| $5.50| | |   
| 5m Cache Write| $2.75| $2.75| |   
| 1h Cache Write| $4.40| $4.40| |   
| Cache Hit| $0.11| $0.11| |   
| 5m Batch Cache Write| $1.375| | |   
| 1h Batch Cache Write| $2.20| | |   
| Batch Cache Hit| $0.055| | |   
Opus 5.5| Input| $4.40| $4.40| |   
| Output| $22.00| $22.00| |   
| Batch Input| $2.20| | |   
| Batch Output| $11.00| | |   
| 5m Cache Write| $5.50| | |   
| 1h Cache Write| $8.80| | |   
| Cache Hit| $0.22| | |   
| 5m Batch Cache Write| $2.75| $2.75| |   
| 1h Batch Cache Write| $4.40| $4.40| |   
| Batch Cache Hit| $0.11| $0.11| |   
Opus 5| Input| $5.50| $5.50| |   
| Output| $27.50| $27.50| |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| $6.875| |   
| 1h Cache Write| $11.00| $11.00| |   
| Cache Hit| $0.55| $0.55| |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
Claude Sonnet 5| Input| $2.20| $2.20| |   
| Output| $11.00| $11.00| |   
| Batch Input| $1.10| $1.10| |   
| Batch Output| $5.50| $5.50| |   
| 5m Cache Write| $2.75| $2.75| |   
| 1h Cache Write| $4.40| $4.40| |   
| Cache Hit| $0.22| $0.22| |   
Claude Fable 5.1| Input| $11.00| $11.00| |   
| Output| $55.00| $55.00| |   
| Batch Input| $5.50| | |   
| Batch Output| $27.50| | |   
| 5m Cache Write| $13.75| $13.75| |   
| Batch Cache Hit| $0.275| | |   
| 1h Cache Write| $22.00| $22.00| |   
| Cache Hit| $0.275| $0.275| |   
| 5m Batch Cache Write| $6.875| | |   
| 1h Batch Cache Write| $11.00| | |   
| Batch Cache Hit| $0.1375| | |   
Claude Fable 5| Input| $11.00| $11.00| |   
| Output| $55.00| $55.00| |   
| Batch Input| $5.50| | |   
| Batch Output| $27.50| | |   
| 5m Cache Write| $13.75| $13.75| |   
| 1h Cache Write| $22.00| $22.00| |   
| Cache Hit| $1.10| $1.10| |   
| 5m Batch Cache Write| $6.875| | |   
| 1h Batch Cache Write| $11.00| | |   
| Batch Cache Hit| $0.55| | |   
Claude Opus 4.8| Input| $5.50| $5.50| |   
| Output| $27.50| $27.50| |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| $6.875| |   
| 1h Cache Write| $11.00| $11.00| |   
| Cache Hit| $0.55| $0.55| |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
Claude Opus 4.7| Input| $5.50| $5.50| |   
| Output| $27.50| $27.50| |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| $6.875| |   
| 1h Cache Write| $11.00| $11.00| |   
| Cache Hit| $0.55| $0.55| |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
  
* If a query input context is longer than or equal to 200K tokens, all tokens (input and output) are charged at long context rates.

** If a query input context is longer than or equal to 100k tokens, all tokens (input and output) are charged at long context rates.

Model| Type| Price (/1M tokens) =< 200K input tokens| Price (/1M tokens) > 200K input tokens  
---|---|---|---  
Claude Opus 4.6| Input| $5.50| $5.50  
| Output| $27.50| $27.50  
| Batch Input| $2.75|   
| Batch Output| $13.75|   
| 5m Cache Write| $6.875| $6.875  
| 1h Cache Write| $11.00| $11.00  
| Cache Hit| $0.55| $0.55  
| 5m Batch Cache Write| $3.438|   
| 1h Batch Cache Write| $5.50|   
| Batch Cache Hit| $0.275|   
Claude Opus 4.5| Input| $5.50| $5.50  
| Output| $27.50| $27.50  
| Batch Input| $2.75|   
| Batch Output| $13.75|   
| 5m Cache Write| $6.875| $6.875  
| 1h Cache Write| $11.00| $11.00  
| Cache Hit| $0.55| $0.55  
| 5m Batch Cache Write| $3.438|   
| 1h Batch Cache Write| $5.50|   
| Batch Cache Hit| $0.275|   
Claude Sonnet 4.6| Input| $3.30| $3.30  
| Output| $16.50| $16.50  
| Batch Input| $1.65|   
| Batch Output| $8.25|   
| 5m Cache Write| $4.13| $4.13  
| 1h Cache Write| $6.60| $6.60  
| Cache Hit| $0.33| $0.33  
| 5m Batch Cache Write| $2.06|   
| 1h Batch Cache Write| $3.30|   
| Batch Cache Hit| $0.17|   
| Input| $6.60|   
| Output| $24.75|   
Claude Sonnet 4.5| Input| $3.30| $6.60  
| Output| $16.50| $24.75  
| Batch Input| $1.65|   
| Batch Output| $8.25|   
| 5m Cache Write| $4.13| $8.25  
| 1h Cache Write| $6.60| $13.20  
| Cache Hit| $0.33| $0.66  
| 5m Batch Cache Write| $2.06|   
| 1h Batch Cache Hit| $3.30|   
| Batch Cache Hit| $0.17|   
Claude Haiku 4.5| Input| $1.10|   
| Output| $5.50|   
| Batch Input| $0.55|   
| Batch Output| $2.75|   
| 5m Cache Write| $1.375|   
| 1h Cache Write| $2.20|   
| Cache Write| $1.375|   
| Cache Hit| $0.11|   
| 5m Batch Cache Write| $0.688|   
| 1h Batch Cache Write| $1.10|   
| Batch Cache Hit| $0.055|   
  
* If a query input context is longer than or equal to 200K tokens, all tokens (input and output) are charged at long context rates.

Model| Type| Price (/1M tokens) =< 200K input tokens *| Price (/1M tokens) > 200K input tokens *| Price (/1M tokens) =< 100K input tokens **| Price (/1M tokens) > 100K input tokens **  
---|---|---|---|---|---  
Claude Haiku 5.5| Inpur| | | $0.11| $0.55  
| Outpur| | | $0.55| $2.75  
| Batch Input| | | $0.055|   
| Batch Output| | | $0.275|   
| 5m Cache Write| | | $0.1375| $0.6875  
| 1h Cache Write| | | $0.22| $1.10  
| Cache Hit| | | $0.011| $0.055  
| 5m Batch Cache Write| | | $0.06875|   
| 1h Batch Cache Write| | | $0.11|   
| Batch Cache Hit| | | $0.0055|   
Claude Opus 4.6| Input| $5.50| $5.50| |   
| Output| $27.50| $27.50| |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| $6.875| |   
| 1h Cache Write| $11.00| $11.00| |   
| Cache Hit| $0.55| $0.55| |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
Claude Opus 4.5| Input| $5.50| | |   
| Output| $27.50| | |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| | |   
| 1h Cache Write| $11.00| | |   
| Batch Cache Hit| $0.055| | |   
| Cache Hit| $0.55| | |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
Claude Sonnet 4.6| Input| $3.30| $3.30| |   
| Output| $16.50| $16.50| |   
| Batch Input| $1.65| | |   
| Batch Output| $8.25| | |   
| 5m Batch Write| $4.13| $4.13| |   
| 1h Cache Write| $6.60| $6.60| |   
| Cache Hit| $0.33| $0.33| |   
| 5m Batch Cache Hit| $2.06| | |   
| 1h Batch Cache Write| $3.30| | |   
| Batch Cache Hit| $0.17| | |   
Claude Sonnet 4.5| Input| $3.30| $6.60| |   
| Output| $16.50| $24.75| |   
| Batch Input| $1.65| | |   
| Batch Output| $8.25| | |   
| 5m Cache Write| $4.13| $8.25| |   
| 1h Cache Write| $6.60| $13.20| |   
| Cache Hit| $0.33| $0.66| |   
| 5m Batch Cache Write| $2.06| | |   
| 1h Batch Cache Write| $3.30| | |   
| Batch Cache Hit| $0.17| | |   
Claude Haiku 4.5| Input| $1.10| | |   
| Output| $5.50| | |   
| Batch Input| $0.55| | |   
| Batch Output| $2.75| | |   
| 5m Cache Write| $1.375| | |   
| 1h Cache Write| $2.20| | |   
| Cache Hit| $0.11| | |   
| 5m Batch Cache Write| $0.688| | |   
| 1h Batch Cache Write| $1.10| | |   
  
* If a query input context is longer than or equal to 200K tokens, all tokens (input and output) are charged at long context rates.

** If a query input context is longer than or equal to 100k tokens, all tokens (input and output) are charged at long context rates.

Model| Type| Price (/1M tokens) =< 200K input tokens| Price (/1M tokens) > 200K input tokens| Price (/1M tokens) =< 100K input tokens **| Price (/1M tokens) > 100K input tokens **  
---|---|---|---|---|---  
Claude Opus 4.6| Input| $5.50| $5.50| |   
| Output| $27.50| $27.50| |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| $6.875| |   
| 1h Cache Write| $11.00| $11.00| |   
| Cache Hit| $0.55| $0.55| |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
Claude Opus 4.5| Input| $5.50| | |   
| Output| $27.50| | |   
| Batch Input| $2.75| | |   
| Batch Output| $13.75| | |   
| 5m Cache Write| $6.875| | |   
| 1h Cache Write| $11.00| | |   
| Cache Hit| $0.55| | |   
| 5m Batch Cache Write| $3.438| | |   
| 1h Batch Cache Write| $5.50| | |   
| Batch Cache Hit| $0.275| | |   
Claude Sonnet 4.6| Input| $3.30| $3.30| |   
| Output| $16.50| $16.50| |   
| Batch Input| $1.65| | |   
| Batch Output| $8.25| | |   
| 5m Cache Write| $4.13| $4.13| |   
| 1h Cache Write| $6.60| $6.60| |   
| Cache Hit| $0.33| | |   
| 5m Batch Cache Write| $2.06| | |   
| 1h Batch Cache Write| $3.30| | |   
| Batch Cache Hit| $0.17| | |   
Claude Sonnet 4.5| Input| $3.30| $6.60| |   
| Output| $16.50| $24.75| |   
| Batch Input| $1.65| | |   
| Batch Output| $8.25| | |   
| 5m Cache Write| $4.13| $8.25| |   
| 1h Cache Write| $6.60| $13.20| |   
| Cache Hit| $0.33| $0.66| |   
| 5m Batch Cache Write| $2.06| | |   
| 1h Batch Cache Write| $3.30| | |   
| Batch Cache Hit| $0.17| | |   
  
* If a query input context is longer than or equal to 200K tokens, all tokens (input and output) are charged at long context rates.

** If a query input context is longer than or equal to 100k tokens, all tokens (input and output) are charged at long context rates.

Model| Type| Price (/1M tokens) =< 200K input tokens| Price (/1M tokens) > 200K input tokens  
---|---|---|---  
Claude Haiku 4.5| Input| $1.10|   
| Output| $5.50|   
| Batch Input| $0.55|   
| Batch Output| $2.75|   
| 5m Cache Write| $1.375|   
| 1h Cache Write| $2.20|   
| Cache Hit| $0.11|   
| 5m Batch Cache Write| $0.688|   
| 1h Batch Cache Write| $1.10|   
| Batch Cache Hit| $0.055|   
  
* If a query input context is longer than or equal to 200K tokens, all tokens (input and output) are charged at long context rates.

### 

Pricing for tools

Tool| Price (USD)  
---|---  
Web Search Request| **$10 per 1000 searches** Models Supported: Claude Haiku 4.5, Claude Sonnet 4.5, Claude Sonnet 4.6, Claude Sonnet 4, Claude Opus 4, Claude Opus 4.5 and Claude Opus 4.6.  
  
* If a query input context is longer than or equal to 200K tokens, all tokens (input and output) are charged at long context rates.

## 

xAI's Grok models

Model| Type| Price (/1M tokens) =< 200K input tokens| Price (/1M tokens) > 200K input tokens  
---|---|---|---  
Grok 4.7| Input| $2.00| $4.00  
| Output| $6.00| $12.00  
| Cache Hit| $0.50| $1.00  
Grok 4.6| Input| $2.00| $4.00  
| Output| $6.00| $12.00  
| Cache Hit| $0.50| $1.00  
Grok 4.20 Reasoning| Input| $1.25| $2.50  
| Output| $2.50| $5.00  
| Cache Hit| $0.20| $0.40  
Grok 4.20 Non-Reasoning| Input| $1.25| $2.50  
| Output| $2.50| $5.00  
| Cache Hit| $0.20| $0.40  
Grok 4.3| Input| $1.25| $2.50  
| Output| $2.50| $5.00  
| Cache Hit| $0.20| $0.40  
  
* If a query input context is longer than 200K tokens, all tokens are charged at long context rates.

Model| Type| Price / 1M tokens (USD)  
---|---|---  
Grok 4.1 Fast Reasoning| Input| $0.20  
| Output| $0.50  
| Cache Hit| $0.05  
Grok 4.1 Fast Non-Reasoning| Input| $0.20  
| Output| $0.50  
| Cache Hit| $0.05  
  
## 

Deepseek's models

Show discount options

Model| Type| Price /1M (USD)  
---|---|---  
DeepSeek-V3.1| Input| $0.60  
| Output| $1.70  
| Cache Hit| $0.06  
| Batch Input| $0.30  
| Batch Output| $0.85  
DeepSeek-V3.2| Input| $0.56  
| Output| $1.68  
| Cache Hit| $0.056  
| Batch Input| $0.28  
| Batch Output| $0.84  
DeepSeek-R1 (0528)| Input| $1.35  
| Output| $5.40  
| Batch Input| $0.675  
| Batch Output| $2.70  
DeepSeek-OCR| Input| $0.30  
| Output| $1.20  
  
## 

MiniMax's models

Show discount options

Model| Type| Price /1M (USD)  
---|---|---  
MiniMax-M2| Input| $0.30  
| Output| $1.20  
| Cache Hit| $0.03  
  
## 

Moonshot's models

Show discount options

Model| Type| Price /1M (USD)  
---|---|---  
Kimi-K2-Thinking| Input| $0.60  
| Output| $2.50  
| Cache Hit| $0.06  
  
## 

Qwen's models

Show discount options

Model| Type| Price /1M (USD)  
---|---|---  
Qwen3-Next-80B-Thinking| Input| $0.15  
| Output| $1.20  
Qwen3-Next-80B-Instruct| Input| $0.15  
| Output| $1.20  
Qwen3-Coder-480B-A35B-Instruct| Input| $0.22  
| Output| $1.80  
| Cache Hit| $0.022  
| Batch Input| $0.11  
| Batch Output| $0.90  
Qwen3-235B-A22B-Instruct-2507| Input| $0.22  
| Output| $0.88  
| Batch Input| $0.11  
| Batch Output| $0.44  
  
## 

GLM's models

Show discount options

Model| Type| Price /1M (USD)  
---|---|---  
GLM-4.7| Input| $0.60  
| Output| $2.20  
| Cache Hit| $0.06  
GLM-5| Input| $1.00  
| Output| $3.20  
| Cache Hit| $0.10  
GLM-5.2| Input| $1.40  
| Output| $4.40  
| Cached Input:| $0.14  
  
## 

OpenAI's models

Show discount options

Model| Type| Price /1M (USD)  
---|---|---  
gpt-oss-120b| Input| $0.09  
| Output| $0.36  
| Batch Input| $0.045  
| Batch Output| $0.18  
gpt-oss-20b| Input| $0.07  
| Output| $0.25  
| Cache Hit| $0.007  
| Batch Input| $0.035  
| Batch Output| $0.125  
  
## 

Meta's Llama models

Show discount options

Model| Type| Price /1M (USD)  
---|---|---  
Llama 3.3 70B| Input| $0.72  
| Output| $0.72  
| Batch Input| $0.36  
| Batch Output| $0.36  
Llama 4 Scout| Input| $0.25  
| Output| $0.70  
| Batch Input| $0.125  
| Batch Output| $0.35  
Llama 4 Maverick| Input| $0.35  
| Output| $1.15  
| Batch Input| $0.175  
| Batch Output| $0.575  
  
## 

Mistral AI’s models

Model| Type| Price /1M (USD)  
---|---|---  
Mistral OCR (25.05)| Input| $0.0005 (or $0.0005/page)  
| Output| $0.0005 (or $0.0005/page)  
Mistral Medium 3| Input| $0.40   
| Output| $2.00  
Mistral Small 3.1 (25.03)| Input| $0.10  
| Output| $0.30  
Codestral 2| Input| $0.30  
| Output| $0.90  
  
## Request a custom quote

With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization.

Contact sales[](https://cloud.google.com/contact?direct=true)

menu

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

[Overview](https://cloud.google.com/why-google-cloud)[Solutions](https://cloud.google.com/solutions)[Products](https://cloud.google.com/products)[Pricing](https://cloud.google.com/pricing)[Resources](https://cloud.google.com/docs/get-started)[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)[Contact us](https://cloud.google.com/contact)



 _search_ _send_




[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)

[Console](https://console.cloud.google.com/)

[Sign in](https://accounts.google.com/AccountChooser?continue=https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing&hl=en-US&prompt=select_account&service=cloudconsole)

Start free[](https://console.cloud.google.com/freetrial)

Start free[](https://console.cloud.google.com/freetrial)

Contact us[](https://cloud.google.com/contact)

close

  * Accelerate your digital transformation
  * Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.
  * [Learn more](https://cloud.google.com/transform)




  * Key benefits
  * [Why Google CloudTop reasons businesses choose us.](https://cloud.google.com/why-google-cloud)

  * [AI and AgentsGet enterprise-ready AI.](https://cloud.google.com/ai)

  * [MulticloudRun your apps wherever you need them.](https://cloud.google.com/multicloud)

  * [Global infrastructureBuild on the same infrastructure as Google.](https://cloud.google.com/infrastructure)




  * [Data CloudMake smarter decisions with unified data.](https://cloud.google.com/data-cloud)

  * [Modern Infrastructure CloudNext generation of cloud infrastructure.](https://cloud.google.com/solutions/modern-infrastructure)

  * [SecurityProtect your users, data, and apps.](https://cloud.google.com/security)

  * [Productivity and collaborationConnect your teams with AI-powered apps.](https://workspace.google.com)




  * Reports and insights
  * [Executive insightsCurated C-suite perspectives.](https://cloud.google.com/executive-insights)

  * [Analyst reportsRead what industry analysts say about us.](https://cloud.google.com/analyst-reports)

  * [WhitepapersBrowse and download popular whitepapers.](https://cloud.google.com/whitepapers)

  * [Customer storiesExplore case studies and videos.](https://cloud.google.com/customers)




close

  * Industry Solutions
  * Application Modernization
  * Artificial Intelligence
  * APIs and Applications
  * Data Analytics
  * Databases
  * Infrastructure Modernization
  * Productivity and Collaboration
  * Security
  * Startups and SMB



See all solutions[](https://cloud.google.com/solutions)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Industry SolutionsReduce cost, increase operational agility, and capture new market opportunities.](https://cloud.google.com/solutions#industry-solutions)


  * [![](https://www.gstatic.com/cloud/images/navigation/retail.svg)RetailAnalytics and collaboration tools for the retail value chain.](https://cloud.google.com/solutions/retail)


  * [![](https://www.gstatic.com/cloud/images/navigation/cpg.svg)Consumer Packaged GoodsSolutions for CPG digital transformation and brand growth.](https://cloud.google.com/solutions/cpg)


  * [![](https://www.gstatic.com/cloud/images/navigation/finance.svg)Financial ServicesComputing, data management, and analytics tools for financial services.](https://cloud.google.com/solutions/financial-services)


  * [![](https://www.gstatic.com/cloud/images/navigation/hcls.svg)Healthcare and Life SciencesAdvance research at scale and empower healthcare innovation.](https://cloud.google.com/solutions/healthcare-life-sciences)


  * [![](https://www.gstatic.com/cloud/images/navigation/media.svg)Media and EntertainmentSolutions for content production and distribution operations.](https://cloud.google.com/solutions/media-entertainment)


  * [![](https://www.gstatic.com/cloud/images/navigation/telecommunications.svg)TelecommunicationsHybrid and multi-cloud services to deploy and monetize 5G.](https://cloud.google.com/solutions/telecommunications)


  * [![](https://www.gstatic.com/cloud/images/navigation/gaming.svg)GamesAI-driven solutions to build and scale games faster.](https://cloud.google.com/solutions/games)


  * [![](https://www.gstatic.com/cloud/images/navigation/manufacturing.svg)ManufacturingMigration and AI tools to optimize the manufacturing value chain.](https://cloud.google.com/solutions/manufacturing)


  * [![](https://www.gstatic.com/cloud/images/navigation/supply-chain.svg)Supply Chain and LogisticsEnable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.](https://cloud.google.com/solutions/supply-chain-logistics)


  * [![](https://www.gstatic.com/cloud/images/navigation/government.svg)GovernmentData storage, AI, and analytics solutions for government agencies.](https://cloud.google.com/gov)


  * [![](https://www.gstatic.com/cloud/images/navigation/icon-sprite.svg#education)EducationTeaching tools to provide more engaging learning experiences.](https://cloud.google.com/edu/higher-education)


  * Not seeing what you're looking for?
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Application ModernizationModernize, automate, and scale your application and data portfolio using enterprise AI, intelligent engineering practices, and cloud-native infrastructure.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Application Modernization with AIAI-assisted code refactoring, assessment, and transformation for legacy applications.](https://cloud.google.com/solutions/application-modernization-with-ai)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Mainframe ModernizationAutomated tools and AI-driven guidance for moving your mainframe apps to the cloud.](https://cloud.google.com/solutions/mainframe-modernization)


  * [Database ModernizationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Data Lake ModernizationUnify and govern multimodal data on an open, high-performance cloud data lake.](https://cloud.google.com/solutions/data-lakehouse)


  * [Data Warehouse ModernizationMigrate and modernize your enterprise data warehouse for serverless analytics and AI.](https://cloud.google.com/solutions/data-migration)


  * [APIsUnlock legacy applications and build new digital channels using APIs and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [Platform EngManaged services and golden paths to build, manage, and scale internal developer platforms.](https://cloud.google.com/solutions/platform-engineering)


  * [DevOps Best PracticesProcesses and resources for implementing DevOps in your org.](https://cloud.google.com/devops)


  * [SRE PrinciplesTools and resources for adopting SRE in your org.](https://cloud.google.com/sre)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Artificial IntelligenceAdd intelligence and efficiency to your business with AI and machine learning.](https://cloud.google.com/solutions/ai)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Gemini for enterpriseUnified agentic portfolio for your entire organization.](https://cloud.google.com/gemini-enterprise)


  * [AI Commerce SearchGoogle-quality search and product recommendations for retailers.](https://cloud.google.com/gemini-enterprise-cx/commerce)


  * [Google Cloud with GeminiAI assistants for application development, coding, and more.](https://cloud.google.com/ai/gemini)


  * [Physical AISimulate, train, and operate the next generation of robots, autonomous vehicles, industrial devices, and machines.](https://cloud.google.com/solutions/physical-ai)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)APIs and ApplicationsSpeed up the pace of innovation without coding, using APIs, apps, and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [New Business Channels Using APIsAttract and empower an ecosystem of developers and partners.](https://cloud.google.com/solutions/new-channels-using-apis)


  * [Unlocking Legacy Applications Using APIsCloud services for extending and modernizing legacy apps.](https://cloud.google.com/solutions/unlocking-legacy-applications)


  * [Open Banking APIxSimplify and accelerate secure delivery of open banking compliant APIs.](https://cloud.google.com/solutions/open-banking-apix)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data AnalyticsGenerate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [Data MigrationMigrate and modernize your data warehouse and data lakes with AI-powered migration services.](https://cloud.google.com/solutions/data-migration)


  * [Data LakehouseUnify and govern your multimodal data with a high-performance and open data lakehouse.](https://cloud.google.com/solutions/data-lakehouse)


  * [Real-time AnalyticsInsights from ingesting, processing, and analyzing event streams.](https://cloud.google.com/solutions/stream-analytics)


  * [Marketing AnalyticsSolutions for collecting, analyzing, and activating customer data.](https://cloud.google.com/solutions/marketing-analytics)


  * [DatasetsData from Google, public, and commercial providers to enrich your analytics and AI initiatives.](https://cloud.google.com/datasets)


  * [Business IntelligenceSolutions for modernizing your BI stack and creating rich data experiences.](https://cloud.google.com/solutions/business-intelligence)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Geospatial AnalyticsA comprehensive platform to solve for geospatial use cases at scale.](https://cloud.google.com/solutions/geospatial)


  * [Data ScienceManaged services and integrated workflows to build, manage, and scale data science.](https://cloud.google.com/solutions/data-science)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)DatabasesMigrate and manage enterprise data with security, reliability, high availability, and fully managed data services.](https://cloud.google.com/solutions/databases)


  * [Database MigrationGuides and tools to simplify your database migration life cycle.](https://cloud.google.com/solutions/database-migration)


  * [Database ModernizationUpgrades to modernize your operational database infrastructure.](https://cloud.google.com/solutions/database-modernization)


  * [Databases for GamesBuild global, live games with Google Cloud databases.](https://cloud.google.com/solutions/databases/games)


  * [Google Cloud DatabasesDatabase services to migrate, manage, and modernize data.](https://cloud.google.com/products/databases)


  * [Migrate Oracle workloads to Google CloudRehost, replatform, rewrite your Oracle workloads.](https://cloud.google.com/solutions/oracle)


  * [Open Source DatabasesFully managed open source databases with enterprise-grade support.](https://cloud.google.com/solutions/open-source-databases)


  * [SQL Server on Google CloudOptions for running SQL Server virtual machines on Google Cloud.](https://cloud.google.com/sql-server)


  * [Gemini for DatabasesSupercharge database development and management with AI.](https://cloud.google.com/products/gemini/databases)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Infrastructure ModernizationMigrate core systems rapidly and modernize enterprise workloads with AI-powered infrastructure and automated cloud solutions.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Rapid Migration and Modernization Program (RaMP)End-to-end migration program to simplify and accelerate your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Data Center ExitsMigration solutions for moving VMs, apps, databases, and workloads out of data centers.](https://cloud.google.com/solutions/data-center-migration)


  * [Application Modernization & MigrationDiscovery, assessment, and migration tools for moving and modernizing applications.](https://cloud.google.com/solutions/application-migration)


  * [Database Modernization & MigrationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Cross-Cloud NetworkingSimplify hybrid and multicloud networking, and secure your workloads, data, and users.](https://cloud.google.com/solutions/cross-cloud-network)


  * [High Performance Computing (HPC)Compute, storage, and networking options to support any high-performance workload.](https://cloud.google.com/solutions/hpc)


  * [VMwareFully managed, native VMware Cloud Foundation software stack on Google Cloud.](https://cloud.google.com/vmware-engine)


  * [SAPCertified infrastructure and AI solutions for running SAP applications and SAP HANA.](https://cloud.google.com/solutions/sap)


  * [WindowsTools, licenses, and partner solutions for running enterprise Windows workloads.](https://cloud.google.com/windows)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Productivity and CollaborationChange the way teams work with solutions designed for humans and built for impact.](https://workspace.google.com/enterprise/)


  * [Google WorkspaceCollaboration and productivity tools for enterprises.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome Browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)SecurityDetect, investigate, and respond to online threats to help protect your business.](https://cloud.google.com/solutions/security)


  * [Agentic SOCDelivering better security outcomes with AI agents.](https://cloud.google.com/solutions/agentic-soc)


  * [Web App and API ProtectionThreat and fraud protection for your web applications and APIs.](https://cloud.google.com/security/solutions/web-app-and-api-protection)


  * [Security and Resilience FrameworkSolutions for each phase of the security and resilience life cycle.](https://cloud.google.com/security/solutions/security-and-resilience)


  * [Risk and compliance as code (RCaC)Solution to modernize your governance, risk, and compliance function with automation.](https://cloud.google.com/solutions/risk-and-compliance-as-code)


  * [Software Supply Chain SecuritySolution for improving end-to-end software supply chain security.](https://cloud.google.com/security/solutions/software-supply-chain-security)


  * [Security FoundationRecommended products to help achieve a strong security posture.](https://cloud.google.com/security/solutions/security-foundation)


  * [Google Cloud Cybershield™Strengthen nationwide cyber defense.](https://cloud.google.com/security/solutions/secops-cybershield)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Startups and SMBAccelerate startup and SMB growth with tailored solutions and programs.](https://cloud.google.com/solutions#section-13)


  * [Startup ProgramGet financial, business, and technical support to take your startup to the next level.](https://cloud.google.com/startup)


  * [Small and Medium BusinessExplore solutions for web hosting, app development, AI, and analytics.](https://cloud.google.com/solutions/smb)


  * [Software as a ServiceBuild better SaaS products, scale efficiently, and grow your business.](https://cloud.google.com/saas)



close

  * Featured Products
  * AI and Machine Learning
  * Business Intelligence
  * Compute
  * Containers
  * Data Analytics
  * Databases
  * Developer Tools
  * Distributed Cloud
  * Hybrid and Multicloud
  * Industry Specific
  * Integration Services
  * Management Tools
  * Maps and Geospatial
  * Media Services
  * Migration
  * Networking
  * Operations
  * Productivity and Collaboration
  * Security and Identity
  * Serverless
  * Storage
  * Web3



See all products (100+)[](https://cloud.google.com/products#featured-products)

  * Featured Products


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [![](https://www.gstatic.com/cloud/images/navigation/compute-engine.png)Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-storage.png)Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [![](https://www.gstatic.com/cloud/images/navigation/bigquery.png)BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-run.png)Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [![](https://www.gstatic.com/cloud/images/navigation/kubernetes-engine.png)Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [![](https://www.gstatic.com/cloud/images/navigation/looker.png)LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [![](https://www.gstatic.com/cloud/images/navigation/apigee.png)Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-sql.png)Cloud SQLRelational database services for MySQL, PostgreSQL and SQL Server.](https://cloud.google.com/sql)


  * [![](https://www.gstatic.com/cloud/images/navigation/networking.png)Cloud CDNContent delivery network for delivering web and video.](https://cloud.google.com/cdn)


  * Not seeing what you're looking for?
  * [See all products (100+)](https://cloud.google.com/products#featured-products)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)AI and Machine Learning](https://cloud.google.com/products/ai)


  * [Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Model GardenSingle place to discover over 200 models from Google and Google partners.](https://console.cloud.google.com/agent-platform/model-garden)


  * [Customer Experience Agent StudioBuild conversational AI with both deterministic and gen AI functionality.](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


  * [Agent SearchBuild Google-quality search for your enterprise apps and experiences.](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)


  * [Speech-to-TextSpeech recognition and transcription across 125 languages.](https://cloud.google.com/speech-to-text)


  * [Text-to-SpeechSpeech synthesis in 220+ voices and 40+ languages.](https://cloud.google.com/text-to-speech)


  * [Translation AILanguage detection, translation, and glossary support.](https://cloud.google.com/translate)


  * [Vision AICustom and pre-trained models to detect emotion, text, and more.](https://cloud.google.com/vision)


  * [Contact Center as a ServiceOmnichannel contact center solution that is native to the cloud.](https://cloud.google.com/solutions/contact-center-ai-platform)


  * Not seeing what you're looking for?
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)



  * Business Intelligence


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [Data StudioInteractive data suite for dashboarding, reporting, and analytics.](https://cloud.google.com/data-studio)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Compute](https://cloud.google.com/products/compute)


  * [Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [Cloud GPUsGPUs for ML, scientific computing, and 3D visualization.](https://cloud.google.com/gpu)


  * [Migrate to Virtual MachinesServer and virtual machine migration to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Spot VMsCompute instances for batch jobs and fault-tolerant workloads.](https://cloud.google.com/spot-vms)


  * [BatchFully managed service for scheduling batch jobs.](https://cloud.google.com/batch)


  * [Sole-Tenant NodesDedicated hardware for compliance, licensing, and management.](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)


  * [Bare MetalInfrastructure to run specialized workloads on Google Cloud.](https://cloud.google.com/bare-metal)


  * [RecommenderUsage recommendations for Google Cloud products and services.](https://cloud.google.com/recommender/docs/whatis-activeassist)


  * [VMware EngineFully managed, native VMware Cloud Foundation software stack.](https://cloud.google.com/vmware-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * Not seeing what you're looking for?
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Containers](https://cloud.google.com/containers)


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud BuildSolution for running build steps in a Docker container.](https://cloud.google.com/build)


  * [Artifact RegistryPackage manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Deep Learning ContainersContainers with data science frameworks, libraries, and tools.](https://cloud.google.com/deep-learning-containers/docs)


  * [KnativeComponents to create Kubernetes-native cloud-based software.](https://knative.dev/docs/)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [DataflowReal-time analytics for stream and batch processing.](https://cloud.google.com/products/dataflow)


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [LakehouseOpen lakehouse platform with enterprise storage and performance capabilities.](https://cloud.google.com/products/lakehouse)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Knowledge CatalogAlways-on catalog for AI that provides universal context for agents.](https://cloud.google.com/products/knowledge-catalog)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Data Analytics Migration ServicesFree-to-use, cloud-native and AI-powered data migration services.](https://cloud.google.com/solutions/data-migration)


  * [Managed Service for Apache KafkaManaged Kafka service to operate highly available Apache Kafka clusters.](https://cloud.google.com/products/managed-service-for-apache-kafka)


  * Not seeing what you're looking for?
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Databases](https://cloud.google.com/products/databases)


  * [AlloyDB for PostgreSQLFully managed, PostgreSQL-compatible database for enterprise workloads.](https://cloud.google.com/alloydb)


  * [Cloud SQLFully managed database for MySQL, PostgreSQL, and SQL Server.](https://cloud.google.com/sql)


  * [FirestoreHighly scalable and serverless NoSQL document database, with MongoDB compatibility.](https://cloud.google.com/firestore)


  * [SpannerCloud-native relational database with unlimited scale and 99.999% availability.](https://cloud.google.com/spanner)


  * [BigtableCloud-native wide-column database for large-scale, low-latency workloads.](https://cloud.google.com/bigtable)


  * [DatastreamServerless change data capture and replication service.](https://cloud.google.com/datastream)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Bare Metal SolutionFully managed infrastructure for your Oracle workloads.](https://cloud.google.com/bare-metal)


  * [MemorystoreFully managed Redis and Memcached for sub-millisecond data access.](https://cloud.google.com/memorystore)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Developer Tools](https://cloud.google.com/products/tools)


  * [Artifact RegistryUniversal package manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud BuildContinuous integration and continuous delivery platform.](https://cloud.google.com/build)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Cloud Deployment ManagerService for creating and managing Google Cloud resources.](https://cloud.google.com/deployment-manager/docs)


  * [Cloud SDKCommand-line tools and libraries for Google Cloud.](https://cloud.google.com/sdk)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Cloud Source RepositoriesPrivate Git repository to store, manage, and track code.](https://cloud.google.com/source-repositories/docs)


  * [Infrastructure ManagerAutomate infrastructure management with Terraform.](https://cloud.google.com/infrastructure-manager/docs)


  * [Cloud WorkstationsManaged and secure development environments in the cloud.](https://cloud.google.com/workstations)


  * [Gemini Code AssistAI-powered assistant available across Google Cloud and your IDE.](https://cloud.google.com/products/gemini/code-assist)


  * Not seeing what you're looking for?
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Distributed Cloud](https://cloud.google.com/distributed-cloud)


  * [Google Distributed Cloud ConnectedDistributed cloud services for edge workloads.](https://cloud.google.com/distributed-cloud-connected)


  * [Google Distributed Cloud Air-gappedDistributed cloud for air-gapped workloads.](https://cloud.google.com/distributed-cloud-air-gapped)



  * Hybrid and Multicloud


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Apigee API ManagementAPI management, development, and security platform.](https://cloud.google.com/apigee)


  * [Migrate to ContainersTool to move workloads and existing applications to GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Cloud BuildService for executing builds on Google Cloud infrastructure.](https://cloud.google.com/build)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Cloud Service MeshFully managed service mesh based on Envoy and Istio.](https://cloud.google.com/products/service-mesh)


  * [Google Distributed CloudFully managed solutions for the edge and data centers.](https://cloud.google.com/distributed-cloud)



  * Industry Specific


  * [Anti Money Laundering AIDetect suspicious, potential money laundering activity with AI.](https://cloud.google.com/anti-money-laundering-ai)


  * [Cloud Healthcare APISolution for bridging existing care systems and apps on Google Cloud.](https://cloud.google.com/healthcare-api)


  * [Device Connect for FitbitGain a 360-degree patient view with connected Fitbit data on Google Cloud.](https://cloud.google.com/device-connect)


  * [Telecom Network AutomationReady to use cloud-native automation for telecom networks.](https://cloud.google.com/telecom-network-automation)


  * [Telecom Data FabricTelecom data management and analytics with an automated approach.](https://cloud.google.com/telecom-data-fabric)


  * [Telecom Subscriber InsightsIngests data to improve subscriber acquisition and retention.](https://cloud.google.com/telecom-subscriber-insights)


  * [Spectrum Access System (SAS)Controls fundamental access to the Citizens Broadband Radio Service (CBRS).](https://cloud.google.com/products/spectrum-access-system)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Integration Services](https://cloud.google.com/integration-services)


  * [Application IntegrationConnect to 3rd party apps and enable data consistency without code.](https://cloud.google.com/application-integration)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [Cloud TasksTask management service for asynchronous task execution.](https://cloud.google.com/tasks/docs)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [Cloud Data FusionData integration for building and managing data pipelines.](https://cloud.google.com/data-fusion)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [EventarcBuild an event-driven architecture that can connect any service.](https://cloud.google.com/eventarc/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Management Tools](https://cloud.google.com/products/management)


  * [Cloud ShellInteractive shell environment with a built-in command line.](https://cloud.google.com/shell/docs)


  * [Cloud consoleWeb-based interface for managing and monitoring cloud apps.](https://cloud.google.com/cloud-console)


  * [Cloud EndpointsDeployment and development management for APIs on Google Cloud.](https://cloud.google.com/endpoints/docs)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Cloud APIsProgrammatic interfaces for Google Cloud services.](https://cloud.google.com/apis)


  * [Service CatalogService catalog for admins managing internal enterprise solutions.](https://cloud.google.com/service-catalog/docs)


  * [Cost ManagementTools for monitoring, controlling, and optimizing your costs.](https://cloud.google.com/cost-management)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Carbon FootprintDashboard to view and export Google Cloud carbon emissions reports.](https://cloud.google.com/carbon-footprint)


  * [Config ConnectorKubernetes add-on for managing Google Cloud resources.](https://cloud.google.com/config-connector/docs/overview)


  * [Active AssistTools for easily managing performance, security, and cost.](https://cloud.google.com/solutions/active-assist)


  * Not seeing what you're looking for?
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Maps and Geospatial](https://cloud.google.com/solutions/geospatial)


  * [Earth EngineGeospatial platform for Earth observation data and analysis.](https://cloud.google.com/earth-engine)


  * [Google Maps PlatformCreate immersive location experiences and improve business operations.](https://mapsplatform.google.com)



  * Media Services


  * [Cloud CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Live Stream APIService to convert live video and package for streaming.](https://cloud.google.com/livestream/docs)


  * [OpenCueOpen source render manager for visual effects and animation.](https://www.opencue.io/docs/getting-started/)


  * [Transcoder APIConvert video files and package them for optimized delivery.](https://cloud.google.com/transcoder/docs)


  * [Video Stitcher APIService for dynamic or server side ad insertion.](https://cloud.google.com/video-stitcher/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Migration](https://cloud.google.com/products/cloud-migration)


  * [Migration CenterUnified platform for migrating and modernizing with Google Cloud.](https://cloud.google.com/migration-center/docs)


  * [Application MigrationApp migration to the cloud for low-cost refresh cycles.](https://cloud.google.com/solutions/application-migration)


  * [Migrate to Virtual MachinesComponents for migrating VMs and physical servers to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Cloud Foundation ToolkitReference templates for Deployment Manager and Terraform.](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Data Analytics Migration ServicesStreamlined data warehouse and data lake migration tooling and incentives.](https://cloud.google.com/solutions/data-migration)


  * [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Transfer ApplianceStorage server for moving large volumes of data to Google Cloud.](https://cloud.google.com/transfer-appliance/docs/4.0/overview)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [VMware EngineMigrate and run your VMware workloads natively on Google Cloud.](https://cloud.google.com/vmware-engine)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Networking](https://cloud.google.com/products/networking)


  * [Cloud ArmorSecurity policies and defense against web and DDoS attacks.](https://cloud.google.com/security/products/armor)


  * [Cloud CDN and Media CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Cloud DNSDomain name system for reliable and low-latency name lookups.](https://cloud.google.com/dns)


  * [Cloud Load BalancingService for distributing traffic across applications and regions.](https://cloud.google.com/load-balancing)


  * [Cloud NATNAT service for giving private instances internet access.](https://cloud.google.com/nat)


  * [Cloud ConnectivityConnectivity options for VPN, peering, and enterprise needs.](https://cloud.google.com/hybrid-connectivity)


  * [Network Connectivity CenterConnectivity management to help simplify and scale networks.](https://cloud.google.com/network-connectivity-center)


  * [Network Intelligence CenterNetwork monitoring, verification, and optimization platform.](https://cloud.google.com/network-intelligence-center)


  * [Network Service TiersCloud network options based on performance, availability, and cost.](https://cloud.google.com/network-tiers)


  * [Virtual Private CloudSingle VPC for an entire organization, isolated within projects.](https://cloud.google.com/vpc)


  * [Private Service ConnectSecure connection between your VPC and services.](https://cloud.google.com/private-service-connect)


  * Not seeing what you're looking for?
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Operations](https://cloud.google.com/products/operations)


  * [Cloud LoggingGoogle Cloud audit, platform, and application logs management.](https://cloud.google.com/logging)


  * [Cloud MonitoringInfrastructure and application health with rich metrics.](https://cloud.google.com/monitoring)


  * [Error ReportingApplication error identification and analysis.](https://cloud.google.com/error-reporting/docs/grouping-errors)


  * [Managed Service for PrometheusFully-managed Prometheus on Google Cloud.](https://cloud.google.com/managed-prometheus)


  * [Cloud TraceTracing system collecting latency data from applications.](https://cloud.google.com/trace/docs)


  * [Cloud ProfilerCPU and heap profiler for analyzing application performance.](https://cloud.google.com/profiler/docs)


  * [Cloud QuotasManage quotas for all Google Cloud services.](https://cloud.google.com/docs/quotas)



  * Productivity and Collaboration


  * [AppSheetNo-code development platform to build and extend applications.](https://about.appsheet.com/home/)


  * [AppSheet AutomationBuild automations and applications on a unified platform.](https://cloud.google.com/appsheet/automation)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Google WorkspaceCollaboration and productivity tools for individuals and organizations.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Security and Identity](https://cloud.google.com/products/security-and-identity)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Sensitive Data ProtectionDiscover, classify, and protect your valuable data assets.](https://cloud.google.com/security/products/sensitive-data-protection)


  * [Mandiant Managed DefenseFind and eliminate threats with confidence 24x7.](https://cloud.google.com/security/products/managed-defense)


  * [Google Threat IntelligenceKnow who’s targeting you.](https://cloud.google.com/security/products/threat-intelligence)


  * [Security Command CenterPlatform for defending against threats to your Google Cloud assets.](https://cloud.google.com/security/products/security-command-center)


  * [Cloud Key ManagementManage encryption keys on Google Cloud.](https://cloud.google.com/security/products/security-key-management)


  * [Mandiant Incident ResponseMinimize the impact of a breach.](https://cloud.google.com/security/consulting/mandiant-incident-response-services)


  * [Chrome Enterprise PremiumGet secure enterprise browsing with extensive endpoint visibility.](https://docs.cloud.google.com/chrome-enterprise-premium/)


  * [Assured WorkloadsCompliance and security controls for sensitive workloads.](https://cloud.google.com/security/products/assured-workloads)


  * [Google Security OperationsDetect, investigate, and respond to cyber threats.](https://cloud.google.com/security/products/security-operations)


  * [Mandiant ConsultingGet expert guidance before, during, and after an incident.](https://cloud.google.com/security/consulting/mandiant-services)


  * Not seeing what you're looking for?
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Serverless](https://cloud.google.com/serverless)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud FunctionsPlatform for creating functions that respond to cloud events.](https://cloud.google.com/functions)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [API GatewayDevelop, deploy, secure, and manage APIs with a fully managed gateway.](https://cloud.google.com/api-gateway/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Storage](https://cloud.google.com/products/storage)


  * [Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [Block StorageHigh-performance storage for AI, analytics, databases, and enterprise applications.](https://cloud.google.com/products/block-storage)


  * [FilestoreFile storage that is highly scalable and secure.](https://cloud.google.com/filestore)


  * [Persistent DiskBlock storage for virtual machine instances running on Google Cloud.](https://cloud.google.com/persistent-disk)


  * [Cloud Storage for FirebaseObject storage for storing and serving user-generated content.](https://firebase.google.com/products/storage)


  * [Local SSDBlock storage that is locally attached for high-performance needs.](https://cloud.google.com/products/local-ssd)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [Google Cloud Managed LustreHigh performance managed parallel file service.](https://cloud.google.com/products/managed-lustre)


  * [Google Cloud NetApp VolumesFile storage service for NFS, SMB, and multi-protocol environments.](https://cloud.google.com/netapp-volumes)


  * [Backup and DR ServiceService for centralized, application-consistent data protection.](https://cloud.google.com/backup-disaster-recovery)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Web3](https://cloud.google.com/web3)


  * [Blockchain Node EngineFully managed node hosting for developing on the blockchain.](https://cloud.google.com/blockchain-node-engine)


  * [Blockchain RPCEnterprise-grade RPC for building on the blockchain.](https://cloud.google.com/products/blockchain-rpc)



close

  * Save money with our transparent approach to pricing
  * Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)




  * Pricing overview and tools
  * [Google Cloud pricingPay only for what you use with no lock-in.](https://cloud.google.com/pricing)

  * [Pricing calculatorCalculate your cloud savings.](https://cloud.google.com/products/calculator)

  * [Google Cloud free tierExplore products with free monthly usage.](https://cloud.google.com/free)




  * [Cost optimization frameworkGet best practices to optimize workload costs.](https://cloud.google.com/architecture/framework/cost-optimization)

  * [Cost management toolsTools to monitor and control your costs.](https://cloud.google.com/cost-management)




  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)

  * [Cloud SQL](https://cloud.google.com/sql/pricing)

  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)

  * [Cloud Storage](https://cloud.google.com/storage/pricing)

  * [BigQuery](https://cloud.google.com/bigquery/pricing)

  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)




close

  * Learn & build
  * [Google Cloud Free Program$300 in free credits and 20+ free products.](https://cloud.google.com/free)

  * [Solution GeneratorGet AI generated solution recommendations.](https://cloud.google.com/solution-generator)

  * [QuickstartsGet tutorials and walkthroughs.](https://cloud.google.com/docs/tutorials?doctype=quickstart)

  * [BlogRead our latest product news and stories.](https://cloud.google.com/blog)




  * [Learning HubGrow your career with role-based training.](https://cloud.google.com/learn)

  * [Google Cloud certificationPrepare and register for certifications.](https://cloud.google.com/certification)

  * [Cloud computing basicsLearn more about cloud computing basics.](https://cloud.google.com/discover)

  * [Cloud Architecture CenterGet reference architectures and best practices.](https://cloud.google.com/architecture)




  * Connect
  * [InnovatorsJoin Google Cloud's developer program.](https://cloud.google.com/innovators/innovatorsplus)

  * [Developer CenterStay in the know and stay connected.](https://cloud.google.com/developers)

  * [Events and webinarsBrowse upcoming and on demand events.](https://cloud.google.com/events)

  * [Google Cloud CommunityAsk questions, find answers, and connect.](https://discuss.google.dev/c/google-cloud/14)




  * Consulting and Partners
  * [Google Cloud ConsultingWork with our experts on cloud projects.](https://cloud.google.com/consulting)

  * [Google Cloud MarketplaceDeploy ready-to-go solutions in a few clicks.](https://cloud.google.com/marketplace)

  * [Find a partnerExplore the benefits of working with a partner.](https://cloud.google.com/partners)

  * [Google Cloud partnersLearn about the ecosystem and resources.](https://partners.cloud.google.com)




close

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

  * [Overview](https://cloud.google.com/why-google-cloud)
    * arrow_forward
  * [Solutions](https://cloud.google.com/solutions)
    * arrow_forward
  * [Products](https://cloud.google.com/products)
    * arrow_forward
  * [Pricing](https://cloud.google.com/pricing)
    * arrow_forward
  * [Resources](https://cloud.google.com/docs/get-started)
    * arrow_forward
  * [Docs](https://cloud.google.com/docs)
  * [Support](https://cloud.google.com/support-hub)
  * [Console](https://console.cloud.google.com/)



  * Accelerate your digital transformation
  * [Learn more](https://cloud.google.com/transform)
  * Key benefits
  * [Why Google Cloud](https://cloud.google.com/why-google-cloud)
  * [AI and Agents](https://cloud.google.com/ai)
  * [Multicloud](https://cloud.google.com/multicloud)
  * [Global infrastructure](https://cloud.google.com/infrastructure)
  * [Data Cloud](https://cloud.google.com/data-cloud)
  * [Modern Infrastructure Cloud](https://cloud.google.com/solutions/modern-infrastructure)
  * [Security](https://cloud.google.com/security)
  * [Productivity and collaboration](https://workspace.google.com)
  * Reports and insights
  * [Executive insights](https://cloud.google.com/executive-insights)
  * [Analyst reports](https://cloud.google.com/analyst-reports)
  * [Whitepapers](https://cloud.google.com/whitepapers)
  * [Customer stories](https://cloud.google.com/customers)


  * [Industry Solutions](https://cloud.google.com/solutions#industry-solutions)
  * [Retail](https://cloud.google.com/solutions/retail)
  * [Consumer Packaged Goods](https://cloud.google.com/solutions/cpg)
  * [Financial Services](https://cloud.google.com/solutions/financial-services)
  * [Healthcare and Life Sciences](https://cloud.google.com/solutions/healthcare-life-sciences)
  * [Media and Entertainment](https://cloud.google.com/solutions/media-entertainment)
  * [Telecommunications](https://cloud.google.com/solutions/telecommunications)
  * [Games](https://cloud.google.com/solutions/games)
  * [Manufacturing](https://cloud.google.com/solutions/manufacturing)
  * [Supply Chain and Logistics](https://cloud.google.com/solutions/supply-chain-logistics)
  * [Government](https://cloud.google.com/gov)
  * [Education](https://cloud.google.com/edu/higher-education)
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)
  * [See all solutions](https://cloud.google.com/solutions)
  * [Application Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Application Modernization with AI](https://cloud.google.com/solutions/application-modernization-with-ai)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Mainframe Modernization](https://cloud.google.com/solutions/mainframe-modernization)
  * [Database Modernization](https://cloud.google.com/products/databases)
  * [Data Lake Modernization](https://cloud.google.com/solutions/data-lakehouse)
  * [Data Warehouse Modernization](https://cloud.google.com/solutions/data-migration)
  * [APIs](https://cloud.google.com/solutions/apis-and-applications)
  * [Platform Eng](https://cloud.google.com/solutions/platform-engineering)
  * [DevOps Best Practices](https://cloud.google.com/devops)
  * [SRE Principles](https://cloud.google.com/sre)
  * [Artificial Intelligence](https://cloud.google.com/solutions/ai)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Gemini for enterprise](https://cloud.google.com/gemini-enterprise)
  * [AI Commerce Search](https://cloud.google.com/gemini-enterprise-cx/commerce)
  * [Google Cloud with Gemini](https://cloud.google.com/ai/gemini)
  * [Physical AI](https://cloud.google.com/solutions/physical-ai)
  * [APIs and Applications](https://cloud.google.com/solutions/apis-and-applications)
  * [New Business Channels Using APIs](https://cloud.google.com/solutions/new-channels-using-apis)
  * [Unlocking Legacy Applications Using APIs](https://cloud.google.com/solutions/unlocking-legacy-applications)
  * [Open Banking APIx](https://cloud.google.com/solutions/open-banking-apix)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [Data Migration](https://cloud.google.com/solutions/data-migration)
  * [Data Lakehouse](https://cloud.google.com/solutions/data-lakehouse)
  * [Real-time Analytics](https://cloud.google.com/solutions/stream-analytics)
  * [Marketing Analytics](https://cloud.google.com/solutions/marketing-analytics)
  * [Datasets](https://cloud.google.com/datasets)
  * [Business Intelligence](https://cloud.google.com/solutions/business-intelligence)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Geospatial Analytics](https://cloud.google.com/solutions/geospatial)
  * [Data Science](https://cloud.google.com/solutions/data-science)
  * [Databases](https://cloud.google.com/solutions/databases)
  * [Database Migration](https://cloud.google.com/solutions/database-migration)
  * [Database Modernization](https://cloud.google.com/solutions/database-modernization)
  * [Databases for Games](https://cloud.google.com/solutions/databases/games)
  * [Google Cloud Databases](https://cloud.google.com/products/databases)
  * [Migrate Oracle workloads to Google Cloud](https://cloud.google.com/solutions/oracle)
  * [Open Source Databases](https://cloud.google.com/solutions/open-source-databases)
  * [SQL Server on Google Cloud](https://cloud.google.com/sql-server)
  * [Gemini for Databases](https://cloud.google.com/products/gemini/databases)
  * [Infrastructure Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Rapid Migration and Modernization Program (RaMP)](https://cloud.google.com/solutions/cloud-migration-program)
  * [Data Center Exits](https://cloud.google.com/solutions/data-center-migration)
  * [Application Modernization & Migration](https://cloud.google.com/solutions/application-migration)
  * [Database Modernization & Migration](https://cloud.google.com/products/databases)
  * [Cross-Cloud Networking](https://cloud.google.com/solutions/cross-cloud-network)
  * [High Performance Computing (HPC)](https://cloud.google.com/solutions/hpc)
  * [VMware](https://cloud.google.com/vmware-engine)
  * [SAP](https://cloud.google.com/solutions/sap)
  * [Windows](https://cloud.google.com/windows)
  * [Productivity and Collaboration](https://workspace.google.com/enterprise/)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security](https://cloud.google.com/solutions/security)
  * [Agentic SOC](https://cloud.google.com/solutions/agentic-soc)
  * [Web App and API Protection](https://cloud.google.com/security/solutions/web-app-and-api-protection)
  * [Security and Resilience Framework](https://cloud.google.com/security/solutions/security-and-resilience)
  * [Risk and compliance as code (RCaC)](https://cloud.google.com/solutions/risk-and-compliance-as-code)
  * [Software Supply Chain Security](https://cloud.google.com/security/solutions/software-supply-chain-security)
  * [Security Foundation](https://cloud.google.com/security/solutions/security-foundation)
  * [Google Cloud Cybershield™](https://cloud.google.com/security/solutions/secops-cybershield)
  * [Startups and SMB](https://cloud.google.com/solutions#section-13)
  * [Startup Program](https://cloud.google.com/startup)
  * [Small and Medium Business](https://cloud.google.com/solutions/smb)
  * [Software as a Service](https://cloud.google.com/saas)


  * Featured Products
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Cloud Run](https://cloud.google.com/run)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Looker](https://cloud.google.com/looker)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [See all products (100+)](https://cloud.google.com/products#featured-products)
  * [AI and Machine Learning](https://cloud.google.com/products/ai)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Model Garden](https://console.cloud.google.com/agent-platform/model-garden)
  * [Customer Experience Agent Studio](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)
  * [Agent Search](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)
  * [Speech-to-Text](https://cloud.google.com/speech-to-text)
  * [Text-to-Speech](https://cloud.google.com/text-to-speech)
  * [Translation AI](https://cloud.google.com/translate)
  * [Vision AI](https://cloud.google.com/vision)
  * [Contact Center as a Service](https://cloud.google.com/solutions/contact-center-ai-platform)
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)
  * Business Intelligence
  * [Looker](https://cloud.google.com/looker)
  * [Data Studio](https://cloud.google.com/data-studio)
  * [Compute](https://cloud.google.com/products/compute)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [App Engine](https://cloud.google.com/appengine)
  * [Cloud GPUs](https://cloud.google.com/gpu)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Spot VMs](https://cloud.google.com/spot-vms)
  * [Batch](https://cloud.google.com/batch)
  * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
  * [Bare Metal](https://cloud.google.com/bare-metal)
  * [Recommender](https://cloud.google.com/recommender/docs/whatis-activeassist)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)
  * [Containers](https://cloud.google.com/containers)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Deep Learning Containers](https://cloud.google.com/deep-learning-containers/docs)
  * [Knative](https://knative.dev/docs/)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Dataflow](https://cloud.google.com/products/dataflow)
  * [Looker](https://cloud.google.com/looker)
  * [Lakehouse](https://cloud.google.com/products/lakehouse)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Managed Service for Apache Kafka](https://cloud.google.com/products/managed-service-for-apache-kafka)
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)
  * [Databases](https://cloud.google.com/products/databases)
  * [AlloyDB for PostgreSQL](https://cloud.google.com/alloydb)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Firestore](https://cloud.google.com/firestore)
  * [Spanner](https://cloud.google.com/spanner)
  * [Bigtable](https://cloud.google.com/bigtable)
  * [Datastream](https://cloud.google.com/datastream)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Bare Metal Solution](https://cloud.google.com/bare-metal)
  * [Memorystore](https://cloud.google.com/memorystore)
  * [Developer Tools](https://cloud.google.com/products/tools)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Build](https://cloud.google.com/build)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs)
  * [Cloud SDK](https://cloud.google.com/sdk)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Cloud Source Repositories](https://cloud.google.com/source-repositories/docs)
  * [Infrastructure Manager](https://cloud.google.com/infrastructure-manager/docs)
  * [Cloud Workstations](https://cloud.google.com/workstations)
  * [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist)
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)
  * [Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * [Google Distributed Cloud Connected](https://cloud.google.com/distributed-cloud-connected)
  * [Google Distributed Cloud Air-gapped](https://cloud.google.com/distributed-cloud-air-gapped)
  * Hybrid and Multicloud
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Cloud Build](https://cloud.google.com/build)
  * [Observability](https://cloud.google.com/products/observability)
  * [Cloud Service Mesh](https://cloud.google.com/products/service-mesh)
  * [Google Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * Industry Specific
  * [Anti Money Laundering AI](https://cloud.google.com/anti-money-laundering-ai)
  * [Cloud Healthcare API](https://cloud.google.com/healthcare-api)
  * [Device Connect for Fitbit](https://cloud.google.com/device-connect)
  * [Telecom Network Automation](https://cloud.google.com/telecom-network-automation)
  * [Telecom Data Fabric](https://cloud.google.com/telecom-data-fabric)
  * [Telecom Subscriber Insights](https://cloud.google.com/telecom-subscriber-insights)
  * [Spectrum Access System (SAS)](https://cloud.google.com/products/spectrum-access-system)
  * [Integration Services](https://cloud.google.com/integration-services)
  * [Application Integration](https://cloud.google.com/application-integration)
  * [Workflows](https://cloud.google.com/workflows)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud Tasks](https://cloud.google.com/tasks/docs)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Cloud Data Fusion](https://cloud.google.com/data-fusion)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Eventarc](https://cloud.google.com/eventarc/docs)
  * [Management Tools](https://cloud.google.com/products/management)
  * [Cloud Shell](https://cloud.google.com/shell/docs)
  * [Cloud console](https://cloud.google.com/cloud-console)
  * [Cloud Endpoints](https://cloud.google.com/endpoints/docs)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Cloud APIs](https://cloud.google.com/apis)
  * [Service Catalog](https://cloud.google.com/service-catalog/docs)
  * [Cost Management](https://cloud.google.com/cost-management)
  * [Observability](https://cloud.google.com/products/observability)
  * [Carbon Footprint](https://cloud.google.com/carbon-footprint)
  * [Config Connector](https://cloud.google.com/config-connector/docs/overview)
  * [Active Assist](https://cloud.google.com/solutions/active-assist)
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)
  * [Maps and Geospatial](https://cloud.google.com/solutions/geospatial)
  * [Earth Engine](https://cloud.google.com/earth-engine)
  * [Google Maps Platform](https://mapsplatform.google.com)
  * Media Services
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [Live Stream API](https://cloud.google.com/livestream/docs)
  * [OpenCue](https://www.opencue.io/docs/getting-started/)
  * [Transcoder API](https://cloud.google.com/transcoder/docs)
  * [Video Stitcher API](https://cloud.google.com/video-stitcher/docs)
  * [Migration](https://cloud.google.com/products/cloud-migration)
  * [Migration Center](https://cloud.google.com/migration-center/docs)
  * [Application Migration](https://cloud.google.com/solutions/application-migration)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Cloud Foundation Toolkit](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program)
  * [Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/4.0/overview)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Networking](https://cloud.google.com/products/networking)
  * [Cloud Armor](https://cloud.google.com/security/products/armor)
  * [Cloud CDN and Media CDN](https://cloud.google.com/cdn)
  * [Cloud DNS](https://cloud.google.com/dns)
  * [Cloud Load Balancing](https://cloud.google.com/load-balancing)
  * [Cloud NAT](https://cloud.google.com/nat)
  * [Cloud Connectivity](https://cloud.google.com/hybrid-connectivity)
  * [Network Connectivity Center](https://cloud.google.com/network-connectivity-center)
  * [Network Intelligence Center](https://cloud.google.com/network-intelligence-center)
  * [Network Service Tiers](https://cloud.google.com/network-tiers)
  * [Virtual Private Cloud](https://cloud.google.com/vpc)
  * [Private Service Connect](https://cloud.google.com/private-service-connect)
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)
  * [Operations](https://cloud.google.com/products/operations)
  * [Cloud Logging](https://cloud.google.com/logging)
  * [Cloud Monitoring](https://cloud.google.com/monitoring)
  * [Error Reporting](https://cloud.google.com/error-reporting/docs/grouping-errors)
  * [Managed Service for Prometheus](https://cloud.google.com/managed-prometheus)
  * [Cloud Trace](https://cloud.google.com/trace/docs)
  * [Cloud Profiler](https://cloud.google.com/profiler/docs)
  * [Cloud Quotas](https://cloud.google.com/docs/quotas)
  * Productivity and Collaboration
  * [AppSheet](https://about.appsheet.com/home/)
  * [AppSheet Automation](https://cloud.google.com/appsheet/automation)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security and Identity](https://cloud.google.com/products/security-and-identity)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection)
  * [Mandiant Managed Defense](https://cloud.google.com/security/products/managed-defense)
  * [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence)
  * [Security Command Center](https://cloud.google.com/security/products/security-command-center)
  * [Cloud Key Management](https://cloud.google.com/security/products/security-key-management)
  * [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services)
  * [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/)
  * [Assured Workloads](https://cloud.google.com/security/products/assured-workloads)
  * [Google Security Operations](https://cloud.google.com/security/products/security-operations)
  * [Mandiant Consulting](https://cloud.google.com/security/consulting/mandiant-services)
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)
  * [Serverless](https://cloud.google.com/serverless)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Functions](https://cloud.google.com/functions)
  * [App Engine](https://cloud.google.com/appengine)
  * [Workflows](https://cloud.google.com/workflows)
  * [API Gateway](https://cloud.google.com/api-gateway/docs)
  * [Storage](https://cloud.google.com/products/storage)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [Block Storage](https://cloud.google.com/products/block-storage)
  * [Filestore](https://cloud.google.com/filestore)
  * [Persistent Disk](https://cloud.google.com/persistent-disk)
  * [Cloud Storage for Firebase](https://firebase.google.com/products/storage)
  * [Local SSD](https://cloud.google.com/products/local-ssd)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [Google Cloud Managed Lustre](https://cloud.google.com/products/managed-lustre)
  * [Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes)
  * [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery)
  * [Web3](https://cloud.google.com/web3)
  * [Blockchain Node Engine](https://cloud.google.com/blockchain-node-engine)
  * [Blockchain RPC](https://cloud.google.com/products/blockchain-rpc)


  * Save money with our transparent approach to pricing
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)
  * Pricing overview and tools
  * [Google Cloud pricing](https://cloud.google.com/pricing)
  * [Pricing calculator](https://cloud.google.com/products/calculator)
  * [Google Cloud free tier](https://cloud.google.com/free)
  * [Cost optimization framework](https://cloud.google.com/architecture/framework/cost-optimization)
  * [Cost management tools](https://cloud.google.com/cost-management)
  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)


  * Learn & build
  * [Google Cloud Free Program](https://cloud.google.com/free)
  * [Solution Generator](https://cloud.google.com/solution-generator)
  * [Quickstarts](https://cloud.google.com/docs/tutorials?doctype=quickstart)
  * [Blog](https://cloud.google.com/blog)
  * [Learning Hub](https://cloud.google.com/learn)
  * [Google Cloud certification](https://cloud.google.com/certification)
  * [Cloud computing basics](https://cloud.google.com/discover)
  * [Cloud Architecture Center](https://cloud.google.com/architecture)
  * Connect
  * [Innovators](https://cloud.google.com/innovators/innovatorsplus)
  * [Developer Center](https://cloud.google.com/developers)
  * [Events and webinars](https://cloud.google.com/events)
  * [Google Cloud Community](https://discuss.google.dev/c/google-cloud/14)
  * Consulting and Partners
  * [Google Cloud Consulting](https://cloud.google.com/consulting)
  * [Google Cloud Marketplace](https://cloud.google.com/marketplace)
  * [Find a partner](https://cloud.google.com/partners)
  * [Google Cloud partners](https://partners.cloud.google.com)


