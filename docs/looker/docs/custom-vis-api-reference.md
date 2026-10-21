---
url: https://docs.cloud.google.com/looker/docs/custom-vis-api-reference/
title: Custom visualization API 2.0 reference \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:21:16.192777+00:00
---

# Custom visualization API 2.0 reference  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/custom-vis-api-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Custom visualization API 2.0 reference Stay organized with collections  Save and categorize content based on your preferences. 

A call to the `looker.plugins.visualizations.add` function is the entry point into the Visualization API. This function accepts a _visualization object_ that fully defines your custom visualization.

Here's an example visualization:
    
    
    looker.plugins.visualizations.add({
        create: function(element, config){
            element.innerHTML = "<h1>Ready to render!</h1>";
        },
        updateAsync: function(data, element, config, queryResponse, details, doneRendering){
            var html = "";
            for(var row of data) {
                var cell = row[queryResponse.fields.dimensions[0].name];
                html += LookerCharts.Utils.htmlForCell(cell);
            }
            element.innerHTML = html;
            doneRendering()
        }
    });
    

## Environment

Since the Visualization API is plain JavaScript, you can use any JavaScript libraries to visualize your data.

Your JavaScript code will run in a sandboxed iframe, separate from your Looker instance. All the same, authors of custom visualizations are responsible for ensuring that the code they write is secure.

Just like all web development, supporting different web browsers (Chrome, Edge, Firefox) can occasionally be an issue. The Visualization API works on all browsers that Looker supports, but it's up to you to ensure browser support for your custom code. For example, uses of ES6 such as `let` or `()=>` will work in most browsers but may cause failures in IE11 or when rendering PDFs by using PhantomJS.

## Installation

You install custom visualizations by defining a manifest with the Admin > Platform > Visualizations form. A manifest consists of a unique string ID, a human-readable label, the URI of your visualization, and links to any dependencies that you require (ex: d3, jQuery, underscore).

Custom visualizations should be served as HTTPS content externally to Looker. If you're migrating from the first version of the custom visualization API, you may have files in your `looker/plugins/visualizations` directory. This location is still accessible, and a relative path to your visualization can be supplied, but we recommend that you migrate your content to a different location. Since the /plugins directory is not in the Shared File System, clustered environments won't have access to your visualization files on all nodes.

## The visualization object

The visualization object uses the following required, optional, and added properties.

### Required properties

  * `create` _function_

This function is called once, when your visualization is first drawn on the page. It's expected to set up anything that you'd like your visualization to always have available. You could load a library or create a set of elements and controls that you'll use later.

See details about the `create` function →

  * `updateAsync` / `update` _function_

This function is called every time the state of your visualization may need to change. It will always be called after `create`, and may be called many times, so it should be as fast as possible.

This function can be called for many reasons, but usually it's when the query to visualize was changed, a configuration option was changed, or the visualization was resized.

This function has a synchronous and asynchronous version :emdash; you'll only need to specify one. (It's an error to define both.) The async method is more reliable for PDF rendering because of the nature of iframes.

See details about these `update` functions →




### Optional properties

  * `options` _object_

An object that details options that users can set on your visualization.

See details about exposing a configuration UI →

  * `destroy` _function_ _Not yet implemented in API V2_

A function that's called just before the visualization is removed from the page. Use this function to clean up any event listeners or other states. It may never be called if, for example, the user closes the window.




### Added properties

Looker adds the following properties to your object automatically after the visualization is passed to `looker.plugins.visualizations.add`. You can reference them by using `this` within the context of the `create`, `update`, `updateAsync`, and `destroy` functions.

  * `addError` _function_

A function that your visualization code may call to tell the UI to display an error message instead of the visualization. It takes an `error` object.

Once an error is added, it will remain visible until `clearErrors` is called.

**Example:**
        
        this.addError({
            title: "Two Dimensions Required",
            message: "This really great visualization requires two dimensions."
        });
        

  * `clearErrors` _function_

A function that your visualization code may call to clear any errors that were added by using `addError`.

**Example:**
        
        this.clearErrors();
        

  * `trigger` _function_

A function that can be called to trigger an event outside the visualization.

See details about events →

**Example:**
        
        this.trigger("limit", [20]);
        




## The `create` function

The `create` function will be passed two parameters, `element` and `config`.
    
    
    create: function(element, config){
      // Your update code here.
    },
    

### Parameters

  * `element` _DOMElement_

A DOM Element that represents a container to render your visualization into.

  * `config` _object_

An object that represents the values of any configuration options that the user has set for this chart.

**Example** : `{my_configuration_option: "User Value"}`




## The `updateAsync` and `update` functions

The preferred method of updating your visualization is the `updateAsync` method. This method allows your visualization to perform an asynchronous action, such as loading a file or sending a web request.

This version of the function has an additional parameter, which is a callback to be called when rendering is complete:
    
    
    updateAsync: function(data, element, config, queryResponse, details, done){
        // An example of an asynchronous update, fetching a file.
        d3.request("https://example.com/fun-file.docx").response(function(xhr) {
            // Your update code here that uses this file.
            done();
        });
    }
    

Alerting Looker when the visualization is done rendering lets Looker optimize PDF rendering and ensures that images of visualizations are properly captured.

Some older visualizations use the `update` function. This function still works but is not the preferred method, since its use means that Looker won't be alerted when a visualization is fully rendered. The `update` function will be passed five parameters:
    
    
    update: function(data, element, config, queryResponse, details){
      // Your update code here.
    }
    

### Parameters

  * `data` _array_

An array of rows that represent the current data in the query. May be `null`.

Each row is an object with the keys that represent field names, and the value that represents a "cell" object. Here's details on dealing with the cell object.

  * `element` _DOMElement_

A DOM Element that represents a container to render your visualization into.

  * `config` _object_

An object that represents the values of any configuration options that the user has set for this chart.

**Example** : `{my_configuration_option: "User Value"}`

  * `queryResponse` _object_

An object that represents metadata about the current query, such as metadata about fields. May be `null`.

  * `details` _object_

Details about the current rendering context. Contains information about why the chart is rendering and what has changed. Usually this information is only used in advanced cases.

Pertaining to [crossfilters](https://docs.looker.com/dashboards/cross-filtering) in Looker dashboards that use the new dashboard experience, allowed attributes include `crossfilterEnabled` and `crossfilters`.

The `print` attribute can be used in conjunction with the `done` function to improve PDF rendering for custom visualizations, especially those that include animation. For example:
        
        if (details.print) {
                done();
        }
        

  * `done` _function_

A callback to indicate that the visualization is fully rendered. This function is especially important to call if your visualization needs to perform asynchronous calls or needs to be rendered as a PDF.




## Rendering Data

Looker has a rich set of data formatting tools in LookML that can be used to customize the appearance and behavior of data points. These tools include field-level LookML settings like custom value formats, HTML, drill links, and data actions.

Cells have a `value` property, which is the only property that exists in all cases. This property is a JavaScript type that matches the type of field that the cell belongs to. However, it's not safe to insert a `value` property directly into HTML or SVG, as no HTML escaping has been performed, and some field values are complex JavaScript objects or arrays that will render in undesirable or confusing ways.

To ensure that all visualizations render these items consistently and safely, there are a number of utility functions for turning the cell metadata that's passed to your chart in `data` into different representations for different purposes. The cell metadata may compress or omit certain fields in some cases, and these helper functions will let you provide a consistent experience.

These helper functions are all available on the global `LookerCharts.Utils` object.

  * `LookerCharts.Utils.textForCell(cell)`

This function accepts a cell and returns a string representation of it that's suitable for display. It will always be a string – this function never returns `null` or any other type.

  * `LookerCharts.Utils.htmlForCell(cell)`

This function accepts a cell and returns a string containing HTML. It will always be a string – this function never returns `null` or any other type.

The output of this function is properly escaped and suitable for directly inserting into your element's HTML. The output HTML will also correctly display the drill menu on click when it's appropriate for the data.

  * `LookerCharts.Utils.filterableValueForCell(cell)`

This function accepts a cell and returns a Looker advanced filter syntax string that would match the value of this cell.

  * `LookerCharts.Utils.toggleCrossfilter({row, pivot, event})`

This function accepts a row, a pivot, or an event and is used to check if cross filtering is enabled for a visualization. The following example shows how to add an event listener to an element that checks if cross filtering is enabled when the event occurs:
        
        d3.select("#myElement")
        .on("click", function (d) {
            if (details.crossfilterEnabled) {
                    LookerCharts.Utils.toggleCrossfilter({
                        row: d.row,
                        event: d3.event,
                    });
            } else {
              // ... handle click when cross-filtering is not enabled
            }
        });
        

  * `LookerCharts.Utils.getCrossfilterSelection(row, pivot?)`

This function accepts a row or pivot and is used to check if that row or pivot is selected in a custom visualization. The function returns an enum for `CrossfilterSelection {NONE, SELECTED, UNSELECTED}` of 0 if `NONE`, 1 if `SELECTED`, and 2 if `UNSELECTED`.

The following example conditionally applies a fill color to a row if it's being cross filtered and applies default colors if cross filtering is not enabled for that row:
        
        d3.select("#myElement")
        .attr("fill", function (d) {
            const crossfilter = LookerCharts.Utils.getCrossfilterSelection(d.row)
            if (details.crossfilterEnabled && crossfilter === 1) {
                    return d.color
            } else {
                    return "#DEE1E5" //Hex used for unselected elements in native visualizations
        ...
        

  * `LookerCharts.Utils.openDrillMenu(options)`

The output of `htmlForCell` will automatically show the drill menu if needed, but that may not be appropriate for certain types of rendering. (For example, SVG cannot render HTML but you may want to capture a click event to begin a drill.)

The `options` object has the following parameters:

    * `links` **Required** _array_

An array of the objects returned from the `links` property of a cell. If you want to display links for multiple cells at once, you may concatenate these arrays together first. For custom links, provide an array of objects with the following form: 
          
          { label: _string_ , type: 'drill', type_label: _string_ , url: _url_ }

    * `event` _HTML DOM Event_

The click (or other) event that caused the drill event. Looker will use this to determine where to place the drill menu. If you don't have one, try passing an object with the pageX and pageY coordinates.

**Example:**
    
    for (var row of data) {
        var cell = row[queryResponse.fields.dimensions[0].name];
        var cellElement = myBuildElementFunction(cell);
        cellElement.onclick = function(event) {
            LookerCharts.Utils.openDrillMenu({
                links: cell.links,
                event: event
            });
        };
        // ... more visualization stuff...
    }
    




## Presenting configuration UI

The `options` parameter is an object where the keys are an arbitrary identifier for an option name, and the value is an object describing information about the option.

Here's an example:
    
    
    options: {
        color_range: {
          type: "array",
          label: "Color Range",
          display: "colors"
        },
       top_label: {
          type: "string",
          label: "Label (for top)",
          placeholder: "My Great Chart"
        },
        transport_mode: {
          type: "string",
          label: "Mode of Transport",
          display: "select",
          values: [
             {"Airplane": "airplane"},
             {"Car": "car"},
             {"Unicycle": "unicycle"}
          ],
          default: "unicycle"
        }
    }
    

### Option Object Parameters

The `option` object has the following basic parameters, display-specific properties, and organizing options.

#### Basic parameters

  * `type` _string_

The data type of the option.

**Allowed Values:** `string` (default), `number`, `boolean`, `array`

  * `label` _string_

The human-readable label of the option that will be displayed to the user.

  * `default`

The default value of the option. When unspecified, the value of the option is `null`. This should be a value of the same type as `type`.

  * `display` _string_

Certain `type` values can be presented in the UI in different ways.

    * when `type` is `string`:

**Allowed Values:** `text` (default), `select`, `radio`

    * when `type` is `number`:

**Allowed Values:** `number` (default), `range`

    * when `type` is `array`:

**Allowed Values:** `text` (default), `color`, `colors`

  * `placeholder` _string_

For `display` values that support it, an example value or explanation to give the user a hint about what to type.




#### Display-specific properties

  * `values` _array_ of _objects_

When `display` is `radio` or `select`, an array containing labels and values that will be listed in the interface.

Each item in the array should be an object with a single key-value pair, that represent the label and the value of the option. The label will be presented only in the UI; at render time, you'll receive only the value.

**Example:**
        
        values: [
            {"Center": "c"},
            {"Left": "l"},
            {"Right": "r"}
        ]
        

If `display` is `radio`, each option can additionally be given a `description`:
        
        values: [
            {"Cool": "c"},
            {"Uncool": {
                    value: "unc",
                    description: "Only choose this if the data is very uncool."
                }
            }
        ]
        

  * `max` _number_

When `display` is `range`, the maximum number allowed to be selected by the range slider.

  * `min` _number_

When `display` is `range`, the minimum number allowed to be selected by the range slider.

  * `step` _number_

When `display` is `range`, the amount each tick of the range slider represents.




#### Organizing options

  * `section` _string_

For charts with many options, a label for which section an option should appear in. The UI will group the options by their `section` values. If there is only one section, the section UI won't be shown.

If you're using `section` then it should be set on every option.

  * `order` _number_

A number that represents the order of options for presentation in the UI. If specified, the options will be sorted according to this order.

  * `display_size` _string_

A size class that represents the width of the option in the UI. For example, if you wanted to show a "Minimum" and a "Maximum" option next to each other, you could set each of their display sizes to `half`.

**Allowed Values:** `normal` (default), `half`, `third`




## Events

Events can be triggered by the chart (usually in response to user interaction) that can update properties of the visualization or query.

They can be triggered by calling the `trigger` function on the visualization object. The first parameter is always the _event name_ and the second parameter is an array of _arguments_.
    
    
    this.trigger("limit", [20]);
    

### Available events

  * `updateConfig`

Update the current configuration settings of the chart.

**Argument:** an object containing config keys to update. Unspecified keys are not changed.

**Example:**
        
        var vis = this;
        $(element).find(".axis").click(function(){
            vis.trigger("updateConfig", [{axis_hidden: true}]);
        });
        

  * `limit`

Update the limit of the underlying query:

**Argument:** an integer that represents a new limit for the query.
        
        var vis = this;
        $(element).find(".show-all").click(function(){
            vis.trigger("limit", [500]);
        });
        

  * `filter`

Update the value of a filter on the underlying query:
        
        var vis = this;
        $(element).find(".show-all-tommys").click(function(){
            vis.trigger("filter", [{
                field: "users.name", // the name of the field to filter
                value: "%tommy%", // the "advanced syntax" for the filter
                run: true, // whether to re-run the query with the new filter
            }]);
        });
        

  * `loadingStart`

Mark the visualization as loading. Most of the time this isn't necessary, but if your visualization loads an object from a remote location or performs a long calculation, you can use this to continue to display the loading indicator.

It will appear loading until `loadingEnd` is triggered.

  * `loadingEnd`

Mark the visualization as no longer loading.

  * `printSize` (Looker 26.0+)

Allows visualizations to take advantage of the "Expand tables to show all rows" option when rendering dashboards to PDF. Using this event allows the application to know how tall the rendered content is and can expand the dashboard tile appropriately so all the information is visible for printing.
        
        this.trigger('printSize', {
            heightExpanded: FULL_HEIGHT_IN_PIXELS
          });
        

  * `registerOptions` (Looker 5.24+)

Allows visualizations to register additional options after the visualization has been registered:
        
        update: function(data, element, config, queryResponse, details){
            options = {}
            // Create an option for each measure in your query
            queryResponse.fields.measure_like.forEach(function(field) {
              id = "color_" + field.name
              options[id] =
              {
            label: field.label_short + " Color",
            default: "#8B7DA8",
            section: "Style",
            type: "string",
            display: "color"
              }
            })
            this.trigger('registerOptions', options) // register options with parent page to update visConfig
            ...
          }
        });
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
