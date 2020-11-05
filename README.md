# 2020 Election Projection
Are the 2020 counts going too slow for you? Run this model and get a guess to either make you less (or more) stressed, depending upon your political slant.

To run, clone the repo and run the `model.py` in a Python3 environment. You will need to have `requests` installed to make it work.

# Model Description

The model pulls the latest by-county information from CNN's API. It then scales the votes in each county to keep the same per-county ratio, but scaled to the expected total number of votes. The model will output the projected winner of the state at 100% reporting, alongside the projected win margin.

## Current Projections

At time of publish, the five remiaing uncalled states are simulated as follows:

```
PA
Trump 98057

NC
Trump 69717

GA
Biden 3366

NV
Biden 12211

AZ
Biden 77602
```
