# github-tutorial
Example Repository for LJMU Data Science Masters Students


## Notes on markdown
Markdown is useful to assist with documenting your project. Any github repository 
should ideally have a README.md file (such as this one) in the root of the project.

This should be done at least to a minimal level. See the following resources;

* https://www.markdowntutorial.com/
* https://www.makeareadme.com/

Markdown is also exceptionally useful for referencing code either `incline` where
you may reference package or function names, but you can also create code blocks as
below and also specify syntax highlighting for the language you are using.

For python;

```python
import time

while True:
  time.sleep(60)
  print("Another minute has passed!)
 ```
 
 
For r;
```r
a <- 42
A <- a * 2  # R is case sensitive
print(a)
cat(A, "\n") # "84" is concatenated with "\n"
if(A>a) # true, 84 > 42
{
  cat(A, ">", a, "\n")
} 
```
