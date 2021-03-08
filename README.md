# github-tutorial
Example Repository for LJMU Data Science Masters Students

## Topics covered and where to find more detailed notes
* [Git and Github overview](docs/git-and-github.md)
* [Creating a repository](docs/creating-a-repo.md)
* [Changing and commiting code locally](docs/git-local.md)
* [Pushing changes to your remote repository](docs/pushing-to-github.md)
* [Pulling down changes from your remote repository](docs/pulling-from-github.md)
* [Bonus: Branches and why you probably don't want to use them](docs/branching-workflow.md)

## Using github locally with Linux, Mac and Windows
**Note**: We will be using the `git` command, run in a terminal for all of
the examples. There are many visual tools to use git, and many IDEs
(Integrated Development Environments) such as vscode, atom, sublime, rstudio
have plugins to make using git easier. These essentially just use the git
command and are too varied to detail here. Good knowledge of the command line
is exceptionally useful. i.e. How will you get your code and start it running
on a supercluster that only has an ssh interface?

To use github, you need a working version of git installed locally on
your machine. This maybe installed by default if you are using linux or
Mac and have installed xcode. To test, open up a terminal and type the
command `git`. If installed you should see the options for the command;

```shell
$> git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
```

If you don't see the above you will need to install git.

### Installing git on Ubuntu Linux
```shell
$> sudo apt install git
```

### Installing git on Mac
There is an installer you can download https://sourceforge.net/projects/git-osx-installer/

However if you have homebrew for mac then just type
```shell
$> brew install git
```

See here for more options https://git-scm.com/download/mac


### Installing git on Windows
See here for installing git on windows https://gitforwindows.org/

As windows doesn't natively have a bash shell (as Linux and Mac do) this
package will install `git bash`, which is a command line implementation
of bash for windows. We will use this for all tutorials.




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
