# COMP472_assignment2_Q2
Feed-forward neural network


Using Python and any of the libraries it provides, please implement a feed-forward neural network for the following training set:
| A | B | C | D | E |                   output                      |
| 1 | 1 | 1 | 0 | 0 |                          1                          |
| 1 | 1 | 1 | 0 | 1 |                          1                          |
| 0 | 0 | 0 | 1 | 0 |                          0                          |
| 0 | 0 | 0 | 1 | 1 |                          0                          |
| 0 | 0 | 1 | 0 | 0 |                          1                          |
| 0 | 0 | 1 | 0 | 1 |                          1                          |
| 0 | 0 | 1 | 1 | 0 |                          1                          |
| 0 | 0 | 1 | 1 | 1 |                          1                          |
| 0 | 1 | 0 | 0 | 0 |                          0                          |
| 0 | 1 | 0 | 0 | 1 |                          0                          |
| 0 | 1 | 0 | 1 | 0 |                          0                          |
| 0 | 1 | 0 | 1 | 1 |                          0                          |
| 0 | 1 | 1 | 0 | 0 |                          1                          |
| 0 | 1 | 1 | 0 | 1 |                          1                          |
| 0 | 1 | 1 | 1 | 0 |                          1                          |
| 0 | 1 | 1 | 1 | 1 |                          1                          |
| 1 | 0 | 0 | 0 | 0 |                          1                          |
| 1 | 0 | 0 | 0 | 1 |                          1                          |
| 1 | 0 | 0 | 1 | 0 |                          1                          |
| 1 | 0 | 0 | 1 | 1 |                          1                          |
| 1 | 0 | 1 | 0 | 0 |                          1                          |
| 1 | 0 | 1 | 0 | 1 |                          1                          |
| 1 | 0 | 1 | 1 | 0 |                          1                          |
| 1 | 0 | 1 | 1 | 1 |                          1                          |

Use the following testing set to check how good the neural net is in classification:
| A | B | C | D | E |                   output                      |
| 1 | 1 | 0 | 0 | 0 |                          1                          |
| 1 | 1 | 0 | 0 | 1 |                          1                          |
| 0 | 0 | 0 | 0 | 0 |                          0                          |
| 0 | 0 | 0 | 0 | 1 |                          0                          |
| 1 | 1 | 0 | 1 | 0 |                          1                          |
| 1 | 1 | 0 | 1 | 1 |                          1                          |
| 1 | 1 | 1 | 1 | 0 |                          1                          |
| 1 | 1 | 1 | 1 | 1 |                          1                         |
