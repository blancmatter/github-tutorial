# Creating a repo on github

## Create a new Repository
* Think about whether you want it to be private or public
* Add a Description
* Add a .gitignore file (potentially useful), although we can create on later

## Our Fresh New repository!
* There is an array of tabs and buttons. These are linked to advanced
development features we won't be using.
* In order the most important things are;
  * The file browser
  * The README.md
  * The commit info button
  * The branch dropdown

## Editing and changing files on Github
* Any file can be edited using the edit icon
* To save you will create a new commit
* This is great for quick editing, especially of Markdown files.
* **Be warned**, this is the most common method for getting out of sync


## Cloning the repo locally
* The repo is set up, we have some files, lets get them locally using git clone.
To do this just copy the address from the webrowser navigation bar, then in
your git terminal, use `git clone <address>`, e.g.

```shell
$> git clone https://github.com/blancmatter/myAwesomeRepo
Cloning into 'myAwesomeRepo'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.

remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), done.
```

* The files will apear on your file system, so run the git command
from where you want the repository to be however you can always move it after.

* go into the repository directory and now we're good to go!

## Next Page
Using git locally - [git-local.md](git-local.md)
