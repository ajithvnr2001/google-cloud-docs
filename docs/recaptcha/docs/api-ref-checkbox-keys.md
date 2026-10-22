---
url: https://docs.cloud.google.com/recaptcha/docs/api-ref-checkbox-keys/
title: JavaScript API reference for reCAPTCHA \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:01.144902+00:00
---

# JavaScript API reference for reCAPTCHA  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/api-ref-checkbox-keys/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Reference ](https://docs.cloud.google.com/recaptcha/docs/apis)



Send feedback 

#  JavaScript API reference for reCAPTCHA Stay organized with collections  Save and categorize content based on your preferences. 

This page describes methods of the reCAPTCHA JavaScript API and their configuration parameters that you can use to render the web pages with a reCAPTCHA key (site key).

## reCAPTCHA JavaScript API methods

This section describes the syntax and parameters of reCAPTCHA JavaScript API methods.

### grecaptcha.enterprise.render

Renders the container as a reCAPTCHA widget and returns the ID of the newly created widget.

#### Syntax
    
    
    **grecaptcha.enterprise.render**(container: string | HTMLelement, parameters: Object): number

#### Method Parameters

Parameter | Description  
---|---  
container | The HTML element to render the reCAPTCHA widget. Specify either the ID of the container (string) or the DOM element itself.  
parameters |  An object containing parameters as key=value pairs, for example, `{"sitekey": "your_site_key", "action": "login", "theme": "dark"}`. See Attributes and parameters for details about each configurable parameter.  
  
#### Return value

Returns the ID of the newly created widget.

### grecaptcha.enterprise.reset

Resets the reCAPTCHA widget.

#### Syntax
    
    
    **grecaptcha.enterprise.reset**(widget_id: number): void

#### Parameters

Parameter | Description  
---|---  
widget_id | Optional. Widget ID returned from `grecaptcha.enterprise.render()`. If not specified, it defaults to the ID of the first widget that was created.   
  
#### Return value

Does not return a value.

### grecaptcha.enterprise.execute

Programmatically invokes the reCAPTCHA verification.

#### Syntax
    
    
    **grecaptcha.enterprise.execute**(widget_id: number): Promise<string>
    
    
    **grecaptcha.enterprise.execute**(sitekey: string, action: Object): Promise<string>

#### Parameters

Parameter | Description  
---|---  
widget_id | Optional. Widget ID returned from `grecaptcha.enterprise.render()`. If not specified, it defaults to the ID of the first widget that was created. **Note:** For use with checkbox site keys.  
sitekey |  Specify the reCAPTCHA site key to be protected. **Note:** For use with score-based site keys.  
action | An object with a single key=value pair, where the value for `action` key specifies the action name associated with the protected element. **Note:** For use with score-based site keys. For example: `{"action": "action_name"}`  
  
#### Return value

If successful, returns a Promise object containing the token if successful.

### grecaptcha.enterprise.ready

Runs your function when the reCAPTCHA JavaScript library loads.

#### Syntax
    
    
    **grecaptcha.enterprise.ready**(callback: function): void

#### Parameters

Parameter | Description  
---|---  
callback | The function to call when the reCAPTCHA library finishes loading.  
  
#### Return value

Does not return a value.

### grecaptcha.enterprise.getResponse

Gets the response for the reCAPTCHA widget.

#### Syntax
    
    
    **grecaptcha.enterprise.getResponse**(widget_id: number): string

#### Parameters

Parameter | Description  
---|---  
widget_id | Optional. Widget ID returned from `grecaptcha.enterprise.render()`. If not specified, it defaults to the ID of the first widget that was created.   
  
#### Return value

Gets the response of the reCAPTCHA widget. It can be either a string with the token created by `grecaptcha.enterprise.execute()` or an empty string if the token has not yet been created.

## Configuration

This section describes the JavaScript resource parameters and the parameters used by `grecaptcha.enterprise.render()` and attributes of the `g-recaptcha` widget.

### JavaScript resource (enterprise.js) parameters

The following table lists the parameters of the JavaScript resource (`enterprise.js`) that you must include when using reCAPTCHA.

For more information about using these parameters, see the examples in [ Rendering the reCAPTCHA widget on the frontend](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox). 

Parameter | Value | Description  
---|---|---  
`onload` | callback | Optional. The name of your callback function to be executed after all the dependencies have loaded.  
`render` | **`onload`** |  Optional, default value. Renders the widget in the first `g-recaptcha` tag it finds. **Note:** For use with checkbox site keys.  
`explicit` |  Optional. Does not render the widget automatically. You need to call `grecaptcha.enterprise.render()` to render it programmatically. **Note:** For use with checkbox site keys.   
siteKey |  When used with score-based site keys, this parameter is not optional. The value siteKey specifies the score-based site key associated. **Note:** For use with score-based site keys only; if used with checkbox site keys the script won't load.   
`hl` | See [language codes](https://docs.cloud.google.com/recaptcha/docs/language). | Optional. Forces the widget to render in a specific language. Auto-detects the user's language if unspecified.  
  
### g-recaptcha tag attributes and grecaptcha.enterprise.render() parameters

The following table lists the `g-recaptcha` tag attributes and the corresponding `grecaptcha.enterprise.render()` parameters.

`g-recaptcha` tag attribute | `grecaptcha.enterprise.render()` parameter | Allowed values | Default | Description  
---|---|---|---|---  
`data-sitekey` | `sitekey` |  |  | reCAPTCHA Key.  
`data-badge` | `badge` |  `bottomright`, `bottomleft`, `inline` | `bottomright` | Optional. Reposition the reCAPTCHA badge. `inline` lets you position it with CSS.  
`data-action` | `action` |  |  | Optional. String describing current [action](https://docs.cloud.google.com/recaptcha/docs/actions-website).  
`data-theme` | `theme` | `dark`, `light` | `light` | Optional. The color theme of the widget.  
`data-size` | `size` | `compact`, `normal` | `normal` | Optional. The size of the widget.  
`data-tabindex` | `tabindex` | Integer | 0 | Optional. The tabindex of the widget and challenge. If other elements in your page use tabindex, it should be set to make user navigation easier.  
`data-callback` | `callback` | String | N/A | Optional. The name of your callback function, executed when the user submits a successful response. The `g-recaptcha-response` token is passed to your callback.  
`data-expired-callback` | `expired-callback` | String | N/A | Optional. The name of your callback function, executed when the reCAPTCHA response expires and the user needs to re-verify.  
`data-error-callback` | `error-callback` | String | N/A | Optional. The name of your callback function, executed when reCAPTCHA encounters an error (usually network connectivity) and cannot continue until connectivity is restored. The callback does not receive any arguments containing error details. If you specify a function here, you are responsible for informing the user that they should retry.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
