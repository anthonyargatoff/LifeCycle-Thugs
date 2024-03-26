# Module Info
Class is used to calculate the distance between 2 coordinates.

## Parameters
Accepts data points in format `(latitude1, longitude1, latitude2, longitude2)`. Must be input in degrees.

## Methods
- `getDistanceKilometers` will return a float in kilometers. It is a static method.
- `getDistanceMiles` will return a float in miles. It is a static method.
- `__getDistance` is a private method (not to be called). It is used to reduce duplicate code (each other method calls it).

## Exceptions
A `ValueError` exception will be raised when an incompatible value is entered (say a value of 500 for latitude).