---
url: https://docs.cloud.google.com/looker/docs/about-custom-viz-builder-legacy-page/
title: How to use the Custom Visualization Builder \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:40:59.990494+00:00
---

# How to use the Custom Visualization Builder  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/about-custom-viz-builder-legacy-page/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  How to use the Custom Visualization Builder Stay organized with collections  Save and categorize content based on your preferences. 

The [Custom Visualization Builder](https://looker-open-source.github.io/custom-viz-builder/) (CVB) is a playground that gives developers an environment to build and test their custom visualization before adding it into [Looker](https://www.looker.com/). Here's an example of how you can use this tool.

![](https://docs.cloud.google.com/static/looker/docs/images/custom-viz-builder-2314.png)

The CVB has two sides:

  1. The left side where you will write the Javascript code of your visualization
  2. The right side which is also divided into two sections: 
     1. The top section has the following tabs: 
        1. **Query Response** : were you can add the JSON format of your query response.
        2. **Raw Data**. You must enter here an array of the data returned by Looker.
        3. **Dependencies** which is also a mandatory tab thus you need to enter a string array with the CDN links of all the dependencies that your visualization needs.
     2. The bottom section where the resulting visualization is displayed.



Let's say that you want to build the following visualization using the Chart.js library:

![A column chart displays the top 5 product categories by count in ascending order: Jumpsuits & Rompers, Suits, Skirts, Plus, and Blazers & Jackets.](https://docs.cloud.google.com/static/looker/docs/images/vis-object-2314.png)

The [visualization object](https://github.com/looker/custom_visualizations_v2/blob/master/docs/api_reference.md) has two properties that are required: `create` and `updateAsync` function. This tutorial will focus on the later which is a function that is called every time the state of your visualization may need to change. It will always be called after `create`, and may be called many times.

## Step 1: Extract and prepare the data

The data will be passed to the `updateAsync` function by using its first parameter, conventionally named `data`. The following code loops through each element of this `data` object and pushes the data values into an `actual_data` array and the labels into a `data_labels` array. These two arrays will be used later to draw the visualization.
    
    
    const data_labels = []
    const actual_data = []
    
    data.forEach((d)=>{
         data_labels.push(d["Products Category"])
         actual_data.push(d["Products Count"])
    })
    

## Step 2: Append the visualization to the page

Chart.js needs a `canvas` to render the visualization onto the page. You need to create a `canvas` element with an `id` of your choice (`myChart` is used for this tutorial), then append this `canvas` to the `div` element that the CVB uses to render the visualization. This `div` has an id attribute named `vis`.
    
    
    const vizCanvas = document.createElement('canvas')
    vizCanvas.setAttribute("id", "myChart")
    
    const vizDiv = document.getElementById("vis")
    vizDiv.appendChild(vizCanvas)
    

## Step 3: Draw the visualization on the page

Now that you have a `canvas` element on the page with an id of `myChart`, you can target this element and draw the visualization like this:
    
    
    const ctx = document.getElementById("myChart")
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: data_labels,
        datasets: [{
          label: 'Top 5 Product Category',
          data: actual_data,
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(153, 102, 255, 0.2)'
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)',
            'rgba(153, 102, 255, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        },
      }
    });
    
    doneRendering()
    

It's important to call the `doneRendering` function in the end to indicate that the visualization is fully rendered. This is especially important to call if your visualization needs to perform asynchronous calls or needs to be rendered as a PDF.

The final code looks like this:
    
    
    const visObject = {
        create: function(element, config){
            element.innerHTML = "";
        },
    
        updateAsync: function (data, element, config, queryResponse, details, doneRendering) {
            const data_labels = []
            const actual_data = []
    
            data.forEach((d)=>{
                data_labels.push(d["Products Category"])
                actual_data.push(d["Products Count"])
            })
    
            const vizCanvas = document.createElement('canvas')
            vizCanvas.setAttribute("id", "myChart")
    
            const vizDiv = document.getElementById("vis")
            vizDiv.appendChild(vizCanvas)
    
            const ctx = document.getElementById("myChart")
            const myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data_labels,
                    datasets: [{
                        label: 'Top 5 Product Category',
                        data: actual_data,
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 206, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(153, 102, 255, 0.2)'
                        ],
                        borderColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    },
    
                }
            });
    
            doneRendering()
        }
    };
    
    looker.plugins.visualizations.add(visObject);
    

### Data from Looker

Here's the data returned by Looker that you can provide in the **RAW DATA** tab of the CVB:
    
    
    [{"Products Category":"Jumpsuits & Rompers","Products Count":"162"},
    {"Products Category":"Suits","Products Count":"184"},
    {"Products Category":"Skirts","Products Count":"364"},
    {"Products Category":"Plus","Products Count":"439"},
    {"Products Category":"Blazers & Jackets","Products Count":"551"}]
    

### Dependencies

Here's the dependency needed to render this visualization:
    
    
    ["https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"]
    

## Query Response

You can extract the query response in Looker by making an API call to the [Get Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/query) endpoint.

### Final Step

Once your code is working and the visualization is rendered as expected, you can follow the steps outlined in the documentation to [submit your visualization to Looker](https://docs.cloud.google.com/looker/docs/marketplace-develop-visualization).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
