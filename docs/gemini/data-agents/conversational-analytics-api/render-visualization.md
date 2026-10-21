---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-visualization/
title: Render an agent response as a visualization \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:36.719034+00:00
---

# Render an agent response as a visualization  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-visualization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Render an agent response as a visualization Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This guide assumes that you're working in an environment like Colaboratory. This guide also builds on the setup in [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk), which shows how to authenticate and initialize the required `client`, `inline_context`, and `messages` variables.

The [Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview) can generate interactive visualizations that are based on user questions. The API returns charts as either [Vega-Lite JSON](https://vega.github.io/vega-lite/) configurations or SVG images (for Looker data sources and only in the [`v1alpha` and `v1beta`](https://docs.cloud.google.com/gemini/data-agents/reference/rest) API versions). You can also instruct an agent to generate charts with specific requirements. The visualizations are created using the data results obtained in response to the user's question.

![A bar chart displays the total sale price and order count of pants for the age groups 20s-30s and 40s-50s in the state of California.](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-vis-bar-chart.png)

![An area chart displays the monthly total sales price performance for the last 12 months, with a peak of $3,395.12 and an average of $2,517.68.](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-vis-area-chart.png)

**Important:** SVG image options are available only for Looker data sources and only in the [`v1alpha` and `v1beta`](https://docs.cloud.google.com/gemini/data-agents/reference/rest) API versions.

## Supported visualizations

The API uses [Vega-Lite](https://vega.github.io/vega-lite/) to create visualizations and supports all standard Vega-Lite features. The following chart types are supported:

  * Area
  * Bar
  * Geoshape
  * Heatmap
  * Line (Time series)
  * Pie
  * Scatter



## How charts are generated

The agent identifies the relevant data result and passes it to a subagent. This subagent executes Python code to generate a Vega-Lite JSON configuration for the chart. The API uses the conversation context to better understand the user's intent when generating charts. By leveraging Python, the API can create more complex charts.

The agent might perform minor data transformations, such as aggregations or applying filters, to make the chart more relevant and readable.

## Output formats

The chart is returned in a `chart` result message and can be provided in the following formats:

  * [Vega-Lite JSON](https://vega.github.io/)
  * SVG image

**Important:** SVG image options are available only for Looker data sources and only in the [`v1alpha` and `v1beta`](https://docs.cloud.google.com/gemini/data-agents/reference/rest) API versions.

You can request images using the [`ChartOptions` field](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#chartoptions) in the context. When an image is requested, the API provides both the image and the Vega-Lite JSON output.

## Render an agent response as a visualization

This section demonstrates how to use the Python SDK to render a visualization from the chart specifications provided in a Conversational Analytics API response. The sample code extracts the chart specification (in Vega-Lite format) from the response's `chart` field and uses the [Altair](https://altair-viz.github.io/) library (which is built on Vega-Lite) to render the chart, save it as an image, and display it.

For more details on rendering charts with Vega-Lite and the Vega-Lite ecosystem, see [Tools for Authoring Vega-Lite Visualizations](https://vega.github.io/vega-lite/ecosystem.html).

### Example: Render a chart from Vega-Lite output

This example shows how to render a bar chart from a Conversational Analytics API agent response. The example sends a request with the following prompt:
    
    
    "Create a bar graph that shows the top five states by the total number of airports."
    

The sample code defines the following helper functions:

  * `render_chart_response`: Extracts the Vega-Lite configuration from the `chart` message, converts it to a format usable by the Altair library, renders the chart, saves it to `chart.png`, and displays it.
  * `chat`: Sends a request to the Conversational Analytics API using the `inline_context` variable and the current `messages` list, processes the streaming response, and if a chart is returned, calls `render_chart_response` to display it.



To use the following sample code, replace the following:

  * sqlgen-testing: The ID of your billing project that has the [required APIs enabled](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api).
  * Create a bar graph that shows the top five states by the total number of airports: The prompt that you want to send to the Conversational Analytics API.


    
    
    from google.cloud import geminidataanalytics
    from google.protobuf.json_format import MessageToDict
    import altair as alt
    import proto
    
    # Helper function for rendering chart response
    def render_chart_response(resp):
      def _convert(v):
        if isinstance(v, proto.marshal.collections.maps.MapComposite):
          return {k: _convert(val) for k, val in v.items()}
        elif isinstance(v, proto.marshal.collections.RepeatedComposite):
          return [_convert(el) for el in v]
        elif isinstance(v, (int, float, str, bool, type(None))):
          return v
        else:
          return MessageToDict(v)
    
      try:
        vega_config = _convert(resp.result.vega_config)
        chart = alt.Chart.from_dict(vega_config)
        chart.save('chart.png')
        chart.display()
        print("Chart rendered and saved as chart.png")
      except Exception as e:
        print(f"Error rendering chart: {e}")
    
    # Helper function for calling the API
    def chat(q: str, inline_context, messages):
      billing_project = "sqlgen-testing"
    
      input_message = geminidataanalytics.[Message](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Message.html)(
          user_message=geminidataanalytics.[UserMessage](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.UserMessage.html)(text=q)
      )
      messages.append(input_message)
    
      client = geminidataanalytics.[DataChatServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.html)()
      request = geminidataanalytics.[ChatRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ChatRequest.html)(
          inline_context=inline_context,
          parent=f"projects/{billing_project}/locations/global",
          messages=messages,
      )
    
      # Make the request
      try:
        stream = client.[chat](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.html)(request=request)
    
        for reply in stream:
          if reply.system_message and hasattr(reply.system_message, 'chart'):
            # ChartMessage includes `query` for generating a chart and `result` with the generated chart.
            if hasattr(reply.system_message.chart, 'result'):
              print("Chart result found in response.")
              render_chart_response(reply.system_message.chart)
            else:
              print("Chart message found, but no result yet.")
          # Append system messages to maintain context for follow-up turns
          if reply.system_message:
              messages.append(geminidataanalytics.[Message](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Message.html)(system_message=reply.system_message))
    
      except Exception as e:
        print(f"Error calling API: {e}")
    
    # Example Usage:
    # Assuming 'inline_context' and 'messages' are initialized as per "Build a data agent using the Python SDK"
    # Example initialization (replace with your actual context and message history):
    # inline_context = geminidataanalytics.InlineContext(...)
    # messages = []
    
    # Send the prompt to make a bar graph
    chat("Create a bar graph that shows the top five states by the total number of airports")
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
