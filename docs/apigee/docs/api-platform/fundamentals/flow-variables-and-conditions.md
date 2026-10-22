---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions/
title: Conditions with flow variables \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:17.850975+00:00
---

# Conditions with flow variables  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Conditions with flow variables Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Conditional statements are a common control structure in all programming languages. Like a programming language, API proxy configuration supports conditional statements for Flows, Policies, Steps, and RouteRules. By defining conditional statements, you define dynamic behavior for your API. This dynamic behavior lets you do things like converting XML into JSON only for mobile devices, or routing to a backend URL based on the content type or HTTP verb of the request message.

This topic shows you how to use conditions to dynamically apply API management features at runtime, without writing any code.

### Video

**Note:** This video was recorded with a previous version of the Apigee UI; however, the concepts are still valid. 

To learn more about flow variables and conditions, watch the following video:

## Configure conditional statements

Conditional behavior is implemented in API proxies by using a combination of _conditions_ and _variables_. A conditional statement is created using a Condition element. The following is an empty condition:
    
    
    <Condition></Condition>

To create a conditional statement, add a conditional operator and a variable using the following syntax:
    
    
    <Condition>VARIABLE_NAME OPERATOR "VALUE"</Condition>

For example:
    
    
    <Condition>request.verb = "GET"</Condition>

Supported conditional operators include `=` (equals), `!=` (not equal), and `>` (greater than). For readability, you can also write the conditionals as text: `equals`, `notequals`, `greaterthan`.

When working with URI paths you can use `~/` or `MatchesPath`. You can also match JavaRegex regular expressions with the `~~` operator.

Conditions are used to define API proxy conditional flows to backend API resources, described in Create conditional flows to backend API resources. For a complete list of conditionals, see [Conditions reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference).

### Variables

Conditions do their work by evaluating the values of _variables_. A variable is a property of an HTTP transaction executed by an API proxy, or a property of an API proxy configuration itself. Whenever an API proxy gets a request from an app, Apigee populates a long list of variables that are associated with things like system time, the app's network information, HTTP headers on messages, the API proxy configuration, policy executions and so on. This creates a rich context that you can use to set up conditional statements.

Variables always use a dotted notation. For example, HTTP headers on the request message are available as variables called `request.header.HEADER_NAME`. So to evaluate the `Content-type header`, you could use the variable `request.header.Content-type`. For example `request.header.Content-type = "application/json"` indicates that the content type of the request should be JSON.

Imagine that you need to create a conditional statement that will cause a policy to be enforced only when a request message is a `GET`. To create a condition that evaluates the HTTP verb of a request, you create the conditional statement below. The variable in this condition is `request.verb`. The value of the variable is `GET`. The operator is `=`.
    
    
    <Condition>request.verb = "GET"</Condition>

You could also use:
    
    
    <Condition>request.verb equals "GET"</Condition>

Apigee uses such a statement to evaluate conditions. The example above evaluates to true if the HTTP verb associated with the request is `GET`. If the HTTP verb associated with the request is `POST`, then the statement evaluates to false.

**Note:** Apigee automatically stores all HTTP headers and query parameters as variables that can be accessed using `request.header.` and `request.queryparam.` variable prefixes.

To enable dynamic behavior, you can attach Conditions to Flows, Steps, and RouteRules.

When you attach a condition to a Flow, you create a _conditional Flow_. Conditional flows execute only when the condition evaluates to true. You can attach as many Policies as you want to a conditional Flow. A conditional Flow enables you to craft highly specialized processing rules for request or response messages that meet certain criteria.

For example, to create a Flow that executes only when the request verb is a `GET`:
    
    
    <Flows>
      <Flow name="ExecuteForGETs">
      <Condition>request.verb="GET"</Condition>
      </Flow>
    </Flows>

To create one Flow for `GET` requests and another for `POST` requests:
    
    
    <Flows>
      <Flow name="ExecuteForGETs">
        <Condition>request.verb="GET"</Condition>
      </Flow>
      <Flow name="ExecuteForPOSTs">
        <Condition>request.verb="POST"</Condition>
      </Flow>
    </Flows>

As shown in the example below, you can apply the condition to the Policy Step itself. The following Condition causes the [VerifyAPIKey policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy) to be enforced only if a request message is a `POST`.
    
    
    <PreFlow name="PreFlow">
        <Request>
            <Step>
                <Condition>request.verb equals "POST"</Condition>
                <Name>VerifyApiKey</Name>
            </Step>
        </Request>
    </PreFlow>

Once you have defined such conditional Flows, you can attach Policies to them, enabling an API proxy to enforce one set of policies for `GET` requests, and another set of policies for `POST` requests.

For comprehensive reference information, see the following resources:

  * [Flow variables reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference)
  * [Conditions reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference)



### Example 1

The following example shows a single conditional flow named `Convert-for-devices`, configured in the ProxyEndpoint response flow. Add the Condition as an element to the entity to which the condition applies. In this example, the condition is a component of the flow. Therefore, the flow will execute whenever the statement evaluates to `true`.
    
    
    <Flows>
      <Flow name="Convert-for-devices">
      <Condition>(request.header.User-Agent = "Mozilla")</Condition>
        <Response>
          <Step><Name>ConvertToJSON</Name></Step>
        </Response>
      </Flow>
    </Flows>

For each request received from an app, Apigee stores the values of all HTTP headers present as variables. If the request contains an HTTP header called `User-Agent`, that header and its value are stored as a variable called `request.header.User-Agent`.

Given the ProxyEndpoint configuration above, Apigee checks the value of the `request.header.User-Agent` variable to see whether the condition evaluates to true.

If the condition does evaluate to `true`, that is, the value of the variable `request.header.User-Agent` equals `Mozilla`, then the conditional Flow executes and the [XMLtoJSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy) called `ConvertToJSON` is enforced. If not, the Flow is not executed, and the XML response is returned unmodified (in XML format) to the requesting app.

### Example 2

Let's use a specific example in which you need to transform response messages from XML to JSON—but only for mobile devices. First, create the policy that will convert the XML-formatted response from the Weather API into JSON:
    
    
    <XMLToJSON name="ConvertToJSON">
      <Options>
      </Options>
      <OutputVariable>response</OutputVariable>
      <Source>response</Source>
    </XMLToJSON>

The policy configuration above tells the API proxy to take the response message, perform a conversion from XML to JSON with default settings, and then write the result to the new response message. (If you are converting a _request_ message from XML to JSON, you simply set both of these values to `request`.)

**Tip:** The [XMLtoJSON policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/xml-json-policy) type defines a set of reasonable defaults, which means that you only need to add configuration elements to craft XML into specific JSON structures.

Since you want to convert responses from XML to JSON, you need to configure a conditional response Flow to perform the conversion. For example, to convert all responses from XML to JSON before they are returned to the client app, configure the following ProxyEndpoint response Flow.
    
    
    <Flows>
      <Flow name="Convert-for-devices">
        <Response>
          <Step><Name>ConvertToJSON</Name></Step>
        </Response>
      </Flow>
    </Flows>

When you invoke the API using the standard request, the response is formatted in JSON.

However, your goal is to only convert Weather reports into JSON _when the requesting client is a mobile device_. To enable such dynamic behavior, you must add a conditional statement to the Flow.

### Test the conditional flow

In this sample request, the HTTP `User-Agent` header is set to `Mozilla`, causing the conditional statement to evaluate to true and the conditional flow `Convert-for-devices` to execute.
    
    
    curl -H "User-Agent:Mozilla" http://example.com/weather/forecastrss?w=12797282

or, to pretty print where Python is available:
    
    
    curl -H "User-Agent:Mozilla" http://example.com/weather/forecastrss?w=12797282 | python -mjson.tool

Sample Response:
    
    
    . . .
    
    "yweather_forecast": [
       {
          "code": "11",
          "date": "12 Dec 2012",
          "day": "Wed",
          "high": "55",
          "low": "36",
          "text": "Showers"
        },
        {
          "code": "32",
          "date": "13 Dec 2012",
          "day": "Thu",
          "high": "56",
          "low": "38",
          "text": "Sunny"
        }
      ]
    }
    
    . . .

A request submitted without the `User-Agent` header, or with a different value than `Mozilla`, will result in an XML-formatted response.
    
    
    $ curl http://example.com/weather/forecastrss?w=12797282

The unmodified XML response is returned.

Sample Response:
    
    
    <yweather:forecast day="Wed" date="12 Dec 2012" low="36" high="55" text="Showers" code="11" /> <yweather:forecast day="Thu" date="13 Dec 2012" low="38" high="56" text="Sunny" code="32" />

## Pattern matching

This section describes how to use pattern matching with conditions in an Apigee flow.

### Further Reading

  * [Conditions reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/conditions-reference)
  * The ["condition-pattern-matching proxy"](https://github.com/apigee/api-platform-samples/tree/master/sample-proxies/condition-pattern-matching) in our api-platform-samples repository in GitHub



### Operators

This section describes how to use the following pattern matching operators in conditional statements:

  * `Matches` operator: Simple pattern matching
  * JavaRegex operator: Finer control over matching
  * `MatchesPath` operator: Path fragment matching



#### Matches

Let's look at the `Matches` or `~` conditional operator first. These two operators are the same — the English version, `Matches`, is considered to be a more readable option.

**Summary:** The `Matches` operator gives you two possibilities. Either match the string literally, or do a wildcard match with `*`. As you might expect, the wildcard matches zero or more characters. Let's see how this works.

**Note:** The `Matches` operator does not match regular expressions. If you want to use regular expression matching, use the [JavaRegex operator.](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-variables-and-conditions#javaregex)

The following XML shows a Step condition. It executes the SomePolicy policy when the condition evaluates to true. In this example, we test the variable `proxy.pathsuffix`, a built-in variable in Apigee that stores the path suffix of the request. Note, however, you can test the value of any flow variable that contains a string. So, in this case, if the base path of the incoming request is `/animals`, and the request is `/animals/cat`, then the path suffix is the literal string `/cat`.
    
    
    <PreFlow name="PreFlow">
      <Request>
        <Step>
          <Condition>(proxy.pathsuffix Matches "/cat")</Condition>
          <Name>SomePolicy</Name>
        </Step>
      </Request>
      <Response/>
    </PreFlow>

**Question:** What proxy path suffix will cause SomePolicy to execute? There's only one possibility.

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? Yes, because the proxy path suffix matches `/cat` exactly. It will not execute if the suffix is `/bat` or `/dog` or `/` or anything else.

Now, consider this conditional statement where we use the wildcard character `*`:
    
    
    <Condition>(proxy.pathsuffix Matches "/*at")</Condition>

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? Yes, because the wildcard matches any character, and `"/cat`" is a match.

**API Call:**

`GET http://example.com/matchtest/bat`

Does the policy execute? Yes, because the wildcard matches any character, `"/bat"` is a match.

**API Call:**

`GET http://example.com/matchtest/owl`

Does the policy execute? Certainly not — although the wildcard matches the `o`, the letters `wl` are not matched.

Now, lets move the wildcard to the end of the suffix:
    
    
    <Condition>(proxy.pathsuffix Matches "/cat*")</Condition>

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? Yes, because the wildcard matches zero or more of any characters.

**API Call:**

`GET http://example.com/matchtest/bat`

Does the policy execute? No, `/bat` is not a match.

**API call:**

`GET http://example.com/matchtest/cat123`

Does the policy execute? Yes, the wildcard matches zero or more of any characters, therefore `123` produces a match.

**API call:**

`GET http://example.com/matchtest/cat/bird/mouse`

Does the policy execute? Yes, because the wildcard matches zero or more of any characters, so `/bird/mouse` produces a match. Note how an expression like this can get you into trouble because it matches everything after the literal characters!

**Question: Is the`Matches` operator case sensitive?**

Yes. Assume you have a condition like this:
    
    
    <Condition>(proxy.pathsuffix Matches "/*At")</Condition>

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? No, the wildcard matches any letter (regardless of case), but the lowercase `a` does not match `A`.

**API call:**

`GET http://example.com/matchtest/bAt`

Does the policy execute? Yes, the case matches.

**Question: How do I escape characters with the`Matches` operator?**

Use the percent `%` character to escape reserved characters. For example:
    
    
    <Condition>(proxy.pathsuffix Matches "/c%*at")</Condition>

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? No, the `Matches` operator is looking for the literal string `c*at`. 

**API call:**

`GET http://example.com/matchtest/c*at`

**Question:Does the policy execute?**

Yes, this path, although a bit unusual, matches.

#### JavaRegex

As you can see, the `Matches` operator is great for simple situations. But you can use another operator, the JavaRegex or `~~` operator. These two are the same operator, except JavaRegex is considered to be more readable. It's called JavaRegex because it allows regular expression pattern matching, and Apigee follows the same rules as the classes in the [java.util.regex package](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html) in the Java language. The way the JavaRegex operator works is very different from the `Matches` operator, so it's important not to confuse the two!

**Note:** If you're used to doing Regex in Perl scripts, it's important to note that the JavaRegex operator in Apigee tests the **entire** subject string. For example, if the subject is `abc` and the regex is `[a-z]` , there is no match because `[a-z]` matches exactly _one_ alpha character. The expression `[a-z]+` would work, as would `[a-z]{3}`. This matching differs from the usual application of regular expressions in tools like Perl or grep or Apache's mod_rewrite. JavaRegex uses `java.util.regex.Pattern.matches(str)`, which is defined to return positive if the entire string (str) matches the pattern. The regex in Perl or mod_rewrite are applied to any part of the string. They return true if the pattern matches anywhere. See the example Matching arbitrary strings with JavaRegex.**Note:** This section is not intended to be a detailed introduction to regular expressions. The main intent is to illustrate a few simple examples, and highlight the difference between the `Matches` and JavaRegex operators. If you'd like to know more about regular expressions, many resources exist for you to explore. 

**Summary:** The JavaRegex operator lets you use regular expression syntax in conditional statements.

The following code shows a Step condition. It executes the SomePolicy policy if the condition evaluates to `true`. In this example, we test the variable `proxy.pathsuffix`, a built-in variable in Apigee that stores the path suffix of the request. If the base path of the incoming request is `/animals`, and the request is `/animals/cat`, then the path suffix is the literal string `/cat`.
    
    
        <PreFlow name="PreFlow">
            <Request>
                <Step>
                    <Condition>(proxy.pathsuffix JavaRegex "/cat")</Condition>
                    <Name>SomePolicy</Name>
                </Step>
            </Request>
            <Response/>
        </PreFlow>

**Note:** It's important to remember that the `proxy.pathsuffix` variable is a string that always starts with a slash (`/`) character, such as `/cat`. Therefore, if you're matching `/c*t`, you are matching the entire string, including the `/`. The `/` is not part of the regular expression construct. If you're matching some other kind of variable, like a `request.querystring` a `/` is not needed (unless the query parameter happens to start with a `/`).

**Question:** What proxy path suffix will cause SomePolicy to execute? Just like with the `Matches` operator, there's only one possibility in this case.

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? Yes, because the proxy path suffix matches `/cat` exactly. It will not execute if the suffix is `/bat` or `/dog` or anything else.

Now, let's create a regular expression using the `*` quantifier. This quantifier matches zero or more of the preceding characters.
    
    
    <Condition>(proxy.pathsuffix JavaRegex "/c*t")</Condition>

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? No! The `*` quantifier matches zero or more of the **preceding** **character** , which is a `c`.

**API Call:**

`GET http://example.com/matchtest/ccccct`

Does the policy execute? Yes, because the wildcard matches zero or more of the preceding character.

Next, we use the `?` quantifier, which matches the preceding character once, or not at all.
    
    
    <Condition>(proxy.pathsuffix JavaRegex "/ca?t")</Condition>

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? Yes. The `?` quantifier matches zero or one occurrence of the **preceding** character, which is an `a`.

**API Call:**

`GET http://example.com/matchtest/ct`

Does the policy execute? Yes. The `?` quantifier matches one **or none** of the preceding character. In this case, there is no `a` character, so the condition evaluates to `true`.

**API Call:**

`GET http://example.com/matchtest/caat`

Does the policy execute? No. The `?` quantifier matches **one** of the preceding character, which is an `a`.

Next, we use the `[abc]` or _grouping_ style of regex expression. It matches the characters `a` or `b` or `c`.
    
    
    <Condition>(proxy.pathsuffix JavaRegex "/[cbr]at")</Condition>

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? Yes. We're using regular expressions here, and the `[cbr]` expression matches a `c`, `b`, OR `r`. These calls are also matches:

`GET http://example.com/matchtest/bat`

`GET http://example.com/matchtest/rat`

But this is not a match:

`GET http://example.com/matchtest/mat`

**Question: Is the JavaRegex operator case sensitive?**

Yes. Assume you have a condition like this:
    
    
    <Condition>(proxy.pathsuffix JavaRegex "/ca?t")</Condition>

**API call:**

`GET http://example.com/matchtest/cat`

Does the policy execute? Yes, the regex matches zero or one of the preceding character, which is `a`.

**API call:**

`GET http://example.com/matchtest/cAt`

**Question: Does the policy execute?**

No, because the capital `A` does not match lowercase `a`.

#### MatchesPath

The `MatchesPath` operator can also be specified like this `~/`. It looks a little bit like the `Matches` (`~`) and the JavaRegex (`~~`) operators. But `MatchesPath` is entirely different.

Just remember that this operator looks at a path as a series of parts. Therefore, if the path is: `/animals/cats/wild`, you can think of the path as consisting of the parts `/animals`, `/cats`, and `/wild`.

The `MatchesPath` operator lets you use two wildcard notations: a single asterisk (*) and a double asterisk (`**`). The single asterisk matches one path element. The double asterisk matches one or many path elements.

Let's look at an example. In this example, we test the variable `proxy.pathsuffix`, a built-in variable in Apigee that stores the path suffix of the request. Note, however, you can test the value of any flow variable that contains a string.
    
    
        <PreFlow name="PreFlow">
            <Request>
                <Step>
                    <Condition>(proxy.pathsuffix MatchesPath "/animals/*")</Condition>
                    <Name>SomePolicy</Name>
                </Step>
            </Request>
            <Response/>
        </PreFlow>

**Question:** What proxy path suffix will cause SomePolicy to execute?

**API call:**

`GET http://example.com/matchtest/animals`

**Question: Does the policy execute?**

No, because condition requires another path element after `/animals`, as specified by `/*`.

**API call:**

`GET http://example.com/matchtest/animals`/

Does the policy execute? Yes, the path does have another path element (the part after `/animals/`), but it's just empty.

**API Call:**

`GET http://example.com/matchtest/animals/cats`

Does the policy execute? Yes, because the path clearly has an element (`/cats`) that comes after `/animals`

**API Call:**

`GET http://example.com/matchtest/animals/cats/wild`

**Question: Does the policy execute?**

No, because the single asterisk only matches one path element, and this API has more than one element after `/animals`.

Now let's use the double asterisk:
    
    
        <PreFlow name="PreFlow">
            <Request>
                <Step>
                    <Condition>(proxy.pathsuffix MatchesPath "/animals/**")</Condition>
                    <Name>SomePolicy</Name>
                </Step>
            </Request>
            <Response/>
        </PreFlow>

**Question:** What proxy path suffix will cause SomePolicy to execute?

**API call:**

`GET http://example.com/matchtest/animals`

Does the policy execute? No, because condition requires at least one following path element specified by `/**`.

**API call:**

`GET http://example.com/matchtest/animals`/

**Does the policy execute?**

Yes, the path does have another path element (the part after `/animals/`), but it's just empty.

**API Call:**

`GET http://example.com/matchtest/animals/cats`

**Does the policy execute?**

Yes, because the path has at least one element that comes after `/animals`

**API Call:**

`GET http://example.com/matchtest/animals/cats/wild`

**Does the policy execute?**

Yes, because the path has more than one element that comes after `/animals`

##### Mixing asterisks

You can use combinations of the single (*) and double (**) asterisk to further refine your path matching.
    
    
        <PreFlow name="PreFlow">
            <Request>
                <Step>
                    <Condition>(proxy.pathsuffix MatchesPath "/animals/*/wild/**")</Condition>
                    <Name>SomePolicy</Name>
                </Step>
            </Request>
            <Response/>
        </PreFlow>

**API call:**

All of these API calls will produce a match:

`GET http://example.com/matchtest/animals/cats/wild/`  
  
and

`GET http://example.com/matchtest/animals/dogs/wild/austrailian`  
  
and  
  
`GET http://example.com/matchtest/animals/birds/wild/american/finches`

### API resources

RESTful services are collections of _API resources_. An API resource is a URI path fragment that identifies some entity that developers can access by calling your API. For example, if your service provides weather reports and weather forecasts, your backend service might define two API resources:

  * `http://mygreatweatherforecast.com**/reports**`
  * `http://mygreatweatherforecast.com**/forecasts**`



### Further Reading

  * Check out this short video for an introduction to the relationship between your RESTful backend resources and Apigee proxy resources, or conditional flows.

  * [Build your first API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started)



When you create an API proxy (as shown in the [Build your first API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-started)), at a minimum you're creating an alias base URL that maps to your backend service. For example:

Backend base URL | New/equivalent API proxy URL  
---|---  
`http://mygreatweatherforecast.com` | `http://example.com/mygreatweatherforecast`  
  
At this point you can make API calls to your backend using either base URL. But when you use the API proxy URL, things start to get interesting.

In addition to API analytics that Apigee starts to collect when you use the API proxy, proxies also let you define conditional flows that map to the resources on your backend. In essence, _If a`GET` call comes into the `/reports` resource, Apigee should do something._

The following image shows the behavior difference between two URLs that ultimately access the same backend. One is the un-proxied resource URL, the other is an Apigee API proxy with a conditional flow to the same backend resource. We'll describe conditional flows in more detail below.

![For the Apigee API proxy URL with a conditional flow, the response converts XML to JSON
    and collects analytics.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/resource_conditional_flow3.png)

#### How API proxies map to specific backend resources

With an API proxy URL mapped to the base URL of the backend service (when you create the proxy), you can add conditional flows to specific resources, such as the `/reports` and `/forecasts` resources mentioned earlier.

Let's say you wanted to have Apigee _do something_ when calls come in to the `/reports` or `/forecasts` resources. At this point you're not telling Apigee _what_ to do, just that it should be listening for calls to those resources. You do this with conditions. In your Apigee API proxy, you can create conditional flows for `/reports` and `/forecasts`. For conceptual purposes, the following API proxy XML shows what those conditions might look like.
    
    
    <Flows>
        <Flow name="reports">
            <Description/>
            <Request/>
            <Response/>
            **< Condition>(proxy.pathsuffix MatchesPath "/reports") and (request.verb = "GET")</Condition>**
        </Flow>
        <Flow name="forecasts">
            <Description/>
            <Request/>
            <Response/>
            **< Condition>(proxy.pathsuffix MatchesPath "/forecasts") and (request.verb = "GET")</Condition>**
        </Flow>
    </Flows>

Those conditions say, _When a`GET` request comes in with `/reports` and `/forecasts` in the URL, Apigee will do whatever you (the API developer) tell it to, through the policies you attach to those flows._

Now here's an example of telling Apigee what to do when a condition is met. In the following API proxy XML, when a `GET` request is sent to `https://example.com/mygreatweatherforecast/reports`, Apigee executes the `XML-to-JSON-1` policy in the response.
    
    
    <Flows>
      <Flow name="reports">
        <Description/>
        <Request/>
        <Response>
          **< Step>
            <Name>XML-to-JSON-1</Name>
          </Step>**
        </Response>
      **< Condition>(proxy.pathsuffix MatchesPath "/reports") and (request.verb = "GET")</Condition>**
    </Flow>

In addition to those optional conditional flows, each API proxy also comes with two default flows: a `<PreFlow>` executed before your conditional flows, and a `<PostFlow>` executed after your conditional flows. Those are useful for executing policies when _any_ call is made to an API proxy. For example, if you want to verify an app's API key with every call, regardless of the backend resource being accessed, you could put a Verify API Key policy on the `<PreFlow>`. For more on flows, see [Configuring flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations).

## Create conditional flows to backend resources

Defining conditional flows to backend resources in an API proxy is completely optional. However, those conditional flows give you the ability to apply fine-grained management and monitoring.

You will be able to:

  * Apply management in way that reflects the semantics of your API model
  * Apply policies and scripted behavior to individual resource paths (URIs)
  * Collect fine-grained metrics for Analytics Services



For example, imagine that you need to apply different types of logic to your backend `/developers` to `/apps` resources.

To do so, you add two conditional flows in your API proxy: `/developers` and `/apps`.

To add a conditional flow:

  1. Select the **Develop** tab in the Proxy Editor.
  2. Select **Proxy endpoints > default** in the left-hand pane. 

![Select Proxy endpoints > default in the left-hand pane.](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/proxy-endpoints-default.png)

  3. Click the **+** button above the **Response** pane. 

![Add conditional flow button](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/add-flow-button.png)

  4. In the **Add Conditional Flow** dialog, enter the following configurations: 
     * **Flow name** : `Developers`
     * **Condition Type** : `Path`
     * **Path** : `/developers`

![Add conditional flow dialog.](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/flow-variables-add-conditional-flow.png)

The condition will be triggered (and policies will be executed) if a call is sent to the proxy with `/developers` at the end of the URI.

  5. Now add a conditional flow for `/apps`, and assume you want the condition to be triggered on both the URI and the `POST` verb in a request. The configuration involves setting the following: 
     * **Flow Name** : `Apps`
     * **Condition Type** : `Path and Verb`
     * **Path** : `/apps`
     * **Verb** : `POST`

The condition will be triggered (and policies will be executed) if a call is sent to the proxy with `/apps` at the end of the URI and a `POST` verb.




The added flows are displayed in the **Response** pane: 

![Add conditional flow dialog.](https://docs.cloud.google.com/static/apigee/docs/api-platform/fundamentals/images/developers-apps-flows.png)

Select one of the flows to view the conditional flow configuration in the API proxy editor code view:
    
    
    <Flow name="Apps">
        <Description>Developer apps registered in Developer Services</Description>
        <Request/>
        <Response/>
        <Condition>(proxy.pathsuffix MatchesPath "/apps") and (request.verb = "POST")</Condition>
    </Flow>

As you can see, API resources are simply conditional Flows that evaluate the URI path of the inbound request. (The `proxy.pathsuffix` variable identifies the URI of the request that follows the BasePath configured in the ProxyEndpoint configuration.)

Each API resource that you define is implemented by a conditional flow in the API proxy. (See [Configuring flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/flow-configurations).)

Once you deploy the API proxy to the test environment, the following request:
    
    
    http://example.com/PROXY_PATH/apps

will cause the condition to evaluate to `true`, and this flow, along with any associated policies, will execute.

The following example condition uses a Java regular expression to recognize calls made to the `/apps` resource with or without a trailing forward slash (`/apps` or `/apps/**`):
    
    
    <Condition>(proxy.pathsuffix JavaRegex "/apps(/?)") and (request.verb = "POST")</Condition>

For more about this type of condition, see [How to match regardless whether there is a trailing "/" ...](https://discuss.google.dev/t/how-to-match-regardless-whether-there-is-a-trailing-on-the-url-when-you-define-a-resource-in-api-proxy/8825.html) in the [Apigee Community](https://discuss.google.dev/).

## Modeling hierarchical URIs

In some cases, you will have hierarchical API resources. For example, the [Developer apps list API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/list) provides a method for listing all apps that belong to a developer. The URI path is:
    
    
    /developers/DEVELOPER_EMAIL/apps

You may have resources where a unique ID is generated for each entity in a collection, which is sometimes annotated as follows:
    
    
    /genus/:id/species

This path applies equally to the following two URIs:
    
    
    /genus/18904/species
    /genus/17908/species

To represent this structure in an API resource, you can use wildcards. For example:
    
    
    /developers/*/apps
    /developers/*example.com/apps
    /genus/*/species

These will resolve the hierarchical URIs as API resources appropriately.

In some cases, especially for deeply hierarchical APIs, you may simply want to resolve everything below a certain URI fragment. To do so, use a double asterisk wildcard in your resource definition. For example, if you define the following API resource:
    
    
    /developers/**

That API resource will resolve the following URI paths:
    
    
    /developers/DEVELOPER_EMAIL/apps
    /developers/DEVELOPER_EMAIL/keys
    /developers/DEVELOPER_EMAIL/apps/APP_ID/keys

Here's what the conditional flow condition would look like in the API proxy definition:
    
    
    <Condition>(proxy.pathsuffix MatchesPath "/developers/**") and (request.verb = "POST")</Condition>

## More examples

### Condition attached to RouteRule
    
    
    <RouteRule name="default">
      <!--this routing executes if the header indicates that this is an XML call. If true, the
        call is routed to the endpoint XMLTargetEndpoint-->
      <Condition>request.header.content-type = "text/xml"</Condition>
      <TargetEndpoint>XmlTargetEndpoint</TargetEndpoint>
    </RouteRule>

### Condition attached to a policy
    
    
    <Step>
      <!--the policy MaintenancePolicy only executes if the response status code is exactly 503 -->
      <Condition>response.status.code = 503</Condition>
      <Name>MaintenancePolicy</Name>
    </Step>

### Conditional Flow
    
    
    <!-- this entire flow is executed only if the request verb is a GET-->
    <Flow name="GetRequests">
      <Condition>request.verb="GET"</Condition>
      <Request>
        <Step>
    <!-- this policy only executes if request path includes a term like statues-->
    <Condition>request.path ~ "/statuses/**"</Condition>
          <Name>StatusesRequestPolicy</Name>
        </Step>
      </Request>
      <Response>
        <Step>
    <!-- this condition has multiple expressions. The policy executes if the response code status is exactly 503 or 400-->
    <Condition>(response.status.code = 503) or (response.status.code = 400)</Condition>
          <Name>MaintenancePolicy</Name>
        </Step>
      </Response>
    </Flow>

### Sample operators in conditions

Here are some examples of operators used to create conditions:

  * `request.header.content-type = text/xml`
  * `request.header.content-length < 4096 && request.verb = PUT`
  * `response.status.code = 404 || response.status.code = 500`
  * `request.uri MatchesPath /*/statuses/**`
  * `request.queryparam.q0 NotEquals 10`



### A practical example: Ignore `/` at the end of a path

Apigee developers commonly want to handle both of these path suffixes: `/cat` and `/cat/`. This is because some users or clients might call your API with the extra slash on the end of the path, and you need to be able to handle that in your conditional statements. This exact use case has been discussed in [how to match regardless whether there is a trailing '/' on the url...](https://discuss.google.dev/t/how-to-match-regardless-whether-there-is-a-trailing-on-the-url-when-you-define-a-resource-in-api-proxy/8825.html).

If you prefer, you can achieve this without using Regex like this:
    
    
        <PreFlow name="PreFlow">
            <Request>
                <Step>
                    <Condition>(proxy.pathsuffix = "/cat") OR (proxy.pathsuffix = "/cat/")</Condition>
                    <Name>SomePolicy</Name>
                </Step>
            </Request>
            <Response/>
        </PreFlow>

This is a good option. It is clear and readable.

You can do the same thing with Regex, however, like this. The parentheses are used to group the regex part of the statement, but they are not required.
    
    
    <Condition>(proxy.pathsuffix JavaRegex "/cat(/?)"</Condition>

**API Calls:**

`GET http://example.com/matchtest/cat`  
or `GET http://example.com/matchtest/cat`/

Does the policy execute? Yes. Note that in a regular expression, the `?` character means: match zero or one of the preceding character. Therefore, both `/cat` and `/cat/` are matches.

API Call:

`GET http://example.com/matchtest/cat/spotted`

Does the policy execute? No. The regular expression matches zero or only one occurrence of the preceding character, and nothing else is allowed.

### Matching arbitrary strings with JavaRegex

In all of the examples in this topic, we show how to match one of the built-in flow variables: `proxy.pathsuffix`. It's good to know that you can do pattern matching on any arbitrary string or flow variable, whether or not it's a built-in flow variable like `proxy.pathsuffix`. 

If for example you have a condition that tests an arbitrary string, perhaps a string returned in a backend payload, or a string returned from an authentication server lookup, you can use matching operators to test it. If you use `JavaRegex`, the regular expression will be compared against the entire subject string. If the subject is `abc` and the regular expression is `[a-z]`, there is no match, because `[a-z]` matches exactly **one** alpha character. The expression `[a-z]+` works, as does `[a-z]*`, and `[a-z]{3}`.

Let's look at a concrete example. Suppose the authentication server returns a list of roles as a comma-delimited string: `editor, author, guest`.

To test the presence of the editor role, this construction will not work, because `editor` is only part of the entire string.

`<Condition>returned_roles ~~ "editor"</Condition>`

However, this construction will work:

`<Condition>(returned_roles ~~ ".*\beditor\b.*")</Condition>`

It works because it takes into account word breaks and any other parts of the string with the `.*` prefix and suffix. 

In this example, you can also test for `editor` with the `Matches` operator:

`<Condition>(returned_roles ~~ "*editor*")</Condition>`

However, in cases where you need more precision, JavaRegex is often a better choice. 

### Escaping double quotes in JavaRegex expressions

The Condition syntax requires a JavaRegex expression to be wrapped in double quotes; therefore, if you have a regex expression that includes double quotes, you need an alternate way to match them. The answer is Unicode. For example, let's say you pass in a header that includes double quotes, like the following: 
    
    
     -H 'content-type:multipart/related; type="application/xop+xml"'

If you try to match that header in a regex condition, you will get an `Invalid Condition` error because the expression includes the double quotes: 
    
    
    request.header.Content-Type ~~ "(multipart\/related)(; *type="application\/xop\+xml\")"

The solution is to replace the ASCII-based double quotes with their Unicode equivalent, `\u0022`. For example, the following expression is valid and produces the expected result: 
    
    
    request.header.Content-Type ~~ "(multipart\/related)(; *type=\u0022application\/xop\+xml\u0022)"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
