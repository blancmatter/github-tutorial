# Git Local Usage


## Creating a repository
* In any folder you can create a git `repository`, this will then create a
`.git/` folder which stores all the file changes.
    ```shell
    $>  git init
    Initialised empty Git repository in /home/disrail/github-tutorial/.git/
    ```
However, in this example we already created and did a `clone` of the
repository in github!

## The .gitignore file
* This file is a list of the files we want to ignore in our git repository

## Making and commiting changes

There is a 2 step process in making a `commit`.
This is to detail which changes will be commite

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

* Then we can check again which files have been added to staging
    ```shell
    $> git status
    On branch main
    Your branch is up-to-date with 'origin/main'.

    Changes to be committed:
      (use "git reset HEAD <file>..." to unstage)

          modified:   docs/git-and-github.md

    ```

* Finally we're ready to commit, specifying the commit message inline.
    ```shell
    $> git commit -m "This is my first commit"
    ```

## Viewing Commit information

* We can see our commits using `git log`. Is best to use the `--oneline` option.
    ```shell
    $> git log --oneline
    4bbf5b5 (HEAD -> main, origin/main, origin/HEAD) Merge branch 'test' into main
    2abb7be (test) Checking rewind
    e51d923 Added image
    89bba62 Changed image format
    4734d07 Fixing image
    ```

* Each commit has a code e.g. `e51d923` if we need to go back we will use this.

## Next Page
Pushing and pulling to/from github - [pushpull-github.md](pushpull-github.md)
