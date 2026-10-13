---
url: https://docs.cloud.google.com/looker/docs/troubleshooting-gemini/
title: Troubleshooting Gemini in Looker issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:40.994625+00:00
---

# Troubleshooting Gemini in Looker issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/troubleshooting-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Troubleshooting Gemini in Looker issues Stay organized with collections  Save and categorize content based on your preferences. 

Gemini in Looker represents a series of features in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio that provides generative AI-powered assistance to help you analyze and gain valuable insights from your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This page describes the following topics as they relate to [Gemini in Looker features](https://docs.cloud.google.com/looker/docs/gemini-overview-looker):

  * Known limitations, troubleshooting, and tips for writing better prompts for each task that is supported by Gemini in Looker
  * Troubleshooting that is related to Gemini in Looker enablement
  * How to submit in-product feedback about Gemini in Looker tasks
  * How to get support
  * Related resources



## Troubleshooting resources

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

### Gemini in Looker resources and troubleshooting

Task performed with Gemini assistance | Available platforms | Limitations of Gemini assistance | Troubleshooting Gemini in Looker tasks | Sample Gemini prompts  
---|---|---|---|---  
[Query data in natural language with Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) | Looker (original)Looker (Google Cloud core) | [Limitations on visualizations](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#limitations-on-visualizations)[Data source-specific limitations](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#limitations_on_data_sources)[Supported questions](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#limitations-on-questions) | [User and platform requirements](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup)[Setting up a data source](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-a-conversation) |   
[Write LookML using natural language](https://docs.cloud.google.com/looker/docs/write-lookml-gemini) | Looker (original)Looker (Google Cloud core) |  | [Tips for using Gemini in the Looker IDE](https://docs.cloud.google.com/looker/docs/write-lookml-gemini#tips)[User and platform requirements](https://docs.cloud.google.com/looker/docs/write-lookml-gemini#before_you_begin) | [Sample prompt: Create a dimension based on longitude or latitude](https://docs.cloud.google.com/looker/docs/write-lookml-gemini#create-dimension)[Sample prompt: Create a measure for today's total sales](https://docs.cloud.google.com/looker/docs/write-lookml-gemini#create-measure)  
[Create custom Looker visualizations using natural language](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini) | Looker (original)Looker (Google Cloud core) | Visualization Assistant is available only for HighCharts-based visualizations. | [Creating successful prompts](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini#creating_successful_prompts)[User and platform requirements](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini#before_you_begin) | [Sample prompts](https://docs.cloud.google.com/looker/docs/custom-looker-visualization-gemini#sample_prompts)  
  
### Gemini in Looker enablement troubleshooting

Platform | Platform requirements to enable Gemini in Looker | Permissions required to enable Gemini in Looker | Troubleshooting  
---|---|---|---  
[Looker (original)](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) | The instance must be Looker-hosted.The instance must be on Looker 25.0 or later to enable Gemini in Looker.The instance must be on Looker 25.6 or later to use Conversational Analytics. The instance must be on Looker 25.16 or later to manage and use Conversational Analytics data agents that use a Looker Explore as a data source.We recommend that instances participating in [Extended Support Release Program](https://docs.cloud.google.com/looker/docs/standard-extended-support-release-program-overview) are on Looker 25.6 or later to use Conversational Analytics. | [Looker Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) | Gemini in Looker supports English-language prompts and responses only.Make sure that the required permissions are assigned to the appropriate users. Only the Gemini in Looker roles and permissions that apply to the Conversational Analytics API [can be assigned to embed users](https://docs.cloud.google.com/looker/docs/signed-embedding#permissions).  
[Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) |  | [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project in which the instance resides | Make sure that the Trusted Testers settings are enabled.Gemini in Looker supports English-language prompts and responses only.Make sure that the required permissions are assigned to the appropriate users. Only the Gemini in Looker roles and permissions that apply to the Conversational Analytics API [can be assigned to embed users](https://docs.cloud.google.com/looker/docs/signed-embedding#permissions) or users of an Embed Looker (Google Cloud core) edition instance.  
  
## How to submit in-product feedback

Submit in-product feedback to rate the quality and accuracy of Gemini in Looker previews.

You can submit in-product feedback about each Gemini in Looker task by using the thumb_up thumbs-up and thumb_down thumbs-down icons.

## How to get support

Reach out to Support if you encounter any of the following issues:

  * Gemini in Looker features are slow to respond or generate content.
  * Gemini in Looker features return blank or empty responses.
  * The instance, report, or chart returns a timeout error.
  * The instance or page returns an internal server error.



Be sure to include a clear description of the problem and the expected behavior, the steps that you took prior to encountering the issue, and any additional relevant details.

For details on how to contact Support, see the documentation for your Looker platform type:

  * [Looker (original)](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details)
  * [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-support)



## Related resources

  * [Write better prompts for Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/write-prompts)
  * [Gemini for Google Cloud limitations](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai#gemini-limitations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
