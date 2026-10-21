---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/best-practices/
title: Best practices and patterns \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:59:00.409131+00:00
---

# Best practices and patterns  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Best practices and patterns Stay organized with collections  Save and categorize content based on your preferences. 

This guide shares proven best practices and design patterns to optimize and scale your agent application. This content can help you reduce design-time costs, reduce runtime costs, and improve agent reliability.

## General

This section provides general best practices for getting started with agent development and instruction writing.

### Start simple

When you first start building your agent application, you should start with simple use cases. Once you have simple use cases working, continue building more complicated use cases.

### Instructions should be specific

Agent instructions should be specific and unambiguous. Instructions should be well organized and grouped by topics. Avoid scattering instructions on specific topics in a haphazard manner. Instructions should be easy for a human to follow as well.

### Use structured instructions

Once you have finished writing your instructions, you should use the [restructure instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction#restructure) feature to format your instructions. In this format, your agent will be more reliable.

### Use modular components from multiple modalities and channels

When agents should respond in different ways for different modalities (text or voice) or channels (API, telephony, or web) you should use [modular components](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components) and [check for channel and modality in Python tools and callbacks](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/python#variable-_session).

## Tools

This section provides best practices for defining and using tools, including wrapping external APIs and chaining tool calls.

### Wrap APIs with Python tools

External API schemas may define many input and output parameters that are not relevant to your agent. If you use OpenAPI tools for cases like this, you might be providing unnecessary context to the model, which can reduce reliability. For example, suppose an OpenAPI spec tool takes 3 parameters as input and returns a large JSON object with 100 key/value pairs. The agent predicts the 3 input arguments for this tool, and when it returns, it sees the full JSON payload with all 100 key/value pairs. If only 3 of these pairs are actually relevant to the conversation, the other 97 pairs are irrelevant data adding tokens to the conversation history. While this may seem harmless, it could create unnecessary confusion for the agent, increase reasoning time, and increase latency.

It is a best practice to use Python tools to wrap API calls. Wrapping lets you obfuscate unnecessary data from the agent and the context history. You can control the exact context that the agent sees by only returning the data that is relevant to the agent at that point in time. This gives you complete control over the input and output parameters defined by the tool, which are shared with the model. This practice is a form of [Context Engineering](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/) with tools.

Sample code:
    
    
    def python_wrapper(arg_a: str, arg_b: str) -> dict:
      """
      Call the scheduling service to schedule an appointment,
      returning only relevant fields.
      """
      res = complicated_external_api_call(...)
      # Process result to extract only relevant key-value pairs.
      processed_res = {
          "appointment_time": res.json()["appointment_time"],
          "appointment_location": res.json()["appointment_location"],
          "confirmation_id": res.json()["confirmation_id"],
      }
      return processed_res
    

### Use tools and callbacks for deterministic behavior

In certain conversational scenarios, you may require more deterministic behavior from your agent application. In these cases, you should use tools or callbacks.

Callbacks are usually the best option for full deterministic control. Callbacks occur outside of the purview of the agent, so the agent is not involved in the execution of callbacks.

The internals of a tool are fully deterministic, but a tool call orchestrated by an agent is not deterministic. The agent decides to call a tool, prepares tool input arguments, and interprets tool results. Its possible for an agent to hallucinate this orchestration.

### Chaining tool calls

Similar to wrapping API calls with tools, If multiple tools need to be executed during a conversational turn, you should instruct the agent to call one tool and implement that tool to call the others. Alternatively, you could instruct the agent to call the first tool and define a `after_tool_callback` callback to call the remaining tools.

#### Bad pattern for chaining tool calls

It is considered a bad pattern to instruct the agent to call multiple tools during a conversational turn in order to accomplish a common goal.

The model has to predict every tool call and every parameter in that tool call. Then it has to ensure that it's predicting the tool calls _in order_ as well. This means you are relying heavily on the model (which is inherently non-deterministic) to perform a deterministic task.

For example, consider the following tool sequence:

  * `tool_1(arg_a, arg_b)` -> output `c`
  * `tool_2(arg_c)` -> output `d`
  * `tool_3(arg_d)` -> output `e`



If you define instructions for these three tool calls, you end up with a runtime sequence of events like the following:

  * User Input
  * Model -> Agent predicts `tool_1(arg_a, arg_b)`
  * `tool_1_response.json()` is returned
  * Agent interprets `tool_1_response.json()` and extracts `arg_c`
  * Model -> Agent predicts `tool_2(arg_c)`
  * `tool_2_response.json()` is returned
  * Agent interprets `tool_2_response.json()` and extracts `arg_d`
  * Model -> Agent predicts `tool_3(arg_d)`
  * `tool_3_response.json()` is returned
  * Model -> Agent provides final response



There are 4 model calls, 3 tool predictions, and 4 input arguments.

#### Good pattern for chaining tool calls

When you need to call multiple tools, it is considered a good pattern to instruct the agent to call a single tool, and to implement that tool to call the others.

The following tool calls three other tools:
    
    
    def python_wrapper(arg_a: str, arg_b: str) -> dict:
      """Makes some sequential API calls."""
      res1 = tools.tool_1({"arg_a": arg_a, "arg_b": arg_b})
      res2 = tools.tool_2(res1.json())
      res3 = tools.tool_3(res2.json())
    
      return res3.json()
    

Consider the sequence of events for a single tool call:

  * User Input
  * Model -> Agent predicts `python_wrapper(arg_a, arg_b)`
  * `python_wrapper_response.json()` is returned
  * Model -> Agent provides final response



This approach reduces tokens and reduces the probability of hallucination.

### Clear and distinct tool definitions

For tool definitions, the following best practices should be applied:

  * Different tools shouldn't have similar names. Make your tool names noticeably distinct from one another.
  * Tools that are not used should be removed from the agent node.
  * For parameter names, use snake case, use descriptive names, and avoid uncommon abbreviations.

Good examples: `first_name`, `phone_number`, `url`.

Bad examples: `i`, `arg1`, `fn`, `pnum`, `rqst`.

  * Parameters should use flattened structures rather than nested structures. The more nested a structure is, the more you are relying on the model to predict key/value pairs and their proper typing.




## Development workflow

This section provides best practices for team collaboration, version control, and testing during agent development.

### Define a development process for agent collaboration

When collaborating with a team on agent application development, you should define a development process. The following are examples of possible collaboration practices:

  * **Use third-party version control** : Use import and restore to synchronize changes with your third-party version control system. Agree on the process for synchronizing, reviewing, and merging. Define clear owners and clear steps to accept changes (for example, having evaluation results).
  * **Use built-in version control** : Setup a process to use the built-in version control. Agree on how to use snapshots for versioning. For example, you could require a snapshot when a milestone is reached (a set of evals passes), or before new feature development is done. Agree on process for synchronizing, reviewing, and merging changes.



### Use versions to save agent state

[Versions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/versions) allow you to memorialize work or changes you have completed within your agent application. After making changes to instructions, tools, variables and other items, you can save that state before any other changes are made. Versions are immutable snapshots in time of the agent. You should create a version when you are satisfied with some changes and the agent application is working as you've designed it, especially after validating changes with evaluations. Once you've created a version, you can always roll back to that version at any point in time.

You should create versions often, perhaps after every 10-15 major changes. Naming versions semantically is also helpful, and you should decide the naming convention to use with your development team. Examples include descriptive names like `pre-prod-instruction-changes` or `prod-ready-for-testing`. You can also use standards like [Semantic Versioning](https://semver.org/), using names like `v1.0.0`, `v1.0.1`, etc. Versions also have a description field that lets you add more details, similar to a commit message body. The version name and description should be short, meaningful, and easy to understand in case you need to roll back to that version.

### Perform end-to-end testing

Your agent application development process should include end-to-end testing to verify integrations with external systems.

## Evaluations

This section provides best practices for using evaluations to ensure agent reliability.

### Use evaluations

[Evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation) help keep your agents reliable. Use them to set the expectations on your agents and the APIs called by your agents.

## Session handling

This section provides patterns for managing the session lifecycle.

### Deterministic greetings and reduced latency with static responses

You can configure your agent to speak a deterministic response when a session starts. This approach can save model calls and tokens, and reduce latency.

Using the [before_model_callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/\(/gemini-enterprise-cx/cx-agent-studio/callback#before_model_callback\)) lets you intercept the incoming input, then respond with a static greeting message.
    
    
    def before_model_callback(
        callback_context: CallbackContext,
        llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      for part in callback_context.get_last_user_input():
        # Or other events or texts
        if part.text == "<event>session start</event>":
          return LlmResponse.from_parts(parts=[
              Part.from_text(text="Hello how can I help you today?")
          ])
      return None
    

### Respond quickly with prefix messages while the model is working

When a session begins, avoid forcing the user to wait for model generation. You can prefix responses so the agent can quickly deliver a friendly, branded greeting (for example, "Hello, I'm Gemini, your personal assistant"), while the model simultaneously processes the user's main request in the background.

This relies on the `partial = True` setting. Normally, a non-`FuctionCall` response is considered a terminal response. Using `partial = True` forces the agent to continue processing after the response.

In the following example, the agent application delivers the welcome message quickly and then continues processing the main request. This eliminates the awkward _typing_ pause, making the agent feel responsive.
    
    
    def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
      for part in callback_context.get_last_user_input():
        if part.text == "<event>session start</event>":
          response = LlmResponse.from_parts([Part.from_text("Hello, I'm Gemini, your personal AI assistant.")])
          response.partial = True
          return response
      return None
    

### Verify and enforce mandatory content

In some cases, you may want to instruct the agent to provide specific mandatory content (like a legal disclaimer) but also verify that the agent actually included it. This pattern lets you rely on the model's natural generation when it works, but enforce the content deterministically when it fails.

You can use an [`after_model_callback`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback#after_model_callback) to check the model's output. If the mandatory content is present, the callback returns `None` (letting the model's response pass through). If it is missing, the callback constructs a new response containing the mandatory content.

Sample variables:

Variable name | Default value  
---|---  
first_turn | True  
      
    
    DISCLAIMER = "THIS CONVERSATION MAY BE RECORDED FOR LEGAL PURPOSES."
    
    def after_model_callback(
        callback_context: CallbackContext,
        llm_response: LlmResponse
    ) -> Optional[LlmResponse]:
      if callback_context.variables.get("first_turn"):
        callback_context.variables["first_turn"] = False
    
        # Check if the agent's response already contains the disclaimer.
        # The agent might have produced it based on instructions.
        for part in callback_context.get_last_agent_output():
          if part.text and DISCLAIMER in part.text:
            return None
    
        # If the agent failed to produce the disclaimer, force it.
        return LlmResponse.from_parts(parts=[
            Part.from_text(DISCLAIMER),
            *llm_response.content.parts
        ])
    
      return None
    

### Call custom tool on session end

You can configure your agent to call a specific tool when a session ends. This can be useful for post-call wrap up events like synchronizing data on exit, sending data to an external API, backend task completion, or logging call metadata.

For example, suppose you have an existing tool like `post_call_logging` that you want to call just before the session ends:
    
    
    def post_call_logging(session_id: str) -> dict:
      """Logs the session ID to external API."""
      API_URL = "https://api.example.com"
      response = ces_requests.post(
        url=API_URL,
        data={"session_id": session_id}
      )
    
      return response.json()
    

You can use the [after_model_callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback#after_model_callback) to perform the following sequence:

  1. Check for the `end_session` tool call in the agent's response.
  2. Create the `post_call_logging` tool part.
  3. Insert the `post_call_logging` tool call _before_ the `end_session` tool call.



This ensures that the agent executes the logging tool before terminating the session.
    
    
    def after_model_callback(
        callback_context: CallbackContext,
        llm_response: LlmResponse
    ) -> Optional[LlmResponse]:
      for index, part in enumerate(llm_response.content.parts):
        if part.has_function_call('end_session'):
          # Add an additional "post_call_logging" function call before "end_session",
          # so the agent will execute the tool before ending the session.
          tool_call = Part.from_function_call(
              name="post_call_logging",
              args={"sessionId": callback_context.session_id}
          )
          return LlmResponse.from_parts(
              parts=llm_response.content.parts[:index] + [tool_call] + llm_response.content.parts[index:]
          )
      return None
    

### Using partial responses for real-time user interface updates

When an agent executes an action (for example, updating order status), there may be a delay as the model processes the final response. Using _partial responses_ lets you to send notifications to the client user interface when a tool finishes execution, decoupling the visual update from the model's text generation.

Your user interface can refresh status bars, trackers, or receipts in real-time.

This relies on the `partial = True` setting. Normally, a non-`FuctionCall` response is considered a terminal response. Using `partial = True` forces the agent to continue processing after the response.

The JSON payload won't be sent to the model. Thus the agent won't be aware of the existence of the payload during response generation.
    
    
    def before_model_callback(
        callback_context: CallbackContext,
        llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      if  llm_request.contents[-1].parts[-1].has_function_response('update_order'):
        order_state =  llm_request.contents[-1].parts[-1].function_response.response['result']['order_state']
        # Return a custom JSON payload before calling the model to generate the final agent response.
        response = LlmResponse.from_parts([Part.from_json(data=json.dumps(order_state))])
        response.partial = True
        return response
      return None
    

## Client-side integration

This section provides patterns for integrating with client-side applications.

### Using custom payloads to drive your user interface

Users expect a dynamic, interactive interface. You can use [custom payloads](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback#custom_payloads) to drive client-side rendering, bridging the gap between the agent and a polished application. Instead of delivering plain text options, configure your agent to detect specific patterns in a response (for example, a list of choices) and transform them into high conversion, interactive user interface elements, such as clickable chips or buttons.

Use an [`after_model_callback`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback#after_model_callback) to scan agent responses for specific triggers. For example, if the model output is: "Available options are: Refund, Track Order, Speak to Agent", the following callback intercepts and extracts those options as a JSON payload, which can be used for user interface rendering.
    
    
    import json
    
    def after_model_callback(
        callback_context: CallbackContext,
        llm_response: LlmResponse
    ) -> Optional[LlmResponse]:
      prefix = 'Available options are:'
      payload = {}
      for part in llm_response.content.parts:
        if part.text is not None and part.text.startswith(prefix):
          # Return available options as chip list
          payload['chips'] = part.text[len(prefix):].split(',')
          break
    
      new_parts = []
      # Keep the original agent response part, as the custom payload won't be sent
      # back to the model in the next turn.
      new_parts.extend(llm_response.content.parts)
      new_parts.append(Part.from_json(data=json.dumps(payload)))
      return LlmResponse.from_parts(parts=new_parts)
    

### Displaying Markdown and HTML

If your conversational interface supports Markdown and HTML for agent responses, you can use the [simulator](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/simulator) to test these responses, because the simulator also supports Markdown and HTML.

Example instructions:
    
    
    <role>
        You are a "Markdown Display Assistant," an AI agent designed to demonstrate
        various rich content formatting options like images, videos, and deep links
        using HTML-style markdown. Your purpose is to generate and display this
        content directly to the user based on their requests.
    </role>
    <persona>
        Your primary goal is to showcase the rich content rendering capabilities of
        the platform by generating HTML markdown for elements like images, videos,
        and hyperlinks. You are a helpful and direct assistant. When asked to show
        something, you generate the markdown for it and present it.
        You should not engage in conversations outside the scope of generating and
        displaying markdown. If the user asks for something unrelated, politely
        state that you can only help with displaying rich content. Adhere strictly
        to the defined constraints and task flow.
    </persona>
    <constraints>
        1.  **Scope Limitation:** Only handle requests related to displaying
            markdown content (images, videos, links, etc.). Do not answer general
            knowledge questions or perform other tasks.
        2.  **Tool Interaction Protocol:** You must use the \`display_markdown\`
            tool to generate the formatted content string.
        3.  **Direct Output:** Your final response to the user must be the raw
            markdown string returned by the \`display_markdown\` tool. Do not add
            any conversational text around it unless the tool returns an error.
            For example, if the tool returns \`"<img src='...'>"\`, your response
            should be exactly \`"<img src='...'>"\`.
        4.  **Clarity and Defaults:** If a user's request is vague (e.g., "show me
            an image"), use the tool's default values to generate a response. There
            is no need to ask for clarification.
        5.  **Error Handling:** If the tool call fails or returns an error, inform
            the user about the issue in a conversational manner.
    </constraints>
    <taskflow>
        These define the conversational subtasks that you can take. Each subtask
        has a sequence of steps that should be taken in order.
        <subtask name="Generate and Display Markdown">
            <step name="Parse Request and Call Tool">
                <trigger>
                    User initiates a request to see any form of rich content (image,
                    video, link, etc.).
                </trigger>
                <action>
                    1.  Identify the types of content the user wants to see (e.g.,
                        image, video, deep link).
                    2.  Call the \`display_markdown\` tool. Set the corresponding
                        boolean arguments to \`True\` based on the user's request.
                        For example, if the user asks for a video and a link, call
                        \`display_markdown(show_video=True, show_deep_link=True)\`.
                    3.  If the user makes a general request like "show me something
                        cool", you can enable all flags.
                </action>
            </step>
            <step name="Output Tool Response">
                <trigger>
                    The \`display_markdown\` tool returns a successful response
                    containing a \`markdown_string\`.
                </trigger>
                <action>
                    1.  Extract the value of the \`markdown_string\` key from the
                        tool's output.
                    2.  Use this value as your direct and final response to the
                        user, without any additional text or formatting.
                </action>
            </step>
        </subtask>
    </taskflow>
    

Sample python tool:
    
    
    from typing import Any
    
    def display_markdown(show_image: bool, show_video: bool, show_deep_link: bool) -> dict[str, Any]:
        """
        Constructs a markdown string containing HTML for various rich media elements.
    
        This function generates an HTML-formatted string based on the boolean flags provided.
        It can include an image, a video, and a hyperlink (deep link). The content for
        these elements is pre-defined.
    
        Args:
            show_image (bool): If True, an <img> tag will be included in the output.
            show_video (bool): If True, a <video> tag will be included in the output.
            show_deep_link (bool): If True, an <a> tag will be included in the output.
    
        Returns:
            dict[str, Any]: A dictionary with a single key 'markdown_string' containing the
                            generated HTML markdown. If no flags are set, it returns a
                            message indicating nothing was requested.
        """
        # MOCK: This is a mock implementation. It does not fetch any dynamic content.
        # It assembles a markdown string from hardcoded HTML snippets to demonstrate
        # the agent's ability to render rich content.
    
        markdown_parts = []
    
        if show_image:
            image_html = "This is a sample image:\n<img src='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png' alt='Google Logo' width='272' height='92' />"
            markdown_parts.append(image_html)
    
        if show_video:
            video_html = "This is a sample video:\n<video controls width='320' height='240'><source src='https://www.w3schools.com/html/mov_bbb.mp4' type='video/mp4'>Sorry, your browser does not support embedded videos.</video>"
            markdown_parts.append(video_html)
    
        if show_deep_link:
            link_html = "This is a sample deep link:\n<a href='https://www.google.com'>Click here to go to Google</a>"
            markdown_parts.append(link_html)
    
        if not markdown_parts:
            return {"markdown_string": "You did not request any content to be displayed. Please specify if you want to see an image, video, or link."}
    
        return {"markdown_string": "\n\n".join(markdown_parts)}
    

## Voice and audio channel controls

This section provides patterns for controlling the voice and audio channel, including prerecorded audio, hold music, and barge-in settings.

Notes:

  * Linear16, mulaw and alaw audio encoding are supported as the audio file.
  * If using a Cloud Storage bucket that belongs to a different cloud project, The Customer Engagement Suite Service Account `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com` must be explicitly granted with `storage.objects.get` permission to the target Cloud Storage bucket.
  * You can use the `interruptable` input argument to configure whether the prerecorded audio can be interrupted by the end user.
  * For music playback, you can use the `cancellable` input argument to indicate that music playback should cease when a new response is generated by the agent.



### Play a brand-specific prerecorded audio

You can configure your agent to play a prerecorded audio file before processing the user request. You can use this for brand-approved greetings or mandatory legal disclosures at session start.

Use `"transcript": "yyy"` to provide the agent with the audio playback text, ensuring it has the necessary context to generate following responses.

Use `"interrupable": false` ensures that the user cannot interrupt the audio playback.
    
    
    def before_model_callback(
        callback_context: CallbackContext,
        llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      for part in callback_context.get_last_user_input():
        if part.text == "<event>session start</event>":
          return LlmResponse.from_parts(parts=[
              Part.from_json(data='{"audioUri": "gs://path/to/audio/file", "transcript": "transcript for the audio file", "interruptable": false}')
          ])
      return None
    

### Play prerecorded music when executing slow tools (no barge-in)

You can configure the agent to play music while a slow, "blocking" tool (such as account validation and activation) is running. The music automatically stops once the tool completes its execution. Users are unable to interact with the agent while the music is playing.
    
    
    def after_model_callback(
        callback_context: CallbackContext,
        llm_response: LlmResponse
    ) -> Optional[LlmResponse]:
      for index, part in enumerate(llm_response.content.parts):
        if part.has_function_call("slow_tool"):
          play_music = Part.from_json(
              data='{"audioUri": "gs://path/to/music/file", "cancellable": true}'
          )
          return LlmResponse.from_parts(
              parts=llm_response.content.parts[:index] +
              [play_music] + llm_response.content.parts[index:]
          )
      return None
    

### Play prerecorded music when executing asynchronous tools (allow barge-in)

You can configure an agent to play music while executing a tool asynchronously, such as during user account validation and activation. The music terminates automatically upon the completion of the asynchronous tool, provided the user has not already interrupted it. End users maintain the ability to interrupt the music at any time to continue their engagement with the agent.
    
    
    def before_model_callback(
        callback_context: CallbackContext,
        llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      for part in llm_request.contents[-1].parts:
        if part.has_function_response("async_tool"):
          text = Part.from_text(text="I'm submitting your order, it may take a while.")
          music = Part.from_json(
              data='{"audioUri": "gs://path/to/music/file", "cancellable": true}'
          )
          return LlmResponse.from_parts(parts=[text, music])
      return None
    

### Disallow user barge-in for certain responses

You can disallow the user from interrupting the agent when the agent is reading out important information (like a legal disclaimer), but allow barge-in for the remaining part of the agent response.

This uses the [`customize_response`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/system#customize_response) system tool.

You can implement this behavior in two ways, depending on whether you want a deterministic outcome:

  1. **Callback (Deterministic):** Force the response from a callback, as shown in the sample.
  2. **Instructions (Agent driven):** Prompt the agent to use the `customize_response` tool in its instructions.


    
    
    def before_model_callback(
        callback_context: CallbackContext,
        llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      for part in callback_context.get_last_user_input():
        if part.text == "<event>session start</event>":
          return LlmResponse.from_parts(parts=[
              Part.from_customized_response(
                  content=("Hello, I'm Gemini. Please listen to the following legal "
                           "disclaimer: <LEGAL_DISCLAIMER>"),
                  disable_barge_in=True
              ),
              Part.from_text("How can I help you today?")
          ])
      return None
    

### Custom response for no-input

When an agent times out waiting for input (see **Silence timeout** in [agent application settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#agent-application-settings)), a generative response is used by default. However, you can check whether input was received by the user in a before model callback and conditionally provide a response.
    
    
    def before_model_callback(
        callback_context: CallbackContext,
        llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      for part in callback_context.get_last_user_input():
        if part.text:
          if "no user activity detected" in part.text:
            return LlmResponse.from_parts(parts=[
                Part.from_text(text="Hi, are you still there?")
            ])
    
      return None
    

## Error handling

This section provides patterns for handling tool errors.

### Transfer to another agent on tool failures

When a specific tool execution fails, you can deterministically hand over to another agent to handle the conversation. This is a critical safety net for protecting the user experience during runtime errors.
    
    
    def before_model_callback(
        callback_context: CallbackContext,
        llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      for part in llm_request.contents[-1].parts:
        if (part.has_function_response('authentication') and
            'error' in part.function_response.response['result']):
          return LlmResponse.from_parts(parts=[
              Part.from_text('Sorry something went wrong, let me transfer you to another agent.'),
              Part.from_agent_transfer(agent='escalation agent')
          ])
      return None
    

### Gracefully terminate the session on tool failures

When a specific tool execution fails, you can terminate the session gracefully. This can prevent infinite loops and confusing responses when critical tool failures occur.

Sample callback:
    
    
    def before_model_callback(
        callback_context: CallbackContext,
        llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      for part in llm_request.contents[-1].parts:
        if (part.has_function_response('authentication') and
            'error' in part.function_response.response['result']):
          return LlmResponse.from_parts(parts=[
              Part.from_text('Sorry something went wrong, please call back later.'),
              Part.from_end_session(reason='Failure during user authentication.')
          ])
      return None
    

## Context and variables

This section provides patterns for using context variables.

### Pass context variables to OpenAPI tools

Personalized AI requires tools to access user session data. Relying on the model to manually recall and pass important details like session IDs or user variables is inherently unreliable and slow. Instead, the agent can pass specific context variables to OpenAPI tools. You can use `x-ces-session-context` to indicate that the value does not need to be produced by the model (and the schema of which is invisible to the model), but rather comes from context variables.

The following table lists the available values:

Value | Description  
---|---  
`$context.project_id` | The Google Cloud project ID.  
`$context.project_number` | The Google Cloud project number.  
`$context.location` | The location (region) of the agent.  
`$context.app_id` | The agent application ID.  
`$context.session_id` | The unique identifier for the session.  
`$context.variables` | All context variable values as an object.  
`$context.variables.variable_name` | The value of a specific context variable. Replace `variable_name` with the name of the variable.  
      
    
    openapi: 3.0.0
    info:
      title: test-title
      description: test-description
      version: 1.0.0
    paths:
      /test-path/{session_id}:
        post:
          parameters:
          - name: session_id
            in: path
            description: The session ID.
            required: true
            schema:
              type: string
            x-ces-session-context: $context.session_id
          - name: test_variable
            in: query
            description: Specific session variable.
            required: true
            schema:
              type: string
            x-ces-session-context: $context.variables.test_variable
          requestBody:
            description: test-description
            required: true
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/SessionParams'
          responses:
            '200':
              description: test-response-description
              content:
                application/json:
                 schema:
                    type: object
                    properties:
                      result:
                        type: string
    components:
      schemas:
        SessionParams:
          type: object
          description: all context variables
          x-ces-session-context: $context.variables
    

### Dynamic prompts

You can build agents that have dynamic prompts sent to the model by using:

  * [Variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/variable) that can be used to control prompt variations.
  * [Instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction) that include references to variables.
  * A [tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool) that can update the variables based on conversation details.
  * A [before_model_callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/callback#before_model_callback).



For example, you can alter the agent instructions based on whether the user is a lawyer or a pirate:

Variables:

Variable name | Default value  
---|---  
current_instructions | You are Gemini and you work for Google.  
lawyer_instructions | You are a lawyer and your job is to tell dad joke style jokes but with a lawyer edge.  
pirate_instructions | You are a pirate and your job is to tell a joke as a pirate.  
username | Unknown  
  
Instructions:
    
    
    The current user is: {username}
    You can use {@TOOL: update_username} to update the user's name if they provide
    it.
    
    Follow the current instruction set below exactly.
    
    {current_instructions}
    

Python tool:
    
    
    from typing import Optional
    
    def update_username(username: str) -> Optional[str]:
      """Updates the current user's name."""
      set_variable("username", username)
    

Callback:
    
    
    def before_model_callback(
      callback_context: CallbackContext,
      llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
      username = callback_context.get_variable("username", None)
    
      if username == "Jenn":
        new_instructions = callback_context.get_variable("pirate_instructions")
    
      elif username == "Gary":
        new_instructions = callback_context.get_variable("lawyer_instructions")
    
      callback_context.set_variable("current_instructions", new_instructions)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
