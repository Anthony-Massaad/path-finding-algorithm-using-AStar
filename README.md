# Path Finding Algorithm GUI

## Short Desciption

This is a path finding algorithm using A-star algorithm to get from points Red to Blue, which uses pygame as the main GUI builder. 

<p align="center">
  <h3>Sample Image Without Diagonal</h3>
  <img src="https://user-images.githubusercontent.com/62800170/154750048-17e03662-36f1-4ee5-8d0d-01e7c0b8b6ab.png" width="40%"/>
  <h3>Sample Image With Diagonal</h3>
  <img src="https://user-images.githubusercontent.com/62800170/154750190-deee4413-c914-4063-92b4-6b489fc4328b.png" width="40%"/>
</p>

## Requirements

```pip install pygame```

## Instuctions 

The first Left click will place a red marker on the screen. The second left click will place a blue marker on the screen. Lastly, the rest of the left clicks will place black markers on the screen. To erase any marker, simply right click on the marker to delete it. 

If either the red or blue marker is not placed or deleted, the algorithm will not start unless they are located onto the map. These markers will take priority over the black markers.

## Each Marker Indication

Red maker = start point

Blue = end point

Black = obstacle/path

## Side Buttons Located On The Right Description

- "Reset" will reset the entire map
- "Path Reset" will reset the obstacles (black markers)
- "Points Reset" will reset the start and end points (red and blue markers)
- "Re-Search" will allow you to reset the search with everything in place
- "+ Diagonal" will enable the diagonal search feature for a quicker search (Active = green, otherwise grey)

## Author

Anthony Massaad

Copyright @ 2021. All rights reserved

