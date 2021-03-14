# Git and Github
<<<<<<< HEAD

![Alt text](../images/flow.jpg)

=======
![Alt text](../images/flow.jpg)
>>>>>>> test

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
Don't try and use these, they'll just confuse!
* `stash` - save the out of sync changes away
* `pop` - merge back in out of sync changes of synchronised    

## Git
* Is a version control system (VCS), common in software development
* Can be used (usefully) on any text based files.
* Not intended for large file storage. **i.e. Not recommended for datasets!**

### Local Usage
* In any folder you can create a git `repository`, this will then create a
`.git/` folder which stores all the file changes.
    ```shell
    $>  git init
    Initialised empty Git repository in /home/disrail/github-tutorial/.git/
    ```

* Next we want to check which files in the folder have changes and have
not been committed
    ``` shell
    $>  git status
    On branch main
    Your branch is ahead of 'origin/main' by 1 commit.
      (use "git push" to publish your local commits)

    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)

            modified:   docs/git-and-github.md

    no changes added to commit (use "git add" and/or "git commit -a")
    ```

* The files for which we want to commit changes need to be added
(also known as staging)
    ```shell
    $>  git add docs/git-and-github.md
    ```
  It can be a pain adding files one by one, so you can bulk add with the command
    ```shell
    $>  git add -A
    ```
