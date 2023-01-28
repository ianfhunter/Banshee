---
title: Elevations
category: The battlefield
---


<table>
  <tr>
    <td>2</td>
    <td>1</td>
    <td>2</td>
    <td>1</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td>4</td>
    <td>4</td>
    <td>6</td>
    <td>4</td>
  </tr>
  <tr>
    <td>3</td>
    <td>5</td>
    <td>3</td>
    <td>3</td>
  </tr>
</table>

If a character is on the top left corner, they cannot see anything in the top right as the height of the third cell obscures the fourth.


<table>
  <tr style="color:cyan">
    <td><b>2</b></td>
    <td>1</td>
    <td>2</td>
    <td>?</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td>4</td>
    <td>4</td>
    <td>6</td>
    <td>4</td>
  </tr>
  <tr>
    <td>?</td>
    <td>5</td>
    <td>?</td>
    <td>?</td>
  </tr>
</table>

Similarly, this happens on the vertical 
<table>
  <tr>
    <td style="color:cyan"><b>2</b></td>
    <td style="color:gray">1</td>
    <td style="color:gray">2</td>
    <td style="color:gray">?</td>
  </tr>
  <tr>
    <td style="color:cyan">3</td>
    <td>2</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td style="color:cyan">4</td>
    <td>4</td>
    <td>6</td>
    <td>4</td>
  </tr>
  <tr>
    <td style="color:cyan">?</td>
    <td>5</td>
    <td>?</td>
    <td>?</td>
  </tr>
</table>

And the diagonal
<table>
  <tr>
    <td style="color:cyan"><b>2</b></td>
    <td style="color:gray">1</td>
    <td style="color:gray">2</td>
    <td style="color:gray">?</td>
  </tr>
  <tr>
    <td style="color:gray">3</td>
    <td style="color:cyan">2</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td style="color:gray">4</td>
    <td>4</td>
    <td style="color:cyan">6</td>
    <td>4</td>
  </tr>
  <tr>
    <td style="color:gray">?</td>
    <td>5</td>
    <td>?</td>
    <td style="color:cyan">?</td>
  </tr>
</table>

And the remaining squares are determined by a double-width line between the start and end point. Both must be highter to conceal a location
<table>
  <tr>
    <td style="color:cyan"><b>2</b></td>
    <td style="color:gray">1</td>
    <td style="color:gray">2</td>
    <td style="color:gray">?</td>
  </tr>
  <tr>
    <td style="color:cyan">3</td>
    <td style="color:cyan">2</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td style="color:cyan">4</td>
    <td style="color:cyan">4</td>
    <td style="color:gray">6</td>
    <td>4</td>
  </tr>
  <tr>
    <td style="color:gray">?</td>
    <td style="color:cyan">5</td>
    <td>?</td>
    <td style="color:gray">?</td>
  </tr>
</table>

The remaining cell on the bottom row is 3, which is lower than both 4 and 6.
<table>
  <tr>
    <td style="color:cyan"><b>2</b></td>
    <td style="color:gray">1</td>
    <td style="color:gray">2</td>
    <td style="color:gray">?</td>
  </tr>
  <tr>
    <td style="color:cyan">3</td>
    <td style="color:cyan">2</td>
    <td>2</td>
    <td>3</td>
  </tr>
  <tr>
    <td style="color:gray">4</td>
    <td style="color:cyan">4</td>
    <td style="color:cyan">6</td>
    <td>4</td>
  </tr>
  <tr>
    <td style="color:gray">?</td>
    <td style="color:gray">5</td>
    <td style="color:cyan">?</td>
    <td style="color:gray">?</td>
  </tr>
</table>
Now the cells to the side. This value 4 is partially visible as one half of the path is all lower or equal to the starting elevation 
<table>
  <tr>
    <td style="color:cyan"><b>2</b></td>
    <td style="color:cyan">1</td>
    <td style="color:gray">2</td>
    <td style="color:gray">?</td>
  </tr>
  <tr>
    <td style="color:gray">3</td>
    <td style="color:cyan">2</td>
    <td style="color:cyan">2</td>
    <td>3</td>
  </tr>
  <tr>
    <td style="color:gray">4</td>
    <td style="color:gray">4</td>
    <td style="color:cyan">6</td>
    <td style="color:cyan">4</td>
  </tr>
  <tr>
    <td style="color:gray">?</td>
    <td style="color:gray">5</td>
    <td style="color:gray">?</td>
    <td style="color:gray">?</td>
  </tr>
</table>
and
<table>
  <tr>
    <td style="color:cyan"><b>2</b></td>
    <td style="color:cyan">1</td>
    <td style="color:cyan">2</td>
    <td style="color:gray">?</td>
  </tr>
  <tr>
    <td style="color:gray">3</td>
    <td style="color:cyan">2</td>
    <td style="color:cyan">2</td>
    <td style="color:cyan">3</td>
  </tr>
  <tr>
    <td style="color:gray">4</td>
    <td style="color:gray">4</td>
    <td style="color:gray">6</td>
    <td style="color:gray">4</td>
  </tr>
  <tr>
    <td style="color:gray">?</td>
    <td style="color:gray">5</td>
    <td style="color:gray">?</td>
    <td style="color:gray">?</td>
  </tr>
</table>

The same logic can apply should you wish to use a hex grid.

<div class="main">
  <div class="container">
    <div style="background-color:yellow"></div>
    <div></div>
    <div></div>
    <div></div>
    <div></div>
    <br />
    <div style="background-color:cyan"></div>
    <div style="background-color:cyan"></div>
    <div></div>
    <div></div>
    <br />
    <div></div>
    <div style="background-color:cyan"></div>
    <div style="background-color:cyan"></div>
    <div></div>
    <div></div>
    <br />
    <div></div>
    <div></div>
    <div style="background-color:green"></div>
    <div></div>
  </div>
</div>

With hexes, double paths can sometimes be reduced to one:

<div class="main">
  <div class="container">
    <div style="background-color:yellow"></div>
    <div style="background-color:cyan"></div>
    <div></div>
    <div></div>
    <div></div>
    <br />
    <div style="background-color:cyan"></div>
    <div style="background-color:cyan"></div>
    <div style="background-color:cyan"></div>
    <div></div>
    <br />
    <div></div>
    <div></div>
    <div style="background-color:cyan"></div>
    <div style="background-color:green"></div>
    <div></div>
    <br />
    <div></div>
    <div></div>
    <div></div>
    <div></div>
  </div>
</div>

Another example


<div class="main">
  <div class="container">
    <div style="background-color:yellow"></div>
    <div style="background-color:cyan"></div>
    <div></div>
    <div></div>
    <div></div>
    <br />
    <div style="background-color:cyan"></div>
    <div style="background-color:cyan"></div>
    <div></div>
    <div></div>
    <br />
    <div></div>
    <div></div>
    <div style="background-color:cyan"></div>
    <div style="background-color:cyan"></div>
    <div></div>
    <br />
    <div></div>
    <div></div>
    <div style="background-color:cyan"></div>
    <div style="background-color:green"></div>
  </div>
</div>

If in doubt, use a measureing tool to draw a line between the center of each point and select the cells that are intersected.

This same logic can be repeated for other shapes too, if you wanted to do that for some reason


<style>
    .main {
  --s: 30px;  /* size of a hexagon */
  --m: 1px;    /* space between each heaxgon */
  --r: calc(var(--s)*3*1.1547/2 + 4*var(--m));
  display:flex;
}
.container div {
  background-color: red;
  width: var(--s);
  height: calc(var(--s)*1.1547); 
  margin: var(--m);
  display: inline-block;
  clip-path: polygon(0% 25%, 0% 75%, 50% 100%, 100% 75%, 100% 25%, 50% 0%);
  margin-bottom: calc(var(--m) - var(--s)*0.2885); 
}
.container::before {
  content: "";
  width: calc(var(--s)/2 + var(--m));
  float: left;
  height: 100%;
  shape-outside: repeating-linear-gradient(     
                  transparent 0 calc(var(--r) - 3px),      
                  #fff        0 var(--r));
}
</style>

