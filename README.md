# github-tutorial
Example Repository for LJMU Data Science Masters Students

## Topics covered and where to find more detailed notes
* Git and Github overview
* Creating a repository
* Creating and changing code locally
* Pushing changes to your remote repository
* Pulling down changes from your remote repository
* Bonus: Branches and why you probably don't want to use them


## Notes on markdown
Markdown is useful to assist with documenting your project. Any github repository 
should ideally have a README.md file (such as this one) in the root of the project.

This should be done at least to a minimal level. See the following resources;

* https://www.markdowntutorial.com/
* https://www.makeareadme.com/

Markdown is also exceptionally useful for referencing code either `inline` where
you may reference package or function names, but you can also create code blocks as
below and also specify syntax highlighting for the language you are using.

For python;

```python
import time

while True:
  time.sleep(60)
  print('Another minute has passed!')
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

**NOTE** It is exceptionally important that you document a project to the correct level. 
Will other poeple just be using the code, or will they be modifying and maintaining it also?
For this project it is unlikely that anyone else will be using your code and you just need 
minimal documentation. If however you feel that yoour supervidory team may with to take the 
code for future projects, the it may be worth spending a **_little_** more time documenting!

