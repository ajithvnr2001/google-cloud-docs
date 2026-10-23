---
url: https://docs.cloud.google.com/looker/docs/custom-vis-custom-color-palette/
title: Custom visualization custom color palette example \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:20.480918+00:00
---

# Custom visualization custom color palette example  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/custom-vis-custom-color-palette/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Custom visualization custom color palette example Stay organized with collections  Save and categorize content based on your preferences. 

This example shows you how to set a custom color palette for a visualization.

In the `options` object, create two color ranges (allowing for custom input):
    
    
        colorPreSet:
        {
          type: 'string',
          display: 'select',
          label: 'Color Range',
          section: 'Data',
          values: [{'Custom': 'c'},
          {'Tomato to Steel Blue': '#F16358,#DF645F,#CD6566,#BB666D,#A96774,#97687B,#856982,#736A89,#616B90,#4F6C97,#3D6D9E'},
          {'Pink to Black': '#170108, #300211, #49031A, #620423, #79052B, #910734, #AA083D, #C30946, #DA0A4E, #F30B57, #F52368, #F63378, #F63C79, #F75389, #F86C9A, #F985AB, #FB9DBC, #FCB4CC, #FDCDDD, #FEE6EE'},
          {'Green to Red': '#7FCDAE, #7ED09C, #7DD389, #85D67C, #9AD97B, #B1DB7A, #CADF79, #E2DF78, #E5C877, #E7AF75, #EB9474, #EE7772'},
          {'White to Green': '#ffffe5,#f7fcb9 ,#d9f0a3,#addd8e,#78c679,#41ab5d,#238443,#006837,#004529'}],
            default: 'c',
          order: 1
        },
        colorRange: {
          type: 'array',
          label: 'Custom Color Ranges',
          section: 'Data',
          order: 2,
          placeholder: '#fff, red, etc...'
        },
    

In the `update` function, add:
    
    
        if (settings.colorPreSet  == 'c') {
          var colorSettings =  settings.colorRange || ['white','green','red']; // put a default in
        } else {
          var colorSettings =  settings.colorPreSet.split(",");
        };
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
