# Predictions

It is not possible (at this point) to predict earthquakes.

1. https://www.usgs.gov/faqs/can-you-predict-earthquakes
1. https://www.preventionweb.net/news/nobody-can-predict-earthquakes-we-can-forecast-them-heres-how

## Ideas

1. Display to user most common areas for earthquakes to occur by calculating all earthquakes in area.
    - For example: create circles on the map that indicated the most hazardous areas.
2. Display to user the worst/largest earthquake to occur. 
    - Mark the area as hazardous.


## Pseudo-code

```
get point i of n from database.
variable iPoints to hold number of points found
compare it with all other database items, i2, i3, i4, ..., in
if $in$ is in the radius, add +1 to iPoints

repeat for each point in db
return the top 10 points that do not overlap with each other
```