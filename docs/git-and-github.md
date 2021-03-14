# Git and Github

## Terminology
* `repository` - the git repository locally and on the remote (i.e. github)
* `clone` - copy a remote repository from github
* `add` - `stage` files ready to make a commit
* `commit` - add the staged changes to the git repository
* `push` - push all changes to the remote repository (i.e. github)
* `pull` - get any changes from the remote repository

### Advanced stuff
* `branch` - create a new branch for development etc
* `merge` - bring two branches back together

And in the following, means you've got out of sync between the local and remote;
Don't try and use these, they'll just confuse!!!
* `stash` - save the out of sync changes away
* `pop` - merge back in out of sync changes of synchronised    




## Git
* Is a version control system (VCS), common in software development
* Can be used (usefully) on any text based files.
* Not intended for large file storage! Not recommended for datasets!

### Local Usage
* In any folder you can create a git `repository`, this will then create a
`.git/` folder which stores all the file changes.
```shell
disrail@soyuz:~/github-tutorial$ git init
Initialised empty Git repository in /home/disrail/github-tutorial/.git/
```

* Next we want to check 
