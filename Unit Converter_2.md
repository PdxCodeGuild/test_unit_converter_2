## Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

```
1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
```

Below is an example of how you should structure your function: 

```python
def unit_converter():
    - input: "what is the distance?" 100
    - input: "what are the units?" mi
    - return : "<initial value> <units> is <converted amount> <units>"
```

Example:

100 mi is 160934 m